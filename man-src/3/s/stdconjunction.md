---
title: "stdconjunction(3)"
name: "stdconjunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdconjunction/"
---

std::conjunction - std::conjunction

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class... B&gt;
    (1)(since C++ 17)

        struct conjunction;</code></pre> 
Forms the logical_conjunction of the type traits B..., effectively performing a logical AND on the sequence of traits. 
The specialization std::conjunction&lt;B1, ..., BN&gt; has a public and unambiguous base that is 
* if sizeof...(B) == 0, std::true_type; otherwise 
* the first type Bi in B1, ..., BN for which bool(Bi::value) == false, or BN if there is no such type. 
The member names of the base class, other than conjunction and operator=, are not hidden and are unambiguously available in conjunction. 
Conjunction is short-circuiting: if there is a template type argument Bi with bool(Bi::value) == false, then instantiating conjunction&lt;B1, ..., BN&gt;::value does not require the instantiation of Bj::value for j &gt; i. 

<h2>Template parameters</h2>

B... - every template argument Bi for which Bi::value is instantiated must be usable as a base class and define member value that is convertible to bool 

 

 
Helper variable template 

 

 
template&lt;class... B&gt; <i>(since C++17)</i> 
inline constexpr bool conjunction_v = conjunction&lt;B...&gt;::value;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class...&gt; struct conjunction : std::true_type { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1&gt; struct conjunction&lt;B1&gt; : B1 { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1, class... Bn&gt; 
&nbsp;<wbr>&nbsp;struct conjunction&lt;B1, Bn...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::conditional_t&lt;bool(B1::value), conjunction&lt;Bn...&gt;, B1&gt; {};

<h2>Notes</h2>

A specialization of conjunction does not necessarily inherit from either std::true_type or std::false_type: it simply inherits from the first B whose ::value, explicitly converted to bool, is false, or from the very last B when all of them convert to true. For example, std::conjunction&lt;std::integral_constant&lt;int, 2&gt;, std::integral_constant&lt;int, 4&gt;&gt;::value is 4. 
The short-circuit instantiation differentiates conjunction from fold expressions: a fold expression like (... &amp;&amp; Bs::value) instantiates every B in Bs, while std::conjunction_v&lt;Bs...&gt; stops instantiation once the value can be determined. This is particularly useful if the later type is expensive to instantiate or can cause a hard error when instantiated with the wrong type. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
// func is enabled if all Ts... have the same type as T

template &lt;typename T, typename... Ts&gt;

std::enable_if_t&lt;std::conjunction_v&lt;std::is_same&lt;T, Ts&gt;...&gt;&gt;

func(T, Ts...)
{
    std::cout &lt;&lt; &quot;all types in pack are T\n&quot;;
}
// otherwise

template &lt;typename T, typename... Ts&gt;

std::enable_if_t&lt;!std::conjunction_v&lt;std::is_same&lt;T, Ts&gt;...&gt;&gt;

func(T, Ts...)
{
    std::cout &lt;&lt; &quot;not all types in pack are T\n&quot;;
}
int main()
{
    func(1, 2, 3);
    func(1, 2, &quot;hello!&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;all types in pack are T 
&nbsp;<wbr>&nbsp;not all types in pack are T

<h2>See also</h2>

negation logical NOT metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
disjunction variadic logical OR metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
