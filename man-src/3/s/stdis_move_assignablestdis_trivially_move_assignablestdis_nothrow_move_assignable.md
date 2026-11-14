---
title: "stdis_move_assignablestdis_trivially_move_assignablestdis_nothrow_move_assignable(3)"
name: "stdis_move_assignablestdis_trivially_move_assignablestdis_nothrow_move_assignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_move_assignablestdis_trivially_move_assignablestdis_nothrow_move_assignable/"
description: "std::is_move_assignable,std::is_trivially_move_assignable,std::is_nothrow_move_assignable – std::is_move_assignable,std::is_trivially_move_assignable,std::is_nothrow_move_assignable"
---

<p>std::is_move_assignable,std::is_trivially_move_assignable,std::is_nothrow_move_assignable &#8211; std::is_move_assignable,std::is_trivially_move_assignable,std::is_nothrow_move_assignable</p>
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
<p>1) If T is not a referenceable type (i.e., possibly cv-qualified void or a function type with a cv-qualifier-seq or a ref-qualifier), provides a member constant value equal to false. Otherwise, provides a member constant value equal to std::is_assignable&lt;T&amp;, T&amp;&amp;&gt;::value.<br />
2) Same as 1), but uses std::is_trivially_assignable&lt;T&amp;, T&amp;&amp;&gt;<br />
3) Same as 1), but uses std::is_nothrow_assignable&lt;T&amp;, T&amp;&amp;&gt;<br />
T shall be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T &gt;                                                                             (since C++17)</p>
<p>inline constexpr bool is_move_assignable_v = is_move_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                             (since C++17)</p>
<p>inline constexpr bool is_trivially_move_assignable_v = is_trivially_move_assignable&lt;T&gt;::value;</p>
<p>template&lt; class T &gt;                                                                             (since C++17)</p>
<p>inline constexpr bool is_nothrow_move_assignable_v = is_nothrow_move_assignable&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is move-assignable, false otherwise<br />
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
&nbsp;<wbr>&nbsp;struct is_move_assignable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::is_assignable&lt; typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_rvalue_reference&lt;T&gt;::type&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_trivially_move_assignable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::is_trivially_assignable&lt; typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_rvalue_reference&lt;T&gt;::type&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt; class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_nothrow_move_assignable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::is_nothrow_assignable&lt; typename std::add_lvalue_reference&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_rvalue_reference&lt;T&gt;::type&gt; {};</p>
<h2>Notes</h2>
<p>The trait std::is_move_assignable is less strict than MoveAssignable because it does not check the type of the result of the assignment (which, for a MoveAssignable type, must be T&amp;), nor the semantic requirement that the target&#8217;s value after the assignment is equivalent to the source&#8217;s value before the assignment.<br />
The type does not have to implement a move_assignment_operator in order to satisfy this trait; see MoveAssignable for details. </p>
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
<p>&nbsp;<wbr>&nbsp;std::string is nothrow move-assignable? true<br />
&nbsp;<wbr>&nbsp;int[2] is move-assignable? false<br />
&nbsp;<wbr>&nbsp;Foo is trivially move-assignable? true<br />
&nbsp;<wbr>&nbsp;NoMove is move-assignable? true<br />
&nbsp;<wbr>&nbsp;NoMove is nothrow move-assignable? false</p>
<h2>See also</h2>
<p>is_assignable<br />
is_trivially_assignable<br />
is_nothrow_assignable checks if a type has a assignment operator for a specific argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_copy_assignable<br />
is_trivially_copy_assignable<br />
is_nothrow_copy_assignable checks if a type has a copy assignment operator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
