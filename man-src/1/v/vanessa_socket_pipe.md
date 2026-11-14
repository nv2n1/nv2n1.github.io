---
title: "vanessa_socket_pipe(1)"
name: "vanessa_socket_pipe"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vanessa_socket_pipe/"
description: "vanessa_socket_pipe – Trivial TCP/IP pipe based on libvanessa_socket"
---

<h2>NAME</h2>
<p> vanessa_socket_pipe &#8211; Trivial TCP/IP pipe based on libvanessa_socket</p>
<h2>SYNOPSIS</h2>
<p> <code>vanessa_socket_pipe</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> A TCP/IP pipe is a user space programme that listens for TCP/IP connections on port on the local host and when a client connects makes a connection to a TCP port, possibly on another host. Once both connections are established data sent on one connection is relayed to the other, hence forming a bi-directional pipe. </p>
<p> Uses include enabling connections to specific ports on hosts behind a packet filter. </p>
<p> This code is intended primarily as an example of how many of the features of libvanessa_socket work.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c|&#8211;connection_limit:</code></p>
<dd> Maximum number of connections to accept simultaneously. A value of zero sets no limit on the number of simultaneous connections. (default 0)</p>
<dt><code>-d|&#8211;debug:</code></p>
<dd> Turn on verbose debuging to stderr.</p>
<dt><code>-h|&#8211;help:</code></p>
<dd> Display this message.</p>
<dt><code>-L|&#8211;listen_port:</code></p>
<dd> Port to listen on. (mandatory)</p>
<dt><code>-l|&#8211;listen_host:</code></p>
<dd> Address to listen on. May be a hostname or an IP address. If not defined then listen on all local addresses.</p>
<dt><code>-n|&#8211;no_lookup:</code></p>
<dd> Turn off lookup of hostnames and portnames. That is, hosts must be given as IP addresses and ports must be given as numbers.</p>
<dt><code>-O|&#8211;outgoing_port: </code></p>
<dd> Define a port to connect to. If not specified -l|&#8211;listen_port will be used.</p>
<dt><code>-o|&#8211;outgoing_host: </code></p>
<dd> Define host to connect to. May be a hostname or an IP address. (mandatory)</p>
<dt><code>-q|&#8211;quiet:</code></p>
<dd> Only log errors. Overriden by -d|&#8211;debug.</p>
<dt><code>-t|&#8211;timeout: </code></p>
<dd> Idle timeout in seconds. Value of zero sets infinite timeout. (default 1800)</p>
<dt><code>Notes: </code></p>
<dd> Default value for binary flags is off.<br />
 -L|&#8211;listen_port and -o|&#8211;outgoing_host must be defined.</dl>
<h2>AUTHOR</h2>
<p> Simon Horman &lt;horms [at] verge.net.au&gt; </p>
<h2>Index</h2>
