---
title: "epydoc(1)"
name: "epydoc"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epydoc/"
description: "epydoc – generate API documentation from Python docstrings"
---

<h2>NAME</h2>
<p> epydoc &#8211; generate API documentation from Python docstrings</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>epydoc</code> [<code>action</code>] [<code>options</code>] <i>names&#8230;</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>epydoc</code></p>
<dd>generates API documentation for Python modules and packages, based on their docstrings. A lightweight markup language called <code>epytext</code> can be used to format docstrings, and to add information about specific fields, such as parameters and instance variables. Epydoc also understands docstrings written in ReStructuredText, Javadoc, and plaintext. Currently, epydoc supports two basic output formats: HTML and LaTeX. </p>
<p> The HTML API documentation produced by <code>epydoc</code> consists of a set of HTML files, including: an API documentation page for each class and module; a syntax-highlighted source code page for each module; an identifier index page; a help page; and a frames-based table of contents. When appropriate, <code>epydoc</code> will also generate index pages for bugs, defined terms, and to-do items; a class hierarchy page; and a package hierarchy page. </p>
<p> The LaTeX API documentation produced by <code>epydoc</code> consists of a main LaTeX file, and a LaTeX file for each module. If you use <code>&#8211;dvi</code>, <code>&#8211;ps</code>, or <code>&#8211;pdf ,</code> then <code>epydoc</code> will invoke external commands to convert the LaTeX output to the requested format. Note that the LaTeX files containing the documentation for individual modules can be included as chapters or sections of other LaTeX documents, using the LaTeX <code>\include</code> command. If you wish to include individual classes in other LaTeX documents, then use the <code>&#8211;separate-classes</code> option to produce a separate LaTeX file for each class. </p>
<p> <code>epydoc</code> can also be used to check the completeness of the API documentation. By default, it checks that every public package, module, class, method, and function has a docstring description. The <code>&#8211;tests</code> option can be used to specify additional tests to perform. </p>
<h2>OPTIONS</h2>
<p> Epydoc&#8217;s options are divided into six categories: basic options, actions, generation options, output options, graph options, and return value options. </p>
<p> <code>BASIC OPTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>names</i>&#8230;</p>
<dd> The list of objects that should be documented. Objects can be specified using Python dotted names (such as <code>os.path</code>), filenames (such as <code>epydoc/epytext.py</code>), or directory names (such as <code>epydoc/</code>). Directory names specify packages, and are expanded to include all sub-modules and sub-packages. If you wish to exclude certain sub-modules or sub-packages, use the <code>&#8211;exclude</code> option (described below).</p>
<dt><code>&#8211;config </code><i>file</i></p>
<dd> A configuration file, specifying additional <code>options</code>and/or<code>names</code>. This option may be repeated.</p>
<dt><code>&#8211;q, &#8211;quiet, &#8211;v, &#8211;verbose</code></p>
<dd> Produce quite (or verbose) output. If used multiple times, this option produces successively more quiet (or verbose) output.</p>
<dt><code>&#8211;debug</code></p>
<dd> Show full tracebacks for internal errors.</p>
<dt><code>&#8211;simple-term</code></p>
<dd> Do not try to use color or cursor control when displaying the progress bar, warnings, or errors.</dl>
</dl>
<p> <code>ACTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;html</code></p>
<dd> Write HTML output. <code>[default]</code></p>
<dt><code>&#8211;latex</code></p>
<dd> Write LaTeX output.</p>
<dt><code>&#8211;dvi</code></p>
<dd> Write DVI output.</p>
<dt><code>&#8211;ps</code></p>
<dd> Write Postscript output.</p>
<dt><code>&#8211;pdf</code></p>
<dd> Write Adobe Acrobat (pdf) output.</p>
<dt><code>&#8211;check</code></p>
<dd> Perform completeness checks on the documentation.</p>
<dt><code>&#8211;pickle</code></p>
<dd> Write the documentation to a pickle file.</dl>
</dl>
<p> <code>GENERATION OPTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;docformat </code><i>format</i></p>
<dd> Set the default value for <code>__docformat__</code> to <i>format</i>. <code>__docformat__</code> is a module variable that specifies the markup language for the docstrings in a module. Its value consists of the name of a markup language, optionally followed by a language code (such as <code>en</code> for English). For a list of the markup languages currently recognized by epydoc, run <code>epydoc &#8211;help docformat</code>.</p>
<dt><code>&#8211;parse-only</code></p>
<dd> Gather all information about the documented objects by parsing the relevant Python source code; in particular, do <i>not</i> use introspection to gather information about the documented objects. This option should be used when epydoc is run on untrusted code; or on code that can not be introspected because of missing dependencies, or because importing it would cause undesired side-effects.</p>
<dt><code>&#8211;introspect-only</code></p>
<dd> Gather all information about the documented objects by introspection; in particular, do <i>not</i> gather information by parsing the object&#8217;s Python source code.</p>
<dt><code>&#8211;exclude </code><i>PATTERN</i></p>
<dd> Do not document any object whose name matches the given regular expression pattern.</p>
<dt><code>&#8211;exclude-introspect </code><i>PATTERN</i></p>
<dd> Do not use introspection to gather information about any object whose name matches the given regular expression.</p>
<dt><code>&#8211;exclude-parse </code><i>PATTERN</i></p>
<dd> Do not use Python source code parsing to gather information about any object whose name matches the given regular expression.</p>
<dt><code>&#8211;inheritance </code><i>format</i></p>
<dd> The format that should be used to display inherited methods, variables, and properties in the generated &quot;summary&quot; tables. If <i>format</i> is &quot;grouped,&quot; then inherited objects are gathered into groups, based on which class that they are inherited from. If <i>format</i> is &quot;listed,&quot; then inherited objects are listed in a short list at the end of the summary table. If <i>format</i> is &quot;included,&quot; then inherited objects are mixed in with non-inherited objects. The default format for HTML output is &quot;grouped.&quot;</p>
<dt><code>&#8211;show-private, &#8211;no-private</code></p>
<dd> These options control whether documentation is generated for private objects. By default, the generated documentation includes private objects, and users can choose whether to view private objects or not, by clicking on &quot;show private&quot; and &quot;hide private&quot; links. But if you want to discourage users from directly accessing private objects, then you may prefer not to generate documentation for private objects.</p>
<dt><code>&#8211;show-imports, &#8211;no-imports</code></p>
<dd> These options control whether module imports are included in the generated documentation. By default, imports are not included.</p>
<dt><code>&#8211;show-sourcecode, &#8211;no-sourcecode</code></p>
<dd> These options control whether or not epydoc should generate syntax-highlighted pages containing the souce code of each module in the HTML output. By default, the sourcecode pages are generated.</p>
<dt><code>&#8211;include-log</code></p>
<dd> Generate an HTML page <code>epydoc-log.html</code> containing all error and warning messages that are generated by epydoc, and include it in the generated output.</dl>
</dl>
<p> <code>OUTPUT OPTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-o </code><i>dir</i><code>, &#8211;output </code><i>dir</i></p>
<dd> The output directory. If <code>dir</code> does not exist, then it will be created. If no output directory is specified, then the action name (e.g., <code>html</code> or <code>pdf</code>). <code>html</code></p>
<dt><code>-c </code><i>sheet</i><code>, &#8211;css </code><i>sheet</i></p>
<dd> CSS stylesheet for HTML output files. If <i>sheet</i> is a file, then the stylesheet is copied from that file; otherwise, <i>sheet</i> is taken to be the name of a built-in stylesheet. For a list of the built-in stylesheets, run <code>epydoc &#8211;help css</code>. If a CSS stylesheet is not specified, then the default stylesheet is used.</p>
<dt><code>-n </code><i>name</i><code>, &#8211;name </code><i>name</i></p>
<dd> The name of the project whose documentation is being generated.</p>
<dt><code>-u </code><i>url</i><code>, &#8211;url </code><i>url</i></p>
<dd> The URL of the project&#8217;s homepage.</p>
<dt>
<dd>
<dt><code>&#8211;navlink </code><i>html</i></p>
<dd> HTML code for the homepage link on the HTML navigation bar. If this HTML code contains any hyperlinks (<code>&lt;a href=&#8230;&gt;</code>), then it will be inserted verbatim. If it does not contain any hyperlinks, and a project url is specified (with <code>&#8211;url</code>), then a hyperlink to the specified URL is added to the link.</p>
<dt><code>&#8211;help-file </code><i>file</i></p>
<dd> An alternate help file. <code>file</code> should contain the body of an HTML file &#8212; navigation bars will be added to it.</p>
<dt><code>&#8211;show-frames, &#8211;no-frames</code></p>
<dd> These options control whether HMTL output will include a frames-base table of contents page. By default, the frames-based table of contents is included.</p>
<dt><code>&#8211;separate-classes</code></p>
<dd> In the LaTeX output, describe each class in a separate section of the documentation, instead of including them in the documentation for their modules. This creates a separate LaTeX file for each class, so it can also be useful if you want to include the documentation for one or two classes as sections of your own LaTeX document.</dl>
</dl>
<p> <code>GRAPH OPTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;graph </code><i>graphtype</i></p>
<dd> Include graphs of type <code>graphtype</code> in the generated output. Graphs are generated using the Graphviz dot executable. If this executable is not on the path, then use <code>&#8211;dotpath</code> to specify its location. This option may be repeated to include multiple graph types in the output. <code>graphtype</code> should be one of: <code>all</code>, <code>classtree</code>, <code>callgraph</code>, or <code>umlclasstree</code>.</p>
<dt><code>&#8211;dotpath </code><i>path</i></p>
<dd> The path to the Graphviz <code>dot</code> executable.</p>
<dt><code>&#8211;graph-font </code><i>font</i></p>
<dd> The name of the font used to generate Graphviz graphs. (e.g., helvetica or times).</p>
<dt><code>&#8211;graph-font-size </code><i>size</i></p>
<dd> The size of the font used to generate Graphviz graphs, in points.</p>
<dt><code>&#8211;pstat </code><i>file</i></p>
<dd> A pstat output file, to be used in generating call graphs.</dl>
</dl>
<p> <code>RETURN VALUE OPTIONS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;fail-on-error</code></p>
<dd> Return a non-zero exit status, indicating failure, if any errors are encountered.</p>
<dt><code>&#8211;fail-on-warning</code></p>
<dd> Return a non-zero exit status, indicating failure, if any errors or warnings are encountered (not including docstring warnings).</p>
<dt><code>&#8211;fail-on-docstring-warning</code></p>
<dd> Return a non-zero exit status, indicating failure, if any errors or warnings are encountered (including docstring warnings).</dl>
</dl>
<h2>HTML FILES</h2>
<p> The HTML API documentation produced by <code>epydoc</code> consists of the following files: </p>
<p> <code>OBJECT DOCUMENTATION PAGES</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>index.html</code></p>
<dd> The standard entry point for the documentation. Normally, <code>index.html</code> is a copy of the frames file (<code>frames.html</code>). But if the <code>&#8211;no-frames</code> option is used, then <code>index.html</code> is a copy of the API documentation home page, which is normally the documentation page for the top-level package or module (or the trees page if there is no top-level package or module).</p>
<dt><i>module</i><code>-module.html</code></p>
<dd> The API documentation for a module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>.</p>
<dt><i>class</i><code>-class.html</code></p>
<dd> The API documentation for a class, exception, or type. <i>class</i> is the complete dotted name of the class, such as <code>epydoc.epytext.Token</code> or <code>array.ArrayType</code>.</p>
<dt><i>module</i><code>-pysrc.html</code></p>
<dd> A syntax-highlighted page containing the Python source code for <i>module</i>. This page includes links back to the API documentation pages.</p>
<dt><code>module-tree.html</code></p>
<dd> The module hierarchy.</p>
<dt><code>class-tree.html</code></p>
<dd> The class hierarchy. This page is only generated if at least one class is documented.</dl>
</dl>
<p> <code>INDICES</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>identifier-index.html</code></p>
<dd> An index of all documented identifiers. If the identifier index contains more than 3,000 entries, then it will be split into separate pages for each letter, named <code>identifier-index-a.html</code>, <code>identifier-index-b.html</code>, etc.</p>
<dt><code>term-index.html</code></p>
<dd> An index of all explicitly marked definitional terms. This page is only generated if at least one definition term is marked in a formatted docstring.</p>
<dt><code>bug-index.html</code></p>
<dd> An index of all explicitly marked <code>@bug</code> fields. This page is only generated if at least one <code>@bug</code> field is listed in a formatted docstring.</p>
<dt><code>todo-index.html</code></p>
<dd> An index of all explicitly marked <code>@todo</code> fields. This page is only generated if at least one <code>@todo</code> field is listed in a formatted docstring.</p>
<dt><code>changed-index.html</code></p>
<dd> An index of all explicitly marked <code>@changed</code> fields. This page is only generated if at least one <code>@changed</code> field is listed in a formatted docstring.</p>
<dt><code>deprecated-index.html</code></p>
<dd> An index of all explicitly marked <code>@deprecated</code> fields. This page is only generated if at least one <code>@deprecated</code> field is listed in a formatted docstring.</p>
<dt><code>since-index.html</code></p>
<dd> An index of all explicitly marked <code>@since</code> fields. This page is only generated if at least one <code>@since</code> field is listed in a formatted docstring.</dl>
</dl>
<p> <code>FRAMES-BASED TABLE OF CONTENTS</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>frames.html</code></p>
<dd> The main frames file. Two frames on the left side of the window contain a table of contents, and the main frame on the right side of the window contains API documentation pages.</p>
<dt><code>toc.html</code></p>
<dd> The top-level table of contents page. This page is displayed in the upper-left frame of <code>frames.html</code>, and provides links to the <code>toc-everything.html</code> and <code>toc-</code><i>module</i><code>-module.html</code> pages.</p>
<dt><code>toc-everything.html</code></p>
<dd> The table of contents for the entire project. This page is displayed in the lower-left frame of <code>frames.html</code>, and provides links to every class, type, exception, function, and variable defined by the project.</p>
<dt><code>toc-</code><i>module</i><code>-module.html</code></p>
<dd> The table of contents for a module. This page is displayed in the lower-left frame of <code>frames.html</code>, and provides links to every class, type, exception, function, and variable defined by the module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>.</dl>
</dl>
<p> <code>OTHER PAGES</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>help.html</code></p>
<dd> The help page for the project. This page explains how to use and navigate the webpage produced by epydoc.</p>
<dt><code>redirect.html</code></p>
<dd> This page uses javascript to translate dotted names to their corresponding URLs. For example, in epydoc&#8217;s documentation, loading the page <code>&lt;redirect.html#epydoc.apidoc.DottedName&gt;</code> will automatically redirect the browser to <code>&lt;epydoc.apidoc-module.html#DottedName&gt;</code>.</p>
<dt><code>epydoc.css</code></p>
<dd> The CSS stylesheet used to display all HTML pages.</p>
<dt><code>epydoc.js</code></p>
<dd> A javascript file used to define javascript functions used by epydoc.</p>
<dt><code>epydoc-log.html</code></p>
<dd> A page containing a log of all warnings and errors that were generated by epydoc, along with a table listing all of the options that were used.</dl>
</dl>
<h2>LATEX FILES</h2>
<p> The LaTeX API documentation produced by <code>epydoc</code> consists of the following files:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>api.pdf</code></p>
<dd> An Adobe Acrobat (pdf) file containing the complete API documentation. This file is only generated if you use the <code>&#8211;pdf</code> option.</p>
<dt><code>api.tex</code></p>
<dd> The top-level LaTeX file. This file imports the other LaTeX files, to create a single unified document.</p>
<dt><code>api.dvi</code></p>
<dd> A dvi file containing the complete API documentation. This file is only generated if you use the <code>&#8211;dvi</code> option, the <code>&#8211;ps</code> option, or the <code>&#8211;pdf</code> option.</p>
<dt><code>api.ps</code></p>
<dd> A postscript file containing the complete API documentation. This file is only generated if you use the <code>&#8211;ps</code> option or the <code>&#8211;pdf</code> option.</p>
<dt><i>module</i><code>-module.tex</code></p>
<dd> The API documentation for a module. <i>module</i> is the complete dotted name of the module, such as <code>sys or</code> <code>epydoc.epytext</code>.</p>
<dt><i>class</i><code>-class.tex</code></p>
<dd> The API documentation for a class, exception, or type. <i>class</i> is the complete dotted name of the class, such as <code>epydoc.epytext.Token</code> or array.ArrayType. These class documentation files are only created if the <code>&#8211;separate-classes</code> option is used; otherwise, the documentation for each class is included in its module&#8217;s documentation file.</dl>
</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>EPYTEXT MARKUP WARNING MESSAGES</code></p>
<dl>
<dt>
<dd> Epytext errors are caused by epytext docstrings that contain invalid markup. Whenever an epytext error is detected, the docstring in question is treated as a plaintext docstring. Epydoc can generate the following epytext errors:</p>
<dl>
<dt><code>Bad link target.</code></p>
<dd> The target specified for an inline link contruction (<code>L{&#8230;}</code>) is not well-formed. Link targets must be valid python identifiers.</p>
<dt><code>Bad uri target.</code></p>
<dd> The target specified for an inline uri contruction (<code>U{&#8230;}</code>) is not well-formed. This typically occurs if inline markup is nested inside the URI target.</p>
<dt><code>Fields must be at the top level.</code></p>
<dd> The list of fields (<code>@param</code>, etc.) is contained by some other block structure (such as a list or a section).</p>
<dt><code>Fields must be the final elements.</code></p>
<dd> The list of fields (<code>@param</code>, etc.) is not at the end of a docstring.</p>
<dt><code>Headings must occur at top level.</code></p>
<dd> The heading is contianed in some other block structure (such as a list).</p>
<dt><code>Improper doctest block indentation.</code></p>
<dd> The doctest block dedents past the indentation of its initial prompt line.</p>
<dt><code>Improper heading indentation.</code></p>
<dd> The heading for a section is not left-aligned with the paragraphs in the section that contains it.</p>
<dt><code>Improper paragraph indentation.</code></p>
<dd> The paragraphs within a block are not left-aligned. This error is often generated when plaintext docstrings are parsed using epytext.</p>
<dt><code>Invalid escape.</code></p>
<dd> An unknown escape sequence was used with the inline escape construction (<code>E{&#8230;}</code>).</p>
<dt><code>Lists must be indented.</code></p>
<dd> An unindented line immediately following a paragraph starts with a list bullet. Epydoc is not sure whether you meant to start a new list item, or meant for a paragraph to include a word that looks like a bullet. If you intended the former, then indent the list. If you intended the latter, then change the word-wrapping of the paragraph, or escape the first character of the word that looks like a bullet.</p>
<dt><code>Unbalanced &#8216;{&#8216;.</code></p>
<dd> The docstring contains unbalanced braces. Epytext requires that all braces must be balanced. To include a single unbalanced brace, use the escape sequences E{lb} (left brace) and E{rb} (right brace).</p>
<dt><code>Unbalanced &#8216;}&#8217;.</code></p>
<dd> The docstring contains unbalanced braces. Epytext requires that all braces must be balanced. To include a single unbalanced brace, use the escape sequences E{lb} (left brace) and E{rb} (right brace).</p>
<dt><code>Unknown inline markup tag.</code></p>
<dd> An unknown tag was used with the inline markup construction ( <i>x</i><code>{&#8230;}</code> ).</p>
<dt><code>Wrong underline character for heading.</code></p>
<dd> The underline character used for this section heading does not indicate an appopriate section level. The &quot;=&quot; character should be used to underline sections; &quot;-&quot; for subsections; and &quot;~&quot; for subsubsections.</p>
<dt><code>Possible mal-formatted field item.</code></p>
<dd> Epytext detected a line that looks like a field item, but is not correctly formatted. This typically occurs when the trailing colon (&quot;:&quot;) is not included in the field tag.</p>
<dt><code>Possible heading typo.</code></p>
<dd> Epytext detected a pair of lines that looks like a heading, but the number of underline characters does not match the number of characters in the heading. The number of characters in these two lines must match exactly for them to be considered a heading.</dl>
</dl>
<p> <code>FIELD WARNINGS</code></p>
<dl>
<dt>
<dd> Field warnings are caused by docstrings containing invalid fields. The contents of the invalid field are generally ignored. Epydoc can generate the following field warnings:</p>
<dl>
<dt><code>@param for unknown parameter </code><i>param</i><code>.</code></p>
<dd> A @param field was used to specify the type for a parameter that is not included in the function&#8217;s signature. This is typically caused by a typo in the parameter name.</p>
<dt><i>tag</i><code> did not expect an argument.</code></p>
<dd> The field tag <i>tag</i> was used with an argument, but it does not take one.</p>
<dt><i>tag</i><code> expected an argument.</code></p>
<dd> The field tag <i>tag</i> was used without an argument, but it requires one.</p>
<dt><code>@type for unknown parameter </code><i>param</i><code>.</code></p>
<dd> A @type field was used to specify the type for a parameter that is not included in the function&#8217;s signature. This is typically caused by a typo in the parameter name.</p>
<dt><code>@type for unknown variable </code><i>var</i><code>.</code></p>
<dd> A @type field was used to specify the type for a variable, but no other information is known about the variable. This is typically caused by a typo in the variable name.</p>
<dt><code>Unknown field tag </code><i>tag</i><code>.</code></p>
<dd> A docstring contains a field with the unknown tag <i>tag</i>.</p>
<dt><code>Redefinition of </code><i>field</i><code>.</code></p>
<dd> Multiple field tags define the value of <i>field</i> in the same docstring, but <i>field</i> can only take a single value.</dl>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>epydoc -n </code>epydoc<code> -u </code><a rel="nofollow" href="http://epydoc.sf.net">http://epydoc.sf.net</a> epydoc/</p>
<dd> Generate the HTML API documentation for the epydoc package and all of its submodules, and write the output to the <code>html</code> directory. In the headers and footers, use <code>epydoc</code> as the project name, and <code><a rel="nofollow" href="http://epydoc.sf.net">http://epydoc.sf.net</a></code> as the project URL.</p>
<dt><code>epydoc &#8211;pdf -n </code>epydoc<code> epydoc/</code></p>
<dd> Generate the LaTeX API documentation for the epydoc package and all of its submodules, and write the output to the <code>latex</code> directory.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful program execution.</p>
<dt><code>1</code></p>
<dd> Usage error.</p>
<dt><code>2</code></p>
<dd> Epydoc generated an error or warning, and one of the options <code>&#8211;fail-on-error</code><i>,</i> <code>&#8211;fail-on-warning</code><i>, or</i> <code>&#8211;fail-on-docstring-warning</code> was specified.</p>
<dt><code>other</code></p>
<dd> Internal error (Python exception).</dl>
<h2>AUTHOR</h2>
<p> Epydoc was written by Edward Loper. This man page was originally written by Moshe Zadka, and is currently maintained by Edward Loper.</p>
<h2>BUGS</h2>
<p> Report bugs to &lt;edloper [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-epydocgui/">epydocgui</a></code>(1)</p>
<dl>
<dt><code>The epydoc webpage</code></p>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net">http://epydoc.sourceforge.net</a>&gt;</p>
<dt><code>The epytext markup language manual</code></p>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net/epytext.html">http://epydoc.sourceforge.net/epytext.html</a>&gt; </p>
</dl>
<h2>Index</h2>
