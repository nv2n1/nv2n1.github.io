---
title: "sc_intv3arraydoublep3(3)"
name: "sc_intv3arraydoublep3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_intv3arraydoublep3/"
---

sc::IntV3Arraydoublep3 -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>int n1 () const



int n2 () const



int n3 () const



void delete_data ()



void set_dim (int n1, int n2, int n3)



double *&amp; operator() (int i, int j, int k)



double ** operator() (int i, int j)



double *** operator() (int i)



void print (std::ostream &amp;)



int nbyte () const
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
