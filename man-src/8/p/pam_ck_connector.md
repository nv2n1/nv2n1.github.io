---
title: "pam_ck_connector(8)"
name: "pam_ck_connector"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ck_connector/"
description: "pam_ck_connector – Register session with ConsoleKit"
---

<p>pam_ck_connector &#8211; Register session with ConsoleKit</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_ck_connector.so</code> [debug]</dl>
<h2>Description</h2>
<dd>The pam_ck_connector PAM module registers a login session with the system-wide <i>ConsoleKit</i> daemon. This PAM module should be used with caution; only local login managers such as <code><a href="/docs/linux/man/1-login/">login</a>(1)</code> should use this. Since the <i>ConsoleKit</i> daemon can accept both an <code>tty</code> and an X11 display the normal parameters set by PAM are not always useful. An application can therefore override these with the PAM environment variables <code>CKCON_TTY,</code> <code>CKCON_X11_DISPLAY</code> and <code>CKCON_X11_DISPLAY_DEVICE</code> (the application should remember to unset these before starting the login session). Also note that the <i>ConsoleKit</i> daemon may reject registration attempts if the given set of data are inconsistent with each other. More more information, see the <i>ConsoleKit</i> documentation on the <code>OpenSessionWithParameters()</code> method call on the <code>org.freedesktop.ConsoleKit.Manager</code> D-Bus interface. If registration with the <i>ConsoleKit</i> daemon succeeds, this PAM module will set the environment variable <code>XDG_SESSION_COOKIE</code> which is used to defined membership of a login session. This PAM module has the side effect that it creates a connection to the system message bus that is kept open until the session ends. This is used by the <i>ConsoleKit</i> daemon to track the life-cycle of the session and, as such, should the login manager crash, the session will be properly unregistered. </p>
<h2>Options</h2>
<dl>
<dt><code>debug</code></p>
<dd>Print debug information.</p>
<dt><code>nox11</code></p>
<dd>Do not create a session if PAM specifies an X11 display instead of a /dev/tty terminal. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/8-pam-d/">pam.d</a></code>(8), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1)</p>
<h2>Author</h2>
<p>pam_ck_connector was written by David Zeuthen &lt;davidz [at] redhat.com&gt;.</p>
