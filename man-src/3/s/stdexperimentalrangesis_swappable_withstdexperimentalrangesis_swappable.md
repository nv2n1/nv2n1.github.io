---
title: "stdexperimentalrangesis_swappable_withstdexperimentalrangesis_swappable(3)"
name: "stdexperimentalrangesis_swappable_withstdexperimentalrangesis_swappable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesis_swappable_withstdexperimentalrangesis_swappable/"
description: "std::experimental::ranges::is_swappable_with,std::experimental::ranges::is_swappable, – std::experimental::ranges::is_swappable_with,std::experimental::ranges::is_swappable,"
---

<p>std::experimental::ranges::is_swappable_with,std::experimental::ranges::is_swappable, &#8211; std::experimental::ranges::is_swappable_with,std::experimental::ranges::is_swappable,</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::experimental::ranges::is_nothrow_swappable </p>
<pre><code>Defined in header&lt;experimental / ranges / type_traits&gt;

    template &lt;class T, class U&gt;
    (1)(ranges TS)

        struct is_swappable_with;

template &lt;class T&gt;
(2)(ranges TS)

    struct is_swappable;

template &lt;class T, class U&gt;
(3)(ranges TS)

    struct is_nothrow_swappable_with;

template &lt;class T&gt;
(4)(ranges TS)

    struct is_nothrow_swappable;</code></pre>
<p>1)&nbsp;<wbr>If the expressions ranges::swap(std::declval&lt;T&gt;(), std::declval&lt;U&gt;())&nbsp;<wbr>and<br />
ranges::swap(std::declval&lt;U&gt;(), std::declval&lt;T&gt;())&nbsp;<wbr>are both well-formed when treated<br />
as an unevaluated operand, provides the member constant value equal true. Otherwise,<br />
value is false. Access checks are performed as if from a context unrelated to either<br />
type.<br />
2)&nbsp;<wbr>If T is not a referenceable type&nbsp;<wbr>(i.e., possibly cv-qualified void or a function<br />
type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value<br />
equal to false. Otherwise, provides a member constant value equal to<br />
ranges::is_swappable_with&lt;T&amp;, T&amp;&gt;::value.<br />
3)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but evaluations of both expressions from&nbsp;<wbr>(1)&nbsp;<wbr>are known not to throw<br />
exceptions.<br />
4)&nbsp;<wbr>Same as&nbsp;<wbr><code>(2)</code>, but uses is_nothrow_swappable_with.<br />
T and U shall each be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of<br />
unknown bound. Otherwise, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates </p>
<pre><code>template &lt;class T, class U&gt;                                          (1) (ranges TS)

constexpr bool is_swappable_with_v = is_swappable_with&lt;T, U&gt;::value;

template &lt;class T&gt;                                                   (2) (ranges TS)

constexpr bool is_swappable_v = is_swappable&lt;T&gt;::value;

template &lt;class T, class U&gt;

constexpr bool is_nothrow_swappable_with_v =                         (3) (ranges TS)

is_nothrow_swappable_with&lt;T, U&gt;::value;

template &lt;class T&gt;

constexpr bool is_nothrow_swappable_v =                              (4) (ranges TS)

is_nothrow_swappable&lt;T&gt;::value;</code></pre>
<p> Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if T is swappable with U , false otherwise<br />
<code>[static]</code>&nbsp;<wbr><i>(public static member constant)</i></p>
<h2>Member functions</h2>
<p>operator bool converts the object to bool, returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i><br />
operator()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>returns value<br />
<i>(C++14)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i></p>
<h2>Member types</h2>
<p>Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Definition<br />
value_type bool<br />
type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::integral_constant&lt;bool, value&gt;</p>
<h2>Notes</h2>
<p>This trait does not check anything outside the immediate context of the swap<br />
expressions: if the use of T or U would trigger template specializations, generation<br />
of implicitly-defined special member functions etc, and those have errors, the<br />
actual swap may not compile even if ranges::is_swappable_with&lt;T,U&gt;::value compiles<br />
and evaluates to true. </p>
<h2>Examples</h2>
<p>&nbsp;<wbr>This section is incomplete<br />
&nbsp;<wbr>Reason: no example </p>
<h2>See also</h2>
<p>Swappable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies that a type can be swapped or that two types can<br />
SwappableWith&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>be swapped with each other<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(concept)<br />
is_swappable_with<br />
is_swappable<br />
is_nothrow_swappable_with checks if objects of a type can be swapped with objects of<br />
is_nothrow_swappable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same or different type<br />
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i> </p>
