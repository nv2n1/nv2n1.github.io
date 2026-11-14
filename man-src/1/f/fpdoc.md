---
title: "fpdoc(1)"
name: "fpdoc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpdoc/"
description: "fpdoc – The FPC Pascal unit documentation generator."
---

<h2>NAME</h2>
<p> fpdoc &#8211; The FPC Pascal unit documentation generator. </p>
<h2>SYNOPSIS</h2>
<p> <code>fpdoc</code> &#8211;input=inputcommand [&#8211;output=output] [&#8211;format=fmt] [&#8211;descr=descriptionfile] [&#8211;show-private] [&#8211;hide-protected] [&#8211;lang=language] [&#8211;content=contentfile] [&#8211;import=importfile] [&#8211;package=packagename] [&#8211;html-search=searchpage] [&#8211;ostarget=target] [&#8211;cpu-target=target] [&#8211;latex-extension=ext] [&#8211;latex-highlight] </p>
<h2>Description</h2>
<p> <code>fpdoc</code> scans a Free Pascal unit source file and generates documentation for it. The documentation can be in various formats (currently HTML and LaTeX) It can read various description files which contain the description for the various symbols found in the unit file. </p>
<h2>Usage</h2>
<p> You can invoke <code>fpdoc</code> with as the only required argument the &#8216;input&#8217; and &#8216;package&#8217; arguments. It should at least contain the name of the unit file for which documentation should be generated and the name of the package to which the unit belongs. </p>
<h2>Options</h2>
<p> <code>fpdoc</code> has several options, most of them optional, defaults will be used in most cases. </p>
<dl>
<dt><code>&#8211;content</code></p>
<dd> This option tells <code>fpdoc</code> to generate a content file. A content file contains a list of all the possible anchors (labels) in the generated documentation file, and can be used to create cross-links in documentation for different units, using the <code>&#8211;import</code> option.</p>
<dt><code>&#8211;descr=descfile</code></p>
<dd> This option specifies the name of a description file <code>descfile</code> that contains the actual documentation for the unit. This option can be given several times, for several description files.</p>
<dt><code>&#8211;format=fmt</code></p>
<dd> Specifies the format <code>fmt</code> in which the documentation will be generated. Currenly, the following formats are known:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>htm</i></p>
<dd> HTML with 8.3 conforming filenames.</p>
<dt><i>html</i></p>
<dd> HTML with long filenames.</p>
<dt><i>xhtml</i></p>
<dd> XHTML with long filesnames.</p>
<dt><i>latex</i></p>
<dd> LaTex, which uses the fpc.sty style used by the Free Pascal documentation.</p>
<dt><i>xml-struct</i></p>
<dd> Structured XML.</dl>
</dl>
<dt><code>&#8211;hide-protected</code></p>
<dd> By default, the documentation will include descriptions and listings of protected fields and methods in classes or objects. This option changes this behaviour; if it is specified, no documentation will be generated for these methods. Note that public methods or properties that refer to these protected method will then have a dangling (i.e. unavailable) link.</p>
<dt><code>&#8211;html-search=link</code></p>
<dd> Adds an entry for an HTML search page at location <code>link</code> in the headers of the generated HTML pages. There is no search page provided, this should be made and provided by the user.</p>
<dt><code>&#8211;import=impfile</code></p>
<dd> imports a content file <code>impfile</code> from another documentation set. This can be used to resolve references to elements within this other documentation file;</p>
<dt><code>&#8211;input=cmd</code></p>
<dd> This option tells <code>fpdoc</code> what input file should be used. The argument <code>cmd</code> can be just a filename, but can also be a complete compiler command-line with options that concern the scanning of the pascal source: defines, include files, syntax options, as they would be specified to the free pascal compiler when compiling the file. If a complete command is used, then it should be enclosed in single or double quotes, so the shell will not break them in parts. It is possible to specify multiple input commands; they will be treated one by one, and documentation will be generated for each of them.</p>
<dt><code>&#8211;lang=language</code></p>
<dd> Sets the language for the output file. This will mainly set the strings used for the headers in various parts of the documentation files (by default they&#8217;re in english). Currently, valid options are</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>de </i></p>
<dd> German.</p>
<dt><i>fr</i></p>
<dd> French.</p>
<dt><i>nl</i></p>
<dd> Dutch.</dl>
</dl>
<dt><code>&#8211;latex-extension=ext</code></p>
<dd> Sets the extension to use for the LaTeX file to <i>ext</i> the default is <code>.tex</code> (with . (dot) included).</p>
<dt><code>&#8211;latex-highlight</code></p>
<dd> Switches on an internal latex syntax highlighter. This is not yet implemented. By default, syntax highlighting is provided by the syntax package that comes with fpc.</p>
<dt><code>&#8211;output=name</code></p>
<dd> This option tells <code>fpdoc</code> where the output file should be generated. How this option is interpreted depends on the format that is used. For latex, <code>name</code> is interpreted as the filename for the tex file. For all other formats, <code>name</code> is interpreted as the directory where all documentation files will be written. The directory will be created if it does not yet exist. Standard this equals the package name.</p>
<dt><code>&#8211;package=packagename</code></p>
<dd> Specifies the package name. All units will be documented as part of <i>packagename</i> , which is also the default output filename or directory. Only documentation nodes inside a package node with this name will be considered when documenting.</p>
<dt><code>&#8211;show-private</code></p>
<dd> By default, no documentation is generated for private methods or fields. This option causes <code>fpdoc</code> to generate documentation for these methods as well.</p>
<dt><code>&#8211;warn-no-node</code></p>
<dd> If this option is specified, <code>fpdoc</code> will emit a warning if it does not find a description node for an identifier it is documenting. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) <code><a href="/docs/linux/man/1-makeskel/">makeskel</a></code>(1) </p>
</dl>
<h2>Index</h2>
