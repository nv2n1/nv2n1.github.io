---
title: "stdpair(3)"
name: "stdpair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpair/"
---

std::pair&lt;T1,T2&gt;::swap - std::pair&lt;T1,T2&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(pair &amp;other) noexcept(/* see below */);
(since C++ 11)(until C++ 20)

    constexpr void swap(pair &amp;other) noexcept(/* see below */);
(since C++ 20)</code></pre> 
Swaps first with other.first and second with other.second. 

<h2>Parameters</h2>

other - pair of values to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept( 
noexcept(swap(first, other.first)) &amp;&amp; <i>(until C++17)</i> 
noexcept(swap(second, other.second)) 
) 
In the expression above, the identifier swap is looked up in the same manner as the one used by the C++17 std::is_nothrow_swappable trait. 
noexcept specification: 
noexcept( 
std::is_nothrow_swappable_v&lt;first_type&gt; &amp;&amp; <i>(since C++17)</i> 
std::is_nothrow_swappable_v&lt;second_type&gt; 
)

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;string&gt;

int main()

{
    std::pair&lt;int, std::string&gt; p1, p2;
    p1 = std::make_pair(10, &quot;test&quot;);
    p2.swap(p1);
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; p2.first &lt;&lt; &quot;, &quot; &lt;&lt; p2.second &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(10, test) 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2456 C++11 the noexcept specification is ill-formed made to work

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
