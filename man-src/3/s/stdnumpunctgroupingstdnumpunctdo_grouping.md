---
title: "stdnumpunctgroupingstdnumpunctdo_grouping(3)"
name: "stdnumpunctgroupingstdnumpunctdo_grouping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunctgroupingstdnumpunctdo_grouping/"
description: "std::numpunct<CharT>::grouping,std::numpunct<CharT>::do_grouping – std::numpunct<CharT>::grouping,std::numpunct<CharT>::do_grouping"
---

<p>std::numpunct&lt;CharT&gt;::grouping,std::numpunct&lt;CharT&gt;::do_grouping &#8211; std::numpunct&lt;CharT&gt;::grouping,std::numpunct&lt;CharT&gt;::do_grouping</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 std::string grouping() const;

protected:
(2)

    virtual std::string do_grouping() const;</code></pre>
<p>1) Public member function, calls the member function do_grouping of the most derived class.<br />
2) Returns an std::string holding, in each char element, the number of digits in each group of the numeric output formatted by num_put::put() (and, therefore, basic_ostream::operator&lt;&lt;)<br />
The groups are stored as binary values: three-digit group is &#8216;\3&#8217;, and 51-digit group is &#8216;3&#8217;. The character at index zero of the returned string holds the number of digits in the rightmost group. The character at index 1 holds the number of digits in the second group from the right, etc. The grouping indicated by the last character in the returned string is reused to group all remaining digits in the (left part of) the number. </p>
<h2>Return value</h2>
<p>The object of type std::string holding the groups. The standard specializations of std::numpunct return an empty string, indicating no grouping. Typical groupings (e.g. the en_US locale) return &quot;&quot;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

#include &lt;locale&gt;
struct space_out : std::numpunct&lt;char&gt;

{
    char do_thousands_sep() const
    {
        return ' ';
    } // separate with spaces
    std::string do_grouping() const
    {
        return &quot;\1&quot;;
    } // groups of 1 digit
};
struct g123 : std::numpunct&lt;char&gt;

{
    std::string do_grouping() const
    {
        return &quot;\1\2\3&quot;;
    }
};
int main()

{
    std::cout &lt;&lt; &quot;default locale: &quot; &lt;&lt; 12345678 &lt;&lt; '
';
    std::cout.imbue(std::locale(std::cout.getloc(), new space_out));
    std::cout &lt;&lt; &quot;locale with modified numpunct: &quot; &lt;&lt; 12345678 &lt;&lt; '
';
    std::cout.imbue(std::locale(std::cout.getloc(), new g123));
    std::cout &lt;&lt; &quot;Locale with \1\2\3 grouping: &quot; &lt;&lt; std::numeric_limits&lt;unsigned long long&gt;::max() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;default locale: 12345678<br />
&nbsp;<wbr>&nbsp;locale with modified numpunct: 1 2 3 4 5 6 7 8<br />
&nbsp;<wbr>&nbsp;Locale with \1\2\3 grouping: 18,446,744,073,709,551,61,5</p>
<h2>See also</h2>
<p>do_thousands_sep provides the character to use as thousands separator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
