---
title: "stdis_rvalue_reference(3)"
name: "stdis_rvalue_reference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_rvalue_reference/"
description: "std::is_rvalue_reference – std::is_rvalue_reference"
---

<p>std::is_rvalue_reference &#8211; std::is_rvalue_reference</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_rvalue_reference;</code></pre>
<p>Checks whether T is a rvalue reference type. Provides the member constant value which is equal to true, if T is a rvalue reference type. Otherwise, value is equal to false. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_rvalue_reference_v = is_rvalue_reference&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an rvalue reference type , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt; struct is_rvalue_reference : std::false_type {};<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt; struct is_rvalue_reference&lt;T&amp;&amp;&gt; : std::true_type {};</p>
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
    std::cout &lt;&lt; std::is_rvalue_reference&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;A &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;A &amp;&amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;int&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;int &amp;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_rvalue_reference&lt;int &amp;&amp;&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
<p>is_lvalue_reference checks if a type is a lvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_reference checks if a type is either a lvalue reference or rvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
