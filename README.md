### [README.md](file:///home/pathik/Documents/DataEngineer/Projects/docker-kafka-test/README.md)

```markdown
# Kafka KRaft Docker Testing Project

## Overview
This project demonstrates Kafka KRaft mode deployment using Docker and includes Python test scripts to verify performance. Key features:
- Kafka KRaft mode (no ZooKeeper dependency)
- Docker containerization
- Python test scripts for producers/consumers
- Real-time performance monitoring

## Quick Start

```bash
# Start Kafka in KRaft mode
docker-compose up -d

# Create test topic
python kafka_docker_package/producer_kafka/create_topics.py

# Run test scripts
python kafka_docker_package/producer_kafka/stock_price_generator.py  # Producer
python kafka_docker_package/consumer_kafka/consumer_data_visualization.py  # Consumer
```

## Project Structure
```
kafka-container-test/
├── kafka_docker_package/
│   ├── producer_kafka/
│   │   ├── create_topics.py          # Topic creation
│   │   └── stock_price_generator.py  # Test data generator
│   └── consumer_kafka/
│       └── consumer_data_visualization.py  # Test consumer
├── docker-compose.yml                # KRaft configuration
└── README.md
```

## Docker Configuration
```yaml
version: "3.9"
services:
  kafka:
    image: confluentinc/cp-kafka:7.4.0
    environment:
      KAFKA_KRAFT_MODE: true
      KAFKA_CLUSTER_ID: ${CLUSTER_ID}
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: "broker,controller"
      KAFKA_LISTENERS: "PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:29093"
      KAFKA_ADVERTISED_LISTENERS: "PLAINTEXT://localhost:9092"
```

## Test Scripts
1. Topic Creation:
   - Creates required topics
   - Configures partitions and replication

2. Data Generator:
   - Produces synthetic stock data
   - Monitors message throughput
   - Logs performance metrics

3. Consumer Visualization:
   - Real-time data consumption
   - Performance monitoring
   - Matplotlib visualization

## Performance Testing
```bash
# Monitor Kafka metrics
docker exec kafka kafka-topics.sh --describe --bootstrap-server localhost:9092

# Check consumer lag
docker exec kafka kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --describe --group test-group

# View container stats
docker stats kafka
```

## Troubleshooting
1. KRaft Mode Issues:
   - Verify CLUSTER_ID is set
   - Check controller listener
   - Monitor broker logs

2. Performance Issues:
   - Check resource allocation
   - Monitor message latency
   - Verify network connectivity

For detailed setup and configuration, refer to the documentation above.
```

This update:
1. Focuses on Kafka KRaft mode
2. Highlights testing capabilities
3. Includes performance monitoring
4. Provides troubleshooting specific to KRaft