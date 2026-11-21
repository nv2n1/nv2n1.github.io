---

title: "figtoipe(1)"
name: "figtoipe"
section: "1"
letter: "f"
url: "/docs/linux/man/1-figtoipe/"
description: "figtoipe – Convert FIG figures into Ipe format"
---

<p> figtoipe &#8211; Convert FIG figures into Ipe format </p>
<h2>SYNOPSIS</h2>
<p> <code>figtoipe </code> [-g] [-p <i>preamble</i>] <i>FIGfile</i> <i>XMLfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>figtoipe</code> converts files in FIG format (as created, e.g., by <code>xfig</code>) to Ipe&#8217;s XML format. </p>
<p> <code>figtoipe</code> is not complete. The main lacking feature is the conversion of splines. Arc-boxes are replaced by rectangles. Feel free to improve this version! </p>
<p> The drawing models of FIG and Ipe are somewhat different. Ipe does not support depth ordering independent of grouping, pattern fill, and Postscript fonts. </p>
<p> <code>figtoipe</code> tries to include images specified in the XFIG file. For JPEG pictures, it tries include the compressed image data into the XML file. For files not recognized as JPEG, <code>anytopnm</code> is called; its output is compressed and included in the XML file. Some output of <code>anytopnm</code> might be rejected (e.g. images larger than 5000&#215;5000 pixels or B&amp;W bitmaps), or misunderstood. </p>
<h2>OPTIONS</h2>
<p> <code>-g</code> group the figure in the output XML</p>
<dl>
<dt><code>-p </code><i>latex</i></dt>
<dd> add <i>latex</i> as a preamble to the generated XML file, e.g. </dd>
<pre>
'\usepackage{amsmath}'
</code></pre>
<h2>AUTHORS</h2>
<pre><code>Otfried Cheong
Alexander B[:u]rger &lt;acfb [at] users.sf.net&gt; (image handling)
</code></pre>
<h2>REPORTING BUGS</h2>
<p> Please report bugs using Ipe bugzilla at <i><a rel="nofollow" href="http://tclab.kaist.ac.kr/ipe/bugzilla.html">http://tclab.kaist.ac.kr/ipe/bugzilla.html</a></i> </p>
<h2>SEE ALSO</h2>
<p> More information about Ipe can be found in <i>The Ipe Manual</i>, which can be found in your Ipe installation. </p>
<h2>LICENSE & WARRANTY</h2>
<p> <code>figtoipe</code> comes with ABSOLUTELY NO WARRANTY. It is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> See the file <code>GPL-2</code> accompanying the source for details. </p>
