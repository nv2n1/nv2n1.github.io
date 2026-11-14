---
title: "obexftpd(1)"
name: "obexftpd"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obexftpd/"
description: "obexftpd – Mobile Equipment file transfer server"
---

<h2>NAME</h2>
<p> obexftpd &#8211; Mobile Equipment file transfer server</p>
<h2>SYNOPSIS</h2>
<p> <code>obexftpd</code> [<i>OPTIONS</i>] [<i>TRANSPORT</i>]</p>
<h2>DESCRIPTION</h2>
<p> With <code>obexftpd</code> you can set up an obex server on any computers using <code>IrDA</code>, <code>Bluetooth</code> or <code>TCP/IP</code>. Use e.g. <code>obexftp</code> or the <code>ObexFS</code> to access the files on this server.</p>
<h2>OPTIONS</h2>
<p> The ordering of options is important. The first transport option will start the server. Use basedir and verbose options prior to any transport. See <code>EXAMPLES</code></p>
<h3>TRANSPORT OPTIONS</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;irda</code></p>
<dd> Acceopt connections using the IrDA protocol.</p>
<dt><code>-b</code>, <code>&#8211;bluetooth</code></p>
<dd> Accept connections via bluetooth.</p>
<dt><code>-t</code> <i>device</i>, <code>&#8211;tty</code> <i>device</i></p>
<dd> Accept connections from this tty device. NOT WORKING!</p>
<dt><code>-n</code> <i>host</i>, <code>&#8211;network</code> <i>host</i></p>
<dd> Accept connections from the network to this port.</dl>
<h3>SETTING THE FILE PATH</h3>
<dl>
<dt><code>-c</code> <i>folder</i>, <code>&#8211;chdir</code> <i>folder</i></p>
<dd> Set the base directory for the server.</dl>
<h3>VERSION INFORMATION AND HELP</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose and give some additional infos.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version string and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;usage</code></p>
<dd> Print short usage instructions.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Start listening for bluetooth connections and use a safe basedir:</p>
<dd> <code>obexftpd -c /tmp/inbox -b</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-obexftp/">obexftp</a>(1), <a href="/docs/linux/man/3-openobex/">openobex</a>(3), <a href="/docs/linux/man/3-obexftp/">obexftp</a>(3), <a href="/docs/linux/man/3-multicobex/">multicobex</a>(3), <a href="/docs/linux/man/3-libbfb/">libbfb</a>(3).</p>
<h2>BUGS</h2>
<p> Bugs ? Features !</p>
<h2>NOTES</h2>
<p> The software has been tested and reported working on at least Siemens, Ericsson, and Nokia phones.</p>
<h2>AUTHOR</h2>
<p> Christian W. Zuckschwerdt &lt;zany [at] triq.net&gt; Alan Zhang &lt;vibra [at] tom.com&gt; </p>
<h2>Index</h2>
