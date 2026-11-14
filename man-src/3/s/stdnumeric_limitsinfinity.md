---
title: "stdnumeric_limitsinfinity(3)"
name: "stdnumeric_limitsinfinity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumeric_limitsinfinity/"
description: "std::numeric_limits<T>::infinity – std::numeric_limits<T>::infinity"
---

<p>std::numeric_limits&lt;T&gt;::infinity &#8211; std::numeric_limits&lt;T&gt;::infinity</p>
<h2>Synopsis</h2>
<pre><code>static T infinity() throw();             (until C++11)

static constexpr T infinity() noexcept;  (since C++11)</code></pre>
<p>Returns the special value &quot;positive infinity&quot;, as represented by the floating-point type T. Only meaningful if std::numeric_limits&lt;T&gt;::has_infinity == true. In IEEE 754, the most common binary representation of floating-point numbers, the positive infinity is the value with all bits of the exponent set and all bits of the fraction cleared. </p>
<h2>Return value</h2>
<p>T std::numeric_limits&lt;T&gt;::infinity()<br />
/* non-specialized */ T()<br />
bool false<br />
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
float HUGE_VALF<br />
double HUGE_VAL<br />
long double HUGE_VALL </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;limits&gt;

int main()

{
    double max = std::numeric_limits&lt;double&gt;::max();
    double inf = std::numeric_limits&lt;double&gt;::infinity();
    if (inf &gt; max)
        std::cout &lt;&lt; inf &lt;&lt; &quot; is greater than &quot; &lt;&lt; max &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;inf is greater than 1.79769e+308</p>
<h2>See also</h2>
<p>has_infinity identifies floating-point types that can represent the special value &quot;positive infinity&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
