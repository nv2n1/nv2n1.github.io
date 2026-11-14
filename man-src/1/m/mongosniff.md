---
title: "mongosniff(1)"
name: "mongosniff"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongosniff/"
description: "mongosniff – MongoDB Protocol Introspection Utility"
---

<h2>NAME</h2>
<p> mongosniff &#8211; MongoDB Protocol Introspection Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>mongosniff</code> provides a low-level operation tracing/sniffing view into database activity in real time. Think of <code>mongosniff</code> as a MongoDB-specific analogue of <code>tcpdump</code> for TCP/IP network traffic. Typically, <code>mongosniff</code> is most frequently used in driver development. </p>
<p> <code>NOTE:</code> <code>mongosniff</code> requires <code>libpcap</code> and is only available for Unix-like systems. Furthermore, the version distributed with the MongoDB binaries is dynamically linked against aversion 0.9 of <code>libpcap</code>. If your system has a different version of <code>libpcap</code>, you will need to compile <code>mongosniff</code> yourself or create a symbolic link pointing to <code>libpcap.so.0.9</code> to your local version of <code>libpcap</code>. Use an operation that resembles the following: </p>
<pre>
ln -s /usr/lib/libpcap.so.1.1.1 /usr/lib/libpcap.so.0.9
</pre>
<p> Change the path&#8217;s and name of the shared library as needed. </p>
<p> As an alternative to <code>mongosniff</code>, Wireshark, a popular network sniffing tool is capable of inspecting and parsing the MongoDB wire protocol.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongosniff</code></p>
<dd>
<dt><code>mongosniff</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongosniff</code> options and usage.</p>
<dt><code>&#8211;forward &lt;host&gt;&lt;:port&gt;</code></p>
<dd> Declares a host to forward all parsed requests that the <code>mongosniff</code> intercepts to another <code>mongod</code> instance and issue those operations on that database instance. </p>
<p> Specify the target host name and port in the <code>&lt;host&gt;&lt;:port&gt;</code> format. </p>
<p> To connect to a replica set, specify the replica set seed name and the seed list of set members. Use the following format: </p>
<pre>
&lt;replica_set_name&gt;/&lt;hostname1&gt;&lt;:port&gt;,&lt;hostname2:&lt;port&gt;,...
</pre>
<dt><code>&#8211;source &lt;NET [interface]&gt;</code></p>
<dd> Specifies source material to inspect. Use <code>&#8211;source NET [interface]</code> to inspect traffic from a network interface (e.g. <code>eth0</code> or <code>lo</code>.) Use <code>&#8211;source FILE [filename]</code> to read captured packets in <i>pcap</i> format. </p>
<p> You may use the <code>&#8211;source DIAGLOG [filename]</code> option to read the output files produced by the <i>&#8211;diaglog</i> option.</p>
<dt><code>&#8211;objcheck</code></p>
<dd> Displays invalid BSON objects only and nothing else. Use this option for troubleshooting driver development. This option has some performance impact on the performance of <code>mongosniff</code>.</p>
<dt><code>&lt;port&gt;</code></p>
<dd> Specifies alternate ports to sniff for traffic. By default, <code>mongosniff</code> watches for MongoDB traffic on port <code>27017</code>. Append multiple port numbers to the end of <code>mongosniff</code> to monitor traffic on multiple ports.</dl>
<h2>USE</h2>
<p> Use the following command to connect to a <code>mongod</code> or <code>mongos</code> running on port 27017 <i>and</i> 27018 on the localhost interface: </p>
<pre>
mongosniff --source NET lo 27017 27018
</pre>
<p> Use the following command to only log invalid <i>BSON</i> objects for the <code>mongod</code> or <code>mongos</code> running on the localhost interface and port 27018, for driver development and troubleshooting: </p>
<pre>
mongosniff --objcheck --source NET lo 27018
</pre>
<h2>BUILD MONGOSNIFF</h2>
<p> To build <code>mongosniff</code> yourself, Linux users can use the following procedure:</p>
<dl>
<dt>1.</p>
<dd> Obtain prerequisites using your operating systems package management software. Dependencies include:</p>
<dt>&bull;</p>
<dd> <code>libpcap</code> &#8211; to capture network packets.</p>
<dt>&bull;</p>
<dd> <code>git</code> &#8211; to download the MongoDB source code.</p>
<dt>&bull;</p>
<dd> <code>scons</code> and a C++ compiler &#8211; to build <code>mongosniff</code>.</p>
<dt>2.</p>
<dd> Download a copy of the MongoDB source code using <code>git</code>: </p>
<pre>
git clone <a href="git://github.com/mongodb/mongo.git">git://github.com/mongodb/mongo.git</a>
</pre>
<dt>3.</p>
<dd> Issue the following sequence of commands to change to the <code>mongo/</code> directory and build <code>mongosniff</code>: </p>
<pre>
cd mongo
scons mongosniff
</pre>
<p> <code>NOTE:</code> If you run <code>scons mongosniff</code> before installing <code>libpcap</code> you must run <code>scons clean</code> before you can build <code>mongosniff</code>.</dl>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
