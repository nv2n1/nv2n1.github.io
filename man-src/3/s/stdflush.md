---
title: "stdflush(3)"
name: "stdflush"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdflush/"
---

std::flush - std::flush

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ostream&gt;

template&lt; class CharT, class Traits &gt;

std::basic_ostream&lt;CharT, Traits&gt;&amp; flush( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );</code></pre> 
Flushes the output sequence os as if by calling os.flush(). 
This is an output-only I/O manipulator, it may be called with an expression such as out &lt;&lt; std::flush for any out of type std::basic_ostream. 

<h2>Notes</h2>

This manipulator may be used to produce an incomplete line of output immediately, e.g. when displaying output from a long-running process, logging activity of multiple threads or logging activity of a program that may crash unexpectedly. An explicit flush of std::cout is also necessary before a call to std::system, if the spawned process performs any screen I/O (a common example is std::system(&quot;pause&quot;) on Windows). In most other usual interactive I/O scenarios, std::endl is redundant when used with std::cout because any input from std::cin, output to std::cerr, or program termination forces a call to std::cout.flush(). 
When a complete line of output needs to be flushed, the std::endl manipulator may be used. 
When every output operation needs to be flushed, the std::unitbuf manipulator may be used. 

<h2>Parameters</h2>

os - reference to output stream

<h2>Return value</h2>

os (reference to the stream after manipulation) 

<h2>Example</h2>

Without std::flush, the output would be the same, but may not appear in real time. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

template &lt;typename Diff&gt;

void log_progress(Diff d)

{
    std::cout &lt;&lt; &quot;..(&quot;
              &lt;&lt; std::chrono::duration_cast&lt;std::chrono::milliseconds&gt;(d).count()
              &lt;&lt; &quot; ms)..&quot; &lt;&lt; std::flush;
}

int main()

{
    volatile int sink = 0;
    auto t1 = std::chrono::high_resolution_clock::now();
    for (int j = 0; j &lt; 5; ++j) {
        for (int n = 0; n &lt; 10000; ++n)
            for (int m = 0; m &lt; 20000; ++m)
                sink += m * n; // do some work
        auto now = std::chrono::high_resolution_clock::now();
        log_progress(now - t1);
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;..(450 ms)....(901 ms)....(1350 ms)....(1800 ms)....(2250 ms)..

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether output is flushed after each operation 
unitbuf <i>(function)</i> 
nounitbuf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs '\n' and flushes the output stream 
endl <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronizes with the underlying storage device 
flush <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
