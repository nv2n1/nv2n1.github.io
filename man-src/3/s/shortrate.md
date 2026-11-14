---
title: "shortrate(3)"
name: "shortrate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shortrate/"
description: "Short-rate modelling framework –"
---

<p>Short-rate modelling framework &#8211;</p>
<h3>Classes</h3>
<p>class <code>AffineModel</code><br />
 <i>Affine model class. </i><br />
 class <code>TermStructureConsistentModel</code><br />
 <i>Term-structure consistent model class. </i><br />
 class <code>ShortRateModel</code><br />
 <i>Abstract short-rate model class. </i><br />
 class <code>OneFactorModel</code><br />
 <i>Single-factor short-rate model abstract class. </i><br />
 class <code>OneFactorAffineModel</code><br />
 <i>Single-factor affine base class. </i><br />
 class <code>BlackKarasinski</code><br />
 <i>Standard Black-Karasinski model class. </i><br />
 class <code>CoxIngersollRoss</code><br />
 <i>Cox-Ingersoll-Ross model class. </i><br />
 class <code>ExtendedCoxIngersollRoss</code><br />
 <i>Extended Cox-Ingersoll-Ross model class. </i><br />
 class <code>HullWhite</code><br />
 <i>Single-factor Hull-White (extended Vasicek) model class. </i><br />
 class <code>Vasicek</code><br />
 <i>Vasicek model class </i><br />
 class <code>TwoFactorModel</code><br />
 <i>Abstract base-class for two-factor models. </i><br />
 class <code>G2</code><br />
 <i>Two-additive-factor gaussian model class. </i></p>
<h2>Detailed Description</h2>
<p>This framework (corresponding to the ql/ShortRateModels directory) implements some single-factor and two-factor short rate models. The models implemented in this library are widely used by practitionners. For the moment, the ShortRateModels::Model class defines the short-rate dynamics with stochastic equations of the type [ dx_i = mu(t,x_i) dt + igma(t,x_i) dW_t ] where $ r = f(t,x) $. If the model is affine (i.e. derived from the <code>QuantLib::AffineModel</code> class), analytical formulas for discount bonds and discount bond options are given (useful for calibration).</p>
<h2>Single-factor models</h2>
<p><code>The Hull &amp; White model</code>.RS 4 [ dr_t = ( heta(t) &#8211; lpha(t) r_t)dt + igma(t) dW_t ] When $ lpha $ and $ igma $ are constants, this model has analytical formulas for discount bonds and discount bond options. </p>
<p> <code>The Black-Karasinski model</code>.RS 4 [ d</p>
<hr>
<p>ded Cox-Ingersoll-Ross model.RS 4 [ dr_t = ( heta(t) &#8211; k r_t)dt + igma qrt{r_t} dW_t ] There are analytical formulas for discount bonds (and soon for discount bond options).</p>
<h2>Calibration</h2>
<p>The class CalibrationHelper is a base class that facilitates the instanciation of market instruments used for calibration. It has a method marketValue() that gives the market price using a Black formula, and a modelValue() method that gives the price according to a model </p>
<p> Derived classed are <code>QuantLib::CapHelper</code> and <code>QuantLib::SwaptionHelper</code>. </p>
<p> For the calibration itself, you must choose an optimization method that will find constant parameters such that the value: [ V = qrt{um_{i=1}^{n} ac{(T_i &#8211; M_i)^2}{M_i}}, ] where $ T_i $ is the price given by the model and $ M_i $ is the market price, is minimized. A few optimization methods are available in the ql/Optimization directory.</p>
<h2>Two-factor models</h2>
<h2>Pricers</h2>
<p><code>Analytical pricers</code>.RS 4 </p>
<p> If the model is affine, i.e. discount bond options formulas exist, caps are easily priced since they are a portfolio of discount bond options. Such a pricer is implemented in QuantLib::AnalyticalCapFloor. In the case of single-factor affine models, swaptions can be priced using the Jamshidian decomposition, implemented in QuantLib::JamshidianSwaption. </p>
<p> <code>Using Finite Differences</code>.RS 4 </p>
<p> (Doesn&#8217;t work for the moment) For the moment, this is only available for single-factor affine models. If $ x = x(t, r) $ is the state variable and follows this stochastic process: [ dx_t = mu(t,x)dt + igma(t,x)dW_t ] any european-style instrument will follow the following PDE: </p>
<p> [ ac{<br />
 artial P}{<br />
 artial t} + mu ac{<br />
 artial P}{<br />
 artial x} + ac{1}{2} igma^2 ac{<br />
 artial^2 P}{<br />
 artial x^2} = r(t,x)P ].PP The adequate operator to feed a Finite Difference Model instance is defined in the QuantLib::OneFactorOperator class. </p>
<p> <code>Using Trees</code>.RS 4 </p>
<p> Each model derived from the single-factor model class has the ability to return a trinomial tree. For yield-curve consistent models, the fitting parameter can be determined either analytically (when possible) or numerically. When a tree is built, it is then pretty straightforward to implement a pricer for any path-independant derivative. Just implement a class derived from NumericalDerivative (see QuantLib::NumericalSwaption for example) and roll it back until the present time&#8230; Just look at QuantLib::TreeCapFloor and QuantLib::TreeSwaption for working pricers.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
