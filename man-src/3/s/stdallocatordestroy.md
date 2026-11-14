---
title: "stdallocatordestroy(3)"
name: "stdallocatordestroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocatordestroy/"
description: "std::allocator<T>::destroy – std::allocator<T>::destroy"
---

<p>std::allocator&lt;T&gt;::destroy &#8211; std::allocator&lt;T&gt;::destroy</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
void destroy( pointer p ); <i>(until C++11)</i><br />
template&lt; class U &gt; <i>(since C++11)</i><br />
void destroy( U* p ); (deprecated in C++17)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20)<br />
Calls the destructor of the object pointed to by p<br />
1) Calls ((T*)p)-&gt;~T()<br />
2) Calls p-&gt;~U() </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to the object that is going to be destroyed</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>See also</h2>
<p>destroy destructs an object stored in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code> </p>
