---
title: "tiffset(1)"
name: "tiffset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffset/"
description: "tiffset – set a field in a TIFF header"
---

<h2>NAME</h2>
<p> tiffset &#8211; set a field in a <font SIZE="-1">TIFF</font> header</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffset</code> [ <i>options</i> ] <i>filename.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Tiffset</i> sets the value of a <font SIZE="-1">TIFF</font> header to a specified value.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> dirnumber</i></p>
<dd> change the current directory (starting at 0).</p>
<dt><code>-s</code><i> tagnumber</i> [<i> count</i> ]<i> value &#8230;</i></p>
<dd> Set the value of the named tag to the value or values specified.</p>
<dt><code>-sd</code><i> diroffset</i></p>
<dd> change the current directory by offset.</p>
<dt><code>-sf</code><i> tagnumber filename</i></p>
<dd> Set the value of the tag to the contents of filename. This option is supported for ASCII tags only.</dl>
<h2>EXAMPLES</h2>
<p> The following example sets the image description tag (270) of a.tif to the contents of the file descrip:</p>
<dl>
<dt>
<dd>
<pre>
tiffset -sf 270 descrip a.tif
</pre>
</dl>
<p> The following example sets the artist tag (315) of a.tif to the string &#8220;Anonymous&#8221;:</p>
<dl>
<dt>
<dd>
<pre>
tiffset -s 315 Anonymous a.tif
</pre>
</dl>
<p> This example sets the resolution of the file a.tif to 300 dpi:</p>
<dl>
<dt>
<dd>
<pre>
tiffset -s 296 2 a.tif
tiffset -s 282 300.0 a.tif
tiffset -s 283 300.0 a.tif
</pre>
</dl>
<p> Set the photometric interpretation of the third page of a.tif to min-is-black (ie. inverts it):</p>
<dl>
<dt>
<dd>
<pre>
tiffset -d 2 -s 262 1 a.tif
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffdump/">tiffdump</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
