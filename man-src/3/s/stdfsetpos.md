---
title: "stdfsetpos(3)"
name: "stdfsetpos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfsetpos/"
---

std::fsetpos - std::fsetpos

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fsetpos(std::FILE *stream, const std::fpos_t *pos);</code></pre> 
Sets the file position indicator and the multibyte parsing state (if any) for the C file stream stream according to the value pointed to by pos. 
Besides establishing new parse state and position, a call to this function undoes the effects of std::ungetc and clears the end-of-file state, if it is set. 
If a read or write error occurs, the error indicator (std::ferror)for the stream is set. 

<h2>Parameters</h2>

stream - file stream to modify 
pos - pointer to a fpos_t object obtained from std::fgetpos called on a stream associated with the same file

<h2>Return value</h2>

0 upon success, nonzero value otherwise. Also, sets errno on failure. 

<h2>Notes</h2>

After seeking to a non-end position in a wide stream, the next call to any output function may render the remainder of the file undefined, e.g. by outputting a multibyte sequence of a different length. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the file position indicator 
fgetpos <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current file position indicator 
ftell <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fseek <i>(function)</i> 
