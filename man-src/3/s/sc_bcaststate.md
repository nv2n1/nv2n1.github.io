---
title: "sc_bcaststate(3)"
name: "sc_bcaststate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bcaststate/"
description: "sc::BcastState –"
---

<p>sc::BcastState &#8211; </p>
<p> This creates and forwards/retrieves data from either a <code>BcastStateRecv</code> or a <code>BcastStateSend</code> depending on the value of the argument to constructor.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;

Public Member Functions</code></pre>
<p> <code>BcastState</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;, int source=0)<br />
 <i>Create a </i><code>BcastState</code> object. The default source is node 0.<br />
 void <code>bcast</code> (int &amp;)<br />
 <i>Broadcast data to all nodes. </i><br />
 void <code>bcast</code> (double &amp;) </p>
<p> void <code>bcast</code> (int *&amp;, int) </p>
<p> void <code>bcast</code> (double *&amp;, int) </p>
<p> template&lt;class T &gt; void <code>bcast</code> (<code>Ref</code>&lt; T &gt; &amp;a) </p>
<p> void <code>flush</code> ()<br />
 <i>Force data to be written. </i><br />
 void <code>forget_references</code> ()<br />
 <i>Call the </i><code>StateOut</code> or <code>StateIn</code> forget_references member.<br />
 void <code>set_buffer_size</code> (int)<br />
 <i>Controls the amount of data that is buffered before it is sent. </i></p>
<h2>Detailed Description</h2>
<p>This creates and forwards/retrieves data from either a <code>BcastStateRecv</code> or a <code>BcastStateSend</code> depending on the value of the argument to constructor.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::BcastState::bcast (int &amp;)</h3>
<p>Broadcast data to all nodes. After these are called for a group of data the flush member must be called to force the source node to actually write the data.</p>
<h3>void sc::BcastState::flush ()</h3>
<p>Force data to be written. Data is not otherwise written until the buffer is full.</p>
<h3>void sc::BcastState::forget_references ()</h3>
<p>Call the <code>StateOut</code> or <code>StateIn</code> forget_references member.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
