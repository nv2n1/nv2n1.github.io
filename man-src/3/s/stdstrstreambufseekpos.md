---
title: "stdstrstreambufseekpos(3)"
name: "stdstrstreambufseekpos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufseekpos/"
description: "std::strstreambuf::seekpos – std::strstreambuf::seekpos"
---

<p>std::strstreambuf::seekpos &#8211; std::strstreambuf::seekpos</p>
<h2>Synopsis</h2>
<pre><code>protected:

virtual pos_type seekpos(pos_type sp,

std::ios_base::openmode which = std::ios_base::in | std::ios_base::out );</code></pre>
<p>Repositions std::basic_streambuf::gptr and/or std::basic_streambuf::pptr, if possible, to the position indicated by sp<br />
If std::ios_base::in is set in which, attempts to reposition gptr() (the next pointer in the get area). If std::ios_base::out is set in which, attempts to reposition pptr() (the next pointer in the put area). If neither bit is set in which, the operation fails.<br />
Each next pointer is repositioned as follows:<br />
1) If the next pointer is null, the operation fails<br />
2) Otherwise, the new offset newoff (of type off_type) is determined by calling sp.offset(). If newoff is negative, out of bounds of the buffer, or invalid, the operation fails.<br />
3) Otherwise, the next pointer is assigned as if by gptr() = eback()+newoff or pptr() = pbase()+newoff. </p>
<h2>Parameters</h2>
<p>sp &#8211; stream position, such as one obtained by seekoff() or seekpos()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants: </p>
<p>which &#8211; Constant Explanation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in affect the input sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;out affect the output sequence</p>
<h2>Return value</h2>
<p>The resultant offset converted to pos_type on success or pos_type(off_type(-1)) on failure. </p>
<h2>Notes</h2>
<p>seekpos() is called by std::basic_streambuf::pubseekpos(), which is called by the single-argument versions of std::basic_istream::seekg() and std::basic_ostream::seekp() </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;strstream&gt;

#include &lt;cstring&gt;

#include &lt;iostream&gt;
struct mybuf : std::strstreambuf

{
    mybuf(const char *str)
        : std::strstreambuf(str, std::strlen(str))
    {
    }
    pos_type seekpos(pos_type sp, std::ios_base::openmode which)
    {
        std::cout &lt;&lt; &quot;Before seekpos(&quot; &lt;&lt; sp &lt;&lt; &quot;), size of the get area is &quot;
                  &lt;&lt; egptr() - eback() &lt;&lt; &quot; with &quot;
                  &lt;&lt; egptr() - gptr() &lt;&lt; &quot; read positions available
&quot;;
        pos_type rc = std::strstreambuf::seekpos(sp, which);
        std::cout &lt;&lt; &quot;seekpos() returns &quot; &lt;&lt; rc &lt;&lt; &quot;.
After the call, &quot;
                  &lt;&lt; &quot;size of the get area is &quot;
                  &lt;&lt; egptr() - eback() &lt;&lt; &quot; with &quot;
                  &lt;&lt; egptr() - gptr() &lt;&lt; &quot; read positions available
&quot;;
        return rc;
    }
};
int main()

{
    mybuf buf(&quot;12345&quot;);
    std::iostream stream(&amp;buf);
    stream.seekg(2);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Before <a href="/docs/linux/man/2-seekpos/">seekpos</a><code>(2)</code>, size of the get area is 5 with 5 read positions available<br />
&nbsp;<wbr>&nbsp;seekpos() returns 2.<br />
&nbsp;<wbr>&nbsp;After the call, size of the get area is 5 with 3 read positions available</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes seekpos()<br />
pubseekpos <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
seekpos repositions the next pointer in the input sequence, output sequence, or both using absolute addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i><br />
<code>[virtual]</code><br />
seekpos repositions the file position, using absolute addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
seekoff repositions the next pointer in the input sequence, output sequence, or both, using relative addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
