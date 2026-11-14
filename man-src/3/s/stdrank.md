---
title: "stdrank(3)"
name: "stdrank"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrank/"
description: "std::rank – std::rank"
---

<p>std::rank &#8211; std::rank</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct rank;</code></pre>
<p>If T is an array type, provides the member constant value equal to the number of dimensions of the array. For any other type, value is 0.<br />
Helper variable template template&lt; class T &gt;                                    (since C++17)</p>
<p>inline constexpr std::size_t rank_v = rank&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value the number of dimensions of T or zero<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to std::size_t, returns value<br />
operator std::size_t <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type std::size_t<br />
type std::integral_constant&lt;std::size_t, value&gt;</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct rank : public std::integral_constant&lt;std::size_t, 0&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct rank&lt;T[]&gt; : public std::integral_constant&lt;std::size_t, rank&lt;T&gt;::value + 1&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, std::size_t N&gt;<br />
&nbsp;<wbr>&nbsp;struct rank&lt;T[N]&gt; : public std::integral_constant&lt;std::size_t, rank&lt;T&gt;::value + 1&gt; {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    std::cout &lt;&lt; std::rank&lt;int&gt;{} &lt;&lt; &quot;

&quot;;
    std::cout &lt;&lt; std::rank&lt;int[5]&gt;{} &lt;&lt; '
';
    std::cout &lt;&lt; std::rank&lt;int[5][5]&gt;{} &lt;&lt; '
';
    std::cout &lt;&lt; std::rank&lt;int[][5][5]&gt;{} &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0 </p>
<p>&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;3</p>
<h2>See also</h2>
<p>is_array checks if a type is an array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
extent obtains the size of an array type along a specified dimension<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_extent removes one extent from the given array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_all_extents removes all extents from the given array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
