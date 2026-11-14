---
title: "stdcerrstdwcerr(3)"
name: "stdcerrstdwcerr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcerrstdwcerr/"
description: "std::cerr,std::wcerr – std::cerr,std::wcerr"
---

<p>std::cerr,std::wcerr &#8211; std::cerr,std::wcerr</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;iostream&gt;<br />
extern std::ostream cerr; <code>(1)</code><br />
extern std::wostream wcerr; <code>(2)</code><br />
The global objects std::cerr and std::wcerr control output to a stream buffer of implementation-defined type (derived from std::streambuf and std::wstreambuf, respectively), associated with the standard C error output stream stderr.<br />
These objects are guaranteed to be initialized during or before the first time an object of type std::ios_base::Init is constructed and are available for use in the constructors and destructors of static objects with ordered_initialization (as long as &lt;iostream&gt; is included before the object is defined).<br />
Unless sync_with_stdio(false) has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output.<br />
Once initialized, (std::cerr.flags() &amp; unitbuf) != 0 (same for wcerr) meaning that any output sent to these stream objects is immediately flushed to the OS (via std::basic_ostream::sentry&#8217;s destructor).<br />
In addition, std::cerr.tie() returns &amp;std::cout (same for wcerr and wcout), meaning that any output operation on std::cerr first executes std::cout.flush() (via std::basic_ostream::sentry&#8217;s constructor) <i>(since C++11)</i> </p>
<h2>Notes</h2>
<p>The &#8216;c&#8217; in the name refers to &quot;character&quot; (stroustrup.com_FAQ); cerr means &quot;character error (stream)&quot; and wcerr means &quot;wide character error (stream)&quot; </p>
<h2>Example</h2>
<p>output to stderr via cerr flushes out the pending output on cout, while output to stderr via clog does not<br />
 // Run this code </p>
<pre><code>#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;chrono&gt;

void f()

{
    std::cout &lt;&lt; &quot;Output from thread...&quot;;
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout &lt;&lt; &quot;...thread calls flush()&quot; &lt;&lt; std::endl;
}
int main()

{
    std::thread t1(f);
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::clog &lt;&lt; &quot;This output from main is not tie()'d to cout
&quot;;
    std::cerr &lt;&lt; &quot;This output is tie()'d to cout
&quot;;
    t1.join();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;This output from main is not tie()&#8217;d to cout<br />
&nbsp;<wbr>&nbsp;Output from thread&#8230;This output is tie()&#8217;d to cout<br />
&nbsp;<wbr>&nbsp;&#8230;thread calls flush()</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initializes standard stream objects<br />
Init <i>(public member class of std::ios_base)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr<br />
clog (global object)<br />
wclog<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C output stream stdout<br />
cout (global object)<br />
wcout </p>
