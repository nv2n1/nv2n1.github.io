---
title: "constraint(3)"
name: "constraint"
section: "3"
letter: "c"
url: "/docs/linux/man/3-constraint/"
description: "ql/math/optimization/constraint.hpp – Abstract constraint class."
---

<h2 class="name">NAME</h2>
<p> ql/math/optimization/constraint.hpp &#8211; Abstract constraint class. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/array.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>Constraint</code><br />
 <i>Base constraint class. </i><br />
 class <code>Impl</code><br />
 <i>Base class for constraint implementations. </i><br />
 class <code>NoConstraint</code><br />
 <i>No constraint. </i><br />
 class <code>PositiveConstraint</code><br />
 <i>Constraint imposing positivity to all arguments </i><br />
 class <code>BoundaryConstraint</code><br />
 <i>Constraint imposing all arguments to be in [low,high] </i><br />
 class <code>CompositeConstraint</code><br />
 <i>Constraint enforcing both given sub-constraints </i></p>
<h2>Detailed Description</h2>
<p> Abstract constraint class. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
