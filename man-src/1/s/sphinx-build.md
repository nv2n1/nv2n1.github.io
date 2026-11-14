---
title: "sphinx-build(1)"
name: "sphinx-build"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphinx-build/"
description: "sphinx-build – Sphinx documentation generator tool"
---

<h2>NAME</h2>
<p> sphinx-build &#8211; Sphinx documentation generator tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sphinx-build</code> [<i>options</i>] &lt;<i>sourcedir</i>&gt; &lt;<i>outdir</i>&gt; [<i>filenames</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>sphinx-build</code> generates documentation from the files in <code>&lt;sourcedir&gt;</code> and places it in the <code>&lt;outdir&gt;</code>. </p>
<p> <code>sphinx-build</code> looks for <code>&lt;sourcedir&gt;/conf.py</code> for the configuration settings. <i><a href="/docs/linux/man/1-sphinx-quickstart/">sphinx-quickstart</a>(1)</i> may be used to generate template files, including <code>conf.py</code>. </p>
<p> <code>sphinx-build</code> can create documentation in different formats. A format is selected by specifying the builder name on the command line; it defaults to HTML. Builders can also perform other tasks related to documentation processing. </p>
<p> By default, everything that is outdated is built. Output only for selected files can be built by specifying individual filenames. </p>
<p> List of available builders:</p>
<dl>
<dt><code>html</code></p>
<dd> HTML file generation. This is the default builder.</p>
<dt><code>dirhtml</code></p>
<dd> HTML file generation with every HTML file named &quot;index.html&quot; in a separate directory.</p>
<dt><code>singlehtml</code></p>
<dd> HTML file generation with all content in a single HTML file.</p>
<dt><code>htmlhelp</code></p>
<dd> Generates files for CHM (compiled help files) generation.</p>
<dt><code>qthelp</code></p>
<dd> Generates files for Qt help collection generation.</p>
<dt><code>devhelp</code></p>
<dd> Generates files for the GNOME Devhelp help viewer.</p>
<dt><code>latex</code></p>
<dd> Generates LaTeX output that can be compiled to a PDF document.</p>
<dt><code>man</code></p>
<dd> Generates manual pages.</p>
<dt><code>texinfo</code></p>
<dd> Generates Texinfo output that can be processed by <code>makeinfo</code> to generate an Info document.</p>
<dt><code>epub</code></p>
<dd> Generates an ePub e-book version of the HTML output.</p>
<dt><code>text</code></p>
<dd> Generates a plain-text version of the documentation.</p>
<dt><code>gettext</code></p>
<dd> Generates Gettext message catalogs for content translation.</p>
<dt><code>changes</code></p>
<dd> Generates HTML files listing changed/added/deprecated items for the current version of the documented project.</p>
<dt><code>linkcheck</code></p>
<dd> Checks the integrity of all external links in the source.</p>
<dt><code>pickle / json</code></p>
<dd> Generates serialized HTML files for use in web applications.</p>
<dt><code>xml</code></p>
<dd> Generates Docutils-native XML files.</p>
<dt><code>pseudoxml</code></p>
<dd> Generates compact pretty-printed &quot;pseudo-XML&quot; files displaying the internal structure of the intermediate document trees.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>&lt;builder&gt;</i></p>
<dd> Builder to use; defaults to html. See the full list of builders above.</p>
<dt><code>-a</code></p>
<dd> Generate output for all files; without this option only output for new and changed files is generated.</p>
<dt><code>-E</code></p>
<dd> Ignore cached files, forces to re-read all source files from disk.</p>
<dt><code>-d</code><i>&nbsp;<wbr>&lt;path&gt;</i></p>
<dd> Path to cached files; defaults to &lt;outdir&gt;/.doctrees.</p>
<dt><code>-j</code><i>&nbsp;<wbr>&lt;N&gt;</i></p>
<dd> Build in parallel with N processes where possible.</p>
<dt><code>-c</code><i>&nbsp;<wbr>&lt;path&gt;</i></p>
<dd> Locate the conf.py file in the specified path instead of &lt;sourcedir&gt;.</p>
<dt><code>-C</code></p>
<dd> Specify that no conf.py file at all is to be used. Configuration can only be set with the -D option.</p>
<dt><code>-D</code><i>&nbsp;<wbr>&lt;setting=value&gt;</i></p>
<dd> Override a setting from the configuration file.</p>
<dt><code>-t</code><i>&nbsp;<wbr>&lt;tag&gt;</i></p>
<dd> Define <i>tag</i> for use in &quot;only&quot; blocks.</p>
<dt><code>-A</code><i>&nbsp;<wbr>&lt;name=value&gt;</i></p>
<dd> Pass a value into the HTML templates (only for HTML builders).</p>
<dt><code>-n</code></p>
<dd> Run in nit-picky mode, warn about all missing references.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity (can be repeated).</p>
<dt><code>-N</code></p>
<dd> Prevent colored output.</p>
<dt><code>-q</code></p>
<dd> Quiet operation, just print warnings and errors on stderr.</p>
<dt><code>-Q</code></p>
<dd> Very quiet operation, don&#8217;t print anything except for errors.</p>
<dt><code>-w</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd> Write warnings and errors into the given file, in addition to stderr.</p>
<dt><code>-W</code></p>
<dd> Turn warnings into errors.</p>
<dt><code>-T</code></p>
<dd> Show full traceback on exception.</p>
<dt><code>-P</code></p>
<dd> Run Pdb on exception.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sphinx-quickstart/">sphinx-quickstart</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Georg Brandl &lt;<i>georg [at] python.org</i>&gt;, Armin Ronacher &lt;<i>armin.ronacher [at] active-4.com</i>&gt; et al. </p>
<p> This manual page was initially written by Mikhail Gusarov &lt;<i>dottedmag [at] dottedmag.net</i>&gt;, for the Debian project.</p>
<h2>COPYRIGHT</h2>
<p> 2007-2014, Georg Brandl and the Sphinx team </p>
<h2>Index</h2>
