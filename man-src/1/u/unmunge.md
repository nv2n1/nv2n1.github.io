---
title: "unmunge(1)"
name: "unmunge"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unmunge/"
description: "unmunge – MUNGE credential decoder"
---

<h2 class="name">NAME</h2>
<p> unmunge &#8211; MUNGE credential decoder</p>
<h2>SYNOPSIS</h2>
<p> <code>unmunge</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>unmunge</code> program validates a MUNGE credential (e.g., one created by the <code>munge</code> program). </p>
<p> By default, the credential is read from stdin and the metadata and payload are written to stdout. When the metadata and payload are written to the same stream, they are separated by a blank line. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a summary of the command-line options.</p>
<dt><code>-L, &#8211;license</code></p>
<dd> Display license information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-i, &#8211;input </code><i>file</i></p>
<dd> Input the credential from the specified file.</p>
<dt><code>-n, &#8211;no-output</code></p>
<dd> Discard all output.</p>
<dt><code>-m, &#8211;metadata </code><i>file</i></p>
<dd> Output metadata to the specified file.</p>
<dt><code>-o, &#8211;output </code><i>file</i></p>
<dd> Output the payload to the specified file.</p>
<dt><code>-k, &#8211;keys </code><i>string</i></p>
<dd> Specify a subset of metadata keys to output. The keys are case-insensitive and delimited by whitespace, commas, semicolons, or periods &#8212; as long as the string is treated as a single argument by the shell (e.g., enclosed by quotes). If a subset is not specified, all available keys are selected by default.</p>
<dt><code>-K, &#8211;list-keys</code></p>
<dd> Display a list of metadata keys.</p>
<dt><code>-S, &#8211;socket </code><i>path</i></p>
<dd> Specify the local domain socket for connecting with <code>munged</code>. </p>
</dl>
<h2>METADATA KEYS</h2>
<p> The following metadata keys are supported.</p>
<dl>
<dt><code>STATUS</code></p>
<dd> The status of the credential decode operation.</p>
<dt><code>ENCODE_HOST</code></p>
<dd> The address of the host on which the credential was encoded.</p>
<dt><code>ENCODE_TIME</code></p>
<dd> The time at which the credential was encoded (according to the local clock of the host that encoded it).</p>
<dt><code>DECODE_TIME</code></p>
<dd> The time at which the credential was decoded (according to the local clock of the host that decoded it).</p>
<dt><code>TTL</code></p>
<dd> The time-to-live value (in seconds) placed within the credential.</p>
<dt><code>CIPHER</code></p>
<dd> The cipher type used to encode the credential.</p>
<dt><code>MAC</code></p>
<dd> The MAC type used to encode the credential.</p>
<dt><code>ZIP</code></p>
<dd> The compression type used to encode the credential.</p>
<dt><code>UID</code></p>
<dd> The user ID of the process that encoded the credential.</p>
<dt><code>GID</code></p>
<dd> The group ID of the process that encoded the credential.</p>
<dt><code>UID_RESTRICTION</code></p>
<dd> The user ID restriction placed within the credential.</p>
<dt><code>GID_RESTRICTION</code></p>
<dd> The group ID restriction placed within the credential.</p>
<dt><code>LENGTH</code></p>
<dd> The length (in bytes) of the payload. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The <code>unmunge</code> program returns an exit code corresponding to the return code of <code>munge_decode</code>(). On success, it returns a zero exit code which signifies the credential is valid. On error, it prints an error message to stderr and returns a non-zero exit code. </p>
<h2>AUTHOR</h2>
<p> Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code> </p>
<h2>Index</h2>
