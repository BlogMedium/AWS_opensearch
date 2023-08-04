# Provision Opensearch using terraform and ingest logs from Ec2
```
git clone
terraform init
terraform plan
terraform apply

Once Opensearch cluster is up and running 

* Modify the ES_ENDPOINT
* To Start logstash
bin/logstash -f /path/to/your/logstash-config.conf

````

