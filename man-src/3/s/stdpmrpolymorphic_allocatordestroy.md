---
title: "stdpmrpolymorphic_allocatordestroy(3)"
name: "stdpmrpolymorphic_allocatordestroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrpolymorphic_allocatordestroy/"
description: "std::pmr::polymorphic_allocator<T>::destroy – std::pmr::polymorphic_allocator<T>::destroy"
---

<p>std::pmr::polymorphic_allocator&lt;T&gt;::destroy &#8211; std::pmr::polymorphic_allocator&lt;T&gt;::destroy</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U&gt;
(since C++ 17)

    void destroy(U *p);</code></pre>
<p>Destroys the object pointed to by p, as if by calling p-&gt;~U(). </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to the object being destroyed</p>
<h2>See also</h2>
<p>destroy destructs an object stored in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code> </p>
