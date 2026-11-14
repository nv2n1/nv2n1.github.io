---
title: "sd_session_is_active(3)"
name: "sd_session_is_active"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_session_is_active/"
description: "sd_session_is_active, sd_session_is_remote, sd_session_get_state, sd_session_get_uid, sd_session_get_seat, sd_session_get_service, sd_session_get_type, sd_session_get_class, sd_session_get_desktop,..."
---

<p>sd_session_is_active, sd_session_is_remote, sd_session_get_state, sd_session_get_uid, sd_session_get_seat, sd_session_get_service, sd_session_get_type, sd_session_get_class, sd_session_get_desktop, sd_session_get_display, sd_session_get_tty, sd_session_get_vt, sd_session_get_remote_host, sd_session_get_remote_user &#8211; Determine state of a specific session</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_session_is_active(const char *session);

int sd_session_is_remote(const char *session);

int sd_session_get_state(const char *session, char **state);

int sd_session_get_uid(const char *session, uid_t *uid);

int sd_session_get_seat(const char *session, char **seat);

int sd_session_get_service(const char *session, char **service);

int sd_session_get_type(const char *session, char **type);

int sd_session_get_class(const char *session, char **class);

int sd_session_get_desktop(const char *session, char **desktop);

int sd_session_get_display(const char *session, char **display);

int sd_session_get_remote_host(const char *session, char **remote_host);

int sd_session_get_remote_user(const char *session, char **remote_user);

int sd_session_get_tty(const char *session, char **tty);

int sd_session_get_vt(const char *session, unsigned int *vt);</code></pre>
<h2>Description</h2>
<p><code>sd_session_is_active()</code></p>
<dd>may be used to determine whether the session identified by the specified session identifier is currently active (i.e. currently in the foreground and available for user input) or not. </p>
<p> <code>sd_session_is_remote()</code> may be used to determine whether the session identified by the specified session identifier is a remote session (i.e. its remote host is known) or not. </p>
<p> <code>sd_session_get_state()</code> may be used to determine the state of the session identified by the specified session identifier. The following states are currently known: &quot;online&quot; (session logged in, but session not active, i.e. not in the foreground), &quot;active&quot; (session logged in and active, i.e. in the foreground), &quot;closing&quot; (session nominally logged out, but some processes belonging to it are still around). In the future additional states might be defined, client code should be written to be robust in regards to additional state strings being returned. This function is a more generic version of <code>sd_session_is_active()</code>. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_uid()</code> may be used to determine the user identifier of the Unix user the session identified by the specified session identifier belongs to. </p>
<p> <code>sd_session_get_seat()</code> may be used to determine the seat identifier of the seat the session identified by the specified session identifier belongs to. Note that not all sessions are attached to a seat, this call will fail for them. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_service()</code> may be used to determine the name of the service (as passed during PAM session setup) that registered the session identified by the specified session identifier. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_type()</code> may be used to determine the type of the session identified by the specified session identifier. The returned string is one of &quot;x11&quot;, &quot;wayland&quot;, &quot;tty&quot;, &quot;mir&quot; or &quot;unspecified&quot; and needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_class()</code> may be used to determine the class of the session identified by the specified session identifier. The returned string is one of &quot;user&quot;, &quot;greeter&quot;, &quot;lock-screen&quot;, or &quot;background&quot; and needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_desktop()</code> may be used to determine the brand of the desktop running on the session identified by the specified session identifier. This field can be set freely by desktop environments and does not follow any special formatting. However, desktops are strongly recommended to use the same identifiers and capitalization as for <i>$XDG_CURRENT_DESKTOP</i>, as defined by the m[blue]<code>Desktop Entry Specification</code>m[]<font SIZE="-2">[1]</font>. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_display()</code> may be used to determine the X11 display of the session identified by the specified session identifier. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_remote_host()</code> may be used to determine the remote hostname of the session identified by the specified session identifier. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_remote_user()</code> may be used to determine the remote username of the session identified by the specified session identifier. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. Note that this value is rarely known to the system, and even then should not be relied on. </p>
<p> <code>sd_session_get_tty()</code> may be used to determine the TTY device of the session identified by the specified session identifier. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_session_get_vt()</code> may be used to determine the VT number of the session identified by the specified session identifier. This function will return an error if the seat does not support VTs. </p>
<p> If the <i>session</i> parameter of any of these functions is passed as <code>NULL</code>, the operation is executed for the session the calling process is a member of, if there is any.</p>
<h2>Return Value</h2>
<p>If the test succeeds, <code>sd_session_is_active()</code> and <code>sd_session_is_remote()</code> return a positive integer; if it fails, 0. On success, <code>sd_session_get_state()</code>, <code>sd_session_get_uid()</code>, <code>sd_session_get_seat()</code>, <code>sd_session_get_service()</code>, <code>sd_session_get_type()</code>, <code>sd_session_get_class()</code>, <code>sd_session_get_display()</code>, <code>sd_session_get_remote_user()</code>, <code>sd_session_get_remote_host()</code> and <code>sd_session_get_tty()</code> return 0 or a positive integer. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_session_is_active()</code>, <code>sd_session_get_state()</code>, <code>sd_session_get_uid()</code>, <code>sd_session_get_seat()</code>, <code>sd_session_get_service()</code>, <code>sd_session_get_type()</code>, <code>sd_session_get_class()</code>, <code>sd_session_get_display()</code>, <code>sd_session_get_remote_host()</code>, <code>sd_session_get_remote_user()</code> and <code>sd_session_get_tty()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_pid_get_session/">sd_pid_get_session</a></code>(3)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Desktop Entry Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/desktop-entry-spec/latest/">http://standards.freedesktop.org/desktop-entry-spec/latest/</a></dl>
