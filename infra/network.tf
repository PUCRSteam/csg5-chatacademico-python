
resource "aws_vpc" "csg5_chatacademico_vpc" {
  cidr_block = "10.0.0.0/24"

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_internet_gateway" "csg5_chatacademico_igw" {
  vpc_id = aws_vpc.csg5_chatacademico_vpc.id

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_subnet" "csg5_chatacademico_public_sbn" {
  vpc_id    							  = aws_vpc.csg5_chatacademico_vpc.id
	map_public_ip_on_launch 	= true
  cidr_block 								= "10.0.0.0/25"
  availability_zone         = "us-east-1a" 

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}

resource "aws_subnet" "csg5_chatacademico_public_sbn2" {
  vpc_id    							  = aws_vpc.csg5_chatacademico_vpc.id
	map_public_ip_on_launch 	= true
  cidr_block 								= "10.0.0.128/25"
  availability_zone         = "us-east-1b" 

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
