---
title: "stdcall_once(3)"
name: "stdcall_once"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcall_once/"
---

std::call_once - std::call_once

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;mutex&gt;

    template &lt;class Callable, class... Args&gt;
    (since C++ 11)

        void call_once(std::once_flag &amp;flag, Callable &amp;&amp;f, Args &amp;&amp;...args);</code></pre> 
Executes the Callable object f exactly once, even if called concurrently, from several threads.

<h2>In detail:</h2>

* If, by the time call_once is called, flag indicates that f was already called, call_once returns right away (such a call to call_once is known as passive). 

 

 
* Otherwise, call_once invokes std::forward&lt;Callable&gt;(f) with the arguments std::forward&lt;Args&gt;(args)... (as if by std::invoke). Unlike the std::thread constructor or std::async, the arguments are not moved or copied because they don't need to be transferred to another thread of execution. (such a call to call_once is known as active). 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If that invocation throws an exception, it is propagated to the caller of call_once, and the flag is not flipped so that another call will be attempted (such call to call_once is known as exceptional). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If that invocation returns normally (such call to call_once is known as returning), the flag is flipped, and all other calls to call_once with the same flag are guaranteed to be passive. 

 

 
All active calls on the same flag form a single total order consisting of zero or more exceptional calls, followed by one returning call. The end of each active call synchronizes-with the next active call in that order. 
The return from the returning call synchronizes-with the returns from all passive calls on the same flag: this means that all concurrent calls to call_once are guaranteed to observe any side-effects made by the active call, with no additional synchronization.

<h2>Parameters</h2>

flag - an object, for which exactly one function gets executed 
f - Callable object to invoke 
args... - arguments to pass to the function

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

* std::system_error if any condition prevents calls to call_once from executing as specified 
* any exception thrown by f

<h2>Notes</h2>

If concurrent calls to call_once pass different functions f, it is unspecified which f will be called. The selected function runs in the same thread as the call_once invocation it was passed to. 
Initialization of function-local_statics is guaranteed to occur only once even when called from multiple threads, and may be more efficient than the equivalent code using std::call_once. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2442 C++11 the arguments are copied and/or moved before invocation no copying/moving is performed 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;

#include &lt;mutex&gt;
std::once_flag flag1, flag2;
void simple_do_once()

{
    std::call_once(flag1, []() { std::cout &lt;&lt; &quot;Simple example: called once\n&quot;; });
}
void may_throw_function(bool do_throw)

{
    if (do_throw) {
        std::cout &lt;&lt; &quot;throw: call_once will retry\n&quot;; // this may appear more than once
        throw std::exception();
    }
    std::cout &lt;&lt; &quot;Didn't throw, call_once will not attempt again\n&quot;; // guaranteed once
}
void do_once(bool do_throw)

{
    try {
        std::call_once(flag2, may_throw_function, do_throw);
    } catch (...) {
    }
}
int main()

{
    std::thread st1(simple_do_once);
    std::thread st2(simple_do_once);
    std::thread st3(simple_do_once);
    std::thread st4(simple_do_once);
    st1.join();
    st2.join();
    st3.join();
    st4.join();
    std::thread t1(do_once, true);
    std::thread t2(do_once, true);
    std::thread t3(do_once, false);
    std::thread t4(do_once, true);
    t1.join();
    t2.join();
    t3.join();
    t4.join();
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Simple example: called once 
&nbsp;<wbr>&nbsp;throw: call_once will retry 
&nbsp;<wbr>&nbsp;throw: call_once will retry 
&nbsp;<wbr>&nbsp;Didn't throw, call_once will not attempt again

<h2>See also</h2>

once_flag helper object to ensure that call_once invokes the function only once 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
