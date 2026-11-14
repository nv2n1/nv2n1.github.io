---
title: "stdis_copy_constructiblestdis_trivially_copy_constructible(3)"
name: "stdis_copy_constructiblestdis_trivially_copy_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_copy_constructiblestdis_trivially_copy_constructible/"
description: "std::is_copy_constructible,std::is_trivially_copy_constructible, – std::is_copy_constructible,std::is_trivially_copy_constructible,"
---

<p>std::is_copy_constructible,std::is_trivially_copy_constructible, &#8211; std::is_copy_constructible,std::is_trivially_copy_constructible,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct is_copy_constructible;

template &lt;class T&gt;
(2)(since C++ 11)

    struct is_trivially_copy_constructible;

template &lt;class T&gt;
(3)(since C++ 11)

    struct is_nothrow_copy_constructible;</code></pre>
<p>1)&nbsp;<wbr>If T is not a referenceable type&nbsp;<wbr>(i.e., possibly cv-qualified void or a function<br />
type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value<br />
equal to false. Otherwise, provides a member constant value equal to<br />
std::is_constructible&lt;T, const T&amp;&gt;::value.<br />
2)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but uses std::is_trivially_constructible&lt;T, const T&amp;&gt;.<br />
3)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but uses std::is_nothrow_constructible&lt;T, const T&amp;&gt;.<br />
T shall be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of unknown<br />
bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates template&lt; class T &gt;</p>
<p>inline constexpr bool is_copy_constructible_v =                        (since C++17)</p>
<p>is_copy_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_trivially_copy_constructible_v =              (since C++17)</p>
<p>is_trivially_copy_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_nothrow_copy_constructible_v =                (since C++17)</p>
<p>is_nothrow_copy_constructible&lt;T&gt;::value; Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if T is copy-constructible , false otherwise<br />
<code>[static]</code>&nbsp;<wbr><i>(public static member constant)</i></p>
<h2>Member functions</h2>
<p>operator bool converts the object to bool, returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i><br />
operator()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>returns value<br />
<i>(C++14)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i></p>
<h2>Member types</h2>
<p>Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Definition<br />
value_type bool<br />
type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::integral_constant&lt;bool, value&gt;</p>
<h2>Possible implementation</h2>
<p>template&lt;class T&gt;<br />
struct is_copy_constructible :<br />
&nbsp;<wbr>std::is_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;class T&gt;<br />
struct is_trivially_copy_constructible :<br />
&nbsp;<wbr>std::is_trivially_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;class T&gt;<br />
struct is_nothrow_copy_constructible :<br />
&nbsp;<wbr>std::is_nothrow_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt;&nbsp;<wbr>{};</p>
<h2>Notes</h2>
<p>In many implementations, is_nothrow_copy_constructible also checks if the destructor<br />
throws because it is effectively noexcept(T(arg)). Same applies to<br />
is_trivially_copy_constructible, which, in these implementations, also requires that<br />
the destructor is trivial: GCC bug 51452 LWG issue 2116. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct Ex1 {
    std::string str; // member has a non-trivial copy ctor
};

struct Ex2 {
    int n;
    Ex2(const Ex2 &amp;) = default; // trivial and non-throwing
};
int main()
{
    std::cout &lt;&lt; std::boolalpha &lt;&lt; &quot;Ex1 is copy-constructible? &quot;
              &lt;&lt; std::is_copy_constructible&lt;Ex1&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex1 is trivially copy-constructible? &quot;
              &lt;&lt; std::is_trivially_copy_constructible&lt;Ex1&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex2 is trivially copy-constructible? &quot;
              &lt;&lt; std::is_trivially_copy_constructible&lt;Ex2&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex2 is nothrow copy-constructible? &quot;
              &lt;&lt; std::is_nothrow_copy_constructible&lt;Ex2&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>Ex1 is copy-constructible?&nbsp;<wbr>true<br />
&nbsp;<wbr>Ex1 is trivially copy-constructible?&nbsp;<wbr>false<br />
&nbsp;<wbr>Ex2 is trivially copy-constructible?&nbsp;<wbr>true<br />
&nbsp;<wbr>Ex2 is nothrow copy-constructible?&nbsp;<wbr>true</p>
<h2>See also</h2>
<p>is_constructible<br />
is_trivially_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a constructor for specific<br />
is_nothrow_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>arguments<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_default_constructible<br />
is_trivially_default_constructible<br />
is_nothrow_default_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a default constructor<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_constructible<br />
is_trivially_move_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type can be constructed from an<br />
is_nothrow_move_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rvalue reference<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
