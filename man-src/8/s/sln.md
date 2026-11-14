---
title: "sln(8)"
name: "sln"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sln/"
description: "sln – create symbolic links"
---

<p>sln &#8211; create symbolic links</p>
<h2>Synopsis</h2>
<p><code>sln</code><i> source dest</i><br />
 <code>sln</code><i> filelist</i></p>
<h2>Description</h2>
<p>The <code>sln</code> program creates symbolic links. Unlike the <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1) program, it is statically linked. This means that if for some reason the dynamic linker is not working, <code>sln</code> can be used to make symbolic links to dynamic libraries. </p>
<p> The command line has two forms. In the first form, it creates <i>dest</i> as a new symbolic link to <i>source</i>. </p>
<p> In the second form, <i>filelist</i> is a list of space-separated pathname pairs, and the effect is as if <code>sln</code> was executed once for each line of the file, with the two pathnames as the arguments. </p>
<p> The <code>sln</code> program supports no command-line options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
