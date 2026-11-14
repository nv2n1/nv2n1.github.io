---
title: "lbzexe(1)"
name: "lbzexe"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzexe/"
description: "lbzexe – compress executable files in place"
---

<h2>NAME</h2>
<p> lbzexe &#8211; compress executable files in place</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzexe</code> <i>name &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>lbzexe</i> utility allows you to compress executables in place and have them automatically uncompress and execute when you run them (at a penalty in performance). For example if you execute &#8220;lbzexe /usr/bin/gdb&#8221; it will create the following two files: </p>
<pre>
<br>
    -rwxr-xr-x  1 root root 1026675 Jun  7 13:53 /usr/bin/gdb
    -rwxr-xr-x  1 root root 2304524 May 30 13:02 /usr/bin/gdb~
</pre>
<p> /usr/bin/gdb~ is the original file and /usr/bin/gdb is the self-uncompressing executable file. You can remove /usr/bin/gdb~ once you are sure that /usr/bin/gdb works properly. </p>
<p> This utility is most useful on systems with very small disks.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Decompress the given executables instead of compressing them.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lbzip2/">lbzip2</a>(1), <a href="/docs/linux/man/1-lbzmore/">lbzmore</a>(1), <a href="/docs/linux/man/1-lbzcmp/">lbzcmp</a>(1), <a href="/docs/linux/man/1-lbzforce/">lbzforce</a>(1)</p>
<h2>CAVEATS</h2>
<p> The compressed executable is a shell script. This may create some security holes. In particular, the compressed executable relies on the PATH environment variable to find <i>lbzip2</i> and some standard utilities (<i>basename</i>, <i>chmod</i>, <i>ln</i>, <i>mkdir</i>, <i>mktemp</i>, <i>rm</i>, <i>sleep</i>, and <i>tail</i>).</p>
<h2>BUGS</h2>
<p> <i>lbzexe</i> attempts to retain the original file attributes on the compressed executable, but you may have to fix them manually in some cases, using <i>chmod</i> or <i>chown</i>. </p>
<h2>Index</h2>
