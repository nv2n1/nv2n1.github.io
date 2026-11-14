---
title: "stdbasic_osyncstream(3)"
name: "stdbasic_osyncstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_osyncstream/"
---

std::basic_osyncstream&lt;CharT,Traits,Allocator&gt;::~basic_osyncstream - std::basic_osyncstream&lt;CharT,Traits,Allocator&gt;::~basic_osyncstream

<h2>Synopsis</h2>

<pre><code>~basic_osyncstream();</code></pre> 
Destroys a synchronized output stream 
First, calls emit(). If an exception is thrown by the call to emit(), it is caught and ignored. Then, destroys the member std::basic_syncbuf and the base std::basic_ostream as usual. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the basic_syncbuf and emits its internal buffer 
destructor <i>(public member function of std::basic_syncbuf&lt;CharT,Traits,Allocator&gt;)</i> 
