---
title: "makeskel(1)"
name: "makeskel"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeskel/"
description: "makeskel – generate description file for fpdoc."
---

<h2>NAME</h2>
<p> makeskel &#8211; generate description file for <code>fpdoc.</code> </p>
<h2>SYNOPSIS</h2>
<p> <code>makeskel</code> [&#8211;descr=filename] [&#8211;disable-arguments] [&#8211;disable-errors] [&#8211;disable-function-results] [&#8211;disable-private] [&#8211;disable-protected] [&#8211;disable-seealso] [&#8211;emit-class-separator] [&#8211;help] [&#8211;lang=language] [&#8211;output=filename] [&#8211;update] &#8211;package=name &#8211;input=cmdline </p>
<h2>Description</h2>
<p> <code>makeskel</code> scans a Free Pascal unit source file and generates a skeleton description file for it. It generates nodes for all identifiers found in the interface section of the unit, although this behaviour can be adjusted with some options. It can also update an existing XML file, and then emits only nodes for identifiers for which no node exists yet. </p>
<h2>Usage</h2>
<p> You can invoke <code>makeskel</code> with as the only required arguments the <code>input</code> and <code>package</code> arguments. It should at least contain the name of the unit file for which documentation should be generated and the name of the package to which the unit belongs. The output of <code>makeskel </code> will go to standard output by default. </p>
<h2>Options</h2>
<p> <code>makeskel</code> has many options, most of them optional, defaults will be used in most cases. </p>
<dl>
<dt><code>&#8211;descr=descfile</code></dt>
<dd> This option must be used in conjunction with the <i>update </i> option. It specifies the name of a description file <code>descfile</code> which must be updated. Note that the file must contain valid XML, or the update will fail. This option can be specified more than once.</dd>
<dt><code>&#8211;disable-arguments</code></dt>
<dd> If this option is specified, <code>makeskel</code> will not emit nodes for the arguments of functions and procedures. By default, documentation nodes are emitted for functions and procedures as well.</dd>
<dt><code>&#8211;disable-errors</code></dt>
<dd> By default, each documentation node will contain a <i>errors</i> node as well (excep for identifiers where this has no use, such as function arguments). If this option is specified, no <i>errors</i> node will be generated.</dd>
<dt><code>&#8211;disable-function-results</code></dt>
<dd> By default, for functions, a <i>result</i> node will be generated, to describe the result of the function. If this option is specified, no function result node will be generated.</dd>
<dt><code>&#8211;disable-private</code></dt>
<dd> By default, documentation nodes are also generated for private fields or methods of a class. if this option is specified, the generation of nodes for private fields or methods is skipped.</dd>
<dt><code>&#8211;disable-protected</code></dt>
<dd> By default, documentation nodes are also generated for protected fields or methods of a class. if this option is specified, the generation of nodes for protected fields or methods is skipped.</dd>
<dt><code>&#8211;emit-class-separator</code></dt>
<dd> If this option is specified, a visible comment with the name of the class for which documentation nodes will follow, is inserted between the nodes of two classes, making navigation easier.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Emit a short help text and exit.</dd>
<dt><code>&#8211;input=cmd</code></dt>
<dd> The input (source) file to process. Multiple input files can be specified. The command may contain valid compiler options, currently the <i>-Fipath</i> (search path) and <i>-dmacro</i> (define macro) options are recognized.</dd>
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
<dt><code>&#8211;output=filename</code></dt>
<dd> This option tells <code>makeskel</code> where the output should go. If this option is not specified, the output is sent to standard output (the screen).</dd>
<dt><code>&#8211;package=packagename</code></dt>
<dd> This option is required. It specifies the name of the package. All nodes will be generated inside a node with <code>name </code> attribute <i>packagename.</i></dd>
<dt><code>&#8211;update</code></dt>
<dd> Turns on update mode. In this mode, the output is a file which contains only the missing nodes to complete the documentation of the input files. The existing nodes must be specified with the <code>descr</code> argument. Note that the output file may <i>not</i> be the same as the input (description) nodes; A separate file must be specified (or no file, in which case output goes to standard output. </dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) <code><a href="/docs/linux/man/1-fpdoc/">fpdoc</a></code>(1) </dd>
</dl>
<h2>Index</h2>
