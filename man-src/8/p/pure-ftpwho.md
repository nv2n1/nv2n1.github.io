---
title: "pure-ftpwho(8)"
name: "pure-ftpwho"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-ftpwho/"
description: "pure-ftpwho – Report current FTP sessions"
---

<p>pure-ftpwho &#8211; Report current FTP sessions</p>
<h2>Syntax</h2>
<p>pure-ftpwho [<i>-c</i>] [<i>-h</i>] [<i>-H</i>] [<i>-n</i>] [<i>-p</i>] [<i>-s</i>] [<i>-v</i>] [<i>-w</i>] [<i>-W</i>] [<i>-x</i>]</p>
<h2>Description</h2>
<p>pure-ftpwho shows current Pure-FTPd client sessions. Only the system administrator may run this. Output can be text (default), HTML, XML data and parser-optimized. The server has to be compiled with <code>&#8211;with-ftpwho</code> to support this command.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>the program is called via a web server (CGI interface) . Output is a full HTML page with the initial content-type header. This option is automatically enabled if an environment variable called GATEWAY_INTERFACE is found. This is the default if you can the program from a CGI-enabled web server (Apache, Roxen, Caudium, WN, &#8230;) .</p>
<dt><code>-h</code></p>
<dd>Output help information and exit.</p>
<dt><code>-H</code></p>
<dd>Don&#8217;t resolve host names, and only show IP addresses (faster).</p>
<dt><code>-n</code></p>
<dd>A synonym for -H.</p>
<dt><code>-p</code></p>
<dd>Output Mac OSX / GNUStep plist data.</p>
<dt><code>-s</code></p>
<dd>Output only one line per client, with only numeric data, delimited by a | character. It&#8217;s not very human-readable, but it&#8217;s designed for easy parsing by shell scripts (cut/sed) . &#8216;|&#8217; characters in user names or file names are quoted (\|) .</p>
<dt><code>-v</code></p>
<dd>Output an ASCII table (just like the default mode), with more info. The verbose output includes the local IP, the local port, the total size of transfered files and the current number of transfered bytes.</p>
<dt><code>-w</code></p>
<dd>Output a complete HTML page (web mode).</p>
<dt><code>-W</code></p>
<dd>Output an HTML page with no header and no footer. This is an embedded mode, suitable for inline calls from CGI, SSI or PHP scripts.</p>
<dt><code>-x</code></p>
<dd>Output well-formed XML data for post-processing. </p>
</dl>
<h2>Files</h2>
<p><code>/var/run/pure-ftpd/</code> Scoreboard directory. Should always owned by root and on a lockable filesystem.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>GATEWAY_INTERFACE</code></p>
<dd>If found, automatically run in CGI mode and output HTML data. </p>
</dl>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2389,</code> <code>RFC 2228</code> and <code>RFC 2428</code>. </p>
