---

title: "sphinx-build(1)"
name: "sphinx-build"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphinx-build/"
description: "sphinx-build – Sphinx documentation generator tool"
---

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
<dt><code>html</code></dt>
<dd> HTML file generation. This is the default builder.</dd>
<dt><code>dirhtml</code></dt>
<dd> HTML file generation with every HTML file named &quot;index.html&quot; in a separate directory.</dd>
<dt><code>singlehtml</code></dt>
<dd> HTML file generation with all content in a single HTML file.</dd>
<dt><code>htmlhelp</code></dt>
<dd> Generates files for CHM (compiled help files) generation.</dd>
<dt><code>qthelp</code></dt>
<dd> Generates files for Qt help collection generation.</dd>
<dt><code>devhelp</code></dt>
<dd> Generates files for the GNOME Devhelp help viewer.</dd>
<dt><code>latex</code></dt>
<dd> Generates LaTeX output that can be compiled to a PDF document.</dd>
<dt><code>man</code></dt>
<dd> Generates manual pages.</dd>
<dt><code>texinfo</code></dt>
<dd> Generates Texinfo output that can be processed by <code>makeinfo</code> to generate an Info document.</dd>
<dt><code>epub</code></dt>
<dd> Generates an ePub e-book version of the HTML output.</dd>
<dt><code>text</code></dt>
<dd> Generates a plain-text version of the documentation.</dd>
<dt><code>gettext</code></dt>
<dd> Generates Gettext message catalogs for content translation.</dd>
<dt><code>changes</code></dt>
<dd> Generates HTML files listing changed/added/deprecated items for the current version of the documented project.</dd>
<dt><code>linkcheck</code></dt>
<dd> Checks the integrity of all external links in the source.</dd>
<dt><code>pickle / json</code></dt>
<dd> Generates serialized HTML files for use in web applications.</dd>
<dt><code>xml</code></dt>
<dd> Generates Docutils-native XML files.</dd>
<dt><code>pseudoxml</code></dt>
<dd> Generates compact pretty-printed &quot;pseudo-XML&quot; files displaying the internal structure of the intermediate document trees.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>&lt;builder&gt;</i></dt>
<dd> Builder to use; defaults to html. See the full list of builders above.</dd>
<dt><code>-a</code></dt>
<dd> Generate output for all files; without this option only output for new and changed files is generated.</dd>
<dt><code>-E</code></dt>
<dd> Ignore cached files, forces to re-read all source files from disk.</dd>
<dt><code>-d</code><i>&nbsp;<wbr>&lt;path&gt;</i></dt>
<dd> Path to cached files; defaults to &lt;outdir&gt;/.doctrees.</dd>
<dt><code>-j</code><i>&nbsp;<wbr>&lt;N&gt;</i></dt>
<dd> Build in parallel with N processes where possible.</dd>
<dt><code>-c</code><i>&nbsp;<wbr>&lt;path&gt;</i></dt>
<dd> Locate the conf.py file in the specified path instead of &lt;sourcedir&gt;.</dd>
<dt><code>-C</code></dt>
<dd> Specify that no conf.py file at all is to be used. Configuration can only be set with the -D option.</dd>
<dt><code>-D</code><i>&nbsp;<wbr>&lt;setting=value&gt;</i></dt>
<dd> Override a setting from the configuration file.</dd>
<dt><code>-t</code><i>&nbsp;<wbr>&lt;tag&gt;</i></dt>
<dd> Define <i>tag</i> for use in &quot;only&quot; blocks.</dd>
<dt><code>-A</code><i>&nbsp;<wbr>&lt;name=value&gt;</i></dt>
<dd> Pass a value into the HTML templates (only for HTML builders).</dd>
<dt><code>-n</code></dt>
<dd> Run in nit-picky mode, warn about all missing references.</dd>
<dt><code>-v</code></dt>
<dd> Increase verbosity (can be repeated).</dd>
<dt><code>-N</code></dt>
<dd> Prevent colored output.</dd>
<dt><code>-q</code></dt>
<dd> Quiet operation, just print warnings and errors on stderr.</dd>
<dt><code>-Q</code></dt>
<dd> Very quiet operation, don&#8217;t print anything except for errors.</dd>
<dt><code>-w</code><i>&nbsp;<wbr>&lt;file&gt;</i></dt>
<dd> Write warnings and errors into the given file, in addition to stderr.</dd>
<dt><code>-W</code></dt>
<dd> Turn warnings into errors.</dd>
<dt><code>-T</code></dt>
<dd> Show full traceback on exception.</dd>
<dt><code>-P</code></dt>
<dd> Run Pdb on exception.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sphinx-quickstart/">sphinx-quickstart</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Georg Brandl &lt;<i>georg [at] python.org</i>&gt;, Armin Ronacher &lt;<i>armin.ronacher [at] active-4.com</i>&gt; et al. </p>
<p> This manual page was initially written by Mikhail Gusarov &lt;<i>dottedmag [at] dottedmag.net</i>&gt;, for the Debian project.</p>
<h2>COPYRIGHT</h2>
<p> 2007-2014, Georg Brandl and the Sphinx team </p>
