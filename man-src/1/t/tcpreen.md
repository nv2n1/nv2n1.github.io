---
title: "tcpreen(1)"
name: "tcpreen"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcpreen/"
description: "tcpreen – TCP stream monitoring tool"
---

<h2>NAME</h2>
<p> tcpreen &#8211; TCP stream monitoring tool</p>
<h2>SYNOPSIS</h2>
<p> <code>tcpreen</code> [<code>-cdflnqv</code>] [<code>-b maxbytes</code>] [ <code>-f format</code>] [<code>-F maxclients</code>] [<code>-m maxconnect</code>] [ <code>-o logfile</code>] [<code>-u user</code>] [<code>-a bindaddress</code>] [ <code>-s servername</code>] [<code>-p proto1/proto2</code>] serverport [localport] </p>
<h2>DESCRIPTON</h2>
<p> <code>TCPreen</code> monitors and let the user analyse data transmitted between clients and servers via TCP connections. It focuses on the data stream and operates at the software layer, not on lower level transmission protocols as a packet sniffers do. </p>
<p> It works like a bridge between a server and clients that communicates through TCP sessions, and can display or save data that is sent either way. </p>
<p> In standard mode, <code>TCPreen</code> opens a listening socket (on port <code>localport</code> which is dynamically allocated by default), and waits until a client connects to it. Then, it connects to the server (on port <code>serverport</code>) and forwards data between each hosts until the session is closed by either side. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a interface</code>, <code>&#8211;accept interface</code> or <code>&#8211;bind interface</code></p>
<dd> Specify an interface that will be used to listen for client connections. By default, all network interfaces are used. </p>
<dt><code>-b bytecount</code> or <code>&#8211;bytes bytecount</code></p>
<dd> Limit the length of a TCP session to <code>bytecount</code> bytes. If a session exceeds this quantity, it will be closed on the next data packet boundary. </p>
<dt><code>-c</code> or <code>&#8211;connect</code></p>
<dd> Connect to the specified client instead of waiting for the client to connect. This is meant for expert users who know what they are doing only. If no hostname is specified, TCPreen will try to connect to the local host. </p>
<p> Use <code>-a address</code> to specify the client address to connect to. </p>
<dt><code>-d</code> or <code>&#8211;daemon</code></p>
<dd> Turn on <i>daemon mode</i>. When this option is selected, <code>TCPreen</code> will run in the background and send informations to <code>syslog</code> instead of the console. This enables <i>quiet mode</i> and <i>multiple clients mode</i> automatically. </p>
<p> You will probably want to use option -F as well. </p>
<p> <code>NOTE</code>: if you turn this feature on, log files will be created from the <code>root</code> directory, not from the current one. See <i><a href="/docs/linux/man/3-daemon/">daemon</a></i>(3) for more details. </p>
<dt><code>-f logformat</code> or <code>&#8211;format logformat</code></p>
<dd> Selects a format for output. Supported formats includes: <code>C</code> (C source strings-like encoding), <code>hex</code> (hexadecimal data dump), <code>count</code> (write quantities of data), <code>null</code> (only displays new connections addresses), <code>password</code> (basic password capture, unfinished yet), <code>raw</code> (write data as is, even if it is not 7-bit clean), <code>strip</code> (replace non printable characters with dots). </p>
<dt><code>-F nproc</code> or <code>&#8211;fork nproc</code></p>
<dd> Specifies the maximum number of sessions that can be treated at the same time. By default, only one session is allowed at a time not so as to keep the program output easy to read. </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display some help and exit. </p>
<dt><code>-l</code> or <code>&#8211;listen</code></p>
<dd> Listen for the &quot;server&quot; instead of connecting to it. This can be used by advanced users to run a human brain-powered server by telnet-ing to <code>TCPreen server</code> address. An optionnal listening interface address can be specified. </p>
<dt><code>-m conn_num</code> or <code>&#8211;maxconn conn_num</code></p>
<dd> Handle <code>conn_num</code> consecutive client connections before exiting. When this option is not used, the program will run forever (until interrupted). </p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd> Disable reverse DNS lookup and service name resolution. Node names and port numbers will appear in numeric form. This option will speed up connections a little. </p>
<dt><code>-o logfile</code> or <code>&#8211;output logfile</code></p>
<dd> Save data to file <code>logfile</code>. If it already exists, it will be overwritten. &quot;-&quot; is used for <i>stdout</i>. </p>
<p> Multiple log files can be used (with different formats). For example: </p>
<p> tcpreen -f hex -o hexafile.log -f C -o file.log smtp </p>
<p> will save <i>hexafile.log</i> in hexadecimal and <i>file.log</i> in C encoding. </p>
<dt><code>-p</code> or <code>&#8211;protocol</code></p>
<dd> Specifies which network protocol(s) is/are going to be used. If a single protocol name is specified, it will be used both ways. Two different protocols can be used on each side by separating them with a slash like this: &#8216;tcp/tcp6&#8217;. The first protocol will then be used to communicate with the server, the last one will be used to exchange data with the client. </p>
<p> The following protocols are currently recognized: <code>tcp</code> (TCP over IPv4), <code>tcp6</code> (TCP over IPv6) and <code>unix</code> or <code>local</code> (Unix interprocess streams). By default, <code>tcp</code> is used. </p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd> Turn on <i>quiet mode</i>: Do not write anything on the standard output (<i>stdout</i>). </p>
<dt><code>-s hostname</code> or <code>&#8211;server hostname</code></p>
<dd> Connect to the specified server instead of the local host which is used by default. </p>
<dt><code>-u user</code> or <code>&#8211;user user</code></p>
<dd> When run as super-user, drop privilege and set UID to that of <code>user</code> (it must be a valid username). That is highly recommended if <code>tcpreen</code> is to be bound to a reserved port, which only root can bind on Unix systems. </p>
<p> You must be root to use this option. </p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd> Increase program verbosity. This can be cumulated. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd> Display program version and license and exit. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> These are common problems: </p>
<p> Nothing happens:</p>
<dl>
<dt>
<dd> The client is communicating with the server correctly, but TCPreen stays quiet. Make sure you told the client to connect to TCPreen address rather than the actual server address. </p>
<p> Make sure you have enabled verbose mode. </p>
</dl>
<p> Strange port names:</p>
<dl>
<dt>
<dd> Have a look at <i>/etc/services</i> and you will realize what this means. Alternatively, you may want to use <code>-n</code>. </p>
</dl>
<h2>SECURITY</h2>
<p> <code>tcpreen</code> requires <i>root</i> privileges to be bound to a reserved TCP port (under 1024). If you really need to do so, you may run <code>tcpreen</code> Set-UID <i>root</i>. In such circumstances, you must ensure that only trustworthy users can run <code>tcpreen</code>, as it could be used to divert traffic to <code>any</code> reserved ports on the system. </p>
<p> <code>tcpreen</code> will automatically drop privileges as soon as it has allocated its listening socket(s) to limit exposure. Log files are always created with the default permission of the current user. </p>
<p> Care should be taken when using <code>tcpreen</code> as it could be used to access your network or system from the outside (that is why it will normally refuse to run as root). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nc/">nc</a>(1), <a href="/docs/linux/man/1-nc6/">nc6</a>(1), <a href="/docs/linux/man/1-tcpflow/">tcpflow</a>(1), <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8), <a href="/docs/linux/man/1-tethereal/">tethereal</a>(1) </p>
<h2>AUTHOR</h2>
<p> Remi Denis-Courmont &lt;rdenis at simphalempin.com&gt; </p>
<p> $Id: tcpreen.1 178 2006-03-18 18:10:23Z remi $ </p>
<p> <a rel="nofollow" href="http://www.simphalempin.com/dev/tcpreen/">http://www.simphalempin.com/dev/tcpreen/</a> </p>
<h2>Index</h2>
