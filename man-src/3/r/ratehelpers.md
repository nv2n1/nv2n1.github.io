---
title: "ratehelpers(3)"
name: "ratehelpers"
section: "3"
letter: "r"
url: "/docs/linux/man/3-ratehelpers/"
description: "ql/termstructures/yield/ratehelpers.hpp – deposit, FRA, futures, and swap rate helpers"
---

<p>ql/termstructures/yield/ratehelpers.hpp &#8211; deposit, FRA, futures, and swap rate helpers </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/termstructures/bootstraphelper.hpp&gt;

#include &lt;ql/instruments/vanillaswap.hpp&gt;

#include &lt;ql/instruments/bmaswap.hpp&gt;

#include &lt;ql/time/calendar.hpp&gt;

#include &lt;ql/time/daycounter.hpp&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>FuturesRateHelper</code><br />
 <i>Rate helper for bootstrapping over </i><code>IborIndex</code> futures prices.<br />
 class <code>RelativeDateRateHelper</code><br />
 <i>Rate helper with date schedule relative to the global evaluation date. </i><br />
 class <code>DepositRateHelper</code><br />
 <i>Rate helper for bootstrapping over deposit rates. </i><br />
 class <code>FraRateHelper</code><br />
 <i>Rate helper for bootstrapping over FRA rates. </i><br />
 class <code>SwapRateHelper</code><br />
 <i>Rate helper for bootstrapping over swap rates. </i><br />
 class <code>BMASwapRateHelper</code><br />
 <i>Rate helper for bootstrapping over BMA swap rates. </i></p>
<h3>Typedefs</h3>
<p>typedef BootstrapHelper&lt; YieldTermStructure &gt; <code>RateHelper</code></p>
<h2>Detailed Description</h2>
<p>deposit, FRA, futures, and swap rate helpers</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
