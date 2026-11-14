---
title: "stdis_swappable_withstdis_swappablestdis_nothrow_swappable_withstdis_nothrow_swappable(3)"
name: "stdis_swappable_withstdis_swappablestdis_nothrow_swappable_withstdis_nothrow_swappable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_swappable_withstdis_swappablestdis_nothrow_swappable_withstdis_nothrow_swappable/"
description: "std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,std::is_nothrow_swappable – std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,std::is_nothrow_swappable"
---

<p>std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,std::is_nothrow_swappable &#8211; std::is_swappable_with,std::is_swappable,std::is_nothrow_swappable_with,std::is_nothrow_swappable</p>
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
<p>1) If the expressions swap(std::declval&lt;T&gt;(), std::declval&lt;U&gt;()) and swap(std::declval&lt;U&gt;(), std::declval&lt;T&gt;()) are both well-formed in unevaluated context after using std::swap; (see Swappable), provides the member constant value equal true. Otherwise, value is false. Access_checks are performed as if from a context unrelated to either type.<br />
2) If T is not a referenceable type (i.e., possibly cv-qualified void or a function type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value equal to false. Otherwise, provides a member constant value equal to std::is_swappable_with&lt;T&amp;, T&amp;&gt;::value<br />
3) Same as <code>(1)</code>, but evaluations of both expressions from (1) are known not to throw exceptions<br />
4) Same as <code>(2)</code>, but uses is_nothrow_swappable_with.<br />
T and U shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates </p>
<pre><code>template &lt;class T, class U&gt;                                                                  (since C++17)

inline constexpr bool is_swappable_with_v = is_swappable_with&lt;T, U&gt;::value;

template &lt;class T&gt;                                                                           (since C++17)

inline constexpr bool is_swappable_v = is_swappable&lt;T&gt;::value;

template &lt;class T, class U&gt;                                                                  (since C++17)

inline constexpr bool is_nothrow_swappable_with_v = is_nothrow_swappable_with&lt;T, U&gt;::value;

template &lt;class T&gt;                                                                           (since C++17)

inline constexpr bool is_nothrow_swappable_v = is_nothrow_swappable&lt;T&gt;::value;
</code></pre>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is swappable with U , false otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to bool, returns value<br />
operator bool <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type bool<br />
type std::integral_constant&lt;bool, value&gt;</p>
<h2>Notes</h2>
<p>This trait does not check anything outside the immediate context of the swap expressions: if the use of T or U would trigger template specializations, generation of implicitly-defined special member functions etc, and those have errors, the actual swap may not compile even if std::is_swappable_with&lt;T,U&gt;::value compiles and evaluates to true. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects<br />
swap <i>(function template)</i><br />
is_move_assignable<br />
is_trivially_move_assignable<br />
is_nothrow_move_assignable checks if a type has a move assignment operator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
