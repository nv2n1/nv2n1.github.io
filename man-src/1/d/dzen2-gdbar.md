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
<dt> <code>dzen2-gdbar</code> [-w <i>characters</i>] [-s <i>symbol</i>] [-fg <i>color</i>] [-bg <i>color</i>] [-min <i>minvalue</i>] [-max <i>maxvalue</i>] [-l <i>string</i>] [-nonl] [-o]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gdbar</code></p>
<dd>application that generates fully graphical progress meters, from some values you supply to it. </dd>
<p> It has the same input semantics as dbar (see <code>dbar (1)</code> ). In contrast to dbar, gdbar draws fully graphical meters which are only useful in combination with dzen. </p>
<p> See the usage examples for a description of the expected input format.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-max</code></dt>
<dd> Value to be considered 100% (default: 100)</dd>
<dt><code>-min</code></dt>
<dd> Value to be considered 0% (default: 0)</dd>
<dt><code>-fg</code></dt>
<dd> Foreground color. (default white)</dd>
<dt><code>-bg</code></dt>
<dd> Bacground color (default darkgrey)</dd>
<dt><code>-w</code></dt>
<dd> Size in pixels to be considered 100% in the bar (default: 80 )</dd>
<dt><code>-h</code></dt>
<dd> Bar height.</dd>
<dt><code>-l</code></dt>
<dd> label to be prepended to the bar (default: &#8221; )</dd>
<dt><code>-o</code></dt>
<dd> Draw conky style meters.</dd>
<dt><code>-nonl</code></dt>
<dd> no new line, don&#8217;t put &#8216; at the end of the bar (default: do print &#8216;)</dd></dl>
<p> Dbar was written by Robert Manea. </p>
<p> This manual page was written by bertagaz &lt;bertagaz [at] ptitcanardnoir.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
