---
title: "goa-daemon(8)"
name: "goa-daemon"
section: "8"
letter: "g"
url: "/docs/linux/man/8-goa-daemon/"
description: "goa-daemon – GNOME Online Accounts Daemon"
---

<p>goa-daemon &#8211; GNOME Online Accounts Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>goa-daemon</code> [<code>&#8211;help</code>] [<code>&#8211;replace</code>]</dl>
<h2>Description</h2>
<dd>The <code>goa-daemon</code> program provides the <i>org.gnome.OnlineAccounts</i> name on the session message bus. Users or administrators should never need to start this daemon as it will be automatically started by <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) whenever an application sends a D-Bus message to the <i>org.gnome.OnlineAccounts</i> name on the session bus.</p>
<h2>Configuration File</h2>
<p>The <code>goa-daemon</code> program stores configuration in the $XDG_CONFIG_HOME/goa-1.0/accounts.conf (typically ~/.config/goa-1.0/accounts.conf) file. The format of this file is private and 3rd party programs or libraries should never read it. This file does not contain any passwords or secrets. </p>
<p> See the m[blue]<code>XDG Base Directory Specification</code>m[]<font SIZE="-2">[1]</font> for more information about $XDG_CONFIG_HOME.</p>
<h2>Secrets</h2>
<p>The <code>goa-daemon</code> program stores secrets (such as OAuth tokens) in m[blue]<code>GNOME Keyring</code>m[]<font SIZE="-2">[2]</font>. The format of the stored secrets is private and 3rd party programs or libraries should never read, modify or delete these secrets.</p>
<h2>Options</h2>
<p><code>&#8211;replace</code></p>
<dl>
<dd>Replace existing instance.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-online-accounts/issues">https://gitlab.gnome.org/GNOME/gnome-online-accounts/issues</a></code>m[]. There are some debugging tips at m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/Projects/GnomeOnlineAccounts/Debugging">https://wiki.gnome.org/Projects/GnomeOnlineAccounts/Debugging</a></code>m[]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>XDG Base Directory Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
<dt> 2.</p>
<dd>GNOME Keyring</p>
<dl>
<dd><a rel="nofollow" href="https://live.gnome.org/GnomeKeyring">https://live.gnome.org/GnomeKeyring</a></dl>
