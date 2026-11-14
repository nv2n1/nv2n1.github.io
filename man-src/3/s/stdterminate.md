---
title: "stdterminate(3)"
name: "stdterminate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdterminate/"
---

std::terminate - std::terminate

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
void terminate(); <i>(until C++11)</i> 
[[noreturn]] void terminate() noexcept; <i>(since C++11)</i> 
std::terminate() is called by the C++ runtime when exception handling fails for any of the following reasons: 
1) an exception_is_thrown and not caught (it is implementation-defined whether any stack unwinding is done in this case) 
2) a function directly invoked by the exception handling mechanism while handling an exception that has not yet been caught exits via an exception (e.g. a destructor of some local object, or a copy constructor constructing a catch-clause parameter) 
3) the constructor or the destructor of a static or thread-local object throws an exception 
4) a function registered with std::atexit or std::at_quick_exit throws an exception 
5) a noexcept_specification is violated (it is implementation-defined whether any stack unwinding is done in this case) 
6) a dynamic_exception_specification is violated and the default handler for std::unexpected is executed <i>(until C++17)</i> 
7) a non-default handler for std::unexpected throws an exception that violates the previously violated dynamic exception specification, if the specification does not include std::bad_exception 
8) std::nested_exception::rethrow_nested is called for an object that isn't holding a captured exception 
9) an exception is thrown from the initial function of std::thread 
10) a joinable std::thread is destroyed or assigned to 
11) a function invoked by a parallel_algorithm exits via an uncaught exception and the execution_policy specifies termination. <i>(since C++17)</i> 
std::terminate() may also be called directly from the program. 
In any case, std::terminate calls the currently installed std::terminate_handler. The default std::terminate_handler calls std::abort. 
If a destructor reset the terminate handler during stack unwinding and the unwinding later led to terminate being called, the handler that was installed at the end of the throw expression is the one that will be called. (note: it was ambiguous whether re-throwing applied the new handlers) <i>(until C++11)</i> 
If a destructor reset the terminate handler during stack unwinding, it is unspecified which handler is called if the unwinding later led to terminate being called. <i>(since C++11)</i> 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2111 C++11 effect of calling set_terminate during stack unwinding differs from C++98 and breaks some ABIs made unspecified 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the type of the function called by std::terminate 
terminate_handler <i>(typedef)</i> 
