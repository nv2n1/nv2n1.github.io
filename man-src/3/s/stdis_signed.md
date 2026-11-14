---
title: "stdis_signed(3)"
name: "stdis_signed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_signed/"
description: "std::is_signed – std::is_signed"
---

<p>std::is_signed &#8211; std::is_signed</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_signed;</code></pre>
<p>If T is an arithmetic type, provides the member constant value equal true if T(-1) &lt; T<code>(0)</code>: this results in true for the floating-point types and the signed integer types, and in false for the unsigned integer types and the type bool.<br />
For any other type, value is false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_signed_v = is_signed&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a signed arithmetic type , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;namespace detail {<br />
&nbsp;<wbr>&nbsp;template&lt;typename T,bool = std::is_arithmetic&lt;T&gt;::value&gt;<br />
&nbsp;<wbr>&nbsp;struct is_signed : std::integral_constant&lt;bool, T(-1) &lt; T<code>(0)</code>&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;typename T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_signed&lt;T,false&gt; : std::false_type {};<br />
&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;template&lt;typename T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_signed : detail::is_signed&lt;T&gt;::type {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class A
{
};

enum B : int {};

enum class C : int {};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_signed&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;float&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;signed int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;unsigned int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;C&gt;::value &lt;&lt; '
';
    // shorter:
    std::cout &lt;&lt; std::is_signed&lt;signed int&gt;() &lt;&lt; '
';
    std::cout &lt;&lt; std::is_signed&lt;unsigned int&gt;() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false</p>
<h2>See also</h2>
<p>is_unsigned checks if a type is an unsigned arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_signed identifies signed types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant of std::numeric_limits&lt;T&gt;)</i><br />
<code>[static]</code><br />
is_arithmetic checks if a type is an arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_signed makes the given integral type signed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_unsigned makes the given integral type unsigned<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
