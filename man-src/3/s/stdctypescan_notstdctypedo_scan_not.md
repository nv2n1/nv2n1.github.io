---
title: "stdctypescan_notstdctypedo_scan_not(3)"
name: "stdctypescan_notstdctypedo_scan_not"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypescan_notstdctypedo_scan_not/"
description: "std::ctype<CharT>::scan_not,std::ctype<CharT>::do_scan_not – std::ctype<CharT>::scan_not,std::ctype<CharT>::do_scan_not"
---

<p>std::ctype&lt;CharT&gt;::scan_not,std::ctype&lt;CharT&gt;::do_scan_not &#8211; std::ctype&lt;CharT&gt;::scan_not,std::ctype&lt;CharT&gt;::do_scan_not</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 const CharT *scan_not(mask m, const CharT *beg, const CharT *end) const;

protected:
(2)

    virtual const CharT *do_scan_not(mask m, const CharT *beg, const CharT *end) const;</code></pre>
<p>1) public member function, calls the protected virtual member function do_scan_not of the most derived class.<br />
2) Locates the first character in the character array [beg, end) that does not satisfy the classification mask m, that is, the first character c such that is(m, c) would return false. </p>
<h2>Parameters</h2>
<p>m &#8211; mask to search for<br />
beg &#8211; pointer to the first character in an array of characters to search<br />
end &#8211; one past the end pointer for the array of characters to search</p>
<h2>Return value</h2>
<p>Pointer to the first character in [beg, end) that doesn&#8217;t satisfy the mask, or end if no such character was found. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;locale&gt;

#include &lt;clocale&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    std::wcout.imbue(std::locale(&quot;en_US.utf8&quot;));
    auto &amp;f = std::use_facet&lt;std::ctype&lt;wchar_t&gt;&gt;(std::wcout.getloc());
    // skip leading whitespace
    wchar_t s1[] = L&quot;      		
  Кошка&quot;;
    const wchar_t *p1 = f.scan_not(std::ctype_base::space, std::begin(s1), std::end(s1));
    std::wcout &lt;&lt; &quot;'&quot; &lt;&lt; p1 &lt;&lt; &quot;'
&quot;;
    // skip leading digits
    wchar_t s2[] = L&quot;123456789ネプネプ&quot;;
    const wchar_t *p2 = f.scan_not(std::ctype_base::digit, std::begin(s2), std::end(s2));
    std::wcout &lt;&lt; &quot;'&quot; &lt;&lt; p2 &lt;&lt; &quot;'
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&#8216;Кошка&#8217;<br />
&nbsp;<wbr>&nbsp;&#8216;ネプネプ&#8217;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locates the first character in a sequence that fails given classification, using the classification table<br />
scan_not <i>(public member function of std::ctype&lt;char&gt;)</i><br />
do_scan_is locates the first character in a sequence that conforms to given classification<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
