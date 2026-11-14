---
title: "xprep(1)"
name: "xprep"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xprep/"
description: "xprep – prepare one or more files for access"
---

<h2>NAME</h2>
<p> xprep &#8211; prepare one or more files for access</p>
<h2>SYNOPSIS</h2>
<pre><code>
xprep[options] target[paths] options : [-d n][-f fn][-p prty][-s][-S][-w] target : host[:port][, target] paths : path[paths]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>xprep</code> utility prepares one or more files for subsequent access by an application. Usage synopsis can be displayed by typing &quot;<code>xprep</code>&quot;. Currently, only the usage synopsis is available as documentation.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code> <i>lvl</i></p>
<dl>
<dt>
<dd> debug level: 1 (low), 2 (medium), 3 (high) </p>
</dl>
<p> <code>-f</code> <i>fname</i></p>
<dl>
<dt>
<dd> specifies that the file, <i>fname</i>, contains the list of files to prepare. Each file name must be on a separate line. </p>
</dl>
<p> <code>-p </code><i>prty</i></p>
<dl>
<dt>
<dd> schedule the request the the specified priority, <i>prty</i>. The lowest priority is 0.<br />
&nbsp;<wbr>Depending on the system configuration, priorities may or may not be honored. </p>
</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> requests that the file be copied into the cluster should it not be found online (i.e. stage). Depending on the system configuration, staging may or may not be honored. </p>
</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> requests that the file be copied into the cluster should it not be found on the same server as the first file in the specified list of files When the file is copied it is co-located with the first file in the list of files, if sufficient space exists on the target server. Depending on the system configuration, co-location may or may not be honored. </p>
</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> when staging or co-locating the file, copy the file to a space that allows file modification (i.e. the file will be modified). Depending on the system configuration, stage to writable space may or may not be honored. </p>
</dl>
<h2>OPERANDS</h2>
<p> <i>target</i></p>
<dl>
<dt>
<dd> is the redirector&#8217;s hostname and optional port number where the prepare is to occur. If the prepare is to occur on more than one redirector, specified each one separated by a comma. </p>
</dl>
<p> <i>paths</i></p>
<dl>
<dt>
<dd> are the files to be prepared. Specify one or more files separated by a space. to occur. If the prepare is to occur on more than one redirector, specified each one separated by a comma. If fB-f is specified, you need not specify any files on the command line. Files specified on the command line are always processed first. </p>
</dl>
<h2>NOTES</h2>
<p> Unless the <code>-s</code> or <code>-S</code> option is specified, file preparation merely seeds the redirector&#8217;s location cache. This allows the look-ups for prepared files to progress much faster in the future. </p>
<p> Documentation for all components associated with <code>xprep</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status.</p>
<h2>LICENSE</h2>
<p> License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xprep</code> command is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
<h2>Index</h2>
