---
title: "Sorting Performance Benchmarks on Hadoop"
date: 2012-01-07 08:55:00 +0000
modified: 2026-04-12 04:39:21 +0000
author: "Eric Ma"
layout: post
categories: [algorithms-data-structures]
canonical: /simple-sort-benchmark-on-hadoop/
---

Running benchmarks after a Hadoop installation helps validate that your cluster works correctly and gives you baseline performance metrics. The Sort benchmark is a standard test that exercises the MapReduce execution engine and HDFS, making it useful for stress-testing both the distributed storage layer and computation framework.

## What the Sort Benchmark Does

The Sort benchmark uses MapReduce to sort an input directory into an output directory. The mapper and reducer are both identity operations — they pass data through unchanged. This means performance differences reflect the overhead of the MapReduce framework itself, HDFS I/O, and network shuffling between nodes, rather than any computational complexity in the application logic.

The benchmark uses Sequence files with BytesWritable keys and values as input and output formats. This format is common in Hadoop workloads and better represents real-world distributed processing than plain text.

## RandomWriter: Generating Test Data

Before running the Sort benchmark, you need test data. The RandomWriter program generates this automatically. It writes 10 GB of random data per node by default, distributed across your HDFS cluster. Each mapper task reads a single filename as input and writes random BytesWritable key-value pairs to a sequence file in HDFS. No reduce phase is used.

## Running the Benchmark

After setting up and starting your Hadoop cluster, run these commands from your Hadoop installation directory:

``` bash
hadoop jar hadoop-*-examples.jar randomwriter rand
hadoop jar hadoop-*-examples.jar sort rand rand-sort
```

The first command generates random data into the `rand` directory. The second command sorts the contents of `rand` and writes the sorted output to `rand-sort`.

If you’re running from outside the Hadoop directory, provide the full or relative path to the jar file:

``` bash
hadoop jar /opt/hadoop/share/hadoop/tools/hadoop-*-examples.jar randomwriter rand
hadoop jar /opt/hadoop/share/hadoop/tools/hadoop-*-examples.jar sort rand rand-sort
```

## Customizing the Benchmark

The RandomWriter program accepts several options to control data generation:

``` bash
hadoop jar hadoop-*-examples.jar randomwriter \
  -Dtest.randomwrite.bytes_per_map=10737418240 \
  -Dtest.randomwrite.maps_per_host=1 \
  rand
```

Key configuration options:

- `test.randomwrite.bytes_per_map`: Total bytes each mapper writes (default: 1 GB)
- `test.randomwrite.maps_per_host`: Number of map tasks per host (default: 1)
- `test.randomwrite.value_length`: Length of values in bytes (default: 100)

For example, to generate 20 GB per node with larger values:

``` bash
hadoop jar hadoop-*-examples.jar randomwriter \
  -Dtest.randomwrite.bytes_per_map=21474836480 \
  -Dtest.randomwrite.value_length=500 \
  rand
```

The Sort benchmark itself accepts configuration through the MapReduce job properties:

``` bash
hadoop jar hadoop-*-examples.jar sort \
  -Dmapred.reduce.tasks=4 \
  rand rand-sort
```

## Monitoring Progress and Results

Check job progress in the ResourceManager web interface (default: `http://localhost:8088` on the active NameNode). You can also monitor HDFS usage at `http://localhost:9870`.

After the sort completes, verify the output:

``` bash
hdfs dfs -ls -lh rand-sort/
hdfs dfs -head rand-sort/part-r-00000 | od -c
```

The `od -c` output shows the sorted BytesWritable format isn’t human-readable, but you can confirm the sort executed successfully by checking for output files.

## Performance Considerations

The Sort benchmark stress-tests several areas:

- **HDFS write performance**: RandomWriter pushes data to HDFS
- **MapReduce scheduling**: Job submission and task allocation overhead
- **Shuffle and sort**: The most computationally expensive phase
- **HDFS read performance**: Reading sorted output

Total runtime depends on data volume, number of nodes, network bandwidth, and disk speed. On a modest cluster with spinning disks, sorting 100+ GB can take 10-30 minutes depending on configuration.

For larger-scale testing, scale both `test.randomwrite.bytes_per_map` and the number of nodes. The benchmark scales reasonably to very large clusters, though I/O becomes the bottleneck before CPU.

## Modern Alternatives

If you’re deploying new systems, consider managed Hadoop distributions like AWS EMR, Google Dataproc, or Azure HDInsight. These handle cluster provisioning, patching, and scaling automatically. For stream processing, Apache Flink or Spark may better suit modern workloads. Traditional MapReduce benchmarking is less common today, but Sort remains useful for validating base Hadoop cluster health.
