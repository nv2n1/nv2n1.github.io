---
title: "chklref(1)"
name: "chklref"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chklref/"
description: "chklref – manual page for chklref 3.1.2"
---

<h2 class="name">NAME</h2>
<p> chklref &#8211; manual page for chklref 3.1.2 </p>
<h2>SYNOPSIS</h2>
<p> <code>chklref</code> [<i>,options/</i>] <i>,texfile/</i></p>
<h2>DESCRIPTION</h2>
<p> Check unused labels and bibitems in a LaTeX file</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;tex</code> &lt;compiler&gt;, <code>-t</code></p>
<dd> Specify the TeX compiler to be used. Default is `pdflatex`.</p>
<dt><code>&#8211;tex-options</code></p>
<dd> List of options to pass to the TeX compiler. It should be a quoted string of white space delimited options. Note that we always add `-interaction nonstopmode` on top of these options.</p>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> Run in debug mode. Do not clean the generated `.chk` file.</p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> Run in quiet mode. Do not print the output of the TeX compiler.</p>
<dt><code>&#8211;parse-only</code></p>
<dd> Do not run the LaTeX compiler but use the already existing `.chk` file. When this option is passed, the following other options are meaningless: `&#8211;tex`, `&#8211;tex-options`, `&#8211;quiet`, `&#8211;debug`.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Print the version of this script.</p>
<dt><code>&#8211;help</code>,h</p>
<dd> Print this help.</dl>
<h2>AUTHOR</h2>
<p> Written by Jerome Lelong &lt;jerome.lelong [at] gmail.com&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/jlelong/chklref.">https://github.com/jlelong/chklref.</a> `chklref` is known not to work with `cleveref`. If you would like to contribute to `chklref`, feel free to open a PR on <a rel="nofollow" href="https://github.com/jlelong/chklref.">https://github.com/jlelong/chklref.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2005-2019 Jerome Lelong &lt;jerome.lelong [at] gmail.com&gt;. This program comes with ABSOLUTELY NO WARRANTY.<br />
 This is free software, and you are welcome to redistribute it under GPLv3.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>chklref</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>chklref</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info chklref</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
