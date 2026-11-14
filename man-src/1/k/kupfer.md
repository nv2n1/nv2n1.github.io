---
title: "kupfer(1)"
name: "kupfer"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kupfer/"
description: "kupfer – Convenient command and access tool for applications and documents"
---

<h2>NAME</h2>
<p> kupfer &#8211; Convenient command and access tool for applications and documents</p>
<h2>SYNOPSIS</h2>
<pre>
<code>kupfer</code> [ <i>OPTIONS</i> | <i>FILE</i> ... ]
<code>kupfer-exec</code> <i>FILE</i> ...
</pre>
<h2>DESCRIPTION</h2>
<p> Kupfer is an interface for quick and convenient access to applications and their documents. </p>
<p> The most typical use is to find a specific application and launch it. We have tried to make Kupfer easy to extend with plugins so that this quick-access paradigm can be extended to many more objects than just applications. </p>
<p> <code>kupfer-exec</code> is a helper script that can execute commands saved to file, but only by connecting to an already running instance of Kupfer.</p>
<h2>SPAWNING</h2>
<p> Running kupfer on the command line (without options) will try to show the program it if already running. </p>
<p> Kupfer can be invoked with a list of files <code>kupfer</code> <i>FILE</i> &#8230; </p>
<p> This can be used to select files given as command-line arguments in the program. Then you can invoke actions even on objects from a shell-based context. </p>
<p> You may also pipe text to <code>kupfer</code> to pass it to a currently running instance of the program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-splash</code></p>
<dd> Launch without presenting main interface</p>
<dt><code>&#8211;list-plugins</code></p>
<dd> Display a list of all installed plugins</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable more verbose output that can help understanding the program&#8217;s operation.</p>
<dt><code>&#8211;relay</code></p>
<dd> Is deprecated and will be started by the Multihead Support plugin when needed</p>
<dt><code>&#8211;exec-helper=</code><i>HELPER</i></p>
<dd> Run plugin helper program, which should be the name of a module inside kupfer. </p>
<p> The following are generic options</p>
<dt><code>&#8211;help</code></p>
<dd> Display usage information</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information</dl>
<h2>CONFIGURATION</h2>
<p> Custom plugins are added to kupfer by installing them to the directory <i>~/.local/share/kupfer/plugins</i>, or any kupfer/plugins directory in any of <code>$XDG_DATA_DIRS</code>.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> If <i>KUPFER_NO_CUSTOM_PLUGINS</i> is set, only allow loading built-in plugins (installed in the program&#8217;s python package). </p>
<p> If <i>KUPFER_NO_CACHE</i> is set, do not load from or write to any source cache files.</p>
<h2>AUTHOR</h2>
<p> Ulrik Sverdrup &lt;ulrik.sverdrup [at] gmail.com&gt; </p>
<h2>Index</h2>
