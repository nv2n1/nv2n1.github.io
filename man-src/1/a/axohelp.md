---

title: "axohelp(1)"
name: "axohelp"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axohelp/"
description: "axohelp – helper program for use of LaTeX package axodraw2 with pdflatex."
---

<p> <code>axohelp [options] [filename]</code></p>
<p> Axohelp is a program used with the axodraw2, which is a LaTeX package for drawing Feynman graphs (and some other simple graphics) in LaTeX documents. </p>
<p> When the axodraw2 package is used with pdflatex (or lualatex or xelatex) it creates a file with extension .ax1. This contains specifications of the graphics elements. Axohelp converts this to a file with extension ax2 that contains the necessary pdf code. The .ax2 file is read by pdflatex (etc) on its next run, and the contents of the .ax2 file are used in the final .pdf output file to draw the desired graphics. </p>
<p> The files processed are specified as follows: When the filename on the command line is of the form file.ax1, then the input file is file.ax1 and the output file is file.ax2. If the filename on the command line does not have extension .ax1, then this extension is appended. </p>
<h2>OPTIONS</h2>
<p> Options can be introduced by single or double hyphen characters. The possible options are: </p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Gives usage information </dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Gives version information </dd>
<dt><code>-V</code></dt>
<dd> NOT CURRENTLY IMPLEMENTED: Give information on each function used. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Current version, by John Collins (username jcc8 at node psu.edu) and Jos Vermaseren (username t68 at nikhef dot nl). </p>
<p> The released version can be obtained from CTAN: &lt;<a rel="nofollow" href="http://www.ctan.org/pkg/axodraw2/">http://www.ctan.org/pkg/axodraw2/</a>&gt;, and an author&#8217;s website &lt;<a rel="nofollow" href="https://www.nikhef.nl/~form/maindir/others/axodraw2/axodraw2.html">https://www.nikhef.nl/~form/maindir/others/axodraw2/axodraw2.html</a>&gt;. </p>
