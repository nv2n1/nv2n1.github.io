---
title: "stdnumeric_limitsepsilon(3)"
name: "stdnumeric_limitsepsilon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsepsilon/"
---

std::numeric_limits&lt;T&gt;::epsilon - std::numeric_limits&lt;T&gt;::epsilon

<h2>Synopsis</h2>

<pre><code>static T epsilon() throw();             (until C++11)

static constexpr T epsilon() noexcept;  (since C++11)</code></pre> 
Returns the machine epsilon, that is, the difference between 1.0 and the next value representable by the floating-point type T. It is only meaningful if std::numeric_limits&lt;T&gt;::is_integer == false. 

<h2>Return value</h2>

T std::numeric_limits&lt;T&gt;::epsilon() 
/* non-specialized */ T() 
bool false 
char 0 
signed char 0 
unsigned char 0 
wchar_t 0 
char8_t 0 
char16_t 0 
char32_t 0 
short 0 
unsigned short 0 
int 0 
unsigned int 0 
long 0 
unsigned long 0 
long long 0 
unsigned long long 0 
float FLT_EPSILON 
double DBL_EPSILON 
long double LDBL_EPSILON 

<h2>Example</h2>

Demonstrates the use of machine epsilon to compare floating-point values for equality 
 // Run this code <pre><code>#include &lt;cmath&gt;

#include &lt;limits&gt;

#include &lt;iomanip&gt;

#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;algorithm&gt;
template &lt;class T&gt;

typename std::enable_if&lt;!std::numeric_limits&lt;T&gt;::is_integer, bool&gt;::type
almost_equal(T x, T y, int ulp)

{
    // the machine epsilon has to be scaled to the magnitude of the values used
    // and multiplied by the desired precision in ULPs (units in the last place)
    return std::abs(x - y) &lt;= std::numeric_limits&lt;T&gt;::epsilon() * std::abs(x + y) * ulp
           // unless the result is subnormal
           || std::abs(x - y) &lt; std::numeric_limits&lt;T&gt;::min();
}
int main()

{
    double d1 = 0.2;
    double d2 = 1 / std::sqrt(5) / std::sqrt(5);
    std::cout &lt;&lt; std::fixed &lt;&lt; std::setprecision(20)
              &lt;&lt; &quot;d1=&quot; &lt;&lt; d1 &lt;&lt; &quot;\nd2=&quot; &lt;&lt; d2 &lt;&lt; '\n';
    if (d1 == d2)
        std::cout &lt;&lt; &quot;d1 == d2\n&quot;;
    else
        std::cout &lt;&lt; &quot;d1 != d2\n&quot;;
    if (almost_equal(d1, d2, 2))
        std::cout &lt;&lt; &quot;d1 almost equals d2\n&quot;;
    else
        std::cout &lt;&lt; &quot;d1 does not almost equal d2\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;d1=0.20000000000000001110 
&nbsp;<wbr>&nbsp;d2=0.19999999999999998335 
&nbsp;<wbr>&nbsp;d1 != d2 
&nbsp;<wbr>&nbsp;d1 almost equals d2

<h2>See also</h2>

nextafter 
nextafterf 
nextafterl 
nexttoward 
nexttowardf 
nexttowardl next representable floating point value towards the given value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
