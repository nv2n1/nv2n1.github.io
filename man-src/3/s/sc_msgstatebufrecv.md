---
title: "sc_msgstatebufrecv(3)"
name: "sc_msgstatebufrecv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_msgstatebufrecv/"
description: "sc::MsgStateBufRecv –"
---

<p>sc::MsgStateBufRecv &#8211; </p>
<p> The <code>MsgStateBufRecv</code> is an abstract base class that buffers objects sent through a <code>MessageGrp</code>.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/mstate.h">mstate.h</a>&gt; </p>
<p> Inherits <code>sc::StateIn</code>. </p>
<p> Inherited by <code>sc::BcastStateInBin</code>, and <code>sc::MsgStateRecv</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>MsgStateBufRecv</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;)<br />
 <i></i><code>MsgStateBufRecv</code> can be initialized with a <code>MessageGrp</code>.<br />
 <code>MsgStateBufRecv</code> ()<br />
 <i>Use the default </i><code>MessageGrp</code>.<br />
 void <code>set_buffer_size</code> (int)<br />
 <i>The buffer size of statein and stateout objects that communicate with each other must match. </i></p>
<h3>Protected Member Functions</h3>
<p> int <code>get_array_void</code> (void *, int) </p>
<p> virtual void <code>next_buffer</code> ()=0<br />
 <i>Specializations must implement </i><code>next_buffer()</code>.</p>
<h3>Protected Attributes</h3>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp</code> </p>
<p> int <code>nbuf</code> </p>
<p> int <code>ibuf</code> </p>
<p> int <code>bufsize</code> </p>
<p> char * <code>buffer</code> </p>
<p> char * <code>send_buffer</code> </p>
<p> int <code>nheader</code> </p>
<p> int * <code>nbuf_buffer</code> </p>
<h2>Detailed Description</h2>
<p> The <code>MsgStateBufRecv</code> is an abstract base class that buffers objects sent through a <code>MessageGrp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MsgStateBufRecv::set_buffer_size (int)</h3>
<p> The buffer size of statein and stateout objects that communicate with each other must match. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
