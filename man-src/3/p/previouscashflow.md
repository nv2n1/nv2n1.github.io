---
title: "previouscashflow(3)"
name: "previouscashflow"
section: "3"
letter: "p"
url: "/docs/linux/man/3-previouscashflow/"
description: "QuantLib::CashFlows – cashflow-analysis functions"
---

<p>QuantLib::CashFlows &#8211; cashflow-analysis functions </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/cashflows/cashflows.hpp&gt;</code></pre>
<h3>Static Public Member Functions</h3>
<p>static Leg::const_iterator <code>previousCashFlow</code> (const Leg &amp;leg, <code>Date</code> refDate=<code>Date</code>()) </p>
<p> static Leg::const_iterator <code>nextCashFlow</code> (const Leg &amp;leg, <code>Date</code> refDate=<code>Date</code>()) </p>
<p> static <code>Rate</code> <code>previousCouponRate</code> (const Leg &amp;leg, const <code>Date</code> &amp;refDate=<code>Date</code>()) </p>
<p> static <code>Rate</code> <code>nextCouponRate</code> (const Leg &amp;leg, const <code>Date</code> &amp;refDate=<code>Date</code>()) </p>
<p> static <code>Date</code> <code>startDate</code> (const Leg &amp;leg) </p>
<p> static <code>Date</code> <code>maturityDate</code> (const Leg &amp;leg) </p>
<p> static <code>Real</code> <code>npv</code> (const Leg &amp;leg, const <code>YieldTermStructure</code> &amp;discountCurve, <code>Date</code> settlementDate=<code>Date</code>(), const <code>Date</code> &amp;npvDate=<code>Date</code>(), <code>Natural</code> exDividendDays=0)<br />
 <i>NPV of the cash flows. </i><br />
 static <code>Real</code> <code>npv</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>NPV of the cash flows. </i><br />
 static <code>Real</code> <code>bps</code> (const Leg &amp;leg, const <code>YieldTermStructure</code> &amp;discountCurve, <code>Date</code> settlementDate=<code>Date</code>(), const <code>Date</code> &amp;npvDate=<code>Date</code>(), <code>Natural</code> exDividendDays=0)<br />
 <i>Basis-point sensitivity of the cash flows. </i><br />
 static <code>Real</code> <code>bps</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>Basis-point sensitivity of the cash flows. </i><br />
 static <code>Rate</code> <code>atmRate</code> (const Leg &amp;leg, const <code>YieldTermStructure</code> &amp;discountCurve, const <code>Date</code> &amp;settlementDate=<code>Date</code>(), const <code>Date</code> &amp;npvDate=<code>Date</code>(), <code>Natural</code> exDividendDays=0, <code>Real</code> npv=<code>Null</code>&lt; <code>Real</code> &gt;())<br />
 <i>At-the-money rate of the cash flows. </i><br />
 static <code>Rate</code> <code>irr</code> (const Leg &amp;leg, <code>Real</code> marketPrice, const <code>DayCounter</code> &amp;dayCounter, Compounding compounding, <code>Frequency</code> frequency=NoFrequency, <code>Date</code> settlementDate=<code>Date</code>(), <code>Real</code> accuracy=1.0e-10, Size maxIterations=100, Rate guess=0.05)<br />
 <i>Internal rate of return. </i><br />
 static <code>Time</code> <code>duration</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;y, Duration::Type type=Duration::Modified, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>Cash-flow duration. </i><br />
 static <code>Real</code> <code>convexity</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;y, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>Cash-flow convexity. </i><br />
 static <code>Real</code> <code>basisPointValue</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;y, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>Basis-point value. </i><br />
 static <code>Real</code> <code>yieldValueBasisPoint</code> (const Leg &amp;leg, const <code>InterestRate</code> &amp;y, <code>Date</code> settlementDate=<code>Date</code>())<br />
 <i>Yield value of a basis point. </i></p>
<h2>Detailed Description</h2>
<p>cashflow-analysis functions </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add tests</dl>
<h2>Member Function Documentation</h2>
<h3>static <code>Real</code> npv (const Leg &amp; leg, const <code>YieldTermStructure</code> &amp; discountCurve, <code>Date</code> settlementDate = <code>Date</code>(), const <code>Date</code> &amp; npvDate = <code>Date</code>(), <code>Natural</code> exDividendDays = 0) [static]</h3>
<p>NPV of the cash flows. </p>
<p> The NPV is the sum of the cash flows, each discounted according to the given term structure.</p>
<h3>static <code>Real</code> npv (const Leg &amp; leg, const <code>InterestRate</code> &amp;, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>NPV of the cash flows. </p>
<p> The NPV is the sum of the cash flows, each discounted according to the given constant interest rate. The result is affected by the choice of the interest-rate compounding and the relative frequency and day counter.</p>
<h3>static <code>Real</code> bps (const Leg &amp; leg, const <code>YieldTermStructure</code> &amp; discountCurve, <code>Date</code> settlementDate = <code>Date</code>(), const <code>Date</code> &amp; npvDate = <code>Date</code>(), <code>Natural</code> exDividendDays = 0) [static]</h3>
<p>Basis-point sensitivity of the cash flows. </p>
<p> The result is the change in NPV due to a uniform 1-basis-point change in the rate paid by the cash flows. The change for each coupon is discounted according to the given term structure.</p>
<h3>static <code>Real</code> bps (const Leg &amp; leg, const <code>InterestRate</code> &amp;, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>Basis-point sensitivity of the cash flows. </p>
<p> The result is the change in NPV due to a uniform 1-basis-point change in the rate paid by the cash flows. The change for each coupon is discounted according to the given constant interest rate. The result is affected by the choice of the interest-rate compounding and the relative frequency and day counter.</p>
<h3>static <code>Rate</code> atmRate (const Leg &amp; leg, const <code>YieldTermStructure</code> &amp; discountCurve, const <code>Date</code> &amp; settlementDate = <code>Date</code>(), const <code>Date</code> &amp; npvDate = <code>Date</code>(), <code>Natural</code> exDividendDays = 0, <code>Real</code> npv = <code>Null</code>&lt; <code>Real</code> &gt;()) [static]</h3>
<p>At-the-money rate of the cash flows. </p>
<p> The result is the fixed rate for which a fixed rate cash flow vector, equivalent to the input vector, has the required NPV according to the given term structure. If the required NPV is not given, the input cash flow vector&#8217;s NPV is used instead.</p>
<h3>static <code>Rate</code> irr (const Leg &amp; leg, <code>Real</code> marketPrice, const <code>DayCounter</code> &amp; dayCounter, Compounding compounding, <code>Frequency</code> frequency = NoFrequency, <code>Date</code> settlementDate = <code>Date</code>(), <code>Real</code> accuracy = 1.0e-10, Size maxIterations = 100, <code>Rate</code> guess = 0.05) [static]</h3>
<p>Internal rate of return. </p>
<p> The IRR is the interest rate at which the NPV of the cash flows equals the given market price. The function verifies the theoretical existance of an IRR and numerically establishes the IRR to the desired precision.</p>
<h3>static <code>Time</code> duration (const Leg &amp; leg, const <code>InterestRate</code> &amp; y, Duration::Type type = Duration::Modified, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>Cash-flow duration. </p>
<p> The simple duration of a string of cash flows is defined as [ D_{mathrm{simple}} = ac{um t_i c_i B(t_i)}{um c_i B(t_i)} ] where $ c_i $ is the amount of the $ i $-th cash flow, $ t_i $ is its payment time, and $ B(t_i) $ is the corresponding discount according to the passed yield. </p>
<p> The modified duration is defined as [ D_{mathrm{modified}} = -ac{1}{P} ac{<br />
 artial P}{<br />
 artial y} ] where $ P $ is the present value of the cash flows according to the given IRR $ y $. </p>
<p> The Macaulay duration is defined for a compounded IRR as [ D_{mathrm{Macaulay}} = </p>
<hr>
<p>d}} ] where $ y $ is the IRR and $ N $ is the number of cash flows per year.</p>
<h3>static <code>Real</code> convexity (const Leg &amp; leg, const <code>InterestRate</code> &amp; y, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>Cash-flow convexity. </p>
<p> The convexity of a string of cash flows is defined as [ C = ac{1}{P} ac{<br />
 artial^2 P}{<br />
 artial y^2} ] where $ P $ is the present value of the cash flows according to the given IRR $ y $.</p>
<h3>static <code>Real</code> basisPointValue (const Leg &amp; leg, const <code>InterestRate</code> &amp; y, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>Basis-point value. </p>
<p> Obtained by setting dy = 0.0001 in the 2nd-order Taylor series expansion.</p>
<h3>static <code>Real</code> yieldValueBasisPoint (const Leg &amp; leg, const <code>InterestRate</code> &amp; y, <code>Date</code> settlementDate = <code>Date</code>()) [static]</h3>
<p>Yield value of a basis point. </p>
<p> The yield value of a one basis point change in price is the derivative of the yield with respect to the price multiplied by 0.01</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
