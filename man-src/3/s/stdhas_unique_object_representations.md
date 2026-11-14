---
title: "stdhas_unique_object_representations(3)"
name: "stdhas_unique_object_representations"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhas_unique_object_representations/"
description: "std::has_unique_object_representations – std::has_unique_object_representations"
---

<p>std::has_unique_object_representations &#8211; std::has_unique_object_representations</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 17)

        struct has_unique_object_representations;</code></pre>
<p>If T is TriviallyCopyable and if any two objects of type T with the same value have the same object_representation, provides the member constant value equal true. For any other type, value is false.<br />
For the purpose of this trait, two arrays have the same value if their elements have the same values, two non-union classes have the same value if their direct subobjects have the same value, and two unions have the same value if they have the same active member and the value of that member are the same.<br />
It is implementation-defined which scalar types satisfy this trait, but<br />
unsigned<br />
<i>(until C++20)</i> integer types that do not use padding bits are guaranteed to have unique object representations.<br />
The behavior is undefined if T is an incomplete type other than (possibly cv-qualified) void or array of unknown bound. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool has_unique_object_representations_v = has_unique_object_representations&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T has unique object representations , false otherwise<br />
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
<p>This trait was introduced to make it possible to determine whether a type can be correctly hashed by hashing its object representation as a byte array. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct foo

{
    char c;
    float f;
    short st;
    int i;
};
struct bar

{
    int a;
    int b;
};
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;Does foo have unique object representations? &quot;
              &lt;&lt; std::has_unique_object_representations_v&lt;foo&gt; &lt;&lt; '
'
              &lt;&lt; &quot;Does bar have unique object representations? &quot;
              &lt;&lt; std::has_unique_object_representations_v&lt;bar&gt; &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Does foo have unique object representations? false<br />
&nbsp;<wbr>&nbsp;Does bar have unique object representations? true</p>
<h2>See also</h2>
<p>is_standard_layout checks if a type is a standard-layout type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
hash hash function object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
