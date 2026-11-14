---
title: "lrztar(1)"
name: "lrztar"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lrztar/"
---

<h2 class="name">NAME</h2>
 

 lrztar - Directory wrapper for lrzip 

<h2>SYNOPSIS</h2>

 <pre><code>
lrztar[options] DIRECTORY
        lrztar -
    d[options] DIRECTORY.tar.lrz
        lrzuntar[options] DIRECTORY.tar.lrz
</code></pre>

<h2>DESCRIPTION</h2>

 lrztar is a wrapper for compressing and decompressing whole directories with <i><a HREF="/docs/linux/man/1-lrzip/">lrzip</a></i>(1) to corresponding file <tt>&quot;DIRECTORY.tar.lrz&quot;</tt>. lrzuntar is identical to <tt>&quot;lrztar -d&quot;</tt>. lrztar takes the same options as lrzip.

<h2>OPTIONS</h2>

 See <i><a HREF="/docs/linux/man/1-lrzip/">lrzip</a></i>(1).

<h2>ENVIRONMENT</h2>

 None.

<h2>FILES</h2>

 None.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/5-lrzip-conf/">lrzip.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-lrzuntar/">lrzuntar</a></i>(1), <i><a HREF="/docs/linux/man/1-lrzip/">lrzip</a></i>(1), <i><a HREF="/docs/linux/man/1-lrunzip/">lrunzip</a></i>(1), <i><a HREF="/docs/linux/man/1-lrzcat/">lrzcat</a></i>(1), <i><a HREF="/docs/linux/man/1-bzip2/">bzip2</a></i>(1), <i><a HREF="/docs/linux/man/1-gzip/">gzip</a></i>(1), <i><a HREF="/docs/linux/man/1-lzop/">lzop</a></i>(1), <i><a HREF="/docs/linux/man/1-rzip/">rzip</a></i>(1), <i><a HREF="/docs/linux/man/1-zip/">zip</a></i>(1)

<h2>AUTHORS</h2>

 Program was written by Con Kolivas. 

 This manual page was written by Jari Aalto &lt;jari.aalto [at] cante.net&gt; (but may be used by others). Released under license <font SIZE="-1">GNU GPL</font> version 2 or (at your option) any later version. For more information about license, visit &lt;<a rel="nofollow" HREF="http://www.gnu.org/copyleft/gpl.html">http://www.gnu.org/copyleft/gpl.html</a>&gt;. 

<h2>Index</h2>


