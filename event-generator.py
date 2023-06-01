import time
import requests
from kubernetes import client, config
import os

config.load_incluster_config()  # Load the in-cluster Kubernetes configuration
v1 = client.CoreV1Api()

def send_request_and_generate_event():
    namespace = "default"
    event_name = "custom_event"

    hub = os.environ.get('SELENIUM_HUB_SERVICE_HOST')
    previous_value = 0

    while True:
        try:
            response = requests.get('http://' + hub + ':4444/se/grid/newsessionqueue/queue', timeout=5)
            response.raise_for_status()

            value = len(response.json()['value'])
            if value != previous_value:
                print("Number of sessions: ", value)
                previous_value = value

                event = {
                    "apiVersion": "v1",
                    "kind": "Event",
                    "metadata": {
                        "name": event_name,
                        "labels": {
                            "SessionCount": str(value)
                        }
                    }
                }
                
                try:
                    events = v1.list_namespaced_event(namespace=namespace, field_selector="metadata.name=custom-event")
                    if events.items:
                        v1.replace_namespaced_event(event_name, namespace, event)
                        print(f"Updated event custom-event with SessionCount: {value}")
                    else:
                        v1.create_namespaced_event(namespace=namespace, body=event)
                        print(f"Created new event custom-event with SessionCount: {value}")
                except client.exceptions.ApiException as e:
                    print(f"Failed to create or update event custom-event: {e}")

        except requests.exceptions.RequestException as e:
            print("Error occurred during the request:", str(e))

        time.sleep(5)

if __name__ == '__main__':
    send_request_and_generate_event()
