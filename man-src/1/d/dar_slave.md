---
title: "dar_slave(1)"
name: "dar_slave"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dar_slave/"
description: "dar_slave – disk archive slave for remote access to a dar archive"
---

<h2 class="name">NAME</h2>
<p> dar_slave &#8211; disk archive slave for remote access to a dar archive </p>
<h2>SYNOPSIS</h2>
<p> dar_slave [options] [&lt;path&gt;/]source </p>
<p> dar_slave -h </p>
<p> dar_slave -V</p>
<h2>DESCRIPTION</h2>
<p> <code>dar_slave</code> reads an archive and listens for <code>dar</code> orders on standard input, sending asked parts of the archive on standard output. </p>
<p> Source is the basename of the archive to read. By default, <code>dar_slave</code> uses standard input and output to communicate with a <code>dar</code> process, which may be running on the local host or on a remote host. It is possible to change the behavior of <code>dar_slave</code> to use named pipe instead of standard input and output </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> Displays help usage.</p>
<dt>-V</p>
<dd> Displays version information.</p>
<dt>-i &lt;filename&gt;</p>
<dd> reads the orders from the named file instead of standard input. In most cases the filename will be a named pipe.</p>
<dt>-o &lt;filename&gt;</p>
<dd> sends the data to the named file &lt;filename&gt; instead of standard output. In most cases the filename will be a named pipe.</p>
<dt>-E &lt;string&gt;</p>
<dd> string is a command to be launched between slices. See <a href="/docs/linux/man/1-dar/">dar</a>(1) man page (same option) for more information.</p>
<dt>-Q</p>
<dd> Do not display any message on stderr when not launched from a terminal (for example when launched from an at job or crontab). Remains that any question to the user will be assumed a &#8216;no&#8217; answer, which most of the time will abort the program.</p>
<dt>-9 &lt;num&gt;</p>
<dd> Defines the minimum number of digits to use for archive slice numbers. See the same option in dar man page for more details.</dl>
<h2>EXIT CODES</h2>
<p> <code>dar_slaves</code> exists with the same codes as dar does, see <a href="/docs/linux/man/1-dar/">dar</a>(1) man page. </p>
<h2>SIGNALS</h2>
<p> Any signal sent to dar_slave will abort the program immediately, there is no way to have a proper termination before the end of the process </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dar/">dar</a>(1), <a href="/docs/linux/man/1-dar_xform/">dar_xform</a>(1), <a href="/docs/linux/man/1-dar_manager/">dar_manager</a>(1), <a href="/docs/linux/man/1-dar_cp/">dar_cp</a>(1), <a href="/docs/linux/man/1-dar_split/">dar_split</a>(1) </p>
<h2>KNOWN BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/p/dar/bugs/">http://sourceforge.net/p/dar/bugs/</a> </p>
<h2>AUTHOR</h2>
<pre>
<a rel="nofollow" href="http://dar.linux.free.fr/">http://dar.linux.free.fr/</a>
Denis Corbin
France
Europe
</pre>
<h2>Index</h2>
