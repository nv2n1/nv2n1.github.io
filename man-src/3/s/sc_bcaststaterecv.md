---
title: "sc_bcaststaterecv(3)"
name: "sc_bcaststaterecv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bcaststaterecv/"
description: "sc::BcastStateRecv –"
---

<p>sc::BcastStateRecv &#8211; </p>
<p> <code>BcastStateRecv</code> does the receive part of a broadcast of an object to all nodes.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;</code></pre>
<p> Inherits <code>sc::MsgStateRecv</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>BcastStateRecv (const Ref&lt; MessageGrp &gt; &amp;, int source=0)


Create the BcastStateRecv.


void source (int s)


Set the source node.



Protected Member Functions
void next_buffer ()


Specializations must implement next_buffer().



Protected Attributes
int source_</code></pre>
<h2>Detailed Description</h2>
<p><code>BcastStateRecv</code> does the receive part of a broadcast of an object to all nodes. </p>
<p> Only one node uses a <code>BcastStateSend</code> and the rest must use a <code>BcastStateRecv</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
