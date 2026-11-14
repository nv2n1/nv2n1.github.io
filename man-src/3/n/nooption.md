---
title: "nooption(3)"
name: "nooption"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nooption/"
description: "ql/cashflows/cashflowvectors.hpp – Cash flow vector builders."
---

<p>ql/cashflows/cashflowvectors.hpp &#8211; Cash flow vector builders. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/cashflows/fixedratecoupon.hpp&gt;

#include &lt;ql/cashflows/replication.hpp&gt;

#include &lt;ql/time/schedule.hpp&gt;

#include &lt;ql/utilities/null.hpp&gt;

#include &lt;ql/utilities/vectors.hpp&gt;

#include &lt;ql/position.hpp&gt;

#include &lt;ql/indexes/swapindex.hpp&gt;</code></pre>
<h3>Functions</h3>
<p>Rate <code>effectiveFixedRate</code> (const std::vector&lt; Spread &gt; &amp;spreads, const std::vector&lt; Rate &gt; &amp;caps, const std::vector&lt; Rate &gt; &amp;floors, Size i) </p>
<p> bool <code>noOption</code> (const std::vector&lt; Rate &gt; &amp;caps, const std::vector&lt; Rate &gt; &amp;floors, Size i) </p>
<p> template&lt;typename InterestRateIndexType , typename FloatingCouponType , typename CappedFlooredCouponType &gt; Leg <code>FloatingLeg</code> (const std::vector&lt; Real &gt; &amp;nominals, const Schedule &amp;schedule, const boost::shared_ptr&lt; InterestRateIndexType &gt; &amp;index, const DayCounter &amp;paymentDayCounter, BusinessDayConvention paymentAdj, const std::vector&lt; Natural &gt; &amp;fixingDays, const std::vector&lt; Real &gt; &amp;gearings, const std::vector&lt; Spread &gt; &amp;spreads, const std::vector&lt; Rate &gt; &amp;caps, const std::vector&lt; Rate &gt; &amp;floors, bool isInArrears, bool isZero) </p>
<p> template&lt;typename InterestRateIndexType , typename FloatingCouponType , typename DigitalCouponType &gt; Leg <code>FloatingDigitalLeg</code> (const std::vector&lt; Real &gt; &amp;nominals, const Schedule &amp;schedule, const boost::shared_ptr&lt; InterestRateIndexType &gt; &amp;index, const DayCounter &amp;paymentDayCounter, BusinessDayConvention paymentAdj, const std::vector&lt; Natural &gt; &amp;fixingDays, const std::vector&lt; Real &gt; &amp;gearings, const std::vector&lt; Spread &gt; &amp;spreads, bool isInArrears, const std::vector&lt; Rate &gt; &amp;callStrikes, Position::Type callPosition, bool isCallATMIncluded, const std::vector&lt; Rate &gt; &amp;callDigitalPayoffs, const std::vector&lt; Rate &gt; &amp;putStrikes, Position::Type putPosition, bool isPutATMIncluded, const std::vector&lt; Rate &gt; &amp;putDigitalPayoffs, const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication)</p>
<h2>Detailed Description</h2>
<p>Cash flow vector builders.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
