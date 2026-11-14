---
title: "stdcondition_variablenotify_one(3)"
name: "stdcondition_variablenotify_one"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcondition_variablenotify_one/"
---

std::condition_variable::notify_one - std::condition_variable::notify_one

<h2>Synopsis</h2>

<pre><code>void notify_one() noexcept;
(since C++ 11)</code></pre> 
If any threads are waiting on *this, calling notify_one unblocks one of the waiting threads. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

The effects of notify_one()/notify_all() and each of the three atomic parts of wait()/wait_for()/wait_until() (unlock+wait, wakeup, and lock) take place in a single total order that can be viewed as modification_order of an atomic variable: the order is specific to this individual condition_variable. This makes it impossible for notify_one() to, for example, be delayed and unblock a thread that started waiting just after the call to notify_one() was made. 
The notifying thread does not need to hold the lock on the same mutex as the one held by the waiting thread(s); in fact doing so is a pessimization, since the notified thread would immediately block again, waiting for the notifying thread to release the lock. However, some implementations (in particular many implementations of pthreads) recognize this situation and avoid this &quot;hurry up and wait&quot; scenario by transferring the waiting thread from the condition variable's queue directly to the queue of the mutex within the notify call, without waking it up. 
Notifying while under the lock may nevertheless be necessary when precise scheduling of events is required, e.g. if the waiting thread would exit the program if the condition is satisfied, causing destruction of the notifying thread's condition_variable. A spurious wakeup after mutex unlock but before notify would result in notify called on a destroyed object. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;condition_variable&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
std::condition_variable cv;

std::mutex cv_m;

int i = 0;

bool done = false;
void waits()

{
    std::unique_lock&lt;std::mutex&gt; lk(cv_m);
    std::cout &lt;&lt; &quot;Waiting... \n&quot;;
    cv.wait(lk, [] { return i == 1; });
    std::cout &lt;&lt; &quot;...finished waiting. i == 1\n&quot;;
    done = true;
}
void signals()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout &lt;&lt; &quot;Notifying falsely...\n&quot;;
    cv.notify_one(); // waiting thread is notified with i == 0.
                     // cv.wait wakes up, checks i, and goes back to waiting
    std::unique_lock&lt;std::mutex&gt; lk(cv_m);
    i = 1;
    while (!done) {
        std::cout &lt;&lt; &quot;Notifying true change...\n&quot;;
        lk.unlock();
        cv.notify_one(); // waiting thread is notified with i == 1, cv.wait returns
        std::this_thread::sleep_for(std::chrono::seconds(1));
        lk.lock();
    }
}
int main()

{
    std::thread t1(waits), t2(signals);
    t1.join();
    t2.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Waiting... 
&nbsp;<wbr>&nbsp;Notifying falsely... 
&nbsp;<wbr>&nbsp;Notifying true change... 
&nbsp;<wbr>&nbsp;...finished waiting. i == 1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;notifies all waiting threads 
notify_all <i>(public member function)</i> 
