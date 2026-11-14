---
title: "stdratio_divide(3)"
name: "stdratio_divide"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdratio_divide/"
---

std::ratio_divide - std::ratio_divide

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ratio&gt;

template&lt; class R1, class R2 &gt;         (since C++11)

using ratio_divide = /* see below */;</code></pre> 
The alias template std::ratio_divide denotes the result of dividing two exact rational fractions represented by the std::ratio specializations R1 and R2. 
The result is a std::ratio specialization std::ratio&lt;U, V&gt;, such that given Num == R1::num * R2::den and Denom == R1::den * R2::num (computed without arithmetic overflow), U is std::ratio&lt;Num, Denom&gt;::num and V is std::ratio&lt;Num, Denom&gt;::den. 

<h2>Notes</h2>

If U or V is not representable in std::intmax_t, the program is ill-formed. If Num or Denom is not representable in std::intmax_t, the program is ill-formed unless the implementation yields correct values for U and V. 
The above definition requires that the result of std::ratio_divide&lt;R1, R2&gt; be already reduced to lowest terms; for example, std::ratio_divide&lt;std::ratio&lt;1, 12&gt;, std::ratio&lt;1, 6&gt;&gt; is the same type as std::ratio&lt;1, 2&gt;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;ratio&gt;
int main()

{
    typedef std::ratio&lt;2, 3&gt; two_third;
    typedef std::ratio&lt;1, 6&gt; one_sixth;
    typedef std::ratio_divide&lt;two_third, one_sixth&gt; r;
    std::cout &lt;&lt; &quot;2/3 / 1/6 = &quot; &lt;&lt; r::num &lt;&lt; '/' &lt;&lt; r::den &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2/3 / 1/6 = 4/1
