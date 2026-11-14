---
title: "stdis_constructiblestdis_trivially_constructiblestdis_nothrow_constructible(3)"
name: "stdis_constructiblestdis_trivially_constructiblestdis_nothrow_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_constructiblestdis_trivially_constructiblestdis_nothrow_constructible/"
description: "std::is_constructible,std::is_trivially_constructible,std::is_nothrow_constructible – std::is_constructible,std::is_trivially_constructible,std::is_nothrow_constructible"
---

<p>std::is_constructible,std::is_trivially_constructible,std::is_nothrow_constructible &#8211; std::is_constructible,std::is_trivially_constructible,std::is_nothrow_constructible</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, class... Args&gt;
    (1)(since C++ 11)

        struct is_constructible;

template &lt;class T, class... Args&gt;
(2)(since C++ 11)

    struct is_trivially_constructible;

template &lt;class T, class... Args&gt;
(3)(since C++ 11)

    struct is_nothrow_constructible;</code></pre>
<p>1) If T is an object or reference type and the variable definition T obj(std::declval&lt;Args&gt;()&#8230;); is well-formed, provides the member constant value equal to true. In all other cases, value is false.<br />
For the purposes of this check, the variable definition is never interpreted as a function declaration, and the use of std::declval is not considered an odr-use. Access_checks are performed as if from a context unrelated to T and any of the types in Args. Only the validity of the immediate context of the variable definition is considered.<br />
2) same as 1), but the variable definition does not call any operation that is not trivial. For the purposes of this check, the call to std::declval is considered trivial.<br />
3) same as 1), but the variable definition is noexcept.<br />
T and all types in the parameter pack Args shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T, class&#8230; Args &gt;                                                                   (since C++17)</p>
<p>inline constexpr bool is_constructible_v = is_constructible&lt;T, Args&#8230;&gt;::value;</p>
<p>template&lt; class T, class&#8230; Args &gt;                                                                   (since C++17)</p>
<p>inline constexpr bool is_trivially_constructible_v = is_trivially_constructible&lt;T, Args&#8230;&gt;::value;</p>
<p>template&lt; class T, class&#8230; Args &gt;                                                                   (since C++17)</p>
<p>inline constexpr bool is_nothrow_constructible_v = is_nothrow_constructible&lt;T, Args&#8230;&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is constructible from Args&#8230; , false otherwise<br />
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
<p>In many implementations, is_nothrow_constructible also checks if the destructor throws because it is effectively noexcept(T(arg)). Same applies to is_trivially_constructible, which, in these implementations, also requires that the destructor is trivial: GCC_bug_51452 LWG_issue_2116. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class Foo
{
    int v1;
    double v2;

  public:
    Foo(int n)
        : v1(n), v2()
    {
    }
    Foo(int n, double f) noexcept
        : v1(n), v2(f)
    {
    }
};
int main()
{
    std::cout &lt;&lt; &quot;Foo is ...
&quot;
              &lt;&lt; std::boolalpha
              &lt;&lt; &quot;	Trivially-constructible from const Foo&amp;? &quot;
              &lt;&lt; std::is_trivially_constructible&lt;Foo, const Foo &amp;&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;	Trivially-constructible from int? &quot;
              &lt;&lt; std::is_trivially_constructible&lt;Foo, int&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;	Constructible from int? &quot;
              &lt;&lt; std::is_constructible&lt;Foo, int&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;	Nothrow-constructible from int? &quot;
              &lt;&lt; std::is_nothrow_constructible&lt;Foo, int&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;	Nothrow-constructible from int and double? &quot;
              &lt;&lt; std::is_nothrow_constructible&lt;Foo, int, double&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Foo is &#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Trivially-constructible from const Foo&amp;? true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Trivially-constructible from int? false<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Constructible from int? true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Nothrow-constructible from int? false<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Nothrow-constructible from int and double? true</p>
<h2>See also</h2>
<p>is_default_constructible<br />
is_trivially_default_constructible<br />
is_nothrow_default_constructible checks if a type has a default constructor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_copy_constructible<br />
is_trivially_copy_constructible<br />
is_nothrow_copy_constructible checks if a type has a copy constructor<br />
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
