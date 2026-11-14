---
title: "sc_pointinputdata(3)"
name: "sc_pointinputdata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pointinputdata/"
description: "sc::PointInputData –"
---

<p>sc::PointInputData &#8211; </p>
<p> Contains data needed at each <code>point</code> by a <code>DenFunctional</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;

Classes struct SpinData

    Public Types enum { X = BatchElectronDensity::X,
                        Y = BatchElectronDensity::Y,
                        Z = BatchElectronDensity::Z }

enum { XX = BatchElectronDensity::XX,
       YX = BatchElectronDensity::YX,
       YY = BatchElectronDensity::YY,
       ZX = BatchElectronDensity::ZX,
       ZY = BatchElectronDensity::ZY,
       ZZ = BatchElectronDensity::ZZ }

Public Member Functions void
compute_derived(int spin_polarized, int need_gradient, int need_hessian)

    PointInputData(const SCVector3 &amp;r_)

        Public Attributes</code></pre>
<p> <code>SpinData</code> <code>a</code> </p>
<p> <code>SpinData</code> <code>b</code> </p>
<p> double <code>gamma_ab</code> </p>
<p> const <code>SCVector3</code> &amp; <code>r</code></p>
<h2>Detailed Description</h2>
<p>Contains data needed at each <code>point</code> by a <code>DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
