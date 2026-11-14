---
title: "stdungetwc(3)"
name: "stdungetwc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdungetwc/"
---

std::ungetwc - std::ungetwc

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwchar&gt;

wint_t ungetwc( wint_t ch, std::FILE* stream );</code></pre> 
If ch does not equal WEOF, pushes the wide character ch into the input buffer associated with the stream stream in such a manner than subsequent read operation from stream will retrieve that wide character. The external device associated with the stream is not modified. 
Stream repositioning operations std::fseek, std::fsetpos, and std::rewind discard the effects of ungetwc. 
If ungetwc is called more than once without an intervening read or repositioning, it may fail (in other words, a pushback buffer of size 1 is guaranteed, but any larger buffer is implementation-defined). If multiple successful ungetwc were performed, read operations retrieve the pushed-back wide characters in reverse order of ungetwc 
If ch equals WEOF, the operation fails and the stream is not affected. 
A successful call to ungetwc clears the end of file status flag feof. 
A successful call to ungetwc on a stream (whether text or binary) modifies the stream position indicator in unspecified manner but guarantees that after all pushed-back wide characters are retrieved with a read operation, the stream position indicator is equal to its value before ungetwc. 

<h2>Parameters</h2>

ch - wide character to be put back 
stream - file stream to put the wide character back to

<h2>Return value</h2>

On success ch is returned. 
On failure WEOF is returned and the given stream remains unchanged. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts a character back into a file stream 
ungetc <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a wide character from a file stream 
fgetwc <i>(function)</i> 
getwc 
