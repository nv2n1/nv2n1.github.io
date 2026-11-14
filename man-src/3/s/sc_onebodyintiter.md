---
title: "sc_onebodyintiter(3)"
name: "sc_onebodyintiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyintiter/"
description: "sc::OneBodyIntIter –"
---

<p>sc::OneBodyIntIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::SymmOneBodyIntIter</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OneBodyIntIter (const Ref&lt; OneBodyInt &gt; &amp;)



virtual void start (int ist=0, int jst=0, int ien=0, int jen=0)



virtual void next ()



int ready () const



int ishell () const



int jshell () const



int ijshell () const



int redundant () const



void set_redundant (int i)



virtual double scale () const



Ref&lt; OneBodyInt &gt; one_body_int ()



ShellPairIter &amp; current_pair ()



virtual bool cloneable ()



virtual Ref&lt; OneBodyIntIter &gt; clone ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>obi</code> </p>
<p> <code>ShellPairIter</code> <code>spi</code> </p>
<p> int <code>redund</code> </p>
<p> int <code>istart</code> </p>
<p> int <code>jstart</code> </p>
<p> int <code>iend</code> </p>
<p> int <code>jend</code> </p>
<p> int <code>icur</code> </p>
<p> int <code>jcur</code> </p>
<p> int <code>ij</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
