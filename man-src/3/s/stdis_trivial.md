---
title: "stdis_trivial(3)"
name: "stdis_trivial"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_trivial/"
description: "std::is_trivial – std::is_trivial"
---

<p>std::is_trivial &#8211; std::is_trivial</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_trivial;</code></pre>
<p>If T is TrivialType (that is, a scalar type, a trivially copyable class with a trivial_default_constructor, or array of such type/class, possibly cv-qualified), provides the member constant value equal true. For any other type, value is false.<br />
The behavior is undefined if std::remove_all_extents_t&lt;T&gt; is an incomplete type and not (possibly cv-qualified) void. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_trivial_v = is_trivial&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a trivial type , false otherwise<br />
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
&nbsp;<wbr>&nbsp;struct is_trivial : std::integral_constant&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_trivially_copyable&lt;T&gt;::value &amp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_trivially_default_constructible&lt;T&gt;::value<br />
&nbsp;<wbr>&nbsp;&gt; {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct A {
    int m;
};
struct B {
    B()
    {
    }
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_trivial&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_trivial&lt;B&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false</p>
<h2>See also</h2>
<p>is_trivially_copyable checks if a type is trivially copyable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
