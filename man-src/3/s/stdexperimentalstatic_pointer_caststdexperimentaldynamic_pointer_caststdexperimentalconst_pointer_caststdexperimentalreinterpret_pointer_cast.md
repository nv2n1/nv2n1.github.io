---
title: "stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_caststdexperimentalconst_pointer_caststdexperimentalreinterpret_pointer_cast(3)"
name: "stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_caststdexperimentalconst_pointer_caststdexperimentalreinterpret_pointer_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalstatic_pointer_caststdexperimentaldynamic_pointer_caststdexperimentalconst_pointer_caststdexperimentalreinterpret_pointer_cast/"
---

std::experimental::static_pointer_cast,std::experimental::dynamic_pointer_cast,std::experimental::const_pointer_cast,std::experimental::reinterpret_pointer_cast - std::experimental::static_pointer_cast,std::experimental::dynamic_pointer_cast,std::experimental::const_pointer_cast,std::experimental::reinterpret_pointer_cast

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class U&gt;
(1)(library fundamentals TS)

    std::experimental::shared_ptr&lt;T&gt; static_pointer_cast(const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(2)(library fundamentals TS)

    std::experimental::shared_ptr&lt;T&gt; dynamic_pointer_cast(const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(3)(library fundamentals TS)

    std::experimental::shared_ptr&lt;T&gt; const_pointer_cast(const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;

template &lt;class T, class U&gt;
(4)(library fundamentals TS)

    std::experimental::shared_ptr&lt;T&gt; reinterpret_pointer_cast(const std::experimental::shared_ptr&lt;U&gt; &amp;r) noexcept;</code></pre> 
Creates a new instance of std::experimental::shared_ptr whose stored pointer is obtained from r's stored pointer using a cast expression. If r is empty, so is the new shared_ptr (but its stored pointer is not necessarily null). 
Otherwise, the new shared_ptr will share ownership with r, except that it is empty if the dynamic_cast performed by dynamic_pointer_cast returns a null pointer. 
Let Y be typename std::experimental::shared_ptr&lt;T&gt;::element_type, then the resulting std::experimental::shared_ptr's stored pointer will be obtained by calling (in respective order): 
1) static_cast&lt;Y*&gt;(r.get()). 
2) dynamic_cast&lt;Y*&gt;(r.get()) (If the result of the dynamic_cast is a null pointer value, the returned shared_ptr will be empty). 
3) const_cast&lt;Y*&gt;(r.get()). 
4) reinterpret_cast&lt;Y*&gt;(r.get()). 
The behavior of these functions is undefined unless the corresponding cast from U* to T* is well formed: 
1) The behavior is undefined unless static_cast&lt;T*&gt;((U*)nullptr) is well formed. 
2) The behavior is undefined unless dynamic_cast&lt;T*&gt;((U*)nullptr) is well formed. 
3) The behavior is undefined unless const_cast&lt;T*&gt;((U*)nullptr) is well formed. 
4) The behavior is undefined unless reinterpret_cast&lt;T*&gt;((U*)nullptr) is well formed. 

<h2>Parameters</h2>

r - The pointer to convert

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr 
constructor <i>(public member function)</i> 
static_pointer_cast 
dynamic_pointer_cast 
const_pointer_cast 
reinterpret_pointer_cast applies static_cast, dynamic_cast, const_cast, or reinterpret_cast to the stored pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
