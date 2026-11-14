---
title: "stdstrstreambufsetbuf(3)"
name: "stdstrstreambufsetbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufsetbuf/"
description: "std::strstreambuf::setbuf – std::strstreambuf::setbuf"
---

<p>std::strstreambuf::setbuf &#8211; std::strstreambuf::setbuf</p>
<h2>Synopsis</h2>
<pre><code>protected:
virtual streambuf&lt;char&gt; *setbuf(char *s, std::streamsize n);</code></pre>
<p>If s is a null pointer and n is zero, this function has no effect.<br />
Otherwise, the effect is implementation-defined: some implementations do nothing, while some implementations deallocate the dynamic member array used as the buffer and begin using the user-supplied character array of size n, whose first element is pointed to by s.<br />
This function is protected virtual, it may only be called through pubsetbuf() or from member functions of a user-defined class derived from std::strstreambuf. </p>
<h2>Parameters</h2>
<p>s &#8211; pointer to the first byte in the user-provided buffer<br />
n &#8211; the number of bytes in the user-provided buffer</p>
<h2>Return value</h2>
<p>this </p>
<h2>Example</h2>
<p>Implementation test to check if setbuf() is supported on a dynamic strstream (output obtained with Sun Studio)<br />
 // Run this code </p>
<pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    char a[100] = {};
    std::strstream str;
    str.rdbuf()-&gt;pubsetbuf(a, sizeof a);
    str &lt;&lt; &quot;Test string&quot; &lt;&lt; std::ends;
    std::cout &lt;&lt; &quot;user-provided buffer holds '&quot; &lt;&lt; a &lt;&lt; &quot;'
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;user-provided buffer holds &#8216;Test string&#8217;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes setbuf()<br />
pubsetbuf <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
setbuf replaces the buffer with user-defined array, if permitted<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
setbuf attempts to replace the controlled character sequence with an array<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i><br />
<code>[virtual]</code><br />
setbuf provides user-supplied buffer or turns this filebuf unbuffered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code> </p>
