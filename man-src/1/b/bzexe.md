---
title: "bzexe(1)"
name: "bzexe"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bzexe/"
description: "bzexe – compress executable files in place"
---

<h2 class="name">NAME</h2>
<p> bzexe &#8211; compress executable files in place </p>
<h2>SYNOPSIS</h2>
<p> <code>bzexe</code> [ name &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>bzexe</i> utility allows you to compress executables in place and have them automatically uncompress and execute when you run them (at a penalty in performance). For example if you execute &#8220;bzexe /bin/cat&#8221; it will create the following two files: </p>
<pre>
<br>
    -r-xr-xr-x  1 root  bin   9644 Feb 11 11:16 /bin/cat
    -r-xr-xr-x  1 bin   bin  24576 Nov 23 13:21 /bin/cat~
</pre>
<p> /bin/cat~ is the original file and /bin/cat is the self-uncompressing executable file. You can remove /bin/cat~ once you are sure that /bin/cat works properly. </p>
<p> This utility is most useful on systems with very small disks.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Decompress the given executables instead of compressing them.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1), <a href="/docs/linux/man/1-znew/">znew</a>(1), <a href="/docs/linux/man/1-zmore/">zmore</a>(1), <a href="/docs/linux/man/1-zcmp/">zcmp</a>(1), <a href="/docs/linux/man/1-zforce/">zforce</a>(1)</p>
<h2>CAVEATS</h2>
<p> The compressed executable is a shell script. This may create some security holes. In particular, the compressed executable relies on the PATH environment variable to find <i>gzip</i> and some other utilities <i>(tail, chmod, ln, sleep).</i></p>
<h2>BUGS</h2>
<p> <i>bzexe</i> attempts to retain the original file attributes on the compressed executable, but you may have to fix them manually in some cases, using <i>chmod</i> or <i>chown.</i> </p>
<h2>Index</h2>
