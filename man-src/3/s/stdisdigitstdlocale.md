---
title: "stdisdigitstdlocale(3)"
name: "stdisdigitstdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisdigitstdlocale/"
---

std::isdigit(std::locale) - std::isdigit(std::locale)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class charT&gt;

    bool isdigit(charT ch, const locale &amp;loc);</code></pre> 
Checks if the given character is classified as a digit by the given locale's std::ctype facet. 

<h2>Parameters</h2>

ch - character 
loc - locale

<h2>Return value</h2>

Returns true if the character is classified as a digit, false otherwise. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class charT &gt; 
&nbsp;<wbr>&nbsp;bool isdigit( charT ch, const std::locale&amp; loc ) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::use_facet&lt;std::ctype&lt;charT&gt;&gt;(loc).is(std::ctype_base::digit, ch); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

#include &lt;string&gt;

#include &lt;set&gt;
struct jdigit_ctype : std::ctype&lt;wchar_t&gt;

{
    std::set&lt;wchar_t&gt; jdigits{L'一', L'二', L'三', L'四', L'五', L'六', L'七', L'八', L'九', L'十'};
    bool do_is(mask m, char_type c) const
    {
        if ((m &amp; digit) &amp;&amp; jdigits.count(c))
            return true;           // Japanese digits will be classified as digits
        return ctype::do_is(m, c); // leave the rest to the parent class
    }
};
int main()

{
    std::wstring text = L&quot;123一二三１２３&quot;;
    std::locale loc(std::locale(&quot;&quot;), new jdigit_ctype);
    std::locale::global(std::locale(&quot;&quot;));
    std::wcout.imbue(std::locale());
    for (wchar_t c : text)
        if (std::isdigit(c, loc))
            std::wcout &lt;&lt; c &lt;&lt; &quot; is a digit\n&quot;;
        else
            std::wcout &lt;&lt; c &lt;&lt; &quot; is NOT a digit\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 is a digit 
&nbsp;<wbr>&nbsp;2 is a digit 
&nbsp;<wbr>&nbsp;3 is a digit 
&nbsp;<wbr>&nbsp;一 is a digit 
&nbsp;<wbr>&nbsp;二 is a digit 
&nbsp;<wbr>&nbsp;三 is a digit 
&nbsp;<wbr>&nbsp;１ is NOT a digit 
&nbsp;<wbr>&nbsp;２ is NOT a digit 
&nbsp;<wbr>&nbsp;３ is NOT a digit

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a character is a digit 
isdigit <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a wide character is a digit 
iswdigit <i>(function)</i> 
