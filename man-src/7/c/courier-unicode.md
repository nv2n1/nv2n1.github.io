---
title: "courier-unicode(7)"
name: "courier-unicode"
section: "7"
letter: "c"
url: "/docs/linux/man/7-courier-unicode/"
description: "courier-unicode – Courier Unicode Library"
---

<p>courier-unicode &#8211; Courier Unicode Library</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;</code></pre>
<h2>Description</h2>
<p>This library implements several algorithms related to the m[blue]<code>Unicode Standard</code>m[]<font SIZE="-2">[1]</font>. This library uses m[blue]<code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)m[]<font SIZE="-2">[2]</font> to convert text in a given character set to unicode. Any character set displayed by <code>iconv &#8211;list</code> can be specified for the corresponding character set parameter. Additionally, courier-unicode.h defines a special character string unicode_x_imap_modutf7 that specifies the pseudo-character set for the modified-UTF7 encoding used in IMAP. This string can also be appended by a space, and up to fifteen additional US-ASCII characters. The resulting character set also encodes these additional characters, in addition to unicode characters, with modified-UTF7.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-unicode_convert/">unicode_convert</a></code>(3), <code><a href="/docs/linux/man/3-unicode_default_chset/">unicode_default_chset</a></code>(3), <code><a href="/docs/linux/man/3-unicode_html40ent_lookup/">unicode_html40ent_lookup</a></code>(3), <code><a href="/docs/linux/man/3-unicode_category_lookup/">unicode_category_lookup</a></code>(3), <code><a href="/docs/linux/man/3-unicode_grapheme_break/">unicode_grapheme_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_script/">unicode_script</a></code>(3), <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3), <code><a href="/docs/linux/man/3-unicode_uc/">unicode_uc</a></code>(3), <code><a href="/docs/linux/man/3-unicode--iconvert--convert/">unicode::iconvert::convert</a></code>(3), <code><a href="/docs/linux/man/3-unicode--iconvert--convert_tocase/">unicode::iconvert::convert_tocase</a></code>(3), <code><a href="/docs/linux/man/3-unicode--iconvert--fromu/">unicode::iconvert::fromu</a></code>(3), <code><a href="/docs/linux/man/3-unicode--iconvert--tou/">unicode::iconvert::tou</a></code>(3), <code><a href="/docs/linux/man/3-unicode--tolower/">unicode::tolower</a></code>(3), <code><a href="/docs/linux/man/3-unicode--linebreak/">unicode::linebreak</a></code>(3), <code><a href="/docs/linux/man/3-unicode--wordbreak/">unicode::wordbreak</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Unicode Standard</p>
<dl>
<dd><a rel="nofollow" href="http://www.unicode.org/standard/standard.html">http://www.unicode.org/standard/standard.html</a></dl>
<dt> 2.</p>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)</p>
<dl>
<dd><a rel="nofollow" href="http://manpages.courier-mta.org/htmlman3/iconv.3.html">http://manpages.courier-mta.org/htmlman3/iconv.3.html</a></dl>
