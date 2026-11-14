---
title: "stdfflush(3)"
name: "stdfflush"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfflush/"
---

std::fflush - std::fflush

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fflush(std::FILE *stream);</code></pre> 
For output streams (and for update streams on which the last operation was output), writes any unwritten data from the stream's buffer to the associated output device. 
For input streams (and for update streams on which the last operation was input), the behavior is undefined. 
If stream is a null pointer, all open output streams are flushed, including the ones manipulated within library packages or otherwise not directly accessible to the program. 

<h2>Parameters</h2>

stream - the file stream to write out

<h2>Return value</h2>

Returns zero on success. Otherwise EOF is returned and the error indicator of the file stream is set. 

<h2>Notes</h2>

POSIX extends_the_specification_of_fflush by defining its effects on an input stream, as long as that stream represents a file or another seekable device: in that case the POSIX file pointer is repositioned to match the C stream pointer (which effectively undoes any read buffering) and the effects of any std::ungetc or std::ungetwc that weren't yet read back from the stream are discarded. 
Microsoft also extends the specification of fflush by defining its effects on an input stream: in Visual Studio 2013 and prior, it discarded_the_input_buffer, in Visual Studio 2015 and newer, it has_no_effect,_buffers_are_retained. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;opens a file 
fopen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;closes a file 
fclose <i>(function)</i> 
