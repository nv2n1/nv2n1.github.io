---

title: "augparse(1)"
name: "augparse"
section: "1"
letter: "a"
url: "/docs/linux/man/1-augparse/"
description: "augparse – execute an Augeas module"
---

<p> augparse &#8211; execute an Augeas module </p>
<h2>SYNOPSIS</h2>
<p> augparse [OPTIONS] MODULE</p>
<h2>DESCRIPTION</h2>
<p> Execute an Augeas module, most commonly to evaluate the tests it contains.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-I</code>, <code>&#8211;include</code>=<i></i><i>DIR</i><i></i></dt>
<dd> Add DIR to the module loadpath. Can be given multiple times. The directories set here are searched before any directories specified in the AUGEAS_LENS_LIB environment variable, and before the default directory <i>/usr/share/augeas/lenses</i>.</dd>
<dt><code>-t</code>, <code>&#8211;trace</code></dt>
<dd> Print a trace of the modules that are being loaded.</dd>
<dt><code>&#8211;nostdinc</code></dt>
<dd> Do not search any of the default directories for modules. When this option is set, only directories specified explicitly with <code>-I</code> or specified in <code>AUGEAS_LENS_LIB</code> will be searched for modules.</dd>
<dt><code>&#8211;notypecheck</code></dt>
<dd> Do not perform lens type checks. Only use this option during lens development and make sure you typecheck lenses when you are done developing &#8211; you should never use a lens that hasn&#8217;t been typechecked. This option is sometimes useful when you are working on unit tests for a lens to speed up the time it takes to repeatedly run and fix tests.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>-h</code></dt>
<dd> Display this help and exit</dd></dl>
<h2>EXAMPLES</h2>
<p> To run the tests in <i>lenses/tests/test_foo.aug</i> and use modules from the directory <i>lenses</i>, run </p>
<dl>
<dt>
</dt><dd> augparse -I lenses lenses/tests/test_foo.aug</dd></dl>
<h2>TESTS</h2>
<p> Tests can appear as top-level forms anywhere in a module. Generally, the tests for a module <i>lenses/foo.aug</i> are kept in a separate file, usually in <i>lenses/tests/test_foo.aug</i>. </p>
<p> There are two different kinds of tests that Augeas can run: <code>get</code> and <code>put</code> tests. The syntax for <code>get</code> tests is </p>
<dl>
<dt>
</dt><dd> test LENS get STRING = RESULT</dd></dl>
<p> which applies the <i>get</i> direction of the lens LENS to STRING and compares it with the given RESULT. RESULT can either be a tree literal, the symbol <code>?</code> to print the result of applying LENS to STRING, or the symbol <code>*</code> to indicate that the test should produce an exception. </p>
<p> The syntax for <code>put</code> tests is </p>
<dl>
<dt>
</dt><dd> test LENS put STRING after COMMANDS = RESULT</dd></dl>
<p> which first applies the <i>get</i> direction of the lens LENS to STRING, then applies the given COMMANDS to the resulting tree, and finally transforms the modified tree back to a string using the <i>put</i> direction of LENS. The resulting string is then compared to RESULT, which can be a string, the symbol <code>?</code> to print the result of applying LENS to STRING, or the symbol <code>*</code> to indicate that the test should produce an exception.</p>
<h2>SEE ALSO</h2>
<p> <code>Augeas</code> project homepage &lt;<a rel="nofollow" href="http://www.augeas.net/">http://www.augeas.net/</a>&gt; </p>
<p> augtool </p>
