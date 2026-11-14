---
title: "stdnumeric_limitsmax_digits10(3)"
name: "stdnumeric_limitsmax_digits10"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsmax_digits10/"
description: "std::numeric_limits<T>::max_digits10 – std::numeric_limits<T>::max_digits10"
---

<p>std::numeric_limits&lt;T&gt;::max_digits10 &#8211; std::numeric_limits&lt;T&gt;::max_digits10</p>
<h2>Synopsis</h2>
<pre><code>static constexpr int max_digits10  (since C++11)</code></pre>
<p>The value of std::numeric_limits&lt;T&gt;::max_digits10 is the number of base-10 digits that are necessary to uniquely represent all distinct values of the type T, such as necessary for serialization/deserialization to text. This constant is meaningful for all floating-point types. </p>
<h2>Standard specializations</h2>
<p>T value of std::numeric_limits&lt;T&gt;::max_digits10<br />
/* non-specialized */ 0<br />
bool 0<br />
char 0<br />
signed char 0<br />
unsigned char 0<br />
wchar_t 0<br />
char8_t 0<br />
char16_t 0<br />
char32_t 0<br />
short 0<br />
unsigned short 0<br />
int 0<br />
unsigned int 0<br />
long 0<br />
unsigned long 0<br />
long long 0<br />
unsigned long long 0<br />
float FLT_DECIMAL_DIG or std::ceil(std::numeric_limits&lt;float&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code> + 1)<br />
double DBL_DECIMAL_DIG orstd::ceil(std::numeric_limits&lt;double&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code> + 1)<br />
long double DECIMAL_DIG or LDBL_DECIMAL_DIG orstd::ceil(std::numeric_limits&lt;long double&gt;::digits * <a href="/docs/linux/man/2-std--log10/">std::log10</a><code>(2)</code> + 1)</p>
<h2>Notes</h2>
<p>Unlike most mathematical operations, the conversion of a floating-point value to text and back is exact as long as at least max_digits10 were used (9 for float, 17 for double): it is guaranteed to produce the same floating-point value, even though the intermediate text representation is not exact. It may take over a hundred decimal digits to represent the precise value of a float in decimal notation. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;limits&gt;

#include &lt;sstream&gt;

#include &lt;iomanip&gt;

#include &lt;cmath&gt;

#include &lt;iostream&gt;
int main()

{
    float value = 10.0000086;
    constexpr auto digits10 = std::numeric_limits&lt;decltype(value)&gt;::digits10;
    constexpr auto max_digits10 = std::numeric_limits&lt;decltype(value)&gt;::max_digits10;
    constexpr auto submax_digits10 = max_digits10 - 1;
    std::cout
        &lt;&lt; &quot;float:
&quot;
        &lt;&lt; &quot;       digits10 is &quot; &lt;&lt; digits10 &lt;&lt; &quot; digits&quot; &lt;&lt; '
'
        &lt;&lt; &quot;   max_digits10 is &quot; &lt;&lt; max_digits10 &lt;&lt; &quot; digits&quot; &lt;&lt; '
'
        &lt;&lt; &quot;submax_digits10 is &quot; &lt;&lt; submax_digits10 &lt;&lt; &quot; digits&quot; &lt;&lt; '
'
        &lt;&lt; '
';
    const auto original_precision = std::cout.precision();
    for (auto i = 0; i &lt; 5; ++i) {
        std::cout
            &lt;&lt; &quot;   max_digits10: &quot; &lt;&lt; std::setprecision(max_digits10) &lt;&lt; value &lt;&lt; '
'
            &lt;&lt; &quot;submax_digits10: &quot; &lt;&lt; std::setprecision(submax_digits10) &lt;&lt; value &lt;&lt; '
'
            &lt;&lt; '
';
        value = std::nextafter(value, std::numeric_limits&lt;decltype(value)&gt;::max());
    }
    std::cout.precision(original_precision);
    return 0;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;float:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;digits10 is 6 digits<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10 is 9 digits<br />
&nbsp;<wbr>&nbsp;submax_digits10 is 8 digits </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10: 10.0000086<br />
&nbsp;<wbr>&nbsp;submax_digits10: 10.000009 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10: 10.0000095<br />
&nbsp;<wbr>&nbsp;submax_digits10: 10.00001 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10: 10.0000105<br />
&nbsp;<wbr>&nbsp;submax_digits10: 10.00001 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10: 10.0000114<br />
&nbsp;<wbr>&nbsp;submax_digits10: 10.000011 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_digits10: 10.0000124<br />
&nbsp;<wbr>&nbsp;submax_digits10: 10.000012</p>
<h2>See also</h2>
<p>radix the radix or integer base used by the representation of the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
digits number of radix digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
digits10 number of decimal digits that can be represented without change<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
min_exponent one more than the smallest negative power of the radix that is a valid normalized floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code><br />
max_exponent one more than the largest integer power of the radix that is a valid finite floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
