---
title: "xrdfs(1)"
name: "xrdfs"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdfs/"
description: "xrdfs – xrootd file and directory meta-data utility"
---

<h2>NAME</h2>
<p> xrdfs &#8211; xrootd file and directory meta-data utility</p>
<h2>SYNOPSIS</h2>
<pre><code>
xrdfs[--no - cwd] host[:port][command[args]] command : help, chmod, ls, locate, mkdir, mv, stat, statvfs, query, rm, rmdir, truncate, prepare, cat, tail, spaceinfo
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>xrdfs</code> utility executes meta-data oriented operations (e.g., ls, mv, rm, etc.) on one or more xrootd servers. Command help is available by invoking <code>xrdfs</code> with no command line options or parameters and then typing &quot;help&quot; in response to the input prompt. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;no-cwd</code></p>
<dl>
<dt>
<dd> No CWD is being preset in interactive mode. </p>
</dl>
<h2>COMMANDS</h2>
<p> <code>chmod</code> <i>path</i> <i>&lt;user&gt;&lt;group&gt;&lt;other&gt;</i></p>
<dl>
<dt>
<dd> Modify permissions of the <i>path</i>. Permission string example: <i>rwxr-x&#8211;x</i> </p>
</dl>
<p> <code>ls</code> <i>[-l]</i> <i>[-u]</i> <i>[dirname]</i></p>
<dl>
<dt>
<dd> Get directory listing.<br />
 <i>-l</i> stat every entry and pring long listing<br />
 <i>-u</i> print paths as URLs </p>
</dl>
<p> <code>locate</code> <i>[-n]</i> <i>[-r]</i> <i>[-d]</i> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> Get the locations of the path.<br />
 <i>-r</i> refresh, don&#8217;t use cached locations<br />
 <i>-n</i> make the server return the response immediately even though it may be incomplete<br />
 <i>-d</i> do a recursive, deep locate in order to find data servers<br />
 <i>-m</i> prefer host names to IP addresses<br />
 <i>-i</i> ignore network dependencies (IPv6/IPv4) </p>
</dl>
<p> <code>mkdir</code> <i>[-p] [-m&lt;user&gt;&lt;group&gt;&lt;other&gt;] &lt;dirname&gt;</i></p>
<dl>
<dt>
<dd> Creates a directory/tree of directories.<br />
 <i>-p</i> create the entire directory tree recursively<br />
 <i>-m</i><code>&lt;user&gt;&lt;group&gt;&lt;other&gt;</code> permissions for newly created directories </p>
</dl>
<p> <code>mv</code> <i>&lt;path1&gt; &lt;path2&gt;</i></p>
<dl>
<dt>
<dd> Move path1 to path2 locally on the same server. </p>
</dl>
<p> <code>stat</code> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> Get info about the file or directory.<br />
 <i>-q</i> query optional flag query parameter that makes xrdfs return error code to the shell if the requested flag combination is not present; flags may be combined together using &#8216;|&#8217; or &#8216;&amp;&#8217;<br />
 Available flags: <code>XBitSet</code>, <code>IsDir</code>, <code>Other</code>, <code>Offline</code>, <code>POSCPending</code>, <code>IsReadable</code>, <code>IsWriteable</code> </p>
</dl>
<p> <code>statvfs</code> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> Get info about a virtual file system. </p>
</dl>
<p> <code>query</code> <i>&lt;code&gt; &lt;params&gt;</i></p>
<dl>
<dt>
<dd> Obtain server information. Query codes:<br />
 <i>config</i> <code>&lt;what&gt;</code> Server configuration; &lt;what&gt; is one of the following:</p>
<dl>
<dt>
<dd> bind_max &#8211; the maximum number of parallel streams<br />
 chksum &#8211; the supported checksum<br />
 pio_max &#8211; maximum number of parallel I/O requests<br />
 readv_ior_max &#8211; maximum size of a readv element<br />
 readv_iov_max &#8211; maximum number of readv entries<br />
 tpc &#8211; support for third party copies<br />
 wan_port &#8211; the port to use for wan copies<br />
 wan_window &#8211; the wan_port window size<br />
 window &#8211; the tcp window size<br />
 cms &#8211; the status of the cmsd<br />
 role &#8211; the role in a cluster<br />
 sitename &#8211; the site name<br />
 version &#8211; the version of the server
</dl>
<p> <i>checksumcancel</i> <code>&lt;path&gt;</code> File checksum cancelation<br />
 <i>checksum</i> <code>&lt;path&gt;</code> File checksum<br />
 <i>opaque</i> <code>&lt;arg&gt;</code> Implementation dependent<br />
 <i>opaquefile</i> <code>&lt;arg&gt;</code> Implementation dependent<br />
 <i>space</i> <code>&lt;space&gt;</code> Logical space stats<br />
 <i>stats</i> <code>&lt;what&gt;</code> Server stats; &lt;what&gt; is a list of letters indicating information to be returned:</p>
<dl>
<dt>
<dd> a &#8211; all statistics<br />
 p &#8211; protocol statistics<br />
 b &#8211; buffer usage statistics<br />
 s &#8211; scheduling statistics<br />
 d &#8211; device polling statistics<br />
 u &#8211; usage statistics<br />
 i &#8211; server identification<br />
 z &#8211; synchronized statistics<br />
 l &#8211; connection statistics
</dl>
<p> <i>xattr</i> <code>&lt;path&gt;</code> Extended attributes </p>
</dl>
<p> <code>rm</code> <i>&lt;filename&gt;</i></p>
<dl>
<dt>
<dd> Remove a file. </p>
</dl>
<p> <code>rmdir</code> <i>&lt;dirname&gt;</i></p>
<dl>
<dt>
<dd> Remove a directory. </p>
</dl>
<p> <code>truncate</code> <i>&lt;filename&gt; &lt;length&gt;</i></p>
<dl>
<dt>
<dd> Truncate a file. </p>
</dl>
<p> <code>prepare</code> <i>[-c]</i> <i>[-f]</i> <i>[-s]</i> <i>[-w]</i> <i>[-p priority]</i> <i>filenames</i></p>
<dl>
<dt>
<dd> Prepare one or more files for access.<br />
 <i>-c</i> co-locate staged files if possible<br />
 <i>-f</i> refresh file access time even if the location is known<br />
 <i>-s</i> stage the files to disk if they are not online<br />
 <i>-w</i> whe files will be accessed for modification<br />
 <i>-p</i> priority of the request, 0 (lowest) &#8211; 3 (highest) </p>
</dl>
<p> <code>cat</code> <i>[-o localfile]</i> <i>file</i></p>
<dl>
<dt>
<dd> Print contents of a file to stdout<br />
 <i>-o</i> print to the specified local file </p>
</dl>
<p> <code>tail</code> <i>[-c bytes] [-f]</i> <i>file</i></p>
<dl>
<dt>
<dd> Output last part of files to stdout.<br />
 <i>-c</i> num_bytes out last num_bytes<br />
 <i>-f</i> output appended data as file grows </p>
</dl>
<p> <code>spaceinfo</code> <i>path</i></p>
<dl>
<dt>
<dd> Get space statistics for given path. </p>
</dl>
<h2>NOTES</h2>
<p> For the list of available environment variables please refere to <a href="/docs/linux/man/1-xrdcopy/">xrdcopy</a>(1) </p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status. </p>
<h2>LICENSE</h2>
<p> LGPL </p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xrdfs</code> command is supported by the XRootD Collaboration. Contact information can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
<h2>Index</h2>
