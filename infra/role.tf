
# resource "aws_iam_instance_profile" "csg5_chatacademico_instance_profile" {
#   name = "csg5-chatacademico-instance-profile"
#   role = aws_iam_role.csg5_chatacademico_instance_role.name

#   tags = {
#     Name = "csg5-chatacademico-prod"
#   }
# }

# data "aws_iam_policy_document" "csg5_chatacademico_assume_role_policy" {
#   statement {
#     effect = "Allow"

#     principals {
#       type        = "Service"
#       identifiers = ["ec2.amazonaws.com"]
#     }

#     actions = ["sts:AssumeRole"]
#   }
# }

# resource "aws_iam_role" "csg5_chatacademico_instance_role" {
#   name               = "csg5-chatacademico-instance-role"
#   path               = "/"
#   assume_role_policy = data.aws_iam_policy_document.csg5_chatacademico_assume_role_policy.json
  
#   inline_policy {
#     name   = "ec2-allow-stream-logs"

#     policy = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Action   = [
#           "logs:CreateLogStream",
#           "logs:PutLogEvents",
#           "logs:DescribeLogGroups",
#           "logs:DescribeLogStreams"
#         ]
#         Effect   = "Allow"
#         Resource = "*"
#       },
#     ]
#    })
#   }

#   tags = {
#     Name = "csg5-chatacademico-prod"
#   }
# }
