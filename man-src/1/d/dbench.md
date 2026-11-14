---
title: "dbench(1)"
name: "dbench"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbench/"
description: "dbench – Measure disk throughput for simulated netbench run"
---

<h2 class="name">NAME</h2>
<p> dbench &#8211; Measure disk throughput for simulated netbench run </p>
<h2>SYNOPSIS</h2>
<p> <code>dbench</code> [<i>options</i>]<i>numclients</i><br />
 <code>tbench</code> [<i>options</i>]<i>numclients</i>server <code>tbench_srv</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>dbench</code> and <code>tbench</code> benchmarks. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. However, it has fairly easy to read source code. </p>
<p> Netbench is a terrible benchmark, but it&#8217;s an &quot;industry standard&quot; and it&#8217;s what is used in the press to rate windows fileservers like Samba and WindowsNT.<br />
 Given the requirements of running netbench (60 and 150 Windows PCs all on switched fast ethernet and a really grunty server, and a to open up netbench to the masses.<br />
 Both <code>dbench</code> and <code>tbench</code> read a load description file called client.txt that was derived from a capture of a real netbench run. client.txt is about 25MB and describes the 500 thousand operations that a netbench client does in a typical netbench run. They parse client.txt and use it to produce the same load without having to buy a huge lab.<br />
 dbench produces only the filesystem load. It does all the same IO calls that the smbd server in Samba would produce when confronted with a netbench run. It does no networking calls.<br />
 tbench produces only the TCP and process load. It does the same socket calls that smbd would do under a netbench load. It does no filesystem calls. The idea behind tbench is to eliminate smbd from the netbench test, as though the smbd code could be made infinately fast.</p>
<h2>OPTIONS</h2>
<p> The <code>dbench</code> program takes a number, which indicates the number of clients to run simultaneously. It can also take the following options:</p>
<dl>
<dt><code>-c client.txt</code></p>
<dd> Use this as the full path name of the client.txt file (the default is /usr/share/dbench/client.txt).</p>
<dt><code>-s</code></p>
<dd> Use synchronous file IO on all file operations.</p>
<dt><code>-t TIME</code></p>
<dd> set the runtime of the benchmark in seconds (default 600)</p>
<dt><code>-D DIR</code></p>
<dd> set the base directory to run the filesystem operations in</p>
<dt><code>-x</code></p>
<dd> enable xattr support, simulating the xattr operations Samba4 would need to perform to run the load</p>
<dt><code>-S</code></p>
<dd> Use synchronous IO for all directory operations (unlink, rmdir, mkdir and rename).<br />
 The <code>tbench</code> program takes a number, which indicates the number of clients to run simultaneously, and a server name: <code>tbench_srv</code> should be invoked on that server before invoking <code>tbench</code>. <code>tbench</code> can also take the following options:</p>
<dt><code>-c loadfile</code></p>
<dd> Use this as the full path name of the client.txt file (the default is /usr/share/dbench/client.txt).</p>
<dt><code>-T option[,&#8230;]</code></p>
<dd> This sets the socket options for the connection to the server. The options are a comma-separated list of one or more of the following: <code>SO_KEEPALIVE</code>, <code>SO_REUSEADDR</code>, <code>SO_BROADCAST</code>, <code>SO_NODELAY</code>, <code>SO_LOWDELAY</code>, <code>SO_THROUGHPUT</code>, <code>SO_SNDBUF</code>=number, <code>SO_RCVBUF</code>=number, <code>SO_SNDLOWAT</code>=number, <code>SO_RCVLOWAT</code>=number, <code>SO_SNDTIMEO</code>=number,<code>and</code> <code>SO_RCVTIMEO</code>=number. See <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details about these options.<br />
 The <code>tbench_srv</code> can only take one option: <code>-t option[,&#8230;]</code> as documented above.</dl>
<h2>SEE ALSO</h2>
<p> <i>/usr/share/doc/dbench/README</i> contains the original README by Andrew Tridgell which accompanies the dbench source.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Russell &lt;prussell [at] alderaan.franken.de&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
