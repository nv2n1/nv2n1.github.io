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
<dl>
<dt> <code>dzen2-dbar</code> [-w <i>characters</i>] [-s <i>symbol</i>] [-min <i>minvalue</i>] [-max <i>maxvalue</i>] [-l <i>string</i>] [-nonl]</dt></dl>
<p> <code>dbar</code></p>
<dd>is an application that generates semi graphical progress meters, from some values you supply to it. </dd>
<p> See the usage examples for a description of the expected input format.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-max</code></dt>
<dd> Value to be considered 100% (default: 100)</dd>
<dt><code>-min</code></dt>
<dd> Value to be considered 0% (default: 0)</dd>
<dt><code>-w</code></dt>
<dd> Number of charcaters to be considered 100% in the bar (default: 25 )</dd>
<dt><code>-s</code></dt>
<dd> Symbol represeting the percentage value in the bar (default: = )</dd>
<dt><code>-l</code></dt>
<dd> label to be prepended to the bar (default: &#8221; )</dd>
<dt><code>-nonl</code></dt>
<dd> no new line, don&#8217;t put &#8216; at the end of the bar (default: do print &#8216;)</dd></dl>
<h2>USAGE EXAMPLES</h2>
<dl>
<dt><code>Static 0% and 100% mark or single value input:</code></dt>
<dd> Command: echo 25 | dbar -m 100 -l Sometext<br />
 Output: Sometext 25% [====== ]</dd>
<dt><code>If your 100% mark changes dynamically or 2-values input:</code></dt>
<dd> Command: echo &quot;50 150&quot; | dbar<br />
 Output: 33% [======== ]</dd>
<dt><code>If your value range is not between [0, maxval] or 3-values input:</code></dt>
<dd> Command: echo &quot;50 -25 150&quot; | dbar<br />
 Output: 43% [=========== ]</dd></dl>
<p> Dbar was written by Robert Manea. </p>
<p> This manual page was written by bertagaz &lt;bertagaz [at] ptitcanardnoir.org&gt;, for the Debian project (but may be used by others). </p>
