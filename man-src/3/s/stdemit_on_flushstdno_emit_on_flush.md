---
title: "stdemit_on_flushstdno_emit_on_flush(3)"
name: "stdemit_on_flushstdno_emit_on_flush"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdemit_on_flushstdno_emit_on_flush/"
---

std::emit_on_flush,std::no_emit_on_flush - std::emit_on_flush,std::no_emit_on_flush

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ostream&gt;

template&lt; class CharT, class Traits &gt;                                                         (1) (since C++20)

std::basic_ostream&lt;CharT, Traits&gt;&amp; emit_on_flush( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );

template&lt; class CharT, class Traits &gt;                                                         (2) (since C++20)

std::basic_ostream&lt;CharT, Traits&gt;&amp; no_emit_on_flush( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );</code></pre> 
If os.rdbuf() actually points to a std::basic_syncbuf&lt;CharT, Traits, Allocator&gt; buf, toggles whether it emits (i.e., transmits data to the underlying stream buffer) when flushed: 
1) calls buf.set_emit_on_sync(true) 
2) calls buf.set_emit_on_sync(false) 
Otherwise, these manipulators have no effect. 
This is an output-only I/O manipulator, it may be called with an expression such as out &lt;&lt; std::emit_on_flush for any out of type std::basic_ostream. 

<h2>Parameters</h2>

os - reference to output stream

<h2>Return value</h2>

os (reference to the stream after manipulation) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the current emit-on-sync policy 
set_emit_on_sync <i>(public member function of std::basic_syncbuf&lt;CharT,Traits,Allocator&gt;)</i> 
