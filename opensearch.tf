provider "aws" {
  region = "us-east-2"
}



resource "aws_elasticsearch_domain" "demo" {
  domain_name    = var.domain_name
  elasticsearch_version = "7.10"

  cluster_config {
    instance_type = "t2.small.elasticsearch"
    instance_count = "1"
  }

  ebs_options {
    ebs_enabled = true
    volume_size = "10"
    volume_type = "gp2"
  }

  tags = {
    Domain = "demo",
    owner =  "ranjiniganeshan@gmail.com"
  }
}


resource "aws_elasticsearch_domain_policy" "es_policy" {
  domain_name = aws_elasticsearch_domain.demo.domain_name

  access_policies = <<POLICIES
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "es:*",
            "Principal": "*",
            "Effect": "Allow",
            "Condition": {
                "IpAddress": {"aws:SourceIp": "************/32"}
            },
            "Resource": "${aws_elasticsearch_domain.demo.arn}/*"
        }
    ]
}
POLICIES
}







