---
title: "stdis_assignablestdis_trivially_assignablestdis_nothrow_assignable(3)"
name: "stdis_assignablestdis_trivially_assignablestdis_nothrow_assignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_assignablestdis_trivially_assignablestdis_nothrow_assignable/"
description: "std::is_assignable,std::is_trivially_assignable,std::is_nothrow_assignable – std::is_assignable,std::is_trivially_assignable,std::is_nothrow_assignable"
---

<p>std::is_assignable,std::is_trivially_assignable,std::is_nothrow_assignable &#8211; std::is_assignable,std::is_trivially_assignable,std::is_nothrow_assignable</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, class U&gt;
    (1)(since C++ 11)

        struct is_assignable;

template &lt;class T, class U&gt;
(2)(since C++ 11)

    struct is_trivially_assignable;

template &lt;class T, class U&gt;
(3)(since C++ 11)

    struct is_nothrow_assignable;</code></pre>
<p>1) If the expression std::declval&lt;T&gt;() = std::declval&lt;U&gt;() is well-formed in unevaluated context, provides the member constant value equal true. Otherwise, value is false. Access_checks are performed as if from a context unrelated to either type.<br />
2) same as <code>(1)</code>, but the evaluation of the assignment expression will not call any operation that is not trivial. For the purposes of this check, a call to std::declval is considered trivial and not considered an odr-use of std::declval.<br />
3) same as <code>(1)</code>, but the evaluation of the assignment expression will not call any operation that is not noexcept.<br />
T and U shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.<br />
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.<br />
Helper variable templates template&lt; class T, class U &gt;                                                             (since C++17)</p>
<p>inline constexpr bool is_assignable_v = is_assignable&lt;T, U&gt;::value;</p>
<p>template&lt; class T, class U &gt;                                                             (since C++17)</p>
<p>inline constexpr bool is_trivially_assignable_v = is_trivially_assignable&lt;T, U&gt;::value;</p>
<p>template&lt; class T, class U &gt;                                                             (since C++17)</p>
<p>inline constexpr bool is_nothrow_assignable_v = is_nothrow_assignable&lt;T, U&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T is assignable from U , false otherwise<br />
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
<p>This trait does not check anything outside the immediate context of the assignment expression: if the use of T or U would trigger template specializations, generation of implicitly-defined special member functions etc, and those have errors, the actual assignment may not compile even if std::is_assignable&lt;T,U&gt;::value compiles and evaluates to true. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;type_traits&gt;

struct Ex1 {
    int n;
};

int main()
{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;int is assignable from int? &quot;
              &lt;&lt; std::is_assignable&lt;int, int&gt;::value &lt;&lt; '
' // 1 = 1; wouldn't compile
              &lt;&lt; &quot;int&amp; is assignable from int? &quot;
              &lt;&lt; std::is_assignable&lt;int &amp;, int&gt;::value &lt;&lt; '
' // int a; a = 1; works
              &lt;&lt; &quot;int is assignable from double? &quot;
              &lt;&lt; std::is_assignable&lt;int, double&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;int&amp; is nothrow assignable from double? &quot;
              &lt;&lt; std::is_nothrow_assignable&lt;int &amp;, double&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;string is assignable from double? &quot;
              &lt;&lt; std::is_assignable&lt;std::string, double&gt;::value &lt;&lt; '
'
              &lt;&lt; &quot;Ex1&amp; is trivially assignable from const Ex1&amp;? &quot;
              &lt;&lt; std::is_trivially_assignable&lt;Ex1 &amp;, const Ex1 &amp;&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;int is assignable from int? false<br />
&nbsp;<wbr>&nbsp;int&amp; is assignable from int? true<br />
&nbsp;<wbr>&nbsp;int is assignable from double? false<br />
&nbsp;<wbr>&nbsp;int&amp; is nothrow assignable from double? true<br />
&nbsp;<wbr>&nbsp;string is assignable from double? true<br />
&nbsp;<wbr>&nbsp;Ex1&amp; is trivially assignable from const Ex1&amp;? true</p>
<h2>See also</h2>
<p>is_copy_assignable<br />
is_trivially_copy_assignable<br />
is_nothrow_copy_assignable checks if a type has a copy assignment operator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
is_move_assignable<br />
is_trivially_move_assignable<br />
is_nothrow_move_assignable checks if a type has a move assignment operator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
