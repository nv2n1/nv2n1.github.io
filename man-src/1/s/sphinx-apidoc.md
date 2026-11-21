---

title: "sphinx-apidoc(1)"
name: "sphinx-apidoc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphinx-apidoc/"
description: "sphinx-apidoc – Sphinx API doc generator tool"
---

<h2>NAME</h2>
<p> sphinx-apidoc &#8211; Sphinx API doc generator tool</p>
<p> <code>sphinx-apidoc</code> [<i>options</i>] -o &lt;<i>outputdir</i>&gt; &lt;<i>sourcedir</i>&gt; [<i>pathnames</i> &#8230;]</p>
<p> <code>sphinx-apidoc</code> is a tool for automatic generation of Sphinx sources that, using the autodoc extension, document a whole package in the style of other automatic API documentation tools. </p>
<p> <i>sourcedir</i> must point to a Python package. Any <i>pathnames</i> given are paths to be excluded from the generation. </p>
<p> <code>WARNING:</code> <code>sphinx-apidoc</code> generates source files that use <code>sphinx.ext.autodoc</code> to document all found modules. If any modules have side effects on import, these will be executed by <code>autodoc</code> when <code>sphinx-build</code> is run. </p>
<p> If you document scripts (as opposed to library modules), make sure their main routine is protected by a <code>if __name__ == &#8216;__main__&#8217;</code> condition.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i>&nbsp;<wbr>&lt;outputdir&gt;</i></dt>
<dd> Directory to place the output files. If it does not exist, it is created.</dd>
<dt><code>-f</code>,<code> &#8211;force</code></dt>
<dd> Usually, apidoc does not overwrite files, unless this option is given.</dd>
<dt><code>-l</code>,<code> &#8211;follow-links</code></dt>
<dd> Follow symbolic links.</dd>
<dt><code>-n</code>,<code> &#8211;dry-run</code></dt>
<dd> If given, apidoc does not create any files.</dd>
<dt><code>-s</code><i>&nbsp;<wbr>&lt;suffix&gt;</i></dt>
<dd> Suffix for the source files generated, default is <code>rst</code>.</dd>
<dt><code>-d</code><i>&nbsp;<wbr>&lt;maxdepth&gt;</i></dt>
<dd> Maximum depth for the generated table of contents file.</dd>
<dt><code>-T</code>,<code> &#8211;no-toc</code></dt>
<dd> Do not create a table of contents file.</dd>
<dt><code>-F</code>,<code> &#8211;full</code></dt>
<dd> If given, a full Sphinx project is generated (<code>conf.py</code>, <code>Makefile</code> etc.) using sphinx-quickstart.</dd>
<dt><code>-e</code>,<code> &#8211;separate</code></dt>
<dd> Put each module file in its own page.</dd>
<dt><code>-E</code>,<code> &#8211;no-headings</code></dt>
<dd> Don&#8217;t create headings for the modules/packages</dd>
<dt><code>-P</code>,<code> &#8211;private</code></dt>
<dd> Include &quot;_private&quot; modules </dd>
<p> These options are used with <code>-F</code>:</p>
<dt><code>-H</code><i>&nbsp;<wbr>&lt;project&gt;</i></dt>
<dd> Project name to put into the configuration.</dd>
<dt><code>-A</code><i>&nbsp;<wbr>&lt;author&gt;</i></dt>
<dd> Author name(s) to put into the configuration.</dd>
<dt><code>-V</code><i>&nbsp;<wbr>&lt;version&gt;</i></dt>
<dd> Project version.</dd>
<dt><code>-R</code><i>&nbsp;<wbr>&lt;release&gt;</i></dt>
<dd> Project release.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sphinx-build/">sphinx-build</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Etienne Desautels, &lt;<i>etienne.desautels [at] gmail.com</i>&gt;, Georg Brandl &lt;<i>georg [at] python.org</i>&gt; et al.</p>
<h2>COPYRIGHT</h2>
<p> 2007-2014, Georg Brandl and the Sphinx team </p>
