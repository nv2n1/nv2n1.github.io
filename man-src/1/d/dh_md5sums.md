---
title: "dh_md5sums(1)"
name: "dh_md5sums"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_md5sums/"
description: "dh_md5sums – generate DEBIAN/md5sums file"
---

<h2 class="name">NAME</h2>
<p> dh_md5sums &#8211; generate DEBIAN/md5sums file </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_md5sums</code> [<i>debhelper options</i>] [<code>-x</code>] [<code>-X</code><i>item</i>] [<code>&#8211;include-conffiles</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_md5sums</code> is a debhelper program that is responsible for generating a <i>DEBIAN/md5sums</i> file, which lists the md5sums of each file in the package. These files are used by <code>dpkg &#8211;verify</code> or the <i><a href="/docs/linux/man/1-debsums/">debsums</a></i>(1) program. </p>
<p> All files in <i></i><font SIZE="-1"><i>DEBIAN/</i></font><i></i> are omitted from the <i>md5sums</i> file, as are all conffiles (unless you use the <code>&#8211;include-conffiles</code> switch). </p>
<p> The md5sums file is installed with proper permissions and ownerships.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code>, <code>&#8211;include-conffiles</code></p>
<dd> Include conffiles in the md5sums list. Note that this information is redundant since it is included elsewhere in Debian packages.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being listed in the md5sums file.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
