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
<pre>
uim-xim [<i>options</i>] 
</pre>
<p> uim-xim is a XIM interface to UIM that allows programs that can only interface with XIM input methods to work with UIM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Show usage</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version</dd>
<dt><code>&#8211;list</code></dt>
<dd> List available backend conversion engines</dd>
<dt><code>&#8211;engine=ENGINE</code></dt>
<dd> Use ENGINE as a backend conversion engine at startup</dd>
<dt><code>&#8211;async</code></dt>
<dd> Use on-demand-synchronous method of XIM event flow (using this option is not safe for Tcl/Tk GUI toolkit)</dd>
<dt><code>&#8211;trace</code></dt>
<dd> Trace connections</dd>
<dt><code>&#8211;trace-xim</code></dt>
<dd> Trace XIM messages</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Wesley J. Landaker &lt;wjl [at] icecavern.net&gt;, for the Debian project (but may be used by others). </p>
