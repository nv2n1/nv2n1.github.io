---
title: "stdfgetcstdgetc(3)"
name: "stdfgetcstdgetc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfgetcstdgetc/"
---

std::fgetc,std::getc - std::fgetc,std::getc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fgetc(std::FILE *stream);

int getc(std::FILE *stream);</code></pre> 
Reads the next character from the given input stream. 

<h2>Parameters</h2>

stream - to read the character from

<h2>Return value</h2>

The obtained character on success or EOF on failure. 
If the failure has been caused by end of file condition, additionally sets the eof indicator (see std::feof()) on stream. If the failure has been caused by some other error, sets the error indicator (see std::ferror()) on stream. 

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

gets reads a character string from stdin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(deprecated in C++11) 
(removed in C++14) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character to a file stream 
fputc <i>(function)</i> 
putc 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts a character back into a file stream 
ungetc <i>(function)</i> 
