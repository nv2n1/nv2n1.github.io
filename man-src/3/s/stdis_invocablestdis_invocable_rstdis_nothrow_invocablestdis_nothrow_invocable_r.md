---
title: "stdis_invocablestdis_invocable_rstdis_nothrow_invocablestdis_nothrow_invocable_r(3)"
name: "stdis_invocablestdis_invocable_rstdis_nothrow_invocablestdis_nothrow_invocable_r"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_invocablestdis_invocable_rstdis_nothrow_invocablestdis_nothrow_invocable_r/"
description: "std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,std::is_nothrow_invocable_r – std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,std::is_nothrow_invocable_r"
---

<p>std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,std::is_nothrow_invocable_r &#8211; std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,std::is_nothrow_invocable_r</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class Fn, class... ArgTypes&gt;
    (1)(since C++ 17)

        struct is_invocable;

template &lt;class R, class Fn, class... ArgTypes&gt;
(2)(since C++ 17)

    struct is_invocable_r;

template &lt;class Fn, class... ArgTypes&gt;
(3)(since C++ 17)

    struct is_nothrow_invocable;

template &lt;class R, class Fn, class... ArgTypes&gt;
(4)(since C++ 17)

    struct is_nothrow_invocable_r;</code></pre>
<p>1) Determines whether Fn can be invoked with the arguments ArgTypes&#8230;. Formally, determines whether INVOKE(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;) is well formed when treated as an unevaluated operand, where INVOKE is the operation defined in Callable.<br />
2) Determines whether Fn can be invoked with the arguments ArgTypes&#8230; to yield a result that is convertible to R. Formally, determines whether INVOKE&lt;R&gt;(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;) is well formed when treated as an unevaluated operand, where INVOKE is the operation defined in Callable<br />
3) Determines whether Fn is callable with the arguments ArgTypes&#8230; (same as <code>(1)</code>), and that such call is known not to throw any exceptions.<br />
4) Determines whether Fn can be invoked with the arguments ArgTypes&#8230; to yield a result that is convertible to R (same as <code>(2)</code>), and that such call (including the conversion) is known not to throw any exceptions.<br />
Fn, R and all types in the parameter pack ArgTypes shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates Defined in header &lt;type_traits&gt;</p>
<p>template &lt;class Fn, class&#8230; ArgTypes&gt;                                                                   (1) (since C++17)</p>
<p>inline constexpr bool is_invocable_v = std::is_invocable&lt;Fn, ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class R, class Fn, class&#8230; ArgTypes&gt;                                                          (2) (since C++17)</p>
<p>inline constexpr bool is_invocable_r_v = std::is_invocable_r&lt;R, Fn, ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class Fn, class&#8230; ArgTypes&gt;                                                                   (3) (since C++17)</p>
<p>inline constexpr bool is_nothrow_invocable_v = std::is_nothrow_invocable&lt;Fn, ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class R, class Fn, class&#8230; ArgTypes&gt;                                                          (4) (since C++17)</p>
<p>inline constexpr bool is_nothrow_invocable_r_v = std::is_nothrow_invocable_r&lt;R, Fn, ArgTypes&#8230;&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if INVOKE&lt;R&gt;(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;) is well formed when treated as an unevaluated operand , false otherwise<br />
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
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;type_traits&gt;
auto func2(char) -&gt; int (*)()

{
    return nullptr;
}
int main()

{
    static_assert(std::is_invocable&lt;int()&gt;::value);
    static_assert(std::is_invocable_r&lt;int, int()&gt;::value);
    static_assert(std::is_invocable_r&lt;void, void(int), int&gt;::value);
    static_assert(std::is_invocable_r&lt;int (*)(), decltype(func2), char&gt;::value);
}
</code></pre>
<h2>See also</h2>
<p>invoke invokes any Callable object with given arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
result_of<br />
invoke_result deduces the result type of invoking a callable object with a set of arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i>(removed in C++20)<br />
<i>(C++17)</i><br />
declval obtains a reference to its argument for use in unevaluated context<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
