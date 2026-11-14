---
title: "sc_procmessagegrp(3)"
name: "sc_procmessagegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_procmessagegrp/"
description: "sc::ProcMessageGrp –"
---

<p>sc::ProcMessageGrp &#8211; </p>
<p> <code>ProcMessageGrp</code> provides a concrete specialization of <code>MessageGrp</code> that supports only one node.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;message.h&gt;</code></pre>
<p> Inherits <code>sc::MessageGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ProcMessageGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>clone</code> (void)<br />
 <i>Returns a copy of this </i><code>MessageGrp</code> specialization that provides an independent communication context.<br />
 void <code>raw_send</code> (int target, const void *data, int nbyte) </p>
<p> void <code>raw_sendt</code> (int target, int type, const void *data, int nbyte) </p>
<p> void <code>raw_recv</code> (int sender, void *data, int nbyte) </p>
<p> void <code>raw_recvt</code> (int type, void *data, int nbyte) </p>
<p> void <code>raw_bcast</code> (void *data, int nbyte, int from) </p>
<p> int <code>probet</code> (int type)<br />
 <i>Ask if a given typed message has been received. </i><br />
 void <code>sync</code> ()<br />
 <i>Synchronize all of the processors. </i></p>
<h2>Detailed Description</h2>
<p><code>ProcMessageGrp</code> provides a concrete specialization of <code>MessageGrp</code> that supports only one node.</p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>MessageGrp</code>&gt; sc::ProcMessageGrp::clone (void) [virtual]</h3>
<p>Returns a copy of this <code>MessageGrp</code> specialization that provides an independent communication context. </p>
<p> Implements <code>sc::MessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
