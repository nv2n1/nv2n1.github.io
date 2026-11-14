---
title: "socket_wrapper(1)"
name: "socket_wrapper"
section: "1"
letter: "s"
url: "/docs/linux/man/1-socket_wrapper/"
description: "socket_wrapper – A library passing all socket communications through unix sockets."
---

<h2 class="name">NAME</h2>
<p> socket_wrapper &#8211; A library passing all socket communications through unix sockets. </p>
<h2>SYNOPSIS</h2>
<p> LD_PRELOAD=libsocket_wrapper.so SOCKET_WRAPPER_DIR=/tmp/tmp.bQRELqDrhM SOCKET_WRAPPER_DEFAULT_IFACE=10 <code>./myapplication</code></p>
<h2>DESCRIPTION</h2>
<p> socket_wrapper aims to help client/server software development teams willing to gain full functional test coverage. It makes possible to run several instances of the full software stack on the same machine and perform locally functional testing of complex network configurations. </p>
<dl>
<dt>
<dd> &bull; Redirects all network communication to happen over unix sockets.</dl>
<dl>
<dt>
<dd> &bull; Support for IPv4 and IPv6 socket and addressing emulation.</dl>
<dl>
<dt>
<dd> &bull; Ablility to capture network traffic in pcap format.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>SOCKET_WRAPPER_DIR</code></p>
<dl>
<dt>
<dd> The user defines a directory where to put all the unix sockets using the envionment variable &quot;SOCKET_WRAPPER_DIR=/path/to/socket_dir&quot;. When a server opens a port or a client wants to connect, socket_wrapper will translate IP addresses to a special socket_wrapper name and look for the relevant unix socket in the SOCKET_WRAPPER_DIR.</dl>
<p> <code>SOCKET_WRAPPER_DEFAULT_IFACE</code></p>
<dl>
<dt>
<dd> Additionally, the default interface to be used by an application is defined with &quot;SOCKET_WRAPPER_DEFAULT_IFACE=&lt;ID&gt;&quot; where &lt;ID&gt; is between 2 and 254. This is analogous to use the IPv4 addresses &quot;127.0.0.&lt;ID&gt;&quot; or IPv6 addresses &quot;fd00::5357:5f&lt;IDx&gt;&quot; (where &lt;IDx&gt; is a hexadecimal presentation of &lt;ID&gt;). You should always set the default interface. If you listen on INADDR_ANY then it will use the default interface to listen on.</dl>
<p> <code>SOCKET_WRAPPER_PCAP_FILE</code></p>
<dl>
<dt>
<dd> When debugging, it is often interesting to investigate the network traffic between the client and server within your application. If you define SOCKET_WRAPPER_PCAP_FILE=/path/to/file.pcap, socket_wrapper will dump all your network traffic to the specified file. After the test has been finished you&#8217;re able to open the file for example with Wireshark.</dl>
<p> <code>SOCKET_WRAPPER_MTU</code></p>
<dl>
<dt>
<dd> With this variable you can change the MTU size. However we do not recomment to do that as the default size of 1500 byte is best for formatting PCAP files.</dl>
<p> The minimum value you can set is 512 and the maximum 32768. </p>
<p> <code>SOCKET_WRAPPER_DEBUGLEVEL</code></p>
<dl>
<dt>
<dd> If you need to see what is going on in socket_wrapper itself or try to find a bug, you can enable logging support in socket_wrapper if you built it with debug symbols. </p>
<dl>
<dt>
<dd> &bull; 0 = ERROR</dl>
<dl>
<dt>
<dd> &bull; 1 = WARNING</dl>
<dl>
<dt>
<dd> &bull; 2 = DEBUG</dl>
<dl>
<dt>
<dd> &bull; 3 = TRACE</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
# Open a console and create a directory for the unix sockets.
$ mktemp -d
/tmp/tmp.bQRELqDrhM
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Then start nc to listen for network traffic using the temporary directory.
$ LD_PRELOAD=libsocket_wrapper.so \
  SOCKET_WRAPPER_DIR=/tmp/tmp.bQRELqDrhM \
  SOCKET_WRAPPER_DEFAULT_IFACE=10 nc -v -l 127.0.0.10 7
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# (If nc, listens on 0.0.0.0 then listener will be open on 127.0.0.10 because
#  it is the default interface)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Now open another console and start 'nc' as a client to connect to the server:
$ LD_PRELOAD=libsocket_wrapper.so \
  SOCKET_WRAPPER_DIR=/tmp/tmp.bQRELqDrhM \
  SOCKET_WRAPPER_DEFAULT_IFACE=100 nc -v 127.0.0.10 7
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# (The client will use the address 127.0.0.100 when connecting to the server)
# Now you can type 'Hello!' which will be sent to the server and should appear
# in the console output of the server.
</pre>
</dl>
<h2>Index</h2>
