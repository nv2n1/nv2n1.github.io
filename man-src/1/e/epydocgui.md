---
title: "epydocgui(1)"
name: "epydocgui"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epydocgui/"
description: "epydocgui – graphical interface to epydoc"
---

<h2>NAME</h2>
<p> epydocgui &#8211; graphical interface to epydoc</p>
<h2>SYNOPSIS</h2>
<p> <code>epydocgui</code> [<i>project.prj</i> | <i>modules</i>&#8230;] </p>
<p> <code>epydoc -h</code> </p>
<p> <code>epydoc -V</code></p>
<h2>DESCRIPTION</h2>
<p> <code>epydocgui</code> is a graphical interface to epydoc, which generates API documentation for Python modules and packages, based on their docstrings. A lightweight markup language called <code>epytext</code> can be used to format docstrings, and to add information about specific fields, such as parameters and instance variables. </p>
<p> The API documentation produced by <code>epydocgui</code> consists of a set of HTML files. Two subdirectories are created for the public and private documentation. Within each subdirectories, every class and module is documented in its own file. An index file, a trees file, and a help file are also created. If you select the <code>frames</code> option, then a frames-based table of contents is also produced.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>project.prj</i></p>
<dd> The name of a project file that was saved with <code>epydocgui</code>. Project files record a list of related modules, and the options that should be used to generate the documentation for those modules.</p>
<dt><i>modules</i>&#8230;</p>
<dd> The list of the modules that should be documented. Modules can be specified using module names (such as <code>os.path</code>), filenames (such as <code>epydoc/epytext.py</code>), or directory names (such as <code>epydoc/</code>). Directory names specify packages, and are expanded to include all sub-modules and sub-packages.</p>
<dt><code>-h, &#8211;help, &#8211;usage, -?</code></p>
<dd> Display a usage message.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the version of Epydoc.</dl>
<h2>HTML FILES</h2>
<p> The API documentation produced by <code>epydoc</code> consists of the following files:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>index.html</code></p>
<dd> The standard entry point for the documentation. Normally, <code>index.html</code> is a frame index file, which defines three frames: two frames on the left side of the browser contain a table of contents, and the main frame on the right side of the window contains documentation pages. But if the <code>&#8211;no-frames</code> option is used, then <code>index.html</code> will redirect the user to the project&#8217;s top page.</p>
<dt><code>m-</code><i>module</i><code>.html</code></p>
<dd> The API documentation for a module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>.</p>
<dt><code>c-</code><i>class</i><code>.html</code></p>
<dd> The API documentation for a class, exception, or type. <i>class</i> is the complete dotted name of the class, such as <code>epydoc.epytext.Token</code> or <code>array.ArrayType</code>.</p>
<dt><code>trees.html</code></p>
<dd> The module and class hierarchies.</p>
<dt><code>indices.html</code></p>
<dd> The term and identifier indices.</p>
<dt><code>help.html</code></p>
<dd> The help page for the project. This page explains how to use and navigate the webpage produced by epydoc.</p>
<dt><code>toc.html</code></p>
<dd> The top-level table of contents page. This page is displayed in the upper-left frame, and provides links to <code>toc-everything.html</code> and the <code>toc-m-</code><i>module</i><code>.html</code> files. <code>toc.html</code> is not generated if the <code>&#8211;no-frames</code> option is used.</p>
<dt><code>toc-everything.html</code></p>
<dd> The table of contents for the entire project. This page is displayed in the lower-left frame, and provides links to every class, type, exception, function, and variable defined by the project. <code>toc-everything.html</code> is not generated if the <code>&#8211;no-frames</code> option is used.</p>
<dt><code>toc-m-</code><i>module</i><code>.html</code></p>
<dd> The table of contents for a module. This page is displayed in the lower-left frame, and provides links to every class, type, exception, function, and variable defined by the module. <i>module</i> is the complete dotted name of the module, such as <code>sys</code> or <code>epydoc.epytext</code>. <code>toc-m-</code><i>module</i><code>.html</code> is not generated if the <code>&#8211;no-frames</code> option is used.</p>
<dt><code>epydoc.css</code></p>
<dd> The CSS stylesheet used to display all HTML pages.</dl>
</dl>
<p> By default, <code>epydoc</code> creates two subdirectories in the output directory: <code>public</code> and <code>private</code>. Each directory contains all of the files specified above. But if the <code>&#8211;no-private</code> option is used, then no subdirectories are created, and the public documentation is written directly to the output directory. ivided into five categories: import errors; epytext errors; epytext warnings; field warnings; and inspection errors. Whenver epydoc encounters an error, it issues a warning message that describes the error, and attempts to continue generating documentation. </p>
<p> Import errors indicate that epydoc was unable to import a module. Import errors typically prevent epydoc from generating documentation for the module in question. Epydoc can generate the following import errors:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Bad module name </code><i>module</i></p>
<dd> Epydoc attempted to import <i>module</i>, but <i>module</i> is not a valid name for a Python module.</p>
<dt><code>Could not find a UID for </code><i>link-target</i></p>
<dd> Epydoc was unable to find the object referred to by an inline link construction (<code>L{&#8230;}</code>). This is usually caused by a typo in the link.</p>
<dt><code>Could not import </code><i>module</i></p>
<dd> Epydoc attempted to import <i>module</i>, but it failed. This typically occurs when <i>module</i> raises an exception.</p>
<dt><i>file</i><code> does not exist</code></p>
<dd> Epydoc attempted to import the module contained in <i>file</i>, but <i>file</i> does not exist.</dl>
</dl>
<p> Epytext errors are caused by epytext docstrings that contain invalid markup. Whenever an epytext error is detected, the docstring in question is treated as a plaintext docstring. Epydoc can generate the following epytext errors:</p>
<dl>
<dt>
<dd>
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
<dd> The underline character used for this section heading does not indicate an appopriate section level. The &quot;=&quot; character should be used to underline sections; &quot;-&quot; for subsections; and &quot;~&quot; for subsubsections.</dl>
</dl>
<p> Epytext warnings are caused by epytext docstrings that contain questionable or suspicious markup. Epytext warnings do <code>not</code> prevent the docstring in question from being parsed. Epydoc can generate the following epytext warnings:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Possible mal-formatted field item.</code></p>
<dd> Epytext detected a line that looks like a field item, but is not correctly formatted. This typically occurs when the trailing colon (&quot;:&quot;) is not included in the field tag.</p>
<dt><code>Possible heading typo.</code></p>
<dd> Epytext detected a pair of lines that looks like a heading, but the number of underline characters does not match the number of characters in the heading. The number of characters in these two lines must match exactly for them to be considered a heading.</dl>
</dl>
<p> Field warnings are caused by epytext docstrings containing invalid fields. The contents of the invalid field are generally ignored. Epydoc can generate the following field warnings:</p>
<dl>
<dt>
<dd>
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
<p> Inspection errors are generated if epydoc encounters problems while attempting to inspect the properties of a documented object. Most of inspection errors do not prevent epydoc from documenting the object in question. Epydoc can generate the following inspection errors:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>The parameters of </code><i>inhmethod</i><code> do not match </code><i>basemethod</i><code>.</code></p>
<dd> The parameters of the undocumented method <i>inhmethod </i> do not match the parameters of the base class method <i>basemethod</i> that it overrides. As a result, <i>inhmethod</i> does not inherit documentation from <i>basemethod</i>. If the difference in parameters is intentional, then you can eliminate the warning by adding a (possibly empty) docstring to <i>inhmethod</i>.</p>
<dt><code>Docmap cannot add a </code><i>type</i></p>
<dd> Epydoc attempted to document an object with an unknown type. This error is typically generated by packages and modules that manipulate the import mechanism, such that importing a module produces some other type of object.</p>
<dt><code>UID conflict detected: </code><i>uid</i></p>
<dd> Two different objects were assigned the same unique identifier by epydoc. This can cause epydoc to substitute the documentation of one object with the documentation of another object that is assigned the same unique identifier. However, this will usually only cause problems if the two objects with the same unique identifiers are both modules or classes, in which case the API documentation page for one object will overwrite the API documentation page for the other object.</p>
<dt><i>object</i><code> appears in multiple builtin modules</code></p>
<dd> While attempting to determine which module defines the builtin object <i>object</i>, epydoc encountered multiple candidates, and was unable to decide which candidate was correct. In this case, epydoc arbitrarily chooses the first candidate that it finds.</p>
<dt><i>object</i><code> appears in multiple .py modules</code></p>
<dd> While attempting to determine which module defines the builtin object <i>object</i>, epydoc encountered multiple candidates, and was unable to decide which candidate was correct. In this case, epydoc arbitrarily chooses the first candidate that it finds.</p>
<dt><i>object</i><code> appears in multiple .so modules</code></p>
<dd> While attempting to determine which module defines the builtin object <i>object</i>, epydoc encountered multiple candidates, and was unable to decide which candidate was correct. In this case, epydoc arbitrarily chooses the first candidate that it finds.</p>
<dt><code>Could not find a module for </code><i>object</i></p>
<dd> Epydoc was unable to determine which module defines <i>object</i>. If <i>object</i> is a function, then this will prevent epydoc from generating any documentation for <i>object</i>, since it does not know what page to put the documentation on. Otherwise, this will prevent the documentation for <i>object</i> from including a link to its containing module.</dl>
</dl>
<h2>AUTHOR</h2>
<p> Epydoc was written by Edward Loper. This man page was originally written by Moshe Zadka, and is currently maintained by Edward Loper.</p>
<h2>BUGS</h2>
<p> Report bugs to &lt;edloper [at] gradient.cis.upenn.edu&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-epydoc/">epydoc</a></code>(1)</p>
<dl>
<dt><code>The epydoc webpage</code></p>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net">http://epydoc.sourceforge.net</a>&gt;</p>
<dt><code>The epytext markup language manual</code></p>
<dd> &lt;<a rel="nofollow" href="http://epydoc.sourceforge.net/epytext.html">http://epydoc.sourceforge.net/epytext.html</a>&gt; </p>
</dl>
<h2>Index</h2>
