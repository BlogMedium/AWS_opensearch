# Provision Opensearch using terraform and ingest logs from Ec2
```
git clone
terraform init
terraform plan
terraform apply

Once Opensearch cluster is up and running 

* Modify the Elk_ENDPOINT
* To Start logstash
* add access_key and secret key

/usr/share/logstash/logstash-8.9.0/bin/logstash -f /path/to/your/logstash-config.conf

````

