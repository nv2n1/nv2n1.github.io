---
title: "unicodeiconvertconvert_tocase(3)"
name: "unicodeiconvertconvert_tocase"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodeiconvertconvert_tocase/"
description: "unicode::iconvert::convert_tocase – unicode uppercase, lowercase, and titlecase conversion"
---

<p>unicode::iconvert::convert_tocase &#8211; unicode uppercase, lowercase, and titlecase conversion</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

std::string unicode::iconvert::convert_tocase(const std::string &amp;text, const std::string &amp;charset, unicode_char (*first_char_func)(unicode_char), unicode_char (*char_func)(unicode_char));

std::string unicode::iconvert::convert_tocase(const std::string &amp;text, const std::string &amp;charset, bool &amp;err, unicode_char (*first_char_func)(unicode_char), unicode_char (*char_func)(unicode_char));</code></pre>
<h2>Description</h2>
<dd>The overloaded <code>unicode::convert::convert_tocase</code>() function converts the <i>text</i> parameter, in the <i>charset</i> characters to lowercase, uppercase, and titlecase. <i>text</i> gets converted, internally, into unicode. <i>first_char_func</i> and <i>char_func</i> are either: <code>unicode_lc</code>, <code>unicode_uc</code>, or <code>unicode_tc</code>. If the converted text string is not empty, <i>first_char_func</i> converts the first unicode character in the text string, and <i>char_func</i> converts any remaining characters. <code>unicode_lc</code> converts its character to lowercase, <code>unicode_uc</code> to uppercase, and <code>unicode_tc</code> to titlecase. Finally, the unicode string gets converted back to <i>charset</i>, which gets returned. </p>
<p> The optional <i>err</i> parameter gets set to true if an error was encounted converting the text string to or from unicode.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode--convert--convert/">unicode::convert::convert</a></code>(3), <code><a href="/docs/linux/man/3-unicode_convert/">unicode_convert</a></code>(3), m[blue]<code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)m[]<font SIZE="-2">[1]</font>.</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)</p>
<dl>
<dd><a rel="nofollow" href="http://manpages.courier-mta.org/htmlman3/iconv.3.html">http://manpages.courier-mta.org/htmlman3/iconv.3.html</a></dl>
