---
title: "stduncaught_exceptionstduncaught_exceptions(3)"
name: "stduncaught_exceptionstduncaught_exceptions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduncaught_exceptionstduncaught_exceptions/"
description: "std::uncaught_exception,std::uncaught_exceptions – std::uncaught_exception,std::uncaught_exceptions"
---

<p>std::uncaught_exception,std::uncaught_exceptions &#8211; std::uncaught_exception,std::uncaught_exceptions</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;exception&gt;<br />
bool uncaught_exception() throw(); <i>(until C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i><br />
bool uncaught_exception() noexcept; <code>(1)</code> (deprecated in C++17)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20)<br />
int uncaught_exceptions() noexcept; <code>(2)</code> <i>(since C++17)</i><br />
1) Detects if the current thread has a live exception object, that is, an exception has been thrown or rethrown and not yet entered a matching catch clause, std::terminate or std::unexpected. In other words, std::uncaught_exception detects if stack_unwinding is currently in progress.<br />
2) Detects how many exceptions in the current thread have been thrown or rethrown and not yet entered their matching catch clauses.<br />
Sometimes it&#8217;s safe to throw an exception even while std::uncaught_exception() == true. For example, if stack_unwinding causes an object to be destructed, the destructor for that object could run code that throws an exception as long as the exception is caught by some catch block before escaping the destructor. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) true if stack unwinding is currently in progress in this thread.<br />
2) The number of uncaught exception objects in the current thread. </p>
<h2>Notes</h2>
<p>An example where int-returning uncaught_exceptions is used is the boost.log library: the expression BOOST_LOG(logger) &lt;&lt; foo(); first creates a guard object and records the number of uncaught exceptions in its constructor. The output is performed by the guard object&#8217;s destructor unless foo() throws (in which case the number of uncaught exceptions in the destructor is greater than what the constructor observed) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;exception&gt;

#include &lt;stdexcept&gt;
struct Foo {
    int count = std::uncaught_exceptions();
    ~Foo()
    {
        std::cout &lt;&lt; (count == std::uncaught_exceptions()
                          ? &quot;~Foo() called normally
&quot;
                          : &quot;~Foo() called during stack unwinding
&quot;);
    }
};

int main()

{
    Foo f;
    try {
        Foo f;
        std::cout &lt;&lt; &quot;Exception thrown
&quot;;
        throw std::runtime_error(&quot;test exception&quot;);
    } catch (const std::exception &amp;e) {
        std::cout &lt;&lt; &quot;Exception caught: &quot; &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Exception thrown<br />
&nbsp;<wbr>&nbsp;~Foo() called during stack unwinding<br />
&nbsp;<wbr>&nbsp;Exception caught: test exception<br />
&nbsp;<wbr>&nbsp;~Foo() called normally</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function called when exception handling fails<br />
terminate <i>(function)</i><br />
exception_ptr shared pointer type for handling exception objects<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i><br />
<i>(C++11)</i><br />
current_exception captures the current exception in a std::exception_ptr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>* GOTW_issue_47:_Uncaught_Exceptions<br />
* Rationale_for_std::uncaught_exceptions</p>
