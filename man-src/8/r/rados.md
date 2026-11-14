---
title: "rados(8)"
name: "rados"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rados/"
description: "rados – rados object storage utility"
---

<p>rados &#8211; rados object storage utility</p>
<h2>Synopsis</h2>
<pre><code>rados</code> [ -m <i>monaddr</i> ] [ mkpool | rmpool <i>foo</i> ] [ -p | --pool
<i>pool</i> ] [ -s | --snap <i>snap</i> ] [ -i <i>infile</i> ] [ -o <i>outfile</i> ]
<i>command</i> ...</pre>
<h2>Description</h2>
<p><code>rados</code> is a utility for interacting with a Ceph object storage cluster (RADOS), part of the Ceph distributed storage system.</p>
<h2>Options</h2>
<dl>
<dt><code>-p pool, &#8211;pool pool</code></p>
<dd>Interact with the given pool. Required by most commands.</p>
<dt><code>-s snap, &#8211;snap snap</code></p>
<dd>Read from the given pool snapshot. Valid for all pool-specific read operations.</p>
<dt><code>-i infile</code></p>
<dd>will specify an input file to be passed along as a payload with the command to the monitor cluster. This is only used for specific monitor commands.</p>
<dt><code>-o outfile</code></p>
<dd>will write any payload returned by the monitor cluster with its reply to outfile. Only specific monitor commands (e.g. osd getmap) return a payload.</p>
<dt><code>-c ceph.conf, &#8211;conf=ceph.conf</code></p>
<dd>Use ceph.conf configuration file instead of the default /etc/ceph/ceph.conf to determine monitor addresses during startup.</p>
<dt><code>-m monaddress[:port]</code></p>
<dd>Connect to specified monitor (instead of looking through ceph.conf).</dl>
<h2>Global Commands</h2>
<dl>
<dt><code>lspools</code></p>
<dd>List object pools</p>
<dt><code>df</code></p>
<dd>Show utilization statistics, including disk usage (bytes) and object counts, over the entire system and broken down by pool.</p>
<dt><code>mkpool</code> <i>foo</i></p>
<dd>Create a pool with name foo.</p>
<dt><code>rmpool</code> <i>foo</i> [ <i>foo</i> &#8211;yes-i-really-really-mean-it ]</p>
<dd>Delete the pool foo (and all its data)</dl>
<h2>Pool Specific Commands</h2>
<dl>
<dt><code>get</code> <i>name</i> <i>outfile</i></p>
<dd>Read object name from the cluster and write it to outfile.</p>
<dt><code>put</code> <i>name</i> <i>infile</i></p>
<dd>Write object name to the cluster with contents from infile.</p>
<dt><code>rm</code> <i>name</i></p>
<dd>Remove object name.</p>
<dt><code>ls</code> <i>outfile</i></p>
<dd>List objects in given pool and write to outfile.</p>
<dt><code>lssnap</code></p>
<dd>List snapshots for given pool.</p>
<dt><code>clonedata</code> <i>srcname</i> <i>dstname</i> &#8211;object-locator <i>key</i></p>
<dd>Clone object byte data from <i>srcname</i> to <i>dstname</i>. Both objects must be stored with the locator key <i>key</i> (usually either <i>srcname</i> or <i>dstname</i>). Object attributes and omap keys are not copied or cloned.</p>
<dt><code>mksnap</code> <i>foo</i></p>
<dd>Create pool snapshot named <i>foo</i>.</p>
<dt><code>rmsnap</code> <i>foo</i></p>
<dd>Remove pool snapshot named <i>foo</i>.</p>
<dt><code>bench</code> <i>seconds</i> <i>mode</i> [ -b <i>objsize</i> ] [ -t <i>threads</i> ]</p>
<dd>Benchmark for <i>seconds</i>. The mode can be <i>write</i>, <i>seq</i>, or <i>rand</i>. <i>seq</i> and <i>rand</i> are read benchmarks, either sequential or random. Before running one of the reading benchmarks, run a write benchmark with the <i>&#8211;no-cleanup</i> option. The default object size is 4 MB, and the default number of simulated threads (parallel writes) is 16. </p>
<p> <code>cleanup</code></p>
<dt><code>listomapkeys</code> <i>name</i></p>
<dd>List all the keys stored in the object map of object name.</p>
<dt><code>listomapvals</code> <i>name</i></p>
<dd>List all key/value pairs stored in the object map of object name. The values are dumped in hexadecimal.</p>
<dt><code>getomapval</code> <i>name</i> <i>key</i></p>
<dd>Dump the hexadecimal value of key in the object map of object name.</p>
<dt><code>setomapval</code> <i>name</i> <i>key</i> <i>value</i></p>
<dd>Set the value of key in the object map of object name.</p>
<dt><code>rmomapkey</code> <i>name</i> <i>key</i></p>
<dd>Remove key from the object map of object name.</p>
<dt><code>getomapheader</code> <i>name</i></p>
<dd>Dump the hexadecimal value of the object map header of object name.</p>
<dt><code>setomapheader</code> <i>name</i> <i>value</i></p>
<dd>Set the value of the object map header of object name.</dl>
<h2>Examples</h2>
<p>To view cluster utilization: </p>
<pre>rados df</pre>
<p>To get a list object in pool foo sent to stdout: </p>
<pre>rados -p foo ls -</pre>
<p>To write an object: </p>
<pre>rados -p foo put myobject blah.txt</pre>
<p>To create a snapshot: </p>
<pre>rados -p foo mksnap mysnap</pre>
<p>To delete the object: </p>
<pre>rados -p foo rm myobject</pre>
<p>To read a previously snapshotted version of an object: </p>
<pre>rados -p foo -s mysnap get myobject blah.txt.old</pre>
<h2>Availability</h2>
<p><code>rados</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
