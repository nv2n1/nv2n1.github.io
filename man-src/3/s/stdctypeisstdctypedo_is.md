---
title: "stdctypeisstdctypedo_is(3)"
name: "stdctypeisstdctypedo_is"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypeisstdctypedo_is/"
---

std::ctype&lt;CharT&gt;::is,std::ctype&lt;CharT&gt;::do_is - std::ctype&lt;CharT&gt;::is,std::ctype&lt;CharT&gt;::do_is

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 bool is(mask m, CharT c) const;

public:
(2)

    const CharT *is(const CharT *low, const CharT *high, mask *vec) const;

protected:
(3)

    virtual bool do_is(mask m, CharT c) const;

protected:
(4)

    virtual const CharT *do_is(const CharT *low, const CharT *high, mask *vec) const;</code></pre> 
1,2) public member function, calls the protected virtual member function do_is of the most derived class. 
3) Checks if the character c is classified by the mask m 
4) For every character in the character array [low, high), identifies the complete classification mask (e.g. digit|xdigit|alnum|print|graph for the digit '0' in the default locale), and stores the masks in the corresponding elements of the array pointed to by vec 

<h2>Parameters</h2>

c - character to classify 
m - mask to use for classifying a single character 
low - pointer to the first character in an array of characters to classify 
high - one past the end pointer for the array of characters to classify 
vec - pointer to the first element of the array of masks to fill

<h2>Return value</h2>

1,3) true if c is classified by m 
2,4) high 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;utility&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
// utility wrapper to make locale-bound facets destructible

template &lt;class Facet&gt;

struct deletable_facet : Facet

{
    template &lt;class... Args&gt;
    deletable_facet(Args &amp;&amp;...args)
        : Facet(std::forward&lt;Args&gt;(args)...)
    {
    }
    ~deletable_facet()
    {
    }
};
int main()

{
    // classify a single character using the default locale
    auto &amp;f = std::use_facet&lt;std::ctype&lt;char&gt;&gt;(std::locale());
    char c = '0';
    if (f.is(std::ctype_base::digit, c)) // or isdigit(c, locale());
    {
        std::cout &lt;&lt; &quot;'&quot; &lt;&lt; c &lt;&lt; &quot;' is a digit\n&quot;;
    }
    // classify every character in a string using a named locale
    deletable_facet&lt;std::ctype_byname&lt;wchar_t&gt;&gt; f2(&quot;en_US.utf8&quot;);
    std::wstring str = L&quot;z\u00df\u6c34\U0001d10b&quot;;
    std::vector&lt;std::ctype_base::mask&gt; vec(str.size());
    f2.is(&amp;str[0], &amp;str[0] + str.size(), &amp;vec[0]);
    for (std::size_t n = 0; n &lt; str.size(); ++n) {
        std::cout &lt;&lt; std::hex &lt;&lt; &quot;U+&quot; &lt;&lt; str[n] &lt;&lt; &quot; is: &quot;;
        if (vec[n] &amp; std::ctype_base::alnum)
            std::cout &lt;&lt; &quot; alnum &quot;;
        if (vec[n] &amp; std::ctype_base::punct)
            std::cout &lt;&lt; &quot; punct &quot;;
        std::cout &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;'0' is a digit 
&nbsp;<wbr>&nbsp;U+7a is: alnum 
&nbsp;<wbr>&nbsp;U+df is: alnum 
&nbsp;<wbr>&nbsp;U+6c34 is: alnum 
&nbsp;<wbr>&nbsp;U+1d10b is: punct

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classifies a character or a character sequence, using the classification table 
is <i>(public member function of std::ctype&lt;char&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classifies a wide character according to the specified LC_CTYPE category 
iswctype <i>(function)</i> 
