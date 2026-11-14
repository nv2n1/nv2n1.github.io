---
title: "stdis_same(3)"
name: "stdis_same"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_same/"
description: "std::is_same – std::is_same"
---

<p>std::is_same &#8211; std::is_same</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T, class U&gt;
    (since C++ 11)

        struct is_same;</code></pre>
<p>If T and U name the same type (including const/volatile qualifications), provides the member constant value equal to true. Otherwise value is false.<br />
Commutativity is satisfied, i.e. for any two types T and U, is_same&lt;T, U&gt;::value == true if and only if is_same&lt;U, T&gt;::value == true.<br />
Helper variable template template&lt; class T, class U &gt;                             (since C++17)</p>
<p>inline constexpr bool is_same_v = is_same&lt;T, U&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if T and U is the same type , false otherwise<br />
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
<p>&nbsp;<wbr>&nbsp;template&lt;class T, class U&gt;<br />
&nbsp;<wbr>&nbsp;struct is_same : std::false_type {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_same&lt;T, T&gt; : std::true_type {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;cstdint&gt;
void print_separator()

{
    std::cout &lt;&lt; &quot;-----
&quot;;
}
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    // some implementation-defined facts
    std::cout &lt;&lt; std::is_same&lt;int, std::int32_t&gt;::value &lt;&lt; '
';
    // usually true if 'int' is 32 bit
    std::cout &lt;&lt; std::is_same&lt;int, std::int64_t&gt;::value &lt;&lt; '
';
    // possibly true if ILP64 data model is used
    print_separator();
    // 'float' is never an integral type
    std::cout &lt;&lt; std::is_same&lt;float, std::int32_t&gt;::value &lt;&lt; '
'; // false
    print_separator();
    // 'int' is implicitly 'signed'
    std::cout &lt;&lt; std::is_same&lt;int, int&gt;::value &lt;&lt; &quot;
&quot;;          // true
    std::cout &lt;&lt; std::is_same&lt;int, unsigned int&gt;::value &lt;&lt; &quot;
&quot;; // false
    std::cout &lt;&lt; std::is_same&lt;int, signed int&gt;::value &lt;&lt; &quot;
&quot;;   // true
    print_separator();
    // unlike other types, 'char' is neither 'unsigned' nor 'signed'
    std::cout &lt;&lt; std::is_same&lt;char, char&gt;::value &lt;&lt; &quot;
&quot;;          // true
    std::cout &lt;&lt; std::is_same&lt;char, unsigned char&gt;::value &lt;&lt; &quot;
&quot;; // false
    std::cout &lt;&lt; std::is_same&lt;char, signed char&gt;::value &lt;&lt; &quot;
&quot;;   // false
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false</p>
<h2>See also</h2>
<p>is_integral checks if a type is an integral type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_signed makes the given integral type signed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
make_unsigned makes the given integral type unsigned<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
