---
title: "sc_msgstaterecv(3)"
name: "sc_msgstaterecv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_msgstaterecv/"
description: "sc::MsgStateRecv –"
---

<p>sc::MsgStateRecv &#8211; </p>
<p> The <code>MsgStateRecv</code> is an abstract base class that receives objects from nodes in a <code>MessageGrp</code>.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/mstate.h">mstate.h</a>&gt; </p>
<p> Inherits <code>sc::MsgStateBufRecv</code>. </p>
<p> Inherited by <code>sc::BcastStateRecv</code>, and <code>sc::StateRecv</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>MsgStateRecv</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;)<br />
 <i></i><code>MsgStateRecv</code> must be initialized with a <code>MessageGrp</code>.<br />
 int <code>version</code> (const <code>ClassDesc</code> *)<br />
 <i>Returns the version of the </i><code>ClassDesc</code>.<br />
 int <code>get</code> (const <code>ClassDesc</code> **)<br />
 <i>I only need to override get(ClassDesc**) but C++ will hide all of the other get&#8217;s so I must override everything. </i><br />
 int <code>get</code> (char &amp;r, const char *key=0)<br />
 <i>These restore data saved with StateOut&#8217;s put. members. </i><br />
 int <code>get</code> (unsigned int &amp;r, const char *key=0) </p>
<p> int <code>get</code> (int &amp;r, const char *key=0) </p>
<p> int <code>get</code> (float &amp;r, const char *key=0) </p>
<p> int <code>get</code> (double &amp;r, const char *key=0) </p>
<p> int <code>get</code> (char *&amp;)<br />
 <i>These restore data saved with StateOut&#8217;s put. </i><br />
 int <code>get</code> (unsigned int *&amp;) </p>
<p> int <code>get</code> (int *&amp;) </p>
<p> int <code>get</code> (float *&amp;) </p>
<p> int <code>get</code> (double *&amp;) </p>
<h2>Detailed Description</h2>
<p> The <code>MsgStateRecv</code> is an abstract base class that receives objects from nodes in a <code>MessageGrp</code>. </p>
<h2>Member Function Documentation</h2>
<h3>int sc::MsgStateRecv::get (char *&amp;) [virtual]</h3>
<p> These restore data saved with StateOut&#8217;s put. members. The data is allocated by <code>StateIn</code>. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::MsgStateRecv::get (const <code>ClassDesc</code> **) [virtual]</h3>
<p> I only need to override get(ClassDesc**) but C++ will hide all of the other get&#8217;s so I must override everything. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::MsgStateRecv::version (const <code>ClassDesc</code> *) [virtual]</h3>
<p> Returns the version of the <code>ClassDesc</code>. This assumes that the version of the remote class is the same as that of the local class. </p>
<p> Reimplemented from <code>sc::StateIn</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
