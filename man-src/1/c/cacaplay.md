---
title: "cacaplay(1)"
name: "cacaplay"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cacaplay/"
description: "cacaplay – play libcaca files"
---

<h2>NAME</h2>
<p> cacaplay &#8211; play libcaca files</p>
<h2>SYNOPSIS</h2>
<p> <code>cacaplay [FILE]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>cacaplay</code> plays libcaca animation files. These files can be created by any libcaca program by setting the <code>CACA_DRIVER</code> environment variable to <code>raw</code> and storing the program&#8217;s standard output. </p>
<p> If no file argument is provided or &#8216;-&#8216; is used, <code>cacaplay</code> will read its data from the standard input.</p>
<h2>EXAMPLES</h2>
<p> cacaplay file.caca </p>
<p> CACA_DRIVER=raw CACA_GEOMETRY=80&#215;32 cacademo | cacaplay</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cacaserver/">cacaserver</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sam Hocevar &lt;sam [at] hocevar.net&gt;. </p>
<h2>Index</h2>
