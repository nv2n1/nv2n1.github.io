---
title: "unicode_script(3)"
name: "unicode_script"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_script/"
description: "unicode_script – unicode script property"
---

<p>unicode_script &#8211; unicode script property</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;





unicode_script_t unicode_script(unicode_char ch);</code></pre>
<h2>Description</h2>
<p><code>unicode_script</code>() looks up the &#8220;script&#8221;</p>
<dd>property of the specified unicode character, and returns it. The unicode_script_t enumeration encodes possible unicode script values. unicode_script_unknown gets returned for a unicode character with an unknown script property.</p>
<h2>See Also</h2>
<p>m[blue]<code>TR-24</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>TR-24</p>
<dl>
<dd><a rel="nofollow" href="http://www.unicode.org/reports/tr24/tr24-24.html">http://www.unicode.org/reports/tr24/tr24-24.html</a></dl>
