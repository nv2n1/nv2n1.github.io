---

title: "unmunge(1)"
name: "unmunge"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unmunge/"
description: "unmunge – MUNGE credential decoder"
---

<p> <code>unmunge</code> [<i>OPTION</i>]&#8230; </p>
<p> The <code>unmunge</code> program validates a MUNGE credential (e.g., one created by the <code>munge</code> program). </p>
<p> By default, the credential is read from stdin and the metadata and payload are written to stdout. When the metadata and payload are written to the same stream, they are separated by a blank line. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a summary of the command-line options.</dd>
<dt><code>-L, &#8211;license</code></dt>
<dd> Display license information.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display version information.</dd>
<dt><code>-i, &#8211;input </code><i>file</i></dt>
<dd> Input the credential from the specified file.</dd>
<dt><code>-n, &#8211;no-output</code></dt>
<dd> Discard all output.</dd>
<dt><code>-m, &#8211;metadata </code><i>file</i></dt>
<dd> Output metadata to the specified file.</dd>
<dt><code>-o, &#8211;output </code><i>file</i></dt>
<dd> Output the payload to the specified file.</dd>
<dt><code>-k, &#8211;keys </code><i>string</i></dt>
<dd> Specify a subset of metadata keys to output. The keys are case-insensitive and delimited by whitespace, commas, semicolons, or periods &#8212; as long as the string is treated as a single argument by the shell (e.g., enclosed by quotes). If a subset is not specified, all available keys are selected by default.</dd>
<dt><code>-K, &#8211;list-keys</code></dt>
<dd> Display a list of metadata keys.</dd>
<dt><code>-S, &#8211;socket </code><i>path</i></dt>
<dd> Specify the local domain socket for connecting with <code>munged</code>. </dd>
</dl>
<h2>METADATA KEYS</h2>
<p> The following metadata keys are supported.</p>
<dl>
<dt><code>STATUS</code></dt>
<dd> The status of the credential decode operation.</dd>
<dt><code>ENCODE_HOST</code></dt>
<dd> The address of the host on which the credential was encoded.</dd>
<dt><code>ENCODE_TIME</code></dt>
<dd> The time at which the credential was encoded (according to the local clock of the host that encoded it).</dd>
<dt><code>DECODE_TIME</code></dt>
<dd> The time at which the credential was decoded (according to the local clock of the host that decoded it).</dd>
<dt><code>TTL</code></dt>
<dd> The time-to-live value (in seconds) placed within the credential.</dd>
<dt><code>CIPHER</code></dt>
<dd> The cipher type used to encode the credential.</dd>
<dt><code>MAC</code></dt>
<dd> The MAC type used to encode the credential.</dd>
<dt><code>ZIP</code></dt>
<dd> The compression type used to encode the credential.</dd>
<dt><code>UID</code></dt>
<dd> The user ID of the process that encoded the credential.</dd>
<dt><code>GID</code></dt>
<dd> The group ID of the process that encoded the credential.</dd>
<dt><code>UID_RESTRICTION</code></dt>
<dd> The user ID restriction placed within the credential.</dd>
<dt><code>GID_RESTRICTION</code></dt>
<dd> The group ID restriction placed within the credential.</dd>
<dt><code>LENGTH</code></dt>
<dd> The length (in bytes) of the payload. </dd>
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
