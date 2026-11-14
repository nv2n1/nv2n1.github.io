---
title: "munge(1)"
name: "munge"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munge/"
description: "munge – MUNGE credential encoder"
---

<h2 class="name">NAME</h2>
<p> munge &#8211; MUNGE credential encoder</p>
<h2>SYNOPSIS</h2>
<p> <code>munge</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>munge</code> program creates an MUNGE credential containing the UID and GID of the calling process. Additional payload data can be encapsulated in as well. The returned credential can be passed to another process which can validate its contents (e.g., via the <code>unmunge</code> program). This allows an unrelated and potentially remote process to ascertain the identity of the calling process. </p>
<p> By default, payload input is read from stdin and the credential is written to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a summary of the command-line options.</p>
<dt><code>-L, &#8211;license</code></p>
<dd> Display license information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-n, &#8211;no-input</code></p>
<dd> Discard all input for the payload.</p>
<dt><code>-s, &#8211;string </code><i>string</i></p>
<dd> Input payload from the specified string.</p>
<dt><code>-i, &#8211;input </code><i>file</i></p>
<dd> Input payload from the specified file.</p>
<dt><code>-o, &#8211;output </code><i>file</i></p>
<dd> Output the credential to the specified file.</p>
<dt><code>-c, &#8211;cipher </code><i>string</i></p>
<dd> Specify the cipher type, either by name or number.</p>
<dt><code>-C, &#8211;list-ciphers</code></p>
<dd> Display a list of supported cipher types.</p>
<dt><code>-m, &#8211;mac </code><i>string</i></p>
<dd> Specify the MAC type, either by name or number.</p>
<dt><code>-M, &#8211;list-macs</code></p>
<dd> Display a list of supported MAC types.</p>
<dt><code>-z, &#8211;zip </code><i>string</i></p>
<dd> Specify the compression type, either by name or number.</p>
<dt><code>-Z, &#8211;list-zips</code></p>
<dd> Display a list of supported compression types.</p>
<dt><code>-u, &#8211;restrict-uid </code><i>uid</i></p>
<dd> Specify the user name or UID allowed to decode the credential. This will be matched against the effective user ID of the process requesting the credential decode.</p>
<dt><code>-U, &#8211;uid </code><i>uid</i></p>
<dd> Specify the user name or UID under which to request the credential. This requires root privileges or the CAP_SETUID capability.</p>
<dt><code>-g, &#8211;restrict-gid </code><i>gid</i></p>
<dd> Specify the group name or GID allowed to decode the credential. This will be matched against the effective group ID of the process requesting the credential decode, as well as each supplementary group of which the effective user ID of that process is a member.</p>
<dt><code>-G, &#8211;gid </code><i>gid</i></p>
<dd> Specify the group name or GID under which to request the credential. This requires root privileges or the CAP_SETGID capability.</p>
<dt><code>-t, &#8211;ttl </code><i>integer</i></p>
<dd> Specify the time-to-live (in seconds). This controls how long the credential is valid once it has been encoded. A value of 0 selects the default TTL. A value of -1 selects the maximum allowed TTL.</p>
<dt><code>-S, &#8211;socket </code><i>path</i></p>
<dd> Specify the local domain socket for connecting with <code>munged</code>. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The <code>munge</code> program returns a zero exit code when the credential is successfully created and returned. On error, it prints an error message to stderr and returns a non-zero exit code. </p>
<h2>AUTHOR</h2>
<p> Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code> </p>
<h2>Index</h2>
