---
title: "stduses_allocator(3)"
name: "stduses_allocator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduses_allocator/"
description: "std::uses_allocator<std::tuple> – std::uses_allocator<std::tuple>"
---

<p>std::uses_allocator&lt;std::tuple&gt; &#8211; std::uses_allocator&lt;std::tuple&gt;</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;tuple&gt;

    template &lt;class... Types, class Alloc&gt;
    (since C++ 11)

        struct uses_allocator&lt;std::tuple&lt;Types...&gt;, Alloc&gt; : std::true_type {
};</code></pre>
<p>This specialization of std::uses_allocator informs other library components that tuples support uses-allocator construction, even though they do not have a nested allocator_type.<br />
Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true<br />
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
<p>// Run this code<br />
&nbsp;<wbr>&nbsp;// myalloc is a stateful Allocator with a single-argument constructor<br />
&nbsp;<wbr>&nbsp;// that takes an int. It has no default constructor.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef std::vector&lt;int, myalloc&lt;int&gt;&gt; innervector_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef std::tuple&lt;int, innervector_t&gt; elem_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef std::scoped_allocator_adaptor&lt; myalloc&lt;elem_t&gt;, myalloc&lt;int&gt;&gt; Alloc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alloc a(1,2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::vector&lt;elem_t, Alloc&gt; v(a);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-v-resize/">v.resize</a>(1); // uses allocator #1 for elements of v<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::get&lt;1&gt;(v[0]).resize(10); // uses allocator #2 for innervector_t </p>
<h2>See also</h2>
<p>uses_allocator checks if the specified type supports uses-allocator construction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
