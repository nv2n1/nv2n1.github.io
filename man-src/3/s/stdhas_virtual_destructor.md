---
title: "stdhas_virtual_destructor(3)"
name: "stdhas_virtual_destructor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhas_virtual_destructor/"
description: "std::has_virtual_destructor – std::has_virtual_destructor"
---

<p>std::has_virtual_destructor &#8211; std::has_virtual_destructor</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct has_virtual_destructor;</code></pre>
<p>If T is a type with a virtual destructor, provides the member constant value equal true. For any other type, value is false.<br />
If T is a non-union class type, T shall be a complete type; otherwise, the behavior is undefined.<br />
Helper variable template template&lt; class T &gt;                                                                 (since C++17)</p>
<p>inline constexpr bool has_virtual_destructor_v = has_virtual_destructor&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T has a virtual destructor , false otherwise<br />
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
<p>If a class has a public virtual destructor, it can be derived from, and the derived object can be safely deleted through a pointer to the base object (GotW_#18) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;string&gt;

#include &lt;stdexcept&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;std::string has a virtual destructor? &quot;
              &lt;&lt; std::has_virtual_destructor&lt;std::string&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;std::runtime_error has a virtual destructor? &quot;
              &lt;&lt; std::has_virtual_destructor&lt;std::runtime_error&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::string has a virtual destructor? false<br />
&nbsp;<wbr>&nbsp;std::runtime_error has a virtual destructor? true</p>
<h2>See also</h2>
<p>is_destructible<br />
is_trivially_destructible<br />
is_nothrow_destructible checks if a type has a non-deleted destructor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
