---
title: "stdis_destructiblestdis_trivially_destructiblestdis_nothrow_destructible(3)"
name: "stdis_destructiblestdis_trivially_destructiblestdis_nothrow_destructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_destructiblestdis_trivially_destructiblestdis_nothrow_destructible/"
description: "std::is_destructible,std::is_trivially_destructible,std::is_nothrow_destructible – std::is_destructible,std::is_trivially_destructible,std::is_nothrow_destructible"
---

<p>std::is_destructible,std::is_trivially_destructible,std::is_nothrow_destructible &#8211; std::is_destructible,std::is_trivially_destructible,std::is_nothrow_destructible</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct is_destructible;

template &lt;class T&gt;
(2)(since C++ 11)

    struct is_trivially_destructible;

template &lt;class T&gt;
(3)(since C++ 11)

    struct is_nothrow_destructible;
</code></pre>
<p>1) If an imaginary struct containing a member object of type T has a non-deleted destructor, provides the member constant value equal true. For any other type, value is false. <i>(until C++14)</i><br />
1) If T is a reference type, provides the member constant value equal true<br />
If T is (possibly cv-qualified) void, a function type, or an array of unknown bound, value equals false. <i>(since C++14)</i><br />
If T is an object type, then, for the type U equal std::remove_all_extents&lt;T&gt;::type, if the expression std::declval&lt;U&amp;&gt;().~U() is well-formed in unevaluated context, value equals true. Otherwise, value equals false.<br />
2) same as 1), and additionally std::remove_all_extents&lt;T&gt;::type is either a non-class type or a class type with a trivial destructor.<br />
3) same as 1), but the destructor is noexcept.<br />
T shall be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T &gt;                                                                       (since C++17)</p>
<p>inline constexpr bool is_destructible_v = is_destructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                       (since C++17)</p>
<p>inline constexpr bool is_trivially_destructible_v = is_trivially_destructible&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                       (since C++17)</p>
<p>inline constexpr bool is_nothrow_destructible_v = is_nothrow_destructible&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is destructible, false otherwise<br />
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
<p>Because the C++ program terminates if a destructor throws an exception during stack unwinding (which usually cannot be predicted), all practical destructors are non-throwing even if they are not declared noexcept. All destructors found in the C++ standard library are non-throwing.<br />
Storage occupied by trivially destructible objects may_be_reused without calling the destructor. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;type_traits&gt;

struct Foo {
    std::string str;
    ~Foo() noexcept {};
};

struct Bar {
    ~Bar() = default;
};

int main()
{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;std::string is destructible? &quot;
              &lt;&lt; std::is_destructible&lt;std::string&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Foo is nothrow destructible? &quot;
              &lt;&lt; std::is_nothrow_destructible&lt;Foo&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Bar is trivally destructible? &quot;
              &lt;&lt; std::is_trivially_destructible&lt;Bar&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::string is destructible? true<br />
&nbsp;<wbr>&nbsp;Foo is nothrow destructible? true<br />
&nbsp;<wbr>&nbsp;Bar is trivally destructible? true</p>
<h2>See also</h2>
<p>is_constructible<br />
is_trivially_constructible<br />
is_nothrow_constructible checks if a type has a constructor for specific arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
has_virtual_destructor checks if a type has a virtual destructor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
