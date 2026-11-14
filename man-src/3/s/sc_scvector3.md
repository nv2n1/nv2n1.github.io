---
title: "sc_scvector3(3)"
name: "sc_scvector3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scvector3/"
description: "sc::SCVector3 –"
---

<p>sc::SCVector3 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>SCVector3 (const double p[3])



SCVector3 (double d)



SCVector3 (double x, double y, double z)



SCVector3 (const SCVector3 &amp;p)



SCVector3 (const RefSCVector &amp;)



SCVector3 (const Ref&lt; KeyVal &gt; &amp;)



void normalize ()



SCVector3 operator- ()



SCVector3 operator* (double) const



void operator= (const double *x)



void operator= (const SCVector3 &amp;x)



void operator= (double d)



void operator-= (const SCVector3 &amp;v)



void operator+= (const SCVector3 &amp;v)



void operator*= (double m)



SCVector3 operator+ (const SCVector3 &amp;v) const



SCVector3 operator- (const SCVector3 &amp;v) const



double dot (const SCVector3 &amp;v) const



SCVector3 cross (const SCVector3 &amp;) const



SCVector3 perp_unit (const SCVector3 &amp;) const



void spherical_coord (double theta, double phi, double r)



void spherical_to_cartesian (SCVector3 &amp;cart) const



double maxabs () const



double dist (const SCVector3 &amp;) const



void rotate (double theta, SCVector3 &amp;v)



double norm () const



double &amp; elem (int xyz)



const double &amp; elem (int xyz) const



double &amp; operator[] (int i)



const double &amp; operator[] (int i) const



double &amp; operator() (int i)



const double &amp; operator() (int i) const



const double * data () const



double * data ()



double &amp; x ()



double &amp; y ()



double &amp; z ()



const double &amp; x () const



const double &amp; y () const



const double &amp; z () const



double &amp; r ()



double &amp; theta ()



double &amp; phi ()



const double &amp; r () const



const double &amp; theta () const



const double &amp; phi () const



void print (std::ostream &amp;=ExEnv::out0()) const



Friends</code></pre>
<p> class <code>SCMatrix3</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
