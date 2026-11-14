---
title: "stdadd_lvalue_referencestdadd_rvalue_reference(3)"
name: "stdadd_lvalue_referencestdadd_rvalue_reference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadd_lvalue_referencestdadd_rvalue_reference/"
description: "std::add_lvalue_reference,std::add_rvalue_reference – std::add_lvalue_reference,std::add_rvalue_reference"
---

<p>std::add_lvalue_reference,std::add_rvalue_reference &#8211; std::add_lvalue_reference,std::add_rvalue_reference</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct add_lvalue_reference;

template &lt;class T&gt;
(2)(since C++ 11)

    struct add_rvalue_reference;</code></pre>
<p>Creates a lvalue or rvalue reference type of T.<br />
1) If T is an object type or a function type that has no cv- or ref- qualifier, provides a member typedef type which is T&amp;. If T is an rvalue reference to some type U, then type is U&amp;. Otherwise, type is T.<br />
2) If T is an object type or a function type that has no cv- or ref- qualifier, provides a member typedef type which is T&amp;&amp;, otherwise type is T. </p>
<h2>Member types</h2>
<p>Name Definition<br />
type reference to T, or T if not allowed</p>
<h2>Helper types</h2>
<p>template&lt; class T &gt; <i>(since C++14)</i><br />
using add_lvalue_reference_t = typename add_lvalue_reference&lt;T&gt;::type;<br />
template&lt; class T &gt; <i>(since C++14)</i><br />
using add_rvalue_reference_t = typename add_rvalue_reference&lt;T&gt;::type;</p>
<h2>Notes</h2>
<p>These type transformations honor reference collapse rules:<br />
std::add_lvalue_reference&lt;T&amp;&gt;::type is T&amp;<br />
std::add_lvalue_reference&lt;T&amp;&amp;&gt;::type is T&amp;<br />
std::add_rvalue_reference&lt;T&amp;&gt;::type is T&amp;<br />
std::add_rvalue_reference&lt;T&amp;&amp;&gt;::type is T&amp;&amp; </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;namespace detail { </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct type_identity { using type = T; }; // or use std::type_identity <i>(since C++20)</i> </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_lvalue_reference(int) -&gt; type_identity&lt;T&amp;&gt;;<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_lvalue_reference(&#8230;) -&gt; type_identity&lt;T&gt;; </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_rvalue_reference(int) -&gt; type_identity&lt;T&amp;&amp;&gt;;<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_rvalue_reference(&#8230;) -&gt; type_identity&lt;T&gt;; </p>
<p>&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct add_lvalue_reference : decltype(detail::try_add_lvalue_reference&lt;T&gt;<code>(0)</code>) {}; </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct add_rvalue_reference : decltype(detail::try_add_rvalue_reference&lt;T&gt;<code>(0)</code>) {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()
{
    using nonref = int;
    using lref = typename std::add_lvalue_reference&lt;nonref&gt;::type;
    using rref = typename std::add_rvalue_reference&lt;nonref&gt;::type;
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_lvalue_reference&lt;nonref&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_lvalue_reference&lt;lref&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;rref&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;true </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2101 C++11 These transformation traits were required Produce cv-/ref-qualified function types themselves.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to produce reference to cv-/ref-qualified function types.</p>
<h2>See also</h2>
<p>is_reference checks if a type is either a lvalue reference or rvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_reference removes a reference from the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_cvref combines std::remove_cv and std::remove_reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
(C++20) </p>
