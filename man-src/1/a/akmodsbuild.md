---
title: "akmodsbuild(1)"
name: "akmodsbuild"
section: "1"
letter: "a"
url: "/docs/linux/man/1-akmodsbuild/"
description: "akmodsbuild – Rebuilds kmod SRPM(s)"
---

<h2>NAME</h2>
<p> <code>akmodsbuild </code>&#8211; Rebuilds kmod SRPM(s)</p>
<h2>SYNOPSIS</h2>
<pre>
<code>akmodsbuild</code> [<i>options</i>] &lt;<i>SRPM(s)</i>&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Rebuilds kmod-SRPMs for kernels</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code>, <code>&#8211;kernels</code> &lt;list&gt;</p>
<dd></dl>
<pre><code>
   Build the kmod for kernels in list; try to build for the current
   kernel (e.g. output from 'uname -r') if option is not used.
</code></pre>
<p> <code>-l</code>, <code>&#8211;logfile</code> &lt;file&gt; </p>
<pre>
   Write output from rpmbuild to &lt;file&gt;
</pre>
<p> <code>-o</code>, <code>&#8211;outputdir</code> &lt;directory&gt; </p>
<pre>
   Save resulting RPMS in &lt;direcotry&gt;. Use current working directory if 
   directory is not specified.
    
</pre>
<p> <code>-t</code>, <code>&#8211;target</code> </p>
<pre>
   Target architecture. Default: output from 'uname -m'.
</pre>
<p> <code>-v</code>, <code>&#8211;verbose</code> </p>
<pre>
   Increase verboselevel; option can be given multiple times
</pre>
<p> <code>-q</code>, <code>&#8211;quiet</code> </p>
<pre>
   Decrease verboselevel; option can be given multiple times
</pre>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<pre>
   Show usage
</pre>
<p> <code>-V</code>, <code>&#8211;version</code> </p>
<pre>
   Output program version
</pre>
<h2>EXAMPLE</h2>
<p> To compile the kmod SRPMs ndiswrapper-kmod-1.52-1.lvn9.1.src.rpm and madwifi-kmod-0.9.4-2.lvn9.src.rpm found in /usr/src/akmods/ use: </p>
<pre>
$ akmodsbuild /usr/src/akmods/ndiswrapper-kmod-1.52-1.lvn9.1.src.rpm /usr/src/akmods/madwifi-kmod-0.9.4-2.lvn9.src.rpm
</pre>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://bugzilla.rpmfusion.org/buglist.cgi?product=Fedora">https://bugzilla.rpmfusion.org/buglist.cgi?product=Fedora</a>&amp;component=akmods&amp;bug_status=NEW&amp;bug_status=ASSIGNED&amp;bug_status=REOPENED</p>
<h2>AUTHOR</h2>
<p> Thorsten Leemhuis &lt;fedora [AT] leemhuis [DOT] info&gt;</p>
<h2>MAINTAINER</h2>
<p> Richard Shaw &lt;hobbes1069 [AT] gmail [DOT] com&gt; </p>
<h2>Index</h2>
