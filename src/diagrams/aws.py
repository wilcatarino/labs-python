from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2Instance
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53

with Diagram("Web Application", show=False):
    dns = Route53("web.application.com.br")
    load_balancer = ELB("lb-1")

    with Cluster("Application"):
        application_group = [EC2Instance("ec2-1"), EC2Instance("ec2-2"), EC2Instance("ec2-3")]

    with Cluster("Database"):
        database = RDS("db-1")

    dns >> load_balancer >> application_group
    application_group >> database
