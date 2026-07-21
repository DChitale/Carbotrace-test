provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.xlarge"

  tags = {
    Name        = "Carbotrace-Test-AppServer"
    Environment = "production"
  }
}

resource "aws_instance" "gpu_compute_cluster" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "c5.9xlarge"

  tags = {
    Name        = "Carbotrace-HighWattage-Compute"
    Environment = "production"
  }
}

resource "aws_db_instance" "default" {
  allocated_storage    = 100
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.r5.large"
  db_name              = "carbotrace_prod"
  username             = "postgres"
  password             = "supersecretpass123"
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
}
