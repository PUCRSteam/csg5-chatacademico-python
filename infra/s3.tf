
resource "aws_s3_bucket" "aws_codedeploy_deployments" {
  bucket = "csg5-chatacademico-codedeploy-deployments"

  tags = {
    Name = "csg5-chatacademico-prod"
  }
}
