---
title: "dc_server(1)"
name: "dc_server"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc_server/"
description: "dc_server – Distributed session cache server"
---

<h2>NAME</h2>
<p> dc_server &#8211; Distributed session cache server</p>
<h2>SYNOPSIS</h2>
<p> <code>dc_server</code> -listen &lt;address&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>dc_server</code> runs a cache server and starts listening on a configurable network address for connections. Incoming connections are expected to communicate using the <i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8) protocol, and would typically be instances of <i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1) running on other machines.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-daemon</code></p>
<dd> After initialising, <code>dc_server</code> will detach from the parent process, close standard file-descriptors, etc. If this flag is not set, <code>dc_server</code> will run in the foreground. It is recommended to use this flag in combination with the <i>pidfile</i> flag to simplify stopping and restarting services.</p>
<dt><code>-user</code> user</p>
<dd> This switch will attempt to change user privileges of <code>dc_server</code> to the given user <font SIZE="-1">ID</font> after initialising its listening socket. On most systems, this can only work if <code>dc_server</code> is started as the <i>root</i> user. It is important to note that the change of user <font SIZE="-1">ID</font> occurs after the listening socket is create. This ensures that the listening socket is created with the most restrictive permissions, and that the ability to connect to servers at run-time corresponds to the given user (rather than having unusual root permissions on startup).</p>
<dt><code>-listen</code> address</p>
<dd> Configures the address on which <code>dc_server</code> should listen for incoming connections. The syntax is that defined by the <i>libnal</i> <font SIZE="-1">API</font>. Some examples follow; </p>
<pre>
    # Listen on port 9001 for all TCP/IPv4 interfaces
    dc_server -listen IP:9001
</pre>
<pre>
    # Listen on port 9001 on a specific TCP/IPv4 interface
    dc_server -listen IP:192.168.0.1:9001
    dc_server -listen IP:cacheserver.localnet:9001
</pre>
<pre>
    # Listen on a unix domain socket in the /tmp directory
    dc_server -listen UNIX:/tmp/cacheserver
</pre>
<dt><code>-sockowner</code> user</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change ownership of the created socket file.</p>
<dt><code>-sockgroup</code> group</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change group ownership of the created socket file.</p>
<dt><code>-sockperms</code> perms</p>
<dd> This switch is only useful when listening (see <code>-listen</code>) on unix domain sockets. It will attempt to change file permissions for the created socket file, and is specified in the standard octal notation used for unix file permissions. Eg. to start dc_server to run as the <i>nobody</i> user, listening on a unix domain socket that can only be connected to by the <i>root</i> user or members of the <i>dcclient</i> group; </p>
<pre>
    # dc_server -listen UNIX:/tmp/cacheserver -user nobody \
          -sockgroup dcclient -sockperms 440
</pre>
<dt><code>-sessions</code> num</p>
<dd> Specifies a maximum number of sessions that should be stored in the cache. All sessions in a cache have an expiry time so that they will, if they have not been forcibly removed before that time, be expired out of the cache. If it is desirable to allow long session timeouts under normal situations yet protect against the session cache growing without limit periods of high-load, this limit can provide the required balance. If the session cache reaches this limit, it will automatically rotate out those sessions in the cache that are due to expire soonest. It is not (yet) possible to have no limit at all, though a future version should support this by allowing the user to specify zero. </p>
<p> The default value for this flag is 512.</p>
<dt><code>-progress</code> num</p>
<dd> <code>dc_server</code> will, by default, log a line of output to stdout whenever there is cache activity, but will make sure to do so no more often than once a second. If <code>-progress</code> is specified, this will take precedence so that output will be emitted whenever <code>num</code> operations have occurred since the last output, irrespective of how little time has elapsed. The once-a-second logic remains behind this, so that if less than <code>num</code> operations has taken place but at least one second has passed, output will still be logged. This flag has no effect if <code>-daemon</code> is used.</p>
<dt><code>-pidfile</code> path</p>
<dd> This is a standard flag for many programs, and most useful in combination with <code>-daemon</code>. When <code>-pidfile</code> is specified <code>dc_server</code> will write its process <font SIZE="-1">ID</font> to a file at the specified path upon successful initialisation. To use this path file to later kill the running <code>dc_server</code> instance, use something like (where <code>pidfile.pid</code> is whatever <code>path</code> was); </p>
<pre>
    kill `cat pidfile.pid`
</pre>
<dt><code>-killable</code></p>
<dd> The default behaviour of <code>dc_server</code> is to silently ignore <font SIZE="-1">SIGUSR1</font> and <font SIZE="-1">SIGUSR2</font> signals, but with this switch enabled it will handle these signals and close down cleanly (mainly useful for developers as an alternative to <font SIZE="-1">SIGKILL</font> which is less useful for debugging memory leaks).</p>
<dt><code>-h</code>, <code>-help</code>, <code>-?</code></p>
<dd> Any of these flags will cause <code>dc_server</code> to display a brief usage summary to the console and exit cleanly. Any other flags are ignored.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1)</p>
<dd> Distributed caching client proxy.</p>
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
