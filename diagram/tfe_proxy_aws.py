# diagram.py
from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.general import Client
from diagrams.aws.general import InternetAlt1

with Diagram("TFE Proxy", show=False):
    Client("Client") >> Edge(label="443") >> EC2("TFE") >> Edge(label="8080") >> EC2("MITMProxy") >> InternetAlt1("Internet")