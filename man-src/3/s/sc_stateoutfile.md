---
title: "sc_stateoutfile(3)"
name: "sc_stateoutfile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateoutfile/"
description: "sc::StateOutFile –"
---

<p>sc::StateOutFile &#8211; </p>
<p> Writes state information to files.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_file.h&gt;</code></pre>
<p> Inherits <code>sc::StateOut</code>. Inherited by <code>sc::StateOutBin</code>, and <code>sc::StateOutText</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateOutFile</code> ()<br />
 <i>State information will be written to </i><code>ExEnv::outn()</code>.<br />
 <code>StateOutFile</code> (std::ostream &amp;s)<br />
 <i>State information will be written to s. </i><br />
 <code>StateOutFile</code> (const char *name)<br />
 <i>State information will be written to name. </i><br />
 virtual int <code>open</code> (const char *name)<br />
 <i>State information will be written to name. </i><br />
 virtual void <code>flush</code> ()<br />
 <i>Flush the output stream. </i><br />
 virtual void <code>close</code> ()<br />
 <i>Close the output stream. </i></p>
<h3>Protected Attributes</h3>
<pre><code>int opened_



std::streambuf * buf_</code></pre>
<h2>Detailed Description</h2>
<p>Writes state information to files.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
