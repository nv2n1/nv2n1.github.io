---
title: "Choosing Stream Processing Tools Based on Latency Needs"
date: 2018-11-27 15:05:37 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /do-big-data-stream-processing-in-the-stream-way/
---

The fundamental lesson from years of big data work is straightforward: solve problems with tools designed for those problems. Organizations routinely force large-scale data through mismatched infrastructure — pushing streams through micro-batching systems, analyzing graphs as tables, handling real-time requirements with batch windows. Each mismatch adds latency, complexity, and operational burden.

Stream processing deserves particular attention here. If your data arrives continuously, your processing engine should be built for continuous flows, not bolted onto batch infrastructure as an afterthought.

## The Latency Problem with Micro-Batching

Micro-batching sounds reasonable in theory: collect stream data into small windows, process the batches, repeat. But every batch carries irreducible overhead — collection time, scheduling, serialization, state management. This cost remains roughly constant regardless of window size.

Shrink the window to reduce latency, and overhead dominates. You pay a fixed penalty repeatedly rather than processing data as it arrives. This becomes painful immediately in production.

Consider a practical case: a financial firm needs live aggregations over five-minute windows — current totals, anomalies, alerts. A micro-batch system still introduces a latency gap between data arrival and result availability. The workarounds are expensive: caching layers, dual systems, manual reconciliation, complex monitoring to detect staleness.

The core question cuts through everything: if data is generated continuously, why shouldn’t it be processed continuously?

## True Stream Processing Architecture

Purpose-built stream processors (Apache Flink, Kafka Streams, Spark Structured Streaming in continuous mode, or Pulsar Functions) treat streams as the fundamental abstraction, not batches. Four concepts form the building blocks:

- **Stream** — data flowing continuously, not accumulated in windows
- **State** — mutable information maintained across events (aggregates, joins, windowed results, session windows)
- **Time** — event time vs. processing time, watermarks to handle out-of-order and late-arriving data
- **Snapshots** — consistent checkpoints for fault tolerance and recovery without reprocessing

With these primitives, you implement complex stateful analytics with millisecond to sub-second latency. Join multiple streams. Maintain windowed aggregations. Detect temporal patterns. Handle late arrivals and machine failures gracefully.

A Flink job processing Kafka topics can maintain state larger than memory via RocksDB, checkpoint state consistently, and recover from failures without losing or duplicating events. Kafka Streams offers a lighter-weight option for JVM environments where you process data where it already lives. Pulsar Functions provides similar capabilities on Pulsar infrastructure.

## When Micro-Batching Still Makes Sense

This isn’t an argument that micro-batching has no place. If latency tolerance is measured in minutes, a well-tuned Spark Streaming job (micro-batch mode) may be simpler operationally and cheaper than maintaining a separate stream processor. The decision hinges on matching latency requirements to tool capabilities.

Consider these scenarios:

- **ETL pipelines refreshing data warehouses every 5-10 minutes**: micro-batching is appropriate
- **User-facing dashboards requiring updates within seconds**: true streaming needed
- **Fraud detection requiring millisecond responses**: true streaming required
- **Log aggregation with per-minute statistics**: either works; choose based on operational preference and existing infrastructure
- **Real-time anomaly detection in metrics**: true streaming recommended
- **Batch model training jobs triggered periodically**: micro-batching sufficient

## Practical Considerations for Stream Processing

If you decide true streaming is necessary, pay attention to these areas.

### Schema Management

Use Confluent Schema Registry, Pulsar Schema Registry, or similar to version and validate message schemas across producers and consumers. This prevents silent data corruption from schema mismatches. Store schemas centrally and enforce compatibility rules (backward, forward, or full compatibility depending on your deployment strategy).

### State Backends and Configuration

Flink and similar frameworks offer state options: RocksDB for larger-than-memory state with checkpointing for fault tolerance, or in-memory for speed with smaller state sets. RocksDB trades some throughput for scalability — state can grow to terabytes. Configure checkpoint intervals carefully; too frequent and overhead dominates, too infrequent and recovery takes longer. Test with your actual state sizes and event rates.

### Exactly-Once Semantics

Ensure your framework and message broker support exactly-once delivery. This prevents both data loss and duplication during failures. Flink provides exactly-once with Kafka and Pulsar. Kafka Streams supports exactly-once with proper configuration. Verify end-to-end exactly-once semantics includes your sink system — idempotent writes to databases or deduplication logic downstream.

### Monitoring and Alerting

Stream processing introduces failure modes batch systems don’t have. Monitor:

- **Lag**: how far behind real-time your processing is (per topic, per consumer group)
- **Checkpoint duration**: long checkpoints indicate performance degradation or state size issues
- **State size**: growing state signals potential memory leaks or missed cleanup logic
- **Record processing rate**: detect when throughput drops unexpectedly
- **Error rates**: track deserialization failures, processing exceptions, sink errors

Set alerts on lag crossing thresholds. Lag that grows unbounded will eventually cause availability issues.

### Local Development and Testing

Test against real message shapes and volumes before production. Use testcontainers for Kafka or Pulsar in integration tests. Generate realistic data volumes and latency patterns. Test failure scenarios: brokers failing, network partitions, consumer lag spike from slow processing. Test state behavior: state size with peak traffic, state recovery after restart, handling of backpressure.

## Example: Flink Stream Job

``` java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
env.enableCheckpointing(5000); // checkpoint every 5 seconds
env.getCheckpointConfig().setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE);

FlinkKafkaConsumer<String> kafkaSource = new FlinkKafkaConsumer<>(
    "input-topic",
    new SimpleStringSchema(),
    properties);

DataStream<String> stream = env.addSource(kafkaSource);

stream
    .map(value -> new Event(value))
    .assignTimestampsAndWatermarks(
        WatermarkStrategy
            .forBoundedOutOfOrderness(Duration.ofSeconds(30))
            .withTimestampAssigner((event, timestamp) -> event.getEventTime()))
    .keyBy(Event::getUserId)
    .window(TumblingEventTimeWindows.of(Time.minutes(5)))
    .grace(Time.minutes(2))
    .aggregate(new CountAggregate(), new WindowFunction<...>(...))
    .addSink(new FlinkKafkaProducer<>(
        "output-topic",
        new SimpleStringSchema(),
        sinkProperties));

env.execute("Stream Processing Job");
```

## Example: Kafka Streams Topology

``` java
StreamsBuilder builder = new StreamsBuilder();

KStream<String, String> input = builder.stream("input-topic");

input
    .mapValues(value -> new Event(value))
    .groupByKey()
    .windowedBy(TimeWindows.of(Duration.ofMinutes(5)).grace(Duration.ofMinutes(2)))
    .aggregate(
        () -> 0L,
        (k, v, agg) -> agg + 1,
        Materialized.as("event-count-store"))
    .toStream()
    .to("output-topic", Produced.with(
        Serdes.String(),
        Serdes.Long()));

Topology topology = builder.build();
KafkaStreams streams = new KafkaStreams(topology, streamsProperties);
streams.start();
Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
```

## Handling Late Data

Real streams don’t deliver events in perfect order. Events arrive late due to network delays, buffering, or clock skew. Define a grace period — how long after window close to accept late events. Flink and Kafka Streams both support grace periods:

``` java
.window(TumblingEventTimeWindows.of(Time.minutes(5)))
.grace(Time.minutes(2)) // accept events up to 2 minutes late
.aggregate(...)
```

Late events beyond the grace period can be sidecar-output to a separate topic for analysis or manual processing. Use watermarks to signal when windows should close. Watermarks represent the timestamp at which all events earlier than that timestamp have arrived:

``` java
DataStream<Event> stream = kafkaSource
    .assignTimestampsAndWatermarks(
        WatermarkStrategy
            .forBoundedOutOfOrderness(Duration.ofSeconds(30))
            .withTimestampAssigner((event, timestamp) -> event.getEventTime()));
```

## Choosing Your Framework

**Apache Flink**: Most mature for complex stateful streaming, exactly-once semantics, and large-scale deployments. Strong state management, flexible windowing, and extensive ecosystem. Higher operational complexity. Good for organizations that can justify a dedicated streaming platform.

**Kafka Streams**: Simpler operational story if you’re already using Kafka. Lightweight, no separate cluster needed. Runs as a library in your application. Good for straightforward transformations, windowing, and joins. Limited compared to Flink for very complex state management.

**Spark Structured Streaming**: Unifies batch and stream via DataFrames. Good if you have existing Spark infrastructure and want a unified engine. Continuous mode provides lower latency than micro-batch but adds complexity.

**Pulsar Functions**: Lightweight compute directly on Pulsar infrastructure. Good for simple transformations and sinks. State management is simpler than Flink but more limited in capability.

## The Real Tradeoff

Stream processing trades operational complexity for latency and result freshness. A micro-batch system may be operationally simpler if your latency requirements allow it. But trying to force sub-second latency out of a batch engine wastes engineering effort and operations budget.

Understand your problem’s actual requirements — latency SLA, throughput, state size, failure tolerance — then choose the system built to solve that problem efficiently. The tool should match the problem, not the reverse.
