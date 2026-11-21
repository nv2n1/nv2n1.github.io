---

title: "shiboken(1)"
name: "shiboken"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shiboken/"
description: "shiboken – CPython bindings generator for C++ libraries"
---

<p> shiboken &#8211; CPython bindings generator for C++ libraries</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> shiboken [options] header-file typesystem-file</dd></dl>
<h3>General options:</h3>
<dl>
<dt><code>&#8211;debug-level</code>=<i>[sparse</i>|medium|full]</dt>
<dd> Set the debug level</dd>
<dt><code>&#8211;documentation-only</code></dt>
<dd> Do not generates any code, just the documentation</dd>
<dt><code>&#8211;generatorSet</code></dt>
<dd> generatorSet to be used. e.g. qtdoc</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display this help and exit</dd>
<dt><code>&#8211;include-paths=</code>&lt;path&gt;[:&lt;path&gt;:&#8230;]</dt>
<dd> Include paths used by the C++ parser</dd>
<dt><code>&#8211;license-file</code>=<i>[licensefile]</i></dt>
<dd> File used for copyright headers of generated files</dd>
<dt><code>&#8211;no-suppress-warnings</code></dt>
<dd> Show all warnings</dd>
<dt><code>&#8211;output-directory</code>=<i>[dir]</i></dt>
<dd> The directory where the generated files will be written</dd>
<dt><code>&#8211;silent</code></dt>
<dd> Avoid printing any message</dd>
<dt><code>&#8211;typesystem-paths=</code>&lt;path&gt;[:&lt;path&gt;:&#8230;]</dt>
<dd> Paths used when searching for typesystems</dd>
<dt><code>&#8211;version</code></dt>
<dd> Output version information and exit</dd></dl>
<h3>Shiboken options:</h3>
<dl>
<dt><code>&#8211;disable-verbose-error-messages</code></dt>
<dd> Disable verbose error messages. Turn the python code hard to debug but safe few kB on the generated bindings.</dd>
<dt><code>&#8211;enable-parent-ctor-heuristic</code></dt>
<dd> Enable heuristics to detect parent relationship on constructors.</dd>
<dt><code>&#8211;enable-pyside-extensions</code></dt>
<dd> Enable PySide extensions, such as support for signal/slots, use this if you are creating a binding for a Qt-based library.</dd>
<dt><code>&#8211;enable-return-value-heuristic</code></dt>
<dd> Enable heuristics to detect parent relationship on return values (USE WITH CAUTION!)</dd></dl>
<h3>Shiboken options:</h3>
<dl>
<dt><code>&#8211;disable-verbose-error-messages</code></dt>
<dd> Disable verbose error messages. Turn the python code hard to debug but safe few kB on the generated bindings.</dd>
<dt><code>&#8211;enable-parent-ctor-heuristic</code></dt>
<dd> Enable heuristics to detect parent relationship on constructors.</dd>
<dt><code>&#8211;enable-pyside-extensions</code></dt>
<dd> Enable PySide extensions, such as support for signal/slots, use this if you are creating a binding for a Qt-based library.</dd>
<dt><code>&#8211;enable-return-value-heuristic</code></dt>
<dd> Enable heuristics to detect parent relationship on return values (USE WITH CAUTION!)</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009-2010 Nokia Corporation and/or its subsidiary(<code>-ies</code>)</p>
<h2>AUTHOR</h2>
<p> This manpage was written for Debian, starting with a help2man output, by Didier Raboud &lt;didier [at] raboud.com&gt;, on the 26. March 2010. </p>
