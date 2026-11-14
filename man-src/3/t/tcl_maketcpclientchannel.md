---
title: "tcl_maketcpclientchannel(3)"
name: "tcl_maketcpclientchannel"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_maketcpclientchannel/"
description: "Tcl_OpenTcpClient, Tcl_MakeTcpClientChannel, Tcl_OpenTcpServer – procedures to open channels using TCP sockets"
---

<p>Tcl_OpenTcpClient, Tcl_MakeTcpClientChannel, Tcl_OpenTcpServer &#8211; procedures to open channels using TCP sockets </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt; </code>
Tcl_Channel
<code>Tcl_OpenTcpClient</code>(<i>interp, port, host, myaddr, myport, async</i>)
Tcl_Channel
<code>Tcl_MakeTcpClientChannel</code>(<i>sock</i>)
Tcl_Channel
<code>Tcl_OpenTcpServer</code>(<i>interp, port, myaddr, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter to use for error reporting. If non-NULL and an error occurs, an error message is left in the interpreter&#8217;s result.</p>
<dd>int <i>port</i> (in) A port number to connect to as a client or to listen on as a server.</p>
<dd>const char <i>*host</i> (in) A string specifying a host name or address for the remote end of the connection.</p>
<dd>int <i>myport</i> (in) A port number for the client&#8217;s end of the socket. If 0, a port number is allocated at random.</p>
<dd>const char <i>*myaddr</i> (in) A string specifying the host name or address for network interface to use for the local end of the connection. If NULL, a default interface is chosen.</p>
<dd>int <i>async</i> (in) If nonzero, the client socket is connected asynchronously to the server.</p>
<dd>ClientData <i>sock</i> (in) Platform-specific handle for client TCP socket.</p>
<dd>Tcl_TcpAcceptProc <i>*proc</i> (in) Pointer to a procedure to invoke each time a new connection is accepted via the socket.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p>These functions are convenience procedures for creating channels that communicate over TCP sockets. The operations on a channel are described in the manual entry for <code>Tcl_OpenFileChannel</code>. </p>
<h2>Tcl_Opentcpclient</h2>
<p><code>Tcl_OpenTcpClient</code> opens a client TCP socket connected to a <i>port</i> on a specific <i>host</i>, and returns a channel that can be used to communicate with the server. The host to connect to can be specified either as a domain name style name (e.g. <code><a rel="nofollow" href="http://www.sunlabs.com">www.sunlabs.com</a></code>), or as a string containing the alphanumeric representation of its four-byte address (e.g. <code>127.0.0.1</code>). Use the string <code>localhost</code> to connect to a TCP socket on the host on which the function is invoked. </p>
<p> The <i>myaddr</i> and <i>myport</i> arguments allow a client to specify an address for the local end of the connection. If <i>myaddr</i> is NULL, then an interface is chosen automatically by the operating system. If <i>myport</i> is 0, then a port number is chosen at random by the operating system. </p>
<p> If <i>async</i> is zero, the call to <code>Tcl_OpenTcpClient</code> returns only after the client socket has either successfully connected to the server, or the attempted connection has failed. If <i>async</i> is nonzero the socket is connected asynchronously and the returned channel may not yet be connected to the server when the call to <code>Tcl_OpenTcpClient</code> returns. If the channel is in blocking mode and an input or output operation is done on the channel before the connection is completed or fails, that operation will wait until the connection either completes successfully or fails. If the channel is in nonblocking mode, the input or output operation will return immediately and a subsequent call to <code>Tcl_InputBlocked</code> on the channel will return nonzero. </p>
<p> The returned channel is opened for reading and writing. If an error occurs in opening the socket, <code>Tcl_OpenTcpClient</code> returns NULL and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. In addition, if <i>interp</i> is non-NULL, an error message is left in the interpreter&#8217;s result. </p>
<p> The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Tcl_Maketcpclientchannel</h2>
<p><code>Tcl_MakeTcpClientChannel</code> creates a <code>Tcl_Channel</code> around an existing, platform specific, handle for a client TCP socket. </p>
<p> The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Tcl_Opentcpserver</h2>
<p><code>Tcl_OpenTcpServer</code> opens a TCP socket on the local host on a specified <i>port</i> and uses the Tcl event mechanism to accept requests from clients to connect to it. The <i>myaddr</i> argument specifies the network interface. If <i>myaddr</i> is NULL the special address INADDR_ANY should be used to allow connections from any network interface. Each time a client connects to this socket, Tcl creates a channel for the new connection and invokes <i>proc</i> with information about the channel. <i>Proc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_TcpAcceptProc(
 ClientData <i>clientData</i>,
 Tcl_Channel <i>channel</i>,
 char *<i>hostName</i>,
 int <i>port</i>);</pre>
</dl>
<p> The <i>clientData</i> argument will be the same as the <i>clientData</i> argument to <code>Tcl_OpenTcpServer</code>, <i>channel</i> will be the handle for the new channel, <i>hostName</i> points to a string containing the name of the client host making the connection, and <i>port</i> will contain the client&#8217;s port number. The new channel is opened for both input and output. If <i>proc</i> raises an error, the connection is closed automatically. <i>Proc</i> has no return value, but if it wishes to reject the connection it can close <i>channel</i>. </p>
<p> <code>Tcl_OpenTcpServer</code> normally returns a pointer to a channel representing the server socket. If an error occurs, <code>Tcl_OpenTcpServer</code> returns NULL and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. In addition, if the interpreter is non-NULL, an error message is left in the interpreter&#8217;s result. </p>
<p> The channel returned by <code>Tcl_OpenTcpServer</code> cannot be used for either input or output. It is simply a handle for the socket used to accept connections. The caller can close the channel to shut down the server and disallow further connections from new clients. </p>
<p> TCP server channels operate correctly only in applications that dispatch events through <code>Tcl_DoOneEvent</code> or through Tcl commands such as <code>vwait</code>; otherwise Tcl will never notice that a connection request from a remote client is pending. </p>
<p> The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Platform Issues</h2>
<p>On Unix platforms, the socket handle is a Unix file descriptor as returned by the <code>socket</code> system call. On the Windows platform, the socket handle is a <code>SOCKET</code> as defined in the WinSock API. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_openfilechannel/">Tcl_OpenFileChannel</a>(3), <a href="/docs/linux/man/3-tcl_registerchannel/">Tcl_RegisterChannel</a>(3), <a href="/docs/linux/man/n-vwait/">vwait</a>(n) </p>
<h2>Keywords</h2>
<p>client, server, TCP</p>
