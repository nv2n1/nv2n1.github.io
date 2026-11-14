---
title: "streamzip(1)"
name: "streamzip"
section: "1"
letter: "s"
url: "/docs/linux/man/1-streamzip/"
---

<h2 class="name">NAME</h2>
 

 streamzip - create a zip file from stdin 

<h2>SYNOPSIS</h2>

 <pre><code>
producer | streamzip[opts] | consumer producer | streamzip[opts] - zipfile = output.zip
</code></pre>

<h2>DESCRIPTION</h2>

 This program will read data from <tt>&quot;stdin&quot;</tt>, compress it into a zip container and, by default, write a <i>streamed</i> zip file to <tt>&quot;stdout&quot;</tt>. No temporary files are created. 

 The zip container written to <tt>&quot;stdout&quot;</tt> is, by necessity, written in streaming format. Most programs that read Zip files can cope with a streamed zip file, but if interoperability is important, and your workflow allows you to write the zip file directly to disk you can create a non-streamed zip file using the <tt>&quot;zipfile&quot;</tt> option.

<h3><font SIZE="-1">OPTIONS</font></h3>

<dl>
<dt>-zip64
<dd> Create a Zip64-compliant zip container. Use this option if the input is greater than 4Gig. 

 Default is disabled.
<dt>-zipfile=F
<dd> Write zip container to the filename <tt>&quot;F&quot;</tt>. 

 Use the <tt>&quot;Stream&quot;</tt> option to force the creation of a streamed zip file.
<dt>-member-name=M
<dd> This option is used to name the ``file'' in the zip container. 

 Default is '-'.
<dt>-stream
<dd> Ignored when writing to <tt>&quot;stdout&quot;</tt>. 

 If the <tt>&quot;zipfile&quot;</tt> option is specified, including this option will trigger the creation of a streamed zip file. 

 Default: Always enabled when writing to <tt>&quot;stdout&quot;</tt>, otherwise disabled.
<dt>-method=M
<dd> Compress using method <tt>&quot;M&quot;</tt>. 

 Valid method names are 

 <pre>
    * store    Store without compression
    * deflate  Use Deflate compression [Deflault]
    * bzip2    Use Bzip2 compression
    * lzma     Use LZMA compression
    * xz       Use xz compression
    * zstd     Use Zstandard compression
</pre> 

 Note that Lzma compress needs <tt>&quot;IO::Compress::Lzma&quot;</tt> to be installed. 

 Note that Zstd compress needs <tt>&quot;IO::Compress::Zstd&quot;</tt> to be installed. 

 Default is <tt>&quot;deflate&quot;</tt>.
<dt>-0, -1, -2, -3, -4, -5, -6, -7, -8, -9
<dd> Sets the compression level for <tt>&quot;deflate&quot;</tt>. Ignored for all other compression methods. 

 <tt>&quot;-0&quot;</tt> means no compression and <tt>&quot;-9&quot;</tt> for maximum compression. 

 Default is 6
<dt>-version
<dd> Display version number
<dt>-help
<dd> Display help</dl>

<h3>Examples</h3>

 Create a zip file bt reading daa from stdin 

 <pre>
    $ echo Lorem ipsum dolor sit | perl ./bin/streamzip &gt;abcd.zip
</pre> 

 Check the contents of <tt>&quot;abcd,zip&quot;</tt> with the standard <tt>&quot;unzip&quot;</tt> utility 

 
Archive : abcd.zip
              Length Date Time Name-- -- -- -- - -- -- -- -- -- -- -- - -- --22 2021 -
    01 - 08 19 : 45 -
    -- -- -- -- - -- -- -- -22 1 file
 

 Notice how the <tt>&quot;Name&quot;</tt> is set to <tt>&quot;-&quot;</tt>. That is the default for a few zip utilities whwre the member name is not given. 

 If you want to explicitly name the file, use the <tt>&quot;-member-name&quot;</tt> option as follows 

 <pre><code>
$ echo Lorem ipsum dolor sit | perl./ bin / streamzip - member - name latin &gt; abcd.zip
                                                                                      $ unzip -
                                                                                  l abcd.zip
                                                                                      Archive : abcd.zip
                                                                                                    Length Date Time Name-- -- -- -- - -- -- -- -- -- -- -- - -- --22 2021 -
                                                                                  01 - 08 19 : 47 latin-- -- -- -- - -- -- -- -22 1 file
</code></pre>

<h3>When to write a Streamed Zip File</h3>

 A Streamed Zip File is useful in situations where you cannot seek backwards/forwards in the file. 

 A good examples is when you are serving dynamic content from a Web Server straight into a socket without needing to create a temporary zip file in the filesystsm. 

 Similarly if your workfow uses a Linux pipelined commands.

<h2>SUPPORT</h2>

 General feedback/questions/bug reports should be sent to &lt;<a rel="nofollow" HREF="https://github.com/pmqs/IO-Compress/issues">https://github.com/pmqs/IO-Compress/issues</a>&gt; (preferred) or &lt;<a rel="nofollow" HREF="https://rt.cpan.org/Public/Dist/Display.html?Name=IO-Compress">https://rt.cpan.org/Public/Dist/Display.html?Name=IO-Compress</a>&gt;.

<h2>AUTHOR</h2>

 Paul Marquess <i>pmqs [at] cpan.org</i>.

<h2>COPYRIGHT</h2>

 Copyright (c) 2019-2021 Paul Marquess. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>



<dt><a HREF="#lbAH">SUPPORT</a>
<dd>
<dt><a HREF="#lbAI">AUTHOR</a>
<dd>
<dt><a HREF="#lbAJ">COPYRIGHT</a>
<dd></dl>
