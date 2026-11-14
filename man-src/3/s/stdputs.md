---
title: "stdputs(3)"
name: "stdputs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdputs/"
---

std::puts - std::puts

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int puts(const char *str);</code></pre> 
Writes every character from the null-terminated string str and one additional newline character '\n' to the output stream stdout, as if by repeatedly executing std::fputc. 
The terminating null character from str is not written. 

<h2>Parameters</h2>

str - character string to be written

<h2>Return value</h2>

On success, returns a non-negative value 
On failure, returns EOF and sets the error indicator (see std::ferror) on stdout. 

<h2>Notes</h2>

The std::puts function appends the newline character to the output, while std::fputs function does not. 
Different implementations return different non-negative numbers: some return the last character written, some return the number of characters written (or INT_MAX if the string was longer than that), some simply return a non-negative constant. 
A typical cause of failure for std::puts is running out of space on the file system, when stdout is redirected to a file. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;
int main()

{
    int rc = std::puts(&quot;Hello World&quot;);
    if (rc == EOF)
        std::perror(&quot;puts()&quot;); // POSIX requires that errno is set
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello World

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to a file stream 
fputs <i>(function)</i> 
printf 
fprintf 
sprintf 
snprintf prints formatted output to stdout, a file stream or a buffer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
