---
title: "stdputchar(3)"
name: "stdputchar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdputchar/"
---

std::putchar - std::putchar

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int putchar(int ch);</code></pre> 
Writes a character ch to stdout. Internally, the character is converted to unsigned char just before being written. 
Equivalent to putc(ch, stdout). 

<h2>Parameters</h2>

ch - character to be written

<h2>Return value</h2>

On success, returns the written character. 
On failure, returns EOF and sets the error indicator (see ferror()) on stdout. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;
int main()

{
    for (char c = 'a'; c != 'z'; c++)
        std::putchar(c);
    std::putchar('\n');
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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character to a file stream 
fputc <i>(function)</i> 
putc 
