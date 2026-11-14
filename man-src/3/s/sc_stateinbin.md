---
title: "sc_stateinbin(3)"
name: "sc_stateinbin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateinbin/"
description: "sc::StateInBin –"
---

<p>sc::StateInBin &#8211; </p>
<p> Read objects written with <code>StateOutBin</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_bin.h&gt;</code></pre>
<p> Inherits <code>sc::StateInFile</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateInBin</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>StateInBin</code> (std::istream &amp;) </p>
<p> <code>StateInBin</code> (const char *) </p>
<p> int <code>open</code> (const char *name)<br />
 <i>State information will be obtained from name. </i><br />
 int <code>use_directory</code> ()<br />
 <i>Returns true of this object uses a directory. </i><br />
 int <code>tell</code> ()<br />
 <i>Return the current position in the file. </i><br />
 void <code>seek</code> (int loc)<br />
 <i>Set the current position in the file. </i><br />
 int <code>seekable</code> ()<br />
 <i>Return non-zero if seek does anything sensible. </i></p>
<h2>Detailed Description</h2>
<p>Read objects written with <code>StateOutBin</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::StateInBin::seek (int) [virtual]</h3>
<p>Set the current position in the file. The default implementation does nothing. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h3>int sc::StateInBin::seekable () [virtual]</h3>
<p>Return non-zero if seek does anything sensible. The default implementation returns 0. </p>
<p> Reimplemented from <code>sc::StateIn</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
