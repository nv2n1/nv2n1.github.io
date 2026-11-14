---
title: "stdis_aggregate(3)"
name: "stdis_aggregate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_aggregate/"
description: "std::is_aggregate – std::is_aggregate"
---

<p>std::is_aggregate &#8211; std::is_aggregate</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 17)

        struct is_aggregate;</code></pre>
<p>Checks if T is an aggregate_type. The member constant value is equal to true if T is an aggregate type and false otherwise.<br />
The behavior is undefined if std::remove_all_extents_t&lt;T&gt; is an incomplete type other than (possibly cv-qualified) void. </p>
<h2>Template parameters</h2>
<p>T &#8211; a type to check </p>
<p>Helper variable template </p>
<p>template&lt; class T &gt; <i>(since C++17)</i><br />
inline constexpr bool is_aggregate_v = is_aggregate&lt;T&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if T is an aggregate type , false otherwise<br />
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
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;type_traits&gt;

#include &lt;new&gt;

#include &lt;utility&gt;
// constructs a T at the uninitialized memory pointed to by p

// using list-initialization for aggregates and non-list initialization otherwise

template &lt;class T, class... Args&gt;

T *construct(T *p, Args &amp;&amp;...args)
{
    if constexpr (std::is_aggregate_v&lt;T&gt;) {
        return ::new (static_cast&lt;void *&gt;(p)) T{std::forward&lt;Args&gt;(args)...};
    } else {
        return ::new (static_cast&lt;void *&gt;(p)) T(std::forward&lt;Args&gt;(args)...);
    }
}
struct A {
    int x, y;
};

struct B {
    B(int, const char *)
    {
    }
};
int main()
{
    std::aligned_union_t&lt;1, A, B&gt; storage;
    A *a = construct(reinterpret_cast&lt;A *&gt;(&amp;storage), 1, 2);
    B *b = construct(reinterpret_cast&lt;B *&gt;(&amp;storage), 1, &quot;hello&quot;);
}
</code></pre>
