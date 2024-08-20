# -*- coding: utf-8 -*-

"""
kafka is like a messaging system

kafka is distributed platform/application:
     -in production environment kafka is referred as kafka cluster.
     - a cluster is made up of morethan one kafka server.
     - each kafka server is referred as broker.
     
     
kafka is fault-tolerant:
    -meaning: ability of a system to continue operating without interruption when one or more of its components fail.
    - in kafka cluster messages are replicated in multiple broker
    -replication factor:
    -means one message is replicated or sent to all nodes or all members of a cluster, whenever one node fails, 
    you can access the message from other nodes as long as one or more is still functioning
    
kafka is scalable system:
    - you can add new brokers any time
    - when your users increase you can add new brokers
    - you can scale it by adding new brokers and consumers
    
zookeeper:
    - its inside the kafka echo system
    - its a distributed, open source configuration, synchronization service
    - it synchronizes the changes which happens in one place to the whole system
    
intsalling kafka:
    - you should download kafka from its website.
    - upzip it in kafka folder in c.
running kafka:
    - first run zookeeper first using this command.
      bin/zookeeper-server-start.sh config/zookeeper.properties  #linux
     .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties  #windows
     
    - second run the kafka.
      bin/kafka-server-start.sh config/kafka.properties   #linux
      .\bin\windows\kafka-server-start.bat .\config\kafka.properties  #windows
      
      other commands are also available
kafka manager:
    - its a GUI for doing kafka commands 
      
what is kafka topic:
    - topic is the kafka component where producers are connected
    - producer publish message in kafka topic
    - topics in kafka is multi subscriber
    """
  #...
