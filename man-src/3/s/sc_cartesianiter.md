---
title: "sc_cartesianiter(3)"
name: "sc_cartesianiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_cartesianiter/"
description: "sc::CartesianIter –"
---

<p>sc::CartesianIter &#8211; </p>
<p> <code>CartesianIter</code> gives the ordering of the Cartesian functions within a shell for the particular integrals specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;cartiter.h&gt;</code></pre>
<p> Inherited by <code>MPQC::CartesianIterCCA</code>, <code>sc::CartesianIterCCA</code>, <code>sc::CartesianIterCints</code>, and <code>sc::CartesianIterV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CartesianIter (int l)


Initialize an iterator for the given angular momentum.


virtual void start ()=0


Start the iteration.


virtual void next ()=0


Move to the next Cartesian function.


virtual operator int ()=0


Returns nonzero if the iterator currently hold valid data.


int n ()


Returns the number of Cartesian functions.


int a ()


Returns the exponent of x.


int b ()


Returns the exponent of y.


int c ()


Returns the exponent of z.


int l ()


Returns the angular momentum.


int l (int i)


Returns a() if i==0, b() if i==1, and c() if i==2.


int bfn ()


Returns the number of the current basis function within the shell.



Protected Attributes
int a_



int b_



int c_



int l_



int bfn_</code></pre>
<h2>Detailed Description</h2>
<p><code>CartesianIter</code> gives the ordering of the Cartesian functions within a shell for the particular integrals specialization.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::CartesianIter::bfn () [inline]</h3>
<p>Returns the number of the current basis function within the shell. This starts at 0 and sequentially increases as <code>next()</code> is called.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
