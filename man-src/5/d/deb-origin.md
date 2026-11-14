---
title: "deb-origin(5)"
name: "deb-origin"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-origin/"
description: "deb-origin – Vendor-specific information files"
---

<p>deb-origin &#8211; Vendor-specific information files</p>
<h2>Synopsis</h2>
<p><code>/etc/dpkg/origins/</code><i>filename</i></p>
<h2>Description</h2>
<p>The files in <code>/etc/dpkg/origins</code> can provide information about various vendors who are providing Debian packages. </p>
<p> They contain a number of fields, or comments when the line starts with &#8216;<code>#</code>&#8216;. Each field begins with a tag, such as <code>Vendor</code> or <code>Parent</code>, followed by a colon and the body of the field. Fields are delimited only by field tags. In other words, field text may be multiple lines in length, but the tools will join lines when processing the body of the field. </p>
<p> The file should be named according to the vendor name. The usual convention is to name the vendor file using the vendor name in all lowercase, but some variation is permitted. Namely, spaces are mapped to dashes (&#8216;<code>&#8211;</code>&#8216;), and the file can have the same casing as the value in <code>Vendor</code> field, or it can be capitalized.</p>
<h2>Fields</h2>
<dl>
<dt><code>Vendor:</code> <i>vendor-name</i> (required)</p>
<dd>The value of this field determines the vendor name.</p>
<dt><code>Vendor-URL:</code> <i>vendor-url</i></p>
<dd>The value of this field determines the vendor <font SIZE="-1">URL.</font></p>
<dt><code>Bugs:</code> <i>bug-url</i></p>
<dd>The value of this field determines the type and address of the bug tracking system used by this vendor. It can be a mailto <font SIZE="-1">URL</font> or a debbugs <font SIZE="-1">URL</font> (e.g., debbugs://bugs.debian.org/).</p>
<dt><code>Parent:</code> <i>vendor-name</i></p>
<dd>The value of this field determines the vendor name of the vendor that this vendor derives from.</dl>
<h2>Example</h2>
<pre> Vendor: Debian
 Vendor-URL: <a rel="nofollow" href="https://www.debian.org/">https://www.debian.org/</a>
 Bugs: debbugs://bugs.debian.org</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-vendor/">dpkg-vendor</a></code>(1) </p>
