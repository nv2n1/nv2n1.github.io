---
title: "augparse(1)"
name: "augparse"
section: "1"
letter: "a"
url: "/docs/linux/man/1-augparse/"
description: "augparse – execute an Augeas module"
---

<h2 class="name">NAME</h2>
<p> augparse &#8211; execute an Augeas module </p>
<h2>SYNOPSIS</h2>
<p> augparse [<font SIZE="-1">OPTIONS</font>] <font SIZE="-1">MODULE</font></p>
<h2>DESCRIPTION</h2>
<p> Execute an Augeas module, most commonly to evaluate the tests it contains.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-I</code>, <code>&#8211;include</code>=<i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Add <font SIZE="-1">DIR</font> to the module loadpath. Can be given multiple times. The directories set here are searched before any directories specified in the <font SIZE="-1">AUGEAS_LENS_LIB</font> environment variable, and before the default directory <i>/usr/share/augeas/lenses</i>.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Print a trace of the modules that are being loaded.</p>
<dt><code>&#8211;nostdinc</code></p>
<dd> Do not search any of the default directories for modules. When this option is set, only directories specified explicitly with <code>-I</code> or specified in <font SIZE="-1"><code>AUGEAS_LENS_LIB</code></font> will be searched for modules.</p>
<dt><code>&#8211;notypecheck</code></p>
<dd> Do not perform lens type checks. Only use this option during lens development and make sure you typecheck lenses when you are done developing &#8211; you should never use a lens that hasn&#8217;t been typechecked. This option is sometimes useful when you are working on unit tests for a lens to speed up the time it takes to repeatedly run and fix tests.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>-h</code></p>
<dd> Display this help and exit</dl>
<h2>EXAMPLES</h2>
<p> To run the tests in <i>lenses/tests/test_foo.aug</i> and use modules from the directory <i>lenses</i>, run </p>
<dl>
<dt>
<dd> augparse -I lenses lenses/tests/test_foo.aug</dl>
<h2>TESTS</h2>
<p> Tests can appear as top-level forms anywhere in a module. Generally, the tests for a module <i>lenses/foo.aug</i> are kept in a separate file, usually in <i>lenses/tests/test_foo.aug</i>. </p>
<p> There are two different kinds of tests that Augeas can run: <code>get</code> and <code>put</code> tests. The syntax for <code>get</code> tests is </p>
<dl>
<dt>
<dd> test <font SIZE="-1">LENS</font> get <font SIZE="-1">STRING</font> = <font SIZE="-1">RESULT</font></dl>
<p> which applies the <i>get</i> direction of the lens <font SIZE="-1">LENS</font> to <font SIZE="-1">STRING</font> and compares it with the given <font SIZE="-1">RESULT. RESULT</font> can either be a tree literal, the symbol <code>?</code> to print the result of applying <font SIZE="-1">LENS</font> to <font SIZE="-1">STRING,</font> or the symbol <code>*</code> to indicate that the test should produce an exception. </p>
<p> The syntax for <code>put</code> tests is </p>
<dl>
<dt>
<dd> test <font SIZE="-1">LENS</font> put <font SIZE="-1">STRING</font> after <font SIZE="-1">COMMANDS</font> = <font SIZE="-1">RESULT</font></dl>
<p> which first applies the <i>get</i> direction of the lens <font SIZE="-1">LENS</font> to <font SIZE="-1">STRING,</font> then applies the given <font SIZE="-1">COMMANDS</font> to the resulting tree, and finally transforms the modified tree back to a string using the <i>put</i> direction of <font SIZE="-1">LENS.</font> The resulting string is then compared to <font SIZE="-1">RESULT,</font> which can be a string, the symbol <code>?</code> to print the result of applying <font SIZE="-1">LENS</font> to <font SIZE="-1">STRING,</font> or the symbol <code>*</code> to indicate that the test should produce an exception.</p>
<h2>SEE ALSO</h2>
<p> <code>Augeas</code> project homepage &lt;<a rel="nofollow" href="http://www.augeas.net/">http://www.augeas.net/</a>&gt; </p>
<p> augtool </p>
<h2>Index</h2>
