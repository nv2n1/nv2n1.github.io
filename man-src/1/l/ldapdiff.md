---
title: "ldapdiff(1)"
name: "ldapdiff"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapdiff/"
description: "ldapdiff – Tool to synchronize ldap servers using ldif formatted input files"
---

<h2 class="name">NAME</h2>
<p> ldapdiff &#8211; Tool to synchronize ldap servers using ldif formatted input files </p>
<h2>SYNOPSIS</h2>
<p> <code>ldapdiff</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>ldapdiff</code> combines classical &quot;diff&quot; and &quot;patch&quot; functionality in one application. the difference is, that <code>ldapdiff</code> is not designed for use on flat ascii files, it is designed for &quot;patching&quot; ldap directories using ldif files. </p>
<p> This manual page was written for the Debian distribution because the original program does not have a manual page.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c conffile</code></p>
<dd> Name of the configuration file. Default: ./ldapdiff.conf</p>
<dt><code>-f ldiffile</code></p>
<dd> ldif input file to be compared to the running server. If this option is not set, stdin will be used.</p>
<dt><code>-l logfile</code></p>
<dd> Name of the logfile. Default: stdout</p>
<dt><code>-p profile</code></p>
<dd> Name of the profile to use from the configuration file.</p>
<dt><code>-s local[0-7]</code></p>
<dd> Log to syslog.</p>
<dt><code>-v</code></p>
<dd> Show version of program. </p>
</dl>
<h2>RETURN VALUES</h2>
<p> <code>0 </code> -&gt; ok </p>
<p> <code>1 </code> -&gt; error </p>
<p> <code>2 </code> -&gt; an online modification error (insert,update,delete) occured </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldapcompare/">ldapcompare</a></code>(1). </p>
<p> The README file of the source distribution contains detailed information about the various parameters for the config file ldapdiff.conf. </p>
<h2>COPYRIGHT</h2>
<p> Copyright 2000-2006 Free Software Foundation, Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>AUTHOR</h2>
<p> ldapdiff was written by Thomas.Reith [at] rhoen.de </p>
<p> This manual page was written by Jeff Waugh &lt;jdub [at] perkypants.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
