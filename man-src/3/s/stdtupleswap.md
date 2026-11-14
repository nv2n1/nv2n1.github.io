---
title: "stdtupleswap(3)"
name: "stdtupleswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtupleswap/"
---

std::tuple&lt;Types...&gt;::swap - std::tuple&lt;Types...&gt;::swap

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
void swap( tuple&amp; other ) noexcept(/* see below */); <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> 
constexpr void swap( tuple&amp; other ) noexcept(/* see below */); <i>(since C++20)</i> 
Calls swap (which might be std::swap, or might be found via ADL) for each element in *this and its corresponding element in other. 

<h2>Parameters</h2>

other - tuple of values to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept( 
noexcept(swap(std::declval&lt;T0&amp;&gt;&gt;(), std::declval&lt;T0&amp;&gt;())) &amp;&amp; 
noexcept(swap(std::declval&lt;T1&amp;&gt;&gt;(), std::declval&lt;T1&amp;&gt;())) &amp;&amp; <i>(until C++17)</i> 
noexcept(swap(std::declval&lt;T2&amp;&gt;&gt;(), std::declval&lt;T2&amp;&gt;())) &amp;&amp; 
... 
) 
In the expression above, the identifier swap is looked up in the same manner as the one used by the C++17 std::is_nothrow_swappable trait. 
noexcept specification: 
noexcept( 
std::is_nothrow_swappable_v&lt;T0&gt; &amp;&amp; 
std::is_nothrow_swappable_v&lt;T1&gt; &amp;&amp; <i>(since C++17)</i> 
std::is_nothrow_swappable_v&lt;T2&gt; &amp;&amp; 
... 
)

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;

#include &lt;string&gt;
int main()

{
    std::tuple&lt;int, std::string, float&gt; p1, p2;
    p1 = std::make_tuple(10, &quot;test&quot;, 3.14);
    p2.swap(p1);
    std::cout &lt;&lt; &quot;(&quot; &lt;&lt; std::get&lt;0&gt;(p2)
              &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;1&gt;(p2)
              &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;2&gt;(p2) &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(10, test, 3.14) 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2456 C++11 the noexcept specification is ill-formed made to work

<h2>See also</h2>


