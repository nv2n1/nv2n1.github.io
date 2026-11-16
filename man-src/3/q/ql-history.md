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
<dt>*</dt>
<dd>Microsoft Visual C++ configurations have been renamed. The default Debug and Release configurations now link to the DLL version of the common runtime library. The names of other configuration should now be more descriptive.</dd>
<dt>*</dt>
<dd>Fixes for Solaris build.</dd></dl>
<p> BONDS</p>
<dl>
<dt>*</dt>
<dd>Added bond example (thanks to Florent Grenier.)</dd>
<dt>*</dt>
<dd>Added support for amortizing bonds (thanks to Simon Ibbotson.)</dd></dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</dt>
<dd>Added two more cashflow analysis functions (thanks to Toyin Akin.)</dd></dl>
<p> DATE/TIME</p>
<dl>
<dt>*</dt>
<dd>Added bespoke calendar.</dd></dl>
<p> INDEXES</p>
<dl>
<dt>*</dt>
<dd>Added GBP/USD/CHF/JPY swap-rate indexes.</dd>
<dt>*</dt>
<dd>Fixed USD LIBOR calendar (settlement, not NYSE.)</dd></dl>
<p> MARKET MODELS</p>
<dl>
<dt>*</dt>
<dd>Added first displaced-diffusion stochastic-volatility evolver.</dd></dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Monte Carlo average-price options now uses past fixings correctly.</dd></dl>
<p> QUOTES</p>
<dl>
<dt>*</dt>
<dd>added LastFixingQuote, a Quote adapter for the last available fixing of a given index.</dd></dl>
<p> EXPERIMENTAL FOLDER The ql/experimental folder contains code which is still not fully integrated with the library or even fully tested, but is released in order to get user feedback. Experimental classes are considered unstable; their interfaces are likely to change in future releases. New contributions for this release were:</p>
<dl>
<dt>*</dt>
<dd>time-dependent binomial trees (thanks to John Maiden.)</dd>
<dt>*</dt>
<dd>a new multidimensional FDM framework based on operator splitting using Craig-Sneyd, Hundsdorfer or Douglas schemes (thanks to Andreas Gaida, Ralph Schreyer, and Klaus Spanderen.)</dd>
<dt>*</dt>
<dd>implementations of Black-variance curve and surface taking a set of quotes as input (thanks to Frank HÃ¶vermann.)</dd>
<dt>*</dt>
<dd>synthetic CDO engines (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>variance options, together with a Heston-process engine (thanks to Lorella Fatone, Francesca Mariani, Maria Cristina Recchioni, and Francesco Zirilli.)</dd>
<dt>*</dt>
<dd>a commodity framework, including instruments such as energy futures and energy swaps (thanks to J. Erik Radmall.)</dd>
<dt>*</dt>
<dd>quanto-barrier options (thanks to Paul Farrington.)</dd>
<dt>*</dt>
<dd>amortizing bonds (thanks to Simon Ibbotson.)</dd>
<dt>*</dt>
<dd>a perturbative engine for barrier options (thanks to Lorella Fatone, Maria Cristina Recchioni, and Francesco Zirilli.)</dd></dl>
<p> <code>Release 0.9.6 &#8211; August 6th, 2008</code> Bug-fix release for QuantLib 0.9.5. It fixes a bug that would cause bootstrapped term structures to silently switch to linear interpolation when log-linear was requested. <code>Release 0.9.5 &#8211; July 30th, 2008</code> CREDIT FRAMEWORK New credit framework due to the joint efforts of StatPro Italia, Roland Lichters, Chris Kenyon, and Jose Aparicio. The framework currently include:</p>
<dl>
<dt>*</dt>
<dd>Interface for default-probability term structure and adapters for hazard-rate and default-density structures.</dd>
<dt>*</dt>
<dd>Flat hazard-rate curve.</dd>
<dt>*</dt>
<dd>Interpolated hazard-rate and default-density curves.</dd>
<dt>*</dt>
<dd>Credit-default swaps (mid-point and integral engines.)</dd>
<dt>*</dt>
<dd>Bootstrapped piecewise default-probability curve.</dd>
<dt>*</dt>
<dd>CDS example.</dd></dl>
<p> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Added support for Microsoft Visual C++ 2008 (Boost 1.35 is required for this compiler.)</dd>
<dt>*</dt>
<dd>Fixes for Cygwin build.</dd></dl>
<p> EXPERIMENTAL FOLDER The new ql/experimental folder contains code which is still not fully integrated with the library, but is released in order to get user feedback. Experimental classes are considered unstable; their interfaces are likely to change in future releases. The folder currently include:</p>
<dl>
<dt>*</dt>
<dd>Generic MC basket option (thanks to Andrea Odetti.)</dd>
<dt>*</dt>
<dd>CDS option (thanks to Roland Stamm.)</dd>
<dt>*</dt>
<dd>Nth-to-default swap (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>Extended Black-Scholes-Merton process (thanks to Frank Hoermann.)</dd>
<dt>*</dt>
<dd>Quanto-adjusted coupons and averaged coupons (thanks to Toyin Akin.)</dd>
<dt>*</dt>
<dd>Callable bonds (thanks to Allen Kuo.)</dd>
<dt>*</dt>
<dd>New framework for volatility term structures.</dd>
<dt>*</dt>
<dd>Sensitivity analysis functions.</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added 2008 holidays for China, India, Indonesia, Singapore, and Taiwan.</dd>
<dt>*</dt>
<dd>Added one-off holiday (President Reagan&#8217;s and Ford&#8217;s funerals) to NYSE calendar.</dd>
<dt>*</dt>
<dd>Fixed South Korea calendar (thanks to Charles Chongseok Hyun.)</dd></dl>
<p> CURRENCIES</p>
<dl>
<dt>*</dt>
<dd>Added Peruvian currency.</dd></dl>
<p> DATES</p>
<dl>
<dt>*</dt>
<dd>Added date-generation rules for CDS schedules (i.e., rolling to the 20th of the month.)</dd></dl>
<p> INDEXES</p>
<dl>
<dt>*</dt>
<dd>Added SEK LIBOR index.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Ported Himalaya and Everest options to pricing-engine framework (thanks to the IMAFA students at Polytech&#8217;Nice Sophia: Jeome Bessi, Seastien Bonifaci, Benjamin Degerbaix and Renaud Pentel.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added matrix determinant.</dd>
<dt>*</dt>
<dd>Added QR matrix decomposition.</dd>
<dt>*</dt>
<dd>Added a number of copulas (thanks to Marek Glowacki.)</dd>
<dt>*</dt>
<dd>Added constrained cubic spline.</dd>
<dt>*</dt>
<dd>Implemented derivative and second derivative of log-interpolations.</dd>
<dt>*</dt>
<dd>Added Gauss-Lobatto integration.</dd>
<dt>*</dt>
<dd>Added student-t distribution (thanks to Roland Lichters.)</dd></dl>
<p> MODELS</p>
<dl>
<dt>*</dt>
<dd>Added calibrated GJR-GARCH model (thanks to Yee Man Chan.)</dd>
<dt>*</dt>
<dd>Added Feller constraint to Heston model.</dd></dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Refactored variance-swap engines (the underlying stochastic process is now passed to the pricing engine.)</dd>
<dt>*</dt>
<dd>Added GJR-GARCH pricing engines for vanilla options (thanks to Yee Man Chan.)</dd></dl>
<p> PROCESSES</p>
<dl>
<dt>*</dt>
<dd>Added Euler end-point discretization (thanks to Frank Hoermann.)</dd>
<dt>*</dt>
<dd>Added GJR-GARCH process (thanks to Yee Man Chan.)</dd>
<dt>*</dt>
<dd>Added Bates process.</dd></dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</dt>
<dd>Added turn-of-year effect to yield-curve bootstrapping (generalized to multiple jumps at arbitrary dates.)</dd>
<dt>*</dt>
<dd>Added local bootstrap of forward rates (thanks to Simon Ibbotson.)</dd>
<dt>*</dt>
<dd>Disabled copies of interpolated curves (the existing behavior was incorrect. A fix to re-enable copying will be included in a future release.)</dd></dl>
<p> VOLATILITY</p>
<dl>
<dt>*</dt>
<dd>Added constant cap/floor term volatility structure.</dd>
<dt>*</dt>
<dd>Added stripped optionlet.</dd></dl>
<p> <code>Release 0.9.0 &#8211; December 24th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Fixes for MSYS and Cygwin build.</dd>
<dt>*</dt>
<dd>Fixes for VC++ build with CLR support enabled.</dd>
<dt>*</dt>
<dd>Dropped MetroWerks CodeWarrior support.</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Fix for business-days calculation (thanks to Piter Dias.)</dd>
<dt>*</dt>
<dd>Updated Hong Kong&#8217;s holidays for 2008 and China&#8217;s for 2007.</dd>
<dt>*</dt>
<dd>Added new holiday to Canadian calendars (thanks to Matt Knox.)</dd>
<dt>*</dt>
<dd>Fixed joint-calendar specification (thanks to Jay Walters.)</dd>
<dt>*</dt>
<dd>Split Canadian calendar into settlement and TSX (thanks to Matt Knox.)</dd>
<dt>*</dt>
<dd>Added Brazilian exchange calendar (thanks to Richard Gomes.)</dd>
<dt>*</dt>
<dd>Fixes for the Brazilian calendars (thanks to Piter Dias.)</dd></dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</dt>
<dd>Added average-BMA coupon (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>Fixed-rate coupons can now accept an InterestRate instance (thanks to Piter Dias.)</dd>
<dt>*</dt>
<dd>implemented cash-flow vector builders as helper classes to ease skipping default parameters and single/multiple inputs.</dd></dl>
<p> DATES</p>
<dl>
<dt>*</dt>
<dd>Extended date range up to year 2199.</dd>
<dt>*</dt>
<dd>Fixed period comparison (thanks to Chris Kenyon.)</dd>
<dt>*</dt>
<dd>Fixed short date formatting (thanks to Robert Lopez.)</dd>
<dt>*</dt>
<dd>Enhanced period algebra.</dd></dl>
<p> INDEXES</p>
<dl>
<dt>*</dt>
<dd>Added BMA index (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>Added inflation indexes (thanks to Chris Kenyon.)</dd>
<dt>*</dt>
<dd>Added historical interest-rate index analysis.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Added BMA swaps (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>Added year-on-year and zero-coupon inflation swaps (thanks to Chris Kenyon.)</dd>
<dt>*</dt>
<dd>Fixed stub-date management and backward date generation for fixed-rate bonds (thanks to Toyin Akin.)</dd>
<dt>*</dt>
<dd>Added clean/dirty bond-price calculation from Z-spread.</dd></dl>
<p> LATTICES</p>
<dl>
<dt>*</dt>
<dd>Fixed Tsiveriotis-Fernandes tree initialization (thanks to John Maiden.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added multi-dimensional cost function for least-square problems (thanks to Guillaume Pealat.)</dd>
<dt>*</dt>
<dd>Added histogram class (thanks to Gang Liang.)</dd>
<dt>*</dt>
<dd>Added log-cubic interpolation.</dd>
<dt>*</dt>
<dd>Fixed conjugate-gradient bug.</dd>
<dt>*</dt>
<dd>Fixed nested Levenberg-Marquardt bug.</dd></dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Refactored option engines (the underlying stochastic process is now passed to the pricing engine.)</dd>
<dt>*</dt>
<dd>Refactored bond, cap/floor, swap, and swaption engines (the discount curve is now passed to the pricing engine.)</dd>
<dt>*</dt>
<dd>Added Heston/Hull-White analytic and Monte Carlo engines for vanilla options.</dd>
<dt>*</dt>
<dd>Fixed bug in blackFormulaCashItmProbability in case of non null displacement.</dd></dl>
<p> PROCESSES</p>
<dl>
<dt>*</dt>
<dd>Added hybrid Heston/Hull-White process.</dd>
<dt>*</dt>
<dd>Fixed joint-process bug.</dd></dl>
<p> QUOTES</p>
<dl>
<dt>*</dt>
<dd>Added forward-swap quote.</dd></dl>
<p> RANDOM NUMBERS</p>
<dl>
<dt>*</dt>
<dd>Fixed ordering of primitive polynomials for Sobol/Levitan and Sobol/Levitan/Lemieux methods.</dd>
<dt>*</dt>
<dd>Added JoeKuoD5, JoeKuoD6 and JoeKuoD7 direction integers for Sobol generator.</dd>
<dt>*</dt>
<dd>Added Kuo, Kuo2 and Kuo3 direction integers for Sobol generator.</dd>
<dt>*</dt>
<dd>Added class to generate low-discrepancy sequences using a lattice rule.</dd></dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</dt>
<dd>Added discount curve fitted on bond prices (thanks to Allen Kuo.)</dd>
<dt>*</dt>
<dd>Added BMA-swap rate helper (thanks to Roland Lichters.)</dd>
<dt>*</dt>
<dd>Made SwapRateHelper forward-start enabled.</dd>
<dt>*</dt>
<dd>Added universal term-structure bootstrapper (thanks to Chris Kenyon.)</dd>
<dt>*</dt>
<dd>Added abstract inflation term structures (thanks to Chris Kenyon.)</dd>
<dt>*</dt>
<dd>Added piecewise inflation curves (thanks to Chris Kenyon.)</dd></dl>
<p> <code>Release 0.8.1 &#8211; June 4th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Version 0.8.1 adds support for Boost 1.34 on Linux systems. If you are using version 0.8.0 on Windows systems, you do not need this upgrade.</dd></dl>
<p> <code>Release 0.8.0 &#8211; May 30th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Version 0.8.0 is the last QuantLib release to support the Metrowerks CodeWarrior compiler (which was discountinued by Metrowerks.) If you use such compiler and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dd></dl>
<p> SOURCE TREE</p>
<dl>
<dt>*</dt>
<dd>Files and folders in the source tree have been reorganized (hopefully for th ebetter.) If you only included &lt;ql/quantlib.hpp&gt;, all changes were taken care of for you. if you included specific headers, you might want to check its current location; in particular, all folder names are now lowercase.</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added 2007 holidays for Indonesia, Saudi Arabia, and South Korea calendars.</dd></dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</dt>
<dd>Added floater range-accrual coupons.</dd></dl>
<p> INDEXES</p>
<dl>
<dt>*</dt>
<dd>Added EuriborSwapFixB family.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Added capped/floored floating-rate bond. It can also be used for reverse floaters.</dd>
<dt>*</dt>
<dd>Added delta, gamma and theta to binomial option engines (thanks to Steve Cook.)</dd>
<dt>*</dt>
<dd>Refactored basket engines to allow for more payoffs.</dd></dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</dt>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. Improvements since release 0.4.0 include normal forward-rate market model, lognormal CMS market model, lognormal coterminal-swap market model, and calibration to caplets and coterminal swaptions. The interface of the model and its integration with the bulk of the library are still in development.</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Adaptive Gauss-Kronrod integration added.</dd>
<dt>*</dt>
<dd>Added Higham&#8217;s nearest correlation matrix method (thanks to Neil Firth)</dd>
<dt>*</dt>
<dd>Refactored optimization framework.</dd></dl>
<p> PROCESSES</p>
<dl>
<dt>*</dt>
<dd>Added new discretization schema to Heston process.</dd></dl>
<p> UTILITIES</p>
<dl>
<dt>*</dt>
<dd>The Handle class was split into RelinkableHandle (behaving like the old Handle class) and Handle (which is notified when its copies are relinked, but cannot itself be relinked.) The former can safely be returned from inspectors.</dd></dl>
<p> <code>Release 0.4.0 &#8211; February 20th, 2007</code> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Starting with release 0.4.0, the Borland free compiler 5.5 and Microsoft Visual C++ 6.0 are no longer supported. If you use one of these compilers and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added 2007 holidays for Hong Kong, India, Singapore, and Taiwan exchanges.</dd></dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</dt>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. Improvements since release 0.3.14 include the use of quasi-random number generators and the calculation of Greeks and of upper bounds for instruments with early-exercise features. The interface of the model and its integration with the bulk of the library are still in development.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Added helper classes to make it easier to instantiate swaps, caps/floors, and CMS instruments.</dd></dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</dt>
<dd>Added capped/floored floating-rate coupons (including convexity adjustment.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Curve, domain and surface interfaces added.</dd></dl>
<p> PROCESSES</p>
<dl>
<dt>*</dt>
<dd>Added reversion level to Ornstein-Uhlenbeck process (thanks to Roland Lichters.)</dd></dl>
<p> VOLATILITY TERM STRUCTURES</p>
<dl>
<dt>*</dt>
<dd>Added stripping of caplet-volatility term structure from cap quotes.</dd>
<dt>*</dt>
<dd>Improved SABR interpolation and calibration.</dd></dl>
<p> <code>Release 0.3.14 &#8211; November 6th, 2006</code> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Version 0.3.14 is the last QuantLib release to support the Borland free compiler 5.5 and Microsoft Visual C++ 6.0. If you use one of these compilers and want support to continue, you can volunteer for maintaining the necessary patches: contact the QuantLib developers for information.</dd></dl>
<p> LIBOR MARKET MODEL</p>
<dl>
<dt>*</dt>
<dd>This release includes an experimental implementation of a Libor market model developed with Mark Joshi. The interface and its integration with the bulk of the library are still in development.</dd></dl>
<p> CURRENCIES</p>
<dl>
<dt>*</dt>
<dd>Added Romanian new lev.</dd></dl>
<p> DATES, CALENDARS, AND DAY COUNTERS</p>
<dl>
<dt>*</dt>
<dd>Added all serial 3M IMM futures (thanks to Toyin Akin.)</dd>
<dt>*</dt>
<dd>Reworked the Schedule class so that it follows market conventions more closely.</dd>
<dt>*</dt>
<dd>Added business/252 day-count convention (thanks to Piter Dias.)</dd></dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</dt>
<dd>Added base swap-rate class and a number of actual swap rates.</dd>
<dt>*</dt>
<dd>Added constant-maturity swap coupons (including convexity adjustment.)</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Added asset swaps.</dd>
<dt>*</dt>
<dd>Added face amount to bonds (defaulting to 100.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added hypersphere and lower-diagonal salvaging algorithms (thanks to Yiping Chen.)</dd></dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Added Longstaff-Schwartz Monte-Carlo algorithm for American/Bermudan equity options with deterministic interest rates.</dd></dl>
<p> TERM STRUCTURE</p>
<dl>
<dt>*</dt>
<dd>Added piecewise-spreaded yield curve (thanks to Roland Lichters.)</dd></dl>
<p> <code>Release 0.3.13 &#8211; July 31st, 2006</code> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added NERC calendar (thanks to Joe Byers.)</dd></dl>
<p> INSTRUMENTS AND PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Added continuous fixed and floating lookback options (thanks to Warren Chou.)</dd>
<dt>*</dt>
<dd>Added FRA and forward fixed-coupon bonds; examples provided (thanks to Allen Kuo.)</dd>
<dt>*</dt>
<dd>Added variance swaps (thanks to Warren Chou.)</dd>
<dt>*</dt>
<dd>Added composite instrument; example provided.</dd>
<dt>*</dt>
<dd>Added cash-settled swaption pricing in Black swaption engine; test provided.</dd>
<dt>*</dt>
<dd>Added discrete dividends and soft callability to convertible bonds.</dd></dl>
<p> INTEREST RATES</p>
<dl>
<dt>*</dt>
<dd>Fixed business-day conventions for Euribor and LIBOR indices (following below one month, month-end from one month onwards.)</dd></dl>
<p> MODELS</p>
<dl>
<dt>*</dt>
<dd>Added more complex market parameterizations and performance improvements for Libor market model (thanks to Klaus Spanderen.)</dd></dl>
<p> PROCESSES</p>
<dl>
<dt>*</dt>
<dd>Renamed BlackScholedProcess to GeneralizedBlackScholedProcess; specialized classes added for Black-Scholes, Merton, Black and Garman-Kohlhagen processes.</dd>
<dt>*</dt>
<dd>Added Hull-White and G2 processes for Monte Carlo simulation (thanks to Banca Profilo.)</dd></dl>
<p> RANDOM NUMBERS</p>
<dl>
<dt>*</dt>
<dd>Added possibility to skip directly to the n-th item in a Sobol sequence (thanks to Richard Gould.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added SABR interpolation for volatilities.</dd>
<dt>*</dt>
<dd>Added general linear least-squares regression (thanks to Klaus Spanderen.)</dd></dl>
<p> <code>Release 0.3.12 &#8211; March 27th, 2006</code> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added Brazilian calendar (thanks to Piter Dias.)</dd>
<dt>*</dt>
<dd>Added Argentinian, Icelandic, Indonesian, Mexican, and Ukrainian calendars.</dd></dl>
<p> INSTRUMENTS AND PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Added convertible bonds (thanks to Theo Boafo.)</dd>
<dt>*</dt>
<dd>The cash flows returned by the Bond::cashflows method now include the redemption.</dd>
<dt>*</dt>
<dd>SimpleSwap can now be set an engine. If none is set, the old cash-flow-based calculation is used.</dd>
<dt>*</dt>
<dd>Generalized McVanillaEngine so that it can manage n-dimensional processes; it now subsumes McHestonEngine.</dd>
<dt>*</dt>
<dd>Added pricing of Bermudan options on binomial trees (thanks to Enrico Michelotti.)</dd>
<dt>*</dt>
<dd>Separated accrual and payment conventions for bonds.</dd>
<dt>*</dt>
<dd>Modified basis-point sensitivity calculation so that it returns the cash variation for a basis-point change in rate (it used to return the figure to be multiplied by the variation in order to obtain the same result.)</dd></dl>
<p> MODELS</p>
<dl>
<dt>*</dt>
<dd>Added weights to short-rate model calibration (thanks to Enrico Michelotti.)</dd>
<dt>*</dt>
<dd>Added Libor market model (thanks to Klaus Spanderen.)</dd></dl>
<p> OPTIMIZATION</p>
<dl>
<dt>*</dt>
<dd>Added Levenberg-Marquardt optimization method (thanks to Klaus Spanderen.)</dd></dl>
<p> EXAMPLES</p>
<dl>
<dt>*</dt>
<dd>Merged American and European option examples; added Bermudan option.</dd>
<dt>*</dt>
<dd>Added convertible-bond example (thanks to Theo Boafo.)</dd></dl>
<p> <code>Release 0.3.11 &#8211; October 20th, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</dt>
<dd>Added configuration option for adding current function information to error messages.</dd>
<dt>*</dt>
<dd>Added hook for multiple sessions to Singleton.</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added Bombay and Taipei calendars.</dd></dl>
<p> CURRENCIES</p>
<dl>
<dt>*</dt>
<dd>Added new Turkish lira.</dd></dl>
<p> INDEXES</p>
<dl>
<dt>*</dt>
<dd>More accurate LIBOR calendars (thanks to Daniele de Francesco.)</dd>
<dt>*</dt>
<dd>Added DKKLibor, EURLibor, and NZDLibor indexes.</dd>
<dt>*</dt>
<dd>Added TRLibor index (thanks to Sercan Atalik.)</dd></dl>
<p> PRICING ENGINES</p>
<dl>
<dt>*</dt>
<dd>Added Bates stochastic-volatility model; tests provided (thanks to Klaus Spanderen.)</dd>
<dt>*</dt>
<dd>Added vega to analytic discrete-averaging Asian engine; test provided (thanks to Gary Kennedy.)</dd>
<dt>*</dt>
<dd>Added stochastic process for caplet Libor market model; tests provided (thanks to Klaus Spanderen.)</dd></dl>
<p> TERM STRUCTURES</p>
<dl>
<dt>*</dt>
<dd>Added fixed-coupon bond helper for curve bootstrapping (thanks to Toyin Akin.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added tabulated Gauss-Legendre quadratures (thanks to Gary Kennedy.)</dd>
<dt>*</dt>
<dd>Added more precise implementation of bivariate cumulative normal distribution (thanks to Gary Kennedy.)</dd></dl>
<p> <code>Release 0.3.10 &#8211; July 14th, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</dt>
<dd>The suggested syntax for setting and registering with the global evaluation date is now:</dd></dl>
<pre><code>Settings::instance().evaluationDate() = date;
registerWith(Settings::instance().evaluationDate());
</code></pre>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Istanbul calendar added (thanks to Serkan Atalik.)</dd></dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Faster implementation of binomial and trinomial trees.</dd></dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Added generic multi-dimensional stochastic process.</dd>
<dt>*</dt>
<dd>Added stochastic process array (thanks to Klaus Spanderen.)</dd>
<dt>*</dt>
<dd>Multi-path generator now takes a generic stochastic process; tests provided.</dd>
<dt>*</dt>
<dd>New Path class implemented which stores asset values rather than variations; this makes pricers independent on whether or not log-variations were calculated. The new class is enabled when QL_DISABLE_DEPRECATED is defined; the old class is used otherwise.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Multi-asset option now takes a generic stochastic process.</dd></dl>
<p> MODELS</p>
<dl>
<dt>*</dt>
<dd>Added Heston stochastic-volatility model; tests provided (thanks to Klaus Spanderen.) Provided code include:</dd>
<dt> *</dt>
<dd>a corresponding stochastic process;</dd>
<dt> *</dt>
<dd>analytic and Monte Carlo option-pricing engines;</dd>
<dt> *</dt>
<dd>parameter calibration.</dd></dl>
<p> CASH FLOWS</p>
<dl>
<dt>*</dt>
<dd>Cash-flow analyses such as NPV, IRR, convexity and duration added (thanks to Charles Whitmore.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added Gaussian orthogonal polynomials and Gaussian quadratures; tests provided (thanks to Klaus Spanderen.)</dd>
<dt>*</dt>
<dd>Convergence statistics added; tests provided (thanks to Gary Kennedy.)</dd></dl>
<p> <code>Release 0.3.9 &#8211; May 2nd, 2005</code> GLOBAL FEATURES</p>
<dl>
<dt>*</dt>
<dd>QL_SQRT, QL_MIN etc. deprecated in favor of std::sqrt, std::min&#8230;</dd>
<dt>*</dt>
<dd>Added a tentative tracing facility to ease debugging.</dd>
<dt>*</dt>
<dd>Formatters deprecated in favor of output manipulators. A number of data types can now be sent directly to output streams.</dd>
<dt>*</dt>
<dd>Stream-based implementation of QL_REQUIRE, QL_TRACE and similar macros. Together with manipulators, this allows one to write simpler error messages, as in:</dd></dl>
<pre> QL_FAIL('forward at date ' &lt;&lt; d &lt;&lt; ' is ' &lt;&lt; io::rate(f));</pre>
<p>INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Improved Bond class</dd>
<dt> *</dt>
<dd>yield-related calculation can be performed with either compounded or continuous compounding;</dd>
<dt> *</dt>
<dd>added theoretical price based on discount curve;</dd>
<dt> *</dt>
<dd>fixed-rate coupon bonds can define different rates for each coupon;</dd>
<dt> *</dt>
<dd>added zero-coupon and floating-rate bonds (thanks to StatPro.)</dd></dl>
<dl>
<dt>*</dt>
<dd>Option instruments now take a generic StochasticProcess; however, most pricing engines still require a BlackScholesProcess. They should be checked to see whether the requirement can be relaxed. Following this change, Merton76Process no longer inherits from BlackScholesProcess. This avoids erroneous upcasts.</dd>
<dt>*</dt>
<dd>Partial fix for Bermudan swaptions with exercise lag (thanks to Luca Berardi for the report and discussion.)</dd>
<dt>*</dt>
<dd>Fix for analytic cap/floor engine; caplets/floorlets whose fixing is in the past are now calculated correctly (thanks to Aurelien Chanudet.)</dd></dl>
<p> CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added Bratislava and Prague calendars.</dd></dl>
<p> INDICES</p>
<dl>
<dt>*</dt>
<dd>Fixed calendars for LIBOR fixings (thanks to Daniele De Francesco.)</dd></dl>
<p> FINITE_DIFFERENCES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Migrated finite-difference pricers to pricing-engine framework (thanks to Joseph Wang.)</dd></dl>
<p> YIELD TERM STRUCTURES</p>
<dl>
<dt>*</dt>
<dd>Added generic piecewise yield term structure. Client code can choose what to interpolate (discounts, zero yields, forwards) and how (linear, log-linear, flat) by instantiating types such as:</dd></dl>
<pre> PiecewiseYieldCurve&lt;Discount,LogLinear&gt;
 PiecewiseYieldCurve&lt;ZeroYield,Linear&gt;
 PiecewiseYieldCurve&lt;ForwardRate,Linear&gt;</pre>
<dl>
<dt>*</dt>
<dd>Interpolated discount, zero-yield and forward-rate curves can now be set any interpolation.</dd>
<dt>*</dt>
<dd>FlatForward can now take rates with compounding other than continuous.</dd>
<dt>*</dt>
<dd>Fix for extrapolation in zero-spreaded and forward-spreaded yield term structure (thanks to Adjriou Belak for the report.)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added backward- and forward-flat interpolations.</dd></dl>
<p> <code>Release 0.3.8 &#8211; December 22nd, 2004</code> REQUIRED PACKAGES</p>
<dl>
<dt>*</dt>
<dd>Boost version 1.31.0 or later is now required.</dd></dl>
<p> DOCUMENTATION</p>
<dl>
<dt>*</dt>
<dd>Documentation now includes a FAQ page.</dd></dl>
<p> GLOBAL FEATURES</p>
<dl>
<dt>*</dt>
<dd>Global evaluation date added through Settings class. Used for index-fixing and exchange-rate lookup.</dd>
<dt>*</dt>
<dd>added InterestRate class, which encapsulate the interest rate compounding algebra. It manages day-counting convention, compounding convention, conversion between different conventions, and discount/compounding factor calculations. It also has its own formatter.</dd></dl>
<p> INSTRUMENTS</p>
<dl>
<dt>*</dt>
<dd>Bond and FixedCouponBond classes added (thanks to Jeff Yu) providing price/yield conversions; tests provided.</dd></dl>
<p> DATE, CALENDARS, AND DAY COUNT CONVENTIONS</p>
<dl>
<dt>*</dt>
<dd>Reworked Date interface. Added nextWeekday() and nthWeekday() static methods to the class Date. Added nextIMM() for the calculation of the next IMM date.</dd>
<dt>*</dt>
<dd>Added WeekdayFormatter and FrequencyFormatter</dd>
<dt>*</dt>
<dd>Added &#8216;1/1&#8217; day counter. The Actual365 is deprecated: as per ISDA documentation &#8216;Actual/365&#8217; is the same as &#8216;Actual/Actual&#8217;. Use the ActualActual class instead, or the Actual365Fixed class.</dd>
<dt>*</dt>
<dd>Added dayCounterFromString(std::string) to QuantLibFunctions.</dd>
<dt>*</dt>
<dd>Improved Beijing calendar (thanks to Zhou Wu.)</dd></dl>
<p> CURRENCIES AND FX RATES</p>
<dl>
<dt>*</dt>
<dd>Added currency classes; CurrencyTag replaced in library code.</dd>
<dt>*</dt>
<dd>Added money class providing arithmetic with or without conversions; tests provided.</dd>
<dt>*</dt>
<dd>Added exchange-rate class; tests provided.</dd>
<dt>*</dt>
<dd>Added exchange-rate manager with smart rate lookup, i.e., able to derive a missing exchange rate as a chain of provided rates; tests provided.</dd></dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Added Faure low-discrepancy sequence (thanks to Gianni Piolanti;) tests provided.</dd>
<dt>*</dt>
<dd>Added randomized (shifted) low discrepancy sequences that will be used for randomized quasi Monte Carlo.</dd>
<dt>*</dt>
<dd>Added SeedGenerator class, for random generation of seeds when they are not given by the user.</dd>
<dt>*</dt>
<dd>Added the implementation of Sobol sequences using the coefficients of the free direction integers as provided by Bratley and Fox, who credited unpublished work of Sobol&#8217;s and Levitan&#8217;s.</dd>
<dt>*</dt>
<dd>Added an implementation of Sobol sequences using the coefficients of the free direction integers of Lemieux, Cieslak, and Luttmer. Coefficients for d&lt;=40 are the same as in Bradley-Fox. For dimension 40&lt;d&lt;=360 the coefficients have been calculated as optimal values based on the &#8216;resolution&#8217; criterion. The values has been provided by Christiane Lemieux, private communication, September 2004.</dd>
<dt>*</dt>
<dd>PathGenerator now works correctly with processes describing S instead of log S. Geometric Brownian process added (thanks to Walter Penschke.)</dd></dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Reworked the DiscretizedAsset interface.</dd></dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Added pricing engine for American options with Ju quadratic approximation.</dd>
<dt>*</dt>
<dd>Average-price Asian pricers have been deprecated. New equivalent pricing engines added.</dd></dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>Added current coupon to discretized swap and cap/floor.</dd>
<dt>*</dt>
<dd>Added IndexManager as a singleton (will replace XiborManager&#8211;already obsoleted in library code.)</dd>
<dt>*</dt>
<dd>Added DayCounter parameter to ParCoupon (to be used for accruing spreads and past fixings.) When missing, it defaults to that of the term structure.</dd>
<dt>*</dt>
<dd>Added compilation flag to select default floating-coupon type.</dd>
<dt>*</dt>
<dd>IndexedCoupon can now take a generic index rather than a Libor (thanks to Daniele De Francesco.)</dd>
<dt>*</dt>
<dd>Added hooks for convexity adjustment in floating-rate coupons; implemented adjustment for InArrearIndexedCoupon.</dd></dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</dt>
<dd>TermStructure renamed to YieldTermStructure (the former name was deprecated.)</dd>
<dt>*</dt>
<dd>New base class BaseTermStructure which can calculate its reference date based on the global evaluation date. YieldTermStructure, BlackVolTermStructure, LocalVolTermStructure, CapFlatVolatilityStructure, CapletForwardVolatilityStructure, and SwaptionVolatilityStructure are now derived from BaseTermStructure so that they inherit its functionality.</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>Added Singleton pattern.</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added N-dimensional cubic spline (thanks to Roman Gitlin.)</dd>
<dt>*</dt>
<dd>Added CovarianceDecomposition class (decomposes a covariance matrix into standard deviations and correlations)</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>Renamed RelinkableHandle to Handle.</dd></dl>
<p> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Support for Dev-C++ IDE added.</dd>
<dt>*</dt>
<dd>Fixes for gcc 2.95 added (thanks to Michael Dirkmann.)</dd></dl>
<p> <code>Release 0.3.7 &#8211; July 23rd, 2004</code> IMPORTANT QuantLib now depends on the Boost library (</p>
<p><a rel="nofollow" href="http://www.boost.org">www.boost.org</a>). You will need a working Boost installation in order to compile and use QuantLib. Instructions for installing Boost from sources are available at &lt;<a rel="nofollow" href="http://www.boost.org/more/getting_started.html">http://www.boost.org/more/getting_started.html</a>&gt;. Pre-packaged binaries might be available from other sources. Google is your friend (or Debian, or Fink&#8230;) DATE, CALENDARS, AND DAY COUNT CONVENTIONS</p>
<dl>
<dt>*</dt>
<dd>Working on differentiating calendars depending on country or exchange, instead of city.</dd>
<dt>*</dt>
<dd>Added Italy (Settlement, Exchange), United Kingdom (Settlement, Exchange, Metals), United States (Settlement, Exchange, GovermentBond), Xetra.</dd>
<dt>*</dt>
<dd>Milan, London, and NewYork calendars have been deprecated.</dd>
<dt>*</dt>
<dd>Added (old-style) calendars: Beijing, Hong Kong, Riyadh, Seoul, Singapore, Taiwan.</dd>
<dt>*</dt>
<dd>RollingConvention has been renamed BusinessDayConvention, as for ISDA definitions.</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added rounding algorythms as per OMG enumeration/definition.</dd></dl>
<p> TEST SUITE</p>
<dl>
<dt>*</dt>
<dd>Moved to Boost unit test framework. CppUnit is no longer needed.</dd>
<dt>*</dt>
<dd>Added test for quanto and forward compound engines.</dd>
<dt>*</dt>
<dd>Added test for roundings.</dd>
<dt>*</dt>
<dd>Added test for discrete dividend European options.</dd>
<dt>*</dt>
<dd>Added test for cliquet options.</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>enable/disableExtrapolation() methods were added to a few classes such as TermStructure. They make it possible to persistently allow extrapolation without the need of specifying it at every method call.</dd>
<dt>*</dt>
<dd>Added user-configurable flag to disable usage of deprecated classes.</dd></dl>
<p> PORTABILITY</p>
<dl>
<dt>*</dt>
<dd>Fink package available</dd>
<dt>*</dt>
<dd>Visual C++ 7.x project files added</dd></dl>
<p> <code>Release 0.3.6 &#8211; April 15th, 2004</code> Bug-fix release for QuantLib 0.3.5. A bug was removed where calls to impliedVolatility() would break the state of the option and of all options sharing the same stochastic process. <code>Release 0.3.5 &#8211; March 31th, 2004</code> BOOST SUPPORT</p>
<dl>
<dt>*</dt>
<dd>When available, QuantLib 0.3.5 now uses parts of the Boost library. The presence of Boost is detected automatically under Unix/Linux systems; on Windows systems, it must be enabled by uncommenting the relevant line in ql/userconfig.hpp.</dd></dl>
<dl>
<dt>*</dt>
<dd>In the next QuantLib release, the presence of the Boost library will be mandatory.</dd></dl>
<p> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Modified MultiPath interface to remove drifts. They are now in the stochastic processes.</dd>
<dt>*</dt>
<dd>Preliminary implementation of Longstaff-Schwartz least-squares</dd>
<dt>*</dt>
<dd>Monte Carlo pricer for European basket options</dd>
<dt>*</dt>
<dd>Brownian-bridge bugs fixed</dd>
<dt>*</dt>
<dd>StochasticProcess base class and derived classes (diffusion, jump-diffusion, etc.) have been created.</dd></dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Pricing engines now use Payoff and Exercise classes.</dd>
<dt>*</dt>
<dd>American basket options.</dd>
<dt>*</dt>
<dd>Binary barrier option replaced by vanilla option with digital payoff.</dd>
<dt>*</dt>
<dd>Stulz engine for max and min basket calls and puts on two assets.</dd>
<dt>*</dt>
<dd>American binary option added (a.k.a. one-touch, american digital, americal barrier, etc.) with different payoffs (cash/asset at hit/expiry, etc.)</dd>
<dt>*</dt>
<dd>Added engine for Merton 1976 jump-diffusion process.</dd>
<dt>*</dt>
<dd>Added Bjerksund and Stensland approximation for American option (still unstable.)</dd>
<dt>*</dt>
<dd>Added Barone-Adesi and Whaley approximation for American option.</dd>
<dt>*</dt>
<dd>Improved Black formula engine with more greeks added.</dd>
<dt>*</dt>
<dd>Discrete geometric asian option.</dd>
<dt>*</dt>
<dd>Added Leisen-Reimer binomial tree.</dd></dl>
<p> SHORT RATE MODELS</p>
<dl>
<dt>*</dt>
<dd>Model renamed to ShortRateModel. A typedef is provided for backward compatibility&#8211;it will be removed in subsequent releases.</dd></dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>bug fix for short time (0&lt;=t&lt;=Tmin) interpolation</dd></dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Method renamed to OptimizationMethod. A typedef is provided for backward compatibility&#8211;it will be removed in subsequent releases.</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>Composite pattern</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Improved cubic spline interpolation. It now handles end conditions such as first derivative value, second derivative value, not-a-knot. Hyman filter for monotonically constrained interpolation has been implemented. Primitive calculation has been enabled in addition to derivative and second derivative.</dd>
<dt>*</dt>
<dd>Primitive, first derivative, and second derivative functions are available for linear interpolator.</dd>
<dt>*</dt>
<dd>Singular value decomposition improved.</dd>
<dt>*</dt>
<dd>Added bivariate cumulative normal distribution.</dd>
<dt>*</dt>
<dd>Added binomial coefficient calculation, binomial distribution, cumulative binomial distribution, and Peizer-Pratt inversion (method 2.)</dd>
<dt>*</dt>
<dd>Added beta functions.</dd>
<dt>*</dt>
<dd>Added Poisson distribution and cumulative distribution.</dd>
<dt>*</dt>
<dd>Added incomplete gamma functions.</dd>
<dt>*</dt>
<dd>Added factorial calculation.</dd>
<dt>*</dt>
<dd>Added rank-reduced square root and improved pseudo-square root of square symmetric matrices.</dd>
<dt>*</dt>
<dd>Added Cholesky decomposition.</dd></dl>
<p> TEST SUITE</p>
<dl>
<dt>*</dt>
<dd>Added test for cubic spline interpolation.</dd>
<dt>*</dt>
<dd>Added test for singular value decomposition.</dd>
<dt>*</dt>
<dd>Added test for two-asset baskets using the Stulz pricing engine.</dd>
<dt>*</dt>
<dd>Added test for Monte Carlo American cash-at-hit options.</dd>
<dt>*</dt>
<dd>Added test for jump-diffusion engine.</dd>
<dt>*</dt>
<dd>Added test for American and European digital options.</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>Inner namespaces have been deprecated.</dd>
<dt>*</dt>
<dd>Added frequency enumeration, including &#8216;once&#8217;.</dd>
<dt>*</dt>
<dd>MarketElement renamed to Quote.</dd>
<dt>*</dt>
<dd>Handling strike=0.0 where possible.</dd>
<dt>*</dt>
<dd>More Payoff classes have been introduced: gap, asset-or-nothing, cash-or-nothing. Payoff is now extensively used.</dd>
<dt>*</dt>
<dd>Exercise class is now polymorphic. More derived classes have been introduced, and they are now extensively used.</dd>
<dt>*</dt>
<dd>Introduced QL_FAIL macro.</dd>
<dt>*</dt>
<dd>Added calendar for Copenhagen</dd>
<dt>*</dt>
<dd>14 April 2004 (election day) added to Johannesburg calendar as a one-off holiday.</dd>
<dt>*</dt>
<dd>Documentation generated with Doxygen 1.3.6.</dd>
<dt>*</dt>
<dd>Win32 installer generated with NSIS 2.0.</dd></dl>
<p> <code>Release 0.3.4 &#8211; November 21th, 2003</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>MC European in one step with strike-independent vol curve (hopefully)</dd>
<dt>*</dt>
<dd>Path pricer for Binary options. It should cover both European and American style options. Also known as: Digital, Binary, Cash-At-Hit, Cash-At-Expiry.</dd>
<dt>*</dt>
<dd>Path pricers for barrier options</dd></dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>More options moved to the new pricing engine framework: binary, barrier</dd>
<dt>*</dt>
<dd>Changed setupEngine() into setupArguments(args)</dd>
<dt>*</dt>
<dd>Moved pricing-engine machinery up to Instrument class</dd></dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>New basis-point sensitivity functions</dd>
<dt>*</dt>
<dd>Added Swap::startDate() and maturity()</dd>
<dt>*</dt>
<dd>Cap/floor fixing days taken into account</dd></dl>
<p> SHORT RATE MODELS</p>
<dl>
<dt>*</dt>
<dd>An additional constraint can now be passed to the calibration</dd></dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Visitable volatility term structures</dd></dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Added composite constraint</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>Visitor, Alexandrescu-style (saves some code duplication)</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added more integration algorithms contributed by Roman Gitlin</dd>
<dt>*</dt>
<dd>Relaxed constaints on interval boundaries for integration algorithms</dd>
<dt>*</dt>
<dd>Interpolation traits</dd></dl>
<p> TEST SUITE</p>
<dl>
<dt>*</dt>
<dd>Added implied cap/floor term volatility test</dd>
<dt>*</dt>
<dd>Added test for binary options in PricingEngine Framework.</dd>
<dt>*</dt>
<dd>Added tests for Barrier options in PricingEngine Framework. Some Monte Carlo tests, but not comprehensive.</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>Conditionally allowed negative yields (disabled by default)</dd>
<dt>*</dt>
<dd>Null calendar and simple day counter for reproducing theoretical calculations</dd>
<dt>*</dt>
<dd>Fixed for VC++.Net compilation</dd>
<dt>*</dt>
<dd>Added spec file for RPMs</dd>
<dt>*</dt>
<dd>Added global flag for early/late payments</dd>
<dt>*</dt>
<dd>Enabled test suite for Borland</dd>
<dt>*</dt>
<dd>Removed OnTheEdge VC++ configurations</dd>
<dt>*</dt>
<dd>Added VC++ configurations for static and dynamic Multithread libraries</dd>
<dt>*</dt>
<dd>Upgraded to use Doxygen 1.3.4</dd></dl>
<p> <code>Release 0.3.3 &#8211; September 3rd, 2003</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Re-templatized Monte Carlo model based on traits.</dd>
<dt>*</dt>
<dd>New path generator based on DiffusionProcess, TimeGrid, and externally initialized random number generator.</dd>
<dt>*</dt>
<dd>Added Halton low discrepancy sequence.</dd>
<dt>*</dt>
<dd>Added sequence generators: random sequence generator creates a sequence generator out of a random number generator. InvCumGaussianRsg creates a gaussian sequence generator out of a uniform (random or low discrepancy) sequence generator.</dd>
<dt>*</dt>
<dd>RNG as constructor input constructor( long seed) deprecated.</dd>
<dt>*</dt>
<dd>Mersenne Twister random number generator added</dd>
<dt>*</dt>
<dd>Old PathPricers, PathGenerators, etc are available with a trailing _old</dd>
<dt>*</dt>
<dd>Added Jakel&#8217;s Brownian Bridge (not used yet.)</dd>
<dt>*</dt>
<dd>Sobol Random Sequence Generator. Unit and Jakel.</dd>
<dt>*</dt>
<dd>Added randomized Halton sequences.</dd></dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Old class Grid no longer exists, use CenteredGrid to obtain the same result.</dd></dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Abstracted discretized option.</dd>
<dt>*</dt>
<dd>Additive binomial trees. All binomial trees now use DiffusionProcess.</dd>
<dt>*</dt>
<dd>Added Tian binomial tree.</dd></dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Partially implemented.</dd>
<dt>*</dt>
<dd>Quanto forward compounded engines.</dd>
<dt>*</dt>
<dd>Integral (european) pricing engine.</dd></dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</dt>
<dd>ZeroCurve: a term structure based on linear interpolation of zero yields.</dd></dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>Up-front and in-arrear indexed coupon.</dd>
<dt>*</dt>
<dd>Specific implementation of compound forward rate from zero yield.</dd>
<dt>*</dt>
<dd>Added compound forward and zero coupon implementations.</dd>
<dt>*</dt>
<dd>Added Futures rate helper with specified maturity date.</dd>
<dt>*</dt>
<dd>Added bucketed bps calculation.</dd>
<dt>*</dt>
<dd>Added swap constructor using specified maturity date as well as added functionality in Scheduler.</dd>
<dt>*</dt>
<dd>Added date-bucketed basis point sensitivity based on 1st derivative of zero coupon rate.</dd></dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Solvers now take any function. ObjectiveFunction disappeared.</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>Abstracted lazy object.</dd>
<dt>*</dt>
<dd>Abstracted the curiously recurring template pattern.</dd></dl>
<p> DATE AND CALENDARS</p>
<dl>
<dt>*</dt>
<dd>Added joint calendars.</dd>
<dt>*</dt>
<dd>Tokyo, Stockholm, Johannesburg calendar improved.</dd>
<dt>*</dt>
<dd>
</dd><dt>*</dt>
<dd>Added basic date generation starting from the end.</dd></dl>
<p> MATH</p>
<dl>
<dt>*</dt>
<dd>Added Gauss-Kronrod integration algorithm.</dd>
<dt>*</dt>
<dd>Added primitive polynomial modulo 2 up to dimension 18 (available up to dimension 27.)</dd>
<dt>*</dt>
<dd>Added BicubicSplineInterpolation.</dd>
<dt>*</dt>
<dd>Numerical Recipes algorithm is back since there is a problem with Nicolas&#8217; code: it is unable to fit a straight line, it waves around the line.</dd>
<dt>*</dt>
<dd>Prime number generation.</dd>
<dt>*</dt>
<dd>Acklam&#8217;s approximation for inverse cumulative normal distribution function (replaced Moro&#8217;s algorithm as default.)</dd>
<dt>*</dt>
<dd>Added error function.</dd>
<dt>*</dt>
<dd>Improved Cumulative Normal Distribution function using the error function.</dd>
<dt>*</dt>
<dd>Matrix pseudo square algorithm using salvaging algorithm(s).</dd>
<dt>*</dt>
<dd>Added SequenceStatistics.</dd>
<dt>*</dt>
<dd>Major Statistic reworking.</dd>
<dt>*</dt>
<dd>Added DiscrepancyStatistic that inherits from SequenceStatistic and extends it with the calculation of L2-discrepancy.</dd>
<dt>*</dt>
<dd>HStatistics.</dd>
<dt>*</dt>
<dd>Added first and second derivative ot cubic splines.</dd></dl>
<p> RISK MEASURES</p>
<dl>
<dt>*</dt>
<dd>Introduced semiVariance and regret.</dd>
<dt>*</dt>
<dd>Redefinition of average shorfall (normalization factor now is cumulative(target) instead of 1.0)</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>QuEP 9 &#8216;generic disposable objects&#8217; implemented.</dd>
<dt>*</dt>
<dd>Added test suite.</dd>
<dt>*</dt>
<dd>Dataformatters extended to format long integers, Ordinal numerals, power of two formatting.</dd>
<dt>*</dt>
<dd>Exercise class adopted.</dd>
<dt>*</dt>
<dd>Added user configuration section.</dd>
<dt>*</dt>
<dd>Inhibited automatic conversion of <code>Handle&lt;T&gt;</code> to RelinkableHandle&lt;T&gt;.</dd>
<dt>*</dt>
<dd>Diffusion process extended.</dd>
<dt>*</dt>
<dd>Added strikeSensitivity to the Greeks.</dd>
<dt>*</dt>
<dd>BS does handle t==0.0 and sigma==0.0.</dd>
<dt>*</dt>
<dd>TimeGrid has been reworked.</dd>
<dt>*</dt>
<dd>Added payoff file for Payoff classes. Added Cash-Or-Nothing and Asset-Or-Nothing payoff classes.</dd>
<dt>*</dt>
<dd>Upgraded to use Doxygen 1.3.</dd></dl>
<p> <code>Release 0.3.1 &#8211; February 4th, 2003</code> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>partially implemented QuEP 2 (<a rel="nofollow" href="http://quantlib.org/quep.shtml)">http://quantlib.org/quep.shtml)</a></dd></dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>added Black and local volatility interface</dd></dl>
<p> PRICING ENGINES FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>partially implemented QuEP 5 (<a rel="nofollow" href="http://quantlib.org/quep.shtml)">http://quantlib.org/quep.shtml)</a></dd></dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</dt>
<dd>interface revisited</dd>
<dt>*</dt>
<dd>added discrete time forward methods</dd>
<dt>*</dt>
<dd>added DiscountCurve (loglinear interpolated) and CompoundForward term structures</dd>
<dt>*</dt>
<dd>ForwardSpreadedTermStructure moved under QuantLibTermStructures namespace</dd></dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>Modified coupons so that the payment date can be after the end of the accrual period</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>added/verified holidays of many calendars</dd>
<dt>*</dt>
<dd>added new calendars</dd>
<dt>*</dt>
<dd>added new currencies</dd>
<dt>*</dt>
<dd>more date formatters</dd>
<dt>*</dt>
<dd>added Period(std::string&amp;)</dd>
<dt>*</dt>
<dd>it is now possible to advance a calandar using a Period</dd>
<dt>*</dt>
<dd>added LogLinear Interpolation</dd>
<dt>*</dt>
<dd>the allowExtrapolation boolean in interpolation classes has been removed from constructors and added to the operator()</dd>
<dt>*</dt>
<dd>Renamed Solver1D::lowBound and hiBound</dd>
<dt>*</dt>
<dd>bug fixes</dd></dl>
<p> BUILD PROCESS</p>
<dl>
<dt>*</dt>
<dd>More autoconfiscated time functions and types</dd>
<dt>*</dt>
<dd>Migrated to latest autotools</dd>
<dt>*</dt>
<dd>added patches for Darwin and Solaris</dd></dl>
<p> <code>Release 0.3.0 &#8211; May 6th, 2002</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Path and MultiPath are time-aware</dd>
<dt>*</dt>
<dd>McPricer: extended interface, improved convergency algorithm</dd></dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>added mixed (implicit/explicit) scheme, from which Crank-Nicolson, ImplicitEuler, and ExplicitEuler are now derived</dd>
<dt>*</dt>
<dd>Finite Difference exercise conditions are now in the FiniteDifferences folder/namespace</dd>
<dt>*</dt>
<dd>Finite Difference pricers now start with &#8216;Fd&#8217; letters</dd>
<dt>*</dt>
<dd>BSMNumericalOption became BsmFdOption</dd></dl>
<p> LATTICE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>introduced first version of the framework</dd>
<dt>*</dt>
<dd>CRR and JR binomial trees</dd></dl>
<p> VOLATILITY FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>early works on reorganization of vol structures</dd></dl>
<p> YIELD TERM STRUCTURE</p>
<dl>
<dt>*</dt>
<dd>new TermStructure class based on affine model</dd>
<dt>*</dt>
<dd>yield curves can be spreaded in term of zeros (ZeroSpreadedTermStructure) and forwards (ForwardSpreadedTermStructure)</dd>
<dt>*</dt>
<dd>Added dates() and times() to PiecewiseFlatForward</dd>
<dt>*</dt>
<dd>discount factor accuracy in the yield curve bootstrapping is an input</dd>
<dt>*</dt>
<dd>added single factor short-rate models (Hull-White, Black-Karasinski)</dd>
<dt>*</dt>
<dd>added two factor short-rate models framework</dd>
<dt>*</dt>
<dd>cap/floor and swaption calibration helpers</dd>
<dt>*</dt>
<dd>added bermudan swaption pricing example (including BK and HW calibrations)</dd></dl>
<p> FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>cap/floor and swaption tree pricer</dd>
<dt>*</dt>
<dd>cap/floor analytical pricer</dd>
<dt>*</dt>
<dd>vanilla swaption Jamshidian pricer</dd>
<dt>*</dt>
<dd>Added accruedAmount() to coupons</dd>
<dt>*</dt>
<dd>Made cash flow vector builders into functions</dd></dl>
<p> OPTIMIZATION FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>added conjugate gradient, simplex</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>implemented QuEP 8 and 10</dd></dl>
<p> MISCELLANEA</p>
<dl>
<dt>*</dt>
<dd>added allowExtrapolation parameter to interpolaton classes</dd>
<dt>*</dt>
<dd>added 2D bilinear interpolation</dd>
<dt>*</dt>
<dd>better spline interpolation algorithm</dd>
<dt>*</dt>
<dd>Added non-central chi-square distribution function.</dd>
<dt>*</dt>
<dd>Improved Inverse Cumulative Normal Distribution using Moro&#8217;s algorithm</dd>
<dt>*</dt>
<dd>Introduced class representing stochastic processes</dd>
<dt>*</dt>
<dd>added isExpired() to Instrument interface</dd>
<dt>*</dt>
<dd>added functions folder and namespace for QuantLibXL and any other function-like interface to QuantLib</dd>
<dt>*</dt>
<dd>Handle is now castable to an Handle of a compatible type</dd>
<dt>*</dt>
<dd>added downsideVariance to the Statistics class</dd>
<dt>*</dt>
<dd>kustosis() and skewness() now handles the case of stddev == 0 and/or variance == 0</dd>
<dt>*</dt>
<dd>added Correlation Matrix to MultiVariateAccumulator</dd>
<dt>*</dt>
<dd>enforced MS VC compilation settings</dd>
<dt>*</dt>
<dd>added &#8216;-debug&#8217; to the QL_VERSION version string ifdef QL_DEBUG</dd>
<dt>*</dt>
<dd>
</dd><dt>*</dt>
<dd>fixed compilation with &#8216;g++ -pedantic&#8217;</dd>
<dt>*</dt>
<dd>Spread as market element</dd>
<dt>*</dt>
<dd>new calendars introduced</dd>
<dt>*</dt>
<dd>new Xibor Indexes introduced</dd>
<dt>*</dt>
<dd>Added optional day count to libor indexes</dd>
<dt>*</dt>
<dd>Shortened file names within 31 char limit to support HFS</dd></dl>
<p> <code>Release 0.2.1 &#8211; December 3rd, 2001</code> MONTE CARLO FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>Path and MultiPath are now classes on their own</dd>
<dt>*</dt>
<dd>PathPricer now handles both Path and MultiPath</dd>
<dt>*</dt>
<dd>MonteCarloModel now handles both single factor and multi factors simulations.</dd>
<dt>*</dt>
<dd>McPricer now handles both single factor and multi factors pricing. New pricing interface</dd>
<dt>*</dt>
<dd>antithetic variance-reduction technique made possible in Monte Carlo for both single factor and multi factors</dd>
<dt>*</dt>
<dd>Control Variate specific class removed: control variation technique is now handled by the general MC model</dd>
<dt>*</dt>
<dd>average price and average strike asian option refactored</dd>
<dt>*</dt>
<dd>Sample as a (value,weight) struct</dd>
<dt>*</dt>
<dd>random number generators moved under RandomNumbers folder and namespace</dd></dl>
<p> FINITE DIFFERENCE FRAMEWORK</p>
<dl>
<dt>*</dt>
<dd>BackwardEuler and ForwardEuler renamed ImplicitEuler and ExplicitEuler, respectively</dd>
<dt>*</dt>
<dd>refactoring of TridiagonalOperator and derived classes</dd></dl>
<p> YIELD TERM STRUCTURE AND FIXED INCOME</p>
<dl>
<dt>*</dt>
<dd>Added some useful methods to term structure classes</dd>
<dt>*</dt>
<dd>Allowed passing a quote to RateHelpers as double</dd>
<dt>*</dt>
<dd>added FuturesRateHelpers (no convexity adjustment yet)</dd>
<dt>*</dt>
<dd>PiecewiseFlatForward now observer of rates passed as MarketElements</dd>
<dt>*</dt>
<dd>Unified Date and Time interface in TermStructure</dd>
<dt>*</dt>
<dd>Added BPS to generic swap legs</dd>
<dt>*</dt>
<dd>added term_structure+swap example</dd>
<dt>*</dt>
<dd>Fixing days introduced for floating-coupon bond</dd></dl>
<p> PATTERNS</p>
<dl>
<dt>*</dt>
<dd>Added factory pattern</dd>
<dt>*</dt>
<dd>Calendar and DayCounter now use the Strategy pattern</dd></dl>
<p> VARIOUS</p>
<dl>
<dt>*</dt>
<dd>used do-while-false idiom in QL_REQUIRE-like macros</dd>
<dt>*</dt>
<dd>now using size_t where appropriate</dd>
<dt>*</dt>
<dd>dividendYield is now a Spread instead of a Rate (that is: cost of carry is allowed)</dd>
<dt>*</dt>
<dd>RelinkableHandle initialized with an optional Handle</dd>
<dt>*</dt>
<dd>Worked around VC++ problems in History constructor</dd>
<dt>*</dt>
<dd>added QL_VERSION and QL_HEX_VERSION</dd>
<dt>*</dt>
<dd>generic bug fixes</dd>
<dt>*</dt>
<dd>removed classes deprecated in 0.2.0</dd></dl>
<p> INSTALLATION FACILITIES</p>
<dl>
<dt>*</dt>
<dd>improved and smoother Win32 binary installer</dd></dl>
<p> DOCUMENTATION</p>
<dl>
<dt>*</dt>
<dd>general re-hauling</dd>
<dt>*</dt>
<dd>improved and extended Monte Carlo documentation</dd>
<dt>*</dt>
<dd>improved and extended examples</dd>
<dt>*</dt>
<dd>Upgraded to Doxygen 1.2.11.1</dd>
<dt>*</dt>
<dd>Added man pages for installed executables</dd>
<dt>*</dt>
<dd>added docs in Windows Help format</dd>
<dt>*</dt>
<dd>added info on &#8216;Win32 OnTheEdgeRelease&#8217; and &#8216;Win32 OnTheEdgeDebug&#8217; MS VC++ configurations</dd>
<dt>*</dt>
<dd>additional information on how to create a MS VC++ project based on QuantLib</dd></dl>
<p> <code>Release 0.2.0 &#8211; September 18th, 2001</code></p>
<dl>
<dt>*</dt>
<dd>Library:</dd>
<dt> *</dt>
<dd>source code moved under ql, better GNU standards</dd>
<dt> *</dt>
<dd>gcc build dir can now be separated from source tree</dd>
<dt> *</dt>
<dd>gcc 3.0.1 port</dd>
<dt> *</dt>
<dd>clean compilation (no warnings)</dd>
<dt> *</dt>
<dd>bootstrap script on cygwin</dd>
<dt> *</dt>
<dd>Fixed automatic choice of seed for random number generators</dd>
<dt> *</dt>
<dd>Actual/actual classes</dd>
<dt> *</dt>
<dd>extended platform support (see table in documentation)</dd>
<dt> *</dt>
<dd>antithetic variance-reduction technique made possible in Monte Carlo</dd>
<dt> *</dt>
<dd>added dividend-Rho greek</dd>
<dt> *</dt>
<dd>First implementation of segment integral (to be redesigned)</dd>
<dt> *</dt>
<dd>Knuth random generator</dd>
<dt> *</dt>
<dd>Cash flows, scheduler, and swap (both generic and simple) added</dd>
<dt> *</dt>
<dd>added ICGaussian random generator</dd>
<dt> *</dt>
<dd>generic bug fixes</dd></dl>
<dl>
<dt>*</dt>
<dd>Installation facilities:</dd>
<dt> *</dt>
<dd>improved and smoother Win32 binary installer</dd>
<dt> *</dt>
<dd>better distribution</dd>
<dt> *</dt>
<dd>debian packages available</dd></dl>
<dl>
<dt>*</dt>
<dd>Documentation:</dd>
<dt> *</dt>
<dd>general re-hauling</dd>
<dt> *</dt>
<dd>added examples of using QuantLib and of projects based on QL</dd></dl>
<p> <code>Release 0.1.9 &#8211; May 31st, 2001</code></p>
<dl>
<dt>*</dt>
<dd>Library:</dd>
<dt> *</dt>
<dd>Style guidelines introduced (see <a rel="nofollow" href="http://quantlib.org/style.shtml)">http://quantlib.org/style.shtml)</a> and partially enforced</dd>
<dt> *</dt>
<dd>full support for Microsoft Visual Studio</dd>
<dt> *</dt>
<dd>full support for Linux/gcc</dd>
<dt> *</dt>
<dd>momentarily broken support for Metrowerks CodeWarrior</dd>
<dt> *</dt>
<dd>autoconfiscation (with specialized config.*.hpp files for platforms without automake/autoconf support)</dd>
<dt> *</dt>
<dd>Include files moved under Include/ql folder and referenced as &#8216;ql/header.hpp&#8217;</dd>
<dt> *</dt>
<dd>Implemented expression templates techniques for array algebra optimization</dd>
<dt> *</dt>
<dd>Added custom iterators</dd>
<dt> *</dt>
<dd>Improved term structure</dd>
<dt> *</dt>
<dd>Added Asian, Bermudan, Shout, Cliquet, Himalaya, and Barrier options (all with greeks calculation, control variated where possible)</dd>
<dt> *</dt>
<dd>Added Helsinki and Wellington calendars</dd>
<dt> *</dt>
<dd>Improved Normal distribution related functions: cumulative, inverse cumulative, etc.</dd>
<dt> *</dt>
<dd>Added uniform and Gaussian random number generators</dd>
<dt> *</dt>
<dd>Added Statistics class (mean, variance, skewness, downside variance, etc.)</dd>
<dt> *</dt>
<dd>Added RiskMeasures class: VAR, average shortfall, expected shortfall, etc.</dd>
<dt> *</dt>
<dd>Added RiskStatistics class combining Statistics and RiskMeasures</dd>
<dt> *</dt>
<dd>Added sample accumulator for multivariate analysis</dd>
<dt> *</dt>
<dd>Added Monte Carlo tools</dd>
<dt> *</dt>
<dd>Added matrix-related functions (square root, symmetric Schur decomposition)</dd>
<dt> *</dt>
<dd>Added interpolation framework (linear and cubic spline interpolation implemented).</dd></dl>
<dl>
<dt>*</dt>
<dd>Installation facilities:</dd>
<dt> *</dt>
<dd>Added Win32 GUI installer for binaries</dd></dl>
<dl>
<dt>*</dt>
<dd>Documentation:</dd>
<dt> *</dt>
<dd>support for Doxygen 1.2.7</dd>
<dt> *</dt>
<dd>Added man documentation</dd></dl>
<p> <code>Release 0.1.1 &#8211; November 21st, 2000</code> Initial release. </p>
