---

title: "pbmtomda(1)"
name: "pbmtomda"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtomda/"
description: "pbmtomda – convert a portable bitmap to a Microdesign .mda"
---

<p> <code>pbmtomda</code> [<code>-d</code>][<code>-i</code>][<code>&#8212;</code>] <i>[ pbmfile ]</i></p>
<p> Reads a portable bitmap file as input. Reads from stdin if input file is omitted. Produces a MicroDesign 2 area file (.MDA) as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></dt>
<dd> Halve the height of the output file, to compensate for the aspect ratio used in MicroDesign files.</dd>
<dt><code>-i</code></dt>
<dd> Invert the colours used.</dd>
<dt><code>&#8212;</code></dt>
<dd> End of options (use this if the filename starts with &quot;-&quot;)</dd></dl>
<h2>BUGS</h2>
<p> There&#8217;s no way to produce files in MicroDesign 3 format. MD3 itself and <a href="/docs/linux/man/1-mdatopbm/">mdatopbm</a>(1) can read files in either format.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mdatopbm/">mdatopbm</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1999 John Elliott &lt;jce [at] seasip.demon.co.uk&gt;. </p>
