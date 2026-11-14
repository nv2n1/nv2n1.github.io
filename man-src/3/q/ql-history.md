---
title: "ql-history(3)"
name: "ql-history"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-history/"
description: "history – Version history Release 0.9.7 – November 2008 PORTABILITY"
---

<p>history &#8211; Version history <code>Release 0.9.7 &#8211; November 2008</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Microsoft Visual C++ configurations have been renamed. The default Debug and Release configurations now link to the DLL version of the common runtime library. The names of other configuration should now be more descriptive.</p>
<dt>*</p>
<dd>Fixes for Solaris build.</dl>
<p> BONDS</p>
<dl>
<dt>*</p>
<dd>Added bond example (thanks to Florent Grenier.)</p>
<dt>*</p>
<dd>Added support for amortizing bonds (thanks to Simon Ibbotson.)</dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</p>
<dd>Added two more cashflow analysis functions (thanks to Toyin Akin.)</dl>
<p> DATE/TIME</p>
<dl>
<dt>*</p>
<dd>Added bespoke calendar.</dl>
<p> INDEXES</p>
<dl>
<dt>*</p>
<dd>Added GBP/USD/CHF/JPY swap-rate indexes.</p>
<dt>*</p>
<dd>Fixed USD LIBOR calendar (settlement, not NYSE.)</dl>
<p> MARKET MODELS</p>
<dl>
<dt>*</p>
<dd>Added first displaced-diffusion stochastic-volatility evolver.</dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Monte Carlo average-price options now uses past fixings correctly.</dl>
<p> QUOTES</p>
<dl>
<dt>*</p>
<dd>added LastFixingQuote, a Quote adapter for the last available fixing of a given index.</dl>
<p> EXPERIMENTAL FOLDER The ql/experimental folder contains code which is still not fully integrated with the library or even fully tested, but is released in order to get user feedback. Experimental classes are considered unstable; their interfaces are likely to change in future releases. New contributions for this release were:</p>
<dl>
<dt>*</p>
<dd>time-dependent binomial trees (thanks to John Maiden.)</p>
<dt>*</p>
<dd>a new multidimensional FDM framework based on operator splitting using Craig-Sneyd, Hundsdorfer or Douglas schemes (thanks to Andreas Gaida, Ralph Schreyer, and Klaus Spanderen.)</p>
<dt>*</p>
<dd>implementations of Black-variance curve and surface taking a set of quotes as input (thanks to Frank HÃ¶vermann.)</p>
<dt>*</p>
<dd>synthetic CDO engines (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>variance options, together with a Heston-process engine (thanks to Lorella Fatone, Francesca Mariani, Maria Cristina Recchioni, and Francesco Zirilli.)</p>
<dt>*</p>
<dd>a commodity framework, including instruments such as energy futures and energy swaps (thanks to J. Erik Radmall.)</p>
<dt>*</p>
<dd>quanto-barrier options (thanks to Paul Farrington.)</p>
<dt>*</p>
<dd>amortizing bonds (thanks to Simon Ibbotson.)</p>
<dt>*</p>
<dd>a perturbative engine for barrier options (thanks to Lorella Fatone, Maria Cristina Recchioni, and Francesco Zirilli.)</dl>
<p> <code>Release 0.9.6 &#8211; August 6th, 2008</code> Bug-fix release for QuantLib 0.9.5. It fixes a bug that would cause bootstrapped term structures to silently switch to linear interpolation when log-linear was requested. <code>Release 0.9.5 &#8211; July 30th, 2008</code> CREDIT FRAMEWORK New credit framework due to the joint efforts of StatPro Italia, Roland Lichters, Chris Kenyon, and Jose Aparicio. The framework currently include:</p>
<dl>
<dt>*</p>
<dd>Interface for default-probability term structure and adapters for hazard-rate and default-density structures.</p>
<dt>*</p>
<dd>Flat hazard-rate curve.</p>
<dt>*</p>
<dd>Interpolated hazard-rate and default-density curves.</p>
<dt>*</p>
<dd>Credit-default swaps (mid-point and integral engines.)</p>
<dt>*</p>
<dd>Bootstrapped piecewise default-probability curve.</p>
<dt>*</p>
<dd>CDS example.</dl>
<p> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Added support for Microsoft Visual C++ 2008 (Boost 1.35 is required for this compiler.)</p>
<dt>*</p>
<dd>Fixes for Cygwin build.</dl>
<p> EXPERIMENTAL FOLDER The new ql/experimental folder contains code which is still not fully integrated with the library, but is released in order to get user feedback. Experimental classes are considered unstable; their interfaces are likely to change in future releases. The folder currently include:</p>
<dl>
<dt>*</p>
<dd>Generic MC basket option (thanks to Andrea Odetti.)</p>
<dt>*</p>
<dd>CDS option (thanks to Roland Stamm.)</p>
<dt>*</p>
<dd>Nth-to-default swap (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>Extended Black-Scholes-Merton process (thanks to Frank Hoermann.)</p>
<dt>*</p>
<dd>Quanto-adjusted coupons and averaged coupons (thanks to Toyin Akin.)</p>
<dt>*</p>
<dd>Callable bonds (thanks to Allen Kuo.)</p>
<dt>*</p>
<dd>New framework for volatility term structures.</p>
<dt>*</p>
<dd>Sensitivity analysis functions.</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added 2008 holidays for China, India, Indonesia, Singapore, and Taiwan.</p>
<dt>*</p>
<dd>Added one-off holiday (President Reagan&#8217;s and Ford&#8217;s funerals) to NYSE calendar.</p>
<dt>*</p>
<dd>Fixed South Korea calendar (thanks to Charles Chongseok Hyun.)</dl>
<p> CURRENCIES</p>
<dl>
<dt>*</p>
<dd>Added Peruvian currency.</dl>
<p> DATES</p>
<dl>
<dt>*</p>
<dd>Added date-generation rules for CDS schedules (i.e., rolling to the 20th of the month.)</dl>
<p> INDEXES</p>
<dl>
<dt>*</p>
<dd>Added SEK LIBOR index.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Ported Himalaya and Everest options to pricing-engine framework (thanks to the IMAFA students at Polytech&#8217;Nice Sophia: Jeome Bessi, Seastien Bonifaci, Benjamin Degerbaix and Renaud Pentel.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added matrix determinant.</p>
<dt>*</p>
<dd>Added QR matrix decomposition.</p>
<dt>*</p>
<dd>Added a number of copulas (thanks to Marek Glowacki.)</p>
<dt>*</p>
<dd>Added constrained cubic spline.</p>
<dt>*</p>
<dd>Implemented derivative and second derivative of log-interpolations.</p>
<dt>*</p>
<dd>Added Gauss-Lobatto integration.</p>
<dt>*</p>
<dd>Added student-t distribution (thanks to Roland Lichters.)</dl>
<p> MODELS</p>
<dl>
<dt>*</p>
<dd>Added calibrated GJR-GARCH model (thanks to Yee Man Chan.)</p>
<dt>*</p>
<dd>Added Feller constraint to Heston model.</dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Refactored variance-swap engines (the underlying stochastic process is now passed to the pricing engine.)</p>
<dt>*</p>
<dd>Added GJR-GARCH pricing engines for vanilla options (thanks to Yee Man Chan.)</dl>
<p> PROCESSES</p>
<dl>
<dt>*</p>
<dd>Added Euler end-point discretization (thanks to Frank Hoermann.)</p>
<dt>*</p>
<dd>Added GJR-GARCH process (thanks to Yee Man Chan.)</p>
<dt>*</p>
<dd>Added Bates process.</dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</p>
<dd>Added turn-of-year effect to yield-curve bootstrapping (generalized to multiple jumps at arbitrary dates.)</p>
<dt>*</p>
<dd>Added local bootstrap of forward rates (thanks to Simon Ibbotson.)</p>
<dt>*</p>
<dd>Disabled copies of interpolated curves (the existing behavior was incorrect. A fix to re-enable copying will be included in a future release.)</dl>
<p> VOLATILITY</p>
<dl>
<dt>*</p>
<dd>Added constant cap/floor term volatility structure.</p>
<dt>*</p>
<dd>Added stripped optionlet.</dl>
<p> <code>Release 0.9.0 &#8211; December 24th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Fixes for MSYS and Cygwin build.</p>
<dt>*</p>
<dd>Fixes for VC++ build with CLR support enabled.</p>
<dt>*</p>
<dd>Dropped MetroWerks CodeWarrior support.</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Fix for business-days calculation (thanks to Piter Dias.)</p>
<dt>*</p>
<dd>Updated Hong Kong&#8217;s holidays for 2008 and China&#8217;s for 2007.</p>
<dt>*</p>
<dd>Added new holiday to Canadian calendars (thanks to Matt Knox.)</p>
<dt>*</p>
<dd>Fixed joint-calendar specification (thanks to Jay Walters.)</p>
<dt>*</p>
<dd>Split Canadian calendar into settlement and TSX (thanks to Matt Knox.)</p>
<dt>*</p>
<dd>Added Brazilian exchange calendar (thanks to Richard Gomes.)</p>
<dt>*</p>
<dd>Fixes for the Brazilian calendars (thanks to Piter Dias.)</dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</p>
<dd>Added average-BMA coupon (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>Fixed-rate coupons can now accept an InterestRate instance (thanks to Piter Dias.)</p>
<dt>*</p>
<dd>implemented cash-flow vector builders as helper classes to ease skipping default parameters and single/multiple inputs.</dl>
<p> DATES</p>
<dl>
<dt>*</p>
<dd>Extended date range up to year 2199.</p>
<dt>*</p>
<dd>Fixed period comparison (thanks to Chris Kenyon.)</p>
<dt>*</p>
<dd>Fixed short date formatting (thanks to Robert Lopez.)</p>
<dt>*</p>
<dd>Enhanced period algebra.</dl>
<p> INDEXES</p>
<dl>
<dt>*</p>
<dd>Added BMA index (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>Added inflation indexes (thanks to Chris Kenyon.)</p>
<dt>*</p>
<dd>Added historical interest-rate index analysis.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Added BMA swaps (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>Added year-on-year and zero-coupon inflation swaps (thanks to Chris Kenyon.)</p>
<dt>*</p>
<dd>Fixed stub-date management and backward date generation for fixed-rate bonds (thanks to Toyin Akin.)</p>
<dt>*</p>
<dd>Added clean/dirty bond-price calculation from Z-spread.</dl>
<p> LATTICES</p>
<dl>
<dt>*</p>
<dd>Fixed Tsiveriotis-Fernandes tree initialization (thanks to John Maiden.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added multi-dimensional cost function for least-square problems (thanks to Guillaume Pealat.)</p>
<dt>*</p>
<dd>Added histogram class (thanks to Gang Liang.)</p>
<dt>*</p>
<dd>Added log-cubic interpolation.</p>
<dt>*</p>
<dd>Fixed conjugate-gradient bug.</p>
<dt>*</p>
<dd>Fixed nested Levenberg-Marquardt bug.</dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Refactored option engines (the underlying stochastic process is now passed to the pricing engine.)</p>
<dt>*</p>
<dd>Refactored bond, cap/floor, swap, and swaption engines (the discount curve is now passed to the pricing engine.)</p>
<dt>*</p>
<dd>Added Heston/Hull-White analytic and Monte Carlo engines for vanilla options.</p>
<dt>*</p>
<dd>Fixed bug in blackFormulaCashItmProbability in case of non null displacement.</dl>
<p> PROCESSES</p>
<dl>
<dt>*</p>
<dd>Added hybrid Heston/Hull-White process.</p>
<dt>*</p>
<dd>Fixed joint-process bug.</dl>
<p> QUOTES</p>
<dl>
<dt>*</p>
<dd>Added forward-swap quote.</dl>
<p> RANDOM NUMBERS</p>
<dl>
<dt>*</p>
<dd>Fixed ordering of primitive polynomials for Sobol/Levitan and Sobol/Levitan/Lemieux methods.</p>
<dt>*</p>
<dd>Added JoeKuoD5, JoeKuoD6 and JoeKuoD7 direction integers for Sobol generator.</p>
<dt>*</p>
<dd>Added Kuo, Kuo2 and Kuo3 direction integers for Sobol generator.</p>
<dt>*</p>
<dd>Added class to generate low-discrepancy sequences using a lattice rule.</dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</p>
<dd>Added discount curve fitted on bond prices (thanks to Allen Kuo.)</p>
<dt>*</p>
<dd>Added BMA-swap rate helper (thanks to Roland Lichters.)</p>
<dt>*</p>
<dd>Made SwapRateHelper forward-start enabled.</p>
<dt>*</p>
<dd>Added universal term-structure bootstrapper (thanks to Chris Kenyon.)</p>
<dt>*</p>
<dd>Added abstract inflation term structures (thanks to Chris Kenyon.)</p>
<dt>*</p>
<dd>Added piecewise inflation curves (thanks to Chris Kenyon.)</dl>
<p> <code>Release 0.8.1 &#8211; June 4th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Version 0.8.1 adds support for Boost 1.34 on Linux systems. If you are using version 0.8.0 on Windows systems, you do not need this upgrade.</dl>
<p> <code>Release 0.8.0 &#8211; May 30th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Version 0.8.0 is the last QuantLib release to support the Metrowerks CodeWarrior compiler (which was discountinued by Metrowerks.) If you use such compiler and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dl>
<p> SOURCE TREE</p>
<dl>
<dt>*</p>
<dd>Files and folders in the source tree have been reorganized (hopefully for th ebetter.) If you only included &lt;ql/quantlib.hpp&gt;, all changes were taken care of for you. if you included specific headers, you might want to check its current location; in particular, all folder names are now lowercase.</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added 2007 holidays for Indonesia, Saudi Arabia, and South Korea calendars.</dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</p>
<dd>Added floater range-accrual coupons.</dl>
<p> INDEXES</p>
<dl>
<dt>*</p>
<dd>Added EuriborSwapFixB family.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Added capped/floored floating-rate bond. It can also be used for reverse floaters.</p>
<dt>*</p>
<dd>Added delta, gamma and theta to binomial option engines (thanks to Steve Cook.)</p>
<dt>*</p>
<dd>Refactored basket engines to allow for more payoffs.</dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</p>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. Improvements since release 0.4.0 include normal forward-rate market model, lognormal CMS market model, lognormal coterminal-swap market model, and calibration to caplets and coterminal swaptions. The interface of the model and its integration with the bulk of the library are still in development.</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Adaptive Gauss-Kronrod integration added.</p>
<dt>*</p>
<dd>Added Higham&#8217;s nearest correlation matrix method (thanks to Neil Firth)</p>
<dt>*</p>
<dd>Refactored optimization framework.</dl>
<p> PROCESSES</p>
<dl>
<dt>*</p>
<dd>Added new discretization schema to Heston process.</dl>
<p> UTILITIES</p>
<dl>
<dt>*</p>
<dd>The Handle class was split into RelinkableHandle (behaving like the old Handle class) and Handle (which is notified when its copies are relinked, but cannot itself be relinked.) The former can safely be returned from inspectors.</dl>
<p> <code>Release 0.4.0 &#8211; February 20th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Starting with release 0.4.0, the Borland free compiler 5.5 and Microsoft Visual C++ 6.0 are no longer supported. If you use one of these compilers and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added 2007 holidays for Hong Kong, India, Singapore, and Taiwan exchanges.</dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</p>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. Improvements since release 0.3.14 include the use of quasi-random number generators and the calculation of Greeks and of upper bounds for instruments with early-exercise features. The interface of the model and its integration with the bulk of the library are still in development.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Added helper classes to make it easier to instantiate swaps, caps/floors, and CMS instruments.</dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</p>
<dd>Added capped/floored floating-rate coupons (including convexity adjustment.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Curve, domain and surface interfaces added.</dl>
<p> PROCESSES</p>
<dl>
<dt>*</p>
<dd>Added reversion level to Ornstein-Uhlenbeck process (thanks to Roland Lichters.)</dl>
<p> VOLATILITY TERM STRUCTURES</p>
<dl>
<dt>*</p>
<dd>Added stripping of caplet-volatility term structure from cap quotes.</p>
<dt>*</p>
<dd>Improved SABR interpolation and calibration.</dl>
<p> <code>Release 0.3.14 &#8211; November 6th, 2006</code> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Version 0.3.14 is the last QuantLib release to support the Borland free compiler 5.5 and Microsoft Visual C++ 6.0. If you use one of these compilers and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</p>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. The interface and its integration with the bulk of the library are still in development.</dl>
<p> CURRENCIES</p>
<dl>
<dt>*</p>
<dd>Added Romanian new lev.</dl>
<p> DATES, CALENDARS, AND DAY COUNTERS</p>
<dl>
<dt>*</p>
<dd>Added all serial 3M IMM futures (thanks to Toyin Akin.)</p>
<dt>*</p>
<dd>Reworked the Schedule class so that it follows market conventions more closely.</p>
<dt>*</p>
<dd>Added business/252 day-count convention (thanks to Piter Dias.)</dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</p>
<dd>Added base swap-rate class and a number of actual swap rates.</p>
<dt>*</p>
<dd>Added constant-maturity swap coupons (including convexity adjustment.)</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Added asset swaps.</p>
<dt>*</p>
<dd>Added face amount to bonds (defaulting to 100.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added hypersphere and lower-diagonal salvaging algorithms (thanks to Yiping Chen.)</dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Added Longstaff-Schwartz Monte-Carlo algorithm for American/Bermudan equity options with deterministic interest rates.</dl>
<p> TERM STRUCTURE</p>
<dl>
<dt>*</p>
<dd>Added piecewise-spreaded yield curve (thanks to Roland Lichters.)</dl>
<p> <code>Release 0.3.13 &#8211; July 31st, 2006</code> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added NERC calendar (thanks to Joe Byers.)</dl>
<p> INSTRUMENTS AND PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Added continuous fixed and floating lookback options (thanks to Warren Chou.)</p>
<dt>*</p>
<dd>Added FRA and forward fixed-coupon bonds; examples provided (thanks to Allen Kuo.)</p>
<dt>*</p>
<dd>Added variance swaps (thanks to Warren Chou.)</p>
<dt>*</p>
<dd>Added composite instrument; example provided.</p>
<dt>*</p>
<dd>Added cash-settled swaption pricing in Black swaption engine; test provided.</p>
<dt>*</p>
<dd>Added discrete dividends and soft callability to convertible bonds.</dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</p>
<dd>Fixed business-day conventions for Euribor and LIBOR indices (following below one month, month-end from one month onwards.)</dl>
<p> MODELS</p>
<dl>
<dt>*</p>
<dd>Added more complex market parameterizations and performance improvements for Libor market model (thanks to Klaus Spanderen.)</dl>
<p> PROCESSES</p>
<dl>
<dt>*</p>
<dd>Renamed BlackScholedProcess to GeneralizedBlackScholedProcess; specialized classes added for Black-Scholes, Merton, Black and Garman-Kohlhagen processes.</p>
<dt>*</p>
<dd>Added Hull-White and G2 processes for Monte Carlo simulation (thanks to Banca Profilo.)</dl>
<p> RANDOM NUMBERS</p>
<dl>
<dt>*</p>
<dd>Added possibility to skip directly to the n-th item in a Sobol sequence (thanks to Richard Gould.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added SABR interpolation for volatilities.</p>
<dt>*</p>
<dd>Added general linear least-squares regression (thanks to Klaus Spanderen.)</dl>
<p> <code>Release 0.3.12 &#8211; March 27th, 2006</code> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added Brazilian calendar (thanks to Piter Dias.)</p>
<dt>*</p>
<dd>Added Argentinian, Icelandic, Indonesian, Mexican, and Ukrainian calendars.</dl>
<p> INSTRUMENTS AND PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Added convertible bonds (thanks to Theo Boafo.)</p>
<dt>*</p>
<dd>The cash flows returned by the Bond::cashflows method now include the redemption.</p>
<dt>*</p>
<dd>SimpleSwap can now be set an engine. If none is set, the old cash-flow-based calculation is used.</p>
<dt>*</p>
<dd>Generalized McVanillaEngine so that it can manage n-dimensional processes; it now subsumes McHestonEngine.</p>
<dt>*</p>
<dd>Added pricing of Bermudan options on binomial trees (thanks to Enrico Michelotti.)</p>
<dt>*</p>
<dd>Separated accrual and payment conventions for bonds.</p>
<dt>*</p>
<dd>Modified basis-point sensitivity calculation so that it returns the cash variation for a basis-point change in rate (it used to return the figure to be multiplied by the variation in order to obtain the same result.)</dl>
<p> MODELS</p>
<dl>
<dt>*</p>
<dd>Added weights to short-rate model calibration (thanks to Enrico Michelotti.)</p>
<dt>*</p>
<dd>Added Libor market model (thanks to Klaus Spanderen.)</dl>
<p> OPTIMIZATION</p>
<dl>
<dt>*</p>
<dd>Added Levenberg-Marquardt optimization method (thanks to Klaus Spanderen.)</dl>
<p> EXAMPLES</p>
<dl>
<dt>*</p>
<dd>Merged American and European option examples; added Bermudan option.</p>
<dt>*</p>
<dd>Added convertible-bond example (thanks to Theo Boafo.)</dl>
<p> <code>Release 0.3.11 &#8211; October 20th, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</p>
<dd>Added configuration option for adding current function information to error messages.</p>
<dt>*</p>
<dd>Added hook for multiple sessions to Singleton.</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added Bombay and Taipei calendars.</dl>
<p> CURRENCIES</p>
<dl>
<dt>*</p>
<dd>Added new Turkish lira.</dl>
<p> INDEXES</p>
<dl>
<dt>*</p>
<dd>More accurate LIBOR calendars (thanks to Daniele de Francesco.)</p>
<dt>*</p>
<dd>Added DKKLibor, EURLibor, and NZDLibor indexes.</p>
<dt>*</p>
<dd>Added TRLibor index (thanks to Sercan Atalik.)</dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</p>
<dd>Added Bates stochastic-volatility model; tests provided (thanks to Klaus Spanderen.)</p>
<dt>*</p>
<dd>Added vega to analytic discrete-averaging Asian engine; test provided (thanks to Gary Kennedy.)</p>
<dt>*</p>
<dd>Added stochastic process for caplet Libor market model; tests provided (thanks to Klaus Spanderen.)</dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</p>
<dd>Added fixed-coupon bond helper for curve bootstrapping (thanks to Toyin Akin.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added tabulated Gauss-Legendre quadratures (thanks to Gary Kennedy.)</p>
<dt>*</p>
<dd>Added more precise implementation of bivariate cumulative normal distribution (thanks to Gary Kennedy.)</dl>
<p> <code>Release 0.3.10 &#8211; July 14th, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</p>
<dd>The suggested syntax for setting and registering with the global evaluation date is now:</dl>
<pre><code>Settings::instance().evaluationDate() = date;
registerWith(Settings::instance().evaluationDate());


</code></pre>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Istanbul calendar added (thanks to Serkan Atalik.)</dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Faster implementation of binomial and trinomial trees.</dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Added generic multi-dimensional stochastic process.</p>
<dt>*</p>
<dd>Added stochastic process array (thanks to Klaus Spanderen.)</p>
<dt>*</p>
<dd>Multi-path generator now takes a generic stochastic process; tests provided.</p>
<dt>*</p>
<dd>New Path class implemented which stores asset values rather than variations; this makes pricers independent on whether or not log-variations were calculated. The new class is enabled when QL_DISABLE_DEPRECATED is defined; the old class is used otherwise.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Multi-asset option now takes a generic stochastic process.</dl>
<p> MODELS</p>
<dl>
<dt>*</p>
<dd>Added Heston stochastic-volatility model; tests provided (thanks to Klaus Spanderen.) Provided code include:</p>
<dt> *</p>
<dd>a corresponding stochastic process;</p>
<dt> *</p>
<dd>analytic and Monte Carlo option-pricing engines;</p>
<dt> *</p>
<dd>parameter calibration.</dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</p>
<dd>Cash-flow analyses such as NPV, IRR, convexity and duration added (thanks to Charles Whitmore.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added Gaussian orthogonal polynomials and Gaussian quadratures; tests provided (thanks to Klaus Spanderen.)</p>
<dt>*</p>
<dd>Convergence statistics added; tests provided (thanks to Gary Kennedy.)</dl>
<p> <code>Release 0.3.9 &#8211; May 2nd, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</p>
<dd>QL_SQRT, QL_MIN etc. deprecated in favor of std::sqrt, std::min&#8230;</p>
<dt>*</p>
<dd>Added a tentative tracing facility to ease debugging.</p>
<dt>*</p>
<dd>Formatters deprecated in favor of output manipulators. A number of data types can now be sent directly to output streams.</p>
<dt>*</p>
<dd>Stream-based implementation of QL_REQUIRE, QL_TRACE and similar macros. Together with manipulators, this allows one to write simpler error messages, as in:</dl>
<pre> QL_FAIL('forward at date ' &lt;&lt; d &lt;&lt; ' is ' &lt;&lt; io::rate(f));</pre>
<p>INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Improved Bond class</p>
<dt> *</p>
<dd>yield-related calculation can be performed with either compounded or continuous compounding;</p>
<dt> *</p>
<dd>added theoretical price based on discount curve;</p>
<dt> *</p>
<dd>fixed-rate coupon bonds can define different rates for each coupon;</p>
<dt> *</p>
<dd>added zero-coupon and floating-rate bonds (thanks to StatPro.)</dl>
<dl>
<dt>*</p>
<dd>Option instruments now take a generic StochasticProcess; however, most pricing engines still require a BlackScholesProcess. They should be checked to see whether the requirement can be relaxed. Following this change, Merton76Process no longer inherits from BlackScholesProcess. This avoids erroneous upcasts.</p>
<dt>*</p>
<dd>Partial fix for Bermudan swaptions with exercise lag (thanks to Luca Berardi for the report and discussion.)</p>
<dt>*</p>
<dd>Fix for analytic cap/floor engine; caplets/floorlets whose fixing is in the past are now calculated correctly (thanks to Aurelien Chanudet.)</dl>
<p> CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added Bratislava and Prague calendars.</dl>
<p> INDICES</p>
<dl>
<dt>*</p>
<dd>Fixed calendars for LIBOR fixings (thanks to Daniele De Francesco.)</dl>
<p> FINITE_DIFFERENCES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Migrated finite-difference pricers to pricing-engine framework (thanks to Joseph Wang.)</dl>
<p> YIELD TERM STRUCTURES</p>
<dl>
<dt>*</p>
<dd>Added generic piecewise yield term structure. Client code can choose what to interpolate (discounts, zero yields, forwards) and how (linear, log-linear, flat) by instantiating types such as:</dl>
<pre> PiecewiseYieldCurve&lt;Discount,LogLinear&gt;
 PiecewiseYieldCurve&lt;ZeroYield,Linear&gt;
 PiecewiseYieldCurve&lt;ForwardRate,Linear&gt;</pre>
<dl>
<dt>*</p>
<dd>Interpolated discount, zero-yield and forward-rate curves can now be set any interpolation.</p>
<dt>*</p>
<dd>FlatForward can now take rates with compounding other than continuous.</p>
<dt>*</p>
<dd>Fix for extrapolation in zero-spreaded and forward-spreaded yield term structure (thanks to Adjriou Belak for the report.)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added backward- and forward-flat interpolations.</dl>
<p> <code>Release 0.3.8 &#8211; December 22nd, 2004</code> REQUIRED PACKAGES</p>
<dl>
<dt>*</p>
<dd>Boost version 1.31.0 or later is now required.</dl>
<p> DOCUMENTATION</p>
<dl>
<dt>*</p>
<dd>Documentation now includes a FAQ page.</dl>
<p> GLOBAL FEATURES</p>
<dl>
<dt>*</p>
<dd>Global evaluation date added through Settings class. Used for index-fixing and exchange-rate lookup.</p>
<dt>*</p>
<dd>added InterestRate class, which encapsulate the interest rate compounding algebra. It manages day-counting convention, compounding convention, conversion between different conventions, and discount/compounding factor calculations. It also has its own formatter.</dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</p>
<dd>Bond and FixedCouponBond classes added (thanks to Jeff Yu) providing price/yield conversions; tests provided.</dl>
<p> DATE, CALENDARS, AND DAY COUNT CONVENTIONS</p>
<dl>
<dt>*</p>
<dd>Reworked Date interface. Added nextWeekday() and nthWeekday() static methods to the class Date. Added nextIMM() for the calculation of the next IMM date.</p>
<dt>*</p>
<dd>Added WeekdayFormatter and FrequencyFormatter</p>
<dt>*</p>
<dd>Added &#8216;1/1&#8217; day counter. The Actual365 is deprecated: as per ISDA documentation &#8216;Actual/365&#8217; is the same as &#8216;Actual/Actual&#8217;. Use the ActualActual class instead, or the Actual365Fixed class.</p>
<dt>*</p>
<dd>Added dayCounterFromString(std::string) to QuantLibFunctions.</p>
<dt>*</p>
<dd>Improved Beijing calendar (thanks to Zhou Wu.)</dl>
<p> CURRENCIES AND FX RATES</p>
<dl>
<dt>*</p>
<dd>Added currency classes; CurrencyTag replaced in library code.</p>
<dt>*</p>
<dd>Added money class providing arithmetic with or without conversions; tests provided.</p>
<dt>*</p>
<dd>Added exchange-rate class; tests provided.</p>
<dt>*</p>
<dd>Added exchange-rate manager with smart rate lookup, i.e., able to derive a missing exchange rate as a chain of provided rates; tests provided.</dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Added Faure low-discrepancy sequence (thanks to Gianni Piolanti;) tests provided.</p>
<dt>*</p>
<dd>Added randomized (shifted) low discrepancy sequences that will be used for randomized quasi Monte Carlo.</p>
<dt>*</p>
<dd>Added SeedGenerator class, for random generation of seeds when they are not given by the user.</p>
<dt>*</p>
<dd>Added the implementation of Sobol sequences using the coefficients of the free direction integers as provided by Bratley and Fox, who credited unpublished work of Sobol&#8217;s and Levitan&#8217;s.</p>
<dt>*</p>
<dd>Added an implementation of Sobol sequences using the coefficients of the free direction integers of Lemieux, Cieslak, and Luttmer. Coefficients for d&lt;=40 are the same as in Bradley-Fox. For dimension 40&lt;d&lt;=360 the coefficients have been calculated as optimal values based on the &#8216;resolution&#8217; criterion. The values has been provided by Christiane Lemieux, private communication, September 2004.</p>
<dt>*</p>
<dd>PathGenerator now works correctly with processes describing S instead of log S. Geometric Brownian process added (thanks to Walter Penschke.)</dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Reworked the DiscretizedAsset interface.</dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Added pricing engine for American options with Ju quadratic approximation.</p>
<dt>*</p>
<dd>Average-price Asian pricers have been deprecated. New equivalent pricing engines added.</dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>Added current coupon to discretized swap and cap/floor.</p>
<dt>*</p>
<dd>Added IndexManager as a singleton (will replace XiborManager&#8211;already obsoleted in library code.)</p>
<dt>*</p>
<dd>Added DayCounter parameter to ParCoupon (to be used for accruing spreads and past fixings.) When missing, it defaults to that of the term structure.</p>
<dt>*</p>
<dd>Added compilation flag to select default floating-coupon type.</p>
<dt>*</p>
<dd>IndexedCoupon can now take a generic index rather than a Libor (thanks to Daniele De Francesco.)</p>
<dt>*</p>
<dd>Added hooks for convexity adjustment in floating-rate coupons; implemented adjustment for InArrearIndexedCoupon.</dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</p>
<dd>TermStructure renamed to YieldTermStructure (the former name was deprecated.)</p>
<dt>*</p>
<dd>New base class BaseTermStructure which can calculate its reference date based on the global evaluation date. YieldTermStructure, BlackVolTermStructure, LocalVolTermStructure, CapFlatVolatilityStructure, CapletForwardVolatilityStructure, and SwaptionVolatilityStructure are now derived from BaseTermStructure so that they inherit its functionality.</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>Added Singleton pattern.</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added N-dimensional cubic spline (thanks to Roman Gitlin.)</p>
<dt>*</p>
<dd>Added CovarianceDecomposition class (decomposes a covariance matrix into standard deviations and correlations)</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>Renamed RelinkableHandle to Handle.</dl>
<p> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Support for Dev-C++ IDE added.</p>
<dt>*</p>
<dd>Fixes for gcc 2.95 added (thanks to Michael Dirkmann.)</dl>
<p> <code>Release 0.3.7 &#8211; July 23rd, 2004</code> IMPORTANT QuantLib now depends on the Boost library (</p>
<p><a rel="nofollow" href="http://www.boost.org">www.boost.org</a>). You will need a working Boost installation in order to compile and use QuantLib. Instructions for installing Boost from sources are available at &lt;<a rel="nofollow" href="http://www.boost.org/more/getting_started.html">http://www.boost.org/more/getting_started.html</a>&gt;. Pre-packaged binaries might be available from other sources. Google is your friend (or Debian, or Fink&#8230;) DATE, CALENDARS, AND DAY COUNT CONVENTIONS</p>
<dl>
<dt>*</p>
<dd>Working on differentiating calendars depending on country or exchange, instead of city.</p>
<dt>*</p>
<dd>Added Italy (Settlement, Exchange), United Kingdom (Settlement, Exchange, Metals), United States (Settlement, Exchange, GovermentBond), Xetra.</p>
<dt>*</p>
<dd>Milan, London, and NewYork calendars have been deprecated.</p>
<dt>*</p>
<dd>Added (old-style) calendars: Beijing, Hong Kong, Riyadh, Seoul, Singapore, Taiwan.</p>
<dt>*</p>
<dd>RollingConvention has been renamed BusinessDayConvention, as for ISDA definitions.</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added rounding algorythms as per OMG enumeration/definition.</dl>
<p> TEST SUITE</p>
<dl>
<dt>*</p>
<dd>Moved to Boost unit test framework. CppUnit is no longer needed.</p>
<dt>*</p>
<dd>Added test for quanto and forward compound engines.</p>
<dt>*</p>
<dd>Added test for roundings.</p>
<dt>*</p>
<dd>Added test for discrete dividend European options.</p>
<dt>*</p>
<dd>Added test for cliquet options.</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>enable/disableExtrapolation() methods were added to a few classes such as TermStructure. They make it possible to persistently allow extrapolation without the need of specifying it at every method call.</p>
<dt>*</p>
<dd>Added user-configurable flag to disable usage of deprecated classes.</dl>
<p> PORTABILITY</p>
<dl>
<dt>*</p>
<dd>Fink package available</p>
<dt>*</p>
<dd>Visual C++ 7.x project files added</dl>
<p> <code>Release 0.3.6 &#8211; April 15th, 2004</code> Bug-fix release for QuantLib 0.3.5. A bug was removed where calls to impliedVolatility() would break the state of the option and of all options sharing the same stochastic process. <code>Release 0.3.5 &#8211; March 31th, 2004</code> BOOST SUPPORT</p>
<dl>
<dt>*</p>
<dd>When available, QuantLib 0.3.5 now uses parts of the Boost library. The presence of Boost is detected automatically under Unix/Linux systems; on Windows systems, it must be enabled by uncommenting the relevant line in ql/userconfig.hpp.</dl>
<dl>
<dt>*</p>
<dd>In the next QuantLib release, the presence of the Boost library will be mandatory.</dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Modified MultiPath interface to remove drifts. They are now in the stochastic processes.</p>
<dt>*</p>
<dd>Preliminary implementation of Longstaff-Schwartz least-squares</p>
<dt>*</p>
<dd>Monte Carlo pricer for European basket options</p>
<dt>*</p>
<dd>Brownian-bridge bugs fixed</p>
<dt>*</p>
<dd>StochasticProcess base class and derived classes (diffusion, jump-diffusion, etc.) have been created.</dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Pricing engines now use Payoff and Exercise classes.</p>
<dt>*</p>
<dd>American basket options.</p>
<dt>*</p>
<dd>Binary barrier option replaced by vanilla option with digital payoff.</p>
<dt>*</p>
<dd>Stulz engine for max and min basket calls and puts on two assets.</p>
<dt>*</p>
<dd>American binary option added (a.k.a. one-touch, american digital, americal barrier, etc.) with different payoffs (cash/asset at hit/expiry, etc.)</p>
<dt>*</p>
<dd>Added engine for Merton 1976 jump-diffusion process.</p>
<dt>*</p>
<dd>Added Bjerksund and Stensland approximation for American option (still unstable.)</p>
<dt>*</p>
<dd>Added Barone-Adesi and Whaley approximation for American option.</p>
<dt>*</p>
<dd>Improved Black formula engine with more greeks added.</p>
<dt>*</p>
<dd>Discrete geometric asian option.</p>
<dt>*</p>
<dd>Added Leisen-Reimer binomial tree.</dl>
<p> SHORT RATE MODELS</p>
<dl>
<dt>*</p>
<dd>Model renamed to ShortRateModel. A typedef is provided for backward compatibility&#8211;it will be removed in subsequent releases.</dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>bug fix for short time (0&lt;=t&lt;=Tmin) interpolation</dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Method renamed to OptimizationMethod. A typedef is provided for backward compatibility&#8211;it will be removed in subsequent releases.</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>Composite pattern</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Improved cubic spline interpolation. It now handles end conditions such as first derivative value, second derivative value, not-a-knot. Hyman filter for monotonically constrained interpolation has been implemented. Primitive calculation has been enabled in addition to derivative and second derivative.</p>
<dt>*</p>
<dd>Primitive, first derivative, and second derivative functions are available for linear interpolator.</p>
<dt>*</p>
<dd>Singular value decomposition improved.</p>
<dt>*</p>
<dd>Added bivariate cumulative normal distribution.</p>
<dt>*</p>
<dd>Added binomial coefficient calculation, binomial distribution, cumulative binomial distribution, and Peizer-Pratt inversion (method 2.)</p>
<dt>*</p>
<dd>Added beta functions.</p>
<dt>*</p>
<dd>Added Poisson distribution and cumulative distribution.</p>
<dt>*</p>
<dd>Added incomplete gamma functions.</p>
<dt>*</p>
<dd>Added factorial calculation.</p>
<dt>*</p>
<dd>Added rank-reduced square root and improved pseudo-square root of square symmetric matrices.</p>
<dt>*</p>
<dd>Added Cholesky decomposition.</dl>
<p> TEST SUITE</p>
<dl>
<dt>*</p>
<dd>Added test for cubic spline interpolation.</p>
<dt>*</p>
<dd>Added test for singular value decomposition.</p>
<dt>*</p>
<dd>Added test for two-asset baskets using the Stulz pricing engine.</p>
<dt>*</p>
<dd>Added test for Monte Carlo American cash-at-hit options.</p>
<dt>*</p>
<dd>Added test for jump-diffusion engine.</p>
<dt>*</p>
<dd>Added test for American and European digital options.</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>Inner namespaces have been deprecated.</p>
<dt>*</p>
<dd>Added frequency enumeration, including &#8216;once&#8217;.</p>
<dt>*</p>
<dd>MarketElement renamed to Quote.</p>
<dt>*</p>
<dd>Handling strike=0.0 where possible.</p>
<dt>*</p>
<dd>More Payoff classes have been introduced: gap, asset-or-nothing, cash-or-nothing. Payoff is now extensively used.</p>
<dt>*</p>
<dd>Exercise class is now polymorphic. More derived classes have been introduced, and they are now extensively used.</p>
<dt>*</p>
<dd>Introduced QL_FAIL macro.</p>
<dt>*</p>
<dd>Added calendar for Copenhagen</p>
<dt>*</p>
<dd>14 April 2004 (election day) added to Johannesburg calendar as a one-off holiday.</p>
<dt>*</p>
<dd>Documentation generated with Doxygen 1.3.6.</p>
<dt>*</p>
<dd>Win32 installer generated with NSIS 2.0.</dl>
<p> <code>Release 0.3.4 &#8211; November 21th, 2003</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>MC European in one step with strike-independent vol curve (hopefully)</p>
<dt>*</p>
<dd>Path pricer for Binary options. It should cover both European and American style options. Also known as: Digital, Binary, Cash-At-Hit, Cash-At-Expiry.</p>
<dt>*</p>
<dd>Path pricers for barrier options</dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>More options moved to the new pricing engine framework: binary, barrier</p>
<dt>*</p>
<dd>Changed setupEngine() into setupArguments(args)</p>
<dt>*</p>
<dd>Moved pricing-engine machinery up to Instrument class</dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>New basis-point sensitivity functions</p>
<dt>*</p>
<dd>Added Swap::startDate() and maturity()</p>
<dt>*</p>
<dd>Cap/floor fixing days taken into account</dl>
<p> SHORT RATE MODELS</p>
<dl>
<dt>*</p>
<dd>An additional constraint can now be passed to the calibration</dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Visitable volatility term structures</dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Added composite constraint</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>Visitor, Alexandrescu-style (saves some code duplication)</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added more integration algorithms contributed by Roman Gitlin</p>
<dt>*</p>
<dd>Relaxed constaints on interval boundaries for integration algorithms</p>
<dt>*</p>
<dd>Interpolation traits</dl>
<p> TEST SUITE</p>
<dl>
<dt>*</p>
<dd>Added implied cap/floor term volatility test</p>
<dt>*</p>
<dd>Added test for binary options in PricingEngine Framework.</p>
<dt>*</p>
<dd>Added tests for Barrier options in PricingEngine Framework. Some Monte Carlo tests, but not comprehensive.</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>Conditionally allowed negative yields (disabled by default)</p>
<dt>*</p>
<dd>Null calendar and simple day counter for reproducing theoretical calculations</p>
<dt>*</p>
<dd>Fixed for VC++.Net compilation</p>
<dt>*</p>
<dd>Added spec file for RPMs</p>
<dt>*</p>
<dd>Added global flag for early/late payments</p>
<dt>*</p>
<dd>Enabled test suite for Borland</p>
<dt>*</p>
<dd>Removed OnTheEdge VC++ configurations</p>
<dt>*</p>
<dd>Added VC++ configurations for static and dynamic Multithread libraries</p>
<dt>*</p>
<dd>Upgraded to use Doxygen 1.3.4</dl>
<p> <code>Release 0.3.3 &#8211; September 3rd, 2003</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Re-templatized Monte Carlo model based on traits.</p>
<dt>*</p>
<dd>New path generator based on DiffusionProcess, TimeGrid, and externally initialized random number generator.</p>
<dt>*</p>
<dd>Added Halton low discrepancy sequence.</p>
<dt>*</p>
<dd>Added sequence generators: random sequence generator creates a sequence generator out of a random number generator. InvCumGaussianRsg creates a gaussian sequence generator out of a uniform (random or low discrepancy) sequence generator.</p>
<dt>*</p>
<dd>RNG as constructor input constructor( long seed) deprecated.</p>
<dt>*</p>
<dd>Mersenne Twister random number generator added</p>
<dt>*</p>
<dd>Old PathPricers, PathGenerators, etc are available with a trailing _old</p>
<dt>*</p>
<dd>Added Jakel&#8217;s Brownian Bridge (not used yet.)</p>
<dt>*</p>
<dd>Sobol Random Sequence Generator. Unit and Jakel.</p>
<dt>*</p>
<dd>Added randomized Halton sequences.</dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Old class Grid no longer exists, use CenteredGrid to obtain the same result.</dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Abstracted discretized option.</p>
<dt>*</p>
<dd>Additive binomial trees. All binomial trees now use DiffusionProcess.</p>
<dt>*</p>
<dd>Added Tian binomial tree.</dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Partially implemented.</p>
<dt>*</p>
<dd>Quanto forward compounded engines.</p>
<dt>*</p>
<dd>Integral (european) pricing engine.</dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</p>
<dd>ZeroCurve: a term structure based on linear interpolation of zero yields.</dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>Up-front and in-arrear indexed coupon.</p>
<dt>*</p>
<dd>Specific implementation of compound forward rate from zero yield.</p>
<dt>*</p>
<dd>Added compound forward and zero coupon implementations.</p>
<dt>*</p>
<dd>Added Futures rate helper with specified maturity date.</p>
<dt>*</p>
<dd>Added bucketed bps calculation.</p>
<dt>*</p>
<dd>Added swap constructor using specified maturity date as well as added functionality in Scheduler.</p>
<dt>*</p>
<dd>Added date-bucketed basis point sensitivity based on 1st derivative of zero coupon rate.</dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Solvers now take any function. ObjectiveFunction disappeared.</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>Abstracted lazy object.</p>
<dt>*</p>
<dd>Abstracted the curiously recurring template pattern.</dl>
<p> DATE AND CALENDARS</p>
<dl>
<dt>*</p>
<dd>Added joint calendars.</p>
<dt>*</p>
<dd>Tokyo, Stockholm, Johannesburg calendar improved.</p>
<dt>*</p>
<dd>
<dt>*</p>
<dd>Added basic date generation starting from the end.</dl>
<p> MATH</p>
<dl>
<dt>*</p>
<dd>Added Gauss-Kronrod integration algorithm.</p>
<dt>*</p>
<dd>Added primitive polynomial modulo 2 up to dimension 18 (available up to dimension 27.)</p>
<dt>*</p>
<dd>Added BicubicSplineInterpolation.</p>
<dt>*</p>
<dd>Numerical Recipes algorithm is back since there is a problem with Nicolas&#8217; code: it is unable to fit a straight line, it waves around the line.</p>
<dt>*</p>
<dd>Prime number generation.</p>
<dt>*</p>
<dd>Acklam&#8217;s approximation for inverse cumulative normal distribution function (replaced Moro&#8217;s algorithm as default.)</p>
<dt>*</p>
<dd>Added error function.</p>
<dt>*</p>
<dd>Improved Cumulative Normal Distribution function using the error function.</p>
<dt>*</p>
<dd>Matrix pseudo square algorithm using salvaging algorithm(s).</p>
<dt>*</p>
<dd>Added SequenceStatistics.</p>
<dt>*</p>
<dd>Major Statistic reworking.</p>
<dt>*</p>
<dd>Added DiscrepancyStatistic that inherits from SequenceStatistic and extends it with the calculation of L2-discrepancy.</p>
<dt>*</p>
<dd>HStatistics.</p>
<dt>*</p>
<dd>Added first and second derivative ot cubic splines.</dl>
<p> RISK MEASURES</p>
<dl>
<dt>*</p>
<dd>Introduced semiVariance and regret.</p>
<dt>*</p>
<dd>Redefinition of average shorfall (normalization factor now is cumulative(target) instead of 1.0)</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>QuEP 9 &#8216;generic disposable objects&#8217; implemented.</p>
<dt>*</p>
<dd>Added test suite.</p>
<dt>*</p>
<dd>Dataformatters extended to format long integers, Ordinal numerals, power of two formatting.</p>
<dt>*</p>
<dd>Exercise class adopted.</p>
<dt>*</p>
<dd>Added user configuration section.</p>
<dt>*</p>
<dd>Inhibited automatic conversion of <code>Handle&lt;T&gt;</code> to RelinkableHandle&lt;T&gt;.</p>
<dt>*</p>
<dd>Diffusion process extended.</p>
<dt>*</p>
<dd>Added strikeSensitivity to the Greeks.</p>
<dt>*</p>
<dd>BS does handle t==0.0 and sigma==0.0.</p>
<dt>*</p>
<dd>TimeGrid has been reworked.</p>
<dt>*</p>
<dd>Added payoff file for Payoff classes. Added Cash-Or-Nothing and Asset-Or-Nothing payoff classes.</p>
<dt>*</p>
<dd>Upgraded to use Doxygen 1.3.</dl>
<p> <code>Release 0.3.1 &#8211; February 4th, 2003</code> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>partially implemented QuEP 2 (<a rel="nofollow" href="http://quantlib.org/quep.shtml)">http://quantlib.org/quep.shtml)</a></dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>added Black and local volatility interface</dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>partially implemented QuEP 5 (<a rel="nofollow" href="http://quantlib.org/quep.shtml)">http://quantlib.org/quep.shtml)</a></dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</p>
<dd>interface revisited</p>
<dt>*</p>
<dd>added discrete time forward methods</p>
<dt>*</p>
<dd>added DiscountCurve (loglinear interpolated) and CompoundForward term structures</p>
<dt>*</p>
<dd>ForwardSpreadedTermStructure moved under QuantLibTermStructures namespace</dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>Modified coupons so that the payment date can be after the end of the accrual period</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>added/verified holidays of many calendars</p>
<dt>*</p>
<dd>added new calendars</p>
<dt>*</p>
<dd>added new currencies</p>
<dt>*</p>
<dd>more date formatters</p>
<dt>*</p>
<dd>added Period(std::string&amp;)</p>
<dt>*</p>
<dd>it is now possible to advance a calandar using a Period</p>
<dt>*</p>
<dd>added LogLinear Interpolation</p>
<dt>*</p>
<dd>the allowExtrapolation boolean in interpolation classes has been removed from constructors and added to the operator()</p>
<dt>*</p>
<dd>Renamed Solver1D::lowBound and hiBound</p>
<dt>*</p>
<dd>bug fixes</dl>
<p> BUILD PROCESS</p>
<dl>
<dt>*</p>
<dd>More autoconfiscated time functions and types</p>
<dt>*</p>
<dd>Migrated to latest autotools</p>
<dt>*</p>
<dd>added patches for Darwin and Solaris</dl>
<p> <code>Release 0.3.0 &#8211; May 6th, 2002</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Path and MultiPath are time-aware</p>
<dt>*</p>
<dd>McPricer: extended interface, improved convergency algorithm</dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>added mixed (implicit/explicit) scheme, from which Crank-Nicolson, ImplicitEuler, and ExplicitEuler are now derived</p>
<dt>*</p>
<dd>Finite Difference exercise conditions are now in the FiniteDifferences folder/namespace</p>
<dt>*</p>
<dd>Finite Difference pricers now start with &#8216;Fd&#8217; letters</p>
<dt>*</p>
<dd>BSMNumericalOption became BsmFdOption</dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>introduced first version of the framework</p>
<dt>*</p>
<dd>CRR and JR binomial trees</dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>early works on reorganization of vol structures</dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</p>
<dd>new TermStructure class based on affine model</p>
<dt>*</p>
<dd>yield curves can be spreaded in term of zeros (ZeroSpreadedTermStructure) and forwards (ForwardSpreadedTermStructure)</p>
<dt>*</p>
<dd>Added dates() and times() to PiecewiseFlatForward</p>
<dt>*</p>
<dd>discount factor accuracy in the yield curve bootstrapping is an input</p>
<dt>*</p>
<dd>added single factor short-rate models (Hull-White, Black-Karasinski)</p>
<dt>*</p>
<dd>added two factor short-rate models framework</p>
<dt>*</p>
<dd>cap/floor and swaption calibration helpers</p>
<dt>*</p>
<dd>added bermudan swaption pricing example (including BK and HW calibrations)</dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>cap/floor and swaption tree pricer</p>
<dt>*</p>
<dd>cap/floor analytical pricer</p>
<dt>*</p>
<dd>vanilla swaption Jamshidian pricer</p>
<dt>*</p>
<dd>Added accruedAmount() to coupons</p>
<dt>*</p>
<dd>Made cash flow vector builders into functions</dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>added conjugate gradient, simplex</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>implemented QuEP 8 and 10</dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</p>
<dd>added allowExtrapolation parameter to interpolaton classes</p>
<dt>*</p>
<dd>added 2D bilinear interpolation</p>
<dt>*</p>
<dd>better spline interpolation algorithm</p>
<dt>*</p>
<dd>Added non-central chi-square distribution function.</p>
<dt>*</p>
<dd>Improved Inverse Cumulative Normal Distribution using Moro&#8217;s algorithm</p>
<dt>*</p>
<dd>Introduced class representing stochastic processes</p>
<dt>*</p>
<dd>added isExpired() to Instrument interface</p>
<dt>*</p>
<dd>added functions folder and namespace for QuantLibXL and any other function-like interface to QuantLib</p>
<dt>*</p>
<dd>Handle is now castable to an Handle of a compatible type</p>
<dt>*</p>
<dd>added downsideVariance to the Statistics class</p>
<dt>*</p>
<dd>kustosis() and skewness() now handles the case of stddev == 0 and/or variance == 0</p>
<dt>*</p>
<dd>added Correlation Matrix to MultiVariateAccumulator</p>
<dt>*</p>
<dd>enforced MS VC compilation settings</p>
<dt>*</p>
<dd>added &#8216;-debug&#8217; to the QL_VERSION version string ifdef QL_DEBUG</p>
<dt>*</p>
<dd>
<dt>*</p>
<dd>fixed compilation with &#8216;g++ -pedantic&#8217;</p>
<dt>*</p>
<dd>Spread as market element</p>
<dt>*</p>
<dd>new calendars introduced</p>
<dt>*</p>
<dd>new Xibor Indexes introduced</p>
<dt>*</p>
<dd>Added optional day count to libor indexes</p>
<dt>*</p>
<dd>Shortened file names within 31 char limit to support HFS</dl>
<p> <code>Release 0.2.1 &#8211; December 3rd, 2001</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>Path and MultiPath are now classes on their own</p>
<dt>*</p>
<dd>PathPricer now handles both Path and MultiPath</p>
<dt>*</p>
<dd>MonteCarloModel now handles both single factor and multi factors simulations.</p>
<dt>*</p>
<dd>McPricer now handles both single factor and multi factors pricing. New pricing interface</p>
<dt>*</p>
<dd>antithetic variance-reduction technique made possible in Monte Carlo for both single factor and multi factors</p>
<dt>*</p>
<dd>Control Variate specific class removed: control variation technique is now handled by the general MC model</p>
<dt>*</p>
<dd>average price and average strike asian option refactored</p>
<dt>*</p>
<dd>Sample as a (value,weight) struct</p>
<dt>*</p>
<dd>random number generators moved under RandomNumbers folder and namespace</dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</p>
<dd>BackwardEuler and ForwardEuler renamed ImplicitEuler and ExplicitEuler, respectively</p>
<dt>*</p>
<dd>refactoring of TridiagonalOperator and derived classes</dl>
<p> YIELD TERM STRUCTURE AND FIXED INCOME</p>
<dl>
<dt>*</p>
<dd>Added some useful methods to term structure classes</p>
<dt>*</p>
<dd>Allowed passing a quote to RateHelpers as double</p>
<dt>*</p>
<dd>added FuturesRateHelpers (no convexity adjustment yet)</p>
<dt>*</p>
<dd>PiecewiseFlatForward now observer of rates passed as MarketElements</p>
<dt>*</p>
<dd>Unified Date and Time interface in TermStructure</p>
<dt>*</p>
<dd>Added BPS to generic swap legs</p>
<dt>*</p>
<dd>added term_structure+swap example</p>
<dt>*</p>
<dd>Fixing days introduced for floating-coupon bond</dl>
<p> PATTERNS</p>
<dl>
<dt>*</p>
<dd>Added factory pattern</p>
<dt>*</p>
<dd>Calendar and DayCounter now use the Strategy pattern</dl>
<p> VARIOUS</p>
<dl>
<dt>*</p>
<dd>used do-while-false idiom in QL_REQUIRE-like macros</p>
<dt>*</p>
<dd>now using size_t where appropriate</p>
<dt>*</p>
<dd>dividendYield is now a Spread instead of a Rate (that is: cost of carry is allowed)</p>
<dt>*</p>
<dd>RelinkableHandle initialized with an optional Handle</p>
<dt>*</p>
<dd>Worked around VC++ problems in History constructor</p>
<dt>*</p>
<dd>added QL_VERSION and QL_HEX_VERSION</p>
<dt>*</p>
<dd>generic bug fixes</p>
<dt>*</p>
<dd>removed classes deprecated in 0.2.0</dl>
<p> INSTALLATION FACILITIES</p>
<dl>
<dt>*</p>
<dd>improved and smoother Win32 binary installer</dl>
<p> DOCUMENTATION</p>
<dl>
<dt>*</p>
<dd>general re-hauling</p>
<dt>*</p>
<dd>improved and extended Monte Carlo documentation</p>
<dt>*</p>
<dd>improved and extended examples</p>
<dt>*</p>
<dd>Upgraded to Doxygen 1.2.11.1</p>
<dt>*</p>
<dd>Added man pages for installed executables</p>
<dt>*</p>
<dd>added docs in Windows Help format</p>
<dt>*</p>
<dd>added info on &#8216;Win32 OnTheEdgeRelease&#8217; and &#8216;Win32 OnTheEdgeDebug&#8217; MS VC++ configurations</p>
<dt>*</p>
<dd>additional information on how to create a MS VC++ project based on QuantLib</dl>
<p> <code>Release 0.2.0 &#8211; September 18th, 2001</code></p>
<dl>
<dt>*</p>
<dd>Library:</p>
<dt> *</p>
<dd>source code moved under ql, better GNU standards</p>
<dt> *</p>
<dd>gcc build dir can now be separated from source tree</p>
<dt> *</p>
<dd>gcc 3.0.1 port</p>
<dt> *</p>
<dd>clean compilation (no warnings)</p>
<dt> *</p>
<dd>bootstrap script on cygwin</p>
<dt> *</p>
<dd>Fixed automatic choice of seed for random number generators</p>
<dt> *</p>
<dd>Actual/actual classes</p>
<dt> *</p>
<dd>extended platform support (see table in documentation)</p>
<dt> *</p>
<dd>antithetic variance-reduction technique made possible in Monte Carlo</p>
<dt> *</p>
<dd>added dividend-Rho greek</p>
<dt> *</p>
<dd>First implementation of segment integral (to be redesigned)</p>
<dt> *</p>
<dd>Knuth random generator</p>
<dt> *</p>
<dd>Cash flows, scheduler, and swap (both generic and simple) added</p>
<dt> *</p>
<dd>added ICGaussian random generator</p>
<dt> *</p>
<dd>generic bug fixes</dl>
<dl>
<dt>*</p>
<dd>Installation facilities:</p>
<dt> *</p>
<dd>improved and smoother Win32 binary installer</p>
<dt> *</p>
<dd>better distribution</p>
<dt> *</p>
<dd>debian packages available</dl>
<dl>
<dt>*</p>
<dd>Documentation:</p>
<dt> *</p>
<dd>general re-hauling</p>
<dt> *</p>
<dd>added examples of using QuantLib and of projects based on QL</dl>
<p> <code>Release 0.1.9 &#8211; May 31st, 2001</code></p>
<dl>
<dt>*</p>
<dd>Library:</p>
<dt> *</p>
<dd>Style guidelines introduced (see <a rel="nofollow" href="http://quantlib.org/style.shtml)">http://quantlib.org/style.shtml)</a> and partially enforced</p>
<dt> *</p>
<dd>full support for Microsoft Visual Studio</p>
<dt> *</p>
<dd>full support for Linux/gcc</p>
<dt> *</p>
<dd>momentarily broken support for Metrowerks CodeWarrior</p>
<dt> *</p>
<dd>autoconfiscation (with specialized config.*.hpp files for platforms without automake/autoconf support)</p>
<dt> *</p>
<dd>Include files moved under Include/ql folder and referenced as &#8216;ql/header.hpp&#8217;</p>
<dt> *</p>
<dd>Implemented expression templates techniques for array algebra optimization</p>
<dt> *</p>
<dd>Added custom iterators</p>
<dt> *</p>
<dd>Improved term structure</p>
<dt> *</p>
<dd>Added Asian, Bermudan, Shout, Cliquet, Himalaya, and Barrier options (all with greeks calculation, control variated where possible)</p>
<dt> *</p>
<dd>Added Helsinki and Wellington calendars</p>
<dt> *</p>
<dd>Improved Normal distribution related functions: cumulative, inverse cumulative, etc.</p>
<dt> *</p>
<dd>Added uniform and Gaussian random number generators</p>
<dt> *</p>
<dd>Added Statistics class (mean, variance, skewness, downside variance, etc.)</p>
<dt> *</p>
<dd>Added RiskMeasures class: VAR, average shortfall, expected shortfall, etc.</p>
<dt> *</p>
<dd>Added RiskStatistics class combining Statistics and RiskMeasures</p>
<dt> *</p>
<dd>Added sample accumulator for multivariate analysis</p>
<dt> *</p>
<dd>Added Monte Carlo tools</p>
<dt> *</p>
<dd>Added matrix-related functions (square root, symmetric Schur decomposition)</p>
<dt> *</p>
<dd>Added interpolation framework (linear and cubic spline interpolation implemented).</dl>
<dl>
<dt>*</p>
<dd>Installation facilities:</p>
<dt> *</p>
<dd>Added Win32 GUI installer for binaries</dl>
<dl>
<dt>*</p>
<dd>Documentation:</p>
<dt> *</p>
<dd>support for Doxygen 1.2.7</p>
<dt> *</p>
<dd>Added man documentation</dl>
<p> <code>Release 0.1.1 &#8211; November 21st, 2000</code> Initial release. </p>
