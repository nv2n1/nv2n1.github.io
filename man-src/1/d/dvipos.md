---
title: "dvipos(1)"
name: "dvipos"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvipos/"
description: "dvipos – compute positions in a DVI file"
---

<h2 class="name">NAME</h2>
<p> dvipos &#8211; compute positions in a DVI file</p>
<h2>SYNOPSIS</h2>
<p> <code>dvipos</code> [ <i>OPTION</i>&#8230; ] <i>infile[.dvi]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>dvipos</code> parses a DVI file looking for <i>pos:</i> specials. It currently recognizes <i>pos:pxy</i>, <i>pos:pxywhd</i>, <i>pos:pxyplus</i>, <i>pos:begbox</i>, <i>pos:endbox</i>, <i>pos:beglines</i>, and <i>pos:endlines</i>. It then outputs the information from those specials along with information that only a DVI postprocessor could determine, such as the current <i>x</i> and <i>y</i> location. The output looks like: </p>
<pre><code>
\pospxywhd{text : 54} {54} {10663sp} {8535sp} {21326sp} {34081sp}
{
    0sp
}
</code></pre>
<p> and is suitable for including in a <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) auxilliary file, such as <i>document.tuo</i>, to be read in by the next run of the <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or similar typesetting engine. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> print usage.</p>
<dt><code>-W, &#8211;warning</code></p>
<dd> print warnings.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> print verbose output.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> print <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1) debugging data.</p>
<dt><code>-s, &#8211;smashchars</code></p>
<dd> regard height and depth as zero.</p>
<dt><code>-o, &#8211;output=</code><i>FILE</i></p>
<dd> send all output to FILE. Without this option, output goes to stdout.</p>
<dt><code>-b, &#8211;bbox[=</code><i>FILE</i>]</p>
<dd> send bounding box to FILE (default FILE is <i>infile.pos</i>).</p>
<dt><code>-f, &#8211;framed[=</code><i>BASE</i>]</p>
<dd> request copy of DVI file, <i>BASE.dvi</i>, with bounding boxes <code>framed</code> (default FILE is <i>infile_frames.dvi</i>). See the <code>&#8211;framesize</code> option.</p>
<dt><code>-m, &#8211;mag=</code><i>INT</i></p>
<dd> override <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) magnification by INT.</p>
<dt><code>-w, &#8211;framesize=</code><i>INT</i></p>
<dd> set frame rule size by INT (default 6554 = .1pt).</p>
<dt><code>-p, &#8211;pages=</code><i>X:Y</i></p>
<dd> set page ranges from X to Y. </p>
</dl>
<h2>USAGE</h2>
<p> <code>dvipos</code> is run mostly behind the scenes by ConTeXt&#8217;s <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1) between runs of <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1), in order to provide information to and get information about positional graphics. These graphics are provided by the MetaFun interface to <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1). <code>dvipos</code> is not used (or needed) in PDF-output mode but is needed for DVI-output mode. <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1) starting with version 1.40 can produce position information even in DVI mode, so once the ConTeXt macros take advantage of this feature, the need for <code>dvipos</code> will fade. </p>
<p> Until then, here is a typical use of <code>dvipos</code>: </p>
<pre>
dvipos notes.dvi
</pre>
<p> The position information that is output is collected by <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1) to include in the <i>notes.tuo</i> auxilliary file to use in the next run. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Extract positions from <i>doc.dvi</i>, with output to <i>doc.loc</i>:</p>
<dd> <tt>dvipos -o doc.loc doc.dvi</tt></p>
<dt>Same as above, but also send bbox information to <i>doc.pos</i>:</p>
<dd> <tt>dvipos -b -o doc.loc doc.dvi</tt></p>
<dt>Instead send bbox information to <i>/tmp/debug.pos</i>:</p>
<dd> <tt>dvipos -b=/tmp/debug.pos -o doc.loc doc.dvi</tt> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-mpost/">mpost</a></code>(1), <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-texexec/">texexec</a></code>(1). </p>
<p> For more about positional graphics, see the MetaFun documentation on the ConTeXt wiki &lt;URL: <a rel="nofollow" href="http://wiki.contextgarden.net/MetaFun">http://wiki.contextgarden.net/MetaFun</a> &gt;. </p>
<h2>BUGS</h2>
<p> If you specify a file for the <code>-b</code> option, you must join the option and name with <code>=</code> rather than (the more common) space: </p>
<pre>
dvipos -b=/tmp/debug.pos notes.dvi
</pre>
<p> works, but </p>
<pre>
dvipos -b /tmp/debug.pos notes.dvi
</pre>
<p> does not. </p>
<h2>AUTHOR</h2>
<p> <code>dvipos</code> is written by Jin-Hwan Cho &lt;chofchof [at] ktug.or.kr&gt;. It is free software (GPLv2 or later). This manpage was written by Sanjoy Mahajan &lt;sanjoy [at] mit.edu&gt; and is in the public domain. </p>
<h2>Index</h2>
