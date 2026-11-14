---
title: "stdendl(3)"
name: "stdendl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdendl/"
---

std::endl - std::endl

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ostream&gt;

template&lt; class CharT, class Traits &gt;

std::basic_ostream&lt;CharT, Traits&gt;&amp; endl( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );</code></pre> 
Inserts a newline character into the output sequence os and flushes it as if by calling os.put(os.widen('\n')) followed by os.flush(). 
This is an output-only I/O manipulator, it may be called with an expression such as out &lt;&lt; std::endl for any out of type std::basic_ostream. 

<h2>Notes</h2>

This manipulator may be used to produce a line of output immediately, e.g. when displaying output from a long-running process, logging activity of multiple threads or logging activity of a program that may crash unexpectedly. An explicit flush of std::cout is also necessary before a call to std::system, if the spawned process performs any screen I/O. In most other usual interactive I/O scenarios, std::endl is redundant when used with std::cout because any input from std::cin, output to std::cerr, or program termination forces a call to std::cout.flush(). Use of std::endl in place of '\n', encouraged by some sources, may significantly degrade output performance. 
In many implementations, standard output is line-buffered, and writing '\n' causes a flush anyway, unless std::ios::sync_with_stdio(false) was executed. In those situations, unnecessary endl only degrades the performance of file output, not standard output. 
The code samples on this wiki follow_Bjarne_Stroustrup and The_C++_Core_Guidelines in flushing the standard output only where necessary. 
When an incomplete line of output needs to be flushed, the std::flush manipulator may be used. 
When every character of output needs to be flushed, the std::unitbuf manipulator may be used. 

<h2>Parameters</h2>

os - reference to output stream

<h2>Return value</h2>

os (reference to the stream after manipulation) 

<h2>Example</h2>

With \n instead of endl, the output would be the same, but may not appear in real time. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;
template &lt;typename Diff&gt;

void log_progress(Diff d)

{
    std::cout &lt;&lt; std::chrono::duration_cast&lt;std::chrono::milliseconds&gt;(d).count()
              &lt;&lt; &quot; ms passed&quot; &lt;&lt; std::endl;
}
int main()

{
    std::cout.sync_with_stdio(false); // on some platforms, stdout flushes on \n
    volatile int sink = 0;
    auto t1 = std::chrono::high_resolution_clock::now();
    for (int j = 0; j &lt; 5; ++j) {
        for (int n = 0; n &lt; 10000; ++n)
            for (int m = 0; m &lt; 20000; ++m)
                sink += m * n; // do some work
        auto now = std::chrono::high_resolution_clock::now();
        log_progress(now - t1);
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;487 ms passed 
&nbsp;<wbr>&nbsp;974 ms passed 
&nbsp;<wbr>&nbsp;1470 ms passed 
&nbsp;<wbr>&nbsp;1965 ms passed 
&nbsp;<wbr>&nbsp;2455 ms passed

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;controls whether output is flushed after each operation 
unitbuf <i>(function)</i> 
nounitbuf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flushes the output stream 
flush <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronizes with the underlying storage device 
flush <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
