---
title: "phpreflect(1)"
name: "phpreflect"
section: "1"
letter: "p"
url: "/docs/linux/man/1-phpreflect/"
description: "phpreflect – Reverse-engineer classes, interfaces, functions, constants, namespaces and more"
---

<h2 class="name">NAME</h2>
<p> phpreflect &#8211; Reverse-engineer classes, interfaces, functions, constants, namespaces and more </p>
<h2>SYNOPSIS</h2>
<p> <code>phpreflect</code> [<i>options</i>] <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) command parse any data source, to find out elements, such as classes, interfaces, functions, constants, namespaces.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display this help message.</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
<dd> Do not output any message.</dl>
<p> <code>-v|vv|v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Display this application version.</dl>
<p> <code>&#8211;ansi</code></p>
<dl>
<dt>
<dd> Force ANSI output.</dl>
<p> <code>&#8211;no-ansi</code></p>
<dl>
<dt>
<dd> Disable ANSI output.</dl>
<p> <code>&#8211;profile</code></p>
<dl>
<dt>
<dd> Display timing and memory usage information.</dl>
<p> <code>&#8211;progress</code></p>
<dl>
<dt>
<dd> Show progress bar.</dl>
<p> <code>&#8211;output</code></p>
<dl>
<dt>
<dd> Write results to file or URL.</dl>
<p> <code>&#8211;manifest</code></p>
<dl>
<dt>
<dd> Show which versions of dependencies are bundled (PHAR version only).</dl>
<h2>ANALYSER:LIST COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>analyser:list</i> command is used to show what analysers are installed (see CONF FILES section).</p>
<h2>ANALYSER:RUN COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>analyser:run</i> command is used to analyse a data source and display results. </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
<pre><code>
phpreflect analyser : run[--alias][--format[= "..."]][--filter[= "..."]] source[analysers1]...[analysersN]
</code></pre>
</dl>
<p> Where: </p>
<p> <code>source</code></p>
<dl>
<dt>
<dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
<dd> If set, the source refers to its alias</dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
<dd> If set, convert result to a specific format. (default: false)</dl>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
<dd> Resource that provide a closure to filter results. (default: false)</dl>
<p> <code>analysers1</code> &#8230; <code>analysersN</code></p>
<dl>
<dt>
<dd> Identify one or more analyser to execute. See <i>analyser:list</i> command to know what analysers are available. (default: [&quot;structure&quot;])</dl>
<h2>CONFIG:VALIDATE COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>config:validate</i> command is used to check syntax of your json configuration file </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
<pre>
phpreflect config:validate [file]
</pre>
</dl>
<p> Where: </p>
<p> <code>file</code></p>
<dl>
<dt>
<dd> Path to phpreflect.json file (optional)</dl>
<h2>DIAGNOSE:RUN COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>diagnose:run</i> command is used to identify common errors on a platform. </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
<pre>
phpreflect diagnose:run [-vv|-vvv]
</pre>
</dl>
<h2>DIAGRAM:CLASS COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>diagram:class</i> command is used to generate diagram about a user class present in a data source </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
phpreflect diagram : class[&#8211;alias][&#8211;engine[= &#8220;&#8230;&#8221;]] argument source
</dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
<dd> Name of the class to inspect</dl>
<p> <code>source</code></p>
<dl>
<dt>
<dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
<dd> If set, the source refers to its alias</dl>
<p> <code>&#8211;engine</code></p>
<dl>
<dt>
<dd> Graphical syntax. (default: &quot;plantuml&quot;)</dl>
<h2>DIAGRAM:PACKAGE COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>diagram:package</i> command is used to generate diagram about namespaces in a data source </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
phpreflect diagram : package[&#8211;alias][&#8211;engine[= &#8220;&#8230;&#8221;]] argument source
</dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
<dd> Name of the namespace to inspect</dl>
<p> <code>source</code></p>
<dl>
<dt>
<dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
<dd> If set, the source refers to its alias</dl>
<p> <code>&#8211;engine</code></p>
<dl>
<dt>
<dd> Graphical syntax. (default: &quot;plantuml&quot;)</dl>
<h2>PLUGIN:LIST COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>plugin:list</i> command is used to show what plugins are installed (see CONF FILES section).</p>
<h2>REFLECTION:CLASS COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>reflection:class</i> command is used to give information about a user class present in a data source. </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
phpreflect reflection : class[&#8211;alias][&#8211;format = &#8220;&#8230;&#8221;] argument source
</dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
<dd> Name of the class to reflect.</dl>
<p> <code>source</code></p>
<dl>
<dt>
<dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
<dd> If set, the source refers to its alias</dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
<dd> To ouput results in other formats. (default: &quot;txt&quot;)</dl>
<h2>REFLECTION:FUNCTION COMMAND</h2>
<p> The <a href="/docs/linux/man/1-phpreflect/">phpreflect</a>(1) <i>reflection:function</i> command is used to give information about a user function present in a data source. </p>
<p> Usage: </p>
<dl>
<dt>
<dd>
<pre><code>
phpreflect reflection : function[--alias][--format = "..."] argument source
</code></pre>
</dl>
<p> Where: </p>
<p> <code>argument</code></p>
<dl>
<dt>
<dd> Name of the function to reflect.</dl>
<p> <code>source</code></p>
<dl>
<dt>
<dd> Identify a data source; may be declared in a json configuration file (see CONF FILES section)</dl>
<p> <code>&#8211;alias</code></p>
<dl>
<dt>
<dd> If set, the source refers to its alias</dl>
<p> <code>&#8211;format</code></p>
<dl>
<dt>
<dd> To ouput results in other formats. (default: &quot;txt&quot;)</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failure (syntax or usage error; configuration error; unexpected error).</dl>
<h2>CONF FILES</h2>
<p> A configuration file contains data sources that can be analysed, but also optional plugins and analysers installed. Require configuration file is loaded in the following order: </p>
<dl>
<dt>
<dd> 1. The CONF_FILE specified by the environment variables BARTLETTRC and BARTLETT_SCAN_DIR.</dl>
<dl>
<dt>
<dd> 2. phpreflect.json from the current directory.</dl>
<dl>
<dt>
<dd> 3. phpreflect.json from the User $HOME/.config directory.</dl>
<dl>
<dt>
<dd> 4. phpreflect.json from the /etc directory.</dl>
<h2>BUGS</h2>
<p> Report any issue at <a rel="nofollow" href="https://github.com/llaville/php-reflect/issues">https://github.com/llaville/php-reflect/issues</a></p>
<h2>AUTHORS</h2>
<p> The Command-Line Interface (CLI) version was introduced in version 2.0 and is written by Laurent Laville.</p>
<h2>SEE ALSO</h2>
<p> Main web site: <a rel="nofollow" href="http://php5.laurent-laville.org/reflect/">http://php5.laurent-laville.org/reflect/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 Laurent Laville.</p>
<h2>LICENSE</h2>
<p> Free use of this software is granted under the terms of the BSD 3-clause license. </p>
<h2>Index</h2>
