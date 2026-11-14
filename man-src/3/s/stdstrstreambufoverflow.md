---
title: "stdstrstreambufoverflow(3)"
name: "stdstrstreambufoverflow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufoverflow/"
description: "std::strstreambuf::overflow – std::strstreambuf::overflow"
---

<p>std::strstreambuf::overflow &#8211; std::strstreambuf::overflow</p>
<h2>Synopsis</h2>
<pre><code>protected:
virtual int_type overflow(int_type c = EOF);
Appends the character c to the put area of the buffer, reallocating if possible.

1) If c==EOF, does nothing

2) Otherwise, if the put area has a write position available (pptr() &lt; epptr()), stores the character as if by *pptr()++ = c

3) Otherwise, if the stream buffer mode is not dynamic or the stream buffer is currently frozen, the function fails and returns EOF

4) Otherwise, the function reallocates (or initially allocates) a dynamic array large enough to hold the contents of the current dynamic array (if any) plus at least one additional write position. If a pointer to the allocating function palloc was used in the constructor, that function is called with (*palloc)(n) where n is the number of bytes to allocate, otherwise new char[n] is used. If a pointer to the deallocating function pfree was used in the constructor, that function is called with (*pfree)(p) to deallocate the previous array, if needed, otherwise delete[] p is used. If allocation fails, the function fails and returns EOF.
</code></pre>
<h2>Parameters</h2>
<p>c &#8211; the character to store in the put area</p>
<h2>Return value</h2>
<p>If c==EOF, returns some value other than EOF. Otherwise, returns (unsigned char)(c) on success, EOF on failure. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
struct mybuf : std::strstreambuf

{
    int_type overflow(int_type c)
    {
        std::cout &lt;&lt; &quot;Before overflow(): size of the put area is &quot; &lt;&lt; epptr() - pbase()
                  &lt;&lt; &quot; with &quot; &lt;&lt; epptr() - pptr() &lt;&lt; &quot; write positions available
&quot;;
        int_type rc = std::strstreambuf::overflow(c);
        std::cout &lt;&lt; &quot;After overflow(): size of the put area is &quot; &lt;&lt; epptr() - pbase()
                  &lt;&lt; &quot; with &quot; &lt;&lt; epptr() - pptr() &lt;&lt; &quot; write positions available
&quot;;
        return rc;
    }
};
int main()

{
    mybuf sbuf; // read-write dynamic strstreambuf
    std::iostream stream(&amp;sbuf);
    stream &lt;&lt; &quot;Sufficiently long string to overflow the initial allocation, at least &quot;
           &lt;&lt; &quot; on some systems.&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Before overflow(): size of the put area is 16 with 0 write positions available<br />
&nbsp;<wbr>&nbsp;After overflow(): size of the put area is 32 with 15 write positions available<br />
&nbsp;<wbr>&nbsp;Before overflow(): size of the put area is 32 with 0 write positions available<br />
&nbsp;<wbr>&nbsp;After overflow(): size of the put area is 64 with 31 write positions available<br />
&nbsp;<wbr>&nbsp;Before overflow(): size of the put area is 64 with 0 write positions available<br />
&nbsp;<wbr>&nbsp;After overflow(): size of the put area is 128 with 63 write positions available</p>
<h2>See also</h2>
<p>overflow writes characters to the associated output sequence from the put area<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
overflow appends a character to the output sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i><br />
<code>[virtual]</code><br />
overflow writes characters to the associated file from the put area<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes one character to the put area and advances the next pointer<br />
sputc <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inserts a character<br />
put <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> </p>
