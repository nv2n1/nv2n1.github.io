---
title: "phpcompatinfo(1)"
name: "phpcompatinfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-phpcompatinfo/"
description: "phpcompatinfo – PHP library that parse any data source to find out the minimum version and extensions required for it to run."
---

<h2>SYNOPSIS</h2>
<p> <code>phpcompatinfo</code> [<i>options</i>] <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) command parse any data source, defined in a json configuration file, to find out elements, such as classes, interfaces, functions, constants, namespaces.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display this help message.</dd></dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
</dt><dd> Do not output any message.</dd></dl>
<p> <code>-v|vv|v, &#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.</dd></dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
</dt><dd> Display this application version.</dd></dl>
<p> <code>&#8211;ansi</code></p>
<dl>
<dt>
</dt><dd> Force ANSI output.</dd></dl>
<p> <code>&#8211;no-ansi</code></p>
<dl>
<dt>
</dt><dd> Disable ANSI output.</dd></dl>
<p> <code>&#8211;profile</code></p>
<dl>
<dt>
</dt><dd> Display timing and memory usage information.</dd></dl>
<p> <code>&#8211;progress</code></p>
<dl>
<dt>
</dt><dd> Show progress bar.</dd></dl>
<p> <code>&#8211;output</code></p>
<dl>
<dt>
</dt><dd> Write results to file or URL.</dd></dl>
<p> <code>&#8211;manifest</code></p>
<dl>
<dt>
</dt><dd> Show which versions of dependencies are bundled (PHAR version only).</dd></dl>
<h2>ANALYSER:LIST COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>analyser:list</i> command is used to show what analysers are installed (see CONF FILES section).</p>
<h2>ANALYSER:RUN COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>analyser:run</i> command is used to analyse a data source and display results. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
phpcompatinfo analyser : run[--alias][--format[= "..."]][--filter[= "..."]] source[analysers1]...[analysersN]
</code></pre>
</dd></dl>
<p> Where: </p>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
</dt><dd> If set, the source refers to its alias</dd></dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
</dt><dd> If set, convert result to a specific format. (default: false)</dd></dl>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
</dt><dd> Resource that provide a closure to filter results. (default: false)</dd></dl>
<p> <code>source</code></p>
<dl>
<dt>
</dt><dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dd></dl>
<p> <code>analysers1</code> &#8230; <code>analysersN</code></p>
<dl>
<dt>
</dt><dd> Identify one or more analyser to execute. See <i>analyser:list</i> command to know what analysers are available. (default: [&quot;compatibility&quot;])</dd></dl>
<h2>CONFIG:VALIDATE COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>config:validate</i> command is used to check syntax of your json configuration file </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
<pre>
phpcompatinfo config:validate [file]
</pre>
</dd></dl>
<p> Where: </p>
<p> <code>file</code></p>
<dl>
<dt>
</dt><dd> Path to phpcompatinfo.json file (optional)</dd></dl>
<h2>DIAGNOSE:RUN COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>diagnose:run</i> command is used to identify common errors on a platform. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
<pre>
phpcompatinfo diagnose:run [-vv|-vvv]
</pre>
</dd></dl>
<h2>DIAGRAM:CLASS COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>diagram:class</i> command is used to generate diagram about a user class present in a data source </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
phpcompatinfo diagram : class[&#8211;alias][&#8211;engine[= &#8220;&#8230;&#8221;]] argument source
</dd></dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
</dt><dd> Name of the class to inspect</dd></dl>
<p> <code>source</code></p>
<dl>
<dt>
</dt><dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dd></dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
</dt><dd> If set, the source refers to its alias</dd></dl>
<p> <code>&#8211;engine</code></p>
<dl>
<dt>
</dt><dd> Graphical syntax. (default: &quot;plantuml&quot;)</dd></dl>
<h2>DIAGRAM:PACKAGE COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>diagram:package</i> command is used to generate diagram about namespaces in a data source </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
phpcompatinfo diagram : package[&#8211;alias][&#8211;engine[= &#8220;&#8230;&#8221;]] source
</dd></dl>
<p> Where: </p>
<p> <code>source</code></p>
<dl>
<dt>
</dt><dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dd></dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
</dt><dd> If set, the source refers to its alias</dd></dl>
<p> <code>&#8211;engine</code></p>
<dl>
<dt>
</dt><dd> Graphical syntax. (default: &quot;plantuml&quot;)</dd></dl>
<h2>PLUGIN:LIST COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>plugin:list</i> command is used to show what plugins are installed (see CONF FILES section).</p>
<h2>REFERENCE:LIST COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>reference:list</i> command is used to list all references supported. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
<pre>
phpcompatinfo reference:list
</pre>
</dd></dl>
<h2>REFERENCE:SHOW COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>reference:show</i> command is used to introspect a reference. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
phpcompatinfo reference : show[&#8211;filter[= &#8220;&#8230;&#8221;]][&#8211;releases][&#8211;ini][&#8211;constants][&#8211;functions][&#8211;interfaces][&#8211;classes] name
</dd></dl>
<p> Where: </p>
<p> <code>name</code></p>
<dl>
<dt>
</dt><dd> Introspection of a reference (case insensitive)</dd></dl>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
</dt><dd> Resource that provide a closure to filter results (default: false)</dd></dl>
<p> <code>&#8211;releases</code></p>
<dl>
<dt>
</dt><dd> Show releases</dd></dl>
<p> <code>&#8211;ini</code></p>
<dl>
<dt>
</dt><dd> Show ini Entries</dd></dl>
<p> <code>&#8211;constants</code></p>
<dl>
<dt>
</dt><dd> Show constants</dd></dl>
<p> <code>&#8211;functions</code></p>
<dl>
<dt>
</dt><dd> Show functions</dd></dl>
<p> <code>&#8211;interfaces</code></p>
<dl>
<dt>
</dt><dd> Show interfaces</dd></dl>
<p> <code>&#8211;classes</code></p>
<dl>
<dt>
</dt><dd> Show classes</dd></dl>
<h2>REFLECTION:CLASS COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>reflection:class</i> command is used to give information about a user class present in a data source. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
phpcompatinfo reflection : class[&#8211;alias][&#8211;return = &#8220;&#8230;&#8221;] argument source
</dd></dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
</dt><dd> Name of the class to reflect.</dd></dl>
<p> <code>source</code></p>
<dl>
<dt>
</dt><dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dd></dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
</dt><dd> If set, the source refers to its alias</dd></dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
</dt><dd> Format of result to return. False when raw text. (default: false)</dd></dl>
<h2>REFLECTION:FUNCTION COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpcompatinfo/">phpcompatinfo</a>(1) <i>reflection:function</i> command is used to give information about a user function present in a data source. </p>
<p> Usage: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
phpcompatinfo reflection : function[--alias][--return = "..."] argument source
</code></pre>
</dd></dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
</dt><dd> Name of the function to reflect.</dd></dl>
<p> <code>source</code></p>
<dl>
<dt>
</dt><dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dd></dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
</dt><dd> If set, the source refers to its alias</dd></dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
</dt><dd> Format of result to return. False when raw text. (default: false)</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
</dt><dd> Success</dd></dl>
<p> <code>1</code></p>
<dl>
<dt>
</dt><dd> Failure (syntax or usage error; configuration error; unexpected error).</dd></dl>
<h2>CONF FILES</h2>
<p> A configuration file contains data sources that can be analysed, but also optional plugins and analysers installed. Require configuration file is loaded in the following order: </p>
<dl>
<dt>
</dt><dd> 1. The CONF_FILE specified by the environment variables BARTLETTRC and BARTLETT_SCAN_DIR.</dd></dl>
<dl>
<dt>
</dt><dd> 2. phpcompatinfo.json from the current directory.</dd></dl>
<dl>
<dt>
</dt><dd> 3. phpcompatinfo.json from the User $HOME/.config directory.</dd></dl>
<dl>
<dt>
</dt><dd> 4. phpcompatinfo.json from the /etc directory.</dd></dl>
<h2>BUGS</h2>
<p> Report any issue at <a rel="nofollow" href="https://github.com/llaville/php-compat-info/issues">https://github.com/llaville/php-compat-info/issues</a></p>
<h2>AUTHORS</h2>
<p> PHP_CompatInfo was originally written by Davey Shafik in 2004. </p>
<p> Remi Collet, contributor of many extensions reference and unit tests, joined the project since version 2.0.0RC2 </p>
<p> The Command-Line Interface (CLI) version was introduced in version 2.0 and is written by Laurent Laville.</p>
<h2>SEE ALSO</h2>
<p> Main web site: <a rel="nofollow" href="http://php5.laurent-laville.org/compatinfo/">http://php5.laurent-laville.org/compatinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2015 Laurent Laville.</p>
<h2>LICENSE</h2>
<p> Free use of this software is granted under the terms of the BSD 3-clause license. </p>
