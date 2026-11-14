---
title: "stdlock(3)"
name: "stdlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlock/"
---

std::lock - std::lock

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;mutex&gt;

    template &lt;class Lockable1, class Lockable2, class... LockableN&gt;
    (since C++ 11)

        void lock(Lockable1 &amp;lock1, Lockable2 &amp;lock2, LockableN &amp;...lockn);</code></pre> 
Locks the given Lockable objects lock1, lock2, ..., lockn using a deadlock avoidance algorithm to avoid deadlock. 
The objects are locked by an unspecified series of calls to lock, try_lock, and unlock. If a call to lock or unlock results in an exception, unlock is called for any locked objects before rethrowing. 

<h2>Parameters</h2>

lock1, lock2, ... , lockn - the Lockable objects to lock

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

Boost_provides_a_version_of_this_function that takes a sequence of Lockable objects defined by a pair of iterators. 
std::scoped_lock offers a RAII wrapper for this function, and is generally preferred to a naked call to std::lock. 

<h2>Example</h2>

The following example uses std::lock to lock pairs of mutexes without deadlock. 
 // Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;functional&gt;

#include &lt;chrono&gt;

#include &lt;string&gt;
struct Employee {
    Employee(std::string id)
        : id(id)
    {
    }
    std::string id;
    std::vector&lt;std::string&gt; lunch_partners;
    std::mutex m;
    std::string output() const
    {
        std::string ret = &quot;Employee &quot; + id + &quot; has lunch partners: &quot;;
        for (const auto &amp;partner : lunch_partners)
            ret += partner + &quot; &quot;;
        return ret;
    }
};
void send_mail(Employee &amp;, Employee &amp;)

{
    // simulate a time-consuming messaging operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
void assign_lunch_partner(Employee &amp;e1, Employee &amp;e2)

{
    static std::mutex io_mutex;
    {
        std::lock_guard&lt;std::mutex&gt; lk(io_mutex);
        std::cout &lt;&lt; e1.id &lt;&lt; &quot; and &quot; &lt;&lt; e2.id &lt;&lt; &quot; are waiting for locks&quot; &lt;&lt; std::endl;
    }
    // use std::lock to acquire two locks without worrying about
    // other calls to assign_lunch_partner deadlocking us
    {
        std::lock(e1.m, e2.m);
        std::lock_guard&lt;std::mutex&gt; lk1(e1.m, std::adopt_lock);
        std::lock_guard&lt;std::mutex&gt; lk2(e2.m, std::adopt_lock);

        // Equivalent code (if unique_locks are needed, e.g. for condition variables)

        //        std::unique_lock&lt;std::mutex&gt; lk1(e1.m, std::defer_lock);

        //        std::unique_lock&lt;std::mutex&gt; lk2(e2.m, std::defer_lock);

        //        std::lock(lk1, lk2);

        // Superior solution available in C++17

        //        std::scoped_lock lk(e1.m, e2.m);
        {
            std::lock_guard&lt;std::mutex&gt; lk(io_mutex);
            std::cout &lt;&lt; e1.id &lt;&lt; &quot; and &quot; &lt;&lt; e2.id &lt;&lt; &quot; got locks&quot; &lt;&lt; std::endl;
        }
        e1.lunch_partners.push_back(e2.id);
        e2.lunch_partners.push_back(e1.id);
    }
    send_mail(e1, e2);
    send_mail(e2, e1);
}
int main()

{
    Employee alice(&quot;alice&quot;), bob(&quot;bob&quot;), christina(&quot;christina&quot;), dave(&quot;dave&quot;);
    // assign in parallel threads because mailing users about lunch assignments
    // takes a long time
    std::vector&lt;std::thread&gt; threads;
    threads.emplace_back(assign_lunch_partner, std::ref(alice), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(alice));
    threads.emplace_back(assign_lunch_partner, std::ref(dave), std::ref(bob));
    for (auto &amp;thread : threads)
        thread.join();
    std::cout &lt;&lt; alice.output() &lt;&lt; '\n'
              &lt;&lt; bob.output() &lt;&lt; '\n'
              &lt;&lt; christina.output() &lt;&lt; '\n'
              &lt;&lt; dave.output() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;alice and bob are waiting for locks 
&nbsp;<wbr>&nbsp;alice and bob got locks 
&nbsp;<wbr>&nbsp;christina and bob are waiting for locks 
&nbsp;<wbr>&nbsp;christina and bob got locks 
&nbsp;<wbr>&nbsp;christina and alice are waiting for locks 
&nbsp;<wbr>&nbsp;christina and alice got locks 
&nbsp;<wbr>&nbsp;dave and bob are waiting for locks 
&nbsp;<wbr>&nbsp;dave and bob got locks 
&nbsp;<wbr>&nbsp;Employee alice has lunch partners: bob christina 
&nbsp;<wbr>&nbsp;Employee bob has lunch partners: alice christina dave 
&nbsp;<wbr>&nbsp;Employee christina has lunch partners: bob alice 
&nbsp;<wbr>&nbsp;Employee dave has lunch partners: bob

<h2>See also</h2>

try_lock attempts to obtain ownership of mutexes via repeated calls to try_lock 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
scoped_lock deadlock-avoiding RAII wrapper for multiple mutexes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
