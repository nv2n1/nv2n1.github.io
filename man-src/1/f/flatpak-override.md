---
title: "flatpak-override(1)"
name: "flatpak-override"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-override/"
description: "flatpak-override – Override application requirements"
---

<h2 class="name">NAME</h2>
<p> flatpak-override &#8211; Override application requirements </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak override</code> [OPTION&#8230;] [APP]</dl>
<h2>DESCRIPTION</h2>
<dd>Overrides the application specified runtime requirements. This can be used to grant a sandboxed application more or less resources than it requested. </p>
<p> By default the application gets access to the resources it requested when it is started. But the user can override it on a particular instance by specifying extra arguments to flatpak run, or every time by using flatpak override. </p>
<p> If the application id is not specified then the overrides affect all applications, but the per-application overrides can override the global overrides. </p>
<p> Unless overridden with the <code>&#8211;user</code> or <code>&#8211;installation</code> options, this command changes the default system-wide installation.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Update a per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Update the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Updates a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;share=SUBSYSTEM</code></p>
<dl>
<dt>
<dd> Share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.</dl>
<p> <code>&#8211;unshare=SUBSYSTEM</code></p>
<dl>
<dt>
<dd> Don&#8217;t share a subsystem with the host session. This overrides the Context section from the application metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.</dl>
<p> <code>&#8211;socket=SOCKET</code></p>
<dl>
<dt>
<dd> Expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times.</dl>
<p> <code>&#8211;nosocket=SOCKET</code></p>
<dl>
<dt>
<dd> Don&#8217;t expose a well-known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times.</dl>
<p> <code>&#8211;device=DEVICE</code></p>
<dl>
<dt>
<dd> Expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, kvm, shm, all. This option can be used multiple times.</dl>
<p> <code>&#8211;nodevice=DEVICE</code></p>
<dl>
<dt>
<dd> Don&#8217;t expose a device to the application. This overrides to the Context section from the application metadata. DEVICE must be one of: dri, kvm, shm, all. This option can be used multiple times.</dl>
<p> <code>&#8211;allow=FEATURE</code></p>
<dl>
<dt>
<dd> Allow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus. This option can be used multiple times. </p>
<p> See <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1) for the meaning of the various features.</dl>
<p> <code>&#8211;disallow=FEATURE</code></p>
<dl>
<dt>
<dd> Disallow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus. This option can be used multiple times.</dl>
<p> <code>&#8211;filesystem=FILESYSTEM</code></p>
<dl>
<dt>
<dd> Allow the application access to a subset of the filesystem. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn&#8217;t exist. This option can be used multiple times. See the &quot;[Context] filesystems&quot; list in <code><a href="/docs/linux/man/5-flatpak-metadata/">flatpak-metadata</a></code>(5) for details of the meanings of these filesystems.</dl>
<p> <code>&#8211;nofilesystem=FILESYSTEM</code></p>
<dl>
<dt>
<dd> Remove access to the specified subset of the filesystem from the application. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, an absolute path, or a homedir-relative path like ~/dir. This option can be used multiple times.</dl>
<p> <code>&#8211;add-policy=SUBSYSTEM.KEY=VALUE</code></p>
<dl>
<dt>
<dd> Add generic policy option. For example, &quot;&#8211;add-policy=subsystem.key=v1 &#8211;add-policy=subsystem.key=v2&quot; would map to this metadata: </p>
<dl>
<dt>
<dd>
<pre><code>
[Policy subsystem] key = v1;
v2;
</code></pre>
</dl>
<p> This option can be used multiple times.</dl>
<p> <code>&#8211;remove-policy=SUBSYSTEM.KEY=VALUE</code></p>
<dl>
<dt>
<dd> Remove generic policy option. This option can be used multiple times.</dl>
<p> <code>&#8211;env=VAR=VALUE</code></p>
<dl>
<dt>
<dd> Set an environment variable in the application. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;own-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to own the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;no-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Don&#8217;t allow the application to talk to the well-known name NAME on the session bus. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-own-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to own the well known name NAME on the system bus. If NAME ends with .*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-no-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Don&#8217;t allow the application to talk to the well known name NAME on the system bus. If NAME ends with .*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;persist=FILENAME</code></p>
<dl>
<dt>
<dd> If the application doesn&#8217;t have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;reset</code></p>
<dl>
<dt>
<dd> Remove overrides. If an APP is given, remove the overrides for that application, otherwise remove the global overrides.</dl>
<p> <code>&#8211;show</code></p>
<dl>
<dt>
<dd> Shows overrides. If an APP is given, shows the overrides for that application, otherwise shows the global overrides.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak override &#8211;nosocket=wayland org.gnome.gedit</code> </p>
<p> <code>$ flatpak override &#8211;filesystem=home org.mozilla.Firefox</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1) </p>
<h2>Index</h2>
