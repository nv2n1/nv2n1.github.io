---
title: "sc_stateinfile(3)"
name: "sc_stateinfile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stateinfile/"
description: "sc::StateInFile –"
---

<p>sc::StateInFile &#8211; </p>
<p> Reads state information from a file.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state_file.h&gt;</code></pre>
<p> Inherits <code>sc::StateIn</code>. Inherited by <code>sc::StateInBin</code>, and <code>sc::StateInText</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StateInFile</code> ()<br />
 <i>State information will be obtained from cin. </i><br />
 <code>StateInFile</code> (std::istream &amp;s)<br />
 <i>State information will be obtained from fp. </i><br />
 <code>StateInFile</code> (const char *name)<br />
 <i>State information will be obtained from name. </i><br />
 virtual int <code>open</code> (const char *name)<br />
 <i>State information will be obtained from name. </i><br />
 virtual void <code>close</code> ()<br />
 <i>Close the output file. </i></p>
<h3>Protected Attributes</h3>
<pre><code>int opened_



std::streambuf * buf_</code></pre>
<h2>Detailed Description</h2>
<p>Reads state information from a file.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
