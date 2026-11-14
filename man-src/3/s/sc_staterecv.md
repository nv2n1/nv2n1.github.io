---
title: "sc_staterecv(3)"
name: "sc_staterecv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_staterecv/"
description: "sc::StateRecv –"
---

<p>sc::StateRecv &#8211; </p>
<p> <code>StateRecv</code> is a concrete specialization of <code>MsgStateRecv</code> that does the receive part of <code>point</code> to <code>point</code> communication in a <code>MessageGrp</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;</code></pre>
<p> Inherits <code>sc::MsgStateRecv</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateRecv</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;)<br />
 <i>Create a </i><code>StateRecv</code> given a <code>MessageGrp</code>.<br />
 void <code>source</code> (int)<br />
 <i>Specify the source node. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void next_buffer ()


Specializations must implement next_buffer().</code></pre>
<h2>Detailed Description</h2>
<p><code>StateRecv</code> is a concrete specialization of <code>MsgStateRecv</code> that does the receive part of <code>point</code> to <code>point</code> communication in a <code>MessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
