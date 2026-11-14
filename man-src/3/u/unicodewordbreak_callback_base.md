---
title: "unicodewordbreak_callback_base(3)"
name: "unicodewordbreak_callback_base"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodewordbreak_callback_base/"
description: "unicode::wordbreak_callback_base, unicode::wordbreak_callback_base – unicode word-breaking rules"
---

<p>unicode::wordbreak_callback_base, unicode::wordbreak_callback_base &#8211; unicode word-breaking rules</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

class wordbreak : public unicode::wordbreak_callback_base
{

  public:
    using unicode::wordbreak_callback_base::operator&lt;&lt;;
    using unicode::wordbreak_callback_base::operator();
    int callback(bool flag)
    {
        // ...
    }
};

unicode_char c;
std::vector&lt;unicode_char&gt; buf;

wordbreak compute_wordbreak;

compute_wordbreak &lt;&lt; c;

compute_wordbreak(buf);
compute_wordbreak(buf.begin(), buf.end());

compute_wordbreak.finish();

// ...

unicode_wordbreakscan scan;

scan &lt;&lt; c;

size_t nchars = scan.finish();</code></pre>
<h2>Description</h2>
<p>unicode::wordbreak_callback_base is a C++ binding for the unicode word-breaking rule implementation described in <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3). </p>
<p> Subclass unicode::wordbreak_callback_base and implement callback() that&#8217;s virtually inherited from unicode::wordbreak_callback_base. The callback() callback function receives the output values from the word-breaking algorithm, namely a bool indicating whether a word break exists before the unicode character in the underlying input sequence. </p>
<p> callback() should return 0. A non-zero return reports an error, that stops the word-breaking algorithm. See <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3) for more information. </p>
<p> The input unicode characters for the word-breaking algorithm are provided by the &lt;&lt; operator, one unicode character at a time; or by the () operator, passing either a container, or a beginning and an ending iterator value for an input sequence of unicode characters. finish() indicates the end of the unicode character sequence. </p>
<p> unicode::wordbreakscan is a C++ binding for the <code>unicode_wbscan_init</code>(), <code>unicode_wbscan_next</code>() and <code>unicode_wbscan_end</code> methods described in <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3). Its &lt;&lt; iterates over the unicode characters, and finish() indicates the number of characters before the first unicode word break. The &lt;&lt; iterator returns a bool indicating when the first word break has already been found, so further calls are not necessary.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_word_break/">unicode_word_break</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
