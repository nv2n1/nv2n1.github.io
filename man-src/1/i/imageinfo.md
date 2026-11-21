---

title: "imageinfo(1)"
name: "imageinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imageinfo/"
description: "imageinfo – display selected image information"
---

<p> imageinfo &#8211; display selected image information </p>
<h2>SYNOPSIS</h2>
<p> <code>imageinfo</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;format</code>] [<code>&#8211;fmtdscr</code>] [<code>&#8211;size</code>] [<code>&#8211;depth</code>] [<code>&#8211;geom</code>] [<code>&#8211;width</code>] [<code>&#8211;height</code>] [<code>&#8211;iccname</code>] [<code>&#8211;iccfile</code>=file] [<code>&#8211;iccmd5</code>] [<code>&#8211;md5hash</code>] [<code>&#8211;sha256hash</code>] <code>imagefile</code></p>
<h2>DESCRIPTION</h2>
<p> <i>imageinfo</i> computes and displays selected image attributes. It is similar in function to the ImageMagick <i>identify</i> utility, but provides a few additional attributes (such as details of embedded ICC profiles), and allows command line selection of the attributes to be computed, avoiding unnecessary computation and and allowing easier parsing of results when this utility is called from a script.</p>
<h2>OPTIONS</h2>
<p> <i>imageinfo</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display help message</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display imageinfo version</dd>
<dt><code>&#8211;format</code></dt>
<dd> Display image format</dd>
<dt><code>&#8211;fmtdscr</code></dt>
<dd> Display image format description</dd>
<dt><code>&#8211;size</code></dt>
<dd> Display image size</dd>
<dt><code>&#8211;depth</code></dt>
<dd> Display bit depth</dd>
<dt><code>&#8211;geom</code></dt>
<dd> Display image geometry</dd>
<dt><code>&#8211;width</code></dt>
<dd> Display image width</dd>
<dt><code>&#8211;height</code></dt>
<dd> Display image height</dd>
<dt><code>&#8211;iccname</code></dt>
<dd> Display ICC profile name</dd>
<dt><code>&#8211;iccfile=file</code></dt>
<dd> Save ICC profile to file</dd>
<dt><code>&#8211;iccmd5</code></dt>
<dd> Display MD5 hash of ICC profile</dd>
<dt><code>&#8211;md5hash</code></dt>
<dd> Display MD5 hash of image</dd>
<dt><code>&#8211;sha256hash</code></dt>
<dd> Display SHA-256 hash of image</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-identify/">identify</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Brendt Wohlberg &lt;software [at] wohlberg.net&gt; </p>
