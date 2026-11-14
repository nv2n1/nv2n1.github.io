---
title: "stdshared_locklock(3)"
name: "stdshared_locklock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_locklock/"
---

std::shared_lock&lt;Mutex&gt;::lock - std::shared_lock&lt;Mutex&gt;::lock

<h2>Synopsis</h2>

<pre><code>void lock();
(since C++ 14)</code></pre> 
Locks the associated mutex in shared mode. Effectively calls mutex()-&gt;lock_shared(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;lock_shared() 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the associated mutex is already locked by this shared_lock (that is, owns_lock returns true), std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: show a meaningful use of shared_lock::lock 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;mutex&gt;

#include &lt;string&gt;

#include &lt;shared_mutex&gt;

#include &lt;thread&gt;
std::string file = &quot;Original content.&quot;; // Simulates a file

std::mutex output_mutex; // mutex that protects output operations.

std::shared_mutex file_mutex; // reader/writer mutex
void read(int id)

{
    std::string content;
    {
        std::shared_lock lock(file_mutex, std::defer_lock); // Do not lock it first.
        lock.lock();                                        // Lock it here.
        content = file;
    }
    std::lock_guard lock(output_mutex);
    std::cout &lt;&lt; &quot;Contents read by reader #&quot; &lt;&lt; id &lt;&lt; &quot;: &quot; &lt;&lt; content &lt;&lt; '\n';
}
void write()

{
    {
        std::lock_guard file_lock(file_mutex);
        file = &quot;New content&quot;;
    }
    std::lock_guard output_lock(output_mutex);
    std::cout &lt;&lt; &quot;New content saved.\n&quot;;
}
int main()

{
    std::cout &lt;&lt; &quot;Two readers reading from file.\n&quot;
              &lt;&lt; &quot;A writer competes with them.\n&quot;;
    std::thread reader1(read, 1);
    std::thread reader2(read, 2);
    std::thread writer(write);
    reader1.join();
    reader2.join();
    writer.join();
    std::cout &lt;&lt; &quot;The first few operations to file are done.\n&quot;;
    reader1 = std::thread(read, 3);
    reader1.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Two readers reading from file. 
&nbsp;<wbr>&nbsp;A writer competes with them. 
&nbsp;<wbr>&nbsp;Contents read by reader #1: Original content. 
&nbsp;<wbr>&nbsp;Contents read by reader #2: Original content. 
&nbsp;<wbr>&nbsp;New content saved. 
&nbsp;<wbr>&nbsp;The first few operations to file are done. 
&nbsp;<wbr>&nbsp;Contents read by reader #3: New content

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
