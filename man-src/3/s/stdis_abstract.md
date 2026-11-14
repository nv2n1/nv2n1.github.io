---
title: "stdis_abstract(3)"
name: "stdis_abstract"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_abstract/"
description: "std::is_abstract – std::is_abstract"
---

<p>std::is_abstract &#8211; std::is_abstract</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_abstract;</code></pre>
<p>If T is an abstract_class (that is, a non-union class that declares or inherits at least one pure virtual function), provides the member constant value equal true. For any other type, value is false.<br />
If T is a non-union class type, T shall be a complete type; otherwise, the behavior is undefined. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_abstract_v = is_abstract&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an abstract_class type , false otherwise<br />
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
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct A {
    int m;
};
struct B {
    virtual void foo();
};
struct C {
    virtual void foo() = 0;
};
struct D : C {
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_abstract&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_abstract&lt;B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_abstract&lt;C&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_abstract&lt;D&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
<p>is_class checks if a type is a non-union class type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
is_polymorphic checks if a type is a polymorphic class type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
