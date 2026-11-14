---
title: "stdtuple_sizestdarray(3)"
name: "stdtuple_sizestdarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple_sizestdarray/"
description: "std::tuple_size(std::array) – std::tuple_size(std::array)"
---

<p>std::tuple_size(std::array) &#8211; std::tuple_size(std::array)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;array&gt;

template&lt; class T, size_t N &gt;

class tuple_size&lt; array&lt;T, N&gt; &gt; :   (1) (since C++11)

public integral_constant&lt;size_t, N&gt;

{ };</code></pre>
<p>Provides access to the number of elements in an std::array as a compile-time constant expression.<br />
Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value N, the number of elements in the array<br />
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
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;array&gt;
template &lt;class T&gt;

void test(T t)

{
    int a[std::tuple_size&lt;T&gt;::value]; // can be used at compile time
    std::cout &lt;&lt; std::tuple_size&lt;T&gt;::value &lt;&lt; '
';
}
int main()

{
    std::array&lt;float, 3&gt; arr;
    test(arr);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;3</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of tuple at compile time<br />
tuple_size <i>(class template specialization)</i> </p>
