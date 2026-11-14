---
title: "uim-xim(1)"
name: "uim-xim"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uim-xim/"
description: "uim-xim – XIM interface to UIM"
---

<h2>NAME</h2>
<p> <code>uim-xim </code>&#8211; XIM interface to UIM</p>
<h2>SYNOPSIS</h2>
<pre>
uim-xim [<i>options</i>] 
</pre>
<h2>DESCRIPTION</h2>
<p> uim-xim is a XIM interface to UIM that allows programs that can only interface with XIM input methods to work with UIM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show usage</p>
<dt><code>&#8211;version</code></p>
<dd> Show version</p>
<dt><code>&#8211;list</code></p>
<dd> List available backend conversion engines</p>
<dt><code>&#8211;engine=ENGINE</code></p>
<dd> Use ENGINE as a backend conversion engine at startup</p>
<dt><code>&#8211;async</code></p>
<dd> Use on-demand-synchronous method of XIM event flow (using this option is not safe for Tcl/Tk GUI toolkit)</p>
<dt><code>&#8211;trace</code></p>
<dd> Trace connections</p>
<dt><code>&#8211;trace-xim</code></p>
<dd> Trace XIM messages</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Wesley J. Landaker &lt;wjl [at] icecavern.net&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
