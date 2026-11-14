---
title: "lattices(3)"
name: "lattices"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lattices/"
description: "Lattice methods –"
---

<h2 class="name">NAME</h2>
<p> Lattice methods &#8211; </p>
<h3>Classes</h3>
<p> class <code>ExtendedBinomialTree&lt; T &gt;</code><br />
 <i>Binomial tree base class. </i><br />
 class <code>ExtendedEqualProbabilitiesBinomialTree&lt; T &gt;</code><br />
 <i>Base class for equal probabilities binomial tree. </i><br />
 class <code>ExtendedEqualJumpsBinomialTree&lt; T &gt;</code><br />
 <i>Base class for equal jumps binomial tree. </i><br />
 class <code>ExtendedJarrowRudd</code><br />
 <i>Jarrow-Rudd (multiplicative) equal probabilities binomial tree. </i><br />
 class <code>ExtendedCoxRossRubinstein</code><br />
 <i>Cox-Ross-Rubinstein (multiplicative) equal jumps binomial tree. </i><br />
 class <code>ExtendedAdditiveEQPBinomialTree</code><br />
 <i>Additive equal probabilities binomial tree. </i><br />
 class <code>ExtendedTrigeorgis</code><br />
 <i>Trigeorgis (additive equal jumps) binomial tree </i><br />
 class <code>ExtendedTian</code><br />
 <i>Tian tree: third moment matching, multiplicative approach </i><br />
 class <code>ExtendedLeisenReimer</code><br />
 <i>Leisen &amp; Reimer tree: multiplicative approach. </i><br />
 class <code>BinomialTree&lt; T &gt;</code><br />
 <i>Binomial tree base class. </i><br />
 class <code>EqualProbabilitiesBinomialTree&lt; T &gt;</code><br />
 <i>Base class for equal probabilities binomial tree. </i><br />
 class <code>EqualJumpsBinomialTree&lt; T &gt;</code><br />
 <i>Base class for equal jumps binomial tree. </i><br />
 class <code>JarrowRudd</code><br />
 <i>Jarrow-Rudd (multiplicative) equal probabilities binomial tree. </i><br />
 class <code>CoxRossRubinstein</code><br />
 <i>Cox-Ross-Rubinstein (multiplicative) equal jumps binomial tree. </i><br />
 class <code>AdditiveEQPBinomialTree</code><br />
 <i>Additive equal probabilities binomial tree. </i><br />
 class <code>Trigeorgis</code><br />
 <i>Trigeorgis (additive equal jumps) binomial tree </i><br />
 class <code>Tian</code><br />
 <i>Tian tree: third moment matching, multiplicative approach </i><br />
 class <code>LeisenReimer</code><br />
 <i>Leisen &amp; Reimer tree: multiplicative approach. </i><br />
 class <code>BlackScholesLattice&lt; T &gt;</code><br />
 <i>Simple binomial lattice approximating the Black-Scholes model. </i><br />
 class <code>TreeLattice&lt; Impl &gt;</code><br />
 <i>Tree-based lattice-method base class. </i><br />
 class <code>TreeLattice1D&lt; Impl &gt;</code><br />
 <i>One-dimensional tree-based lattice. </i><br />
 class <code>TreeLattice2D&lt; Impl, T &gt;</code><br />
 <i>Two-dimensional tree-based lattice. </i><br />
 class <code>TsiveriotisFernandesLattice&lt; T &gt;</code><br />
 <i>Binomial lattice approximating the Tsiveriotis-Fernandes model. </i><br />
 class <code>Tree&lt; T &gt;</code><br />
 <i>Tree approximating a single-factor diffusion </i><br />
 class <code>TrinomialTree</code><br />
 <i>Recombining trinomial tree class. </i></p>
<h2>Detailed Description</h2>
<p> The framework (corresponding to the ql/Lattices directory) contains basic building blocks for pricing instruments using lattice methods (trees). A lattice, i.e. an instance of the abstract class <code>QuantLib::Lattice</code>, relies on one or several trees (each one approximating a diffusion process) to price an instance of the DiscretizedAsset class. Trees are instances of classes derived from <code>QuantLib::Tree</code>, classes which define the branching between nodes and transition probabilities.</p>
<h2>Binomial trees</h2>
<p> The binomial method is the simplest numerical method that can be used to price path-independent derivatives. It is usually the preferred lattice method under the Black-Scholes-Merton model. As an example, let&#8217;s see the framework implemented in the <code>bsmlattice.hpp</code> file. It is a method based on a binomial tree, with constant short-rate (discounting). There are several approaches to build the underlying binomial tree, like Jarrow-Rudd or Cox-Ross-Rubinstein.</p>
<h2>Trinomial trees</h2>
<p> When the underlying stochastic process has a mean-reverting pattern, it is usually better to use a trinomial tree instead of a binomial tree. An example is implemented in the <code>QuantLib::TrinomialTree</code> class, which is constructed using a diffusion process and a time-grid. The goal is to build a recombining trinomial tree that will discretize, at a finite set of times, the possible evolutions of a random variable $ y $ satisfying [ dy_t = mu(t, y_t) dt + igma(t, y_t) dW_t. ] At each node, there is a probability $ p_u, p_m $ and $ p_d $ to go through respectively the upper, the middle and the lower branch. These probabilities must satisfy [ p_{u}y_{i+1,k+1}+p_{m}y_{i+1,k}+p_{d}y_{i+1,k-1}=E_{i,j} ] and [ p_u y_{i+1,k+1}^2 + p_m y_{i+1,k}^2 + p_d y_{i+1,k-1}^2 = V^2_{i,j}+E_{i,j}^2, ] where k (the index of the node at the end of the middle branch) is the index of the node which is the nearest to the expected future value, $ E_{i,j}=mathbf{E}</p>
<hr>
<p> suppose that the variance is only dependant on time $ V_{i,j}=V_{i} $ and set $ y_{i+1} $ to $ V_{i}qrt{3} $, we find that [ p_{u} = ac{1}{6}+ac{(E_{i,j}-y_{i+1,k})^{2}}{6V_{i}^{2}} + ac{E_{i,j}-y_{i+1,k}}{2qrt{3}V_{i}}, ] [ p_{m} = ac{2}{3}-ac{(E_{i,j}-y_{i+1,k})^{2}}{3V_{i}^{2}}, ] [ p_{d} = ac{1}{6}+ac{(E_{i,j}-y_{i+1,k})^{2}}{6V_{i}^{2}} &#8211; ac{E_{i,j}-y_{i+1,k}}{2qrt{3}V_{i}}. ]</p>
<h2>Bidimensional lattices</h2>
<p> To come&#8230;</p>
<h2>The QuantLib::DiscretizedAsset class</h2>
<p> This class is a representation of the price of a derivative at a specific time. It is roughly an array of values, each value being associated to a state of the underlying stochastic variables. For the moment, it is only used when working with trees, but it should be quite easy to make a use of it in finite-differences methods. The two main points, when deriving classes from <code>QuantLib::DiscretizedAsset</code>, are:</p>
<dl>
<dt>1.</p>
<dd> Define the initialisation procedure (e.g. terminal payoff for european stock options).</p>
<dt>2.</p>
<dd> Define the method adjusting values, when necessary, at each time steps (e.g. apply the step condition for american or bermudan options). Some examples are found in QuantLib::DiscretizedSwap and QuantLib::DiscretizedSwaption.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
