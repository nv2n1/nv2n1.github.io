---
title: "gv(1)"
name: "gv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gv/"
description: "gv – Postscript and PDF viewer"
---

<h2>NAME</h2>
<p> gv &#8211; Postscript and PDF viewer</p>
<h2>SYNOPSIS</h2>
<p> <code>gv</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> PostScript and PDF viewer.</p>
<dl>
<dt>[-]-monochrome</p>
<dd> display document using only black and white</p>
<dt>[-]-grayscale</p>
<dd> display document without colors</p>
<dt>[-]-color</p>
<dd> display document as usual</p>
<dt>[-]-safer</p>
<dd> start ghostscript in safe mode</p>
<dt>[-]-nosafer</p>
<dd> do not start ghostscript in safe mode</p>
<dt>[-]-safedir</p>
<dd> start ghostscript from a safe diretory</p>
<dt>[-]-nosafedir</p>
<dd> do not start ghostscript from a safe diretory</p>
<dt>[-]-quiet</p>
<dd> start ghostscript with the <code>-dQUIET</code> option</p>
<dt>[-]-noquiet</p>
<dd> do not start ghostscript with the <code>-dQUIET</code> option</p>
<dt>[-]-infoSilent</p>
<dd> do not show any messages in the info popup window</p>
<dt>[-]-infoErrors</p>
<dd> do not show warning messages in the info popup window</p>
<dt>[-]-infoAll</p>
<dd> do show all messages in the info popup window</p>
<dt>[-]-arguments=ARGS</p>
<dd> start ghostscript with additional options as specified by the string ARGS</p>
<dt>[-]-page=LABEL</p>
<dd> display the page with label LABEL first</p>
<dt>[-]-center</p>
<dd> the page should be centered automatically</p>
<dt>[-]-nocenter</p>
<dd> the page should not be centered automatically</p>
<dt>[-]-media=MEDIA</p>
<dd> selects the paper size to be used</p>
<dt>[-]-orientation=ORIENTATION</p>
<dd> sets the orientation of the page</p>
<dt>[-]-scale=N|f.f</p>
<dd> selects the scale N, or arbitrary scale f.f</p>
<dt>[-]-scalebase=N</p>
<dd> selects the scale base N</p>
<dt>[-]-swap</p>
<dd> interchange the meaning of the orientations landscape and seascape</p>
<dt>[-]-noswap</p>
<dd> do not interchange the meaning of the orientation landscape and seascape</p>
<dt>[-]-antialias</p>
<dd> use antialiasing</p>
<dt>[-]-noantialias</p>
<dd> do not use antialiasing</p>
<dt>[-]-dsc</p>
<dd> dsc comments are respected</p>
<dt>[-]-nodsc</p>
<dd> dsc comments are not respected</p>
<dt>[-]-eof</p>
<dd> ignore the postscript EOF comment while scanning documents</p>
<dt>[-]-noeof</p>
<dd> do not ignore the postscript EOF comment while scanning documents</p>
<dt>[-]-pixmap</p>
<dd> use backing pixmap</p>
<dt>[-]-nopixmap</p>
<dd> do not use backing pixmap</p>
<dt>[-]-watch</p>
<dd> watch the document file for changes</p>
<dt>[-]-nowatch</p>
<dd> do not watch the document file for changes</p>
<dt>[-]-help</p>
<dd> print a help message and exit</p>
<dt>[-]-usage</p>
<dd> print a usage message and exit</p>
<dt>[-]-resize</p>
<dd> fit the size of the window to the size of the page</p>
<dt>[-]-noresize</p>
<dd> do not fit the size of the window to the size of the page</p>
<dt> <code>-geometry</code> [&lt;width&gt;][x&lt;height&gt;][{+-}&lt;xoffset&gt;{+-}&lt;yoffset&gt;]</p>
<dt>[-]-ad=FILE</p>
<dd>
<dd>read and use additional resources from FILE</p>
<dt>[-]-style=FILE</p>
<dd> read and use additional resources from FILE. These resources have lower priority than those provided on the context of <code>&#8211;ad</code></p>
<dt>[-]-password=PASSWORD</p>
<dd> Sets the password for opening encrypted PDF files</p>
<dt>[-]-spartan</p>
<dd> shortcut for <code>&#8211;style</code>=<i>gv_spartan</i>.dat</p>
<dt>[-]-widgetless</p>
<dd> shortcut for <code>&#8211;style</code>=<i>gv_widgetless</i>.dat</p>
<dt>[-]-fullscreen</p>
<dd> start in fullscreen mode (needs support from WM)</p>
<dt>[-]-presentation</p>
<dd> Presentation mode (fullscreen, Fit to window, widgetless and no resizing of window)</p>
<dt>[-]-version</p>
<dd> show gv version and exit</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gv</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gv</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gv</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
