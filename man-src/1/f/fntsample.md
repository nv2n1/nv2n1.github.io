---
title: "fntsample(1)"
name: "fntsample"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fntsample/"
description: "fntsample – PDF and PostScript font samples generator"
---

<h2>NAME</h2>
<p> fntsample &#8211; PDF and PostScript font samples generator</p>
<h2>SYNOPSIS</h2>
<p> <code>fntsample</code> <code>[ </code><i>OPTIONS</i><code> ]</code> <code>-f </code><i>FONT-FILE</i><code> -o </code><i>OUTPUT-FILE</i><br />
 <code>fntsample -h</code></p>
<h2>DESCRIPTION</h2>
<p> <code>fntsample</code> program can be used to generate font samples that show Unicode coverage of the font and are similar in appearance to Unicode charts. Samples can be saved into PDF (default) or PostScript file.</p>
<h2>OPTIONS</h2>
<p> <code>fntsample</code> supports the following options.</p>
<dl>
<dt><code>&#8211;font-file, -f </code><i>FONT-FILE</i></p>
<dd> Make samples of <i>FONT-FILE</i>.</p>
<dt><code>&#8211;font-index, -n </code><i>IDX</i></p>
<dd> Font index for <i>FONT-FILE</i> specified using <code>&#8211;font-file</code> option. Useful for files that contain multiple fonts, like TrueType Collections (.ttc). By default font with index 0 is used.</p>
<dt><code>&#8211;output-file, -o </code><i>OUTPUT-FILE</i></p>
<dd> Write output to <i>OUTPUT-FILE</i>.</p>
<dt><code>&#8211;other-font-file, -d </code><i>OTHER-FONT</i></p>
<dd> Compare <i>FONT-FILE</i> with <i>OTHER-FONT</i>. Glyphs added to <i>FONT-FILE</i> will be highlighted.</p>
<dt><code>&#8211;other-index, -m </code><i>IDX</i></p>
<dd> Font index for <i>OTHER-FONT</i> specified using <code>&#8211;other-font-file</code> option.</p>
<dt><code>&#8211;postscript-output, -s</code></p>
<dd> Use PostScript format for output instead of PDF.</p>
<dt><code>&#8211;svg, -g</code></p>
<dd> Use SVG format for output. The generated document contains one page. Use range selection options to specify which.</p>
<dt><code>&#8211;print-outline, -l</code></p>
<dd> Print document outlines data to standard output. This data can be used to add outlines (aka bookmarks) to resulting PDF file with <code>pdfoutline</code> program.</p>
<dt><code>&#8211;include-range, -i </code><i>RANGE</i></p>
<dd> Show characters in <i>RANGE</i>.</p>
<dt><code>&#8211;exclude-range, -x </code><i>RANGE</i></p>
<dd> Do not show characters in <i>RANGE</i>.</p>
<dt><code>&#8211;style, -t &quot;</code><i>STYLE</i><code>: </code><i>VAL</i><code>&quot;</code></p>
<dd> Set <i>STYLE</i> to value <i>VAL</i>. Run <code>fntsample</code> with option <code>&#8211;help</code> to see list of styles and default values.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Display help text and exit.</dl>
<p> Parameter <i>RANGE</i> for <code>-i</code> and <code>-x</code> can be given as one integer or a pair of integers delimited by minus sign (-). Integers can be specified in decimal, hexadecimal (0x&#8230;) or octal (0&#8230;) format. One integer of a pair can be missing (-N can be used to specify all characters with codes less or equal to N, and N- for all characters with codes greather or equal to N). Multiple <code>-i</code> and <code>-x</code> options can be used.</p>
<h2>EXAMPLES</h2>
<p> Make PDF samples for <i>font.ttf</i> and write them to file <i>samples.pdf</i>: </p>
<dl>
<dt>
<dd>
<pre>
fntsample -f font.ttf -o samples.pdf
</pre>
</dl>
<p> Make PDF samples for <i>font.ttf</i>, compare it with <i>oldfont.ttf</i> and highlight new glyphs. Write output to file <i>samples.pdf</i>: </p>
<dl>
<dt>
<dd>
<pre>
fntsample -f font.ttf -d oldfont.ttf -o samples.pdf
</pre>
</dl>
<p> Make PostScript samples for <i>font.ttf</i> and write output to file <i>samples.ps</i>. Show only glyphs for characters with codes less or equal to U+04FF but exclude U+0370-U+03FF: </p>
<dl>
<dt>
<dd>
<pre>
fntsample -f font.ttf -s -o samples.ps -i -0x04FF -x 0x0370-0x03FF
</pre>
</dl>
<p> Make PDF samples for <i>font.ttf</i> and save output to file <i>samples.pdf</i> adding outlines to it: </p>
<dl>
<dt>
<dd>
<pre>
fntsample -f font.ttf -o temp.pdf -l &gt; outlines.txt
pdfoutline temp.pdf outlines.txt samples.pdf
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 2007 Eugeniy Meshcheryakov &lt;eugen [at] debian.org&gt;<br />
 Homepage: &lt;<a rel="nofollow" href="http://fntsample.sourceforge.net/">http://fntsample.sourceforge.net/</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfoutline/">pdfoutline</a></code>(1) </p>
<h2>Index</h2>
