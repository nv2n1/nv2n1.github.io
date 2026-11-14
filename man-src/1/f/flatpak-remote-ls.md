---
title: "flatpak-remote-ls(1)"
name: "flatpak-remote-ls"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-ls/"
description: "flatpak-remote-ls – Show available runtimes and applications"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-ls &#8211; Show available runtimes and applications </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-ls</code> [OPTION&#8230;] [REMOTE]</dl>
<h2>DESCRIPTION</h2>
<dd>Shows runtimes and applications that are available in the remote repository with the name REMOTE, or all remotes if one isn&#8217;t specified. You can find all configured remote repositories with <code>flatpak remotes</code>. </p>
<p> REMOTE can be a file:// URI pointing to a local repository instead of a remote name. </p>
<p> Unless overridden with the <code>&#8211;system</code>, <code>&#8211;user</code>, or <code>&#8211;installation</code> options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Use the per-user configuration.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Use the default system-wide configuration.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Use a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;cached</code></p>
<dl>
<dt>
<dd> Prefer to use locally cached information if possible, even though it may be out of date. This is faster, but risks returning stale information.</dl>
<p> <code>-d</code>, <code>&#8211;show-details</code></p>
<dl>
<dt>
<dd> Show arches, branches and commit ids, in addition to the names. Equivalent to <code>&#8211;columns=all</code>.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Show only runtimes, omit applications.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Show only applications, omit runtimes.</dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
<dd> Show everything. By default locale and debug extensions as well as secondary arches when the primary arch is available are hidden.</dl>
<p> <code>&#8211;updates</code></p>
<dl>
<dt>
<dd> Show only those which have updates available.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> Show only those matching the specified architecture. By default, only supported architectures are shown. Use <code>&#8211;arch=*</code> to show all architectures. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<p> <code>&#8211;app-runtime=RUNTIME</code></p>
<dl>
<dt>
<dd> List applications that use the given runtime</dl>
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
<dd> Specify what information to show about each ref. You can list multiple fields, or use this option multiple times. </p>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> name</p>
<dl>
<dt>
<dd> Show the name</dl>
<p> description</p>
<dl>
<dt>
<dd> Show the application description</dl>
<p> application</p>
<dl>
<dt>
<dd> Show the application ID</dl>
<p> arch</p>
<dl>
<dt>
<dd> Show the arch</dl>
<p> branch</p>
<dl>
<dt>
<dd> Show the branch</dl>
<p> version</p>
<dl>
<dt>
<dd> Show the version</dl>
<p> ref</p>
<dl>
<dt>
<dd> Show the ref</dl>
<p> origin</p>
<dl>
<dt>
<dd> Show the origin remote</dl>
<p> commit</p>
<dl>
<dt>
<dd> Show the active commit</dl>
<p> installed-size</p>
<dl>
<dt>
<dd> Show the installed size</dl>
<p> download-size</p>
<dl>
<dt>
<dd> Show the download size</dl>
<p> options</p>
<dl>
<dt>
<dd> Show options</dl>
<p> all</p>
<dl>
<dt>
<dd> Show all columns</dl>
<p> help</p>
<dl>
<dt>
<dd> Show the list of available columns</dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user remote-ls &#8211;app testrepo</code> </p>
<dl>
<dt>
<dd>
<pre>
Ref
org.gnome.Builder
org.freedesktop.glxgears
</pre>
</dl>
<p> <code>$ flatpak remote-ls file:///run/media/mwleeds/d4d37026-cde2-4e5e-8bcc-d23ebbf231f9/.ostree/repo</code> </p>
<dl>
<dt>
<dd>
<pre>
Ref
org.kde.Khangman
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1) </p>
<h2>Index</h2>
