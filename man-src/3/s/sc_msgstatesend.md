---
title: "sc_msgstatesend(3)"
name: "sc_msgstatesend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_msgstatesend/"
description: "sc::MsgStateSend –"
---

<p>sc::MsgStateSend &#8211; </p>
<p> The <code>MsgStateSend</code> is an abstract base class that sends objects to nodes in a <code>MessageGrp</code>.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/mstate.h">mstate.h</a>&gt; </p>
<p> Inherits <code>sc::StateOut</code>. </p>
<p> Inherited by <code>sc::BcastStateSend</code>, and <code>sc::StateSend</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>MsgStateSend</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;) </p>
<p> virtual void <code>flush</code> ()=0<br />
 <i>Specializations must implement </i><code>flush()</code>.<br />
 void <code>set_buffer_size</code> (int)<br />
 <i>The buffer size of statein and stateout objects that communicate with each other must match. </i><br />
 int <code>put</code> (const <code>ClassDesc</code> *)<br />
 <i>I only need to override </i><code>put(const ClassDesc*)</code> but C++ will hide all of the other put&#8217;s so I must override everything.<br />
 int <code>put</code> (char r)<br />
 <i>Write the given datum. </i><br />
 int <code>put</code> (unsigned int r) </p>
<p> int <code>put</code> (int r) </p>
<p> int <code>put</code> (float r) </p>
<p> int <code>put</code> (double r) </p>
<p> int <code>put</code> (const char *, int)<br />
 <i>Write the given array data. </i><br />
 int <code>put</code> (const int *, int) </p>
<p> int <code>put</code> (const unsigned int *, int) </p>
<p> int <code>put</code> (const float *, int) </p>
<p> int <code>put</code> (const double *, int) </p>
<h3>Protected Member Functions</h3>
<p> int <code>put_array_void</code> (const void *, int) </p>
<h3>Protected Attributes</h3>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp</code> </p>
<p> int <code>nbuf</code> </p>
<p> int <code>bufsize</code> </p>
<p> char * <code>buffer</code> </p>
<p> char * <code>send_buffer</code> </p>
<p> int <code>nheader</code> </p>
<p> int * <code>nbuf_buffer</code> </p>
<h2>Detailed Description</h2>
<p> The <code>MsgStateSend</code> is an abstract base class that sends objects to nodes in a <code>MessageGrp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::MsgStateSend::put (const char *, int) [virtual]</h3>
<p> Write the given array data. Size information is also saved. The data is allocated and read by the get(T*&amp;) routines. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::MsgStateSend::put (const <code>ClassDesc</code> *) [virtual]</h3>
<p> I only need to override <code>put(const ClassDesc*)</code> but C++ will hide all of the other put&#8217;s so I must override everything. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>void sc::MsgStateSend::set_buffer_size (int)</h3>
<p> The buffer size of statein and stateout objects that communicate with each other must match. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
