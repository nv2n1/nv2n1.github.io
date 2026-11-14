---
title: "stdfixedstdscientificstdhexfloatstddefaultfloat(3)"
name: "stdfixedstdscientificstdhexfloatstddefaultfloat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfixedstdscientificstdhexfloatstddefaultfloat/"
description: "std::fixed,std::scientific,std::hexfloat,std::defaultfloat – std::fixed,std::scientific,std::hexfloat,std::defaultfloat"
---

<p>std::fixed,std::scientific,std::hexfloat,std::defaultfloat &#8211; std::fixed,std::scientific,std::hexfloat,std::defaultfloat</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; fixed( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; scientific( std::ios_base&amp; str ); <code>(2)</code><br />
std::ios_base&amp; hexfloat( std::ios_base&amp; str ); <code>(3)</code> <i>(since C++11)</i><br />
std::ios_base&amp; defaultfloat( std::ios_base&amp; str ); <code>(4)</code> <i>(since C++11)</i><br />
Modifies the default formatting for floating-point input/output.<br />
1) Sets the floatfield of the stream str to fixed as if by calling str.setf(std::ios_base::fixed, std::ios_base::floatfield)<br />
2) Sets the floatfield of the stream str to scientific as if by calling str.setf(std::ios_base::scientific, std::ios_base::floatfield)<br />
3) Sets the floatfield of the stream str to fixed and scientific simultaneously as if by calling str.setf(std::ios_base::fixed | std::ios_base::scientific, std::ios_base::floatfield). This enables hexadecimal floating-point formatting.<br />
4) Sets the floatfield of the stream str to zero, as if by calling str.unsetf(std::ios_base::floatfield). This enables the default floating-point formatting, which is different from fixed and scientific.<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::fixed for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::scientific for any in of type std::basic_istream. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Notes</h2>
<p>Hexadecimal floating-point formatting ignores the stream precision specification, as required by the specification of std::num_put::do_put. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;
int main()

{
    std::cout &lt;&lt; &quot;The number 0.01 in fixed:      &quot; &lt;&lt; std::fixed &lt;&lt; 0.01 &lt;&lt; '
'
              &lt;&lt; &quot;The number 0.01 in scientific: &quot; &lt;&lt; std::scientific &lt;&lt; 0.01 &lt;&lt; '
'
              &lt;&lt; &quot;The number 0.01 in hexfloat:   &quot; &lt;&lt; std::hexfloat &lt;&lt; 0.01 &lt;&lt; '
'
              &lt;&lt; &quot;The number 0.01 in default:    &quot; &lt;&lt; std::defaultfloat &lt;&lt; 0.01 &lt;&lt; '
';
    double f;
    std::istringstream(&quot;0x1P-1022&quot;) &gt;&gt; std::hexfloat &gt;&gt; f;
    std::cout &lt;&lt; &quot;Parsing 0x1P-1022 as hex gives &quot; &lt;&lt; f &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The number 0.01 in fixed: 0.010000<br />
&nbsp;<wbr>&nbsp;The number 0.01 in scientific: 1.000000e-02<br />
&nbsp;<wbr>&nbsp;The number 0.01 in hexfloat: 0x1.47ae147ae147bp-7<br />
&nbsp;<wbr>&nbsp;The number 0.01 in default: 0.01<br />
&nbsp;<wbr>&nbsp;Parsing 0x1P-1022 as hex gives 2.22507e-308</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes floating-point precision<br />
setprecision <i>(function)</i> </p>
