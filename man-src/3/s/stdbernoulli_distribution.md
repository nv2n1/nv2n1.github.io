---
title: "stdbernoulli_distribution(3)"
name: "stdbernoulli_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbernoulli_distribution/"
---

std::bernoulli_distribution - std::bernoulli_distribution

<h2>Synopsis</h2>

Defined in header &lt;random&gt; 
class bernoulli_distribution; <i>(since C++11)</i> 
Produces random boolean values, according to the discrete probability function. The probability of true is <pre><code>P(b|p) =⎧
⎨
⎩p if b == true
1 − p if b == false</code></pre> 
std::bernoulli_distribution satisfies RandomNumberDistribution 

<h2>Member types</h2>

Member type Definition 
result_type bool 
param_type the type of the parameter set, see RandomNumberDistribution.

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new distribution 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resets the internal state of the distribution 
reset <i>(public member function)</i>

<h2>Generation</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next random number in the distribution 
operator() <i>(public member function)</i>

<h2>Characteristics</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the p distribution parameter (probability of generating true) 
p <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object 
param <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the minimum potentially generated value 
min <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the maximum potentially generated value 
max <i>(public member function)</i>

<h2>Non-member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two distribution objects 
operator== <i>(function)</i> 
operator!= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs stream input and output on pseudo-random number distribution 
operator&lt;&lt; <i>(function template)</i> 
operator&gt;&gt;

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;string&gt;

#include &lt;map&gt;

#include &lt;random&gt;
int main()

{
    std::random_device rd;
    std::mt19937 gen(rd());
    // give &quot;true&quot; 1/4 of the time
    // give &quot;false&quot; 3/4 of the time
    std::bernoulli_distribution d(0.25);
    std::map&lt;bool, int&gt; hist;
    for (int n = 0; n &lt; 10000; ++n) {
        ++hist[d(gen)];
    }
    for (auto p : hist) {
        std::cout &lt;&lt; std::boolalpha &lt;&lt; std::setw(5) &lt;&lt; p.first
                  &lt;&lt; ' ' &lt;&lt; std::string(p.second / 500, '*') &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;false *************** 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;true ****

<h2>External links</h2>

Weisstein,_Eric_W._&quot;Bernoulli_Distribution.&quot; From MathWorld--A Wolfram Web Resource.
