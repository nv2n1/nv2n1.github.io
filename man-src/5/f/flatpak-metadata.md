---
title: "flatpak-metadata(5)"
name: "flatpak-metadata"
section: "5"
letter: "f"
url: "/docs/linux/man/5-flatpak-metadata/"
description: "flatpak-metadata – Information about an application or runtime"
---

<p>flatpak-metadata &#8211; Information about an application or runtime</p>
<h2>Description</h2>
<p>Flatpak uses metadata files to describe applications and runtimes. The metadata file for a deployed application or runtime is placed in the toplevel deploy directory. For example, the metadata for the locally installed application org.gnome.Calculator is in ~/.local/share/flatpak/app/org.gnome.Calculator/current/active/metadata. </p>
<p> Most aspects of the metadata configuration can be overridden when launching applications, either temporarily via options of the flatpak run command, or permanently with the flatpak override command. </p>
<p> A metadata file describing the effective configuration is available inside the running sandbox at /.flatpak-info. For compatibility with older Flatpak versions, /run/user/$UID/flatpak-info is a symbolic link to the same file.</p>
<h2>File Format</h2>
<p>The metadata file is using the same .ini file format that is used for systemd unit files or application .desktop files.</p>
<h3>[Application] or [Runtime]</h3>
<p>Metadata for applications starts with an [Application] group, metadata for runtimes with a [Runtime] group. </p>
<p> The following keys can be present in these groups: </p>
<p> <code>name</code> (string)</p>
<dl>
<dd>The name of the application or runtime. This key is mandatory.</dl>
<p> <code>runtime</code> (string)</p>
<dl>
<dd>The fully qualified name of the runtime that is used by the application. This key is mandatory for applications.</dl>
<p> <code>sdk</code> (string)</p>
<dl>
<dd>The fully qualified name of the sdk that matches the runtime. Available since 0.1.</dl>
<p> <code>command</code> (string)</p>
<dl>
<dd>The command to run. Only relevant for applications. Available since 0.1.</dl>
<p> <code>required-flatpak</code> (string list)</p>
<dl>
<dd>The required version of Flatpak to run this application or runtime. For applications, this was available since 0.8.0. For runtimes, this was available since 0.9.1, and backported to 0.8.3 for the 0.8.x branch. </p>
<p> Flatpak after version 1.4.3 and 1.2.5 support multiple versions here. This can be useful if you need to support features that are backported to a previous stable series. For example if you want to use a feature added in 1.6.0 that was also backported to 1.4.4 you would use 1.6.0;1.4.4;. Note that older versions of flatpak will just use the first element in the list, so make that the largest version.</dl>
<p> <code>tags</code> (string list)</p>
<dl>
<dd>Tags to include in AppStream XML. Available since 0.4.12.</dl>
<h3>[Context]</h3>
<p>This group determines various system resources that may be shared with the application when it is run in a flatpak sandbox. </p>
<p> All keys in this group (and the group itself) are optional. </p>
<p> <code>shared</code> (list)</p>
<dl>
<dd>List of subsystems to share with the host system. Possible subsystems: network, ipc. Available since 0.3.</dl>
<p> <code>sockets</code> (list)</p>
<dl>
<dd>List of well-known sockets to make available in the sandbox. Possible sockets: x11, wayland, fallback-x11, pulseaudio, session-bus, system-bus, ssh-auth, pcsc, cups. When making a socket available, flatpak also sets well-known environment variables like DISPLAY or DBUS_SYSTEM_BUS_ADDRESS to let the application find sockets that are not in a fixed location. Available since 0.3.</dl>
<p> <code>devices</code> (list)</p>
<dl>
<dd>List of devices to make available in the sandbox. Possible values: </p>
<p> <code>dri</code></p>
<dl>
<dd>Graphics direct rendering (/dev/dri). Available since 0.3.</dl>
<p> <code>kvm</code></p>
<dl>
<dd>Virtualization (/dev/kvm). Available since 0.6.12.</dl>
<p> <code>all</code></p>
<dl>
<dd>All device nodes in /dev, but not /dev/shm (which is separately specified). Available since 0.6.6.</dl>
<p> <code>shm</code></p>
<dl>
<dd>Access to the host /dev/shm (/dev/shm). Available since 1.6.1.</dl>
</dl>
<p> <code>filesystems</code> (list)</p>
<dl>
<dd>List of filesystem subsets to make available to the application. Possible values: </p>
<p> <code>home</code></p>
<dl>
<dd>The entire home directory. Available since 0.3.</dl>
<p> <code>host</code></p>
<dl>
<dd>The entire host file system, except for directories that are handled specially by Flatpak. In particular, this shares /home, /media, /opt, /run/media and /srv if they exist. </p>
<p> /dev is not shared: use <code>devices=all;</code> instead. </p>
<p> Parts of /sys are always shared. This option does not make additional files in /sys available. </p>
<p> These other reserved directories are currently excluded: /app, /bin, /boot, /etc, /lib, /lib32, /lib64, /proc, /root, /run, /sbin, /tmp, /usr, /var. </p>
<p> Available since 0.3.</dl>
<p> <code>xdg-desktop</code>, <code>xdg-documents</code>, <code>xdg-download</code>, <code>xdg-music</code>, <code>xdg-pictures</code>, <code>xdg-public-share</code>, <code>xdg-videos</code>, <code>xdg-templates</code></p>
<dl>
<dd>m[blue]<code>freedesktop.org special directories</code>m[]<font SIZE="-2">[1]</font>. Available since 0.3.</dl>
<p> <code>xdg-desktop/</code><i>path</i>, <code>xdg-documents/</code><i>path</i>, etc.</p>
<dl>
<dd>Subdirectories of freedesktop.org special directories. Available since 0.4.13.</dl>
<p> <code>xdg-cache</code>, <code>xdg-config</code>, <code>xdg-data</code></p>
<dl>
<dd>Directories defined by the m[blue]<code>freedesktop.org Base Directory Specification</code>m[]<font SIZE="-2">[2]</font>. Available since 0.6.14.</dl>
<p> <code>xdg-cache/</code><i>path</i>, <code>xdg-config/</code><i>path</i>, <code>xdg-data/</code><i>path</i></p>
<dl>
<dd>Subdirectories of directories defined by the freedesktop.org Base Directory Specification. Available since 0.6.14.</dl>
<p> <code>xdg-run/</code><i>path</i></p>
<dl>
<dd>Subdirectories of the <code>XDG_RUNTIME_DIR</code> defined by the freedesktop.org Base Directory Specification. Note that <code>xdg-run</code> on its own is not supported. Available since 0.4.13.</dl>
<p> <code>/</code><i>path</i></p>
<dl>
<dd>An arbitrary absolute path. Available since 0.3.</dl>
<p> <code>~/</code><i>path</i></p>
<dl>
<dd>An arbitrary path relative to the home directory. Available since 0.3.</dl>
<p> One of the above followed by <code>:ro</code></p>
<dl>
<dd>Make the given directory available read-only.</dl>
<p> One of the above followed by <code>:rw</code></p>
<dl>
<dd>Make the given directory available read/write. This is the default.</dl>
<p> One of the above followed by <code>:create</code></p>
<dl>
<dd>Make the given directory available read/write, and create it if it does not already exist.</dl>
</dl>
<p> <code>persistent</code> (list)</p>
<dl>
<dd>List of homedir-relative paths to make available at the corresponding path in the per-application home directory, allowing the locations to be used for persistent data when the application does not have access to the real homedir. For instance making &quot;.myapp&quot; persistent would make &quot;~/.myapp&quot; in the sandbox a bind mount to &quot;~/.var/app/org.my.App/.myapp&quot;, thus allowing an unmodified application to save data in the per-application location. Available since 0.3.</dl>
<p> <code>features</code> (list)</p>
<dl>
<dd>List of features available or unavailable to the application, currently from the following list: </p>
<p> <code>devel</code></p>
<dl>
<dd>Allow system calls used by development-oriented tools such as <code>perf</code>, <code>strace</code> and <code>gdb</code>. Available since 0.6.10.</dl>
<p> <code>multiarch</code></p>
<dl>
<dd>Allow running multilib/multiarch binaries, for example i386 binaries in an x86_64 environment. Available since 0.6.12.</dl>
<p> <code>bluetooth</code></p>
<dl>
<dd>Allow the application to use bluetooth (AF_BLUETOOTH) sockets. Note, for bluetooth to fully work you must also have network access. Available since 0.11.8.</dl>
<p> <code>canbus</code></p>
<dl>
<dd>Allow the application to use canbus (AF_CAN) sockets. Note, for this work you must also have network access. Available since 1.0.3.</dl>
<p> A feature can be prefixed with <code>!</code> to indicate the absence of that feature, for example <code>!devel</code> if development and debugging are not allowed.</dl>
<h3>[Instance]</h3>
<p>This group only appears in /.flatpak-info for a running app, and not in the metadata files written by application authors. It is filled in by Flatpak itself. </p>
<p> <code>instance-id</code> (string)</p>
<dl>
<dd>The ID of the running instance. This number is used as the name of the directory in <code>XDG_RUNTIME_DIR</code>/.flatpak where Flatpak stores information about this instance.</dl>
<p> <code>instance-path</code> (string)</p>
<dl>
<dd>The absolute path on the host system of the app&#8217;s persistent storage area in $HOME/.var.</dl>
<p> <code>app-path</code> (string)</p>
<dl>
<dd>The absolute path on the host system of the app&#8217;s app files, as mounted at /app inside the container. Available since 0.6.10.</dl>
<p> <code>app-commit</code> (string)</p>
<dl>
<dd>The commit ID of the application that is running.</dl>
<p> <code>app-extensions</code> (list of strings)</p>
<dl>
<dd>A list of app extensions that are mounted into the running instance. The format for each list item is <code>EXTENSION_ID=COMMIT</code>.</dl>
<p> <code>branch</code> (string)</p>
<dl>
<dd>The branch of the app, for example stable. Available since 0.6.10.</dl>
<p> <code>arch</code> (string)</p>
<dl>
<dd>The architecture of the running instance.</dl>
<p> <code>flatpak-version</code> (string)</p>
<dl>
<dd>The version number of the Flatpak version that ran this app. Available since 0.6.11.</dl>
<p> <code>runtime-path</code> (string)</p>
<dl>
<dd>The absolute path on the host system of the app&#8217;s runtime files, as mounted at /usr inside the container. Available since 0.6.10.</dl>
<p> <code>runtime-commit</code> (string)</p>
<dl>
<dd>The commit ID of the runtime that is used.</dl>
<p> <code>runtime-extensions</code> (list of strings)</p>
<dl>
<dd>A list of runtime extensions that are mounted into the running instance. The format for each list item is <code>EXTENSION_ID=COMMIT</code>.</dl>
<p> <code>extra-args</code> (string)</p>
<dl>
<dd>Extra arguments that were passed to flatpak run.</dl>
<p> <code>sandbox</code> (boolean)</p>
<dl>
<dd>Whether the <code>&#8211;sandbox</code> option was passed to flatpak run.</dl>
<p> <code>build</code> (boolean)</p>
<dl>
<dd>Whether this instance was created by flatpak build.</dl>
<p> <code>session-bus-proxy</code> (boolean)</p>
<dl>
<dd>True if this app cannot access the D-Bus session bus directly (either it goes via a proxy, or it cannot access the session bus at all). Available since 0.8.0.</dl>
<p> <code>system-bus-proxy</code> (boolean)</p>
<dl>
<dd>True if this app cannot access the D-Bus system bus directly (either it goes via a proxy, or it cannot access the system bus at all). Available since 0.8.0.</dl>
<h3>[Session Bus Policy]</h3>
<p>If the <code>sockets</code> key is not allowing full access to the D-Bus session bus, then flatpak provides filtered access. </p>
<p> The default policy for the session bus only allows the application to own its own application ID and subnames. For instance if the app is called &quot;org.my.App&quot;, it can only own &quot;org.my.App&quot; and &quot;org.my.App.*&quot;. Its also only allowed to talk to the bus itself (org.freedesktop.DBus) and the portal APIs APIs (bus names of the form org.freedesktop.portal.*). </p>
<p> Additionally the app is always allowed to reply to messages sent to it, and emit broadcast signals (but these will not reach other sandboxed apps unless they are allowed to talk to your app. </p>
<p> If the [Session Bus Policy] group is present, it provides policy for session bus access. </p>
<p> Each key in this group has the form of a D-Bus bus name or prefix thereof, for example <code>org.gnome.SessionManager</code> or <code>org.freedesktop.portal.*</code> </p>
<p> The possible values for entry are, in increasing order or access: </p>
<p> <code>none</code></p>
<dl>
<dd>The bus name or names in question is invisible to the application. Available since 0.2.</dl>
<p> <code>see</code></p>
<dl>
<dd>The bus name or names can be enumerated by the application. Available since 0.2.</dl>
<p> <code>talk</code></p>
<dl>
<dd>The application can send messages/ and receive replies and signals from the bus name or names. Available since 0.2.</dl>
<p> <code>own</code></p>
<dl>
<dd>The application can own the bus name or names (as well as all the above). Available since 0.2.</dl>
<h3>[System Bus Policy]</h3>
<p>If the <code>sockets</code> key is not allowing full access to the D-Bus system bus, then flatpak does not make the system bus available unless the [System Bus Policy] group is present and provides a policy for filtered access. Available since 0.2. </p>
<p> Entries in this group have the same form as for the [Session Bus Policy] group. However, the app has no permissions by default.</p>
<h3>[Environment]</h3>
<p>The [Environment] group specifies environment variables to set when running the application. Available since 0.3. </p>
<p> Entries in this group have the form <code>VAR=VALUE</code> where <code>VAR</code> is the name of an environment variable to set.</p>
<h3>[Extension NAME]</h3>
<p>Runtimes and applications can define extension points, which allow optional, additional runtimes to be mounted at a specified location inside the sandbox when they are present on the system. Typical uses for extension points include translations for applications, or debuginfo for sdks. The name of the extension point is specified as part of the group heading. Since 0.11.4, the name may optionally include a tag in the NAME in the name@tag ref syntax if you wish to use different configurations (eg, versions) of the same extension concurrently. The &quot;tag&quot; is effectively ignored, but is necessary in order to allow the same extension name to be specified more than once. </p>
<p> <code>directory</code> (string)</p>
<dl>
<dd>The relative path at which the extension will be mounted in the sandbox. If the extension point is for an application, the path is relative to /app, otherwise it is relative to /usr. This key is mandatory. Available since 0.1.</dl>
<p> <code>version</code> (string)</p>
<dl>
<dd>The branch to use when looking for the extension. If this is not specified, it defaults to the branch of the application or runtime that the extension point is for. Available since 0.4.1.</dl>
<p> <code>versions</code> (string)</p>
<dl>
<dd>The branches to use when looking for the extension. If this is not specified, it defaults to the branch of the application or runtime that the extension point is for. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.4.</dl>
<p> <code>add-ld-path</code> (string)</p>
<dl>
<dd>A path relative to the extension point directory that will be appended to LD_LIBRARY_PATH. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.</dl>
<p> <code>merge-dirs</code> (string)</p>
<dl>
<dd>A list of relative paths of directories below the extension point directory that will be merged. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.</dl>
<p> <code>download-if</code> (string)</p>
<dl>
<dd>A condition that must be true for the extension to be auto-downloaded. As of 1.1.1 this supports multiple conditions separated by semi-colons. </p>
<p> These are the supported conditions: </p>
<p> <code>active-gl-driver</code></p>
<dl>
<dd>Is true if the name of the active GL driver matches the extension point basename. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.</dl>
<p> <code>active-gtk-theme</code></p>
<dl>
<dd>Is true if the name of the current GTK theme (via org.gnome.desktop.interface GSetting) matches the extension point basename. Added 0.10.1.</dl>
<p> <code>have-intel-gpu</code></p>
<dl>
<dd>Is true if the i915 kernel module is loaded. Added 0.10.1.</dl>
<p> <code>on-xdg-desktop-*</code></p>
<dl>
<dd>Is true if the suffix (case-insensitively) is in the XDG_CURRENT_DESKTOP env var. For example on-xdg-desktop-GNOME-classic. Added 1.1.1.</dl>
</dl>
<p> <code>autoprune-unless</code> (string)</p>
<dl>
<dd>A condition that must be false for the extension to be considered unused when pruning. For example, <code>flatpak uninstall &#8211;unused</code> uses this information. The only currently recognized value is active-gl-driver, which is true if the name of the active GL driver matches the extension point basename. Available since 0.11.8.</dl>
<p> <code>enable-if</code> (string)</p>
<dl>
<dd>A condition that must be true for the extension to be enabled. As of 1.1.1 this supports multiple conditions separated by semi-colons. See <code>download-if</code> for available conditions.</dl>
<p> <code>subdirectory-suffix</code> (string)</p>
<dl>
<dd>A suffix that gets appended to the directory name. This is very useful when the extension point naming scheme is &quot;reversed&quot;. For example, an extension point for GTK+ themes would be /usr/share/themes/$NAME/gtk-3.0, which could be achieved using subdirectory-suffix=gtk-3.0. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.</dl>
<p> <code>subdirectories</code> (boolean)</p>
<dl>
<dd>If this key is set to true, then flatpak will look for extensions whose name is a prefix of the extension point name, and mount them at the corresponding name below the subdirectory. Available since 0.1.</dl>
<p> <code>no-autodownload</code> (boolean)</p>
<dl>
<dd>Whether to automatically download extensions matching this extension point when updating or installing a &#8216;related&#8217; application or runtime. Available since 0.6.7.</dl>
<p> <code>locale-subset</code> (boolean)</p>
<dl>
<dd>If set, then the extensions are partially downloaded by default, based on the currently configured locales. This means that the extension contents should be a set of directories with the language code as name. Available since 0.9.13 (and 0.6.6 for any extensions called *.Locale)</dl>
<p> <code>autodelete</code> (boolean)</p>
<dl>
<dd>Whether to automatically delete extensions matching this extension point when deleting a &#8216;related&#8217; application or runtime. Available since 0.6.7.</dl>
<p> <code>collection-id</code> (string)</p>
<dl>
<dd>The ID of the collection that this extension point belongs to. If this is unspecified, it defaults to the collection ID of the application or runtime that the extension point is for. Currently, extension points must be in the same collection as the application or runtime that they are for. Available since 0.99.1.</dl>
<h3>[ExtensionOf]</h3>
<p>This optional group may be present if the runtime is an extension. </p>
<p> <code>ref</code> (string)</p>
<dl>
<dd>The ref of the runtime or application that this extension belongs to. Available since 0.9.1.</dl>
<p> <code>runtime</code> (string)</p>
<dl>
<dd>The runtime this extension will be inside of. If it is an app extension, this is the app&#8217;s runtime; otherwise, this is identical to ref, without the runtime/ prefix. Available since 1.5.0.</dl>
<p> <code>priority</code> (integer)</p>
<dl>
<dd>The priority to give this extension when looking for the best match. Default is 0. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.3.</dl>
<p> <code>tag</code> (string)</p>
<dl>
<dd>The tag name to use when searching for this extension&#8217;s mount point in the parent flatpak. Available since 0.11.4.</dl>
<h3>[Extra Data]</h3>
<p>This optional group may be present if the runtime or application uses extra data that gets downloaded separately. The data in this group gets merged into the repository summary, with the xa.extra-data-sources key. </p>
<p> If multiple extra data sources are present, their uri, size and checksum keys are grouped together by using the same suffix. If only one extra data source is present, the suffix can be omitted. </p>
<p> <code>NoRuntime</code> (boolean)</p>
<dl>
<dd>Whether to mount the runtime while running the /app/bin/apply_extra script. Defaults to true, i.e. not mounting the runtime. Available since 0.9.1, and backported to the 0.8.x branch in 0.8.4.</dl>
<p> <code>uri</code><i>X</i> (string)</p>
<dl>
<dd>The uri for extra data source <i>X</i>. The only supported uri schemes are http and https. Available since 0.6.13.</dl>
<p> <code>size</code><i>X</i> (integer)</p>
<dl>
<dd>The size for extra data source <i>X</i>. Available since 0.6.13.</dl>
<p> <code>checksum</code><i>X</i> (string)</p>
<dl>
<dd>The sha256 sum for extra data source <i>X</i>. Available since 0.6.13.</dl>
<h3>[Policy SUBSYSTEM]</h3>
<p>Subsystems can define their own policies to be placed in a group whose name has this form. Their values are treated as lists, in which items can have their meaning negated by prepending ! to the value. They are not otherwise parsed by Flatpak. Available since 0.6.13.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>[Application]
name=org.gnome.Calculator
runtime=org.gnome.Platform/x86_64/3.20
sdk=org.gnome.Sdk/x86_64/3.20
command=gnome-calculator
[Context]
shared=network;ipc;
sockets=x11;wayland;
filesystems=xdg-run/dconf;~/.config/dconf:ro;
[Session Bus Policy]
ca.desrt.dconf=talk
[Environment]
DCONF_USER_CONFIG_DIR=.config/dconf
[Extension org.gnome.Calculator.Locale]
directory=share/runtime/locale
subdirectories=true
[Extension org.gnome.Calculator.Debug]
directory=lib/debug</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>freedesktop.org special directories</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/xdg-user-dirs/">https://www.freedesktop.org/wiki/Software/xdg-user-dirs/</a></dl>
<dt> 2.</p>
<dd>freedesktop.org Base Directory Specification</p>
<dl>
<dd><a rel="nofollow" href="https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html">https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dl>
