---
title: "unicodetoupper(3)"
name: "unicodetoupper"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodetoupper/"
description: "unicode::tolower, unicode::toupper – unicode version of"
---

<p>unicode::tolower, unicode::toupper &#8211; unicode version of <code></p>
<p><a href="/docs/linux/man/3-tolower/">tolower</a></code>(3) and <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

std::string unicode::tolower(const std::string &amp;string);

std::string unicode::tolower(const std::string &amp;string, const std::string &amp;charset);

std::vector&lt;unicode_char&gt; unicode::tolower(const std::vector&lt;unicode_char&gt; &amp;u);

std::string unicode::toupper(const std::string &amp;string);

std::string unicode::toupper(const std::string &amp;string, const std::string &amp;charset);

std::vector&lt;unicode_char&gt; unicode::toupper(const std::vector&lt;unicode_char&gt; &amp;u);</code></pre>
<h2>Description</h2>
<dd>These functions convert the <i>string</i> parameter, in <i>charset</i> or <code><a href="/docs/linux/man/3-unicode_default_chset/">unicode_default_chset</a></code>(3), to unicode, replace each character with <code><a href="/docs/linux/man/3-unicode_lc/">unicode_lc</a></code>(3) or <code><a href="/docs/linux/man/3-unicode_uc/">unicode_uc</a></code>(3), then convert it back to the same character set, returning the resulting string. </p>
<p> Passing a const std::vector&lt;unicode_char&gt; &amp; directly also converts it accordingly, returning the converted unicode string.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
