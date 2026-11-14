---
title: "stdfreopen(3)"
name: "stdfreopen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfreopen/"
---

std::freopen - std::freopen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    std::FILE *freopen(const char *filename, const char *mode, std::FILE *stream);</code></pre> 
First, attempts to close the file associated with stream, ignoring any errors. Then, if filename is not null, attempts to open the file specified by filename using mode as if by fopen, and associates that file with the file stream pointed to by stream. If filename is a null pointer, then the function attempts to reopen the file that is already associated with stream (it is implementation defined which mode changes are allowed in this case) 

<h2>Parameters</h2>

filename - file name to associate the file stream to 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;null-terminated character string determining new file access mode 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access Meaning Explanation Action if file Action if file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode string already exists does not exist 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;r&quot; read Open a file for reading read from start failure to open 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;w&quot; write Create a file for writing destroy contents create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;a&quot; append Append to a file write to end create new 
mode - &quot;r+&quot; read extended Open a file for read/write read from start error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;w+&quot; write extended Create a file for read/write destroy contents create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;a+&quot; append extended Open a file for read/write write to end create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access mode flag &quot;b&quot; can optionally be specified to open a file in_binary_mode. This flag has no effect on POSIX systems, but on Windows, for example, it disables special handling of '\n' and 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;'\x1A'. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;On the append file access modes, data is written to the end of the file regardless of the current position of the file position indicator. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access mode flag &quot;x&quot; can optionally be appended to &quot;w&quot; or &quot;w+&quot; specifiers. This flag forces the function to fail if the file exists, instead of overwriting it. <i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The behavior is undefined if the mode is not one of the strings listed above. Some implementations define additional supported modes (e.g. Windows). 

 
stream - the file stream to modify

<h2>Return value</h2>

stream on success, NULL on failure 

<h2>Notes</h2>

freopen is the only way to change the narrow/wide orientation of a stream once it has been established by an I/O operation or by std::fwide. 

<h2>Example</h2>

The following code redirects stdout to a file 
 // Run this code <pre><code>#include &lt;cstdio&gt;
int main()

{
    std::printf(&quot;stdout is printed to console\n&quot;);
    if (std::freopen(&quot;redir.txt&quot;, &quot;w&quot;, stdout)) {
        std::printf(&quot;stdout is redirected to a file\n&quot;); // this is written to redir.txt
        std::fclose(stdout);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;stdout is printed to console

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;opens a file 
fopen <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;closes a file 
fclose <i>(function)</i> 
