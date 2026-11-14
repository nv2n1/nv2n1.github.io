---
title: "flatpak-run(1)"
name: "flatpak-run"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-run/"
description: "flatpak-run – Run an application or open a shell in a runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-run &#8211; Run an application or open a shell in a runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak run</code> [OPTION&#8230;] REF [ARG&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>If REF names an installed application, flatpak runs the application in a sandboxed environment. Extra arguments are passed on to the application. </p>
<p> If REF names a runtime, a shell is opened in the runtime. This is useful for development and testing. </p>
<p> By default, flatpak will look for the application or runtime in all per-user and system installations. This can be overridden with the <code>&#8211;user</code>, <code>&#8211;system</code> and <code>&#8211;installation</code> options. </p>
<p> flatpak creates a sandboxed environment for the application to run in by mounting the right runtime at /usr and a writable directory at /var, whose content is preserved between application runs. The application itself is mounted at /app. </p>
<p> The details of the sandboxed environment are controlled by the application metadata and various options like <code>&#8211;share</code> and <code>&#8211;socket</code> that are passed to the run command: Access is allowed if it was requested either in the application metadata file or with an option and the user hasn&#8217;t overridden it. </p>
<p> The remaining arguments are passed to the command that gets run in the sandboxed environment. See the <code>&#8211;file-forwarding</code> option for handling of file arguments. </p>
<p> Environment variables are generally passed on to the sandboxed application, with certain exceptions. The application metadata can override environment variables, as well as the <code>&#8211;env</code> option. Apart from that, Flatpak always unsets or overrides the following variables, since their session values are likely to interfere with the functioning of the sandbox:</p>
<dl>
<dt>
<dd> PATH</dl>
<dl>
<dt>
<dd> LD_LIBRARY_PATH</dl>
<dl>
<dt>
<dd> XDG_CONFIG_DIRS</dl>
<dl>
<dt>
<dd> XDG_DATA_DIRS</dl>
<dl>
<dt>
<dd> SHELL</dl>
<dl>
<dt>
<dd> TMPDIR</dl>
<dl>
<dt>
<dd> PYTHONPATH</dl>
<dl>
<dt>
<dd> PERLLIB</dl>
<dl>
<dt>
<dd> PERL5LIB</dl>
<dl>
<dt>
<dd> XCURSOR_PATH</dl>
<p> Flatpak also overrides the XDG environment variables to point sandboxed applications at their writable filesystem locations below ~/.var/app/$APPID/:</p>
<dl>
<dt>
<dd> XDG_DATA_HOME</dl>
<dl>
<dt>
<dd> XDG_CONFIG_HOME</dl>
<dl>
<dt>
<dd> XDG_CACHE_HOME</dl>
<p> The host values of these variables are made available inside the sandbox via these HOST_-prefixed variables:</p>
<dl>
<dt>
<dd> HOST_XDG_DATA_HOME</dl>
<dl>
<dt>
<dd> HOST_XDG_CONFIG_HOME</dl>
<dl>
<dt>
<dd> HOST_XDG_CACHE_HOME</dl>
<p> Flatpak sets the environment variable <code>FLATPAK_ID</code> to the application ID of the running app. </p>
<p> If parental controls support is enabled, flatpak will check the current user&#8217;s parental controls settings, and will refuse to run an app if it is blacklisted for the current user.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Look for the application and runtime in per-user installations.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Look for the application and runtime in the default system-wide installations.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Look for the application and runtime in the system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to run. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;command=COMMAND</code></p>
<dl>
<dt>
<dd> The command to run instead of the one listed in the application metadata.</dl>
<p> <code>&#8211;cwd=DIR</code></p>
<dl>
<dt>
<dd> The directory to run the command in. Note that this must be a directory inside the sandbox.</dl>
<p> <code>&#8211;branch=BRANCH</code></p>
<dl>
<dt>
<dd> The branch to use.</dl>
<p> <code>-d</code>, <code>&#8211;devel</code></p>
<dl>
<dt>
<dd> Use the devel runtime that is specified in the application metadata instead of the regular runtime, and use a seccomp profile that is less likely to break development tools.</dl>
<p> <code>&#8211;runtime=RUNTIME</code></p>
<dl>
<dt>
<dd> Use this runtime instead of the one that is specified in the application metadata. This is a full tuple, like for example org.freedesktop.Sdk/x86_64/1.2, but partial tuples are allowed. Any empty or missing parts are filled in with the corresponding values specified by the app.</dl>
<p> <code>&#8211;runtime-version=VERSION</code></p>
<dl>
<dt>
<dd> Use this version of the runtime instead of the one that is specified in the application metadata. This overrides any version specified with the &#8211;runtime option.</dl>
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
<dd> Expose a well known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times.</dl>
<p> <code>&#8211;nosocket=SOCKET</code></p>
<dl>
<dt>
<dd> Don&#8217;t expose a well known socket to the application. This overrides to the Context section from the application metadata. SOCKET must be one of: x11, wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups. This option can be used multiple times.</dl>
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
<dd> Allow access to a specific feature. This overrides to the Context section from the application metadata. FEATURE must be one of: devel, multiarch, bluetooth. This option can be used multiple times. </p>
<p> See <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1) for the meaning of the various features.</dl>
<p> <code>&#8211;disallow=FEATURE</code></p>
<dl>
<dt>
<dd> Disallow access to a specific feature. This overrides to the Context section from the application metadata. FEATURE must be one of: devel, multiarch, bluetooth. This option can be used multiple times.</dl>
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
<dd> Allow the application to own the well known name NAME on the session bus. If NAME ends with .*, it allows the application to own all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;talk-name=NAME</code></p>
<dl>
<dt>
<dd> Allow the application to talk to the well known name NAME on the session bus. If NAME ends with .*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
<p> <code>&#8211;no-talk-name=NAME</code></p>
<dl>
<dt>
<dd> Don&#8217;t allow the application to talk to the well known name NAME on the session bus. If NAME ends with .*, it allows the application to talk to all matching names. This overrides to the Context section from the application metadata. This option can be used multiple times.</dl>
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
<p> <code>&#8211;no-session-bus</code></p>
<dl>
<dt>
<dd> Run this instance without the filtered access to the session dbus connection. Note, this is the default when run with &#8211;sandbox.</dl>
<p> <code>&#8211;session-bus</code></p>
<dl>
<dt>
<dd> Allow filtered access to the session dbus connection. This is the default, except when run with &#8211;sandbox. </p>
<p> Isandbox mode, even if you allow access to the session bus the sandbox cannot talk to or own the application ids (org.the.App.*) on the bus (unless explicitly added), only names in the .Sandbox subset (org.the.App.Sandbox.*).</dl>
<p> <code>&#8211;no-a11y-bus</code></p>
<dl>
<dt>
<dd> Run this instance without the access to the accessibility bus. Note, this is the default when run with &#8211;sandbox.</dl>
<p> <code>&#8211;a11y-bus</code></p>
<dl>
<dt>
<dd> Allow access to the accessibility bus. This is the default, except when run with &#8211;sandbox.</dl>
<p> <code>&#8211;sandbox</code></p>
<dl>
<dt>
<dd> Run the application in sandboxed mode, which means dropping all the extra permissions it would otherwise have, as well as access to the session/system/a11y busses and document portal.</dl>
<p> <code>&#8211;log-session-bus</code></p>
<dl>
<dt>
<dd> Log session bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.</dl>
<p> <code>&#8211;log-system-bus</code></p>
<dl>
<dt>
<dd> Log system bus traffic. This can be useful to see what access you need to allow in your D-Bus policy.</dl>
<p> <code>-p</code>, <code>&#8211;die-with-parent</code></p>
<dl>
<dt>
<dd> Kill the entire sandbox when the launching process dies.</dl>
<p> <code>&#8211;parent-pid=PID</code></p>
<dl>
<dt>
<dd> Specifies the pid of the &quot;parent&quot; flatpak, used by &#8211;parent-expose-pids.</dl>
<p> <code>&#8211;parent-expose-pids</code></p>
<dl>
<dt>
<dd> Make the processes of the new sandbox visible in the sandbox of the parent flatpak, as defined by &#8211;parent-pid.</dl>
<p> <code>&#8211;file-forwarding</code></p>
<dl>
<dt>
<dd> If this option is specified, the remaining arguments are scanned, and all arguments that are enclosed between a pair of &#8216;@@&#8217; arguments are interpreted as file paths, exported in the document store, and passed to the command in the form of the resulting document path. Arguments between &#8216;@@u&#8217; and &#8216;@@&#8217; are considered uris, and any file: uris are exported. The exports are non-persistent and with read and write permissions for the application.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak run org.gnome.gedit</code> </p>
<p> <code>$ flatpak run &#8211;devel &#8211;command=bash org.gnome.Builder</code> </p>
<p> <code>$ flatpak run &#8211;command=bash org.gnome.Sdk</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-enter/">flatpak-enter</a></code>(1) </p>
<h2>Index</h2>
