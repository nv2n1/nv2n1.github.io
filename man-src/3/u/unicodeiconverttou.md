---
title: "unicodeiconverttou(3)"
name: "unicodeiconverttou"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodeiconverttou/"
description: "unicode::iconvert::tou – template for converting text sequence to unicode"
---

<p>unicode::iconvert::tou &#8211; template for converting text sequence to unicode</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

output_iter_t convert(input_iter_t beg_iter, input_iter_t end_iter, const std::string &amp;charset, bool &amp;errflag, output_iter_t output_iter);

bool convert(input_iter_t beg_iter, input_iter_t end_iter, const std::string &amp;charset, std::vector&lt;unicode_char&gt; &amp;out_buf);

std::pair&lt;std::vector&lt;unicode_char&gt;, bool&gt; convert(const std::string &amp;text, const std::string &amp;charset);</code></pre>
<h2>Description</h2>
<dd>These template functions convert text in a given character set to unicode characters. <i>beg_iter</i> and <i>end_iter</i> define an input sequence of chars in the <i>charset</i> character set. They get converted to unicode characters. <i>output_iter</i> is an output iterator that <code>convert</code>() iterates over unicode_chars. <code>convert</code>() returns the value of the output iterator after iterating over the converted character sequence. <i>errflag</i>, passed by reference, gets set to true if some character could not be converted to unicode, from the specified character set, and false if the conversion completed without errors. </p>
<p> An overloaded <code>convert</code>() puts the unicode character sequence into a vector of unicode_chars, instead of an output sequence, and returned the error flag. Finally, a single std::string specifies the character string, instead of a beginning and an ending iterator, and returns a std::pair with the converted unicode text in a vector, and the error flag.</p>
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
