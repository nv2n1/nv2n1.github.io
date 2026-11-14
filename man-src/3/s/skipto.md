---
title: "skipto(3)"
name: "skipto"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipto/"
description: "QuantLib::SobolRsg – Sobol low-discrepancy sequence generator."
---

<p>QuantLib::SobolRsg &#8211; Sobol low-discrepancy sequence generator. </p>
<h2>Synopsis</h2>
<p> #include &lt;ql/math/randomnumbers/sobolrsg.hpp&gt; </p>
<h3>Public Types</h3>
<p> enum <code>DirectionIntegers</code> { <code>Unit</code>, <code>Jaeckel</code>, <code>SobolLevitan</code>, <code>SobolLevitanLemieux</code>, <code>JoeKuoD5</code>, <code>JoeKuoD6</code>, <code>JoeKuoD7</code>, <code>Kuo</code>, <code>Kuo2</code>, <code>Kuo3</code> } </p>
<p> typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>SobolRsg</code> (Size dimensionality, unsigned long seed=0, DirectionIntegers directionIntegers=Jaeckel) </p>
<p> void <code>skipTo</code> (unsigned long n) </p>
<p> const std::vector&lt; unsigned long &gt; &amp; <code>nextInt32Sequence</code> () const </p>
<p> const <code>SobolRsg::sample_type</code> &amp; <code>nextSequence</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<p> Sobol low-discrepancy sequence generator. </p>
<p> A Gray code counter and bitwise operations are used for very fast sequence generation. </p>
<p> The implementation relies on primitive polynomials modulo two from the book &#8216;Monte Carlo Methods in Finance&#8217; by Peter J�ckel. </p>
<p> 21 200 primitive polynomials modulo two are provided in QuantLib. J�ckel has calculated 8 129 334 polynomials: if you need that many dimensions you can replace the primitivepolynomials.c file included in QuantLib with the one provided in the CD of the &#8216;Monte Carlo Methods in Finance&#8217; book. </p>
<p> The choice of initialization numbers (also know as free direction integers) is crucial for the homogeneity properties of the sequence. Sobol defines two homogeneity properties: Property A and Property A&#8217;. </p>
<p> The unit initialization numbers suggested in &#8216;Numerical Recipes in C&#8217;, 2nd edition, by Press, Teukolsky, Vetterling, and Flannery (section 7.7) fail the test for Property A even for low dimensions. </p>
<p> Bratley and Fox published coefficients of the free direction integers up to dimension 40, crediting unpublished work of Sobol&#8217; and Levitan. See Bratley, P., Fox, B.L. (1988) &#8216;Algorithm 659: Implementing Sobol&#8217;s quasirandom sequence generator,&#8217; ACM Transactions on Mathematical Software 14:88-100. These values satisfy Property A for d&lt;=20 and d = 23, 31, 33, 34, 37; Property A&#8217; holds for d&lt;=6. </p>
<p> J�ckel provides in his book (section 8.3) initialization numbers up to dimension 32. Coefficients for d&lt;=8 are the same as in Bradley-Fox, so Property A&#8217; holds for d&lt;=6 but Property A holds for d&lt;=32. </p>
<p> The implementation of Lemieux, Cieslak, and Luttmer includes coefficients of the free direction integers up to dimension 360. Coefficients for d&lt;=40 are the same as in Bradley-Fox. For dimension 40&lt;d&lt;=360 the coefficients have been calculated as optimal values based on the &#8216;resolution&#8217; criterion. See &#8216;RandQMC user&#8217;s guide &#8211; A package for randomized quasi-Monte Carlo methods in C,&#8217; by C. Lemieux, M. Cieslak, and K. Luttmer, version January 13 2004, and references cited there (<a rel="nofollow" href="http://www.math.ucalgary.ca/~lemieux/randqmc.html">http://www.math.ucalgary.ca/~lemieux/randqmc.html</a>). The values up to d&lt;=360 has been provided to the QuantLib team by Christiane Lemieux, private communication, September 2004. </p>
<p> For more info on Sobol&#8217; sequences see also &#8216;Monte Carlo Methods in Financial Engineering,&#8217; by P. Glasserman, 2004, Springer, section 5.2.3 </p>
<p> The Joe&#8211;Kuo numbers and the Kuo numbers are due to Stephen Joe and Frances Kuo. </p>
<p> S. Joe and F. Y. Kuo, Constructing Sobol sequences with better two-dimensional projections, preprint Nov 22 2007 </p>
<p> See <a rel="nofollow" href="http://web.maths.unsw.edu.au/~fkuo/sobol/">http://web.maths.unsw.edu.au/~fkuo/sobol/</a> for more information. </p>
<p> Note that the Kuo numbers were generated to work with a different ordering of primitive polynomials for the first 40 or so dimensions which is why we have the Alternative Primitive Polynomials. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt>*</p>
<dd> the correctness of the returned values is tested by reproducing known good values.</p>
<dt>*</p>
<dd> the correctness of the returned values is tested by checking their discrepancy against known good values.</dl>
</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>SobolRsg</code> (Size dimensionality, unsigned long seed = 0, DirectionIntegers directionIntegers = Jaeckel)</h3>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dt>
<dd> dimensionality must be &lt;= PPMT_MAX_DIM</dl>
<h2>Member Function Documentation</h2>
<h3>void skipTo (unsigned long n)</h3>
<p> skip to the n-th sample in the low-discrepancy sequence </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code.</p>
