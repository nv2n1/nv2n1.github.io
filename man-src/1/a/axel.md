---
title: "axel(1)"
name: "axel"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axel/"
description: "Axel – A light download accelerator for Linux."
---

<h2 class="name">NAME</h2>
<p> <code>Axel</code> &#8211; A light download accelerator for Linux.</p>
<h2>SYNOPSIS</h2>
<p> <code>axel</code> [<i>OPTIONS</i>] <i>url1</i> [<i>url2</i>] [<i>url&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> Axel is a program that downloads a file from a FTP or HTTP server through multiple connection, each connection downloads its own part of the file. </p>
<p> Unlike most other programs, Axel downloads all the data directly to the destination file, using one single thread. It just saves some time at the end because the program doesn&#8217;t have to concatenate all the downloaded parts. </p>
<h2>OPTIONS</h2>
<p> One argument is required, the URL to the file you want to download. When downloading from FTP, the filename may contain wildcards and the program will try to resolve the full filename. Multiple URL&#8217;s can be specified as well and the program will use all those URL&#8217;s for the download. Please note that the program does not check whether the files are equal. </p>
<p> Other options: </p>
<dl>
<dt><code>&#8211;max-speed=x</code>, <code>-s x</code></p>
<dd> You can specify a speed (bytes per second) here and Axel will try to keep the average speed around this speed. Useful if you don&#8217;t want the program to suck up all of your bandwidth. </p>
<dt><code>&#8211;num-connections=x</code>, <code>-n x</code></p>
<dd> You can specify an alternative number of connections here. </p>
<dt><code>&#8211;output=x</code>, <code>-o x</code></p>
<dd> Downloaded data will be put in a local file with the same name, unless you specify a different name using this option. You can specify a directory as well, the program will append the filename. </p>
<dt><code>&#8211;search[=x]</code>, <code>-S[x]</code></p>
<dd> Axel can do a search for mirrors using the filesearching.com search engine. This search will be done if you use this option. You can specify how many different mirrors should be used for the download as well. </p>
<p> The search for mirrors can be time-consuming because the program tests every server&#8217;s speed, and it checks whether the file&#8217;s still available. </p>
<dt><code>&#8211;no-proxy</code>, <code>-N</code></p>
<dd> Don&#8217;t use any proxy server to download the file. Not possible when a transparent proxy is active somewhere, of course. </p>
<dt><code>&#8211;verbose</code></p>
<dd> If you want to see more status messages, you can use this option. Use it more than once if you want to see more. </p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> No output to stdout. </p>
<dt><code>&#8211;alternate</code>, <code>-a</code></p>
<dd> This will show an alternate progress indicator. A bar displays the progress and status of the different threads, along with current speed and an estimate for the remaining download time. </p>
<dt><code>&#8211;header=x</code>, <code>-H x</code></p>
<dd> Add an additional HTTP header. This option should be in the form &quot;Header: Value&quot;. See RFC 2616 section 4.2 and 14 for details on the format and standardized headers. </p>
<dt><code>&#8211;user-agent=x</code>, <code>-U x</code></p>
<dd> Set the HTTP user agent to use. Some websites serve different content based upon this parameter. The default value will include &quot;Axel&quot;, its version and the platform. </p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> A brief summary of all the options. </p>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd> Get version information. </p>
</dl>
<h2>NOTE</h2>
<p> Long (double dash) options are supported only if your platform knows about the getopt_long call. If it does not (like *BSD), only the short options can be used. </p>
<h2>RETURN VALUE</h2>
<p> The program returns 0 when the download was succesful, 1 if something really went wrong and 2 if the download was interrupted. If something else comes back, it must be a bug.. </p>
<h2>EXAMPLES</h2>
<pre>
axel <a href="ftp://ftp.{be,nl,uk,de}.kernel.org/pub/linux/kernel/v2.4/linux-2.4.17.tar.bz2">ftp://ftp.{be,nl,uk,de}.kernel.org/pub/linux/kernel/v2.4/linux-2.4.17.tar.bz2</a>
</pre>
<p> This will use the Belgian, Dutch, English and German kernel.org mirrors to download a Linux 2.4.17 kernel image. </p>
<pre>
axel -S4 <a href="ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-2.4.17.tar.bz2">ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-2.4.17.tar.bz2</a>
</pre>
<p> This will do a search for the linux-2.4.17.tar.bz2 file on filesearching.com and it&#8217;ll use the four (if possible) fastest mirrors for the download. (Possibly including <a href="ftp://ftp.kernel.org">ftp.kernel.org</a>) </p>
<p> (Of course, the commands are a single line, but they&#8217;re too long to fit on one line in this page.) </p>
<h2>FILES</h2>
<p> <i>/etc/axelrc</i> System-wide configuration file. Note that development versions place this file in /usr/local/etc. </p>
<p> <i>~/.axelrc</i> Personal configuration file </p>
<p> These files are not documented in a man-page, but the example file which comes with the program contains enough information, I hope. The position of the system-wide configuration file might be different. </p>
<h2>COPYRIGHT</h2>
<p> Axel is Copyright 2001-2002 Wilmer van der Gaast. </p>
<h2>BUGS</h2>
<p> Please report bugs at <a rel="nofollow" href="https://alioth.debian.org/tracker/?group_id=100070">https://alioth.debian.org/tracker/?group_id=100070</a>&amp;atid=413085. </p>
<h2>AUTHORS</h2>
<p> Wilmer van der Gaast. &lt;wilmer [at] gaast.net&gt; </p>
<h2>Index</h2>
