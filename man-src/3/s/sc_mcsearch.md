---
title: "sc_mcsearch(3)"
name: "sc_mcsearch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mcsearch/"
description: "sc::MCSearch –"
---

<p>sc::MCSearch &#8211; </p>
<p> This performs line searches with cubic steps.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mcsearch.h&gt;</code></pre>
<p> Inherits <code>sc::LineOpt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MCSearch</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>MCSearch</code> <code>KeyVal</code> CTOR does not read any input.<br />
 int <code>update</code> ()<br />
 <i>Take a step. </i><br />
 void <code>init</code> (<code>RefSCVector</code> &amp;direction)<br />
 <i>Initializes the line search object. </i><br />
 void <code>init</code> (<code>RefSCVector</code> &amp;direction, <code>Ref</code>&lt; <code>Function</code> &gt; function)<br />
 <i>Initializes the line search object. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void mcstep (double *stx, double *fx, double *dx, double *sty, double *fy, double *dy, double *stp, double *fp, double *dp, bool *brackt, double *stpmin, double *stpmax, int *info)



void mcsrch (int *n, double *x, double *f, double *g, double *s, double *stp, double *ftol, double *xtol, int *maxfev, int *info, int *nfev, double *wa)



void mcinit ()



Protected Attributes
double gtol_



double stpmin_



double stpmax_



double dg



double fm



double fx



double fy



double dgm



double dgx



double dgy



double fxm



double fym



double stx



double sty



double dgxm



double dgym



int infoc



double finit



double width



double stmin



double stmax



bool stage1



double width1



double ftest1



bool brackt



double dginit



double dgtest



double p



double q



double r__



double s



double sgnd



double stpc



double stpf



double stpq



double gamma



double theta



bool bound



int info_



auto_vec&lt; double &gt; wa_</code></pre>
<h2>Detailed Description</h2>
<p>This performs line searches with cubic steps. </p>
<p> It is based on the Fortran MCSRCH and MCSTEP routines produced by: Argonne National Laboratory. MINPACK Project. June 1983 Jorge J. More&#8217;, David J. Thuente.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MCSearch::MCSearch (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>MCSearch</code> <code>KeyVal</code> CTOR does not read any input. See the <code>LineOpt</code> <code>KeyVal</code> CTOR for parameters that it takes.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MCSearch::init (<code>RefSCVector</code> &amp; direction, <code>Ref</code>&lt; <code>Function</code> &gt; function) [virtual]</h3>
<p>Initializes the line search object. First argument is a search direction, second argument is a function object to optimize. Use this method when a function must be passed to the <code>Optimize</code> base class. </p>
<p> Reimplemented from <code>sc::LineOpt</code>.</p>
<h3>void sc::MCSearch::init (<code>RefSCVector</code> &amp; direction) [virtual]</h3>
<p>Initializes the line search object. Argument is a search direction. Use of this method assumes the <code>Optimize</code> base class already has a function object (got it from a keyval or elsewhere). </p>
<p> Reimplemented from <code>sc::LineOpt</code>.</p>
<h3>int sc::MCSearch::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
