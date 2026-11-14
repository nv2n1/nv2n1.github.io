---
title: "stdis_copy_constructiblestdis_trivially_copy_constructiblestdis_nothrow_copy_constructible(3)"
name: "stdis_copy_constructiblestdis_trivially_copy_constructiblestdis_nothrow_copy_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_copy_constructiblestdis_trivially_copy_constructiblestdis_nothrow_copy_constructible/"
description: "std::is_copy_constructible,std::is_trivially_copy_constructible,std::is_nothrow_copy_constructible – std::is_copy_constructible,std::is_trivially_copy_constructible,std::is_nothrow_copy_constructible"
---

<p>std::is_copy_constructible,std::is_trivially_copy_constructible,std::is_nothrow_copy_constructible &#8211; std::is_copy_constructible,std::is_trivially_copy_constructible,std::is_nothrow_copy_constructible</p>
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
<p>1) If T is not a referenceable type (i.e., possibly cv-qualified void or a function type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value equal to false. Otherwise, provides a member constant value equal to std::is_constructible&lt;T, const T&amp;&gt;::value.<br />
2) Same as <code>(1)</code>, but uses std::is_trivially_constructible&lt;T, const T&amp;&gt;.<br />
3) Same as <code>(1)</code>, but uses std::is_nothrow_constructible&lt;T, const T&amp;&gt;.<br />
T shall be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T &gt;                                                                                   (since C++17)</p>
<p>inline constexpr bool is_copy_constructible_v = is_copy_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                                   (since C++17)</p>
<p>inline constexpr bool is_trivially_copy_constructible_v = is_trivially_copy_constructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                                   (since C++17)</p>
<p>inline constexpr bool is_nothrow_copy_constructible_v = is_nothrow_copy_constructible&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is copy-constructible , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_copy_constructible :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_trivially_copy_constructible :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_trivially_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_nothrow_copy_constructible :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_nothrow_constructible&lt;T, typename std::add_lvalue_reference&lt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_const&lt;T&gt;::type&gt;::type&gt;&gt; {};</p>
<h2>Notes</h2>
<p>In many implementations, is_nothrow_copy_constructible also checks if the destructor throws because it is effectively noexcept(T(arg)). Same applies to is_trivially_copy_constructible, which, in these implementations, also requires that the destructor is trivial: GCC_bug_51452 LWG_issue_2116. </p>
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
<p>&nbsp;<wbr>&nbsp;Ex1 is copy-constructible? true<br />
&nbsp;<wbr>&nbsp;Ex1 is trivially copy-constructible? false<br />
&nbsp;<wbr>&nbsp;Ex2 is trivially copy-constructible? true<br />
&nbsp;<wbr>&nbsp;Ex2 is nothrow copy-constructible? true</p>
<h2>See also</h2>
<p>is_constructible<br />
is_trivially_constructible<br />
is_nothrow_constructible checks if a type has a constructor for specific arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_default_constructible<br />
is_trivially_default_constructible<br />
is_nothrow_default_constructible checks if a type has a default constructor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_constructible<br />
is_trivially_move_constructible<br />
is_nothrow_move_constructible checks if a type can be constructed from an rvalue reference<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
