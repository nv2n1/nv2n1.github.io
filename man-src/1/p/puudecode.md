---
title: "puudecode(1)"
name: "puudecode"
section: "1"
letter: "p"
url: "/docs/linux/man/1-puudecode/"
---

<h2 class="name">NAME</h2>
 

 <pre>
 puudecode - perl replacement for uudecode
</pre> 

<h2>SYNOPSIS</h2>

 <pre>
 puudecode inputfile
</pre>

<h2>DESCRIPTION</h2>

 Uudecode reads a uuencoded inputfile and writes the decoded string to the file named in the uuencoded string. It changes the permissions to the mode given in the uuencoded string.

<h2>BUGS</h2>

 This implementation is much slower than most uudecode programs written in C. Its primary intention is to allow quick testing of the underlying Convert::UU module.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-puuencode/">puuencode</a></i>(1), <i><a HREF="/docs/linux/man/3-convert--uu/">Convert::UU</a></i>(3)

<h2>AUTHOR</h2>

 Andreas Koenig &lt;andreas.koenig [at] anima.de&gt; 

<h2>Index</h2>


