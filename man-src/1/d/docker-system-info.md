---
title: "docker-system-info(1)"
name: "docker-system-info"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-system-info/"
description: "docker-system-info – Display system-wide information"
---

<h2 class="name">NAME</h2>
<p> docker-system-info &#8211; Display system-wide information </p>
<h2>SYNOPSIS</h2>
<p> <code>docker system info [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> This command displays system wide information regarding the Docker installation. Information displayed includes the kernel version, number of containers and images. The number of images shown is the number of unique images. The same image tagged under different names is counted only once. </p>
<p> If a format is specified, the given template will be executed instead of the default format. Go&#8217;s <code>text/template</code> package describes all the details of the format. </p>
<p> Depending on the storage driver in use, additional information can be shown, such as pool name, data file, metadata file, data space used, total data space, metadata space used, and total metadata space. </p>
<p> The data file is where the images are stored and the metadata file is where the meta data regarding those images are stored. When run for the first time Docker allocates a certain amount of data space and meta data space from the space available on the volume where /var/lib/docker is mounted. </p>
<h2>EXAMPLES</h2>
<h2>Display Docker system information</h2>
<p> Here is a sample output for a daemon running on Ubuntu, using the overlay2 storage driver: </p>
<dl>
<dt>
<dd>
<pre>
$ docker -D info
Client:
 Debug Mode: true
Server:
 Containers: 14
  Running: 3
  Paused: 1
  Stopped: 10
 Images: 52
 Server Version: 1.13.0
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Native Overlay Diff: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Plugins:
  Volume: local
  Network: bridge host macvlan null overlay
 Swarm: active
  NodeID: rdjq45w1op418waxlairloqbm
  Is Manager: true
  ClusterID: te8kdyw33n36fqiz74bfjeixd
  Managers: 1
  Nodes: 2
  Orchestration:
   Task History Retention Limit: 5
  Raft:
   Snapshot Interval: 10000
   Number of Old Snapshots to Retain: 0
   Heartbeat Tick: 1
   Election Tick: 3
  Dispatcher:
   Heartbeat Period: 5 seconds
  CA Configuration:
   Expiry Duration: 3 months
  Node Address: 172.16.66.128 172.16.66.129
  Manager Addresses:
   172.16.66.128:2477
 Runtimes: runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 8517738ba4b82aff5662c97ca4627e7e4d03b531
 runc version: ac031b5bf1cc92239461125f4c1ffb760522bbf2
 init version: N/A (expected: v0.13.0)
 Security Options:
  apparmor
  seccomp
   Profile: default
 Kernel Version: 4.4.0-31-generic
 Operating System: Ubuntu 16.04.1 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 2
 Total Memory: 1.937 GiB
 Name: ubuntu
 ID: H52R:7ZR6:EIIA:76JG:ORIY:BVKF:GSFU:HNPG:B5MK:APSC:SZ3Q:N326
 Docker Root Dir: /var/lib/docker
 Debug Mode: true
  File Descriptors: 30
  Goroutines: 123
  System Time: 2016-11-12T17:24:37.955404361-08:00
  EventsListeners: 0
 Http Proxy: <a rel="nofollow" href="http://test:test@proxy.example.com:8080">http://test:test@proxy.example.com:8080</a>
 Https Proxy: <a rel="nofollow" href="https://test:test@proxy.example.com:8080">https://test:test@proxy.example.com:8080</a>
 No Proxy: localhost,127.0.0.1,docker-registry.somecorporation.com
 Registry: <a rel="nofollow" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>
 WARNING: No swap limit support
 Labels:
  storage=ssd
  staging=true
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Registry Mirrors:
   <a rel="nofollow" href="http://192.168.1.2/">http://192.168.1.2/</a>
   <a rel="nofollow" href="http://registry-mirror.example.com:5000/">http://registry-mirror.example.com:5000/</a>
 Live Restore Enabled: false
</pre>
</dl>
<p> The global -D option tells all docker commands to output debug information. </p>
<p> The example below shows the output for a daemon running on Red Hat Enterprise Linux, using the devicemapper storage driver. As can be seen in the output, additional information about the devicemapper storage driver is shown: </p>
<dl>
<dt>
<dd>
<pre>
$ docker info
Client:
 Debug Mode: false
Server:
 Containers: 14
  Running: 3
  Paused: 1
  Stopped: 10
 Untagged Images: 52
 Server Version: 1.10.3
 Storage Driver: devicemapper
  Pool Name: docker-202:2-25583803-pool
  Pool Blocksize: 65.54 kB
  Base Device Size: 10.74 GB
  Backing Filesystem: xfs
  Data file: /dev/loop0
  Metadata file: /dev/loop1
  Data Space Used: 1.68 GB
  Data Space Total: 107.4 GB
  Data Space Available: 7.548 GB
  Metadata Space Used: 2.322 MB
  Metadata Space Total: 2.147 GB
  Metadata Space Available: 2.145 GB
  Udev Sync Supported: true
  Deferred Removal Enabled: false
  Deferred Deletion Enabled: false
  Deferred Deleted Device Count: 0
  Data loop file: /var/lib/docker/devicemapper/devicemapper/data
  Metadata loop file: /var/lib/docker/devicemapper/devicemapper/metadata
  Library Version: 1.02.107-RHEL7 (2015-12-01)
 Execution Driver: native-0.2
 Logging Driver: json-file
 Plugins:
  Volume: local
  Network: null host bridge
 Kernel Version: 3.10.0-327.el7.x86_64
 Operating System: Red Hat Enterprise Linux Server 7.2 (Maipo)
 OSType: linux
 Architecture: x86_64
 CPUs: 1
 Total Memory: 991.7 MiB
 Name: ip-172-30-0-91.ec2.internal
 ID: I54V:OLXT:HVMM:TPKO:JPHQ:CQCD:JNLC:O3BZ:4ZVJ:43XJ:PFHZ:6N2S
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Username: gordontheturtle
 Registry: <a rel="nofollow" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>
 Insecure registries:
  myinsecurehost:5000
  127.0.0.0/8
</pre>
</dl>
<p> You can also specify the output format: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker info-- format '&#123;&#123;json .}}'
{
    "ID" : "I54V:OLXT:HVMM:TPKO:JPHQ:CQCD:JNLC:O3BZ:4ZVJ:43XJ:PFHZ:6N2S", "Containers" : 14, ...
}
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Format the output using the given Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for info</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-system/">docker-system</a>(1)</code> </p>
<h2>Index</h2>
