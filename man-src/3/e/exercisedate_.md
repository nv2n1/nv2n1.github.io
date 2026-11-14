---
title: "exercisedate_(3)"
name: "exercisedate_"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exercisedate_/"
description: "QuantLib::FDVanillaEngine – Finite-differences pricing engine for BSM one asset options."
---

<p>QuantLib::FDVanillaEngine &#8211; Finite-differences pricing engine for BSM one asset options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/fdvanillaengine.hpp&gt; </p>
<p> Inherited by <code>FDEuropeanEngine</code>, FDMultiPeriodEngine, and <code>FDStepConditionEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FDVanillaEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps, Size gridPoints, bool timeDependent=false) </p>
<p> const <code>Array</code> &amp; <code>grid</code> () const </p>
<h3>Protected Types</h3>
<p>typedef <code>BoundaryCondition</code>&lt; <code>TridiagonalOperator</code> &gt; <code>bc_type</code> </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>setupArguments</code> (const PricingEngine::arguments *) const </p>
<p> virtual void <code>setGridLimits</code> () const </p>
<p> virtual void <code>setGridLimits</code> (Real, <code>Time</code>) const </p>
<p> virtual void <code>initializeInitialCondition</code> () const </p>
<p> virtual void <code>initializeBoundaryConditions</code> () const </p>
<p> virtual void <code>initializeOperator</code> () const </p>
<p> virtual <code>Time</code> <code>getResidualTime</code> () const </p>
<p> void <code>ensureStrikeInGrid</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> Size <code>timeSteps_</code> </p>
<p> Size <code>gridPoints_</code> </p>
<p> bool <code>timeDependent_</code> </p>
<p> Real <code>requiredGridValue_</code> </p>
<p> <code>Date</code> <code>exerciseDate_</code> </p>
<p> boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff_</code> </p>
<p> <code>TridiagonalOperator</code> <code>finiteDifferenceOperator_</code> </p>
<p> <code>SampledCurve</code> <code>intrinsicValues_</code> </p>
<p> std::vector&lt; boost::shared_ptr&lt; <code>bc_type</code> &gt; &gt; <code>BCs_</code> </p>
<p> Real <code>sMin_</code> </p>
<p> Real <code>center_</code> </p>
<p> Real <code>sMax_</code> </p>
<h2>Detailed Description</h2>
<p>Finite-differences pricing engine for BSM one asset options. </p>
<p> The name is a misnomer as this is a base class for any finite difference scheme. Its main job is to handle grid layout. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
