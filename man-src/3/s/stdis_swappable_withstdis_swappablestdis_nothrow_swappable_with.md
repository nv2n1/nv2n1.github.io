---
title: "stdis_swappable_withstdis_swappablestdis_nothrow_swappable_with(3)"
name: "stdis_swappable_withstdis_swappablestdis_nothrow_swappable_with"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_swappable_withstdis_swappablestdis_nothrow_swappable_with/"
description: "std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with, – std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,"
---

<p>std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with, &#8211; std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, class U&gt;
    (1)(since C++ 17)

        struct is_swappable_with;

template &lt;class T&gt;
(2)(since C++ 17)

    struct is_swappable;

template &lt;class T, class U&gt;
(3)(since C++ 17)

    struct is_nothrow_swappable_with;

template &lt;class T&gt;
(4)(since C++ 17)

    struct is_nothrow_swappable;</code></pre>
<p>1)&nbsp;<wbr>If the expressions swap(std::declval&lt;T&gt;(), std::declval&lt;U&gt;())&nbsp;<wbr>and<br />
swap(std::declval&lt;U&gt;(), std::declval&lt;T&gt;())&nbsp;<wbr>are both well-formed in unevaluated<br />
context after using std::swap;&nbsp;<wbr>(see Swappable), provides the member constant value<br />
equal true. Otherwise, value is false. Access checks are performed as if from a<br />
context unrelated to either type.<br />
2)&nbsp;<wbr>If T is not a referenceable type&nbsp;<wbr>(i.e., possibly cv-qualified void or a function<br />
type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value<br />
equal to false. Otherwise, provides a member constant value equal to<br />
std::is_swappable_with&lt;T&amp;, T&amp;&gt;::value<br />
3)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but evaluations of both expressions from&nbsp;<wbr>(1)&nbsp;<wbr>are known not to throw<br />
exceptions<br />
4)&nbsp;<wbr>Same as&nbsp;<wbr><code>(2)</code>, but uses is_nothrow_swappable_with.<br />
T and U shall each be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of<br />
unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates </p>
<pre><code>template &lt;class T, class U&gt;

inline constexpr bool is_swappable_with_v = is_swappable_with&lt;T,       (since C++17)

U&gt;::value;

template &lt;class T&gt;                                                     (since C++17)

inline constexpr bool is_swappable_v = is_swappable&lt;T&gt;::value;

template &lt;class T, class U&gt;

inline constexpr bool is_nothrow_swappable_with_v =                    (since C++17)

is_nothrow_swappable_with&lt;T, U&gt;::value;

template &lt;class T&gt;

inline constexpr bool is_nothrow_swappable_v =                         (since C++17)

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
actual swap may not compile even if std::is_swappable_with&lt;T,U&gt;::value compiles and<br />
evaluates to true. </p>
<h2>Example</h2>
<p>&nbsp;<wbr>This section is incomplete<br />
&nbsp;<wbr>Reason: no example </p>
<h2>See also</h2>
<p>swap&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>swaps the values of two objects<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
is_move_assignable<br />
is_trivially_move_assignable<br />
is_nothrow_move_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a move assignment operator<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
