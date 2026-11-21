---

title: "gplcpt(1)"
name: "gplcpt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gplcpt/"
description: "gplcpt – convert GIMP colour palette (gpl) to GMT colour palette table (cpt)."
---

<dl>
<dt> <code>gplcpt</code> [-b&nbsp;<wbr><i>rgb</i>] [-f&nbsp;<wbr><i>rgb</i>] [-h] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>file</i>] [-v] [-V] [<i>file</i>]</dt></dl>
<dd>The <code>gplcpt</code> converts <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1) colour palette (gpl) files to the <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1) colour palette table (cpt) format. The output is a piecewise constant (step or discrete) gradient. One could use <code><a href="/docs/linux/man/1-cptcont/">cptcont</a></code>(1) program to convert the output to a continuous cpt file if so desired. </dd>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
</dt><dd> Set the background colour of the output.</dd></dl>
<p> <code>-f</code>, <code>&#8211;foreground</code> <i>rgb</i></p>
<dl>
<dt>
</dt><dd> Set the foreground colour of the output.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Brief help.</dd></dl>
<p> <code>-n</code>, <code>&#8211;nan</code> <i>rgb</i></p>
<dl>
<dt>
</dt><dd> Set the NaN (no data) colour of the output.</dd></dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
</dt><dd> Write the output to <i>file</i>, rather than stdout.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Verbose operation.</dd></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Version information.</dd></dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), <code><a href="/docs/linux/man/1-gmt/">GMT</a></code>(1), <code><a href="/docs/linux/man/1-cptcont/">cptcont</a></code>(1). </p>
