---
title: "stdclamp(3)"
name: "stdclamp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdclamp/"
description: "std::clamp – std::clamp"
---

<p>std::clamp &#8211; std::clamp</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class T&gt;
    (1)(since C++ 17)

        constexpr const T &amp;clamp(const T &amp;v, const T &amp;lo, const T &amp;hi);

template &lt;class T, class Compare&gt;
(2)(since C++ 17)

    constexpr const T &amp;clamp(const T &amp;v, const T &amp;lo, const T &amp;hi, Compare comp);</code></pre>
<p>1) If v compares less than lo, returns lo; otherwise if hi compares less than v, returns hi; otherwise returns v. Uses operator&lt; to compare the values.<br />
2) Same as <code>(1)</code>, but uses comp to compare the values.<br />
The behavior is undefined if the value of lo is greater than hi </p>
<h2>Parameters</h2>
<p>v &#8211; the value to clamp<br />
lo,hi &#8211; the boundaries to clamp v to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b);<br />
comp &#8211; While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type T can be implicitly converted to both of them.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
T must meet the requirements of LessThanComparable in order to use overloads <code>(1)</code>.</p>
<h2>Return value</h2>
<p>Reference to lo if v is less than lo, reference to hi if hi is less than v, otherwise reference to v. </p>
<h2>Complexity</h2>
<p>At most two comparisons.</p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;constexpr const T&amp; clamp( const T&amp; v, const T&amp; lo, const T&amp; hi )<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return clamp( v, lo, hi, std::less&lt;&gt;() );<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Second version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, class Compare&gt;<br />
&nbsp;<wbr>&nbsp;constexpr const T&amp; clamp( const T&amp; v, const T&amp; lo, const T&amp; hi, Compare comp )<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return assert( !comp(hi, lo) ),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comp(v, lo) ? lo : comp(hi, v) ? hi : v;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Notes</h2>
<p>Capturing the result of std::clamp by reference if one of the parameters is rvalue produces a dangling reference if that parameter is returned: int n = -1;</p>
<p>const int &amp;r = std::clamp(n, 0, 255);</p>
<p>// r is dangling<br />
If v compares equivalent to either bound, returns a reference to v, not the bound.<br />
Only works for floating-point T if NaNs are avoided. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cstdint&gt;

#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;random&gt;
int main()

{
    std::mt19937 g(std::random_device{}());
    std::uniform_int_distribution&lt;&gt; d(-300, 300);
    std::cout &lt;&lt; &quot; raw   clamped to int8_t   clamped to uint8_t
&quot;;
    for (int n = 0; n &lt; 5; ++n) {
        int v = d(g);
        std::cout &lt;&lt; std::setw(4) &lt;&lt; v
                  &lt;&lt; std::setw(20) &lt;&lt; std::clamp(v, INT8_MIN, INT8_MAX)
                  &lt;&lt; std::setw(21) &lt;&lt; std::clamp(v, 0, UINT8_MAX) &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;.raw clamped to int8_t clamped to uint8_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;168 127 168<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;128 127 128<br />
&nbsp;<wbr>&nbsp;-137 -128 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;40 40 40<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;-66 -66 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the smaller of the given values<br />
min <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the greater of the given values<br />
max <i>(function template)</i> </p>
