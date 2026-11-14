---
title: "stdexperimentalconjunction(3)"
name: "stdexperimentalconjunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalconjunction/"
---

std::experimental::conjunction - std::experimental::conjunction

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / type_traits&gt;

    template &lt;class... B&gt;
    (library fundamentals TS v2)

        struct conjunction;</code></pre> 
Forms the logical_conjunction of the type traits B..., effectively performing a logical AND on the sequence of traits. 
The specialization std::experimental::conjunction&lt;B1, ..., BN&gt; has a public and unambiguous base that is 
* if sizeof...(B) == 0, std::true_type; otherwise 
* the first type Bi in B1, ..., BN for which bool(Bi::value) == false, or BN if there is no such type. 
The member names of the base class, other than conjunction and operator=, are not hidden and are unambiguously available in conjunction. 
Conjunction is short-circuiting: if there is a template type argument Bi with bool(Bi::value) == false, then instantiating conjunction&lt;B1, ..., BN&gt;::value does not require the instantiation of Bj::value for j &gt; i. 

<h2>Template parameters</h2>

B... - every template argument Bi for which Bi::value is instantiated must be usable as a base class and define member value that is convertible to bool 

 

 
Helper variable template 

 

 
template&lt;class... B&gt; (library fundamentals TS v2) 
constexpr bool conjunction_v = conjunction&lt;B...&gt;::value;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class...&gt; struct conjunction : std::true_type { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1&gt; struct conjunction&lt;B1&gt; : B1 { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1, class... Bn&gt; 
&nbsp;<wbr>&nbsp;struct conjunction&lt;B1, Bn...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::conditional_t&lt;bool(B1::value), conjunction&lt;Bn...&gt;, B1&gt; {};

<h2>Notes</h2>

A specialization of conjunction does not necessarily inherit from either std::true_type or std::false_type: it simply inherits from the first B whose ::value, converted to bool, is false, or from the very last B when all of them convert to true. For example, conjunction&lt;std::integral_constant&lt;int, 2&gt;, std::integral_constant&lt;int, 4&gt;&gt;::value is 4. 

<h2>Example</h2>

// Run this code <pre><code>// func is enabled if all Ts... have the same type

template &lt;typename T, typename... Ts&gt;

std::enable_if_t&lt;std::experimental::conjunction_v&lt;std::is_same&lt;T, Ts&gt;...&gt;&gt;

func(T, Ts...)
{
    // TODO something to show
}
</code></pre>

<h2>See also</h2>

conjunction variadic logical AND metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
