---
title: "dc_snoop(1)"
name: "dc_snoop"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc_snoop/"
description: "dc_snoop – Distributed session cache traffic analysis"
---

<h2>NAME</h2>
<p> dc_snoop &#8211; Distributed session cache traffic analysis</p>
<h2>SYNOPSIS</h2>
<p> <code>dc_snoop</code> -listen &lt;address&gt; -server &lt;address&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>dc_snoop</code> runs as a transparent proxy supporting the <i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8) protocol and (in theory) should work when inserted between any compliant tools. Ie. this can be used to monitor cache operation requests and responses between applications and <code>dc_client</code>, or between <code>dc_client</code> and <code>dc_server</code>. </p>
<p> This tool is still in early stages of development and is provided very much &#8220;as-is&#8221;. It is intended to be used by developers with access to the source code &#8211; for now, most configurable behaviour of <code>dc_snoop</code> is set in source code and can not be manipulated on the command-line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-listen</code> address</p>
<dd> Configures the address on which <code>dc_snoop</code> should listen for incoming connections. The syntax is that defined by the <i>libnal</i> <font SIZE="-1">API</font>.</p>
<dt><code>-server</code> address</p>
<dd>
<dt><code>-connect</code> address</p>
<dd> These flags are identical, and specify the address <code>dc_snoop</code> should transparently proxy all incoming connections to. For each connection accepted by <code>dc_snoop</code> (on the address specified by <code>-listen</code>) a corresponding connection is opened to the address specified by these flags. When either connection is closed, <code>dc_snoop</code> will correspondingly close the other connection.</p>
<dt><code>-h</code>, <code>-help</code>, <code>-?</code></p>
<dd> Any of these flags will cause <code>dc_snoop</code> to display a brief usage summary to the console and exit cleanly. Any other flags are ignored.</dl>
<h2>EXAMPLES</h2>
<p> This example demonstrates the use of <code>dc_snoop</code> to monitor communications between an instance of <code>dc_client</code> and <code>dc_server</code> both running on the same machine using only unix domain sockets. Suppose the tools are started and tested using the following commands; </p>
<pre>
    # Start services
    dc_server -daemon -listen UNIX:/tmp/cacheserver
    dc_client -deamon -listen UNIX:/tmp/cacheclient \
              -server UNIX:/tmp/cacheserver
    # Run some tests
    dc_test -connect UNIX:/tmp/cacheclient
</pre>
<p> The following modification should be functionally equivalent (ignoring the additional latency and overhead of <code>dc_snoop</code>&#8216;s involvement) and should generate a log file of all cache transactions to <i>logfile</i>. Note the change to the <code>-server</code> flag in <code>dc_client</code>; </p>
<pre>
    # Start services
    dc_server -daemon -listen UNIX:/tmp/cacheserver
    dc_client -deamon -listen UNIX:/tmp/cacheclient \
              -server UNIX:/tmp/cachesnoop
    # Start dc_snoop logging to logfile in the background
    dc_snoop -listen UNIX:/tmp/cachesnoop \
             -server UNIX:/tmp/cacheserver &gt; logfile &amp;
    # Run some tests
    dc_test -connect UNIX:/tmp/cacheclient
</pre>
<h2>BUGS</h2>
<p> This program is incomplete and not at all configurable on the command-line.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1)</p>
<dd> Distributed caching client proxy.</p>
<dt><i><a href="/docs/linux/man/1-dc_server/">dc_server</a></i>(1)</p>
<dd> Distributed cache server.</p>
<dt><i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8)</p>
<dd> Overview of the distcache architecture.</p>
<dt><i><a rel="nofollow" href="http://www.distcache.org/">http://www.distcache.org/</a></i></p>
<dd> Distcache home page.</dl>
<h2>AUTHOR</h2>
<p> This toolkit was designed and implemented by Geoff Thorpe for Cryptographic Appliances Incorporated. Since the project was released into open source, it has a home page and a project environment where development, mailing lists, and releases are organised. For problems with the software or this man page please check for new releases at the project web-site below, mail the users mailing list described there, or contact the author at <i>geoff [at] geoffthorpe.net</i>. </p>
<p> Home Page: <i><a rel="nofollow" href="http://www.distcache.org">http://www.distcache.org</a></i> </p>
<h2>Index</h2>
