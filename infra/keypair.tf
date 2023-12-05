
resource "aws_key_pair" "csg5_chatacademico_key_pair" {
  key_name   = "csg5-chatacademico-key-pair"
  public_key = tls_private_key.csg5_chatacademico_rsa.public_key_openssh
}

resource "tls_private_key" "csg5_chatacademico_rsa" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "csg5_chatacademico_key_pair_file" {
  content  = tls_private_key.csg5_chatacademico_rsa.private_key_pem
  filename = "csg5-chatacademico-key-pair"
}
