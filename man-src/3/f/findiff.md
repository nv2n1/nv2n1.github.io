---
title: "findiff(3)"
name: "findiff"
section: "3"
letter: "f"
url: "/docs/linux/man/3-findiff/"
description: "Finite-differences framework –"
---

<h2 class="name">NAME</h2>
<p> Finite-differences framework &#8211; </p>
<h3>Classes</h3>
<p> class <code>BoundaryCondition&lt; Operator &gt;</code><br />
 <i>Abstract boundary condition class for finite difference problems. </i><br />
 class <code>NeumannBC</code><br />
 <i>Neumann boundary condition (i.e., constant derivative). </i><br />
 class <code>DirichletBC</code><br />
 <i>Neumann boundary condition (i.e., constant value). </i><br />
 class <code>BSMOperator</code><br />
 <i>Black-Scholes-Merton differential operator. </i><br />
 class <code>CrankNicolson&lt; Operator &gt;</code><br />
 <i>Crank-Nicolson scheme for finite difference methods. </i><br />
 class <code>DMinus</code><br />
 <i>$ D_{-} $ matricial representation </i><br />
 class <code>DPlus</code><br />
 <i>$ D_{+} $ matricial representation </i><br />
 class <code>DPlusDMinus</code><br />
 <i>$ D_{+}D_{-} $ matricial representation </i><br />
 class <code>DZero</code><br />
 <i>$ D_{0} $ matricial representation </i><br />
 class <code>ExplicitEuler&lt; Operator &gt;</code><br />
 <i>Forward Euler scheme for finite difference methods </i><br />
 class <code>FiniteDifferenceModel&lt; Evolver &gt;</code><br />
 <i>Generic finite difference model. </i><br />
 class <code>ImplicitEuler&lt; Operator &gt;</code><br />
 <i>Backward Euler scheme for finite difference methods. </i><br />
 class <code>MixedScheme&lt; Operator &gt;</code><br />
 <i>Mixed (explicit/implicit) scheme for finite difference methods. </i><br />
 class <code>OperatorFactory</code><br />
 <i>Black-Scholes-Merton differential operator. </i><br />
 class <code>StepConditionSet&lt; array_type &gt;</code><br />
 <i>Parallel evolver for multiple arrays. </i><br />
 class <code>StepCondition&lt; array_type &gt;</code><br />
 <i>condition to be applied at every time step </i><br />
 class <code>NullCondition&lt; array_type &gt;</code><br />
 <i>null step condition </i><br />
 class <code>TridiagonalOperator</code><br />
 <i>Base implementation for tridiagonal operator. </i></p>
<h3>Typedefs</h3>
<p> typedef PdeOperator&lt; PdeBSM &gt; <code>BSMTermOperator</code><br />
 <i>Black-Scholes-Merton differential operator. </i><br />
 typedef PdeOperator&lt; PdeShortRate &gt; <code>OneFactorOperator</code><br />
 <i>Interest-rate single factor model differential operator. </i></p>
<h2>Detailed Description</h2>
<p> This framework (corresponding to the ql/FiniteDifferences directory) contains basic building blocks for the numerical solution of partial differential equations by means of finite-difference methods.</p>
<h2>Typedef Documentation</h2>
<h3>typedef PdeOperator&lt;PdeBSM&gt; BSMTermOperator</h3>
<p> Black-Scholes-Merton differential operator. </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> coefficients are tested against constant BSM operator</dl>
<h3>typedef PdeOperator&lt;PdeShortRate&gt; OneFactorOperator</h3>
<p> Interest-rate single factor model differential operator. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
