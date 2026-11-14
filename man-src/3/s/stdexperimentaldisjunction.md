---
title: "stdexperimentaldisjunction(3)"
name: "stdexperimentaldisjunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaldisjunction/"
---

std::experimental::disjunction - std::experimental::disjunction

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / type_traits&gt;

    template &lt;class... B&gt;
    (library fundamentals TS v2)

        struct disjunction;</code></pre> 
Forms the logical_disjunction of the type traits B..., effectively performing a logical or on the sequence of traits. 
The specialization std::experimental::disjunction&lt;B1, ..., BN&gt; has a public and unambiguous base that is 
* if sizeof...(B) == 0, std::false_type; otherwise 
* the first type Bi in B1, ..., BN for which bool(Bi::value) == true, or BN if there is no such type. 
The member names of the base class, other than disjunction and operator=, are not hidden and are unambiguously available in disjunction. 
Disjunction is short-circuiting: if there is a template type argument Bi with bool(Bi::value) != false, then instantiating disjunction&lt;B1, ..., BN&gt;::value does not require the instantiation of Bj::value for j &gt; i 

<h2>Template parameters</h2>

B... - every template argument Bi for which Bi::value is instantiated must be usable as a base class and define member value that is convertible to bool 

 

 
Helper variable template 

 

 
template&lt;class... B&gt; (library fundamentals TS v2) 
constexpr bool disjunction_v = disjunction&lt;B...&gt;::value;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class...&gt; struct disjunction : std::false_type { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1&gt; struct disjunction&lt;B1&gt; : B1 { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1, class... Bn&gt; 
&nbsp;<wbr>&nbsp;struct disjunction&lt;B1, Bn...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::conditional_t&lt;bool(B1::value), B1, disjunction&lt;Bn...&gt;&gt; { };

<h2>Notes</h2>

A specialization of disjunction does not necessarily inherit from of either std::true_type or std::false_type: it simply inherits from the first B whose ::value, explicitly converted to bool, is true, or from the very last B when all of them convert to false. For example, disjunction&lt;std::integral_constant&lt;int, 2&gt;, std::integral_constant&lt;int, 4&gt;&gt;::value is 2. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

disjunction variadic logical OR metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
