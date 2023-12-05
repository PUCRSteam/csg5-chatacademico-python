
resource "aws_vpc" "csg5_chatacademico_vpc" {
  cidr_block = "172.16.0.0/16"

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_subnet" "csg5_chatacademico_public_sbn" {
  vpc_id    							  = aws_vpc.csg5_chatacademico_vpc.id
	map_public_ip_on_launch 	= true
  cidr_block 								= "172.16.10.0/24"

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_network_interface" "csg5_chatacademico_eni" {
  subnet_id   = aws_subnet.csg5_chatacademico_public_sbn.id
  private_ips = ["172.16.10.100"]

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_security_group" "csg5_chatacademico_http_sg" {
  name        = "csg5-chatacademico-http-sg"
  description = "Created by Terraform"
  vpc_id      = aws_vpc.csg5_chatacademico_vpc.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    description = "Managed by Terraform."
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    description = "Managed by Terraform."
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_security_group" "csg5_chatacademico_ssh_sg" {
  name        = "csg5-chatacademico-ssh-sg"
  description = "Created by Terraform"
  vpc_id      = aws_vpc.csg5_chatacademico_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    description = "Managed by Terraform."
    cidr_blocks = ["0.0.0.0/0"]
  }


  tags = {
    Name = "csg5-chatacademico-prod"
  }
}
