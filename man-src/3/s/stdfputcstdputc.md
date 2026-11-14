---
title: "stdfputcstdputc(3)"
name: "stdfputcstdputc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfputcstdputc/"
---

std::fputc,std::putc - std::fputc,std::putc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fputc(int ch, std::FILE *stream);

int putc(int ch, std::FILE *stream);</code></pre> 
Writes a character ch to the given output stream stream. 
Internally, the character is converted to unsigned char just before being written. 
In C, putc() may be implemented as a macro, which is disallowed in C++. Therefore calls to std::fputc() and std::putc() always have the same effect. 

<h2>Parameters</h2>

ch - character to be written 
stream - output stream

<h2>Return value</h2>

On success, returns the written character. 
On failure, returns EOF and sets the error indicator (see std::ferror()) on stream. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;
int main()

{
    for (char c = 'a'; c != 'z'; c++)
        std::putc(c, stdout);
    std::putc('\n', stdout);
    // putchar return value is not equal to the argument
    int r = 0x1070;
    std::printf(&quot;\n0x%x\n&quot;, r);
    r = std::putchar(r);
    std::printf(&quot;\n0x%x\n&quot;, r);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;abcdefghijklmnopqrstuvwxy 
&nbsp;<wbr>&nbsp;0x1070 
&nbsp;<wbr>&nbsp;p 
&nbsp;<wbr>&nbsp;0x70

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character to stdout 
putchar <i>(function)</i> 
