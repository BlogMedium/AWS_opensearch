#!/bin/bash

wget https://artifacts.elastic.co/downloads/logstash/logstash-7.17.6-linux-x86_64.tar.gz /tmp
sudo amazon-linux-extras install java-openjdk11
mkdir -p /usr/share/logstash
tar -xzvf /tmp/logstash-7.17.6-linux-x86_64.tar.gz -C /usr/share/logstash/
/usr/share/logstash/logstash-7.17.6/bin/logstash-plugin install logstash-output-opensearch 
mkdir -p /etc/logstash/conf.d
cat <<EOF > /etc/logstash/conf.d/logstash.conf
input {
    file {
        path => "/var/log/*.log"
        start_position => "beginning"
    }
}
output {
  opensearch {
    ecs_compatibility => disabled
    hosts => "ElasticsearchEndpoint:443"
    index => my-index
    auth_type => {
      type => 'aws_iam'
      region => 'us-east-2'
      service_name => 'aoss'
    }
    default_server_major_version => 2
    legacy_template => false
  }
}
EOF
