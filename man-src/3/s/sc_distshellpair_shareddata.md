---
title: "sc_distshellpair_shareddata(3)"
name: "sc_distshellpair_shareddata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distshellpair_shareddata/"
description: "sc::DistShellPair::SharedData –"
---

<p>sc::DistShellPair::SharedData &#8211; </p>
<p> This is used to store data that must be shared between all cooperating shell pairs.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;distshpair.h&gt;

Public Member Functions</code></pre>
<p> <code>SharedData</code> ()<br />
 <i>Construct and initialize. </i><br />
 void <code>init</code> ()<br />
 <i>If this will be used to iterate through the shells again, then init must be called. </i></p>
<h3>Public Attributes</h3>
<p>volatile long int <code>shellpair_</code></p>
<h2>Detailed Description</h2>
<p>This is used to store data that must be shared between all cooperating shell pairs.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
