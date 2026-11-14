---
title: "bc_type(3)"
name: "bc_type"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bc_type/"
description: "QuantLib::ExplicitEuler – Forward Euler scheme for finite difference methods"
---

<h2 class="name">NAME</h2>
<p> QuantLib::ExplicitEuler &#8211; Forward Euler scheme for finite difference methods </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/finitedifferences/expliciteuler.hpp&gt; </p>
<p> Inherits <code>MixedScheme&lt; Operator &gt;</code>. </p>
<h3>Public Types</h3>
<p> typedef OperatorTraits&lt; Operator &gt; <code>traits</code> </p>
<p> typedef traits::operator_type <code>operator_type</code> </p>
<p> typedef traits::array_type <code>array_type</code> </p>
<p> typedef <code>traits::bc_type</code> <code>bc_type</code> </p>
<p> typedef traits::bc_set <code>bc_set</code> </p>
<p> typedef <code>traits::condition_type</code> <code>condition_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>ExplicitEuler</code> (const operator_type &amp;L, const std::vector&lt; boost::shared_ptr&lt; <code>bc_type</code> &gt; &gt; &amp;bcs) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Operator&gt; class QuantLib::ExplicitEuler&lt; Operator &gt;</h3>
<p> Forward Euler scheme for finite difference methods </p>
<p> See sect. <code>Finite-differences framework</code> for details on the method. </p>
<p> In this implementation, the passed operator must be derived from either TimeConstantOperator or TimeDependentOperator. Also, it must implement at least the following interface: </p>
<pre><code>
typedef... array_type;
// copy constructor/assignment
// (these will be provided by the compiler if none is defined)
Operator(const Operator &amp;);
Operator &amp;operator=(const Operator &amp;);
// inspectors
Size size();
// modifiers
void setTime(Time t);
// operator interface
array_type applyTo(const array_type &amp;);
static Operator identity(Size size);
// operator algebra
Operator operator*(Real, const Operator &amp;);
Operator operator-(const Operator &amp;, const Operator &amp;);
</code></pre>
<p> <code>Possible enhancements</code></p>
<dl>
<dt>
<dd> add Richardson extrapolation</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
