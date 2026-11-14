---
title: "texi2dvi4a2ps(1)"
name: "texi2dvi4a2ps"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texi2dvi4a2ps/"
description: "texi2dvi4a2ps – Compile Texinfo and LaTeX files to DVI or PDF"
---

<h2 class="name">NAME</h2>
<p> texi2dvi4a2ps &#8211; Compile Texinfo and LaTeX files to DVI or PDF </p>
<h2>SYNOPSIS</h2>
<p> <code>texi2dvi4a2ps</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run each Texinfo or LaTeX FILE through TeX in turn until all cross-references are resolved, building all indices. The directory containing each FILE is searched for included files. The suffix of FILE is used to determine its language (LaTeX or Texinfo). </p>
<p> Makeinfo is used to perform Texinfo macro expansion before running TeX when needed.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd> no interaction</p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> remove all auxiliary files</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> turn on shell debugging (set <code>-x</code>)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit successfully</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>OFILE</i></p>
<dd> leave output in OFILE (implies <code>&#8211;clean</code>); Only one input FILE may be specified in this case</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> no output unless errors (implies <code>&#8211;batch</code>)</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> same as <code>&#8211;quiet</code></p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display version information and exit successfully</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> report on what is done</dl>
<h3>TeX tuning:</h3>
<dl>
<dt>-@</p>
<dd> use @input instead of \input; for preloaded Texinfo</p>
<dt><code>-e</code>, <code>&#8211;expand</code></p>
<dd> force macro expansion using makeinfo</p>
<dt><code>-I</code> DIR</p>
<dd> search DIR for Texinfo files</p>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>LANG</i></p>
<dd> specify the LANG of FILE (LaTeX or Texinfo)</p>
<dt><code>-p</code>, <code>&#8211;pdf</code></p>
<dd> use pdftex or pdflatex for processing</p>
<dt><code>-t</code>, <code>&#8211;texinfo</code>=<i>CMD</i></p>
<dd> insert CMD after @setfilename in copy of input file multiple values accumulate</dl>
<p> The values of the BIBTEX, LATEX (or PDFLATEX), MAKEINDEX, MAKEINFO, TEX (or PDFTEX), and TEXINDEX environment variables are used to run those commands, if they are set.</p>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to &lt;bug-texinfo [at] gnu.org&gt;, general questions and discussion to &lt;help-texinfo [at] gnu.org&gt;. Texinfo home page: <a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002 Free Software Foundation, Inc. There is NO warranty. You may redistribute this software under the terms of the GNU General Public License. For more information about these matters, see the files named COPYING.</p>
<h2>SEE ALSO</h2>
<p> texi2dvi4a2ps is exactly the same script as texi2dvi, part of the package GNU Texinfo. It is used by a2ps when delegating LaTeX and Texinfo files. Instead of checking whether the version of texi2dvi which is installed is recent enough, it is more convenient for the users that a2ps is shipped with the version of texi2dvi it requires. <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>texi2dvi</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>texi2dvi</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info texi2dvi</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
