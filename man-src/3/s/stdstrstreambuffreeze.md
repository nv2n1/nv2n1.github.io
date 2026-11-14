---
title: "stdstrstreambuffreeze(3)"
name: "stdstrstreambuffreeze"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambuffreeze/"
description: "std::strstreambuf::freeze – std::strstreambuf::freeze"
---

<p>std::strstreambuf::freeze &#8211; std::strstreambuf::freeze</p>
<h2>Synopsis</h2>
<pre><code>void freeze(bool freezefl = true);</code></pre>
<p>If the buffer uses dynamic allocation, sets the frozen status of the stream to freezefl.<br />
While the stream is frozen, overflow() will not reallocate the buffer and the destructor will not deallocate the buffer (thereby causing a memory leak). </p>
<h2>Parameters</h2>
<p>freezefl &#8211; new value to set the freeze status to</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Notes</h2>
<p>Every call to str() freezes the stream to preserve the validity of the pointer it returns. To allow the destructor to deallocate the buffer, freeze(false) needs to be called explicitly. </p>
<h2>Example</h2>
<p>In this example, initial allocation of the underlying array was for 16 bytes<br />
 // Run this code </p>
<pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    {
        std::strstream dyn;      // dynamically-allocated read/write buffer
        dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23; // note: no std::ends to demonstrate append behavior
        std::cout &lt;&lt; &quot;dynamic buffer holds &quot; &lt;&lt; dyn.pcount() &lt;&lt; &quot; characters: '&quot;;
        std::cout.write(dyn.str(), dyn.pcount()) &lt;&lt; &quot;'
&quot;;
        // the buffer is now frozen, further output will not make the buffer grow
        dyn &lt;&lt; &quot;more output, hopefully enough to run out of the allocated space&quot; &lt;&lt; std::ends;
        std::cout &lt;&lt; &quot;After more output, it holds &quot;
                  &lt;&lt; dyn.pcount() &lt;&lt; &quot; characters: '&quot; &lt;&lt; dyn.str() &lt;&lt; &quot;'
&quot;;
        dyn.freeze(false); // unfreeze before destructor
    }                      // memory freed by the destructor
    {
        char arr[20];
        std::ostrstream st(arr, sizeof arr); // fixed-size buffer
        st &lt;&lt; 1.23;                          // note: no std::ends to demonstrate append behavior
        std::cout &lt;&lt; &quot;static buffer holds &quot;
                  &lt;&lt; st.pcount() &lt;&lt; &quot; characters: '&quot;;
        std::cout.write(st.str(), st.pcount());
        std::cout &lt;&lt; &quot;'
&quot;;
        st &lt;&lt; &quot;more output, hopefully enough to run out of the allocated space&quot; &lt;&lt; std::ends;
        std::cout &lt;&lt; &quot;static buffer holds &quot;
                  &lt;&lt; st.pcount() &lt;&lt; &quot; characters: '&quot;;
        std::cout.write(st.str(), st.pcount());
        std::cout &lt;&lt; &quot;'
&quot;;
    } // nothing to deallocate, no need to unfreeze,
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;dynamic buffer holds 10 characters: &#8216;Test: 1.23&#8217;<br />
&nbsp;<wbr>&nbsp;After more output, it holds 16 characters: &#8216;Test: 1.23more o&#8217;<br />
&nbsp;<wbr>&nbsp;static buffer holds 4 characters: &#8216;1.23&#8217;<br />
&nbsp;<wbr>&nbsp;static buffer holds 20 characters: &#8216;1.23more output, hop&#8217;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disables/enables automatic reallocation<br />
freeze <i>(public member function of std::strstream)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disables/enables automatic reallocation<br />
freeze <i>(public member function of std::ostrstream)</i><br />
destructor destructs a strstreambuf object, optionally deallocating the character array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function)</i><br />
<code>[virtual]</code><br />
overflow appends a character to the output sequence, may reallocate or initially allocate the buffer if dynamic and not frozen<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
