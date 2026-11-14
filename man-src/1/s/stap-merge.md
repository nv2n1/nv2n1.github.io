---
title: "stap-merge(1)"
name: "stap-merge"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stap-merge/"
description: "stap-merge – systemtap per-cpu binary merger"
---

<h2>NAME</h2>
<p> stap-merge &#8211; systemtap per-cpu binary merger </p>
<h2>SYNOPSIS</h2>
<p> <code>stap-merge</code> [ <i>OPTIONS</i> ] [ <i>INPUT FILENAMES</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The stap-merge executable applies when the -b option has been used while running a <i>stap</i> script. The -b option will generate files per-cpu, based on the timestamp field. Then stap-merge will merge and sort through the per-cpu files based on the timestamp field. </p>
<h2>OPTIONS</h2>
<p> The systemtap merge executable supports the following options.</p>
<dl>
<dt><code>-v</code></p>
<dd> Verbose mode, displays three extra fields per set of collected data. </p>
<dl>
<dt>
<dd>
<pre>
<code>[cpu</code>number,<code>sequence</code>number<code>of</code>data,<code>the</code>length<code>of</code>the<code>data</code>set]
</pre>
</dl>
<dt><code>-o</code><i> OUTPUT_FILENAME</i></p>
<dd>
<p> Specify the name of the file you would like the output to be redirected into. If this option is not specified than the output will be pushed to standard out. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ stap -v -b -e 'probe syscall.open { printf(&quot;%s(%d) open
&quot;,
execname(), pid()) }' 
</pre>
</dl>
<p> This should result in several <i>stpd_cpu</i> files (each labled with a number representing which cpu the file was produced from). </p>
<dl>
<dt>
<dd>
<pre>
$ stap-merge -v stpd_cpu0 stpd_cpu1
</pre>
</dl>
<p> Running the stap-merge program in the same directory as the stap script earlier in the example, will produce an ordered sequence of packets with the three part label for each set of data. This result will be pushed through the standard output. An output file could have been specified using the &quot;-o&quot; option. </p>
<h2>FILES</h2>
<dl>
<dt>Important files and their corresponding paths can be located in the</p>
<dd> stappaths (7) manual page. </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/7-stappaths/">stappaths</a></i>(7),
<i><a href="//www.systutorials.com/docs/linux/man/8-staprun/">staprun</a></i>(8),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapvars/">stapvars</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/8-stap-server/">stap-server</a></i>(8),
<i><a href="//www.systutorials.com/docs/linux/man/1-gdb/">gdb</a></i>(1)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<h2>Index</h2>
