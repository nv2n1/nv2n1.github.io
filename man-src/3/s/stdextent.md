---
title: "stdextent(3)"
name: "stdextent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdextent/"
description: "std::extent – std::extent"
---

<p>std::extent &#8211; std::extent</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, unsigned N = 0&gt;
    (since C++ 11)

        struct extent;</code></pre>
<p>If T is an array type, provides the member constant value equal to the number of elements along the Nth dimension of the array, if N is in [0, std::rank&lt;T&gt;::value). For any other type, or if T is array of unknown bound along its first dimension and N is 0, value is 0.<br />
Helper variable template template&lt; class T, unsigned N = 0 &gt;                           (since C++17)</p>
<p>inline constexpr std::size_t extent_v = extent&lt;T, N&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value the number of elements along the Nth dimension of T<br />
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
<p>&nbsp;<wbr>&nbsp;template&lt;class T, unsigned N = 0&gt;<br />
&nbsp;<wbr>&nbsp;struct extent : std::integral_constant&lt;std::size_t, 0&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct extent&lt;T[], 0&gt; : std::integral_constant&lt;std::size_t, 0&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, unsigned N&gt;<br />
&nbsp;<wbr>&nbsp;struct extent&lt;T[], N&gt; : std::extent&lt;T, N-1&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, std::size_t I&gt;<br />
&nbsp;<wbr>&nbsp;struct extent&lt;T[I], 0&gt; : std::integral_constant&lt;std::size_t, I&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T, std::size_t I, unsigned N&gt;<br />
&nbsp;<wbr>&nbsp;struct extent&lt;T[I], N&gt; : std::extent&lt;T, N-1&gt; {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    std::cout &lt;&lt; std::extent&lt;int[3]&gt;::value &lt;&lt; '
'; //&lt; default dimension is 0
    std::cout &lt;&lt; std::extent&lt;int[3][4], 0&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::extent&lt;int[3][4], 1&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::extent&lt;int[3][4], 2&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::extent&lt;int[]&gt;::value &lt;&lt; '
';
    const auto ext = std::extent&lt;int[9]&gt;{};
    std::cout &lt;&lt; ext &lt;&lt; '
'; //&lt; implicit conversion to std::size_t
    const int ints[] = {1, 2, 3, 4};
    std::cout &lt;&lt; std::extent&lt;decltype(ints)&gt;::value &lt;&lt; '
'; //&lt; array size
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;3<br />
&nbsp;<wbr>&nbsp;3<br />
&nbsp;<wbr>&nbsp;4<br />
&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;9<br />
&nbsp;<wbr>&nbsp;4</p>
<h2>See also</h2>
<p>is_array checks if a type is an array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
rank obtains the number of dimensions of an array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_extent removes one extent from the given array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_all_extents removes all extents from the given array type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
