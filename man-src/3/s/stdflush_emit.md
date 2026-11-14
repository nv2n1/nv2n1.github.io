---
title: "stdflush_emit(3)"
name: "stdflush_emit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdflush_emit/"
---

std::flush_emit - std::flush_emit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ostream&gt;

template&lt; class CharT, class Traits &gt;                                                    (since C++20)

std::basic_ostream&lt;CharT, Traits&gt;&amp; flush_emit( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );</code></pre> 
Flushes the output sequence os as if by calling os.flush(). Then, if os.rdbuf() actually points to a std::basic_syncbuf&lt;CharT, Traits, Allocator&gt; buf, calls buf.emit(). 
This is an output-only I/O manipulator, it may be called with an expression such as out &lt;&lt; std::flush_emit for any out of type std::basic_ostream. 

<h2>Parameters</h2>

os - reference to output stream

<h2>Return value</h2>

os (reference to the stream after manipulation) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronizes with the underlying storage device 
flush <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
