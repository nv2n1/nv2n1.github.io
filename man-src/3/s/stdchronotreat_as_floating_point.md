---
title: "stdchronotreat_as_floating_point(3)"
name: "stdchronotreat_as_floating_point"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotreat_as_floating_point/"
---

std::chrono::treat_as_floating_point - std::chrono::treat_as_floating_point

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    template &lt;class Rep&gt;
    (since C++ 11)

        struct treat_as_floating_point : std::is_floating_point&lt;Rep&gt; {
};</code></pre> 
The std::chrono::treat_as_floating_point trait helps determine if a duration can be converted to another duration with a different tick period. 
Implicit conversions between two durations normally depends on the tick period of the durations. However, implicit conversions can happen regardless of tick period if std::chrono::treat_as_floating_point&lt;Rep&gt;::value == true. 
Helper variable template template&lt; class Rep &gt;                                                                   (since C++17)

inline constexpr bool treat_as_floating_point_v = treat_as_floating_point&lt;Rep&gt;::value;



<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;
void timed_piece_of_code()

{
    std::chrono::milliseconds simulated_work(2);
    std::this_thread::sleep_for(simulated_work);
}
int main()

{
    auto start = std::chrono::high_resolution_clock::now();
    std::cout &lt;&lt; &quot;Running some timed piece of code...&quot; &lt;&lt; '\n';
    timed_piece_of_code();
    auto stop = std::chrono::high_resolution_clock::now();
    // A floating point milliseconds type
    using FpMilliseconds =
        std::chrono::duration&lt;float, std::chrono::milliseconds::period&gt;;
    static_assert(std::chrono::treat_as_floating_point&lt;FpMilliseconds::rep&gt;::value,
                  &quot;Rep required to be floating point&quot;);
    // Note that implicit conversion is not allowed here
    auto i_ms = std::chrono::duration_cast&lt;std::chrono::milliseconds&gt;(stop - start);
    // Note that implicit conversion is allowed here
    auto f_ms = FpMilliseconds(stop - start);
    std::cout &lt;&lt; &quot;Time in milliseconds, using default rep: &quot;
              &lt;&lt; i_ms.count() &lt;&lt; '\n';

    std::cout &lt;&lt; &quot;Time in milliseconds, using floating point rep: &quot;
              &lt;&lt; f_ms.count() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Running some timed piece of code... 
&nbsp;<wbr>&nbsp;Timing stats: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Time in milliseconds, using default rep: 2 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Time in milliseconds, using floating point rep: 2.57307

<h2>See also</h2>


