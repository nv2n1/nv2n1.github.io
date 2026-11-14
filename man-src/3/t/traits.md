---
title: "traits(3)"
name: "traits"
section: "3"
letter: "t"
url: "/docs/linux/man/3-traits/"
description: "QuantLib::CrankNicolson – Crank-Nicolson scheme for finite difference methods."
---

<p>QuantLib::CrankNicolson &#8211; Crank-Nicolson scheme for finite difference methods. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/methods/finitedifferences/cranknicolson.hpp&gt;</code></pre>
<p> Inherits <code>MixedScheme&lt; Operator &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef OperatorTraits&lt; Operator &gt; <code>traits</code> </p>
<p> typedef traits::operator_type <code>operator_type</code> </p>
<p> typedef traits::array_type <code>array_type</code> </p>
<p> typedef traits::bc_set <code>bc_set</code> </p>
<p> typedef <code>traits::condition_type</code> <code>condition_type</code></p>
<h3>Public Member Functions</h3>
<p><code>CrankNicolson</code> (const operator_type &amp;L, const bc_set &amp;bcs)</p>
<h2>Detailed Description</h2>
<h3>template&lt;class Operator&gt; class QuantLib::CrankNicolson&lt; Operator &gt;</h3>
<p>Crank-Nicolson scheme for finite difference methods. </p>
<p> In this implementation, the passed operator must be derived from either TimeConstantOperator or TimeDependentOperator. Also, it must implement at least the following interface: </p>
<pre> typedef ... array_type;
 // copy constructor/assignment
 // (these will be provided by the compiler if none is defined)
 Operator(const Operator&amp;);
 Operator&amp; operator=(const Operator&amp;);
 // inspectors
 Size size();
 // modifiers
 void setTime(Time t);
 // operator interface
 array_type applyTo(const array_type&amp;);
 array_type solveFor(const array_type&amp;);
 static Operator identity(Size size);
 // operator algebra
 Operator operator*(Real, const Operator&amp;);
 Operator operator+(const Operator&amp;, const Operator&amp;);
 Operator operator+(const Operator&amp;, const Operator&amp;);</pre>
<p><code>Warning</code></p>
<dl>
<dd>The differential operator must be linear for this evolver to work.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
