---
title: "dc_client(1)"
name: "dc_client"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc_client/"
description: "dc_client – Distributed session cache client proxy"
---

<h2>NAME</h2>
<p> dc_client &#8211; Distributed session cache client proxy</p>
<h2>SYNOPSIS</h2>
<p> <code>dc_client</code> -server &lt;address&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>dc_client</code> runs a client proxy to provide access to a remote cache server (typically over TCP/IPv4) by providing a local service (typically over unix domain sockets). It starts listening on a configurable network address for connections and establishes a persistent connection to an instance of <code>dc_server</code> for proxying cache operations to. Incoming connections are expected to communicate using the <i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8) protocol, and would typically be applications using one of the distcache APIs in <i>libdistcache</i> to encapsulate these communications. </p>
<p> The common use of <code>dc_client</code> is to run as a local agent on each host machine that requires use of the distributed cache, as the listening address should probably use unix domain sockets which are better suited to frequent (and temporary) connections being used for individual cache operations. Likewise, the connection <code>dc_client</code> makes to the cache server (<code>dc_server</code>) for proxying cache operations is typically over a genuine network to remote machine, using TCP/IPv4.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-daemon</code></p>
<dd> After initialising, <code>dc_client</code> will detach from the parent process, close standard file-descriptors, etc. If this flag is not set, <code>dc_client</code> will run in the foreground. It is recommended to use this flag in combination with the <i>pidfile</i> flag to simplify stopping and restarting services.</p>
<dt><code>-user</code> user</p>
<dd> This switch will attempt to change user privileges of <code>dc_client</code> to the given user <font SIZE="-1">ID</font> after initialising its listening socket. On most systems, this can only work if <code>dc_client</code> is started as the <i>root</i> user. It is important to note that the change of user <font SIZE="-1">ID</font> occurs after the listening socket is created but before any attempts are made to connect to distcache servers. This ensures that the listening socket is created with the most restrictive permissions, and that the ability to connect to servers at run-time corresponds to the given user (rather than having unusual root permissions on startup).</p>
<dt><code>-listen</code> address</p>
<dd> Configures the address on which <code>dc_client</code> should listen for incoming connections. The syntax is that defined by the <i>libnal</i> <font SIZE="-1">API</font>. Though this can listen on any supported network transport, <code>dc_client</code> should be expected to receive a lot of short-lived (and frequest) connections, so unix domain sockets are generally preferable to TCP/IPv4. Eg. </p>
<pre>
    # Listen on a unix domain socket in the /tmp directory
    dc_client -listen UNIX:/tmp/cacheclient
</pre>
<p> The default value for this flag is: UNIX:/tmp/scache</p>
<dt><code>-sockowner</code> user</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change ownership of the created socket file.</p>
<dt><code>-sockgroup</code> group</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change group ownership of the created socket file.</p>
<dt><code>-sockperms</code> perms</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change file permissions for the created socket file, and is specified in the standard octal notation used for unix file permissions. Eg. to start dc_client to run as the <i>nobody</i> user, listening on a unix domain socket that can only be connected to by the <i>root</i> user or members of the <i>ssl</i> group; </p>
<pre>
    # dc_client -listen UNIX:/tmp/cacheclient -user nobody \
          -sockgroup ssl -sockperms 440
</pre>
<dt><code>-server</code> address</p>
<dd>
<dt><code>-connect</code> address</p>
<dd> These flags are identical, and specify the address of the cache server <code>dc_client</code> should connect to. Cache operations requested by clients of <code>dc_client</code> (using short-lived local connections to the service address specified by <code>-listen</code>) are multiplexed to/from the cache server over this persistent connection. The syntax is that defined by the <i>libnal</i> <font SIZE="-1">API</font> and would typically be over TCP/IPv4, particularly if the cache server is running on a remote machine. Eg. </p>
<pre>
    # Connect to a remote cache server listening on port 9001
    dc_client -listen UNIX:/tmp/cacheclient \
              -server IP:cacheserver.localnet:9001
</pre>
<dt><code>-retry</code> msecs</p>
<dd> Distcache is designed to be as fault-tolerant as possible, and part of this approach is to have <code>dc_client</code> manage the possible disappearance and subsequent reappearance of the remote instance of <code>dc_server</code> it proxies to. In actuality, this could happen for a variety of reasons including the cache server being restarted, or a network error at any point in between the two programs. During any period in which <code>dc_client</code> has lost communications with the cache server, any/all local connections and corresponding cache operation requests will be responded to directly by <code>dc_client</code> itself. The consequence is that cache operations return as failures during this time, so the application requesting the operations must make do without (eg. in <font SIZE="-1">SSL/TLS</font> session caching, this means that attempts to resume <font SIZE="-1">SSL/TLS</font> sessions fail and so full handshakes are required). </p>
<p> The default behaviour of <code>dc_client</code> when losing communications with the instance of <code>dc_server</code> (as specified by <code>-server</code> or <code>-connect</code>) is to try to reestablish communications every 5 seconds. This flag allows the retry period to be configured to any number of milliseconds. Note: confusing milliseconds with seconds can cause emotional disturbance and should be avoided at all costs.</p>
<dt><code>-idle</code> msecs</p>
<dd> Normal behaviour with <code>dc_client</code> is to have its clients (applications using <a href="/docs/linux/man/8-distcache/">distcache</a><code>(8)</code> APIs for communication) use temporary connections for each cache operation. However, there are modes of operation in those APIs that allow persistent connections to be used together with various associated options. This is especially important for any platforms that (for whatever reason) can&#8217;t use unix domain sockets and don&#8217;t want to bloat file-descriptor tables with IPv4 sockets sitting in <font SIZE="-1">TIME_WAIT</font> state. For this reason, as well as resilience against client applications that hang, it useful to configure <code>dc_client</code> to automatically drop client connections that have been idle for some configurable period of time. </p>
<p> This flag specifies the period of idle time after which client connections will be dropped, and is in units of milliseconds and <code>not</code> seconds. The default value is zero, and this means that client connections are never intentionally dropped. </p>
<p> Note, provided client applications are appropriately configured they need not necessarily be vulnerable to race conditions when <code>dc_client</code> configures this flag. The <a href="/docs/linux/man/8-distcache/">distcache</a><code>(8)</code> <i></i><font SIZE="-1"><i>DC_CTX</i></font><i></i> <font SIZE="-1">API</font> provides additional persistence options such as <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2)-checking and resistance against idle timeouts. Ie. if a request is commenced on a client connection that is in the process of being timed-out by <code>dc_client</code>, the <i></i><font SIZE="-1"><i>DC_CTX</i></font><i></i> will allow one retry with an immediate re-connection before considering the operation to have failed.</p>
<dt><code>-pidfile</code> path</p>
<dd> This is a standard flag for many programs, and most useful in combination with <code>-daemon</code>. When <code>-pidfile</code> is specified <code>dc_client</code> will write its process <font SIZE="-1">ID</font> to a file at the specified path upon successful initialisation. To use this path file to later kill the running <code>dc_client</code> instance, use something like (where <code>pidfile.pid</code> is whatever <code>path</code> was); </p>
<pre>
    kill `cat pidfile.pid`
</pre>
<dt><code>-h</code>, <code>-help</code>, <code>-?</code></p>
<dd> Any of these flags will cause <code>dc_client</code> to display a brief usage summary to the console and exit cleanly. Any other flags are ignored.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-dc_server/">dc_server</a></i>(1)</p>
<dd> Distributed cache server.</p>
<dt><i><a href="/docs/linux/man/1-dc_snoop/">dc_snoop</a></i>(1)</p>
<dd> Distcache protocol analyser and debugging tool.</p>
<dt><i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8)</p>
<dd> Overview of the distcache architecture.</p>
<dt><i><a rel="nofollow" href="http://www.distcache.org/">http://www.distcache.org/</a></i></p>
<dd> Distcache home page.</dl>
<h2>AUTHOR</h2>
<p> This toolkit was designed and implemented by Geoff Thorpe for Cryptographic Appliances Incorporated. Since the project was released into open source, it has a home page and a project environment where development, mailing lists, and releases are organised. For problems with the software or this man page please check for new releases at the project web-site below, mail the users mailing list described there, or contact the author at <i>geoff [at] geoffthorpe.net</i>. </p>
<p> Home Page: <i><a rel="nofollow" href="http://www.distcache.org">http://www.distcache.org</a></i> </p>
<h2>Index</h2>
