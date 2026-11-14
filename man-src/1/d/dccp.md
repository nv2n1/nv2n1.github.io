---
title: "dccp(1)"
name: "dccp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dccp/"
description: "dccp – Copy a file from or to a dCache server."
---

<h2>Name</h2>
<p> dccp &#8211; Copy a file from or to a dCache server. </p>
<h2>Synopsis</h2>
<p> dccp [option&#8230;] &lt;sourceUrl&gt; &lt;destUrl&gt; </p>
<h2>Arguments</h2>
<p> The following arguments are required: </p>
<p> <code>sourceUrl </code> </p>
<dl>
<dt>
<dd> The URL of the source file.</dl>
<p> <code>destUrl</code> </p>
<dl>
<dt>
<dd> The URL of the destination file.</dl>
<h2>Description</h2>
<p> The dccp utility provides a <a href="/docs/linux/man/1-cp/">cp</a>(1) like functionality on the dCache file system. The source must be a single file while the destination could be a directory name or a file name. If the directory is a destination, a new file with the same name as the source name will be created there and the contents of the source will be copied. If the final destination file exists in dCache, it won’t be overwritten and an error code will be returned. Files in regular file systems will always be overwritten if the -i option is not specified. If the source and the final destination file are located on a regular file system, the dccp utility can be used similar to the <a href="/docs/linux/man/1-cp/">cp</a>(1) program. </p>
<h2>Options</h2>
<p> The following arguments are optional: </p>
<p> -a</p>
<dl>
<dt>
<dd> Enable read-ahead functionality.</dl>
<p> -b &lt;bufferSize&gt; </p>
<dl>
<dt>
<dd> Set read-ahead buffer size. The default value is 1048570 Bytes. To disable the buffer this can be set to any value below the default. dccp will attempt to allocate the buffer size so very large values should be used with care.</dl>
<p> -B &lt;bufferSize&gt; </p>
<dl>
<dt>
<dd> Set buffer size. The size of the buffer is requested in each request, larger buffers will be needed to saturate higher bandwidth connections. The optimum value is network dependent. Too large a value will lead to excessive memory usage, too small a value will lead to excessive network communication.</dl>
<p> -d &lt;debug level&gt; </p>
<dl>
<dt>
<dd> Set the debug level. &lt;debug level&gt; is a integer between 0 and 127. If the value is 0 then no output is generated, otherwise the value is formed by adding together one or more of the following values:</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>Value<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Enabled output</p>
<p>&nbsp;<wbr>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Error messages</p>
<p>&nbsp;<wbr>2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Info messages</p>
<p>&nbsp;<wbr>4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Timing information</p>
<p>&nbsp;<wbr>8<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Trace information</p>
<p>&nbsp;<wbr>16<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Show stack-trace</p>
<p>&nbsp;<wbr>32<tt>&nbsp;<wbr>&nbsp;<wbr></tt>IO operations</p>
<p>&nbsp;<wbr>32<tt>&nbsp;<wbr>&nbsp;<wbr></tt>IO operations</p>
<p>&nbsp;<wbr>64<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Thread information
</dl>
<p> -h &lt;replyHostName&gt; </p>
<dl>
<dt>
<dd> Bind the callback connection to the specific hostname interface.</dl>
<p> -H </p>
<dl>
<dt>
<dd> show progress during file transfer.</dl>
<p> -i </p>
<dl>
<dt>
<dd> Secure mode. Do not overwrite the existing files.</dl>
<p> -l &lt;location&gt; </p>
<dl>
<dt>
<dd> Set location for pre-stage. if the location is not specified, the local host of the door will be used. This option must be used with the -P option.</dl>
<p> -p &lt;first_port&gt;:&lt;last_port&gt; </p>
<dl>
<dt>
<dd> Bind the callback data connection to the specified TCP port/rangeSet port range. Delimited by the ’:’ character, the &lt;first_port&gt; is required but the &lt;last_port&gt; is optional.</dl>
<p> -P </p>
<dl>
<dt>
<dd> Pre-stage. Do not copy the file to a local host but make sure the file is on disk on the dCache server.</dl>
<p> -r &lt;bufferSize&gt; </p>
<dl>
<dt>
<dd> TCP receive buffer size. The default is 256K. Setting to 0 uses the system default value. Memory useage will increase with higher values, but performance better.</dl>
<p> -s &lt;bufferSize&gt; </p>
<dl>
<dt>
<dd> TCP send buffer size. The default is 256K. Setting to 0 uses the system default value.</dl>
<p> -t &lt;time&gt; </p>
<dl>
<dt>
<dd> Stage timeout in seconds. This option must be used with the -P option.</dl>
<h2>Examples:</h2>
<p> To copy a file to dCache: </p>
<dl>
<dt>
<dd> [user] $ dccp /etc/group <a href="dcap://example.org/pnfs/desy.de/gading/">dcap://example.org/pnfs/desy.de/gading/</a></dl>
<p> To copy a file from dCache: </p>
<dl>
<dt>
<dd> [user] $ dccp <a href="dcap://example.org/pnfs/desy.de/gading/group">dcap://example.org/pnfs/desy.de/gading/group</a> /tmp/</dl>
<p> Pre-Stage request: </p>
<dl>
<dt>
<dd> [user] $ dccp -P -t 3600 -l example.org /acs/user_space/data_file</dl>
<p> stdin: </p>
<dl>
<dt>
<dd> [user] $ tar cf &#8211; data_dir | dccp &#8211; /acs/user_space/data_arch.tar</dl>
<p> stdout: </p>
<dl>
<dt>
<dd> [user] $ dccp /acs/user_space/data_arch.tar &#8211; | tar xf &#8211;</dl>
<h2>See also</h2>
<p> cp </p>
<h2>Index</h2>
