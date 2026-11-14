---
title: "gnome-keyring-daemon(1)"
name: "gnome-keyring-daemon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-keyring-daemon/"
description: "gnome-keyring-daemon – The gnome-keyring daemon"
---

<h2 class="name">NAME</h2>
<p> gnome-keyring-daemon &#8211; The gnome-keyring daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-keyring-daemon</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gnome-keyring-daemon</code> is a service that stores your passwords and secrets. It is normally started automatically when a user logs into a desktop session. </p>
<p> The <code>gnome-keyring-daemon</code> implements the DBus Secret Service API, and you can use tools like <code>seahorse</code> or <code>secret-tool</code> to interact with it. </p>
<p> The daemon also implements a GnuPG and SSH agent both of which automatically load the user&#8217;s keys, and prompt for passwords when necessary. </p>
<p> The daemon will print out various environment variables which should be set in the user&#8217;s environment, in order to interact with the daemon.</p>
<h2>OPTIONS</h2>
<p> The various startup arguments below can be used: </p>
<p> <code>-c</code>, <code>&#8211;components=</code><i>ssh,secrets,pkcs11</i></p>
<dl>
<dt>
<dd> Ask the daemon to only initialize certain components. Valid components are ssh, secrets, pkcs11. </p>
<p> By default all components are initialized.</dl>
<p> <code>-C</code>, <code>&#8211;control-directory=</code><i>/path/to/directory</i></p>
<dl>
<dt>
<dd> Use this directory for creating communication sockets. By default a temporary directory is automatically created.</dl>
<p> <code>-d</code>, <code>&#8211;daemonize</code></p>
<dl>
<dt>
<dd> Run as a real daemon, disconnected from the terminal.</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code></p>
<dl>
<dt>
<dd> Run in the foreground, and do not fork or become a daemon.</dl>
<p> <code>-l</code>, <code>&#8211;login</code></p>
<dl>
<dt>
<dd> This argument tells the daemon it is being run by PAM. It reads all of stdin (including any newlines) as a login password and does not complete actual initialization. </p>
<p> The daemon should later be initialized with a <code>gnome-keyring-daemon</code>&nbsp;<code>&#8211;start</code> invocation. </p>
<p> This option implies <code>&#8211;unlock</code>. It may not be used together with either the <code>&#8211;replace</code> or <code>&#8211;start</code> arguments.</dl>
<p> <code>-r</code>, <code>&#8211;replace</code></p>
<dl>
<dt>
<dd> Try to replace a running keyring daemon, and assume its environment variables. A successful replacement depends on the GNOME_KEYRING_CONTROL environment variable being set by an earlier daemon. </p>
<p> This option may not be used together with either the <code>&#8211;login</code> or <code>&#8211;start</code> arguments.</dl>
<p> <code>-s</code>, <code>&#8211;start</code></p>
<dl>
<dt>
<dd> Connect to an already running daemon and initialize it. This is often used to complete initialization of a daemon that was started by PAM using the <code>&#8211;login</code> argument. </p>
<p> This option may not be used together with either the <code>&#8211;login</code> or <code>&#8211;replace</code> arguments.</dl>
<p> <code>&#8211;unlock</code></p>
<dl>
<dt>
<dd> Read a password from stdin, and use it to unlock the login keyring or create it if the login keyring does not exist.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print out the gnome-keyring version and then exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://bugzilla.gnome.org/enter_bug.cgi?product=gnome-keyring">https://bugzilla.gnome.org/enter_bug.cgi?product=gnome-keyring</a></code>m[]</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-secret-tool/">secret-tool</a></code>(1), <code><a href="/docs/linux/man/1-seahorse/">seahorse</a></code>(1) </p>
<p> Further details available in the gnome-keyring online documentation at m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/GnomeKeyring">https://wiki.gnome.org/GnomeKeyring</a></code>m[] and in the secret-service online documentation at m[blue]<code><a rel="nofollow" href="http://standards.freedesktop.org/secret-service/">http://standards.freedesktop.org/secret-service/</a></code>m[] </p>
<h2>Index</h2>
