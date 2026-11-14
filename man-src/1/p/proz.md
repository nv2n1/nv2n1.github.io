---
title: "proz(1)"
name: "proz"
section: "1"
letter: "p"
url: "/docs/linux/man/1-proz/"
description: "ProZilla – a download accelerator for GNU/Linux"
---

<h2>NAME</h2>
<p> <code>ProZilla</code> &#8211; a download accelerator for GNU/Linux</p>
<h2>SYNTAX</h2>
<p> <code>proz [OPTIONS] &lt;URL&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ProZilla</code> is a download program that makes multiple connections and downloads a file in multiple parts from different servers simultaneously, thus enhancing the download speed and downloading the file faster than a download with a single connection. </p>
<p> ProZilla is able to do ftp searches for other possible sites that contain the same file, ping them for connection speeds and automatically download from the fastest sites. </p>
<p> FTP passwords can be specified with the URL, or can be obtained automatically from <code>~/.netrc</code> if it exists.</p>
<h2>Options:</h2>
<dl>
<dt>-r, &#8211;resume</p>
<dd> Resume an interrupted download</p>
<dt>-f, &#8211;force</p>
<dd> Never prompt the user when overwriting files</p>
<dt>-1</p>
<dd> Force a single connection only</p>
<dt>-n, &#8211;no-netrc</p>
<dd> Don&#8217;t use .netrc, get the user/password from the command line, otherwise use the anonymous login for FTP sessions</p>
<dt>&#8211;debug</p>
<dd> Log debugging info to a file (default is debug.log)</p>
<dt>-v,&#8211;verbose</p>
<dd> Increase the amount of information sent to stdout</p>
<dt>&#8211;no-curses</p>
<dd> Don&#8217;t use the Curses interface, but the traditional plain text interface</dl>
<h2>Directories:</h2>
<dl>
<dt>-P, &#8211;directory-prefix=DIR</p>
<dd> save the generated file to DIR/</dl>
<h2>FTP Options:</h2>
<dl>
<dt>&#8211;use-port</p>
<dd> Force usage of PORT insted of PASV (default) for ftp transactions</dl>
<h2>Download Options:</h2>
<dl>
<dt>-s, &#8211;ftpsearch</p>
<dd> Do a ftpsearch for faster mirrors</p>
<dt>&#8211;no-search</p>
<dd> Do a direct download (no ftpsearch)</p>
<dt>-k=n</p>
<dd> Use &lt;n&gt; connections instead of the <a href="/docs/linux/man/4-default/">default</a>(4)</p>
<dt>&#8211;timeout=n</p>
<dd> Set the timeout for connections to &lt;n&gt; seconds (default 180)</p>
<dt>-t, &#8211;tries=n</p>
<dd> Set number of attempts to n (default(200), 0=unlimited)</p>
<dt>&#8211;retry-delay=n</p>
<dd> Set the time between retrys to &lt;n&gt; seconds (default 15 seconds)</p>
<dt>&#8211;max-bps=n</p>
<dd> Limit bandwith consumed to &lt;n&gt; bps (0=unlimited)</dl>
<h2>FTP Search Options:</h2>
<dl>
<dt>&#8211;pt=n</p>
<dd> Wait 2*n seconds for a server response (default 2*4)</p>
<dt>&#8211;pao=n</p>
<dd> Ping n servers at once(default 5 servers at once)</p>
<dt>&#8211;max-ftps-servers=n</p>
<dd> Request a max of &lt;n&gt; servers from ftpsearch (default 40)</p>
<dt>&#8211;min-size=n</p>
<dd> If a file is smaller than &lt;n&gt;Kb, don&#8217;t search, just download it</p>
<dt>&#8211;ftpsid=n</p>
<dd> The ftpsearch server to use (0=filesearching.com, 1=ftpsearch.elmundo.es)</dl>
<h2>Information Options:</h2>
<dl>
<dt>-L, &#8211;license</p>
<dd> Display software license</p>
<dt>-V, &#8211;version</p>
<dd> Display version number</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>proz &lt;URL&gt;</p>
<dd> ProZilla will connect to that server and download the file using the default settings</p>
<dt>proz -1 &lt;URL&gt;</p>
<dd> ProZilla will connect and download the file in 1 part only</p>
<dt>proz -s &lt;URL&gt;</p>
<dd> invokes ftpsearch and will download from the fastest servers</p>
<dt>proz -s -k=10 &lt;URL&gt;</p>
<dd> invokes ftpsearch and will download from the fastest servers using 10 connections</dl>
<h2>GENTOO EXAMPLE</h2>
<dl>
<dt>FETCHCOMMAND=&#8217;/usr/local/bin/proz &#8211;no-curses &#8211;min-size=500 &#8211;no-getch -s ${URI} -P ${DISTDIR}&#8217;</p>
<dd> can be placed in /etc/make.conf to use ProZilla to download your system updates. This example will not do FTP searches for files &lt; 500Kb, uses the text interface (handier with portage) and saves the files in your ${DISTDIR} (normally /usr/portage/distfiles)</dl>
<h2>FILES</h2>
<dl>
<dt>&quot;/etc/prozilla.conf&quot;</p>
<dd> The global config file</p>
<dt>&quot;~/.prozrc&quot;</p>
<dd> The per-user config file</p>
<dt>&quot;~/.netrc&quot;</p>
<dd> A file which can be used to provide ProZilla with hosts, accounts and passwords</dl>
<h2>BUGS</h2>
<p> Please report bugs to our mailinglist via the website <a rel="nofollow" href="http://prozilla.genesys.ro/">http://prozilla.genesys.ro/</a> </p>
<h2>Index</h2>
