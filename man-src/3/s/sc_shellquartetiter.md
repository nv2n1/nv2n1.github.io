---
title: "sc_shellquartetiter(3)"
name: "sc_shellquartetiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellquartetiter/"
description: "sc::ShellQuartetIter –"
---

<p>sc::ShellQuartetIter &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p>virtual void <code>init</code> (const double *, int, int, int, int, int, int, int, int, int, int, int, int, double, int) </p>
<p> virtual void <code>start</code> () </p>
<p> virtual void <code>next</code> () </p>
<p> int <code>ready</code> () const </p>
<p> int <code>i</code> () const </p>
<p> int <code>j</code> () const </p>
<p> int <code>k</code> () const </p>
<p> int <code>l</code> () const </p>
<p> int <code>nint</code> () const </p>
<p> double <code>val</code> () const</p>
<h3>Protected Attributes</h3>
<pre><code>const double * buf



double scale_



int redund_



int e12



int e34



int e13e24



int index



int istart



int jstart



int kstart



int lstart



int iend



int jend



int kend



int lend



int icur



int jcur



int kcur



int lcur



int i_



int j_



int k_



int l_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
