---
title: "stdctypescan_is(3)"
name: "stdctypescan_is"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypescan_is/"
description: "std::ctype<char>::scan_is – std::ctype<char>::scan_is"
---

<p>std::ctype&lt;char&gt;::scan_is &#8211; std::ctype&lt;char&gt;::scan_is</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
const char* scan_is (mask m, const char* beg, const char* end) const; <code>(1)</code> </p>
<pre><code>Locates the first character in the character array [beg, end) that satisfies the classification mask m, that is, the first character c such that table()[(unsigned char) c] &amp; m would return true.

If (unsigned char)c &gt;= std::ctype&lt;char&gt;::table_size, then an implementation-defined value is substituted instead of table()[(unsigned char)c], possibly different for different values of c.
</code></pre>
<h2>Parameters</h2>
<p>m &#8211; mask to search for<br />
beg &#8211; pointer to the first character in an array of characters to search<br />
end &#8211; one past the end pointer for the array of characters to search</p>
<h2>Return value</h2>
<p>Pointer to the first character in [beg, end) that satisfies the mask, or end if no such character was found. </p>
<h2>Notes</h2>
<p>Unlike the primary template std::ctype, this specialization does not perform a virtual function call when classifying characters. To customize the behavior, a derived class may provide a non-default classification table to the base class constructor. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;
int main()

{
    std::locale loc(&quot;&quot;);
    auto &amp;f = std::use_facet&lt;std::ctype&lt;char&gt;&gt;(loc);
    // skip until the first letter
    char s1[] = &quot;      		
  Test&quot;;
    const char *p1 = f.scan_is(std::ctype_base::alpha, std::begin(s1), std::end(s1));
    std::cout &lt;&lt; &quot;'&quot; &lt;&lt; p1 &lt;&lt; &quot;'
&quot;;
    // skip until the first letter
    char s2[] = &quot;123456789abcd&quot;;
    const char *p2 = f.scan_is(std::ctype_base::alpha, std::begin(s2), std::end(s2));
    std::cout &lt;&lt; &quot;'&quot; &lt;&lt; p2 &lt;&lt; &quot;'
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&#8216;Test&#8217;<br />
&nbsp;<wbr>&nbsp;&#8216;abcd&#8217;</p>
<h2>See also</h2>
<p>do_scan_is locates the first character in a sequence that conforms to given classification<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::ctype&lt;CharT&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locates the first character in a sequence that fails given classification, using the classification table<br />
scan_not <i>(public member function)</i> </p>
