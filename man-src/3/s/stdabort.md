---
title: "stdabort(3)"
name: "stdabort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdabort/"
---

std::abort - std::abort

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
void abort(); <i>(until C++11)</i> 
[[noreturn]] void abort() noexcept; <i>(since C++11)</i> 
Causes abnormal program termination unless SIGABRT is being caught by a signal handler passed to std::signal and the handler does not return. 
Destructors of variables with automatic, 
thread local 
<i>(since C++11)</i> and static storage_durations are not called. Functions registered with std::atexit() 
and std::at_quick_exit 
<i>(since C++11)</i> are also not called. Whether open resources such as files are closed is implementation defined. An implementation defined status is returned to the host environment that indicates unsuccessful execution. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

POSIX specifies that the abort() function overrides blocking or ignoring the SIGABRT signal. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;csignal&gt;

#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
class Tester {

    public:
    Tester()  { std::cout &lt;&lt; &quot;Tester ctor\n&quot;; }
    ~Tester() { std::cout &lt;&lt; &quot;Tester dtor\n&quot;; }

};</code></pre> 
&nbsp;<wbr>&nbsp;Tester static_tester; // Destructor not called <pre><code>void signal_handler(int signal)

{
    if (signal == SIGABRT) {
        std::cerr &lt;&lt; &quot;SIGABRT received\n&quot;;
    } else {
        std::cerr &lt;&lt; &quot;Unexpected signal &quot; &lt;&lt; signal &lt;&lt; &quot; received\n&quot;;
    }
    std::_Exit(EXIT_FAILURE);
}
int main()

{
    Tester automatic_tester; // Destructor not called
                             // Setup handler
    auto previous_handler = std::signal(SIGABRT, signal_handler);
    if (previous_handler == SIG_ERR) {
        std::cerr &lt;&lt; &quot;Setup failed\n&quot;;
        return EXIT_FAILURE;
    }
    std::abort(); // Raise SIGABRT
    std::cout &lt;&lt; &quot;This code is unreachable\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Tester ctor 
&nbsp;<wbr>&nbsp;Tester ctor 
&nbsp;<wbr>&nbsp;SIGABRT received

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;causes normal program termination with cleaning up 
exit <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers a function to be called on std::exit() invocation 
atexit <i>(function)</i> 
quick_exit causes quick program termination without completely cleaning up 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
at_quick_exit registers a function to be called on quick_exit invocation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets a signal handler for particular signal 
signal <i>(function)</i> 
