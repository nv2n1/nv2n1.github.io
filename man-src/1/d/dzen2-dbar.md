---
title: "dzen2-dbar(1)"
name: "dzen2-dbar"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dzen2-dbar/"
description: "dzen2-dbar – simple gadget that you can use in combination with dzen to display a progressbar."
---

<h2>NAME</h2>
<p> dzen2-dbar &#8211; simple gadget that you can use in combination with dzen to display a progressbar.</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dzen2-dbar</code> [-w <i>characters</i>] [-s <i>symbol</i>] [-min <i>minvalue</i>] [-max <i>maxvalue</i>] [-l <i>string</i>] [-nonl]</dl>
<h2>DESCRIPTION</h2>
<p> <code>dbar</code></p>
<dd>is an application that generates semi graphical progress meters, from some values you supply to it. </p>
<p> See the usage examples for a description of the expected input format.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-max</code></p>
<dd> Value to be considered 100% (default: 100)</p>
<dt><code>-min</code></p>
<dd> Value to be considered 0% (default: 0)</p>
<dt><code>-w</code></p>
<dd> Number of charcaters to be considered 100% in the bar (default: 25 )</p>
<dt><code>-s</code></p>
<dd> Symbol represeting the percentage value in the bar (default: = )</p>
<dt><code>-l</code></p>
<dd> label to be prepended to the bar (default: &#8221; )</p>
<dt><code>-nonl</code></p>
<dd> no new line, don&#8217;t put &#8216; at the end of the bar (default: do print &#8216;)</dl>
<h2>USAGE EXAMPLES</h2>
<dl>
<dt><code>Static 0% and 100% mark or single value input:</code></p>
<dd> Command: echo 25 | dbar -m 100 -l Sometext<br />
 Output: Sometext 25% [====== ]</p>
<dt><code>If your 100% mark changes dynamically or 2-values input:</code></p>
<dd> Command: echo &quot;50 150&quot; | dbar<br />
 Output: 33% [======== ]</p>
<dt><code>If your value range is not between [0, maxval] or 3-values input:</code></p>
<dd> Command: echo &quot;50 -25 150&quot; | dbar<br />
 Output: 43% [=========== ]</dl>
<p> Dbar was written by Robert Manea. </p>
<p> This manual page was written by bertagaz &lt;bertagaz [at] ptitcanardnoir.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
