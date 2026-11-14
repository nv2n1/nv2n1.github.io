---
title: "stdfseek(3)"
name: "stdfseek"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfseek/"
---

std::fseek - std::fseek

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fseek(std::FILE *stream, long offset, int origin);</code></pre> 
Sets the file position indicator for the file stream stream. 
If the stream is open in binary mode, the new position is exactly offset bytes measured from the beginning of the file if origin is SEEK_SET, from the current file position if origin is SEEK_CUR, and from the end of the file if origin is SEEK_END. Binary streams are not required to support SEEK_END, in particular if additional null bytes are output. 
If the stream is open in text mode, the only supported values for offset are zero (which works with any origin) and a value returned by an earlier call to std::ftell on a stream associated with the same file (which only works with origin of SEEK_SET). 
If the stream is wide-oriented, the restrictions of both text and binary streams apply (result of std::ftell is allowed with SEEK_SET and zero offset is allowed from SEEK_SET and SEEK_CUR, but not SEEK_END) 
In addition to changing the file position indicator, fseek undoes the effects of std::ungetc and clears the end-of-file status, if applicable. 
If a read or write error occurs, the error indicator for the stream (std::ferror) is set and the file position is unaffected. 

<h2>Parameters</h2>

stream - file stream to modify 
offset - number of characters to shift the position relative to origin 
origin - position to which offset is added. It can have one of the following values: SEEK_SET, SEEK_CUR, SEEK_END

<h2>Return value</h2>

0 upon success, nonzero value otherwise. 

<h2>Notes</h2>

After seeking to a non-end position in a wide stream, the next call to any output function may render the remainder of the file undefined, e.g. by outputting a multibyte sequence of a different length. 
POSIX allows seeking beyond the existing end of file. If an output is performed after this seek, any read from the gap will return zero bytes. Where supported by the filesystem, this creates a sparse file. 
POSIX also requires that fseek first performs fflush if there are any unwritten data (but whether the shift state is restored is implementation-defined). The standard C++ file streams guarantee both flushing and unshifting: std::basic_filebuf::seekoff 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;cstdint&gt;

#include &lt;vector&gt;

#include &lt;fstream&gt;

#include &lt;cassert&gt;
int main()

{
    std::ofstream(&quot;dummy.nfo&quot;) &lt;&lt; &quot;sample data\n&quot;;

    std::FILE *fp = std::fopen(&quot;dummy.nfo&quot;, &quot;rb&quot;);
    assert(fp);
    std::fseek(fp, 0, SEEK_END); // seek to end
    std::size_t filesize = std::ftell(fp);
    std::fseek(fp, 0, SEEK_SET); // seek to start
    std::vector&lt;uint8_t&gt; buffer(filesize);
    std::fread(buffer.data(), sizeof(uint8_t), buffer.size(), fp);
    std::fclose(fp);
    std::printf(&quot;i've read %zi bytes\n&quot;, filesize);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;i've read 12 bytes

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fsetpos <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the file position indicator 
fgetpos <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current file position indicator 
ftell <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to the beginning in a file 
rewind <i>(function)</i> 
