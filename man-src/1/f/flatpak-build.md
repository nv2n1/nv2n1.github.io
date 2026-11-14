---
title: "flatpak-build(1)"
name: "flatpak-build"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build/"
description: "flatpak-build – Build in a directory"
---

<h2 class="name">NAME</h2>
<p> flatpak-build &#8211; Build in a directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build</code> [OPTION&#8230;] DIRECTORY [COMMAND&nbsp;[ARG&#8230;]]</dl>
<h2>DESCRIPTION</h2>
<dd>Runs a build command in a directory. DIRECTORY must have been initialized with <code>flatpak build-init</code>. </p>
<p> The sdk that is specified in the metadata file in the directory is mounted at /usr and the files and var subdirectories are mounted at /app and /var, respectively. They are writable, and their contents are preserved between build commands, to allow accumulating build artifacts there.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<p> <code>-r</code>, <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Use the non-devel runtime that is specified in the application metadata instead of the devel runtime.</dl>
<p> <code>-p</code>, <code>&#8211;die-with-parent</code></p>
<dl>
<dt>
<dd> Kill the build process and all children when the launching process dies.</dl>
<p> <code>&#8211;bind-mount=DEST=SOURCE</code></p>
<dl>
<dt>
<dd> Add a custom bind mount in the build namespace. Can be specified multiple times.</dl>
<p> <code>&#8211;build-dir=PATH</code></p>
<dl>
<dt>
<dd> Start the build in this directory (default is in the current directory).</dl>
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
<p> <code>&#8211;filesystem=FILESYSTEM[:ro|:create]</code></p>
<dl>
<dt>
<dd> Allow the application access to a subset of the filesystem. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn&#8217;t exist. This option can be used multiple times. See the &quot;[Context] filesystems&quot; list in <code><a href="/docs/linux/man/5-flatpak-metadata/">flatpak-metadata</a></code>(5) for details of the meanings of these filesystems.</dl>
<p> <code>&#8211;nofilesystem=FILESYSTEM</code></p>
<dl>
<dt>
<dd> Remove access to the specified subset of the filesystem from the application. This overrides to the Context section from the application metadata. FILESYSTEM can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, an absolute path, or a homedir-relative path like ~/dir. This option can be used multiple times.</dl>
<p> <code>&#8211;with-appdir</code></p>
<dl>
<dt>
<dd> Expose and configure access to the per-app storage directory in $HOME/.var/app. This is not normally useful when building, but helps when testing built apps.</dl>
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
<p> <code>&#8211;system-own-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to own the well-known name NAME on the system bus. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well-known name NAME on the system bus. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;persist=FILENAME</code></p>
<dl>
<dt>
<dd> If the application doesn&#8217;t have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;sdk-dir=DIR</code></p>
<dl>
<dt>
<dd> Normally if there is a usr directory in the build dir, this is used for the runtime files (this can be created by <code>&#8211;writable-sdk</code> or <code>&#8211;type=runtime</code> arguments to build-init). If you specify <code>&#8211;sdk-dir</code>, this directory will be used instead. Use this if you passed <code>&#8211;sdk-dir</code> to build-init.</dl>
<p> <code>&#8211;readonly</code></p>
<dl>
<dt>
<dd> Mount the normally writable destination directories read-only. This can be useful if you want to run something in the sandbox but guarantee that it doesn&#8217;t affect the build results. For example tests.</dl>
<p> <code>&#8211;metadata=FILE</code></p>
<dl>
<dt>
<dd> Use the specified filename as metadata in the exported app instead of the default file (called metadata). This is useful if you build multiple things from a single build tree (such as both a platform and a sdk).</dl>
<p> <code>&#8211;log-session-bus</code></p>
<dl>
<dt>
<dd> Log session bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.</dl>
<p> <code>&#8211;log-system-bus</code></p>
<dl>
<dt>
<dd> Log system bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build /build/my-app rpmbuild my-app.src.rpm</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1) </p>
<h2>Index</h2>
