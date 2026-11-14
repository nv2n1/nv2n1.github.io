---
title: "stdintegral_constant(3)"
name: "stdintegral_constant"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdintegral_constant/"
description: "std::integral_constant – std::integral_constant"
---

<p>std::integral_constant &#8211; std::integral_constant</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, T v&gt;
    (since C++ 11)

        struct integral_constant;</code></pre>
<p>std::integral_constant wraps a static constant of specified type. It is the base class for the C++ type traits.<br />
Helper templates<br />
A helper alias template std::bool_constant is defined for the common case where T is bool. <i>(since C++17)</i> template &lt;bool B&gt;</p>
<p>using bool_constant = integral_constant&lt;bool, B&gt;;</p>
<p>Two typedefs for the common case where T is bool are provided:<br />
Defined in header &lt;type_traits&gt;<br />
Type Definition<br />
true_type std::integral_constant&lt;bool, true&gt;<br />
false_type std::integral_constant&lt;bool, false&gt; </p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type T<br />
type std::integral_constant&lt;T,v&gt;</p>
<h2>Member constants</h2>
<p>Name Value </p>
<p>constexpr T value static constant of type T with value v<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the wrapped value<br />
operator value_type <i>(public member function)</i> </p>
<p>operator() returns the wrapped value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i> </p>
<p>&nbsp;std::integral_constant::operator value_type </p>
<p>constexpr operator value_type() const noexcept; </p>
<p>Conversion function. Returns the wrapped value. </p>
<p>&nbsp;std::integral_constant::operator() </p>
<p>constexpr value_type operator()() const noexcept; <i>(since C++14)</i> </p>
<p>Returns the wrapped value. This function enables std::integral_constant to serve as a source of compile-time function objects.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, T v&gt;<br />
&nbsp;<wbr>&nbsp;struct integral_constant {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static constexpr T value = v;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef T value_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef integral_constant type; // using injected-class-name<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constexpr operator value_type() const noexcept { return value; }<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constexpr value_type operator()() const noexcept { return value; } //since c++14<br />
&nbsp;<wbr>&nbsp;};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    typedef std::integral_constant&lt;int, 2&gt; two_t;
    typedef std::integral_constant&lt;int, 4&gt; four_t;
    //  static_assert(std::is_same&lt;two_t, four_t&gt;::value,

    //                &quot;two_t and four_t are not equal!&quot;);

    //  error: static assertion failed: &quot;two_t and four_t are not equal!&quot;
    static_assert(two_t::value * 2 == four_t::value,
                  &quot;2*2 != 4&quot;);
    enum class my_e {
        e1,
        e2
    };
    typedef std::integral_constant&lt;my_e, my_e::e1&gt; my_e_e1;
    typedef std::integral_constant&lt;my_e, my_e::e2&gt; my_e_e2;
    //  static_assert(my_e_e1::value == my_e::e2,

    //               &quot;my_e_e1::value != my_e::e2&quot;);

    //  error: static assertion failed: &quot;my_e_e1::value != my_e::e2&quot;
    static_assert(std::is_same&lt;my_e_e2, my_e_e2&gt;::value,
                  &quot;my_e_e2 != my_e_e2&quot;);
}
</code></pre>
