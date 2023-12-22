# Provision Opensearch using terraform and ingest logs from Ec2
```
git clone
terraform init
terraform plan
terraform apply

Once Opensearch cluster is up and running 

* Execute the script file logstash_install.sh file on the ec2 instance.
* Make sure to modify the end_point ()
  - access key
  - secret key

/usr/share/logstash/logstash-8.11.3/bin/logstash -f /etc/logstash/conf.d/logstash.conf

````

