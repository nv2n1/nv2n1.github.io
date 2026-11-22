---
title: "rmt-tar(8)"
name: "rmt-tar"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rmt-tar/"
description: "rmt – remote magnetic tape server"
---

<p>rmt &#8211; remote magnetic tape server</p>
<h2>Synopsis</h2>
<p><code>rmt</code></p>
<h2>Description</h2>
<p><code>Rmt</code> provides remote access to files and devices for <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-cpio/">cpio</a></code>(1), and similar backup utilities. It is normally called by running <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1) or <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) to the remote machine, optionally using a different login name if one is supplied. </p>
<p> The calling program communicates with <code>rmt</code> by sending requests on its standard input and reading replies from the standard output. A request consists of a request letter followed by an argument (if required) and a newline character. Additional data, if any, are sent after the newline. On success, <code>rmt</code> returns </p>
<p> <code>A</code><i>number</i><code>
</code> </p>
<p> where <i>number</i> is an ASCII representation of a decimal return code. Additional data are returned after this line. On error, the following response is returned: </p>
<p> <code>E</code><i>errno</i><code>
</code><i>error-message</i><code>
</code> </p>
<p> where <i>errno</i> is one of the system error codes, as described in <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), and <i>error-message</i> is a one-line human-readable description of the error, as printed by <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3). </p>
<p> Available commands and possible responses are discussed in detail in the subsequent section.</p>
<h2>Commands</h2>
<dl>
<dt><code>O</code><i>device</i><code>
</code><i>flags</i><code>
</code></dt>
<dd>Opens the <i>device</i> with given <i>flags</i>. If a device had already been opened, it is closed before opening the new one. </dd>
<p> <code>Arguments</code></p>
<dl>
<dd>
</dd><dl>
<dt><i>device</i></dt>
<dd>The name of the device to open.</dd>
<dt><i>flags</i></dt>
<dd>Flags for <code><a href="/docs/linux/man/2-open/">open</a></code>(2): a decimal number, or any valid <code>O_*</code> constant from <code>fcntl.h</code> (the initial <code>O_</code> may be omitted), or a bitwise or (using <code>|</code>) of any number of these, e.g.: 576 64|512 CREAT|TRUNC</dd>
<dl>
<dd>In addition, a combined form is also allowed, i.e. a decimal mode followed by its symbolic representation. In this case the symbolic representation is given preference.</dd></dl>
<p> <code>Reply</code></p>
<dl>
<dd><code>A0
</code> on success.</dd></dl>
<p> <code>Extensions</code></p>
<dl>
<dd>BSD version allows only decimal number as <i>flags</i>.</dd></dl>
<dt><code>C</code>[<i>device</i>]<code>
</code></dt>
<dd>Close the currently open device.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Arguments</code></dt>
<dd>Any arguments are silently ignored.</dd>
<dt><code>Reply</code></dt>
<dd><code>A0
</code> on success.</dd></dl>
</dl>
<dt><code>L</code><i>whence</i><code>
</code><i>offset</i><code>
</code></dt>
<dd>
</dd><dl>
<dd>Performs an <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) on the currently open device with the specified parameters.</dd>
<dl>
<dt><code>Arguments</code></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><i>whence</i></dt>
<dd>Where to measure offset from. Valid values are: </dd>
<pre> 0, SET, SEEK_SET seek from the file beginning
 1, CUR, SEEK_CUR seek from the current location
 2, END, SEEK_END seek from the file end</pre>
</dl>
</dl>
<dt><code>Reply</code></dt>
<dd><code>A</code><i>offset</i><code>
</code> on success. The <i>offset</i> is the new offset in file.</dd>
<dt><code>Extensions</code></dt>
<dd>BSD version allows only 0,1,2 as <i>whence</i>.</dd></dl>
</dl>
<dt><code>R</code><i>count</i><code>
</code></dt>
<dd>Read <i>count</i> bytes of data from the current device.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Arguments</code></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><i>count</i></dt>
<dd>number of bytes to read.</dd></dl>
</dl>
<dt><code>Reply</code></dt>
<dd>On success: </dd>
<p> <code>A</code><i>rdcount</i><code>
</code> </p>
<p> followed by <i>rdcount</i> bytes of data read from the device.</dl>
</dl>
<dt><code>W</code><i>count</i><code>
</code></dt>
<dd>Writes data onto the current device. The command is followed by <i>count</i> bytes of input data.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Arguments</code></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><i>count</i></dt>
<dd>Number of bytes to write.</dd></dl>
</dl>
<dt><code>Reply</code></dt>
<dd>On success: <code>A</code><i>wrcount</i><code>
</code>, where <i>wrcount</i> is the number of bytes actually written.</dd></dl>
</dl>
<dt><code>I</code><i>opcode</i><code>
</code><i>count</i><code>
</code></dt>
<dd>Perform a <code>MTIOCOP</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) command with the specified paramedters.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Arguments</code></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><i>opcode</i></dt>
<dd><code>MTIOCOP</code> operation code.</dd>
<dt><i>count</i></dt>
<dd>mt_count.</dd></dl>
</dl>
<dt><code>Reply</code></dt>
<dd>On success: <code>A0
</code>.</dd></dl>
</dl>
<dt><code>S
</code></dt>
<dd>Returns the status of the currently open device, as obtained from a <code>MTIOCGET</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) call.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Arguments</code></dt>
<dd>None</dd>
<dt><code>Reply</code></dt>
<dd>On success: <code>A</code><i>count</i><code>
</code> followed by <i>count</i> bytes of data.</dd></dl>
</dl>
</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tar/">tar</a></code>(1).</p>
<h2>Bugs</h2>
<p>Using this utility as a general-purpose remote file access tool is discouraged.</p>
<h2>Bug Reports</h2>
<p>Report bugs to &lt;bug-tar [at] gnu.org&gt;.</p>
<h2>History</h2>
<p>The <code>rmt</code> command appeared in 4.2BSD. The GNU <code>rmt</code> is written from scratch, using the BSD specification.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013, 2018 Free Software Foundation, Inc.<br/>
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
