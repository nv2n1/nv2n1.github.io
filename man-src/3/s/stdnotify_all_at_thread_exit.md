---
title: "stdnotify_all_at_thread_exit(3)"
name: "stdnotify_all_at_thread_exit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnotify_all_at_thread_exit/"
---

std::notify_all_at_thread_exit - std::notify_all_at_thread_exit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;condition_variable&gt;

    void notify_all_at_thread_exit(std::condition_variable &amp;cond, (since C++ 11)

                                                                      std::unique_lock&lt;std::mutex&gt;
                                                                          lk);</code></pre> 
notify_all_at_thread_exit provides a mechanism to notify other threads that a given thread has completely finished, including destroying all thread_local objects. It operates as follows: 
* Ownership of the previously acquired lock lk is transferred to internal storage. 
* The execution environment is modified such that when the current thread exits, the condition variable cond is notified as if by: 
lk.unlock(); 
cond.notify_all(); 
The implied lk.unlock is sequenced after (as defined in std::memory_order) the destruction of all objects with thread_local_storage_duration associated with the current thread. 
An equivalent effect may be achieved with the facilities provided by std::promise or std::packaged_task. 

<h2>Notes</h2>

Calling this function if lock.mutex() is not locked by the current thread is undefined behavior. 
Calling this function if lock.mutex() is not the same mutex as the one used by all other threads that are currently waiting on the same condition variable is undefined behavior. 
The supplied lock lk is held until the thread exits. Once this function has been called, no more threads may acquire the same lock in order to wait on cond. If some thread is waiting on this condition variable, it should not attempt to release and reacquire the lock when it wakes up spuriously. 
In typical use cases, this function is the last thing called by a detached thread. 

<h2>Parameters</h2>

cond - the condition variable to notify at thread exit 
lk - the lock associated with the condition variable cond

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

This partial code fragment illustrates how notify_all_at_thread_exit can be used to avoid accessing data that depends on thread locals while those thread locals are in the process of being destructed: 
 // Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;cassert&gt;
#include &lt;condition_variable&gt;

#include &lt;string&gt;
std::mutex m;

std::condition_variable cv;
bool ready = false;

std::string result; // some arbitrary type
void thread_func()

{
    thread_local std::string thread_local_data = &quot;42&quot;;
    std::unique_lock&lt;std::mutex&gt; lk(m);
    // assign a value to result using thread_local data
    result = thread_local_data;
    ready = true;
    std::notify_all_at_thread_exit(cv, std::move(lk));
} // 1. destroy thread_locals;
  // 2. unlock mutex;
  // 3. notify cv.
int main()

{
    std::thread t(thread_func);
    t.detach();
    // do other work
    // ...
    // wait for the detached thread
    std::unique_lock&lt;std::mutex&gt; lk(m);
    cv.wait(lk, [] { return ready; });
    // result is ready and thread_local destructors have finished, no UB
    assert(result == &quot;42&quot;);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the result to specific value while delivering the notification only at thread exit 
set_value_at_thread_exit <i>(public member function of std::promise&lt;R&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;executes the function ensuring that the result is ready only once the current thread exits 
make_ready_at_thread_exit <i>(public member function of std::packaged_task&lt;R(Args...)&gt;)</i> 
