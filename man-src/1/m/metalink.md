---

title: "metalink(1)"
name: "metalink"
section: "1"
letter: "m"
url: "/docs/linux/man/1-metalink/"
description: "metalink — commandline metalink generator"
---

<h2>NAME</h2>
<p> metalink &#8212; commandline metalink generator</p>
<p> <code>metalink</code> [<i>input files</i>] [ &lt; <i>mirror list</i>]</p>
<p> This manual page documents briefly the <code>metalink</code> command. </p>
<p> This manual page was written for the <code>Debian</code> distribution because the original program does not have a manual page. </p>
<p> <code>metalink</code> allows you to generate metalinks from a list of mirrors and a collection of files. The files are hashed and the resulting metalink is generated on the stdout.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> Produce a help message</dd>
<dt> <code>&#8211;version</code></dt>
<dd> Print out the name and version.</dd>
<dt> <code>&#8211;md5</code></dt>
<dd> Generate metalink from md5sum file(s).</dd>
<dt> <code>&#8211;addpath path</code></dt>
<dd> Append a path to the mirrors (&#8216;/&#8217; is not checked)</dd>
<dt> <code>&#8211;headerfile arg</code></dt>
<dd> Include file after the root element declaration.</dd>
<dt> <code>&#8211;nomirrors</code></dt>
<dd> Don&#8217;t read mirrors from stdin</dd>
<dt> <code>&#8211;hashlist</code></dt>
<dd> List hashes only (implies nomirrors)</dd>
<dt> <code>&#8211;desc arg</code></dt>
<dd> Add metalink description</dd>
<dt> <code>-d arg</code></dt>
<dd> Include given digest</dd>
<dt> <code>&#8211;mindigests</code></dt>
<dd> Include: md5 sha1</dd>
<dt> <code>&#8211;somedigests</code></dt>
<dd> Include: md5 sha1 ed2k</dd>
<dt> <code>&#8211;alldigests</code></dt>
<dd> Include all possible digests</dd>
</dl>
<p> Supported algorithms are (-d options): md4 md5 sha1 sha256 sha384 sha512 rmd160 tiger crc32 ed2k gnunet sha1pieces </p>
<p> Mirror lists are single line definitions according to: [location [preference] [type] % ] mirror base url</p>
<h2>EXAMPLES</h2>
<p> <a rel="nofollow" href="http://example.com/">http://example.com/</a> as a mirror: echo <a rel="nofollow" href="http://example.com">http://example.com</a> | metalink -d md5 -d sha1 *<br />
&nbsp;<wbr> </p>
<p> <a rel="nofollow" href="http://example.com/">http://example.com/</a> as a mirror with preference and location: echo us 10 % <a rel="nofollow" href="http://example.com">http://example.com</a> | metalink -d md5 -d sha1 * </p>
<p> <a rel="nofollow" href="http://example.com/">http://example.com/</a> as a mirror with preference only: echo 0 10 % <a rel="nofollow" href="http://example.com">http://example.com</a> | metalink -d md5 *</p>
<h2>AUTHOR</h2>
<p> This manual page was written by A. Bram Neijt bneijt [at] gmail.com for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.<br />
&nbsp;<wbr> </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.<br />
&nbsp;<wbr> </p>
