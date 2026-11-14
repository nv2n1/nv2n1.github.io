---
title: "stdmutextry_lock(3)"
name: "stdmutextry_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmutextry_lock/"
description: "std::mutex::try_lock – std::mutex::try_lock"
---

<p>std::mutex::try_lock &#8211; std::mutex::try_lock</p>
<h2>Synopsis</h2>
<p>bool try_lock(); <i>(since C++11)</i><br />
Tries to lock the mutex. Returns immediately. On successful lock acquisition returns true, otherwise returns false.<br />
This function is allowed to fail spuriously and return false even if the mutex is not currently locked by any other thread.<br />
If try_lock is called by a thread that already owns the mutex, the behavior is undefined.<br />
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. Note that prior lock() does not synchronize with this operation if it returns false. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>true if the lock was acquired successfully, otherwise false. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;chrono&gt;

#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;iostream&gt; // std::cout
std::chrono::milliseconds interval(100);
std::mutex mutex;

int job_shared = 0;    // both threads can modify 'job_shared',
                       // mutex will protect this variable
int job_exclusive = 0; // only one thread can modify 'job_exclusive'
                       // no protection needed</code></pre>
<p>&nbsp;<wbr>&nbsp;// this thread can modify both &#8216;job_shared&#8217; and &#8216;job_exclusive&#8217;<br />
&nbsp;<wbr>&nbsp;void job_1()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::this_thread::sleep_for(interval); // let &#8216;job_2&#8217; take a lock </p>
<pre><code>while (true) {
    // try to lock mutex to modify 'job_shared'
    if (mutex.try_lock()) {
        std::cout &lt;&lt; &quot;job shared (&quot; &lt;&lt; job_shared &lt;&lt; &quot;)
&quot;;
        mutex.unlock();
        return;
    } else {
        // can't get lock to modify 'job_shared'
        // but there is some other work to do
        ++job_exclusive;
        std::cout &lt;&lt; &quot;job exclusive (&quot; &lt;&lt; job_exclusive &lt;&lt; &quot;)
&quot;;
        std::this_thread::sleep_for(interval);
    }
}
}
// this thread can modify only 'job_shared'

void job_2()

{
    mutex.lock();
    std::this_thread::sleep_for(5 * interval);
    ++job_shared;
    mutex.unlock();
}
int main()

{
    std::thread thread_1(job_1);
    std::thread thread_2(job_2);
    thread_1.join();
    thread_2.join();
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;job exclusive <code>(1)</code><br />
&nbsp;<wbr>&nbsp;job exclusive <code>(2)</code><br />
&nbsp;<wbr>&nbsp;job exclusive <code>(3)</code><br />
&nbsp;<wbr>&nbsp;job exclusive <code>(4)</code><br />
&nbsp;<wbr>&nbsp;job shared <code>(1)</code></p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available<br />
lock <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex<br />
unlock <i>(public member function)</i> </p>
