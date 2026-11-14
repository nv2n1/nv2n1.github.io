---
title: "sc_msgmemorygrp(3)"
name: "sc_msgmemorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_msgmemorygrp/"
description: "sc::MsgMemoryGrp –"
---

<p>sc::MsgMemoryGrp &#8211; </p>
<p> A <code>MsgMemoryGrp</code> that initializes its data using a messagegrp.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memmsg.h&gt;</code></pre>
<p> Inherits <code>sc::MemoryGrp</code>. Inherited by <code>sc::ActiveMsgMemoryGrp</code>, <code>sc::RDMAMemoryGrp</code>, and <code>sc::ShmMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MsgMemoryGrp</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;msg) </p>
<p> <code>MsgMemoryGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval) </p>
<p> void <code>set_localsize</code> (size_t localsize)<br />
 <i>Set the size of locally held memory. </i><br />
 void <code>sync</code> ()<br />
 <i>Synchronizes all the nodes. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>msg_</code></p>
<h2>Detailed Description</h2>
<p>A <code>MsgMemoryGrp</code> that initializes its data using a messagegrp.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MsgMemoryGrp::set_localsize (size_t) [virtual]</h3>
<p>Set the size of locally held memory. When memory is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Implements <code>sc::MemoryGrp</code>. </p>
<p> Reimplemented in <code>sc::ActiveMsgMemoryGrp</code>, <code>sc::ARMCIMemoryGrp</code>, <code>sc::RDMAMemoryGrp</code>, and <code>sc::ShmMemoryGrp</code>.</p>
<h3>void sc::MsgMemoryGrp::sync () [virtual]</h3>
<p>Synchronizes all the nodes. This is useful after remote memory writes to be certain that all of the writes have completed and the data can be accessed locally, for example. </p>
<p> Implements <code>sc::MemoryGrp</code>. </p>
<p> Reimplemented in <code>sc::ARMCIMemoryGrp</code>, and <code>sc::MTMPIMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
