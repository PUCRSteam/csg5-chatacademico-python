
resource "aws_codedeploy_app" "csg5_chatacademico_application" {
  compute_platform = "Server"
  name             = "csg5-chatacademico-application"
}

resource "aws_codedeploy_deployment_group" "csg5_chatacademico_deployment_group" {
  app_name              = aws_codedeploy_app.csg5_chatacademico_application.name
  deployment_group_name = "csg5-chatacademico-deployment-group"
  service_role_arn      = "arn:aws:iam::813303321040:role/LabRole"

  autoscaling_groups = [
		aws_autoscaling_group.csg5_chatacademico_asg.name
	]

  auto_rollback_configuration {
    enabled = true
    events  = ["DEPLOYMENT_FAILURE"]
  }

}
