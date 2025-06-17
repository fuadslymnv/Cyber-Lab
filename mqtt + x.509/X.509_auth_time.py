import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

ENDPOINT = "a2fufd1sshzu8r-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "MyTestClient"
ROOT_CA = "AmazonRootCA1.pem"              
PRIVATE_KEY = "a67c941f07ef43d59feede0cb31c390efda64c0dfb0c5be3fab5ad4e0f6fec55-private.pem.key"
CERTIFICATE = "a67c941f07ef43d59feede0cb31c390efda64c0dfb0c5be3fab5ad4e0f6fec55-certificate.pem.crt"   

def measure_connection_time():
    mqtt_client = AWSIoTMQTTClient(CLIENT_ID)
    mqtt_client.configureEndpoint(ENDPOINT, 8883)
    mqtt_client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)

    mqtt_client.configureOfflinePublishQueueing(-1)  
    mqtt_client.configureDrainingFrequency(2)  
    mqtt_client.configureConnectDisconnectTimeout(10)  
    mqtt_client.configureMQTTOperationTimeout(5)  

    start_time = time.time()
    mqtt_client.connect()
    end_time = time.time()

    connection_time = end_time - start_time
    print(f"Connection and authentication took {connection_time:.3f} seconds.")

    mqtt_client.disconnect()

if __name__ == "__main__":
    measure_connection_time()
