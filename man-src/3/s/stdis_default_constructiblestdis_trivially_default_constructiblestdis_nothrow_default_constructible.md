---
title: "stdis_default_constructiblestdis_trivially_default_constructiblestdis_nothrow_default_constructible(3)"
name: "stdis_default_constructiblestdis_trivially_default_constructiblestdis_nothrow_default_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_default_constructiblestdis_trivially_default_constructiblestdis_nothrow_default_constructible/"
description: "std::is_default_constructible,std::is_trivially_default_constructible,std::is_nothrow_default_constructible – std::is_default_constructible,std::is_trivially_default_constructible,std::is_nothrow_d..."
---

<p>std::is_default_constructible,std::is_trivially_default_constructible,std::is_nothrow_default_constructible &#8211; std::is_default_constructible,std::is_trivially_default_constructible,std::is_nothrow_default_constructible</p>
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
<p>1) If std::is_constructible&lt;T&gt;::value is true, provides the member constant value equal to true, otherwise value is false.<br />
2) If std::is_trivially_constructible&lt;T&gt;::value is true, provides the member constant value equal to true, otherwise value is false.<br />
3) If std::is_nothrow_constructible&lt;T&gt;::value is true, provides the member constant value equal to true, otherwise value is false.<br />
T shall be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T &gt;                                                                                         (since C++17)</p>
<p>inline constexpr bool is_default_constructible_v = is_default_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                                         (since C++17)</p>
<p>inline constexpr bool is_trivially_default_constructible_v = is_trivially_default_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                                         (since C++17)</p>
<p>inline constexpr bool is_nothrow_default_constructible_v = is_nothrow_default_constructible&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is default-constructible , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;template&lt; class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_default_constructible : std::is_constructible&lt;T&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_trivially_default_constructible : std::is_trivially_constructible&lt;T&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_nothrow_default_constructible : std::is_nothrow_constructible&lt;T&gt; {};</p>
<h2>Notes</h2>
<p>In many implementations, is_nothrow_default_constructible also checks if the destructor throws because it is effectively noexcept(T()). Same applies to is_trivially_default_constructible, which, in these implementations, also requires that the destructor is trivial: GCC_bug_51452 LWG_issue_2116.<br />
std::is_default_constructible&lt;T&gt; does not test that T x; would compile; it attempts direct-initialization with an empty argument list (see std::is_constructible). Thus, std::is_default_constructible_v&lt;const int&gt; and std::is_default_constructible_v&lt;const int[10]&gt; are true. </p>
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
<p>&nbsp;<wbr>&nbsp;Ex1 is default-constructible? true<br />
&nbsp;<wbr>&nbsp;Ex1 is trivially default-constructible? false<br />
&nbsp;<wbr>&nbsp;Ex2 is trivially default-constructible? true<br />
&nbsp;<wbr>&nbsp;Ex2 is nothrow default-constructible? true</p>
<h2>See also</h2>
<p>is_constructible<br />
is_trivially_constructible<br />
is_nothrow_constructible checks if a type has a constructor for specific arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_copy_constructible<br />
is_trivially_copy_constructible<br />
is_nothrow_copy_constructible checks if a type has a copy constructor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_constructible<br />
is_trivially_move_constructible<br />
is_nothrow_move_constructible checks if a type can be constructed from an rvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
