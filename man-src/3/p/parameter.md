---
title: "parameter(3)"
name: "parameter"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parameter/"
description: "ql/models/parameter.hpp – Model parameter classes."
---

<p>ql/models/parameter.hpp &#8211; Model parameter classes. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/qldefines.hpp&gt;

#include &lt;ql/handle.hpp&gt;

#include &lt;ql/math/optimization/constraint.hpp&gt;

#include &lt;vector&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>Parameter</code><br />
 <i>Base class for model arguments. </i><br />
 class <code>Impl</code><br />
 <i>Base class for model parameter implementation. </i><br />
 class <code>ConstantParameter</code><br />
 <i>Standard constant parameter $ a(t) = a $. </i><br />
 class <code>NullParameter</code><br />
 <i>Parameter which is always zero $ a(t) = 0 $ </i><br />
 class <code>PiecewiseConstantParameter</code><br />
 <i>Piecewise-constant parameter. </i><br />
 class <code>TermStructureFittingParameter</code><br />
 <i>Deterministic time-dependent parameter used for yield-curve fitting. </i></p>
<h2>Detailed Description</h2>
<p>Model parameter classes.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
