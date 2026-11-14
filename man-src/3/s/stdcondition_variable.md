---
title: "stdcondition_variable(3)"
name: "stdcondition_variable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variable/"
---

std::condition_variable - std::condition_variable

<h2>Synopsis</h2>

Defined in header &lt;condition_variable&gt; 
class condition_variable; <i>(since C++11)</i> 
The condition_variable class is a synchronization primitive that can be used to block a thread, or multiple threads at the same time, until another thread both modifies a shared variable (the condition), and notifies the condition_variable. 
The thread that intends to modify the variable has to 
&nbsp;<wbr>&nbsp;1. acquire a std::mutex (typically via std::lock_guard) 
&nbsp;<wbr>&nbsp;2. perform the modification while the lock is held 
&nbsp;<wbr>&nbsp;3. execute notify_one or notify_all on the std::condition_variable (the lock does not need to be held for notification) 
Even if the shared variable is atomic, it must be modified under the mutex in order to correctly publish the modification to the waiting thread. 
Any thread that intends to wait on std::condition_variable has to 
&nbsp;<wbr>&nbsp;1. acquire a std::unique_lock&lt;std::mutex&gt;, on the same mutex as used to protect the shared variable 
&nbsp;<wbr>&nbsp;2. execute wait, wait_for, or wait_until. The wait operations atomically release the mutex and suspend the execution of the thread. 
&nbsp;<wbr>&nbsp;3. When the condition variable is notified, a timeout expires, or a spurious_wakeup occurs, the thread is awakened, and the mutex is atomically reacquired. The thread should then check the condition and resume waiting if the wake up was spurious. 
std::condition_variable works only with std::unique_lock&lt;std::mutex&gt;; this restriction allows for maximal efficiency on some platforms. std::condition_variable_any provides a condition variable that works with any BasicLockable object, such as std::shared_lock. 
Condition variables permit concurrent invocation of the wait, wait_for, wait_until, notify_one and notify_all member functions. 
The class std::condition_variable is a StandardLayoutType. It is not CopyConstructible, MoveConstructible, CopyAssignable, or MoveAssignable. 

<h2>Member types</h2>

Member type Definition 
native_handle_type implementation-defined

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the object 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Notification</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies one waiting thread 
notify_one <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies all waiting threads 
notify_all <i>(public member function)</i>

<h2>Waiting</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up 
wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or after the specified timeout duration 
wait_for <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks the current thread until the condition variable is woken up or until specified time point has been reached 
wait_until <i>(public member function)</i>

<h2>Native handle</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the native handle 
native_handle <i>(public member function)</i>

<h2>Example</h2>

condition_variable is used in combination with a std::mutex to facilitate inter-thread communication. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;thread&gt;

#include &lt;mutex&gt;

#include &lt;condition_variable&gt;
std::mutex m;

std::condition_variable cv;

std::string data;

bool ready = false;

bool processed = false;
void worker_thread()

{
    // Wait until main() sends data
    std::unique_lock&lt;std::mutex&gt; lk(m);
    cv.wait(lk, [] { return ready; });
    // after the wait, we own the lock.
    std::cout &lt;&lt; &quot;Worker thread is processing data\n&quot;;
    data += &quot; after processing&quot;;
    // Send data back to main()
    processed = true;
    std::cout &lt;&lt; &quot;Worker thread signals data processing completed\n&quot;;
    // Manual unlocking is done before notifying, to avoid waking up
    // the waiting thread only to block again (see notify_one for details)
    lk.unlock();
    cv.notify_one();
}
int main()

{
    std::thread worker(worker_thread);
    data = &quot;Example data&quot;;
    // send data to the worker thread
    {
        std::lock_guard&lt;std::mutex&gt; lk(m);
        ready = true;
        std::cout &lt;&lt; &quot;main() signals data ready for processing\n&quot;;
    }
    cv.notify_one();
    // wait for the worker
    {
        std::unique_lock&lt;std::mutex&gt; lk(m);
        cv.wait(lk, [] { return processed; });
    }
    std::cout &lt;&lt; &quot;Back in main(), data = &quot; &lt;&lt; data &lt;&lt; '\n';
    worker.join();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;main() signals data ready for processing 
&nbsp;<wbr>&nbsp;Worker thread is processing data 
&nbsp;<wbr>&nbsp;Worker thread signals data processing completed 
&nbsp;<wbr>&nbsp;Back in main(), data = Example data after processing
