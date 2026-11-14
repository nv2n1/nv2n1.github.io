---
title: "stdsetbuf(3)"
name: "stdsetbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsetbuf/"
---

std::setbuf - std::setbuf

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    void setbuf(std::FILE *stream, char *buffer);</code></pre> 
Sets the internal buffer to use for I/O operations performed on the C stream stream. 
If buffer is not null, equivalent to std::setvbuf(stream, buffer, _IOFBF, BUFSIZ) 
If buffer is null, equivalent to std::setvbuf(stream, NULL, _IONBF, 0), which turns off buffering. 

<h2>Parameters</h2>

stream - the file stream to set the buffer to. 
buffer - pointer to a buffer for the stream to use. If NULL is supplied, the buffering is turned off. If not null, must be able to hold at least BUFSIZ characters

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

If BUFSIZ is not the appropriate buffer size, std::setvbuf can be used to change it. 
std::setvbuf should also be used to detect errors, since std::setbuf does not indicate success or failure. 
This function may only be used after stream has been associated with an open file, but before any other operation (other than a failed call to std::setbuf/std::setvbuf). 
A common error is setting the buffer of stdin or stdout to an array whose lifetime ends before the program terminates: int main()
{
    char buf[BUFSIZ];
    std::setbuf(stdin, buf);

} // lifetime of buf ends, undefined behavior


<h2>Example</h2>

setbuf may be used to disable buffering on streams that require immediate output 
 // Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;
int main()

{
    using namespace std::chrono_literals;
    std::setbuf(stdout, NULL); // unbuffered stdout
    std::putchar('a');         // appears immediately on unbuffered stream
    std::this_thread::sleep_for(1s);
    std::putchar('b');
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ab

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the buffer and its size for a file stream 
setvbuf <i>(function)</i> 
