---
title: "stdsetvbuf(3)"
name: "stdsetvbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetvbuf/"
description: "std::setvbuf – std::setvbuf"
---

<p>std::setvbuf &#8211; std::setvbuf</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cstdio&gt;

    int setvbuf(std::FILE *stream, char *buffer, int mode, std::size_t size);</code></pre>
<p>Changes the the buffering mode of the given file stream stream as indicated by the argument mode. In addition,<br />
* If buffer is a null pointer, resizes the internal buffer to size.<br />
* If buffer is not a null pointer, instructs the stream to use the user-provided buffer of size size beginning at buffer. The stream must be closed (with fclose) before the lifetime of the array pointed to by buffer ends. The contents of the array after a successful call to setvbuf are indeterminate and any attempt to use it is undefined behavior. </p>
<h2>Parameters</h2>
<p>stream &#8211; the file stream to set the buffer to<br />
buffer &#8211; pointer to a buffer for the stream to use or null pointer to change size and mode only<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffering mode to use. It can be one of the following values: </p>
<p>mode &#8211; _IOFBF full buffering<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_IOLBF line buffering<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_IONBF no buffering </p>
<p>size &#8211; size of the buffer</p>
<h2>Return value</h2>
<p>0 on success or nonzero on failure. </p>
<h2>Notes</h2>
<p>This function may only be used after stream has been associated with an open file, but before any other operation (other than a failed call to std::setbuf/std::setvbuf).<br />
Not all size bytes will necessarily be used for buffering: the actual buffer size is usually rounded down to a multiple of 2, a multiple of page size, etc.<br />
On many implementations, line buffering is only available for terminal input streams.<br />
A common error is setting the buffer of stdin or stdout to an array whose lifetime ends before the program terminates: int main()<br />
{<br />
    char buf[BUFSIZ];<br />
    std::setbuf(stdin, buf);</p>
<p>} // lifetime of buf ends, undefined behavior<br />
The default buffer size BUFSIZ is expected to be the most efficient buffer size for file I/O on the implementation, but POSIX fstat often provides a better estimate. </p>
<h2>Example</h2>
<p>one use case for changing buffer size is when a better size is known<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cstdio&gt;

#include &lt;stdlib.h&gt;

#include &lt;sys/stat.h&gt;
int main()

{
    std::FILE *fp = std::fopen(&quot;test.txt&quot;, &quot;r&quot;);
    if (!fp) {
        std::perror(&quot;fopen&quot;);
        return 1;
    }
    struct stat stats;
    if (fstat(fileno(fp), &amp;stats) == -1) { // POSIX only
        std::perror(&quot;fstat&quot;);
        return 1;
    }
    std::cout &lt;&lt; &quot;BUFSIZ is &quot; &lt;&lt; BUFSIZ &lt;&lt; &quot;, but optimal block size is &quot;
              &lt;&lt; stats.st_blksize &lt;&lt; '
';
    if (std::setvbuf(fp, NULL, _IOFBF, stats.st_blksize) != 0) {
        perror(&quot;setvbuf failed&quot;); // POSIX version sets errno
        return 1;
    }
    int ch;
    while ((ch = std::fgetc(fp)) != EOF)
        ; // read entire file: use truss/strace to
          // observe the read(2) syscalls used
    std::fclose(fp);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;BUFSIZ is 8192, but optimal block size is 65536</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the buffer for a file stream<br />
setbuf <i>(function)</i><br />
setbuf provides user-supplied buffer or turns this filebuf unbuffered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code> </p>
