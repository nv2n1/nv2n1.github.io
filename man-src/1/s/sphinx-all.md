---
title: "sphinx-all(1)"
name: "sphinx-all"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphinx-all/"
description: "sphinx-all – Sphinx documentation generator system manual"
---

<h2>NAME</h2>
<p> sphinx-all &#8211; Sphinx documentation generator system manual</p>
<h2>INTRODUCTION</h2>
<p> This is the documentation for the Sphinx documentation builder. Sphinx is a tool that translates a set of <i>reStructuredText</i> source files into various output formats, automatically producing cross-references, indices etc. That is, if you have a directory containing a bunch of reST-formatted documents (and possibly subdirectories of docs in there as well), Sphinx can generate a nicely-organized arrangement of HTML files (in some other directory) for easy browsing and navigation. But from the same source, it can also generate a LaTeX file that you can compile into a PDF version of the documents, or a PDF file directly using <i>rst2pdf</i>. </p>
<p> The focus is on hand-written documentation, rather than auto-generated API docs. Though there is support for that kind of docs as well (which is intended to be freely mixed with hand-written content), if you need pure API docs have a look at <i>Epydoc</i>, which also understands reST. </p>
<p> For a great &quot;introduction&quot; to writing docs in general &#8212; the whys and hows, see also <i>Write the docs</i>, written by Eric Holscher.</p>
<h3>Conversion from other systems</h3>
<p> This section is intended to collect helpful hints for those wanting to migrate to reStructuredText/Sphinx from other documentation systems.</p>
<dl>
<dt>&bull;</p>
<dd> Gerard Flanagan has written a script to convert pure HTML to reST; it can be found at the <i>Python Package Index</i>.</p>
<dt>&bull;</p>
<dd> For converting the old Python docs to Sphinx, a converter was written which can be found at <i>the Python SVN repository</i>. It contains generic code to convert Python-doc-style LaTeX markup to Sphinx reST.</p>
<dt>&bull;</p>
<dd> Marcin Wojdyr has written a script to convert Docbook to reST with Sphinx markup; it is at <i>Google Code</i>.</p>
<dt>&bull;</p>
<dd> Christophe de Vienne wrote a tool to convert from Open/LibreOffice documents to Sphinx: <i>odt2sphinx</i>.</p>
<dt>&bull;</p>
<dd> To convert different markups, <i>Pandoc</i> is a very helpful tool.</dl>
<h3>Use with other systems</h3>
<p> See the <i>pertinent section in the FAQ list</i>.</p>
<h3>Prerequisites</h3>
<p> Sphinx needs at least <code>Python 2.5</code> or <code>Python 3.1</code> to run, as well as the <i>docutils</i> and <i>Jinja2</i> libraries. Sphinx should work with docutils version 0.7 or some (not broken) SVN trunk snapshot. If you like to have source code highlighting support, you must also install the <i>Pygments</i> library.</p>
<h3>Usage</h3>
<p> See <code>tutorial</code> for an introduction. It also contains links to more advanced sections in this manual for the topics it discusses.</p>
<h2>FIRST STEPS WITH SPHINX</h2>
<p> This document is meant to give a tutorial-like overview of all common tasks while using Sphinx. </p>
<p> The green arrows designate &quot;more info&quot; links leading to advanced sections about the described task.</p>
<h3>Setting up the documentation sources</h3>
<p> The root directory of a Sphinx collection of reStructuredText document sources is called the <i>source directory</i>. This directory also contains the Sphinx configuration file <code>conf.py</code>, where you can configure all aspects of how Sphinx reads your sources and builds your documentation. [1] </p>
<p> Sphinx comes with a script called <code>sphinx-quickstart</code> that sets up a source directory and creates a default <code>conf.py</code> with the most useful configuration values from a few questions it asks you. Just run </p>
<pre>
$ sphinx-quickstart
</pre>
<p> and answer its questions. (Be sure to say yes to the &quot;autodoc&quot; extension.) </p>
<p> There is also an automatic &quot;API documentation&quot; generator called <code>sphinx-apidoc</code>; see <i>invocation-apidoc</i> for details.</p>
<h3>Defining document structure</h3>
<p> Let&#8217;s assume you&#8217;ve run <code>sphinx-quickstart</code>. It created a source directory with <code>conf.py</code> and a master document, <code>index.rst</code> (if you accepted the defaults). The main function of the <i>master document</i> is to serve as a welcome page, and to contain the root of the &quot;table of contents tree&quot; (or <i>toctree</i>). This is one of the main things that Sphinx adds to reStructuredText, a way to connect multiple files to a single hierarchy of documents.</p>
<h3>reStructuredText directives</h3>
<p> <code>toctree</code> is a reStructuredText <i>directive</i>, a very versatile piece of markup. Directives can have arguments, options and content. </p>
<p> <i>Arguments</i> are given directly after the double colon following the directive&#8217;s name. Each directive decides whether it can have arguments, and how many. </p>
<p> <i>Options</i> are given after the arguments, in form of a &quot;field list&quot;. The <code>maxdepth</code> is such an option for the <code>toctree</code> directive. </p>
<p> <i>Content</i> follows the options or arguments after a blank line. Each directive decides whether to allow content, and what to do with it. </p>
<p> A common gotcha with directives is that <code>the first line of the content must be indented to the same level as the options are</code>. </p>
<p> The toctree directive initially is empty, and looks like this: </p>
<pre>
.. toctree::
   :maxdepth: 2
</pre>
<p> You add documents listing them in the <i>content</i> of the directive: </p>
<pre>
.. toctree::
   :maxdepth: 2
   intro
   tutorial
   ...
</pre>
<p> This is exactly how the toctree for this documentation looks. The documents to include are given as <i>document name</i>s, which in short means that you leave off the file name extension and use slashes as directory separators. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>Read more about&nbsp;<wbr><i>the toctree directive</i>. </p>
<p> You can now create the files you listed in the toctree and add content, and their section titles will be inserted (up to the &quot;maxdepth&quot; level) at the place where the toctree directive is placed. Also, Sphinx now knows about the order and hierarchy of your documents. (They may contain <code>toctree</code> directives themselves, which means you can create deeply nested hierarchies if necessary.)</p>
<h3>Adding content</h3>
<p> In Sphinx source files, you can use most features of standard reStructuredText. There are also several features added by Sphinx. For example, you can add cross-file references in a portable way (which works for all output types) using the <code>ref</code> role. </p>
<p> For an example, if you are viewing the HTML version you can look at the source for this document &#8212; use the &quot;Show Source&quot; link in the sidebar. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><i>rst-primer</i>&nbsp;<wbr>for a more in-depth introduction to reStructuredText and <i>sphinxmarkup</i> for a full list of markup added by Sphinx.</p>
<h3>Running the build</h3>
<p> Now that you have added some files and content, let&#8217;s make a first build of the docs. A build is started with the <code>sphinx-build</code> program, called like this: </p>
<pre>
$ sphinx-build -b html sourcedir builddir
</pre>
<p> where <i>sourcedir</i> is the <i>source directory</i>, and <i>builddir</i> is the directory in which you want to place the built documentation. The <i>-b</i> option selects a builder; in this example Sphinx will build HTML files. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><i>invocation</i>&nbsp;<wbr>for all options that&nbsp;<wbr><code>sphinx-build</code> supports. </p>
<p> However, <code>sphinx-quickstart</code> script creates a <code>Makefile</code> and a <code>make.bat</code> which make life even easier for you: with them you only need to run </p>
<pre>
$ make html
</pre>
<p> to build HTML docs in the build directory you chose. Execute <code>make</code> without an argument to see which targets are available.</p>
<dl>
<dt>How do I generate PDF documents?</p>
<dd>
<p> <code>make latexpdf</code> runs the <code>LaTeX builder</code> and readily invokes the pdfTeX toolchain for you.</dl>
<h3>Documenting objects</h3>
<p> One of Sphinx&#8217; main objectives is easy documentation of <i>objects</i> (in a very general sense) in any <i>domain</i>. A domain is a collection of object types that belong together, complete with markup to create and reference descriptions of these objects. </p>
<p> The most prominent domain is the Python domain. To e.g. document the Python built-in function <code>enumerate()</code>, you would add this to one of your source files: </p>
<pre>
.. py:function:: enumerate(sequence[, start=0])
   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)
</pre>
<p> This is rendered like this:</p>
<dl>
<dt><code>enumerate(sequence[, start=0])</code></p>
<dd> Return an iterator that yields tuples of an index and an item of the <i>sequence</i>. (And so on.) </p>
<p> The argument of the directive is the <i>signature</i> of the object you describe, the content is the documentation for it. Multiple signatures can be given, each in its own line. </p>
<p> The Python domain also happens to be the default domain, so you don&#8217;t need to prefix the markup with the domain name: </p>
<pre>
.. function:: enumerate(sequence[, start=0])
   ...
</pre>
<p> does the same job if you keep the default setting for the default domain. </p>
<p> There are several more directives for documenting other types of Python objects, for example <code>py:class</code> or <code>py:method</code>. There is also a cross-referencing <i>role</i> for each of these object types. This markup will create a link to the documentation of <code>enumerate()</code>: </p>
<pre>
The :py:func:`enumerate` function can be used for ...
</pre>
<p> And here is the proof: A link to <code>enumerate()</code>. </p>
<p> Again, the <code>py:</code> can be left out if the Python domain is the default one. It doesn&#8217;t matter which file contains the actual documentation for <code>enumerate()</code>; Sphinx will find it and create a link to it. </p>
<p> Each domain will have special rules for how the signatures can look like, and make the formatted output look pretty, or add specific features like links to parameter types, e.g. in the C/C++ domains. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><i>domains</i>&nbsp;<wbr>for all the available domains and their directives/roles.</dl>
<h3>Basic configuration</h3>
<p> Earlier we mentioned that the <code>conf.py</code> file controls how Sphinx processes your documents. In that file, which is executed as a Python source file, you assign configuration values. For advanced users: since it is executed by Sphinx, you can do non-trivial tasks in it, like extending <code>sys.path</code> or importing a module to find out the version your are documenting. </p>
<p> The config values that you probably want to change are already put into the <code>conf.py</code> by <code>sphinx-quickstart</code> and initially commented out (with standard Python syntax: a <code>#</code> comments the rest of the line). To change the default value, remove the hash sign and modify the value. To customize a config value that is not automatically added by <code>sphinx-quickstart</code>, just add an additional assignment. </p>
<p> Keep in mind that the file uses Python syntax for strings, numbers, lists and so on. The file is saved in UTF-8 by default, as indicated by the encoding declaration in the first line. If you use non-ASCII characters in any string value, you need to use Python Unicode strings (like <code>project = u&#8217;ExposÃ©&#8217;</code>). </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><i>build-config</i>&nbsp;<wbr>for documentation of all available config values.</p>
<h3>Autodoc</h3>
<p> When documenting Python code, it is common to put a lot of documentation in the source files, in documentation strings. Sphinx supports the inclusion of docstrings from your modules with an <i>extension</i> (an extension is a Python module that provides additional features for Sphinx projects) called &quot;autodoc&quot;. </p>
<p> In order to use autodoc, you need to activate it in <code>conf.py</code> by putting the string <code>&#8216;sphinx.ext.autodoc&#8217;</code> into the list assigned to the <code>extensions</code> config value. Then, you have a few additional directives at your disposal. </p>
<p> For example, to document the function <code>io.open()</code>, reading its signature and docstring from the source file, you&#8217;d write this: </p>
<pre>
.. autofunction:: io.open
</pre>
<p> You can also document whole classes or even modules automatically, using member options for the auto directives, like </p>
<pre>
.. automodule:: io
   :members:
</pre>
<p> autodoc needs to import your modules in order to extract the docstrings. Therefore, you must add the appropriate path to <code>sys.path</code> in your <code>conf.py</code>. </p>
<p> <code>WARNING:</code> <code>autodoc</code> <code>imports</code> the modules to be documented. If any modules have side effects on import, these will be executed by <code>autodoc</code> when <code>sphinx-build</code> is run. </p>
<p> If you document scripts (as opposed to library modules), make sure their main routine is protected by a <code>if __name__ == &#8216;__main__&#8217;</code> condition. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><code>sphinx.ext.autodoc</code>&nbsp;<wbr>for the complete description of the features of autodoc.</p>
<h3>Intersphinx</h3>
<p> Many Sphinx documents including the <i>Python documentation</i> are published on the internet. When you want to make links to such documents from your documentation, you can do it with <code>sphinx.ext.intersphinx</code>. </p>
<p> In order to use intersphinx, you need to activate it in <code>conf.py</code> by putting the string <code>&#8216;sphinx.ext.intersphinx&#8217;</code> into the <code>extensions</code> list and set up the <code>intersphinx_mapping</code> config value. </p>
<p> For example, to link to <code>io.open()</code> in the Python library manual, you need to setup your <code>intersphinx_mapping</code> like: </p>
<pre>
intersphinx_mapping = {'python': ('<a rel="nofollow" href="http://docs.python.org/3',">http://docs.python.org/3',</a> None)}
</pre>
<p> And now, you can write a cross-reference like <code>:py:func:`io.open`</code>. Any cross-reference that has no matching target in the current documentation set, will be looked up in the documentation sets configured in <code>intersphinx_mapping</code> (this needs access to the URL in order to download the list of valid targets). Intersphinx also works for some other <i>domains&#8217;</i> roles including <code>:ref:</code>, however it doesn&#8217;t work for <code>:doc:</code> as that is non-domain role. </p>
<p> [image: more info] [image]<br />
&nbsp;<wbr>See&nbsp;<wbr><code>sphinx.ext.intersphinx</code>&nbsp;<wbr>for the complete description of the features of intersphinx.</p>
<h3>More topics to be covered</h3>
<dl>
<dt>&bull;</p>
<dd> Other extensions (math, viewcode, doctest)</p>
<dt>&bull;</p>
<dd> Static files</p>
<dt>&bull;</p>
<dd> Selecting a theme</p>
<dt>&bull;</p>
<dd> Templating</p>
<dt>&bull;</p>
<dd> Using extensions</p>
<dt>&bull;</p>
<dd> Writing extensions</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> This is the usual lay-out. However, <code>conf.py</code> can also live in another directory, the <i>configuration directory</i>. See <i>invocation</i>.</dl>
<h2>INVOCATION OF SPHINX-BUILD</h2>
<p> The <code>sphinx-build</code> script builds a Sphinx documentation set. It is called like this: </p>
<pre>
$ sphinx-build [options] sourcedir builddir [filenames]
</pre>
<p> where <i>sourcedir</i> is the <i>source directory</i>, and <i>builddir</i> is the directory in which you want to place the built documentation. Most of the time, you don&#8217;t need to specify any <i>filenames</i>. </p>
<p> The <code>sphinx-build</code> script has several options:</p>
<dl>
<dt><code>-b buildername</code></p>
<dd> The most important option: it selects a builder. The most common builders are:</p>
<dt><code>html</code></p>
<dd> Build HTML pages. This is the default builder.</p>
<dt><code>dirhtml</code></p>
<dd> Build HTML pages, but with a single directory per document. Makes for prettier URLs (no <code>.html</code>) if served from a webserver.</p>
<dt><code>singlehtml</code></p>
<dd> Build a single HTML with the whole content.</p>
<dt><code>htmlhelp</code>, <code>qthelp</code>, <code>devhelp</code>, <code>epub</code></p>
<dd> Build HTML files with additional information for building a documentation collection in one of these formats.</p>
<dt><code>latex</code></p>
<dd> Build LaTeX sources that can be compiled to a PDF document using <code>pdflatex</code>.</p>
<dt><code>man</code></p>
<dd> Build manual pages in groff format for UNIX systems.</p>
<dt><code>texinfo</code></p>
<dd> Build Texinfo files that can be processed into Info files using <code>makeinfo</code>.</p>
<dt><code>text</code></p>
<dd> Build plain text files.</p>
<dt><code>gettext</code></p>
<dd> Build gettext-style message catalogs (<code>.pot</code> files).</p>
<dt><code>doctest</code></p>
<dd> Run all doctests in the documentation, if the <code>doctest</code> extension is enabled.</p>
<dt><code>linkcheck</code></p>
<dd> Check the integrity of all external links.</p>
<dt><code>xml</code></p>
<dd> Build Docutils-native XML files.</p>
<dt><code>pseudoxml</code></p>
<dd> Build compact pretty-printed &quot;pseudo-XML&quot; files displaying the internal structure of the intermediate document trees. </p>
<p> See <i>builders</i> for a list of all builders shipped with Sphinx. Extensions can add their own builders.</p>
<dt><code>-a</code></p>
<dd> If given, always write all output files. The default is to only write output files for new and changed source files. (This may not apply to all builders.)</p>
<dt><code>-E</code></p>
<dd> Don&#8217;t use a saved <i>environment</i> (the structure caching all cross-references), but rebuild it completely. The default is to only read and parse source files that are new or have changed since the last run.</p>
<dt><code>-t tag</code></p>
<dd> Define the tag <i>tag</i>. This is relevant for <code>only</code> directives that only include their content if this tag is set. </p>
<p> New in version 0.6. </p>
<dt><code>-d path</code></p>
<dd> Since Sphinx has to read and parse all source files before it can write an output file, the parsed source files are cached as &quot;doctree pickles&quot;. Normally, these files are put in a directory called <code>.doctrees</code> under the build directory; with this option you can select a different cache directory (the doctrees can be shared between all builders).</p>
<dt><code>-j N</code></p>
<dd> Distribute the build over <i>N</i> processes in parallel, to make building on multiprocessor machines more effective. Note that not all parts and not all builders of Sphinx can be parallelized. </p>
<p> New in version 1.2: This option should be considered <i>experimental</i>. </p>
<dt><code>-c path</code></p>
<dd> Don&#8217;t look for the <code>conf.py</code> in the source directory, but use the given configuration directory instead. Note that various other files and paths given by configuration values are expected to be relative to the configuration directory, so they will have to be present at this location too. </p>
<p> New in version 0.3. </p>
<dt><code>-C</code></p>
<dd> Don&#8217;t look for a configuration file; only take options via the <code>-D</code> option. </p>
<p> New in version 0.5. </p>
<dt><code>-D setting=value</code></p>
<dd> Override a configuration value set in the <code>conf.py</code> file. The value must be a string or dictionary value. For the latter, supply the setting name and key like this: <code>-D latex_elements.docclass=scrartcl</code>. For boolean values, use <code>0</code> or <code>1</code> as the value. </p>
<p> Changed in version 0.6: The value can now be a dictionary value. </p>
<dt><code>-A name=value</code></p>
<dd> Make the <i>name</i> assigned to <i>value</i> in the HTML templates. </p>
<p> New in version 0.5. </p>
<dt><code>-n</code></p>
<dd> Run in nit-picky mode. Currently, this generates warnings for all missing references. See the config value <code>nitpick_ignore</code> for a way to exclude some references as &quot;known missing&quot;.</p>
<dt><code>-N</code></p>
<dd> Do not emit colored output. (On Windows, colored output is disabled in any case.)</p>
<dt><code>-v</code></p>
<dd> Increase verbosity (loglevel). This option can be given up to three times to get more debug logging output. It implies <i>-T</i>. </p>
<p> New in version 1.2. </p>
<dt><code>-q</code></p>
<dd> Do not output anything on standard output, only write warnings and errors to standard error.</p>
<dt><code>-Q</code></p>
<dd> Do not output anything on standard output, also suppress warnings. Only errors are written to standard error.</p>
<dt><code>-w file</code></p>
<dd> Write warnings (and errors) to the given file, in addition to standard error.</p>
<dt><code>-W</code></p>
<dd> Turn warnings into errors. This means that the build stops at the first warning and <code>sphinx-build</code> exits with exit status 1.</p>
<dt><code>-T</code></p>
<dd> Display the full traceback when an unhandled exception occurs. Otherwise, only a summary is displayed and the traceback information is saved to a file for further analysis. </p>
<p> New in version 1.2. </p>
<dt><code>-P</code></p>
<dd> (Useful for debugging only.) Run the Python debugger, <code>pdb</code>, if an unhandled exception occurs while building.</p>
<dt><code>-h, &#8211;help, &#8211;version</code></p>
<dd> Display usage summary or Sphinx version. </p>
<p> New in version 1.2. </p>
<p> You can also give one or more filenames on the command line after the source and build directories. Sphinx will then try to build only these output files (and their dependencies).</dl>
<h3>Makefile options</h3>
<p> The <code>Makefile</code> and <code>make.bat</code> files created by <code>sphinx-quickstart</code> usually run <code>sphinx-build</code> only with the <i>-b</i> and <i>-d</i> options. However, they support the following variables to customize behavior:</p>
<dl>
<dt><code>PAPER</code></p>
<dd> The value for <code>latex_paper_size</code>.</p>
<dt><code>SPHINXBUILD</code></p>
<dd> The command to use instead of <code>sphinx-build</code>.</p>
<dt><code>BUILDDIR</code></p>
<dd> The build directory to use instead of the one chosen in <code>sphinx-quickstart</code>.</p>
<dt><code>SPHINXOPTS</code></p>
<dd> Additional options for <code>sphinx-build</code>.</dl>
<h2>INVOCATION OF SPHINX-APIDOC</h2>
<p> The <code>sphinx-apidoc</code> generates completely automatic API documentation for a Python package. It is called like this: </p>
<pre>
$ sphinx-apidoc [options] -o outputdir packagedir [pathnames]
</pre>
<p> where <i>packagedir</i> is the path to the package to document, and <i>outputdir</i> is the directory where the generated sources are placed. Any <i>pathnames</i> given are paths to be excluded ignored during generation. </p>
<p> <code>WARNING:</code> <code>sphinx-apidoc</code> generates reST files that use <code>sphinx.ext.autodoc</code> to document all found modules. If any modules have side effects on import, these will be executed by <code>autodoc</code> when <code>sphinx-build</code> is run. </p>
<p> If you document scripts (as opposed to library modules), make sure their main routine is protected by a <code>if __name__ == &#8216;__main__&#8217;</code> condition. </p>
<p> The <code>sphinx-apidoc</code> script has several options:</p>
<dl>
<dt><code>-o outputdir</code></p>
<dd> Gives the directory in which to place the generated output.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Normally, sphinx-apidoc does not overwrite any files. Use this option to force the overwrite of all files that it generates.</p>
<dt><code>-n, &#8211;dry-run</code></p>
<dd> With this option given, no files will be written at all.</p>
<dt><code>-s suffix</code></p>
<dd> This option selects the file name suffix of output files. By default, this is <code>rst</code>.</p>
<dt><code>-d maxdepth</code></p>
<dd> This sets the maximum depth of the table of contents, if one is generated.</p>
<dt><code>-l, &#8211;follow-links</code></p>
<dd> This option makes sphinx-apidoc follow symbolic links when recursing the filesystem to discover packages and modules. You may need it if you want to generate documentation from a source directory managed by <i>collective.recipe.omelette</i>. By default, symbolic links are skipped. </p>
<p> New in version 1.2. </p>
<dt><code>-T, &#8211;no-toc</code></p>
<dd> This prevents the generation of a table-of-contents file <code>modules.rst</code>. This has no effect when <i>&#8211;full</i> is given.</p>
<dt><code>-F, &#8211;full</code></p>
<dd> This option makes sphinx-apidoc create a full Sphinx project, using the same mechanism as <code>sphinx-quickstart</code>. Most configuration values are set to default values, but you can influence the most important ones using the following options.</p>
<dt><code>-H project</code></p>
<dd> Sets the project name to put in generated files (see <code>project</code>).</p>
<dt><code>-A author</code></p>
<dd> Sets the author name(s) to put in generated files (see <code>copyright</code>).</p>
<dt><code>-V version</code></p>
<dd> Sets the project version to put in generated files (see <code>version</code>).</p>
<dt><code>-R release</code></p>
<dd> Sets the project release to put in generated files (see <code>release</code>).</dl>
<h2>RESTRUCTUREDTEXT PRIMER</h2>
<p> This section is a brief introduction to reStructuredText (reST) concepts and syntax, intended to provide authors with enough information to author documents productively. Since reST was designed to be a simple, unobtrusive markup language, this will not take too long. </p>
<p> <code>SEE ALSO:</code> The authoritative <i>reStructuredText User Documentation</i>. The &quot;ref&quot; links in this document link to the description of the individual constructs in the reST reference.</p>
<h3>Paragraphs</h3>
<p> The paragraph (<i>ref</i>) is the most basic block in a reST document. Paragraphs are simply chunks of text separated by one or more blank lines. As in Python, indentation is significant in reST, so all lines of the same paragraph must be left-aligned to the same level of indentation.</p>
<h3>Inline markup</h3>
<p> The standard reST inline markup is quite simple: use</p>
<dl>
<dt>&bull;</p>
<dd> one asterisk: <code>*text*</code> for emphasis (italics),</p>
<dt>&bull;</p>
<dd> two asterisks: <code>**text**</code> for strong emphasis (boldface), and</p>
<dt>&bull;</p>
<dd> backquotes: <code>&#8220;text&#8220;</code> for code samples. </p>
<p> If asterisks or backquotes appear in running text and could be confused with inline markup delimiters, they have to be escaped with a backslash. </p>
<p> Be aware of some restrictions of this markup:</p>
<dt>&bull;</p>
<dd> it may not be nested,</p>
<dt>&bull;</p>
<dd> content may not start or end with whitespace: <code>* text*</code> is wrong,</p>
<dt>&bull;</p>
<dd> it must be separated from surrounding text by non-word characters. Use a backslash escaped space to work around that: <code>thisis\ *one*\ word</code>. </p>
<p> These restrictions may be lifted in future versions of the docutils. </p>
<p> reST also allows for custom &quot;interpreted text roles&quot;, which signify that the enclosed text should be interpreted in a specific way. Sphinx uses this to provide semantic markup and cross-referencing of identifiers, as described in the appropriate section. The general syntax is <code>:rolename:`content`</code>. </p>
<p> Standard reST provides the following roles:</p>
<dt>&bull;</p>
<dd> <i>emphasis</i> &#8212; alternate spelling for <code>*emphasis*</code></p>
<dt>&bull;</p>
<dd> <i>strong</i> &#8212; alternate spelling for <code>**strong**</code></p>
<dt>&bull;</p>
<dd> <i>literal</i> &#8212; alternate spelling for <code>&#8220;literal&#8220;</code></p>
<dt>&bull;</p>
<dd> <i>subscript</i> &#8212; subscript text</p>
<dt>&bull;</p>
<dd> <i>superscript</i> &#8212; superscript text</p>
<dt>&bull;</p>
<dd> <i>title-reference</i> &#8212; for titles of books, periodicals, and other materials </p>
<p> See <i>inline-markup</i> for roles added by Sphinx.</dl>
<h3>Lists and Quote-like blocks</h3>
<p> List markup (<i>ref</i>) is natural: just place an asterisk at the start of a paragraph and indent properly. The same goes for numbered lists; they can also be autonumbered using a <code>#</code> sign: </p>
<pre>
* This is a bulleted list.
* It has two items, the second
  item uses two lines.
1. This is a numbered list.
2. It has two items too.
#. This is a numbered list.
#. It has two items too.
</pre>
<p> Nested lists are possible, but be aware that they must be separated from the parent list items by blank lines: </p>
<pre>
* this is
* a list
  * with a nested list
  * and some subitems
* and here the parent list continues
</pre>
<p> Definition lists (<i>ref</i>) are created as follows: </p>
<pre>
term (up to a line of text)
   Definition of the term, which must be indented
   and can even consist of multiple paragraphs
next term
   Description.
</pre>
<p> Note that the term cannot have more than one line of text. </p>
<p> Quoted paragraphs (<i>ref</i>) are created by just indenting them more than the surrounding paragraphs. </p>
<p> Line blocks (<i>ref</i>) are a way of preserving line breaks: </p>
<pre>
| These lines are
| broken exactly like in
| the source file.
</pre>
<p> There are also several more special blocks available:</p>
<dl>
<dt>&bull;</p>
<dd> field lists (<i>ref</i>)</p>
<dt>&bull;</p>
<dd> option lists (<i>ref</i>)</p>
<dt>&bull;</p>
<dd> quoted literal blocks (<i>ref</i>)</p>
<dt>&bull;</p>
<dd> doctest blocks (<i>ref</i>)</dl>
<h3>Source Code</h3>
<p> Literal code blocks (<i>ref</i>) are introduced by ending a paragraph with the special marker <code>::</code>. The literal block must be indented (and, like all paragraphs, separated from the surrounding ones by blank lines): </p>
<pre>
This is a normal text paragraph. The next paragraph is a code sample::
   It is not processed in any way, except
   that the indentation is removed.
   It can span multiple lines.
This is a normal text paragraph again.
</pre>
<p> The handling of the <code>::</code> marker is smart:</p>
<dl>
<dt>&bull;</p>
<dd> If it occurs as a paragraph of its own, that paragraph is completely left out of the document.</p>
<dt>&bull;</p>
<dd> If it is preceded by whitespace, the marker is removed.</p>
<dt>&bull;</p>
<dd> If it is preceded by non-whitespace, the marker is replaced by a single colon. </p>
<p> That way, the second sentence in the above example&#8217;s first paragraph would be rendered as &quot;The next paragraph is a code sample:&quot;.</dl>
<h3>Tables</h3>
<p> Two forms of tables are supported. For <i>grid tables</i> (<i>ref</i>), you have to &quot;paint&quot; the cell grid yourself. They look like this: </p>
<pre>
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
</pre>
<p> <i>Simple tables</i> (<i>ref</i>) are easier to write, but limited: they must contain more than one row, and the first column cannot contain multiple lines. They look like this: </p>
<pre>
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
</pre>
<h3>Hyperlinks</h3>
<h3>External links</h3>
<p> Use <code>`Link text &lt;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&gt;`_</code> for inline web links. If the link text should be the web address, you don&#8217;t need special markup at all, the parser finds links and mail addresses in ordinary text. </p>
<p> You can also separate the link and the target definition (<i>ref</i>), like this: </p>
<pre>
This is a paragraph that contains `a link`_.
.. _a link: <a rel="nofollow" href="http://example.com/">http://example.com/</a>
</pre>
<h3>Internal links</h3>
<p> Internal linking is done via a special reST role provided by Sphinx, see the section on specific markup, <i>ref-role</i>.</p>
<h3>Sections</h3>
<p> Section headers (<i>ref</i>) are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text: </p>
<pre>
=================
This is a heading
=================
</pre>
<p> Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings. However, for the Python documentation, this convention is used which you may follow:</p>
<dl>
<dt>&bull;</p>
<dd> <code>#</code> with overline, for parts</p>
<dt>&bull;</p>
<dd> <code>*</code> with overline, for chapters</p>
<dt>&bull;</p>
<dd> <code>=</code>, for sections</p>
<dt>&bull;</p>
<dd> <code>&#8211;</code>, for subsections</p>
<dt>&bull;</p>
<dd> <code>^</code>, for subsubsections</p>
<dt>&bull;</p>
<dd> <code>&quot;</code>, for paragraphs </p>
<p> Of course, you are free to use your own marker characters (see the reST documentation), and use a deeper nesting level, but keep in mind that most target formats (HTML, LaTeX) have a limited supported nesting depth.</dl>
<h3>Explicit Markup</h3>
<p> &quot;Explicit markup&quot; (<i>ref</i>) is used in reST for most constructs that need special handling, such as footnotes, specially-highlighted paragraphs, comments, and generic directives. </p>
<p> An explicit markup block begins with a line starting with <code>..</code> followed by whitespace and is terminated by the next paragraph at the same level of indentation. (There needs to be a blank line between explicit markup and normal paragraphs. This may all sound a bit complicated, but it is intuitive enough when you write it.)</p>
<h3>Directives</h3>
<p> A directive (<i>ref</i>) is a generic block of explicit markup. Besides roles, it is one of the extension mechanisms of reST, and Sphinx makes heavy use of it. </p>
<p> Docutils supports the following directives:</p>
<dl>
<dt>&bull;</p>
<dd> Admonitions: <i>attention</i>, <i>caution</i>, <i>danger</i>, <i>error</i>, <i>hint</i>, <i>important</i>, <i>note</i>, <i>tip</i>, <i>warning</i> and the generic <i>admonition</i>. (Most themes style only &quot;note&quot; and &quot;warning&quot; specially.)</p>
<dt>&bull;</p>
<dd> Images:</p>
<dt>&bull;</p>
<dd> <i>image</i> (see also <i>Images</i> below)</p>
<dt>&bull;</p>
<dd> <i>figure</i> (an image with caption and optional legend)</p>
<dt>&bull;</p>
<dd> Additional body elements:</p>
<dt>&bull;</p>
<dd> <i>contents</i> (a local, i.e. for the current file only, table of contents)</p>
<dt>&bull;</p>
<dd> <i>container</i> (a container with a custom class, useful to generate an outer <code>&lt;div&gt;</code> in HTML)</p>
<dt>&bull;</p>
<dd> <i>rubric</i> (a heading without relation to the document sectioning)</p>
<dt>&bull;</p>
<dd> <i>topic</i>, <i>sidebar</i> (special highlighted body elements)</p>
<dt>&bull;</p>
<dd> <i>parsed-literal</i> (literal block that supports inline markup)</p>
<dt>&bull;</p>
<dd> <i>epigraph</i> (a block quote with optional attribution line)</p>
<dt>&bull;</p>
<dd> <i>highlights</i>, <i>pull-quote</i> (block quotes with their own class attribute)</p>
<dt>&bull;</p>
<dd> <i>compound</i> (a compound paragraph)</p>
<dt>&bull;</p>
<dd> Special tables:</p>
<dt>&bull;</p>
<dd> <i>table</i> (a table with title)</p>
<dt>&bull;</p>
<dd> <i>csv-table</i> (a table generated from comma-separated values)</p>
<dt>&bull;</p>
<dd> <i>list-table</i> (a table generated from a list of lists)</p>
<dt>&bull;</p>
<dd> Special directives:</p>
<dt>&bull;</p>
<dd> <i>raw</i> (include raw target-format markup)</p>
<dt>&bull;</p>
<dd> <i>include</i> (include reStructuredText from another file) &#8212; in Sphinx, when given an absolute include file path, this directive takes it as relative to the source directory</p>
<dt>&bull;</p>
<dd> <i>class</i> (assign a class attribute to the next element) [1]</p>
<dt>&bull;</p>
<dd> HTML specifics:</p>
<dt>&bull;</p>
<dd> <i>meta</i> (generation of HTML <code>&lt;meta&gt;</code> tags)</p>
<dt>&bull;</p>
<dd> <i>title</i> (override document title)</p>
<dt>&bull;</p>
<dd> Influencing markup:</p>
<dt>&bull;</p>
<dd> <i>default-role</i> (set a new default role)</p>
<dt>&bull;</p>
<dd> <i>role</i> (create a new role) </p>
<p> Since these are only per-file, better use Sphinx&#8217; facilities for setting the <code>default_role</code>. </p>
<p> Do <i>not</i> use the directives <i>sectnum</i>, <i>header</i> and <i>footer</i>. </p>
<p> Directives added by Sphinx are described in <i>sphinxmarkup</i>. </p>
<p> Basically, a directive consists of a name, arguments, options and content. (Keep this terminology in mind, it is used in the next chapter describing custom directives.) Looking at this example, </p>
<pre>
.. function:: foo(x)
              foo(y, z)
   :module: some.module.name
   Return a line of text input from the user.
</pre>
<p> <code>function</code> is the directive name. It is given two arguments here, the remainder of the first line and the second line, as well as one option <code>module</code> (as you can see, options are given in the lines immediately following the arguments and indicated by the colons). Options must be indented to the same level as the directive content. </p>
<p> The directive content follows after a blank line and is indented relative to the directive start.</dl>
<h3>Images</h3>
<p> reST supports an image directive (<i>ref</i>), used like so: </p>
<pre>
.. image:: gnu.png
   (options)
</pre>
<p> When used within Sphinx, the file name given (here <code>gnu.png</code>) must either be relative to the source file, or absolute which means that they are relative to the top source directory. For example, the file <code>sketch/spam.rst</code> could refer to the image <code>images/spam.png</code> as <code>../images/spam.png</code> or <code>/images/spam.png</code>. </p>
<p> Sphinx will automatically copy image files over to a subdirectory of the output directory on building (e.g. the <code>_static</code> directory for HTML output.) </p>
<p> Interpretation of image size options (<code>width</code> and <code>height</code>) is as follows: if the size has no unit or the unit is pixels, the given size will only be respected for output channels that support pixels (i.e. not in LaTeX output). Other units (like <code>pt</code> for points) will be used for HTML and LaTeX output. </p>
<p> Sphinx extends the standard docutils behavior by allowing an asterisk for the extension: </p>
<pre>
.. image:: gnu.*
</pre>
<p> Sphinx then searches for all images matching the provided pattern and determines their type. Each builder then chooses the best image out of these candidates. For instance, if the file name <code>gnu.*</code> was given and two files <code>gnu.pdf</code> and <code>gnu.png</code> existed in the source tree, the LaTeX builder would choose the former, while the HTML builder would prefer the latter. Supported image types and choosing priority are defined at <i>builders</i>. </p>
<p> Note that image file names should not contain spaces. </p>
<p> Changed in version 0.4: Added the support for file names ending in an asterisk. </p>
<p> Changed in version 0.6: Image paths can now be absolute. </p>
<h3>Footnotes</h3>
<p> For footnotes (<i>ref</i>), use <code>[#name]_</code> to mark the footnote location, and add the footnote body at the bottom of the document after a &quot;Footnotes&quot; rubric heading, like so: </p>
<pre>
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_
.. rubric:: Footnotes
.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
</pre>
<p> You can also explicitly number the footnotes (<code>[1]_</code>) or use auto-numbered footnotes without names (<code>[#]_</code>).</p>
<h3>Citations</h3>
<p> Standard reST citations (<i>ref</i>) are supported, with the additional feature that they are &quot;global&quot;, i.e. all citations can be referenced from all files. Use them like so: </p>
<pre>
Lorem ipsum [Ref]_ dolor sit amet.
.. [Ref] Book or article reference, URL or whatever.
</pre>
<p> Citation usage is similar to footnote usage, but with a label that is not numeric or begins with <code>#</code>.</p>
<h3>Substitutions</h3>
<p> reST supports &quot;substitutions&quot; (<i>ref</i>), which are pieces of text and/or markup referred to in the text by <code>|name|</code>. They are defined like footnotes with explicit markup blocks, like this: </p>
<pre>
.. |name| replace:: replacement *text*
</pre>
<p> or this: </p>
<pre>
.. |caution| image:: warning.png
             :alt: Warning!
</pre>
<p> See the <i>reST reference for substitutions</i> for details. </p>
<p> If you want to use some substitutions for all documents, put them into <code>rst_prolog</code> or put them into a separate file and include it into all documents you want to use them in, using the <code>include</code> directive. (Be sure to give the include file a file name extension differing from that of other source files, to avoid Sphinx finding it as a standalone document.) </p>
<p> Sphinx defines some default substitutions, see <i>default-substitutions</i>.</p>
<h3>Comments</h3>
<p> Every explicit markup block which isn&#8217;t a valid markup construct (like the footnotes above) is regarded as a comment (<i>ref</i>). For example: </p>
<pre>
.. This is a comment.
</pre>
<p> You can indent text after a comment start to form multiline comments: </p>
<pre>
..
   This whole indented block
   is a comment.
   Still in the comment.
</pre>
<h3>Source encoding</h3>
<p> Since the easiest way to include special characters like em dashes or copyright signs in reST is to directly write them as Unicode characters, one has to specify an encoding. Sphinx assumes source files to be encoded in UTF-8 by default; you can change this with the <code>source_encoding</code> config value.</p>
<h3>Gotchas</h3>
<p> There are some problems one commonly runs into while authoring reST documents:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Separation of inline markup:</code> As said above, inline markup spans must be separated from the surrounding text by non-word characters, you have to use a backslash-escaped space to get around that. See <i>the reference</i> for the details.</p>
<dt>&bull;</p>
<dd> <code>No nested inline markup:</code> Something like <code>*see :func:`foo`*</code> is not possible.</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> When the default domain contains a <code>class</code> directive, this directive will be shadowed. Therefore, Sphinx re-exports it as <code>rst-class</code>.</dl>
<h2>SPHINX MARKUP CONSTRUCTS</h2>
<p> Sphinx adds a lot of new directives and interpreted text roles to <i>standard reST markup</i>. This section contains the reference material for these facilities.</p>
<h3>The TOC tree</h3>
<p> Since reST does not have facilities to interconnect several documents, or split documents into multiple output files, Sphinx uses a custom directive to add relations between the single files the documentation is made of, as well as tables of contents. The <code>toctree</code> directive is the central element. </p>
<p> <code>NOTE:</code> Simple &quot;inclusion&quot; of one file in another can be done with the <i>include</i> directive.</p>
<dl>
<dt><code>.. toctree::</code></p>
<dd> This directive inserts a &quot;TOC tree&quot; at the current location, using the individual TOCs (including &quot;sub-TOC trees&quot;) of the documents given in the directive body. Relative document names (not beginning with a slash) are relative to the document the directive occurs in, absolute names are relative to the source directory. A numeric <code>maxdepth</code> option may be given to indicate the depth of the tree; by default, all levels are included. [1] </p>
<p> Consider this example (taken from the Python docs&#8217; library reference index): </p>
<pre>
.. toctree::
   :maxdepth: 2
   intro
   strings
   datatypes
   numeric
   (many more documents listed here)
</pre>
<p> This accomplishes two things:</p>
<dt>&bull;</p>
<dd> Tables of contents from all those documents are inserted, with a maximum depth of two, that means one nested heading. <code>toctree</code> directives in those documents are also taken into account.</p>
<dt>&bull;</p>
<dd> Sphinx knows that the relative order of the documents <code>intro</code>, <code>strings</code> and so forth, and it knows that they are children of the shown document, the library index. From this information it generates &quot;next chapter&quot;, &quot;previous chapter&quot; and &quot;parent chapter&quot; links. </p>
<p> <code>Entries</code> </p>
<p> Document titles in the <code>toctree</code> will be automatically read from the title of the referenced document. If that isn&#8217;t what you want, you can specify an explicit title and target using a similar syntax to reST hyperlinks (and Sphinx&#8217;s <i>cross-referencing syntax</i>). This looks like: </p>
<pre>
.. toctree::
   intro
   All about strings &lt;strings&gt;
   datatypes
</pre>
<p> The second line above will link to the <code>strings</code> document, but will use the title &quot;All about strings&quot; instead of the title of the <code>strings</code> document. </p>
<p> You can also add external links, by giving an HTTP URL instead of a document name. </p>
<p> <code>Section numbering</code> </p>
<p> If you want to have section numbers even in HTML output, give the <code>toplevel</code> toctree a <code>numbered</code> option. For example: </p>
<pre>
.. toctree::
   :numbered:
   foo
   bar
</pre>
<p> Numbering then starts at the heading of <code>foo</code>. Sub-toctrees are automatically numbered (don&#8217;t give the <code>numbered</code> flag to those). </p>
<p> Numbering up to a specific depth is also possible, by giving the depth as a numeric argument to <code>numbered</code>. </p>
<p> <code>Additional options</code> </p>
<p> If you want only the titles of documents in the tree to show up, not other headings of the same level, you can use the <code>titlesonly</code> option: </p>
<pre>
.. toctree::
   :titlesonly:
   foo
   bar
</pre>
<p> You can use &quot;globbing&quot; in toctree directives, by giving the <code>glob</code> flag option. All entries are then matched against the list of available documents, and matches are inserted into the list alphabetically. Example: </p>
<pre>
.. toctree::
   :glob:
   intro*
   recipe/*
   *
</pre>
<p> This includes first all documents whose names start with <code>intro</code>, then all documents in the <code>recipe</code> folder, then all remaining documents (except the one containing the directive, of course.) [2] </p>
<p> The special entry name <code>self</code> stands for the document containing the toctree directive. This is useful if you want to generate a &quot;sitemap&quot; from the toctree. </p>
<p> You can also give a &quot;hidden&quot; option to the directive, like this: </p>
<pre>
.. toctree::
   :hidden:
   doc_1
   doc_2
</pre>
<p> This will still notify Sphinx of the document hierarchy, but not insert links into the document at the location of the directive &#8212; this makes sense if you intend to insert these links yourself, in a different style, or in the HTML sidebar. </p>
<p> In cases where you want to have only one top-level toctree and hide all other lower level toctrees you can add the &quot;includehidden&quot; option to the top-level toctree entry: </p>
<pre>
.. toctree::
   :includehidden:
   doc_1
   doc_2
</pre>
<p> All other toctree entries can then be eliminated by the &quot;hidden&quot; option. </p>
<p> In the end, all documents in the <i>source directory</i> (or subdirectories) must occur in some <code>toctree</code> directive; Sphinx will emit a warning if it finds a file that is not included, because that means that this file will not be reachable through standard navigation. </p>
<p> Use <code>exclude_patterns</code> to explicitly exclude documents or directories from building completely. Use <i>the &quot;orphan&quot; metadata</i> to let a document be built, but notify Sphinx that it is not reachable via a toctree. </p>
<p> The &quot;master document&quot; (selected by <code>master_doc</code>) is the &quot;root&quot; of the TOC tree hierarchy. It can be used as the documentation&#8217;s main page, or as a &quot;full table of contents&quot; if you don&#8217;t give a <code>maxdepth</code> option. </p>
<p> Changed in version 0.3: Added &quot;globbing&quot; option. </p>
<p> Changed in version 0.6: Added &quot;numbered&quot; and &quot;hidden&quot; options as well as external links and support for &quot;self&quot; references. </p>
<p> Changed in version 1.0: Added &quot;titlesonly&quot; option. </p>
<p> Changed in version 1.1: Added numeric argument to &quot;numbered&quot;. </p>
<p> Changed in version 1.2: Added &quot;includehidden&quot; option. </p>
</dl>
<h3>Special names</h3>
<p> Sphinx reserves some document names for its own use; you should not try to create documents with these names &#8212; it will cause problems. </p>
<p> The special document names (and pages generated for them) are:</p>
<dl>
<dt>&bull;</p>
<dd> <code>genindex</code>, <code>modindex</code>, <code>search</code> </p>
<p> These are used for the general index, the Python module index, and the search page, respectively. </p>
<p> The general index is populated with entries from modules, all index-generating <i>object descriptions</i>, and from <code>index</code> directives. </p>
<p> The Python module index contains one entry per <code>py:module</code> directive. </p>
<p> The search page contains a form that uses the generated JSON search index and JavaScript to full-text search the generated documents for search words; it should work on every major browser that supports modern JavaScript.</p>
<dt>&bull;</p>
<dd> every name beginning with <code>_</code> </p>
<p> Though only few such names are currently used by Sphinx, you should not create documents or document-containing directories with such names. (Using <code>_</code> as a prefix for a custom template directory is fine.) </p>
<p> <code>WARNING:</code> Be careful with unusual characters in filenames. Some formats may interpret these characters in unexpected ways:</p>
<dt>&bull;</p>
<dd> Do not user the colon <code>:</code> for HTML based formats. Links to other parts may not work.</p>
<dt>&bull;</p>
<dd> Do not use the plus <code>+</code> for the ePub format. Some resources may not be found.</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> The <code>maxdepth</code> option does not apply to the LaTeX writer, where the whole table of contents will always be presented at the begin of the document, and its depth is controlled by the <code>tocdepth</code> counter, which you can reset in your <code>latex_preamble</code> config value using e.g. <code>\setcounter{tocdepth}{2}</code>.</p>
<dt>[2]</p>
<dd> A note on available globbing syntax: you can use the standard shell constructs <code>*</code>, <code>?</code>, <code>[&#8230;]</code> and <code>[!&#8230;]</code> with the feature that these all don&#8217;t match slashes. A double star <code>**</code> can be used to match any sequence of characters <i>including</i> slashes.</dl>
<h3>Paragraph-level markup</h3>
<p> These directives create short paragraphs and can be used inside information units as well as normal text:</p>
<dl>
<dt><code>.. note:: </code></p>
<dd> An especially important bit of information about an API that a user should be aware of when using whatever bit of API the note pertains to. The content of the directive should be written in complete sentences and include all appropriate punctuation. </p>
<p> Example: </p>
<pre>
.. note::
   This function is not suitable for sending spam e-mails.
</pre>
<dt><code>.. warning:: </code></p>
<dd> An important bit of information about an API that a user should be very aware of when using whatever bit of API the warning pertains to. The content of the directive should be written in complete sentences and include all appropriate punctuation. This differs from <code>note</code> in that it is recommended over <code>note</code> for information regarding security.</p>
<dt><code>.. versionadded:: version</code></p>
<dd> This directive documents the version of the project which added the described feature to the library or C API. When this applies to an entire module, it should be placed at the top of the module section before any prose. </p>
<p> The first argument must be given and is the version in question; you can add a second argument consisting of a <i>brief</i> explanation of the change. </p>
<p> Example: </p>
<pre>
.. versionadded:: 2.5
   The *spam* parameter.
</pre>
<p> Note that there must be no blank line between the directive head and the explanation; this is to make these blocks visually continuous in the markup.</p>
<dt><code>.. versionchanged:: version</code></p>
<dd> Similar to <code>versionadded</code>, but describes when and what changed in the named feature in some way (new parameters, changed side effects, etc.).</p>
<dt><code>.. deprecated:: version</code></p>
<dd> Similar to <code>versionchanged</code>, but describes when the feature was deprecated. An explanation can also be given, for example to inform the reader what should be used instead. Example: </p>
<pre>
.. deprecated:: 3.1
   Use :func:`spam` instead.
</pre>
<p> <center> &#8212;-<br />
 </center> </p>
<dt><code>.. seealso::</code></p>
<dd> Many sections include a list of references to module documentation or external documents. These lists are created using the <code>seealso</code> directive. </p>
<p> The <code>seealso</code> directive is typically placed in a section just before any sub-sections. For the HTML output, it is shown boxed off from the main flow of the text. </p>
<p> The content of the <code>seealso</code> directive should be a reST definition list. Example: </p>
<pre>
.. seealso::
   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.
   `GNU tar manual, Basic Tar Format &lt;<a rel="nofollow" href="http://link">http://link</a>&gt;`_
      Documentation for tar archive files, including GNU tar extensions.
</pre>
<p> There&#8217;s also a &quot;short form&quot; allowed that looks like this: </p>
<pre>
.. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`
</pre>
<p> New in version 0.5: The short form. </p>
<dt><code>.. rubric:: title</code></p>
<dd> This directive creates a paragraph heading that is not used to create a table of contents node. </p>
<p> <code>NOTE:</code> If the <i>title</i> of the rubric is &quot;Footnotes&quot; (or the selected language&#8217;s equivalent), this rubric is ignored by the LaTeX writer, since it is assumed to only contain footnote definitions and therefore would create an empty heading.</p>
<dt><code>.. centered::</code></p>
<dd> This directive creates a centered boldfaced line of text. Use it as follows: </p>
<pre>
.. centered:: LICENSE AGREEMENT
</pre>
<p> Deprecated since version 1.1: This presentation-only directive is a legacy from older versions. Use a <code>rst-class</code> directive instead and add an appropriate style. </p>
<dt><code>.. hlist::</code></p>
<dd> This directive must contain a bullet list. It will transform it into a more compact list by either distributing more than one item horizontally, or reducing spacing between items, depending on the builder. </p>
<p> For builders that support the horizontal distribution, there is a <code>columns</code> option that specifies the number of columns; it defaults to 2. Example: </p>
<pre>
.. hlist::
   :columns: 3
   * A list of
   * short items
   * that should be
   * displayed
   * horizontally
</pre>
<p> New in version 0.6. </p>
</dl>
<h3>Table-of-contents markup</h3>
<p> The <code>toctree</code> directive, which generates tables of contents of subdocuments, is described in <i>toctree-directive</i>. </p>
<p> For local tables of contents, use the standard reST <i>contents directive</i>.</p>
<h3>Glossary</h3>
<dl>
<dt><code>.. glossary:: </code></p>
<dd> This directive must contain a reST definition-list-like markup with terms and definitions. The definitions will then be referencable with the <code>term</code> role. Example: </p>
<pre>
.. glossary::
   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.
   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.
</pre>
<p> In contrast to regular definition lists, <i>multiple</i> terms per entry are allowed, and inline markup is allowed in terms. You can link to all of the terms. For example: </p>
<pre>
.. glossary::
   term 1
   term 2
      Definition of both terms.
</pre>
<p> (When the glossary is sorted, the first term determines the sort order.) </p>
<p> New in version 0.6: You can now give the glossary directive a <code>:sorted:</code> flag that will automatically sort the entries alphabetically. </p>
<p> Changed in version 1.1: Now supports multiple terms and inline markup in terms. </p>
</dl>
<h3>Grammar production displays</h3>
<p> Special markup is available for displaying the productions of a formal grammar. The markup is simple and does not attempt to model all aspects of BNF (or any derived forms), but provides enough to allow context-free grammars to be displayed in a way that causes uses of a symbol to be rendered as hyperlinks to the definition of the symbol. There is this directive:</p>
<dl>
<dt><code>.. productionlist:: [name]</code></p>
<dd> This directive is used to enclose a group of productions. Each production is given on a single line and consists of a name, separated by a colon from the following definition. If the definition spans multiple lines, each continuation line must begin with a colon placed at the same column as in the first line. </p>
<p> The argument to <code>productionlist</code> serves to distinguish different sets of production lists that belong to different grammars. </p>
<p> Blank lines are not allowed within <code>productionlist</code> directive arguments. </p>
<p> The definition can contain token names which are marked as interpreted text (e.g. <code>sum ::= `integer` &quot;+&quot; `integer`</code>) &#8212; this generates cross-references to the productions of these tokens. Outside of the production list, you can reference to token productions using <code>token</code>. </p>
<p> Note that no further reST parsing is done in the production, so that you don&#8217;t have to escape <code>*</code> or <code>|</code> characters. </p>
<p> The following is an example taken from the Python Reference Manual: </p>
<pre>
.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: &quot;try&quot; &quot;:&quot; `suite`
            : (&quot;except&quot; [`expression` [&quot;,&quot; `target`]] &quot;:&quot; `suite`)+
            : [&quot;else&quot; &quot;:&quot; `suite`]
            : [&quot;finally&quot; &quot;:&quot; `suite`]
   try2_stmt: &quot;try&quot; &quot;:&quot; `suite`
            : &quot;finally&quot; &quot;:&quot; `suite`
</pre>
</dl>
<h3>Showing code examples</h3>
<p> Examples of Python source code or interactive sessions are represented using standard reST literal blocks. They are started by a <code>::</code> at the end of the preceding paragraph and delimited by indentation. </p>
<p> Representing an interactive session requires including the prompts and output along with the Python code. No special markup is required for interactive sessions. After the last line of input or output presented, there should not be an &quot;unused&quot; primary prompt; this is an example of what <i>not</i> to do: </p>
<pre>
&gt;&gt;&gt; 1 + 1
2
&gt;&gt;&gt;
</pre>
<p> Syntax highlighting is done with <i>Pygments</i> (if it&#8217;s installed) and handled in a smart way:</p>
<dl>
<dt>&bull;</p>
<dd> There is a &quot;highlighting language&quot; for each source file. Per default, this is <code>&#8216;python&#8217;</code> as the majority of files will have to highlight Python snippets, but the doc-wide default can be set with the <code>highlight_language</code> config value.</p>
<dt>&bull;</p>
<dd> Within Python highlighting mode, interactive sessions are recognized automatically and highlighted appropriately. Normal Python code is only highlighted if it is parseable (so you can use Python as the default, but interspersed snippets of shell commands or other code blocks will not be highlighted as Python).</p>
<dt>&bull;</p>
<dd> The highlighting language can be changed using the <code>highlight</code> directive, used as follows: </p>
<pre>
.. highlight:: c
</pre>
<p> This language is used until the next <code>highlight</code> directive is encountered.</p>
<dt>&bull;</p>
<dd> For documents that have to show snippets in different languages, there&#8217;s also a <code>code-block</code> directive that is given the highlighting language directly: </p>
<pre>
.. code-block:: ruby
   Some Ruby code.
</pre>
<p> The directive&#8217;s alias name <code>sourcecode</code> works as well.</p>
<dt>&bull;</p>
<dd> The valid values for the highlighting language are:</p>
<dt>&bull;</p>
<dd> <code>none</code> (no highlighting)</p>
<dt>&bull;</p>
<dd> <code>python</code> (the default when <code>highlight_language</code> isn&#8217;t set)</p>
<dt>&bull;</p>
<dd> <code>guess</code> (let Pygments guess the lexer based on contents, only works with certain well-recognizable languages)</p>
<dt>&bull;</p>
<dd> <code>rest</code></p>
<dt>&bull;</p>
<dd> <code>c</code></p>
<dt>&bull;</p>
<dd> &#8230; and any other <i>lexer alias that Pygments supports</i>.</p>
<dt>&bull;</p>
<dd> If highlighting with the selected language fails (i.e. Pygments emits an &quot;Error&quot; token), the block is not highlighted in any way.</dl>
<h3>Line numbers</h3>
<p> If installed, Pygments can generate line numbers for code blocks. For automatically-highlighted blocks (those started by <code>::</code>), line numbers must be switched on in a <code>highlight</code> directive, with the <code>linenothreshold</code> option: </p>
<pre>
.. highlight:: python
   :linenothreshold: 5
</pre>
<p> This will produce line numbers for all code blocks longer than five lines. </p>
<p> For <code>code-block</code> blocks, a <code>linenos</code> flag option can be given to switch on line numbers for the individual block: </p>
<pre>
.. code-block:: ruby
   :linenos:
   Some more Ruby code.
</pre>
<p> Additionally, an <code>emphasize-lines</code> option can be given to have Pygments emphasize particular lines: </p>
<pre>
.. code-block:: python
   :emphasize-lines: 3,5
   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'
</pre>
<p> Changed in version 1.1: <code>emphasize-lines</code> has been added. </p>
<h3>Includes</h3>
<dl>
<dt><code>.. literalinclude:: filename</code></p>
<dd> Longer displays of verbatim text may be included by storing the example text in an external file containing only plain text. The file may be included using the <code>literalinclude</code> directive. [1] For example, to include the Python source file <code>example.py</code>, use: </p>
<pre>
.. literalinclude:: example.py
</pre>
<p> The file name is usually relative to the current file&#8217;s path. However, if it is absolute (starting with <code>/</code>), it is relative to the top source directory. </p>
<p> Tabs in the input are expanded if you give a <code>tab-width</code> option with the desired tab width. </p>
<p> The directive also supports the <code>linenos</code> flag option to switch on line numbers, the <code>emphasize-lines</code> option to emphasize particular lines, and a <code>language</code> option to select a language different from the current file&#8217;s standard language. Example with options: </p>
<pre>
.. literalinclude:: example.rb
   :language: ruby
   :emphasize-lines: 12,15-18
   :linenos:
</pre>
<p> Include files are assumed to be encoded in the <code>source_encoding</code>. If the file has a different encoding, you can specify it with the <code>encoding</code> option: </p>
<pre>
.. literalinclude:: example.py
   :encoding: latin-1
</pre>
<p> The directive also supports including only parts of the file. If it is a Python module, you can select a class, function or method to include using the <code>pyobject</code> option: </p>
<pre>
.. literalinclude:: example.py
   :pyobject: Timer.start
</pre>
<p> This would only include the code lines belonging to the <code>start()</code> method in the <code>Timer</code> class within the file. </p>
<p> Alternately, you can specify exactly which lines to include by giving a <code>lines</code> option: </p>
<pre>
.. literalinclude:: example.py
   :lines: 1,3,5-10,20-
</pre>
<p> This includes the lines 1, 3, 5 to 10 and lines 20 to the last line. </p>
<p> Another way to control which part of the file is included is to use the <code>start-after</code> and <code>end-before</code> options (or only one of them). If <code>start-after</code> is given as a string option, only lines that follow the first line containing that string are included. If <code>end-before</code> is given as a string option, only lines that precede the first lines containing that string are included. </p>
<p> You can prepend and/or append a line to the included code, using the <code>prepend</code> and <code>append</code> option, respectively. This is useful e.g. for highlighting PHP code that doesn&#8217;t include the <code>&lt;?php</code>/<code>?&gt;</code> markers. </p>
<p> New in version 0.4.3: The <code>encoding</code> option. </p>
<p> New in version 0.6: The <code>pyobject</code>, <code>lines</code>, <code>start-after</code> and <code>end-before</code> options, as well as support for absolute filenames. </p>
<p> New in version 1.0: The <code>prepend</code> and <code>append</code> options, as well as <code>tab-width</code>. </p>
</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> There is a standard <code>.. include</code> directive, but it raises errors if the file is not found. This one only emits a warning.</dl>
<h3>Inline markup</h3>
<p> Sphinx uses interpreted text roles to insert semantic markup into documents. They are written as <code>:rolename:`content`</code>. </p>
<p> <code>NOTE:</code> The default role (<code>`content`</code>) has no special meaning by default. You are free to use it for anything you like, e.g. variable names; use the <code>default_role</code> config value to set it to a known role. </p>
<p> See <i>domains</i> for roles added by domains.</p>
<h3>Cross-referencing syntax</h3>
<p> Cross-references are generated by many semantic interpreted text roles. Basically, you only need to write <code>:role:`target`</code>, and a link will be created to the item named <i>target</i> of the type indicated by <i>role</i>. The links&#8217;s text will be the same as <i>target</i>. </p>
<p> There are some additional facilities, however, that make cross-referencing roles more versatile:</p>
<dl>
<dt>&bull;</p>
<dd> You may supply an explicit title and reference target, like in reST direct hyperlinks: <code>:role:`title &lt;target&gt;`</code> will refer to <i>target</i>, but the link text will be <i>title</i>.</p>
<dt>&bull;</p>
<dd> If you prefix the content with <code>!</code>, no reference/hyperlink will be created.</p>
<dt>&bull;</p>
<dd> If you prefix the content with <code>~</code>, the link text will only be the last component of the target. For example, <code>:py:meth:`~Queue.Queue.get`</code> will refer to <code>Queue.Queue.get</code> but only display <code>get</code> as the link text. </p>
<p> In HTML output, the link&#8217;s <code>title</code> attribute (that is e.g. shown as a tool-tip on mouse-hover) will always be the full target name.</dl>
<h3>Cross-referencing objects</h3>
<p> These roles are described with their respective domains:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python</i></p>
<dt>&bull;</p>
<dd> <i>C</i></p>
<dt>&bull;</p>
<dd> <i>C++</i></p>
<dt>&bull;</p>
<dd> <i>JavaScript</i></p>
<dt>&bull;</p>
<dd> <i>ReST</i></dl>
<h3>Cross-referencing arbitrary locations</h3>
<dl>
<dt><code>:ref:</code></p>
<dd> To support cross-referencing to arbitrary locations in any document, the standard reST labels are used. For this to work label names must be unique throughout the entire documentation. There are two ways in which you can refer to labels:</p>
<dt>&bull;</p>
<dd> If you place a label directly before a section title, you can reference to it with <code>:ref:`label-name`</code>. Example: </p>
<pre>
.. _my-reference-label:
Section to cross-reference
--------------------------
This is the text of the section.
It refers to the section itself, see :ref:`my-reference-label`.
</pre>
<p> The <code>:ref:</code> role would then generate a link to the section, with the link title being &quot;Section to cross-reference&quot;. This works just as well when section and reference are in different source files. </p>
<p> Automatic labels also work with figures: given </p>
<pre>
.. _my-figure:
.. figure:: whatever
   Figure caption
</pre>
<p> a reference <code>:ref:`my-figure`</code> would insert a reference to the figure with link text &quot;Figure caption&quot;. </p>
<p> The same works for tables that are given an explicit caption using the <i>table</i> directive.</p>
<dt>&bull;</p>
<dd> Labels that aren&#8217;t placed before a section title can still be referenced to, but you must give the link an explicit title, using this syntax: <code>:ref:`Link title &lt;label-name&gt;`</code>. </p>
<p> Using <code>ref</code> is advised over standard reStructuredText links to sections (like <code>`Section title`_</code>) because it works across files, when section headings are changed, and for all builders that support cross-references.</dl>
<h3>Cross-referencing documents</h3>
<p> New in version 0.6. </p>
<p> There is also a way to directly link to documents:</p>
<dl>
<dt><code>:doc:</code></p>
<dd> Link to the specified document; the document name can be specified in absolute or relative fashion. For example, if the reference <code>:doc:`parrot`</code> occurs in the document <code>sketches/index</code>, then the link refers to <code>sketches/parrot</code>. If the reference is <code>:doc:`/people`</code> or <code>:doc:`../people`</code>, the link refers to <code>people</code>. </p>
<p> If no explicit link text is given (like usual: <code>:doc:`Monty Python members &lt;/people&gt;`</code>), the link caption will be the title of the given document.</dl>
<h3>Referencing downloadable files</h3>
<p> New in version 0.6. </p>
<dl>
<dt><code>:download:</code></p>
<dd> This role lets you link to files within your source tree that are not reST documents that can be viewed, but files that can be downloaded. </p>
<p> When you use this role, the referenced file is automatically marked for inclusion in the output when building (obviously, for HTML output only). All downloadable files are put into the <code>_downloads</code> subdirectory of the output directory; duplicate filenames are handled. </p>
<p> An example: </p>
<pre>
See :download:`this example script &lt;../example.py&gt;`.
</pre>
<p> The given filename is usually relative to the directory the current source file is contained in, but if it absolute (starting with <code>/</code>), it is taken as relative to the top source directory. </p>
<p> The <code>example.py</code> file will be copied to the output directory, and a suitable link generated to it.</dl>
<h3>Cross-referencing other items of interest</h3>
<p> The following roles do possibly create a cross-reference, but do not refer to objects:</p>
<dl>
<dt><code>:envvar:</code></p>
<dd> An environment variable. Index entries are generated. Also generates a link to the matching <code>envvar</code> directive, if it exists.</p>
<dt><code>:token:</code></p>
<dd> The name of a grammar token (used to create links between <code>productionlist</code> directives).</p>
<dt><code>:keyword:</code></p>
<dd> The name of a keyword in Python. This creates a link to a reference label with that name, if it exists.</p>
<dt><code>:option:</code></p>
<dd> A command-line option to an executable program. The leading hyphen(s) must be included. This generates a link to a <code>option</code> directive, if it exists. </p>
<p> The following role creates a cross-reference to the term in the glossary:</p>
<dt><code>:term:</code></p>
<dd> Reference to a term in the glossary. The glossary is created using the <code>glossary</code> directive containing a definition list with terms and definitions. It does not have to be in the same file as the <code>term</code> markup, for example the Python docs have one global glossary in the <code>glossary.rst</code> file. </p>
<p> If you use a term that&#8217;s not explained in a glossary, you&#8217;ll get a warning during build.</dl>
<h3>Other semantic markup</h3>
<p> The following roles don&#8217;t do anything special except formatting the text in a different style:</p>
<dl>
<dt><code>:abbr:</code></p>
<dd> An abbreviation. If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML, and output only once in LaTeX. </p>
<p> Example: <code>:abbr:`LIFO (last-in, first-out)`</code>. </p>
<p> New in version 0.6. </p>
<dt><code>:command:</code></p>
<dd> The name of an OS-level command, such as <code>rm</code>.</p>
<dt><code>:dfn:</code></p>
<dd> Mark the defining instance of a term in the text. (No index entries are generated.)</p>
<dt><code>:file:</code></p>
<dd> The name of a file or directory. Within the contents, you can use curly braces to indicate a &quot;variable&quot; part, for example: </p>
<pre>
... is installed in :file:`/usr/lib/python2.{x}/site-packages` ...
</pre>
<p> In the built documentation, the <code>x</code> will be displayed differently to indicate that it is to be replaced by the Python minor version.</p>
<dt><code>:guilabel:</code></p>
<dd> Labels presented as part of an interactive user interface should be marked using <code>guilabel</code>. This includes labels from text-based interfaces such as those created using <code>curses</code> or other text-based libraries. Any label used in the interface should be marked with this role, including button labels, window titles, field names, menu and menu selection names, and even values in selection lists. </p>
<p> Changed in version 1.0: An accelerator key for the GUI label can be included using an ampersand; this will be stripped and displayed underlined in the output (example: <code>:guilabel:`&amp;Cancel`</code>). To include a literal ampersand, double it. </p>
<dt><code>:kbd:</code></p>
<dd> Mark a sequence of keystrokes. What form the key sequence takes may depend on platform- or application-specific conventions. When there are no relevant conventions, the names of modifier keys should be spelled out, to improve accessibility for new users and non-native speakers. For example, an <i>xemacs</i> key sequence may be marked like <code>:kbd:`C-x C-f`</code>, but without reference to a specific application or platform, the same sequence should be marked as <code>:kbd:`Control-x Control-f`</code>.</p>
<dt><code>:mailheader:</code></p>
<dd> The name of an RFC 822-style mail header. This markup does not imply that the header is being used in an email message, but can be used to refer to any header of the same &quot;style.&quot; This is also used for headers defined by the various MIME specifications. The header name should be entered in the same way it would normally be found in practice, with the camel-casing conventions being preferred where there is more than one common usage. For example: <code>:mailheader:`Content-Type`</code>.</p>
<dt><code>:makevar:</code></p>
<dd> The name of a <code>make</code> variable.</p>
<dt><code>:manpage:</code></p>
<dd> A reference to a Unix manual page including the section, e.g. <code>:manpage:`<a href="/docs/linux/man/1-ls/">ls</a>(1)`</code>.</p>
<dt><code>:menuselection:</code></p>
<dd> Menu selections should be marked using the <code>menuselection</code> role. This is used to mark a complete sequence of menu selections, including selecting submenus and choosing a specific operation, or any subsequence of such a sequence. The names of individual selections should be separated by <code>&#8211;&gt;</code>. </p>
<p> For example, to mark the selection &quot;Start &gt; Programs&quot;, use this markup: </p>
<pre>
:menuselection:`Start --&gt; Programs`
</pre>
<p> When including a selection that includes some trailing indicator, such as the ellipsis some operating systems use to indicate that the command opens a dialog, the indicator should be omitted from the selection name. </p>
<p> <code>menuselection</code> also supports ampersand accelerators just like <code>guilabel</code>.</p>
<dt><code>:mimetype:</code></p>
<dd> The name of a MIME type, or a component of a MIME type (the major or minor portion, taken alone).</p>
<dt><code>:newsgroup:</code></p>
<dd> The name of a Usenet newsgroup.</p>
<dt><code>:program:</code></p>
<dd> The name of an executable program. This may differ from the file name for the executable for some platforms. In particular, the <code>.exe</code> (or other) extension should be omitted for Windows programs.</p>
<dt><code>:regexp:</code></p>
<dd> A regular expression. Quotes should not be included.</p>
<dt><code>:samp:</code></p>
<dd> A piece of literal text, such as code. Within the contents, you can use curly braces to indicate a &quot;variable&quot; part, as in <code>file</code>. For example, in <code>:samp:`print 1+{variable}`</code>, the part <code>variable</code> would be emphasized. </p>
<p> If you don&#8217;t need the &quot;variable part&quot; indication, use the standard <code>&#8220;code&#8220;</code> instead. </p>
<p> There is also an <code>index</code> role to generate index entries. </p>
<p> The following roles generate external links:</p>
<dt><code>:pep:</code></p>
<dd> A reference to a Python Enhancement Proposal. This generates appropriate index entries. The text &quot;PEP <i>number</i>&quot; is generated; in the HTML output, this text is a hyperlink to an online copy of the specified PEP. You can link to a specific section by saying <code>:pep:`number#anchor`</code>.</p>
<dt><code>:rfc:</code></p>
<dd> A reference to an Internet Request for Comments. This generates appropriate index entries. The text &quot;RFC <i>number</i>&quot; is generated; in the HTML output, this text is a hyperlink to an online copy of the specified RFC. You can link to a specific section by saying <code>:rfc:`number#anchor`</code>. </p>
<p> Note that there are no special roles for including hyperlinks as you can use the standard reST markup for that purpose.</dl>
<h3>Substitutions</h3>
<p> The documentation system provides three substitutions that are defined by default. They are set in the build configuration file.</p>
<dl>
<dt><code>|release|</code></p>
<dd> Replaced by the project release the documentation refers to. This is meant to be the full version string including alpha/beta/release candidate tags, e.g. <code>2.5.2b3</code>. Set by <code>release</code>.</p>
<dt><code>|version|</code></p>
<dd> Replaced by the project version the documentation refers to. This is meant to consist only of the major and minor version parts, e.g. <code>2.5</code>, even for version 2.5.1. Set by <code>version</code>.</p>
<dt><code>|today|</code></p>
<dd> Replaced by either today&#8217;s date (the date on which the document is read), or the date set in the build configuration file. Normally has the format <code>April 14, 2007</code>. Set by <code>today_fmt</code> and <code>today</code>.</dl>
<h3>Miscellaneous markup</h3>
<h3>File-wide metadata</h3>
<p> reST has the concept of &quot;field lists&quot;; these are a sequence of fields marked up like this: </p>
<pre>
:fieldname: Field content
</pre>
<p> A field list near the top of a file is parsed by docutils as the &quot;docinfo&quot; which is normally used to record the author, date of publication and other metadata. <i>In Sphinx</i>, a field list preceding any other markup is moved from the docinfo to the Sphinx environment as document metadata and is not displayed in the output; a field list appearing after the document title will be part of the docinfo as normal and will be displayed in the output. </p>
<p> At the moment, these metadata fields are recognized:</p>
<dl>
<dt><code>tocdepth</code></p>
<dd> The maximum depth for a table of contents of this file. </p>
<p> New in version 0.4. </p>
<dt><code>nocomments</code></p>
<dd> If set, the web application won&#8217;t display a comment form for a page generated from this source file.</p>
<dt><code>orphan</code></p>
<dd> If set, warnings about this file not being included in any toctree will be suppressed. </p>
<p> New in version 1.0. </p>
</dl>
<h3>Meta-information markup</h3>
<dl>
<dt><code>.. sectionauthor:: name &lt;email&gt;</code></p>
<dd> Identifies the author of the current section. The argument should include the author&#8217;s name such that it can be used for presentation and email address. The domain name portion of the address should be lower case. Example: </p>
<pre>
.. sectionauthor:: Guido van Rossum &lt;guido [at] python.org&gt;
</pre>
<p> By default, this markup isn&#8217;t reflected in the output in any way (it helps keep track of contributions), but you can set the configuration value <code>show_authors</code> to True to make them produce a paragraph in the output.</p>
<dt><code>.. codeauthor:: name &lt;email&gt;</code></p>
<dd> The <code>codeauthor</code> directive, which can appear multiple times, names the authors of the described code, just like <code>sectionauthor</code> names the author(s) of a piece of documentation. It too only produces output if the <code>show_authors</code> configuration value is True.</dl>
<h3>Index-generating markup</h3>
<p> Sphinx automatically creates index entries from all object descriptions (like functions, classes or attributes) like discussed in <i>domains</i>. </p>
<p> However, there is also explicit markup available, to make the index more comprehensive and enable index entries in documents where information is not mainly contained in information units, such as the language reference.</p>
<dl>
<dt><code>.. index:: &lt;entries&gt;</code></p>
<dd> This directive contains one or more index entries. Each entry consists of a type and a value, separated by a colon. </p>
<p> For example: </p>
<pre>
.. index::
   single: execution; context
   module: __main__
   module: sys
   triple: module; search; path
The execution context
---------------------
...
</pre>
<p> This directive contains five entries, which will be converted to entries in the generated index which link to the exact location of the index statement (or, in case of offline media, the corresponding page number). </p>
<p> Since index directives generate cross-reference targets at their location in the source, it makes sense to put them <i>before</i> the thing they refer to &#8212; e.g. a heading, as in the example above. </p>
<p> The possible entry types are:</p>
<dt><code>single</code></p>
<dd> Creates a single index entry. Can be made a subentry by separating the subentry text with a semicolon (this notation is also used below to describe what entries are created).</p>
<dt><code>pair</code></p>
<dd> <code>pair: loop; statement</code> is a shortcut that creates two index entries, namely <code>loop; statement</code> and <code>statement; loop</code>.</p>
<dt><code>triple</code></p>
<dd> Likewise, <code>triple: module; search; path</code> is a shortcut that creates three index entries, which are <code>module; search path</code>, <code>search; path, module</code> and <code>path; module search</code>.</p>
<dt><code>see</code></p>
<dd> <code>see: entry; other</code> creates an index entry that refers from <code>entry</code> to <code>other</code>.</p>
<dt><code>seealso</code></p>
<dd> Like <code>see</code>, but inserts &quot;see also&quot; instead of &quot;see&quot;.</p>
<dt><code>module, keyword, operator, object, exception, statement, builtin</code></p>
<dd> These all create two index entries. For example, <code>module: hashlib</code> creates the entries <code>module; hashlib</code> and <code>hashlib; module</code>. (These are Python-specific and therefore deprecated.) </p>
<p> You can mark up &quot;main&quot; index entries by prefixing them with an exclamation mark. The references to &quot;main&quot; entries are emphasized in the generated index. For example, if two pages contain </p>
<pre>
.. index:: Python
</pre>
<p> and one page contains </p>
<pre>
.. index:: ! Python
</pre>
<p> then the backlink to the latter page is emphasized among the three backlinks. </p>
<p> For index directives containing only &quot;single&quot; entries, there is a shorthand notation: </p>
<pre>
.. index:: BNF, grammar, syntax, notation
</pre>
<p> This creates four index entries. </p>
<p> Changed in version 1.1: Added <code>see</code> and <code>seealso</code> types, as well as marking main entries. </p>
<dt><code>:index:</code></p>
<dd> While the <code>index</code> directive is a block-level markup and links to the beginning of the next paragraph, there is also a corresponding role that sets the link target directly where it is used. </p>
<p> The content of the role can be a simple phrase, which is then kept in the text and used as an index entry. It can also be a combination of text and index entry, styled like with explicit targets of cross-references. In that case, the &quot;target&quot; part can be a full entry as described for the directive above. For example: </p>
<pre>
This is a normal reST :index:`paragraph` that contains several
:index:`index entries &lt;pair: index; entry&gt;`.
</pre>
<p> New in version 1.1. </p>
</dl>
<h3>Including content based on tags</h3>
<dl>
<dt><code>.. only:: &lt;expression&gt;</code></p>
<dd> Include the content of the directive only if the <i>expression</i> is true. The expression should consist of tags, like this: </p>
<pre>
.. only:: html and draft
</pre>
<p> Undefined tags are false, defined tags (via the <code>-t</code> command-line option or within <code>conf.py</code>, see <i>here</i>) are true. Boolean expressions, also using parentheses (like <code>html and (latex or draft)</code>) are supported. </p>
<p> The <i>format</i> and the <i>name</i> of the current builder (<code>html</code>, <code>latex</code> or <code>text</code>) are always set as a tag [1]. To make the distinction between format and name explicit, they are also added with the prefix <code>format_</code> and <code>builder_</code>, e.g. the epub builder defines the tags <code>html</code>, <code>epub</code>, <code>format_html</code> and <code>builder_epub</code>. </p>
<p> These standard tags are set <i>after</i> the configuration file is read, so they are not available there. </p>
<p> New in version 0.6. </p>
<p> Changed in version 1.2: Added the name of the builder and the prefixes. </p>
</dl>
<h3>Tables</h3>
<p> Use <i>standard reStructuredText tables</i>. They work fine in HTML output, however there are some gotchas when using tables in LaTeX: the column width is hard to determine correctly automatically. For this reason, the following directive exists:</p>
<dl>
<dt><code>.. tabularcolumns:: column spec</code></p>
<dd> This directive gives a &quot;column spec&quot; for the next table occurring in the source file. The spec is the second argument to the LaTeX <code>tabulary</code> package&#8217;s environment (which Sphinx uses to translate tables). It can have values like </p>
<pre>
|l|l|l|
</pre>
<p> which means three left-adjusted, nonbreaking columns. For columns with longer text that should automatically be broken, use either the standard <code>p{width}</code> construct, or tabulary&#8217;s automatic specifiers: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>L</code> </td>
<td> flush left column with automatic width
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>R</code> </td>
<td> flush right column with automatic width
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>C</code> </td>
<td> centered column with automatic width
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>J</code> </td>
<td> justified column with automatic width
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The automatic width is determined by rendering the content in the table, and scaling them according to their share of the total width. </p>
<p> By default, Sphinx uses a table layout with <code>L</code> for every column. </p>
<p> New in version 0.3. </p>
<p> <code>WARNING:</code> Tables that contain list-like elements such as object descriptions, blockquotes or any kind of lists cannot be set out of the box with <code>tabulary</code>. They are therefore set with the standard LaTeX <code>tabular</code> environment if you don&#8217;t give a <code>tabularcolumns</code> directive. If you do, the table will be set with <code>tabulary</code>, but you must use the <code>p{width}</code> construct for the columns that contain these elements. </p>
<p> Literal blocks do not work with <code>tabulary</code> at all, so tables containing a literal block are always set with <code>tabular</code>. Also, the verbatim environment used for literal blocks only works in <code>p{width}</code> columns, which means that by default, Sphinx generates such column specs for such tables. Use the <code>tabularcolumns</code> directive to get finer control over such tables.</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> For most builders name and format are the same. At the moment only builders derived from the html builder distinguish between the builder format and the builder name. </p>
<p> Note that the current builder tag is not available in <code>conf.py</code>, it is only available after the builder is intialized. </p>
<p> More markup is added by <i>domains</i>.</dl>
<h2>SPHINX DOMAINS</h2>
<p> New in version 1.0. </p>
<h3>What is a Domain?</h3>
<p> Originally, Sphinx was conceived for a single project, the documentation of the Python language. Shortly afterwards, it was made available for everyone as a documentation tool, but the documentation of Python modules remained deeply built in &#8212; the most fundamental directives, like <code>function</code>, were designed for Python objects. Since Sphinx has become somewhat popular, interest developed in using it for many different purposes: C/C++ projects, JavaScript, or even reStructuredText markup (like in this documentation). </p>
<p> While this was always possible, it is now much easier to easily support documentation of projects using different programming languages or even ones not supported by the main Sphinx distribution, by providing a <code>domain</code> for every such purpose. </p>
<p> A domain is a collection of markup (reStructuredText <i>directive</i>s and <i>role</i>s) to describe and link to <i>object</i>s belonging together, e.g. elements of a programming language. Directive and role names in a domain have names like <code>domain:name</code>, e.g. <code>py:function</code>. Domains can also provide custom indices (like the Python Module Index). </p>
<p> Having domains means that there are no naming problems when one set of documentation wants to refer to e.g. C++ and Python classes. It also means that extensions that support the documentation of whole new languages are much easier to write. </p>
<p> This section describes what the domains that come with Sphinx provide. The domain API is documented as well, in the section <i>domain-api</i>.</p>
<h3>Basic Markup</h3>
<p> Most domains provide a number of <i>object description directives</i>, used to describe specific objects provided by modules. Each directive requires one or more signatures to provide basic information about what is being described, and the content should be the description. The basic version makes entries in the general index; if no index entry is desired, you can give the directive option flag <code>:noindex:</code>. An example using a Python domain directive: </p>
<pre>
.. py:function:: spam(eggs)
                 ham(eggs)
   Spam or ham the foo.
</pre>
<p> This describes the two Python functions <code>spam</code> and <code>ham</code>. (Note that when signatures become too long, you can break them if you add a backslash to lines that are continued in the next line. Example: </p>
<pre>
.. py:function:: filterwarnings(action, message='', category=Warning, \
                                module='', lineno=0, append=False)
   :noindex:
</pre>
<p> (This example also shows how to use the <code>:noindex:</code> flag.) </p>
<p> The domains also provide roles that link back to these object descriptions. For example, to link to one of the functions described in the example above, you could say </p>
<pre>
The function :py:func:`spam` does a similar thing.
</pre>
<p> As you can see, both directive and role names contain the domain name and the directive name. Default Domain </p>
<p> To avoid having to writing the domain name all the time when you e.g. only describe Python objects, a default domain can be selected with either the config value <code>primary_domain</code> or this directive:</p>
<dl>
<dt><code>.. default-domain:: name</code></p>
<dd> Select a new default domain. While the <code>primary_domain</code> selects a global default, this only has an effect within the same file. </p>
<p> If no other default is selected, the Python domain (named <code>py</code>) is the default one, mostly for compatibility with documentation written for older versions of Sphinx. </p>
<p> Directives and roles that belong to the default domain can be mentioned without giving the domain name, i.e. </p>
<pre>
.. function:: pyfunc()
   Describes a Python function.
Reference to :func:`pyfunc`.
</pre>
</dl>
<h3>Cross-referencing syntax</h3>
<p> For cross-reference roles provided by domains, the same facilities exist as for general cross-references. See <i>xref-syntax</i>. </p>
<p> In short:</p>
<dl>
<dt>&bull;</p>
<dd> You may supply an explicit title and reference target: <code>:role:`title &lt;target&gt;`</code> will refer to <i>target</i>, but the link text will be <i>title</i>.</p>
<dt>&bull;</p>
<dd> If you prefix the content with <code>!</code>, no reference/hyperlink will be created.</p>
<dt>&bull;</p>
<dd> If you prefix the content with <code>~</code>, the link text will only be the last component of the target. For example, <code>:py:meth:`~Queue.Queue.get`</code> will refer to <code>Queue.Queue.get</code> but only display <code>get</code> as the link text.</dl>
<h3>The Python Domain</h3>
<p> The Python domain (name <code>py</code>) provides the following directives for module declarations:</p>
<dl>
<dt><code>.. py:module:: name</code></p>
<dd> This directive marks the beginning of the description of a module (or package submodule, in which case the name should be fully qualified, including the package name). It does not create content (like e.g. <code>py:class</code> does). </p>
<p> This directive will also cause an entry in the global module index. </p>
<p> The <code>platform</code> option, if present, is a comma-separated list of the platforms on which the module is available (if it is available on all platforms, the option should be omitted). The keys are short identifiers; examples that are in use include &quot;IRIX&quot;, &quot;Mac&quot;, &quot;Windows&quot;, and &quot;Unix&quot;. It is important to use a key which has already been used when applicable. </p>
<p> The <code>synopsis</code> option should consist of one sentence describing the module&#8217;s purpose &#8212; it is currently only used in the Global Module Index. </p>
<p> The <code>deprecated</code> option can be given (with no value) to mark a module as deprecated; it will be designated as such in various locations then.</p>
<dt><code>.. py:currentmodule:: name</code></p>
<dd> This directive tells Sphinx that the classes, functions etc. documented from here are in the given module (like <code>py:module</code>), but it will not create index entries, an entry in the Global Module Index, or a link target for <code>py:mod</code>. This is helpful in situations where documentation for things in a module is spread over multiple files or sections &#8212; one location has the <code>py:module</code> directive, the others only <code>py:currentmodule</code>. </p>
<p> The following directives are provided for module and class contents:</p>
<dt><code>.. py:data:: name</code></p>
<dd> Describes global data in a module, including both variables and values used as &quot;defined constants.&quot; Class and object attributes are not documented using this environment.</p>
<dt><code>.. py:exception:: name</code></p>
<dd> Describes an exception class. The signature can, but need not include parentheses with constructor arguments.</p>
<dt><code>.. py:function:: name(parameters)</code></p>
<dd> Describes a module-level function. The signature should include the parameters as given in the Python function definition, see <i>signatures</i>. For example: </p>
<pre>
.. py:function:: Timer.repeat(repeat=3, number=1000000)
</pre>
<p> For methods you should use <code>py:method</code>. </p>
<p> The description should include information about the parameters required and how they are used (especially whether mutable objects passed as parameters are modified), side effects, and possible exceptions. This information can optionally be given in a structured form, see <i>info-field-lists</i>. A small example may be provided.</p>
<dt><code>.. py:class:: name</code></p>
<dd>
<dt><code>.. py:class:: name(parameters)</code></p>
<dd> Describes a class. The signature can optionally include parentheses with parameters which will be shown as the constructor arguments. See also <i>signatures</i>. </p>
<p> Methods and attributes belonging to the class should be placed in this directive&#8217;s body. If they are placed outside, the supplied name should contain the class name so that cross-references still work. Example: </p>
<pre>
.. py:class:: Foo
   .. py:method:: quux()
-- or --
.. py:class:: Bar
.. py:method:: Bar.quux()
</pre>
<p> The first way is the preferred one.</p>
<dt><code>.. py:attribute:: name</code></p>
<dd> Describes an object data attribute. The description should include information about the type of the data to be expected and whether it may be changed directly.</p>
<dt><code>.. py:method:: name(parameters)</code></p>
<dd> Describes an object method. The parameters should not include the <code>self</code> parameter. The description should include similar information to that described for <code>function</code>. See also <i>signatures</i> and <i>info-field-lists</i>.</p>
<dt><code>.. py:staticmethod:: name(parameters)</code></p>
<dd> Like <code>py:method</code>, but indicates that the method is a static method. </p>
<p> New in version 0.4. </p>
<dt><code>.. py:classmethod:: name(parameters)</code></p>
<dd> Like <code>py:method</code>, but indicates that the method is a class method. </p>
<p> New in version 0.6. </p>
<dt><code>.. py:decorator:: name</code></p>
<dd>
<dt><code>.. py:decorator:: name(parameters)</code></p>
<dd> Describes a decorator function. The signature should represent the usage as a decorator. For example, given the functions </p>
<pre>
def removename(func):
    func.__name__ = ''
    return func
def setnewname(name):
    def decorator(func):
        func.__name__ = name
        return func
    return decorator
</pre>
<p> the descriptions should look like this: </p>
<pre>
.. py:decorator:: removename
   Remove name of the decorated function.
.. py:decorator:: setnewname(name)
   Set name of the decorated function to *name*.
</pre>
<p> (as opposed to <code>.. py:decorator:: removename(func)</code>.) </p>
<p> There is no <code>py:deco</code> role to link to a decorator that is marked up with this directive; rather, use the <code>py:func</code> role.</p>
<dt><code>.. py:decoratormethod:: name</code></p>
<dd>
<dt><code>.. py:decoratormethod:: name(signature)</code></p>
<dd> Same as <code>py:decorator</code>, but for decorators that are methods. </p>
<p> Refer to a decorator method using the <code>py:meth</code> role.</dl>
<h3>Python Signatures</h3>
<p> Signatures of functions, methods and class constructors can be given like they would be written in Python. </p>
<p> Default values for optional arguments can be given (but if they contain commas, they will confuse the signature parser). Python 3-style argument annotations can also be given as well as return type annotations: </p>
<pre>
.. py:function:: compile(source : string, filename, symbol='file') -&gt; ast object
</pre>
<p> For functions with optional parameters that don&#8217;t have default values (typically functions implemented in C extension modules without keyword argument support), you can use brackets to specify the optional parts:</p>
<dl>
<dt><code>compile(source[, filename[, symbol]])</code></p>
<dd>
<p> It is customary to put the opening bracket before the comma.</dl>
<h3>Info field lists</h3>
<p> New in version 0.4. </p>
<p> Inside Python object description directives, reST field lists with these fields are recognized and formatted nicely:</p>
<dl>
<dt>&bull;</p>
<dd> <code>param</code>, <code>parameter</code>, <code>arg</code>, <code>argument</code>, <code>key</code>, <code>keyword</code>: Description of a parameter.</p>
<dt>&bull;</p>
<dd> <code>type</code>: Type of a parameter.</p>
<dt>&bull;</p>
<dd> <code>raises</code>, <code>raise</code>, <code>except</code>, <code>exception</code>: That (and when) a specific exception is raised.</p>
<dt>&bull;</p>
<dd> <code>var</code>, <code>ivar</code>, <code>cvar</code>: Description of a variable.</p>
<dt>&bull;</p>
<dd> <code>returns</code>, <code>return</code>: Description of the return value.</p>
<dt>&bull;</p>
<dd> <code>rtype</code>: Return type. </p>
<p> The field names must consist of one of these keywords and an argument (except for <code>returns</code> and <code>rtype</code>, which do not need an argument). This is best explained by an example: </p>
<pre>
.. py:function:: send_message(sender, recipient, message_body, [priority=1])
   Send a message to a recipient
   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring
</pre>
<p> This will render like this:</p>
<dt><code>send_message(sender, recipient, message_body[, priority=1])</code></p>
<dd> Send a message to a recipient</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>sender</code> (<i>str</i>) &#8212; The person sending the message</p>
<dt>&bull;</p>
<dd> <code>recipient</code> (<i>str</i>) &#8212; The recipient of the message</p>
<dt>&bull;</p>
<dd> <code>message_body</code> (<i>str</i>) &#8212; The body of the message</p>
<dt>&bull;</p>
<dd> <code>priority</code> (<i>integer or None</i>) &#8212; The priority of the message, can be a number 1-5</p>
<dt><code>Returns</code></p>
<dd> the message id</p>
<dt><code>Return type</code></p>
<dd> int</p>
<dt><code>Raises</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>ValueError</code> &#8212; if the message_body exceeds 160 characters</p>
<dt>&bull;</p>
<dd> <code>TypeError</code> &#8212; if the message_body is not a basestring </p>
<p> It is also possible to combine parameter type and description, if the type is a single word, like this: </p>
<pre>
:param int priority: The priority of the message, can be a number 1-5
</pre>
</dl>
<h3>Cross-referencing Python objects</h3>
<p> The following roles refer to objects in modules and are possibly hyperlinked if a matching identifier is found:</p>
<dl>
<dt><code>:py:mod:</code></p>
<dd> Reference a module; a dotted name may be used. This should also be used for package names.</p>
<dt><code>:py:func:</code></p>
<dd> Reference a Python function; dotted names may be used. The role text needs not include trailing parentheses to enhance readability; they will be added automatically by Sphinx if the <code>add_function_parentheses</code> config value is true (the default).</p>
<dt><code>:py:data:</code></p>
<dd> Reference a module-level variable.</p>
<dt><code>:py:const:</code></p>
<dd> Reference a &quot;defined&quot; constant. This may be a Python variable that is not intended to be changed.</p>
<dt><code>:py:class:</code></p>
<dd> Reference a class; a dotted name may be used.</p>
<dt><code>:py:meth:</code></p>
<dd> Reference a method of an object. The role text can include the type name and the method name; if it occurs within the description of a type, the type name can be omitted. A dotted name may be used.</p>
<dt><code>:py:attr:</code></p>
<dd> Reference a data attribute of an object.</p>
<dt><code>:py:exc:</code></p>
<dd> Reference an exception. A dotted name may be used.</p>
<dt><code>:py:obj:</code></p>
<dd> Reference an object of unspecified type. Useful e.g. as the <code>default_role</code>. </p>
<p> New in version 0.4. </p>
<p> The name enclosed in this markup can include a module name and/or a class name. For example, <code>:py:func:`filter`</code> could refer to a function named <code>filter</code> in the current module, or the built-in function of that name. In contrast, <code>:py:func:`foo.filter`</code> clearly refers to the <code>filter</code> function in the <code>foo</code> module. </p>
<p> Normally, names in these roles are searched first without any further qualification, then with the current module name prepended, then with the current module and class name (if any) prepended. If you prefix the name with a dot, this order is reversed. For example, in the documentation of Python&#8217;s <code>codecs</code> module, <code>:py:func:`open`</code> always refers to the built-in function, while <code>:py:func:`.open`</code> refers to <code>codecs.open()</code>. </p>
<p> A similar heuristic is used to determine whether the name is an attribute of the currently documented class. </p>
<p> Also, if the name is prefixed with a dot, and no exact match is found, the target is taken as a suffix and all object names with that suffix are searched. For example, <code>:py:meth:`.TarFile.close`</code> references the <code>tarfile.TarFile.close()</code> function, even if the current module is not <code>tarfile</code>. Since this can get ambiguous, if there is more than one possible match, you will get a warning from Sphinx. </p>
<p> Note that you can combine the <code>~</code> and <code>.</code> prefixes: <code>:py:meth:`~.TarFile.close`</code> will reference the <code>tarfile.TarFile.close()</code> method, but the visible link caption will only be <code>close()</code>.</dl>
<h3>The C Domain</h3>
<p> The C domain (name <code>c</code>) is suited for documentation of C API.</p>
<dl>
<dt><code>.. c:function:: type name(signature)</code></p>
<dd> Describes a C function. The signature should be given as in C, e.g.: </p>
<pre>
.. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
</pre>
<p> This is also used to describe function-like preprocessor macros. The names of the arguments should be given so they may be used in the description. </p>
<p> Note that you don&#8217;t have to backslash-escape asterisks in the signature, as it is not parsed by the reST inliner.</p>
<dt><code>.. c:member:: type name</code></p>
<dd> Describes a C struct member. Example signature: </p>
<pre>
.. c:member:: PyObject* PyTypeObject.tp_bases
</pre>
<p> The text of the description should include the range of values allowed, how the value should be interpreted, and whether the value can be changed. References to structure members in text should use the <code>member</code> role.</p>
<dt><code>.. c:macro:: name</code></p>
<dd> Describes a &quot;simple&quot; C macro. Simple macros are macros which are used for code expansion, but which do not take arguments so cannot be described as functions. This is a simple C-language <code>#define</code>. Examples of its use in the Python documentation include <code>PyObject_HEAD</code> and <code>Py_BEGIN_ALLOW_THREADS</code>.</p>
<dt><code>.. c:type:: name</code></p>
<dd> Describes a C type (whether defined by a typedef or struct). The signature should just be the type name.</p>
<dt><code>.. c:var:: type name</code></p>
<dd> Describes a global C variable. The signature should include the type, such as: </p>
<pre>
.. c:var:: PyObject* PyClass_Type
</pre>
</dl>
<h3>Cross-referencing C constructs</h3>
<p> The following roles create cross-references to C-language constructs if they are defined in the documentation:</p>
<dl>
<dt><code>:c:data:</code></p>
<dd> Reference a C-language variable.</p>
<dt><code>:c:func:</code></p>
<dd> Reference a C-language function. Should include trailing parentheses.</p>
<dt><code>:c:macro:</code></p>
<dd> Reference a &quot;simple&quot; C macro, as defined above.</p>
<dt><code>:c:type:</code></p>
<dd> Reference a C-language type.</dl>
<h3>The C++ Domain</h3>
<p> The C++ domain (name <code>cpp</code>) supports documenting C++ projects. </p>
<p> The following directives are available:</p>
<dl>
<dt><code>.. cpp:class:: signatures</code></p>
<dd>
<dt><code>.. cpp:function:: signatures</code></p>
<dd>
<dt><code>.. cpp:member:: signatures</code></p>
<dd>
<dt><code>.. cpp:type:: signatures</code></p>
<dd> Describe a C++ object. Full signature specification is supported &#8212; give the signature as you would in the declaration. Here some examples: </p>
<pre>
.. cpp:function:: bool namespaced::theclass::method(int arg1, std::string arg2)
   Describes a method with parameters and types.
.. cpp:function:: bool namespaced::theclass::method(arg1, arg2)
   Describes a method without types.
.. cpp:function:: const T &amp;array&lt;T&gt;::operator[]() const
   Describes the constant indexing operator of a templated array.
.. cpp:function:: operator bool() const
   Describe a casting operator here.
.. cpp:function:: constexpr void foo(std::string &amp;bar[2]) noexcept
   Describe a constexpr function here.
.. cpp:member:: std::string theclass::name
.. cpp:member:: std::string theclass::name[N][M]
.. cpp:type:: theclass::const_iterator
</pre>
<p> Will be rendered like this:</p>
<dt><code>bool namespaced::theclass::method(int </code><i>arg1</i>, std::string <i>arg2</i>)</p>
<dd> Describes a method with parameters and types.</p>
<dt><code>bool namespaced::theclass::method(</code><i>arg1</i>, <i>arg2</i>)</p>
<dd> Describes a method without types.</p>
<dt><code>const T&amp; array&lt;T&gt;::operator[]() const</code></p>
<dd> Describes the constant indexing operator of a templated array.</p>
<dt><code>operator bool() const</code></p>
<dd> Describe a casting operator here.</p>
<dt><code>constexpr void foo(std::string&amp; </code><i>bar</i>[2]) noexcept</p>
<dd> Describe a constexpr function here.</p>
<dt><code>std::string theclass::name</code></p>
<dd>
<dt><code>std::string theclass::name[N][M]</code></p>
<dd>
<dt><code>type theclass::const_iterator</code></p>
<dd>
<dt><code>.. cpp:namespace:: namespace</code></p>
<dd> Select the current C++ namespace for the following objects. </p>
<p> These roles link to the given object types:</p>
<dt><code>:cpp:class:</code></p>
<dd>
<dt><code>:cpp:func:</code></p>
<dd>
<dt><code>:cpp:member:</code></p>
<dd>
<dt><code>:cpp:type:</code></p>
<dd> Reference a C++ object. You can give the full signature (and need to, for overloaded functions.) </p>
<p> <code>NOTE:</code> Sphinx&#8217; syntax to give references a custom title can interfere with linking to template classes, if nothing follows the closing angle bracket, i.e. if the link looks like this: <code>:cpp:class:`MyClass&lt;T&gt;`</code>. This is interpreted as a link to <code>T</code> with a title of <code>MyClass</code>. In this case, please escape the opening angle bracket with a backslash, like this: <code>:cpp:class:`MyClass\&lt;T&gt;`</code>.</p>
<dt>Note on References</p>
<dd>
<p> It is currently impossible to link to a specific version of an overloaded method. Currently the C++ domain is the first domain that has basic support for overloaded methods and until there is more data for comparison we don&#8217;t want to select a bad syntax to reference a specific overload. Currently Sphinx will link to the first overloaded version of the method / function.</dl>
<h3>The Standard Domain</h3>
<p> The so-called &quot;standard&quot; domain collects all markup that doesn&#8217;t warrant a domain of its own. Its directives and roles are not prefixed with a domain name. </p>
<p> The standard domain is also where custom object descriptions, added using the <code>add_object_type()</code> API, are placed. </p>
<p> There is a set of directives allowing documenting command-line programs:</p>
<dl>
<dt><code>.. option:: name args, name args, &#8230;</code></p>
<dd> Describes a command line argument or switch. Option argument names should be enclosed in angle brackets. Examples: </p>
<pre>
.. option:: dest_dir
   Destination directory.
.. option:: -m &lt;module&gt;, --module &lt;module&gt;
   Run a module as a script.
</pre>
<p> The directive will create cross-reference targets for the given options, referencable by <code>option</code> (in the example case, you&#8217;d use something like <code>:option:`dest_dir`</code>, <code>:option:`-m`</code>, or <code>:option:`&#8211;module`</code>).</p>
<dt><code>.. envvar:: name</code></p>
<dd> Describes an environment variable that the documented code or program uses or defines. Referencable by <code>envvar</code>.</p>
<dt><code>.. program:: name</code></p>
<dd> Like <code>py:currentmodule</code>, this directive produces no output. Instead, it serves to notify Sphinx that all following <code>option</code> directives document options for the program called <i>name</i>. </p>
<p> If you use <code>program</code>, you have to qualify the references in your <code>option</code> roles by the program name, so if you have the following situation </p>
<pre>
.. program:: rm
.. option:: -r
   Work recursively.
.. program:: svn
.. option:: -r revision
   Specify the revision to work upon.
</pre>
<p> then <code>:option:`rm -r`</code> would refer to the first option, while <code>:option:`svn -r`</code> would refer to the second one. </p>
<p> The program name may contain spaces (in case you want to document subcommands like <code>svn add</code> and <code>svn commit</code> separately). </p>
<p> New in version 0.5. </p>
<p> There is also a very generic object description directive, which is not tied to any domain:</p>
<dt><code>.. describe:: text</code></p>
<dd>
<dt><code>.. object:: text</code></p>
<dd> This directive produces the same formatting as the specific ones provided by domains, but does not create index entries or cross-referencing targets. Example: </p>
<pre>
.. describe:: PAPER
   You can set this variable to select a paper size.
</pre>
</dl>
<h3>The JavaScript Domain</h3>
<p> The JavaScript domain (name <code>js</code>) provides the following directives:</p>
<dl>
<dt><code>.. js:function:: name(signature)</code></p>
<dd> Describes a JavaScript function or method. If you want to describe arguments as optional use square brackets as <i>documented</i> for Python signatures. </p>
<p> You can use fields to give more details about arguments and their expected types, errors which may be thrown by the function, and the value being returned: </p>
<pre>
.. js:function:: $.getJSON(href, callback[, errback])
   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.
</pre>
<p> This is rendered as:</p>
<dt><code>$.getJSON(href, callback[, errback])</code></p>
<dd>
<dt><code>Arguments</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>href</code> (<i>string</i>) &#8212; An URI to the location of the resource.</p>
<dt>&bull;</p>
<dd> <code>callback</code> &#8212; Gets called with the object.</p>
<dt>&bull;</p>
<dd> <code>errback</code> &#8212; Gets called in case the request fails. And a lot of other text so we need multiple lines.</p>
<dt><code>Throws SomeError</code></p>
<dd> For whatever reason in that case.</p>
<dt><code>Returns</code></p>
<dd> Something.</p>
<dt><code>.. js:class:: name</code></p>
<dd> Describes a constructor that creates an object. This is basically like a function but will show up with a <i>class</i> prefix: </p>
<pre>
.. js:class:: MyAnimal(name[, age])
   :param string name: The name of the animal
   :param number age: an optional age for the animal
</pre>
<p> This is rendered as:</p>
<dt><code>class MyAnimal(name[, age])</code></p>
<dd>
<dt><code>Arguments</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> (<i>string</i>) &#8212; The name of the animal</p>
<dt>&bull;</p>
<dd> <code>age</code> (<i>number</i>) &#8212; an optional age for the animal</p>
<dt><code>.. js:data:: name</code></p>
<dd> Describes a global variable or constant.</p>
<dt><code>.. js:attribute:: object.name</code></p>
<dd> Describes the attribute <i>name</i> of <i>object</i>. </p>
<p> These roles are provided to refer to the described objects:</p>
<dt><code>:js:func:</code></p>
<dd>
<dt><code>:js:class:</code></p>
<dd>
<dt><code>:js:data:</code></p>
<dd>
<dt><code>:js:attr:</code></p>
<dd></dl>
<h3>The reStructuredText domain</h3>
<p> The reStructuredText domain (name <code>rst</code>) provides the following directives:</p>
<dl>
<dt><code>.. rst:directive:: name</code></p>
<dd> Describes a reST directive. The <i>name</i> can be a single directive name or actual directive syntax (<i>..</i> prefix and <i>::</i> suffix) with arguments that will be rendered differently. For example: </p>
<pre>
.. rst:directive:: foo
   Foo description.
.. rst:directive:: .. bar:: baz
   Bar description.
</pre>
<p> will be rendered as:</p>
<dt><code>.. foo::</code></p>
<dd> Foo description.</p>
<dt><code>.. bar:: baz</code></p>
<dd> Bar description.</p>
<dt><code>.. rst:role:: name</code></p>
<dd> Describes a reST role. For example: </p>
<pre>
.. rst:role:: foo
   Foo description.
</pre>
<p> will be rendered as:</p>
<dt><code>:foo:</code></p>
<dd> Foo description. </p>
<p> These roles are provided to refer to the described objects:</p>
<dt><code>:rst:dir:</code></p>
<dd>
<dt><code>:rst:role:</code></p>
<dd></dl>
<h3>More domains</h3>
<p> The <i>sphinx-contrib</i> repository contains more domains available as extensions; currently <i>Ada</i>, <i>CoffeeScript</i>, <i>Erlang</i>, <i>HTTP</i>, <i>Lasso</i>, <i>MATLAB</i>, <i>PHP</i>, and <i>Ruby</i> domains. Also available are domains for <i>Common Lisp</i>, <i>dqn</i>, <i>Go</i>, <i>Jinja</i>, <i>Operation</i>, and <i>Scala</i>.</p>
<h2>AVAILABLE BUILDERS</h2>
<p> These are the built-in Sphinx builders. More builders can be added by <i>extensions</i>. </p>
<p> The builder&#8217;s &quot;name&quot; must be given to the <code>-b</code> command-line option of <code>sphinx-build</code> to select a builder.</p>
<dl>
<dt><code>class sphinx.builders.html.StandaloneHTMLBuilder</code></p>
<dd> This is the standard HTML builder. Its output is a directory with HTML files, complete with style sheets and optionally the reST sources. There are quite a few configuration values that customize the output of this builder, see the chapter <i>html-options</i> for details.</p>
<dt><code>name = &#8216;html&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<dt><code>class sphinx.builders.html.DirectoryHTMLBuilder</code></p>
<dd> This is a subclass of the standard HTML builder. Its output is a directory with HTML files, where each file is called <code>index.html</code> and placed in a subdirectory named like its page name. For example, the document <code>markup/rest.rst</code> will not result in an output file <code>markup/rest.html</code>, but <code>markup/rest/index.html</code>. When generating links between pages, the <code>index.html</code> is omitted, so that the URL would look like <code>markup/rest/</code>.</p>
<dt><code>name = &#8216;dirhtml&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<p> New in version 0.6. </p>
<dt><code>class sphinx.builders.html.SingleFileHTMLBuilder</code></p>
<dd> This is an HTML builder that combines the whole project in one output file. (Obviously this only works with smaller projects.) The file is named like the master document. No indices will be generated.</p>
<dt><code>name = &#8216;singlehtml&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<p> New in version 1.0. </p>
<dt><code>class sphinx.builders.htmlhelp.HTMLHelpBuilder</code></p>
<dd> This builder produces the same output as the standalone HTML builder, but also generates HTML Help support files that allow the Microsoft HTML Help Workshop to compile them into a CHM file.</p>
<dt><code>name = &#8216;htmlhelp&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<dt><code>class sphinx.builders.qthelp.QtHelpBuilder</code></p>
<dd> This builder produces the same output as the standalone HTML builder, but also generates <i>Qt help</i> collection support files that allow the Qt collection generator to compile them.</p>
<dt><code>name = &#8216;qthelp&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<dt><code>class sphinx.builders.devhelp.DevhelpBuilder</code></p>
<dd> This builder produces the same output as the standalone HTML builder, but also generates <i>GNOME Devhelp</i> support file that allows the GNOME Devhelp reader to view them.</p>
<dt><code>name = &#8216;devhelp&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<dt><code>class sphinx.builders.epub.EpubBuilder</code></p>
<dd> This builder produces the same output as the standalone HTML builder, but also generates an <i>epub</i> file for ebook readers. See <i>epub-faq</i> for details about it. For definition of the epub format, have a look at <i><a rel="nofollow" href="http://idpf.org/epub">http://idpf.org/epub</a></i> or <i><a href="http://en.wikipedia.org/wiki/EPUB">http://en.wikipedia.org/wiki/EPUB</a></i>. The builder creates <i>EPUB 2</i> files.</p>
<dt><code>name = &#8216;epub&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<dt><code>class sphinx.builders.latex.LaTeXBuilder</code></p>
<dd> This builder produces a bunch of LaTeX files in the output directory. You have to specify which documents are to be included in which LaTeX files via the <code>latex_documents</code> configuration value. There are a few configuration values that customize the output of this builder, see the chapter <i>latex-options</i> for details. </p>
<p> <code>NOTE:</code> The produced LaTeX file uses several LaTeX packages that may not be present in a &quot;minimal&quot; TeX distribution installation. For TeXLive, the following packages need to be installed:</p>
<dt>&bull;</p>
<dd> latex-recommended</p>
<dt>&bull;</p>
<dd> latex-extra</p>
<dt>&bull;</p>
<dd> fonts-recommended</p>
<dt><code>name = &#8216;latex&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;application/pdf&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<p> Note that a direct PDF builder using ReportLab is available in <i>rst2pdf</i> version 0.12 or greater. You need to add <code>&#8216;rst2pdf.pdfbuilder&#8217;</code> to your <code>extensions</code> to enable it, its name is <code>pdf</code>. Refer to the <i>rst2pdf manual</i> for details.</p>
<dt><code>class sphinx.builders.text.TextBuilder</code></p>
<dd> This builder produces a text file for each reST file &#8212; this is almost the same as the reST source, but with much of the markup stripped for better readability.</p>
<dt><code>name = &#8216;text&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<p> New in version 0.4. </p>
<dt><code>class sphinx.builders.manpage.ManualPageBuilder</code></p>
<dd> This builder produces manual pages in the groff format. You have to specify which documents are to be included in which manual pages via the <code>man_pages</code> configuration value.</p>
<dt><code>name = &#8216;man&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<p> <code>NOTE:</code> This builder requires the docutils manual page writer, which is only available as of docutils 0.6. </p>
<p> New in version 1.0. </p>
<dt><code>class sphinx.builders.texinfo.TexinfoBuilder</code></p>
<dd> This builder produces Texinfo files that can be processed into Info files by the <code>makeinfo</code> program. You have to specify which documents are to be included in which Texinfo files via the <code>texinfo_documents</code> configuration value. </p>
<p> The Info format is the basis of the on-line help system used by GNU Emacs and the terminal-based program <code>info</code>. See <i>texinfo-faq</i> for more details. The Texinfo format is the official documentation system used by the GNU project. More information on Texinfo can be found at <i><a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></i>.</p>
<dt><code>name = &#8216;texinfo&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/png&#8217;, &#8216;image/jpeg&#8217;, &#8216;image/gif&#8217;]</code></p>
<dd>
<p> New in version 1.1. </p>
<dt><code>class sphinx.builders.html.SerializingHTMLBuilder</code></p>
<dd> This builder uses a module that implements the Python serialization API (<i>pickle</i>, <i>simplejson</i>, <i>phpserialize</i>, and others) to dump the generated HTML documentation. The pickle builder is a subclass of it. </p>
<p> A concrete subclass of this builder serializing to the <i>PHP serialization</i> format could look like this: </p>
<pre>
import phpserialize
class PHPSerializedBuilder(SerializingHTMLBuilder):
    name = 'phpserialized'
    implementation = phpserialize
    out_suffix = '.file.phpdump'
    globalcontext_filename = 'globalcontext.phpdump'
    searchindex_filename = 'searchindex.phpdump'
</pre>
<dt><code>implementation</code></p>
<dd> A module that implements <i>dump()</i>, <i>load()</i>, <i>dumps()</i> and <i>loads()</i> functions that conform to the functions with the same names from the pickle module. Known modules implementing this interface are <i>simplejson</i> (or <i>json</i> in Python 2.6), <i>phpserialize</i>, <i>plistlib</i>, and others.</p>
<dt><code>out_suffix</code></p>
<dd> The suffix for all regular files.</p>
<dt><code>globalcontext_filename</code></p>
<dd> The filename for the file that contains the &quot;global context&quot;. This is a dict with some general configuration values such as the name of the project.</p>
<dt><code>searchindex_filename</code></p>
<dd> The filename for the search index Sphinx generates. </p>
<p> See <i>serialization-details</i> for details about the output format. </p>
<p> New in version 0.5. </p>
<dt><code>class sphinx.builders.html.PickleHTMLBuilder</code></p>
<dd> This builder produces a directory with pickle files containing mostly HTML fragments and TOC information, for use of a web application (or custom postprocessing tool) that doesn&#8217;t use the standard HTML templates. </p>
<p> See <i>serialization-details</i> for details about the output format.</p>
<dt><code>name = &#8216;pickle&#8217;</code></p>
<dd> The old name <code>web</code> still works as well.</p>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<p> The file suffix is <code>.fpickle</code>. The global context is called <code>globalcontext.pickle</code>, the search index <code>searchindex.pickle</code>.</p>
<dt><code>class sphinx.builders.html.JSONHTMLBuilder</code></p>
<dd> This builder produces a directory with JSON files containing mostly HTML fragments and TOC information, for use of a web application (or custom postprocessing tool) that doesn&#8217;t use the standard HTML templates. </p>
<p> See <i>serialization-details</i> for details about the output format.</p>
<dt><code>name = &#8216;json&#8217;</code></p>
<dd>
<dt><code>supported_image_types = [&#8216;image/svg+xml&#8217;, &#8216;image/png&#8217;, &#8216;image/gif&#8217;, &#8216;image/jpeg&#8217;]</code></p>
<dd>
<p> The file suffix is <code>.fjson</code>. The global context is called <code>globalcontext.json</code>, the search index <code>searchindex.json</code>. </p>
<p> New in version 0.5. </p>
<dt><code>class sphinx.builders.gettext.MessageCatalogBuilder</code></p>
<dd> This builder produces gettext-style message catalogs. Each top-level file or subdirectory grows a single <code>.pot</code> catalog template. </p>
<p> See the documentation on <i>intl</i> for further reference.</p>
<dt><code>name = &#8216;gettext&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<p> New in version 1.1. </p>
<dt><code>class sphinx.builders.changes.ChangesBuilder</code></p>
<dd> This builder produces an HTML overview of all <code>versionadded</code>, <code>versionchanged</code> and <code>deprecated</code> directives for the current <code>version</code>. This is useful to generate a ChangeLog file, for example.</p>
<dt><code>name = &#8216;changes&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<dt><code>class sphinx.builders.linkcheck.CheckExternalLinksBuilder</code></p>
<dd> This builder scans all documents for external links, tries to open them with <code>urllib2</code>, and writes an overview which ones are broken and redirected to standard output and to <code>output.txt</code> in the output directory.</p>
<dt><code>name = &#8216;linkcheck&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<dt><code>class sphinx.builders.xml.XMLBuilder</code></p>
<dd> This builder produces Docutils-native XML files. The output can be transformed with standard XML tools such as XSLT processors into arbitrary final forms.</p>
<dt><code>name = &#8216;xml&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<p> New in version 1.2. </p>
<dt><code>class sphinx.builders.xml.PseudoXMLBuilder</code></p>
<dd> This builder is used for debugging the Sphinx/Docutils &quot;Reader to Transform to Writer&quot; pipeline. It produces compact pretty-printed &quot;pseudo-XML&quot;, files where nesting is indicated by indentation (no end-tags). External attributes for all elements are output, and internal attributes for any leftover &quot;pending&quot; elements are also given.</p>
<dt><code>name = &#8216;pseudoxml&#8217;</code></p>
<dd>
<dt><code>supported_image_types = []</code></p>
<dd>
<p> New in version 1.2. </p>
<p> Built-in Sphinx extensions that offer more builders are:</p>
<dt>&bull;</p>
<dd> <code>doctest</code></p>
<dt>&bull;</p>
<dd> <code>coverage</code></dl>
<h3>Serialization builder details</h3>
<p> All serialization builders outputs one file per source file and a few special files. They also copy the reST source files in the directory <code>_sources</code> under the output directory. </p>
<p> The <code>PickleHTMLBuilder</code> is a builtin subclass that implements the pickle serialization interface. </p>
<p> The files per source file have the extensions of <code>out_suffix</code>, and are arranged in directories just as the source files are. They unserialize to a dictionary (or dictionary like structure) with these keys:</p>
<dl>
<dt><code>body</code></p>
<dd> The HTML &quot;body&quot; (that is, the HTML rendering of the source file), as rendered by the HTML translator.</p>
<dt><code>title</code></p>
<dd> The title of the document, as HTML (may contain markup).</p>
<dt><code>toc</code></p>
<dd> The table of contents for the file, rendered as an HTML <code>&lt;ul&gt;</code>.</p>
<dt><code>display_toc</code></p>
<dd> A boolean that is <code>True</code> if the <code>toc</code> contains more than one entry.</p>
<dt><code>current_page_name</code></p>
<dd> The document name of the current file.</p>
<dt><code>parents</code>, <code>prev</code> and <code>next</code></p>
<dd> Information about related chapters in the TOC tree. Each relation is a dictionary with the keys <code>link</code> (href for the relation) and <code>title</code> (title of the related document, as HTML). <code>parents</code> is a list of relations, while <code>prev</code> and <code>next</code> are a single relation.</p>
<dt><code>sourcename</code></p>
<dd> The name of the source file under <code>_sources</code>. </p>
<p> The special files are located in the root output directory. They are:</p>
<dt><code>SerializingHTMLBuilder.globalcontext_filename</code></p>
<dd> A pickled dict with these keys:</p>
<dt><code>project</code>, <code>copyright</code>, <code>release</code>, <code>version</code></p>
<dd> The same values as given in the configuration file.</p>
<dt><code>style</code></p>
<dd> <code>html_style</code>.</p>
<dt><code>last_updated</code></p>
<dd> Date of last build.</p>
<dt><code>builder</code></p>
<dd> Name of the used builder, in the case of pickles this is always <code>&#8216;pickle&#8217;</code>.</p>
<dt><code>titles</code></p>
<dd> A dictionary of all documents&#8217; titles, as HTML strings.</p>
<dt><code>SerializingHTMLBuilder.searchindex_filename</code></p>
<dd> An index that can be used for searching the documentation. It is a pickled list with these entries:</p>
<dt>&bull;</p>
<dd> A list of indexed docnames.</p>
<dt>&bull;</p>
<dd> A list of document titles, as HTML strings, in the same order as the first list.</p>
<dt>&bull;</p>
<dd> A dict mapping word roots (processed by an English-language stemmer) to a list of integers, which are indices into the first list.</p>
<dt><code>environment.pickle</code></p>
<dd> The build environment. This is always a pickle file, independent of the builder and a copy of the environment that was used when the builder was started.</dl>
<h3>Todo</h3>
<p> Document common members. </p>
<p> Unlike the other pickle files this pickle file requires that the <code>sphinx</code> package is available on unpickling.</p>
<h2>THE BUILD CONFIGURATION FILE</h2>
<p> The <i>configuration directory</i> must contain a file named <code>conf.py</code>. This file (containing Python code) is called the &quot;build configuration file&quot; and contains all configuration needed to customize Sphinx input and output behavior. </p>
<p> The configuration file is executed as Python code at build time (using <code>execfile()</code>, and with the current directory set to its containing directory), and therefore can execute arbitrarily complex code. Sphinx then reads simple names from the file&#8217;s namespace as its configuration. </p>
<p> Important points to note:</p>
<dl>
<dt>&bull;</p>
<dd> If not otherwise documented, values must be strings, and their default is the empty string.</p>
<dt>&bull;</p>
<dd> The term &quot;fully-qualified name&quot; refers to a string that names an importable Python object inside a module; for example, the FQN <code>&quot;sphinx.builders.Builder&quot;</code> means the <code>Builder</code> class in the <code>sphinx.builders</code> module.</p>
<dt>&bull;</p>
<dd> Remember that document names use <code>/</code> as the path separator and don&#8217;t contain the file name extension.</p>
<dt>&bull;</p>
<dd> Since <code>conf.py</code> is read as a Python file, the usual rules apply for encodings and Unicode support: declare the encoding using an encoding cookie (a comment like <code># -*- coding: utf-8 -*-</code>) and use Unicode string literals when you include non-ASCII characters in configuration values.</p>
<dt>&bull;</p>
<dd> The contents of the config namespace are pickled (so that Sphinx can find out when configuration changes), so it may not contain unpickleable values &#8212; delete them from the namespace with <code>del</code> if appropriate. Modules are removed automatically, so you don&#8217;t need to <code>del</code> your imports after use.</p>
<dt>&bull;</p>
<dd> There is a special object named <code>tags</code> available in the config file. It can be used to query and change the tags (see <i>tags</i>). Use <code>tags.has(&#8216;tag&#8217;)</code> to query, <code>tags.add(&#8216;tag&#8217;)</code> and <code>tags.remove(&#8216;tag&#8217;)</code> to change. Note that the current builder tag is not available in <code>conf.py</code>, as it is created <i>after</i> the builder is initialized.</dl>
<h3>General configuration</h3>
<dl>
<dt><code>extensions</code></p>
<dd> A list of strings that are module names of Sphinx extensions. These can be extensions coming with Sphinx (named <code>sphinx.ext.*</code>) or custom ones. </p>
<p> Note that you can extend <code>sys.path</code> within the conf file if your extensions live in another directory &#8212; but make sure you use absolute paths. If your extension path is relative to the <i>configuration directory</i>, use <code>os.path.abspath()</code> like so: </p>
<pre>
import sys, os
sys.path.append(os.path.abspath('sphinxext'))
extensions = ['extname']
</pre>
<p> That way, you can load an extension called <code>extname</code> from the subdirectory <code>sphinxext</code>. </p>
<p> The configuration file itself can be an extension; for that, you only need to provide a <code>setup()</code> function in it.</p>
<dt><code>source_suffix</code></p>
<dd> The file name extension of source files. Only files with this suffix will be read as sources. Default is <code>&#8216;.rst&#8217;</code>.</p>
<dt><code>source_encoding</code></p>
<dd> The encoding of all reST source files. The recommended encoding, and the default value, is <code>&#8216;utf-8-sig&#8217;</code>. </p>
<p> New in version 0.5: Previously, Sphinx accepted only UTF-8 encoded sources. </p>
<dt><code>master_doc</code></p>
<dd> The document name of the &quot;master&quot; document, that is, the document that contains the root <code>toctree</code> directive. Default is <code>&#8216;contents&#8217;</code>.</p>
<dt><code>exclude_patterns</code></p>
<dd> A list of glob-style patterns that should be excluded when looking for source files. [1] They are matched against the source file names relative to the source directory, using slashes as directory separators on all platforms. </p>
<p> Example patterns:</p>
<dt>&bull;</p>
<dd> <code>&#8216;library/xml.rst&#8217;</code> &#8212; ignores the <code>library/xml.rst</code> file (replaces entry in <code>unused_docs</code>)</p>
<dt>&bull;</p>
<dd> <code>&#8216;library/xml&#8217;</code> &#8212; ignores the <code>library/xml</code> directory (replaces entry in <code>exclude_trees</code>)</p>
<dt>&bull;</p>
<dd> <code>&#8216;library/xml*&#8217;</code> &#8212; ignores all files and directories starting with <code>library/xml</code></p>
<dt>&bull;</p>
<dd> <code>&#8216;**/.svn&#8217;</code> &#8212; ignores all <code>.svn</code> directories (replaces entry in <code>exclude_dirnames</code>) </p>
<p> <code>exclude_patterns</code> is also consulted when looking for static files in <code>html_static_path</code>. </p>
<p> New in version 1.0. </p>
<dt><code>unused_docs</code></p>
<dd> A list of document names that are present, but not currently included in the toctree. Use this setting to suppress the warning that is normally emitted in that case. </p>
<p> Deprecated since version 1.0: Use <code>exclude_patterns</code> instead. </p>
<dt><code>exclude_trees</code></p>
<dd> A list of directory paths, relative to the source directory, that are to be recursively excluded from the search for source files, that is, their subdirectories won&#8217;t be searched too. The default is <code>[]</code>. </p>
<p> New in version 0.4. </p>
<p> Deprecated since version 1.0: Use <code>exclude_patterns</code> instead. </p>
<dt><code>exclude_dirnames</code></p>
<dd> A list of directory names that are to be excluded from any recursive operation Sphinx performs (e.g. searching for source files or copying static files). This is useful, for example, to exclude version-control-specific directories like <code>&#8216;CVS&#8217;</code>. The default is <code>[]</code>. </p>
<p> New in version 0.5. </p>
<p> Deprecated since version 1.0: Use <code>exclude_patterns</code> instead. </p>
<dt><code>templates_path</code></p>
<dd> A list of paths that contain extra templates (or templates that overwrite builtin/theme-specific templates). Relative paths are taken as relative to the configuration directory.</p>
<dt><code>template_bridge</code></p>
<dd> A string with the fully-qualified name of a callable (or simply a class) that returns an instance of <code>TemplateBridge</code>. This instance is then used to render HTML documents, and possibly the output of other builders (currently the changes builder). (Note that the template bridge must be made theme-aware if HTML themes are to be used.)</p>
<dt><code>rst_epilog</code></p>
<dd> A string of reStructuredText that will be included at the end of every source file that is read. This is the right place to add substitutions that should be available in every file. An example: </p>
<pre>
rst_epilog = &quot;&quot;&quot;
.. |psf| replace:: Python Software Foundation
&quot;&quot;&quot;
</pre>
<p> New in version 0.6. </p>
<dt><code>rst_prolog</code></p>
<dd> A string of reStructuredText that will be included at the beginning of every source file that is read. </p>
<p> New in version 1.0. </p>
<dt><code>primary_domain</code></p>
<dd> The name of the default <i>domain</i>. Can also be <code>None</code> to disable a default domain. The default is <code>&#8216;py&#8217;</code>. Those objects in other domains (whether the domain name is given explicitly, or selected by a <code>default-domain</code> directive) will have the domain name explicitly prepended when named (e.g., when the default domain is C, Python functions will be named &quot;Python function&quot;, not just &quot;function&quot;). </p>
<p> New in version 1.0. </p>
<dt><code>default_role</code></p>
<dd> The name of a reST role (builtin or Sphinx extension) to use as the default role, that is, for text marked up <code>`like this`</code>. This can be set to <code>&#8216;py:obj&#8217;</code> to make <code>`filter`</code> a cross-reference to the Python function &quot;filter&quot;. The default is <code>None</code>, which doesn&#8217;t reassign the default role. </p>
<p> The default role can always be set within individual documents using the standard reST <code>default-role</code> directive. </p>
<p> New in version 0.4. </p>
<dt><code>keep_warnings</code></p>
<dd> If true, keep warnings as &quot;system message&quot; paragraphs in the built documents. Regardless of this setting, warnings are always written to the standard error stream when <code>sphinx-build</code> is run. </p>
<p> The default is <code>False</code>, the pre-0.5 behavior was to always keep them. </p>
<p> New in version 0.5. </p>
<dt><code>needs_sphinx</code></p>
<dd> If set to a <code>major.minor</code> version string like <code>&#8216;1.1&#8217;</code>, Sphinx will compare it with its version and refuse to build if it is too old. Default is no requirement. </p>
<p> New in version 1.0. </p>
<dt><code>nitpicky</code></p>
<dd> If true, Sphinx will warn about <i>all</i> references where the target cannot be found. Default is <code>False</code>. You can activate this mode temporarily using the <i>-n</i> command-line switch. </p>
<p> New in version 1.0. </p>
<dt><code>nitpick_ignore</code></p>
<dd> A list of <code>(type, target)</code> tuples (by default empty) that should be ignored when generating warnings in &quot;nitpicky mode&quot;. Note that <code>type</code> should include the domain name if present. Example entries would be <code>(&#8216;py:func&#8217;, &#8216;int&#8217;)</code> or <code>(&#8216;envvar&#8217;, &#8216;LD_LIBRARY_PATH&#8217;)</code>. </p>
<p> New in version 1.1. </p>
</dl>
<h3>Project information</h3>
<dl>
<dt><code>project</code></p>
<dd> The documented project&#8217;s name.</p>
<dt><code>copyright</code></p>
<dd> A copyright statement in the style <code>&#8216;2008, Author Name&#8217;</code>.</p>
<dt><code>version</code></p>
<dd> The major project version, used as the replacement for <code>|version|</code>. For example, for the Python documentation, this may be something like <code>2.6</code>.</p>
<dt><code>release</code></p>
<dd> The full project version, used as the replacement for <code>|release|</code> and e.g. in the HTML templates. For example, for the Python documentation, this may be something like <code>2.6.0rc1</code>. </p>
<p> If you don&#8217;t need the separation provided between <code>version</code> and <code>release</code>, just set them both to the same value.</p>
<dt><code>today</code></p>
<dd>
<dt><code>today_fmt</code></p>
<dd> These values determine how to format the current date, used as the replacement for <code>|today|</code>.</p>
<dt>&bull;</p>
<dd> If you set <code>today</code> to a non-empty value, it is used.</p>
<dt>&bull;</p>
<dd> Otherwise, the current time is formatted using <code>time.strftime()</code> and the format given in <code>today_fmt</code>. </p>
<p> The default is no <code>today</code> and a <code>today_fmt</code> of <code>&#8216;%B %d, %Y&#8217;</code> (or, if translation is enabled with <code>language</code>, an equivalent %format for the selected locale).</p>
<dt><code>highlight_language</code></p>
<dd> The default language to highlight source code in. The default is <code>&#8216;python&#8217;</code>. The value should be a valid Pygments lexer name, see <i>code-examples</i> for more details. </p>
<p> New in version 0.5. </p>
<dt><code>pygments_style</code></p>
<dd> The style name to use for Pygments highlighting of source code. The default style is selected by the theme for HTML output, and <code>&#8216;sphinx&#8217;</code> otherwise. </p>
<p> Changed in version 0.3: If the value is a fully-qualified name of a custom Pygments style class, this is then used as custom style. </p>
<dt><code>add_function_parentheses</code></p>
<dd> A boolean that decides whether parentheses are appended to function and method role text (e.g. the content of <code>:func:`input`</code>) to signify that the name is callable. Default is <code>True</code>.</p>
<dt><code>add_module_names</code></p>
<dd> A boolean that decides whether module names are prepended to all <i>object</i> names (for object types where a &quot;module&quot; of some kind is defined), e.g. for <code>py:function</code> directives. Default is <code>True</code>.</p>
<dt><code>show_authors</code></p>
<dd> A boolean that decides whether <code>codeauthor</code> and <code>sectionauthor</code> directives produce any output in the built files.</p>
<dt><code>modindex_common_prefix</code></p>
<dd> A list of prefixes that are ignored for sorting the Python module index (e.g., if this is set to <code>[&#8216;foo.&#8217;]</code>, then <code>foo.bar</code> is shown under <code>B</code>, not <code>F</code>). This can be handy if you document a project that consists of a single package. Works only for the HTML builder currently. Default is <code>[]</code>. </p>
<p> New in version 0.6. </p>
<dt><code>trim_footnote_reference_space</code></p>
<dd> Trim spaces before footnote references that are necessary for the reST parser to recognize the footnote, but do not look too nice in the output. </p>
<p> New in version 0.6. </p>
<dt><code>trim_doctest_flags</code></p>
<dd> If true, doctest flags (comments looking like <code># doctest: FLAG, &#8230;</code>) at the ends of lines and <code>&lt;BLANKLINE&gt;</code> markers are removed for all code blocks showing interactive Python sessions (i.e. doctests). Default is true. See the extension <code>doctest</code> for more possibilities of including doctests. </p>
<p> New in version 1.0. </p>
<p> Changed in version 1.1: Now also removes <code>&lt;BLANKLINE&gt;</code>. </p>
</dl>
<h3>Options for internationalization</h3>
<p> These options influence Sphinx&#8217; <i>Native Language Support</i>. See the documentation on <i>intl</i> for details.</p>
<dl>
<dt><code>language</code></p>
<dd> The code for the language the docs are written in. Any text automatically generated by Sphinx will be in that language. Also, Sphinx will try to substitute individual paragraphs from your documents with the translation sets obtained from <code>locale_dirs</code>. In the LaTeX builder, a suitable language will be selected as an option for the <i>Babel</i> package. Default is <code>None</code>, which means that no translation will be done. </p>
<p> New in version 0.5. </p>
<p> Currently supported languages by Sphinx are:</p>
<dt>&bull;</p>
<dd> <code>bn</code> &#8212; Bengali</p>
<dt>&bull;</p>
<dd> <code>ca</code> &#8212; Catalan</p>
<dt>&bull;</p>
<dd> <code>cs</code> &#8212; Czech</p>
<dt>&bull;</p>
<dd> <code>da</code> &#8212; Danish</p>
<dt>&bull;</p>
<dd> <code>de</code> &#8212; German</p>
<dt>&bull;</p>
<dd> <code>en</code> &#8212; English</p>
<dt>&bull;</p>
<dd> <code>es</code> &#8212; Spanish</p>
<dt>&bull;</p>
<dd> <code>et</code> &#8212; Estonian</p>
<dt>&bull;</p>
<dd> <code>eu</code> &#8212; Basque</p>
<dt>&bull;</p>
<dd> <code>fa</code> &#8212; Iranian</p>
<dt>&bull;</p>
<dd> <code>fi</code> &#8212; Finnish</p>
<dt>&bull;</p>
<dd> <code>fr</code> &#8212; French</p>
<dt>&bull;</p>
<dd> <code>he</code> &#8212; Hebrew</p>
<dt>&bull;</p>
<dd> <code>hr</code> &#8212; Croatian</p>
<dt>&bull;</p>
<dd> <code>hu</code> &#8212; Hungarian</p>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; Indonesian</p>
<dt>&bull;</p>
<dd> <code>it</code> &#8212; Italian</p>
<dt>&bull;</p>
<dd> <code>ja</code> &#8212; Japanese</p>
<dt>&bull;</p>
<dd> <code>ko</code> &#8212; Korean</p>
<dt>&bull;</p>
<dd> <code>lt</code> &#8212; Lithuanian</p>
<dt>&bull;</p>
<dd> <code>lv</code> &#8212; Latvian</p>
<dt>&bull;</p>
<dd> <code>mk</code> &#8212; Macedonian</p>
<dt>&bull;</p>
<dd> <code>nb_NO</code> &#8212; Norwegian Bokmal</p>
<dt>&bull;</p>
<dd> <code>ne</code> &#8212; Nepali</p>
<dt>&bull;</p>
<dd> <code>nl</code> &#8212; Dutch</p>
<dt>&bull;</p>
<dd> <code>pl</code> &#8212; Polish</p>
<dt>&bull;</p>
<dd> <code>pt_BR</code> &#8212; Brazilian Portuguese</p>
<dt>&bull;</p>
<dd> <code>pt_PT</code> &#8212; European Portuguese</p>
<dt>&bull;</p>
<dd> <code>ru</code> &#8212; Russian</p>
<dt>&bull;</p>
<dd> <code>si</code> &#8212; Sinhala</p>
<dt>&bull;</p>
<dd> <code>sk</code> &#8212; Slovak</p>
<dt>&bull;</p>
<dd> <code>sl</code> &#8212; Slovenian</p>
<dt>&bull;</p>
<dd> <code>sv</code> &#8212; Swedish</p>
<dt>&bull;</p>
<dd> <code>tr</code> &#8212; Turkish</p>
<dt>&bull;</p>
<dd> <code>uk_UA</code> &#8212; Ukrainian</p>
<dt>&bull;</p>
<dd> <code>vi</code> &#8212; Vietnamese</p>
<dt>&bull;</p>
<dd> <code>zh_CN</code> &#8212; Simplified Chinese</p>
<dt>&bull;</p>
<dd> <code>zh_TW</code> &#8212; Traditional Chinese</p>
<dt><code>locale_dirs</code></p>
<dd> New in version 0.5. </p>
<p> Directories in which to search for additional message catalogs (see <code>language</code>), relative to the source directory. The directories on this path are searched by the standard <code>gettext</code> module. </p>
<p> Internal messages are fetched from a text domain of <code>sphinx</code>; so if you add the directory <code>./locale</code> to this settting, the message catalogs (compiled from <code>.po</code> format using <code>msgfmt</code>) must be in <code>./locale/</code><i>language</i>/LC_MESSAGES/sphinx.mo. The text domain of individual documents depends on <code>gettext_compact</code>. </p>
<p> The default is <code>[]</code>.</p>
<dt><code>gettext_compact</code></p>
<dd> New in version 1.1. </p>
<p> If true, a document&#8217;s text domain is its docname if it is a top-level project file and its very base directory otherwise. </p>
<p> By default, the document <code>markup/code.rst</code> ends up in the <code>markup</code> text domain. With this option set to <code>False</code>, it is <code>markup/code</code>.</dl>
<h3>Options for HTML output</h3>
<p> These options influence HTML as well as HTML Help output, and other builders that use Sphinx&#8217; HTMLWriter class.</p>
<dl>
<dt><code>html_theme</code></p>
<dd> The &quot;theme&quot; that the HTML output should use. See the <code>section about theming</code>. The default is <code>&#8216;default&#8217;</code>. </p>
<p> New in version 0.6. </p>
<dt><code>html_theme_options</code></p>
<dd> A dictionary of options that influence the look and feel of the selected theme. These are theme-specific. For the options understood by the builtin themes, see <i>this section</i>. </p>
<p> New in version 0.6. </p>
<dt><code>html_theme_path</code></p>
<dd> A list of paths that contain custom themes, either as subdirectories or as zip files. Relative paths are taken as relative to the configuration directory. </p>
<p> New in version 0.6. </p>
<dt><code>html_style</code></p>
<dd> The style sheet to use for HTML pages. A file of that name must exist either in Sphinx&#8217; <code>static/</code> path, or in one of the custom paths given in <code>html_static_path</code>. Default is the stylesheet given by the selected theme. If you only want to add or override a few things compared to the theme&#8217;s stylesheet, use CSS <code>@import</code> to import the theme&#8217;s stylesheet.</p>
<dt><code>html_title</code></p>
<dd> The &quot;title&quot; for HTML documentation generated with Sphinx&#8217; own templates. This is appended to the <code>&lt;title&gt;</code> tag of individual pages, and used in the navigation bar as the &quot;topmost&quot; element. It defaults to <code>&#8216;</code><i>&lt;project&gt;</i> v<i>&lt;revision&gt;</i> documentation&#8217; (with the values coming from the config values).</p>
<dt><code>html_short_title</code></p>
<dd> A shorter &quot;title&quot; for the HTML docs. This is used in for links in the header and in the HTML Help docs. If not given, it defaults to the value of <code>html_title</code>. </p>
<p> New in version 0.4. </p>
<dt><code>html_context</code></p>
<dd> A dictionary of values to pass into the template engine&#8217;s context for all pages. Single values can also be put in this dictionary using the <i>-A</i> command-line option of <code>sphinx-build</code>. </p>
<p> New in version 0.5. </p>
<dt><code>html_logo</code></p>
<dd> If given, this must be the name of an image file (path relative to the <i>configuration directory</i>) that is the logo of the docs. It is placed at the top of the sidebar; its width should therefore not exceed 200 pixels. Default: <code>None</code>. </p>
<p> New in version 0.4.1: The image file will be copied to the <code>_static</code> directory of the output HTML, but only if the file does not already exist there. </p>
<dt><code>html_favicon</code></p>
<dd> If given, this must be the name of an image file (path relative to the <i>configuration directory</i>) that is the favicon of the docs. Modern browsers use this as icon for tabs, windows and bookmarks. It should be a Windows-style icon file (<code>.ico</code>), which is 16&#215;16 or 32&#215;32 pixels large. Default: <code>None</code>. </p>
<p> New in version 0.4: The image file will be copied to the <code>_static</code> directory of the output HTML, but only if the file does not already exist there. </p>
<dt><code>html_static_path</code></p>
<dd> A list of paths that contain custom static files (such as style sheets or script files). Relative paths are taken as relative to the configuration directory. They are copied to the output&#8217;s <code>_static</code> directory after the theme&#8217;s static files, so a file named <code>default.css</code> will overwrite the theme&#8217;s <code>default.css</code>. </p>
<p> Changed in version 0.4: The paths in <code>html_static_path</code> can now contain subdirectories. </p>
<p> Changed in version 1.0: The entries in <code>html_static_path</code> can now be single files. </p>
<dt><code>html_extra_path</code></p>
<dd> A list of paths that contain extra files not directly related to the documentation, such as <code>robots.txt</code> or <code>.htaccess</code>. Relative paths are taken as relative to the configuration directory. They are copied to the output directory. They will overwrite any existing file of the same name. </p>
<p> As these files are not meant to be built, they are automatically added to <code>exclude_patterns</code>. </p>
<p> New in version 1.2. </p>
<dt><code>html_last_updated_fmt</code></p>
<dd> If this is not the empty string, a &#8216;Last updated on:&#8217; timestamp is inserted at every page bottom, using the given <code>strftime()</code> format. Default is <code>&#8216;%b %d, %Y&#8217;</code> (or a locale-dependent equivalent).</p>
<dt><code>html_use_smartypants</code></p>
<dd> If true, <i>SmartyPants</i> will be used to convert quotes and dashes to typographically correct entities. Default: <code>True</code>.</p>
<dt><code>html_add_permalinks</code></p>
<dd> Sphinx will add &quot;permalinks&quot; for each heading and description environment as paragraph signs that become visible when the mouse hovers over them. </p>
<p> This value determines the text for the permalink; it defaults to <code>&quot;Â¶&quot;</code>. Set it to <code>None</code> or the empty string to disable permalinks. </p>
<p> New in version 0.6: Previously, this was always activated. </p>
<p> Changed in version 1.1: This can now be a string to select the actual text of the link. Previously, only boolean values were accepted. </p>
<dt><code>html_sidebars</code></p>
<dd> Custom sidebar templates, must be a dictionary that maps document names to template names. </p>
<p> The keys can contain glob-style patterns [1], in which case all matching documents will get the specified sidebars. (A warning is emitted when a more than one glob-style pattern matches for any document.) </p>
<p> The values can be either lists or single strings.</p>
<dt>&bull;</p>
<dd> If a value is a list, it specifies the complete list of sidebar templates to include. If all or some of the default sidebars are to be included, they must be put into this list as well. </p>
<p> The default sidebars (for documents that don&#8217;t match any pattern) are: <code>[&#8216;localtoc.html&#8217;, &#8216;relations.html&#8217;, &#8216;sourcelink.html&#8217;, &#8216;searchbox.html&#8217;]</code>.</p>
<dt>&bull;</p>
<dd> If a value is a single string, it specifies a custom sidebar to be added between the <code>&#8216;sourcelink.html&#8217;</code> and <code>&#8216;searchbox.html&#8217;</code> entries. This is for compatibility with Sphinx versions before 1.0. </p>
<p> Builtin sidebar templates that can be rendered are:</p>
<dt>&bull;</p>
<dd> <code>localtoc.html</code> &#8212; a fine-grained table of contents of the current document</p>
<dt>&bull;</p>
<dd> <code>globaltoc.html</code> &#8212; a coarse-grained table of contents for the whole documentation set, collapsed</p>
<dt>&bull;</p>
<dd> <code>relations.html</code> &#8212; two links to the previous and next documents</p>
<dt>&bull;</p>
<dd> <code>sourcelink.html</code> &#8212; a link to the source of the current document, if enabled in <code>html_show_sourcelink</code></p>
<dt>&bull;</p>
<dd> <code>searchbox.html</code> &#8212; the &quot;quick search&quot; box </p>
<p> Example: </p>
<pre>
html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
</pre>
<p> This will render the custom template <code>windowssidebar.html</code> and the quick search box within the sidebar of the given document, and render the default sidebars for all other pages (except that the local TOC is replaced by the global TOC). </p>
<p> New in version 1.0: The ability to use globbing keys and to specify multiple sidebars. </p>
<p> Note that this value only has no effect if the chosen theme does not possess a sidebar, like the builtin <code>scrolls</code> and <code>haiku</code> themes.</p>
<dt><code>html_additional_pages</code></p>
<dd> Additional templates that should be rendered to HTML pages, must be a dictionary that maps document names to template names. </p>
<p> Example: </p>
<pre>
html_additional_pages = {
    'download': 'customdownload.html',
}
</pre>
<p> This will render the template <code>customdownload.html</code> as the page <code>download.html</code>.</p>
<dt><code>html_domain_indices</code></p>
<dd> If true, generate domain-specific indices in addition to the general index. For e.g. the Python domain, this is the global module index. Default is <code>True</code>. </p>
<p> This value can be a bool or a list of index names that should be generated. To find out the index name for a specific index, look at the HTML file name. For example, the Python module index has the name <code>&#8216;py-modindex&#8217;</code>. </p>
<p> New in version 1.0. </p>
<dt><code>html_use_modindex</code></p>
<dd> If true, add a module index to the HTML documents. Default is <code>True</code>. </p>
<p> Deprecated since version 1.0: Use <code>html_domain_indices</code>. </p>
<dt><code>html_use_index</code></p>
<dd> If true, add an index to the HTML documents. Default is <code>True</code>. </p>
<p> New in version 0.4. </p>
<dt><code>html_split_index</code></p>
<dd> If true, the index is generated twice: once as a single page with all the entries, and once as one page per starting letter. Default is <code>False</code>. </p>
<p> New in version 0.4. </p>
<dt><code>html_copy_source</code></p>
<dd> If true, the reST sources are included in the HTML build as <code>_sources/</code><i>name</i>. The default is <code>True</code>. </p>
<p> <code>WARNING:</code> If this config value is set to <code>False</code>, the JavaScript search function will only display the titles of matching documents, and no excerpt from the matching contents.</p>
<dt><code>html_show_sourcelink</code></p>
<dd> If true (and <code>html_copy_source</code> is true as well), links to the reST sources will be added to the sidebar. The default is <code>True</code>. </p>
<p> New in version 0.6. </p>
<dt><code>html_use_opensearch</code></p>
<dd> If nonempty, an <i>OpenSearch &lt;<a rel="nofollow" href="http://opensearch.org">http://opensearch.org</a>&gt;</i> description file will be output, and all pages will contain a <code>&lt;link&gt;</code> tag referring to it. Since OpenSearch doesn&#8217;t support relative URLs for its search page location, the value of this option must be the base URL from which these documents are served (without trailing slash), e.g. <code>&quot;<a rel="nofollow" href="http://docs.python.org">http://docs.python.org</a>&quot;</code>. The default is <code>&#8221;</code>.</p>
<dt><code>html_file_suffix</code></p>
<dd> This is the file name suffix for generated HTML files. The default is <code>&quot;.html&quot;</code>. </p>
<p> New in version 0.4. </p>
<dt><code>html_link_suffix</code></p>
<dd> Suffix for generated links to HTML files. The default is whatever <code>html_file_suffix</code> is set to; it can be set differently (e.g. to support different web server setups). </p>
<p> New in version 0.6. </p>
<dt><code>html_translator_class</code></p>
<dd> A string with the fully-qualified name of a HTML Translator class, that is, a subclass of Sphinx&#8217; <code>HTMLTranslator</code>, that is used to translate document trees to HTML. Default is <code>None</code> (use the builtin translator).</p>
<dt><code>html_show_copyright</code></p>
<dd> If true, &quot;(C) Copyright &#8230;&quot; is shown in the HTML footer. Default is <code>True</code>. </p>
<p> New in version 1.0. </p>
<dt><code>html_show_sphinx</code></p>
<dd> If true, &quot;Created using Sphinx&quot; is shown in the HTML footer. Default is <code>True</code>. </p>
<p> New in version 0.4. </p>
<dt><code>html_output_encoding</code></p>
<dd> Encoding of HTML output files. Default is <code>&#8216;utf-8&#8217;</code>. Note that this encoding name must both be a valid Python encoding name and a valid HTML <code>charset</code> value. </p>
<p> New in version 1.0. </p>
<dt><code>html_compact_lists</code></p>
<dd> If true, list items containing only a single paragraph will not be rendered with a <code>&lt;p&gt;</code> element. This is standard docutils behavior. Default: <code>True</code>. </p>
<p> New in version 1.0. </p>
<dt><code>html_secnumber_suffix</code></p>
<dd> Suffix for section numbers. Default: <code>&quot;. &quot;</code>. Set to <code>&quot; &quot;</code> to suppress the final dot on section numbers. </p>
<p> New in version 1.0. </p>
<dt><code>html_search_language</code></p>
<dd> Language to be used for generating the HTML full-text search index. This defaults to the global language selected with <code>language</code>. If there is no support for this language, <code>&quot;en&quot;</code> is used which selects the English language. </p>
<p> Support is present for these languages:</p>
<dt>&bull;</p>
<dd> <code>en</code> &#8212; English</p>
<dt>&bull;</p>
<dd> <code>ja</code> &#8212; Japanese </p>
<p> New in version 1.1. </p>
<dt><code>html_search_options</code></p>
<dd> A dictionary with options for the search language support, empty by default. The meaning of these options depends on the language selected. </p>
<p> The English support has no options. </p>
<p> The Japanese support has these options:</p>
<dt>&bull;</p>
<dd> <code>type</code> &#8212; <code>&#8216;mecab&#8217;</code> or <code>&#8216;default&#8217;</code> (selects either MeCab or TinySegmenter word splitter algorithm)</p>
<dt>&bull;</p>
<dd> <code>dic_enc</code> &#8212; the encoding for the MeCab algorithm</p>
<dt>&bull;</p>
<dd> <code>dict</code> &#8212; the dictionary to use for the MeCab algorithm</p>
<dt>&bull;</p>
<dd> <code>lib</code> &#8212; the library name for finding the MeCab library via ctypes if the Python binding is not installed </p>
<p> New in version 1.1. </p>
<dt><code>html_search_scorer</code></p>
<dd> The name of a javascript file (relative to the configuration directory) that implements a search results scorer. If empty, the default will be used. </p>
<p> New in version 1.2. </p>
<dt><code>htmlhelp_basename</code></p>
<dd> Output file base name for HTML help builder. Default is <code>&#8216;pydoc&#8217;</code>.</dl>
<h3>Options for epub output</h3>
<p> These options influence the epub output. As this builder derives from the HTML builder, the HTML options also apply where appropriate. The actual values for some of the options is not really important, they just have to be entered into the <i>Dublin Core metadata</i>.</p>
<dl>
<dt><code>epub_basename</code></p>
<dd> The basename for the epub file. It defaults to the <code>project</code> name.</p>
<dt><code>epub_theme</code></p>
<dd> The HTML theme for the epub output. Since the default themes are not optimized for small screen space, using the same theme for HTML and epub output is usually not wise. This defaults to <code>&#8216;epub&#8217;</code>, a theme designed to save visual space.</p>
<dt><code>epub_theme_options</code></p>
<dd> A dictionary of options that influence the look and feel of the selected theme. These are theme-specific. For the options understood by the builtin themes, see <i>this section</i>. </p>
<p> New in version 1.2. </p>
<dt><code>epub_title</code></p>
<dd> The title of the document. It defaults to the <code>html_title</code> option but can be set independently for epub creation.</p>
<dt><code>epub_author</code></p>
<dd> The author of the document. This is put in the Dublin Core metadata. The default value is <code>&#8216;unknown&#8217;</code>.</p>
<dt><code>epub_language</code></p>
<dd> The language of the document. This is put in the Dublin Core metadata. The default is the <code>language</code> option or <code>&#8216;en&#8217;</code> if unset.</p>
<dt><code>epub_publisher</code></p>
<dd> The publisher of the document. This is put in the Dublin Core metadata. You may use any sensible string, e.g. the project homepage. The default value is <code>&#8216;unknown&#8217;</code>.</p>
<dt><code>epub_copyright</code></p>
<dd> The copyright of the document. It defaults to the <code>copyright</code> option but can be set independently for epub creation.</p>
<dt><code>epub_identifier</code></p>
<dd> An identifier for the document. This is put in the Dublin Core metadata. For published documents this is the ISBN number, but you can also use an alternative scheme, e.g. the project homepage. The default value is <code>&#8216;unknown&#8217;</code>.</p>
<dt><code>epub_scheme</code></p>
<dd> The publication scheme for the <code>epub_identifier</code>. This is put in the Dublin Core metadata. For published books the scheme is <code>&#8216;ISBN&#8217;</code>. If you use the project homepage, <code>&#8216;URL&#8217;</code> seems reasonable. The default value is <code>&#8216;unknown&#8217;</code>.</p>
<dt><code>epub_uid</code></p>
<dd> A unique identifier for the document. This is put in the Dublin Core metadata. You may use a random string. The default value is <code>&#8216;unknown&#8217;</code>.</p>
<dt><code>epub_cover</code></p>
<dd> The cover page information. This is a tuple containing the filenames of the cover image and the html template. The rendered html cover page is inserted as the first item in the spine in <code>content.opf</code>. If the template filename is empty, no html cover page is created. No cover at all is created if the tuple is empty. Examples: </p>
<pre>
epub_cover = ('_static/cover.png', 'epub-cover.html')
epub_cover = ('_static/cover.png', '')
epub_cover = ()
</pre>
<p> The default value is <code>()</code>. </p>
<p> New in version 1.1. </p>
<dt><code>epub_guide</code></p>
<dd> Meta data for the guide element of <code>content.opf</code>. This is a sequence of tuples containing the <i>type</i>, the <i>uri</i> and the <i>title</i> of the optional guide information. See the OPF documentation at <i><a rel="nofollow" href="http://idpf.org/epub">http://idpf.org/epub</a></i> for details. If possible, default entries for the <i>cover</i> and <i>toc</i> types are automatically inserted. However, the types can be explicitely overwritten if the default entries are not appropriate. Example: </p>
<pre>
epub_guide = (('cover', 'cover.html', u'Cover Page'),)
</pre>
<p> The default value is <code>()</code>.</p>
<dt><code>epub_pre_files</code></p>
<dd> Additional files that should be inserted before the text generated by Sphinx. It is a list of tuples containing the file name and the title. If the title is empty, no entry is added to <code>toc.ncx</code>. Example: </p>
<pre>
epub_pre_files = [
    ('index.html', 'Welcome'),
]
</pre>
<p> The default value is <code>[]</code>.</p>
<dt><code>epub_post_files</code></p>
<dd> Additional files that should be inserted after the text generated by Sphinx. It is a list of tuples containing the file name and the title. This option can be used to add an appendix. If the title is empty, no entry is added to <code>toc.ncx</code>. The default value is <code>[]</code>.</p>
<dt><code>epub_exclude_files</code></p>
<dd> A list of files that are generated/copied in the build directory but should not be included in the epub file. The default value is <code>[]</code>.</p>
<dt><code>epub_tocdepth</code></p>
<dd> The depth of the table of contents in the file <code>toc.ncx</code>. It should be an integer greater than zero. The default value is 3. Note: A deeply nested table of contents may be difficult to navigate.</p>
<dt><code>epub_tocdup</code></p>
<dd> This flag determines if a toc entry is inserted again at the beginning of it&#8217;s nested toc listing. This allows easier navitation to the top of a chapter, but can be confusing because it mixes entries of differnet depth in one list. The default value is <code>True</code>.</p>
<dt><code>epub_tocscope</code></p>
<dd> This setting control the scope of the epub table of contents. The setting can have the following values:</p>
<dt>&bull;</p>
<dd> <code>&#8216;default&#8217;</code> &#8212; include all toc entries that are not hidden (default)</p>
<dt>&bull;</p>
<dd> <code>&#8216;includehidden&#8217;</code> &#8212; include all toc entries </p>
<p> New in version 1.2. </p>
<dt><code>epub_fix_images</code></p>
<dd> This flag determines if sphinx should try to fix image formats that are not supported by some epub readers. At the moment palette images with a small color table are upgraded. You need the Python Image Library (PIL) installed to use this option. The default value is <code>False</code> because the automatic conversion may lose information. </p>
<p> New in version 1.2. </p>
<dt><code>epub_max_image_width</code></p>
<dd> This option specifies the maximum width of images. If it is set to a value greater than zero, images with a width larger than the given value are scaled accordingly. If it is zero, no scaling is performed. The default value is <code>0</code>. You need the Python Image Library (PIL) installed to use this option. </p>
<p> New in version 1.2. </p>
<dt><code>epub_show_urls</code></p>
<dd> Control whether to display URL addresses. This is very useful for readers that have no other means to display the linked URL. The settings can have the following values:</p>
<dt>&bull;</p>
<dd> <code>&#8216;inline&#8217;</code> &#8212; display URLs inline in parentheses (default)</p>
<dt>&bull;</p>
<dd> <code>&#8216;footnote&#8217;</code> &#8212; display URLs in footnotes</p>
<dt>&bull;</p>
<dd> <code>&#8216;no&#8217;</code> &#8212; do not display URLs </p>
<p> The display of inline URLs can be customized by adding CSS rules for the class <code>link-target</code>. </p>
<p> New in version 1.2. </p>
<dt><code>epub_use_index</code></p>
<dd> If true, add an index to the epub document. It defaults to the <code>html_use_index</code> option but can be set independently for epub creation. </p>
<p> New in version 1.2. </p>
</dl>
<h3>Options for LaTeX output</h3>
<p> These options influence LaTeX output.</p>
<dl>
<dt><code>latex_documents</code></p>
<dd> This value determines how to group the document tree into LaTeX source files. It must be a list of tuples <code>(startdocname, targetname, title, author, documentclass, toctree_only)</code>, where the items are:</p>
<dt>&bull;</p>
<dd> <i>startdocname</i>: document name that is the &quot;root&quot; of the LaTeX file. All documents referenced by it in TOC trees will be included in the LaTeX file too. (If you want only one LaTeX file, use your <code>master_doc</code> here.)</p>
<dt>&bull;</p>
<dd> <i>targetname</i>: file name of the LaTeX file in the output directory.</p>
<dt>&bull;</p>
<dd> <i>title</i>: LaTeX document title. Can be empty to use the title of the <i>startdoc</i>. This is inserted as LaTeX markup, so special characters like a backslash or ampersand must be represented by the proper LaTeX commands if they are to be inserted literally.</p>
<dt>&bull;</p>
<dd> <i>author</i>: Author for the LaTeX document. The same LaTeX markup caveat as for <i>title</i> applies. Use <code>nd</code> to separate multiple authors, as in: <code>&#8216;John nd Sarah&#8217;</code>.</p>
<dt>&bull;</p>
<dd> <i>documentclass</i>: Normally, one of <code>&#8216;manual&#8217;</code> or <code>&#8216;howto&#8217;</code> (provided by Sphinx). Other document classes can be given, but they must include the &quot;sphinx&quot; package in order to define Sphinx&#8217; custom LaTeX commands. &quot;howto&quot; documents will not get appendices. Also, howtos will have a simpler title page.</p>
<dt>&bull;</p>
<dd> <i>toctree_only</i>: Must be <code>True</code> or <code>False</code>. If <code>True</code>, the <i>startdoc</i> document itself is not included in the output, only the documents referenced by it via TOC trees. With this option, you can put extra stuff in the master document that shows up in the HTML, but not the LaTeX output. </p>
<p> New in version 1.2: In the past including your own document class required you to prepend the document class name with the string &quot;sphinx&quot;. This is not necessary anymore. </p>
<p> New in version 0.3: The 6th item <code>toctree_only</code>. Tuples with 5 items are still accepted. </p>
<dt><code>latex_logo</code></p>
<dd> If given, this must be the name of an image file (relative to the configuration directory) that is the logo of the docs. It is placed at the top of the title page. Default: <code>None</code>.</p>
<dt><code>latex_use_parts</code></p>
<dd> If true, the topmost sectioning unit is parts, else it is chapters. Default: <code>False</code>. </p>
<p> New in version 0.3. </p>
<dt><code>latex_appendices</code></p>
<dd> A list of document names to append as an appendix to all manuals.</p>
<dt><code>latex_domain_indices</code></p>
<dd> If true, generate domain-specific indices in addition to the general index. For e.g. the Python domain, this is the global module index. Default is <code>True</code>. </p>
<p> This value can be a bool or a list of index names that should be generated, like for <code>html_domain_indices</code>. </p>
<p> New in version 1.0. </p>
<dt><code>latex_use_modindex</code></p>
<dd> If true, add a module index to LaTeX documents. Default is <code>True</code>. </p>
<p> Deprecated since version 1.0: Use <code>latex_domain_indices</code>. </p>
<dt><code>latex_show_pagerefs</code></p>
<dd> If true, add page references after internal references. This is very useful for printed copies of the manual. Default is <code>False</code>. </p>
<p> New in version 1.0. </p>
<dt><code>latex_show_urls</code></p>
<dd> Control whether to display URL addresses. This is very useful for printed copies of the manual. The setting can have the following values:</p>
<dt>&bull;</p>
<dd> <code>&#8216;no&#8217;</code> &#8212; do not display URLs (default)</p>
<dt>&bull;</p>
<dd> <code>&#8216;footnote&#8217;</code> &#8212; display URLs in footnotes</p>
<dt>&bull;</p>
<dd> <code>&#8216;inline&#8217;</code> &#8212; display URLs inline in parentheses </p>
<p> New in version 1.0. </p>
<p> Changed in version 1.1: This value is now a string; previously it was a boolean value, and a true value selected the <code>&#8216;inline&#8217;</code> display. For backwards compatibility, <code>True</code> is still accepted. </p>
<dt><code>latex_elements</code></p>
<dd> New in version 0.5. </p>
<p> A dictionary that contains LaTeX snippets that override those Sphinx usually puts into the generated <code>.tex</code> files. </p>
<p> Keep in mind that backslashes must be doubled in Python string literals to avoid interpretation as escape sequences.</p>
<dt>&bull;</p>
<dd> Keys that you may want to override include:</p>
<dt><code>&#8216;papersize&#8217;</code></p>
<dd> Paper size option of the document class (<code>&#8216;a4paper&#8217;</code> or <code>&#8216;letterpaper&#8217;</code>), default <code>&#8216;letterpaper&#8217;</code>.</p>
<dt><code>&#8216;pointsize&#8217;</code></p>
<dd> Point size option of the document class (<code>&#8217;10pt&#8217;</code>, <code>&#8217;11pt&#8217;</code> or <code>&#8217;12pt&#8217;</code>), default <code>&#8217;10pt&#8217;</code>.</p>
<dt><code>&#8216;babel&#8217;</code></p>
<dd> &quot;babel&quot; package inclusion, default <code>&#8216;\usepackage{babel}&#8217;</code>.</p>
<dt><code>&#8216;fontpkg&#8217;</code></p>
<dd> Font package inclusion, default <code>&#8216;\usepackage{times}&#8217;</code> (which uses Times and Helvetica). You can set this to <code>&#8221;</code> to use the Computer Modern fonts. </p>
<p> Changed in version 1.2: Defaults to <code>&#8221;</code> when the <code>language</code> uses the Cyrillic script. </p>
<dt><code>&#8216;fncychap&#8217;</code></p>
<dd> Inclusion of the &quot;fncychap&quot; package (which makes fancy chapter titles), default <code>&#8216;\usepackage[Bjarne]{fncychap}&#8217;</code> for English documentation, <code>&#8216;\usepackage[Sonny]{fncychap}&#8217;</code> for internationalized docs (because the &quot;Bjarne&quot; style uses numbers spelled out in English). Other &quot;fncychap&quot; styles you can try include &quot;Lenny&quot;, &quot;Glenn&quot;, &quot;Conny&quot; and &quot;Rejne&quot;. You can also set this to <code>&#8221;</code> to disable fncychap.</p>
<dt><code>&#8216;preamble&#8217;</code></p>
<dd> Additional preamble content, default empty.</p>
<dt><code>&#8216;footer&#8217;</code></p>
<dd> Additional footer content (before the indices), default empty.</p>
<dt>&bull;</p>
<dd> Keys that don&#8217;t need be overridden unless in special cases are:</p>
<dt><code>&#8216;inputenc&#8217;</code></p>
<dd> &quot;inputenc&quot; package inclusion, default <code>&#8216;\usepackage[utf8]{inputenc}&#8217;</code>.</p>
<dt><code>&#8216;cmappkg&#8217;</code></p>
<dd> &quot;cmap&quot; package inclusion, default <code>&#8216;\usepackage{cmap}&#8217;</code>. </p>
<p> New in version 1.2. </p>
<dt><code>&#8216;fontenc&#8217;</code></p>
<dd> &quot;fontenc&quot; package inclusion, default <code>&#8216;\usepackage[T1]{fontenc}&#8217;</code>.</p>
<dt><code>&#8216;maketitle&#8217;</code></p>
<dd> &quot;maketitle&quot; call, default <code>&#8216;\maketitle&#8217;</code>. Override if you want to generate a differently-styled title page.</p>
<dt><code>&#8216;tableofcontents&#8217;</code></p>
<dd> &quot;tableofcontents&quot; call, default <code>&#8216;\tableofcontents&#8217;</code>. Override if you want to generate a different table of contents or put content between the title page and the TOC.</p>
<dt><code>&#8216;transition&#8217;</code></p>
<dd> Commands used to display transitions, default <code>&#8216;

\bigskip\hrule{}\bigskip

&#8217;</code>. Override if you want to display transitions differently. </p>
<p> New in version 1.2. </p>
<dt><code>&#8216;printindex&#8217;</code></p>
<dd> &quot;printindex&quot; call, the last thing in the file, default <code>&#8216;\printindex&#8217;</code>. Override if you want to generate the index differently or append some content after the index.</p>
<dt>&bull;</p>
<dd> Keys that are set by other options and therefore should not be overridden are: </p>
<p> <code>&#8216;docclass&#8217;</code> <code>&#8216;classoptions&#8217;</code> <code>&#8216;title&#8217;</code> <code>&#8216;date&#8217;</code> <code>&#8216;release&#8217;</code> <code>&#8216;author&#8217;</code> <code>&#8216;logo&#8217;</code> <code>&#8216;releasename&#8217;</code> <code>&#8216;makeindex&#8217;</code> <code>&#8216;shorthandoff&#8217;</code></p>
<dt><code>latex_docclass</code></p>
<dd> A dictionary mapping <code>&#8216;howto&#8217;</code> and <code>&#8216;manual&#8217;</code> to names of real document classes that will be used as the base for the two Sphinx classes. Default is to use <code>&#8216;article&#8217;</code> for <code>&#8216;howto&#8217;</code> and <code>&#8216;report&#8217;</code> for <code>&#8216;manual&#8217;</code>. </p>
<p> New in version 1.0. </p>
<dt><code>latex_additional_files</code></p>
<dd> A list of file names, relative to the configuration directory, to copy to the build directory when building LaTeX output. This is useful to copy files that Sphinx doesn&#8217;t copy automatically, e.g. if they are referenced in custom LaTeX added in <code>latex_elements</code>. Image files that are referenced in source files (e.g. via <code>.. image::</code>) are copied automatically. </p>
<p> You have to make sure yourself that the filenames don&#8217;t collide with those of any automatically copied files. </p>
<p> New in version 0.6. </p>
<p> Changed in version 1.2: This overrides the files which is provided from Sphinx such as sphinx.sty. </p>
<dt><code>latex_preamble</code></p>
<dd> Additional LaTeX markup for the preamble. </p>
<p> Deprecated since version 0.5: Use the <code>&#8216;preamble&#8217;</code> key in the <code>latex_elements</code> value. </p>
<dt><code>latex_paper_size</code></p>
<dd> The output paper size (<code>&#8216;letter&#8217;</code> or <code>&#8216;a4&#8217;</code>). Default is <code>&#8216;letter&#8217;</code>. </p>
<p> Deprecated since version 0.5: Use the <code>&#8216;papersize&#8217;</code> key in the <code>latex_elements</code> value. </p>
<dt><code>latex_font_size</code></p>
<dd> The font size (&#8217;10pt&#8217;, &#8217;11pt&#8217; or &#8217;12pt&#8217;). Default is <code>&#8217;10pt&#8217;</code>. </p>
<p> Deprecated since version 0.5: Use the <code>&#8216;pointsize&#8217;</code> key in the <code>latex_elements</code> value. </p>
</dl>
<h3>Options for text output</h3>
<p> These options influence text output.</p>
<dl>
<dt><code>text_newlines</code></p>
<dd> Determines which end-of-line character(s) are used in text output.</p>
<dt>&bull;</p>
<dd> <code>&#8216;unix&#8217;</code>: use Unix-style line endings (<code>
</code>)</p>
<dt>&bull;</p>
<dd> <code>&#8216;windows&#8217;</code>: use Windows-style line endings (<code>
</code>)</p>
<dt>&bull;</p>
<dd> <code>&#8216;native&#8217;</code>: use the line ending style of the platform the documentation is built on </p>
<p> Default: <code>&#8216;unix&#8217;</code>. </p>
<p> New in version 1.1. </p>
<dt><code>text_sectionchars</code></p>
<dd> A string of 7 characters that should be used for underlining sections. The first character is used for first-level headings, the second for second-level headings and so on. </p>
<p> The default is <code>&#8216;*=-~&quot;+`&#8217;</code>. </p>
<p> New in version 1.1. </p>
</dl>
<h3>Options for manual page output</h3>
<p> These options influence manual page output.</p>
<dl>
<dt><code>man_pages</code></p>
<dd> This value determines how to group the document tree into manual pages. It must be a list of tuples <code>(startdocname, name, description, authors, section)</code>, where the items are:</p>
<dt>&bull;</p>
<dd> <i>startdocname</i>: document name that is the &quot;root&quot; of the manual page. All documents referenced by it in TOC trees will be included in the manual file too. (If you want one master manual page, use your <code>master_doc</code> here.)</p>
<dt>&bull;</p>
<dd> <i>name</i>: name of the manual page. This should be a short string without spaces or special characters. It is used to determine the file name as well as the name of the manual page (in the NAME section).</p>
<dt>&bull;</p>
<dd> <i>description</i>: description of the manual page. This is used in the NAME section.</p>
<dt>&bull;</p>
<dd> <i>authors</i>: A list of strings with authors, or a single string. Can be an empty string or list if you do not want to automatically generate an AUTHORS section in the manual page.</p>
<dt>&bull;</p>
<dd> <i>section</i>: The manual page section. Used for the output file name as well as in the manual page header. </p>
<p> New in version 1.0. </p>
<dt><code>man_show_urls</code></p>
<dd> If true, add URL addresses after links. Default is <code>False</code>. </p>
<p> New in version 1.1. </p>
</dl>
<h3>Options for Texinfo output</h3>
<p> These options influence Texinfo output.</p>
<dl>
<dt><code>texinfo_documents</code></p>
<dd> This value determines how to group the document tree into Texinfo source files. It must be a list of tuples <code>(startdocname, targetname, title, author, dir_entry, description, category, toctree_only)</code>, where the items are:</p>
<dt>&bull;</p>
<dd> <i>startdocname</i>: document name that is the &quot;root&quot; of the Texinfo file. All documents referenced by it in TOC trees will be included in the Texinfo file too. (If you want only one Texinfo file, use your <code>master_doc</code> here.)</p>
<dt>&bull;</p>
<dd> <i>targetname</i>: file name (no extension) of the Texinfo file in the output directory.</p>
<dt>&bull;</p>
<dd> <i>title</i>: Texinfo document title. Can be empty to use the title of the <i>startdoc</i>. Inserted as Texinfo markup, so special characters like @ and {} will need to be escaped to be inserted literally.</p>
<dt>&bull;</p>
<dd> <i>author</i>: Author for the Texinfo document. Inserted as Texinfo markup. Use <code>@*</code> to separate multiple authors, as in: <code>&#8216;John@*Sarah&#8217;</code>.</p>
<dt>&bull;</p>
<dd> <i>dir_entry</i>: The name that will appear in the top-level <code>DIR</code> menu file.</p>
<dt>&bull;</p>
<dd> <i>description</i>: Descriptive text to appear in the top-level <code>DIR</code> menu file.</p>
<dt>&bull;</p>
<dd> <i>category</i>: Specifies the section which this entry will appear in the top-level <code>DIR</code> menu file.</p>
<dt>&bull;</p>
<dd> <i>toctree_only</i>: Must be <code>True</code> or <code>False</code>. If <code>True</code>, the <i>startdoc</i> document itself is not included in the output, only the documents referenced by it via TOC trees. With this option, you can put extra stuff in the master document that shows up in the HTML, but not the Texinfo output. </p>
<p> New in version 1.1. </p>
<dt><code>texinfo_appendices</code></p>
<dd> A list of document names to append as an appendix to all manuals. </p>
<p> New in version 1.1. </p>
<dt><code>texinfo_domain_indices</code></p>
<dd> If true, generate domain-specific indices in addition to the general index. For e.g. the Python domain, this is the global module index. Default is <code>True</code>. </p>
<p> This value can be a bool or a list of index names that should be generated, like for <code>html_domain_indices</code>. </p>
<p> New in version 1.1. </p>
<dt><code>texinfo_show_urls</code></p>
<dd> Control how to display URL addresses.</p>
<dt>&bull;</p>
<dd> <code>&#8216;footnote&#8217;</code> &#8212; display URLs in footnotes (default)</p>
<dt>&bull;</p>
<dd> <code>&#8216;no&#8217;</code> &#8212; do not display URLs</p>
<dt>&bull;</p>
<dd> <code>&#8216;inline&#8217;</code> &#8212; display URLs inline in parentheses </p>
<p> New in version 1.1. </p>
<dt><code>texinfo_no_detailmenu</code></p>
<dd> If true, do not generate a <code>@detailmenu</code> in the &quot;Top&quot; node&#8217;s menu containing entries for each sub-node in the document. Default is <code>False</code>. </p>
<p> New in version 1.2. </p>
<dt><code>texinfo_elements</code></p>
<dd> A dictionary that contains Texinfo snippets that override those Sphinx usually puts into the generated <code>.texi</code> files.</p>
<dt>&bull;</p>
<dd> Keys that you may want to override include:</p>
<dt><code>&#8216;paragraphindent&#8217;</code></p>
<dd> Number of spaces to indent the first line of each paragraph, default <code>2</code>. Specify <code>0</code> for no indentation.</p>
<dt><code>&#8216;exampleindent&#8217;</code></p>
<dd> Number of spaces to indent the lines for examples or literal blocks, default <code>4</code>. Specify <code>0</code> for no indentation.</p>
<dt><code>&#8216;preamble&#8217;</code></p>
<dd> Texinfo markup inserted near the beginning of the file.</p>
<dt><code>&#8216;copying&#8217;</code></p>
<dd> Texinfo markup inserted within the <code>@copying</code> block and displayed after the title. The default value consists of a simple title page identifying the project.</p>
<dt>&bull;</p>
<dd> Keys that are set by other options and therefore should not be overridden are: </p>
<p> <code>&#8216;author&#8217;</code> <code>&#8216;body&#8217;</code> <code>&#8216;date&#8217;</code> <code>&#8216;direntry&#8217;</code> <code>&#8216;filename&#8217;</code> <code>&#8216;project&#8217;</code> <code>&#8216;release&#8217;</code> <code>&#8216;title&#8217;</code> <code>&#8216;direntry&#8217;</code> </p>
<p> New in version 1.1. </p>
</dl>
<h3>Options for the linkcheck builder</h3>
<dl>
<dt><code>linkcheck_ignore</code></p>
<dd> A list of regular expressions that match URIs that should not be checked when doing a <code>linkcheck</code> build. Example: </p>
<pre>
linkcheck_ignore = [r'<a rel="nofollow" href="http://localhost:\d+/']">http://localhost:\d+/']</a>
</pre>
<p> New in version 1.1. </p>
<dt><code>linkcheck_timeout</code></p>
<dd> A timeout value, in seconds, for the linkcheck builder. <code>Only works in Python 2.6 and higher.</code> The default is to use Python&#8217;s global socket timeout. </p>
<p> New in version 1.1. </p>
<dt><code>linkcheck_workers</code></p>
<dd> The number of worker threads to use when checking links. Default is 5 threads. </p>
<p> New in version 1.1. </p>
<dt><code>linkcheck_anchors</code></p>
<dd> True or false, whether to check the validity of <code>#anchor</code>s in links. Since this requires downloading the whole document, it&#8217;s considerably slower when enabled. Default is <code>True</code>. </p>
<p> New in version 1.2. </p>
</dl>
<h3>Options for the XML builder</h3>
<dl>
<dt><code>xml_pretty</code></p>
<dd> If True, pretty-print the XML. Default is <code>True</code>. </p>
<p> New in version 1.2. </p>
</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> A note on available globbing syntax: you can use the standard shell constructs <code>*</code>, <code>?</code>, <code>[&#8230;]</code> and <code>[!&#8230;]</code> with the feature that these all don&#8217;t match slashes. A double star <code>**</code> can be used to match any sequence of characters <i>including</i> slashes.</dl>
<h2>INTERNATIONALIZATION</h2>
<p> New in version 1.1. </p>
<p> Complementary to translations provided for Sphinx-generated messages such as navigation bars, Sphinx provides mechanisms facilitating <i>document</i> translations in itself. See the <i>intl-options</i> for details on configuration. [image] Workflow visualization of translations in Sphinx. (The stick-figure is taken from an <i>XKCD comic</i>.).UNINDENT</p>
<dl>
<dt>&bull;</p>
<dd> <i>Sphinx internationalization details</i></p>
<dt>&bull;</p>
<dd> <i>Translating with sphinx-intl</i></p>
<dt>&bull;</p>
<dd> <i>Quick guide</i></p>
<dt>&bull;</p>
<dd> <i>Translating</i></p>
<dt>&bull;</p>
<dd> <i>Update your po files by new pot files</i></p>
<dt>&bull;</p>
<dd> <i>Using Transifex service for team translation</i></p>
<dt>&bull;</p>
<dd> <i>Contributing to Sphinx reference translation</i></dl>
<h3>Sphinx internationalization details</h3>
<p> <code>gettext</code> [1] is an established standard for internationalization and localization. It naively maps messages in a program to a translated string. Sphinx uses these facilities to translate whole documents. </p>
<p> Initially project maintainers have to collect all translatable strings (also referred to as <i>messages</i>) to make them known to translators. Sphinx extracts these through invocation of <code>sphinx-build -b gettext</code>. </p>
<p> Every single element in the doctree will end up in a single message which results in lists being equally split into different chunks while large paragraphs will remain as coarsely-grained as they were in the original document. This grants seamless document updates while still providing a little bit of context for translators in free-text passages. It is the maintainer&#8217;s task to split up paragraphs which are too large as there is no sane automated way to do that. </p>
<p> After Sphinx successfully ran the <code>MessageCatalogBuilder</code> you will find a collection of <code>.pot</code> files in your output directory. These are <code>catalog templates</code> and contain messages in your original language <i>only</i>. </p>
<p> They can be delivered to translators which will transform them to <code>.po</code> files &#8212; so called <code>message catalogs</code> &#8212; containing a mapping from the original messages to foreign-language strings. </p>
<p> Gettext compiles them into a binary format known as <code>binary catalogs</code> through <code>msgfmt</code> for efficiency reasons. If you make these files discoverable with <code>locale_dirs</code> for your <code>language</code>, Sphinx will pick them up automatically. </p>
<p> An example: you have a document <code>usage.rst</code> in your Sphinx project. The gettext builder will put its messages into <code>usage.pot</code>. Imagine you have Spanish translations [2] on your hands in <code>usage.po</code> &#8212; for your builds to be translated you need to follow these instructions:</p>
<dl>
<dt>&bull;</p>
<dd> Compile your message catalog to a locale directory, say <code>locale</code>, so it ends up in <code>./locale/es/LC_MESSAGES/usage.mo</code> in your source directory (where <code>es</code> is the language code for Spanish.) </p>
<pre>
msgfmt &quot;usage.po&quot; -o &quot;locale/es/LC_MESSAGES/usage.mo&quot;
</pre>
<dt>&bull;</p>
<dd> Set <code>locale_dirs</code> to <code>[&quot;locale/&quot;]</code>.</p>
<dt>&bull;</p>
<dd> Set <code>language</code> to <code>es</code> (also possible via <i>-D</i>).</p>
<dt>&bull;</p>
<dd> Run your desired build.</dl>
<h3>Translating with sphinx-intl</h3>
<h3>Quick guide</h3>
<p> <i>sphinx-intl</i> is a useful tool to work with Sphinx translation flow. This section describe a easy way to translate with sphinx-intl.</p>
<dl>
<dt>1.</p>
<dd> Install <i>sphinx-intl</i> by <code>pip install sphinx-intl</code> or <code>easy_install sphinx-intl</code>.</p>
<dt>2.</p>
<dd> Add configurations to your <i>conf.py</i>: </p>
<pre>
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
</pre>
<p> This case-study assumes that <code>locale_dirs</code> is set to &#8216;locale/&#8217; and <code>gettext_compact</code> is set to <i>False</i> (the Sphinx document is already configured as such).</p>
<dt>3.</p>
<dd> Extract document&#8217;s translatable messages into pot files: </p>
<pre>
$ make gettext
</pre>
<p> As a result, many pot files are generated under <code>_build/locale</code> directory.</p>
<dt>4.</p>
<dd> Setup/Update your <i>locale_dir</i>: </p>
<pre>
$ sphinx-intl update -p _build/locale -l de -l ja
</pre>
<p> Done. You got these directories that contain po files:</p>
<dt>&bull;</p>
<dd> <i>./locale/de/LC_MESSAGES/</i></p>
<dt>&bull;</p>
<dd> <i>./locale/ja/LC_MESSAGES/</i></p>
<dt>5.</p>
<dd> Translate your po files under <i>./locale/&lt;lang&gt;/LC_MESSAGES/</i>.</p>
<dt>6.</p>
<dd> Build mo files and make translated document. </p>
<p> You need a <code>language</code> parameter in <code>conf.py</code> or you may also specify the parameter on the command line: </p>
<pre>
$ sphinx-intl build
$ make -e SPHINXOPTS=&quot;-D language='de'&quot; html
</pre>
<p> Congratulations! You got the translated documentation in the <code>_build/html</code> directory.</dl>
<h3>Translating</h3>
<p> Translate po file under <code>./locale/de/LC_MESSAGES</code> directory. The case of builders.po file for sphinx document: </p>
<pre>
# a5600c3d2e3d48fc8c261ea0284db79b
#: ../../builders.rst:4
msgid &quot;Available builders&quot;
msgstr &quot;&lt;FILL HERE BY TARGET LANGUAGE&gt;&quot;
</pre>
<p> Another case, msgid is multi-line text and contains reStructuredText syntax: </p>
<pre>
# 302558364e1d41c69b3277277e34b184
#: ../../builders.rst:9
msgid &quot;&quot;
&quot;These are the built-in Sphinx builders. More builders can be added by &quot;
&quot;:ref:`extensions &lt;extensions&gt;`.&quot;
msgstr &quot;&quot;
&quot;FILL HERE BY TARGET LANGUAGE FILL HERE BY TARGET LANGUAGE FILL HERE &quot;
&quot;BY TARGET LANGUAGE :ref:`EXTENSIONS &lt;extensions&gt;` FILL HERE.&quot;
</pre>
<p> Please be careful not to break reST notation. Most po-editors will help you with that.</p>
<h3>Update your po files by new pot files</h3>
<p> If a document is updated, it is necessary to generate updated pot files and to apply differences to translated po files. In order to apply the updating difference of a pot file to po file, use the <code>sphinx-intl update</code> command. </p>
<pre>
$ sphinx-intl update -p _build/locale
</pre>
<h3>Using Transifex service for team translation</h3>
<p> <i>Transifex</i> is one of several services that allow collaborative translation via a web interface. It has a nifty Python-based command line client that makes it easy to fetch and push translations.</p>
<dl>
<dt>1.</p>
<dd> Install <i>transifex-client</i> </p>
<p> You need <code>tx</code> command to upload resources (pot files). </p>
<pre>
$ pip install transifex-client
</pre>
<p> <code>SEE ALSO:</code> <i>Transifex Client v0.8 &amp;mdash; Transifex documentation</i></p>
<dt>2.</p>
<dd> Create your <i>transifex</i> account and create new project for your document </p>
<p> Currently, transifex does not allow for a translation project to have more than one version of the document, so you&#8217;d better include a version number in your project name. </p>
<p> For example:</p>
<dt><code>Project ID</code></p>
<dd> <code>sphinx-document-test_1_0</code></p>
<dt><code>Project URL</code></p>
<dd> <i><a rel="nofollow" href="https://www.transifex.com/projects/p/sphinx-document-test_1_0/">https://www.transifex.com/projects/p/sphinx-document-test_1_0/</a></i></p>
<dt>3.</p>
<dd> Create config files for tx command </p>
<p> This process will create <code>.tx/config</code> in the current directory, as well as a <code>~/.transifexrc</code> file that includes auth information. </p>
<pre>
$ tx init --user=&lt;transifex-username&gt; --pass=&lt;transifex-password&gt;
Creating .tx folder...
Transifex instance [<a rel="nofollow" href="https://www.transifex.com]:">https://www.transifex.com]:</a>
...
Done.
</pre>
<dt>4.</p>
<dd> Upload pot files to transifex service </p>
<p> Register pot files to <code>.tx/config</code> file: </p>
<pre>
$ cd /your/document/root
$ sphinx-intl update-txconfig-resources --pot-dir _build/locale \
  --transifex-project-name sphinx-document-test_1_0
</pre>
<p> and upload pot files: </p>
<pre>
$ tx push -s
Pushing translations for resource sphinx-document-test_1_0.builders:
Pushing source file (locale/pot/builders.pot)
Resource does not exist.  Creating...
...
Done.
</pre>
<dt>5.</p>
<dd> Forward the translation on transifex</p>
<dt>6.</p>
<dd> Pull translated po files and make translated html </p>
<p> Get translated catalogs and build mo files (ex. for &#8216;de&#8217;): </p>
<pre>
$ cd /your/document/root
$ tx pull -l de
Pulling translations for resource sphinx-document-test_1_0.builders (...)
 -&gt; de: locale/de/LC_MESSAGES/builders.po
...
Done.
</pre>
<p> Build po files into mo and make html: </p>
<pre>
$ sphinx-intl build
$ make -e SPHINXOPTS=&quot;-D language='de'&quot; html
</pre>
<p> That&#8217;s all! </p>
<p> <code>TIP:</code> Translating locally and on Transifex </p>
<p> If you want to push all language&#8217;s po files, you can be done by using <code>tx push -t</code> command. Watch out! This operation overwrites translations in transifex. </p>
<p> In other words, if you have updated each in the service and local po files, it would take much time and effort to integrate them.</dl>
<h3>Contributing to Sphinx reference translation</h3>
<p> The recommended way for new contributors to translate Sphinx reference is to join the translation team on Transifex. </p>
<p> There is <i>sphinx translation page</i> for Sphinx-1.2 documentation.</p>
<dl>
<dt>1.</p>
<dd> Login to <i>transifex</i> service.</p>
<dt>2.</p>
<dd> Go to <i>sphinx translation page</i>.</p>
<dt>3.</p>
<dd> Click <code>Request language</code> and fill form.</p>
<dt>4.</p>
<dd> Wait acceptance by transifex sphinx translation maintainers.</p>
<dt>5.</p>
<dd> (after acceptance) translate on transifex.</dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</p>
<dd> See the <i>GNU gettext utilites</i> for details on that software suite.</p>
<dt>[2]</p>
<dd> Because nobody expects the Spanish Inquisition!</dl>
<h2>HTML THEMING SUPPORT</h2>
<p> New in version 0.6. </p>
<p> Sphinx supports changing the appearance of its HTML output via <i>themes</i>. A theme is a collection of HTML templates, stylesheet(s) and other static files. Additionally, it has a configuration file which specifies from which theme to inherit, which highlighting style to use, and what options exist for customizing the theme&#8217;s look and feel. </p>
<p> Themes are meant to be project-unaware, so they can be used for different projects without change.</p>
<h3>Using a theme</h3>
<p> Using an existing theme is easy. If the theme is builtin to Sphinx, you only need to set the <code>html_theme</code> config value. With the <code>html_theme_options</code> config value you can set theme-specific options that change the look and feel. For example, you could have the following in your <code>conf.py</code>: </p>
<pre>
html_theme = &quot;default&quot;
html_theme_options = {
    &quot;rightsidebar&quot;: &quot;true&quot;,
    &quot;relbarbgcolor&quot;: &quot;black&quot;
}
</pre>
<p> That would give you the default theme, but with a sidebar on the right side and a black background for the relation bar (the bar with the navigation links at the page&#8217;s top and bottom). </p>
<p> If the theme does not come with Sphinx, it can be in two static forms: either a directory (containing <code>theme.conf</code> and other needed files), or a zip file with the same contents. Either of them must be put where Sphinx can find it; for this there is the config value <code>html_theme_path</code>. It gives a list of directories, relative to the directory containing <code>conf.py</code>, that can contain theme directories or zip files. For example, if you have a theme in the file <code>blue.zip</code>, you can put it right in the directory containing <code>conf.py</code> and use this configuration: </p>
<pre>
html_theme = &quot;blue&quot;
html_theme_path = [&quot;.&quot;]
</pre>
<p> The third form provides your theme path dynamically to Sphinx if the <code>setuptools</code> package is installed. You can provide an entry point section called <code>sphinx_themes</code> in your setup.py file and write a <code>get_path</code> function that has to return the directory with themes in it: </p>
<pre>
// in your 'setup.py'
setup(
    ...
    entry_points = {
        'sphinx_themes': [
            'path = your_package:get_path',
        ]
    },
    ...
)
// in 'your_package.py'
from os import path
package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'themes')
def get_path():
    return template_path
</pre>
<p> New in version 1.2: &#8216;sphinx_themes&#8217; entry_points feature. </p>
<h3>Builtin themes</h3>
<p> <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Theme overview</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> [image: default] [image] </p>
<p> <i>default</i> </td>
<td> [image: sphinxdoc] [image] </p>
<p> <i>sphinxdoc</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> [image: scrolls] [image] </p>
<p> <i>scrolls</i> </td>
<td> [image: agogo] [image] </p>
<p> <i>agogo</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> [image: traditional] [image] </p>
<p> <i>traditional</i> </td>
<td> [image: nature] [image] </p>
<p> <i>nature</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> [image: haiku] [image] </p>
<p> <i>haiku</i> </td>
<td> [image: pyramid] [image] </p>
<p> <i>pyramid</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Sphinx comes with a selection of themes to choose from. </p>
<p> These themes are:</p>
<dl>
<dt>&bull;</p>
<dd> <code>basic</code> &#8212; This is a basically unstyled layout used as the base for the other themes, and usable as the base for custom themes as well. The HTML contains all important elements like sidebar and relation bar. There are these options (which are inherited by the other themes):</p>
<dt>&bull;</p>
<dd> <code>nosidebar</code> (true or false): Don&#8217;t include the sidebar. Defaults to false.</p>
<dt>&bull;</p>
<dd> <code>sidebarwidth</code> (an integer): Width of the sidebar in pixels. (Do not include <code>px</code> in the value.) Defaults to 230 pixels.</p>
<dt>&bull;</p>
<dd> <code>default</code> &#8212; This is the default theme, which looks like <i>the Python documentation</i>. It can be customized via these options:</p>
<dt>&bull;</p>
<dd> <code>rightsidebar</code> (true or false): Put the sidebar on the right side. Defaults to false.</p>
<dt>&bull;</p>
<dd> <code>stickysidebar</code> (true or false): Make the sidebar &quot;fixed&quot; so that it doesn&#8217;t scroll out of view for long body content. This may not work well with all browsers. Defaults to false.</p>
<dt>&bull;</p>
<dd> <code>collapsiblesidebar</code> (true or false): Add an <i>experimental</i> JavaScript snippet that makes the sidebar collapsible via a button on its side. <i>Doesn&#8217;t work with &quot;stickysidebar&quot;.</i> Defaults to false.</p>
<dt>&bull;</p>
<dd> <code>externalrefs</code> (true or false): Display external links differently from internal links. Defaults to false. </p>
<p> There are also various color and font options that can change the color scheme without having to write a custom stylesheet:</p>
<dt>&bull;</p>
<dd> <code>footerbgcolor</code> (CSS color): Background color for the footer line.</p>
<dt>&bull;</p>
<dd> <code>footertextcolor</code> (CSS color): Text color for the footer line.</p>
<dt>&bull;</p>
<dd> <code>sidebarbgcolor</code> (CSS color): Background color for the sidebar.</p>
<dt>&bull;</p>
<dd> <code>sidebarbtncolor</code> (CSS color): Background color for the sidebar collapse button (used when <i>collapsiblesidebar</i> is true).</p>
<dt>&bull;</p>
<dd> <code>sidebartextcolor</code> (CSS color): Text color for the sidebar.</p>
<dt>&bull;</p>
<dd> <code>sidebarlinkcolor</code> (CSS color): Link color for the sidebar.</p>
<dt>&bull;</p>
<dd> <code>relbarbgcolor</code> (CSS color): Background color for the relation bar.</p>
<dt>&bull;</p>
<dd> <code>relbartextcolor</code> (CSS color): Text color for the relation bar.</p>
<dt>&bull;</p>
<dd> <code>relbarlinkcolor</code> (CSS color): Link color for the relation bar.</p>
<dt>&bull;</p>
<dd> <code>bgcolor</code> (CSS color): Body background color.</p>
<dt>&bull;</p>
<dd> <code>textcolor</code> (CSS color): Body text color.</p>
<dt>&bull;</p>
<dd> <code>linkcolor</code> (CSS color): Body link color.</p>
<dt>&bull;</p>
<dd> <code>visitedlinkcolor</code> (CSS color): Body color for visited links.</p>
<dt>&bull;</p>
<dd> <code>headbgcolor</code> (CSS color): Background color for headings.</p>
<dt>&bull;</p>
<dd> <code>headtextcolor</code> (CSS color): Text color for headings.</p>
<dt>&bull;</p>
<dd> <code>headlinkcolor</code> (CSS color): Link color for headings.</p>
<dt>&bull;</p>
<dd> <code>codebgcolor</code> (CSS color): Background color for code blocks.</p>
<dt>&bull;</p>
<dd> <code>codetextcolor</code> (CSS color): Default text color for code blocks, if not set differently by the highlighting style.</p>
<dt>&bull;</p>
<dd> <code>bodyfont</code> (CSS font-family): Font for normal text.</p>
<dt>&bull;</p>
<dd> <code>headfont</code> (CSS font-family): Font for headings.</p>
<dt>&bull;</p>
<dd> <code>sphinxdoc</code> &#8212; The theme used for this documentation. It features a sidebar on the right side. There are currently no options beyond <i>nosidebar</i> and <i>sidebarwidth</i>.</p>
<dt>&bull;</p>
<dd> <code>scrolls</code> &#8212; A more lightweight theme, based on <i>the Jinja documentation</i>. The following color options are available:</p>
<dt>&bull;</p>
<dd> <code>headerbordercolor</code></p>
<dt>&bull;</p>
<dd> <code>subheadlinecolor</code></p>
<dt>&bull;</p>
<dd> <code>linkcolor</code></p>
<dt>&bull;</p>
<dd> <code>visitedlinkcolor</code></p>
<dt>&bull;</p>
<dd> <code>admonitioncolor</code></p>
<dt>&bull;</p>
<dd> <code>agogo</code> &#8212; A theme created by Andi Albrecht. The following options are supported:</p>
<dt>&bull;</p>
<dd> <code>bodyfont</code> (CSS font family): Font for normal text.</p>
<dt>&bull;</p>
<dd> <code>headerfont</code> (CSS font family): Font for headings.</p>
<dt>&bull;</p>
<dd> <code>pagewidth</code> (CSS length): Width of the page content, default 70em.</p>
<dt>&bull;</p>
<dd> <code>documentwidth</code> (CSS length): Width of the document (without sidebar), default 50em.</p>
<dt>&bull;</p>
<dd> <code>sidebarwidth</code> (CSS length): Width of the sidebar, default 20em.</p>
<dt>&bull;</p>
<dd> <code>bgcolor</code> (CSS color): Background color.</p>
<dt>&bull;</p>
<dd> <code>headerbg</code> (CSS value for &quot;background&quot;): background for the header area, default a grayish gradient.</p>
<dt>&bull;</p>
<dd> <code>footerbg</code> (CSS value for &quot;background&quot;): background for the footer area, default a light gray gradient.</p>
<dt>&bull;</p>
<dd> <code>linkcolor</code> (CSS color): Body link color.</p>
<dt>&bull;</p>
<dd> <code>headercolor1</code>, <code>headercolor2</code> (CSS color): colors for &lt;h1&gt; and &lt;h2&gt; headings.</p>
<dt>&bull;</p>
<dd> <code>headerlinkcolor</code> (CSS color): Color for the backreference link in headings.</p>
<dt>&bull;</p>
<dd> <code>textalign</code> (CSS <i>text-align</i> value): Text alignment for the body, default is <code>justify</code>.</p>
<dt>&bull;</p>
<dd> <code>nature</code> &#8212; A greenish theme. There are currently no options beyond <i>nosidebar</i> and <i>sidebarwidth</i>.</p>
<dt>&bull;</p>
<dd> <code>pyramid</code> &#8212; A theme from the Pyramid web framework project, designed by Blaise Laflamme. There are currently no options beyond <i>nosidebar</i> and <i>sidebarwidth</i>.</p>
<dt>&bull;</p>
<dd> <code>haiku</code> &#8212; A theme without sidebar inspired by the <i>Haiku OS user guide</i>. The following options are supported:</p>
<dt>&bull;</p>
<dd> <code>full_logo</code> (true or false, default false): If this is true, the header will only show the <code>html_logo</code>. Use this for large logos. If this is false, the logo (if present) will be shown floating right, and the documentation title will be put in the header.</p>
<dt>&bull;</p>
<dd> <code>textcolor</code>, <code>headingcolor</code>, <code>linkcolor</code>, <code>visitedlinkcolor</code>, <code>hoverlinkcolor</code> (CSS colors): Colors for various body elements.</p>
<dt>&bull;</p>
<dd> <code>traditional</code> &#8212; A theme resembling the old Python documentation. There are currently no options beyond <i>nosidebar</i> and <i>sidebarwidth</i>.</p>
<dt>&bull;</p>
<dd> <code>epub</code> &#8212; A theme for the epub builder. This theme tries to save visual space which is a sparse resource on ebook readers. The following options are supported:</p>
<dt>&bull;</p>
<dd> <code>relbar1</code> (true or false, default true): If this is true, the <i>relbar1</i> block is inserted in the epub output, otherwise it is omitted.</p>
<dt>&bull;</p>
<dd> <code>footer</code> (true or false, default true): If this is true, the <i>footer</i> block is inserted in the epub output, otherwise it is ommitted.</dl>
<h3>Creating themes</h3>
<p> As said, themes are either a directory or a zipfile (whose name is the theme name), containing the following:</p>
<dl>
<dt>&bull;</p>
<dd> A <code>theme.conf</code> file, see below.</p>
<dt>&bull;</p>
<dd> HTML templates, if needed.</p>
<dt>&bull;</p>
<dd> A <code>static/</code> directory containing any static files that will be copied to the output static directory on build. These can be images, styles, script files. </p>
<p> The <code>theme.conf</code> file is in INI format [1] (readable by the standard Python <code>ConfigParser</code> module) and has the following structure: </p>
<pre>
[theme]
inherit = base theme
stylesheet = main CSS name
pygments_style = stylename
[options]
variable = default value
</pre>
<dt>&bull;</p>
<dd> The <code>inherit</code> setting gives the name of a &quot;base theme&quot;, or <code>none</code>. The base theme will be used to locate missing templates (most themes will not have to supply most templates if they use <code>basic</code> as the base theme), its options will be inherited, and all of its static files will be used as well.</p>
<dt>&bull;</p>
<dd> The <code>stylesheet</code> setting gives the name of a CSS file which will be referenced in the HTML header. If you need more than one CSS file, either include one from the other via CSS&#8217; <code>@import</code>, or use a custom HTML template that adds <code>&lt;link rel=&quot;stylesheet&quot;&gt;</code> tags as necessary. Setting the <code>html_style</code> config value will override this setting.</p>
<dt>&bull;</p>
<dd> The <code>pygments_style</code> setting gives the name of a Pygments style to use for highlighting. This can be overridden by the user in the <code>pygments_style</code> config value.</p>
<dt>&bull;</p>
<dd> The <code>options</code> section contains pairs of variable names and default values. These options can be overridden by the user in <code>html_theme_options</code> and are accessible from all templates as <code>theme_&lt;name&gt;</code>.</dl>
<h3>Templating</h3>
<p> The <code>guide to templating</code> is helpful if you want to write your own templates. What is important to keep in mind is the order in which Sphinx searches for templates:</p>
<dl>
<dt>&bull;</p>
<dd> First, in the user&#8217;s <code>templates_path</code> directories.</p>
<dt>&bull;</p>
<dd> Then, in the selected theme.</p>
<dt>&bull;</p>
<dd> Then, in its base theme, its base&#8217;s base theme, etc. </p>
<p> When extending a template in the base theme with the same name, use the theme name as an explicit directory: <code>{% extends &quot;basic/layout.html&quot; %}</code>. From a user <code>templates_path</code> template, you can still use the &quot;exclamation mark&quot; syntax as described in the templating document.</dl>
<h3>Static templates</h3>
<p> Since theme options are meant for the user to configure a theme more easily, without having to write a custom stylesheet, it is necessary to be able to template static files as well as HTML files. Therefore, Sphinx supports so-called &quot;static templates&quot;, like this: </p>
<p> If the name of a file in the <code>static/</code> directory of a theme (or in the user&#8217;s static path, for that matter) ends with <code>_t</code>, it will be processed by the template engine. The <code>_t</code> will be left from the final file name. For example, the <i>default</i> theme has a file <code>static/default.css_t</code> which uses templating to put the color options into the stylesheet. When a documentation is built with the default theme, the output directory will contain a <code>_static/default.css</code> file where all template tags have been processed.</p>
<dl>
<dt>[1]</p>
<dd> It is not an executable Python file, as opposed to <code>conf.py</code>, because that would pose an unnecessary security risk if themes are shared.</dl>
<h2>TEMPLATING</h2>
<p> Sphinx uses the <i>Jinja</i> templating engine for its HTML templates. Jinja is a text-based engine, and inspired by Django templates, so anyone having used Django will already be familiar with it. It also has excellent documentation for those who need to make themselves familiar with it.</p>
<h3>Do I need to use Sphinx&#8217; templates to produce HTML?</h3>
<p> No. You have several other options:</p>
<dl>
<dt>&bull;</p>
<dd> You can write a <code>TemplateBridge</code> subclass that calls your template engine of choice, and set the <code>template_bridge</code> configuration value accordingly.</p>
<dt>&bull;</p>
<dd> You can <i>write a custom builder</i> that derives from <code>StandaloneHTMLBuilder</code> and calls your template engine of choice.</p>
<dt>&bull;</p>
<dd> You can use the <code>PickleHTMLBuilder</code> that produces pickle files with the page contents, and postprocess them using a custom tool, or use them in your Web application.</dl>
<h3>Jinja/Sphinx Templating Primer</h3>
<p> The default templating language in Sphinx is Jinja. It&#8217;s Django/Smarty inspired and easy to understand. The most important concept in Jinja is <i>template inheritance</i>, which means that you can overwrite only specific blocks within a template, customizing it while also keeping the changes at a minimum. </p>
<p> To customize the output of your documentation you can override all the templates (both the layout templates and the child templates) by adding files with the same name as the original filename into the template directory of the structure the Sphinx quickstart generated for you. </p>
<p> Sphinx will look for templates in the folders of <code>templates_path</code> first, and if it can&#8217;t find the template it&#8217;s looking for there, it falls back to the selected theme&#8217;s templates. </p>
<p> A template contains <code>variables</code>, which are replaced with values when the template is evaluated, <code>tags</code>, which control the logic of the template and <code>blocks</code> which are used for template inheritance. </p>
<p> Sphinx&#8217; <i>basic</i> theme provides base templates with a couple of blocks it will fill with data. These are located in the <code>themes/basic</code> subdirectory of the Sphinx installation directory, and used by all builtin Sphinx themes. Templates with the same name in the <code>templates_path</code> override templates supplied by the selected theme. </p>
<p> For example, to add a new link to the template area containing related links all you have to do is to add a new template called <code>layout.html</code> with the following contents: </p>
<pre>
{% extends &quot;!layout.html&quot; %}
{% block rootrellink %}
    &lt;li&gt;&lt;a href=&quot;<a rel="nofollow" href="http://project.invalid/">http://project.invalid/</a>&quot;&gt;Project Homepage&lt;/a&gt; &amp;raquo;&lt;/li&gt;
    &#123;&#123; super() }}
{% endblock %}
</pre>
<p> By prefixing the name of the overridden template with an exclamation mark, Sphinx will load the layout template from the underlying HTML theme. </p>
<p> <code>Important</code>: If you override a block, call <code>&#123;&#123; super() }}</code> somewhere to render the block&#8217;s content in the extended template &#8212; unless you don&#8217;t want that content to show up.</p>
<h3>Working with the builtin templates</h3>
<p> The builtin <code>basic</code> theme supplies the templates that all builtin Sphinx themes are based on. It has the following elements you can override or use:</p>
<h3>Blocks</h3>
<p> The following blocks exist in the <code>layout.html</code> template:</p>
<dl>
<dt><i>doctype</i></p>
<dd> The doctype of the output format. By default this is XHTML 1.0 Transitional as this is the closest to what Sphinx and Docutils generate and it&#8217;s a good idea not to change it unless you want to switch to HTML 5 or a different but compatible XHTML doctype.</p>
<dt><i>linktags</i></p>
<dd> This block adds a couple of <code>&lt;link&gt;</code> tags to the head section of the template.</p>
<dt><i>extrahead</i></p>
<dd> This block is empty by default and can be used to add extra contents into the <code>&lt;head&gt;</code> tag of the generated HTML file. This is the right place to add references to JavaScript or extra CSS files.</p>
<dt><i>relbar1</i> / <i>relbar2</i></p>
<dd> This block contains the <i>relation bar</i>, the list of related links (the parent documents on the left, and the links to index, modules etc. on the right). <i>relbar1</i> appears before the document, <i>relbar2</i> after the document. By default, both blocks are filled; to show the relbar only before the document, you would override <i>relbar2</i> like this: </p>
<pre>
{% block relbar2 %}{% endblock %}
</pre>
<dt><i>rootrellink</i> / <i>relbaritems</i></p>
<dd> Inside the relbar there are three sections: The <i>rootrellink</i>, the links from the documentation and the custom <i>relbaritems</i>. The <i>rootrellink</i> is a block that by default contains a list item pointing to the master document by default, the <i>relbaritems</i> is an empty block. If you override them to add extra links into the bar make sure that they are list items and end with the <code>reldelim1</code>.</p>
<dt><i>document</i></p>
<dd> The contents of the document itself. It contains the block &quot;body&quot; where the individual content is put by subtemplates like <code>page.html</code>.</p>
<dt><i>sidebar1</i> / <i>sidebar2</i></p>
<dd> A possible location for a sidebar. <i>sidebar1</i> appears before the document and is empty by default, <i>sidebar2</i> after the document and contains the default sidebar. If you want to swap the sidebar location override this and call the <i>sidebar</i> helper: </p>
<pre>
{% block sidebar1 %}&#123;&#123; sidebar() }}{% endblock %}
{% block sidebar2 %}{% endblock %}
</pre>
<p> (The <i>sidebar2</i> location for the sidebar is needed by the <code>sphinxdoc.css</code> stylesheet, for example.)</p>
<dt><i>sidebarlogo</i></p>
<dd> The logo location within the sidebar. Override this if you want to place some content at the top of the sidebar.</p>
<dt><i>footer</i></p>
<dd> The block for the footer div. If you want a custom footer or markup before or after it, override this one. </p>
<p> The following four blocks are <i>only</i> used for pages that do not have assigned a list of custom sidebars in the <code>html_sidebars</code> config value. Their use is deprecated in favor of separate sidebar templates, which can be included via <code>html_sidebars</code>.</p>
<dt><i>sidebartoc</i></p>
<dd> The table of contents within the sidebar. </p>
<p> Deprecated since version 1.0. </p>
<dt><i>sidebarrel</i></p>
<dd> The relation links (previous, next document) within the sidebar. </p>
<p> Deprecated since version 1.0. </p>
<dt><i>sidebarsourcelink</i></p>
<dd> The &quot;Show source&quot; link within the sidebar (normally only shown if this is enabled by <code>html_show_sourcelink</code>). </p>
<p> Deprecated since version 1.0. </p>
<dt><i>sidebarsearch</i></p>
<dd> The search box within the sidebar. Override this if you want to place some content at the bottom of the sidebar. </p>
<p> Deprecated since version 1.0. </p>
</dl>
<h3>Configuration Variables</h3>
<p> Inside templates you can set a couple of variables used by the layout template using the <code>{% set %}</code> tag:</p>
<dl>
<dt><code>reldelim1</code></p>
<dd> The delimiter for the items on the left side of the related bar. This defaults to <code>&#8216; &amp;raquo;&#8217;</code> Each item in the related bar ends with the value of this variable.</p>
<dt><code>reldelim2</code></p>
<dd> The delimiter for the items on the right side of the related bar. This defaults to <code>&#8216; |&#8217;</code>. Each item except of the last one in the related bar ends with the value of this variable. </p>
<p> Overriding works like this: </p>
<pre>
{% extends &quot;!layout.html&quot; %}
{% set reldelim1 = ' &amp;gt;' %}
</pre>
<dt><code>script_files</code></p>
<dd> Add additional script files here, like this: </p>
<pre>
{% set script_files = script_files + [&quot;_static/myscript.js&quot;] %}
</pre>
<dt><code>css_files</code></p>
<dd> Similar to <code>script_files</code>, for CSS files.</dl>
<h3>Helper Functions</h3>
<p> Sphinx provides various Jinja functions as helpers in the template. You can use them to generate links or output multiply used elements.</p>
<dl>
<dt><code>pathto(document)</code></p>
<dd> Return the path to a Sphinx document as a URL. Use this to refer to built documents.</p>
<dt><code>pathto(file, 1)</code></p>
<dd> Return the path to a <i>file</i> which is a filename relative to the root of the generated output. Use this to refer to static files.</p>
<dt><code>hasdoc(document)</code></p>
<dd> Check if a document with the name <i>document</i> exists.</p>
<dt><code>sidebar()</code></p>
<dd> Return the rendered sidebar.</p>
<dt><code>relbar()</code></p>
<dd> Return the rendered relation bar.</dl>
<h3>Global Variables</h3>
<p> These global variables are available in every template and are safe to use. There are more, but most of them are an implementation detail and might change in the future.</p>
<dl>
<dt><code>builder</code></p>
<dd> The name of the builder (e.g. <code>html</code> or <code>htmlhelp</code>).</p>
<dt><code>copyright</code></p>
<dd> The value of <code>copyright</code>.</p>
<dt><code>docstitle</code></p>
<dd> The title of the documentation (the value of <code>html_title</code>), except when the &quot;single-file&quot; builder is used, when it is set to <code>None</code>.</p>
<dt><code>embedded</code></p>
<dd> True if the built HTML is meant to be embedded in some viewing application that handles navigation, not the web browser, such as for HTML help or Qt help formats. In this case, the sidebar is not included.</p>
<dt><code>favicon</code></p>
<dd> The path to the HTML favicon in the static path, or <code>&#8221;</code>.</p>
<dt><code>file_suffix</code></p>
<dd> The value of the builder&#8217;s <code>out_suffix</code> attribute, i.e. the file name extension that the output files will get. For a standard HTML builder, this is usually <code>.html</code>.</p>
<dt><code>has_source</code></p>
<dd> True if the reST document sources are copied (if <code>html_copy_source</code> is true).</p>
<dt><code>last_updated</code></p>
<dd> The build date.</p>
<dt><code>logo</code></p>
<dd> The path to the HTML logo image in the static path, or <code>&#8221;</code>.</p>
<dt><code>master_doc</code></p>
<dd> The value of <code>master_doc</code>, for usage with <code>pathto()</code>.</p>
<dt><code>next</code></p>
<dd> The next document for the navigation. This variable is either false or has two attributes <i>link</i> and <i>title</i>. The title contains HTML markup. For example, to generate a link to the next page, you can use this snippet: </p>
<pre>
{% if next %}
&lt;a href=&quot;&#123;&#123; next.link|e }}&quot;&gt;&#123;&#123; next.title }}&lt;/a&gt;
{% endif %}
</pre>
<dt><code>pagename</code></p>
<dd> The &quot;page name&quot; of the current file, i.e. either the document name if the file is generated from a reST source, or the equivalent hierarchical name relative to the output directory (<code>[directory/]filename_without_extension</code>).</p>
<dt><code>parents</code></p>
<dd> A list of parent documents for navigation, structured like the <code>next</code> item.</p>
<dt><code>prev</code></p>
<dd> Like <code>next</code>, but for the previous page.</p>
<dt><code>project</code></p>
<dd> The value of <code>project</code>.</p>
<dt><code>release</code></p>
<dd> The value of <code>release</code>.</p>
<dt><code>rellinks</code></p>
<dd> A list of links to put at the left side of the relbar, next to &quot;next&quot; and &quot;prev&quot;. This usually contains links to the general index and other indices, such as the Python module index. If you add something yourself, it must be a tuple <code>(pagename, link title, accesskey, link text)</code>.</p>
<dt><code>shorttitle</code></p>
<dd> The value of <code>html_short_title</code>.</p>
<dt><code>show_source</code></p>
<dd> True if <code>html_show_sourcelink</code> is true.</p>
<dt><code>sphinx_version</code></p>
<dd> The version of Sphinx used to build.</p>
<dt><code>style</code></p>
<dd> The name of the main stylesheet, as given by the theme or <code>html_style</code>.</p>
<dt><code>title</code></p>
<dd> The title of the current document, as used in the <code>&lt;title&gt;</code> tag.</p>
<dt><code>use_opensearch</code></p>
<dd> The value of <code>html_use_opensearch</code>.</p>
<dt><code>version</code></p>
<dd> The value of <code>version</code>. </p>
<p> In addition to these values, there are also all <code>theme options</code> available (prefixed by <code>theme_</code>), as well as the values given by the user in <code>html_context</code>. </p>
<p> In documents that are created from source files (as opposed to automatically-generated files like the module index, or documents that already are in HTML form), these variables are also available:</p>
<dt><code>meta</code></p>
<dd> Document metadata (a dictionary), see <i>metadata</i>.</p>
<dt><code>sourcename</code></p>
<dd> The name of the copied source file for the current document. This is only nonempty if the <code>html_copy_source</code> value is true.</p>
<dt><code>toc</code></p>
<dd> The local table of contents for the current page, rendered as HTML bullet lists.</p>
<dt><code>toctree</code></p>
<dd> A callable yielding the global TOC tree containing the current page, rendered as HTML bullet lists. Optional keyword arguments:</p>
<dt>&bull;</p>
<dd> <code>collapse</code> (true by default): if true, all TOC entries that are not ancestors of the current page are collapsed</p>
<dt>&bull;</p>
<dd> <code>maxdepth</code> (defaults to the max depth selected in the toctree directive): the maximum depth of the tree; set it to <code>-1</code> to allow unlimited depth</p>
<dt>&bull;</p>
<dd> <code>titles_only</code> (false by default): if true, put only toplevel document titles in the tree</p>
<dt>&bull;</p>
<dd> <code>includehidden</code> (false by default): if true, the TOC tree will also contain hidden entries.</dl>
<h2>SPHINX EXTENSIONS</h2>
<p> Since many projects will need special features in their documentation, Sphinx allows to add &quot;extensions&quot; to the build process, each of which can modify almost any aspect of document processing. </p>
<p> This chapter describes the extensions bundled with Sphinx. For the API documentation on writing your own extension, see <i>dev-extensions</i>.</p>
<h3>Builtin Sphinx extensions</h3>
<p> These extensions are built in and can be activated by respective entries in the <code>extensions</code> configuration value:</p>
<h3><code>sphinx.ext.autodoc</code> &#8212; Include documentation from docstrings</h3>
<p> This extension can import the modules you are documenting, and pull in documentation from docstrings in a semi-automatic way. </p>
<p> <code>NOTE:</code> For Sphinx (actually, the Python interpreter that executes Sphinx) to find your module, it must be importable. That means that the module or the package must be in one of the directories on <code>sys.path</code> &#8212; adapt your <code>sys.path</code> in the configuration file accordingly. </p>
<p> <code>WARNING:</code> <code>autodoc</code> <code>imports</code> the modules to be documented. If any modules have side effects on import, these will be executed by <code>autodoc</code> when <code>sphinx-build</code> is run. </p>
<p> If you document scripts (as opposed to library modules), make sure their main routine is protected by a <code>if __name__ == &#8216;__main__&#8217;</code> condition. </p>
<p> For this to work, the docstrings must of course be written in correct reStructuredText. You can then use all of the usual Sphinx markup in the docstrings, and it will end up correctly in the documentation. Together with hand-written documentation, this technique eases the pain of having to maintain two locations for documentation, while at the same time avoiding auto-generated-looking pure API documentation. </p>
<p> <code>autodoc</code> provides several directives that are versions of the usual <code>py:module</code>, <code>py:class</code> and so forth. On parsing time, they import the corresponding module and extract the docstring of the given objects, inserting them into the page source under a suitable <code>py:module</code>, <code>py:class</code> etc. directive. </p>
<p> <code>NOTE:</code> Just as <code>py:class</code> respects the current <code>py:module</code>, <code>autoclass</code> will also do so. Likewise, <code>automethod</code> will respect the current <code>py:class</code>.</p>
<dl>
<dt><code>.. automodule::</code></p>
<dd>
<dt><code>.. autoclass::</code></p>
<dd>
<dt><code>.. autoexception::</code></p>
<dd> Document a module, class or exception. All three directives will by default only insert the docstring of the object itself: </p>
<pre>
.. autoclass:: Noodle
</pre>
<p> will produce source like this: </p>
<pre>
.. class:: Noodle
   Noodle's docstring.
</pre>
<p> The &quot;auto&quot; directives can also contain content of their own, it will be inserted into the resulting non-auto directive source after the docstring (but before any automatic member documentation). </p>
<p> Therefore, you can also mix automatic and non-automatic member documentation, like so: </p>
<pre>
.. autoclass:: Noodle
   :members: eat, slurp
   .. method:: boil(time=10)
      Boil the noodle *time* minutes.
</pre>
<p> <code>Options and advanced usage</code></p>
<dt>&bull;</p>
<dd> If you want to automatically document members, there&#8217;s a <code>members</code> option: </p>
<pre>
.. automodule:: noodle
   :members:
</pre>
<p> will document all module members (recursively), and </p>
<pre>
.. autoclass:: Noodle
   :members:
</pre>
<p> will document all non-private member functions and properties (that is, those whose name doesn&#8217;t start with <code>_</code>). </p>
<p> For modules, <code>__all__</code> will be respected when looking for members; the order of the members will also be the order in <code>__all__</code>. </p>
<p> You can also give an explicit list of members; only these will then be documented: </p>
<pre>
.. autoclass:: Noodle
   :members: eat, slurp
</pre>
<dt>&bull;</p>
<dd> If you want to make the <code>members</code> option (or other flag options described below) the default, see <code>autodoc_default_flags</code>.</p>
<dt>&bull;</p>
<dd> Members without docstrings will be left out, unless you give the <code>undoc-members</code> flag option: </p>
<pre>
.. automodule:: noodle
   :members:
   :undoc-members:
</pre>
<dt>&bull;</p>
<dd> &quot;Private&quot; members (that is, those named like <code>_private</code> or <code>__private</code>) will be included if the <code>private-members</code> flag option is given. </p>
<p> New in version 1.1. </p>
<dt>&bull;</p>
<dd> Python &quot;special&quot; members (that is, those named like <code>__special__</code>) will be included if the <code>special-members</code> flag option is given: </p>
<pre>
.. autoclass:: my.Class
   :members:
   :private-members:
   :special-members:
</pre>
<p> would document both &quot;private&quot; and &quot;special&quot; members of the class. </p>
<p> New in version 1.1. </p>
<p> Changed in version 1.2: The option can now take arguments, i.e. the special members to document. </p>
<dt>&bull;</p>
<dd> For classes and exceptions, members inherited from base classes will be left out when documenting all members, unless you give the <code>inherited-members</code> flag option, in addition to <code>members</code>: </p>
<pre>
.. autoclass:: Noodle
   :members:
   :inherited-members:
</pre>
<p> This can be combined with <code>undoc-members</code> to document <i>all</i> available members of the class or module. </p>
<p> Note: this will lead to markup errors if the inherited members come from a module whose docstrings are not reST formatted. </p>
<p> New in version 0.3. </p>
<dt>&bull;</p>
<dd> It&#8217;s possible to override the signature for explicitly documented callable objects (functions, methods, classes) with the regular syntax that will override the signature gained from introspection: </p>
<pre>
.. autoclass:: Noodle(type)
   .. automethod:: eat(persona)
</pre>
<p> This is useful if the signature from the method is hidden by a decorator. </p>
<p> New in version 0.4. </p>
<dt>&bull;</p>
<dd> The <code>automodule</code>, <code>autoclass</code> and <code>autoexception</code> directives also support a flag option called <code>show-inheritance</code>. When given, a list of base classes will be inserted just below the class signature (when used with <code>automodule</code>, this will be inserted for every class that is documented in the module). </p>
<p> New in version 0.4. </p>
<dt>&bull;</p>
<dd> All autodoc directives support the <code>noindex</code> flag option that has the same effect as for standard <code>py:function</code> etc. directives: no index entries are generated for the documented object (and all autodocumented members). </p>
<p> New in version 0.4. </p>
<dt>&bull;</p>
<dd> <code>automodule</code> also recognizes the <code>synopsis</code>, <code>platform</code> and <code>deprecated</code> options that the standard <code>py:module</code> directive supports. </p>
<p> New in version 0.5. </p>
<dt>&bull;</p>
<dd> <code>automodule</code> and <code>autoclass</code> also has an <code>member-order</code> option that can be used to override the global value of <code>autodoc_member_order</code> for one directive. </p>
<p> New in version 0.6. </p>
<dt>&bull;</p>
<dd> The directives supporting member documentation also have a <code>exclude-members</code> option that can be used to exclude single member names from documentation, if all members are to be documented. </p>
<p> New in version 0.6. </p>
<dt>&bull;</p>
<dd> In an <code>automodule</code> directive with the <code>members</code> option set, only module members whose <code>__module__</code> attribute is equal to the module name as given to <code>automodule</code> will be documented. This is to prevent documentation of imported classes or functions. Set the <code>imported-members</code> option if you want to prevent this behavior and document all available members. Note that attributes from imported modules will not be documented, because attribute documentation is discovered by parsing the source file of the current module. </p>
<p> New in version 1.2. </p>
<dt><code>.. autofunction::</code></p>
<dd>
<dt><code>.. autodata::</code></p>
<dd>
<dt><code>.. automethod::</code></p>
<dd>
<dt><code>.. autoattribute::</code></p>
<dd> These work exactly like <code>autoclass</code> etc., but do not offer the options used for automatic member documentation. </p>
<p> <code>autodata</code> and <code>autoattribute</code> support the <code>annotation</code> option. Without this option, the representation of the object will be shown in the documentation. When the option is given without arguments, only the name of the object will be printed: </p>
<pre>
.. autodata:: CD_DRIVE
   :annotation:
</pre>
<p> You can tell sphinx what should be printed after the name: </p>
<pre>
.. autodata:: CD_DRIVE
   :annotation: = your CD device name
</pre>
<p> For module data members and class attributes, documentation can either be put into a comment with special formatting (using a <code>#:</code> to start the comment instead of just <code>#</code>), or in a docstring <i>after</i> the definition. Comments need to be either on a line of their own <i>before</i> the definition, or immediately after the assignment <i>on the same line</i>. The latter form is restricted to one line only. </p>
<p> This means that in the following class definition, all attributes can be autodocumented: </p>
<pre>
class Foo:
    &quot;&quot;&quot;Docstring for class Foo.&quot;&quot;&quot;
    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1
    flox = 1.5   #: Doc comment for Foo.flox. One line only.
    baz = 2
    &quot;&quot;&quot;Docstring for class attribute Foo.baz.&quot;&quot;&quot;
    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3
        self.spam = 4
        &quot;&quot;&quot;Docstring for instance attribute spam.&quot;&quot;&quot;
</pre>
<p> Changed in version 0.6: <code>autodata</code> and <code>autoattribute</code> can now extract docstrings. </p>
<p> Changed in version 1.1: Comment docs are now allowed on the same line after an assignment. </p>
<p> Changed in version 1.2: <code>autodata</code> and <code>autoattribute</code> have an <code>annotation</code> option </p>
<p> <code>NOTE:</code> If you document decorated functions or methods, keep in mind that autodoc retrieves its docstrings by importing the module and inspecting the <code>__doc__</code> attribute of the given function or method. That means that if a decorator replaces the decorated function with another, it must copy the original <code>__doc__</code> to the new function. </p>
<p> From Python 2.5, <code>functools.wraps()</code> can be used to create well-behaved decorating functions. </p>
<p> There are also new config values that you can set:</p>
<dt><code>autoclass_content</code></p>
<dd> This value selects what content will be inserted into the main body of an <code>autoclass</code> directive. The possible values are:</p>
<dt><code>class</code></p>
<dd> Only the class&#8217; docstring is inserted. This is the default. You can still document <code>__init__</code> as a separate method using <code>automethod</code> or the <code>members</code> option to <code>autoclass</code>.</p>
<dt><code>both</code></p>
<dd> Both the class&#8217; and the <code>__init__</code> method&#8217;s docstring are concatenated and inserted.</p>
<dt><code>init</code></p>
<dd> Only the <code>__init__</code> method&#8217;s docstring is inserted. </p>
<p> New in version 0.3. </p>
<dt><code>autodoc_member_order</code></p>
<dd> This value selects if automatically documented members are sorted alphabetical (value <code>&#8216;alphabetical&#8217;</code>), by member type (value <code>&#8216;groupwise&#8217;</code>) or by source order (value <code>&#8216;bysource&#8217;</code>). The default is alphabetical. </p>
<p> Note that for source order, the module must be a Python module with the source code available. </p>
<p> New in version 0.6. </p>
<p> Changed in version 1.0: Support for <code>&#8216;bysource&#8217;</code>. </p>
<dt><code>autodoc_default_flags</code></p>
<dd> This value is a list of autodoc directive flags that should be automatically applied to all autodoc directives. The supported flags are <code>&#8216;members&#8217;</code>, <code>&#8216;undoc-members&#8217;</code>, <code>&#8216;private-members&#8217;</code>, <code>&#8216;special-members&#8217;</code>, <code>&#8216;inherited-members&#8217;</code> and <code>&#8216;show-inheritance&#8217;</code>. </p>
<p> If you set one of these flags in this config value, you can use a negated form, <code>&#8216;no-</code><i>flag</i>&#8216;, in an autodoc directive, to disable it once. For example, if <code>autodoc_default_flags</code> is set to <code>[&#8216;members&#8217;, &#8216;undoc-members&#8217;]</code>, and you write a directive like this: </p>
<pre>
.. automodule:: foo
   :no-undoc-members:
</pre>
<p> the directive will be interpreted as if only <code>:members:</code> was given. </p>
<p> New in version 1.0. </p>
<dt><code>autodoc_docstring_signature</code></p>
<dd> Functions imported from C modules cannot be introspected, and therefore the signature for such functions cannot be automatically determined. However, it is an often-used convention to put the signature into the first line of the function&#8217;s docstring. </p>
<p> If this boolean value is set to <code>True</code> (which is the default), autodoc will look at the first line of the docstring for functions and methods, and if it looks like a signature, use the line as the signature and remove it from the docstring content. </p>
<p> New in version 1.1. </p>
</dl>
<h3>Docstring preprocessing</h3>
<p> autodoc provides the following additional events:</p>
<dl>
<dt><code>autodoc-process-docstring(app, what, name, obj, options, lines)</code></p>
<dd> New in version 0.4. </p>
<p> Emitted when autodoc has read and processed a docstring. <i>lines</i> is a list of strings &#8212; the lines of the processed docstring &#8212; that the event handler can modify <code>in place</code> to change what Sphinx puts into the output.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>app</code> &#8212; the Sphinx application object</p>
<dt>&bull;</p>
<dd> <code>what</code> &#8212; the type of the object which the docstring belongs to (one of <code>&quot;module&quot;</code>, <code>&quot;class&quot;</code>, <code>&quot;exception&quot;</code>, <code>&quot;function&quot;</code>, <code>&quot;method&quot;</code>, <code>&quot;attribute&quot;</code>)</p>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the fully qualified name of the object</p>
<dt>&bull;</p>
<dd> <code>obj</code> &#8212; the object itself</p>
<dt>&bull;</p>
<dd> <code>options</code> &#8212; the options given to the directive: an object with attributes <code>inherited_members</code>, <code>undoc_members</code>, <code>show_inheritance</code> and <code>noindex</code> that are true if the flag option of same name was given to the auto directive</p>
<dt>&bull;</p>
<dd> <code>lines</code> &#8212; the lines of the docstring, see above</p>
<dt><code>autodoc-process-signature(app, what, name, obj, options, signature, return_annotation)</code></p>
<dd> New in version 0.5. </p>
<p> Emitted when autodoc has formatted a signature for an object. The event handler can return a new tuple <code>(signature, return_annotation)</code> to change what Sphinx puts into the output.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>app</code> &#8212; the Sphinx application object</p>
<dt>&bull;</p>
<dd> <code>what</code> &#8212; the type of the object which the docstring belongs to (one of <code>&quot;module&quot;</code>, <code>&quot;class&quot;</code>, <code>&quot;exception&quot;</code>, <code>&quot;function&quot;</code>, <code>&quot;method&quot;</code>, <code>&quot;attribute&quot;</code>)</p>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the fully qualified name of the object</p>
<dt>&bull;</p>
<dd> <code>obj</code> &#8212; the object itself</p>
<dt>&bull;</p>
<dd> <code>options</code> &#8212; the options given to the directive: an object with attributes <code>inherited_members</code>, <code>undoc_members</code>, <code>show_inheritance</code> and <code>noindex</code> that are true if the flag option of same name was given to the auto directive</p>
<dt>&bull;</p>
<dd> <code>signature</code> &#8212; function signature, as a string of the form <code>&quot;(parameter_1, parameter_2)&quot;</code>, or <code>None</code> if introspection didn&#8217;t succeed and signature wasn&#8217;t specified in the directive.</p>
<dt>&bull;</p>
<dd> <code>return_annotation</code> &#8212; function return annotation as a string of the form <code>&quot; -&gt; annotation&quot;</code>, or <code>None</code> if there is no return annotation </p>
<p> The <code>sphinx.ext.autodoc</code> module provides factory functions for commonly needed docstring processing in event <code>autodoc-process-docstring</code>:</p>
<dt><code>sphinx.ext.autodoc.cut_lines(pre, post=0, what=None)</code></p>
<dd> Return a listener that removes the first <i>pre</i> and last <i>post</i> lines of every docstring. If <i>what</i> is a sequence of strings, only docstrings of a type in <i>what</i> will be processed. </p>
<p> Use like this (e.g. in the <code>setup()</code> function of <code>conf.py</code>): </p>
<pre>
from sphinx.ext.autodoc import cut_lines
app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
</pre>
<p> This can (and should) be used in place of <code>automodule_skip_lines</code>.</p>
<dt><code>sphinx.ext.autodoc.between(marker, what=None, keepempty=False, exclude=False)</code></p>
<dd> Return a listener that either keeps, or if <i>exclude</i> is True excludes, lines between lines that match the <i>marker</i> regular expression. If no line matches, the resulting docstring would be empty, so no change will be made unless <i>keepempty</i> is true. </p>
<p> If <i>what</i> is a sequence of strings, only docstrings of a type in <i>what</i> will be processed.</dl>
<h3>Skipping members</h3>
<p> autodoc allows the user to define a custom method for determining whether a member should be included in the documentation by using the following event:</p>
<dl>
<dt><code>autodoc-skip-member(app, what, name, obj, skip, options)</code></p>
<dd> New in version 0.5. </p>
<p> Emitted when autodoc has to decide whether a member should be included in the documentation. The member is excluded if a handler returns <code>True</code>. It is included if the handler returns <code>False</code>.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>app</code> &#8212; the Sphinx application object</p>
<dt>&bull;</p>
<dd> <code>what</code> &#8212; the type of the object which the docstring belongs to (one of <code>&quot;module&quot;</code>, <code>&quot;class&quot;</code>, <code>&quot;exception&quot;</code>, <code>&quot;function&quot;</code>, <code>&quot;method&quot;</code>, <code>&quot;attribute&quot;</code>)</p>
<dt>&bull;</p>
<dd> <code>name</code> &#8212; the fully qualified name of the object</p>
<dt>&bull;</p>
<dd> <code>obj</code> &#8212; the object itself</p>
<dt>&bull;</p>
<dd> <code>skip</code> &#8212; a boolean indicating if autodoc will skip this member if the user handler does not override the decision</p>
<dt>&bull;</p>
<dd> <code>options</code> &#8212; the options given to the directive: an object with attributes <code>inherited_members</code>, <code>undoc_members</code>, <code>show_inheritance</code> and <code>noindex</code> that are true if the flag option of same name was given to the auto directive</dl>
<h3><code>sphinx.ext.autosummary</code> &#8212; Generate autodoc summaries</h3>
<p> New in version 0.6. </p>
<p> This extension generates function/method/attribute summary lists, similar to those output e.g. by Epydoc and other API doc generation tools. This is especially useful when your docstrings are long and detailed, and putting each one of them on a separate page makes them easier to read. </p>
<p> The <code>sphinx.ext.autosummary</code> extension does this in two parts:</p>
<dl>
<dt>1.</p>
<dd> There is an <code>autosummary</code> directive for generating summary listings that contain links to the documented items, and short summary blurbs extracted from their docstrings.</p>
<dt>2.</p>
<dd> Optionally, the convenience script <code>sphinx-autogen</code> or the new <code>autosummary_generate</code> config value can be used to generate short &quot;stub&quot; files for the entries listed in the <code>autosummary</code> directives. These files by default contain only the corresponding <code>sphinx.ext.autodoc</code> directive, but can be customized with templates.</p>
<dt><code>.. autosummary::</code></p>
<dd> Insert a table that contains links to documented items, and a short summary blurb (the first sentence of the docstring) for each of them. </p>
<p> The <code>autosummary</code> directive can also optionally serve as a <code>toctree</code> entry for the included items. Optionally, stub <code>.rst</code> files for these items can also be automatically generated. </p>
<p> For example, </p>
<pre>
.. currentmodule:: sphinx
.. autosummary::
   environment.BuildEnvironment
   util.relative_uri
</pre>
<p> produces a table like this: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>environment.BuildEnvironment</code>(srcdir, &#8230;) </td>
<td> The environment in which the ReST files are translated.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>util.relative_uri</code>(base, to) </td>
<td> Return a relative URL from <code>base</code> to <code>to</code>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Autosummary preprocesses the docstrings and signatures with the same <code>autodoc-process-docstring</code> and <code>autodoc-process-signature</code> hooks as <code>autodoc</code>. </p>
<p> <code>Options</code></p>
<dt>&bull;</p>
<dd> If you want the <code>autosummary</code> table to also serve as a <code>toctree</code> entry, use the <code>toctree</code> option, for example: </p>
<pre>
.. autosummary::
   :toctree: DIRNAME
   sphinx.environment.BuildEnvironment
   sphinx.util.relative_uri
</pre>
<p> The <code>toctree</code> option also signals to the <code>sphinx-autogen</code> script that stub pages should be generated for the entries listed in this directive. The option accepts a directory name as an argument; <code>sphinx-autogen</code> will by default place its output in this directory. If no argument is given, output is placed in the same directory as the file that contains the directive.</p>
<dt>&bull;</p>
<dd> If you don&#8217;t want the <code>autosummary</code> to show function signatures in the listing, include the <code>nosignatures</code> option: </p>
<pre>
.. autosummary::
   :nosignatures:
   sphinx.environment.BuildEnvironment
   sphinx.util.relative_uri
</pre>
<dt>&bull;</p>
<dd> You can specify a custom template with the <code>template</code> option. For example, </p>
<pre>
.. autosummary::
   :template: mytemplate.rst
   sphinx.environment.BuildEnvironment
</pre>
<p> would use the template <code>mytemplate.rst</code> in your <code>templates_path</code> to generate the pages for all entries listed. See <i>Customizing templates</i> below. </p>
<p> New in version 1.0. </p>
</dl>
<h3><code>sphinx-autogen</code> &#8212; generate autodoc stub pages</h3>
<p> The <code>sphinx-autogen</code> script can be used to conveniently generate stub documentation pages for items included in <code>autosummary</code> listings. </p>
<p> For example, the command </p>
<pre>
$ sphinx-autogen -o generated *.rst
</pre>
<p> will read all <code>autosummary</code> tables in the <code>*.rst</code> files that have the <code>:toctree:</code> option set, and output corresponding stub pages in directory <code>generated</code> for all documented items. The generated pages by default contain text of the form: </p>
<pre>
sphinx.util.relative_uri
========================
.. autofunction:: sphinx.util.relative_uri
</pre>
<p> If the <code>-o</code> option is not given, the script will place the output files in the directories specified in the <code>:toctree:</code> options.</p>
<h3>Generating stub pages automatically</h3>
<p> If you do not want to create stub pages with <code>sphinx-autogen</code>, you can also use this new config value:</p>
<dl>
<dt><code>autosummary_generate</code></p>
<dd> Boolean indicating whether to scan all found documents for autosummary directives, and to generate stub pages for each. </p>
<p> Can also be a list of documents for which stub pages should be generated. </p>
<p> The new files will be placed in the directories specified in the <code>:toctree:</code> options of the directives.</dl>
<h3>Customizing templates</h3>
<p> New in version 1.0. </p>
<p> You can customize the stub page templates, in a similar way as the HTML Jinja templates, see <i>templating</i>. (<code>TemplateBridge</code> is not supported.) </p>
<p> <code>NOTE:</code> If you find yourself spending much time tailoring the stub templates, this may indicate that it&#8217;s a better idea to write custom narrative documentation instead. </p>
<p> Autosummary uses the following template files:</p>
<dl>
<dt>&bull;</p>
<dd> <code>autosummary/base.rst</code> &#8212; fallback template</p>
<dt>&bull;</p>
<dd> <code>autosummary/module.rst</code> &#8212; template for modules</p>
<dt>&bull;</p>
<dd> <code>autosummary/class.rst</code> &#8212; template for classes</p>
<dt>&bull;</p>
<dd> <code>autosummary/function.rst</code> &#8212; template for functions</p>
<dt>&bull;</p>
<dd> <code>autosummary/attribute.rst</code> &#8212; template for class attributes</p>
<dt>&bull;</p>
<dd> <code>autosummary/method.rst</code> &#8212; template for class methods </p>
<p> The following variables available in the templates:</p>
<dt><code>name</code></p>
<dd> Name of the documented object, excluding the module and class parts.</p>
<dt><code>objname</code></p>
<dd> Name of the documented object, excluding the module parts.</p>
<dt><code>fullname</code></p>
<dd> Full name of the documented object, including module and class parts.</p>
<dt><code>module</code></p>
<dd> Name of the module the documented object belongs to.</p>
<dt><code>class</code></p>
<dd> Name of the class the documented object belongs to. Only available for methods and attributes.</p>
<dt><code>underline</code></p>
<dd> A string containing <code>len(full_name) * &#8216;=&#8217;</code>.</p>
<dt><code>members</code></p>
<dd> List containing names of all members of the module or class. Only available for modules and classes.</p>
<dt><code>functions</code></p>
<dd> List containing names of &quot;public&quot; functions in the module. Here, &quot;public&quot; here means that the name does not start with an underscore. Only available for modules.</p>
<dt><code>classes</code></p>
<dd> List containing names of &quot;public&quot; classes in the module. Only available for modules.</p>
<dt><code>exceptions</code></p>
<dd> List containing names of &quot;public&quot; exceptions in the module. Only available for modules.</p>
<dt><code>methods</code></p>
<dd> List containing names of &quot;public&quot; methods in the class. Only available for classes.</p>
<dt><code>attributes</code></p>
<dd> List containing names of &quot;public&quot; attributes in the class. Only available for classes. </p>
<p> <code>NOTE:</code> You can use the <code>autosummary</code> directive in the stub pages. Stub pages are generated also based on these directives.</dl>
<h3><code>sphinx.ext.doctest</code> &#8212; Test snippets in the documentation</h3>
<p> This extension allows you to test snippets in the documentation in a natural way. It works by collecting specially-marked up code blocks and running them as doctest tests. </p>
<p> Within one document, test code is partitioned in <i>groups</i>, where each group consists of:</p>
<dl>
<dt>&bull;</p>
<dd> zero or more <i>setup code</i> blocks (e.g. importing the module to test)</p>
<dt>&bull;</p>
<dd> one or more <i>test</i> blocks </p>
<p> When building the docs with the <code>doctest</code> builder, groups are collected for each document and run one after the other, first executing setup code blocks, then the test blocks in the order they appear in the file. </p>
<p> There are two kinds of test blocks:</p>
<dt>&bull;</p>
<dd> <i>doctest-style</i> blocks mimic interactive sessions by interleaving Python code (including the interpreter prompt) and output.</p>
<dt>&bull;</p>
<dd> <i>code-output-style</i> blocks consist of an ordinary piece of Python code, and optionally, a piece of output for that code. </p>
<p> The doctest extension provides four directives. The <i>group</i> argument is interpreted as follows: if it is empty, the block is assigned to the group named <code>default</code>. If it is <code>*</code>, the block is assigned to all groups (including the <code>default</code> group). Otherwise, it must be a comma-separated list of group names.</p>
<dt><code>.. testsetup:: [group]</code></p>
<dd> A setup code block. This code is not shown in the output for other builders, but executed before the doctests of the group(s) it belongs to.</p>
<dt><code>.. testcleanup:: [group]</code></p>
<dd> A cleanup code block. This code is not shown in the output for other builders, but executed after the doctests of the group(s) it belongs to. </p>
<p> New in version 1.1. </p>
<dt><code>.. doctest:: [group]</code></p>
<dd> A doctest-style code block. You can use standard <code>doctest</code> flags for controlling how actual output is compared with what you give as output. By default, these options are enabled: <code>ELLIPSIS</code> (allowing you to put ellipses in the expected output that match anything in the actual output), <code>IGNORE_EXCEPTION_DETAIL</code> (not comparing tracebacks), <code>DONT_ACCEPT_TRUE_FOR_1</code> (by default, doctest accepts &quot;True&quot; in the output where &quot;1&quot; is given &#8212; this is a relic of pre-Python 2.2 times). </p>
<p> This directive supports two options:</p>
<dt>&bull;</p>
<dd> <code>hide</code>, a flag option, hides the doctest block in other builders. By default it is shown as a highlighted doctest block.</p>
<dt>&bull;</p>
<dd> <code>options</code>, a string option, can be used to give a comma-separated list of doctest flags that apply to each example in the tests. (You still can give explicit flags per example, with doctest comments, but they will show up in other builders too.) </p>
<p> Note that like with standard doctests, you have to use <code>&lt;BLANKLINE&gt;</code> to signal a blank line in the expected output. The <code>&lt;BLANKLINE&gt;</code> is removed when building presentation output (HTML, LaTeX etc.). </p>
<p> Also, you can give inline doctest options, like in doctest: </p>
<pre>
&gt;&gt;&gt; datetime.date.now()   # doctest: +SKIP
datetime.date(2008, 1, 1)
</pre>
<p> They will be respected when the test is run, but stripped from presentation output.</p>
<dt><code>.. testcode:: [group]</code></p>
<dd> A code block for a code-output-style test. </p>
<p> This directive supports one option:</p>
<dt>&bull;</p>
<dd> <code>hide</code>, a flag option, hides the code block in other builders. By default it is shown as a highlighted code block. </p>
<p> <code>NOTE:</code> Code in a <code>testcode</code> block is always executed all at once, no matter how many statements it contains. Therefore, output will <i>not</i> be generated for bare expressions &#8212; use <code>print</code>. Example: </p>
<pre>
.. testcode::
   1+1        # this will give no output!
   print 2+2  # this will give output
.. testoutput::
   4
</pre>
<p> Also, please be aware that since the doctest module does not support mixing regular output and an exception message in the same snippet, this applies to testcode/testoutput as well.</p>
<dt><code>.. testoutput:: [group]</code></p>
<dd> The corresponding output, or the exception message, for the last <code>testcode</code> block. </p>
<p> This directive supports two options:</p>
<dt>&bull;</p>
<dd> <code>hide</code>, a flag option, hides the output block in other builders. By default it is shown as a literal block without highlighting.</p>
<dt>&bull;</p>
<dd> <code>options</code>, a string option, can be used to give doctest flags (comma-separated) just like in normal doctest blocks. </p>
<p> Example: </p>
<pre>
.. testcode::
   print 'Output     text.'
.. testoutput::
   :hide:
   :options: -ELLIPSIS, +NORMALIZE_WHITESPACE
   Output text.
</pre>
<p> The following is an example for the usage of the directives. The test via <code>doctest</code> and the test via <code>testcode</code> and <code>testoutput</code> are equivalent. </p>
<pre>
The parrot module
=================
.. testsetup:: *
   import parrot
The parrot module is a module about parrots.
Doctest example:
.. doctest::
   &gt;&gt;&gt; parrot.voom(3000)
   This parrot wouldn't voom if you put 3000 volts through it!
Test-Output example:
.. testcode::
   parrot.voom(3000)
This would output:
.. testoutput::
   This parrot wouldn't voom if you put 3000 volts through it!
</pre>
<p> There are also these config values for customizing the doctest extension:</p>
<dt><code>doctest_path</code></p>
<dd> A list of directories that will be added to <code>sys.path</code> when the doctest builder is used. (Make sure it contains absolute paths.)</p>
<dt><code>doctest_global_setup</code></p>
<dd> Python code that is treated like it were put in a <code>testsetup</code> directive for <i>every</i> file that is tested, and for every group. You can use this to e.g. import modules you will always need in your doctests. </p>
<p> New in version 0.6. </p>
<dt><code>doctest_global_cleanup</code></p>
<dd> Python code that is treated like it were put in a <code>testcleanup</code> directive for <i>every</i> file that is tested, and for every group. You can use this to e.g. remove any temporary files that the tests leave behind. </p>
<p> New in version 1.1. </p>
<dt><code>doctest_test_doctest_blocks</code></p>
<dd> If this is a nonempty string (the default is <code>&#8216;default&#8217;</code>), standard reST doctest blocks will be tested too. They will be assigned to the group name given. </p>
<p> reST doctest blocks are simply doctests put into a paragraph of their own, like so: </p>
<pre>
Some documentation text.
&gt;&gt;&gt; print 1
1
Some more documentation text.
</pre>
<p> (Note that no special <code>::</code> is used to introduce a doctest block; docutils recognizes them from the leading <code>&gt;&gt;&gt;</code>. Also, no additional indentation is used, though it doesn&#8217;t hurt.) </p>
<p> If this value is left at its default value, the above snippet is interpreted by the doctest builder exactly like the following: </p>
<pre>
Some documentation text.
.. doctest::
   &gt;&gt;&gt; print 1
   1
Some more documentation text.
</pre>
<p> This feature makes it easy for you to test doctests in docstrings included with the <code>autodoc</code> extension without marking them up with a special directive. </p>
<p> Note though that you can&#8217;t have blank lines in reST doctest blocks. They will be interpreted as one block ending and another one starting. Also, removal of <code>&lt;BLANKLINE&gt;</code> and <code># doctest:</code> options only works in <code>doctest</code> blocks, though you may set <code>trim_doctest_flags</code> to achieve that in all code blocks with Python console content.</dl>
<h3><code>sphinx.ext.intersphinx</code> &#8212; Link to other projects&#8217; documentation</h3>
<p> New in version 0.5. </p>
<p> This extension can generate automatic links to the documentation of objects in other projects. </p>
<p> Usage is simple: whenever Sphinx encounters a cross-reference that has no matching target in the current documentation set, it looks for targets in the documentation sets configured in <code>intersphinx_mapping</code>. A reference like <code>:py:class:`zipfile.ZipFile`</code> can then link to the Python documentation for the ZipFile class, without you having to specify where it is located exactly. </p>
<p> When using the &quot;new&quot; format (see below), you can even force lookup in a foreign set by prefixing the link target appropriately. A link like <code>:ref:`comparison manual &lt;python:comparisons&gt;`</code> will then link to the label &quot;comparisons&quot; in the doc set &quot;python&quot;, if it exists. </p>
<p> Behind the scenes, this works as follows:</p>
<dl>
<dt>&bull;</p>
<dd> Each Sphinx HTML build creates a file named <code>objects.inv</code> that contains a mapping from object names to URIs relative to the HTML set&#8217;s root.</p>
<dt>&bull;</p>
<dd> Projects using the Intersphinx extension can specify the location of such mapping files in the <code>intersphinx_mapping</code> config value. The mapping will then be used to resolve otherwise missing references to objects into links to the other documentation.</p>
<dt>&bull;</p>
<dd> By default, the mapping file is assumed to be at the same location as the rest of the documentation; however, the location of the mapping file can also be specified individually, e.g. if the docs should be buildable without Internet access. </p>
<p> To use intersphinx linking, add <code>&#8216;sphinx.ext.intersphinx&#8217;</code> to your <code>extensions</code> config value, and use these new config values to activate linking:</p>
<dt><code>intersphinx_mapping</code></p>
<dd> This config value contains the locations and names of other projects that should be linked to in this documentation. </p>
<p> Relative local paths for target locations are taken as relative to the base of the built documentation, while relative local paths for inventory locations are taken as relative to the source directory. </p>
<p> When fetching remote inventory files, proxy settings will be read from the <code>$HTTP_PROXY</code> environment variable. </p>
<p> <code>Old format for this config value</code> </p>
<p> This is the format used before Sphinx 1.0. It is still recognized. </p>
<p> A dictionary mapping URIs to either <code>None</code> or an URI. The keys are the base URI of the foreign Sphinx documentation sets and can be local paths or HTTP URIs. The values indicate where the inventory file can be found: they can be <code>None</code> (at the same location as the base URI) or another local or HTTP URI. </p>
<p> <code>New format for this config value</code> </p>
<p> New in version 1.0. </p>
<p> A dictionary mapping unique identifiers to a tuple <code>(target, inventory)</code>. Each <code>target</code> is the base URI of a foreign Sphinx documentation set and can be a local path or an HTTP URI. The <code>inventory</code> indicates where the inventory file can be found: it can be <code>None</code> (at the same location as the base URI) or another local or HTTP URI. </p>
<p> The unique identifier can be used to prefix cross-reference targets, so that it is clear which intersphinx set the target belongs to. A link like <code>:ref:`comparison manual &lt;python:comparisons&gt;`</code> will link to the label &quot;comparisons&quot; in the doc set &quot;python&quot;, if it exists. </p>
<p> <code>Example</code> </p>
<p> To add links to modules and objects in the Python standard library documentation, use: </p>
<pre>
intersphinx_mapping = {'python': ('<a rel="nofollow" href="http://docs.python.org/3.2',">http://docs.python.org/3.2',</a> None)}
</pre>
<p> This will download the corresponding <code>objects.inv</code> file from the Internet and generate links to the pages under the given URI. The downloaded inventory is cached in the Sphinx environment, so it must be redownloaded whenever you do a full rebuild. </p>
<p> A second example, showing the meaning of a non-<code>None</code> value of the second tuple item: </p>
<pre>
intersphinx_mapping = {'python': ('<a rel="nofollow" href="http://docs.python.org/3.2',">http://docs.python.org/3.2',</a>
                                  'python-inv.txt')}
</pre>
<p> This will read the inventory from <code>python-inv.txt</code> in the source directory, but still generate links to the pages under <code><a rel="nofollow" href="http://docs.python.org/3.2">http://docs.python.org/3.2</a></code>. It is up to you to update the inventory file as new objects are added to the Python documentation.</p>
<dt><code>intersphinx_cache_limit</code></p>
<dd> The maximum number of days to cache remote inventories. The default is <code>5</code>, meaning five days. Set this to a negative value to cache inventories for unlimited time.</dl>
<h3>Math support in Sphinx</h3>
<p> New in version 0.5. </p>
<p> Since mathematical notation isn&#8217;t natively supported by HTML in any way, Sphinx supports math in documentation with several extensions. </p>
<p> The basic math support is contained in <code>sphinx.ext.mathbase</code>. Other math support extensions should, if possible, reuse that support too. </p>
<p> <code>NOTE:</code> <code>mathbase</code> is not meant to be added to the <code>extensions</code> config value, instead, use either <code>sphinx.ext.pngmath</code> or <code>sphinx.ext.mathjax</code> as described below. </p>
<p> The input language for mathematics is LaTeX markup. This is the de-facto standard for plain-text math notation and has the added advantage that no further translation is necessary when building LaTeX output. </p>
<p> Keep in mind that when you put math markup in <code>Python docstrings</code> read by <code>autodoc</code>, you either have to double all backslashes, or use Python raw strings (<code>r&quot;raw&quot;</code>). </p>
<p> <code>mathbase</code> defines these new markup elements:</p>
<dl>
<dt><code>:math:</code></p>
<dd> Role for inline math. Use like this: </p>
<pre>
Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.
</pre>
<dt><code>.. math::</code></p>
<dd> Directive for displayed math (math that takes the whole line for itself). </p>
<p> The directive supports multiple equations, which should be separated by a blank line: </p>
<pre>
.. math::
   (a + b)^2 = a^2 + 2ab + b^2
   (a - b)^2 = a^2 - 2ab + b^2
</pre>
<p> In addition, each single equation is set within a <code>split</code> environment, which means that you can have multiple aligned lines in an equation, aligned at <code>&amp;</code> and separated by <code>\</code>: </p>
<pre>
.. math::
   (a + b)^2  &amp;=  (a + b)(a + b) \
              &amp;=  a^2 + 2ab + b^2
</pre>
<p> For more details, look into the documentation of the <i>AmSMath LaTeX package</i>. </p>
<p> When the math is only one line of text, it can also be given as a directive argument: </p>
<pre>
.. math:: (a + b)^2 = a^2 + 2ab + b^2
</pre>
<p> Normally, equations are not numbered. If you want your equation to get a number, use the <code>label</code> option. When given, it selects an internal label for the equation, by which it can be cross-referenced, and causes an equation number to be issued. See <code>eqref</code> for an example. The numbering style depends on the output format. </p>
<p> There is also an option <code>nowrap</code> that prevents any wrapping of the given math in a math environment. When you give this option, you must make sure yourself that the math is properly set up. For example: </p>
<pre>
.. math::
   :nowrap:
   egin{eqnarray}
      y    &amp; = &amp; ax^2 + bx + c \
      f(x) &amp; = &amp; x^2 + 2xy + y^2
   nd{eqnarray}
</pre>
<dt><code>:eq:</code></p>
<dd> Role for cross-referencing equations via their label. This currently works only within the same document. Example: </p>
<pre>
.. math:: e^{i\pi} + 1 = 0
   :label: euler
Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.
</pre>
</dl>
<h3><code>sphinx.ext.pngmath</code> &#8212; Render math as PNG images</h3>
<p> This extension renders math via LaTeX and <i>dvipng</i> into PNG images. This of course means that the computer where the docs are built must have both programs available. </p>
<p> There are various config values you can set to influence how the images are built:</p>
<dl>
<dt><code>pngmath_latex</code></p>
<dd> The command name with which to invoke LaTeX. The default is <code>&#8216;latex&#8217;</code>; you may need to set this to a full path if <code>latex</code> is not in the executable search path. </p>
<p> Since this setting is not portable from system to system, it is normally not useful to set it in <code>conf.py</code>; rather, giving it on the <code>sphinx-build</code> command line via the <i>-D</i> option should be preferable, like this: </p>
<pre>
sphinx-build -b html -D pngmath_latex=C:	ex\latex.exe . _build/html
</pre>
<p> Changed in version 0.5.1: This value should only contain the path to the latex executable, not further arguments; use <code>pngmath_latex_args</code> for that purpose. </p>
<dt><code>pngmath_dvipng</code></p>
<dd> The command name with which to invoke <code>dvipng</code>. The default is <code>&#8216;dvipng&#8217;</code>; you may need to set this to a full path if <code>dvipng</code> is not in the executable search path.</p>
<dt><code>pngmath_latex_args</code></p>
<dd> Additional arguments to give to latex, as a list. The default is an empty list. </p>
<p> New in version 0.5.1. </p>
<dt><code>pngmath_latex_preamble</code></p>
<dd> Additional LaTeX code to put into the preamble of the short LaTeX files that are used to translate the math snippets. This is empty by default. Use it e.g. to add more packages whose commands you want to use in the math.</p>
<dt><code>pngmath_dvipng_args</code></p>
<dd> Additional arguments to give to dvipng, as a list. The default value is <code>[&#8216;-gamma&#8217;, &#8216;1.5&#8217;, &#8216;-D&#8217;, &#8216;110&#8217;, &#8216;-bg&#8217;, &#8216;Transparent&#8217;]</code> which makes the image a bit darker and larger then it is by default, and produces PNGs with a transparent background. </p>
<p> Changed in version 1.2: Now includes <code>-bg Transparent</code> by default. </p>
<dt><code>pngmath_use_preview</code></p>
<dd> <code>dvipng</code> has the ability to determine the &quot;depth&quot; of the rendered text: for example, when typesetting a fraction inline, the baseline of surrounding text should not be flush with the bottom of the image, rather the image should extend a bit below the baseline. This is what TeX calls &quot;depth&quot;. When this is enabled, the images put into the HTML document will get a <code>vertical-align</code> style that correctly aligns the baselines. </p>
<p> Unfortunately, this only works when the <i>preview-latex package</i> is installed. Therefore, the default for this option is <code>False</code>.</p>
<dt><code>pngmath_add_tooltips</code></p>
<dd> Default: true. If false, do not add the LaTeX code as an &quot;alt&quot; attribute for math images. </p>
<p> New in version 1.1. </p>
</dl>
<h3><code>sphinx.ext.mathjax</code> &#8212; Render math via JavaScript</h3>
<p> New in version 1.1. </p>
<p> This extension puts math as-is into the HTML files. The JavaScript package <i>MathJax</i> is then loaded and transforms the LaTeX markup to readable math live in the browser. </p>
<p> Because MathJax (and the necessary fonts) is very large, it is not included in Sphinx.</p>
<dl>
<dt><code>mathjax_path</code></p>
<dd> The path to the JavaScript file to include in the HTML files in order to load MathJax. </p>
<p> The default is the <code>http://</code> URL that loads the JS files from the <i>MathJax CDN</i>. If you want MathJax to be available offline, you have to donwload it and set this value to a different path. </p>
<p> The path can be absolute or relative; if it is relative, it is relative to the <code>_static</code> directory of the built docs. </p>
<p> For example, if you put MathJax into the static path of the Sphinx docs, this value would be <code>MathJax/MathJax.js</code>. If you host more than one Sphinx documentation set on one server, it is advisable to install MathJax in a shared location. </p>
<p> You can also give a full <code>http://</code> URL different from the CDN URL.</dl>
<h3><code>sphinx.ext.jsmath</code> &#8212; Render math via JavaScript</h3>
<p> This extension works just as the MathJax extension does, but uses the older package <i>jsMath</i>. It provides this config value:</p>
<dl>
<dt><code>jsmath_path</code></p>
<dd> The path to the JavaScript file to include in the HTML files in order to load JSMath. There is no default. </p>
<p> The path can be absolute or relative; if it is relative, it is relative to the <code>_static</code> directory of the built docs. </p>
<p> For example, if you put JSMath into the static path of the Sphinx docs, this value would be <code>jsMath/easy/load.js</code>. If you host more than one Sphinx documentation set on one server, it is advisable to install jsMath in a shared location.</dl>
<h3><code>sphinx.ext.graphviz</code> &#8212; Add Graphviz graphs</h3>
<p> New in version 0.6. </p>
<p> This extension allows you to embed <i>Graphviz</i> graphs in your documents. </p>
<p> It adds these directives:</p>
<dl>
<dt><code>.. graphviz::</code></p>
<dd> Directive to embed graphviz code. The input code for <code>dot</code> is given as the content. For example: </p>
<pre>
.. graphviz::
   digraph foo {
      &quot;bar&quot; -&gt; &quot;baz&quot;;
   }
</pre>
<p> In HTML output, the code will be rendered to a PNG or SVG image (see <code>graphviz_output_format</code>). In LaTeX output, the code will be rendered to an embeddable PDF file. </p>
<p> You can also embed external dot files, by giving the file name as an argument to <code>graphviz</code> and no additional content: </p>
<pre>
.. graphviz:: external.dot
</pre>
<p> As for all file references in Sphinx, if the filename is absolute, it is taken as relative to the source directory. </p>
<p> Changed in version 1.1: Added support for external files. </p>
<dt><code>.. graph::</code></p>
<dd> Directive for embedding a single undirected graph. The name is given as a directive argument, the contents of the graph are the directive content. This is a convenience directive to generate <code>graph &lt;name&gt; { &lt;content&gt; }</code>. </p>
<p> For example: </p>
<pre>
.. graph:: foo
   &quot;bar&quot; -- &quot;baz&quot;;
</pre>
<dt><code>.. digraph::</code></p>
<dd> Directive for embedding a single directed graph. The name is given as a directive argument, the contents of the graph are the directive content. This is a convenience directive to generate <code>digraph &lt;name&gt; { &lt;content&gt; }</code>. </p>
<p> For example: </p>
<pre>
.. digraph:: foo
   &quot;bar&quot; -&gt; &quot;baz&quot; -&gt; &quot;quux&quot;;
</pre>
<p> New in version 1.0: All three directives support an <code>alt</code> option that determines the image&#8217;s alternate text for HTML output. If not given, the alternate text defaults to the graphviz code. </p>
<p> New in version 1.1: All three directives support an <code>inline</code> flag that controls paragraph breaks in the output. When set, the graph is inserted into the current paragraph. If the flag is not given, paragraph breaks are introduced before and after the image (the default). </p>
<p> New in version 1.1: All three directives support a <code>caption</code> option that can be used to give a caption to the diagram. Naturally, diagrams marked as &quot;inline&quot; cannot have a caption. </p>
<p> There are also these new config values:</p>
<dt><code>graphviz_dot</code></p>
<dd> The command name with which to invoke <code>dot</code>. The default is <code>&#8216;dot&#8217;</code>; you may need to set this to a full path if <code>dot</code> is not in the executable search path. </p>
<p> Since this setting is not portable from system to system, it is normally not useful to set it in <code>conf.py</code>; rather, giving it on the <code>sphinx-build</code> command line via the <i>-D</i> option should be preferable, like this: </p>
<pre>
sphinx-build -b html -D graphviz_dot=C:\graphvizin\dot.exe . _build/html
</pre>
<dt><code>graphviz_dot_args</code></p>
<dd> Additional command-line arguments to give to dot, as a list. The default is an empty list. This is the right place to set global graph, node or edge attributes via dot&#8217;s <code>-G</code>, <code>-N</code> and <code>-E</code> options.</p>
<dt><code>graphviz_output_format</code></p>
<dd> The output format for Graphviz when building HTML files. This must be either <code>&#8216;png&#8217;</code> or <code>&#8216;svg&#8217;</code>; the default is <code>&#8216;png&#8217;</code>. </p>
<p> New in version 1.0: Previously, output always was PNG. </p>
</dl>
<h3><code>sphinx.ext.inheritance_diagram</code> &#8212; Include inheritance diagrams</h3>
<p> New in version 0.6. </p>
<p> This extension allows you to include inheritance diagrams, rendered via the <code>Graphviz extension</code>. </p>
<p> It adds this directive:</p>
<dl>
<dt><code>.. inheritance-diagram::</code></p>
<dd> This directive has one or more arguments, each giving a module or class name. Class names can be unqualified; in that case they are taken to exist in the currently described module (see <code>py:module</code>). </p>
<p> For each given class, and each class in each given module, the base classes are determined. Then, from all classes and their base classes, a graph is generated which is then rendered via the graphviz extension to a directed graph. </p>
<p> This directive supports an option called <code>parts</code> that, if given, must be an integer, advising the directive to remove that many parts of module names from the displayed names. (For example, if all your class names start with <code>lib.</code>, you can give <code>:parts: 1</code> to remove that prefix from the displayed node names.) </p>
<p> It also supports a <code>private-bases</code> flag option; if given, private base classes (those whose name starts with <code>_</code>) will be included. </p>
<p> Changed in version 1.1: Added <code>private-bases</code> option; previously, all bases were always included. </p>
<p> New config values are:</p>
<dt><code>inheritance_graph_attrs</code></p>
<dd> A dictionary of graphviz graph attributes for inheritance diagrams. </p>
<p> For example: </p>
<pre>
inheritance_graph_attrs = dict(rankdir=&quot;LR&quot;, size='&quot;6.0, 8.0&quot;',
                               fontsize=14, ratio='compress')
</pre>
<dt><code>inheritance_node_attrs</code></p>
<dd> A dictionary of graphviz node attributes for inheritance diagrams. </p>
<p> For example: </p>
<pre>
inheritance_node_attrs = dict(shape='ellipse', fontsize=14, height=0.75,
                              color='dodgerblue1', style='filled')
</pre>
<dt><code>inheritance_edge_attrs</code></p>
<dd> A dictionary of graphviz edge attributes for inheritance diagrams.</dl>
<h3><code>sphinx.ext.ifconfig</code> &#8212; Include content based on configuration</h3>
<p> This extension is quite simple, and features only one directive:</p>
<dl>
<dt><code>.. ifconfig::</code></p>
<dd> Include content of the directive only if the Python expression given as an argument is <code>True</code>, evaluated in the namespace of the project&#8217;s configuration (that is, all registered variables from <code>conf.py</code> are available). </p>
<p> For example, one could write </p>
<pre>
.. ifconfig:: releaselevel in ('alpha', 'beta', 'rc')
   This stuff is only included in the built docs for unstable versions.
</pre>
<p> To make a custom config value known to Sphinx, use <code>add_config_value()</code> in the setup function in <code>conf.py</code>, e.g.: </p>
<pre>
def setup(app):
    app.add_config_value('releaselevel', '', True)
</pre>
<p> The second argument is the default value, the third should always be <code>True</code> for such values (it selects if Sphinx re-reads the documents if the value changes).</dl>
<h3><code>sphinx.ext.coverage</code> &#8212; Collect doc coverage stats</h3>
<p> This extension features one additional builder, the <code>CoverageBuilder</code>.</p>
<dl>
<dt><code>class sphinx.ext.coverage.CoverageBuilder</code></p>
<dd> To use this builder, activate the coverage extension in your configuration file and give <code>-b coverage</code> on the command line.</dl>
<h3>Todo</h3>
<p> Write this section. </p>
<p> Several new configuration values can be used to specify what the builder should check:</p>
<dl>
<dt><code>coverage_ignore_modules</code></p>
<dd>
<dt><code>coverage_ignore_functions</code></p>
<dd>
<dt><code>coverage_ignore_classes</code></p>
<dd>
<dt><code>coverage_c_path</code></p>
<dd>
<dt><code>coverage_c_regexes</code></p>
<dd>
<dt><code>coverage_ignore_c_items</code></p>
<dd>
<dt><code>coverage_write_headline</code></p>
<dd> Set to <code>False</code> to not write headlines. </p>
<p> New in version 1.1. </p>
<dt><code>coverage_skip_undoc_in_source</code></p>
<dd> Skip objects that are not documented in the source with a docstring. <code>False</code> by default. </p>
<p> New in version 1.1. </p>
</dl>
<h3><code>sphinx.ext.todo</code> &#8212; Support for todo items</h3>
<p> <i>Module author: Daniel BÃ¼ltmann</i> </p>
<p> New in version 0.5. </p>
<p> There are two additional directives when using this extension:</p>
<dl>
<dt><code>.. todo::</code></p>
<dd> Use this directive like, for example, <code>note</code>. </p>
<p> It will only show up in the output if <code>todo_include_todos</code> is true.</p>
<dt><code>.. todolist::</code></p>
<dd> This directive is replaced by a list of all todo directives in the whole documentation, if <code>todo_include_todos</code> is true. </p>
<p> There is also an additional config value:</p>
<dt><code>todo_include_todos</code></p>
<dd> If this is <code>True</code>, <code>todo</code> and <code>todolist</code> produce output, else they produce nothing. The default is <code>False</code>.</dl>
<h3><code>sphinx.ext.extlinks</code> &#8212; Markup to shorten external links</h3>
<p> <i>Module author: Georg Brandl</i> </p>
<p> New in version 1.0. </p>
<p> This extension is meant to help with the common pattern of having many external links that point to URLs on one and the same site, e.g. links to bug trackers, version control web interfaces, or simply subpages in other websites. It does so by providing aliases to base URLs, so that you only need to give the subpage name when creating a link. </p>
<p> Let&#8217;s assume that you want to include many links to issues at the Sphinx tracker, at <code><a rel="nofollow" href="http://bitbucket.org/birkenfeld/sphinx/issue/">http://bitbucket.org/birkenfeld/sphinx/issue/</a></code><i>num</i>. Typing this URL again and again is tedious, so you can use <code>extlinks</code> to avoid repeating yourself. </p>
<p> The extension adds one new config value:</p>
<dl>
<dt><code>extlinks</code></p>
<dd> This config value must be a dictionary of external sites, mapping unique short alias names to a base URL and a <i>prefix</i>. For example, to create an alias for the above mentioned issues, you would add </p>
<pre>
extlinks = {'issue': ('<a rel="nofollow" href="https://bitbucket.org/birkenfeld/sphinx/issue/%s',">https://bitbucket.org/birkenfeld/sphinx/issue/%s',</a>
                      'issue ')}
</pre>
<p> Now, you can use the alias name as a new role, e.g. <code>:issue:`123`</code>. This then inserts a link to <i><a rel="nofollow" href="https://bitbucket.org/birkenfeld/sphinx/issue/123">https://bitbucket.org/birkenfeld/sphinx/issue/123</a></i>. As you can see, the target given in the role is substituted in the base URL in the place of <code>%s</code>. </p>
<p> The link <i>caption</i> depends on the second item in the tuple, the <i>prefix</i>:</p>
<dt>&bull;</p>
<dd> If the prefix is <code>None</code>, the link caption is the full URL.</p>
<dt>&bull;</p>
<dd> If the prefix is the empty string, the link caption is the partial URL given in the role content (<code>123</code> in this case.)</p>
<dt>&bull;</p>
<dd> If the prefix is a non-empty string, the link caption is the partial URL, prepended by the prefix &#8212; in the above example, the link caption would be <code>issue 123</code>. </p>
<p> You can also use the usual &quot;explicit title&quot; syntax supported by other roles that generate links, i.e. <code>:issue:`this issue &lt;123&gt;`</code>. In this case, the <i>prefix</i> is not relevant. </p>
<p> <code>NOTE:</code> Since links are generated from the role in the reading stage, they appear as ordinary links to e.g. the <code>linkcheck</code> builder.</dl>
<h3><code>sphinx.ext.viewcode</code> &#8212; Add links to highlighted source code</h3>
<p> <i>Module author: Georg Brandl</i> </p>
<p> New in version 1.0. </p>
<p> This extension looks at your Python object descriptions (<code>.. class::</code>, <code>.. function::</code> etc.) and tries to find the source files where the objects are contained. When found, a separate HTML page will be output for each module with a highlighted version of the source code, and a link will be added to all object descriptions that leads to the source code of the described object. A link back from the source to the description will also be inserted. </p>
<p> There are currently no configuration values for this extension; you just need to add <code>&#8216;sphinx.ext.viewcode&#8217;</code> to your <code>extensions</code> value for it to work.</p>
<h3><code>sphinx.ext.linkcode</code> &#8212; Add external links to source code</h3>
<p> <i>Module author: Pauli Virtanen</i> </p>
<p> New in version 1.2. </p>
<p> This extension looks at your object descriptions (<code>.. class::</code>, <code>.. function::</code> etc.) and adds external links to code hosted somewhere on the web. The intent is similar to the <code>sphinx.ext.viewcode</code> extension, but assumes the source code can be found somewhere on the Internet. </p>
<p> In your configuration, you need to specify a <code>linkcode_resolve</code> function that returns an URL based on the object.</p>
<dl>
<dt><code>linkcode_resolve</code></p>
<dd> This is a function <code>linkcode_resolve(domain, info)</code>, which should return the URL to source code corresponding to the object in given domain with given information. </p>
<p> The function should return <code>None</code> if no link is to be added. </p>
<p> The argument <code>domain</code> specifies the language domain the object is in. <code>info</code> is a dictionary with the following keys guaranteed to be present (dependent on the domain):</p>
<dt>&bull;</p>
<dd> <code>py</code>: <code>module</code> (name of the module), <code>fullname</code> (name of the object)</p>
<dt>&bull;</p>
<dd> <code>c</code>: <code>names</code> (list of names for the object)</p>
<dt>&bull;</p>
<dd> <code>cpp</code>: <code>names</code> (list of names for the object)</p>
<dt>&bull;</p>
<dd> <code>javascript</code>: <code>object</code> (name of the object), <code>fullname</code> (name of the item) </p>
<p> Example: </p>
<pre>
def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return &quot;<a rel="nofollow" href="http://somesite/sourcerepo/%s.py">http://somesite/sourcerepo/%s.py</a>&quot; % filename
</pre>
</dl>
<h3><code>sphinx.ext.oldcmarkup</code> &#8212; Compatibility extension for old C markup</h3>
<p> <i>Module author: Georg Brandl</i> </p>
<p> New in version 1.0. </p>
<p> This extension is a transition helper for projects that used the old (pre-domain) C markup, i.e. the directives like <code>cfunction</code> and roles like <code>cfunc</code>. Since the introduction of domains, they must be called by their fully-qualified name (<code>c:function</code> and <code>c:func</code>, respectively) or, with the default domain set to <code>c</code>, by their new name (<code>function</code> and <code>func</code>). (See <i>c-domain</i> for the details.) </p>
<p> If you activate this extension, it will register the old names, and you can use them like before Sphinx 1.0. The directives are:</p>
<dl>
<dt>&bull;</p>
<dd> <code>cfunction</code></p>
<dt>&bull;</p>
<dd> <code>cmember</code></p>
<dt>&bull;</p>
<dd> <code>cmacro</code></p>
<dt>&bull;</p>
<dd> <code>ctype</code></p>
<dt>&bull;</p>
<dd> <code>cvar</code> </p>
<p> The roles are:</p>
<dt>&bull;</p>
<dd> <code>cdata</code></p>
<dt>&bull;</p>
<dd> <code>cfunc</code></p>
<dt>&bull;</p>
<dd> <code>cmacro</code></p>
<dt>&bull;</p>
<dd> <code>ctype</code> </p>
<p> However, it is advised to migrate to the new markup &#8212; this extension is a compatibility convenience and will disappear in a future version of Sphinx.</dl>
<h3>Third-party extensions</h3>
<p> You can find several extensions contributed by users in the <i>Sphinx Contrib</i> repository. It is open for anyone who wants to maintain an extension publicly; just send a short message asking for write permissions. </p>
<p> There are also several extensions hosted elsewhere. The <i>Wiki at BitBucket</i> maintains a list of those. </p>
<p> If you write an extension that you think others will find useful or you think should be included as a part of Sphinx, please write to the project mailing list (<i>join here</i>).</p>
<h3>Where to put your own extensions?</h3>
<p> Extensions local to a project should be put within the project&#8217;s directory structure. Set Python&#8217;s module search path, <code>sys.path</code>, accordingly so that Sphinx can find them. E.g., if your extension <code>foo.py</code> lies in the <code>exts</code> subdirectory of the project root, put into <code>conf.py</code>: </p>
<pre>
import sys, os
sys.path.append(os.path.abspath('exts'))
extensions = ['foo']
</pre>
<p> You can also install extensions anywhere else on <code>sys.path</code>, e.g. in the <code>site-packages</code> directory.</p>
<h2>DEVELOPING EXTENSIONS FOR SPHINX</h2>
<p> Since many projects will need special features in their documentation, Sphinx is designed to be extensible on several levels. </p>
<p> This is what you can do in an extension: First, you can add new <i>builder</i>s to support new output formats or actions on the parsed documents. Then, it is possible to register custom reStructuredText roles and directives, extending the markup. And finally, there are so-called &quot;hook points&quot; at strategic places throughout the build process, where an extension can register a hook and run specialized code. </p>
<p> An extension is simply a Python module. When an extension is loaded, Sphinx imports this module and executes its <code>setup()</code> function, which in turn notifies Sphinx of everything the extension offers &#8212; see the extension tutorial for examples. </p>
<p> The configuration file itself can be treated as an extension if it contains a <code>setup()</code> function. All other extensions to load must be listed in the <code>extensions</code> configuration value.</p>
<h3>Tutorial: Writing a simple extension</h3>
<p> This section is intended as a walkthrough for the creation of custom extensions. It covers the basics of writing and activating an extensions, as well as commonly used features of extensions. </p>
<p> As an example, we will cover a &quot;todo&quot; extension that adds capabilities to include todo entries in the documentation, and collecting these in a central place. (A similar &quot;todo&quot; extension is distributed with Sphinx.)</p>
<h3>Important objects</h3>
<p> There are several key objects whose API you will use while writing an extension. These are:</p>
<dl>
<dt><code>Application</code></p>
<dd> The application object (usually called <code>app</code>) is an instance of <code>Sphinx</code>. It controls the most high-level functionality, such as the setup of extensions, event dispatching and producing output (logging). </p>
<p> If you have the environment object, the application is available as <code>env.app</code>.</p>
<dt><code>Environment</code></p>
<dd> The build environment object (usually called <code>env</code>) is an instance of <code>BuildEnvironment</code>. It is responsible for parsing the source documents stores all metadata about the document collection and is serialized after each build. </p>
<p> Its API provides methods to do with access to metadata, resolving references, etc. It can also be used by extensions to cache information that should persist for incremental rebuilds. </p>
<p> If you have the application or builder object, the environment is available as <code>app.env</code> or <code>builder.env</code>.</p>
<dt><code>Builder</code></p>
<dd> The builder object (usually called <code>builder</code>) is an instance of a specific subclass of <code>Builder</code>. Each builder class knows how to convert the parsed documents into an output format, or otherwise process them (e.g. check external links). </p>
<p> If you have the application object, the environment is available as <code>app.builder</code>.</p>
<dt><code>Config</code></p>
<dd> The config object (usually called <code>config</code>) provides the values of configuration values set in <code>conf.py</code> as attributes. It is an instance of <code>Config</code>. </p>
<p> The config is available as <code>app.config</code> or <code>env.config</code>.</dl>
<h3>Build Phases</h3>
<p> One thing that is vital in order to understand extension mechanisms is the way in which a Sphinx project is built: this works in several phases. </p>
<p> <code>Phase 0: Initialization</code> In this phase, almost nothing interesting for us happens. The source directory is searched for source files, and extensions are initialized. Should a stored build environment exist, it is loaded, otherwise a new one is created. </p>
<p> <code>Phase 1: Reading</code> In Phase 1, all source files (and on subsequent builds, those that are new or changed) are read and parsed. This is the phase where directives and roles are encountered by the docutils, and the corresponding code is executed. The output of this phase is a <i>doctree</i> for each source files, that is a tree of docutils nodes. For document elements that aren&#8217;t fully known until all existing files are read, temporary nodes are created. </p>
<p> There are nodes provided by docutils, which are documented <i>in the docutils documentation</i>. Additional nodes are provided by Sphinx and <i>documented here</i>. </p>
<p> During reading, the build environment is updated with all meta- and cross reference data of the read documents, such as labels, the names of headings, described Python objects and index entries. This will later be used to replace the temporary nodes. </p>
<p> The parsed doctrees are stored on the disk, because it is not possible to hold all of them in memory. </p>
<p> <code>Phase 2: Consistency checks</code> Some checking is done to ensure no surprises in the built documents. </p>
<p> <code>Phase 3: Resolving</code> Now that the metadata and cross-reference data of all existing documents is known, all temporary nodes are replaced by nodes that can be converted into output. For example, links are created for object references that exist, and simple literal nodes are created for those that don&#8217;t. </p>
<p> <code>Phase 4: Writing</code> This phase converts the resolved doctrees to the desired output format, such as HTML or LaTeX. This happens via a so-called docutils writer that visits the individual nodes of each doctree and produces some output in the process. </p>
<p> <code>NOTE:</code> Some builders deviate from this general build plan, for example, the builder that checks external links does not need anything more than the parsed doctrees and therefore does not have phases 2&#8211;4.</p>
<h3>Extension Design</h3>
<p> We want the extension to add the following to Sphinx:</p>
<dl>
<dt>&bull;</p>
<dd> A &quot;todo&quot; directive, containing some content that is marked with &quot;TODO&quot;, and only shown in the output if a new config value is set. (Todo entries should not be in the output by default.)</p>
<dt>&bull;</p>
<dd> A &quot;todolist&quot; directive that creates a list of all todo entries throughout the documentation. </p>
<p> For that, we will need to add the following elements to Sphinx:</p>
<dt>&bull;</p>
<dd> New directives, called <code>todo</code> and <code>todolist</code>.</p>
<dt>&bull;</p>
<dd> New document tree nodes to represent these directives, conventionally also called <code>todo</code> and <code>todolist</code>. We wouldn&#8217;t need new nodes if the new directives only produced some content representable by existing nodes.</p>
<dt>&bull;</p>
<dd> A new config value <code>todo_include_todos</code> (config value names should start with the extension name, in order to stay unique) that controls whether todo entries make it into the output.</p>
<dt>&bull;</p>
<dd> New event handlers: one for the <code>doctree-resolved</code> event, to replace the todo and todolist nodes, and one for <code>env-purge-doc</code> (the reason for that will be covered later).</dl>
<h3>The Setup Function</h3>
<p> The new elements are added in the extension&#8217;s setup function. Let us create a new Python module called <code>todo.py</code> and add the setup function: </p>
<pre>
def setup(app):
    app.add_config_value('todo_include_todos', False, False)
    app.add_node(todolist)
    app.add_node(todo,
                 html=(visit_todo_node, depart_todo_node),
                 latex=(visit_todo_node, depart_todo_node),
                 text=(visit_todo_node, depart_todo_node))
    app.add_directive('todo', TodoDirective)
    app.add_directive('todolist', TodolistDirective)
    app.connect('doctree-resolved', process_todo_nodes)
    app.connect('env-purge-doc', purge_todos)
</pre>
<p> The calls in this function refer to classes and functions not yet written. What the individual calls do is the following:</p>
<dl>
<dt>&bull;</p>
<dd> <code>add_config_value()</code> lets Sphinx know that it should recognize the new <i>config value</i> <code>todo_include_todos</code>, whose default value should be <code>False</code> (this also tells Sphinx that it is a boolean value). </p>
<p> If the third argument was <code>True</code>, all documents would be re-read if the config value changed its value. This is needed for config values that influence reading (build phase 1).</p>
<dt>&bull;</p>
<dd> <code>add_node()</code> adds a new <i>node class</i> to the build system. It also can specify visitor functions for each supported output format. These visitor functions are needed when the new nodes stay until phase 4 &#8212; since the <code>todolist</code> node is always replaced in phase 3, it doesn&#8217;t need any. </p>
<p> We need to create the two node classes <code>todo</code> and <code>todolist</code> later.</p>
<dt>&bull;</p>
<dd> <code>add_directive()</code> adds a new <i>directive</i>, given by name and class. </p>
<p> The handler functions are created later.</p>
<dt>&bull;</p>
<dd> Finally, <code>connect()</code> adds an <i>event handler</i> to the event whose name is given by the first argument. The event handler function is called with several arguments which are documented with the event.</dl>
<h3>The Node Classes</h3>
<p> Let&#8217;s start with the node classes: </p>
<pre>
from docutils import nodes
class todo(nodes.Admonition, nodes.Element):
    pass
class todolist(nodes.General, nodes.Element):
    pass
def visit_todo_node(self, node):
    self.visit_admonition(node)
def depart_todo_node(self, node):
    self.depart_admonition(node)
</pre>
<p> Node classes usually don&#8217;t have to do anything except inherit from the standard docutils classes defined in <code>docutils.nodes</code>. <code>todo</code> inherits from <code>Admonition</code> because it should be handled like a note or warning, <code>todolist</code> is just a &quot;general&quot; node. </p>
<p> <code>NOTE:</code> Many extensions will not have to create their own node classes and work fine with the nodes already provided by <i>docutils</i> and <i>Sphinx</i>.</p>
<h3>The Directive Classes</h3>
<p> A directive class is a class deriving usually from <code>docutils.parsers.rst.Directive</code>. The directive interface is also covered in detail in the <i>docutils documentation</i>; the important thing is that the class has attributes that configure the allowed markup and a method <code>run</code> that returns a list of nodes. </p>
<p> The <code>todolist</code> directive is quite simple: </p>
<pre>
from docutils.parsers.rst import Directive
class TodolistDirective(Directive):
    def run(self):
        return [todolist('')]
</pre>
<p> An instance of our <code>todolist</code> node class is created and returned. The todolist directive has neither content nor arguments that need to be handled. </p>
<p> The <code>todo</code> directive function looks like this: </p>
<pre>
from sphinx.util.compat import make_admonition
class TodoDirective(Directive):
    # this enables content in the directive
    has_content = True
    def run(self):
        env = self.state.document.settings.env
        targetid = &quot;todo-%d&quot; % env.new_serialno('todo')
        targetnode = nodes.target('', '', ids=[targetid])
        ad = make_admonition(todo, self.name, [_('Todo')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)
        if not hasattr(env, 'todo_all_todos'):
            env.todo_all_todos = []
        env.todo_all_todos.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'todo': ad[0].deepcopy(),
            'target': targetnode,
        })
        return [targetnode] + ad
</pre>
<p> Several important things are covered here. First, as you can see, you can refer to the build environment instance using <code>self.state.document.settings.env</code>. </p>
<p> Then, to act as a link target (from the todolist), the todo directive needs to return a target node in addition to the todo node. The target ID (in HTML, this will be the anchor name) is generated by using <code>env.new_serialno</code> which returns a new unique integer on each call and therefore leads to unique target names. The target node is instantiated without any text (the first two arguments). </p>
<p> An admonition is created using a standard docutils function (wrapped in Sphinx for docutils cross-version compatibility). The first argument gives the node class, in our case <code>todo</code>. The third argument gives the admonition title (use <code>arguments</code> here to let the user specify the title). A list of nodes is returned from <code>make_admonition</code>. </p>
<p> Then, the todo node is added to the environment. This is needed to be able to create a list of all todo entries throughout the documentation, in the place where the author puts a <code>todolist</code> directive. For this case, the environment attribute <code>todo_all_todos</code> is used (again, the name should be unique, so it is prefixed by the extension name). It does not exist when a new environment is created, so the directive must check and create it if necessary. Various information about the todo entry&#8217;s location are stored along with a copy of the node. </p>
<p> In the last line, the nodes that should be put into the doctree are returned: the target node and the admonition node. </p>
<p> The node structure that the directive returns looks like this: </p>
<pre>
+--------------------+
| target node        |
+--------------------+
+--------------------+
| todo node          |
+--------------------+
  \__+--------------------+
     | admonition title   |
     +--------------------+
     | paragraph          |
     +--------------------+
     | ...                |
     +--------------------+
</pre>
<h3>The Event Handlers</h3>
<p> Finally, let&#8217;s look at the event handlers. First, the one for the <code>env-purge-doc</code> event: </p>
<pre>
def purge_todos(app, env, docname):
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]
</pre>
<p> Since we store information from source files in the environment, which is persistent, it may become out of date when the source file changes. Therefore, before each source file is read, the environment&#8217;s records of it are cleared, and the <code>env-purge-doc</code> event gives extensions a chance to do the same. Here we clear out all todos whose docname matches the given one from the <code>todo_all_todos</code> list. If there are todos left in the document, they will be added again during parsing. </p>
<p> The other handler belongs to the <code>doctree-resolved</code> event. This event is emitted at the end of phase 3 and allows custom resolving to be done: </p>
<pre>
def process_todo_nodes(app, doctree, fromdocname):
    if not app.config.todo_include_todos:
        for node in doctree.traverse(todo):
            node.parent.remove(node)
    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env
    for node in doctree.traverse(todolist):
        if not app.config.todo_include_todos:
            node.replace_self([])
            continue
        content = []
        for todo_info in env.todo_all_todos:
            para = nodes.paragraph()
            filename = env.doc2path(todo_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, todo_info['lineno']))
            para += nodes.Text(description, description)
            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = todo_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, todo_info['docname'])
            newnode['refuri'] += '#' + todo_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')
            # Insert into the todolist
            content.append(todo_info['todo'])
            content.append(para)
        node.replace_self(content)
</pre>
<p> It is a bit more involved. If our new &quot;todo_include_todos&quot; config value is false, all todo and todolist nodes are removed from the documents. </p>
<p> If not, todo nodes just stay where and how they are. Todolist nodes are replaced by a list of todo entries, complete with backlinks to the location where they come from. The list items are composed of the nodes from the todo entry and docutils nodes created on the fly: a paragraph for each entry, containing text that gives the location, and a link (reference node containing an italic node) with the backreference. The reference URI is built by <code>app.builder.get_relative_uri</code> which creates a suitable URI depending on the used builder, and appending the todo node&#8217;s (the target&#8217;s) ID as the anchor name.</p>
<h3>Application API</h3>
<p> Each Sphinx extension is a Python module with at least a <code>setup()</code> function. This function is called at initialization time with one argument, the application object representing the Sphinx process.</p>
<dl>
<dt><code>class sphinx.application.Sphinx</code></p>
<dd> This application object has the public API described in the following.</dl>
<h3>Extension setup</h3>
<p> These methods are usually called in an extension&#8217;s <code>setup()</code> function. </p>
<p> Examples of using the Sphinx extension API can be seen in the <code>sphinx.ext</code> package.</p>
<dl>
<dt><code>Sphinx.setup_extension(name)</code></p>
<dd> Load the extension given by the module <i>name</i>. Use this if your extension needs the features provided by another extension.</p>
<dt><code>Sphinx.add_builder(builder)</code></p>
<dd> Register a new builder. <i>builder</i> must be a class that inherits from <code>Builder</code>.</p>
<dt><code>Sphinx.add_config_value(name, default, rebuild)</code></p>
<dd> Register a configuration value. This is necessary for Sphinx to recognize new values and set default values accordingly. The <i>name</i> should be prefixed with the extension name, to avoid clashes. The <i>default</i> value can be any Python object. The string value <i>rebuild</i> must be one of those values:</p>
<dt>&bull;</p>
<dd> <code>&#8216;env&#8217;</code> if a change in the setting only takes effect when a document is parsed &#8212; this means that the whole environment must be rebuilt.</p>
<dt>&bull;</p>
<dd> <code>&#8216;html&#8217;</code> if a change in the setting needs a full rebuild of HTML documents.</p>
<dt>&bull;</p>
<dd> <code>&#8221;</code> if a change in the setting will not need any special rebuild. </p>
<p> Changed in version 0.4: If the <i>default</i> value is a callable, it will be called with the config object as its argument in order to get the default value. This can be used to implement config values whose default depends on other values. </p>
<p> Changed in version 0.6: Changed <i>rebuild</i> from a simple boolean (equivalent to <code>&#8221;</code> or <code>&#8216;env&#8217;</code>) to a string. However, booleans are still accepted and converted internally. </p>
<dt><code>Sphinx.add_domain(domain)</code></p>
<dd> Make the given <i>domain</i> (which must be a class; more precisely, a subclass of <code>Domain</code>) known to Sphinx. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.override_domain(domain)</code></p>
<dd> Make the given <i>domain</i> class known to Sphinx, assuming that there is already a domain with its <code>.name</code>. The new domain must be a subclass of the existing one. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.add_index_to_domain(domain, index)</code></p>
<dd> Add a custom <i>index</i> class to the domain named <i>domain</i>. <i>index</i> must be a subclass of <code>Index</code>. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.add_event(name)</code></p>
<dd> Register an event called <i>name</i>. This is needed to be able to emit it.</p>
<dt><code>Sphinx.add_node(node, **kwds)</code></p>
<dd> Register a Docutils node class. This is necessary for Docutils internals. It may also be used in the future to validate nodes in the parsed documents. </p>
<p> Node visitor functions for the Sphinx HTML, LaTeX, text and manpage writers can be given as keyword arguments: the keyword must be one or more of <code>&#8216;html&#8217;</code>, <code>&#8216;latex&#8217;</code>, <code>&#8216;text&#8217;</code>, <code>&#8216;man&#8217;</code>, <code>&#8216;texinfo&#8217;</code>, the value a 2-tuple of <code>(visit, depart)</code> methods. <code>depart</code> can be <code>None</code> if the <code>visit</code> function raises <code>docutils.nodes.SkipNode</code>. Example: </p>
<pre>
class math(docutils.nodes.Element): pass
def visit_math_html(self, node):
    self.body.append(self.starttag(node, 'math'))
def depart_math_html(self, node):
    self.body.append('&lt;/math&gt;')
app.add_node(math, html=(visit_math_html, depart_math_html))
</pre>
<p> Obviously, translators for which you don&#8217;t specify visitor methods will choke on the node when encountered in a document to translate. </p>
<p> Changed in version 0.5: Added the support for keyword arguments giving visit functions. </p>
<dt><code>Sphinx.add_directive(name, func, content, arguments, **options)</code></p>
<dd>
<dt><code>Sphinx.add_directive(name, directiveclass)</code></p>
<dd> Register a Docutils directive. <i>name</i> must be the prospective directive name. There are two possible ways to write a directive:</p>
<dt>&bull;</p>
<dd> In the docutils 0.4 style, <i>obj</i> is the directive function. <i>content</i>, <i>arguments</i> and <i>options</i> are set as attributes on the function and determine whether the directive has content, arguments and options, respectively. <code>This style is deprecated.</code></p>
<dt>&bull;</p>
<dd> In the docutils 0.5 style, <i>directiveclass</i> is the directive class. It must already have attributes named <i>has_content</i>, <i>required_arguments</i>, <i>optional_arguments</i>, <i>final_argument_whitespace</i> and <i>option_spec</i> that correspond to the options for the function way. See <i>the Docutils docs</i> for details. </p>
<p> The directive class must inherit from the class <code>docutils.parsers.rst.Directive</code>. </p>
<p> For example, the (already existing) <code>literalinclude</code> directive would be added like this: </p>
<pre>
from docutils.parsers.rst import directives
add_directive('literalinclude', literalinclude_directive,
              content = 0, arguments = (1, 0, 0),
              linenos = directives.flag,
              language = direcitves.unchanged,
              encoding = directives.encoding)
</pre>
<p> Changed in version 0.6: Docutils 0.5-style directive classes are now supported. </p>
<dt><code>Sphinx.add_directive_to_domain(domain, name, func, content, arguments, **options)</code></p>
<dd>
<dt><code>Sphinx.add_directive_to_domain(domain, name, directiveclass)</code></p>
<dd> Like <code>add_directive()</code>, but the directive is added to the domain named <i>domain</i>. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.add_role(name, role)</code></p>
<dd> Register a Docutils role. <i>name</i> must be the role name that occurs in the source, <i>role</i> the role function (see the <i>Docutils documentation</i> on details).</p>
<dt><code>Sphinx.add_role_to_domain(domain, name, role)</code></p>
<dd> Like <code>add_role()</code>, but the role is added to the domain named <i>domain</i>. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.add_generic_role(name, nodeclass)</code></p>
<dd> Register a Docutils role that does nothing but wrap its contents in the node given by <i>nodeclass</i>. </p>
<p> New in version 0.6. </p>
<dt><code>Sphinx.add_object_type(directivename, rolename, indextemplate=&#8221;, parse_node=None, ref_nodeclass=None, objname=&#8221;, doc_field_types=[])</code></p>
<dd> This method is a very convenient way to add a new <i>object</i> type that can be cross-referenced. It will do this:</p>
<dt>&bull;</p>
<dd> Create a new directive (called <i>directivename</i>) for documenting an object. It will automatically add index entries if <i>indextemplate</i> is nonempty; if given, it must contain exactly one instance of <code>%s</code>. See the example below for how the template will be interpreted.</p>
<dt>&bull;</p>
<dd> Create a new role (called <i>rolename</i>) to cross-reference to these object descriptions.</p>
<dt>&bull;</p>
<dd> If you provide <i>parse_node</i>, it must be a function that takes a string and a docutils node, and it must populate the node with children parsed from the string. It must then return the name of the item to be used in cross-referencing and index entries. See the <code>conf.py</code> file in the source for this documentation for an example.</p>
<dt>&bull;</p>
<dd> The <i>objname</i> (if not given, will default to <i>directivename</i>) names the type of object. It is used when listing objects, e.g. in search results. </p>
<p> For example, if you have this call in a custom Sphinx extension: </p>
<pre>
app.add_object_type('directive', 'dir', 'pair: %s; directive')
</pre>
<p> you can use this markup in your documents: </p>
<pre>
.. rst:directive:: function
   Document a function.
&lt;...&gt;
See also the :rst:dir:`function` directive.
</pre>
<p> For the directive, an index entry will be generated as if you had prepended </p>
<pre>
.. index:: pair: function; directive
</pre>
<p> The reference node will be of class <code>literal</code> (so it will be rendered in a proportional font, as appropriate for code) unless you give the <i>ref_nodeclass</i> argument, which must be a docutils node class (most useful are <code>docutils.nodes.emphasis</code> or <code>docutils.nodes.strong</code> &#8212; you can also use <code>docutils.nodes.generated</code> if you want no further text decoration). </p>
<p> For the role content, you have the same syntactical possibilities as for standard Sphinx roles (see <i>xref-syntax</i>). </p>
<p> This method is also available under the deprecated alias <code>add_description_unit</code>.</p>
<dt><code>Sphinx.add_crossref_type(directivename, rolename, indextemplate=&#8221;, ref_nodeclass=None, objname=&#8221;)</code></p>
<dd> This method is very similar to <code>add_object_type()</code> except that the directive it generates must be empty, and will produce no output. </p>
<p> That means that you can add semantic targets to your sources, and refer to them using custom roles instead of generic ones (like <code>ref</code>). Example call: </p>
<pre>
app.add_crossref_type('topic', 'topic', 'single: %s', docutils.nodes.emphasis)
</pre>
<p> Example usage: </p>
<pre>
.. topic:: application API
The application API
-------------------
&lt;...&gt;
See also :topic:`this section &lt;application API&gt;`.
</pre>
<p> (Of course, the element following the <code>topic</code> directive needn&#8217;t be a section.)</p>
<dt><code>Sphinx.add_transform(transform)</code></p>
<dd> Add the standard docutils <code>Transform</code> subclass <i>transform</i> to the list of transforms that are applied after Sphinx parses a reST document.</p>
<dt><code>Sphinx.add_javascript(filename)</code></p>
<dd> Add <i>filename</i> to the list of JavaScript files that the default HTML template will include. The filename must be relative to the HTML static path, see <code>the docs for the config value</code>. A full URI with scheme, like <code><a rel="nofollow" href="http://example.org/foo.js">http://example.org/foo.js</a></code>, is also supported. </p>
<p> New in version 0.5. </p>
<dt><code>Sphinx.add_stylesheet(filename)</code></p>
<dd> Add <i>filename</i> to the list of CSS files that the default HTML template will include. Like for <code>add_javascript()</code>, the filename must be relative to the HTML static path, or a full URI with scheme. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.add_lexer(alias, lexer)</code></p>
<dd> Use <i>lexer</i>, which must be an instance of a Pygments lexer class, to highlight code blocks with the given language <i>alias</i>. </p>
<p> New in version 0.6. </p>
<dt><code>Sphinx.add_autodocumenter(cls)</code></p>
<dd> Add <i>cls</i> as a new documenter class for the <code>sphinx.ext.autodoc</code> extension. It must be a subclass of <code>sphinx.ext.autodoc.Documenter</code>. This allows to auto-document new types of objects. See the source of the autodoc module for examples on how to subclass <code>Documenter</code>. </p>
<p> New in version 0.6. </p>
<dt><code>Sphinx.add_autodoc_attrgetter(type, getter)</code></p>
<dd> Add <i>getter</i>, which must be a function with an interface compatible to the <code>getattr()</code> builtin, as the autodoc attribute getter for objects that are instances of <i>type</i>. All cases where autodoc needs to get an attribute of a type are then handled by this function instead of <code>getattr()</code>. </p>
<p> New in version 0.6. </p>
<dt><code>Sphinx.add_search_language(cls)</code></p>
<dd> Add <i>cls</i>, which must be a subclass of <code>sphinx.search.SearchLanguage</code>, as a support language for building the HTML full-text search index. The class must have a <i>lang</i> attribute that indicates the language it should be used for. See <code>html_search_language</code>. </p>
<p> New in version 1.1. </p>
<dt><code>Sphinx.require_sphinx(version)</code></p>
<dd> Compare <i>version</i> (which must be a <code>major.minor</code> version string, e.g. <code>&#8216;1.1&#8217;</code>) with the version of the running Sphinx, and abort the build when it is too old. </p>
<p> New in version 1.0. </p>
<dt><code>Sphinx.connect(event, callback)</code></p>
<dd> Register <i>callback</i> to be called when <i>event</i> is emitted. For details on available core events and the arguments of callback functions, please see <i>events</i>. </p>
<p> The method returns a &quot;listener ID&quot; that can be used as an argument to <code>disconnect()</code>.</p>
<dt><code>Sphinx.disconnect(listener_id)</code></p>
<dd> Unregister callback <i>listener_id</i>.</p>
<dt><code>exception sphinx.application.ExtensionError</code></p>
<dd> All these methods raise this exception if something went wrong with the extension API.</dl>
<h3>Emitting events</h3>
<dl>
<dt><code>Sphinx.emit(event, *arguments)</code></p>
<dd> Emit <i>event</i> and pass <i>arguments</i> to the callback functions. Return the return values of all callbacks as a list. Do not emit core Sphinx events in extensions!</p>
<dt><code>Sphinx.emit_firstresult(event, *arguments)</code></p>
<dd> Emit <i>event</i> and pass <i>arguments</i> to the callback functions. Return the result of the first callback that doesn&#8217;t return <code>None</code>. </p>
<p> New in version 0.5. </p>
</dl>
<h3>Producing messages / logging</h3>
<p> The application object also provides support for emitting leveled messages. </p>
<p> <code>NOTE:</code> There is no &quot;error&quot; call: in Sphinx, errors are defined as things that stop the build; just raise an exception (<code>sphinx.errors.SphinxError</code> or a custom subclass) to do that.</p>
<dl>
<dt><code>Sphinx.warn(message, location=None, prefix=&#8217;WARNING: &#8216;)</code></p>
<dd> Emit a warning. </p>
<p> If <i>location</i> is given, it should either be a tuple of (docname, lineno) or a string describing the location of the warning as well as possible. </p>
<p> <i>prefix</i> usually should not be changed. </p>
<p> <code>NOTE:</code> For warnings emitted during parsing, you should use <code>BuildEnvironment.warn()</code> since that will collect all warnings during parsing for later output.</p>
<dt><code>Sphinx.info(message=&#8221;, nonl=False)</code></p>
<dd> Emit an informational message. </p>
<p> If <i>nonl</i> is true, don&#8217;t emit a newline at the end (which implies that more info output will follow soon.)</p>
<dt><code>Sphinx.verbose(message, *args, **kwargs)</code></p>
<dd> Emit a verbose informational message. </p>
<p> The message will only be emitted for verbosity levels &gt;= 1 (i.e. at least one <code>-v</code> option was given). </p>
<p> The message can contain %-style interpolation placeholders, which is formatted with either the <code>*args</code> or <code>**kwargs</code> when output.</p>
<dt><code>Sphinx.debug(message, *args, **kwargs)</code></p>
<dd> Emit a debug-level informational message. </p>
<p> The message will only be emitted for verbosity levels &gt;= 2 (i.e. at least two <code>-v</code> options were given). </p>
<p> The message can contain %-style interpolation placeholders, which is formatted with either the <code>*args</code> or <code>**kwargs</code> when output.</p>
<dt><code>Sphinx.debug2(message, *args, **kwargs)</code></p>
<dd> Emit a lowlevel debug-level informational message. </p>
<p> The message will only be emitted for verbosity level 3 (i.e. three <code>-v</code> options were given). </p>
<p> The message can contain %-style interpolation placeholders, which is formatted with either the <code>*args</code> or <code>**kwargs</code> when output.</dl>
<h3>Sphinx core events</h3>
<p> These events are known to the core. The arguments shown are given to the registered event handlers. Use <code>connect()</code> in an extension&#8217;s <code>setup</code> function (note that <code>conf.py</code> can also have a <code>setup</code> function) to connect handlers to the events. Example: </p>
<pre>
def source_read_handler(app, docname, source):
    print('do something here...')
def setup(app):
    app.connect('source-read', source_read_handler)
</pre>
<dl>
<dt><code>builder-inited(app)</code></p>
<dd> Emitted when the builder object has been created. It is available as <code>app.builder</code>.</p>
<dt><code>env-get-outdated(app, env, added, changed, removed)</code></p>
<dd> Emitted when the environment determines which source files have changed and should be re-read. <i>added</i>, <i>changed</i> and <i>removed</i> are sets of docnames that the environment has determined. You can return a list of docnames to re-read in addition to these. </p>
<p> New in version 1.1. </p>
<dt><code>env-purge-doc(app, env, docname)</code></p>
<dd> Emitted when all traces of a source file should be cleaned from the environment, that is, if the source file is removed or before it is freshly read. This is for extensions that keep their own caches in attributes of the environment. </p>
<p> For example, there is a cache of all modules on the environment. When a source file has been changed, the cache&#8217;s entries for the file are cleared, since the module declarations could have been removed from the file. </p>
<p> New in version 0.5. </p>
<dt><code>source-read(app, docname, source)</code></p>
<dd> Emitted when a source file has been read. The <i>source</i> argument is a list whose single element is the contents of the source file. You can process the contents and replace this item to implement source-level transformations. </p>
<p> For example, if you want to use <code>$</code> signs to delimit inline math, like in LaTeX, you can use a regular expression to replace <code>$&#8230;$</code> by <code>:math:`&#8230;`</code>. </p>
<p> New in version 0.5. </p>
<dt><code>doctree-read(app, doctree)</code></p>
<dd> Emitted when a doctree has been parsed and read by the environment, and is about to be pickled. The <i>doctree</i> can be modified in-place.</p>
<dt><code>missing-reference(app, env, node, contnode)</code></p>
<dd> Emitted when a cross-reference to a Python module or object cannot be resolved. If the event handler can resolve the reference, it should return a new docutils node to be inserted in the document tree in place of the node <i>node</i>. Usually this node is a <code>reference</code> node containing <i>contnode</i> as a child.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>env</code> &#8212; The build environment (<code>app.builder.env</code>).</p>
<dt>&bull;</p>
<dd> <code>node</code> &#8212; The <code>pending_xref</code> node to be resolved. Its attributes <code>reftype</code>, <code>reftarget</code>, <code>modname</code> and <code>classname</code> attributes determine the type and target of the reference.</p>
<dt>&bull;</p>
<dd> <code>contnode</code> &#8212; The node that carries the text and formatting inside the future reference and should be a child of the returned reference node. </p>
<p> New in version 0.5. </p>
<dt><code>doctree-resolved(app, doctree, docname)</code></p>
<dd> Emitted when a doctree has been &quot;resolved&quot; by the environment, that is, all references have been resolved and TOCs have been inserted. The <i>doctree</i> can be modified in place. </p>
<p> Here is the place to replace custom nodes that don&#8217;t have visitor methods in the writers, so that they don&#8217;t cause errors when the writers encounter them.</p>
<dt><code>env-updated(app, env)</code></p>
<dd> Emitted when the <code>update()</code> method of the build environment has completed, that is, the environment and all doctrees are now up-to-date. </p>
<p> New in version 0.5. </p>
<dt><code>html-collect-pages(app)</code></p>
<dd> Emitted when the HTML builder is starting to write non-document pages. You can add pages to write by returning an iterable from this event consisting of <code>(pagename, context, templatename)</code>. </p>
<p> New in version 1.0. </p>
<dt><code>html-page-context(app, pagename, templatename, context, doctree)</code></p>
<dd> Emitted when the HTML builder has created a context dictionary to render a template with &#8212; this can be used to add custom elements to the context. </p>
<p> The <i>pagename</i> argument is the canonical name of the page being rendered, that is, without <code>.html</code> suffix and using slashes as path separators. The <i>templatename</i> is the name of the template to render, this will be <code>&#8216;page.html&#8217;</code> for all pages from reST documents. </p>
<p> The <i>context</i> argument is a dictionary of values that are given to the template engine to render the page and can be modified to include custom values. Keys must be strings. </p>
<p> The <i>doctree</i> argument will be a doctree when the page is created from a reST documents; it will be <code>None</code> when the page is created from an HTML template alone. </p>
<p> New in version 0.4. </p>
<dt><code>build-finished(app, exception)</code></p>
<dd> Emitted when a build has finished, before Sphinx exits, usually used for cleanup. This event is emitted even when the build process raised an exception, given as the <i>exception</i> argument. The exception is reraised in the application after the event handlers have run. If the build process raised no exception, <i>exception</i> will be <code>None</code>. This allows to customize cleanup actions depending on the exception status. </p>
<p> New in version 0.5. </p>
</dl>
<h3>Checking the Sphinx version</h3>
<p> Use this to adapt your extension to API changes in Sphinx.</p>
<dl>
<dt><code>sphinx.version_info</code></p>
<dd> A tuple of five elements; for Sphinx version 1.2.1 beta 3 this would be <code>(1, 2, 1, &#8216;beta&#8217;, 3)</code>. </p>
<p> New in version 1.2: Before version 1.2, check the string <code>sphinx.__version__</code>. </p>
</dl>
<h3>The Config object</h3>
<dl>
<dt><code>class sphinx.config.Config</code></p>
<dd> The config object makes the values of all config values available as attributes. </p>
<p> It is available as the <code>config</code> attribute on the application and environment objects. For example, to get the value of <code>language</code>, use either <code>app.config.language</code> or <code>env.config.language</code>.</dl>
<h3>The template bridge</h3>
<dl>
<dt><code>class sphinx.application.TemplateBridge</code></p>
<dd> This class defines the interface for a &quot;template bridge&quot;, that is, a class that renders templates given a template name and a context.</p>
<dt><code>init(builder, theme=None, dirs=None)</code></p>
<dd> Called by the builder to initialize the template system. </p>
<p> <i>builder</i> is the builder object; you&#8217;ll probably want to look at the value of <code>builder.config.templates_path</code>. </p>
<p> <i>theme</i> is a <code>sphinx.theming.Theme</code> object or None; in the latter case, <i>dirs</i> can be list of fixed directories to look for templates.</p>
<dt><code>newest_template_mtime()</code></p>
<dd> Called by the builder to determine if output files are outdated because of template changes. Return the mtime of the newest template file that was changed. The default implementation returns <code>0</code>.</p>
<dt><code>render(template, context)</code></p>
<dd> Called by the builder to render a template given as a filename with a specified context (a Python dictionary).</p>
<dt><code>render_string(template, context)</code></p>
<dd> Called by the builder to render a template given as a string with a specified context (a Python dictionary).</dl>
<h3>Exceptions</h3>
<dl>
<dt><code>exception sphinx.errors.SphinxError</code></p>
<dd> This is the base class for &quot;nice&quot; exceptions. When such an exception is raised, Sphinx will abort the build and present the exception category and message to the user. </p>
<p> Extensions are encouraged to derive from this exception for their custom errors. </p>
<p> Exceptions <i>not</i> derived from <code>SphinxError</code> are treated as unexpected and shown to the user with a part of the traceback (and the full traceback saved in a temporary file).</p>
<dt><code>category</code></p>
<dd> Description of the exception &quot;category&quot;, used in converting the exception to a string (&quot;category: message&quot;). Should be set accordingly in subclasses.</p>
<dt><code>exception sphinx.errors.ConfigError</code></p>
<dd> Used for erroneous values or nonsensical combinations of configuration values.</p>
<dt><code>exception sphinx.errors.ExtensionError</code></p>
<dd> Used for errors in setting up extensions.</p>
<dt><code>exception sphinx.errors.ThemeError</code></p>
<dd> Used for errors to do with themes.</p>
<dt><code>exception sphinx.errors.VersionRequirementError</code></p>
<dd> Raised when the docs require a higher Sphinx version than the current one.</dl>
<h3>Build environment API</h3>
<dl>
<dt><code>class sphinx.environment.BuildEnvironment</code></p>
<dd> <code>Attributes</code></p>
<dt><code>app</code></p>
<dd> Reference to the <code>Sphinx</code> (application) object.</p>
<dt><code>config</code></p>
<dd> Reference to the <code>Config</code> object.</p>
<dt><code>srcdir</code></p>
<dd> Source directory (the directory containing <code>conf.py</code>).</p>
<dt><code>doctreedir</code></p>
<dd> Directory for storing pickled doctrees.</p>
<dt><code>found_docs</code></p>
<dd> A set of all existing docnames.</p>
<dt><code>metadata</code></p>
<dd> Dictionary mapping docnames to &quot;metadata&quot; (see <i>metadata</i>).</p>
<dt><code>titles</code></p>
<dd> Dictionary mapping docnames to the docutils node for their main title.</p>
<dt><code>docname</code></p>
<dd> Returns the docname of the document currently being parsed. </p>
<p> <code>Utility methods</code></p>
<dt><code>warn(docname, msg, lineno=None)</code></p>
<dd> Emit a warning. </p>
<p> This differs from using <code>app.warn()</code> in that the warning may not be emitted instantly, but collected for emitting all warnings after the update of the environment.</p>
<dt><code>warn_node(msg, node)</code></p>
<dd> Like <code>warn()</code>, but with source information taken from <i>node</i>.</p>
<dt><code>doc2path(docname, base=True, suffix=None)</code></p>
<dd> Return the filename for the document name. </p>
<p> If <i>base</i> is True, return absolute path under self.srcdir. If <i>base</i> is None, return relative path to self.srcdir. If <i>base</i> is a path string, return absolute path under that. If <i>suffix</i> is not None, add it instead of config.source_suffix.</p>
<dt><code>relfn2path(filename, docname=None)</code></p>
<dd> Return paths to a file referenced from a document, relative to documentation root and absolute. </p>
<p> In the input &quot;filename&quot;, absolute filenames are taken as relative to the source dir, while relative filenames are relative to the dir of the containing document.</p>
<dt><code>note_dependency(filename)</code></p>
<dd> Add <i>filename</i> as a dependency of the current document. </p>
<p> This means that the document will be rebuilt if this file changes. </p>
<p> <i>filename</i> should be absolute or relative to the source directory.</p>
<dt><code>new_serialno(category=&#8221;)</code></p>
<dd> Return a serial number, e.g. for index entry targets. </p>
<p> The number is guaranteed to be unique in the current document.</p>
<dt><code>note_reread()</code></p>
<dd> Add the current document to the list of documents that will automatically be re-read at the next build.</dl>
<h3>Builder API</h3>
<h3>Todo</h3>
<p> Expand this.</p>
<dl>
<dt><code>class sphinx.builders.Builder</code></p>
<dd> This is the base class for all builders. </p>
<p> These methods are predefined and will be called from the application:</p>
<dt><code>get_relative_uri(from_, to, typ=None)</code></p>
<dd> Return a relative URI between two source filenames. </p>
<p> May raise environment.NoUri if there&#8217;s no way to return a sensible URI.</p>
<dt><code>build_all()</code></p>
<dd> Build all source files.</p>
<dt><code>build_specific(filenames)</code></p>
<dd> Only rebuild as much as needed for changes in the <i>filenames</i>.</p>
<dt><code>build_update()</code></p>
<dd> Only rebuild what was changed or added since last build.</p>
<dt><code>build(docnames, summary=None, method=&#8217;update&#8217;)</code></p>
<dd> Main build method. </p>
<p> First updates the environment, and then calls <code>write()</code>. </p>
<p> These methods can be overridden in concrete builder classes:</p>
<dt><code>init()</code></p>
<dd> Load necessary templates and perform initialization. The default implementation does nothing.</p>
<dt><code>get_outdated_docs()</code></p>
<dd> Return an iterable of output files that are outdated, or a string describing what an update build will build. </p>
<p> If the builder does not output individual files corresponding to source files, return a string here. If it does, return an iterable of those files that need to be written.</p>
<dt><code>get_target_uri(docname, typ=None)</code></p>
<dd> Return the target URI for a document name. </p>
<p> <i>typ</i> can be used to qualify the link characteristic for individual builders.</p>
<dt><code>prepare_writing(docnames)</code></p>
<dd> A place where you can add logic before <code>write_doc()</code> is run</p>
<dt><code>write_doc(docname, doctree)</code></p>
<dd> Where you actually write something to the filesystem.</p>
<dt><code>finish()</code></p>
<dd> Finish the building process. </p>
<p> The default implementation does nothing.</dl>
<h3>Docutils markup API</h3>
<p> This section describes the API for adding ReST markup elements (roles and directives).</p>
<h3>Roles</h3>
<h3>Directives</h3>
<p> Directives are handled by classes derived from <code>docutils.parsers.rst.Directive</code>. They have to be registered by an extension using <code>Sphinx.add_directive()</code> or <code>Sphinx.add_directive_to_domain()</code>.</p>
<dl>
<dt><code>class docutils.parsers.rst.Directive</code></p>
<dd> The markup syntax of the new directive is determined by the follow five class attributes:</p>
<dt><code>required_arguments = 0</code></p>
<dd> Number of required directive arguments.</p>
<dt><code>optional_arguments = 0</code></p>
<dd> Number of optional arguments after the required arguments.</p>
<dt><code>final_argument_whitespace = False</code></p>
<dd> May the final argument contain whitespace?</p>
<dt><code>option_spec = None</code></p>
<dd> Mapping of option names to validator functions. </p>
<p> Option validator functions take a single parameter, the option argument (or <code>None</code> if not given), and should validate it or convert it to the proper form. They raise <code>ValueError</code> or <code>TypeError</code> to indicate failure. </p>
<p> There are several predefined and possibly useful validators in the <code>docutils.parsers.rst.directives</code> module.</p>
<dt><code>has_content = False</code></p>
<dd> May the directive have content? </p>
<p> New directives must implement the <code>run()</code> method:</p>
<dt><code>run()</code></p>
<dd> This method must process the directive arguments, options and content, and return a list of Docutils/Sphinx nodes that will be inserted into the document tree at the point where the directive was encountered. </p>
<p> Instance attributes that are always set on the directive are:</p>
<dt><code>name</code></p>
<dd> The directive name (useful when registering the same directive class under multiple names).</p>
<dt><code>arguments</code></p>
<dd> The arguments given to the directive, as a list.</p>
<dt><code>options</code></p>
<dd> The options given to the directive, as a dictionary mapping option names to validated/converted values.</p>
<dt><code>content</code></p>
<dd> The directive content, if given, as a <code>ViewList</code>.</p>
<dt><code>lineno</code></p>
<dd> The absolute line number on which the directive appeared. This is not always a useful value; use <code>srcline</code> instead.</p>
<dt><code>src</code></p>
<dd> The source file of the directive.</p>
<dt><code>srcline</code></p>
<dd> The line number in the source file on which the directive appeared.</p>
<dt><code>content_offset</code></p>
<dd> Internal offset of the directive content. Used when calling <code>nested_parse</code> (see below).</p>
<dt><code>block_text</code></p>
<dd> The string containing the entire directive.</p>
<dt><code>state</code></p>
<dd>
<dt><code>state_machine</code></p>
<dd> The state and state machine which controls the parsing. Used for <code>nested_parse</code>.</dl>
<h3>ViewLists</h3>
<p> Docutils represents document source lines in a class <code>docutils.statemachine.ViewList</code>. This is a list with extended functionality &#8212; for one, slicing creates views of the original list, and also the list contains information about the source line numbers. </p>
<p> The <code>Directive.content</code> attribute is a ViewList. If you generate content to be parsed as ReST, you have to create a ViewList yourself. Important for content generation are the following points:</p>
<dl>
<dt>&bull;</p>
<dd> The constructor takes a list of strings (lines) and a source (document) name.</p>
<dt>&bull;</p>
<dd> The <code>.append()</code> method takes a line and a source name as well.</dl>
<h3>Parsing directive content as ReST</h3>
<p> Many directives will contain more markup that must be parsed. To do this, use one of the following APIs from the <code>Directive.run()</code> method:</p>
<dl>
<dt>&bull;</p>
<dd> <code>self.state.nested_parse</code></p>
<dt>&bull;</p>
<dd> <code>sphinx.util.nodes.nested_parse_with_titles()</code> &#8212; this allows titles in the parsed content. </p>
<p> Both APIs parse the content into a given node. They are used like this: </p>
<pre>
node = docutils.nodes.paragraph()
# either
nested_parse_with_titles(self.state, self.result, node)
# or
self.state.nested_parse(self.result, 0, node)
</pre>
<p> If you don&#8217;t need the wrapping node, you can use any concrete node type and return <code>node.children</code> from the Directive. </p>
<p> <code>SEE ALSO:</code></p>
<dt><i>Creating directives</i></p>
<dd> HOWTO of the Docutils documentation</dl>
<h3>Domain API</h3>
<dl>
<dt><code>class sphinx.domains.Domain(env)</code></p>
<dd> A Domain is meant to be a group of &quot;object&quot; description directives for objects of a similar nature, and corresponding roles to create references to them. Examples would be Python modules, classes, functions etc., elements of a templating language, Sphinx roles and directives, etc. </p>
<p> Each domain has a separate storage for information about existing objects and how to reference them in <i>self.data</i>, which must be a dictionary. It also must implement several functions that expose the object information in a uniform way to parts of Sphinx that allow the user to reference or search for objects in a domain-agnostic way. </p>
<p> About <i>self.data</i>: since all object and cross-referencing information is stored on a BuildEnvironment instance, the <i>domain.data</i> object is also stored in the <i>env.domaindata</i> dict under the key <i>domain.name</i>. Before the build process starts, every active domain is instantiated and given the environment object; the <i>domaindata</i> dict must then either be nonexistent or a dictionary whose &#8216;version&#8217; key is equal to the domain class&#8217; <code>data_version</code> attribute. Otherwise, <i>IOError</i> is raised and the pickled environment is discarded.</p>
<dt><code>clear_doc(docname)</code></p>
<dd> Remove traces of a document in the domain-specific inventories.</p>
<dt><code>directive(name)</code></p>
<dd> Return a directive adapter class that always gives the registered directive its full name (&#8216;domain:name&#8217;) as <code>self.name</code>.</p>
<dt><code>get_objects()</code></p>
<dd> Return an iterable of &quot;object descriptions&quot;, which are tuples with five items:</p>
<dt>&bull;</p>
<dd> <i>name</i> &#8212; fully qualified name</p>
<dt>&bull;</p>
<dd> <i>dispname</i> &#8212; name to display when searching/linking</p>
<dt>&bull;</p>
<dd> <i>type</i> &#8212; object type, a key in <code>self.object_types</code></p>
<dt>&bull;</p>
<dd> <i>docname</i> &#8212; the document where it is to be found</p>
<dt>&bull;</p>
<dd> <i>anchor</i> &#8212; the anchor name for the object</p>
<dt>&bull;</p>
<dd> <i>priority</i> &#8212; how &quot;important&quot; the object is (determines placement in search results)</p>
<dt>&bull;</p>
<dd> 1: default priority (placed before full-text matches)</p>
<dt>&bull;</p>
<dd> 0: object is important (placed before default-priority objects)</p>
<dt>&bull;</p>
<dd> 2: object is unimportant (placed after full-text matches)</p>
<dt>&bull;</p>
<dd> -1: object should not show up in search at all</p>
<dt><code>get_type_name(type, primary=False)</code></p>
<dd> Return full name for given ObjType.</p>
<dt><code>process_doc(env, docname, document)</code></p>
<dd> Process a document after it is read by the environment.</p>
<dt><code>resolve_xref(env, fromdocname, builder, typ, target, node, contnode)</code></p>
<dd> Resolve the pending_xref <i>node</i> with the given <i>typ</i> and <i>target</i>. </p>
<p> This method should return a new node, to replace the xref node, containing the <i>contnode</i> which is the markup content of the cross-reference. </p>
<p> If no resolution can be found, None can be returned; the xref node will then given to the &#8216;missing-reference&#8217; event, and if that yields no resolution, replaced by <i>contnode</i>. </p>
<p> The method can also raise <code>sphinx.environment.NoUri</code> to suppress the &#8216;missing-reference&#8217; event being emitted.</p>
<dt><code>role(name)</code></p>
<dd> Return a role adapter function that always gives the registered role its full name (&#8216;domain:name&#8217;) as the first argument.</p>
<dt><code>dangling_warnings = {}</code></p>
<dd> role name -&gt; a warning message if reference is missing</p>
<dt><code>data_version = 0</code></p>
<dd> data version, bump this when the format of <i>self.data</i> changes</p>
<dt><code>directives = {}</code></p>
<dd> directive name -&gt; directive class</p>
<dt><code>indices = []</code></p>
<dd> a list of Index subclasses</p>
<dt><code>initial_data = {}</code></p>
<dd> data value for a fresh environment</p>
<dt><code>label = &#8221;</code></p>
<dd> domain label: longer, more descriptive (used in messages)</p>
<dt><code>name = &#8221;</code></p>
<dd> domain name: should be short, but unique</p>
<dt><code>object_types = {}</code></p>
<dd> type (usually directive) name -&gt; ObjType instance</p>
<dt><code>roles = {}</code></p>
<dd> role name -&gt; role callable</p>
<dt><code>class sphinx.domains.ObjType(lname, *roles, **attrs)</code></p>
<dd> An ObjType is the description for a type of object that a domain can document. In the object_types attribute of Domain subclasses, object type names are mapped to instances of this class. </p>
<p> Constructor arguments:</p>
<dt>&bull;</p>
<dd> <i>lname</i>: localized name of the type (do not include domain name)</p>
<dt>&bull;</p>
<dd> <i>roles</i>: all the roles that can refer to an object of this type</p>
<dt>&bull;</p>
<dd> <i>attrs</i>: object attributes &#8212; currently only &quot;searchprio&quot; is known, which defines the object&#8217;s priority in the full-text search index, see <code>Domain.get_objects()</code>.</p>
<dt><code>class sphinx.domains.Index(domain)</code></p>
<dd> An Index is the description for a domain-specific index. To add an index to a domain, subclass Index, overriding the three name attributes:</p>
<dt>&bull;</p>
<dd> <i>name</i> is an identifier used for generating file names.</p>
<dt>&bull;</p>
<dd> <i>localname</i> is the section title for the index.</p>
<dt>&bull;</p>
<dd> <i>shortname</i> is a short name for the index, for use in the relation bar in HTML output. Can be empty to disable entries in the relation bar. </p>
<p> and providing a <code>generate()</code> method. Then, add the index class to your domain&#8217;s <i>indices</i> list. Extensions can add indices to existing domains using <code>add_index_to_domain()</code>.</p>
<dt><code>generate(docnames=None)</code></p>
<dd> Return entries for the index given by <i>name</i>. If <i>docnames</i> is given, restrict to entries referring to these docnames. </p>
<p> The return value is a tuple of <code>(content, collapse)</code>, where <i>collapse</i> is a boolean that determines if sub-entries should start collapsed (for output formats that support collapsing sub-entries). </p>
<p> <i>content</i> is a sequence of <code>(letter, entries)</code> tuples, where <i>letter</i> is the &quot;heading&quot; for the given <i>entries</i>, usually the starting letter. </p>
<p> <i>entries</i> is a sequence of single entries, where a single entry is a sequence <code>[name, subtype, docname, anchor, extra, qualifier, descr]</code>. The items in this sequence have the following meaning:</p>
<dt>&bull;</p>
<dd> <i>name</i> &#8212; the name of the index entry to be displayed</p>
<dt>&bull;</p>
<dd> <i>subtype</i> &#8212; sub-entry related type: 0 &#8212; normal entry 1 &#8212; entry with sub-entries 2 &#8212; sub-entry</p>
<dt>&bull;</p>
<dd> <i>docname</i> &#8212; docname where the entry is located</p>
<dt>&bull;</p>
<dd> <i>anchor</i> &#8212; anchor for the entry within <i>docname</i></p>
<dt>&bull;</p>
<dd> <i>extra</i> &#8212; extra info for the entry</p>
<dt>&bull;</p>
<dd> <i>qualifier</i> &#8212; qualifier for the description</p>
<dt>&bull;</p>
<dd> <i>descr</i> &#8212; description for the entry </p>
<p> Qualifier and description are not rendered e.g. in LaTeX output.</dl>
<h3>Doctree node classes added by Sphinx</h3>
<h3>Nodes for domain-specific object descriptions</h3>
<dl>
<dt><code>class sphinx.addnodes.desc(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for object descriptions. </p>
<p> This node is similar to a &quot;definition list&quot; with one definition. It contains one or more <code>desc_signature</code> and a <code>desc_content</code>.</p>
<dt><code>class sphinx.addnodes.desc_signature(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for object signatures. </p>
<p> The &quot;term&quot; part of the custom Sphinx definition list.</p>
<dt><code>class sphinx.addnodes.desc_addname(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for additional name parts (module name, class name).</p>
<dt><code>class sphinx.addnodes.desc_type(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for return types or object type names.</p>
<dt><code>class sphinx.addnodes.desc_returns(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for a &quot;returns&quot; annotation (a la -&gt; in Python).</p>
<dt><code>class sphinx.addnodes.desc_name(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for the main object name.</p>
<dt><code>class sphinx.addnodes.desc_parameterlist(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for a general parameter list.</p>
<dt><code>class sphinx.addnodes.desc_parameter(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for a single parameter.</p>
<dt><code>class sphinx.addnodes.desc_optional(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for marking optional parts of the parameter list.</p>
<dt><code>class sphinx.addnodes.desc_annotation(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for signature annotations (not Python 3-style annotations).</p>
<dt><code>class sphinx.addnodes.desc_content(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for object description content. </p>
<p> This is the &quot;definition&quot; part of the custom Sphinx definition list.</dl>
<h3>New admonition-like constructs</h3>
<dl>
<dt><code>class sphinx.addnodes.versionmodified(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for version change entries. </p>
<p> Currently used for &quot;versionadded&quot;, &quot;versionchanged&quot; and &quot;deprecated&quot; directives.</p>
<dt><code>class sphinx.addnodes.seealso(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Custom &quot;see also&quot; admonition.</dl>
<h3>Other paragraph-level nodes</h3>
<dl>
<dt><code>class sphinx.addnodes.compact_paragraph(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for a compact paragraph (which never makes a &lt;p&gt; node).</dl>
<h3>New inline nodes</h3>
<dl>
<dt><code>class sphinx.addnodes.index(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for index entries. </p>
<p> This node is created by the <code>index</code> directive and has one attribute, <code>entries</code>. Its value is a list of 4-tuples of <code>(entrytype, entryname, target, ignored)</code>. </p>
<p> <i>entrytype</i> is one of &quot;single&quot;, &quot;pair&quot;, &quot;double&quot;, &quot;triple&quot;.</p>
<dt><code>class sphinx.addnodes.pending_xref(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for cross-references that cannot be resolved without complete information about all documents. </p>
<p> These nodes are resolved before writing output, in BuildEnvironment.resolve_references.</p>
<dt><code>class sphinx.addnodes.literal_emphasis(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node that behaves like <i>emphasis</i>, but further text processors are not applied (e.g. smartypants for HTML output).</p>
<dt><code>class sphinx.addnodes.abbreviation(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for abbreviations with explanations.</p>
<dt><code>class sphinx.addnodes.download_reference(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for download references, similar to pending_xref.</dl>
<h3>Special nodes</h3>
<dl>
<dt><code>class sphinx.addnodes.only(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for &quot;only&quot; directives (conditional inclusion based on tags).</p>
<dt><code>class sphinx.addnodes.meta(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for meta directive &#8212; same as docutils&#8217; standard meta node, but pickleable.</p>
<dt><code>class sphinx.addnodes.highlightlang(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Inserted to set the highlight language and line number options for subsequent code blocks. </p>
<p> You should not need to generate the nodes below in extensions.</p>
<dt><code>class sphinx.addnodes.glossary(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node to insert a glossary.</p>
<dt><code>class sphinx.addnodes.toctree(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for inserting a &quot;TOC tree&quot;.</p>
<dt><code>class sphinx.addnodes.start_of_file(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node to mark start of a new file, used in the LaTeX builder only.</p>
<dt><code>class sphinx.addnodes.productionlist(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Node for grammar production lists. </p>
<p> Contains <code>production</code> nodes.</p>
<dt><code>class sphinx.addnodes.production(rawsource=&#8221;, text=&#8221;, *children, **attributes)</code></p>
<dd> Node for a single grammar production rule.</p>
<dt><code>class sphinx.addnodes.termsep(rawsource=&#8221;, *children, **attributes)</code></p>
<dd> Separates two terms within a &lt;term&gt; node.</dl>
<h2>SPHINX WEB SUPPORT</h2>
<p> New in version 1.1. </p>
<p> Sphinx provides a Python API to easily integrate Sphinx documentation into your web application. To learn more read the <i>websupportquickstart</i>.</p>
<h3>Web Support Quick Start</h3>
<h3>Building Documentation Data</h3>
<p> To make use of the web support package in your application you&#8217;ll need to build the data it uses. This data includes pickle files representing documents, search indices, and node data that is used to track where comments and other things are in a document. To do this you will need to create an instance of the <code>WebSupport</code> class and call its <code>build()</code> method: </p>
<pre>
from sphinx.websupport import WebSupport
support = WebSupport(srcdir='/path/to/rst/sources/',
                     builddir='/path/to/build/outdir',
                     search='xapian')
support.build()
</pre>
<p> This will read reStructuredText sources from <i>srcdir</i> and place the necessary data in <i>builddir</i>. The <i>builddir</i> will contain two sub-directories: one named &quot;data&quot; that contains all the data needed to display documents, search through documents, and add comments to documents. The other directory will be called &quot;static&quot; and contains static files that should be served from &quot;/static&quot;. </p>
<p> <code>NOTE:</code> If you wish to serve static files from a path other than &quot;/static&quot;, you can do so by providing the <i>staticdir</i> keyword argument when creating the <code>WebSupport</code> object.</p>
<h3>Integrating Sphinx Documents Into Your Webapp</h3>
<p> Now that the data is built, it&#8217;s time to do something useful with it. Start off by creating a <code>WebSupport</code> object for your application: </p>
<pre>
from sphinx.websupport import WebSupport
support = WebSupport(datadir='/path/to/the/data',
                     search='xapian')
</pre>
<p> You&#8217;ll only need one of these for each set of documentation you will be working with. You can then call it&#8217;s <code>get_document()</code> method to access individual documents: </p>
<pre>
contents = support.get_document('contents')
</pre>
<p> This will return a dictionary containing the following items:</p>
<dl>
<dt>&bull;</p>
<dd> <code>body</code>: The main body of the document as HTML</p>
<dt>&bull;</p>
<dd> <code>sidebar</code>: The sidebar of the document as HTML</p>
<dt>&bull;</p>
<dd> <code>relbar</code>: A div containing links to related documents</p>
<dt>&bull;</p>
<dd> <code>title</code>: The title of the document</p>
<dt>&bull;</p>
<dd> <code>css</code>: Links to css files used by Sphinx</p>
<dt>&bull;</p>
<dd> <code>js</code>: Javascript containing comment options </p>
<p> This dict can then be used as context for templates. The goal is to be easy to integrate with your existing templating system. An example using <i>Jinja2</i> is: </p>
<pre>
{%- extends &quot;layout.html&quot; %}
{%- block title %}
    &#123;&#123; document.title }}
{%- endblock %}
{% block css %}
    &#123;&#123; super() }}
    &#123;&#123; document.css|safe }}
    &lt;link rel=&quot;stylesheet&quot; href=&quot;/static/websupport-custom.css&quot; type=&quot;text/css&quot;&gt;
{% endblock %}
{%- block js %}
    &#123;&#123; super() }}
    &#123;&#123; document.js|safe }}
{%- endblock %}
{%- block relbar %}
    &#123;&#123; document.relbar|safe }}
{%- endblock %}
{%- block body %}
    &#123;&#123; document.body|safe }}
{%- endblock %}
{%- block sidebar %}
    &#123;&#123; document.sidebar|safe }}
{%- endblock %}
</pre>
</dl>
<h3>Authentication</h3>
<p> To use certain features such as voting, it must be possible to authenticate users. The details of the authentication are left to your application. Once a user has been authenticated you can pass the user&#8217;s details to certain <code>WebSupport</code> methods using the <i>username</i> and <i>moderator</i> keyword arguments. The web support package will store the username with comments and votes. The only caveat is that if you allow users to change their username you must update the websupport package&#8217;s data: </p>
<pre>
support.update_username(old_username, new_username)
</pre>
<p> <i>username</i> should be a unique string which identifies a user, and <i>moderator</i> should be a boolean representing whether the user has moderation privilieges. The default value for <i>moderator</i> is <i>False</i>. </p>
<p> An example <i>Flask</i> function that checks whether a user is logged in and then retrieves a document is: </p>
<pre>
from sphinx.websupport.errors import *
@app.route('/&lt;path:docname&gt;')
def doc(docname):
    username = g.user.name if g.user else ''
    moderator = g.user.moderator if g.user else False
    try:
        document = support.get_document(docname, username, moderator)
    except DocumentNotFoundError:
        abort(404)
    return render_template('doc.html', document=document)
</pre>
<p> The first thing to notice is that the <i>docname</i> is just the request path. This makes accessing the correct document easy from a single view. If the user is authenticated, then the username and moderation status are passed along with the docname to <code>get_document()</code>. The web support package will then add this data to the <code>COMMENT_OPTIONS</code> that are used in the template. </p>
<p> <code>NOTE:</code> This only works works if your documentation is served from your document root. If it is served from another directory, you will need to prefix the url route with that directory, and give the <i>docroot</i> keyword argument when creating the web support object: </p>
<pre>
support = WebSupport(..., docroot='docs')
@app.route('/docs/&lt;path:docname&gt;')
</pre>
<h3>Performing Searches</h3>
<p> To use the search form built-in to the Sphinx sidebar, create a function to handle requests to the url &#8216;search&#8217; relative to the documentation root. The user&#8217;s search query will be in the GET parameters, with the key <i>q</i>. Then use the <code>get_search_results()</code> method to retrieve search results. In <i>Flask</i> that would be like this: </p>
<pre>
@app.route('/search')
def search():
    q = request.args.get('q')
    document = support.get_search_results(q)
    return render_template('doc.html', document=document)
</pre>
<p> Note that we used the same template to render our search results as we did to render our documents. That&#8217;s because <code>get_search_results()</code> returns a context dict in the same format that <code>get_document()</code> does.</p>
<h3>Comments &amp; Proposals</h3>
<p> Now that this is done it&#8217;s time to define the functions that handle the AJAX calls from the script. You will need three functions. The first function is used to add a new comment, and will call the web support method <code>add_comment()</code>: </p>
<pre>
@app.route('/docs/add_comment', methods=['POST'])
def add_comment():
    parent_id = request.form.get('parent', '')
    node_id = request.form.get('node', '')
    text = request.form.get('text', '')
    proposal = request.form.get('proposal', '')
    username = g.user.name if g.user is not None else 'Anonymous'
    comment = support.add_comment(text, node_id='node_id',
                                  parent_id='parent_id',
                                  username=username, proposal=proposal)
    return jsonify(comment=comment)
</pre>
<p> You&#8217;ll notice that both a <i>parent_id</i> and <i>node_id</i> are sent with the request. If the comment is being attached directly to a node, <i>parent_id</i> will be empty. If the comment is a child of another comment, then <i>node_id</i> will be empty. Then next function handles the retrieval of comments for a specific node, and is aptly named <code>get_data()</code>: </p>
<pre>
@app.route('/docs/get_comments')
def get_comments():
    username = g.user.name if g.user else None
    moderator = g.user.moderator if g.user else False
    node_id = request.args.get('node', '')
    data = support.get_data(node_id, username, moderator)
    return jsonify(**data)
</pre>
<p> The final function that is needed will call <code>process_vote()</code>, and will handle user votes on comments: </p>
<pre>
@app.route('/docs/process_vote', methods=['POST'])
def process_vote():
    if g.user is None:
        abort(401)
    comment_id = request.form.get('comment_id')
    value = request.form.get('value')
    if value is None or comment_id is None:
        abort(400)
    support.process_vote(comment_id, g.user.id, value)
    return &quot;success&quot;
</pre>
<h3>Comment Moderation</h3>
<p> By default, all comments added through <code>add_comment()</code> are automatically displayed. If you wish to have some form of moderation, you can pass the <i>displayed</i> keyword argument: </p>
<pre>
comment = support.add_comment(text, node_id='node_id',
                              parent_id='parent_id',
                              username=username, proposal=proposal,
                              displayed=False)
</pre>
<p> You can then create a new view to handle the moderation of comments. It will be called when a moderator decides a comment should be accepted and displayed: </p>
<pre>
@app.route('/docs/accept_comment', methods=['POST'])
def accept_comment():
    moderator = g.user.moderator if g.user else False
    comment_id = request.form.get('id')
    support.accept_comment(comment_id, moderator=moderator)
    return 'OK'
</pre>
<p> Rejecting comments happens via comment deletion. </p>
<p> To perform a custom action (such as emailing a moderator) when a new comment is added but not displayed, you can pass callable to the <code>WebSupport</code> class when instantiating your support object: </p>
<pre>
def moderation_callback(comment):
    &quot;&quot;&quot;Do something...&quot;&quot;&quot;
support = WebSupport(..., moderation_callback=moderation_callback)
</pre>
<p> The moderation callback must take one argument, which will be the same comment dict that is returned by <code>add_comment()</code>.</p>
<h3>The WebSupport Class</h3>
<dl>
<dt><code>class sphinx.websupport.WebSupport</code></p>
<dd> The main API class for the web support package. All interactions with the web support package should occur through this class. </p>
<p> The class takes the following keyword arguments:</p>
<dt><code>srcdir</code></p>
<dd> The directory containing reStructuredText source files.</p>
<dt><code>builddir</code></p>
<dd> The directory that build data and static files should be placed in. This should be used when creating a <code>WebSupport</code> object that will be used to build data.</p>
<dt><code>datadir</code></p>
<dd> The directory that the web support data is in. This should be used when creating a <code>WebSupport</code> object that will be used to retrieve data.</p>
<dt><code>search</code></p>
<dd> This may contain either a string (e.g. &#8216;xapian&#8217;) referencing a built-in search adapter to use, or an instance of a subclass of <code>BaseSearch</code>.</p>
<dt><code>storage</code></p>
<dd> This may contain either a string representing a database uri, or an instance of a subclass of <code>StorageBackend</code>. If this is not provided, a new sqlite database will be created.</p>
<dt><code>moderation_callback</code></p>
<dd> A callable to be called when a new comment is added that is not displayed. It must accept one argument: a dictionary representing the comment that was added.</p>
<dt><code>staticdir</code></p>
<dd> If static files are served from a location besides <code>&#8216;/static&#8217;</code>, this should be a string with the name of that location (e.g. <code>&#8216;/static_files&#8217;</code>).</p>
<dt><code>docroot</code></p>
<dd> If the documentation is not served from the base path of a URL, this should be a string specifying that path (e.g. <code>&#8216;docs&#8217;</code>).</dl>
<h3>Methods</h3>
<dl>
<dt><code>WebSupport.build()</code></p>
<dd> Build the documentation. Places the data into the <i>outdir</i> directory. Use it like this: </p>
<pre>
support = WebSupport(srcdir, builddir, search='xapian')
support.build()
</pre>
<p> This will read reStructured text files from <i>srcdir</i>. Then it will build the pickles and search index, placing them into <i>builddir</i>. It will also save node data to the database.</p>
<dt><code>WebSupport.get_document(docname, username=&#8221;, moderator=False)</code></p>
<dd> Load and return a document from a pickle. The document will be a dict object which can be used to render a template: </p>
<pre>
support = WebSupport(datadir=datadir)
support.get_document('index', username, moderator)
</pre>
<p> In most cases <i>docname</i> will be taken from the request path and passed directly to this function. In Flask, that would be something like this: </p>
<pre>
@app.route('/&lt;path:docname&gt;')
def index(docname):
    username = g.user.name if g.user else ''
    moderator = g.user.moderator if g.user else False
    try:
        document = support.get_document(docname, username,
                                        moderator)
    except DocumentNotFoundError:
        abort(404)
    render_template('doc.html', document=document)
</pre>
<p> The document dict that is returned contains the following items to be used during template rendering.</p>
<dt>&bull;</p>
<dd> <code>body</code>: The main body of the document as HTML</p>
<dt>&bull;</p>
<dd> <code>sidebar</code>: The sidebar of the document as HTML</p>
<dt>&bull;</p>
<dd> <code>relbar</code>: A div containing links to related documents</p>
<dt>&bull;</p>
<dd> <code>title</code>: The title of the document</p>
<dt>&bull;</p>
<dd> <code>css</code>: Links to css files used by Sphinx</p>
<dt>&bull;</p>
<dd> <code>script</code>: Javascript containing comment options </p>
<p> This raises <code>DocumentNotFoundError</code> if a document matching <i>docname</i> is not found.</p>
<dt><code>Parameters</code></p>
<dd> <code>docname</code> &#8212; the name of the document to load.</p>
<dt><code>WebSupport.get_data(node_id, username=None, moderator=False)</code></p>
<dd> Get the comments and source associated with <i>node_id</i>. If <i>username</i> is given vote information will be included with the returned comments. The default CommentBackend returns a dict with two keys, <i>source</i>, and <i>comments</i>. <i>source</i> is raw source of the node and is used as the starting point for proposals a user can add. <i>comments</i> is a list of dicts that represent a comment, each having the following items: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Key </td>
<td> Contents
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> text </td>
<td> The comment text.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> username </td>
<td> The username that was stored with the comment.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> id </td>
<td> The comment&#8217;s unique identifier.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> rating </td>
<td> The comment&#8217;s current rating.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> age </td>
<td> The time in seconds since the comment was added.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> A dict containing time information. It contains the following keys: year, month, day, hour, minute, second, iso, and delta. <i>iso</i> is the time formatted in ISO 8601 format. <i>delta</i> is a printable form of how old the comment is (e.g. &quot;3 hours ago&quot;).
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> vote </td>
<td> If <i>user_id</i> was given, this will be an integer representing the vote. 1 for an upvote, -1 for a downvote, or 0 if unvoted.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> node </td>
<td> The id of the node that the comment is attached to. If the comment&#8217;s parent is another comment rather than a node, this will be null.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> parent </td>
<td> The id of the comment that this comment is attached to if it is not attached to a node.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> children </td>
<td> A list of all children, in this format.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> proposal_diff </td>
<td> An HTML representation of the differences between the the current source and the user&#8217;s proposed source.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>node_id</code> &#8212; the id of the node to get comments for.</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; the username of the user viewing the comments.</p>
<dt>&bull;</p>
<dd> <code>moderator</code> &#8212; whether the user is a moderator.</p>
<dt><code>WebSupport.add_comment(text, node_id=&#8221;, parent_id=&#8221;, displayed=True, username=None, time=None, proposal=None, moderator=False)</code></p>
<dd> Add a comment to a node or another comment. Returns the comment in the same format as <code>get_comments()</code>. If the comment is being attached to a node, pass in the node&#8217;s id (as a string) with the node keyword argument: </p>
<pre>
comment = support.add_comment(text, node_id=node_id)
</pre>
<p> If the comment is the child of another comment, provide the parent&#8217;s id (as a string) with the parent keyword argument: </p>
<pre>
comment = support.add_comment(text, parent_id=parent_id)
</pre>
<p> If you would like to store a username with the comment, pass in the optional <i>username</i> keyword argument: </p>
<pre>
comment = support.add_comment(text, node=node_id,
                              username=username)
</pre>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>parent_id</code> &#8212; the prefixed id of the comment&#8217;s parent.</p>
<dt>&bull;</p>
<dd> <code>text</code> &#8212; the text of the comment.</p>
<dt>&bull;</p>
<dd> <code>displayed</code> &#8212; for moderation purposes</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; the username of the user making the comment.</p>
<dt>&bull;</p>
<dd> <code>time</code> &#8212; the time the comment was created, defaults to now.</p>
<dt><code>WebSupport.process_vote(comment_id, username, value)</code></p>
<dd> Process a user&#8217;s vote. The web support package relies on the API user to perform authentication. The API user will typically receive a comment_id and value from a form, and then make sure the user is authenticated. A unique username must be passed in, which will also be used to retrieve the user&#8217;s past voting data. An example, once again in Flask: </p>
<pre>
@app.route('/docs/process_vote', methods=['POST'])
def process_vote():
    if g.user is None:
        abort(401)
    comment_id = request.form.get('comment_id')
    value = request.form.get('value')
    if value is None or comment_id is None:
        abort(400)
    support.process_vote(comment_id, g.user.name, value)
    return &quot;success&quot;
</pre>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>comment_id</code> &#8212; the comment being voted on</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; the unique username of the user voting</p>
<dt>&bull;</p>
<dd> <code>value</code> &#8212; 1 for an upvote, -1 for a downvote, 0 for an unvote.</p>
<dt><code>WebSupport.get_search_results(q)</code></p>
<dd> Perform a search for the query <i>q</i>, and create a set of search results. Then render the search results as html and return a context dict like the one created by <code>get_document()</code>: </p>
<pre>
document = support.get_search_results(q)
</pre>
<dt><code>Parameters</code></p>
<dd> <code>q</code> &#8212; the search query</dl>
<h3>Search Adapters</h3>
<p> To create a custom search adapter you will need to subclass the <code>BaseSearch</code> class. Then create an instance of the new class and pass that as the <i>search</i> keyword argument when you create the <code>WebSupport</code> object: </p>
<pre>
support = WebSupport(srcdir=srcdir,
                     builddir=builddir,
                     search=MySearch())
</pre>
<p> For more information about creating a custom search adapter, please see the documentation of the <code>BaseSearch</code> class below.</p>
<dl>
<dt><code>class sphinx.websupport.search.BaseSearch</code></p>
<dd> Defines an interface for search adapters.</dl>
<h3>BaseSearch Methods</h3>
<p> The following methods are defined in the BaseSearch class. Some methods do not need to be overridden, but some (<code>add_document()</code> and <code>handle_query()</code>) must be overridden in your subclass. For a working example, look at the built-in adapter for whoosh.</p>
<dl>
<dt><code>BaseSearch.init_indexing(changed=[])</code></p>
<dd> Called by the builder to initialize the search indexer. <i>changed</i> is a list of pagenames that will be reindexed. You may want to remove these from the search index before indexing begins.</p>
<dt><code>Parameters</code></p>
<dd> <code>changed</code> &#8212; a list of pagenames that will be re-indexed</p>
<dt><code>BaseSearch.finish_indexing()</code></p>
<dd> Called by the builder when writing has been completed. Use this to perform any finalization or cleanup actions after indexing is complete.</p>
<dt><code>BaseSearch.feed(pagename, title, doctree)</code></p>
<dd> Called by the builder to add a doctree to the index. Converts the <i>doctree</i> to text and passes it to <code>add_document()</code>. You probably won&#8217;t want to override this unless you need access to the <i>doctree</i>. Override <code>add_document()</code> instead.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>pagename</code> &#8212; the name of the page to be indexed</p>
<dt>&bull;</p>
<dd> <code>title</code> &#8212; the title of the page to be indexed</p>
<dt>&bull;</p>
<dd> <code>doctree</code> &#8212; is the docutils doctree representation of the page</p>
<dt><code>BaseSearch.add_document(pagename, title, text)</code></p>
<dd> Called by <code>feed()</code> to add a document to the search index. This method should should do everything necessary to add a single document to the search index. </p>
<p> <i>pagename</i> is name of the page being indexed. It is the combination of the source files relative path and filename, minus the extension. For example, if the source file is &quot;ext/builders.rst&quot;, the <i>pagename</i> would be &quot;ext/builders&quot;. This will need to be returned with search results when processing a query.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>pagename</code> &#8212; the name of the page being indexed</p>
<dt>&bull;</p>
<dd> <code>title</code> &#8212; the page&#8217;s title</p>
<dt>&bull;</p>
<dd> <code>text</code> &#8212; the full text of the page</p>
<dt><code>BaseSearch.query(q)</code></p>
<dd> Called by the web support api to get search results. This method compiles the regular expression to be used when <code>extracting context</code>, then calls <code>handle_query()</code>. You won&#8217;t want to override this unless you don&#8217;t want to use the included <code>extract_context()</code> method. Override <code>handle_query()</code> instead.</p>
<dt><code>Parameters</code></p>
<dd> <code>q</code> &#8212; the search query string.</p>
<dt><code>BaseSearch.handle_query(q)</code></p>
<dd> Called by <code>query()</code> to retrieve search results for a search query <i>q</i>. This should return an iterable containing tuples of the following format: </p>
<pre>
(&lt;path&gt;, &lt;title&gt;, &lt;context&gt;)
</pre>
<p> <i>path</i> and <i>title</i> are the same values that were passed to <code>add_document()</code>, and <i>context</i> should be a short text snippet of the text surrounding the search query in the document. </p>
<p> The <code>extract_context()</code> method is provided as a simple way to create the <i>context</i>.</p>
<dt><code>Parameters</code></p>
<dd> <code>q</code> &#8212; the search query</p>
<dt><code>BaseSearch.extract_context(text, length=240)</code></p>
<dd> Extract the context for the search query from the document&#8217;s full <i>text</i>.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>text</code> &#8212; the full text of the document to create the context for</p>
<dt>&bull;</p>
<dd> <code>length</code> &#8212; the length of the context snippet to return.</dl>
<h3>Storage Backends</h3>
<p> To create a custom storage backend you will need to subclass the <code>StorageBackend</code> class. Then create an instance of the new class and pass that as the <i>storage</i> keyword argument when you create the <code>WebSupport</code> object: </p>
<pre>
support = WebSupport(srcdir=srcdir,
                     builddir=builddir,
                     storage=MyStorage())
</pre>
<p> For more information about creating a custom storage backend, please see the documentation of the <code>StorageBackend</code> class below.</p>
<dl>
<dt><code>class sphinx.websupport.storage.StorageBackend</code></p>
<dd> Defines an interface for storage backends.</dl>
<h3>StorageBackend Methods</h3>
<dl>
<dt><code>StorageBackend.pre_build()</code></p>
<dd> Called immediately before the build process begins. Use this to prepare the StorageBackend for the addition of nodes.</p>
<dt><code>StorageBackend.add_node(id, document, source)</code></p>
<dd> Add a node to the StorageBackend.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>id</code> &#8212; a unique id for the comment.</p>
<dt>&bull;</p>
<dd> <code>document</code> &#8212; the name of the document the node belongs to.</p>
<dt>&bull;</p>
<dd> <code>source</code> &#8212; the source files name.</p>
<dt><code>StorageBackend.post_build()</code></p>
<dd> Called after a build has completed. Use this to finalize the addition of nodes if needed.</p>
<dt><code>StorageBackend.add_comment(text, displayed, username, time, proposal, node_id, parent_id, moderator)</code></p>
<dd> Called when a comment is being added.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>text</code> &#8212; the text of the comment</p>
<dt>&bull;</p>
<dd> <code>displayed</code> &#8212; whether the comment should be displayed</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; the name of the user adding the comment</p>
<dt>&bull;</p>
<dd> <code>time</code> &#8212; a date object with the time the comment was added</p>
<dt>&bull;</p>
<dd> <code>proposal</code> &#8212; the text of the proposal the user made</p>
<dt>&bull;</p>
<dd> <code>node_id</code> &#8212; the id of the node that the comment is being added to</p>
<dt>&bull;</p>
<dd> <code>parent_id</code> &#8212; the id of the comment&#8217;s parent comment.</p>
<dt>&bull;</p>
<dd> <code>moderator</code> &#8212; whether the user adding the comment is a moderator</p>
<dt><code>StorageBackend.delete_comment(comment_id, username, moderator)</code></p>
<dd> Delete a comment. </p>
<p> Raises <code>UserNotAuthorizedError</code> if moderator is False and <i>username</i> doesn&#8217;t match the username on the comment.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>comment_id</code> &#8212; The id of the comment being deleted.</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; The username of the user requesting the deletion.</p>
<dt>&bull;</p>
<dd> <code>moderator</code> &#8212; Whether the user is a moderator.</p>
<dt><code>StorageBackend.get_data(node_id, username, moderator)</code></p>
<dd> Called to retrieve all data for a node. This should return a dict with two keys, <i>source</i> and <i>comments</i> as described by <code>WebSupport</code>&#8216;s <code>get_data()</code> method.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>node_id</code> &#8212; The id of the node to get data for.</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; The name of the user requesting the data.</p>
<dt>&bull;</p>
<dd> <code>moderator</code> &#8212; Whether the requestor is a moderator.</p>
<dt><code>StorageBackend.process_vote(comment_id, username, value)</code></p>
<dd> Process a vote that is being cast. <i>value</i> will be either -1, 0, or 1.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>comment_id</code> &#8212; The id of the comment being voted on.</p>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; The username of the user casting the vote.</p>
<dt>&bull;</p>
<dd> <code>value</code> &#8212; The value of the vote being cast.</p>
<dt><code>StorageBackend.update_username(old_username, new_username)</code></p>
<dd> If a user is allowed to change their username this method should be called so that there is not stagnate data in the storage system.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>old_username</code> &#8212; The username being changed.</p>
<dt>&bull;</p>
<dd> <code>new_username</code> &#8212; What the username is being changed to.</p>
<dt><code>StorageBackend.accept_comment(comment_id)</code></p>
<dd> Called when a moderator accepts a comment. After the method is called the comment should be displayed to all users.</p>
<dt><code>Parameters</code></p>
<dd> <code>comment_id</code> &#8212; The id of the comment being accepted.</dl>
<h2>SPHINX FAQ</h2>
<p> This is a list of Frequently Asked Questions about Sphinx. Feel free to suggest new entries!</p>
<h3>How do I&#8230;</h3>
<dl>
<dt><code>&#8230; create PDF files without LaTeX?</code></p>
<dd> You can use <i>rst2pdf</i> version 0.12 or greater which comes with built-in Sphinx integration. See the <i>builders</i> section for details.</p>
<dt><code>&#8230; get section numbers?</code></p>
<dd> They are automatic in LaTeX output; for HTML, give a <code>:numbered:</code> option to the <code>toctree</code> directive where you want to start numbering.</p>
<dt><code>&#8230; customize the look of the built HTML files?</code></p>
<dd> Use themes, see <code>theming</code>.</p>
<dt><code>&#8230; add global substitutions or includes?</code></p>
<dd> Add them in the <code>rst_epilog</code> config value.</p>
<dt><code>&#8230; display the whole TOC tree in the sidebar?</code></p>
<dd> Use the <code>toctree</code> callable in a custom layout template, probably in the <code>sidebartoc</code> block.</p>
<dt><code>&#8230; write my own extension?</code></p>
<dd> See the <i>extension tutorial</i>.</p>
<dt><code>&#8230; convert from my existing docs using MoinMoin markup?</code></p>
<dd> The easiest way is to convert to xhtml, then convert <i>xhtml to reST</i>. You&#8217;ll still need to mark up classes and such, but the headings and code examples come through cleanly.</p>
<dt><code>&#8230; create HTML slides from Sphinx documents?</code></p>
<dd> See the &quot;Hieroglyph&quot; package at <i><a rel="nofollow" href="https://github.com/nyergler/hieroglyph">https://github.com/nyergler/hieroglyph</a></i>. </p>
<p> For many more extensions and other contributed stuff, see the <i>sphinx-contrib</i> repository.</dl>
<h3>Using Sphinx with&#8230;</h3>
<dl>
<dt><code>Read the Docs</code></p>
<dd> <i><a rel="nofollow" href="https://readthedocs.org">https://readthedocs.org</a></i> is a documentation hosting service based around Sphinx. They will host sphinx documentation, along with supporting a number of other features including version support, PDF generation, and more. The <i>Getting Started</i> guide is a good place to start.</p>
<dt><code>Epydoc</code></p>
<dd> There&#8217;s a third-party extension providing an <i>api role</i> which refers to Epydoc&#8217;s API docs for a given identifier.</p>
<dt><code>Doxygen</code></p>
<dd> Michael Jones is developing a reST/Sphinx bridge to doxygen called <i>breathe</i>.</p>
<dt><code>SCons</code></p>
<dd> Glenn Hutchings has written a SCons build script to build Sphinx documentation; it is hosted here: <i><a rel="nofollow" href="https://bitbucket.org/zondo/sphinx-scons">https://bitbucket.org/zondo/sphinx-scons</a></i></p>
<dt><code>PyPI</code></p>
<dd> Jannis Leidel wrote a <i>setuptools command</i> that automatically uploads Sphinx documentation to the PyPI package documentation area at <i><a rel="nofollow" href="http://pythonhosted.org/">http://pythonhosted.org/</a></i>.</p>
<dt><code>GitHub Pages</code></p>
<dd> Directories starting with underscores are ignored by default which breaks static files in Sphinx. GitHub&#8217;s preprocessor can be <i>disabled</i> to support Sphinx HTML output properly.</p>
<dt><code>MediaWiki</code></p>
<dd> See <i><a rel="nofollow" href="https://bitbucket.org/kevindunn/sphinx-wiki">https://bitbucket.org/kevindunn/sphinx-wiki</a></i>, a project by Kevin Dunn.</p>
<dt><code>Google Analytics</code></p>
<dd> You can use a custom <code>layout.html</code> template, like this: </p>
<pre>
{% extends &quot;!layout.html&quot; %}
{%- block extrahead %}
&#123;&#123; super() }}
&lt;script type=&quot;text/javascript&quot;&gt;
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'XXX account number XXX']);
  _gaq.push(['_trackPageview']);
&lt;/script&gt;
{% endblock %}
{% block footer %}
&#123;&#123; super() }}
&lt;div class=&quot;footer&quot;&gt;This page uses &lt;a href=&quot;<a rel="nofollow" href="http://analytics.google.com/">http://analytics.google.com/</a>&quot;&gt;
Google Analytics&lt;/a&gt; to collect statistics. You can disable it by blocking
the JavaScript coming from <a rel="nofollow" href="http://www.google-analytics.com">www.google-analytics.com</a>.
&lt;script type=&quot;text/javascript&quot;&gt;
  (function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ?
              '<a rel="nofollow" href="https://ssl'">https://ssl'</a> : '<a href="http://www')">http://www')</a> + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
  })();
&lt;/script&gt;
&lt;/div&gt;
{% endblock %}
</pre>
</dl>
<h3>Epub info</h3>
<p> The following list gives some hints for the creation of epub files:</p>
<dl>
<dt>&bull;</p>
<dd> Split the text into several files. The longer the individual HTML files are, the longer it takes the ebook reader to render them. In extreme cases, the rendering can take up to one minute.</p>
<dt>&bull;</p>
<dd> Try to minimize the markup. This also pays in rendering time.</p>
<dt>&bull;</p>
<dd> For some readers you can use embedded or external fonts using the CSS <code>@font-face</code> directive. This is <i>extremely</i> useful for code listings which are often cut at the right margin. The default Courier font (or variant) is quite wide and you can only display up to 60 characters on a line. If you replace it with a narrower font, you can get more characters on a line. You may even use <i>FontForge</i> and create narrow variants of some free font. In my case I get up to 70 characters on a line. </p>
<p> You may have to experiment a little until you get reasonable results.</p>
<dt>&bull;</p>
<dd> Test the created epubs. You can use several alternatives. The ones I am aware of are <i>Epubcheck</i>, <i>Calibre</i>, <i>FBreader</i> (although it does not render the CSS), and <i>Bookworm</i>. For bookworm you can download the source from <i><a rel="nofollow" href="http://code.google.com/p/threepress/">http://code.google.com/p/threepress/</a></i> and run your own local server.</p>
<dt>&bull;</p>
<dd> Large floating divs are not displayed properly. If they cover more than one page, the div is only shown on the first page. In that case you can copy the <code>epub.css</code> from the <code>sphinx/themes/epub/static/</code> directory to your local <code>_static/</code> directory and remove the float settings.</p>
<dt>&bull;</p>
<dd> Files that are inserted outside of the <code>toctree</code> directive must be manually included. This sometimes applies to appendixes, e.g. the glossary or the indices. You can add them with the <code>epub_post_files</code> option.</p>
<dt>&bull;</p>
<dd> The handling of the epub cover page differs from the reStructuredText procedure which automatically resolves image paths and puts the images into the <code>_images</code> directory. For the epub cover page put the image in the <code>html_static_path</code> directory and reference it with its full path in the <code>epub_cover</code> config option.</dl>
<h3>Texinfo info</h3>
<p> There are two main programs for reading Info files, <code>info</code> and GNU Emacs. The <code>info</code> program has less features but is available in most Unix environments and can be quickly accessed from the terminal. Emacs provides better font and color display and supports extensive customization (of course).</p>
<h3>Displaying Links</h3>
<p> One noticeable problem you may encounter with the generated Info files is how references are displayed. If you read the source of an Info file, a reference to this section would look like: </p>
<pre>
* note Displaying Links: target-id
</pre>
<p> In the stand-alone reader, <code>info</code>, references are displayed just as they appear in the source. Emacs, on the other-hand, will by default replace <code>*note:</code> with <code>see</code> and hide the <code>target-id</code>. For example: <i>texinfo-links</i> </p>
<p> The exact behavior of how Emacs displays references is dependent on the variable <code>Info-hide-note-references</code>. If set to the value of <code>hide</code>, Emacs will hide both the <code>*note:</code> part and the <code>target-id</code>. This is generally the best way to view Sphinx-based documents since they often make frequent use of links and do not take this limitation into account. However, changing this variable affects how all Info documents are displayed and most due take this behavior into account. </p>
<p> If you want Emacs to display Info files produced by Sphinx using the value <code>hide</code> for <code>Info-hide-note-references</code> and the default value for all other Info files, try adding the following Emacs Lisp code to your start-up file, <code>~/.emacs.d/init.el</code>. </p>
<pre>
(defadvice info-insert-file-contents (after
                                      sphinx-info-insert-file-contents
                                      activate)
  &quot;Hack to make `Info-hide-note-references' buffer-local and
automatically set to `hide' iff it can be determined that this file
was created from a Texinfo file generated by Docutils or Sphinx.&quot;
  (set (make-local-variable 'Info-hide-note-references)
       (default-value 'Info-hide-note-references))
  (save-excursion
    (save-restriction
      (widen) (goto-char (point-min))
      (when (re-search-forward
             &quot;^Generated by \(Sphinx\|Docutils\)&quot;
             (save-excursion (search-forward &quot;&quot; nil t)) t)
        (set (make-local-variable 'Info-hide-note-references)
             'hide)))))
</pre>
<h3>Notes</h3>
<p> The following notes may be helpful if you want to create Texinfo files:</p>
<dl>
<dt>&bull;</p>
<dd> Each section corresponds to a different <code>node</code> in the Info file.</p>
<dt>&bull;</p>
<dd> Colons (<code>:</code>) cannot be properly escaped in menu entries and xrefs. They will be replaced with semicolons (<code>;</code>).</p>
<dt>&bull;</p>
<dd> Links to external Info files can be created using the somewhat official URI scheme <code>info</code>. For example: </p>
<pre>
info:Texinfo#makeinfo_options
</pre>
<p> which produces: <i>info:Texinfo#makeinfo_options</i></p>
<dt>&bull;</p>
<dd> Inline markup </p>
<p> The standard formatting for <code>*strong*</code> and <code>_emphasis_</code> can result in ambiguous output when used to markup parameter names and other values. Since this is a fairly common practice, the default formatting has been changed so that <code>emphasis</code> and <code>strong</code> are now displayed like <code>`literal&#8217;</code>s. </p>
<p> The standard formatting can be re-enabled by adding the following to your <code>conf.py</code>: </p>
<pre>
texinfo_elements = {'preamble': &quot;&quot;&quot;
@definfoenclose strong,*,*
@definfoenclose emph,_,_
&quot;&quot;&quot;}
</pre>
</dl>
<h2>GLOSSARY</h2>
<dl>
<dt><code>builder</code></p>
<dd> A class (inheriting from <code>Builder</code>) that takes parsed documents and performs an action on them. Normally, builders translate the documents to an output format, but it is also possible to use the builder builders that e.g. check for broken links in the documentation, or build coverage information. </p>
<p> See <i>builders</i> for an overview over Sphinx&#8217; built-in builders.</p>
<dt><code>configuration directory</code></p>
<dd> The directory containing <code>conf.py</code>. By default, this is the same as the <i>source directory</i>, but can be set differently with the <code>-c</code> command-line option.</p>
<dt><code>directive</code></p>
<dd> A reStructuredText markup element that allows marking a block of content with special meaning. Directives are supplied not only by docutils, but Sphinx and custom extensions can add their own. The basic directive syntax looks like this: </p>
<pre>
.. directivename:: argument ...
   :option: value
   Content of the directive.
</pre>
<p> See <i>directives</i> for more information.</p>
<dt><code>document name</code></p>
<dd> Since reST source files can have different extensions (some people like <code>.txt</code>, some like <code>.rst</code> &#8212; the extension can be configured with <code>source_suffix</code>) and different OSes have different path separators, Sphinx abstracts them: <i>document names</i> are always relative to the <i>source directory</i>, the extension is stripped, and path separators are converted to slashes. All values, parameters and such referring to &quot;documents&quot; expect such document names. </p>
<p> Examples for document names are <code>index</code>, <code>library/zipfile</code>, or <code>reference/datamodel/types</code>. Note that there is no leading or trailing slash.</p>
<dt><code>domain</code></p>
<dd> A domain is a collection of markup (reStructuredText <i>directive</i>s and <i>role</i>s) to describe and link to <i>object</i>s belonging together, e.g. elements of a programming language. Directive and role names in a domain have names like <code>domain:name</code>, e.g. <code>py:function</code>. </p>
<p> Having domains means that there are no naming problems when one set of documentation wants to refer to e.g. C++ and Python classes. It also means that extensions that support the documentation of whole new languages are much easier to write. For more information about domains, see the chapter <i>domains</i>.</p>
<dt><code>environment</code></p>
<dd> A structure where information about all documents under the root is saved, and used for cross-referencing. The environment is pickled after the parsing stage, so that successive runs only need to read and parse new and changed documents.</p>
<dt><code>master document</code></p>
<dd> The document that contains the root <code>toctree</code> directive.</p>
<dt><code>object</code></p>
<dd> The basic building block of Sphinx documentation. Every &quot;object directive&quot; (e.g. <code>function</code> or <code>object</code>) creates such a block; and most objects can be cross-referenced to.</p>
<dt><code>role</code></p>
<dd> A reStructuredText markup element that allows marking a piece of text. Like directives, roles are extensible. The basic syntax looks like this: <code>:rolename:`content`</code>. See <i>inlinemarkup</i> for details.</p>
<dt><code>source directory</code></p>
<dd> The directory which, including its subdirectories, contains all source files for one Sphinx project.</dl>
<h2>SPHINX DEVELOPER&#8217;S GUIDE</h2>
<h3>Abstract</h3>
<p> This document describes the development process of Sphinx, a documentation system used by developers to document systems used by other developers to develop other systems that may also be documented using Sphinx. </p>
<p> The Sphinx source code is managed using <i>Mercurial</i> and is hosted on <i>BitBucket</i>. hg clone <i><a rel="nofollow" href="https://bitbucket.org/birkenfeld/sphinx">https://bitbucket.org/birkenfeld/sphinx</a></i> Community.INDENT 0.0</p>
<dl>
<dt><code>sphinx-users &lt;</code><i>sphinx-users [at] googlegroups.com</i>&gt;</p>
<dd> Mailing list for user support.</p>
<dt><code>sphinx-dev &lt;</code><i>sphinx-dev [at] googlegroups.com</i>&gt;</p>
<dd> Mailing list for development related discussions.</p>
<dt><code>#sphinx-doc on irc.freenode.net</code></p>
<dd> IRC channel for development questions and user support.</dl>
<h3>Bug Reports and Feature Requests</h3>
<p> If you have encountered a problem with Sphinx or have an idea for a new feature, please submit it to the <i>issue tracker</i> on BitBucket or discuss it on the sphinx-dev mailing list. </p>
<p> For bug reports, please include the output produced during the build process and also the log file Sphinx creates after it encounters an un-handled exception. The location of this file should be shown towards the end of the error message. </p>
<p> Including or providing a link to the source files involved may help us fix the issue. If possible, try to create a minimal project that produces the error and post that instead.</p>
<h3>Contributing to Sphinx</h3>
<p> The recommended way for new contributors to submit code to Sphinx is to fork the Mercurial repository on BitBucket and then submit a pull request after committing the changes. The pull request will then need to be approved by one of the core developers before it is merged into the main repository.</p>
<h3>Getting Started</h3>
<p> These are the basic steps needed to start developing on Sphinx.</p>
<dl>
<dt>1.</p>
<dd> Create an account on BitBucket.</p>
<dt>2.</p>
<dd> Fork the main Sphinx repository (<i>birkenfeld/sphinx</i>) using the BitBucket interface.</p>
<dt>3.</p>
<dd> Clone the forked repository to your machine. </p>
<pre>
hg clone <a rel="nofollow" href="https://bitbucket.org/USERNAME/sphinx-fork">https://bitbucket.org/USERNAME/sphinx-fork</a>
cd sphinx-fork
</pre>
<dt>4.</p>
<dd> Checkout the appropriate branch. </p>
<p> For changes that should be included in the next minor release (namely bug fixes), use the <code>stable</code> branch. </p>
<pre>
hg checkout stable
</pre>
<p> For new features or other substantial changes that should wait until the next major release, use the <code>default</code> branch.</p>
<dt>5.</p>
<dd> Optional: setup a virtual environment. </p>
<pre>
virtualenv ~/sphinxenv
. ~/sphinxenv/bin/activate
pip install -e .
</pre>
<dt>6.</p>
<dd> Hack, hack, hack. </p>
<p> For tips on working with the code, see the <i>Coding Guide</i>.</p>
<dt>7.</p>
<dd> Test, test, test. Possible steps:</p>
<dt>&bull;</p>
<dd> Run the unit tests: </p>
<pre>
pip install nose mock
make test
</pre>
<dt>&bull;</p>
<dd> Build the documentation and check the output for different builders: </p>
<pre>
cd doc
make clean html latexpdf
</pre>
<dt>&bull;</p>
<dd> Run the unit tests under different Python environments using <code>tox</code>: </p>
<pre>
pip install tox
tox -v
</pre>
<dt>&bull;</p>
<dd> Add a new unit test in the <code>tests</code> directory if you can.</p>
<dt>&bull;</p>
<dd> For bug fixes, first add a test that fails without your changes and passes after they are applied.</p>
<dt>8.</p>
<dd> Please add a bullet point to <code>CHANGES</code> if the fix or feature is not trivial (small doc updates, typo fixes). Then commit: </p>
<pre>
hg commit -m '#42: Add useful new feature that does this.'
</pre>
<p> BitBucket recognizes <i>certain phrases</i> that can be used to automatically update the issue tracker. </p>
<p> For example: </p>
<pre>
hg commit -m 'Closes #42: Fix invalid markup in docstring of Foo.bar.'
</pre>
<p> would close issue #42.</p>
<dt>9.</p>
<dd> Push changes to your forked repository on BitBucket. </p>
<pre>
hg push
</pre>
<dt>10.</p>
<dd> Submit a pull request from your repository to <code>birkenfeld/sphinx</code> using the BitBucket interface.</p>
<dt>11.</p>
<dd> Wait for a core developer to review your changes.</dl>
<h3>Core Developers</h3>
<p> The core developers of Sphinx have write access to the main repository. They can commit changes, accept/reject pull requests, and manage items on the issue tracker. </p>
<p> You do not need to be a core developer or have write access to be involved in the development of Sphinx. You can submit patches or create pull requests from forked repositories and have a core developer add the changes for you. </p>
<p> The following are some general guidelines for core developers:</p>
<dl>
<dt>&bull;</p>
<dd> Questionable or extensive changes should be submitted as a pull request instead of being committed directly to the main repository. The pull request should be reviewed by another core developer before it is merged.</p>
<dt>&bull;</p>
<dd> Trivial changes can be committed directly but be sure to keep the repository in a good working state and that all tests pass before pushing your changes.</p>
<dt>&bull;</p>
<dd> When committing code written by someone else, please attribute the original author in the commit message and any relevant <code>CHANGES</code> entry.</p>
<dt>&bull;</p>
<dd> Using Mercurial named branches other than <code>default</code> and <code>stable</code> is not encouraged.</dl>
<h3>Locale updates</h3>
<p> The parts of messages in Sphinx that go into builds are translated into several locales. The translations are kept as gettext <code>.po</code> files translated from the master template <code>sphinx/locale/sphinx.pot</code>. </p>
<p> Sphinx uses <i>Babel</i> to extract messages and maintain the catalog files. It is integrated in <code>setup.py</code>:</p>
<dl>
<dt>&bull;</p>
<dd> Use <code>python setup.py extract_messages</code> to update the <code>.pot</code> template.</p>
<dt>&bull;</p>
<dd> Use <code>python setup.py update_catalog</code> to update all existing language catalogs in <code>sphinx/locale/*/LC_MESSAGES</code> with the current messages in the template file.</p>
<dt>&bull;</p>
<dd> Use <code>python setup.py compile_catalog</code> to compile the <code>.po</code> files to binary <code>.mo</code> files and <code>.js</code> files. </p>
<p> When an updated <code>.po</code> file is submitted, run compile_catalog to commit both the source and the compiled catalogs. </p>
<p> When a new locale is submitted, add a new directory with the ISO 639-1 language identifier and put <code>sphinx.po</code> in there. Don&#8217;t forget to update the possible values for <code>language</code> in <code>doc/config.rst</code>. </p>
<p> The Sphinx core messages can also be translated on <i>Transifex</i>. There exists a client tool named <code>tx</code> in the Python package &quot;transifex_client&quot;, which can be used to pull translations in <code>.po</code> format from Transifex. To do this, go to <code>sphinx/locale</code> and then run <code>tx pull -f -l LANG</code> where LANG is an existing language identifier. It is good practice to run <code>python setup.py update_catalog</code> afterwards to make sure the <code>.po</code> file has the canonical Babel formatting.</dl>
<h3>Coding Guide</h3>
<dl>
<dt>&bull;</p>
<dd> Try to use the same code style as used in the rest of the project. See the <i>Pocoo Styleguide</i> for more information.</p>
<dt>&bull;</p>
<dd> For non-trivial changes, please update the <code>CHANGES</code> file. If your changes alter existing behavior, please document this.</p>
<dt>&bull;</p>
<dd> New features should be documented. Include examples and use cases where appropriate. If possible, include a sample that is displayed in the generated output.</p>
<dt>&bull;</p>
<dd> When adding a new configuration variable, be sure to document it and update <code>sphinx/quickstart.py</code> if it&#8217;s important enough.</p>
<dt>&bull;</p>
<dd> Use the included <code>utils/check_sources.py</code> script to check for common formatting issues (trailing whitespace, lengthy lines, etc).</p>
<dt>&bull;</p>
<dd> Add appropriate unit tests.</dl>
<h3>Debugging Tips</h3>
<dl>
<dt>&bull;</p>
<dd> Delete the build cache before building documents if you make changes in the code by running the command <code>make clean</code> or using the <i>sphinx-build -E</i> option.</p>
<dt>&bull;</p>
<dd> Use the <i>sphinx-build -P</i> option to run Pdb on exceptions.</p>
<dt>&bull;</p>
<dd> Use <code>node.pformat()</code> and <code>node.asdom().toxml()</code> to generate a printable representation of the document structure.</p>
<dt>&bull;</p>
<dd> Set the configuration variable <code>keep_warnings</code> to True so warnings will be displayed in the generated output.</p>
<dt>&bull;</p>
<dd> Set the configuration variable <code>nitpicky</code> to True so that Sphinx will complain about references without a known target.</p>
<dt>&bull;</p>
<dd> Set the debugging options in the <i>Docutils configuration file</i>.</dl>
<h2>CHANGES IN SPHINX</h2>
<h3>Release 1.2.3 (released Sep 1, 2014)</h3>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> #1518: <i>sphinx-apidoc</i> command now have a <i>&#8211;version</i> option to show version information and exit</p>
<dt>&bull;</p>
<dd> New locales: Hebrew, European Portuguese, Vietnamese.</dl>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> #636: Keep straight single quotes in literal blocks in the LaTeX build.</p>
<dt>&bull;</p>
<dd> #1419: Generated i18n sphinx.js files are missing message catalog entries from &#8216;.js_t&#8217; and &#8216;.html&#8217;. The issue was introduced from Sphinx-1.1</p>
<dt>&bull;</p>
<dd> #1363: Fix i18n: missing python domain&#8217;s cross-references with currentmodule directive or currentclass directive.</p>
<dt>&bull;</p>
<dd> #1444: autosummary does not create the description from attributes docstring.</p>
<dt>&bull;</p>
<dd> #1457: In python3 environment, make linkcheck cause &quot;Can&#8217;t convert &#8216;bytes&#8217; object to str implicitly&quot; error when link target url has a hash part. Thanks to Jorge_C.</p>
<dt>&bull;</p>
<dd> #1467: Exception on Python3 if nonexistent method is specified by automethod</p>
<dt>&bull;</p>
<dd> #1441: autosummary can&#8217;t handle nested classes correctly.</p>
<dt>&bull;</p>
<dd> #1499: With non-callable <i>setup</i> in a conf.py, now sphinx-build emits user-friendly error message.</p>
<dt>&bull;</p>
<dd> #1502: In autodoc, fix display of parameter defaults containing backslashes.</p>
<dt>&bull;</p>
<dd> #1226: autodoc, autosummary: importing setup.py by automodule will invoke setup process and execute <i>sys.exit()</i>. Now sphinx avoids SystemExit exception and emits warnings without unexpected termination.</p>
<dt>&bull;</p>
<dd> #1503: py:function directive generate incorrectly signature when specifying a default parameter with an empty list <i>[]</i>. Thanks to Geert Jansen.</p>
<dt>&bull;</p>
<dd> #1508: Non-ASCII filename raise exception on make singlehtml, latex, man, texinfo and changes.</p>
<dt>&bull;</p>
<dd> #1531: On Python3 environment, docutils.conf with &#8216;source_link=true&#8217; in the general section cause type error.</p>
<dt>&bull;</p>
<dd> PR#270, #1533: Non-ASCII docstring cause UnicodeDecodeError when uses with inheritance-diagram directive. Thanks to WAKAYAMA shirou.</p>
<dt>&bull;</p>
<dd> PR#281, PR#282, #1509: TODO extension not compatible with websupport. Thanks to Takeshi Komiya.</p>
<dt>&bull;</p>
<dd> #1477: gettext does not extract nodes.line in a table or list.</p>
<dt>&bull;</p>
<dd> #1544: <i>make text</i> generate wrong table when it has empty table cells.</p>
<dt>&bull;</p>
<dd> #1522: Footnotes from table get displayed twice in LaTeX. This problem has been appeared from Sphinx-1.2.1 by #949.</p>
<dt>&bull;</p>
<dd> #508: Sphinx every time exit with zero when is invoked from setup.py command. ex. <i>python setup.py build_sphinx -b doctest</i> return zero even if doctest failed.</dl>
<h3>Release 1.2.2 (released Mar 2, 2014)</h3>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> PR#211: When checking for existence of the <code>html_logo</code> file, check the full relative path and not the basename.</p>
<dt>&bull;</p>
<dd> PR#212: Fix traceback with autodoc and <code>__init__</code> methods without docstring.</p>
<dt>&bull;</p>
<dd> PR#213: Fix a missing import in the setup command.</p>
<dt>&bull;</p>
<dd> #1357: Option names documented by <code>option</code> are now again allowed to not start with a dash or slash, and referencing them will work correctly.</p>
<dt>&bull;</p>
<dd> #1358: Fix handling of image paths outside of the source directory when using the &quot;wildcard&quot; style reference.</p>
<dt>&bull;</p>
<dd> #1374: Fix for autosummary generating overly-long summaries if first line doesn&#8217;t end with a period.</p>
<dt>&bull;</p>
<dd> #1383: Fix Python 2.5 compatibility of sphinx-apidoc.</p>
<dt>&bull;</p>
<dd> #1391: Actually prevent using &quot;pngmath&quot; and &quot;mathjax&quot; extensions at the same time in sphinx-quickstart.</p>
<dt>&bull;</p>
<dd> #1386: Fix bug preventing more than one theme being added by the entry point mechanism.</p>
<dt>&bull;</p>
<dd> #1370: Ignore &quot;toctree&quot; nodes in text writer, instead of raising.</p>
<dt>&bull;</p>
<dd> #1364: Fix &#8216;make gettext&#8217; fails when the &#8216;.. todolist::&#8217; directive is present.</p>
<dt>&bull;</p>
<dd> #1367: Fix a change of PR#96 that break sphinx.util.docfields.Field.make_field interface/behavior for <i>item</i> argument usage.</dl>
<h3>Documentation</h3>
<dl>
<dt>&bull;</p>
<dd> Extended the <i>documentation about building extensions</i>.</dl>
<h3>Release 1.2.1 (released Jan 19, 2014)</h3>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> #1335: Fix autosummary template overloading with exclamation prefix like <code>{% extends &quot;!autosummary/class.rst&quot; %}</code> cause infinite recursive function call. This was caused by PR#181.</p>
<dt>&bull;</p>
<dd> #1337: Fix autodoc with <code>autoclass_content=&quot;both&quot;</code> uses useless <code>object.__init__</code> docstring when class does not have <code>__init__</code>. This was caused by a change for #1138.</p>
<dt>&bull;</p>
<dd> #1340: Can&#8217;t search alphabetical words on the HTML quick search generated with language=&#8217;ja&#8217;.</p>
<dt>&bull;</p>
<dd> #1319: Do not crash if the <code>html_logo</code> file does not exist.</p>
<dt>&bull;</p>
<dd> #603: Do not use the HTML-ized title for building the search index (that resulted in &quot;literal&quot; being found on every page with a literal in the title).</p>
<dt>&bull;</p>
<dd> #751: Allow production lists longer than a page in LaTeX by using longtable.</p>
<dt>&bull;</p>
<dd> #764: Always look for stopwords lowercased in JS search.</p>
<dt>&bull;</p>
<dd> #814: autodoc: Guard against strange type objects that don&#8217;t have <code>__bases__</code>.</p>
<dt>&bull;</p>
<dd> #932: autodoc: Do not crash if <code>__doc__</code> is not a string.</p>
<dt>&bull;</p>
<dd> #933: Do not crash if an <code>option</code> value is malformed (contains spaces but no option name).</p>
<dt>&bull;</p>
<dd> #908: On Python 3, handle error messages from LaTeX correctly in the pngmath extension.</p>
<dt>&bull;</p>
<dd> #943: In autosummary, recognize &quot;first sentences&quot; to pull from the docstring if they contain uppercase letters.</p>
<dt>&bull;</p>
<dd> #923: Take the entire LaTeX document into account when caching pngmath-generated images. This rebuilds them correctly when <code>pngmath_latex_preamble</code> changes.</p>
<dt>&bull;</p>
<dd> #901: Emit a warning when using docutils&#8217; new &quot;math&quot; markup without a Sphinx math extension active.</p>
<dt>&bull;</p>
<dd> #845: In code blocks, when the selected lexer fails, display line numbers nevertheless if configured.</p>
<dt>&bull;</p>
<dd> #929: Support parsed-literal blocks in LaTeX output correctly.</p>
<dt>&bull;</p>
<dd> #949: Update the tabulary.sty packed with Sphinx.</p>
<dt>&bull;</p>
<dd> #1050: Add anonymous labels into <code>objects.inv</code> to be referenced via <code>intersphinx</code>.</p>
<dt>&bull;</p>
<dd> #1095: Fix print-media stylesheet being included always in the &quot;scrolls&quot; theme.</p>
<dt>&bull;</p>
<dd> #1085: Fix current classname not getting set if class description has <code>:noindex:</code> set.</p>
<dt>&bull;</p>
<dd> #1181: Report option errors in autodoc directives more gracefully.</p>
<dt>&bull;</p>
<dd> #1155: Fix autodocumenting C-defined methods as attributes in Python 3.</p>
<dt>&bull;</p>
<dd> #1233: Allow finding both Python classes and exceptions with the &quot;class&quot; and &quot;exc&quot; roles in intersphinx.</p>
<dt>&bull;</p>
<dd> #1198: Allow &quot;image&quot; for the &quot;figwidth&quot; option of the <code>figure</code> directive as documented by docutils.</p>
<dt>&bull;</p>
<dd> #1152: Fix pycode parsing errors of Python 3 code by including two grammar versions for Python 2 and 3, and loading the appropriate version for the running Python version.</p>
<dt>&bull;</p>
<dd> #1017: Be helpful and tell the user when the argument to <code>option</code> does not match the required format.</p>
<dt>&bull;</p>
<dd> #1345: Fix two bugs with <code>nitpick_ignore</code>; now you don&#8217;t have to remove the store environment for changes to have effect.</p>
<dt>&bull;</p>
<dd> #1072: In the JS search, fix issues searching for upper-cased words by lowercasing words before stemming.</p>
<dt>&bull;</p>
<dd> #1299: Make behavior of the <code>math</code> directive more consistent and avoid producing empty environments in LaTeX output.</p>
<dt>&bull;</p>
<dd> #1308: Strip HTML tags from the content of &quot;raw&quot; nodes before feeding it to the search indexer.</p>
<dt>&bull;</p>
<dd> #1249: Fix duplicate LaTeX page numbering for manual documents.</p>
<dt>&bull;</p>
<dd> #1292: In the linkchecker, retry HEAD requests when denied by HTTP 405. Also make the redirect code apparent and tweak the output a bit to be more obvious.</p>
<dt>&bull;</p>
<dd> #1285: Avoid name clashes between C domain objects and section titles.</p>
<dt>&bull;</p>
<dd> #848: Always take the newest code in incremental rebuilds with the <code>sphinx.ext.viewcode</code> extension.</p>
<dt>&bull;</p>
<dd> #979, #1266: Fix exclude handling in <code>sphinx-apidoc</code>.</p>
<dt>&bull;</p>
<dd> #1302: Fix regression in <code>sphinx.ext.inheritance_diagram</code> when documenting classes that can&#8217;t be pickled.</p>
<dt>&bull;</p>
<dd> #1316: Remove hard-coded <code>font-face</code> resources from epub theme.</p>
<dt>&bull;</p>
<dd> #1329: Fix traceback with empty translation msgstr in .po files.</p>
<dt>&bull;</p>
<dd> #1300: Fix references not working in translated documents in some instances.</p>
<dt>&bull;</p>
<dd> #1283: Fix a bug in the detection of changed files that would try to access doctrees of deleted documents.</p>
<dt>&bull;</p>
<dd> #1330: Fix <code>exclude_patterns</code> behavior with subdirectories in the <code>html_static_path</code>.</p>
<dt>&bull;</p>
<dd> #1323: Fix emitting empty <code>&lt;ul&gt;</code> tags in the HTML writer, which is not valid HTML.</p>
<dt>&bull;</p>
<dd> #1147: Don&#8217;t emit a sidebar search box in the &quot;singlehtml&quot; builder.</dl>
<h3>Documentation</h3>
<dl>
<dt>&bull;</p>
<dd> #1325: Added a &quot;Intersphinx&quot; tutorial section. (<code>doc/tutorial.rst</code>)</dl>
<h3>Release 1.2 (released Dec 10, 2013)</h3>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> Added <code>sphinx.version_info</code> tuple for programmatic checking of the Sphinx version.</dl>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> Removed the <code>sphinx.ext.refcounting</code> extension &#8212; it is very specific to CPython and has no place in the main distribution.</dl>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> Restore <code>versionmodified</code> CSS class for versionadded/changed and deprecated directives.</p>
<dt>&bull;</p>
<dd> PR#181: Fix <i>html_theme_path=[&#8216;.&#8217;]</i> is a trigger of rebuild all documents always (This change keeps the current &quot;theme changes cause a rebuild&quot; feature).</p>
<dt>&bull;</p>
<dd> #1296: Fix invalid charset in HTML help generated HTML files for default locale.</p>
<dt>&bull;</p>
<dd> PR#190: Fix gettext does not extract figure caption and rubric title inside other blocks. Thanks to Michael Schlenker.</p>
<dt>&bull;</p>
<dd> PR#176: Make sure setup_command test can always import Sphinx. Thanks to Dmitry Shachnev.</p>
<dt>&bull;</p>
<dd> #1311: Fix test_linkcode.test_html fails with C locale and Python 3.</p>
<dt>&bull;</p>
<dd> #1269: Fix ResourceWarnings with Python 3.2 or later.</p>
<dt>&bull;</p>
<dd> #1138: Fix: When <code>autodoc_docstring_signature = True</code> and <code>autoclass_content = &#8216;init&#8217;</code> or <code>&#8216;both&#8217;</code>, __init__ line should be removed from class documentation.</dl>
<h3>Release 1.2 beta3 (released Oct 3, 2013)</h3>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> The Sphinx error log files will now include a list of the loaded extensions for help in debugging.</dl>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> PR#154: Remove &quot;sphinx&quot; prefix from LaTeX class name except &#8216;sphinxmanual&#8217; and &#8216;sphinxhowto&#8217;. Now you can use your custom document class without &#8216;sphinx&#8217; prefix. Thanks to Erik B.</dl>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> #1265: Fix i18n: crash when translating a section name that is pointed to from a named target.</p>
<dt>&bull;</p>
<dd> A wrong condition broke the search feature on first page that is usually index.rst. This issue was introduced in 1.2b1.</p>
<dt>&bull;</p>
<dd> #703: When Sphinx can&#8217;t decode filenames with non-ASCII characters, Sphinx now catches UnicodeError and will continue if possible instead of raising the exception.</dl>
<h3>Release 1.2 beta2 (released Sep 17, 2013)</h3>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> <code>apidoc</code> now ignores &quot;_private&quot; modules by default, and has an option <code>-P</code> to include them.</p>
<dt>&bull;</p>
<dd> <code>apidoc</code> now has an option to not generate headings for packages and modules, for the case that the module docstring already includes a reST heading.</p>
<dt>&bull;</p>
<dd> PR#161: <code>apidoc</code> can now write each module to a standalone page instead of combining all modules in a package on one page.</p>
<dt>&bull;</p>
<dd> Builders: rebuild i18n target document when catalog updated.</p>
<dt>&bull;</p>
<dd> Support docutils.conf &#8216;writers&#8217; and &#8216;html4css1 writer&#8217; section in the HTML writer. The latex, manpage and texinfo writers also support their respective &#8216;writers&#8217; sections.</p>
<dt>&bull;</p>
<dd> The new <code>html_extra_path</code> config value allows to specify directories with files that should be copied directly to the HTML output directory.</p>
<dt>&bull;</p>
<dd> Autodoc directives for module data and attributes now support an <code>annotation</code> option, so that the default display of the data/attribute value can be overridden.</p>
<dt>&bull;</p>
<dd> PR#136: Autodoc directives now support an <code>imported-members</code> option to include members imported from different modules.</p>
<dt>&bull;</p>
<dd> New locales: Macedonian, Sinhala, Indonesian.</p>
<dt>&bull;</p>
<dd> Theme package collection by using setuptools plugin mechanism.</dl>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> PR#144, #1182: Force timezone offset to LocalTimeZone on POT-Creation-Date that was generated by gettext builder. Thanks to masklinn and Jakub Wilk.</dl>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> PR#132: Updated jQuery version to 1.8.3.</p>
<dt>&bull;</p>
<dd> PR#141, #982: Avoid crash when writing PNG file using Python 3. Thanks to Marcin Wojdyr.</p>
<dt>&bull;</p>
<dd> PR#145: In parallel builds, sphinx drops second document file to write. Thanks to tychoish.</p>
<dt>&bull;</p>
<dd> PR#151: Some styling updates to tables in LaTeX.</p>
<dt>&bull;</p>
<dd> PR#153: The &quot;extensions&quot; config value can now be overridden.</p>
<dt>&bull;</p>
<dd> PR#155: Added support for some C++11 function qualifiers.</p>
<dt>&bull;</p>
<dd> Fix: &#8216;make gettext&#8217; caused UnicodeDecodeError when templates contain utf-8 encoded strings.</p>
<dt>&bull;</p>
<dd> #828: use inspect.getfullargspec() to be able to document functions with keyword-only arguments on Python 3.</p>
<dt>&bull;</p>
<dd> #1090: Fix i18n: multiple cross references (term, ref, doc) in the same line return the same link.</p>
<dt>&bull;</p>
<dd> #1157: Combination of &#8216;globaltoc.html&#8217; and hidden toctree caused exception.</p>
<dt>&bull;</p>
<dd> #1159: fix wrong generation of objects inventory for Python modules, and add a workaround in intersphinx to fix handling of affected inventories.</p>
<dt>&bull;</p>
<dd> #1160: Citation target missing caused an AssertionError.</p>
<dt>&bull;</p>
<dd> #1162, PR#139: singlehtml builder didn&#8217;t copy images to _images/.</p>
<dt>&bull;</p>
<dd> #1173: Adjust setup.py dependencies because Jinja2 2.7 discontinued compatibility with Python &lt; 3.3 and Python &lt; 2.6. Thanks to Alexander Dupuy.</p>
<dt>&bull;</p>
<dd> #1185: Don&#8217;t crash when a Python module has a wrong or no encoding declared, and non-ASCII characters are included.</p>
<dt>&bull;</p>
<dd> #1188: sphinx-quickstart raises UnicodeEncodeError if &quot;Project version&quot; includes non-ASCII characters.</p>
<dt>&bull;</p>
<dd> #1189: &quot;Title underline is too short&quot; WARNING is given when using fullwidth characters to &quot;Project name&quot; on quickstart.</p>
<dt>&bull;</p>
<dd> #1190: Output TeX/texinfo/man filename has no basename (only extension) when using non-ASCII characters in the &quot;Project name&quot; on quickstart.</p>
<dt>&bull;</p>
<dd> #1192: Fix escaping problem for hyperlinks in the manpage writer.</p>
<dt>&bull;</p>
<dd> #1193: Fix i18n: multiple link references in the same line return the same link.</p>
<dt>&bull;</p>
<dd> #1176: Fix i18n: footnote reference number missing for auto numbered named footnote and auto symbol footnote.</p>
<dt>&bull;</p>
<dd> PR#146,#1172: Fix ZeroDivisionError in parallel builds. Thanks to tychoish.</p>
<dt>&bull;</p>
<dd> #1204: Fix wrong generation of links to local intersphinx targets.</p>
<dt>&bull;</p>
<dd> #1206: Fix i18n: gettext did not translate admonition directive&#8217;s title.</p>
<dt>&bull;</p>
<dd> #1232: Sphinx generated broken ePub files on Windows.</p>
<dt>&bull;</p>
<dd> #1259: Guard the debug output call when emitting events; to prevent the repr() implementation of arbitrary objects causing build failures.</p>
<dt>&bull;</p>
<dd> #1142: Fix NFC/NFD normalizing problem of rst filename on Mac OS X.</p>
<dt>&bull;</p>
<dd> #1234: Ignoring the string consists only of white-space characters.</dl>
<h3>Release 1.2 beta1 (released Mar 31, 2013)</h3>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> Removed <code>sphinx.util.compat.directive_dwim()</code> and <code>sphinx.roles.xfileref_role()</code> which were deprecated since version 1.0.</p>
<dt>&bull;</p>
<dd> PR#122: the files given in <code>latex_additional_files</code> now override TeX files included by Sphinx, such as <code>sphinx.sty</code>.</p>
<dt>&bull;</p>
<dd> PR#124: the node generated by <code>versionadded</code>, <code>versionchanged</code> and <code>deprecated</code> directives now includes all added markup (such as &quot;New in version X&quot;) as child nodes, and no additional text must be generated by writers.</p>
<dt>&bull;</p>
<dd> PR#99: the <code>seealso</code> directive now generates admonition nodes instead of the custom <code>seealso</code> node.</dl>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> Markup</p>
<dt>&bull;</p>
<dd> The <code>toctree</code> directive and the <code>toctree()</code> template function now have an <code>includehidden</code> option that includes hidden toctree entries (bugs #790 and #1047). A bug in the <code>maxdepth</code> option for the <code>toctree()</code> template function has been fixed (bug #1046).</p>
<dt>&bull;</p>
<dd> PR#99: Strip down seealso directives to normal admonitions. This removes their unusual CSS classes (admonition-see-also), inconsistent LaTeX admonition title (&quot;See Also&quot; instead of &quot;See also&quot;), and spurious indentation in the text builder.</p>
<dt>&bull;</p>
<dd> HTML builder</p>
<dt>&bull;</p>
<dd> #783: Create a link to full size image if it is scaled with width or height.</p>
<dt>&bull;</p>
<dd> #1067: Improve the ordering of the JavaScript search results: matches in titles come before matches in full text, and object results are better categorized. Also implement a pluggable search scorer.</p>
<dt>&bull;</p>
<dd> #1053: The &quot;rightsidebar&quot; and &quot;collapsiblesidebar&quot; HTML theme options now work together.</p>
<dt>&bull;</p>
<dd> Update to jQuery 1.7.1 and Underscore.js 1.3.1.</p>
<dt>&bull;</p>
<dd> Texinfo builder</p>
<dt>&bull;</p>
<dd> An &quot;Index&quot; node is no longer added when there are no entries.</p>
<dt>&bull;</p>
<dd> &quot;deffn&quot; categories are no longer capitalized if they contain capital letters.</p>
<dt>&bull;</p>
<dd> <code>desc_annotation</code> nodes are now rendered.</p>
<dt>&bull;</p>
<dd> <code>strong</code> and <code>emphasis</code> nodes are now formatted like <code>literal</code>s. The reason for this is because the standard Texinfo markup (<code>*strong*</code> and <code>_emphasis_</code>) resulted in confusing output due to the common usage of using these constructs for documenting parameter names.</p>
<dt>&bull;</p>
<dd> Field lists formatting has been tweaked to better display &quot;Info field lists&quot;.</p>
<dt>&bull;</p>
<dd> <code>system_message</code> and <code>problematic</code> nodes are now formatted in a similar fashion as done by the text builder.</p>
<dt>&bull;</p>
<dd> &quot;en-dash&quot; and &quot;em-dash&quot; conversion of hyphens is no longer performed in option directive signatures.</p>
<dt>&bull;</p>
<dd> <code>@ref</code> is now used instead of <code>@pxref</code> for cross-references which prevents the word &quot;see&quot; from being added before the link (does not affect the Info output).</p>
<dt>&bull;</p>
<dd> The <code>@finalout</code> command has been added for better TeX output.</p>
<dt>&bull;</p>
<dd> <code>transition</code> nodes are now formatted using underscores (&quot;_&quot;) instead of asterisks (&quot;*&quot;).</p>
<dt>&bull;</p>
<dd> The default value for the <code>paragraphindent</code> has been changed from 2 to 0 meaning that paragraphs are no longer indented by default.</p>
<dt>&bull;</p>
<dd> #1110: A new configuration value <code>texinfo_no_detailmenu</code> has been added for controlling whether a <code>@detailmenu</code> is added in the &quot;Top&quot; node&#8217;s menu.</p>
<dt>&bull;</p>
<dd> Detailed menus are no longer created except for the &quot;Top&quot; node.</p>
<dt>&bull;</p>
<dd> Fixed an issue where duplicate domain indices would result in invalid output.</p>
<dt>&bull;</p>
<dd> LaTeX builder:</p>
<dt>&bull;</p>
<dd> PR#115: Add <code>&#8216;transition&#8217;</code> item in <code>latex_elements</code> for customizing how transitions are displayed. Thanks to Jeff Klukas.</p>
<dt>&bull;</p>
<dd> PR#114: The LaTeX writer now includes the &quot;cmap&quot; package by default. The <code>&#8216;cmappkg&#8217;</code> item in <code>latex_elements</code> can be used to control this. Thanks to Dmitry Shachnev.</p>
<dt>&bull;</p>
<dd> The <code>&#8216;fontpkg&#8217;</code> item in <code>latex_elements</code> now defaults to <code>&#8221;</code> when the <code>language</code> uses the Cyrillic script. Suggested by Dmitry Shachnev.</p>
<dt>&bull;</p>
<dd> The <code>latex_documents</code>, <code>texinfo_documents</code>, and <code>man_pages</code> configuration values will be set to default values based on the <code>master_doc</code> if not explicitly set in <code>conf.py</code>. Previously, if these values were not set, no output would be genereted by their respective builders.</p>
<dt>&bull;</p>
<dd> Internationalization:</p>
<dt>&bull;</p>
<dd> Add i18n capabilities for custom templates. For example: The Sphinx reference documentation in doc directory provides a <code>sphinx.pot</code> file with message strings from <code>doc/_templates/*.html</code> when using <code>make gettext</code>.</p>
<dt>&bull;</p>
<dd> PR#61,#703: Add support for non-ASCII filename handling.</p>
<dt>&bull;</p>
<dd> Other builders:</p>
<dt>&bull;</p>
<dd> Added the Docutils-native XML and pseudo-XML builders. See <code>XMLBuilder</code> and <code>PseudoXMLBuilder</code>.</p>
<dt>&bull;</p>
<dd> PR#45: The linkcheck builder now checks <code>#anchor</code>s for existence.</p>
<dt>&bull;</p>
<dd> PR#123, #1106: Add <code>epub_use_index</code> configuration value. If provided, it will be used instead of <code>html_use_index</code> for epub builder.</p>
<dt>&bull;</p>
<dd> PR#126: Add <code>epub_tocscope</code> configuration value. The setting controls the generation of the epub toc. The user can now also include hidden toc entries.</p>
<dt>&bull;</p>
<dd> PR#112: Add <code>epub_show_urls</code> configuration value.</p>
<dt>&bull;</p>
<dd> Extensions:</p>
<dt>&bull;</p>
<dd> PR#52: <code>special_members</code> flag to autodoc now behaves like <code>members</code>.</p>
<dt>&bull;</p>
<dd> PR#47: Added <code>sphinx.ext.linkcode</code> extension.</p>
<dt>&bull;</p>
<dd> PR#25: In inheritance diagrams, the first line of the class docstring is now the tooltip for the class.</p>
<dt>&bull;</p>
<dd> Command-line interfaces:</p>
<dt>&bull;</p>
<dd> PR#75: Added <code>&#8211;follow-links</code> option to sphinx-apidoc.</p>
<dt>&bull;</p>
<dd> #869: sphinx-build now has the option <i>-T</i> for printing the full traceback after an unhandled exception.</p>
<dt>&bull;</p>
<dd> sphinx-build now supports the standard <i>&#8211;help</i> and <i>&#8211;version</i> options.</p>
<dt>&bull;</p>
<dd> sphinx-build now provides more specific error messages when called with invalid options or arguments.</p>
<dt>&bull;</p>
<dd> sphinx-build now has a verbose option <i>-v</i> which can be repeated for greater effect. A single occurrance provides a slightly more verbose output than normal. Two or more occurrences of this option provides more detailed output which may be useful for debugging.</p>
<dt>&bull;</p>
<dd> Locales:</p>
<dt>&bull;</p>
<dd> PR#74: Fix some Russian translation.</p>
<dt>&bull;</p>
<dd> PR#54: Added Norwegian bokmaal translation.</p>
<dt>&bull;</p>
<dd> PR#35: Added Slovak translation.</p>
<dt>&bull;</p>
<dd> PR#28: Added Hungarian translation.</p>
<dt>&bull;</p>
<dd> #1113: Add Hebrew locale.</p>
<dt>&bull;</p>
<dd> #1097: Add Basque locale.</p>
<dt>&bull;</p>
<dd> #1037: Fix typos in Polish translation. Thanks to Jakub Wilk.</p>
<dt>&bull;</p>
<dd> #1012: Update Estonian translation.</p>
<dt>&bull;</p>
<dd> Optimizations:</p>
<dt>&bull;</p>
<dd> Speed up building the search index by caching the results of the word stemming routines. Saves about 20 seconds when building the Python documentation.</p>
<dt>&bull;</p>
<dd> PR#108: Add experimental support for parallel building with a new <i>-j</i> option.</dl>
<h3>Documentation</h3>
<dl>
<dt>&bull;</p>
<dd> PR#88: Added the &quot;Sphinx Developer&#8217;s Guide&quot; (<code>doc/devguide.rst</code>) which outlines the basic development process of the Sphinx project.</p>
<dt>&bull;</p>
<dd> Added a detailed &quot;Installing Sphinx&quot; document (<code>doc/install.rst</code>).</dl>
<h3>Bugs fixed</h3>
<dl>
<dt>&bull;</p>
<dd> PR#124: Fix paragraphs in versionmodified are ignored when it has no dangling paragraphs. Fix wrong html output (nested <code>&lt;p&gt;</code> tag). Fix versionmodified is not translatable. Thanks to Nozomu Kaneko.</p>
<dt>&bull;</p>
<dd> PR#111: Respect add_autodoc_attrgetter() even when inherited-members is set. Thanks to A. Jesse Jiryu Davis.</p>
<dt>&bull;</p>
<dd> PR#97: Fix footnote handling in translated documents.</p>
<dt>&bull;</p>
<dd> Fix text writer not handling visit_legend for figure directive contents.</p>
<dt>&bull;</p>
<dd> Fix text builder not respecting wide/fullwidth characters: title underline width, table layout width and text wrap width.</p>
<dt>&bull;</p>
<dd> Fix leading space in LaTeX table header cells.</p>
<dt>&bull;</p>
<dd> #1132: Fix LaTeX table output for multi-row cells in the first column.</p>
<dt>&bull;</p>
<dd> #1128: Fix Unicode errors when trying to format time strings with a non-standard locale.</p>
<dt>&bull;</p>
<dd> #1127: Fix traceback when autodoc tries to tokenize a non-Python file.</p>
<dt>&bull;</p>
<dd> #1126: Fix double-hyphen to en-dash conversion in wrong places such as command-line option names in LaTeX.</p>
<dt>&bull;</p>
<dd> #1123: Allow whitespaces in filenames given to <code>literalinclude</code>.</p>
<dt>&bull;</p>
<dd> #1120: Added improvements about i18n for themes &quot;basic&quot;, &quot;haiku&quot; and &quot;scrolls&quot; that Sphinx built-in. Thanks to Leonardo J. Caballero G.</p>
<dt>&bull;</p>
<dd> #1118: Updated Spanish translation. Thanks to Leonardo J. Caballero G.</p>
<dt>&bull;</p>
<dd> #1117: Handle .pyx files in sphinx-apidoc.</p>
<dt>&bull;</p>
<dd> #1112: Avoid duplicate download files when referenced from documents in different ways (absolute/relative).</p>
<dt>&bull;</p>
<dd> #1111: Fix failure to find uppercase words in search when <code>html_search_language</code> is &#8216;ja&#8217;. Thanks to Tomo Saito.</p>
<dt>&bull;</p>
<dd> #1108: The text writer now correctly numbers enumerated lists with non-default start values (based on patch by Ewan Edwards).</p>
<dt>&bull;</p>
<dd> #1102: Support multi-context &quot;with&quot; statements in autodoc.</p>
<dt>&bull;</p>
<dd> #1090: Fix gettext not extracting glossary terms.</p>
<dt>&bull;</p>
<dd> #1074: Add environment version info to the generated search index to avoid compatibility issues with old builds.</p>
<dt>&bull;</p>
<dd> #1070: Avoid un-pickling issues when running Python 3 and the saved environment was created under Python 2.</p>
<dt>&bull;</p>
<dd> #1069: Fixed error caused when autodoc would try to format signatures of &quot;partial&quot; functions without keyword arguments (patch by Artur Gaspar).</p>
<dt>&bull;</p>
<dd> #1062: sphinx.ext.autodoc use __init__ method signature for class signature.</p>
<dt>&bull;</p>
<dd> #1055: Fix web support with relative path to source directory.</p>
<dt>&bull;</p>
<dd> #1043: Fix sphinx-quickstart asking again for yes/no questions because <code>input()</code> returns values with an extra &#8216;r&#8217; on Python 3.2.0 + Windows. Thanks to RÃ©gis DÃ©camps.</p>
<dt>&bull;</p>
<dd> #1041: Fix failure of the cpp domain parser to parse a const type with a modifier.</p>
<dt>&bull;</p>
<dd> #1038: Fix failure of the cpp domain parser to parse C+11 &quot;static constexpr&quot; declarations. Thanks to Jakub Wilk.</p>
<dt>&bull;</p>
<dd> #1029: Fix intersphinx_mapping values not being stable if the mapping has plural key/value set with Python 3.3.</p>
<dt>&bull;</p>
<dd> #1028: Fix line block output in the text builder.</p>
<dt>&bull;</p>
<dd> #1024: Improve Makefile/make.bat error message if Sphinx is not found. Thanks to Anatoly Techtonik.</p>
<dt>&bull;</p>
<dd> #1018: Fix &quot;container&quot; directive handling in the text builder.</p>
<dt>&bull;</p>
<dd> #1015: Stop overriding jQuery contains() in the JavaScript.</p>
<dt>&bull;</p>
<dd> #1010: Make pngmath images transparent by default; IE7+ should handle it.</p>
<dt>&bull;</p>
<dd> #1008: Fix test failures with Python 3.3.</p>
<dt>&bull;</p>
<dd> #995: Fix table-of-contents and page numbering for the LaTeX &quot;howto&quot; class.</p>
<dt>&bull;</p>
<dd> #976: Fix gettext does not extract index entries.</p>
<dt>&bull;</p>
<dd> PR#72: #975: Fix gettext not extracting definition terms before docutils 0.10.</p>
<dt>&bull;</p>
<dd> #961: Fix LaTeX output for triple quotes in code snippets.</p>
<dt>&bull;</p>
<dd> #958: Do not preserve <code>environment.pickle</code> after a failed build.</p>
<dt>&bull;</p>
<dd> #955: Fix i18n transformation.</p>
<dt>&bull;</p>
<dd> #940: Fix gettext does not extract figure caption.</p>
<dt>&bull;</p>
<dd> #920: Fix PIL packaging issue that allowed to import <code>Image</code> without PIL namespace. Thanks to Marc Schlaich.</p>
<dt>&bull;</p>
<dd> #723: Fix the search function on local files in WebKit based browsers.</p>
<dt>&bull;</p>
<dd> #440: Fix coarse timestamp resolution in some filesystem generating a wrong list of outdated files.</dl>
<h3>Release 1.1.3 (Mar 10, 2012)</h3>
<dl>
<dt>&bull;</p>
<dd> PR#40: Fix <code>safe_repr</code> function to decode bytestrings with non-ASCII characters correctly.</p>
<dt>&bull;</p>
<dd> PR#37: Allow configuring sphinx-apidoc via <code>SPHINX_APIDOC_OPTIONS</code>.</p>
<dt>&bull;</p>
<dd> PR#34: Restore Python 2.4 compatibility.</p>
<dt>&bull;</p>
<dd> PR#36: Make the &quot;bibliography to TOC&quot; fix in LaTeX output specific to the document class.</p>
<dt>&bull;</p>
<dd> #695: When the highlight language &quot;python&quot; is specified explicitly, do not try to parse the code to recognize non-Python snippets.</p>
<dt>&bull;</p>
<dd> #859: Fix exception under certain circumstances when not finding appropriate objects to link to.</p>
<dt>&bull;</p>
<dd> #860: Do not crash when encountering invalid doctest examples, just emit a warning.</p>
<dt>&bull;</p>
<dd> #864: Fix crash with some settings of <code>modindex_common_prefix</code>.</p>
<dt>&bull;</p>
<dd> #862: Fix handling of <code>-D</code> and <code>-A</code> options on Python 3.</p>
<dt>&bull;</p>
<dd> #851: Recognize and warn about circular toctrees, instead of running into recursion errors.</p>
<dt>&bull;</p>
<dd> #853: Restore compatibility with docutils trunk.</p>
<dt>&bull;</p>
<dd> #852: Fix HtmlHelp index entry links again.</p>
<dt>&bull;</p>
<dd> #854: Fix inheritance_diagram raising attribute errors on builtins.</p>
<dt>&bull;</p>
<dd> #832: Fix crashes when putting comments or lone terms in a glossary.</p>
<dt>&bull;</p>
<dd> #834, #818: Fix HTML help language/encoding mapping for all Sphinx supported languages.</p>
<dt>&bull;</p>
<dd> #844: Fix crashes when dealing with Unicode output in doctest extension.</p>
<dt>&bull;</p>
<dd> #831: Provide <code>&#8211;project</code> flag in setup_command as advertised.</p>
<dt>&bull;</p>
<dd> #875: Fix reading config files under Python 3.</p>
<dt>&bull;</p>
<dd> #876: Fix quickstart test under Python 3.</p>
<dt>&bull;</p>
<dd> #870: Fix spurious KeyErrors when removing documents.</p>
<dt>&bull;</p>
<dd> #892: Fix single-HTML builder misbehaving with the master document in a subdirectory.</p>
<dt>&bull;</p>
<dd> #873: Fix assertion errors with empty <code>only</code> directives.</p>
<dt>&bull;</p>
<dd> #816: Fix encoding issues in the Qt help builder.</dl>
<h3>Release 1.1.2 (Nov 1, 2011) &#8212; 1.1.1 is a silly version number anyway!</h3>
<dl>
<dt>&bull;</p>
<dd> #809: Include custom fixers in the source distribution.</dl>
<h3>Release 1.1.1 (Nov 1, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> #791: Fix QtHelp, DevHelp and HtmlHelp index entry links.</p>
<dt>&bull;</p>
<dd> #792: Include &quot;sphinx-apidoc&quot; in the source distribution.</p>
<dt>&bull;</p>
<dd> #797: Don&#8217;t crash on a misformatted glossary.</p>
<dt>&bull;</p>
<dd> #801: Make intersphinx work properly without SSL support.</p>
<dt>&bull;</p>
<dd> #805: Make the <code>Sphinx.add_index_to_domain</code> method work correctly.</p>
<dt>&bull;</p>
<dd> #780: Fix Python 2.5 compatibility.</dl>
<h3>Release 1.1 (Oct 9, 2011)</h3>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> The <code>py:module</code> directive doesn&#8217;t output its <code>platform</code> option value anymore. (It was the only thing that the directive did output, and therefore quite inconsistent.)</p>
<dt>&bull;</p>
<dd> Removed support for old dependency versions; requirements are now:</p>
<dt>&bull;</p>
<dd> Pygments &gt;= 1.2</p>
<dt>&bull;</p>
<dd> Docutils &gt;= 0.7</p>
<dt>&bull;</p>
<dd> Jinja2 &gt;= 2.3</dl>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> Added Python 3.x support.</p>
<dt>&bull;</p>
<dd> New builders and subsystems:</p>
<dt>&bull;</p>
<dd> Added a Texinfo builder.</p>
<dt>&bull;</p>
<dd> Added i18n support for content, a <code>gettext</code> builder and related utilities.</p>
<dt>&bull;</p>
<dd> Added the <code>websupport</code> library and builder.</p>
<dt>&bull;</p>
<dd> #98: Added a <code>sphinx-apidoc</code> script that autogenerates a hierarchy of source files containing autodoc directives to document modules and packages.</p>
<dt>&bull;</p>
<dd> #273: Add an API for adding full-text search support for languages other than English. Add support for Japanese.</p>
<dt>&bull;</p>
<dd> Markup:</p>
<dt>&bull;</p>
<dd> #138: Added an <code>index</code> role, to make inline index entries.</p>
<dt>&bull;</p>
<dd> #454: Added more index markup capabilities: marking see/seealso entries, and main entries for a given key.</p>
<dt>&bull;</p>
<dd> #460: Allowed limiting the depth of section numbers for HTML using the <code>toctree</code>&#8216;s <code>numbered</code> option.</p>
<dt>&bull;</p>
<dd> #586: Implemented improved <code>glossary</code> markup which allows multiple terms per definition.</p>
<dt>&bull;</p>
<dd> #478: Added <code>py:decorator</code> directive to describe decorators.</p>
<dt>&bull;</p>
<dd> C++ domain now supports array definitions.</p>
<dt>&bull;</p>
<dd> C++ domain now supports doc fields (<code>:param x:</code> inside directives).</p>
<dt>&bull;</p>
<dd> Section headings in <code>only</code> directives are now correctly handled.</p>
<dt>&bull;</p>
<dd> Added <code>emphasize-lines</code> option to source code directives.</p>
<dt>&bull;</p>
<dd> #678: C++ domain now supports superclasses.</p>
<dt>&bull;</p>
<dd> HTML builder:</p>
<dt>&bull;</p>
<dd> Added <code>pyramid</code> theme.</p>
<dt>&bull;</p>
<dd> #559: <code>html_add_permalinks</code> is now a string giving the text to display in permalinks.</p>
<dt>&bull;</p>
<dd> #259: HTML table rows now have even/odd CSS classes to enable &quot;Zebra styling&quot;.</p>
<dt>&bull;</p>
<dd> #554: Add theme option <code>sidebarwidth</code> to the basic theme.</p>
<dt>&bull;</p>
<dd> Other builders:</p>
<dt>&bull;</p>
<dd> #516: Added new value of the <code>latex_show_urls</code> option to show the URLs in footnotes.</p>
<dt>&bull;</p>
<dd> #209: Added <code>text_newlines</code> and <code>text_sectionchars</code> config values.</p>
<dt>&bull;</p>
<dd> Added <code>man_show_urls</code> config value.</p>
<dt>&bull;</p>
<dd> #472: linkcheck builder: Check links in parallel, use HTTP HEAD requests and allow configuring the timeout. New config values: <code>linkcheck_timeout</code> and <code>linkcheck_workers</code>.</p>
<dt>&bull;</p>
<dd> #521: Added <code>linkcheck_ignore</code> config value.</p>
<dt>&bull;</p>
<dd> #28: Support row/colspans in tables in the LaTeX builder.</p>
<dt>&bull;</p>
<dd> Configuration and extensibility:</p>
<dt>&bull;</p>
<dd> #537: Added <code>nitpick_ignore</code>.</p>
<dt>&bull;</p>
<dd> #306: Added <code>env-get-outdated</code> event.</p>
<dt>&bull;</p>
<dd> <code>Application.add_stylesheet()</code> now accepts full URIs.</p>
<dt>&bull;</p>
<dd> Autodoc:</p>
<dt>&bull;</p>
<dd> #564: Add <code>autodoc_docstring_signature</code>. When enabled (the default), autodoc retrieves the signature from the first line of the docstring, if it is found there.</p>
<dt>&bull;</p>
<dd> #176: Provide <code>private-members</code> option for autodoc directives.</p>
<dt>&bull;</p>
<dd> #520: Provide <code>special-members</code> option for autodoc directives.</p>
<dt>&bull;</p>
<dd> #431: Doc comments for attributes can now be given on the same line as the assignment.</p>
<dt>&bull;</p>
<dd> #437: autodoc now shows values of class data attributes.</p>
<dt>&bull;</p>
<dd> autodoc now supports documenting the signatures of <code>functools.partial</code> objects.</p>
<dt>&bull;</p>
<dd> Other extensions:</p>
<dt>&bull;</p>
<dd> Added the <code>sphinx.ext.mathjax</code> extension.</p>
<dt>&bull;</p>
<dd> #443: Allow referencing external graphviz files.</p>
<dt>&bull;</p>
<dd> Added <code>inline</code> option to graphviz directives, and fixed the default (block-style) in LaTeX output.</p>
<dt>&bull;</p>
<dd> #590: Added <code>caption</code> option to graphviz directives.</p>
<dt>&bull;</p>
<dd> #553: Added <code>testcleanup</code> blocks in the doctest extension.</p>
<dt>&bull;</p>
<dd> #594: <code>trim_doctest_flags</code> now also removes <code>&lt;BLANKLINE&gt;</code> indicators.</p>
<dt>&bull;</p>
<dd> #367: Added automatic exclusion of hidden members in inheritance diagrams, and an option to selectively enable it.</p>
<dt>&bull;</p>
<dd> Added <code>pngmath_add_tooltips</code>.</p>
<dt>&bull;</p>
<dd> The math extension displaymath directives now support <code>name</code> in addition to <code>label</code> for giving the equation label, for compatibility with Docutils.</p>
<dt>&bull;</p>
<dd> New locales:</p>
<dt>&bull;</p>
<dd> #221: Added Swedish locale.</p>
<dt>&bull;</p>
<dd> #526: Added Iranian locale.</p>
<dt>&bull;</p>
<dd> #694: Added Latvian locale.</p>
<dt>&bull;</p>
<dd> Added Nepali locale.</p>
<dt>&bull;</p>
<dd> #714: Added Korean locale.</p>
<dt>&bull;</p>
<dd> #766: Added Estonian locale.</p>
<dt>&bull;</p>
<dd> Bugs fixed:</p>
<dt>&bull;</p>
<dd> #778: Fix &quot;hide search matches&quot; link on pages linked by search.</p>
<dt>&bull;</p>
<dd> Fix the source positions referenced by the &quot;viewcode&quot; extension.</dl>
<h3>Release 1.0.8 (Sep 23, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> #627: Fix tracebacks for AttributeErrors in autosummary generation.</p>
<dt>&bull;</p>
<dd> Fix the <code>abbr</code> role when the abbreviation has newlines in it.</p>
<dt>&bull;</p>
<dd> #727: Fix the links to search results with custom object types.</p>
<dt>&bull;</p>
<dd> #648: Fix line numbers reported in warnings about undefined references.</p>
<dt>&bull;</p>
<dd> #696, #666: Fix C++ array definitions and template arguments that are not type names.</p>
<dt>&bull;</p>
<dd> #633: Allow footnotes in section headers in LaTeX output.</p>
<dt>&bull;</p>
<dd> #616: Allow keywords to be linked via intersphinx.</p>
<dt>&bull;</p>
<dd> #613: Allow Unicode characters in production list token names.</p>
<dt>&bull;</p>
<dd> #720: Add dummy visitors for graphviz nodes for text and man.</p>
<dt>&bull;</p>
<dd> #704: Fix image file duplication bug.</p>
<dt>&bull;</p>
<dd> #677: Fix parsing of multiple signatures in C++ domain.</p>
<dt>&bull;</p>
<dd> #637: Ignore Emacs lock files when looking for source files.</p>
<dt>&bull;</p>
<dd> #544: Allow .pyw extension for importable modules in autodoc.</p>
<dt>&bull;</p>
<dd> #700: Use <code>$(MAKE)</code> in quickstart-generated Makefiles.</p>
<dt>&bull;</p>
<dd> #734: Make sidebar search box width consistent in browsers.</p>
<dt>&bull;</p>
<dd> #644: Fix spacing of centered figures in HTML output.</p>
<dt>&bull;</p>
<dd> #767: Safely encode SphinxError messages when printing them to sys.stderr.</p>
<dt>&bull;</p>
<dd> #611: Fix LaTeX output error with a document with no sections but a link target.</p>
<dt>&bull;</p>
<dd> Correctly treat built-in method descriptors as methods in autodoc.</p>
<dt>&bull;</p>
<dd> #706: Stop monkeypatching the Python textwrap module.</p>
<dt>&bull;</p>
<dd> #657: viewcode now works correctly with source files that have non-ASCII encoding.</p>
<dt>&bull;</p>
<dd> #669: Respect the <code>noindex</code> flag option in py:module directives.</p>
<dt>&bull;</p>
<dd> #675: Fix IndexErrors when including nonexisting lines with <code>literalinclude</code>.</p>
<dt>&bull;</p>
<dd> #676: Respect custom function/method parameter separator strings.</p>
<dt>&bull;</p>
<dd> #682: Fix JS incompatibility with jQuery &gt;= 1.5.</p>
<dt>&bull;</p>
<dd> #693: Fix double encoding done when writing HTMLHelp .hhk files.</p>
<dt>&bull;</p>
<dd> #647: Do not apply SmartyPants in parsed-literal blocks.</p>
<dt>&bull;</p>
<dd> C++ domain now supports array definitions.</dl>
<h3>Release 1.0.7 (Jan 15, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> #347: Fix wrong generation of directives of static methods in autosummary.</p>
<dt>&bull;</p>
<dd> #599: Import PIL as <code>from PIL import Image</code>.</p>
<dt>&bull;</p>
<dd> #558: Fix longtables with captions in LaTeX output.</p>
<dt>&bull;</p>
<dd> Make token references work as hyperlinks again in LaTeX output.</p>
<dt>&bull;</p>
<dd> #572: Show warnings by default when reference labels cannot be found.</p>
<dt>&bull;</p>
<dd> #536: Include line number when complaining about missing reference targets in nitpicky mode.</p>
<dt>&bull;</p>
<dd> #590: Fix inline display of graphviz diagrams in LaTeX output.</p>
<dt>&bull;</p>
<dd> #589: Build using app.build() in setup command.</p>
<dt>&bull;</p>
<dd> Fix a bug in the inheritance diagram exception that caused base classes to be skipped if one of them is a builtin.</p>
<dt>&bull;</p>
<dd> Fix general index links for C++ domain objects.</p>
<dt>&bull;</p>
<dd> #332: Make admonition boundaries in LaTeX output visible.</p>
<dt>&bull;</p>
<dd> #573: Fix KeyErrors occurring on rebuild after removing a file.</p>
<dt>&bull;</p>
<dd> Fix a traceback when removing files with globbed toctrees.</p>
<dt>&bull;</p>
<dd> If an autodoc object cannot be imported, always re-read the document containing the directive on next build.</p>
<dt>&bull;</p>
<dd> If an autodoc object cannot be imported, show the full traceback of the import error.</p>
<dt>&bull;</p>
<dd> Fix a bug where the removal of download files and images wasn&#8217;t noticed.</p>
<dt>&bull;</p>
<dd> #571: Implement <code>~</code> cross-reference prefix for the C domain.</p>
<dt>&bull;</p>
<dd> Fix regression of LaTeX output with the fix of #556.</p>
<dt>&bull;</p>
<dd> #568: Fix lookup of class attribute documentation on descriptors so that comment documentation now works.</p>
<dt>&bull;</p>
<dd> Fix traceback with <code>only</code> directives preceded by targets.</p>
<dt>&bull;</p>
<dd> Fix tracebacks occurring for duplicate C++ domain objects.</p>
<dt>&bull;</p>
<dd> Fix JavaScript domain links to objects with <code>$</code> in their name.</dl>
<h3>Release 1.0.6 (Jan 04, 2011)</h3>
<dl>
<dt>&bull;</p>
<dd> #581: Fix traceback in Python domain for empty cross-reference targets.</p>
<dt>&bull;</p>
<dd> #283: Fix literal block display issues on Chrome browsers.</p>
<dt>&bull;</p>
<dd> #383, #148: Support sorting a limited range of accented characters in the general index and the glossary.</p>
<dt>&bull;</p>
<dd> #570: Try decoding <code>-D</code> and <code>-A</code> command-line arguments with the locale&#8217;s preferred encoding.</p>
<dt>&bull;</p>
<dd> #528: Observe <code>locale_dirs</code> when looking for the JS translations file.</p>
<dt>&bull;</p>
<dd> #574: Add special code for better support of Japanese documents in the LaTeX builder.</p>
<dt>&bull;</p>
<dd> Regression of #77: If there is only one parameter given with <code>:param:</code> markup, the bullet list is now suppressed again.</p>
<dt>&bull;</p>
<dd> #556: Fix missing paragraph breaks in LaTeX output in certain situations.</p>
<dt>&bull;</p>
<dd> #567: Emit the <code>autodoc-process-docstring</code> event even for objects without a docstring so that it can add content.</p>
<dt>&bull;</p>
<dd> #565: In the LaTeX builder, not only literal blocks require different table handling, but also quite a few other list-like block elements.</p>
<dt>&bull;</p>
<dd> #515: Fix tracebacks in the viewcode extension for Python objects that do not have a valid signature.</p>
<dt>&bull;</p>
<dd> Fix strange reportings of line numbers for warnings generated from autodoc-included docstrings, due to different behavior depending on docutils version.</p>
<dt>&bull;</p>
<dd> Several fixes to the C++ domain.</dl>
<h3>Release 1.0.5 (Nov 12, 2010)</h3>
<dl>
<dt>&bull;</p>
<dd> #557: Add CSS styles required by docutils 0.7 for aligned images and figures.</p>
<dt>&bull;</p>
<dd> In the Makefile generated by LaTeX output, do not delete pdf files on clean; they might be required images.</p>
<dt>&bull;</p>
<dd> #535: Fix LaTeX output generated for line blocks.</p>
<dt>&bull;</p>
<dd> #544: Allow <code>.pyw</code> as a source file extension.</dl>
<h3>Release 1.0.4 (Sep 17, 2010)</h3>
<dl>
<dt>&bull;</p>
<dd> #524: Open intersphinx inventories in binary mode on Windows, since version 2 contains zlib-compressed data.</p>
<dt>&bull;</p>
<dd> #513: Allow giving non-local URIs for JavaScript files, e.g. in the JSMath extension.</p>
<dt>&bull;</p>
<dd> #512: Fix traceback when <code>intersphinx_mapping</code> is empty.</dl>
<h3>Release 1.0.3 (Aug 23, 2010)</h3>
<dl>
<dt>&bull;</p>
<dd> #495: Fix internal vs. external link distinction for links coming from a docutils table-of-contents.</p>
<dt>&bull;</p>
<dd> #494: Fix the <code>maxdepth</code> option for the <code>toctree()</code> template callable when used with <code>collapse=True</code>.</p>
<dt>&bull;</p>
<dd> #507: Fix crash parsing Python argument lists containing brackets in string literals.</p>
<dt>&bull;</p>
<dd> #501: Fix regression when building LaTeX docs with figures that don&#8217;t have captions.</p>
<dt>&bull;</p>
<dd> #510: Fix inheritance diagrams for classes that are not picklable.</p>
<dt>&bull;</p>
<dd> #497: Introduce separate background color for the sidebar collapse button, making it easier to see.</p>
<dt>&bull;</p>
<dd> #502, #503, #496: Fix small layout bugs in several builtin themes.</dl>
<h3>Release 1.0.2 (Aug 14, 2010)</h3>
<dl>
<dt>&bull;</p>
<dd> #490: Fix cross-references to objects of types added by the <code>add_object_type()</code> API function.</p>
<dt>&bull;</p>
<dd> Fix handling of doc field types for different directive types.</p>
<dt>&bull;</p>
<dd> Allow breaking long signatures, continuing with backlash-escaped newlines.</p>
<dt>&bull;</p>
<dd> Fix unwanted styling of C domain references (because of a namespace clash with Pygments styles).</p>
<dt>&bull;</p>
<dd> Allow references to PEPs and RFCs with explicit anchors.</p>
<dt>&bull;</p>
<dd> #471: Fix LaTeX references to figures.</p>
<dt>&bull;</p>
<dd> #482: When doing a non-exact search, match only the given type of object.</p>
<dt>&bull;</p>
<dd> #481: Apply non-exact search for Python reference targets with <code>.name</code> for modules too.</p>
<dt>&bull;</p>
<dd> #484: Fix crash when duplicating a parameter in an info field list.</p>
<dt>&bull;</p>
<dd> #487: Fix setting the default role to one provided by the <code>oldcmarkup</code> extension.</p>
<dt>&bull;</p>
<dd> #488: Fix crash when json-py is installed, which provides a <code>json</code> module but is incompatible to simplejson.</p>
<dt>&bull;</p>
<dd> #480: Fix handling of target naming in intersphinx.</p>
<dt>&bull;</p>
<dd> #486: Fix removal of <code>!</code> for all cross-reference roles.</dl>
<h3>Release 1.0.1 (Jul 27, 2010)</h3>
<dl>
<dt>&bull;</p>
<dd> #470: Fix generated target names for reST domain objects; they are not in the same namespace.</p>
<dt>&bull;</p>
<dd> #266: Add Bengali language.</p>
<dt>&bull;</p>
<dd> #473: Fix a bug in parsing JavaScript object names.</p>
<dt>&bull;</p>
<dd> #474: Fix building with SingleHTMLBuilder when there is no toctree.</p>
<dt>&bull;</p>
<dd> Fix display names for objects linked to by intersphinx with explicit targets.</p>
<dt>&bull;</p>
<dd> Fix building with the JSON builder.</p>
<dt>&bull;</p>
<dd> Fix hyperrefs in object descriptions for LaTeX.</dl>
<h3>Release 1.0 (Jul 23, 2010)</h3>
<h3>Incompatible changes</h3>
<dl>
<dt>&bull;</p>
<dd> Support for domains has been added. A domain is a collection of directives and roles that all describe objects belonging together, e.g. elements of a programming language. A few builtin domains are provided:</p>
<dt>&bull;</p>
<dd> Python</p>
<dt>&bull;</p>
<dd> C</p>
<dt>&bull;</p>
<dd> C++</p>
<dt>&bull;</p>
<dd> JavaScript</p>
<dt>&bull;</p>
<dd> reStructuredText</p>
<dt>&bull;</p>
<dd> The old markup for defining and linking to C directives is now deprecated. It will not work anymore in future versions without activating the <code>oldcmarkup</code> extension; in Sphinx 1.0, it is activated by default.</p>
<dt>&bull;</p>
<dd> Removed support for old dependency versions; requirements are now:</p>
<dt>&bull;</p>
<dd> docutils &gt;= 0.5</p>
<dt>&bull;</p>
<dd> Jinja2 &gt;= 2.2</p>
<dt>&bull;</p>
<dd> Removed deprecated elements:</p>
<dt>&bull;</p>
<dd> <code>exclude_dirs</code> config value</p>
<dt>&bull;</p>
<dd> <code>sphinx.builder</code> module</dl>
<h3>Features added</h3>
<dl>
<dt>&bull;</p>
<dd> General:</p>
<dt>&bull;</p>
<dd> Added a &quot;nitpicky&quot; mode that emits warnings for all missing references. It is activated by the <i>-n</i> command-line switch or the <code>nitpicky</code> config value.</p>
<dt>&bull;</p>
<dd> Added <code>latexpdf</code> target in quickstart Makefile.</p>
<dt>&bull;</p>
<dd> Markup:</p>
<dt>&bull;</p>
<dd> The <code>menuselection</code> and <code>guilabel</code> roles now support ampersand accelerators.</p>
<dt>&bull;</p>
<dd> New more compact doc field syntax is now recognized: <code>:param type name: description</code>.</p>
<dt>&bull;</p>
<dd> Added <code>tab-width</code> option to <code>literalinclude</code> directive.</p>
<dt>&bull;</p>
<dd> Added <code>titlesonly</code> option to <code>toctree</code> directive.</p>
<dt>&bull;</p>
<dd> Added the <code>prepend</code> and <code>append</code> options to the <code>literalinclude</code> directive.</p>
<dt>&bull;</p>
<dd> #284: All docinfo metadata is now put into the document metadata, not just the author.</p>
<dt>&bull;</p>
<dd> The <code>ref</code> role can now also reference tables by caption.</p>
<dt>&bull;</p>
<dd> The <code>include</code> directive now supports absolute paths, which are interpreted as relative to the source directory.</p>
<dt>&bull;</p>
<dd> In the Python domain, references like <code>:func:`.name`</code> now look for matching names with any prefix if no direct match is found.</p>
<dt>&bull;</p>
<dd> Configuration:</p>
<dt>&bull;</p>
<dd> Added <code>rst_prolog</code> config value.</p>
<dt>&bull;</p>
<dd> Added <code>html_secnumber_suffix</code> config value to control section numbering format.</p>
<dt>&bull;</p>
<dd> Added <code>html_compact_lists</code> config value to control docutils&#8217; compact lists feature.</p>
<dt>&bull;</p>
<dd> The <code>html_sidebars</code> config value can now contain patterns as keys, and the values can be lists that explicitly select which sidebar templates should be rendered. That means that the builtin sidebar contents can be included only selectively.</p>
<dt>&bull;</p>
<dd> <code>html_static_path</code> can now contain single file entries.</p>
<dt>&bull;</p>
<dd> The new universal config value <code>exclude_patterns</code> makes the old <code>unused_docs</code>, <code>exclude_trees</code> and <code>exclude_dirnames</code> obsolete.</p>
<dt>&bull;</p>
<dd> Added <code>html_output_encoding</code> config value.</p>
<dt>&bull;</p>
<dd> Added the <code>latex_docclass</code> config value and made the &quot;twoside&quot; documentclass option overridable by &quot;oneside&quot;.</p>
<dt>&bull;</p>
<dd> Added the <code>trim_doctest_flags</code> config value, which is true by default.</p>
<dt>&bull;</p>
<dd> Added <code>html_show_copyright</code> config value.</p>
<dt>&bull;</p>
<dd> Added <code>latex_show_pagerefs</code> and <code>latex_show_urls</code> config values.</p>
<dt>&bull;</p>
<dd> The behavior of <code>html_file_suffix</code> changed slightly: the empty string now means &quot;no suffix&quot; instead of &quot;default suffix&quot;, use <code>None</code> for &quot;default suffix&quot;.</p>
<dt>&bull;</p>
<dd> New builders:</p>
<dt>&bull;</p>
<dd> Added a builder for the Epub format.</p>
<dt>&bull;</p>
<dd> Added a builder for manual pages.</p>
<dt>&bull;</p>
<dd> Added a single-file HTML builder.</p>
<dt>&bull;</p>
<dd> HTML output:</p>
<dt>&bull;</p>
<dd> Inline roles now get a CSS class with their name, allowing styles to customize their appearance. Domain-specific roles get two classes, <code>domain</code> and <code>domain-rolename</code>.</p>
<dt>&bull;</p>
<dd> References now get the class <code>internal</code> if they are internal to the whole project, as opposed to internal to the current page.</p>
<dt>&bull;</p>
<dd> External references can be styled differently with the new <code>externalrefs</code> theme option for the default theme.</p>
<dt>&bull;</p>
<dd> In the default theme, the sidebar can experimentally now be made collapsible using the new <code>collapsiblesidebar</code> theme option.</p>
<dt>&bull;</p>
<dd> #129: Toctrees are now wrapped in a <code>div</code> tag with class <code>toctree-wrapper</code> in HTML output.</p>
<dt>&bull;</p>
<dd> The <code>toctree</code> callable in templates now has a <code>maxdepth</code> keyword argument to control the depth of the generated tree.</p>
<dt>&bull;</p>
<dd> The <code>toctree</code> callable in templates now accepts a <code>titles_only</code> keyword argument.</p>
<dt>&bull;</p>
<dd> Added <code>htmltitle</code> block in layout template.</p>
<dt>&bull;</p>
<dd> In the JavaScript search, allow searching for object names including the module name, like <code>sys.argv</code>.</p>
<dt>&bull;</p>
<dd> Added new theme <code>haiku</code>, inspired by the Haiku OS user guide.</p>
<dt>&bull;</p>
<dd> Added new theme <code>nature</code>.</p>
<dt>&bull;</p>
<dd> Added new theme <code>agogo</code>, created by Andi Albrecht.</p>
<dt>&bull;</p>
<dd> Added new theme <code>scrolls</code>, created by Armin Ronacher.</p>
<dt>&bull;</p>
<dd> #193: Added a <code>visitedlinkcolor</code> theme option to the default theme.</p>
<dt>&bull;</p>
<dd> #322: Improved responsiveness of the search page by loading the search index asynchronously.</p>
<dt>&bull;</p>
<dd> Extension API:</p>
<dt>&bull;</p>
<dd> Added <code>html-collect-pages</code>.</p>
<dt>&bull;</p>
<dd> Added <code>needs_sphinx</code> config value and <code>require_sphinx()</code> application API method.</p>
<dt>&bull;</p>
<dd> #200: Added <code>add_stylesheet()</code> application API method.</p>
<dt>&bull;</p>
<dd> Extensions:</p>
<dt>&bull;</p>
<dd> Added the <code>viewcode</code> extension.</p>
<dt>&bull;</p>
<dd> Added the <code>extlinks</code> extension.</p>
<dt>&bull;</p>
<dd> Added support for source ordering of members in autodoc, with <code>autodoc_member_order = &#8216;bysource&#8217;</code>.</p>
<dt>&bull;</p>
<dd> Added <code>autodoc_default_flags</code> config value, which can be used to select default flags for all autodoc directives.</p>
<dt>&bull;</p>
<dd> Added a way for intersphinx to refer to named labels in other projects, and to specify the project you want to link to.</p>
<dt>&bull;</p>
<dd> #280: Autodoc can now document instance attributes assigned in <code>__init__</code> methods.</p>
<dt>&bull;</p>
<dd> Many improvements and fixes to the <code>autosummary</code> extension, thanks to Pauli Virtanen.</p>
<dt>&bull;</p>
<dd> #309: The <code>graphviz</code> extension can now output SVG instead of PNG images, controlled by the <code>graphviz_output_format</code> config value.</p>
<dt>&bull;</p>
<dd> Added <code>alt</code> option to <code>graphviz</code> extension directives.</p>
<dt>&bull;</p>
<dd> Added <code>exclude</code> argument to <code>autodoc.between()</code>.</p>
<dt>&bull;</p>
<dd> Translations:</p>
<dt>&bull;</p>
<dd> Added Croatian translation, thanks to Bojan MihelaÄ.</p>
<dt>&bull;</p>
<dd> Added Turkish translation, thanks to Firat Ozgul.</p>
<dt>&bull;</p>
<dd> Added Catalan translation, thanks to Pau FernÃ¡ndez.</p>
<dt>&bull;</p>
<dd> Added simplified Chinese translation.</p>
<dt>&bull;</p>
<dd> Added Danish translation, thanks to Hjorth Larsen.</p>
<dt>&bull;</p>
<dd> Added Lithuanian translation, thanks to Dalius Dobravolskas.</p>
<dt>&bull;</p>
<dd> Bugs fixed:</p>
<dt>&bull;</p>
<dd> #445: Fix links to result pages when using the search function of HTML built with the <code>dirhtml</code> builder.</p>
<dt>&bull;</p>
<dd> #444: In templates, properly re-escape values treated with the &quot;striptags&quot; Jinja filter.</dl>
<h3>Previous versions</h3>
<p> The changelog for versions before 1.0 can be found in the file <code>CHANGES.old</code> in the source distribution or <i>at BitBucket</i>.</p>
<h2>PROJECTS USING SPHINX</h2>
<p> This is an (incomplete) alphabetic list of projects that use Sphinx or are experimenting with using it for their documentation. If you like to be included, please mail to <i>the Google group</i>. </p>
<p> I&#8217;ve grouped the list into sections to make it easier to find interesting examples.</p>
<h3>Documentation using the default theme</h3>
<dl>
<dt>&bull;</p>
<dd> APSW: <i><a rel="nofollow" href="http://apidoc.apsw.googlecode.com/hg/index.html">http://apidoc.apsw.googlecode.com/hg/index.html</a></i></p>
<dt>&bull;</p>
<dd> ASE: <i><a rel="nofollow" href="https://wiki.fysik.dtu.dk/ase/">https://wiki.fysik.dtu.dk/ase/</a></i></p>
<dt>&bull;</p>
<dd> boostmpi: <i><a rel="nofollow" href="http://documen.tician.de/boostmpi/">http://documen.tician.de/boostmpi/</a></i></p>
<dt>&bull;</p>
<dd> Calibre: <i><a rel="nofollow" href="http://manual.calibre-ebook.com/">http://manual.calibre-ebook.com/</a></i></p>
<dt>&bull;</p>
<dd> CodePy: <i><a rel="nofollow" href="http://documen.tician.de/codepy/">http://documen.tician.de/codepy/</a></i></p>
<dt>&bull;</p>
<dd> Cython: <i><a rel="nofollow" href="http://docs.cython.org/">http://docs.cython.org/</a></i></p>
<dt>&bull;</p>
<dd> C\C++ Python language binding project: <i><a rel="nofollow" href="http://language-binding.net/index.html">http://language-binding.net/index.html</a></i></p>
<dt>&bull;</p>
<dd> Cormoran: <i><a rel="nofollow" href="http://cormoran.nhopkg.org/docs/">http://cormoran.nhopkg.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Director: <i><a rel="nofollow" href="http://pythonhosted.org/director/">http://pythonhosted.org/director/</a></i></p>
<dt>&bull;</p>
<dd> Dirigible: <i><a rel="nofollow" href="http://www.projectdirigible.com/documentation/">http://www.projectdirigible.com/documentation/</a></i></p>
<dt>&bull;</p>
<dd> Elemental: <i><a rel="nofollow" href="http://elemental.googlecode.com/hg/doc/build/html/index.html">http://elemental.googlecode.com/hg/doc/build/html/index.html</a></i></p>
<dt>&bull;</p>
<dd> F2py: <i><a rel="nofollow" href="http://f2py.sourceforge.net/docs/">http://f2py.sourceforge.net/docs/</a></i></p>
<dt>&bull;</p>
<dd> GeoDjango: <i><a rel="nofollow" href="http://geodjango.org/docs/">http://geodjango.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Genomedata: <i><a rel="nofollow" href="http://noble.gs.washington.edu/proj/genomedata/doc/1.2.2/genomedata.html">http://noble.gs.washington.edu/proj/genomedata/doc/1.2.2/genomedata.html</a></i></p>
<dt>&bull;</p>
<dd> gevent: <i><a rel="nofollow" href="http://www.gevent.org/">http://www.gevent.org/</a></i></p>
<dt>&bull;</p>
<dd> Google Wave API: <i><a rel="nofollow" href="http://wave-robot-python-client.googlecode.com/svn/trunk/pydocs/index.html">http://wave-robot-python-client.googlecode.com/svn/trunk/pydocs/index.html</a></i></p>
<dt>&bull;</p>
<dd> GSL Shell: <i><a rel="nofollow" href="http://www.nongnu.org/gsl-shell/">http://www.nongnu.org/gsl-shell/</a></i></p>
<dt>&bull;</p>
<dd> Heapkeeper: <i><a rel="nofollow" href="http://heapkeeper.org/">http://heapkeeper.org/</a></i></p>
<dt>&bull;</p>
<dd> Hands-on Python Tutorial: <i><a rel="nofollow" href="http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/">http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/</a></i></p>
<dt>&bull;</p>
<dd> Hedge: <i><a rel="nofollow" href="http://documen.tician.de/hedge/">http://documen.tician.de/hedge/</a></i></p>
<dt>&bull;</p>
<dd> Kaa: <i><a rel="nofollow" href="http://doc.freevo.org/api/kaa/">http://doc.freevo.org/api/kaa/</a></i></p>
<dt>&bull;</p>
<dd> Leo: <i><a rel="nofollow" href="http://webpages.charter.net/edreamleo/front.html">http://webpages.charter.net/edreamleo/front.html</a></i></p>
<dt>&bull;</p>
<dd> Lino: <i><a rel="nofollow" href="http://lino.saffre-rumma.net/">http://lino.saffre-rumma.net/</a></i></p>
<dt>&bull;</p>
<dd> MeshPy: <i><a rel="nofollow" href="http://documen.tician.de/meshpy/">http://documen.tician.de/meshpy/</a></i></p>
<dt>&bull;</p>
<dd> mpmath: <i><a rel="nofollow" href="http://mpmath.googlecode.com/svn/trunk/doc/build/index.html">http://mpmath.googlecode.com/svn/trunk/doc/build/index.html</a></i></p>
<dt>&bull;</p>
<dd> OpenEXR: <i><a rel="nofollow" href="http://excamera.com/articles/26/doc/index.html">http://excamera.com/articles/26/doc/index.html</a></i></p>
<dt>&bull;</p>
<dd> OpenGDA: <i><a rel="nofollow" href="http://www.opengda.org/gdadoc/html/">http://www.opengda.org/gdadoc/html/</a></i></p>
<dt>&bull;</p>
<dd> openWNS: <i><a rel="nofollow" href="http://docs.openwns.org/">http://docs.openwns.org/</a></i></p>
<dt>&bull;</p>
<dd> Paste: <i><a rel="nofollow" href="http://pythonpaste.org/script/">http://pythonpaste.org/script/</a></i></p>
<dt>&bull;</p>
<dd> Paver: <i><a rel="nofollow" href="http://paver.github.com/paver/">http://paver.github.com/paver/</a></i></p>
<dt>&bull;</p>
<dd> Pioneers and Prominent Men of Utah: <i><a rel="nofollow" href="http://pioneers.rstebbing.com/">http://pioneers.rstebbing.com/</a></i></p>
<dt>&bull;</p>
<dd> Pyccuracy: <i><a rel="nofollow" href="https://github.com/heynemann/pyccuracy/wiki/">https://github.com/heynemann/pyccuracy/wiki/</a></i></p>
<dt>&bull;</p>
<dd> PyCuda: <i><a rel="nofollow" href="http://documen.tician.de/pycuda/">http://documen.tician.de/pycuda/</a></i></p>
<dt>&bull;</p>
<dd> Pyevolve: <i><a rel="nofollow" href="http://pyevolve.sourceforge.net/">http://pyevolve.sourceforge.net/</a></i></p>
<dt>&bull;</p>
<dd> Pylo: <i><a rel="nofollow" href="http://documen.tician.de/pylo/">http://documen.tician.de/pylo/</a></i></p>
<dt>&bull;</p>
<dd> PyMQI: <i><a rel="nofollow" href="http://packages.python.org/pymqi/">http://packages.python.org/pymqi/</a></i></p>
<dt>&bull;</p>
<dd> PyPubSub: <i><a rel="nofollow" href="http://pubsub.sourceforge.net/">http://pubsub.sourceforge.net/</a></i></p>
<dt>&bull;</p>
<dd> pyrticle: <i><a rel="nofollow" href="http://documen.tician.de/pyrticle/">http://documen.tician.de/pyrticle/</a></i></p>
<dt>&bull;</p>
<dd> Python: <i><a rel="nofollow" href="http://docs.python.org/">http://docs.python.org/</a></i></p>
<dt>&bull;</p>
<dd> python-apt: <i><a rel="nofollow" href="http://apt.alioth.debian.org/python-apt-doc/">http://apt.alioth.debian.org/python-apt-doc/</a></i></p>
<dt>&bull;</p>
<dd> PyUblas: <i><a rel="nofollow" href="http://documen.tician.de/pyublas/">http://documen.tician.de/pyublas/</a></i></p>
<dt>&bull;</p>
<dd> Quex: <i><a rel="nofollow" href="http://quex.sourceforge.net/doc/html/main.html">http://quex.sourceforge.net/doc/html/main.html</a></i></p>
<dt>&bull;</p>
<dd> Scapy: <i><a rel="nofollow" href="http://www.secdev.org/projects/scapy/doc/">http://www.secdev.org/projects/scapy/doc/</a></i></p>
<dt>&bull;</p>
<dd> Segway: <i><a rel="nofollow" href="http://noble.gs.washington.edu/proj/segway/doc/1.1.0/segway.html">http://noble.gs.washington.edu/proj/segway/doc/1.1.0/segway.html</a></i></p>
<dt>&bull;</p>
<dd> SimPy: <i><a rel="nofollow" href="http://simpy.sourceforge.net/SimPyDocs/index.html">http://simpy.sourceforge.net/SimPyDocs/index.html</a></i></p>
<dt>&bull;</p>
<dd> SymPy: <i><a rel="nofollow" href="http://docs.sympy.org/">http://docs.sympy.org/</a></i></p>
<dt>&bull;</p>
<dd> WTForms: <i><a rel="nofollow" href="http://wtforms.simplecodes.com/docs/">http://wtforms.simplecodes.com/docs/</a></i></p>
<dt>&bull;</p>
<dd> z3c: <i><a rel="nofollow" href="http://docs.carduner.net/z3c-tutorial/">http://docs.carduner.net/z3c-tutorial/</a></i></dl>
<h3>Documentation using a customized version of the default theme</h3>
<dl>
<dt>&bull;</p>
<dd> Advanced Generic Widgets: <i><a rel="nofollow" href="http://xoomer.virgilio.it/infinity77/AGW_Docs/index.html">http://xoomer.virgilio.it/infinity77/AGW_Docs/index.html</a></i></p>
<dt>&bull;</p>
<dd> Bazaar: <i><a rel="nofollow" href="http://doc.bazaar.canonical.com/en/">http://doc.bazaar.canonical.com/en/</a></i></p>
<dt>&bull;</p>
<dd> CakePHP: <i><a rel="nofollow" href="http://book.cakephp.org/2.0/en/index.html">http://book.cakephp.org/2.0/en/index.html</a></i></p>
<dt>&bull;</p>
<dd> Chaco: <i><a rel="nofollow" href="http://code.enthought.com/projects/chaco/docs/html/">http://code.enthought.com/projects/chaco/docs/html/</a></i></p>
<dt>&bull;</p>
<dd> Chef: <i><a rel="nofollow" href="http://docs.opscode.com/">http://docs.opscode.com/</a></i></p>
<dt>&bull;</p>
<dd> Djagios: <i><a rel="nofollow" href="http://djagios.org/">http://djagios.org/</a></i></p>
<dt>&bull;</p>
<dd> GetFEM++: <i><a rel="nofollow" href="http://home.gna.org/getfem/">http://home.gna.org/getfem/</a></i></p>
<dt>&bull;</p>
<dd> Google or-tools: <i><a rel="nofollow" href="https://or-tools.googlecode.com/svn/trunk/documentation/user_manual/index.html">https://or-tools.googlecode.com/svn/trunk/documentation/user_manual/index.html</a></i></p>
<dt>&bull;</p>
<dd> GPAW: <i><a rel="nofollow" href="https://wiki.fysik.dtu.dk/gpaw/">https://wiki.fysik.dtu.dk/gpaw/</a></i></p>
<dt>&bull;</p>
<dd> Grok: <i><a rel="nofollow" href="http://grok.zope.org/doc/current/">http://grok.zope.org/doc/current/</a></i></p>
<dt>&bull;</p>
<dd> IFM: <i><a rel="nofollow" href="http://fluffybunny.memebot.com/ifm-docs/index.html">http://fluffybunny.memebot.com/ifm-docs/index.html</a></i></p>
<dt>&bull;</p>
<dd> LEPL: <i><a rel="nofollow" href="http://www.acooke.org/lepl/">http://www.acooke.org/lepl/</a></i></p>
<dt>&bull;</p>
<dd> Mayavi: <i><a rel="nofollow" href="http://code.enthought.com/projects/mayavi/docs/development/html/mayavi">http://code.enthought.com/projects/mayavi/docs/development/html/mayavi</a></i></p>
<dt>&bull;</p>
<dd> NOC: <i><a rel="nofollow" href="http://redmine.nocproject.org/projects/noc">http://redmine.nocproject.org/projects/noc</a></i></p>
<dt>&bull;</p>
<dd> NumPy: <i><a rel="nofollow" href="http://docs.scipy.org/doc/numpy/reference/">http://docs.scipy.org/doc/numpy/reference/</a></i></p>
<dt>&bull;</p>
<dd> OpenCV: <i><a rel="nofollow" href="http://docs.opencv.org/">http://docs.opencv.org/</a></i></p>
<dt>&bull;</p>
<dd> Peach^3: <i><a rel="nofollow" href="http://peach3.nl/doc/latest/userdoc/">http://peach3.nl/doc/latest/userdoc/</a></i></p>
<dt>&bull;</p>
<dd> PyLit: <i><a rel="nofollow" href="http://pylit.berlios.de/">http://pylit.berlios.de/</a></i></p>
<dt>&bull;</p>
<dd> Sage: <i><a rel="nofollow" href="http://sagemath.org/doc/">http://sagemath.org/doc/</a></i></p>
<dt>&bull;</p>
<dd> SciPy: <i><a rel="nofollow" href="http://docs.scipy.org/doc/scipy/reference/">http://docs.scipy.org/doc/scipy/reference/</a></i></p>
<dt>&bull;</p>
<dd> simuPOP: <i><a rel="nofollow" href="http://simupop.sourceforge.net/manual_release/build/userGuide.html">http://simupop.sourceforge.net/manual_release/build/userGuide.html</a></i></p>
<dt>&bull;</p>
<dd> Sprox: <i><a rel="nofollow" href="http://sprox.org/">http://sprox.org/</a></i></p>
<dt>&bull;</p>
<dd> TurboGears: <i><a rel="nofollow" href="http://turbogears.org/2.0/docs/">http://turbogears.org/2.0/docs/</a></i></p>
<dt>&bull;</p>
<dd> Varnish: <i><a rel="nofollow" href="https://www.varnish-cache.org/docs/">https://www.varnish-cache.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Zentyal: <i><a rel="nofollow" href="http://doc.zentyal.org/">http://doc.zentyal.org/</a></i></p>
<dt>&bull;</p>
<dd> Zope: <i><a rel="nofollow" href="http://docs.zope.org/zope2/index.html">http://docs.zope.org/zope2/index.html</a></i></p>
<dt>&bull;</p>
<dd> zc.async: <i><a rel="nofollow" href="http://packages.python.org/zc.async/1.5.0/">http://packages.python.org/zc.async/1.5.0/</a></i></dl>
<h3>Documentation using the sphinxdoc theme</h3>
<dl>
<dt>&bull;</p>
<dd> Fityk: <i><a rel="nofollow" href="http://fityk.nieto.pl/">http://fityk.nieto.pl/</a></i></p>
<dt>&bull;</p>
<dd> MapServer: <i><a rel="nofollow" href="http://mapserver.org/">http://mapserver.org/</a></i></p>
<dt>&bull;</p>
<dd> Matplotlib: <i><a rel="nofollow" href="http://matplotlib.sourceforge.net/">http://matplotlib.sourceforge.net/</a></i></p>
<dt>&bull;</p>
<dd> Music21: <i><a rel="nofollow" href="http://mit.edu/music21/doc/html/contents.html">http://mit.edu/music21/doc/html/contents.html</a></i></p>
<dt>&bull;</p>
<dd> MyHDL: <i><a rel="nofollow" href="http://www.myhdl.org/doc/0.6/">http://www.myhdl.org/doc/0.6/</a></i></p>
<dt>&bull;</p>
<dd> NetworkX: <i><a rel="nofollow" href="http://networkx.lanl.gov/">http://networkx.lanl.gov/</a></i></p>
<dt>&bull;</p>
<dd> Pweave: <i><a rel="nofollow" href="http://mpastell.com/pweave/">http://mpastell.com/pweave/</a></i></p>
<dt>&bull;</p>
<dd> Pyre: <i><a rel="nofollow" href="http://docs.danse.us/pyre/sphinx/">http://docs.danse.us/pyre/sphinx/</a></i></p>
<dt>&bull;</p>
<dd> Pysparse: <i><a rel="nofollow" href="http://pysparse.sourceforge.net/">http://pysparse.sourceforge.net/</a></i></p>
<dt>&bull;</p>
<dd> PyTango: <i><a rel="nofollow" href="http://www.tango-controls.org/static/PyTango/latest/doc/html/index.html">http://www.tango-controls.org/static/PyTango/latest/doc/html/index.html</a></i></p>
<dt>&bull;</p>
<dd> Python Wild Magic: <i><a rel="nofollow" href="http://python-wild-magic.googlecode.com/svn/doc/html/index.html">http://python-wild-magic.googlecode.com/svn/doc/html/index.html</a></i></p>
<dt>&bull;</p>
<dd> Reteisi: <i><a rel="nofollow" href="http://www.reteisi.org/contents.html">http://www.reteisi.org/contents.html</a></i></p>
<dt>&bull;</p>
<dd> Satchmo: <i><a rel="nofollow" href="http://www.satchmoproject.com/docs/dev/">http://www.satchmoproject.com/docs/dev/</a></i></p>
<dt>&bull;</p>
<dd> Sphinx: <i><a rel="nofollow" href="http://sphinx-doc.org/">http://sphinx-doc.org/</a></i></p>
<dt>&bull;</p>
<dd> Sqlkit: <i><a rel="nofollow" href="http://sqlkit.argolinux.org/">http://sqlkit.argolinux.org/</a></i></p>
<dt>&bull;</p>
<dd> Tau: <i><a rel="nofollow" href="http://www.tango-controls.org/static/tau/latest/doc/html/index.html">http://www.tango-controls.org/static/tau/latest/doc/html/index.html</a></i></p>
<dt>&bull;</p>
<dd> Total Open Station: <i><a rel="nofollow" href="http://tops.berlios.de/">http://tops.berlios.de/</a></i></p>
<dt>&bull;</p>
<dd> Turbulenz: <i><a rel="nofollow" href="http://docs.turbulenz.com/">http://docs.turbulenz.com/</a></i></p>
<dt>&bull;</p>
<dd> WebFaction: <i><a rel="nofollow" href="http://docs.webfaction.com/">http://docs.webfaction.com/</a></i></dl>
<h3>Documentation using another builtin theme</h3>
<dl>
<dt>&bull;</p>
<dd> C/C++ Development with Eclipse: <i><a rel="nofollow" href="http://eclipsebook.in/">http://eclipsebook.in/</a></i> (agogo)</p>
<dt>&bull;</p>
<dd> Distribute: <i><a rel="nofollow" href="http://packages.python.org/distribute/">http://packages.python.org/distribute/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> Jinja: <i><a rel="nofollow" href="http://jinja.pocoo.org/">http://jinja.pocoo.org/</a></i> (scrolls)</p>
<dt>&bull;</p>
<dd> jsFiddle: <i><a rel="nofollow" href="http://doc.jsfiddle.net/">http://doc.jsfiddle.net/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> libLAS: <i><a rel="nofollow" href="http://liblas.org/">http://liblas.org/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> MPipe: <i><a rel="nofollow" href="http://vmlaker.github.io/mpipe/">http://vmlaker.github.io/mpipe/</a></i> (sphinx13)</p>
<dt>&bull;</p>
<dd> pip: <i><a rel="nofollow" href="http://pip.openplans.org/">http://pip.openplans.org/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> Programmieren mit PyGTK und Glade (German): <i><a rel="nofollow" href="http://www.florian-diesch.de/doc/python-und-glade/online/">http://www.florian-diesch.de/doc/python-und-glade/online/</a></i> (agogo)</p>
<dt>&bull;</p>
<dd> Spring Python: <i><a rel="nofollow" href="http://springpython.webfactional.com/current/sphinx/index.html">http://springpython.webfactional.com/current/sphinx/index.html</a></i> (nature)</p>
<dt>&bull;</p>
<dd> sqlparse: <i><a rel="nofollow" href="http://python-sqlparse.googlecode.com/svn/docs/api/index.html">http://python-sqlparse.googlecode.com/svn/docs/api/index.html</a></i> (agogo)</p>
<dt>&bull;</p>
<dd> Sylli: <i><a rel="nofollow" href="http://sylli.sourceforge.net/">http://sylli.sourceforge.net/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> Tuleap Open ALM: <i><a rel="nofollow" href="https://tuleap.net/doc/en/">https://tuleap.net/doc/en/</a></i> (nature)</p>
<dt>&bull;</p>
<dd> Valence: <i><a rel="nofollow" href="http://docs.valence.desire2learn.com/">http://docs.valence.desire2learn.com/</a></i> (haiku)</dl>
<h3>Documentation using a custom theme/integrated in a site</h3>
<dl>
<dt>&bull;</p>
<dd> Blender: <i><a rel="nofollow" href="http://www.blender.org/documentation/250PythonDoc/">http://www.blender.org/documentation/250PythonDoc/</a></i></p>
<dt>&bull;</p>
<dd> Blinker: <i><a rel="nofollow" href="http://discorporate.us/projects/Blinker/docs/">http://discorporate.us/projects/Blinker/docs/</a></i></p>
<dt>&bull;</p>
<dd> Ceph: <i><a rel="nofollow" href="http://ceph.com/docs/master/">http://ceph.com/docs/master/</a></i></p>
<dt>&bull;</p>
<dd> Classy: <i><a rel="nofollow" href="http://classy.pocoo.org/">http://classy.pocoo.org/</a></i></p>
<dt>&bull;</p>
<dd> DEAP: <i><a rel="nofollow" href="http://deap.gel.ulaval.ca/doc/0.8/index.html">http://deap.gel.ulaval.ca/doc/0.8/index.html</a></i></p>
<dt>&bull;</p>
<dd> Django: <i><a rel="nofollow" href="http://docs.djangoproject.com/">http://docs.djangoproject.com/</a></i></p>
<dt>&bull;</p>
<dd> Enterprise Toolkit for Acrobat products: <i><a rel="nofollow" href="http://www.adobe.com/devnet-docs/acrobatetk/">http://www.adobe.com/devnet-docs/acrobatetk/</a></i></p>
<dt>&bull;</p>
<dd> e-cidadania: <i><a rel="nofollow" href="http://e-cidadania.readthedocs.org/en/latest/">http://e-cidadania.readthedocs.org/en/latest/</a></i></p>
<dt>&bull;</p>
<dd> Flask: <i><a rel="nofollow" href="http://flask.pocoo.org/docs/">http://flask.pocoo.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Flask-OpenID: <i><a rel="nofollow" href="http://packages.python.org/Flask-OpenID/">http://packages.python.org/Flask-OpenID/</a></i></p>
<dt>&bull;</p>
<dd> Gameduino: <i><a rel="nofollow" href="http://excamera.com/sphinx/gameduino/">http://excamera.com/sphinx/gameduino/</a></i></p>
<dt>&bull;</p>
<dd> GeoServer: <i><a rel="nofollow" href="http://docs.geoserver.org/">http://docs.geoserver.org/</a></i></p>
<dt>&bull;</p>
<dd> Glashammer: <i><a rel="nofollow" href="http://glashammer.org/">http://glashammer.org/</a></i></p>
<dt>&bull;</p>
<dd> Istihza (Turkish Python documentation project): <i><a rel="nofollow" href="http://www.istihza.com/py2/icindekiler_python.html">http://www.istihza.com/py2/icindekiler_python.html</a></i></p>
<dt>&bull;</p>
<dd> MathJax: <i><a rel="nofollow" href="http://docs.mathjax.org/en/latest/">http://docs.mathjax.org/en/latest/</a></i></p>
<dt>&bull;</p>
<dd> MirrorBrain: <i><a rel="nofollow" href="http://mirrorbrain.org/docs/">http://mirrorbrain.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> nose: <i><a rel="nofollow" href="http://somethingaboutorange.com/mrl/projects/nose/">http://somethingaboutorange.com/mrl/projects/nose/</a></i></p>
<dt>&bull;</p>
<dd> NoTex: <i><a rel="nofollow" href="https://notex.ch/overview/">https://notex.ch/overview/</a></i></p>
<dt>&bull;</p>
<dd> ObjectListView: <i><a rel="nofollow" href="http://objectlistview.sourceforge.net/python">http://objectlistview.sourceforge.net/python</a></i></p>
<dt>&bull;</p>
<dd> Open ERP: <i><a rel="nofollow" href="http://doc.openerp.com/">http://doc.openerp.com/</a></i></p>
<dt>&bull;</p>
<dd> OpenCV: <i><a rel="nofollow" href="http://docs.opencv.org/">http://docs.opencv.org/</a></i></p>
<dt>&bull;</p>
<dd> Open Dylan: <i><a rel="nofollow" href="http://opendylan.org/documentation/">http://opendylan.org/documentation/</a></i> and also provides <i>dylan domain</i></p>
<dt>&bull;</p>
<dd> OpenLayers: <i><a rel="nofollow" href="http://docs.openlayers.org/">http://docs.openlayers.org/</a></i></p>
<dt>&bull;</p>
<dd> PyEphem: <i><a rel="nofollow" href="http://rhodesmill.org/pyephem/">http://rhodesmill.org/pyephem/</a></i></p>
<dt>&bull;</p>
<dd> German Plone user manual: <i><a rel="nofollow" href="http://www.hasecke.com/plone-benutzerhandbuch/">http://www.hasecke.com/plone-benutzerhandbuch/</a></i></p>
<dt>&bull;</p>
<dd> PSI4: <i><a rel="nofollow" href="http://sirius.chem.vt.edu/psi4manual/latest/index.html">http://sirius.chem.vt.edu/psi4manual/latest/index.html</a></i></p>
<dt>&bull;</p>
<dd> Pylons: <i><a rel="nofollow" href="http://pylonshq.com/docs/en/0.9.7/">http://pylonshq.com/docs/en/0.9.7/</a></i></p>
<dt>&bull;</p>
<dd> PyMOTW: <i><a rel="nofollow" href="http://www.doughellmann.com/PyMOTW/">http://www.doughellmann.com/PyMOTW/</a></i></p>
<dt>&bull;</p>
<dd> pypol: <i><a rel="nofollow" href="http://pypol.altervista.org/">http://pypol.altervista.org/</a></i> (celery)</p>
<dt>&bull;</p>
<dd> QGIS: <i><a rel="nofollow" href="http://qgis.org/">http://qgis.org/</a></i></p>
<dt>&bull;</p>
<dd> qooxdoo: <i><a rel="nofollow" href="http://manual.qooxdoo.org/current">http://manual.qooxdoo.org/current</a></i></p>
<dt>&bull;</p>
<dd> Roundup: <i><a rel="nofollow" href="http://www.roundup-tracker.org/">http://www.roundup-tracker.org/</a></i></p>
<dt>&bull;</p>
<dd> Selenium: <i><a rel="nofollow" href="http://seleniumhq.org/docs/">http://seleniumhq.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Self: <i><a rel="nofollow" href="http://selflanguage.org/">http://selflanguage.org/</a></i></p>
<dt>&bull;</p>
<dd> Tablib: <i><a rel="nofollow" href="http://tablib.org/">http://tablib.org/</a></i></p>
<dt>&bull;</p>
<dd> SQLAlchemy: <i><a rel="nofollow" href="http://www.sqlalchemy.org/docs/">http://www.sqlalchemy.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> tinyTiM: <i><a rel="nofollow" href="http://tinytim.sourceforge.net/docs/2.0/">http://tinytim.sourceforge.net/docs/2.0/</a></i></p>
<dt>&bull;</p>
<dd> tipfy: <i><a rel="nofollow" href="http://www.tipfy.org/docs/">http://www.tipfy.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> Ubuntu packaging guide: <i><a rel="nofollow" href="http://packaging.ubuntu.com/html/">http://packaging.ubuntu.com/html/</a></i></p>
<dt>&bull;</p>
<dd> Werkzeug: <i><a rel="nofollow" href="http://werkzeug.pocoo.org/docs/">http://werkzeug.pocoo.org/docs/</a></i></p>
<dt>&bull;</p>
<dd> WFront: <i><a rel="nofollow" href="http://discorporate.us/projects/WFront/">http://discorporate.us/projects/WFront/</a></i></dl>
<h3>Homepages and other non-documentation sites</h3>
<dl>
<dt>&bull;</p>
<dd> Applied Mathematics at the Stellenbosch University: <i><a rel="nofollow" href="http://dip.sun.ac.za/">http://dip.sun.ac.za/</a></i></p>
<dt>&bull;</p>
<dd> A personal page: <i><a rel="nofollow" href="http://www.dehlia.in/">http://www.dehlia.in/</a></i></p>
<dt>&bull;</p>
<dd> Benoit Boissinot: <i><a rel="nofollow" href="http://bboissin.appspot.com/">http://bboissin.appspot.com/</a></i></p>
<dt>&bull;</p>
<dd> lunarsite: <i><a rel="nofollow" href="http://lunaryorn.de/">http://lunaryorn.de/</a></i></p>
<dt>&bull;</p>
<dd> Red Hot Chili Python: <i><a rel="nofollow" href="http://redhotchilipython.com/">http://redhotchilipython.com/</a></i></p>
<dt>&bull;</p>
<dd> The Wine Cellar Book: <i><a rel="nofollow" href="http://www.thewinecellarbook.com/doc/en/">http://www.thewinecellarbook.com/doc/en/</a></i></p>
<dt>&bull;</p>
<dd> Uni. Berkeley Advanced Control Systems course: <i><a rel="nofollow" href="http://www.me.berkeley.edu/ME233/sp14/">http://www.me.berkeley.edu/ME233/sp14/</a></i></p>
<dt>&bull;</p>
<dd> VOR: <i><a rel="nofollow" href="http://www.vor-cycling.be/">http://www.vor-cycling.be/</a></i></dl>
<h3>Books produced using Sphinx</h3>
<dl>
<dt>&bull;</p>
<dd> &quot;The <code>repoze.bfg</code> Web Application Framework&quot;: <i><a rel="nofollow" href="http://www.amazon.com/repoze-bfg-Web-Application-Framework-Version/dp/0615345379">http://www.amazon.com/repoze-bfg-Web-Application-Framework-Version/dp/0615345379</a></i></p>
<dt>&bull;</p>
<dd> A Theoretical Physics Reference book: <i><a rel="nofollow" href="http://theoretical-physics.net/">http://theoretical-physics.net/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Simple and Steady Way of Learning for Software Engineering&quot; (in Japanese): <i><a rel="nofollow" href="http://www.amazon.co.jp/dp/477414259X/">http://www.amazon.co.jp/dp/477414259X/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Expert Python Programming&quot;: <i><a rel="nofollow" href="http://www.packtpub.com/expert-python-programming/book">http://www.packtpub.com/expert-python-programming/book</a></i></p>
<dt>&bull;</p>
<dd> &quot;Expert Python Programming&quot; (Japanese translation): <i><a rel="nofollow" href="http://www.amazon.co.jp/dp/4048686291/">http://www.amazon.co.jp/dp/4048686291/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Pomodoro Technique Illustrated&quot; (Japanese translation): <i><a rel="nofollow" href="http://www.amazon.co.jp/dp/4048689525/">http://www.amazon.co.jp/dp/4048689525/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Python Professional Programming&quot; (in Japanese): <i><a rel="nofollow" href="http://www.amazon.co.jp/dp/4798032948/">http://www.amazon.co.jp/dp/4798032948/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Die Wahrheit des Sehens. Der DEKALOG von Krzysztof KieÅlowski&quot;: <i><a rel="nofollow" href="http://www.hasecke.eu/Dekalog/">http://www.hasecke.eu/Dekalog/</a></i></p>
<dt>&bull;</p>
<dd> The &quot;Varnish Book&quot;: <i><a rel="nofollow" href="https://www.varnish-software.com/static/book/">https://www.varnish-software.com/static/book/</a></i></p>
<dt>&bull;</p>
<dd> &quot;Learning Sphinx&quot; (in Japanese): <i><a rel="nofollow" href="http://www.oreilly.co.jp/books/9784873116488/">http://www.oreilly.co.jp/books/9784873116488/</a></i></dl>
<h3>Thesis using Sphinx</h3>
<dl>
<dt>&bull;</p>
<dd> &quot;A Web-Based System for Comparative Analysis of OpenStreetMap Data by the Use of CouchDB&quot;: <i><a rel="nofollow" href="http://gisforge.no-ip.org/files/MasterThesis_MarkusMayr_0542042.pdf">http://gisforge.no-ip.org/files/MasterThesis_MarkusMayr_0542042.pdf</a></i></p>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></p>
<dt>&bull;</p>
<dd> <i>glossary</i></dl>
<h2>AUTHOR</h2>
<p> Georg Brandl</p>
<h2>COPYRIGHT</h2>
<p> 2007-2014, Georg Brandl and the Sphinx team </p>
<h2>Index</h2>
<dt><a href="#lbAH">FIRST STEPS WITH SPHINX</a></p>
<dd>
<dt><a href="#lbAS">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbAT">INVOCATION OF SPHINX-BUILD</a></p>
<dd>
<dt><a href="#lbAV">INVOCATION OF SPHINX-APIDOC</a></p>
<dd>
<dt><a href="#lbAW">RESTRUCTUREDTEXT PRIMER</a></p>
<dd>
<dt><a href="#lbBP">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbBQ">SPHINX MARKUP CONSTRUCTS</a></p>
<dd>
<dt><a href="#lbBT">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbCB">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbCR">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbCS">SPHINX DOMAINS</a></p>
<dd>
<dt><a href="#lbDH">AVAILABLE BUILDERS</a></p>
<dd>
<dt><a href="#lbDK">THE BUILD CONFIGURATION FILE</a></p>
<dd>
<dt><a href="#lbDW">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbDX">INTERNATIONALIZATION</a></p>
<dd>
<dt><a href="#lbEF">FOOTNOTES</a></p>
<dd>
<dt><a href="#lbEG">HTML THEMING SUPPORT</a></p>
<dd>
<dt><a href="#lbEM">TEMPLATING</a></p>
<dd>
<dt><a href="#lbEU">SPHINX EXTENSIONS</a></p>
<dd>
<dt><a href="#lbFV">DEVELOPING EXTENSIONS FOR SPHINX</a></p>
<dd>
<dt><a href="#lbHC">SPHINX WEB SUPPORT</a></p>
<dd>
<dt><a href="#lbHQ">SPHINX FAQ</a></p>
<dd>
<dt><a href="#lbHX">GLOSSARY</a></p>
<dd>
<dt><a href="#lbHY">SPHINX DEVELOPER&#8217;S GUIDE</a></p>
<dd>
<dt><a href="#lbIH">CHANGES IN SPHINX</a></p>
<dd>
<dt><a href="#lbKA">PROJECTS USING SPHINX</a></p>
<dd>
<dt><a href="#lbKJ">AUTHOR</a></p>
<dd>
<dt><a href="#lbKK">COPYRIGHT</a></p>
<dd></dl>
