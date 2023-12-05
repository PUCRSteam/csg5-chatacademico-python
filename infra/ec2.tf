
# resource "aws_instance" "csg5_chatacademico_instance" {
#   instance_type               = "t2.micro"
#   associate_public_ip_address = true
#   key_name                    = aws_key_pair.csg5_chatacademico_key_pair.key_name
#   iam_instance_profile        = aws_iam_instance_profile.aws_ec2_role.name

#   vpc_security_group_ids = [
#     aws_security_group.csg5_chatacademico_ssh_sg.id,
#     aws_security_group.csg5_chatacademico_http_sg.id
#   ]


#   network_interface {
#     network_interface_id = aws_network_interface.csg5_chatacademico_eni.id
#     device_index         = 0
#   }

#   tags = {
#     Name = "csg5-chatacademico-prod"
#   }
# }
