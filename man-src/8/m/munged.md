---
title: "munged(8)"
name: "munged"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munged/"
description: "munged – MUNGE daemon"
---

<p>munged &#8211; MUNGE daemon</p>
<h2>Synopsis</h2>
<p><code>munged</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>The <code>munged</code> daemon is responsible for authenticating local MUNGE clients and servicing their credential encode &amp; decode requests. All <code>munged</code> daemons within a security realm share a secret key. This key is used to protect the contents of a credential. When a credential is created, <code>munged</code> embeds metadata within it including the effective UID and GID of the requesting client (as determined by <code>munged</code>) and the current time (as determined by the local clock). It then compresses the data, computes a message authentication code, encrypts the data, and base64-encodes the result before returning the credential to the client. When a credential is validated, <code>munged</code> first checks the message authentication code to ensure the credential has not been subsequently altered. Next, it checks the embedded UID/GID restrictions to determine whether the requesting client is allowed to decode it. Then, it checks the embedded encode time against the current time; if this difference exceeds the embedded time-to-live, the credential has expired. Finally, it checks whether this credential has been previously decoded on this host; if so, the credential has been replayed. If all checks pass, the credential metadata and payload are returned to the client. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Display a summary of the command-line options.</p>
<dt><code>-L, &#8211;license</code></p>
<dd>Display license information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Display version information.</p>
<dt><code>-f, &#8211;force</code></p>
<dd>Force the daemon to run if at all possible. This overrides warnings for an existing local domain socket, a lack of entropy for the PRNG, and insecure file/directory permissions. Use with caution as overriding these warnings can affect security.</p>
<dt><code>-F, &#8211;foreground</code></p>
<dd>Run the daemon in the foreground.</p>
<dt><code>-M, &#8211;mlockall</code></p>
<dd>Lock all current and future pages in the virtual memory address space. Access to locked pages will never be delayed by a page fault. This can improve performance and help the daemon remain responsive when the system is under heavy memory pressure. This typically requires root privileges or the CAP_IPC_LOCK capability.</p>
<dt><code>-S, &#8211;socket </code><i>path</i></p>
<dd>Specify the local domain socket for communicating with clients.</p>
<dt><code>&#8211;auth-server-dir </code><i>directory</i></p>
<dd>Specify an alternate directory in which the daemon will create the pipe used to authenticate clients. The recommended permissions for this directory are 0711. This option is only valid on platforms where client authentication is performed via a file-descriptor passing mechanism.</p>
<dt><code>&#8211;auth-client-dir </code><i>directory</i></p>
<dd>Specify an alternate directory in which clients will create the file used to authenticate themselves to the daemon. The recommended permissions for this directory are 1733. This option is only valid on platforms where client authentication is performed via a file-descriptor passing mechanism.</p>
<dt><code>&#8211;benchmark</code></p>
<dd>Disable recurring timers in order to reduce some noise while benchmarking. This affects the PRNG entropy pool, supplementary group mapping, and credential replay hash. Do not enable this option when running in production.</p>
<dt><code>&#8211;group-check-mtime </code><i>boolean</i></p>
<dd>Specify whether the modification time of <i>/etc/group</i> should be checked before updating the supplementary group membership mapping. If this value is non-zero, the check will be enabled and the mapping will not be updated unless the file has been modified since the last update.</p>
<dt><code>&#8211;group-update-time </code><i>integer</i></p>
<dd>Specify the number of seconds between updates to the supplementary group membership mapping; this mapping is used when restricting credentials by GID. A value of 0 causes it to be computed initially but never updated (unless triggered by a <code>SIGHUP</code>). A value of -1 causes it to be disabled.</p>
<dt><code>&#8211;key-file </code><i>file</i></p>
<dd>Specify an alternate secret key file.</p>
<dt><code>&#8211;num-threads </code><i>integer</i></p>
<dd>Specify the number of threads to spawn for processing credential requests.</p>
<dt><code>&#8211;syslog</code></p>
<dd>Redirect log messages to syslog when the daemon is running in the background. </p>
</dl>
<h2>Signals</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Immediately update the supplementary group membership mapping instead of waiting for the next scheduled update; this mapping is used when restricting credentials by GID.</p>
<dt><code>SIGTERM</code></p>
<dd>Terminate the daemon. </p>
</dl>
<h2>Notes</h2>
<p>All clocks within a security realm must be kept in sync within the credential time-to-live setting. While <code>munged</code> prevents a given credential from being decoded on a particular host more than once, nothing prevents a credential from being decoded on multiple hosts within the security realm before it expires. </p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7). <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code> </p>
