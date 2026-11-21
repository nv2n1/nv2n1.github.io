---

title: "epydoc(1)"
name: "epydoc"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epydoc/"
description: "epydoc – generate API documentation from Python docstrings"
---

<p> epydoc &#8211; generate API documentation from Python docstrings</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>epydoc</code> [<code>action</code>] [<code>options</code>] <i>names&#8230;</i></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>epydoc</code></p>
<dd>generates API documentation for Python modules and packages, based on their docstrings. A lightweight markup language called <code>epytext</code> can be used to format docstrings, and to add information about specific fields, such as parameters and instance variables. Epydoc also understands docstrings written in ReStructuredText, Javadoc, and plaintext. Currently, epydoc supports two basic output formats: HTML and LaTeX. </dd>
<p> The HTML API documentation produced by <code>epydoc</code> consists of a set of HTML files, including: an API documentation page for each class and module; a syntax-highlighted source code page for each module; an identifier index page; a help page; and a frames-based table of contents. When appropriate, <code>epydoc</code> will also generate index pages for bugs, defined terms, and to-do items; a class hierarchy page; and a package hierarchy page. </p>
<p> The LaTeX API documentation produced by <code>epydoc</code> consists of a main LaTeX file, and a LaTeX file for each module. If you use <code>&#8211;dvi</code>, <code>&#8211;ps</code>, or <code>&#8211;pdf ,</code> then <code>epydoc</code> will invoke external commands to convert the LaTeX output to the requested format. Note that the LaTeX files containing the documentation for individual modules can be included as chapters or sections of other LaTeX documents, using the LaTeX <code>\include</code> command. If you wish to include individual classes in other LaTeX documents, then use the <code>&#8211;separate-classes</code> option to produce a separate LaTeX file for each class. </p>
<p> <code>epydoc</code> can also be used to check the completeness of the API documentation. By default, it checks that every public package, module, class, method, and function has a docstring description. The <code>&#8211;tests</code> option can be used to specify additional tests to perform. </p>
<h2>OPTIONS</h2>
<p> Epydoc&#8217;s options are divided into six categories: basic options, actions, generation options, output options, graph options, and return value options. </p>
<p> <code>BASIC OPTIONS</code></p>
<dl>
<dl>
<dt><i>names</i>&#8230;</dt>
<dd> The list of objects that should be documented. Objects can be specified using Python dotted names (such as <code>os.path</code>), filenames (such as <code>epydoc/epytext.py</code>), or directory names (such as <code>epydoc/</code>). Directory names specify packages, and are expanded to include all sub-modules and sub-packages. If you wish to exclude certain sub-modules or sub-packages, use the <code>&#8211;exclude</code> option (described below).</dd>
<dt><code>&#8211;config </code><i>file</i></dt>
<dd> A configuration file, specifying additional <code>options</code>and/or<code>names</code>. This option may be repeated.</dd>
<dt><code>&#8211;q, &#8211;quiet, &#8211;v, &#8211;verbose</code></dt>
<dd> Produce quite (or verbose) output. If used multiple times, this option produces successively more quiet (or verbose) output.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Show full tracebacks for internal errors.</dd>
<dt><code>&#8211;simple-term</code></dt>
<dd> Do not try to use color or cursor control when displaying the progress bar, warnings, or errors.</dd></dl>
</dl>
<p> <code>ACTIONS</code></p>
<dl>
<dl>
<dt><code>&#8211;html</code></dt>
<dd> Write HTML output. <code>[default]</code></dd>
<dt><code>&#8211;latex</code></dt>
<dd> Write LaTeX output.</dd>
<dt><code>&#8211;dvi</code></dt>
<dd> Write DVI output.</dd>
<dt><code>&#8211;ps</code></dt>
<dd> Write Postscript output.</dd>
<dt><code>&#8211;pdf</code></dt>
<dd> Write Adobe Acrobat (pdf) output.</dd>
<dt><code>&#8211;check</code></dt>
<dd> Perform completeness checks on the documentation.</dd>
<dt><code>&#8211;pickle</code></dt>
<dd> Write the documentation to a pickle file.</dd></dl>
</dl>
<p> <code>GENERATION OPTIONS</code></p>
<dl>
<dl>
<dt><code>&#8211;docformat </code><i>format</i></dt>
<dd> Set the default value for <code>__docformat__</code> to <i>format</i>. <code>__docformat__</code> is a module variable that specifies the markup language for the docstrings in a module. Its value consists of the name of a markup language, optionally followed by a language code (such as <code>en</code> for English). For a list of the markup languages currently recognized by epydoc, run <code>epydoc &#8211;help docformat</code>.</dd>
<dt><code>&#8211;parse-only</code></dt>
<dd> Gather all information about the documented objects by parsing the relevant Python source code; in particular, do <i>not</i> use introspection to gather information about the documented objects. This option should be used when epydoc is run on untrusted code; or on code that can not be introspected because of missing dependencies, or because importing it would cause undesired side-effects.</dd>
<dt><code>&#8211;introspect-only</code></dt>
<dd> Gather all information about the documented objects by introspection; in particular, do <i>not</i> gather information by parsing the object&#8217;s Python source code.</dd>
<dt><code>&#8211;exclude </code><i>PATTERN</i></dt>
<dd> Do not document any object whose name matches the given regular expression pattern.</dd>
<dt><code>&#8211;exclude-introspect </code><i>PATTERN</i></dt>
<dd> Do not use introspection to gather information about any object whose name matches the given regular expression.</dd>
<dt><code>&#8211;exclude-parse </code><i>PATTERN</i></dt>
<dd> Do not use Python source code parsing to gather information about any object whose name matches the given regular expression.</dd>
<dt><code>&#8211;inheritance </code><i>format</i></dt>
<dd> The format that should be used to display inherited methods, variables, and properties in the generated &quot;summary&quot; tables. If <i>format</i> is &quot;grouped,&quot; then inherited objects are gathered into groups, based on which class that they are inherited from. If <i>format</i> is &quot;listed,&quot; then inherited objects are listed in a short list at the end of the summary table. If <i>format</i> is &quot;included,&quot; then inherited objects are mixed in with non-inherited objects. The default format for HTML output is &quot;grouped.&quot;</dd>
<dt><code>&#8211;show-private, &#8211;no-private</code></dt>
<dd> These options control whether documentation is generated for private objects. By default, the generated documentation includes private objects, and users can choose whether to view private objects or not, by clicking on &quot;show private&quot; and &quot;hide private&quot; links. But if you want to discourage users from directly accessing private objects, then you may prefer not to generate documentation for private objects.</dd>
<dt><code>&#8211;show-imports, &#8211;no-imports</code></dt>
<dd> These options control whether module imports are included in the generated documentation. By default, imports are not included.</dd>
<dt><code>&#8211;show-sourcecode, &#8211;no-sourcecode</code></dt>
<dd> These options control whether or not epydoc should generate syntax-highlighted pages containing the souce code of each module in the HTML output. By default, the sourcecode pages are generated.</dd>
<dt><code>&#8211;include-log</code></dt>
<dd> Generate an HTML page <code>epydoc-log.html</code> containing all error and warning messages that are generated by epydoc, and include it in the generated output.</dd></dl>
</dl>
<p> <code>OUTPUT OPTIONS</code></p>
<dl>
<dl>
<dt><code>-o </code><i>dir</i><code>, &#8211;output </code><i>dir</i></dt>
<dd> The output directory. If <code>dir</code> does not exist, then it will be created. If no output directory is specified, then the action name (e.g., <code>html</code> or <code>pdf</code>). <code>html</code></dd>
<dt><code>-c </code><i>sheet</i><code>, &#8211;css </code><i>sheet</i></dt>
<dd> CSS stylesheet for HTML output files. If <i>sheet</i> is a file, then the stylesheet is copied from that file; otherwise, <i>sheet</i> is taken to be the name of a built-in stylesheet. For a list of the built-in stylesheets, run <code>epydoc &#8211;help css</code>. If a CSS stylesheet is not specified, then the default stylesheet is used.</dd>
<dt><code>-n </code><i>name</i><code>, &#8211;name </code><i>name</i></dt>
<dd> The name of the project whose documentation is being generated.</dd>
<dt><code>-u </code><i>url</i><code>, &#8211;url </code><i>url</i></dt>
<dd> The URL of the project&#8217;s homepage.</dd>
<dt><code>&#8211;navlink </code><i>html</i></dt>
<dd> HTML code for the homepage link on the HTML navigation bar. If this HTML code contains any hyperlinks (<code>&lt;a href=&#8230;&gt;</code>), then it will be inserted verbatim. If it does not contain any hyperlinks, and a project url is specified (with <code>&#8211;url</code>), then a hyperlink to the specified URL is added to the link.</dd>
<dt><code>&#8211;help-file </code><i>file</i></dt>
<dd> An alternate help file. <code>file</code> should contain the body of an HTML file &#8212; navigation bars will be added to it.</dd>
<dt><code>&#8211;show-frames, &#8211;no-frames</code></dt>
<dd> These options control whether HMTL output will include a frames-base table of contents page. By default, the frames-based table of contents is included.</dd>
<dt><code>&#8211;separate-classes</code></dt>
<dd> In the LaTeX output, describe each class in a separate section of the documentation, instead of including them in the documentation for their modules. This creates a separate LaTeX file for each class, so it can also be useful if you want to include the documentation for one or two classes as sections of your own LaTeX document.</dd></dl>
</dl>
<p> <code>GRAPH OPTIONS</code></p>
<dl>
<dl>
<dt><code>&#8211;graph </code><i>graphtype</i></dt>
<dd> Include graphs of type <code>graphtype</code> in the generated output. Graphs are generated using the Graphviz dot executable. If this executable is not on the path, then use <code>&#8211;dotpath</code> to specify its location. This option may be repeated to include multiple graph types in the output. <code>graphtype</code> should be one of: <code>all</code>, <code>classtree</code>, <code>callgraph</code>, or <code>umlclasstree</code>.</dd>
<dt><code>&#8211;dotpath </code><i>path</i></dt>
<dd> The path to the Graphviz <code>dot</code> executable.</dd>
<dt><code>&#8211;graph-font </code><i>font</i></dt>
<dd> The name of the font used to generate Graphviz graphs. (e.g., helvetica or times).</dd>
<dt><code>&#8211;graph-font-size </code><i>size</i></dt>
<dd> The size of the font used to generate Graphviz graphs, in points.</dd>
<dt><code>&#8211;pstat </code><i>file</i></dt>
<dd> A pstat output file, to be used in generating call graphs.</dd></dl>
</dl>
<p> <code>RETURN VALUE OPTIONS</code></p>
<dl>
<dl>
<dt><code>&#8211;fail-on-error</code></dt>
<dd> Return a non-zero exit status, indicating failure, if any errors are encountered.</dd>
<dt><code>&#8211;fail-on-warning</code></dt>
<dd> Return a non-zero exit status, indicating failure, if any errors or warnings are encountered (not including docstring warnings).</dd>
<dt><code>&#8211;fail-on-docstring-warning</code></dt>
<dd> Return a non-zero exit status, indicating failure, if any errors or warnings are encountered (including docstring warnings).</dd></dl>
</dl>
<h2>HTML FILES</h2>
<p> The HTML API documentation produced by <code>epydoc</code> consists of the following files: </p>
<p> <code>OBJECT DOCUMENTATION PAGES</code></p>
<dl>
<dl>
<dt><code>index.html</code></dt>
<dd> The standard entry point for the documentation. Normally, <code>index.html</code> is a copy of the frames file (<code>frames.html</code>). But if the <code>&#8211;no-frames</code> option is used, then <code>index.html</code> is a copy of the API documentation home page, which is normally the documentation page for the top-level package or module (or the trees page if there is no top-level package or module).</dd>
<dt><i>module</i><code>-module.html</code></dt>
<dd> The API documentation for a module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>.</dd>
<dt><i>class</i><code>-class.html</code></dt>
<dd> The API documentation for a class, exception, or type. <i>class</i> is the complete dotted name of the class, such as <code>epydoc.epytext.Token</code> or <code>array.ArrayType</code>.</dd>
<dt><i>module</i><code>-pysrc.html</code></dt>
<dd> A syntax-highlighted page containing the Python source code for <i>module</i>. This page includes links back to the API documentation pages.</dd>
<dt><code>module-tree.html</code></dt>
<dd> The module hierarchy.</dd>
<dt><code>class-tree.html</code></dt>
<dd> The class hierarchy. This page is only generated if at least one class is documented.</dd></dl>
</dl>
<p> <code>INDICES</code></p>
<dl>
<dl>
<dt><code>identifier-index.html</code></dt>
<dd> An index of all documented identifiers. If the identifier index contains more than 3,000 entries, then it will be split into separate pages for each letter, named <code>identifier-index-a.html</code>, <code>identifier-index-b.html</code>, etc.</dd>
<dt><code>term-index.html</code></dt>
<dd> An index of all explicitly marked definitional terms. This page is only generated if at least one definition term is marked in a formatted docstring.</dd>
<dt><code>bug-index.html</code></dt>
<dd> An index of all explicitly marked <code>@bug</code> fields. This page is only generated if at least one <code>@bug</code> field is listed in a formatted docstring.</dd>
<dt><code>todo-index.html</code></dt>
<dd> An index of all explicitly marked <code>@todo</code> fields. This page is only generated if at least one <code>@todo</code> field is listed in a formatted docstring.</dd>
<dt><code>changed-index.html</code></dt>
<dd> An index of all explicitly marked <code>@changed</code> fields. This page is only generated if at least one <code>@changed</code> field is listed in a formatted docstring.</dd>
<dt><code>deprecated-index.html</code></dt>
<dd> An index of all explicitly marked <code>@deprecated</code> fields. This page is only generated if at least one <code>@deprecated</code> field is listed in a formatted docstring.</dd>
<dt><code>since-index.html</code></dt>
<dd> An index of all explicitly marked <code>@since</code> fields. This page is only generated if at least one <code>@since</code> field is listed in a formatted docstring.</dd></dl>
</dl>
<p> <code>FRAMES-BASED TABLE OF CONTENTS</code></p>
<dl>
<dl>
<dt><code>frames.html</code></dt>
<dd> The main frames file. Two frames on the left side of the window contain a table of contents, and the main frame on the right side of the window contains API documentation pages.</dd>
<dt><code>toc.html</code></dt>
<dd> The top-level table of contents page. This page is displayed in the upper-left frame of <code>frames.html</code>, and provides links to the <code>toc-everything.html</code> and <code>toc-</code><i>module</i><code>-module.html</code> pages.</dd>
<dt><code>toc-everything.html</code></dt>
<dd> The table of contents for the entire project. This page is displayed in the lower-left frame of <code>frames.html</code>, and provides links to every class, type, exception, function, and variable defined by the project.</dd>
<dt><code>toc-</code><i>module</i><code>-module.html</code></dt>
<dd> The table of contents for a module. This page is displayed in the lower-left frame of <code>frames.html</code>, and provides links to every class, type, exception, function, and variable defined by the module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>.</dd></dl>
</dl>
<p> <code>OTHER PAGES</code></p>
<dl>
<dl>
<dt><code>help.html</code></dt>
<dd> The help page for the project. This page explains how to use and navigate the webpage produced by epydoc.</dd>
<dt><code>redirect.html</code></dt>
<dd> This page uses javascript to translate dotted names to their corresponding URLs. For example, in epydoc&#8217;s documentation, loading the page <code>&lt;redirect.html#epydoc.apidoc.DottedName&gt;</code> will automatically redirect the browser to <code>&lt;epydoc.apidoc-module.html#DottedName&gt;</code>.</dd>
<dt><code>epydoc.css</code></dt>
<dd> The CSS stylesheet used to display all HTML pages.</dd>
<dt><code>epydoc.js</code></dt>
<dd> A javascript file used to define javascript functions used by epydoc.</dd>
<dt><code>epydoc-log.html</code></dt>
<dd> A page containing a log of all warnings and errors that were generated by epydoc, along with a table listing all of the options that were used.</dd></dl>
</dl>
<h2>LATEX FILES</h2>
<p> The LaTeX API documentation produced by <code>epydoc</code> consists of the following files:</p>
<dl>
<dl>
<dt><code>api.pdf</code></dt>
<dd> An Adobe Acrobat (pdf) file containing the complete API documentation. This file is only generated if you use the <code>&#8211;pdf</code> option.</dd>
<dt><code>api.tex</code></dt>
<dd> The top-level LaTeX file. This file imports the other LaTeX files, to create a single unified document.</dd>
<dt><code>api.dvi</code></dt>
<dd> A dvi file containing the complete API documentation. This file is only generated if you use the <code>&#8211;dvi</code> option, the <code>&#8211;ps</code> option, or the <code>&#8211;pdf</code> option.</dd>
<dt><code>api.ps</code></dt>
<dd> A postscript file containing the complete API documentation. This file is only generated if you use the <code>&#8211;ps</code> option or the <code>&#8211;pdf</code> option.</dd>
<dt><i>module</i><code>-module.tex</code></dt>
<dd> The API documentation for a module. <i>module</i> is the complete dotted name of the module, such as <code>sys or</code> <code>epydoc.epytext</code>.</dd>
<dt><i>class</i><code>-class.tex</code></dt>
<dd> The API documentation for a class, exception, or type. <i>class</i> is the complete dotted name of the class, such as <code>epydoc.epytext.Token</code> or array.ArrayType. These class documentation files are only created if the <code>&#8211;separate-classes</code> option is used; otherwise, the documentation for each class is included in its module&#8217;s documentation file.</dd></dl>
</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>EPYTEXT MARKUP WARNING MESSAGES</code></p>
<dl>
<dt>
</dt><dd> Epytext errors are caused by epytext docstrings that contain invalid markup. Whenever an epytext error is detected, the docstring in question is treated as a plaintext docstring. Epydoc can generate the following epytext errors:</dd>
<dl>
<dt><code>Bad link target.</code></dt>
<dd> The target specified for an inline link contruction (<code>L{&#8230;}</code>) is not well-formed. Link targets must be valid python identifiers.</dd>
<dt><code>Bad uri target.</code></dt>
<dd> The target specified for an inline uri contruction (<code>U{&#8230;}</code>) is not well-formed. This typically occurs if inline markup is nested inside the URI target.</dd>
<dt><code>Fields must be at the top level.</code></dt>
<dd> The list of fields (<code>@param</code>, etc.) is contained by some other block structure (such as a list or a section).</dd>
<dt><code>Fields must be the final elements.</code></dt>
<dd> The list of fields (<code>@param</code>, etc.) is not at the end of a docstring.</dd>
<dt><code>Headings must occur at top level.</code></dt>
<dd> The heading is contianed in some other block structure (such as a list).</dd>
<dt><code>Improper doctest block indentation.</code></dt>
<dd> The doctest block dedents past the indentation of its initial prompt line.</dd>
<dt><code>Improper heading indentation.</code></dt>
<dd> The heading for a section is not left-aligned with the paragraphs in the section that contains it.</dd>
<dt><code>Improper paragraph indentation.</code></dt>
<dd> The paragraphs within a block are not left-aligned. This error is often generated when plaintext docstrings are parsed using epytext.</dd>
<dt><code>Invalid escape.</code></dt>
<dd> An unknown escape sequence was used with the inline escape construction (<code>E{&#8230;}</code>).</dd>
<dt><code>Lists must be indented.</code></dt>
<dd> An unindented line immediately following a paragraph starts with a list bullet. Epydoc is not sure whether you meant to start a new list item, or meant for a paragraph to include a word that looks like a bullet. If you intended the former, then indent the list. If you intended the latter, then change the word-wrapping of the paragraph, or escape the first character of the word that looks like a bullet.</dd>
<dt><code>Unbalanced &#8216;{&#8216;.</code></dt>
<dd> The docstring contains unbalanced braces. Epytext requires that all braces must be balanced. To include a single unbalanced brace, use the escape sequences E{lb} (left brace) and E{rb} (right brace).</dd>
<dt><code>Unbalanced &#8216;}&#8217;.</code></dt>
<dd> The docstring contains unbalanced braces. Epytext requires that all braces must be balanced. To include a single unbalanced brace, use the escape sequences E{lb} (left brace) and E{rb} (right brace).</dd>
<dt><code>Unknown inline markup tag.</code></dt>
<dd> An unknown tag was used with the inline markup construction ( <i>x</i><code>{&#8230;}</code> ).</dd>
<dt><code>Wrong underline character for heading.</code></dt>
<dd> The underline character used for this section heading does not indicate an appopriate section level. The &quot;=&quot; character should be used to underline sections; &quot;-&quot; for subsections; and &quot;~&quot; for subsubsections.</dd>
<dt><code>Possible mal-formatted field item.</code></dt>
<dd> Epytext detected a line that looks like a field item, but is not correctly formatted. This typically occurs when the trailing colon (&quot;:&quot;) is not included in the field tag.</dd>
<dt><code>Possible heading typo.</code></dt>
<dd> Epytext detected a pair of lines that looks like a heading, but the number of underline characters does not match the number of characters in the heading. The number of characters in these two lines must match exactly for them to be considered a heading.</dd></dl>
</dl>
<p> <code>FIELD WARNINGS</code></p>
<dl>
<dt>
</dt><dd> Field warnings are caused by docstrings containing invalid fields. The contents of the invalid field are generally ignored. Epydoc can generate the following field warnings:</dd>
<dl>
<dt><code>@param for unknown parameter </code><i>param</i><code>.</code></dt>
<dd> A @param field was used to specify the type for a parameter that is not included in the function&#8217;s signature. This is typically caused by a typo in the parameter name.</dd>
<dt><i>tag</i><code> did not expect an argument.</code></dt>
<dd> The field tag <i>tag</i> was used with an argument, but it does not take one.</dd>
<dt><i>tag</i><code> expected an argument.</code></dt>
<dd> The field tag <i>tag</i> was used without an argument, but it requires one.</dd>
<dt><code>@type for unknown parameter </code><i>param</i><code>.</code></dt>
<dd> A @type field was used to specify the type for a parameter that is not included in the function&#8217;s signature. This is typically caused by a typo in the parameter name.</dd>
<dt><code>@type for unknown variable </code><i>var</i><code>.</code></dt>
<dd> A @type field was used to specify the type for a variable, but no other information is known about the variable. This is typically caused by a typo in the variable name.</dd>
<dt><code>Unknown field tag </code><i>tag</i><code>.</code></dt>
<dd> A docstring contains a field with the unknown tag <i>tag</i>.</dd>
<dt><code>Redefinition of </code><i>field</i><code>.</code></dt>
<dd> Multiple field tags define the value of <i>field</i> in the same docstring, but <i>field</i> can only take a single value.</dd></dl>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>epydoc -n </code>epydoc<code> -u </code><a rel="nofollow" href="http://epydoc.sf.net">http://epydoc.sf.net</a> epydoc/</dt>
<dd> Generate the HTML API documentation for the epydoc package and all of its submodules, and write the output to the <code>html</code> directory. In the headers and footers, use <code>epydoc</code> as the project name, and <code><a rel="nofollow" href="http://epydoc.sf.net">http://epydoc.sf.net</a></code> as the project URL.</dd>
<dt><code>epydoc &#8211;pdf -n </code>epydoc<code> epydoc/</code></dt>
<dd> Generate the LaTeX API documentation for the epydoc package and all of its submodules, and write the output to the <code>latex</code> directory.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> Successful program execution.</dd>
<dt><code>1</code></dt>
<dd> Usage error.</dd>
<dt><code>2</code></dt>
<dd> Epydoc generated an error or warning, and one of the options <code>&#8211;fail-on-error</code><i>,</i> <code>&#8211;fail-on-warning</code><i>, or</i> <code>&#8211;fail-on-docstring-warning</code> was specified.</dd>
<dt><code>other</code></dt>
<dd> Internal error (Python exception).</dd></dl>
<h2>AUTHOR</h2>
<p> Epydoc was written by Edward Loper. This man page was originally written by Moshe Zadka, and is currently maintained by Edward Loper.</p>
<h2>BUGS</h2>
<p> Report bugs to &lt;edloper [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-epydocgui/">epydocgui</a></code>(1)</p>
<dl>
<dt><code>The epydoc webpage</code></dt>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net">http://epydoc.sourceforge.net</a>&gt;</dd>
<dt><code>The epytext markup language manual</code></dt>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net/epytext.html">http://epydoc.sourceforge.net/epytext.html</a>&gt; </dd>
</dl>
