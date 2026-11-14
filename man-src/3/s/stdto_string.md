---
title: "stdto_string(3)"
name: "stdto_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdto_string/"
description: "std::to_string – std::to_string"
---

<p>std::to_string &#8211; std::to_string</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;string&gt;<br />
std::string to_string( int value ); <code>(1)</code> <i>(since C++11)</i><br />
std::string to_string( long value ); <code>(2)</code> <i>(since C++11)</i><br />
std::string to_string( long long value ); <code>(3)</code> <i>(since C++11)</i><br />
std::string to_string( unsigned value ); <code>(4)</code> <i>(since C++11)</i><br />
std::string to_string( unsigned long value ); <code>(5)</code> <i>(since C++11)</i><br />
std::string to_string( unsigned long long value ); <code>(6)</code> <i>(since C++11)</i><br />
std::string to_string( float value ); <code>(7)</code> <i>(since C++11)</i><br />
std::string to_string( double value ); <code>(8)</code> <i>(since C++11)</i><br />
std::string to_string( long double value ); <code>(9)</code> <i>(since C++11)</i><br />
Converts a numeric value to std::string.<br />
1) Converts a signed decimal integer to a string with the same content as what std::sprintf(buf, &quot;%d&quot;, value) would produce for sufficiently large buf.<br />
2) Converts a signed decimal integer to a string with the same content as what std::sprintf(buf, &quot;%ld&quot;, value) would produce for sufficiently large buf.<br />
3) Converts a signed decimal integer to a string with the same content as what std::sprintf(buf, &quot;%lld&quot;, value) would produce for sufficiently large buf.<br />
4) Converts an unsigned decimal integer to a string with the same content as what std::sprintf(buf, &quot;%u&quot;, value) would produce for sufficiently large buf.<br />
5) Converts an unsigned decimal integer to a string with the same content as what std::sprintf(buf, &quot;%lu&quot;, value) would produce for sufficiently large buf.<br />
6) Converts an unsigned decimal integer to a string with the same content as what std::sprintf(buf, &quot;%llu&quot;, value) would produce for sufficiently large buf.<br />
7,8) Converts a floating point value to a string with the same content as what std::sprintf(buf, &quot;%f&quot;, value) would produce for sufficiently large buf.<br />
9) Converts a floating point value to a string with the same content as what std::sprintf(buf, &quot;%Lf&quot;, value) would produce for sufficiently large buf. </p>
<h2>Parameters</h2>
<p>value &#8211; a numeric value to convert</p>
<h2>Return value</h2>
<p>a string holding the converted value </p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc from the std::string constructor.</p>
<h2>Notes</h2>
<p>* With floating point types std::to_string may yield unexpected results as the number of significant digits in the returned string can be zero, see the example.<br />
* The return value may differ significantly from what std::cout prints by default, see the example.<br />
* std::to_string relies on the current locale for formatting purposes, and therefore concurrent calls to std::to_string from multiple threads may result in partial serialization of calls. C++17 provides std::to_chars as a higher-performance locale-independent alternative. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    double f = 23.43;
    double f2 = 1e-9;
    double f3 = 1e40;
    double f4 = 1e-40;
    double f5 = 123456789;
    std::string f_str = std::to_string(f);
    std::string f_str2 = std::to_string(f2); // Note: returns &quot;0.000000&quot;
    std::string f_str3 = std::to_string(f3); // Note: Does not return &quot;1e+40&quot;.
    std::string f_str4 = std::to_string(f4); // Note: returns &quot;0.000000&quot;
    std::string f_str5 = std::to_string(f5);
    std::cout &lt;&lt; &quot;std::cout: &quot; &lt;&lt; f &lt;&lt; '
'
              &lt;&lt; &quot;to_string: &quot; &lt;&lt; f_str &lt;&lt; &quot;

&quot;
              &lt;&lt; &quot;std::cout: &quot; &lt;&lt; f2 &lt;&lt; '
'
              &lt;&lt; &quot;to_string: &quot; &lt;&lt; f_str2 &lt;&lt; &quot;

&quot;
              &lt;&lt; &quot;std::cout: &quot; &lt;&lt; f3 &lt;&lt; '
'
              &lt;&lt; &quot;to_string: &quot; &lt;&lt; f_str3 &lt;&lt; &quot;

&quot;
              &lt;&lt; &quot;std::cout: &quot; &lt;&lt; f4 &lt;&lt; '
'
              &lt;&lt; &quot;to_string: &quot; &lt;&lt; f_str4 &lt;&lt; &quot;

&quot;
              &lt;&lt; &quot;std::cout: &quot; &lt;&lt; f5 &lt;&lt; '
'
              &lt;&lt; &quot;to_string: &quot; &lt;&lt; f_str5 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::cout: 23.43<br />
&nbsp;<wbr>&nbsp;to_string: 23.430000 </p>
<p>&nbsp;<wbr>&nbsp;std::cout: 1e-09<br />
&nbsp;<wbr>&nbsp;to_string: 0.000000 </p>
<p>&nbsp;<wbr>&nbsp;std::cout: 1e+40<br />
&nbsp;<wbr>&nbsp;to_string: 10000000000000000303786028427003666890752.000000 </p>
<p>&nbsp;<wbr>&nbsp;std::cout: 1e-40<br />
&nbsp;<wbr>&nbsp;to_string: 0.000000 </p>
<p>&nbsp;<wbr>&nbsp;std::cout: 1.23457e+08<br />
&nbsp;<wbr>&nbsp;to_string: 123456789.000000</p>
<h2>See also</h2>
<p>to_wstring converts an integral or floating point value to wstring<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
stoul<br />
stoull converts a string to an unsigned integer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
stoi<br />
stol<br />
stoll converts a string to a signed integer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
stof<br />
stod<br />
stold converts a string to a floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
to_chars converts an integer or floating-point value to a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
