---
title: "stdis_default_constructiblestdis_trivially_default_constructible(3)"
name: "stdis_default_constructiblestdis_trivially_default_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_default_constructiblestdis_trivially_default_constructible/"
description: "std::is_default_constructible,std::is_trivially_default_constructible, – std::is_default_constructible,std::is_trivially_default_constructible,"
---

<p>std::is_default_constructible,std::is_trivially_default_constructible, &#8211; std::is_default_constructible,std::is_trivially_default_constructible,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct is_default_constructible;

template &lt;class T&gt;
(2)(since C++ 11)

    struct is_trivially_default_constructible;

template &lt;class T&gt;
(3)(since C++ 11)

    struct is_nothrow_default_constructible;</code></pre>
<p>1)&nbsp;<wbr>If std::is_constructible&lt;T&gt;::value is true, provides the member constant value<br />
equal to true, otherwise value is false.<br />
2)&nbsp;<wbr>If std::is_trivially_constructible&lt;T&gt;::value is true, provides the member<br />
constant value equal to true, otherwise value is false.<br />
3)&nbsp;<wbr>If std::is_nothrow_constructible&lt;T&gt;::value is true, provides the member constant<br />
value equal to true, otherwise value is false.<br />
T shall be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of unknown<br />
bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates template&lt; class T &gt;</p>
<p>inline constexpr bool is_default_constructible_v =                     (since C++17)</p>
<p>is_default_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_trivially_default_constructible_v =           (since C++17)</p>
<p>is_trivially_default_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_nothrow_default_constructible_v =             (since C++17)</p>
<p>is_nothrow_default_constructible&lt;T&gt;::value; Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if T is default-constructible , false otherwise<br />
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
<p>template&lt;&nbsp;<wbr>class T&gt;<br />
struct is_default_constructible : std::is_constructible&lt;T&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;&nbsp;<wbr>class T&gt;<br />
struct is_trivially_default_constructible : std::is_trivially_constructible&lt;T&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;&nbsp;<wbr>class T&gt;<br />
struct is_nothrow_default_constructible : std::is_nothrow_constructible&lt;T&gt;&nbsp;<wbr>{};</p>
<h2>Notes</h2>
<p>In many implementations, is_nothrow_default_constructible also checks if the<br />
destructor throws because it is effectively noexcept(T()). Same applies to<br />
is_trivially_default_constructible, which, in these implementations, also requires<br />
that the destructor is trivial: GCC bug 51452 LWG issue 2116.<br />
std::is_default_constructible&lt;T&gt;&nbsp;<wbr>does not test that T x;&nbsp;<wbr>would compile;&nbsp;<wbr>it attempts<br />
direct-initialization with an empty argument list&nbsp;<wbr>(see std::is_constructible). Thus,<br />
std::is_default_constructible_v&lt;const int&gt;&nbsp;<wbr>and std::is_default_constructible_v&lt;const<br />
int[10]&gt;&nbsp;<wbr>are true. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct Ex1 {
    std::string str; // member has a non-trivial default ctor
};

struct Ex2 {
    int n;
    Ex2() = default; // trivial and non-throwing
};
int main()
{
    std::cout &lt;&lt; std::boolalpha &lt;&lt; &quot;Ex1 is default-constructible? &quot;
              &lt;&lt; std::is_default_constructible&lt;Ex1&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex1 is trivially default-constructible? &quot;
              &lt;&lt; std::is_trivially_default_constructible&lt;Ex1&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex2 is trivially default-constructible? &quot;
              &lt;&lt; std::is_trivially_default_constructible&lt;Ex2&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex2 is nothrow default-constructible? &quot;
              &lt;&lt; std::is_nothrow_default_constructible&lt;Ex2&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>Ex1 is default-constructible?&nbsp;<wbr>true<br />
&nbsp;<wbr>Ex1 is trivially default-constructible?&nbsp;<wbr>false<br />
&nbsp;<wbr>Ex2 is trivially default-constructible?&nbsp;<wbr>true<br />
&nbsp;<wbr>Ex2 is nothrow default-constructible?&nbsp;<wbr>true</p>
<h2>See also</h2>
<p>is_constructible<br />
is_trivially_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a constructor for specific<br />
is_nothrow_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>arguments<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_copy_constructible<br />
is_trivially_copy_constructible<br />
is_nothrow_copy_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a copy constructor<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_constructible<br />
is_trivially_move_constructible checks if a type can be constructed from an rvalue<br />
is_nothrow_move_constructible&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reference<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
