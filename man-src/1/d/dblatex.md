---
title: "dblatex(1)"
name: "dblatex"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dblatex/"
description: "dblatex – convert DocBook to LaTeX, DVI, PostScript, and PDF"
---

<h2 class="name">NAME</h2>
<p> dblatex &#8211; convert DocBook to LaTeX, DVI, PostScript, and PDF </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dblatex</code> [<code>options</code>] {<i>file</i>&nbsp;<wbr>| -}</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page briefly documents the <code>dblatex</code> command. For more details read the PDF manual; see below. </p>
<p> <code>dblatex</code> is a program that transforms your SGML/XML DocBook documents to DVI, PostScript or PDF by translating them into pure LaTeX as a first process. MathML 2.0 markups are supported, too. It started as a clone of DB2LaTeX.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the PDF manual. </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message and exit.</dl>
<p> <code>-b </code><i>backend</i>, <code>&#8211;backend=</code><i>backend</i></p>
<dl>
<dt>
<dd> Backend driver to use: <i>pdftex</i> (default), <i>dvips</i>, or <i>xetex</i>.</dl>
<p> <code>-B</code>, <code>&#8211;no-batch</code></p>
<dl>
<dt>
<dd> All the tex output is printed.</dl>
<p> <code>-c </code><i>config</i>, <code>-S </code><i>config</i>, <code>&#8211;config=</code><i>config</i></p>
<dl>
<dt>
<dd> Configuration file. A configuration file can be used to group all the options and customizations to apply.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Debug mode: Keep the temporary directory in which dblatex actually works.</dl>
<p> <code>-D</code>, <code>&#8211;dump</code></p>
<dl>
<dt>
<dd> Dump the error stack when an error occurs (debug purpose).</dl>
<p> <code>-e </code><i>indexstyle</i>, <code>&#8211;indexstyle </code><i>indexstyle</i></p>
<dl>
<dt>
<dd> Index style file to pass to <code>makeindex</code> instead of the dblatex default index style.</dl>
<p> <code>-f </code><i>figure_format</i>, <code>&#8211;fig-format=</code><i>figure_format</i></p>
<dl>
<dt>
<dd> Input figure format: <i>fig</i>, <i>eps</i>. Used when not deduced from figure file extension.</dl>
<p> <code>-F </code><i>input_format</i>, <code>&#8211;input-format=</code><i>input_format</i></p>
<dl>
<dt>
<dd> Input file format: <i>sgml</i>, <i>xml</i> (default).</dl>
<p> <code>-i </code><i>texinputs</i>, <code>&#8211;texinputs </code><i>texinputs</i></p>
<dl>
<dt>
<dd> Path added to <code>TEXINPUTS</code></dl>
<p> <code>-I </code><i>figure_path</i>, <code>&#8211;fig-path=</code><i>figure_path</i></p>
<dl>
<dt>
<dd> Additional lookup path of the figures.</dl>
<p> <code>-l </code><i>bst_path</i>, <code>&#8211;bst-path=</code><i>bst_path</i></p>
<dl>
<dt>
<dd> Additional lookup path of the BibTeX styles.</dl>
<p> <code>-L </code><i>bib_path</i>, <code>&#8211;bib-path=</code><i>bib_path</i></p>
<dl>
<dt>
<dd> Additional lookup path of the BibTeX databases.</dl>
<p> <code>-m </code><i>xslt</i>, <code>&#8211;xslt=</code><i>xslt</i></p>
<dl>
<dt>
<dd> XSLT engine to use. The available engines are: xsltproc (default), 4xslt.</dl>
<p> <code>-o </code><i>output</i>, <code>&#8211;output=</code><i>output</i></p>
<dl>
<dt>
<dd> Output filename. When not specified, the input filename is used, with the suffix of the output format. The option is ignored if several books are chunked from a set. In this case the <code>-O</code> option is applied instead.</dl>
<p> <code>-O </code><i>output_dir</i>, <code>&#8211;output-dir=</code><i>output_dir</i></p>
<dl>
<dt>
<dd> Output directory of the books built from a set. When not specified, the current working directory is used instead. The option is ignored if a single document is outputed, and the <code>-o</code> is taken into account.</dl>
<p> <code>-p </code><i>xsl_user</i>, <code>&#8211;xsl-user=</code><i>xsl_user</i></p>
<dl>
<dt>
<dd> An XSL user stylesheet to use. Several user stylesheets can be specified, but the option order is meaningful: a user stylesheet takes precedence over previously defined user stylesheets.</dl>
<p> <code>-P </code><i>param</i><code>=</code><i>value</i>, <code>&#8211;param=</code><i>param</i><code>=</code><i>value</i></p>
<dl>
<dt>
<dd> Set an XSL parameter from command line.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Less verbose, showing only TeX output messages and error messages.</dl>
<p> <code>-r </code><i>script</i>, <code>&#8211;texpost=</code><i>script</i></p>
<dl>
<dt>
<dd> Script called at the very end of the tex compilation. Its role is to modify the tex file or one of the compilation files before the last round.</dl>
<p> <code>-s </code><i>latex_style</i>, <code>&#8211;texstyle=</code><i>latex_style</i></p>
<dl>
<dt>
<dd> Latex style to apply. It can be a package name, or directly a latex package path. A package name must be without a directory path and without the &#8216;.sty&#8217; extension. On the contrary, a full latex package path can contain a directory path, but must ends with the &#8216;.sty&#8217; extension.</dl>
<p> <code>-t </code><i>format</i>, <code>&#8211;type=</code><i>format</i></p>
<dl>
<dt>
<dd> Output format. Available formats: <i>tex</i>, <i>dvi</i>, <i>ps</i>, <i>pdf</i> (default).</dl>
<p> <code>&#8211;dvi</code></p>
<dl>
<dt>
<dd> DVI output. Equivalent to <code>-tdvi</code>.</dl>
<p> <code>&#8211;pdf</code></p>
<dl>
<dt>
<dd> PDF output. Equivalent to <code>-tpdf</code>.</dl>
<p> <code>&#8211;ps</code></p>
<dl>
<dt>
<dd> PostScript output. Equivalent to <code>-tps</code>.</dl>
<p> <code>-T </code><i>style</i>, <code>&#8211;style=</code><i>style</i></p>
<dl>
<dt>
<dd> Output style, predefined are: <i>db2latex</i>, <i>simple</i>, <i>native</i> (default).</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the dblatex version.</dl>
<p> <code>-V</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode, showing the running commands</dl>
<p> <code>-x </code><i>xslt_options</i>, <code>&#8211;xslt-opts=</code><i>xslt_options</i></p>
<dl>
<dt>
<dd> Arguments directly passed to the XSLT engine</dl>
<p> <code>-X</code>, <code>&#8211;no-external</code></p>
<dl>
<dt>
<dd> Disable the external text file support. This support is needed for callouts on external files referenced by textdata or imagedata, but it can be disabled if the document does not contain such callouts. Disabling this support can improve the processing performance for big documents.</dl>
<h2>FILES AND DIRECTORIES</h2>
<p> $HOME/.dblatex/</p>
<dl>
<dt>
<dd> User configuration directory.</dl>
<p> /etc/dblatex/</p>
<dl>
<dt>
<dd> System-wide configuration directory.</dl>
<p> The predefined output styles are located in the installed package directory.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>DBLATEX_CONFIG_FILES</code></p>
<dl>
<dt>
<dd> Extra configuration directories that may contain some dblatex configuration files.</dl>
<h2>EXAMPLES</h2>
<p> To produce myfile.pdf from myfile.xml: </p>
<dl>
<dt>
<dd>
<pre>
dblatex myfile.xml
</pre>
</dl>
<p> To set some XSL parameters from the command line: </p>
<dl>
<dt>
<dd>
<pre>
dblatex -P latex.babel.language=de myfile.xml
</pre>
</dl>
<p> To use the db2latex output style: </p>
<dl>
<dt>
<dd>
<pre>
dblatex -T db2latex myfile.xml
</pre>
</dl>
<p> To apply your own latex style: </p>
<dl>
<dt>
<dd>
<pre>
dblatex -s mystyle myfile.xml
dblatex -s /path/to/mystyle.sty myfile.xml
</pre>
</dl>
<p> To pass extra arguments to the XSLT engine: </p>
<dl>
<dt>
<dd>
<pre>
dblatex -x &quot;--path /path/to/load/entity&quot; myfile.xml
</pre>
</dl>
<p> To use <code>dblatex</code> and profiling: </p>
<dl>
<dt>
<dd>
<pre>
xsltproc --param profile.attribute &quot;'output'&quot; \
         --param profile.value &quot;'pdf'&quot; \
         /path/to/profiling/profile.xsl \
         myfile.xml | dblatex -o myfile.pdf -
</pre>
</dl>
<p> To build a set of books: </p>
<dl>
<dt>
<dd>
<pre>
dblatex -O /path/to/chunk/dir -Pset.book.num=all myfile.xml
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> The program is documented fully by &quot;DocBook to LaTeX Publishing &#8211; User Manual&quot; available in the package&#8217;s documentation directory.</p>
<h2>AUTHORS</h2>
<p> <code>Benoit Guillon</code></p>
<dl>
<dt>
<dd> Upstream maintainer</dl>
<p> <code>Andreas Hoenen</code> &lt;andreas.hoenen [at] arcor.de&gt;</p>
<dl>
<dt>
<dd> Debian maintainer</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012 Andreas Hoenen </p>
<p> This manual page was written for the Debian(TM) system (but it may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian(TM) systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
