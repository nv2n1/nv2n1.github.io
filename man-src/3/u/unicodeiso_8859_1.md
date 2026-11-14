---
title: "unicodeiso_8859_1(3)"
name: "unicodeiso_8859_1"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodeiso_8859_1/"
description: "unicode::iconvert::convert, unicode::ucs_4, unicode::ucs_2, unicode::utf_8, unicode::iso_8859_1 – unicode character set conversion"
---

<p>unicode::iconvert::convert, unicode::ucs_4, unicode::ucs_2, unicode::utf_8, unicode::iso_8859_1 &#8211; unicode character set conversion</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

extern const char unicode::ucs_4[];
extern const char unicode::ucs_2[];
extern const char unicode::utf_8[];
extern const char unicode::iso_8859_1[];

std::string unicode::iconvert::convert(const std::string &amp;text, const std::string &amp;srccharset, const std::string &amp;dstcharset);

std::string unicode::iconvert::convert(const std::string &amp;text, const std::string &amp;srccharset, const std::string &amp;dstcharset, bool &amp;errflag);

std::string unicode::iconvert::convert(const std::vector&lt;unicode_char&gt; &amp;text, const std::string &amp;dstcharset);

std::string unicode::iconvert::convert(const std::vector&lt;unicode_char&gt; &amp;text, const std::string &amp;dstcharset, bool &amp;errflag);

bool unicode::iconvert::convert(const std::string &amp;text, const std::string &amp;charset, std::vector&lt;unicode_char&gt; &amp;text);</code></pre>
<h2>Description</h2>
<dd>The overloaded <code>unicode::convert::convert</code>() functions convert: </p>
<dl>
<dd>&bull; A text string between two different character sets, returning the new string.</dl>
<dl>
<dd>&bull; A vector of unicode characters (not null-terminated) to a character string in a supported character set.</dl>
<dl>
<dd>&bull; Initialize a vector of unicode characters, passed by reference, by converting a text string in a given character set to unicode.</dl>
<p> These functions use <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), and can use any character set that&#8217;s supported by <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3). Use <i>unicode::ucs_2</i> and <i>unicode::ucs_4</i> to specify the 16 and the 32 bit unicode octet in native byte order. Use <i>unicode::utf_8</i> and <i>unicode::iso_8859_1</i> to specify these two standard character sets. The overloaded versions that pass a reference to a bool set the flag to true if some characters could not be converted. The overloaded version that initializes a unicode vector returns the bool flag, instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode--convert--convert_tocase/">unicode::convert::convert_tocase</a></code>(3), <code><a href="/docs/linux/man/3-unicode_convert/">unicode_convert</a></code>(3), m[blue]<code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)m[]<font SIZE="-2">[1]</font>.</p>
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
