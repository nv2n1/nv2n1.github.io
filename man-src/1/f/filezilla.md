---
title: "filezilla(1)"
name: "filezilla"
section: "1"
letter: "f"
url: "/docs/linux/man/1-filezilla/"
description: "FileZilla – FTP client"
---

<h2>NAME</h2>
<p> FileZilla &#8211; FTP client</p>
<h2>SYNOPSIS</h2>
<p> <code>filezilla</code><br />
 <code>filezilla [-l &lt;logontype&gt;] &lt;FTP URL&gt;</code><br />
 <code>filezilla -h|-s|-v</code><br />
 <code>filezilla -c &lt;site&gt;</code><br />
 <code>filezilla -a &lt;path&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> FileZilla is a powerful client for plain FTP, FTP over SSL/TLS (FTPS) and the SSH File Transfer Protocol (SFTP).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &lt;site&gt;, &#8211;site &lt;site&gt;</code></p>
<dd> Connect to the given site from the Site Manager. Site has to be given as complete path, with a slash as separation character. Any slash or backslash that is part of a segment has to be escaped with a backslash. Path has to be prefixed with 0 for user defined entries or 1 for default entries. Site path may not contain double quotation marks.</p>
<dt>
<dd> Example: filezilla -c 0/foo/bar/sl\/ash connects to the user site sl/ash in the site directory foo/bar</p>
<dt>
<dd> May not be used together with <code>-s</code> nor with URL parameter. </p>
<dt><code>-a &lt;path&gt;, &#8211;local &lt;path&gt;</code></p>
<dd> Sets the local site to the given path.</p>
<dt>
<dd> Example: filezilla -a &quot;/foo bar/&quot; </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a help dialog listing these commandline options. </p>
<dt><code>-l &lt;logontype&gt;, &#8211;logontype &lt;logontype&gt;</code></p>
<dd> Set a special logontype, can only be used in combination with a FTP URL as argument. </p>
<p> Logontype has to be either <code>ask</code> or <code>interactive</code>. If <code>-l</code> isn&#8217;t given, the normal logontype is used. </p>
<dt><code>-s, &#8211;sitemanager</code></p>
<dd> Start with Site Manager opened. May not be used together with <code>-c</code> nor with URL parameter. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version number of FileZilla. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>FZ_DATADIR</code> environment variable can be used to specify the directory containing FileZilla&#8217;s data files.</p>
<h2>SUPPORT</h2>
<p> Please visit <a rel="nofollow" href="https://filezilla-project.org/">https://filezilla-project.org/</a> for further information. Report bugs only if you are using the latest version available from the FileZilla website.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004-2014 Tim Kosse </p>
<p> FileZilla is distributed under the terms of the GNU General Public License version 2 or later.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-fzdefaults-xml/">fzdefaults.xml</a>(5) </p>
<h2>Index</h2>
