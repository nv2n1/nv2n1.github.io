---
title: "rubber-pipe(1)"
name: "rubber-pipe"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rubber-pipe/"
description: "rubber – a building system for LaTeX documents"
---

<h2>NAME</h2>
<p> rubber &#8211; a building system for LaTeX documents </p>
<h2>SYNOPSIS</h2>
<p> <code>rubber</code> [<i>options</i>] <i>sources &#8230;</i><br />
 <code>rubber-pipe</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> Rubber is a wrapper for LaTeX and companion programs. Its purpose is, given a LaTeX source to process, to compile it enough times to resolve all references, possibly running satellite programs such as BibTeX, makeindex, Metapost, etc. to produce appropriate data files. </p>
<p> The command <code>rubber</code> builds the specified documents completely. The source files may be either LaTeX sources (in which case the suffix .tex may be omitted) or documents in a format Rubber knows how to translate into LaTeX (this currently means CWEB or Literate Haskell documents). If one compilation fails, the whole process stops, including the compilation of the next documents on the command line, and <code>rubber</code> returns a non-zero exit code. </p>
<p> The command <code>rubber-pipe</code> does the same for one document but it reads the LaTeX source from standard input and dumps the compiled document on standard output. </p>
<p> Some information cannot be extracted from the LaTeX sources. This is the case, for instance, with the search paths (which can be specified in environment variables like TEXINPUTS), or the style to be used with Makeindex. To address this problem, one can add information for Rubber in the comments of the LaTeX sources, see section Directives. </p>
<h2>OPTIONS</h2>
<p> The options are used either to choose the action to be performed or to configure the building process. They are mostly the same in <code>rubber</code> and <code>rubber-pipe</code>. Options are parsed using GNU Getopt conventions.</p>
<dl>
<dt><code>&#8211;cache</code></p>
<dd> Use the experimental cache system. This uses a file <i>rubber.cache</i> in the current directory to store the results of parsing and dependency analysis, so that subsequent compilations are faster.</p>
<dt><code>&#8211;clean</code></p>
<dd> Remove all files produced by the compilation, instead of building the document. This option is present in <code>rubber</code> only. It applies to the compilation as it would be done with the other options of the command line, i.e. saying &quot;rubber &#8211;clean foo&quot; will not delete foo.ps, while saying &quot;rubber &#8211;ps &#8211;clean foo&quot; will.</p>
<dt><code>-c, &#8211;command</code><i>&nbsp;<wbr>&lt;command&gt;</i></p>
<dd> Execute the specified command (or directive) <i>before</i> parsing the input files. See section &quot;Directives&quot; for details.</p>
<dt><code>-e, &#8211;epilogue</code><i>&nbsp;<wbr>&lt;command&gt;</i></p>
<dd> Execute the specified command (or directive) <i>after</i> parsing the input files. See section &quot;Directives&quot; for details.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force at least one compilation of the source. This may be useful, for instance, if some unusual dependency was modified (e.g. a package in a system directory). This option is irrelevant in <code>rubber-pipe</code>.</p>
<dt><code>-z, &#8211;gzip</code></p>
<dd> Compress the final document (in <i>gzip</i> format). This is equivalent to saying <i>-o gz</i> after all other options.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display the list of all available options and exit nicely.</p>
<dt><code>&#8211;inplace</code></p>
<dd> Go to the directory of the source files before compiling, so that compilation results are in the same place as their sources.</p>
<dt><code>&#8211;into</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Go to the specified directory before compiling, so that all files are produced there and not in the current directory.</p>
<dt><code>-k, &#8211;keep</code></p>
<dd> This option is used in <code>rubber-pipe</code> only. With this option, the temporary files will not be removed after compiling the document and dumping the results on standard output. The temporary document is named rubtmpX.tex, where X is a number such that no file of that name exists initially.</p>
<dt><code>-l, &#8211;landscape</code></p>
<dd> Specify that the final document should use landscape orientation. This is relevant only when using <code>dvips</code> or <code>dvipdfm</code>.</p>
<dt><code>-n, &#8211;maxerr</code><i>&nbsp;<wbr>&lt;num&gt;</i></p>
<dd> Set the maximum number of displayed errors. By default, up to 10 errors are reported, saying <i>-n -1</i> displays all errors.</p>
<dt><code>-m, &#8211;module</code><i>&nbsp;<wbr>&lt;module&gt;</i><code>[:</code><i>&lt;args&gt;</i><code>]</code></p>
<dd> Use the specified module in addition to the document&#8217;s packages. Arguments can be passed to the package by adding them after a colon, they correspond to the package options in LaTeX. The module is loaded <i>before</i> parsing the document&#8217;s sources.</p>
<dt><code>&#8211;only</code><i>&nbsp;<wbr>&lt;sources&gt;</i></p>
<dd> Compile the document partially, including only the specified sources. This works by inserting a call to \includeonly on the command line. The argument is a comma-separated list of file names.</p>
<dt><code>-o, &#8211;post</code>&nbsp;<wbr>&lt;module&gt;<code>[:</code>&lt;args&gt;<code>]</code></p>
<dd> Use the specified module as a post-processor. This is similar to the <i>-m</i> options except that the module is loaded <i>after</i> parsing the document.</p>
<dt><code>-d, &#8211;pdf</code></p>
<dd> Produce PDF output. When this option comes after <i>&#8211;ps</i> (for instance in the form <i>-pd</i>) it is a synonym for <i>-o ps2pdf</i>, otherwise it acts as <i>-m pdftex</i>, in order to use pdfLaTeX instead of LaTeX.</p>
<dt><code>-p, &#8211;ps</code></p>
<dd> Process the DVI produced by the process through <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1) to produce a PostScript document. This option is a synonym for <i>-o dvips</i>, it cannot come after <i>&#8211;pdf</i>.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Decrease the verbosity level. This is the reverse of <i>-v</i>.</p>
<dt><code>-r, &#8211;read</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Read additional directives form the specified file (see also the directive &quot;read&quot;).</p>
<dt><code>-s, &#8211;short</code></p>
<dd> Display LaTeX&#8217;s error messages in a compact form (one error per line).</p>
<dt><code>-I, &#8211;texpath</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Add the specified directory to TeX&#8217;s search path.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase the verbosity level. Levels between 0 and 4 exist, the default level is 1 for <code>rubber</code> and 0 for <code>rubber-pipe</code>. Beware, saying <i>-vvv</i> makes Rubber speak a lot.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit nicely.</p>
<dt><code>-W, &#8211;warn</code><i>&nbsp;<wbr>&lt;type&gt;</i></p>
<dd> Report information of the given type if there was no error during compilation. The available types are: <code>boxes</code> (overfull and underfull boxes), <code>refs</code> (undefined or multiply defined references), <code>misc</code> (other warnings) and <code>all</code> to report all warnings.</dl>
<h2>MODULES</h2>
<p> Rubber&#8217;s action is influenced by modules. Modules take care of the particular features of packages and external programs. </p>
<h3>Packages</h3>
<p> For every package that a document uses, Rubber looks for a module of the same name to perform the tasks that this package my require apart from the compilation by LaTeX. Modules can be added to the ones provided by default to include new features (this is the point of the module system). The standard modules are the following:</p>
<dl>
<dt><code>beamer</code></p>
<dd> This module handles Beamer&#8217;s extra files the same way as other tables of contents.</p>
<dt><code>bibtex</code></p>
<dd> Takes care of processing the document&#8217;s bibliography with BibTeX when needed. This module is automatically loaded if the document contains the macro ibliography (see also in &quot;Directives&quot; for options).</p>
<dt><code>combine</code></p>
<dd> The combine package is used to gather several LaTeX documents into a single one, and this module handles the dependencies in this case.</p>
<dt><code>epsfig</code></p>
<dd> This modules handles graphics inclusion for the documents that use the old style \psfig macro. It is actually an interface for the graphics module, see this one for details.</p>
<dt><code>graphics, graphicx</code></p>
<dd> These modules identify the graphics included in the document and consider them as dependencies for compilation. They also use standard rules to build these files with external programs. See the info documentation for details.</p>
<dt><code>hyperref</code></p>
<dd> Handle the extra files that this package produces in some cases.</p>
<dt><code>index, makeidx</code></p>
<dd> Process the document&#8217;s index (or indexes) with <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1) when needed (see section &quot;Directives&quot; for options).</p>
<dt><code>minitoc, minitoc-hyper</code></p>
<dd> On cleaning, remove additional files that produced to make partial tables of contents.</p>
<dt><code>moreverb, verbatim</code></p>
<dd> Adds the files included with erbatiminput and similar macros to the list of dependencies.</p>
<dt><code>multibib</code></p>
<dd> Handles the extra bibliographies that this package creates, and removes the extra files on cleaning.</p>
<dt><code>natbib</code></p>
<dd> May cause an extra compilation to solve references.</p>
<dt><code>xr</code></p>
<dd> Add additional .aux files used for external references to the list of dependencies, so recompiling is automatic when referenced document are changed.</dl>
<h3>Pre-processing</h3>
<p> The following modules are provided for using programs that generate a LaTeX source from a different file format:</p>
<dl>
<dt><code>cweb</code></p>
<dd> This module&#8217;s purpose is to run <code><a href="/docs/linux/man/1-cweave/">cweave</a></code>(1) if needed before the compiling process to produce the LaTeX source. This module is automatically loaded if the file specified on the command line has <code>.w</code> as its suffix.</p>
<dt><code>lhs2TeX</code></p>
<dd> This module uses the <code>lhs2TeX</code> preprocessor to generate the LaTeX source from a Literate Haskell program. It is automatically triggered if the input file&#8217;s name ends with <code>.lhs</code>.</dl>
<h3>Post-processing</h3>
<p> The following modules are provided to support different kinds of post-processings. Note that the order matters when using these modules: if you want to use a processing chain like</p>
<dl>
<dt>
<dd> foo.tex -&gt; foo.dvi -&gt; foo.ps -&gt; foo.pdf -&gt; foo.pdf.gz</dl>
<p> you have to load the modules <code>dvips</code>, <code>ps2pdf</code> and <code>gz</code> in that order, for instance using the command line</p>
<dl>
<dt>
<dd> rubber -p -o ps2pdf -z foo.tex</dl>
<dl>
<dt><code>dvipdfm</code></p>
<dd> Runs <code><a href="/docs/linux/man/1-dvipdfm/">dvipdfm</a></code>(1) at the end of compilation to produce a PDF document.</p>
<dt><code>dvips</code></p>
<dd> Runs <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1) at the end of compilation to produce a PostScript document. This module is also loaded by the command line option <i>&#8211;ps</i>.</p>
<dt><code>expand</code></p>
<dd> Produce an expanded LaTeX source by replacing \input macros by included files, bibliography macros by the bibliography produced by <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1), and local classes and packages by their source. If the main file is <i>foo.tex</i> then then expanded file will be named <i>foo-final.tex</i>. See the info documentation for details.</p>
<dt><code>gz</code></p>
<dd> Produce a version of the final file compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1).</p>
<dt><code>ps2pdf</code></p>
<dd> Assuming that the compilation produces a PostScript document (for instance using module <code>dvips</code>), convert this document to PDF using <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1).</dl>
<h3>Compiler choice</h3>
<p> The following modules are used to change the LaTeX compiler:</p>
<dl>
<dt><code>aleph</code></p>
<dd> Use the Aleph compiler instead of TeX, i.e. compiles the document using <code><a href="/docs/linux/man/1-lamed/">lamed</a></code>(1) instead of <code>latex</code>.</p>
<dt><code>etex</code></p>
<dd> Instructs Rubber to use <code><a href="/docs/linux/man/1-elatex/">elatex</a></code>(1) instead of <code>latex</code>.</p>
<dt><code>omega</code></p>
<dd> Use the Omega compiler instead of TeX, i.e. compiles the document using <code><a href="/docs/linux/man/1-lambda/">lambda</a></code>(1) instead of <code>latex</code>. If the module <code>dvips</code> is used too, it will use <code><a href="/docs/linux/man/1-odvips/">odvips</a></code>(1) to translate the DVI file. Note that this module is triggered automatically when the document uses the package <code>omega</code>.</p>
<dt><code>pdftex</code></p>
<dd> Instructs Rubber to use <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1) instead of <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) to compile the document. By default, this produces a PDF file instead of a DVI, but when loading the module with the option <code>dvi</code> (for instance by saying <i>-m pdftex:dvi</i>) the document is compiled into DVI using <code>pdflatex</code>. This module is also loaded by the command line option <i>&#8211;pdf</i>.</p>
<dt><code>vtex</code></p>
<dd> Instructs Rubber to use the VTeX compiler. By default this uses <code>vlatex</code> as the compiler to produce PDF output. With the option <code>ps</code> (e.g. when saying &quot;rubber -m vtex:ps foo.tex&quot;) the compiler used is <code>vlatexp</code> and the result is a PostScript file.</dl>
<h2>DIRECTIVES</h2>
<p> The automatic behavior of Rubber is based on searching for macros in the LaTeX sources. When this is not enough, directives can be added in the comments of the sources. A directive is a line like</p>
<dl>
<dt>
<dd> % rubber: cmd args</dl>
<p> The line must begin with a &quot;%&quot;, then any sequence of &quot;%&quot; signs and spaces, then the text &quot;rubber:&quot; followed by spaces and a command name, possibly followed by spaces and arguments. </p>
<h3>General directives</h3>
<dl>
<dt><code>alias</code><i>&nbsp;<wbr>&lt;name1&gt;&nbsp;<wbr>&lt;name2&gt;</i></p>
<dd> Pretend that the LaTeX macro <i>name1</i> is equivalent to <i>name2</i>. This can be useful when defining wrappers around supported macros.</p>
<dt><code>clean</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Indicates that the specified file should be removed when cleaning using <i>&#8211;clean</i>.</p>
<dt><code>depend</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Consider the specified file as a dependency, so that its modification time will be checked.</p>
<dt><code>make</code><i>&nbsp;<wbr>&lt;file&gt;</i><code>&nbsp;<wbr>[</code><i>&lt;options&gt;</i><code>]</code></p>
<dd> Declare that the specified file has to be generated. Options can specify the way it should be produced, the available options are <code>from</code><i>&nbsp;<wbr>&lt;file&gt;</i> to specify the source and <code>with</code><i>&nbsp;<wbr>&lt;rule&gt;</i> to specify the conversion rule. For instance, saying &quot;make foo.pdf from foo.eps&quot; indicates that <i>foo.pdf</i> should be produced from <i>foo.eps</i>, with any conversion rule that can do it. See the info documentation for details on file conversion.</p>
<dt><code>module</code><i>&nbsp;<wbr>&lt;module&gt;</i><code>&nbsp;<wbr>[</code><i>&lt;options&gt;</i><code>]</code></p>
<dd> Loads the specified module, possibly with options. This is equivalent to the command-line option <i>&#8211;module</i>.</p>
<dt><code>onchange</code><i>&nbsp;<wbr>&lt;file&gt;&nbsp;<wbr>&lt;command&gt;</i></p>
<dd> Execute the specified shell command after compiling if the contents of the specified file have changed. The file name ends at the first space.</p>
<dt><code>paper</code><i>&nbsp;<wbr>&lt;options&gt;</i></p>
<dd> Specify options related to paper size. Currently they are used to give <i>-t</i> options to <code>dvips</code> and <i>-p</i> options to <code>dvipdfm</code>.</p>
<dt><code>path</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Adds the specified directory to the search path for TeX (and Rubber). The name of the directory is everything that follows the spaces after &quot;path&quot;.</p>
<dt><code>read</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Read the specified file of directives. The file must contain one directive per line. Empty lines and lines that begin with &quot;%&quot; are ignored.</p>
<dt><code>rules</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Read extra conversion rules from the specified file. The format of this file is the same as that of <i>rules.ini</i>, see the info documentation for details.</p>
<dt><code>set</code><i>&nbsp;<wbr>&lt;name&gt;&nbsp;<wbr>&lt;value&gt;</i></p>
<dd> Set the value of a variable. For details on the existing variables and their meaning, see the info documentataion.</p>
<dt><code>watch</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Watch the specified file for changes. If the contents of this file has changed after a compilation, then another compilation is triggered. This is useful in the case of tables of contents, for instance.</dl>
<h3>Module-specific directives</h3>
<p> If a command has the form <i>foo.bar</i>, it is considered a command <i>bar</i> for the module <i>foo</i>. If this module is not registered when the directive is found, then the command is silently ignored. For the standard modules, the directives are the following:</p>
<dl>
<dt><code>bibtex.path</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Adds the specified directory to the search path for BibTeX databases (.bib files).</p>
<dt><code>bibtex.sorted</code><i>&nbsp;<wbr>&lt;boolean&gt;</i></p>
<dd> If the argument is <i>true</i>, <i>yes</i> or <i>1</i>, declare that the bibliography is sorted (this is the default), otherwise declare that the citations appear in the same order as in the text. This may require additional calls to <code>bibtex</code>.</p>
<dt><code>bibtex.stylepath</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Adds the specified directory to the search path for BibTeX styles (.bst files).</p>
<dt><code>dvipdfm.options</code><i>&nbsp;<wbr>&lt;options&gt;</i></p>
<dd> Pass the specified command-line switches to <code>dvipdfm</code>.</p>
<dt><code>dvips.options</code><i>&nbsp;<wbr>&lt;options&gt;</i></p>
<dd> Pass the specified command-line switches to <code>dvips</code>.</p>
<dt><code>index.tool</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;name&gt;</i></p>
<dd> Specifies which tool is to be used to process the index. The currently supported tools are <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1) (the default choice) and <code><a href="/docs/linux/man/1-xindy/">xindy</a></code>(1). The argument <i>index</i> is optional, it may be used to specify the list of indexes the command applies to. When present, it must be enclosed in parentheses; the list is comma-separated. When the argument is not present, the command applies to all indices.</p>
<dt><code>index.language</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;language&gt;</i></p>
<dd> Selects the language used for sorting the index. This only applies when using <code><a href="/docs/linux/man/1-xindy/">xindy</a></code>(1) as the indexing tool. The optional argument has the same semantics as above.</p>
<dt><code>index.modules</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;module&gt;&#8230;</i></p>
<dd> Specify which modules to use when processing an index with <code><a href="/docs/linux/man/1-xindy/">xindy</a></code>(1). The optional argument has the same semantics as above.</p>
<dt><code>index.order</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;options&gt;</i></p>
<dd> Modifies the sorting options for the indexes. The arguments are words (separated by spaces) among <i>standard</i>, <i>german</i> and <i>letter</i>. This only applies when using <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1). The optional argument has the same semantics as above.</p>
<dt><code>index.path</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd> Adds the specified directory to the search path for index styles (.ist files). The optional argument has the same semantics as above.</p>
<dt><code>index.style</code><i>&nbsp;<wbr>(index)&nbsp;<wbr>&lt;style&gt;</i></p>
<dd> Specifies the index style to be used. The optional argument has the same semantics as above.</p>
<dt><code>makeidx.language, .modules, .order, .path, .style, .tool</code></p>
<dd> These directives are the same as for the <code>index</code> module, except that they don&#8217;t accept the optional argument.</dl>
<h2>BUGS</h2>
<p> There are surely a some&#8230; </p>
<p> This page documents Rubber version 1.1. The program and this man-page are maintained by Emmanuel Beffara &lt;manu [at] beffara.org&gt;. The homepage for Rubber can be found at <a rel="nofollow" href="http://www.pps.jussieu.fr/~beffara/soft/rubber/.">http://www.pps.jussieu.fr/~beffara/soft/rubber/.</a> </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>rubber</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>rubber</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rubber</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
