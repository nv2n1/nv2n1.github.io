---
title: "sd_seat_can_multi_session(3)"
name: "sd_seat_can_multi_session"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_seat_can_multi_session/"
description: "sd_seat_get_active, sd_seat_get_sessions, sd_seat_can_multi_session, sd_seat_can_tty, sd_seat_can_graphical – Determine state of a specific seat"
---

<p>sd_seat_get_active, sd_seat_get_sessions, sd_seat_can_multi_session, sd_seat_can_tty, sd_seat_can_graphical &#8211; Determine state of a specific seat</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_seat_get_active(const char *seat, char **session, uid_t *uid);

int sd_seat_get_sessions(const char *seat, char ***sessions, uid_t **uid, unsigned int *n_uids);

int sd_seat_can_multi_session(const char *seat);

int sd_seat_can_tty(const char *seat);

int sd_seat_can_graphical(const char *seat);</code></pre>
<h2>Description</h2>
<p><code>sd_seat_get_active()</code></p>
<dd>may be used to determine which session is currently active on a seat, if there is any. Returns the session identifier and the user identifier of the Unix user the session is belonging to. Either the session or the user identifier parameter can be passed <code>NULL</code>, in case only one of the parameters shall be queried. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_seat_get_sessions()</code> may be used to determine all sessions on the specified seat. Returns two arrays, one (<code>NULL</code> terminated) with the session identifiers of the sessions and one with the user identifiers of the Unix users the sessions belong to. An additional parameter may be used to return the number of entries in the latter array. The two arrays and the latter parameter may be passed as <code>NULL</code> in case these values need not to be determined. The arrays and the strings referenced by them need to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. Note that instead of an empty array <code>NULL</code> may be returned and should be considered equivalent to an empty array. </p>
<p> <code>sd_seat_can_multi_session()</code> may be used to determine whether a specific seat is capable of multi-session, i.e. allows multiple login sessions in parallel (with only one being active at a time). </p>
<p> <code>sd_seat_can_tty()</code> may be used to determine whether a specific seat provides TTY functionality, i.e. is useful as a text console. </p>
<p> <code>sd_seat_can_graphical()</code> may be used to determine whether a specific seat provides graphics functionality, i.e. is useful as a graphics display. </p>
<p> If the <i>seat</i> parameter of any of these functions is passed as <code>NULL</code>, the operation is executed for the seat of the session of the calling process, if there is any.</p>
<h2>Return Value</h2>
<p>On success, <code>sd_seat_get_active()</code> returns 0 or a positive integer. On success, <code>sd_seat_get_sessions()</code> returns the number of entries in the session identifier array. If the test succeeds, <code>sd_seat_can_multi_session</code>, <code>sd_seat_can_tty</code> and <code>sd_seat_can_graphical</code> return a positive integer, if it fails 0. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_seat_get_active()</code>, <code>sd_seat_get_sessions()</code>, <code>sd_seat_can_multi_session()</code>, <code>sd_seat_can_tty()</code> and <code>sd_seat_can_grapical()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_session_get_seat/">sd_session_get_seat</a></code>(3) </p>
