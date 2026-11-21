---

title: "mdatopbm(1)"
name: "mdatopbm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdatopbm/"
description: "mdatopbm – convert a Microdesign .mda or .mdp file into a portable bitmap"
---

<p> <code>mdatopbm</code> [<code>-a</code>][<code>-d</code>][<code>-i</code>][<code>&#8212;</code>] <i>[ mdafile ]</i></p>
<p> Reads a MicroDesign file as input. Reads from stdin if input file is omitted. Produces a portable bitmap as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Output the PBM in ASCII rather than binary.</dd>
<dt><code>-d</code></dt>
<dd> Double the height of the output file, to compensate for the aspect ratio used in MicroDesign files.</dd>
<dt><code>-i</code></dt>
<dd> Invert the colours used.</dd>
<dt><code>&#8212;</code></dt>
<dd> End of options (use this if the filename starts with &quot;-&quot;)</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmtomda/">pbmtomda</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1999 John Elliott &lt;jce [at] seasip.demon.co.uk&gt;. </p>
