---
title: "stddiscrete_distributiondiscrete_distribution(3)"
name: "stddiscrete_distributiondiscrete_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddiscrete_distributiondiscrete_distribution/"
description: "std::discrete_distribution<IntType>::discrete_distribution – std::discrete_distribution<IntType>::discrete_distribution"
---

<p>std::discrete_distribution&lt;IntType&gt;::discrete_distribution &#8211; std::discrete_distribution&lt;IntType&gt;::discrete_distribution</p>
<h2>Synopsis</h2>
<p>discrete_distribution(); <code>(1)</code> <i>(since C++11)</i><br />
template&lt; class InputIt &gt; <code>(2)</code> <i>(since C++11)</i><br />
discrete_distribution( InputIt first, InputIt last );<br />
discrete_distribution( std::initializer_list&lt;double&gt; weights ); <code>(3)</code> <i>(since C++11)</i><br />
template&lt; class UnaryOperation &gt;<br />
discrete_distribution( std::size_t count, double xmin, double xmax, <code>(4)</code> <i>(since C++11)</i><br />
UnaryOperation unary_op );<br />
explicit discrete_distribution( const param_type&amp; params ); <code>(5)</code> <i>(since C++11)</i> </p>
<pre><code>Constructs a new distribution object.

1) Default constructor. Constructs the distribution with a single weight p={1}. This distribution will always generate 0.

2) Constructs the distribution with weights in the range [first, last). If first == last, the effects are the same as of the default constructor.

3) Constructs the distribution with weights in weights. Effectively calls discrete_distribution(weights.begin(), weights.end()).

4) Constructs the distribution with count weights that are generated using function unary_op. Each of the weights is equal to w

i = unary_op(xmin + δ/2 + i · δ), where δ =</code></pre>
<p>(xmax − xmin)<br />
count<br />
and i ∈ {0, &#8230;, count−1}. xmin and xmax must be such that δ &gt; 0. If count == 0 the effects are the same as of the default constructor.<br />
5) Constructs the distribution with params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements defining the numbers to use as weights. The type of the elements referred by InputIterator must be convertible to double<br />
weights &#8211; initializer list containing the weights<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary operation function object that will be applied.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following:<br />
unary_op &#8211; Ret fun(const Type &amp;a);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type must be such that an object of type double can be dereferenced and then implicitly converted to Type. The type Ret must be such that an object of type double can be dereferenced and assigned a value of type Ret.<br />
params &#8211; the distribution parameter set</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.</p>
