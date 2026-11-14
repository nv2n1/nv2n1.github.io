---
title: "stdis_invocablestdis_invocable_rstdis_nothrow_invocable(3)"
name: "stdis_invocablestdis_invocable_rstdis_nothrow_invocable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_invocablestdis_invocable_rstdis_nothrow_invocable/"
description: "std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable, – std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,"
---

<p>std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable, &#8211; std::is_invocable,std::is_invocable_r,std::is_nothrow_invocable,</p>
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
<p>1)&nbsp;<wbr>Determines whether Fn can be invoked with the arguments ArgTypes&#8230;. Formally,<br />
determines whether INVOKE(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;)&nbsp;<wbr>is well formed when<br />
treated as an unevaluated operand, where INVOKE is the operation defined in<br />
Callable.<br />
2)&nbsp;<wbr>Determines whether Fn can be invoked with the arguments ArgTypes&#8230; to yield a<br />
result that is convertible to R. Formally, determines whether<br />
INVOKE&lt;R&gt;(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;)&nbsp;<wbr>is well formed when treated as an<br />
unevaluated operand, where INVOKE is the operation defined in Callable<br />
3)&nbsp;<wbr>Determines whether Fn is callable with the arguments ArgTypes&#8230;&nbsp;<wbr>(same as&nbsp;<wbr><code>(1)</code>),<br />
and that such call is known not to throw any exceptions.<br />
4)&nbsp;<wbr>Determines whether Fn can be invoked with the arguments ArgTypes&#8230; to yield a<br />
result that is convertible to R&nbsp;<wbr>(same as&nbsp;<wbr><code>(2)</code>), and that such call&nbsp;<wbr>(including the<br />
conversion)&nbsp;<wbr>is known not to throw any exceptions.<br />
Fn, R and all types in the parameter pack ArgTypes shall each be a complete type,<br />
(possibly cv-qualified)&nbsp;<wbr>void, or an array of unknown bound. Otherwise, the behavior<br />
is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates Defined in header &lt;type_traits&gt;</p>
<p>template &lt;class Fn, class&#8230; ArgTypes&gt;</p>
<p>inline constexpr bool is_invocable_v = std::is_invocable&lt;Fn,       (1) (since C++17)</p>
<p>ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class R, class Fn, class&#8230; ArgTypes&gt;</p>
<p>inline constexpr bool is_invocable_r_v = std::is_invocable_r&lt;R,    (2) (since C++17)</p>
<p>Fn, ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class Fn, class&#8230; ArgTypes&gt;</p>
<p>inline constexpr bool is_nothrow_invocable_v =                     (3) (since C++17)</p>
<p>std::is_nothrow_invocable&lt;Fn, ArgTypes&#8230;&gt;::value;</p>
<p>template &lt;class R, class Fn, class&#8230; ArgTypes&gt;</p>
<p>inline constexpr bool is_nothrow_invocable_r_v =                   (4) (since C++17)</p>
<p>std::is_nothrow_invocable_r&lt;R, Fn, ArgTypes&#8230;&gt;::value; Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if INVOKE&lt;R&gt;(declval&lt;Fn&gt;(), declval&lt;ArgTypes&gt;()&#8230;)&nbsp;<wbr>is well formed<br />
<code>[static]</code>&nbsp;<wbr>when treated as an unevaluated operand , false otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public static member constant)</i></p>
<h2>Member functions</h2>
<p>operator bool converts the object to bool, returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i><br />
operator()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>returns value<br />
<i>(C++14)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i></p>
<h2>Member types</h2>
<p>Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Definition<br />
value_type bool<br />
type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::integral_constant&lt;bool, value&gt;</p>
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
<p>invoke&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>invokes any Callable object with given arguments<br />
<i>(C++17)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i><br />
result_of&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>deduces the result type of invoking a callable object with<br />
invoke_result&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a set of arguments<br />
<i>(C++11)</i>(removed in C++20)&nbsp;<wbr><i>(class template)</i><br />
<i>(C++17)</i><br />
declval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>obtains a reference to its argument for use in unevaluated<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>context<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(function template)</i> </p>
