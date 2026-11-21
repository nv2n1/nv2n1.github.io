---

title: "cptsvg(1)"
name: "cptsvg"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cptsvg/"
description: "cptsvg – convert GMT colour palette tables (cpt) to SVG gradients."
---

<dl>
<dt> <code>cptsvg</code> [-g&nbsp;<wbr><i>geometry</i>] [-h] [-o&nbsp;<wbr><i>file</i>] [-p] [-v] [-V] [<i>file</i>]</dt></dl>
<dd>The <code>cptsvg</code> utility converts the colour palette table (cpt) files used by <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1) to the gradients in the Scalar Vector Graphics (SVG) format. </dd>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified. </p>
<p> The output is formatted for machines to read, rather than humans. A post-processor such as <code><a href="/docs/linux/man/1-tidy/">tidy</a></code>(1) could be used in the latter case.</p>
<h2>OPTIONS</h2>
<p> <code>-g</code>, <code>&#8211;geometry</code> <i>width</i>x<i>height</i></p>
<dl>
<dt>
</dt><dd> Specify the size of the SVG preview in pixels.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Brief help.</dd></dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
</dt><dd> Write the output to <i>file</i>, rather than stdout.</dd></dl>
<p> <code>-p</code>, <code>&#8211;preview</code></p>
<dl>
<dt>
</dt><dd> Include a preview in the SVG output. See also the <code>&#8211;geometry</code> option.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Verbose operation.</dd></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Version information.</dd></dl>
<h2>EXAMPLES</h2>
<p> Create a machine-readable SVG file: </p>
<dl>
<dt>
</dt><dd>
<pre>
  cptsvg -v -o new.svg old.cpt
</pre>
</dd></dl>
<p> Create a human-readable SVG file with a preview: </p>
<dl>
<dt>
</dt><dd>
<pre>
  cptsvg -p old.cpt | tidy -xml -indent -o new.svg
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-tidy/">tidy</a></code>(1). </p>
