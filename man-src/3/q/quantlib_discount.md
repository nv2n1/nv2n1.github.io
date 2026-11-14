---
title: "quantlib_discount(3)"
name: "quantlib_discount"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_discount/"
description: "QuantLib::Discount – Discount-curve traits."
---

<p>QuantLib::Discount &#8211; Discount-curve traits. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/bootstraptraits.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>BootstrapHelper</code>&lt; <code>YieldTermStructure</code> &gt; <code>helper</code> </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Date</code> <code>initialDate</code> (const <code>YieldTermStructure</code> *c) </p>
<p> static <code>DiscountFactor</code> <code>initialValue</code> (const <code>YieldTermStructure</code> *) </p>
<p> static bool <code>dummyInitialValue</code> () </p>
<p> static <code>DiscountFactor</code> <code>initialGuess</code> () </p>
<p> static <code>DiscountFactor</code> <code>guess</code> (const <code>YieldTermStructure</code> *c, const <code>Date</code> &amp;d) </p>
<p> static <code>DiscountFactor</code> <code>minValueAfter</code> (Size, const std::vector&lt; <code>Real</code> &gt; &amp;) </p>
<p> static <code>DiscountFactor</code> <code>maxValueAfter</code> (Size i, const std::vector&lt; <code>Real</code> &gt; &amp;data) </p>
<p> static void <code>updateGuess</code> (std::vector&lt; <code>DiscountFactor</code> &gt; &amp;data, <code>DiscountFactor</code> discount, Size i) </p>
<p> static Size <code>maxIterations</code> () </p>
<h2>Detailed Description</h2>
<p>Discount-curve traits. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
