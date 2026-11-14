---
title: "stdfclose(3)"
name: "stdfclose"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfclose/"
---

std::fclose - std::fclose

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fclose(std::FILE *stream);</code></pre> 
Closes the given file stream. Any unwritten buffered data are flushed to the OS. Any unread buffered data are discarded. 
Whether or not the operation succeeds, the stream is no longer associated with a file, and the buffer allocated by std::setbuf or std::setvbuf, if any, is also disassociated and deallocated if automatic allocation was used. 
The behavior is undefined if the value of the pointer stream is used after fclose returns. 

<h2>Parameters</h2>

stream - the file stream to close

<h2>Return value</h2>

0 on success, EOF otherwise 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;
int main()

{
    FILE *fp = std::fopen(&quot;test.txt&quot;, &quot;r&quot;);
    if (!fp) {
        std::perror(&quot;File opening failed&quot;);
        return EXIT_FAILURE;
    }
    int c;                                // note: int, not char, required to handle EOF
    while ((c = std::fgetc(fp)) != EOF) { // standard C I/O file reading loop
        std::putchar(c);
    }
    if (std::ferror(fp))
        std::puts(&quot;I/O error when reading&quot;);
    else if (std::feof(fp))
        std::puts(&quot;End of file reached successfully&quot;);
    std::fclose(fp);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;opens a file 
fopen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;open an existing stream with a different name 
freopen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flushes the put area buffer and closes the associated file 
close <i>(public member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i> 
