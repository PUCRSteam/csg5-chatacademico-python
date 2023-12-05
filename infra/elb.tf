data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20231030"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_launch_configuration" "csg5_chatacademico_lc" {
  name          = "csg5-chatacademico-lc"
  image_id      = data.aws_ami.ubuntu.id
	associate_public_ip_address = true
  instance_type = "t2.micro"

	security_groups = [
    aws_security_group.csg5_chatacademico_ssh_sg.id,
    aws_security_group.csg5_chatacademico_http_sg.id
  ]
  
	lifecycle {
    create_before_destroy = true
  }
}

resource "aws_lb" "csg5_chatacademico_lb" {
  name = "csg5-chatacademico-lb"
	load_balancer_type = "application"

  security_groups = [
    aws_security_group.csg5_chatacademico_ssh_sg.id,
    aws_security_group.csg5_chatacademico_http_sg.id
  ]

  subnets = [
    aws_subnet.csg5_chatacademico_public_sbn.id
  ]

	tags = {
    Name = "csg5-chatacademico-prod"
  }

}

resource "aws_autoscaling_group" "csg5_chatacademico_asg" {
  name = "csg5-chatacademico-asg"
  min_size             = 1
  desired_capacity     = 1
  max_size             = 2
  
  health_check_type    = "ELB"

  load_balancers = [
    "${aws_lb.csg5_chatacademico_lb.id}"
  ]

	launch_configuration = "${aws_launch_configuration.csg5_chatacademico_lc.name}"

	enabled_metrics = [
			"GroupMinSize",
			"GroupMaxSize",
			"GroupDesiredCapacity",
			"GroupInServiceInstances",
			"GroupTotalInstances"
	]

	metrics_granularity = "1Minute"

	vpc_zone_identifier  = [
			aws_subnet.csg5_chatacademico_public_sbn.id
	]

	lifecycle {
		create_before_destroy = true
	}

}
