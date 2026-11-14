---
title: "sc_bcaststateinbin(3)"
name: "sc_bcaststateinbin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bcaststateinbin/"
description: "sc::BcastStateInBin –"
---

<p>sc::BcastStateInBin &#8211; </p>
<p> BcastStateBin reads a file in written by <code>StateInBin</code> on node 0 and broadcasts it to all nodes so state can be simultaneously restored on all nodes.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mstate.h&gt;</code></pre>
<p> Inherits <code>sc::MsgStateBufRecv</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BcastStateInBin</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Create the </i><code>BcastStateRecv</code> using the default <code>MessageGrp</code>.<br />
 <code>BcastStateInBin</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;, const char *filename)<br />
 <i>Create the </i><code>BcastStateRecv</code>.<br />
 virtual int <code>open</code> (const char *name) </p>
<p> virtual void <code>close</code> () </p>
<p> void <code>seek</code> (int loc)<br />
 <i>Set the current position in the file. </i><br />
 int <code>seekable</code> ()<br />
 <i>Return non-zero if seek does anything sensible. </i><br />
 int <code>tell</code> ()<br />
 <i>Return the current position in the file. </i><br />
 int <code>use_directory</code> ()<br />
 <i>Returns true of this object uses a directory. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void next_buffer ()


Specializations must implement next_buffer().


int get_array_void (void *, int)



Protected Attributes
int opened_



int file_position_



std::streambuf * buf_</code></pre>
<h2>Detailed Description</h2>
<p>BcastStateBin reads a file in written by <code>StateInBin</code> on node 0 and broadcasts it to all nodes so state can be simultaneously restored on all nodes.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::BcastStateInBin::seek (int) [virtual]</h3>
<p>Set the current position in the file. The default implementation does nothing. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::BcastStateInBin::seekable () [virtual]</h3>
<p>Return non-zero if seek does anything sensible. The default implementation returns 0. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
