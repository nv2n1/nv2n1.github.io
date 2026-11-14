---
title: "stdraise(3)"
name: "stdraise"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdraise/"
---

std::raise - std::raise

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;csignal&gt;

    int raise(int sig);</code></pre> 
Sends signal sig to the program. The signal handler (specified using the std::signal() function) is invoked. 
If the user-defined signal handling strategy is not set using std::signal() yet, it is implementation-defined whether the signal will be ignored or default handler will be invoked. 

<h2>Parameters</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the signal to be sent. It can be an implementation-defined value or one of the following values: 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGABRT 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGFPE defines signal types 
sig - SIGILL (macro constant) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGINT 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGSEGV 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SIGTERM

<h2>Return value</h2>

0 upon success, non-zero value on failure. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;csignal&gt;

#include &lt;iostream&gt;
void signal_handler(int signal)

{
    std::cout &lt;&lt; &quot;Received signal &quot; &lt;&lt; signal &lt;&lt; '\n';
}
int main()

{
    // Install a signal handler
    std::signal(SIGTERM, signal_handler);
    std::cout &lt;&lt; &quot;Sending signal &quot; &lt;&lt; SIGTERM &lt;&lt; '\n';
    std::raise(SIGTERM);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Sending signal 15 
&nbsp;<wbr>&nbsp;Received signal 15

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets a signal handler for particular signal 
signal <i>(function)</i> 
