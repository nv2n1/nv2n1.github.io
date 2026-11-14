---
title: "sc_twobodyintiter(3)"
name: "sc_twobodyintiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyintiter/"
description: "sc::TwoBodyIntIter –"
---

<p>sc::TwoBodyIntIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>sc::SymmTwoBodyIntIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyIntIter</code> (const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;) </p>
<p> virtual void <code>start</code> () </p>
<p> virtual void <code>next</code> () </p>
<p> int <code>ready</code> () const </p>
<p> int <code>ishell</code> () const </p>
<p> int <code>jshell</code> () const </p>
<p> int <code>kshell</code> () const </p>
<p> int <code>lshell</code> () const </p>
<p> virtual double <code>scale</code> () const </p>
<p> <code>ShellQuartetIter</code> &amp; <code>current_quartet</code> ()</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>tbi</code> </p>
<p> <code>ShellQuartetIter</code> <code>sqi</code> </p>
<p> int <code>iend</code> </p>
<p> int <code>icur</code> </p>
<p> int <code>jcur</code> </p>
<p> int <code>kcur</code> </p>
<p> int <code>lcur</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
