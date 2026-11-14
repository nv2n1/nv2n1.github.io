---
title: "stdnumeric_limitsround_style(3)"
name: "stdnumeric_limitsround_style"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsround_style/"
---

std::numeric_limits&lt;T&gt;::round_style - std::numeric_limits&lt;T&gt;::round_style

<h2>Synopsis</h2>

<pre><code>static const std::float_round_style round_style;
(until C++ 11)

    static constexpr std::float_round_style round_style;
(since C++ 11)</code></pre> 
The value of std::numeric_limits&lt;T&gt;::round_style identifies the rounding style used by the floating-point type T whenever a value that is not one of the exactly repesentable values of T is stored in an object of that type. 

<h2>Standard specializations</h2>

T value of std::numeric_limits&lt;T&gt;::round_style 
/* non-specialized */ std::round_toward_zero 
bool std::round_toward_zero 
char std::round_toward_zero 
signed char std::round_toward_zero 
unsigned char std::round_toward_zero 
wchar_t std::round_toward_zero 
char8_t std::round_toward_zero 
char16_t std::round_toward_zero 
char32_t std::round_toward_zero 
short std::round_toward_zero 
unsigned short std::round_toward_zero 
int std::round_toward_zero 
unsigned int std::round_toward_zero 
long std::round_toward_zero 
unsigned long std::round_toward_zero 
long long std::round_toward_zero 
unsigned long long std::round_toward_zero 
float usually std::round_to_nearest 
double usually std::round_to_nearest 
long double usually std::round_to_nearest

<h2>Notes</h2>

These values are constants, and do not reflect the changes to the rounding made by std::fesetround. The changed values may be obtained from FLT_ROUNDS or std::fegetround. 

<h2>Example</h2>

The decimal value 0.1 cannot be represented by a binary floating-point type. When stored in an IEEE-745 double, it falls between 0x1.9999999999999*2-4 
and 0x1.999999999999a*2-4 
. Rounding to nearest representable value results in 0x1.999999999999a*2-4 
. 
Similarly, the decimal value 0.3, which is between 0x1.3333333333333*2-2 
and 0x1.3333333333334*2-2 
is rounded to nearest and is stored as 0x1.3333333333333*2-2 
. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

int main()

{
    std::cout &lt;&lt; std::hexfloat &lt;&lt; &quot;The decimal 0.1 is stored in a double as &quot;
              &lt;&lt; 0.1 &lt;&lt; '\n'
              &lt;&lt; &quot;The decimal 0.3 is stored in a double as &quot;
              &lt;&lt; 0.3 &lt;&lt; '\n'
              &lt;&lt; &quot;The rounding style is &quot; &lt;&lt; std::numeric_limits&lt;double&gt;::round_style &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The decimal 0.1 is stored in a double as 0x1.999999999999ap-4 
&nbsp;<wbr>&nbsp;The decimal 0.3 is stored in a double as 0x1.3333333333333p-2 
&nbsp;<wbr>&nbsp;The rounding style is 1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates floating-point rounding modes 
float_round_style <i>(enum)</i> 
