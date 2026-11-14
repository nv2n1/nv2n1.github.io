---
title: "remunge(1)"
name: "remunge"
section: "1"
letter: "r"
url: "/docs/linux/man/1-remunge/"
description: "remunge – MUNGE credential benchmark"
---

<h2 class="name">NAME</h2>
<p> remunge &#8211; MUNGE credential benchmark</p>
<h2>SYNOPSIS</h2>
<p> <code>remunge</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>remunge</code> program benchmarks the performance of MUNGE. A benchmark runs for the specified duration or until the specified number of credentials are processed, whichever comes first. At its conclusion, the number of credentials processed per second is written to stdout. </p>
<p> By default, credentials are encoded for one second using a single thread. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a summary of the command-line options.</p>
<dt><code>-L, &#8211;license</code></p>
<dd> Display license information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Display only the creds/sec numeric result. This is useful for producing input files for <code>ministat</code>.</p>
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
<dt><code>-e, &#8211;encode</code></p>
<dd> Encode (but do not decode) each credential. By bypassing the decode operation, the credential is not stored in the replay cache.</p>
<dt><code>-d, &#8211;decode</code></p>
<dd> Encode and decode each credential.</p>
<dt><code>-l, &#8211;length </code><i>integer</i></p>
<dd> Specify an arbitrary payload length (in bytes). The integer may be followed by a single-character modifier: k=kilobytes, m=megabytes, g=gigabytes; K=kibibytes, M=mebibytes, G=gibibytes.</p>
<dt><code>-u, &#8211;restrict-uid </code><i>uid</i></p>
<dd> Specify the user name or UID allowed to decode the credential. This will be matched against the effective user ID of the process requesting the credential decode.</p>
<dt><code>-g, &#8211;restrict-gid </code><i>gid</i></p>
<dd> Specify the group name or GID allowed to decode the credential. This will be matched against the effective group ID of the process requesting the credential decode, as well as each supplementary group of which the effective user ID of that process is a member.</p>
<dt><code>-t, &#8211;ttl </code><i>integer</i></p>
<dd> Specify the time-to-live (in seconds). This controls how long the credential is valid once it has been encoded. A value of 0 selects the default TTL. A value of -1 selects the maximum allowed TTL.</p>
<dt><code>-S, &#8211;socket </code><i>path</i></p>
<dd> Specify the local domain socket for connecting with <code>munged</code>.</p>
<dt><code>-D, &#8211;duration </code><i>integer</i></p>
<dd> Specify the test duration (in seconds). The default duration is one second. A value of -1 selects the maximum duration. The integer may be followed by a single-character modifier: s=seconds, m=minutes, h=hours, d=days.</p>
<dt><code>-N, &#8211;num-creds </code><i>integer</i></p>
<dd> Specify the number of credentials to generate. The integer may be followed by a single-character modifier: k=kilobytes, m=megabytes, g=gigabytes; K=kibibytes, M=mebibytes, G=gibibytes.</p>
<dt><code>-T, &#8211;num-threads </code><i>integer</i></p>
<dd> Specify the number of threads to spawn for processing credentials.</p>
<dt><code>-W, &#8211;warn-time </code><i>integer</i></p>
<dd> Specify the maximum number of seconds to allow for a given <code>munge_encode</code>() or <code>munge_decode</code>() operation before issuing a warning. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The <code>remunge</code> program returns a zero exit code if the benchmark completes. On error, it prints an error message to stderr and returns a non-zero exit code. </p>
<h2>AUTHOR</h2>
<p> Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code> </p>
<h2>Index</h2>
