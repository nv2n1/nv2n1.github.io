---
title: "scrot(1)"
name: "scrot"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scrot/"
description: "scrot – capture a screenshot using imlib2"
---

<h2 class="name">NAME</h2>
<p> scrot &#8211; capture a screenshot using imlib2 </p>
<h2>SYNOPSIS</h2>
<p> scrot [options] [file]</p>
<h2>DESCRIPTION</h2>
<p> <code>scrot</code> is a screen capture utility using the <code>imlib2</code> library to aquire and save images. <code>scrot</code> has a few options, detailed below. Specify [file] as the filename to save the screenshot to. If [file] is not specified, a date-stamped file will be dropped in the current directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> display help output and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-b, &#8211;border</code></p>
<dd> When selecting a window, grab wm border too</p>
<dt><code>-c, &#8211;count</code></p>
<dd> Display a countdown when used with delay.</p>
<dt><code>-d, &#8211;delay NUM</code></p>
<dd> Wait NUM seconds before taking a shot.</p>
<dt><code>-e, &#8211;exec APP</code></p>
<dd> Exec APP on the saved image.</p>
<dt><code>-q, &#8211;quality NUM</code></p>
<dd> Image quality (1-100) high value means high size, low compression. Default: 75. (Effect differs depending on file format chosen).</p>
<dt><code>-m, &#8211;multidisp</code></p>
<dd> For multiple heads, grab shot from each and join them together.</p>
<dt><code>-s, &#8211;select</code></p>
<dd> Interactively select a window or rectangle with the mouse.</p>
<dt><code>-u, &#8211;focused</code></p>
<dd> Use the currently focused window.</p>
<dt><code>-t, &#8211;thumb NUM</code></p>
<dd> generate thumbnail too. NUM is the percentage of the original size for the thumbnail to be.</p>
<dt><code>-z, &#8211;silent</code></p>
<dd> prevent beeping.</dl>
<h2>SPECIAL STRINGS</h2>
<p> Both the <code>&#8211;exec</code> and <code>filename</code> parameters can take format specifiers that are expanded by scrot when encountered. There are two types of format specifier. Characters preceded by a &#8216;%&#8217; are interpretted by <a href="/docs/linux/man/2-strftime/">strftime</a>(2). See man strftime for examples. These options may be used to refer to the current date and time. The second kind are internal to scrot and are prefixed by &#8216;$&#8217; The following specifiers are recognised: </p>
<p> <code>$f</code> image path/filename (ignored when used in the filename)<br />
 <code>$n</code> image name (ignored when used in the filename)<br />
 <code>$s</code> image size (bytes) (ignored when used in the filename)<br />
 <code>$p</code> image pixel size<br />
 <code>$w</code> image width<br />
 <code>$h</code> image height<br />
 <code>$t</code> image format<br />
 <code>$$</code> prints a literal &#8216;$&#8217; </p>
<pre>

 prints a newline (ignored when used in the filename)
</pre>
<h2>EXAMPLE</h2>
<p> scrot &#8216;%Y-%m-%d_$wx$h.png&#8217; -e &#8216;mv $f ~/shots/&#8217;<br />
 This would create a file called something like 2000-10-30_2560x1024.png and move it to your shots directory.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>LICENSE</h2>
<p> Copyright Tom Gilbert 2000 </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies of the Software, its documentation and marketing &amp; publicity materials, and acknowledgment shall be given in the documentation, materials and software packages that this Software was used. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </p>
<p> Email bugs and feature requests to<br />
 <code>&lt;scrot_sucks [at] linuxbrit.co.uk&gt;</code> </p>
<h2>Index</h2>
