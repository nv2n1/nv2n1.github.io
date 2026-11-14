---
title: "stdungetc(3)"
name: "stdungetc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdungetc/"
---

std::ungetc - std::ungetc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int ungetc(int ch, std::FILE *stream);</code></pre> 
If ch does not equal EOF, pushes the character ch (reinterpreted as unsigned char) into the input buffer associated with the stream stream in such a manner than subsequent read operation from stream will retrieve that character. The external device associated with the stream is not modified. 
Stream repositioning operations std::fseek, std::fsetpos, and std::rewind discard the effects of ungetc. 
If ungetc is called more than once without an intervening read or repositioning, it may fail (in other words, a pushback buffer of size 1 is guaranteed, but any larger buffer is implementation-defined). If multiple successful ungetc were performed, read operations retrieve the pushed-back characters in reverse order of ungetc 
If ch equals EOF, the operation fails and the stream is not affected. 
A successful call to ungetc clears the end of file status flag std::feof. 
A successful call to ungetc on a binary stream decrements the stream position indicator by one (the behavior is indeterminate if the stream position indicator was zero). 
A successful call to ungetc on a text stream modifies the stream position indicator in unspecified manner but guarantees that after all pushed-back characters are retrieved with a read operation, the stream position indicator is equal to its value before ungetc. 

<h2>Parameters</h2>

ch - character to be pushed into the input stream buffer 
stream - file stream to put the character back to

<h2>Return value</h2>

On success ch is returned. 
On failure EOF is returned and the given stream remains unchanged. 

<h2>Notes</h2>

The size of the pushback buffer varies in practice from 4k (Linux, MacOS) to as little as 4 (Solaris) or the guaranteed minimum 1 (HPUX, AIX) 
The apparent size of the pushback buffer may be larger if the character that is pushed back equals the character existing at that location in the external character sequence (the implementation may simply decrement the read file position indicator and avoid maintaining a pushback buffer) 

<h2>Example</h2>

demonstrates the use of ungetc in its original purpose: implementing scanf 
 // Run this code <pre><code>#include &lt;cctype&gt;

#include &lt;cstdio&gt;
void demo_scanf(const char *fmt, std::FILE *s)
{
    if (*fmt == '%') {
        switch (*++fmt) {
        case 'u': {
            int c;
            while (std::isspace(c = std::getc(s))) {
            } // skip leading white space
            unsigned int num = 0;
            while (std::isdigit(c)) {
                num = num * 10 + c - '0';
                c = std::getc(s);
            }
            std::printf(&quot;%%u scanned %u\n&quot;, num);
            std::ungetc(c, s); // reprocess the non-digit
        }
        case 'c': {
            int c = std::getc(s);
            std::printf(&quot;%%c scanned '%c'\n&quot;, c);
        }
        }
    }
}
int main()

{
    std::FILE *f = std::fopen(&quot;input.txt&quot;, &quot;w+&quot;);
    std::fputs(&quot;123x&quot;, f);
    std::rewind(f);
    demo_scanf(&quot;%u%c&quot;, f);
    std::fclose(f);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;%u scanned 123 
&nbsp;<wbr>&nbsp;%c scanned 'x'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character from a file stream 
fgetc <i>(function)</i> 
getc 
