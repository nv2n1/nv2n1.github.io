---
title: "redemption(3)"
name: "redemption"
section: "3"
letter: "r"
url: "/docs/linux/man/3-redemption/"
description: "QuantLib::Bond – Base bond class."
---

<p>QuantLib::Bond &#8211; Base bond class. </p>
<h2>Synopsis</h2>
<pre><code>Real cleanPrice () const


theoretical clean price


Real dirtyPrice () const


theoretical dirty price


Real settlementValue () const


theoretical settlement value


Rate yield (const DayCounter &amp;dc, Compounding comp, Frequency freq, Real accuracy=1.0e-8, Size maxEvaluations=100) const


theoretical bond yield


Real cleanPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


clean price given a yield and settlement date


Real dirtyPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


dirty price given a yield and settlement date


Real settlementValue (Real cleanPrice) const


settlement value as a function of the clean price


Rate yield (Real cleanPrice, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date(), Real accuracy=1.0e-8, Size maxEvaluations=100) const


yield given a (clean) price and settlement date


Real cleanPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


clean price given Z-spread


Real dirtyPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


dirty price given Z-spread


virtual Real accruedAmount (Date d=Date()) const


accrued amount at a given date


bool isExpired () const


returns whether the instrument is still tradable.




Protected Member Functions
void setupExpired () const



void setupArguments (PricingEngine::arguments *) const



void fetchResults (const PricingEngine::results *) const



void addRedemptionsToCashflows (const std::vector&lt; Real &gt; &amp;redemptions=std::vector&lt; Real &gt;())



void calculateNotionalsFromCashflows ()



void setSingleRedemption (Real notional, Real redemption, const Date &amp;date)



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>. Inherited by <code>AmortizingCmsRateBond</code>, <code>AmortizingFixedRateBond</code>, <code>AmortizingFloatingRateBond</code>, <code>CallableBond</code>, <code>CmsRateBond</code>, <code>ConvertibleBond</code>, <code>FixedRateBond</code>, <code>FloatingRateBond</code>, and <code>ZeroCouponBond</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Bond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const Leg &amp;coupons=Leg())<br />
 <i>constructor for amortizing or non-amortizing bonds. </i><br />
 <code>Bond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp;maturityDate, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const Leg &amp;cashflows=Leg())<br />
 <i>old constructor for non amortizing bonds. </i><br />
 virtual <code>Rate</code> <code>nextCoupon</code> (<code>Date</code> d=<code>Date</code>()) const </p>
<p> <code>Rate</code> <code>previousCoupon</code> (<code>Date</code> d=<code>Date</code>()) const<br />
 <i>Previous coupon already paid at a given date. </i> <code>Inspectors</code><br />
 Real cleanPrice () const</p>
<p>theoretical clean price</p>
<p>Real dirtyPrice () const</p>
<p>theoretical dirty price</p>
<p>Real settlementValue () const</p>
<p>theoretical settlement value</p>
<p>Rate yield (const DayCounter &amp;dc, Compounding comp, Frequency freq, Real accuracy=1.0e-8, Size maxEvaluations=100) const</p>
<p>theoretical bond yield</p>
<p>Real cleanPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const</p>
<p>clean price given a yield and settlement date</p>
<p>Real dirtyPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const</p>
<p>dirty price given a yield and settlement date</p>
<p>Real settlementValue (Real cleanPrice) const</p>
<p>settlement value as a function of the clean price</p>
<p>Rate yield (Real cleanPrice, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date(), Real accuracy=1.0e-8, Size maxEvaluations=100) const</p>
<p>yield given a (clean) price and settlement date</p>
<p>Real cleanPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const</p>
<p>clean price given Z-spread</p>
<p>Real dirtyPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const</p>
<p>dirty price given Z-spread</p>
<p>virtual Real accruedAmount (Date d=Date()) const</p>
<p>accrued amount at a given date</p>
<p>bool isExpired () const</p>
<p>returns whether the instrument is still tradable.</p>
<p>Protected Member Functions<br />
void setupExpired () const</p>
<p>void setupArguments (PricingEngine::arguments *) const</p>
<p>void fetchResults (const PricingEngine::results *) const</p>
<p>void addRedemptionsToCashflows (const std::vector&lt; Real &gt; &amp;redemptions=std::vector&lt; Real &gt;())</p>
<p>void calculateNotionalsFromCashflows ()</p>
<p>void setSingleRedemption (Real notional, Real redemption, const Date &amp;date)</p>
<p>Protected Attributes <code>Calculations</code> </p>
<pre><code>Real cleanPrice () const


theoretical clean price


Real dirtyPrice () const


theoretical dirty price


Real settlementValue () const


theoretical settlement value


Rate yield (const DayCounter &amp;dc, Compounding comp, Frequency freq, Real accuracy=1.0e-8, Size maxEvaluations=100) const


theoretical bond yield


Real cleanPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


clean price given a yield and settlement date


Real dirtyPrice (Rate yield, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


dirty price given a yield and settlement date


Real settlementValue (Real cleanPrice) const


settlement value as a function of the clean price


Rate yield (Real cleanPrice, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date(), Real accuracy=1.0e-8, Size maxEvaluations=100) const


yield given a (clean) price and settlement date


Real cleanPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


clean price given Z-spread


Real dirtyPriceFromZSpread (Spread zSpread, const DayCounter &amp;dc, Compounding comp, Frequency freq, Date settlementDate=Date()) const


dirty price given Z-spread


virtual Real accruedAmount (Date d=Date()) const


accrued amount at a given date


bool isExpired () const


returns whether the instrument is still tradable.




Protected Member Functions
void setupExpired () const



void setupArguments (PricingEngine::arguments *) const



void fetchResults (const PricingEngine::results *) const



void addRedemptionsToCashflows (const std::vector&lt; Real &gt; &amp;redemptions=std::vector&lt; Real &gt;())



void calculateNotionalsFromCashflows ()



void setSingleRedemption (Real notional, Real redemption, const Date &amp;date)



Protected Attributes</code></pre>
<p> <code>Natural</code> <code>settlementDays_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>notionalSchedule_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>notionals_</code> </p>
<p> Leg <code>cashflows_</code> </p>
<p> Leg <code>redemptions_</code> </p>
<p> <code>Date</code> <code>maturityDate_</code> </p>
<p> <code>Date</code> <code>issueDate_</code> </p>
<p> <code>Real</code> <code>settlementValue_</code></p>
<h2>Detailed Description</h2>
<p>Base bond class. </p>
<p> Derived classes must fill the uninitialized data members. </p>
<p> <code>Warning</code></p>
<dl>
<dd>Most methods assume that the cash flows are stored sorted by date, the redemption(s) being after any cash flow at the same date. In particular, if there&#8217;s one single redemption, it must be the last cash flow,</dl>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>price/yield calculations are cross-checked for consistency.</p>
<dt>*</p>
<dd>price/yield calculations are checked against known good values.</dl>
</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Bond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp; calendar, const <code>Date</code> &amp; issueDate = <code>Date</code>(), const Leg &amp; coupons = Leg())</h3>
<p>constructor for amortizing or non-amortizing bonds. </p>
<p> Redemptions and maturity are calculated from the coupon data, if available. Therefore, redemptions must not be included in the passed cash flows.</p>
<h3><code>Bond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp; calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp; maturityDate, const <code>Date</code> &amp; issueDate = <code>Date</code>(), const Leg &amp; cashflows = Leg())</h3>
<p>old constructor for non amortizing bonds. </p>
<p> <code>Warning</code></p>
<dl>
<dd>The last passed cash flow must be the bond redemption. No other cash flow can have a date later than the redemption date.</dl>
<h2>Member Function Documentation</h2>
<h3>const Leg &amp; cashflows () const</h3>
<p><code>Note:</code></p>
<dl>
<dd>returns all the cashflows, including the redemptions.</dl>
<h3>const Leg &amp; redemptions () const</h3>
<p>returns just the redemption flows (not interest payments)</p>
<h3>const boost::shared_ptr&lt;<code>CashFlow</code>&gt;&amp; redemption () const</h3>
<p>returns the redemption, if only one is defined</p>
<h3><code>Real</code> cleanPrice () const</h3>
<p>theoretical clean price </p>
<p> The default bond settlement is used for calculation. </p>
<p> <code>Warning</code></p>
<dl>
<dd>the theoretical price calculated from a flat term structure might differ slightly from the price calculated from the corresponding yield by means of the other overload of this function. If the price from a constant yield is desired, it is advisable to use such other overload.</dl>
<h3><code>Real</code> dirtyPrice () const</h3>
<p>theoretical dirty price </p>
<p> The default bond settlement is used for calculation. </p>
<p> <code>Warning</code></p>
<dl>
<dd>the theoretical price calculated from a flat term structure might differ slightly from the price calculated from the corresponding yield by means of the other overload of this function. If the price from a constant yield is desired, it is advisable to use such other overload.</dl>
<h3><code>Real</code> settlementValue () const</h3>
<p>theoretical settlement value </p>
<p> The default bond settlement date is used for calculation.</p>
<h3><code>Rate</code> yield (const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Real</code> accuracy = 1.0e-8, Size maxEvaluations = 100) const</h3>
<p>theoretical bond yield </p>
<p> The default bond settlement and theoretical price are used for calculation.</p>
<h3><code>Real</code> cleanPrice (<code>Rate</code> yield, const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Date</code> settlementDate = <code>Date</code>()) const</h3>
<p>clean price given a yield and settlement date </p>
<p> The default bond settlement is used if no date is given.</p>
<h3><code>Real</code> dirtyPrice (<code>Rate</code> yield, const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Date</code> settlementDate = <code>Date</code>()) const</h3>
<p>dirty price given a yield and settlement date </p>
<p> The default bond settlement is used if no date is given.</p>
<h3><code>Real</code> settlementValue (<code>Real</code> cleanPrice) const</h3>
<p>settlement value as a function of the clean price </p>
<p> The default bond settlement date is used for calculation.</p>
<h3><code>Rate</code> yield (<code>Real</code> cleanPrice, const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Date</code> settlementDate = <code>Date</code>(), <code>Real</code> accuracy = 1.0e-8, Size maxEvaluations = 100) const</h3>
<p>yield given a (clean) price and settlement date </p>
<p> The default bond settlement is used if no date is given.</p>
<h3><code>Real</code> cleanPriceFromZSpread (<code>Spread</code> zSpread, const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Date</code> settlementDate = <code>Date</code>()) const</h3>
<p>clean price given Z-spread </p>
<p> Z-spread compounding, frequency, daycount are taken into account The default bond settlement is used if no date is given. For details on Z-spread refer to: &#8216;Credit Spreads Explained&#8217;, Lehman Brothers European Fixed Income Research &#8211; March 2004, D. O&#8217;Kane</p>
<h3><code>Real</code> dirtyPriceFromZSpread (<code>Spread</code> zSpread, const <code>DayCounter</code> &amp; dc, Compounding comp, <code>Frequency</code> freq, <code>Date</code> settlementDate = <code>Date</code>()) const</h3>
<p>dirty price given Z-spread </p>
<p> Z-spread compounding, frequency, daycount are taken into account The default bond settlement is used if no date is given. For details on Z-spread refer to: &#8216;Credit Spreads Explained&#8217;, Lehman Brothers European Fixed Income Research &#8211; March 2004, D. O&#8217;Kane</p>
<h3>virtual <code>Real</code> accruedAmount (<code>Date</code> d = <code>Date</code>()) const [virtual]</h3>
<p>accrued amount at a given date </p>
<p> The default bond settlement is used if no date is given.</p>
<h3>virtual <code>Rate</code> nextCoupon (<code>Date</code> d = <code>Date</code>()) const [virtual]</h3>
<p>Expected next coupon: depending on (the bond and) the given date the coupon can be historic, deterministic or expected in a stochastic sense. When the bond settlement date is used the coupon is the already-fixed not-yet-paid one. </p>
<p> The current bond settlement is used if no date is given.</p>
<h3><code>Rate</code> previousCoupon (<code>Date</code> d = <code>Date</code>()) const</h3>
<p>Previous coupon already paid at a given date. </p>
<p> Expected previous coupon: depending on (the bond and) the given date the coupon can be historic, deterministic or expected in a stochastic sense. When the bond settlement date is used the coupon is the last paid one. </p>
<p> The current bond settlement is used if no date is given.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void setupArguments (PricingEngine::arguments *) const [protected, virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>CallableBond</code>, and <code>CallableFixedRateBond</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [protected, virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void addRedemptionsToCashflows (const std::vector&lt; <code>Real</code> &gt; &amp; redemptions = std::vector&lt; <code>Real</code> &gt;()) [protected]</h3>
<p>This method can be called by derived classes in order to build redemption payments from the existing cash flows. It must be called after setting up the cashflows_ vector and will fill the notionalSchedule_, notionals_, and redemptions_ data members. </p>
<p> If given, the elements of the redemptions vector will multiply the amount of the redemption cash flow. The elements will be taken in base 100, i.e., a redemption equal to 100 does not modify the amount. </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>The cashflows_ vector must contain at least one coupon and must be sorted by date.</dl>
<h3>void setSingleRedemption (<code>Real</code> notional, <code>Real</code> redemption, const <code>Date</code> &amp; date) [protected]</h3>
<p>This method can be called by derived classes in order to build a bond with a single redemption payment. It will fill the notionalSchedule_, notionals_, and redemptions_ data members.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
