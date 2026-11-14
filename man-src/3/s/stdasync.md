---
title: "stdasync(3)"
name: "stdasync"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasync/"
description: "std::async – std::async"
---

<p>std::async &#8211; std::async</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;future&gt;

template&lt; class Function, class... Args&gt;                                             (since C++11)

std::future&lt;std::result_of_t&lt;std::decay_t&lt;Function&gt;(std::decay_t&lt;Args&gt;...)&gt;&gt;         (until C++17)

async( Function&amp;&amp; f, Args&amp;&amp;... args );

template&lt; class Function, class... Args&gt;

std::future&lt;std::invoke_result_t&lt;std::decay_t&lt;Function&gt;,                             (since C++17)

std::decay_t&lt;Args&gt;...&gt;&gt;                                                              (until C++20)

async( Function&amp;&amp; f, Args&amp;&amp;... args );

template&lt; class Function, class... Args&gt;

[[nodiscard]]

std::future&lt;std::invoke_result_t&lt;std::decay_t&lt;Function&gt;,                             (since C++20)

std::decay_t&lt;Args&gt;...&gt;&gt;

async( Function&amp;&amp; f, Args&amp;&amp;... args );                                       (1)

template&lt; class Function, class... Args &gt;                                                           (since C++11)

std::future&lt;std::result_of_t&lt;std::decay_t&lt;Function&gt;(std::decay_t&lt;Args&gt;...)&gt;&gt;                        (until C++17)

async( std::launch policy, Function&amp;&amp; f, Args&amp;&amp;... args );

template&lt; class Function, class... Args &gt;

std::future&lt;std::invoke_result_t&lt;std::decay_t&lt;Function&gt;,                                            (since C++17)

std::decay_t&lt;Args&gt;...&gt;&gt;                                                          (2)                (until C++20)

async( std::launch policy, Function&amp;&amp; f, Args&amp;&amp;... args );

template&lt; class Function, class... Args &gt;

[[nodiscard]]

std::future&lt;std::invoke_result_t&lt;std::decay_t&lt;Function&gt;,                                            (since C++20)

std::decay_t&lt;Args&gt;...&gt;&gt;

async( std::launch policy, Function&amp;&amp; f, Args&amp;&amp;... args );</code></pre>
<p>The template function async runs the function f asynchronously (potentially in a separate thread which may be part of a thread pool) and returns a std::future that will eventually hold the result of that function call.<br />
1) Behaves as if <code>(2)</code> is called with policy being std::launch::async | std::launch::deferred. In other words, f may be executed in another thread or it may be run synchronously when the resulting std::future is queried for a value.<br />
2) Calls a function f with arguments args according to a specific launch policy policy:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If the async flag is set (i.e. (policy &amp; std::launch::async) != 0), then async executes the callable object f on a new thread of execution (with all thread-locals initialized) as if spawned by std::thread(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)&#8230;), except that if the function f returns a value or throws an exception, it is stored in the shared state accessible through the std::future that async returns to the caller.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If the deferred flag is set (i.e. (policy &amp; std::launch::deferred) != 0), then async converts f and args&#8230; the same way as by std::thread constructor, but does not spawn a new thread of execution. Instead, lazy evaluation is performed: the first call to a non-timed wait function on the std::future that async returned to the caller will cause the copy of f to be invoked (as an rvalue) with the copies of args&#8230; (also passed as rvalues) in the current thread (which does not have to be the thread that originally called std::async). The result or exception is placed in the shared state associated with the future and only then it is made ready. All further accesses to the same std::future will return the result immediately.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If both the std::launch::async and std::launch::deferred flags are set in policy, it is up to the implementation whether to perform asynchronous execution or lazy evaluation.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If neither std::launch::async nor std::launch::deferred, nor any implementation-defined policy flag is set in policy, the behavior is undefined. <i>(since C++14)</i><br />
In any case, the call to std::async synchronizes-with (as defined in std::memory_order) the call to f, and the completion of f is sequenced-before making the shared state ready. If the async policy is chosen, the associated thread completion synchronizes-with the successful return from the first function that is waiting on the shared state, or with the return of the last function that releases the shared state, whichever comes first. </p>
<h2>Parameters</h2>
<p>f &#8211; Callable object to call<br />
args&#8230; &#8211; parameters to pass to f<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bitmask value, where individual bits control the allowed methods of execution </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bit Explanation<br />
policy &#8211; std::launch::async enable asynchronous evaluation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::launch::deferred enable lazy evaluation</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
Function, Args must meet the requirements of MoveConstructible.</p>
<h2>Return value</h2>
<p>std::future referring to the shared state created by this call to std::async. </p>
<h2>Exceptions</h2>
<p>Throws std::system_error with error condition std::errc::resource_unavailable_try_again if the launch policy equals std::launch::async and the implementation is unable to start a new thread (if the policy is async|deferred or has additional bits set, it will fall back to deferred or the implementation-defined policies in this case), or std::bad_alloc if memory for the internal data structures could not be allocated.</p>
<h2>Notes</h2>
<p>The implementation may extend the behavior of the first overload of std::async by enabling additional (implementation-defined) bits in the default launch policy.<br />
Examples of implementation-defined launch policies are the sync policy (execute immediately, within the async call) and the task policy (similar to async, but thread-locals are not cleared)<br />
If the std::future obtained from std::async is not moved from or bound to a reference, the destructor of the std::future will block at the end of the full expression until the asynchronous operation completes, essentially making code such as the following synchronous:<br />
&nbsp;<wbr>&nbsp;std::async(std::launch::async, []{ f(); }); // temporary&#8217;s dtor waits for f()<br />
&nbsp;<wbr>&nbsp;std::async(std::launch::async, []{ g(); }); // does not start until f() completes<br />
(note that the destructors of std::futures obtained by means other than a call to std::async never block)<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. DR       Applied to Behavior as published                                                              Correct behavior</p>
<p>LWG_2021 C++11      return type incorrect and value category of arguments unclear in the deferred case corrected return type and clarified that rvalues are used</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;

#include &lt;numeric&gt;

#include &lt;future&gt;

#include &lt;string&gt;

#include &lt;mutex&gt;
std::mutex m;

struct X {
    void foo(int i, const std::string &amp;str)
    {
        std::lock_guard&lt;std::mutex&gt; lk(m);
        std::cout &lt;&lt; str &lt;&lt; ' ' &lt;&lt; i &lt;&lt; '
';
    }
    void bar(const std::string &amp;str)
    {
        std::lock_guard&lt;std::mutex&gt; lk(m);
        std::cout &lt;&lt; str &lt;&lt; '
';
    }
    int operator()(int i)
    {
        std::lock_guard&lt;std::mutex&gt; lk(m);
        std::cout &lt;&lt; i &lt;&lt; '
';
        return i + 10;
    }
};
template &lt;typename RandomIt&gt;

int parallel_sum(RandomIt beg, RandomIt end)

{
    auto len = end - beg;
    if (len &lt; 1000)
        return std::accumulate(beg, end, 0);
    RandomIt mid = beg + len / 2;
    auto handle = std::async(std::launch::async,
                             parallel_sum&lt;RandomIt&gt;, mid, end);
    int sum = parallel_sum(beg, mid);
    return sum + handle.get();
}
int main()

{
    std::vector&lt;int&gt; v(10000, 1);
    std::cout &lt;&lt; &quot;The sum is &quot; &lt;&lt; parallel_sum(v.begin(), v.end()) &lt;&lt; '
';
    X x;
    // Calls (&amp;x)-&gt;foo(42, &quot;Hello&quot;) with default policy:
    // may print &quot;Hello 42&quot; concurrently or defer execution
    auto a1 = std::async(&amp;X::foo, &amp;x, 42, &quot;Hello&quot;);
    // Calls x.bar(&quot;world!&quot;) with deferred policy
    // prints &quot;world!&quot; when a2.get() or a2.wait() is called
    auto a2 = std::async(std::launch::deferred, &amp;X::bar, x, &quot;world!&quot;);
    // Calls X()(43); with async policy
    // prints &quot;43&quot; concurrently
    auto a3 = std::async(std::launch::async, X(), 43);
    a2.wait();                     // prints &quot;world!&quot;
    std::cout &lt;&lt; a3.get() &lt;&lt; '
'; // prints &quot;53&quot;

} // if a1 is not done at this point, destructor of a1 prints &quot;Hello 42&quot; here
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;The sum is 10000<br />
&nbsp;<wbr>&nbsp;43<br />
&nbsp;<wbr>&nbsp;world!<br />
&nbsp;<wbr>&nbsp;53<br />
&nbsp;<wbr>&nbsp;Hello 42</p>
