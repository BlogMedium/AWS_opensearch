import argparse
import random
import time
from datetime import datetime

LUT_IP_TO_COUNTRY_CODE = {
    "192.0.2.3": 1000,
    "10.0.0.0": 2000,
    "1.2.3.4": 5000,
}

def get_country_from_ip(ip_address):
    try: 
        return LUT_IP_TO_COUNTRY_CODE[ip_address]
    except KeyError:
        return random.randint(10000, 50000)

def http_status_class_one_hot_encoding(http_status):
    if 100 <= http_status <= 199:
        return (1, 0, 0, 0, 0 )
    elif 200 <= http_status <= 299:
        return (0, 1, 0, 0, 0 )
    elif 300 <= http_status <= 399:
        return (0, 0, 1, 0, 0 )
    elif 400 <= http_status <= 499:
        return (0, 0, 0, 1, 0 )
    elif 500 <= http_status <= 599:
        return (0, 0, 0, 0, 1 )

def main():
    try:
        arg_parse = argparse.ArgumentParser()
        sub_arg_parse = arg_parse.add_subparsers(help='Available commands',
                                                  dest='command')
        setup_parser = sub_arg_parse.add_parser('normal', help='generate normal logs')
        clear_parser = sub_arg_parse.add_parser('anomaly', help='generate anomalies')
        args = arg_parse.parse_args()
        if args.command == 'normal':
            MODE = "NORMAL"
        elif args.command == 'anomaly':
            MODE = "ANOMALY"
        else:
            print("Mode not specified")
            MODE = "NORMAL"
        
        while True:
            timestamp = datetime.now()
            remote_ip = random.choice(list(LUT_IP_TO_COUNTRY_CODE.keys()))
            if MODE == "ANOMALY":
                country_code = random.randint(1000, 5000)
                status = random.choice([200, 400, 401, 403, 405,429, 500, 502, 502, 503, 511])
            else:
                country_code = get_country_from_ip(remote_ip)
                status = random.choices([200, 404], weights=(1000,5))[0]

            http_1xx, http_2xx, http_3xx, http_4xx, http_5xx = http_status_class_one_hot_encoding(status)

            log_entry = {
                'es_timestamp': timestamp,
                's3_timestamp': timestamp,
                'day_of_week': timestamp.weekday(),
                'hour_of_week': timestamp.hour,
                'remote_ip': remote_ip,
                'country_code': country_code,
                'requester': "3E58BAD0-FA0D-11E8-3DCF-0050569E227D",
                'bucket': "somebucket",
                'key': "somekey",
                'operation': "REST.GET VERSIONING",
                'request_uri': "GET /EPOCore/ready-status HTTP/1.1",
                'status_code': status,
                'http_1xx': http_1xx,
                'http_2xx': http_2xx,
                'http_3xx': http_3xx,
                'http_4xx': http_4xx,
                'http_5xx': http_5xx,
                'error_code': "-",
                'bytes_sent': 113,
                'object_size': 0,
                'user_agent': "https-jsse-nio-443-exec-670"
            }  
            print(log_entry)
            if MODE == "ANOMALY":
                continue
            else:
                m = timestamp.time().minute
                m = m % 10
                if m:
                    time.sleep(1/m)
                else:
                    continue
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
