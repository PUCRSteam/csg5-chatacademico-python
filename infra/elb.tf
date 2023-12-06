
resource "aws_launch_configuration" "csg5_chatacademico_lc" {
  name          = "csg5-chatacademico-lc"
  image_id      = "ami-0c2c9e6756c906505"
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

resource "aws_lb_target_group" "csg5_chatacademico_tglb" {
  name     = "csg5-chatacademico-tglb"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.csg5_chatacademico_vpc.id
}

resource "aws_lb" "csg5_chatacademico_lb" {
  name = "csg5-chatacademico-lb"
	load_balancer_type = "application"

  security_groups = [
    aws_security_group.csg5_chatacademico_ssh_sg.id,
    aws_security_group.csg5_chatacademico_http_sg.id
  ]

  subnets = [
    aws_subnet.csg5_chatacademico_public_sbn.id,
    aws_subnet.csg5_chatacademico_public_sbn2.id
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

  target_group_arns = [
    aws_lb_target_group.csg5_chatacademico_tglb.arn
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
			aws_subnet.csg5_chatacademico_public_sbn.id,
      aws_subnet.csg5_chatacademico_public_sbn2.id
	]

	lifecycle {
		create_before_destroy = true
	}

}
