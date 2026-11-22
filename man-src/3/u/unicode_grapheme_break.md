---
title: "unicode_grapheme_break(3)"
name: "unicode_grapheme_break"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_grapheme_break/"
description: "unicode_grapheme_break – unicode grapheme cluster boundary rules"
---

<p>unicode_grapheme_break &#8211; unicode grapheme cluster boundary rules</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;
int unicode_grapheme_break(unicode_char a, unicode_char b);</code></pre>
<h2>Description</h2>
<p><code>unicode_grapheme_break</code>() returns non-zero if there is a grapheme break between the two unicode characters <i>a</i></p>
<dd>and <i>b</i>.</dd>
<h2>See Also</h2>
<p>m[blue]<code>TR-29</code>m[][1], <code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_convert_tocase/">unicode_convert_tocase</a></code>(3), <code>unicode_line_break</code>(3), <code>unicode_word_break</code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>TR-29</dd>
<dl>
<dd><a rel="nofollow" href="http://www.unicode.org/reports/tr29/tr29-27.html">http://www.unicode.org/reports/tr29/tr29-27.html</a></dd></dl>
</dl>