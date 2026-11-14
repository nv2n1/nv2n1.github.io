---
title: "stdto_wstring(3)"
name: "stdto_wstring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdto_wstring/"
description: "std::to_wstring – std::to_wstring"
---

<p>std::to_wstring &#8211; std::to_wstring</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;string&gt;<br />
std::wstring to_wstring( int value ); <code>(1)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( long value ); <code>(2)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( long long value ); <code>(3)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( unsigned value ); <code>(4)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( unsigned long value ); <code>(5)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( unsigned long long value ); <code>(6)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( float value ); <code>(7)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( double value ); <code>(8)</code> <i>(since C++11)</i><br />
std::wstring to_wstring( long double value ); <code>(9)</code> <i>(since C++11)</i><br />
Converts a numeric value to std::wstring.<br />
1) Converts a signed decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%d&quot;, value) would produce for sufficiently large buf.<br />
2) Converts a signed decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%ld&quot;, value) would produce for sufficiently large buf..<br />
3) Converts a signed decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%lld&quot;, value) would produce for sufficiently large buf.<br />
4) Converts an unsigned decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%u&quot;, value) would produce for sufficiently large buf.<br />
5) Converts an unsigned decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%lu&quot;, value) would produce for sufficiently large buf.<br />
6) Converts an unsigned decimal integer to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%llu&quot;, value) would produce for sufficiently large buf.<br />
7,8) Converts a floating point value to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%f&quot;, value) would produce for sufficiently large buf.<br />
9) Converts a floating point value to a wide string with the same content as what std::swprintf(buf, sz, L&quot;%Lf&quot;, value) would produce for sufficiently large buf. </p>
<h2>Parameters</h2>
<p>value &#8211; a numeric value to convert</p>
<h2>Return value</h2>
<p>a wide string holding the converted value </p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc from the std::wstring constructor.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;
int main()
{
    double f = 23.43;

    std::wstring f_str = std::to_wstring(f);
    std::wcout &lt;&lt; f_str;
}</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;23.430000</p>
<h2>See also</h2>
<p>to_string converts an integral or floating point value to string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
