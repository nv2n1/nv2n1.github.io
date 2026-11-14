---
title: "unicode_convert_tocase(3)"
name: "unicode_convert_tocase"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicode_convert_tocase/"
description: "unicode_uc, unicode_lc, unicode_tc, unicode_convert_tocase – unicode uppercase, lowercase, and titlecase character lookup"
---

<p>unicode_uc, unicode_lc, unicode_tc, unicode_convert_tocase &#8211; unicode uppercase, lowercase, and titlecase character lookup</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

unicode_char unicode_uc(unicode_char c);

unicode_char unicode_lc(unicode_char c);

unicode_char unicode_tc(unicode_char c);

char *unicode_convert_tocase(const char *str, const char *charset, unicode_char (*first_char_func)(uncode_char), unicode_char (*char_func)(uncode_char));</code></pre>
<h2>Description</h2>
<p><code>unicode_uc</code>(), <code>unicode_lc</code>(), <code>unicode_tc</code>() return the uppercase, lowercase, or the titlecase equivalent of the unicode character <i>c</i>. If this character does not have an uppercase, lowercase, or a titlecase equivalent, these functions return <i>c</i>, the same character. </p>
<p> <code>unicode_convert_tocase</code>() takes the string <i>str</i></p>
<dd>in the character set <i>charset</i>. <i>first_char_func</i> and <i>char_func</i>, each, should be <code>unicode_uc</code>, <code>unicode_lc</code>, or <code>unicode_tc</code>. <code>unicode_convert_tocase</code>() returns a malloc()ed buffer. The first unicode character in <i>str</i> gets processed by <i>first_char_func</i>, and all other characters by <i>char_func</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_convert/">unicode_convert</a></code>(3), <code><a href="/docs/linux/man/3-unicode_default_chset/">unicode_default_chset</a></code>(3), <code><a href="/docs/linux/man/3-unicode_html40ent_lookup/">unicode_html40ent_lookup</a></code>(3), <code><a href="/docs/linux/man/3-unicode_category_lookup/">unicode_category_lookup</a></code>(3), <code><a href="/docs/linux/man/3-unicode_grapheme_break/">unicode_grapheme_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
