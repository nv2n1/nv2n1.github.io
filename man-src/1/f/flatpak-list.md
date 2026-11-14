---
title: "flatpak-list(1)"
name: "flatpak-list"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-list/"
description: "flatpak-list – List installed applications and/or runtimes"
---

<h2 class="name">NAME</h2>
<p> flatpak-list &#8211; List installed applications and/or runtimes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak list</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Lists the names of the installed applications and runtimes. </p>
<p> By default, both apps and runtimes are shown, but you can change this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> options. </p>
<p> By default, both per-user and system-wide installations are shown. Use the <code>&#8211;user</code>, <code>&#8211;installation</code> or <code>&#8211;system</code> options to change this. </p>
<p> The list command can also be used to find installed apps that use a certain runtime, with the <code>&#8211;app-runtime</code> option.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> List per-user installations.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> List the default system-wide installations.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> List a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> List apps/runtimes for this architecture. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-d</code>, <code>&#8211;show-details</code></p>
<dl>
<dt>
<dd> Show origin, sizes and other extra information. Equivalent to <code>&#8211;columns=all</code>.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> List applications.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> List runtimes.</dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
<dd> List all installed runtimes, including locale and debug extensions. These are hidden by default.</dl>
<p> <code>&#8211;app-runtime=RUNTIME</code></p>
<dl>
<dt>
<dd> List applications that use the given runtime.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
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
<dd> Show the description</dl>
<p> application</p>
<dl>
<dt>
<dd> Show the application or runtime ID</dl>
<p> arch</p>
<dl>
<dt>
<dd> Show the architecture</dl>
<p> branch</p>
<dl>
<dt>
<dd> Show the branch</dl>
<p> runtime</p>
<dl>
<dt>
<dd> Show the used runtime</dl>
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
<p> installation</p>
<dl>
<dt>
<dd> Show the installation</dl>
<p> active</p>
<dl>
<dt>
<dd> Show the active commit</dl>
<p> latest</p>
<dl>
<dt>
<dd> Show the latest commit</dl>
<p> size</p>
<dl>
<dt>
<dd> Show the installed size</dl>
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
<p> <code>$ flatpak &#8211;user &#8211;columns=app list</code> </p>
<dl>
<dt>
<dd>
<pre>
<code>Application</code>
org.gnome.Builder
org.freedesktop.glxgears
org.gnome.MyApp
org.gnome.gedit
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1) </p>
<h2>Index</h2>
