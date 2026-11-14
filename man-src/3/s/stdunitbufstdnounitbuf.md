---
title: "stdunitbufstdnounitbuf(3)"
name: "stdunitbufstdnounitbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunitbufstdnounitbuf/"
description: "std::unitbuf,std::nounitbuf – std::unitbuf,std::nounitbuf"
---

<p>std::unitbuf,std::nounitbuf &#8211; std::unitbuf,std::nounitbuf</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ios&gt;<br />
std::ios_base&amp; unitbuf( std::ios_base&amp; str ); <code>(1)</code><br />
std::ios_base&amp; nounitbuf( std::ios_base&amp; str ); <code>(2)</code><br />
Enables or disables automatic flushing of the output stream after any output operation. Has no effect on input.<br />
1) enables the unitbuf flag in the stream str as if by calling str.setf(std::ios_base::unitbuf)<br />
2) disables the unitbuf flag in the stream str as if by calling str.unsetf(std::ios_base::unitbuf)<br />
This is an I/O manipulator, it may be called with an expression such as out &lt;&lt; std::unitbuf for any out of type std::basic_ostream or with an expression such as in &gt;&gt; std::unitbuf for any in of type std::basic_istream. </p>
<h2>Notes</h2>
<p>Flushing is performed in the destructor of the std::basic_ostream::sentry object, which calls str.rdbuf()-&gt;pubsync() if str.flags() &amp; std::ios_base::unitbuf == true.<br />
The standard output objects std::cerr and std::wcerr have their unitbuf bit set by default. </p>
<h2>Parameters</h2>
<p>str &#8211; reference to I/O stream</p>
<h2>Return value</h2>
<p>str (reference to the stream after manipulation) </p>
<h2>Example</h2>
<p>Without std::unitbuf or another explicit flush, the output is the same, but does not appear in real time.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;
template &lt;typename Diff&gt;

void log_progress(Diff d)

{
    std::cout &lt;&lt; &quot;..(&quot;
              &lt;&lt; std::chrono::duration_cast&lt;std::chrono::milliseconds&gt;(d).count()
              &lt;&lt; &quot; ms)..&quot;;
}
int main()

{
    volatile int sink = 0;
    std::cout &lt;&lt; std::unitbuf; // enable automatic flushing
    auto t1 = std::chrono::high_resolution_clock::now();
    for (int j = 0; j &lt; 5; ++j) {
        for (int n = 0; n &lt; 10000; ++n)
            for (int m = 0; m &lt; 20000; ++m)
                sink += m * n; // do some work
        auto now = std::chrono::high_resolution_clock::now();
        log_progress(now - t1);
    }
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;..(450 ms)&#8230;.(902 ms)&#8230;.(1352 ms)&#8230;.(1802 ms)&#8230;.(2252 ms)..</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flushes the output stream<br />
flush <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs &#8216;
&#8217; and flushes the output stream<br />
endl <i>(function template)</i> </p>
