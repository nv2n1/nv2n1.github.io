---
title: "sd_uid_is_on_seat(3)"
name: "sd_uid_is_on_seat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_uid_is_on_seat/"
description: "sd_uid_get_state, sd_uid_is_on_seat, sd_uid_get_sessions, sd_uid_get_seats, sd_uid_get_display – Determine login state of a specific Unix user ID"
---

<p>sd_uid_get_state, sd_uid_is_on_seat, sd_uid_get_sessions, sd_uid_get_seats, sd_uid_get_display &#8211; Determine login state of a specific Unix user ID</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_uid_get_state(uid_t uid, char **state);

int sd_uid_is_on_seat(uid_t uid, int require_active, const char *seat);

int sd_uid_get_sessions(uid_t uid, int require_active, char ***sessions);

int sd_uid_get_seats(uid_t uid, int require_active, char ***seats);

int sd_uid_get_display(uid_t uid, char **session);</code></pre>
<h2>Description</h2>
<p><code>sd_uid_get_state()</code></p>
<dd>may be used to determine the login state of a specific Unix user identifier. The following states are currently known: &quot;offline&quot; (user not logged in at all), &quot;lingering&quot; (user not logged in, but some user services running), &quot;online&quot; (user logged in, but not active, i.e. has no session in the foreground), &quot;active&quot; (user logged in, and has at least one active session, i.e. one session in the foreground), &quot;closing&quot; (user not logged in, and not lingering, but some processes are still around). In the future additional states might be defined, client code should be written to be robust in regards to additional state strings being returned. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_uid_is_on_seat()</code> may be used to determine whether a specific user is logged in or active on a specific seat. Accepts a Unix user identifier and a seat identifier string as parameters. The <i>require_active</i> parameter is a boolean value. If non-zero (true), this function will test if the user is active (i.e. has a session that is in the foreground and accepting user input) on the specified seat, otherwise (false) only if the user is logged in (and possibly inactive) on the specified seat. </p>
<p> <code>sd_uid_get_sessions()</code> may be used to determine the current sessions of the specified user. Accepts a Unix user identifier as parameter. The <i>require_active</i> parameter controls whether the returned list shall consist of only those sessions where the user is currently active (&gt; 0), where the user is currently online but possibly inactive (= 0), or logged in at all but possibly closing the session (&lt; 0). The call returns a <code>NULL</code> terminated string array of session identifiers in <i>sessions</i> which needs to be freed by the caller with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use, including all the strings referenced. If the string array parameter is passed as <code>NULL</code>, the array will not be filled in, but the return code still indicates the number of current sessions. Note that instead of an empty array <code>NULL</code> may be returned and should be considered equivalent to an empty array. </p>
<p> Similarly, <code>sd_uid_get_seats()</code> may be used to determine the list of seats on which the user currently has sessions. Similar semantics apply, however note that the user may have multiple sessions on the same seat as well as sessions with no attached seat and hence the number of entries in the returned array may differ from the one returned by <code>sd_uid_get_sessions()</code>. </p>
<p> <code>sd_uid_get_display()</code> returns the name of the &quot;primary&quot; session of a user. If the user has graphical sessions, it will be the oldest graphical session. Otherwise, it will be the oldest open session.</p>
<h2>Return Value</h2>
<p>On success, <code>sd_uid_get_state()</code> returns 0 or a positive integer. If the test succeeds, <code>sd_uid_is_on_seat()</code> returns a positive integer; if it fails, 0. <code>sd_uid_get_sessions()</code> and <code>sd_uid_get_seats()</code> return the number of entries in the returned arrays. <code>sd_uid_get_display()</code> returns a non-negative code on success. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>Functions described here are available as a shared library, and can be compiled and linked to using the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) entry.</p>
<h2>History</h2>
<p><code>sd_uid_get_state()</code>, <code>sd_uid_is_on_seat()</code>, <code>sd_uid_get_sessions()</code>, and <code>sd_uid_get_seats()</code> functions were added in systemd-31. </p>
<p> <code>sd_uid_get_display()</code> was added in systemd-213.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_pid_get_owner_uid/">sd_pid_get_owner_uid</a></code>(3) </p>
