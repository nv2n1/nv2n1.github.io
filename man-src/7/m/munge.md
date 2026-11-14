---
title: "munge(7)"
name: "munge"
section: "7"
letter: "m"
url: "/docs/linux/man/7-munge/"
description: "munge – MUNGE overview"
---

<p>munge &#8211; MUNGE overview</p>
<h2>Introduction</h2>
<p>MUNGE (MUNGE Uid &#8216;N&#8217; Gid Emporium) is an authentication service for creating and validating credentials. It is designed to be highly scalable for use in an HPC cluster environment. It allows a process to authenticate the UID and GID of another local or remote process within a group of hosts having common users and groups. These hosts form a security realm that is defined by a shared cryptographic key. Clients within this security realm can create and validate credentials without the use of root privileges, reserved ports, or platform-specific methods.</p>
<h2>Rationale</h2>
<p>The need for MUNGE arose out of the HPC cluster environment. Consider the scenario in which a local daemon running on a login node receives a client request and forwards it on to remote daemons running on compute nodes within the cluster. Since the user has already logged on to the login node, the local daemon just needs a reliable means of ascertaining the UID and GID of the client process. Furthermore, the remote daemons need a mechanism to ensure the forwarded authentication data has not been subsequently altered. </p>
<p> A common solution to this problem is to use Unix domain sockets to determine the identity of the local client, and then forward this information on to remote hosts via trusted rsh connections. But this presents several new problems. First, there is no portable API for determining the identity of a client over a Unix domain socket. Second, rsh connections must originate from a reserved port; the limited number of reserved ports available on a given host directly limits scalability. Third, root privileges are required in order to bind to a reserved port. Finally, the remote daemons have no means of determining whether the client identity is authentic.</p>
<h2>Usage</h2>
<p>A process creates a credential by requesting one from the local MUNGE service, either via the <code>munge_encode</code>() C library call or the <code>munge</code> executable. The encoded credential contains the UID and GID of the originating process. This process sends the credential to another process within the security realm as a means of proving its identity. The receiving process validates the credential with the use of its local MUNGE service, either via the <code>munge_decode</code>() C library call or the <code>unmunge</code> executable. The decoded credential provides the receiving process with a reliable means of ascertaining the UID and GID of the originating process. This information can be used for accounting or access control decisions.</p>
<h2>Details</h2>
<p>The contents of the credential (including any optional payload data) are encrypted with a key shared by all <code>munged</code> daemons within the security realm. The integrity of the credential is ensured by a message authentication code (MAC). The credential is valid for a limited time defined by its time-to-live (TTL); this presumes clocks within a security realm are in sync. Unexpired credentials are tracked by the local <code>munged</code> daemon in order to prevent replay attacks on a given host. Decoding of a credential can be restricted to a particular user and/or group ID. The payload data can be used for purposes such as embedding the destination&#8217;s address to ensure the credential is only valid on a specific host. The internal format of the credential is encoded in a platform-independent manner. And the credential itself is base64 encoded to allow it to be transmitted over virtually any transport.</p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code> </p>
