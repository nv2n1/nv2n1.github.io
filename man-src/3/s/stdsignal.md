---
title: "stdsignal(3)"
name: "stdsignal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsignal/"
---

std::signal - std::signal

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;csignal&gt;

    /*signal-handler*/ *signal(int sig, /*signal-handler*/ *handler);
(1)

    extern &quot;C&quot; using /*signal-handler*/
    = void(int);     // exposition-only (2)</code></pre> 
Sets the handler for signal sig. The signal handler can be set so that default handling will occur, signal is ignored, or a user-defined function is called. 
When signal handler is set to a function and a signal occurs, it is implementation defined whether std::signal(sig, SIG_DFL) will be executed immediately before the start of signal handler. Also, the implementation can prevent some implementation-defined set of signals from occurring while the signal handler runs. 
For some of the signals, the implementation may call std::signal(sig, SIG_IGN) at the startup of the program. For the rest, the implementation must call std::signal(sig, SIG_DFL). 
(Note: POSIX introduced sigaction to standardize these implementation-defined behaviors) 

<h2>Parameters</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the signal to set the signal handler to. It can be an implementation-defined value or one of the following values: 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGABRT 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGFPE defines signal types 
sig - SIGILL (macro constant) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGINT 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGSEGV 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGTERM 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the signal handler. This must be one of the following: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* SIG_DFL macro. The signal handler is set to default signal handler. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* SIG_IGN macro. The signal is ignored. 
handler - * pointer to a function. The signature of the function must be equivalent to the following: 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extern &quot;C&quot; void fun(int sig);

<h2>Return value</h2>

Previous signal handler on success or SIG_ERR on failure (setting a signal handler can be disabled on some implementations). 
Signal handler 
The following limitations are imposed on the user-defined function that is installed as a signal handler. 
If the signal handler is called NOT as a result of std::abort or std::raise (asynchronous signal), the behavior is undefined if 
* the signal handler calls any function within the standard library, except 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::abort 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::_Exit <i>(until C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::quick_exit 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::signal with the first argument being the number of the signal currently handled (async handler can re-register itself, but not other signals). 
* the signal handler refers to any object with static storage duration that is not std::atomic<i>(since C++11)</i> or volatile std::sig_atomic_t. 
The behavior is undefined if any signal handler performs any of the following: 
* call to any library function, except the following signal-safe functions (note, in particular, dynamic allocation is not signal-safe): 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* members functions of std::atomic and non-member functions from &lt;atomic&gt; if the atomic type they operate on is lock-free. The functions std::atomic_is_lock_free and std::atomic::is_lock_free are signal-safe for any atomic type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::signal with the first argument being the number of the signal currently handled (signal handler can re-register itself, but not other signals). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* member functions of std::numeric_limits 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::_Exit 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::abort 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::quick_exit 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The member functions of std::initializer_list and the std::initializer_list overloads of std::begin and std::end <i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::forward, std::move, std::move_if_noexcept 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions from &lt;type_traits&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::memcpy and std::memmove 
* access to an object with thread storage duration 
* a dynamic_cast expression 
* a throw expression 
* entry to a try block, including function-try-block 
* initialization of a static variable that performs dynamic_non-local_initialization (including delayed until first ODR-use) 
* waits for completion of initialization of any variable with static storage duration due to another thread concurrently initializing it 
If the user defined function returns when handling SIGFPE, SIGILL, SIGSEGV or any other implementation-defined signal specifying a computational exception, the behavior is undefined. 
If the signal handler is called as a result of std::abort or std::raise (synchronous signal), the behavior is undefined if the signal handler calls std::raise. 
On entry to the signal handler, the state of the floating-point_environment and the values of all objects is unspecified, except for 
* objects of type volatile std::sig_atomic_t 
* objects of lock-free std::atomic types <i>(since C++11)</i> <i>(until C++14)</i> 
* side effects made visible through std::atomic_signal_fence <i>(since C++11)</i> 
On return from a signal handler, the value of any object modified by the signal handler that is not volatile std::sig_atomic_t or lock-free std::atomic is indeterminate. 
A call to the function signal() synchronizes-with any resulting invocation of the signal handler. 
If a signal handler is executed as a result of a call to std::raise (synchronously), then the execution of the handler is sequenced-after the invocation of std::raise and sequenced-before the return from it and runs on the same thread as std::raise. Execution of the handlers for other signals is unsequenced with respect to the rest of the program and runs on an unspecified thread. <i>(since C++14)</i> 
Two accesses to the same object of type volatile std::sig_atomic_t do not result in a data race if both occur in the same thread, even if one or more occurs in a signal handler. For each signal handler invocation, evaluations performed by the thread invoking a signal handler can be divided into two groups A and B, such that no evaluations in B happen-before evaluations in A, and the evaluations of such volatile std::sig_atomic_t objects take values as though all evaluations in A happened-before the execution of the signal handler and the execution of the signal handler happened-before all evaluations in B. 

<h2>Notes</h2>

POSIX requires that signal is thread-safe, and specifies_a_list_of_async-signal-safe_library_functions that may be called from any signal handler. 
Signal handlers are expected to have C_linkage and, in general, only use the features from the common subset of C and C++. It is implementation-defined if a function with C++ linkage can be used as a signal handler. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;csignal&gt;

#include &lt;iostream&gt;
namespace

{
volatile std::sig_atomic_t gSignalStatus;

}
void signal_handler(int signal)

{
    gSignalStatus = signal;
}
int main()

{
    // Install a signal handler
    std::signal(SIGINT, signal_handler);
    std::cout &lt;&lt; &quot;SignalValue: &quot; &lt;&lt; gSignalStatus &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;Sending signal &quot; &lt;&lt; SIGINT &lt;&lt; '\n';
    std::raise(SIGINT);
    std::cout &lt;&lt; &quot;SignalValue: &quot; &lt;&lt; gSignalStatus &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;SignalValue: 0 
&nbsp;<wbr>&nbsp;Sending signal 2 
&nbsp;<wbr>&nbsp;SignalValue: 2

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;runs the signal handler for particular signal 
raise <i>(function)</i> 
atomic_signal_fence fence between a thread and a signal handler executed in the same thread 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
