---

title: "fontimage(1)"
name: "fontimage"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontimage/"
description: "fontimage – produce a font thumbnail image"
---

<p> <code>fontimage &#8211; produce a font thumbnail image</code></p>
<h2>SYNOPSIS</h2>
<p> <code>fontimage</code> [<code>&#8211;help</code>] [<code>&#8211;width</code> <i>num</i>] [<code>&#8211;height</code> <i>num</i>] [<code>&#8211;pixelsize</code> <i>num</i>] [<code>&#8211;text</code> <i>string</i>] [<code>&#8211;o</code> <i>outputfile</i>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>] <i>fontfile</i></p>
<h2>DESCRIPTION</h2>
<p> The program <code>fontimage</code> loads a font, which may be in any format <i><a href="/docs/linux/man/1-fontforge/">fontforge</a></i>(1) can read, and then produces an image showing representative glyphs of the font. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Provide a description with a list of the available options.</dd>
<dt><code>&#8211;width num</code></dt>
<dd> Specifies the width of the output image. If this is omitted the image will be as wide as necessary to display the text.</dd>
<dt><code>&#8211;height num</code></dt>
<dd> Specifies the height of the output image. If this is omitted the image will be as high as necessary to display the text.</dd>
<dt><code>&#8211;pixelsize num</code></dt>
<dd> Specifies the pixelsize used to display the text. This argument may be specified multiple times and each refers to any &#8211;text lines that follow it.</dd>
<dt><code>&#8211;text string</code></dt>
<dd> Specifies a line of text to be displayed. The string must be in UTF-8. This argument may be specified multiple times to provide several lines of text. If no &#8211;text arguments are supplied <i>fontimage</i> will examine the font, looking for various scripts it knows about, and will try to display something appropriate for each.</dd>
<dt><code>-o outfile</code></dt>
<dd> Specifies the output filename for the image. The type of image will be determined by the file&#8217;s extension. Currently only &quot;.bmp&quot; and &quot;.png&quot; are recognized. If omitted <i>fontimage</i> will choose an output name based on the font&#8217;s fontname field.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display the usage description.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the current version</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual at:<br />
 <a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2006 by George Williams (gww [at] silcom.com). </p>
