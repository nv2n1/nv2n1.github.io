---
title: "stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_cast(3)"
name: "stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_cast/"
---

std::experimental::static_pointer_cast,std::experimental::dynamic_pointer_cast, - std::experimental::static_pointer_cast,std::experimental::dynamic_pointer_cast,

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class U&gt;
(library fundamentals

     std::experimental::shared_ptr&lt;T&gt;
         static_pointer_cast((1)TS)

             const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(library fundamentals

     std::experimental::shared_ptr&lt;T&gt;
         dynamic_pointer_cast((2)TS)

             const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(library fundamentals

     std::experimental::shared_ptr&lt;T&gt;
         const_pointer_cast(const(3) TS)

             std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(library fundamentals

     std::experimental::shared_ptr&lt;T&gt;
         reinterpret_pointer_cast((4)TS)

             const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;</code></pre> 
Creates a new instance of std::experimental::shared_ptr whose stored pointer is 
obtained from r's stored pointer using a cast expression. If r is empty, so is the 
new shared_ptr&nbsp;<wbr>(but its stored pointer is not necessarily null). 
Otherwise, the new shared_ptr will share ownership with r, except that it is empty 
if the dynamic_cast performed by dynamic_pointer_cast returns a null pointer. 
Let Y be typename std::experimental::shared_ptr&lt;T&gt;::element_type, then the resulting 
std::experimental::shared_ptr's stored pointer will be obtained by calling&nbsp;<wbr>(in 
respective order): 
1)&nbsp;<wbr>static_cast&lt;Y*&gt;(r.get()). 
2)&nbsp;<wbr>dynamic_cast&lt;Y*&gt;(r.get())&nbsp;<wbr>(If the result of the dynamic_cast is a null pointer 
value, the returned shared_ptr will be empty). 
3)&nbsp;<wbr>const_cast&lt;Y*&gt;(r.get()). 
4)&nbsp;<wbr>reinterpret_cast&lt;Y*&gt;(r.get()). 
The behavior of these functions is undefined unless the corresponding cast from U* 
to T*&nbsp;<wbr>is well formed: 
1)&nbsp;<wbr>The behavior is undefined unless static_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed. 
2)&nbsp;<wbr>The behavior is undefined unless dynamic_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed. 
3)&nbsp;<wbr>The behavior is undefined unless const_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well formed. 
4)&nbsp;<wbr>The behavior is undefined unless reinterpret_cast&lt;T*&gt;((U*)nullptr)&nbsp;<wbr>is well 
formed. 

<h2>Parameters</h2>

r - The pointer to convert

<h2>Example</h2>

&nbsp;<wbr>This section is incomplete 
&nbsp;<wbr>Reason: no example 

<h2>See also</h2>

constructor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>constructs new shared_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i> 
static_pointer_cast 
dynamic_pointer_cast&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applies static_cast, dynamic_cast, const_cast, or 
const_pointer_cast&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reinterpret_cast to the stored pointer 
reinterpret_pointer_cast&nbsp;<wbr><i>(function template)</i> 
<i>(C++17)</i> 
