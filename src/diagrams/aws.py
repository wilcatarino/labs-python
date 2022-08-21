from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53

with Diagram("Biller Development", show=False):
    development_dns = Route53("biller-development.estoca.com.br")
    development_lb = ELB("lb-biller-development")

    with Cluster("Application"):
        application_group = [ECS("biller-development-1")]

    with Cluster("Database"):
        development_db = RDS("biller-development")

    development_dns >> development_lb >> application_group
    application_group >> development_db
