---
title: "stdis_unsigned(3)"
name: "stdis_unsigned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_unsigned/"
description: "std::is_unsigned – std::is_unsigned"
---

<p>std::is_unsigned &#8211; std::is_unsigned</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_unsigned;</code></pre>
<p>If T is an arithmetic type, provides the member constant value equal true if T<code>(0)</code> &lt; T(-1): this results in true for the unsigned integer types and the type bool and in false for the signed integer types and the floating-point types.<br />
For any other type, value is false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_unsigned_v = is_unsigned&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an unsigned arithmetic type , false otherwise<br />
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
&nbsp;<wbr>&nbsp;struct is_unsigned : std::integral_constant&lt;bool, T<code>(0)</code> &lt; T(-1)&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;typename T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_unsigned&lt;T,false&gt; : std::false_type {};<br />
&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;template&lt;typename T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_unsigned : detail::is_unsigned&lt;T&gt;::type {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class A
{
};

enum B : unsigned {};

enum class C : unsigned {};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_unsigned&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_unsigned&lt;float&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_unsigned&lt;signed int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_unsigned&lt;unsigned int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_unsigned&lt;B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_unsigned&lt;C&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false</p>
<h2>See also</h2>
<p>is_signed checks if a type is a signed arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_arithmetic checks if a type is an arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_signed makes the given integral type signed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_unsigned makes the given integral type unsigned<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
