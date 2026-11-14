---
title: "stdis_copy_assignablestdis_trivially_copy_assignable(3)"
name: "stdis_copy_assignablestdis_trivially_copy_assignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_copy_assignablestdis_trivially_copy_assignable/"
description: "std::is_copy_assignable,std::is_trivially_copy_assignable, – std::is_copy_assignable,std::is_trivially_copy_assignable,"
---

<p>std::is_copy_assignable,std::is_trivially_copy_assignable, &#8211; std::is_copy_assignable,std::is_trivially_copy_assignable,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct is_copy_assignable;

template &lt;class T&gt;
(2)(since C++ 11)

    struct is_trivially_copy_assignable;

template &lt;class T&gt;
(3)(since C++ 11)

    struct is_nothrow_copy_assignable;</code></pre>
<p>1)&nbsp;<wbr>If T is not a referenceable type&nbsp;<wbr>(i.e., possibly cv-qualified void or a function<br />
type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value<br />
equal to false. Otherwise, provides a member constant value equal to<br />
std::is_assignable&lt;T&amp;, const T&amp;&gt;::value.<br />
2)&nbsp;<wbr>Same as 1), but uses std::is_trivially_assignable&lt;T&amp;, const T&amp;&gt;<br />
3)&nbsp;<wbr>Same as 1), but uses std::is_nothrow_assignable&lt;T&amp;, const T&amp;&gt;<br />
T shall be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of unknown<br />
bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates template&lt; class T &gt;</p>
<p>inline constexpr bool is_copy_assignable_v =                           (since C++17)</p>
<p>is_copy_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_trivially_copy_assignable_v =                 (since C++17)</p>
<p>is_trivially_copy_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_nothrow_copy_assignable_v =                   (since C++17)</p>
<p>is_nothrow_copy_assignable&lt;T&gt;::value; Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if T is copy-assignable, false otherwise<br />
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
<p>template&lt; class T&gt; struct is_copy_assignable<br />
&nbsp;<wbr>: std::is_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_lvalue_reference&lt;const T&gt;::type&gt;&nbsp;<wbr>{}; </p>
<p> template&lt; class T&gt; struct is_trivially_copy_assignable<br />
&nbsp;<wbr>: std::is_trivially_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_lvalue_reference&lt;const T&gt;::type&gt;&nbsp;<wbr>{}; </p>
<p> template&lt; class T&gt; struct is_nothrow_copy_assignable<br />
&nbsp;<wbr>: std::is_nothrow_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_lvalue_reference&lt;const T&gt;::type&gt;&nbsp;<wbr>{};</p>
<h2>Notes</h2>
<p>The trait std::is_copy_assignable is less strict than CopyAssignable because it does<br />
not check the type of the result of the assignment&nbsp;<wbr>(which, for a CopyAssignable<br />
type, must be an lvalue of type T)&nbsp;<wbr>and does not check the semantic requirement that<br />
the argument expression remains unchanged. It also does not check that T satisfies<br />
MoveAssignable, which is required of all CopyAssignable types. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;type_traits&gt;

struct Foo {
    int n;
};

int main()
{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;Foo is trivially copy-assignable? &quot;
              &lt;&lt; std::is_trivially_copy_assignable&lt;Foo&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;int[2] is copy-assignable? &quot;
              &lt;&lt; std::is_copy_assignable&lt;int[2]&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;int is nothrow copy-assignable? &quot;
              &lt;&lt; std::is_nothrow_copy_assignable&lt;int&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>Foo is trivially copy-assignable?&nbsp;<wbr>true<br />
&nbsp;<wbr>int[2]&nbsp;<wbr>is copy-assignable?&nbsp;<wbr>false<br />
&nbsp;<wbr>int is nothrow copy-assignable?&nbsp;<wbr>true</p>
<h2>See also</h2>
<p>is_assignable<br />
is_trivially_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a assignment operator for a<br />
is_nothrow_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specific argument<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_assignable<br />
is_trivially_move_assignable<br />
is_nothrow_move_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a move assignment operator<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
