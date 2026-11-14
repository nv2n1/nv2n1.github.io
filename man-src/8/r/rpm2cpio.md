---
title: "rpm2cpio(8)"
name: "rpm2cpio"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpm2cpio/"
description: "rpm2cpio – Extract cpio archive from RPM Package Manager (RPM) package."
---

<p>rpm2cpio &#8211; Extract cpio archive from RPM Package Manager (RPM) package.</p>
<h2>Synopsis</h2>
<p><code>rpm2cpio</code> [filename]</p>
<h2>Description</h2>
<p><code>rpm2cpio</code> converts the .rpm file specified as a single argument to a cpio archive on standard out. If a &#8216;-&#8216; argument is given, an rpm stream is read from standard in.<br />
 <i></i><code>rpm2cpio rpm-1.1-1.i386.rpm</code><br />
 <i></i><code>rpm2cpio &#8211; &lt; glint-1.0-1.i386.rpm</code><br />
 <i></i><code>rpm2cpio glint-1.0-1.i386.rpm | cpio -dium</code> </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-rpm/">rpm</a></i>(8)</p>
<h2>Author</h2>
<pre>Erik Troan &lt;ewt [at] redhat.com&gt;</pre>
