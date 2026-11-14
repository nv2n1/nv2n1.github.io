---
title: "sc_bcaststatesend(3)"
name: "sc_bcaststatesend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bcaststatesend/"
description: "sc::BcastStateSend –"
---

<p>sc::BcastStateSend &#8211; </p>
<p> <code>BcastStateSend</code> does the send part of a broadcast of an object to all nodes.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;</code></pre>
<p> Inherits <code>sc::MsgStateSend</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BcastStateSend</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;)<br />
 <i>Create the </i><code>BcastStateSend</code>.<br />
 void <code>flush</code> ()<br />
 <i>Flush the data remaining in the buffer. </i></p>
<h2>Detailed Description</h2>
<p><code>BcastStateSend</code> does the send part of a broadcast of an object to all nodes. </p>
<p> Only one node uses a <code>BcastStateSend</code> and the rest must use a <code>BcastStateRecv</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
