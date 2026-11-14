---
title: "img2txt(1)"
name: "img2txt"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img2txt/"
description: "img2txt – convert images to various text-based coloured files"
---

<h2>NAME</h2>
<p> img2txt &#8211; convert images to various text-based coloured files</p>
<h2>SYNOPSIS</h2>
<p> <code>img2txt </code> [ <code>-W</code> <i>width</i> ] [ <code>-H</code> <i>height</i> ] [ <code>-x</code> <i>font-width</i> ] [ <code>-y</code> <i>font-height</i> ]</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>[ <code>-b</code> <i>brightness</i> ] [ <code>-c</code> <i>contrast</i> ] [ <code>-g</code> <i>gamma</i> ]</p>
<dt>
<dd>
&nbsp;<wbr>[ <code>-d</code> <i>dither</i> ] [ <code>-f</code> <i>format</i> ] <i>FILE</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>img2txt</code> converts images to colour ASCII characters and outputs them to text-based coloured files. </p>
<p> <code>img2txt</code> can load the most widespread image formats: PNG, JPEG, GIF, PNG, BMP etc (see <code>NOTES</code> for details). By default the output text is 60 columns wide, and the line count is computed accordingly to respect aspect ratio of original file. The default output format is standard ANSI coloured text. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-W, &#8211;width=&lt;width&gt;</code></p>
<dd> Change output column count. If not given, the default is set to 60.</p>
<dt><code>-H, &#8211;height=&lt;height&gt;</code></p>
<dd> Change output line count. If not given, the height is computed to match correct aspect ratio.</p>
<dt><code>-x, &#8211;font-width=&lt;width&gt;</code></p>
<dd> Change output font width. If not given, the default is set to 6. This value will be used for computing aspect ratio.</p>
<dt><code>-y, &#8211;font-height=&lt;height&gt;</code></p>
<dd> Change output font height. If not given, the default is set to 10. This value will be used for computing aspect ratio.</p>
<dt><code>-b, &#8211;brightness=&lt;brightness&gt;</code></p>
<dd> Change image brightness. Default to 1.0.</p>
<dt><code>-c, &#8211;contrast=&lt;contrast&gt;</code></p>
<dd> Change image contrast. Default to 1.0.</p>
<dt><code>-g, &#8211;gamma=&lt;gamma&gt;</code></p>
<dd> Change image gamma. Default to 1.0.</p>
<dt><code>-d, &#8211;dither=&lt;dither&gt;</code></p>
<dd> Change dithering algorithm. This can be one of the following (default to fstein) :<br />
&nbsp;<wbr>&nbsp;<wbr>none&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Nearest color<br />
&nbsp;<wbr>&nbsp;<wbr>ordered2 : Ordered 2&#215;2<br />
&nbsp;<wbr>&nbsp;<wbr>ordered4 : Ordered 4&#215;4<br />
&nbsp;<wbr>&nbsp;<wbr>ordered8 : Ordered 8&#215;8<br />
&nbsp;<wbr>&nbsp;<wbr>random&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Random<br />
&nbsp;<wbr>&nbsp;<wbr>fstein&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Floyd Steinberg</p>
<dt><code>-f, &#8211;format=&lt;format&gt;</code></p>
<dd> Change output format. This can be one of the following (default to ansi) :<br />
&nbsp;<wbr>&nbsp;<wbr>ansi&nbsp;<wbr>&nbsp;<wbr>: coloured ANSI&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>caca&nbsp;<wbr>&nbsp;<wbr>: internal libcaca format<br />
&nbsp;<wbr>&nbsp;<wbr>utf8&nbsp;<wbr>&nbsp;<wbr>: UTF8 with CR<br />
&nbsp;<wbr>&nbsp;<wbr>utf8&nbsp;<wbr>&nbsp;<wbr>: UTF8 with CRLF&nbsp;<wbr>(MS Windows)<br />
&nbsp;<wbr>&nbsp;<wbr>html&nbsp;<wbr>&nbsp;<wbr>: HTML with CSS and DIV support<br />
&nbsp;<wbr>&nbsp;<wbr>html3 : Pure HTML3 with tables<br />
&nbsp;<wbr>&nbsp;<wbr>irc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: IRC with ctrl-k codes<br />
&nbsp;<wbr>&nbsp;<wbr>bbfr&nbsp;<wbr>&nbsp;<wbr>: BBCode&nbsp;<wbr>(French)<br />
&nbsp;<wbr>&nbsp;<wbr>ps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Postscript<br />
&nbsp;<wbr>&nbsp;<wbr>svg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Scalable Vector Graphics<br />
&nbsp;<wbr>&nbsp;<wbr>tga&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Targa Image</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help message and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version of the program and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> img2txt hello.jpg &gt; hello.ans </p>
<p> img2txt &#8211;width=40 &#8211;format=svg hello.jpg &gt; tinyhello.svg </p>
<h2>NOTES</h2>
<p> Setting both column and line count (using &#8211;width and &#8211;height) will let you choose the exact output size without taking aspect ratio in account. </p>
<p> You must compile libcaca package with support of <i>Imlib2</i> to be able to load a wide variety of image formats. Otherwise you will only be able to load regular BMP files. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cacaview/">cacaview</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sam Hocevar &lt;sam [at] hocevar.net&gt; and Jean-Yves Lamoureux &lt;jylam [at] lnxscene.org&gt;. </p>
<h2>Index</h2>
