---
title: "stdratio_add(3)"
name: "stdratio_add"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdratio_add/"
---

std::ratio_add - std::ratio_add

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ratio&gt;

template&lt; class R1, class R2 &gt;      (since C++11)

using ratio_add = /* see below */;</code></pre> 
The alias template std::ratio_add denotes the result of adding two exact rational fractions represented by the std::ratio specializations R1 and R2. 
The result is a std::ratio specialization std::ratio&lt;U, V&gt;, such that given Num == R1::num * R2::den + R2::num * R1::den and Denom == R1::den * R2::den (computed without arithmetic overflow), U is std::ratio&lt;Num, Denom&gt;::num and V is std::ratio&lt;Num, Denom&gt;::den. 

<h2>Notes</h2>

If U or V is not representable in std::intmax_t, the program is ill-formed. If Num or Denom is not representable in std::intmax_t, the program is ill-formed unless the implementation yields correct values for U and V. 
The above definition requires that the result of std::ratio_add&lt;R1, R2&gt; be already reduced to lowest terms; for example, std::ratio_add&lt;std::ratio&lt;1, 3&gt;, std::ratio&lt;1, 6&gt;&gt; is the same type as std::ratio&lt;1, 2&gt;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;ratio&gt;
int main()

{
    typedef std::ratio&lt;2, 3&gt; two_third;
    typedef std::ratio&lt;1, 6&gt; one_sixth;
    typedef std::ratio_add&lt;two_third, one_sixth&gt; sum;
    std::cout &lt;&lt; &quot;2/3 + 1/6 = &quot; &lt;&lt; sum::num &lt;&lt; '/' &lt;&lt; sum::den &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2/3 + 1/6 = 5/6
