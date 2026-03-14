provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "devops_server" {
  ami           = "ami-0030e4319cbf4dbf2"
  instance_type = "t3.micro"

  tags = {
    Name = "devops-project-server"
  }
}
