---
title: "stdrecursive_mutextry_lock(3)"
name: "stdrecursive_mutextry_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrecursive_mutextry_lock/"
---

std::recursive_mutex::try_lock - std::recursive_mutex::try_lock

<h2>Synopsis</h2>

bool try_lock(); <i>(since C++11)</i> 
Tries to lock the mutex. Returns immediately. On successful lock acquisition returns true, otherwise returns false. 
This function is allowed to fail spuriously and return false even if the mutex is not currently locked by any other thread. 
A thread may call try_lock on a recursive mutex repeatedly. Successful calls to try_lock increment the ownsership count: the mutex will only be released after the thread makes a matching number of calls to unlock. 
The maximum number of levels of ownership is unspecified. A call to try_lock will return false if this number is exceeded. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. Note that prior lock() does not synchronize with this operation if it returns false. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the lock was acquired successfully, otherwise false. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;mutex&gt;
int main()

{
    std::recursive_mutex test;
    if (test.try_lock() == true) {
        std::cout &lt;&lt; &quot;lock acquired&quot; &lt;&lt; std::endl;
        test.unlock();
        // now unlock the mutex
    } else {
        std::cout &lt;&lt; &quot;lock not acquired&quot; &lt;&lt; std::endl;
    }
    test.lock();

    // to lock it again
    if (test.try_lock()) { // true can be left out
        std::cout &lt;&lt; &quot;lock acquired&quot; &lt;&lt; std::endl;
    } else {
        std::cout &lt;&lt; &quot;lock not acquired&quot; &lt;&lt; std::endl;
    }
    test.unlock();
}</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;lock acquired 
&nbsp;<wbr>&nbsp;lock not acquired

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i> 
