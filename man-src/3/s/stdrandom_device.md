---
title: "stdrandom_device(3)"
name: "stdrandom_device"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrandom_device/"
description: "std::random_device – std::random_device"
---

<p>std::random_device &#8211; std::random_device</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;random&gt;<br />
class random_device; <i>(since C++11)</i><br />
std::random_device is a uniformly-distributed integer random number generator that produces non-deterministic random numbers.<br />
std::random_device may be implemented in terms of an implementation-defined pseudo-random number engine if a non-deterministic source (e.g. a hardware device) is not available to the implementation. In this case each std::random_device object may generate the same number sequence. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
result_type unsigned int</p>
<h2>Member functions</h2>
<h2>Construction</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the engine<br />
constructor <i>(public member function)</i> </p>
<p>operator= the assignment operator is deleted<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
(deleted)</p>
<h2>Generation</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances the engine&#8217;s state and returns the generated value<br />
operator() <i>(public member function)</i></p>
<h2>Characteristics</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the entropy estimate for the non-deterministic random number generator<br />
entropy <i>(public member function)</i> </p>
<p>min gets the smallest possible value in the output range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>max gets the largest possible value in the output range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Notes</h2>
<p>A notable implementation where std::random_device is deterministic is MinGW (bug_338), although replacement implementations exist, such as mingw-std-random_device. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;map&gt;

#include &lt;random&gt;
int main()

{
    std::random_device rd;
    std::map&lt;int, int&gt; hist;
    std::uniform_int_distribution&lt;int&gt; dist(0, 9);
    for (int n = 0; n &lt; 20000; ++n) {
        ++hist[dist(rd)]; // note: demo only: the performance of many
                          // implementations of random_device degrades sharply
                          // once the entropy pool is exhausted. For practical use
                          // random_device is generally only used to seed
                          // a PRNG such as mt19937
    }
    for (auto p : hist) {
        std::cout &lt;&lt; p.first &lt;&lt; &quot; : &quot; &lt;&lt; std::string(p.second / 100, '*') &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;0 : ********************<br />
&nbsp;<wbr>&nbsp;1 : *******************<br />
&nbsp;<wbr>&nbsp;2 : ********************<br />
&nbsp;<wbr>&nbsp;3 : ********************<br />
&nbsp;<wbr>&nbsp;4 : ********************<br />
&nbsp;<wbr>&nbsp;5 : *******************<br />
&nbsp;<wbr>&nbsp;6 : ********************<br />
&nbsp;<wbr>&nbsp;7 : ********************<br />
&nbsp;<wbr>&nbsp;8 : *******************<br />
&nbsp;<wbr>&nbsp;9 : ********************</p>
