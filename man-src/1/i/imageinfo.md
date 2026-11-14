---
title: "imageinfo(1)"
name: "imageinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imageinfo/"
description: "imageinfo – display selected image information"
---

<h2 class="name">NAME</h2>
<p> imageinfo &#8211; display selected image information </p>
<h2>SYNOPSIS</h2>
<p> <code>imageinfo</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;format</code>] [<code>&#8211;fmtdscr</code>] [<code>&#8211;size</code>] [<code>&#8211;depth</code>] [<code>&#8211;geom</code>] [<code>&#8211;width</code>] [<code>&#8211;height</code>] [<code>&#8211;iccname</code>] [<code>&#8211;iccfile</code>=file] [<code>&#8211;iccmd5</code>] [<code>&#8211;md5hash</code>] [<code>&#8211;sha256hash</code>] <code>imagefile</code></p>
<h2>DESCRIPTION</h2>
<p> <i>imageinfo</i> computes and displays selected image attributes. It is similar in function to the ImageMagick <i>identify</i> utility, but provides a few additional attributes (such as details of embedded ICC profiles), and allows command line selection of the attributes to be computed, avoiding unnecessary computation and and allowing easier parsing of results when this utility is called from a script.</p>
<h2>OPTIONS</h2>
<p> <i>imageinfo</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help message</p>
<dt><code>&#8211;version</code></p>
<dd> Display imageinfo version</p>
<dt><code>&#8211;format</code></p>
<dd> Display image format</p>
<dt><code>&#8211;fmtdscr</code></p>
<dd> Display image format description</p>
<dt><code>&#8211;size</code></p>
<dd> Display image size</p>
<dt><code>&#8211;depth</code></p>
<dd> Display bit depth</p>
<dt><code>&#8211;geom</code></p>
<dd> Display image geometry</p>
<dt><code>&#8211;width</code></p>
<dd> Display image width</p>
<dt><code>&#8211;height</code></p>
<dd> Display image height</p>
<dt><code>&#8211;iccname</code></p>
<dd> Display ICC profile name</p>
<dt><code>&#8211;iccfile=file</code></p>
<dd> Save ICC profile to file</p>
<dt><code>&#8211;iccmd5</code></p>
<dd> Display MD5 hash of ICC profile</p>
<dt><code>&#8211;md5hash</code></p>
<dd> Display MD5 hash of image</p>
<dt><code>&#8211;sha256hash</code></p>
<dd> Display SHA-256 hash of image</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-identify/">identify</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Brendt Wohlberg &lt;software [at] wohlberg.net&gt; </p>
<h2>Index</h2>
