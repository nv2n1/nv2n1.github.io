---
title: "unitdiff(1)"
name: "unitdiff"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unitdiff/"
description: "unitdiff – Describe differences in the interface of a FPC unit."
---

<h2>NAME</h2>
<p> unitdiff &#8211; Describe differences in the interface of a FPC unit. </p>
<h2>SYNOPSIS</h2>
<p> <code>unitdiff</code> [&#8211;disable-arguments] [&#8211;disable-private] [&#8211;disable-protected] [&#8211;help] [&#8211;lang=language] [&#8211;list] [&#8211;output=filename] [&#8211;sparse] file1 file2 </p>
<h2>Description</h2>
<p> <code>unitdiff</code> scans one or two Free Pascal unit source files and either lists all available identifiers, or describes the differences in identifiers between the two units. </p>
<h2>Usage</h2>
<p> You can invoke <code>unitdiff</code> with as the only required argument a <code>input</code> filename. It will then simply list all available identifiers. </p>
<p> The regular use is to invoke <code>unitdiff</code> with <code>input1 input2</code> arguments. It will then show the difference in interface between the two units, or list the available identifiers in both units. The output of <code>unitdiff</code> will go to standard output by default. </p>
<h2>Options</h2>
<p> <code>unitdiff</code> has some options, most of them optional, defaults will be used in most cases. </p>
<dl>
<dt><code>&#8211;disable-arguments</code></p>
<dd> If this option is specified, <code>unitdiff</code> will not check the arguments of functions and procedures. By default, these are checked as well.</p>
<dt><code>&#8211;disable-private</code></p>
<dd> By default, private methods of classes are checked. if this option is specified, private fields or methods are not checked.</p>
<dt><code>&#8211;disable-protected</code></p>
<dd> By default, protected methods of classes are checked. if this option is specified, protected <i>and</i> private fields or methods are not checked.</p>
<dt><code>&#8211;help</code></p>
<dd> Emit a short help text and exit.</p>
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
<dt><code>&#8211;list</code></p>
<dd> If this option is specified, only the list of available identifiers will be specified for the unit or units. If only 1 unit is specified, this option is automatically assumed.</p>
<dt><code>&#8211;output=filename</code></p>
<dd> This option tells <code>unitdiff</code> where the output should go. If this option is not specified, the output is sent to standard output (the screen).</p>
<dt><code>&#8211;sparse</code></p>
<dd> Turns on sparse mode. In this mode, the output will not contain the types of the identifiers. Only the names of the identifiers are written to the output. By default, also type descriptions are written. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-fpdoc/">fpdoc</a></code>(1) </p>
</dl>
<h2>Index</h2>
