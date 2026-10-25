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

# New: GPU training cluster — very high energy footprint
resource "aws_instance" "ml_training_cluster" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "p3.8xlarge"
  count         = 4

  tags = {
    Name        = "Carbotrace-ML-GPU-Training"
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

# New: ElastiCache cluster with large nodes
resource "aws_elasticache_cluster" "cache" {
  cluster_id           = "carbotrace-cache"
  engine               = "redis"
  node_type            = "cache.r6g.2xlarge"
  num_cache_nodes      = 3
  parameter_group_name = "default.redis7"
}
