---
title: "quantlib_zeroinflationtraits(3)"
name: "quantlib_zeroinflationtraits"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zeroinflationtraits/"
description: "QuantLib::ZeroInflationTraits – Bootstrap traits to use for PiecewiseZeroInflationCurve."
---

<p>QuantLib::ZeroInflationTraits &#8211; Bootstrap traits to use for <code>PiecewiseZeroInflationCurve</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflation/piecewisezeroinflationcurve.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>BootstrapHelper</code>&lt; <code>ZeroInflationTermStructure</code> &gt; <code>helper</code> </p>
<h3>Static Public Member Functions</h3>
<p>static Size <code>maxIterations</code> () </p>
<p> static <code>Date</code> <code>initialDate</code> (const <code>ZeroInflationTermStructure</code> *t) </p>
<p> static bool <code>dummyInitialValue</code> () </p>
<p> static <code>Rate</code> <code>initialValue</code> (const <code>ZeroInflationTermStructure</code> *t) </p>
<p> static <code>Rate</code> <code>initialGuess</code> () </p>
<p> static <code>Rate</code> <code>guess</code> (const <code>ZeroInflationTermStructure</code> *, const <code>Date</code> &amp;) </p>
<p> static <code>Real</code> <code>minValueAfter</code> (Size, const std::vector&lt; <code>Rate</code> &gt; &amp;) </p>
<p> static <code>Real</code> <code>maxValueAfter</code> (Size, const std::vector&lt; <code>Rate</code> &gt; &amp;) </p>
<p> static void <code>updateGuess</code> (std::vector&lt; <code>Rate</code> &gt; &amp;data, <code>Rate</code> level, Size i) </p>
<h2>Detailed Description</h2>
<p>Bootstrap traits to use for <code>PiecewiseZeroInflationCurve</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
