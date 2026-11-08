---
title: "Hadoop MapReduce: When to Use It and Deployment Strategies"
date: 2013-07-17 09:37:11 +0000
layout: post
canonical: https://www.systutorials.com/hadoop-mapreduce-tutorials/
---

MapReduce is a foundational distributed computing model, but it’s no longer the default choice for new projects. Hadoop’s MapReduce (via YARN in Hadoop 2.x+) remains production-stable and useful for specific scenarios, while Apache Spark, Flink, and cloud-native services handle most modern workloads more efficiently.

## When MapReduce Still Makes Sense

Use MapReduce if you’re:

- Maintaining existing Hadoop clusters with established MapReduce jobs
- Running legacy batch ETL pipelines where latency isn’t critical
- Operating in strict on-premise environments where you control infrastructure
- Needing predictable resource isolation and allocation guarantees via YARN
- Working with teams already experienced with MapReduce internals

For anything else—new projects, real-time processing, interactive queries, or machine learning—evaluate Spark, Flink, or managed services first.

## MapReduce Architecture Basics

Every MapReduce job follows a two-phase model: **Mapper** processes input in parallel, **Reducer** aggregates results.

Here’s a complete Word Count example:

``` java
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import java.io.IOException;

public class WordCount {
    public static class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final IntWritable one = new IntWritable(1);
        private Text word = new Text();

        @Override
        public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
            String[] words = value.toString().split("\\s+");
            for (String w : words) {
                if (!w.isEmpty()) {
                    word.set(w.toLowerCase());
                    context.write(word, one);
                }
            }
        }
    }

    public static class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) 
            throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        Job job = Job.getInstance();
        job.setJarByClass(WordCount.class);
        job.setMapperClass(WordCountMapper.class);
        job.setReducerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

## Submitting and Monitoring Jobs

Compile and package your code, then submit:

``` bash
javac -cp /opt/hadoop/share/hadoop/common/\* WordCount.java
jar cvf wordcount.jar WordCount*.class
hadoop jar wordcount.jar WordCount /input/data /output/results
```

Monitor job progress via the YARN ResourceManager UI at `http://namenode-host:8088`. Check application logs for task-level details, spill metrics, and GC overhead.

## YARN Resource Configuration

Edit `mapred-site.xml` to tune memory, parallelism, and container behavior:

``` xml
<property>
    <name>mapreduce.job.maps</name>
    <value>32</value>
</property>
<property>
    <name>mapreduce.job.reduces</name>
    <value>8</value>
</property>
<property>
    <name>mapreduce.map.memory.mb</name>
    <value>2048</value>
</property>
<property>
    <name>mapreduce.reduce.memory.mb</name>
    <value>4096</value>
</property>
<property>
    <name>mapreduce.map.java.opts</name>
    <value>-Xmx1536m</value>
</property>
<property>
    <name>mapreduce.reduce.java.opts</name>
    <value>-Xmx3072m</value>
</property>
<property>
    <name>mapreduce.task.io.sort.mb</name>
    <value>512</value>
</property>
```

Set heap size (`java.opts`) to about 80% of memory allocation to avoid out-of-memory errors. Increase `io.sort.mb` if you see many spill events in task logs. Start conservative and scale based on actual job performance.

## Common Tuning Issues

**High spill overhead**: Mappers write intermediate data to disk during shuffle-sort. Increase `mapreduce.task.io.sort.mb` and reducer memory.

**Slow reducers**: If task logs show reduce phase taking much longer than map, you have uneven key distribution. Consider custom partitioners to balance load across reducers.

**Memory pressure**: Monitor YARN NodeManager logs for container preemption. Reduce per-task memory or decrease parallelism if the cluster is oversubscribed.

## Modern Alternatives

**Apache Spark**: 10–100x faster on iterative workloads. Supports SQL, streaming, and MLlib. Runs on the same HDFS infrastructure.

**Apache Flink**: Purpose-built for stream processing with batch as a special case. Better for continuous data pipelines.

**Cloud-managed services**: AWS EMR, Google Dataproc, Azure HDInsight, or Databricks handle cluster provisioning, auto-scaling, and security updates automatically.

**Distributed SQL engines**: Trino or Spark SQL give you SQL access to HDFS without writing code.

## Learning Resources

- <a href="https://hadoop.apache.org/docs/stable/" rel="nofollow noopener" target="_blank">Apache Hadoop 3.x Documentation</a>: Current stable branch with YARN improvements and erasure coding support
- <a href="https://www.oreilly.com/library/view/hadoop-the-definitive/9781491901632/" rel="nofollow noopener" target="_blank">Hadoop: The Definitive Guide by Tom White</a>: Still the most comprehensive reference
- Original MapReduce paper by Dean and Ghemawat: Understanding the conceptual foundation helps with debugging distributed algorithm issues

MapReduce excels at predictable, isolated batch jobs on existing infrastructure. If you’re building something new and need speed, flexibility, or operational automation, start with Spark or a managed service instead.
