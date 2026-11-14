---
title: "unicodelinebreak_callback_save_buf(3)"
name: "unicodelinebreak_callback_save_buf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unicodelinebreak_callback_save_buf/"
description: "unicode::linebreak_callback_base, unicode::linebreak_callback_save_buf, unicode::linebreakc_callback_base, unicode::linebreak_iter, unicode::linebreakc_iter – unicode line-breaking rules"
---

<p>unicode::linebreak_callback_base, unicode::linebreak_callback_save_buf, unicode::linebreakc_callback_base, unicode::linebreak_iter, unicode::linebreakc_iter &#8211; unicode line-breaking rules</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;courier-unicode.h&gt;

class linebreak : public unicode::linebreak_callback_base
{

  public:
    using unicode::linebreak_callback_base::operator&lt;&lt;;
    using unicode::linebreak_callback_base::operator();
    int callback(int linebreak_code)
    {
        // ...
    }
};

unicode_char c;
std::vector&lt;unicode_char&gt; buf;

linebreak compute_linebreak;

compute_linebreak.set_opts(UNICODE_LB_OPT_SYBREAK);
compute_linebreak &lt;&lt; c;

compute_linebreak(buf);
compute_linebreak(buf.begin(), buf.end());

compute_linebreak.finish();

// ...

unicode::linebreak_callback_save_buf linebreaks;

std::list&lt;int&gt; lb = linebreaks.lb_buf;

class linebreakc : public unicode::linebreakc_callback_base
{

  public:
    using unicode::linebreak_callback_base::operator&lt;&lt;;
    using unicode::linebreak_callback_base::operator();
    int callback(int linebreak_code, unicode_char ch)
    {
        // ...
    }
};

// ...

std::vector&lt;unicode_char&gt; buf;

typedef unicode::linebreak_iter&lt;std::vector&lt;unicode_char&gt;::const_iterator&gt; iter_t;

iter_t beg_iter(buf.begin(), buf.end()), end_iter;

beg_iter.set_opts(UNICODE_LB_OPT_SYBREAK);

std::vector&lt;int&gt; linebreaks;

std::copy(beg_iter, end_iter, std::back_insert_iterator&lt;std::vector&lt;int&gt;&gt;(linebreaks));

// ...

typedef unicode::linebreakc_iter&lt;std::vector&lt;unicode_char&gt;::const_iterator&gt; iter_t;

iter_t beg_iter(buf.begin(), buf.end()), end_iter;

beg_iter.set_opts(UNICODE_LB_OPT_SYBREAK);

std::vector&lt;std::pair&lt;int, unicode_char&gt;&gt; linebreaks;

std::copy(beg_iter, end_iter, std::back_insert_iterator&lt;std::vector&lt;int&gt;&gt;(linebreaks));</code></pre>
<h2>Description</h2>
<p>unicode::linebreak_callback_base is a C++ binding for the unicode line-breaking rule implementation described in <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3). </p>
<p> Subclass unicode::linebreak_callback_base and implement callback() that&#8217;s virtually inherited from unicode::linebreak_callback_base. The callback() callback function receives the output values from the line-breaking algorithm, the UNICODE_LB_MANDATORY, UNICODE_LB_NONE, or the UNICODE_LB_ALLOWED value, for each unicode character. </p>
<p> callback() should return 0. A non-zero return reports an error, that stops the line-breaking algorithm. See <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3) for more information. </p>
<p> The alternate unicode::linebreakc_callback_base interface uses a virtually inherited callback() that receives two parameters, the line-break code value, and the corresponding unicode character. </p>
<p> The input unicode characters for the line-breaking algorithm are provided by the &lt;&lt; operator, one unicode character at a time; or by the () operator, passing either a container, or a beginning and an ending iterator value for an input sequence of unicode characters. finish() indicates the end of the unicode character sequence. </p>
<p> set_opts sets line-breaking options (see unicode_lb_set_opts() for more information). </p>
<p> unicode::linebreak_callback_save_buf is a subclass that implements callback() by saving the linebreaks codes into a std::list. </p>
<p> The linebreak_iter template implements an input iterator over ints. The template parameter is an input iterator over unicode chars. The constructor&#8217;s parameters are a beginning and an ending iterator value for a sequence of unicode_char. This constructs the beginning iterator value for a sequence of ints consisting of line-break values (UNICODE_LB_MANDATORY, UNICODE_LB_NONE, or UNICODE_LB_ALLOWED) corresponding to each unicode_char in the underlying sequence. The default constructor creates the ending iterator value for the sequence. </p>
<p> The iterator implements a set_opts() methods that sets the options for the line-breaking algorithm. </p>
<p> The linebreakc_iter template implements a similar input iterator, with the difference that it ends up iterating over a std::pair of line-breaking values and the corresponding unicode_char from the underlying input sequence.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-courier-unicode/">courier-unicode</a></code>(7), <code><a href="/docs/linux/man/3-unicode_line_break/">unicode_line_break</a></code>(3).</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
