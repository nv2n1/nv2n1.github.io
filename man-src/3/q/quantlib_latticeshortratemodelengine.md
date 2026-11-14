---
title: "quantlib_latticeshortratemodelengine(3)"
name: "quantlib_latticeshortratemodelengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_latticeshortratemodelengine/"
description: "QuantLib::LatticeShortRateModelEngine – Engine for a short-rate model specialized on a lattice."
---

<p>QuantLib::LatticeShortRateModelEngine &#8211; Engine for a short-rate model specialized on a lattice. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/latticeshortratemodelengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; ShortRateModel, Arguments, Results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LatticeShortRateModelEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, Size timeSteps) </p>
<p> <code>LatticeShortRateModelEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, const <code>TimeGrid</code> &amp;timeGrid) </p>
<p> void <code>update</code> () </p>
<h3>Protected Attributes</h3>
<p><code>TimeGrid</code> <code>timeGrid_</code> </p>
<p> Size <code>timeSteps_</code> </p>
<p> boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>lattice_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Arguments, class Results&gt; class QuantLib::LatticeShortRateModelEngine&lt; Arguments, Results &gt;</h3>
<p>Engine for a short-rate model specialized on a lattice. </p>
<p> Derived engines only need to implement the calculate() method</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>GenericEngine&lt; Arguments, Results &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
