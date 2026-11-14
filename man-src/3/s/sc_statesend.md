---
title: "sc_statesend(3)"
name: "sc_statesend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_statesend/"
description: "sc::StateSend –"
---

<p>sc::StateSend &#8211; </p>
<p> <code>StateSend</code> is a concrete specialization of <code>MsgStateSend</code> that does the send part of <code>point</code> to <code>point</code> communication in a <code>MessageGrp</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;</code></pre>
<p> Inherits <code>sc::MsgStateSend</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateSend</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;)<br />
 <i>Create a </i><code>StateSend</code> given a <code>MessageGrp</code>.<br />
 void <code>target</code> (int)<br />
 <i>Specify the target node. </i><br />
 void <code>flush</code> ()<br />
 <i>Flush the buffer. </i></p>
<h2>Detailed Description</h2>
<p><code>StateSend</code> is a concrete specialization of <code>MsgStateSend</code> that does the send part of <code>point</code> to <code>point</code> communication in a <code>MessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
