---

title: "ipetoipe(1)"
name: "ipetoipe"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipetoipe/"
description: "ipetoipe – Convert between Ipe file formats"
---

<p> ipetoipe &#8211; Convert between Ipe file formats </p>
<h2>SYNOPSIS</h2>
<p> <code>ipetoipe</code> ( -pdf | -eps | -ps | -xml ) [ -export ] [ -from page ] [ -to page ] [ -noshading ] [ -lastview ] <i>input-file</i> <i>output-file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ipetoipe</code> converts between the various Ipe file formats. </p>
<dl>
<dt><code>-pdf</code></dt>
<dd> convert to PDF format</dd>
<dt><code>-eps</code></dt>
<dd> convert to EPS (encapsulated Postscript) format</dd>
<dt><code>-ps</code></dt>
<dd> convert to Postscript format</dd>
<dt><code>-xml</code></dt>
<dd> convert to XML format</dd>
<dt><code>-export</code></dt>
<dd> do not include Ipe markup in the output file.<br/>
 <i>Warning:</i> this means that Ipe will not be able to read the resulting output file.</dd>
<dt><code>-from</code> and <code>-to</code></dt>
<dd> restrict exporting to PDF to this page range. This only works in conjunction with the <code>-export</code> option.</dd>
<dt><code>-noshading</code></dt>
<dd> do not shade the background of PDF output (if a shading has been defined in the document&#8217;s style sheet).</dd>
<dt><code>-lastview</code></dt>
<dd> create a Postscript/PDF page only for the last view of each Ipe page. This is often convenient for making handouts for slides used in a presentation.</dd>
<dt><code>-runlatex</code></dt>
<dd> run Latex even for XML output. This has the effect of including the dimensions of each text object in the XML file.</dd>
<dt><code>-nocolor</code></dt>
<dd> do not use any color commands in Postscript output. This is useful if you are preparing a manuscript for publication where the publisher checks that the figures are grayscale only. Note that this option doesn&#8217;t actually verify that the figure contains no color (a figure using color processed with this option will cause a Postscript error when displayed).</dd>
<dt><code>-styleupdate</code></dt>
<dd> update all style sheets in the document from external style sheet files in the current directory. The external file&#8217;s name must match the name of the style sheet and have the extension &#8216;isy&#8217;. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>ipetoipe</code> respects the following environment variables: </p>
<dl>
<dt><code>IPELATEXDIR</code></dt>
<dd> the directory where <code>ipetoipe</code> runs Pdflatex. </dd>
<dt><code>IPEPDFLATEX</code></dt>
<dd> the name of the Pdflatex executable. If Pdflatex is on your path, the value <i>pdflatex</i> is sufficient. </dd>
<dt><code>TEXINPUTS</code></dt>
<dd> when running Pdflatex, Ipe prepends both the current directory (where Ipe was started) as the directory containing the current document to the <code>TEXINPUTS</code> environment variable. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Otfried Cheong </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs using Ipe bugzilla at <i><a rel="nofollow" href="http://tclab.kaist.ac.kr/ipe/bugzilla.html">http://tclab.kaist.ac.kr/ipe/bugzilla.html</a></i> </p>
<h2>SEE ALSO</h2>
<p> More information about Ipe can be found in <i>The Ipe Manual</i>, which can be found in <i>/usr/share/doc/ipe/manual.html</i> or in pdf format in <i>/usr/share/doc/ipe/manual.pdf</i>. </p>
