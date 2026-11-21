---

title: "ipetopng(1)"
name: "ipetopng"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipetopng/"
description: "ipetopng – Save an Ipe document as a bitmap"
---

<p> <code>ipetopng</code> <i>page</i> <i>resolution</i> <i>input-file</i> <i>output-file</i> </p>
<p> <code>ipetopng</code> converts a single page of an Ipe document as a PNG image. You have to specify the <i>page</i> and the <i>resolution</i> in pixels per inch. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>ipetopng</code> respects the following environment variables: </p>
<dl>
<dt><code>IPELATEXDIR</code></dt>
<dd> the directory where <code>ipetopng</code> runs Pdflatex. </dd>
<dt><code>IPEPDFLATEX</code></dt>
<dd> the name of the Pdflatex executable. If Pdflatex is on your path, the value <i>pdflatex</i> is sufficient. </dd>
<dt><code>IPEFONTMAP</code></dt>
<dd> the complete path of the font map, describing where Ipe can find the 14 standard PDF fonts. </dd>
<dt><code>TEXINPUTS</code></dt>
<dd> when running Pdflatex, Ipe prepends both the current directory (where Ipe was started) as the directory containing the current document to the <code>TEXINPUTS</code> environment variable. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Otfried Cheong </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs using Ipe bugzilla at <i><a rel="nofollow" href="http://tclab.kaist.ac.kr/ipe/bugzilla.html">http://tclab.kaist.ac.kr/ipe/bugzilla.html</a></i> </p>
<h2>SEE ALSO</h2>
<p> More information about Ipe can be found in <i>The Ipe Manual</i>, which can be found in <i>/usr/share/doc/ipe/manual.html</i> or in pdf format in <i>/usr/share/doc/ipe/manual.pdf</i>. </p>
