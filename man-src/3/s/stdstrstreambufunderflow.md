---
title: "stdstrstreambufunderflow(3)"
name: "stdstrstreambufunderflow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufunderflow/"
description: "std::strstreambuf::underflow – std::strstreambuf::underflow"
---

<p>std::strstreambuf::underflow &#8211; std::strstreambuf::underflow</p>
<h2>Synopsis</h2>
<pre><code>protected:

virtual int_type underflow();</code></pre>
<p>Reads the next character from the get area of the buffer.<br />
If the input sequence has a read position available (gptr() &lt; egptr(), returns (unsigned char)(*gptr()).<br />
Otherwise, if pptr() is not null and pptr() &gt; egptr() (there is a put area and it is located after the get area), extends the end of the get area to include the characters that were recently written into the put area by incrementing egptr() to some value between gptr() and pptr(), and then returns (unsigned char)(*gptr()).<br />
Otherwise, returns EOF to indicate failure. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The next character in the get area, (unsigned char)(*gptr()) on success, EOF on failure </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
struct mybuf : std::strstreambuf

{
    int_type overflow(int_type c)
    {
        std::cout &lt;&lt; &quot;Before overflow(): size of the get area is &quot; &lt;&lt; egptr() - eback()
                  &lt;&lt; &quot; size of the put area is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        int_type rc = std::strstreambuf::overflow(c);
        std::cout &lt;&lt; &quot;After overflow(): size of the get area is &quot; &lt;&lt; egptr() - eback()
                  &lt;&lt; &quot; size of the put area is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        return rc;
    }
    int_type underflow()
    {
        std::cout &lt;&lt; &quot;Before underflow(): size of the get area is &quot; &lt;&lt; egptr() - eback()
                  &lt;&lt; &quot; size of the put area is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        int_type ch = std::strstreambuf::underflow();
        std::cout &lt;&lt; &quot;After underflow(): size of the get area is &quot; &lt;&lt; egptr() - eback()
                  &lt;&lt; &quot; size of the put area is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        if (ch == EOF) {
            std::cout &lt;&lt; &quot;underflow() returns EOF
&quot;;
        } else {
            std::cout &lt;&lt; &quot;underflow() returns '&quot; &lt;&lt; char(ch) &lt;&lt; &quot;'
&quot;;
        }
        return ch;
    }
};
int main()

{
    mybuf sbuf; // read-write dynamic strstreambuf
    std::iostream stream(&amp;sbuf);
    int n;
    stream &gt;&gt; n;
    stream.clear();
    stream &lt;&lt; &quot;123&quot;;
    stream &gt;&gt; n;
    std::cout &lt;&lt; n &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Before underflow(): size of the get area is 0 size of the put area is 0<br />
&nbsp;<wbr>&nbsp;After underflow(): size of the get area is 0 size of the put area is 0<br />
&nbsp;<wbr>&nbsp;underflow() returns EOF<br />
&nbsp;<wbr>&nbsp;Before overflow(): size of the get area is 0 size of the put area is 0<br />
&nbsp;<wbr>&nbsp;After overflow(): size of the get area is 0 size of the put area is 32<br />
&nbsp;<wbr>&nbsp;Before underflow(): size of the get area is 0 size of the put area is 32<br />
&nbsp;<wbr>&nbsp;After underflow(): size of the get area is 3 size of the put area is 32<br />
&nbsp;<wbr>&nbsp;underflow() returns &#8216;1&#8217;<br />
&nbsp;<wbr>&nbsp;Before underflow(): size of the get area is 3 size of the put area is 32<br />
&nbsp;<wbr>&nbsp;After underflow(): size of the get area is 3 size of the put area is 32<br />
&nbsp;<wbr>&nbsp;underflow() returns EOF<br />
&nbsp;<wbr>&nbsp;123</p>
<h2>See also</h2>
<p>underflow reads characters from the associated input sequence to the get area<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
underflow returns the next character available in the input sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i><br />
<code>[virtual]</code><br />
underflow reads from the associated file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reads one character from the input sequence without advancing the sequence<br />
sgetc <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts characters<br />
get <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> </p>
