---
title: "stdfputws(3)"
name: "stdfputws"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfputws/"
---

std::fputws - std::fputws

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int fputws(const wchar_t *str, std::FILE *stream);</code></pre> 
Writes every wide character from the null-terminated wide string str to the output stream stream, as if by repeatedly executing std::fputwc. 
The terminating null wide character from str is not written. 

<h2>Parameters</h2>

str - null-terminated wide string to be written 
stream - output stream

<h2>Return value</h2>

On success, returns a non-negative value 
On failure, returns EOF and sets the error indicator (see std::ferror) on stream. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;clocale&gt;

#include &lt;cstdio&gt;

#include &lt;cwchar&gt;
int main()

{
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    int rc = std::fputws(L&quot;御休みなさい&quot;, stdout);
    if (rc == EOF)
        std::perror(&quot;fputws()&quot;); // POSIX requires that errno is set
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;御休みなさい

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to a file stream 
fputs <i>(function)</i> 
wprintf prints formatted wide character output to stdout, a file stream or a buffer 
fwprintf <i>(function)</i> 
swprintf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide string to a file stream 
fputws <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a wide string from a file stream 
fgetws <i>(function)</i> 
