---
title: "stdlongjmp(3)"
name: "stdlongjmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlongjmp/"
description: "std::longjmp – std::longjmp"
---

<p>std::longjmp &#8211; std::longjmp</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;csetjmp&gt;<br />
void longjmp( std::jmp_buf env, int status ); <i>(until C++17)</i><br />
[[noreturn]] void longjmp( std::jmp_buf env, int status ); <i>(since C++17)</i><br />
Loads the execution context env saved by a previous call to setjmp. This function does not return. Control is transferred to the call site of the macro setjmp that set up env. That setjmp then returns the value, passed as the status.<br />
If the function that called setjmp has exited, the behavior is undefined (in other words, only long jumps up the call stack are allowed)<br />
No destructors for automatic objects are called. If replacing of std::longjmp with throw and setjmp with catch would execute a non-trivial destructor for any automatic object, the behavior of such std::longjmp is undefined. </p>
<h2>Parameters</h2>
<p>env &#8211; variable referring to the execution state of the program saved by setjmp<br />
status &#8211; the value to return from setjmp. If it is equal to 0, 1 is used instead</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Notes</h2>
<p>longjmp is the mechanism used in C to handle unexpected error conditions where the function cannot return meaningfully. C++ generally uses exception_handling for this purpose. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;csetjmp&gt;
std::jmp_buf jump_buffer;
[[noreturn]] void a(int count)

{
    std::cout &lt;&lt; &quot;a(&quot; &lt;&lt; count &lt;&lt; &quot;) called
&quot;;
    std::longjmp(jump_buffer, count + 1); // setjmp() will return count+1
}
int main()

{
    volatile int count = 0; // local variables must be volatile for setjmp
    if (setjmp(jump_buffer) != 9) {
        a(count++); // This will cause setjmp() to exit
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;a<code>(0)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-a/">a</a><code>(1)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-a/">a</a><code>(2)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/3-a/">a</a><code>(3)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/4-a/">a</a><code>(4)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/5-a/">a</a><code>(5)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/6-a/">a</a><code>(6)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/7-a/">a</a><code>(7)</code> called<br />
&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/8-a/">a</a><code>(8)</code> called</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;saves the context<br />
setjmp <i>(function macro)</i> </p>
