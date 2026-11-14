---
title: "flatpak-build-finish(1)"
name: "flatpak-build-finish"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-finish/"
description: "flatpak-build-finish – Finalize a build directory"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-finish &#8211; Finalize a build directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-finish</code> [OPTION&#8230;] DIRECTORY</dl>
<h2>DESCRIPTION</h2>
<dd>Finalizes a build directory, to prepare it for exporting. DIRECTORY is the name of the directory. </p>
<p> The result of this command is that desktop files, icons and D-Bus service files from the files subdirectory are copied to a new export subdirectory. In the metadata file, the command key is set in the [Application] group, and the supported keys in the [Environment] group are set according to the options. </p>
<p> As part of finalization you can also specify permissions that the app needs, using the various options specified below. Additionally during finalization the permissions from the runtime are inherited into the app unless you specify <code>&#8211;no-inherit-permissions</code> </p>
<p> You should review the exported files and the application metadata before creating and distributing an application bundle. </p>
<p> It is an error to run build-finish on a directory that has not been initialized as a build directory, or has already been finalized.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;command=COMMAND</code></p>
<dl>
<dt>
<dd> The command to use. If this option is not specified, the first executable found in files/bin is used. </p>
<p> Note that the command is used when the application is run via <code>flatpak run</code>, and does not affect what gets executed when the application is run in other ways, e.g. via the desktop file or D-Bus activation.</dl>
<p> <code>&#8211;require-version=MAJOR.MINOR.MICRO</code></p>
<dl>
<dt>
<dd> Require this version or later of flatpak to install/update to this build.</dl>
<p> <code>&#8211;share=SUBSYSTEM</code></p>
<dl>
<dt>
<dd> Share a subsystem with the host session. This updates the [Context] group in the metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.</dl>
<p> <code>&#8211;unshare=SUBSYSTEM</code></p>
<dl>
<dt>
<dd> Don&#8217;t share a subsystem with the host session. This updates the [Context] group in the metadata. SUBSYSTEM must be one of: network, ipc. This option can be used multiple times.</dl>
<p> <code>&#8211;socket=SOCKET</code></p>
<dl>
<dt>
<dd> Expose a well-known socket to the application. This updates the [Context] group in the metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times. </p>
<p> The fallback-x11 option makes the X11 socket available only if there is no Wayland socket. This option was introduced in 0.11.3. To support older Flatpak releases, specify both x11 and fallback-x11. The fallback-x11 option takes precedence when both are supported.</dl>
<p> <code>&#8211;nosocket=SOCKET</code></p>
<dl>
<dt>
<dd> Don&#8217;t expose a well known socket to the application. This updates the [Context] group in the metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times.</dl>
<p> <code>&#8211;device=DEVICE</code></p>
<dl>
<dt>
<dd> Expose a device to the application. This updates the [Context] group in the metadata. DEVICE must be one of: dri, kvm, shm, all. This option can be used multiple times.</dl>
<p> <code>&#8211;nodevice=DEVICE</code></p>
<dl>
<dt>
<dd> Don&#8217;t expose a device to the application. This updates the [Context] group in the metadata. DEVICE must be one of: dri, kvm, shm, all. This option can be used multiple times.</dl>
<p> <code>&#8211;allow=FEATURE</code></p>
<dl>
<dt>
<dd> Allow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus. This option can be used multiple times. </p>
<p> The devel feature allows the application to access certain syscalls such as ptrace(), and perf_event_open(). </p>
<p> The multiarch feature allows the application to execute programs compiled for an ABI other than the one supported natively by the system. For example, for the x86_64 architecture, 32-bit x86 binaries will be allowed as well. </p>
<p> The bluetooth feature allows the application to use bluetooth (AF_BLUETOOTH) sockets. Note, for bluetooth to fully work you must also have network access. </p>
<p> The canbus feature allows the application to use canbus (AF_CAN) sockets. Note, for this work you must also have network access.</dl>
<p> <code>&#8211;disallow=FEATURE</code></p>
<dl>
<dt>
<dd> Disallow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch, bluetooth, canbus. This option can be used multiple times.</dl>
<p> <code>&#8211;filesystem=FS</code></p>
<dl>
<dt>
<dd> Allow the application access to a subset of the filesystem. This updates the [Context] group in the metadata. FS can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix indicates that the location will be read-write and created if it doesn&#8217;t exist. This option can be used multiple times. See the &quot;[Context] filesystems&quot; list in <code><a href="/docs/linux/man/5-flatpak-metadata/">flatpak-metadata</a></code>(5) for details of the meanings of these filesystems.</dl>
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
<dd> Set an environment variable in the application. This updates the [Environment] group in the metadata. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;own-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to own the well known name NAME on the session bus. If NAME ends with .*, it allows the application to own all matching names. This updates the [Session Bus Policy] group in the metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well known name NAME on the session bus. If NAME ends with .*, it allows the application to talk to all matching names. This updates the [Session Bus Policy] group in the metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-own-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to own the well known name NAME on the system bus. If NAME ends with .*, it allows the application to own all matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;system-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .*, it allows the application to talk to all matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;persist=FILENAME</code></p>
<dl>
<dt>
<dd> If the application doesn&#8217;t have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the corresponding path in the per-application directory, allowing that location to be used for persistent data. This updates the [Context] group in the metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;runtime=RUNTIME</code>, <code>&#8211;sdk=SDK</code></p>
<dl>
<dt>
<dd> Change the runtime or sdk used by the app to the specified partial ref. Unspecified parts of the ref are taken from the old values or defaults.</dl>
<p> <code>&#8211;metadata=GROUP=KEY[=VALUE]</code></p>
<dl>
<dt>
<dd> Set a generic key in the metadata file. If value is left out it will be set to &quot;true&quot;.</dl>
<p> <code>&#8211;extension=NAME=VARIABLE[=VALUE]</code></p>
<dl>
<dt>
<dd> Add extension point info. See the documentation for <code><a href="/docs/linux/man/5-flatpak-metadata/">flatpak-metadata</a></code>(5) for the possible values of <i>VARIABLE</i> and <i>VALUE</i>.</dl>
<p> <code>&#8211;remove-extension=NAME</code></p>
<dl>
<dt>
<dd> Remove extension point info.</dl>
<p> <code>&#8211;extension-priority=VALUE</code></p>
<dl>
<dt>
<dd> Set the priority (library override order) of the extension point. Only useful for extensions. 0 is the default, and higher value means higher priority.</dl>
<p> <code>&#8211;extra-data=NAME:SHA256:DOWNLOAD-SIZE:INSTALL-SIZE:URL</code></p>
<dl>
<dt>
<dd> Adds information about extra data uris to the app. These will be downloaded and verified by the client when the app is installed and placed in the /app/extra directory. You can also supply an /app/bin/apply_extra script that will be run after the files are downloaded.</dl>
<p> <code>&#8211;no-exports</code></p>
<dl>
<dt>
<dd> Don&#8217;t look for exports in the build.</dl>
<p> <code>&#8211;no-inherit-permissions</code></p>
<dl>
<dt>
<dd> Don&#8217;t inherit runtime permissions in the app.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build-finish /build/my-app &#8211;socket=x11 &#8211;share=ipc</code> </p>
<dl>
<dt>
<dd>
<pre>
Exporting share/applications/gnome-calculator.desktop
Exporting share/dbus-1/services/org.gnome.Calculator.SearchProvider.service
More than one executable
Using gcalccmd as command
Please review the exported files and the metadata
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1) </p>
<h2>Index</h2>
