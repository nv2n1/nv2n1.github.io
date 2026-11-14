---
title: "stdis_move_assignablestdis_trivially_move_assignable(3)"
name: "stdis_move_assignablestdis_trivially_move_assignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_move_assignablestdis_trivially_move_assignable/"
description: "std::is_move_assignable,std::is_trivially_move_assignable, – std::is_move_assignable,std::is_trivially_move_assignable,"
---

<p>std::is_move_assignable,std::is_trivially_move_assignable, &#8211; std::is_move_assignable,std::is_trivially_move_assignable,</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct is_move_assignable;

template &lt;class T&gt;
(2)(since C++ 11)

    struct is_trivially_move_assignable;

template &lt;class T&gt;
(3)(since C++ 11)

    struct is_nothrow_move_assignable;</code></pre>
<p>1)&nbsp;<wbr>If T is not a referenceable type&nbsp;<wbr>(i.e., possibly cv-qualified void or a function<br />
type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value<br />
equal to false. Otherwise, provides a member constant value equal to<br />
std::is_assignable&lt;T&amp;, T&amp;&amp;&gt;::value.<br />
2)&nbsp;<wbr>Same as 1), but uses std::is_trivially_assignable&lt;T&amp;, T&amp;&amp;&gt;<br />
3)&nbsp;<wbr>Same as 1), but uses std::is_nothrow_assignable&lt;T&amp;, T&amp;&amp;&gt;<br />
T shall be a complete type,&nbsp;<wbr>(possibly cv-qualified)&nbsp;<wbr>void, or an array of unknown<br />
bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an<br />
incomplete type, and that instantiation could yield a different result if that type<br />
were hypothetically completed, the behavior is undefined.<br />
&nbsp;<wbr>&nbsp;<wbr>Helper variable templates template&lt; class T &gt;</p>
<p>inline constexpr bool is_move_assignable_v =                           (since C++17)</p>
<p>is_move_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_trivially_move_assignable_v =                 (since C++17)</p>
<p>is_trivially_move_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;</p>
<p>inline constexpr bool is_nothrow_move_assignable_v =                   (since C++17)</p>
<p>is_nothrow_move_assignable&lt;T&gt;::value; Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>true if T is move-assignable, false otherwise<br />
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
struct is_move_assignable<br />
&nbsp;<wbr>: std::is_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_rvalue_reference&lt;T&gt;::type&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;&nbsp;<wbr>class T&gt;<br />
struct is_trivially_move_assignable<br />
&nbsp;<wbr>: std::is_trivially_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_rvalue_reference&lt;T&gt;::type&gt;&nbsp;<wbr>{}; </p>
<p>template&lt;&nbsp;<wbr>class T&gt;<br />
struct is_nothrow_move_assignable<br />
&nbsp;<wbr>: std::is_nothrow_assignable&lt;&nbsp;<wbr>typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>typename std::add_rvalue_reference&lt;T&gt;::type&gt;&nbsp;<wbr>{};</p>
<h2>Notes</h2>
<p>The trait std::is_move_assignable is less strict than MoveAssignable because it does<br />
not check the type of the result of the assignment&nbsp;<wbr>(which, for a MoveAssignable<br />
type, must be T&amp;), nor the semantic requirement that the target&#8217;s value after the<br />
assignment is equivalent to the source&#8217;s value before the assignment.<br />
The type does not have to implement a move assignment operator in order to satisfy<br />
this trait;&nbsp;<wbr>see MoveAssignable for details. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;type_traits&gt;

struct Foo {
    int n;
};

struct NoMove {
    // prevents implicit declaration of default move assignment operator
    // however, the class is still move-assignable because its
    // copy assignment operator can bind to an rvalue argument
    NoMove &amp;operator=(const NoMove &amp;)
    {
        return *this;
    }
};

int main()
{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;std::string is nothrow move-assignable? &quot;
              &lt;&lt; std::is_nothrow_move_assignable&lt;std::string&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;int[2] is move-assignable? &quot;
              &lt;&lt; std::is_move_assignable&lt;int[2]&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Foo is trivally move-assignable? &quot;
              &lt;&lt; std::is_trivially_move_assignable&lt;Foo&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;NoMove is move-assignable? &quot;
              &lt;&lt; std::is_move_assignable&lt;NoMove&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;NoMove is nothrow move-assignable? &quot;
              &lt;&lt; std::is_nothrow_move_assignable&lt;NoMove&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>std::string is nothrow move-assignable?&nbsp;<wbr>true<br />
&nbsp;<wbr>int[2]&nbsp;<wbr>is move-assignable?&nbsp;<wbr>false<br />
&nbsp;<wbr>Foo is trivially move-assignable?&nbsp;<wbr>true<br />
&nbsp;<wbr>NoMove is move-assignable?&nbsp;<wbr>true<br />
&nbsp;<wbr>NoMove is nothrow move-assignable?&nbsp;<wbr>false</p>
<h2>See also</h2>
<p>is_assignable<br />
is_trivially_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a assignment operator for a<br />
is_nothrow_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specific argument<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_copy_assignable<br />
is_trivially_copy_assignable<br />
is_nothrow_copy_assignable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>checks if a type has a copy assignment operator<br />
<i>(C++11)</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
