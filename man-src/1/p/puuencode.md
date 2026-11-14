---
title: "puuencode(1)"
name: "puuencode"
section: "1"
letter: "p"
url: "/docs/linux/man/1-puuencode/"
---

<h2 class="name">NAME</h2>
 

 <pre>
 puuencode - perl replacement for uuencode
</pre> 

<h2>SYNOPSIS</h2>

 <pre>
 puuencode inputfile as_outputfile
</pre>

<h2>DESCRIPTION</h2>

 Puuencode reads the inputfile and writes a printable version of it to <font SIZE="-1">STDOUT</font> in uuencoded style. Nothing fancy, just a simple uuencode replacement.

<h2>BUGS</h2>

 This implementation is much slower than most uuencode programs written in C. Its primary intention is to allow quick testing of the underlying Convert::UU module.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-puudecode/">puudecode</a></i>(1), <i><a HREF="/docs/linux/man/3-convert--uu/">Convert::UU</a></i>(3)

<h2>AUTHOR</h2>

 Andreas Koenig &lt;andreas.koenig [at] mind.de&gt; 

<h2>Index</h2>


