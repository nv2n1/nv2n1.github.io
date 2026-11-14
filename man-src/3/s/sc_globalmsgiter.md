---
title: "sc_globalmsgiter(3)"
name: "sc_globalmsgiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_globalmsgiter/"
description: "sc::GlobalMsgIter –"
---

<p>sc::GlobalMsgIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::HypercubeGMI</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>GlobalMsgIter (int nproc, int me, int root=0)



void backwards ()



void forwards ()



void next ()



int done ()



int n ()



int sendto ()



int send ()



int recvfrom ()



int recv ()



Protected Member Functions
virtual int fwdsendto ()=0



virtual int fwdsend ()=0



virtual int fwdrecvfrom ()=0



virtual int fwdrecv ()=0



Protected Attributes
int me_



int nproc_



int root_



int i_



int n_



int fwd_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
