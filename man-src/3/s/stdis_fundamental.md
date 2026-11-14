---
title: "stdis_fundamental(3)"
name: "stdis_fundamental"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_fundamental/"
description: "std::is_fundamental – std::is_fundamental"
---

<p>std::is_fundamental &#8211; std::is_fundamental</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_fundamental;</code></pre>
<p>If T is a fundamental type (that is, arithmetic type, void, or nullptr_t), provides the member constant value equal true. For any other type, value is false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_fundamental_v = is_fundamental&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a fundamental type , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;template&lt; class T &gt;<br />
&nbsp;<wbr>&nbsp;struct is_fundamental<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::integral_constant&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_arithmetic&lt;T&gt;::value ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_void&lt;T&gt;::value ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_same&lt;std::nullptr_t, typename std::remove_cv&lt;T&gt;::type&gt;::value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// you can also use &#8216;std::is_null_pointer&lt;T&gt;::value&#8217; instead in C++14<br />
&nbsp;<wbr>&nbsp;&gt; {};</p>
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
    std::cout &lt;&lt; &quot;A	&quot; &lt;&lt; std::is_fundamental&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int	&quot; &lt;&lt; std::is_fundamental&lt;int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int&amp;	&quot; &lt;&lt; std::is_fundamental&lt;int &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;int*	&quot; &lt;&lt; std::is_fundamental&lt;int *&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float	&quot; &lt;&lt; std::is_fundamental&lt;float&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float&amp;	&quot; &lt;&lt; std::is_fundamental&lt;float &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;float*	&quot; &lt;&lt; std::is_fundamental&lt;float *&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;A<tt> </tt>false</p>
<p>&nbsp;<wbr>&nbsp;int<tt> </tt>true</p>
<p>&nbsp;<wbr>&nbsp;int&amp;<tt> </tt>false</p>
<p>&nbsp;<wbr>&nbsp;int*<tt> </tt>false</p>
<p>&nbsp;<wbr>&nbsp;float<tt> </tt>true</p>
<p>&nbsp;<wbr>&nbsp;float&amp;<tt> </tt>false</p>
<p>&nbsp;<wbr>&nbsp;float*<tt> </tt>false</p>
<h2>See also</h2>
<p>is_compound checks if a type is a compound type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_arithmetic checks if a type is an arithmetic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_void checks if a type is void<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_null_pointer checks if a type is std::nullptr_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++14)</i> </p>
