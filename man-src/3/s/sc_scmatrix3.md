---
title: "sc_scmatrix3(3)"
name: "sc_scmatrix3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrix3/"
---

sc::SCMatrix3 -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>SCMatrix3 (const SCMatrix3 &amp;)



SCMatrix3 (const RefSCMatrix3 &amp;)



SCMatrix3 (double x[9])



SCMatrix3 (const SCVector3 &amp;p1, const SCVector3 &amp;p2, const SCVector3 &amp;p3)



SCMatrix3 &amp; operator= (const SCMatrix3 &amp;)



SCMatrix3 operator* (double) const



SCMatrix3 operator* (const SCMatrix3 &amp;) const



SCVector3 operator* (const SCVector3 &amp;v) const



SCMatrix3 operator+ (const SCMatrix3 &amp;) const



SCMatrix3 operator- (const SCMatrix3 &amp;) const



double &amp; elem (int i, int j)



const double &amp; elem (int i, int j) const



double &amp; elem (int i)



const double &amp; elem (int i) const



double &amp; operator[] (int i)



const double &amp; operator[] (int i) const



double &amp; operator() (int i, int j)



const double &amp; operator() (int i, int j) const



const double * data () const



void print (std::ostream &amp;=ExEnv::out0()) const
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
