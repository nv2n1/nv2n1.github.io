---
title: "sc_stateoutbin(3)"
name: "sc_stateoutbin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateoutbin/"
description: "sc::StateOutBin –"
---

<p>sc::StateOutBin &#8211; </p>
<p> Save state to a binary file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_bin.h&gt;</code></pre>
<p> Inherits <code>sc::StateOutFile</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateOutBin</code> (std::ostream &amp;) </p>
<p> <code>StateOutBin</code> (const char *) </p>
<p> int <code>open</code> (const char *name)<br />
 <i>State information will be written to name. </i><br />
 void <code>close</code> ()<br />
 <i>Close the output stream. </i><br />
 int <code>use_directory</code> ()<br />
 <i>Returns true if this object uses a directory. </i><br />
 int <code>tell</code> ()<br />
 <i>Returns the current position in the file. </i><br />
 void <code>seek</code> (int loc)<br />
 <i>Set the current position in the file. </i><br />
 int <code>seekable</code> ()<br />
 <i>Return non-zero if tell and seek do anything sensible. </i></p>
<h2>Detailed Description</h2>
<p>Save state to a binary file.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::StateOutBin::seek (int loc) [virtual]</h3>
<p>Set the current position in the file. The default implementation does nothing. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::StateOutBin::seekable () [virtual]</h3>
<p>Return non-zero if tell and seek do anything sensible. The default implementation returns 0. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h3>int sc::StateOutBin::tell () [virtual]</h3>
<p>Returns the current position in the file. The default implementation returns 0. </p>
<p> Reimplemented from <code>sc::StateOut</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
