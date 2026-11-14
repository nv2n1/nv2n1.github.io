---
title: "sd_get_seats(3)"
name: "sd_get_seats"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_get_seats/"
description: "sd_get_seats, sd_get_sessions, sd_get_uids, sd_get_machine_names – Determine available seats, sessions, logged in users and virtual machines/containers"
---

<p>sd_get_seats, sd_get_sessions, sd_get_uids, sd_get_machine_names &#8211; Determine available seats, sessions, logged in users and virtual machines/containers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_get_seats(char ***seats);

int sd_get_sessions(char ***sessions);

int sd_get_uids(uid_t **users);

int sd_get_machine_names(char ***machines);</code></pre>
<h2>Description</h2>
<p><code>sd_get_seats()</code></p>
<dd>may be used to determine all currently available local seats. Returns a <code>NULL</code> terminated array of seat identifiers. The returned array and all strings it references need to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. Note that instead of an empty array <code>NULL</code> may be returned and should be considered equivalent to an empty array. </p>
<p> Similarly, <code>sd_get_sessions()</code> may be used to determine all current login sessions. </p>
<p> Similarly, <code>sd_get_uids()</code> may be used to determine all Unix users who currently have login sessions. </p>
<p> Similarly, <code>sd_get_machine_names()</code> may be used to determine all current virtual machines and containers on the system. </p>
<p> Note that the returned lists are not sorted and in an undefined order.</p>
<h2>Return Value</h2>
<p>On success, <code>sd_get_seats()</code>, <code>sd_get_sessions()</code>, <code>sd_get_uids()</code> and <code>sd_get_machine_names()</code> return the number of entries in the arrays. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_get_seats()</code>, <code>sd_get_sessions()</code>, <code>sd_get_uids()</code> and <code>sd_get_machine_names()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_session_get_seat/">sd_session_get_seat</a></code>(3) </p>
