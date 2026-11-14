---
title: "stdtry_lock(3)"
name: "stdtry_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtry_lock/"
---

std::try_lock - std::try_lock

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;mutex&gt;

    template &lt;class Lockable1, class Lockable2, class... LockableN&gt;
    (since C++ 11)

        int try_lock(Lockable1 &amp;lock1, Lockable2 &amp;lock2, LockableN &amp;...lockn);</code></pre> 
Tries to lock each of the given Lockable objects lock1, lock2, ..., lockn by calling try_lock in order beginning with the first. 
If a call to try_lock fails, no further call to try_lock is performed, unlock is called for any locked objects and a 0-based index of the object that failed to lock is returned. 
If a call to try_lock results in an exception, unlock is called for any locked objects before rethrowing. 

<h2>Parameters</h2>

lock1, lock2, ... , lockn - the Lockable objects to lock

<h2>Return value</h2>

-1 on success, or 0-based index value of the object that failed to lock. 

<h2>Example</h2>

The following example uses std::try_lock to periodically tally and reset counters running in separate threads. 
 // Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;vector&gt;

#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;

#include &lt;chrono&gt;
int main()

{
    int foo_count = 0;
    std::mutex foo_count_mutex;
    int bar_count = 0;
    std::mutex bar_count_mutex;
    int overall_count = 0;
    bool done = false;
    std::mutex done_mutex;
    auto increment = [](int &amp;counter, std::mutex &amp;m, const char *desc) {
        for (int i = 0; i &lt; 10; ++i) {
            std::unique_lock&lt;std::mutex&gt; lock(m);
            ++counter;
            std::cout &lt;&lt; desc &lt;&lt; &quot;: &quot; &lt;&lt; counter &lt;&lt; '\n';
            lock.unlock();
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    };
    std::thread increment_foo(increment, std::ref(foo_count),
                              std::ref(foo_count_mutex), &quot;foo&quot;);
    std::thread increment_bar(increment, std::ref(bar_count),
                              std::ref(bar_count_mutex), &quot;bar&quot;);
    std::thread update_overall([&amp;]() {
        done_mutex.lock();
        while (!done) {
            done_mutex.unlock();
            int result = std::try_lock(foo_count_mutex, bar_count_mutex);
            if (result == -1) {
                overall_count += foo_count + bar_count;
                foo_count = 0;
                bar_count = 0;
                std::cout &lt;&lt; &quot;overall: &quot; &lt;&lt; overall_count &lt;&lt; '\n';
                foo_count_mutex.unlock();
                bar_count_mutex.unlock();
            }
            std::this_thread::sleep_for(std::chrono::seconds(2));
            done_mutex.lock();
        }
        done_mutex.unlock();
    });
    increment_foo.join();
    increment_bar.join();
    done_mutex.lock();
    done = true;
    done_mutex.unlock();
    update_overall.join();
    std::cout &lt;&lt; &quot;Done processing\n&quot;
              &lt;&lt; &quot;foo: &quot; &lt;&lt; foo_count &lt;&lt; '\n'
              &lt;&lt; &quot;bar: &quot; &lt;&lt; bar_count &lt;&lt; '\n'
              &lt;&lt; &quot;overall: &quot; &lt;&lt; overall_count &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;bar: 1 
&nbsp;<wbr>&nbsp;foo: 1 
&nbsp;<wbr>&nbsp;foo: 2 
&nbsp;<wbr>&nbsp;bar: 2 
&nbsp;<wbr>&nbsp;foo: 3 
&nbsp;<wbr>&nbsp;overall: 5 
&nbsp;<wbr>&nbsp;bar: 1 
&nbsp;<wbr>&nbsp;foo: 1 
&nbsp;<wbr>&nbsp;bar: 2 
&nbsp;<wbr>&nbsp;foo: 2 
&nbsp;<wbr>&nbsp;bar: 3 
&nbsp;<wbr>&nbsp;overall: 10 
&nbsp;<wbr>&nbsp;bar: 1 
&nbsp;<wbr>&nbsp;foo: 1 
&nbsp;<wbr>&nbsp;bar: 2 
&nbsp;<wbr>&nbsp;foo: 2 
&nbsp;<wbr>&nbsp;overall: 14 
&nbsp;<wbr>&nbsp;bar: 1 
&nbsp;<wbr>&nbsp;foo: 1 
&nbsp;<wbr>&nbsp;bar: 2 
&nbsp;<wbr>&nbsp;overall: 17 
&nbsp;<wbr>&nbsp;foo: 1 
&nbsp;<wbr>&nbsp;bar: 1 
&nbsp;<wbr>&nbsp;foo: 2 
&nbsp;<wbr>&nbsp;overall: 20 
&nbsp;<wbr>&nbsp;Done processing 
&nbsp;<wbr>&nbsp;foo: 0 
&nbsp;<wbr>&nbsp;bar: 0 
&nbsp;<wbr>&nbsp;overall: 20

<h2>See also</h2>

lock locks specified mutexes, blocks if any are unavailable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
