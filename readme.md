Real Time Twitter Sentiment Analysis using Kafka and ELK Stack 


Steps to run : 

// Start up of Kafka Enivronment 

1. Zookeeper: 
	 bin/zookeeper-server-start.sh config/zookeeper.properties
2. Kafka
	bin/kafka-server-start.sh config/server.properties
3. Create Topic: 
	bin/kafka-topics.sh --create --topic assignment3 --bootstrap-server localhost:9092
4. Producer:
	bin/kafka-console-producer.sh --topic assignment3 --bootstrap-server localhost:9092
5. Consumer: 
	bin/kafka-console-consumer.sh --topic assignment3 --from-beginning --bootstrap-server localhost:9092


// Start of ELK Stack : 
1. Elasticsearch (At the directory of Elasticsearch) :
    ./bin/elasticsearch
2. Kibana (At the directory of Kibana) :
    ./bin/kibana
3. Logstash (At the directory of Logstash) :
    ./bin/logstash  (OR) ./bin/logstash -f /path/to/conf/logstash-sample.conf
    This depends on the mode of installation. 

This Application is built on Tweepy - Python for Twitter API Analysis.
1. Arguments has been configured using "config.ini" which is at the same directory as "Producer.py"
3. All the necessary libraries are present in "requirements.txt".  
2. Run the python file using command : 
	python Producer.py

// Note:- 
1. Have employed Hugging Face - Transformers for Sentiment Analysis. 
2. Logstash requires its .conf file to point the input and output. 
ex. 
input {

  kafka {
      bootstrap_servers => ["localhost:9092"]
      topics => ["assignment3"]
  }


}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "assignment3"
    #user => "elastic"
    #password => "changeme"
  }
} 





