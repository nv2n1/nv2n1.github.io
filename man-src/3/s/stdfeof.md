---
title: "stdfeof(3)"
name: "stdfeof"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfeof/"
---

std::feof - std::feof

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int feof(std::FILE *stream);</code></pre> 
Checks if the end of the given file stream has been reached. 

<h2>Parameters</h2>

stream - the file stream to check

<h2>Return value</h2>

Nonzero value if the end of the stream has been reached, otherwise 0. 

<h2>Notes</h2>

This function only reports the stream state as reported by the most recent I/O operation, it does not examine the associated data source. For example, if the most recent I/O was a std::fgetc, which returned the last byte of a file, std::feof returns zero. The next std::fgetc fails and changes the stream state to end-of-file. Only then std::feof returns non-zero. 
In typical usage, input stream processing stops on any error; feof and std::ferror are then used to distinguish between different error conditions. 

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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if end-of-file has been reached 
eof <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears errors 
clearerr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displays a character string corresponding of the current error to stderr 
perror <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks for a file error 
ferror <i>(function)</i> 
