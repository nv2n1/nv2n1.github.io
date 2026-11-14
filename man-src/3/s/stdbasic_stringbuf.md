---
title: "stdbasic_stringbuf(3)"
name: "stdbasic_stringbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_stringbuf/"
description: "std::basic_stringbuf<CharT,Traits,Allocator>::underflow – std::basic_stringbuf<CharT,Traits,Allocator>::underflow"
---

<p>std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;::underflow &#8211; std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;::underflow</p>
<h2>Synopsis</h2>
<p>protected:<br />
virtual int_type underflow()<br />
Reads the next character from the get area of the buffer.<br />
Specifically:<br />
1) If the input sequence has a read position available (egptr() &gt; gptr()), returns Traits::to_int_type(*gptr())<br />
2) Otherwise, if pptr() &gt; egptr() (some characters were inserted into the stream since the last time overflow() changed egptr()) then extends the end of the get area to include the most recently inserted characters, by changing egptr() to equal pptr(), and then returns Traits::to_int_type(*gptr())<br />
3) Otherwise, returns Traits::eof().<br />
Any character in the buffer which has been initialized, regardless of whether it originated from the string passed in the constructor or was appended by overflow(), is considered to be part of the input sequence. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>Traits::to_int_type(*gptr()) (the next character to read in the get area) in case of success, or Traits::eof() in case of failure. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;
struct mybuf : std::stringbuf

{
    mybuf(const std::string &amp;new_str,
          std::ios_base::openmode which = std::ios_base::in | std::ios_base::out)
        : std::stringbuf(new_str, which)
    {
    }
    int_type overflow(int_type c)
    {
        std::cout &lt;&lt; &quot;Before overflow(): get area size is &quot; &lt;&lt; egptr() - eback() &lt;&lt; ' '
                  &lt;&lt; &quot; the put area size is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        int_type rc = std::stringbuf::overflow(c);
        std::cout &lt;&lt; &quot;After overflow(): get area size is &quot; &lt;&lt; egptr() - eback() &lt;&lt; ' '
                  &lt;&lt; &quot; put area size is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        return rc;
    }
    int_type underflow()
    {
        std::cout &lt;&lt; &quot;Before underflow(): get area size is &quot; &lt;&lt; egptr() - eback() &lt;&lt; ' '
                  &lt;&lt; &quot; put area size is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        int_type ch = std::stringbuf::underflow();
        std::cout &lt;&lt; &quot;After underflow(): get area size is &quot; &lt;&lt; egptr() - eback() &lt;&lt; ' '
                  &lt;&lt; &quot; put area size is &quot; &lt;&lt; epptr() - pbase() &lt;&lt; '
';
        if (ch == EOF)
            std::cout &lt;&lt; &quot;underflow() returns EOF
&quot;;
        else
            std::cout &lt;&lt; &quot;underflow() returns '&quot; &lt;&lt; char(ch) &lt;&lt; &quot;'
&quot;;
        return ch;
    }
};
int main()

{
    mybuf sbuf(&quot;123&quot;); // read-write stream
    std::iostream stream(&amp;sbuf);
    int n;
    stream &gt;&gt; n; // calls sgetc() four times
                 // three calls return the characters '1', '2', '3'
                 // the fourth call, gptr() == egptr() and underflow() is called
                 // underflow returns EOF
    std::cout &lt;&lt; n &lt;&lt; '
';
    stream.clear();     // clear the eofbit
    stream &lt;&lt; &quot;123456&quot;; // sputc() is called 6 times
                        // first three calls store &quot;123&quot; in the existing buffer
                        // 4th call finds that pptr() == epptr() and calls overflow()
                        // overflow() grows the buffer and sets egptr() to 4
                        // 5th and 6th calls store '5' and '6', advancing pptr()
    stream &gt;&gt; n;        // calls sgetc() 4 times
                        // 1st call returns the '4' that was made available by overflow()
                        // on the 2nd call, egptr() == egptr() and underflow() is called
                        // underflow advances egptr() to equal pptr() (which is 6)
                        // 3rd sgetc() returns '6'
                        // 4th sgetc() finds gptr() == egptr(), calls underflow()
                        // underflow() returns EOF
    std::cout &lt;&lt; n &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Before underflow(): get area size is 3 put area size is 3<br />
&nbsp;<wbr>&nbsp;After underflow(): get area size is 3 put area size is 3<br />
&nbsp;<wbr>&nbsp;underflow() returns EOF<br />
&nbsp;<wbr>&nbsp;123<br />
&nbsp;<wbr>&nbsp;Before overflow(): get area size is 3 the put area size is 3<br />
&nbsp;<wbr>&nbsp;After overflow(): get area size is 4 put area size is 35<br />
&nbsp;<wbr>&nbsp;Before underflow(): get area size is 4 put area size is 35<br />
&nbsp;<wbr>&nbsp;After underflow(): get area size is 6 put area size is 35<br />
&nbsp;<wbr>&nbsp;underflow() returns &#8216;5&#8217;<br />
&nbsp;<wbr>&nbsp;Before underflow(): get area size is 6 put area size is 35<br />
&nbsp;<wbr>&nbsp;After underflow(): get area size is 6 put area size is 35<br />
&nbsp;<wbr>&nbsp;underflow() returns EOF<br />
&nbsp;<wbr>&nbsp;456</p>
<h2>See also</h2>
<p>underflow reads characters from the associated input sequence to the get area<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
underflow reads from the associated file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
underflow reads a character from the input sequence without advancing the next pointer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::strstreambuf)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reads one character from the input sequence without advancing the sequence<br />
sgetc <i>(public member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i> </p>
