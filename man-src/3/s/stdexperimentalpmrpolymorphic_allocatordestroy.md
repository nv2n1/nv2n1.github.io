---
title: "stdexperimentalpmrpolymorphic_allocatordestroy(3)"
name: "stdexperimentalpmrpolymorphic_allocatordestroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrpolymorphic_allocatordestroy/"
description: "std::experimental::pmr::polymorphic_allocator<T>::destroy – std::experimental::pmr::polymorphic_allocator<T>::destroy"
---

<p>std::experimental::pmr::polymorphic_allocator&lt;T&gt;::destroy &#8211; std::experimental::pmr::polymorphic_allocator&lt;T&gt;::destroy</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U&gt;
(library fundamentals TS)

    void destroy(U *p);</code></pre>
<p>Destroys the object pointed to by p, as if by calling p-&gt;~U(). </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to the object being destroyed</p>
<h2>See also</h2>
<p>destroy destructs an object stored in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code> </p>
