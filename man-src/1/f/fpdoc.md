---

title: "fpdoc(1)"
name: "fpdoc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpdoc/"
description: "fpdoc – The FPC Pascal unit documentation generator."
---

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
<dt><code>&#8211;content</code></dt>
<dd> This option tells <code>fpdoc</code> to generate a content file. A content file contains a list of all the possible anchors (labels) in the generated documentation file, and can be used to create cross-links in documentation for different units, using the <code>&#8211;import</code> option.</dd>
<dt><code>&#8211;descr=descfile</code></dt>
<dd> This option specifies the name of a description file <code>descfile</code> that contains the actual documentation for the unit. This option can be given several times, for several description files.</dd>
<dt><code>&#8211;format=fmt</code></dt>
<dd> Specifies the format <code>fmt</code> in which the documentation will be generated. Currenly, the following formats are known:</dd>
<dl>
<dl>
<dt><i>htm</i></dt>
<dd> HTML with 8.3 conforming filenames.</dd>
<dt><i>html</i></dt>
<dd> HTML with long filenames.</dd>
<dt><i>xhtml</i></dt>
<dd> XHTML with long filesnames.</dd>
<dt><i>latex</i></dt>
<dd> LaTex, which uses the fpc.sty style used by the Free Pascal documentation.</dd>
<dt><i>xml-struct</i></dt>
<dd> Structured XML.</dd></dl>
</dl>
<dt><code>&#8211;hide-protected</code></dt>
<dd> By default, the documentation will include descriptions and listings of protected fields and methods in classes or objects. This option changes this behaviour; if it is specified, no documentation will be generated for these methods. Note that public methods or properties that refer to these protected method will then have a dangling (i.e. unavailable) link.</dd>
<dt><code>&#8211;html-search=link</code></dt>
<dd> Adds an entry for an HTML search page at location <code>link</code> in the headers of the generated HTML pages. There is no search page provided, this should be made and provided by the user.</dd>
<dt><code>&#8211;import=impfile</code></dt>
<dd> imports a content file <code>impfile</code> from another documentation set. This can be used to resolve references to elements within this other documentation file;</dd>
<dt><code>&#8211;input=cmd</code></dt>
<dd> This option tells <code>fpdoc</code> what input file should be used. The argument <code>cmd</code> can be just a filename, but can also be a complete compiler command-line with options that concern the scanning of the pascal source: defines, include files, syntax options, as they would be specified to the free pascal compiler when compiling the file. If a complete command is used, then it should be enclosed in single or double quotes, so the shell will not break them in parts. It is possible to specify multiple input commands; they will be treated one by one, and documentation will be generated for each of them.</dd>
<dt><code>&#8211;lang=language</code></dt>
<dd> Sets the language for the output file. This will mainly set the strings used for the headers in various parts of the documentation files (by default they&#8217;re in english). Currently, valid options are</dd>
<dl>
<dl>
<dt><i>de </i></dt>
<dd> German.</dd>
<dt><i>fr</i></dt>
<dd> French.</dd>
<dt><i>nl</i></dt>
<dd> Dutch.</dd></dl>
</dl>
<dt><code>&#8211;latex-extension=ext</code></dt>
<dd> Sets the extension to use for the LaTeX file to <i>ext</i> the default is <code>.tex</code> (with . (dot) included).</dd>
<dt><code>&#8211;latex-highlight</code></dt>
<dd> Switches on an internal latex syntax highlighter. This is not yet implemented. By default, syntax highlighting is provided by the syntax package that comes with fpc.</dd>
<dt><code>&#8211;output=name</code></dt>
<dd> This option tells <code>fpdoc</code> where the output file should be generated. How this option is interpreted depends on the format that is used. For latex, <code>name</code> is interpreted as the filename for the tex file. For all other formats, <code>name</code> is interpreted as the directory where all documentation files will be written. The directory will be created if it does not yet exist. Standard this equals the package name.</dd>
<dt><code>&#8211;package=packagename</code></dt>
<dd> Specifies the package name. All units will be documented as part of <i>packagename</i> , which is also the default output filename or directory. Only documentation nodes inside a package node with this name will be considered when documenting.</dd>
<dt><code>&#8211;show-private</code></dt>
<dd> By default, no documentation is generated for private methods or fields. This option causes <code>fpdoc</code> to generate documentation for these methods as well.</dd>
<dt><code>&#8211;warn-no-node</code></dt>
<dd> If this option is specified, <code>fpdoc</code> will emit a warning if it does not find a description node for an identifier it is documenting. </dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) <code><a href="/docs/linux/man/1-makeskel/">makeskel</a></code>(1) </dd>
</dl>
