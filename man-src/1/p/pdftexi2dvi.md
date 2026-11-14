---
title: "pdftexi2dvi(1)"
name: "pdftexi2dvi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftexi2dvi/"
description: "texi2dvi – convert Texinfo documents to DVI or PDF"
---

<h2 class="name">NAME</h2>
<p> texi2dvi &#8211; convert Texinfo documents to DVI or PDF </p>
<h2>SYNOPSIS</h2>
<p> <code>texi2dvi</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;<br />
 <code>texi2pdf</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;<br />
 <code>pdftexi2dvi</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run each Texinfo or (La)TeX FILE through TeX in turn until all cross-references are resolved, building all indices. The directory containing each FILE is searched for included files. The suffix of FILE is used to determine its language ((La)TeX or Texinfo). To process (e)plain TeX files, set the environment variable LATEX=tex. </p>
<p> When invoked as `texi2pdf&#8217; or given the option <code>&#8211;pdf</code> generate PDF output. Otherwise, generate DVI.</p>
<h3>General options:</h3>
<dl>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> turn on shell debugging (set <code>-x</code>)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit successfully</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,OFILE/</i></p>
<dd> leave output in OFILE; only one input FILE is allowed</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> no output unless errors</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display version information and exit successfully</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> report on what is done</p>
<dt><code>&#8211;max-iterations</code>=<i>,N/</i></p>
<dd> don&#8217;t process files more than N times [7]</p>
<dt><code>&#8211;mostly-clean</code></p>
<dd> remove auxiliary files or directories from previous runs (but not the output)</dl>
<h3>Output format:</h3>
<dl>
<dt><code>&#8211;dvi</code></p>
<dd> output a DVI file [default]</p>
<dt><code>&#8211;dvipdf</code></p>
<dd> output a PDF file via DVI (using a dvi-to-pdf program)</p>
<dt><code>&#8211;html</code></p>
<dd> output an HTML file from LaTeX, using HeVeA</p>
<dt><code>&#8211;info</code></p>
<dd> output an Info file from LaTeX, using HeVeA</p>
<dt><code>-p</code>, <code>&#8211;pdf</code></p>
<dd> use pdftex or pdflatex for processing</p>
<dt><code>&#8211;ps</code></p>
<dd> output a PostScript file via DVI (using dvips)</p>
<dt><code>&#8211;text</code></p>
<dd> output a plain text file from LaTeX, using HeVeA</dl>
<h3>TeX tuning:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;expand</code></p>
<dd> macro expansion using makeinfo</p>
<dt><code>-I</code> DIR</p>
<dd> search DIR for Texinfo files</p>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>,LANG/</i></p>
<dd> specify LANG for FILE, either latex or texinfo</p>
<dt><code>&#8211;no-line-error</code></p>
<dd> do not pass <code>&#8211;file-line-error</code> to TeX</p>
<dt><code>&#8211;shell-escape</code></p>
<dd> pass <code>&#8211;shell-escape</code> to TeX</p>
<dt><code>&#8211;src-specials</code></p>
<dd> pass <code>&#8211;src-specials</code> to TeX</p>
<dt><code>&#8211;translate-file</code>=<i>,FILE/</i></p>
<dd> use given charset translation file for TeX</p>
<dt><code>-t</code>, <code>&#8211;command</code>=<i>,CMD/</i></p>
<dd> insert CMD in copy of input file</dl>
<h3>Build modes:</h3>
<dl>
<dt><code>&#8211;build</code>=<i>,MODE/</i></p>
<dd> specify the treatment of auxiliary files [local]</p>
<dt><code>&#8211;tidy</code></p>
<dd> same as <code>&#8211;build</code>=<i>,tidy/</i></p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> same as <code>&#8211;build</code>=<i>,clean/</i></p>
<dt><code>&#8211;build-dir</code>=<i>,DIR/</i></p>
<dd> specify where the tidy compilation is performed; implies <code>&#8211;tidy</code>; defaults to TEXI2DVI_BUILD_DIRECTORY [.]</dl>
<p> The MODE specifies where the TeX compilation takes place, and, as a consequence, how auxiliary files are treated. The build mode can also be set using the environment variable TEXI2DVI_BUILD_MODE.</p>
<h3>Valid values of MODE are:</h3>
<dl>
<dt>`local&#8217;</p>
<dd> compile in the current directory, leaving all the auxiliary files around. This is the traditional TeX use.</p>
<dt>`tidy&#8217;</p>
<dd> compile in a local *.t2d directory, where the auxiliary files are left. Output files are copied back to the original file.</p>
<dt>`clean&#8217;</p>
<dd> same as `tidy&#8217;, but remove the auxiliary directory afterwards. Every compilation therefore requires the full cycle.</dl>
<p> The values of these environment variables are used to run the corresponding commands, if they are set:</p>
<dl>
<dt>
<dd> BIBER BIBTEX DVIPDF DVIPS EGREP HEVEA LATEX MAKEINDEX MAKEINFO PDFLATEX PDFTEX SED T4HT TEX TEX4HT TEXINDEX TEXINDY THUMBPDF_CMD</dl>
<p> Regarding <code>&#8211;dvipdf</code>, if DVIPDF is not set in the environment, the following programs are looked for (in this order): dvipdfmx dvipdfm dvipdf dvi2pdf dvitopdf. </p>
<p> If Texinfo is installed on your site, then the command</p>
<dl>
<dt>
<dd> info texi2dvi</dl>
<p> should give you access to more documentation.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-texinfo [at] gnu.org, general questions and discussion to help-texinfo [at] gnu.org.<br />
 GNU Texinfo home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>texi2dvi</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>texi2dvi</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info texi2dvi</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
