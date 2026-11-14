---
title: "sc_shellpairiter(3)"
name: "sc_shellpairiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellpairiter/"
---

sc::ShellPairIter -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>void init (const double *buffer, int ishell, int jshell, int ioff, int joff, int nfunci, int nfuncj, int redund=0, double scale=1.0)



void start ()



int ready () const



void next ()



int current_i () const



int current_j () const



int i () const



int j () const



int nint () const



double val () const
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
