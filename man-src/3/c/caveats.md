---
title: "caveats(3)"
name: "caveats"
section: "3"
letter: "c"
url: "/docs/linux/man/3-caveats/"
description: "caveats – Caveats"
---

<h2 class="name">NAME</h2>
<p> caveats &#8211; Caveats<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class Actual365Fixed</code></p>
<dd> According to ISDA, &#8216;Actual/365&#8217; (without &#8216;Fixed&#8217;) is an alias for &#8216;Actual/Actual (ISDA)&#8217; (see ActualActual.) If Actual/365 is not explicitly specified as fixed in an instrument specification, you might want to double-check its meaning.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BarrierOption::impliedVolatility</code>(Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const</p>
<dd> see VanillaOption for notes on implied-volatility calculation.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BespokeCalendar::BespokeCalendar</code>(const std::string &amp;name=&#8221;)</p>
<dd> different bespoke calendars created with the same name (or different bespoke calendars created with no name) will compare as equal.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BlackAtmVolCurve::BlackAtmVolCurve</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCallableFixedRateBondEngine</code></p>
<dd> This class has yet to be tested</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCallableZeroCouponBondEngine</code></p>
<dd> This class has yet to be tested.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackSwaptionEngine</code></p>
<dd> The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BlackVarianceTermStructure::BlackVarianceTermStructure</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BlackVolatilityTermStructure::BlackVolatilityTermStructure</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BlackVolSurface::BlackVolSurface</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BlackVolTermStructure::BlackVolTermStructure</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Bond</code></p>
<dd> Most methods assume that the cash flows are stored sorted by date, the redemption(s) being after any cash flow at the same date. In particular, if there&#8217;s one single redemption, it must be the last cash flow,</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Bond::cleanPrice</code>() const</p>
<dd> the theoretical price calculated from a flat term structure might differ slightly from the price calculated from the corresponding yield by means of the other overload of this function. If the price from a constant yield is desired, it is advisable to use such other overload.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Bond::dirtyPrice</code>() const</p>
<dd> the theoretical price calculated from a flat term structure might differ slightly from the price calculated from the corresponding yield by means of the other overload of this function. If the price from a constant yield is desired, it is advisable to use such other overload.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Bond::Bond</code>(Natural settlementDays, const Calendar &amp;calendar, Real faceAmount, const Date &amp;maturityDate, const Date &amp;issueDate=Date(), const Leg &amp;cashflows=Leg())</p>
<dd> The last passed cash flow must be the bond redemption. No other cash flow can have a date later than the redemption date.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BootstrapHelper::setTermStructure</code>(TS *)</p>
<dd> Being a pointer and not a shared_ptr, the term structure is not guaranteed to remain allocated for the whole life of the rate helper. It is responsibility of the programmer to ensure that the pointer remains valid. It is advised that this method is called only inside the term structure being bootstrapped, setting the pointer to <code>this</code>, i.e., the term structure itself.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CADLibor</code></p>
<dd> This is the rate fixed in London by BBA. Use CDOR if you&#8217;re interested in the Canadian fixing by IDA.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Calendar::name</code>() const</p>
<dd> This method is used for output and comparison between calendars. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::CallableBondVolatilityStructure::CallableBondVolatilityStructure</code>(const DayCounter &amp;dc=DayCounter(), BusinessDayConvention bdc=Following)</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::CapFloorTermVolatilityStructure::CapFloorTermVolatilityStructure</code>(const Calendar &amp;cal, BusinessDayConvention bdc, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Cdor</code></p>
<dd> This is the rate fixed in Canada by IDA. Use CADLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></p>
<dd> the current implementation does not take premium accrual into account</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></p>
<dd> the current implementation quietly assumes that the expiry equals the start date of the underlying CDS</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CHFLibor</code></p>
<dd> This is the rate fixed in London by BBA. Use ZIBOR if you&#8217;re interested in the Zurich fixing.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CmsCoupon</code></p>
<dd> This class does not perform any date adjustment, i.e., the start and end date passed upon construction should be already rolled to a business day.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CompositeInstrument</code></p>
<dd> Methods that drive the calculation directly (such as recalculate(), freeze() and others) might not work correctly.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ConvertibleFixedCouponBond</code></p>
<dd> Most methods inherited from Bond (such as yield or the yield-based dirtyPrice and cleanPrice) refer to the underlying plain-vanilla bond and do not take convertibility and callability into account.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ConvertibleFloatingRateBond</code></p>
<dd> Most methods inherited from Bond (such as yield or the yield-based dirtyPrice and cleanPrice) refer to the underlying plain-vanilla bond and do not take convertibility and callability into account.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ConvertibleZeroCouponBond</code></p>
<dd> Most methods inherited from Bond (such as yield or the yield-based dirtyPrice and cleanPrice) refer to the underlying plain-vanilla bond and do not take convertibility and callability into account.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Coupon::Coupon</code>(Real nominal, const Date &amp;paymentDate, const Date &amp;accrualStartDate, const Date &amp;accrualEndDate, const Date &amp;refPeriodStart=Date(), const Date &amp;refPeriodEnd=Date())</p>
<dd> the coupon does not adjust the payment date which must already be a business day.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CrankNicolson&lt; Operator &gt;</code></p>
<dd> The differential operator must be linear for this evolver to work.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CreditDefaultSwap</code></p>
<dd> if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-spread calculation. This might not be what you want.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CubicBSplinesFitting</code></p>
<dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DailyTenorEuribor</code></p>
<dd> This is the rate fixed by the ECB. Use EurLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DailyTenorEURLibor</code></p>
<dd> This is the rate fixed in London by BBA. Use Euribor if you&#8217;re interested in the fixing by the ECB.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::DayCounter::name</code>() const</p>
<dd> This method is used for output and comparison between day counters. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::DefaultDensityStructure::DefaultDensityStructure</code>(const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::DefaultProbabilityTermStructure::DefaultProbabilityTermStructure</code>(const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DiscretizedOption</code></p>
<dd> it is advised that derived classes take care of creating and initializing themselves an instance of the underlying.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Disposable&lt; T &gt;</code></p>
<dd> In order to avoid copies in code such as shown above, the conversion from T to Disposable&lt;T&gt; is destructive, i.e., it does <code>not</code> preserve the state of the original object. Therefore, it is necessary for the developer to avoid code such as</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::DividendVanillaOption::impliedVolatility</code>(Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const</p>
<dd> see VanillaOption for notes on implied-volatility calculation.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::EquityFXVolSurface::EquityFXVolSurface</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Euribor</code></p>
<dd> This is the rate fixed by the ECB. Use EurLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class EURLibor</code></p>
<dd> This is the rate fixed in London by BBA. Use Euribor if you&#8217;re interested in the fixing by the ECB.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::ExchangeRateManager::lookup</code>(const Currency &amp;source, const Currency &amp;target, Date date=Date(), ExchangeRate::Type type=ExchangeRateDerived) const</p>
<dd> if two or more exchange-rate chains are possible which allow to specify a requested rate, it is unspecified which one is returned.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExponentialSplinesFitting</code></p>
<dd> convergence may be slow</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::FiniteDifferenceModel::rollback</code>(array_type &amp;a, Time from, Time to, Size steps)</p>
<dd> being this a rollback, from must be a later time than to.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::FiniteDifferenceModel::rollback</code>(array_type &amp;a, Time from, Time to, Size steps, const condition_type &amp;condition)</p>
<dd> being this a rollback, from must be a later time than to.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></p>
<dd> The method can be slow if there are many bonds to fit. Speed also depends on the particular choice of fitting method chosen and its convergence properties under optimization. See also todo list for BondDiscountCurveFittingMethod.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittingMethod</code></p>
<dd> some parameters to the Simplex optimization method may need to be tweaked internally to the class, depending on the fitting method used, in order to get proper/reasonable/faster convergence.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></p>
<dd> This class still needs to be rigorously tested</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondHelper</code></p>
<dd> This class assumes that the reference date does not change between calls of setTermStructure().</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::FixedRateBondHelper::FixedRateBondHelper</code>(const <code>Handle&lt; Quote &gt;</code> &amp;cleanPrice, const boost::shared_ptr&lt; FixedRateBond &gt; &amp;bond)</p>
<dd> Setting a pricing engine to the passed bond from external code will cause the bootstrap to fail or to give wrong results. It is advised to discard the bond after creating the helper, so that the helper has sole ownership of it.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Forward</code></p>
<dd> This class still needs to be rigorously tested</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::ForwardRateStructure::zeroYieldImpl</code>(Time) const</p>
<dd> This is just a default, highly inefficient and possibly wildly inaccurate implementation. Derived classes should implement their own zeroYield method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class G2SwaptionEngine</code></p>
<dd> The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GapPayoff</code></p>
<dd> this payoff can be negative depending on the strikes</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Handle::Handle</code>(const boost::shared_ptr&lt; T &gt; &amp;h=boostshared_ptr&lt; T &gt;(), bool registerAsObserver=true)</p>
<dd> registerAsObserver is left as a backdoor in case the programmer cannot guarantee that the object pointed to will remain alive for the whole lifetime of the handle&#8212;namely, it should be set to false when the passed shared pointer does not own the pointee (this should only happen in a controlled environment, so that the programmer is aware of it). Failure to do so can very likely result in a program crash. If the programmer does want the handle to register as observer of such a shared pointer, it is his responsibility to ensure that the handle gets destroyed before the pointed object does.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::HazardRateStructure::HazardRateStructure</code>(const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HimalayaOption</code></p>
<dd> This implementation still does not manage seasoned options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::IMM::code</code>(const Date &amp;immDate)</p>
<dd> It raises an exception if the input date is not an IMM date</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::IMM::date</code>(const std::string &amp;immCode, const Date &amp;referenceDate=Date())</p>
<dd> It raises an exception if the input string is not an IMM code</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ImpliedVolTermStructure</code></p>
<dd> It doesn&#8217;t make financial sense to have an asset-dependant implied Vol Term Structure. This class should be used with term structures that are time dependant only.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class IncrementalStatistics</code></p>
<dd> high moments are numerically unstable for high average/standardDeviation ratios.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Index</code></p>
<dd> this class performs no check that the provided/requested fixings are for dates in the past, i.e. for dates less than or equal to the evaluation date. It is up to the client code to take care of possible inconsistencies due to &#8216;seeing in the future&#8217;</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Index::name</code>() const =0</p>
<dd> This method is used for output and comparison between indexes. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Instrument::setPricingEngine</code>(const boost::shared_ptr&lt; PricingEngine &gt; &amp;)</p>
<dd> calling this method will have no effects in case the <code>performCalculation</code> method was overridden in a derived class.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::InterestRate::discountFactor</code>(Time t) const</p>
<dd> Time must be measured using InterestRate&#8217;s own day counter.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::InterestRate::compoundFactor</code>(Time t) const</p>
<dd> Time must be measured using InterestRate&#8217;s own day counter.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::InterestRate::equivalentRate</code>(Time t, Compounding comp, Frequency freq=Annual) const</p>
<dd> Time must be measured using the InterestRate&#8217;s own day counter.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::InterestRate::impliedRate</code>(Real compound, Time t, const DayCounter &amp;resultDC, Compounding comp, Frequency freq=Annual)</p>
<dd> Time must be measured using the day-counter provided as input.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::InterestRateVolSurface::InterestRateVolSurface</code>(const boost::shared_ptr&lt; InterestRateIndex &gt; &amp;, const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JamshidianSwaptionEngine</code></p>
<dd> The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JPYLibor</code></p>
<dd> This is the rate fixed in London by BBA. Use TIBOR if you&#8217;re interested in the Tokio fixing.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JuQuadraticApproximationEngine</code></p>
<dd> Barone-Adesi-Whaley critical commodity price calculation is used, it has not been modified to see whether the method of Ju is faster. Ju does not say how he solves the equation for the critical stock price, e.g. Newton method. He just gives the solution. The method of BAW gives answers to the same accuracy as in Ju (1999).</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Lattice::partialRollback</code>(DiscretizedAsset &amp;, Time to) const =0</p>
<dd> In version 0.3.7 and earlier, this method was called rollAlmostBack method and performed pre-adjustment. This is no longer true; when migrating your code, you&#8217;ll have to replace calls such as:</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::LazyObject::calculate</code>() const</p>
<dd> Objects cache the results of the previous calculation. Such results will be returned upon later invocations of <i></i><code>calculate</code>. When the results depend on arguments which could change between invocations, the lazy object must register itself as observer of such objects for the calculations to be performed again when they change.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::LazyObject::calculate</code>() const</p>
<dd> Should this method be redefined in derived classes, LazyObject::calculate() should be called in the overriding method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LiborForwardModelProcess</code></p>
<dd> this class does not work correctly with Visual C++ 6.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::LocalVolTermStructure::LocalVolTermStructure</code>(const Calendar &amp;cal=Calendar(), BusinessDayConvention bdc=Following, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member pseudoSqrt</code></p>
<dd> Higham algorithm only works for correlation matrices.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCAmericanBasketEngine&lt; RNG &gt;</code></p>
<dd> This method is intrinsically weak for out-of-the-money options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCDiscreteAveragingAsianEngine&lt; RNG, S &gt;</code></p>
<dd> control-variate calculation is disabled under VC++6.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MixedScheme&lt; Operator &gt;</code></p>
<dd> The differential operator must be linear for this evolver to work.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class NeumannBC</code></p>
<dd> The value passed must not be the value of the derivative. Instead, it must be comprehensive of the grid step between the first two points&#8211;i.e., it must be the difference between f[0] and f[1].</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Observable::operator=</code>(const Observable &amp;)</p>
<dd> notification is sent before the copy constructor has a chance of actually change the data members. Therefore, observers whose update() method tries to use their observables will not see the updated values. It is suggested that the update() method just raise a flag in order to trigger a later recalculation.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::OptionletVolatilityStructure::OptionletVolatilityStructure</code>(const Calendar &amp;cal, BusinessDayConvention bdc, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PagodaOption</code></p>
<dd> This implementation still does not manage seasoned options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::PathPayoff::name</code>() const =0</p>
<dd> This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Payoff::name</code>() const =0</p>
<dd> This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</code></p>
<dd> The bootstrapping algorithm will raise an exception if any two instruments have the same maturity date.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</code></p>
<dd> The bootstrapping algorithm will raise an exception if any two instruments have the same maturity date.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Problem::reset</code>()</p>
<dd> it does not reset the current minumum to any initial value</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class QuantoEngine&lt; Instr, Engine &gt;</code></p>
<dd> for the time being, this engine will only work with simple Black-Scholes processes (i.e., no Merton.)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class RandomizedLDS&lt; LDS, PRS &gt;</code></p>
<dd> Inverting LDS and PRS is possible, but it doesn&#8217;t make sense.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class RandomSequenceGenerator&lt; RNG &gt;</code></p>
<dd> do not use with low-discrepancy sequence generator.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::RelinkableHandle::RelinkableHandle</code>(const boost::shared_ptr&lt; T &gt; &amp;h=boostshared_ptr&lt; T &gt;(), bool registerAsObserver=true)</p>
<dd> see the Handle documentation for issues relatives to registerAsObserver.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::RelinkableHandle::linkTo</code>(const boost::shared_ptr&lt; T &gt; &amp;, bool registerAsObserver=true)</p>
<dd> see the Handle documentation for issues relatives to registerAsObserver.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Rounding::Type</code></p>
<dd> the names of the Floor and Ceiling methods might be misleading. Check the provided reference.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::Settings::evaluationDate</code>()</p>
<dd> a notification is not sent when the evaluation date changes for natural causes&#8212;i.e., a date was not explicitly set (which results in today&#8217;s date being used for pricing) and the current date changes as the clock strikes midnight.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SimpleDayCounter</code></p>
<dd> this day counter should be used together with NullCalendar, which ensures that dates at whole-month distances share the same day of month. It is <code>not</code> guaranteed to work with any other calendar.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SingleAssetOption::impliedVolatility</code>(Real targetValue, Real accuracy=1e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const</p>
<dd> Options with a gamma that changes sign have values that are <code>not</code> monotonic in the volatility, e.g binary options. In these cases impliedVolatility can fail and in any case is meaningless. Another possible source of failure is to have a targetValue that is not attainable with any volatility, e.g. a targetValue lower than the intrinsic value in the case of American options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SwapIndex::underlyingSwap</code>(const Date &amp;fixingDate) const</p>
<dd> Relinking the term structure underlying the index will not have effect on the returned swap.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SwaptionVolatilityCube</code></p>
<dd> this class is not finalized and its interface might change in subsequent releases.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SwaptionVolatilityStructure::SwaptionVolatilityStructure</code>(const Calendar &amp;calendar, BusinessDayConvention bdc, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::TermStructure::TermStructure</code>(const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Tibor</code></p>
<dd> This is the rate fixed in Tokio by JBA. Use JPYLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TreeSwaptionEngine</code></p>
<dd> This engine is not guaranteed to work if the underlying swap has a start date in the past, i.e., before today&#8217;s date. When using this engine, prune the initial part of the swap so that it starts at $ t geq 0 $.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TridiagonalOperator</code></p>
<dd> to use real time-dependant algebra, you must overload the corresponding operators in the inheriting time-dependent class.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TrinomialTree</code></p>
<dd> The diffusion term of the SDE must be independent of the underlying process.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::VanillaOption::impliedVolatility</code>(Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const</p>
<dd> currently, this method returns the Black-Scholes implied volatility using analytic formulas for European options and a finite-difference method for American and Bermudan options. It will give unconsistent results if the pricing was performed with any other methods (such as jump-diffusion models.)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::VanillaOption::impliedVolatility</code>(Real price, const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const</p>
<dd> options with a gamma that changes sign (e.g., binary options) have values that are <code>not</code> monotonic in the volatility. In these cases, the calculation can fail and the result (if any) is almost meaningless. Another possible source of failure is to have a target value that is not attainable with any volatility, e.g., a target value lower than the intrinsic value in the case of American options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class VanillaSwap</code></p>
<dd> if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-rate and fair-spread calculation. This might not be what you want.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class VarianceOption</code></p>
<dd> This class does not manage seasoned variance options.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class VarianceSwap</code></p>
<dd> This class does not manage seasoned variance swaps.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::VolatilityTermStructure::VolatilityTermStructure</code>(const Calendar &amp;cal, BusinessDayConvention bdc, const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::YieldTermStructure::YieldTermStructure</code>(const DayCounter &amp;dc=DayCounter())</p>
<dd> term structures initialized by means of this constructor must manage their own reference date by overriding the referenceDate() method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::YieldTermStructure::forwardRate</code>(const Date &amp;d, const Period &amp;p, const DayCounter &amp;resultDayCounter, Compounding comp, Frequency freq=Annual, bool extrapolate=false) const</p>
<dd> dates are not adjusted for holidays</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Zibor</code></p>
<dd> This is the rate fixed in Zurich by BBA. Use CHFLibor if you&#8217;re interested in the London fixing by BBA.</dl>
<hr>
<h2>Index</h2>
