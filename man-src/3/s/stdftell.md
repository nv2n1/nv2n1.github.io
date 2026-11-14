---
title: "stdftell(3)"
name: "stdftell"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdftell/"
---

std::ftell - std::ftell

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cstdio&gt;

long ftell( std::FILE* stream );</code></pre> 
Returns the current value of the file position indicator for the file stream stream. 
If the stream is open in binary mode, the value obtained by this function is the number of bytes from the beginning of the file. 
If the stream is open in text mode, the value returned by this function is unspecified and is only meaningful as the input to std::fseek 

<h2>Parameters</h2>

stream - file stream to examine

<h2>Return value</h2>

File position indicator on success or -1L if failure occurs. Also sets errno on failure. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the file position indicator 
fgetpos <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fseek <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fsetpos <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the input position indicator 
tellg <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the output position indicator 
tellp <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
