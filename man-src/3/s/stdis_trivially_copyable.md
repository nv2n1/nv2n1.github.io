---
title: "stdis_trivially_copyable(3)"
name: "stdis_trivially_copyable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_trivially_copyable/"
description: "std::is_trivially_copyable – std::is_trivially_copyable"
---

<p>std::is_trivially_copyable &#8211; std::is_trivially_copyable</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_trivially_copyable;</code></pre>
<p>If T is a TriviallyCopyable type, provides the member constant value equal true. For any other type, value is false.<br />
The only trivially copyable types are scalar types, trivially copyable classes, and arrays of such types/classes (possibly const-qualified, but not volatile-qualified).<br />
The behavior is undefined if std::remove_all_extents_t&lt;T&gt; is an incomplete type and not (possibly cv-qualified) void. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_trivially_copyable_v = is_trivially_copyable&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is a trivially copyable type , false otherwise<br />
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
<p>Objects of trivially-copyable types are the only C++ objects that may be safely copied with std::memcpy or serialized to/from binary files with std::ofstream::write()/std::ifstream::read().<br />
In general, for any trivially copyable type T and an object obj1 of T, the underlying bytes of obj1 can be copied (e.g. by means of std::memcpy or std::memmove) into an array of char, unsigned char or std::byte or into obj2, a distinct object of T. Neither obj1 nor obj2 may be a potentially-overlapping subobject.<br />
If the underlying bytes of obj1 is copied into such an array, and then the resulting content is copied back into obj1, obj1 will hold its original value. If the underlying bytes of obj1 are copied into obj2, obj2 will hold obj1&#8217;s value. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
struct A {
    int m;
};
struct B {
    B(B const &amp;)
    {
    }
};
struct C {
    virtual void foo();
};
struct D {
    int m;
    D(D const &amp;) = default; // -&gt; trivially copyable
    D(int x)
        : m(x + 1)
    {
    }
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::is_trivially_copyable&lt;A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_trivially_copyable&lt;B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_trivially_copyable&lt;C&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::is_trivially_copyable&lt;D&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
<p>is_trivial checks if a type is trivial<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
