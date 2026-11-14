---
title: "stddivstdldivstdlldiv(3)"
name: "stddivstdldivstdlldiv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddivstdldivstdlldiv/"
description: "std::div,std::ldiv,std::lldiv – std::div,std::ldiv,std::lldiv"
---

<p>std::div,std::ldiv,std::lldiv &#8211; std::div,std::ldiv,std::lldiv</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstdlib&gt;<br />
std::div_t div( int x, int y ); <code>(1)</code><br />
std::ldiv_t div( long x, long y ); <code>(2)</code><br />
std::lldiv_t div( long long x, long long y ); <code>(3)</code> <i>(since C++11)</i><br />
std::ldiv_t ldiv( long x, long y ); <code>(4)</code><br />
std::lldiv_t lldiv( long long x, long long y ); <code>(5)</code> <i>(since C++11)</i><br />
Defined in header &lt;cinttypes&gt;<br />
std::imaxdiv_t div( std::intmax_t x, std::intmax_t y ); <code>(6)</code> <i>(since C++11)</i><br />
std::imaxdiv_t imaxdiv( std::intmax_t x, std::intmax_t y ); <code>(7)</code> <i>(since C++11)</i><br />
Computes both the quotient and the remainder of the division of the numerator x by the denominator y<br />
The quotient is the algebraic quotient with any fractional part discarded (truncated towards zero). The remainder is such that quot * y + rem == x. <i>(until C++11)</i><br />
The quotient is the result of the expression x/y. The remainder is the result of the expression x%y. <i>(since C++11)</i> </p>
<h2>Parameters</h2>
<p>x, y &#8211; integer values</p>
<h2>Return value</h2>
<p>If both the remainder and the quotient can be represented as objects of the corresponding type (int, long, long long, std::imaxdiv_t, respectively), returns both as an object of type std::div_t, std::ldiv_t, std::lldiv_t, std::imaxdiv_t defined as follows:<br />
&nbsp;std::div_t<br />
or<br />
&nbsp;std::ldiv_t<br />
or<br />
&nbsp;std::lldiv_t<br />
or<br />
&nbsp;std::imaxdiv_t<br />
or<br />
If either the remainder or the quotient cannot be represented, the behavior is undefined. </p>
<h2>Notes</h2>
<p>Until C++11, the rounding direction of the quotient and the sign of the remainder in the built-in_division_and_remainder_operators was implementation-defined if either of the operands was negative, but it was well-defined in std::div.<br />
On many platforms, a single CPU instruction obtains both the quotient and the remainder, and this function may leverage that, although compilers are generally able to merge nearby / and % where suitable. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;string&gt;

#include &lt;cmath&gt;

#include &lt;cstdlib&gt;

#include &lt;iostream&gt;
std::string itoa(int n, int base)

{
    std::string buf;
    std::div_t dv{};
    dv.quot = n;
    do {
        dv = std::div(dv.quot, base);
        buf += &quot;0123456789abcdef&quot;[std::abs(dv.rem)]; // string literals are arrays
    } while (dv.quot);
    if (n &lt; 0)
        buf += '-';
    return {buf.rbegin(), buf.rend()};
}
int main()

{
    std::cout &lt;&lt; itoa(12345, 10) &lt;&lt; '
'
              &lt;&lt; itoa(-12345, 10) &lt;&lt; '
'
              &lt;&lt; itoa(65535, 16) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;12345<br />
&nbsp;<wbr>&nbsp;-12345<br />
&nbsp;<wbr>&nbsp;ffff</p>
<h2>See also</h2>
<p>fmod<br />
fmodf<br />
fmodl remainder of the floating point division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
remainder<br />
remainderf<br />
remainderl signed remainder of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
remquo<br />
remquof<br />
remquol signed remainder as well as the three last bits of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
