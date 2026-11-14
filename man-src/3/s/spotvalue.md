---
title: "spotvalue(3)"
name: "spotvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spotvalue/"
description: "QuantLib::FixedRateBondForward – Forward contract on a fixed-rate bond"
---

<p>QuantLib::FixedRateBondForward &#8211; Forward contract on a fixed-rate bond </p>
<h2>Synopsis</h2>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Forward</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 void performCalculations () const</p>
<p>Protected Attributes <code>Calculations</code> </p>
<p> <code>Real</code> <code>forwardPrice</code> () const<br />
 <i>(dirty) forward bond price </i><br />
 <code>Real</code> <code>cleanForwardPrice</code> () const<br />
 <i>(dirty) forward bond price minus accrued on bond at delivery </i><br />
 <code>Real</code> <code>spotIncome</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;incomeDiscountCurve) const<br />
 <i>NPV of bond coupons discounted using incomeDiscountCurve. </i><br />
 <code>Real</code> <code>spotValue</code> () const<br />
 <i>NPV of underlying bond. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>FixedRateBond</code> &gt; <code>fixedCouponBond_</code></p>
<h2>Detailed Description</h2>
<p>Forward contract on a fixed-rate bond </p>
<p> 1. valueDate refers to the settlement date of the bond forward contract. maturityDate is the delivery (or repurchase) date for the underlying bond (not the bond&#8217;s maturity date). </p>
<p> 2. Relevant formulas used in the calculations ($P$ refers to a price): </p>
<p> a. $ P_{CleanFwd}(t) = P_{DirtyFwd}(t) &#8211; AI(t=deliveryDate) $ where $ AI $ refers to the accrued interest on the underlying bond. </p>
<p> b. $ P_{DirtyFwd}(t) = ac{P_{DirtySpot}(t) &#8211; SpotIncome(t)} {discountCurve-&gt;discount(t=deliveryDate)} $ </p>
<p> c. $ SpotIncome(t) = um_i </p>
<hr>
<p>s incomeDiscountCurve-&gt;discount(t_i) ight) $ where $ CF_i $ represents the ith bond cash flow (coupon payment) associated with the underlying bond falling between the settlementDate and the deliveryDate. (Note the two different discount curves used in b. and c.) </p>
<p> <code>Example: </code> <code>valuation of a repo on a fixed-rate bond </code> </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>Add preconditions and tests</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>Create switch- if coupon goes to seller is toggled on, don&#8217;t consider income in the $ P_{DirtyFwd}(t) $ calculation.</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>Verify this works when the underlying is paper (in which case ignore all AI.)</dl>
<p> <code>Warning</code></p>
<dl>
<dd>This class still needs to be rigorously tested</dl>
<p> <code>Examples: </code> </p>
<p> <code>Repo.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>FixedRateBondForward</code> (const <code>Date</code> &amp; valueDate, const <code>Date</code> &amp; maturityDate, Position::Type type, <code>Real</code> strike, <code>Natural</code> settlementDays, const <code>DayCounter</code> &amp; dayCounter, const <code>Calendar</code> &amp; calendar, <code>BusinessDayConvention</code> businessDayConvention, const boost::shared_ptr&lt; <code>FixedRateBond</code> &gt; &amp; fixedCouponBond, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; discountCurve = <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;(), const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; incomeDiscountCurve = <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;())</h3>
<p>If strike is given in the constructor, can calculate the NPV of the contract via <code>NPV()</code>. </p>
<p> If strike/forward price is desired, it can be obtained via <code>forwardPrice()</code>. In this case, the strike variable in the constructor is irrelevant and will be ignored.</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> spotIncome (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; incomeDiscountCurve) const [virtual]</h3>
<p>NPV of bond coupons discounted using incomeDiscountCurve. </p>
<p> Here only coupons between max(evaluation date,settlement date) and maturity date of bond forward contract are considered income. </p>
<p> Implements <code>Forward</code>.</p>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Forward</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
