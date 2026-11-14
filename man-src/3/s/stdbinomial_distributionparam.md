---
title: "stdbinomial_distributionparam(3)"
name: "stdbinomial_distributionparam"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinomial_distributionparam/"
description: "std::binomial_distribution<IntType>::param – std::binomial_distribution<IntType>::param"
---

<p>std::binomial_distribution&lt;IntType&gt;::param &#8211; std::binomial_distribution&lt;IntType&gt;::param</p>
<h2>Synopsis</h2>
<p>param_type param() const; <code>(1)</code> <i>(since C++11)</i><br />
void param( const param_type&amp; params ); <code>(2)</code> <i>(since C++11)</i><br />
Manages the associated distribution parameter set.<br />
1) Returns the associated parameter set.<br />
2) Sets the associated parameter set to params </p>
<h2>Parameters</h2>
<p>params &#8211; new contents of the associated parameter set</p>
<h2>Return value</h2>
<p>1) The associated parameter set<br />
2) <i>(none)</i> </p>
<h2>Complexity</h2>
<p>Constant.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;random&gt;
int main()

{
    std::random_device rd;
    std::mt19937 gen(rd());
    using BinomialDist = std::binomial_distribution&lt;&gt;;
    BinomialDist bino_dis(1, 0.5);
    std::cout &lt;&lt; &quot;A sample of Binomial(  1, 0.5): &quot; &lt;&lt; bino_dis(gen) &lt;&lt; '
';
    // Use another parameter set
    bino_dis.param(BinomialDist::param_type(100, 0.9));
    std::cout &lt;&lt; &quot;A sample of Binomial(100, 0.9): &quot; &lt;&lt; bino_dis(gen) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;A sample of Binomial( 1, 0.5): 0<br />
&nbsp;<wbr>&nbsp;A sample of Binomial(100, 0.9): 94</p>
