---
title: "lmdif(3)"
name: "lmdif"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lmdif/"
description: "ql/math/optimization/lmdif.hpp – wrapper for MINPACK minimization routine"
---

<h2 class="name">NAME</h2>
<p> ql/math/optimization/lmdif.hpp &#8211; wrapper for MINPACK minimization routine </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/qldefines.hpp&gt;<br />
 #include &lt;boost/function.hpp&gt; </p>
<h3>Typedefs</h3>
<p> typedef boost::function&lt; void(int, int, double *, double *, int *) <code>LmdifCostFunction</code> ) </p>
<h3>Functions</h3>
<p> void <code>lmdif</code> (int m, int n, double *x, double *fvec, double ftol, double xtol, double gtol, int maxfev, double epsfcn, double *diag, int mode, double factor, int nprint, int *info, int *nfev, double *fjac, int ldfjac, int *ipvt, double *qtf, double *wa1, double *wa2, double *wa3, double *wa4, const LmdifCostFunction &amp;fcn) </p>
<p> void <code>qrsolv</code> (int n, double *r, int ldr, int *ipvt, double *diag, double *qtb, double *x, double *sdiag, double *wa) </p>
<p> void <code>qrfac</code> (int m, int n, double *a, int, int pivot, int *ipvt, int, double *rdiag, double *acnorm, double *wa) </p>
<h2>Detailed Description</h2>
<p> wrapper for MINPACK minimization routine </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
