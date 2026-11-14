---
title: "shiboken(1)"
name: "shiboken"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shiboken/"
description: "shiboken – CPython bindings generator for C++ libraries"
---

<h2>NAME</h2>
<p> shiboken &#8211; CPython bindings generator for C++ libraries</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> shiboken [options] header-file typesystem-file</dl>
<h3>General options:</h3>
<dl>
<dt><code>&#8211;debug-level</code>=<i>[sparse</i>|medium|full]</p>
<dd> Set the debug level</p>
<dt><code>&#8211;documentation-only</code></p>
<dd> Do not generates any code, just the documentation</p>
<dt><code>&#8211;generatorSet</code></p>
<dd> generatorSet to be used. e.g. qtdoc</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help and exit</p>
<dt><code>&#8211;include-paths=</code>&lt;path&gt;[:&lt;path&gt;:&#8230;]</p>
<dd> Include paths used by the C++ parser</p>
<dt><code>&#8211;license-file</code>=<i>[licensefile]</i></p>
<dd> File used for copyright headers of generated files</p>
<dt><code>&#8211;no-suppress-warnings</code></p>
<dd> Show all warnings</p>
<dt><code>&#8211;output-directory</code>=<i>[dir]</i></p>
<dd> The directory where the generated files will be written</p>
<dt><code>&#8211;silent</code></p>
<dd> Avoid printing any message</p>
<dt><code>&#8211;typesystem-paths=</code>&lt;path&gt;[:&lt;path&gt;:&#8230;]</p>
<dd> Paths used when searching for typesystems</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit</dl>
<h3>Shiboken options:</h3>
<dl>
<dt><code>&#8211;disable-verbose-error-messages</code></p>
<dd> Disable verbose error messages. Turn the python code hard to debug but safe few kB on the generated bindings.</p>
<dt><code>&#8211;enable-parent-ctor-heuristic</code></p>
<dd> Enable heuristics to detect parent relationship on constructors.</p>
<dt><code>&#8211;enable-pyside-extensions</code></p>
<dd> Enable PySide extensions, such as support for signal/slots, use this if you are creating a binding for a Qt-based library.</p>
<dt><code>&#8211;enable-return-value-heuristic</code></p>
<dd> Enable heuristics to detect parent relationship on return values (USE WITH CAUTION!)</dl>
<h3>Shiboken options:</h3>
<dl>
<dt><code>&#8211;disable-verbose-error-messages</code></p>
<dd> Disable verbose error messages. Turn the python code hard to debug but safe few kB on the generated bindings.</p>
<dt><code>&#8211;enable-parent-ctor-heuristic</code></p>
<dd> Enable heuristics to detect parent relationship on constructors.</p>
<dt><code>&#8211;enable-pyside-extensions</code></p>
<dd> Enable PySide extensions, such as support for signal/slots, use this if you are creating a binding for a Qt-based library.</p>
<dt><code>&#8211;enable-return-value-heuristic</code></p>
<dd> Enable heuristics to detect parent relationship on return values (USE WITH CAUTION!)</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009-2010 Nokia Corporation and/or its subsidiary(<code>-ies</code>)</p>
<h2>AUTHOR</h2>
<p> This manpage was written for Debian, starting with a help2man output, by Didier Raboud &lt;didier [at] raboud.com&gt;, on the 26. March 2010. </p>
<h2>Index</h2>
