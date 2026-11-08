---
title: "Adding a Secondary NameNode Metadata Directory to HDFS"
date: 2018-03-24 11:44:04 +0000
layout: post
canonical: https://www.systutorials.com/how-to-add-a-new-hdfs-namenode-metadata-directory-to-an-existing-cluster/
---

Adding a second metadata directory to your HDFS NameNode increases reliability by maintaining synchronized replicas of the namespace and transaction logs across separate disks. This guide walks through the process safely.

## Prerequisites and Planning

Before starting, verify your current configuration and plan the new directory location:

``` bash
grep -A2 "dfs.namenode.name.dir" $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

The new directory should be on a physically separate disk from your existing metadata directory. If both directories are on the same disk, you gain no reliability benefit. Ensure the target disk has adequate free space—the new directory will be a full copy of your existing metadata.

## Step 1: Back Up Existing NameNode Metadata

Before making any changes, create a complete backup of your current metadata directory:

``` bash
# As the hadoop user (or appropriate service account)
tar czf /backup/namenode-metadata-$(date +%Y%m%d-%H%M%S).tar.gz /home/hadoop/hdfs/
```

Keep this backup in a safe location separate from your cluster. If something goes wrong during the procedure, you’ll need this to recover.

## Step 2: Stop the NameNode

Shut down the NameNode gracefully. First check for any running jobs or active file transfers:

``` bash
hdfs dfsadmin -safemode get
```

Wait until safe mode is entered, then stop the NameNode:

``` bash
$HADOOP_HOME/sbin/stop-namenode.sh
```

Verify it has fully stopped:

``` bash
jps | grep NameNode
```

## Step 3: Prepare the New Directory

Create the new metadata directory and set proper permissions:

``` bash
sudo mkdir -p /home/hadoop/hdfs2
sudo chown hadoop:hadoop /home/hadoop/hdfs2
sudo chmod 700 /home/hadoop/hdfs2
```

Copy the entire contents of the existing metadata directory:

``` bash
cp -r /home/hadoop/hdfs/* /home/hadoop/hdfs2/
```

Verify the copy completed successfully and file counts match:

``` bash
diff <(find /home/hadoop/hdfs -type f | wc -l) \
     <(find /home/hadoop/hdfs2 -type f | wc -l)
```

## Step 4: Update hdfs-site.xml

Edit your hdfs-site.xml to include both directories. The NameNode will maintain synchronized copies in both locations:

``` xml
<property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///home/hadoop/hdfs,file:///home/hadoop/hdfs2</value>
    <description>Comma-separated list of NameNode metadata directories for namespace and transaction logs.</description>
</property>
```

Note: Use commas without spaces between paths, or include spaces consistently—HDFS is sensitive to formatting here.

Distribute this updated configuration to all NameNode and Secondary NameNode hosts if you have them. Use your configuration management tool (Ansible, Puppet, etc.) if available:

``` bash
ansible namenode_group -m copy -a "src=hdfs-site.xml dest=/etc/hadoop/conf/"
```

## Step 5: Start the NameNode

Start the NameNode:

``` bash
$HADOOP_HOME/sbin/start-namenode.sh
```

Monitor the startup logs for errors:

``` bash
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log
```

Look for messages confirming both directories are being used. Once started, verify NameNode health:

``` bash
hdfs dfsadmin -report
```

## Step 6: Verify Both Directories Are in Use

Check that both metadata directories contain current transaction logs and images:

``` bash
ls -lh /home/hadoop/hdfs/current/
ls -lh /home/hadoop/hdfs2/current/
```

Both should have identical `fsimage_*` and `edits_*` files with matching timestamps. If one directory is empty or outdated, there’s a configuration problem—stop the NameNode and investigate before proceeding.

## Monitoring and Troubleshooting

If the NameNode fails to start with multiple directories configured, common issues include:

- **Permission problems**: Ensure the hadoop user can write to both directories
- **Disk full**: Check available space with `df -h` on both mount points
- **Mismatched metadata**: If directories diverge, you must restart with a single known-good directory and recopy

If you need to remove a directory later, update hdfs-site.xml with only the desired directory, restart the NameNode, then clean up the removed directory’s files.

## Performance Note

Maintaining multiple metadata directories has a small I/O cost—each metadata update is written to all configured directories. In 2026 deployments with modern SSDs, this is typically negligible, but high-frequency metadata operations (millions of files) may show slight latency increases. Monitor your NameNode’s write latency before and after adding the secondary directory.
