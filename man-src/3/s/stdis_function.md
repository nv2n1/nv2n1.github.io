---
title: "stdis_function(3)"
name: "stdis_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_function/"
description: "std::is_function – std::is_function"
---

<p>std::is_function &#8211; std::is_function</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_function;</code></pre>
<p>Checks whether T is a function type. Types like std::function, lambdas, classes with overloaded operator() and pointers to functions don&#8217;t count as function types. Provides the member constant value which is equal to true, if T is a function type. Otherwise, value is equal to false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_function_v = is_function&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a function type , false otherwise<br />
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
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;// primary template<br />
&nbsp;<wbr>&nbsp;template&lt;class&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function : std::false_type { }; </p>
<p>&nbsp;<wbr>&nbsp;// specialization for regular functions<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;)&gt; : std::true_type {}; </p>
<p>&nbsp;<wbr>&nbsp;// specialization for variadic functions such as std::printf<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;)&gt; : std::true_type {}; </p>
<p>&nbsp;<wbr>&nbsp;// specialization for function types that have cv-qualifiers<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile&gt; : std::true_type {}; </p>
<p>&nbsp;<wbr>&nbsp;// specialization for function types that have ref-qualifiers<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile &amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile &amp;&amp;&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile &amp;&amp;&gt; : std::true_type {}; </p>
<p>&nbsp;<wbr>&nbsp;// specializations for noexcept versions of all the above (C++17 and later) </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile &amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) volatile &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;) const volatile &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) volatile &amp;&amp; noexcept&gt; : std::true_type {};<br />
&nbsp;<wbr>&nbsp;template&lt;class Ret, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;struct is_function&lt;Ret(Args&#8230;&#8230;) const volatile &amp;&amp; noexcept&gt; : std::true_type {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct A {
    int fun() const &amp;;
};
template &lt;typename&gt;

struct PM_traits {
};
template &lt;class T, class U&gt;

struct PM_traits&lt;U T::*&gt; {
    using member_type = U;
};
int f();
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_function&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_function&lt;int(int)&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_function&lt;decltype(f)&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_function&lt;int&gt;::value &lt;&lt; '
';
    using T = PM_traits&lt;decltype(&amp;A::fun)&gt;::member_type; // T is int() const&amp;
    std::cout &lt;&lt; std::is_function&lt;T&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
<p>is_invocable<br />
is_invocable_r checks if a type can be invoked (as if by std::invoke) with the given argument types<br />
is_nothrow_invocable <i>(class template)</i><br />
is_nothrow_invocable_r<br />
<i>(C++17)</i><br />
is_object checks if a type is an object type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_class checks if a type is a non-union class type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
