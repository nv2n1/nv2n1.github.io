---
title: "unicodeiconvertfromu(3)"
name: "unicodeiconvertfromu"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodeiconvertfromu/"
description: "unicode::iconvert::fromu – template for converting text sequence from unicode"
---

<p>unicode::iconvert::fromu &#8211; template for converting text sequence from unicode</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

output_iter_t unicode::iconvert::fromu::convert(input_iter_t beg_iter, input_iter_t end_iter, const std::string &amp;charset, output_iter_t output_iter, bool &amp;errflag);

void unicode::iconvert::fromu::convert(input_iter_t beg_iter, input_iter_t end_iter, const std::string &amp;charset, std::string &amp;out_buf, bool &amp;errflag);

std::pair&lt;std::string, bool&gt; unicode::iconvert::fromu::convert(const std::vector&lt;unicode_char&gt; &amp;text, const std::string &amp;charset);</code></pre>
<h2>Description</h2>
<dd>These template functions convert unicode characters to text in the given character set. <i>beg_iter</i> and <i>end_iter</i> define an input sequence of unicode_chars. They get converted to unicode characters. <i>output_iter</i> is an output iterator that <code>convert</code>() iterates over chars in the specified character set. <code>convert</code>() returns the value of the output iterator after iterating over the converted character sequence. <i>err_flag</i> gets set to true if unicode text could not be converted to the requested character set, or false for a successful conversion. </p>
<p> An overloaded <code>convert</code>() puts the text string into a std::string, instead of using an output iterator. Finally, a single std::vector&lt;unicode_char&gt; specifies the character string, instead of a beginning and an ending iterator.</p>
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
