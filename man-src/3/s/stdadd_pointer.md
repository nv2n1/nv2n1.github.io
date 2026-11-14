---
title: "stdadd_pointer(3)"
name: "stdadd_pointer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadd_pointer/"
description: "std::add_pointer – std::add_pointer"
---

<p>std::add_pointer &#8211; std::add_pointer</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct add_pointer;</code></pre>
<p>If T is a reference type, then provides the member typedef type which is a pointer to the referred type.<br />
Otherwise, if T names an object type, a function type that is not cv- or ref-qualified, or a (possibly cv-qualified) void type, provides the member typedef type which is the type T*.<br />
Otherwise (if T is a cv- or ref-qualified function type), provides the member typedef type which is the type T. </p>
<h2>Member types</h2>
<p>Name Definition<br />
type pointer to T or to the type referenced by T</p>
<h2>Helper types</h2>
<p>template&lt; class T &gt; <i>(since C++14)</i><br />
using add_pointer_t = typename add_pointer&lt;T&gt;::type;</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;namespace detail { </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct type_identity { using type = T; }; // or use std::type_identity <i>(since C++20)</i> </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_pointer(int) -&gt; type_identity&lt;typename std::remove_reference&lt;T&gt;::type*&gt;;<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;auto try_add_pointer(&#8230;) -&gt; type_identity&lt;T&gt;; </p>
<p>&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct add_pointer : decltype(detail::try_add_pointer&lt;T&gt;<code>(0)</code>) {};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    int i = 123;
    int &amp;ri = i;
    typedef std::add_pointer&lt;decltype(i)&gt;::type IntPtr;
    typedef std::add_pointer&lt;decltype(ri)&gt;::type IntPtr2;
    IntPtr pi = &amp;i;
    std::cout &lt;&lt; &quot;i = &quot; &lt;&lt; i &lt;&lt; &quot;
&quot;;
    std::cout &lt;&lt; &quot;*pi = &quot; &lt;&lt; *pi &lt;&lt; &quot;
&quot;;
    static_assert(std::is_pointer&lt;IntPtr&gt;::value, &quot;IntPtr should be a pointer&quot;);
    static_assert(std::is_same&lt;IntPtr, int *&gt;::value, &quot;IntPtr should be a pointer to int&quot;);
    static_assert(std::is_same&lt;IntPtr2, IntPtr&gt;::value, &quot;IntPtr2 should be equal to IntPtr&quot;);
    typedef std::remove_pointer&lt;IntPtr&gt;::type IntAgain;
    IntAgain j = i;
    std::cout &lt;&lt; &quot;j = &quot; &lt;&lt; j &lt;&lt; &quot;
&quot;;
    static_assert(!std::is_pointer&lt;IntAgain&gt;::value, &quot;IntAgain should not be a pointer&quot;);
    static_assert(std::is_same&lt;IntAgain, int&gt;::value, &quot;IntAgain should be equal to int&quot;);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;i = 123<br />
&nbsp;<wbr>&nbsp;*pi = 123<br />
&nbsp;<wbr>&nbsp;j = 123 </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2101 C++11 std::add_pointer was required to produce Produces cv-/ref-qualified function types themselves.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to cv-/ref-qualified function types.</p>
<h2>See also</h2>
<p>is_pointer checks if a type is a pointer type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
remove_pointer removes a pointer from the given type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
