---
title: "unicode_html40ent_lookup(3)"
name: "unicode_html40ent_lookup"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_html40ent_lookup/"
description: "unicode_html40ent_lookup – look up unicode character for an HTML 4.0 entity"
---

<p>unicode_html40ent_lookup &#8211; look up unicode character for an HTML 4.0 entity</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

unicode_char unicode_html40ent_lookup(const char *entity);</code></pre>
<h2>Description</h2>
<p><code>unicode_html40ent_lookup</code>() returns the unicode character represented by an HTML 4.0 entity. The <i>entity</i></p>
<dd>is a string, such as &#8220;quot&#8221;, in which case <code>unicode_html40ent_lookup</code>() returns 34. </p>
<p> Additionally, <code>unicode_html40ent_lookup</code>() parses a numerical entity given as &#8220;#<i>decimal</i>&#8221; or &#8220;#x<i>hex</i>&#8220;. </p>
<p> <code>unicode_html40ent_lookup</code>() returns 0 if the <i>entity</i> is not a known entity that represents a single unicode character.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_convert_tocase/">unicode_convert_tocase</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
