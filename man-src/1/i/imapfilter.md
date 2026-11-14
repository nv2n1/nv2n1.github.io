---
title: "imapfilter(1)"
name: "imapfilter"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imapfilter/"
description: "imapfilter – mail filter"
---

<h2>NAME</h2>
<p> <code>imapfilter</code> &#8211; mail filter</p>
<h2>SYNOPSIS</h2>
<p> [-<code>iVv </code>[-<code>c </code><i>configfile</i> ] ] [-<code>d </code><i>debugfile</i> ] [-<code>e </code><i>&#8216;command&#8217;</i> ] [-<code>l </code><i>logfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a mail filtering utility. It connects to remote mail servers using the Internet Message Access Protocol (IMAP), sends searching queries to the server and processes mailboxes based on the results. It can be used to delete, copy, move, flag, etc. messages residing in mailboxes at the same or different mail servers. The 4rev1 and 4 versions of the IMAP protocol are supported. </p>
<p> The command line options of <a href="/docs/linux/man/1-imapfilter/">imapfilter</a>(1) are as follows:</p>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd> Path to the configuration file to read, or the `-&#8216; character to read the configuration from the standard input stream. The default is $HOME/.imapfilter/config.lua</p>
<dt><code>-d </code><i>debugfile</i></p>
<dd> File that contains debugging information about the full communication with the server, along with other inner workings&#8217; details.</p>
<dt><code>-e </code><i>&#8216;command&#8217;</i></p>
<dd> May be used to enter &#8220;one line&#8221; of configuration, while it is also possible to pipe a full configuration as a string. When this options is used, a configuration file will not be loaded.</p>
<dt><code>-i</code></p>
<dd> Enters interactive mode after executing the configuration file.</p>
<dt><code>-l </code><i>logfile</i></p>
<dd> File that contains logs of error messages produced.</p>
<dt><code>-V</code></p>
<dd> Displays version and copyright information.</p>
<dt><code>-v</code></p>
<dd> Enables printing of some brief details of the communication with the server.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> User&#8217;s home directory.</p>
<dt><code>IMAPFILTER_HOME</code></p>
<dd> Program&#8217;s configuration directory, which overrides the default $HOME/.imapfilter/</dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.imapfilter/config.lua </code></p>
<dd> Default configuration file. Because this file may contain sensitive data such as user passwords, the recommended permissions are read/write for the user, and not accessible by others.</p>
<dt><code>$HOME/.imapfilter/certificates </code></p>
<dd> File where the SSL/TLS certificates are stored.</dl>
<h2>SEE ALSO</h2>
<p> imapfilter_config5</p>
<h2>CONFORMING TO</h2>
<dl>
<dt><code>IMAP4rev1:</code></p>
<dd> RFC 3501, RFC 3348, RFC 2683, RFC 2595, RFC 2342, RFC 2195, RFC 2177</p>
<dt><code>IMAP4:</code></p>
<dd> RFC 1730</dl>
<h2>Index</h2>
