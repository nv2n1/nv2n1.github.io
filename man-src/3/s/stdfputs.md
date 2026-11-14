---
title: "stdfputs(3)"
name: "stdfputs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfputs/"
---

std::fputs - std::fputs

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fputs(const char *str, std::FILE *stream);</code></pre> 
Writes every character from the null-terminated string str to the output stream stream, as if by repeatedly executing std::fputc. 
The terminating null character from str is not written. 

<h2>Parameters</h2>

str - null-terminated character string to be written 
stream - output stream

<h2>Return value</h2>

On success, returns a non-negative value 
On failure, returns EOF and sets the error indicator (see std::ferror) on stream. 

<h2>Notes</h2>

The related function std::puts appends a newline character to the output, while std::fputs writes the string unmodified. 
Different implementations return different non-negative numbers: some return the last character written, some return the number of characters written (or INT_MAX if the string was longer than that), some simply return a non-negative constant such as zero. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;
int main(void)

{
    int rc = std::fputs(&quot;Hello World&quot;, stdout);
    if (rc == EOF)
        std::perror(&quot;fputs()&quot;); // POSIX requires that errno is set
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello World

<h2>See also</h2>

printf 
fprintf 
sprintf 
snprintf prints formatted output to stdout, a file stream or a buffer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to stdout 
puts <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide string to a file stream 
fputws <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character string from a file stream 
fgets <i>(function)</i> 
