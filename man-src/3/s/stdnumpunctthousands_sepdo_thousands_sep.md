---
title: "stdnumpunctthousands_sepdo_thousands_sep(3)"
name: "stdnumpunctthousands_sepdo_thousands_sep"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunctthousands_sepdo_thousands_sep/"
description: "std::numpunct<CharT>::thousands_sep,do_thousands_sep – std::numpunct<CharT>::thousands_sep,do_thousands_sep"
---

<p>std::numpunct&lt;CharT&gt;::thousands_sep,do_thousands_sep &#8211; std::numpunct&lt;CharT&gt;::thousands_sep,do_thousands_sep</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 char_type thousands_sep() const;

protected:
(2)

    virtual char_type do_thousands_sep() const;</code></pre>
<p>1) Public member function, calls the member function do_thousands_sep of the most derived class.<br />
2) Returns the character to be used as the separator between digit groups when parsing or formatting integers and integral parts of floating-point values. </p>
<h2>Return value</h2>
<p>The object of type char_type to use as the thousands separator. The standard specializations of std::numpunct return &#8216;,&#8217; and L&#8217;,&#8217;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
struct space_out : std::numpunct&lt;char&gt; {
    char do_thousands_sep() const
    {
        return ' ';
    } // separate with spaces
    std::string do_grouping() const
    {
        return &quot;\1&quot;;
    } // groups of 1 digit
};
int main()

{
    std::cout &lt;&lt; &quot;default locale: &quot; &lt;&lt; 12345678 &lt;&lt; '
';
    std::cout.imbue(std::locale(std::cout.getloc(), new space_out));
    std::cout &lt;&lt; &quot;locale with modified numpunct: &quot; &lt;&lt; 12345678 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;default locale: 12345678<br />
&nbsp;<wbr>&nbsp;locale with modified numpunct: 1 2 3 4 5 6 7 8</p>
<h2>See also</h2>
<p>do_grouping provides the numbers of digits between each pair of thousands separators<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
