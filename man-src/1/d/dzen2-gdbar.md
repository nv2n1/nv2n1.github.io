---
title: "dzen2-gdbar(1)"
name: "dzen2-gdbar"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dzen2-gdbar/"
description: "dzen2-gdbar – generates fully graphical progress meters"
---

<h2>NAME</h2>
<p> dzen2-gdbar &#8211; generates fully graphical progress meters</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dzen2-gdbar</code> [-w <i>characters</i>] [-s <i>symbol</i>] [-fg <i>color</i>] [-bg <i>color</i>] [-min <i>minvalue</i>] [-max <i>maxvalue</i>] [-l <i>string</i>] [-nonl] [-o]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gdbar</code></p>
<dd>application that generates fully graphical progress meters, from some values you supply to it. </p>
<p> It has the same input semantics as dbar (see <code>dbar (1)</code> ). In contrast to dbar, gdbar draws fully graphical meters which are only useful in combination with dzen. </p>
<p> See the usage examples for a description of the expected input format.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-max</code></p>
<dd> Value to be considered 100% (default: 100)</p>
<dt><code>-min</code></p>
<dd> Value to be considered 0% (default: 0)</p>
<dt><code>-fg</code></p>
<dd> Foreground color. (default white)</p>
<dt><code>-bg</code></p>
<dd> Bacground color (default darkgrey)</p>
<dt><code>-w</code></p>
<dd> Size in pixels to be considered 100% in the bar (default: 80 )</p>
<dt><code>-h</code></p>
<dd> Bar height.</p>
<dt><code>-l</code></p>
<dd> label to be prepended to the bar (default: &#8221; )</p>
<dt><code>-o</code></p>
<dd> Draw conky style meters.</p>
<dt><code>-nonl</code></p>
<dd> no new line, don&#8217;t put &#8216; at the end of the bar (default: do print &#8216;)</dl>
<p> Dbar was written by Robert Manea. </p>
<p> This manual page was written by bertagaz &lt;bertagaz [at] ptitcanardnoir.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
