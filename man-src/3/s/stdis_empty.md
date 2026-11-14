---
title: "stdis_empty(3)"
name: "stdis_empty"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_empty/"
description: "std::is_empty – std::is_empty"
---

<p>std::is_empty &#8211; std::is_empty</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_empty;</code></pre>
<p>If T is an empty type (that is, a non-union class type with no non-static data members other than bit-fields of size 0, no virtual functions, no virtual base classes, and no non-empty base classes), provides the member constant value equal true. For any other type, value is false.<br />
If T is a non-union class type, T shall be a complete type; otherwise, the behavior is undefined. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_empty_v = is_empty&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an empty class type , false otherwise<br />
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
<p>Inheriting from empty base classes usually does not increase the size of a class due to empty_base_optimization.<br />
std::is_empty&lt;T&gt; and all other type traits are empty classes. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct A {
};
struct B {
    int m;
};
struct C {
    static int m;
};
struct D {
    virtual ~D();
};
union E {
};
struct F {
    [[no_unique_address]] E e;
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;A &quot; &lt;&lt; std::is_empty&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;B &quot; &lt;&lt; std::is_empty&lt;B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;C &quot; &lt;&lt; std::is_empty&lt;C&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;D &quot; &lt;&lt; std::is_empty&lt;D&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;E &quot; &lt;&lt; std::is_empty&lt;E&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;F &quot; &lt;&lt; std::is_empty&lt;F&gt;::value &lt;&lt; '
'; // the result is ABI-dependent
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;A true<br />
&nbsp;<wbr>&nbsp;B false<br />
&nbsp;<wbr>&nbsp;C true<br />
&nbsp;<wbr>&nbsp;D false<br />
&nbsp;<wbr>&nbsp;E false<br />
&nbsp;<wbr>&nbsp;F true</p>
<h2>See also</h2>
<p>is_class checks if a type is a non-union class type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
