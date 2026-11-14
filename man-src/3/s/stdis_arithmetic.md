---
title: "stdis_arithmetic(3)"
name: "stdis_arithmetic"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_arithmetic/"
description: "std::is_arithmetic – std::is_arithmetic"
---

<p>std::is_arithmetic &#8211; std::is_arithmetic</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_arithmetic;</code></pre>
<p>If T is an arithmetic type (that is, an integral type or a floating-point type) or a cv-qualified version thereof, provides the member constant value equal true. For any other type, value is false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_arithmetic_v = is_arithmetic&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an arithmetic type , false otherwise<br />
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
<p>Arithmetic types are the built-in types for which the arithmetic_operators (+, -, *, /) are defined (possibly in combination with the usual arithmetic conversions)<br />
Specializations of std::numeric_limits are provided for all arithmetic types. </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class T &gt;<br />
&nbsp;<wbr>&nbsp;struct is_arithmetic : std::integral_constant&lt;bool,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_integral&lt;T&gt;::value ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_floating_point&lt;T&gt;::value&gt; {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class A
{
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;A:           &quot; &lt;&lt; std::is_arithmetic&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;bool:        &quot; &lt;&lt; std::is_arithmetic&lt;bool&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int:         &quot; &lt;&lt; std::is_arithmetic&lt;int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int const:   &quot; &lt;&lt; std::is_arithmetic&lt;int const&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int &amp;:       &quot; &lt;&lt; std::is_arithmetic&lt;int &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int *:       &quot; &lt;&lt; std::is_arithmetic&lt;int *&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float:       &quot; &lt;&lt; std::is_arithmetic&lt;float&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float const: &quot; &lt;&lt; std::is_arithmetic&lt;float const&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float &amp;:     &quot; &lt;&lt; std::is_arithmetic&lt;float &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float *:     &quot; &lt;&lt; std::is_arithmetic&lt;float *&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;char:        &quot; &lt;&lt; std::is_arithmetic&lt;char&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;char const:  &quot; &lt;&lt; std::is_arithmetic&lt;char const&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;char &amp;:      &quot; &lt;&lt; std::is_arithmetic&lt;char &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;char *:      &quot; &lt;&lt; std::is_arithmetic&lt;char *&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;A: false<br />
&nbsp;<wbr>&nbsp;bool: true<br />
&nbsp;<wbr>&nbsp;int: true<br />
&nbsp;<wbr>&nbsp;int const: true<br />
&nbsp;<wbr>&nbsp;int &amp;: false<br />
&nbsp;<wbr>&nbsp;int *: false<br />
&nbsp;<wbr>&nbsp;float: true<br />
&nbsp;<wbr>&nbsp;float const: true<br />
&nbsp;<wbr>&nbsp;float &amp;: false<br />
&nbsp;<wbr>&nbsp;float *: false<br />
&nbsp;<wbr>&nbsp;char: true<br />
&nbsp;<wbr>&nbsp;char const: true<br />
&nbsp;<wbr>&nbsp;char &amp;: false<br />
&nbsp;<wbr>&nbsp;char *: false</p>
<h2>See also</h2>
<p>is_integral checks if a type is an integral type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_floating_point checks if a type is a floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
