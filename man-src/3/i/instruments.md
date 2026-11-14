---
title: "instruments(3)"
name: "instruments"
section: "3"
letter: "i"
url: "/docs/linux/man/3-instruments/"
description: "Financial instruments –"
---

<h2 class="name">NAME</h2>
<p> Financial instruments &#8211; </p>
<h3>Classes</h3>
<p> class <code>DigitalCoupon</code><br />
 <i>Digital-payoff coupon. </i><br />
 class <code>CallableBond</code><br />
 <i>Callable bond base class. </i><br />
 class <code>CallableFixedRateBond</code><br />
 <i>callable/puttable fixed rate bond </i><br />
 class <code>CallableZeroCouponBond</code><br />
 <i>callable/puttable zero coupon bond </i><br />
 class <code>Commodity</code><br />
 <i></i><code>Commodity</code> base class.<br />
 class <code>EnergyCommodity</code><br />
 <i>Energy commodity class. </i><br />
 class <code>EnergyFuture</code><br />
 <i>Energy future. </i><br />
 class <code>DividendBarrierOption</code><br />
 <i>Single-asset barrier option with discrete dividends. </i><br />
 class <code>VarianceOption</code><br />
 <i>Variance option. </i><br />
 class <code>ContinuousAveragingAsianOption</code><br />
 <i>Continuous-averaging Asian option. </i><br />
 class <code>DiscreteAveragingAsianOption</code><br />
 <i>Discrete-averaging Asian option. </i><br />
 class <code>AssetSwap</code><br />
 <i>Bullet bond vs Libor swap. </i><br />
 class <code>BarrierOption</code><br />
 <i>Barrier option on a single asset. </i><br />
 class <code>BasketOption</code><br />
 <i></i><code>Basket</code> option on a number of assets.<br />
 class <code>Bond</code><br />
 <i>Base bond class. </i><br />
 class <code>CmsRateBond</code><br />
 <i>CMS-rate bond. </i><br />
 class <code>FixedRateBond</code><br />
 <i>fixed-rate bond </i><br />
 class <code>FloatingRateBond</code><br />
 <i>floating-rate bond (possibly capped and/or floored) </i><br />
 class <code>ZeroCouponBond</code><br />
 <i>zero-coupon bond </i><br />
 class <code>CapFloor</code><br />
 <i>Base class for cap-like instruments. </i><br />
 class <code>Cap</code><br />
 <i>Concrete cap class. </i><br />
 class <code>Floor</code><br />
 <i>Concrete floor class. </i><br />
 class <code>Collar</code><br />
 <i>Concrete collar class. </i><br />
 class <code>CliquetOption</code><br />
 <i>cliquet (Ratchet) option </i><br />
 class <code>CompositeInstrument</code><br />
 <i>Composite instrument </i><br />
 class <code>CreditDefaultSwap</code><br />
 <i>Credit default swap. </i><br />
 class <code>DividendVanillaOption</code><br />
 <i>Single-asset vanilla option (no barriers) with discrete dividends. </i><br />
 class <code>EuropeanOption</code><br />
 <i>European option on a single asset. </i><br />
 class <code>FixedRateBondForward</code><br />
 <i>Forward contract on a fixed-rate bond </i><br />
 class <code>Forward</code><br />
 <i>Abstract base forward class. </i><br />
 class <code>ForwardVanillaOption</code><br />
 <i>Forward version of a vanilla option </i><br />
 class <code>InflationSwap</code><br />
 <i>Abstract base class for inflation swaps. </i><br />
 class <code>ContinuousFloatingLookbackOption</code><br />
 <i>Continuous-floating lookback option. </i><br />
 class <code>ContinuousFixedLookbackOption</code><br />
 <i>Continuous-fixed lookback option. </i><br />
 class <code>PagodaOption</code><br />
 <i>Roofed Asian option on a number of assets. </i><br />
 class <code>QuantoBarrierOption</code><br />
 <i>Quanto version of a barrier option. </i><br />
 class <code>QuantoForwardVanillaOption</code><br />
 <i>Quanto version of a forward vanilla option. </i><br />
 class <code>QuantoVanillaOption</code><br />
 <i>quanto version of a vanilla option </i><br />
 class <code>Stock</code><br />
 <i>Simple stock class. </i><br />
 class <code>Swap</code><br />
 <i>Interest rate swap. </i><br />
 class <code>Swaption</code><br />
 <i>Swaption class </i><br />
 class <code>VanillaOption</code><br />
 <i>Vanilla option (no discrete dividends, no barriers) on a single asset. </i><br />
 class <code>VanillaSwap</code><br />
 <i>Plain-vanilla swap. </i><br />
 class <code>VarianceSwap</code><br />
 <i>Variance swap. </i></p>
<h2>Detailed Description</h2>
<p> Since version 0.3.4, the Instrument class was reworked as shown in the following figure. </p>
<p> On the one hand, the checking of the expiration condition is now performed in a method isExpired() separated from the actual calculation, and a setupExpired() method is provided. The latter sets the NPV to 0.0 and can be extended in derived classes should any other results be returned. </p>
<p> On the other hand, the pricing-engine machinery previously contained in the Option class was moved upwards to the Instrument class. Also, the setupEngine() method was replaced by a setupArguments(Arguments*) method. This allows one to cleanly implement containment of instruments with code such as: </p>
<pre><code>
class FooArguments : public Arguments
{
    ...
};
class Foo : public Instrument
{
  public:
    void setupArguments(Arguments *);
    ...
};
class FooOptionArguments : public FooArguments
{
    ...
};
class FooOption : public Option
{
  private:
    Foo underlying_;

  public:
    void setupArguments(Arguments *args)
    {
        underlying_.setupArguments(args);
        // set the option-specific part
    }
    ...
};
</code></pre>
<p> which was more difficult to write with setupEngine(). </p>
<p> Therefore, there are now two ways to inherit from Instrument, namely: </p>
<dl>
<dt>1.</p>
<dd> implement the isExpired method, and completely override the performCalculations method so that it bypasses the pricing-engine machinery. If the class declared any other results beside NPV_ and errorEstimate_, the setupExpired method should also be extended so that those results are set to a value suitable for an expired instrument. This was the migration path taken for all instruments not previously deriving from the Option class.</p>
<dt>2.</p>
<dd> define suitable argument and result classes for the instrument and implement the isExpired and setupArguments methods, reusing the pricing-engine machinery provided by the default performCalculations method. The latter can be extended by first calling the default implementation and then performing any additional tasks required by the instrument&#8212;most often, copying additional results from the pricing engine results to the corresponding data members of the instrument. As in the previous case, the setupExpired method can be extended to account for such extra data members.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
