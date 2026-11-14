---
title: "stdbasic_syncbuf(3)"
name: "stdbasic_syncbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_syncbuf/"
---

std::basic_syncbuf&lt;CharT,Traits,Allocator&gt;::~basic_syncbuf - std::basic_syncbuf&lt;CharT,Traits,Allocator&gt;::~basic_syncbuf

<h2>Synopsis</h2>

<pre><code>~basic_syncbuf();</code></pre> 
Calls emit() to transmit all pending output (and delayed flush, if any) to the wrapped stream. If an exception is thrown by this call, it is caught and ignored. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Notes</h2>

Normally called by the destructor of the owning std::basic_osyncstream. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the basic_osyncstream and emits its internal buffer 
destructor <i>(public member function of std::basic_osyncstream&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a basic_syncbuf object 
constructor <i>(public member function)</i> 
