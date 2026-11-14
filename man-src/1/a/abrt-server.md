---
title: "abrt-server(1)"
name: "abrt-server"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-server/"
---

<h2 class="name">NAME</h2>
 

 abrt-server - Unix socket for ABRT. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-server</i> [-u UID] [-spv[v]...]

<h2>DESCRIPTION</h2>

 

 <i>abrt-server</i> is executed by abrtd daemon to handle socket connections. Every application in system is able to invoke creation of a new problem directory by following the communication protocol (described below in section <i>PROTOCOL</i>).

<h2>OPTIONS</h2>

 

 -u UID
<dl>
<dt>
<dd> Use UID as client uid</dl>
 

 -s
<dl>
<dt>
<dd> Log to system log.</dl>
 

 -p
<dl>
<dt>
<dd> Add program names to log.</dl>
 

 -v
<dl>
<dt>
<dd> Log more detailed debugging information.</dl>

<h2>PROTOCOL</h2>

 

 Initializing new dump: connect to UNIX domain socket /var/run/abrt.socket 

 Providing data (writting data to the socket): 

<dl>
<dt>
<dd> <pre><code>
-&gt;"POST / HTTP/1.1\r\n"
    -&gt;"\r\n"
    -&gt;"type=string\0" string,
    maximum length 100 bytes
        -&gt;"reason=string\0" string,
    maximum length 512 bytes
        -&gt;"pid=number\0" number,
    0 - PID_MAX(/ proc / sys / kernel / pid_max)
            -&gt;"executable=string\0" string,
    maximum length ~MAX_PATH
        -&gt;"backtrace=string\0" string,
    maximum length 1 MB
            -&gt;(close writing half of the socket) &lt; -"HTTP/1.1 201 \r\n" &lt; -"\r\n"
</code></pre></dl>
 

 Deleting problem directory: 

<dl>
<dt>
<dd> <pre>
-&gt; &quot;DELETE &lt;directory_name&gt; HTTP/1.1\r\n&quot;
-&gt; &quot;\r\n&quot;
-&gt; (close writing half of the socket)
&lt;- &quot;HTTP/1.1 200 \r\n&quot;
&lt;- &quot;\r\n&quot;
</pre></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


