---
title: "fdtypedefs(3)"
name: "fdtypedefs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdtypedefs/"
description: "ql/methods/finitedifferences/fdtypedefs.hpp – default choices for template instantiations"
---

<h2 class="name">NAME</h2>
<p> ql/methods/finitedifferences/fdtypedefs.hpp &#8211; default choices for template instantiations </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/finitedifferences/cranknicolson.hpp&gt;<br />
 #include &lt;ql/methods/finitedifferences/parallelevolver.hpp&gt; </p>
<h3>Typedefs</h3>
<p> typedef FiniteDifferenceModel&lt; CrankNicolson&lt; TridiagonalOperator &gt; &gt; <code>StandardFiniteDifferenceModel</code><br />
 <i>default choice for finite-difference model </i><br />
 typedef FiniteDifferenceModel&lt; ParallelEvolver&lt; CrankNicolson&lt; TridiagonalOperator &gt; &gt; &gt; <code>StandardSystemFiniteDifferenceModel</code><br />
 <i>default choice for parallel finite-difference model </i><br />
 typedef StepCondition&lt; Array &gt; <code>StandardStepCondition</code><br />
 <i>default choice for step condition </i><br />
 typedef CurveDependentStepCondition&lt; Array &gt; <code>StandardCurveDependentStepCondition</code> </p>
<h2>Detailed Description</h2>
<p> default choices for template instantiations </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
