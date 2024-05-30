#!/bin/bash

wget https://artifacts.elastic.co/downloads/logstash/logstash-8.12.0-linux-x86_64.tar.gz /tmp
sudo amazon-linux-extras -y install java-openjdk11


mkdir -p /usr/share/logstash
tar -xzvf /tmp/logstash-8.12.0-linux-x86_64.tar.gz -C /usr/share/logstash/
/usr/share/logstash/logstash-8.12.0/bin/logstash-plugin install logstash-output-amazon_es
mkdir -p /etc/logstash/conf.d
cat <<EOF > /etc/logstash/conf.d/logstash.conf
input {
    file {
        path => "/var/log/*.log"
        start_position => "beginning"
    }
}
output {
    amazon_es {
        hosts => ["$ES_ENDPOINT:443"]
        region => "us-east-2"
        aws_access_key_id => "************************"
        aws_secret_access_key => "*********************"
        index => "production-logs-%{+YYYY.MM.dd}"
    }
}
EOF

