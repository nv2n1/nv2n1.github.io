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
<dt> <code>flatpak list</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Lists the names of the installed applications and runtimes. </dd>
<p> By default, both apps and runtimes are shown, but you can change this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> options. </p>
<p> By default, both per-user and system-wide installations are shown. Use the <code>&#8211;user</code>, <code>&#8211;installation</code> or <code>&#8211;system</code> options to change this. </p>
<p> The list command can also be used to find installed apps that use a certain runtime, with the <code>&#8211;app-runtime</code> option.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help options and exit.</dd></dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
</dt><dd> List per-user installations.</dd></dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
</dt><dd> List the default system-wide installations.</dd></dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
</dt><dd> List a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dd></dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
</dt><dd> List apps/runtimes for this architecture. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dd></dl>
<p> <code>-d</code>, <code>&#8211;show-details</code></p>
<dl>
<dt>
</dt><dd> Show origin, sizes and other extra information. Equivalent to <code>&#8211;columns=all</code>.</dd></dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
</dt><dd> List applications.</dd></dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
</dt><dd> List runtimes.</dd></dl>
<p> <code>&#8211;all</code>, <code>-a</code></p>
<dl>
<dt>
</dt><dd> List all installed runtimes, including locale and debug extensions. These are hidden by default.</dd></dl>
<p> <code>&#8211;app-runtime=RUNTIME</code></p>
<dl>
<dt>
</dt><dd> List applications that use the given runtime.</dd></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Print debug information during command processing.</dd></dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
</dt><dd> Print OSTree debug information during command processing.</dd></dl>
<p> <code>&#8211;columns=FIELD,&#8230;</code></p>
<dl>
<dt>
</dt><dd> Specify what information to show about each ref. You can list multiple fields, or use this option multiple times. </dd>
<p> Append :s[tart], :m[iddle], :e[nd] or :f[ull] to column names to change ellipsization.</dl>
<h2>FIELDS</h2>
<p> The following fields are understood by the <code>&#8211;columns</code> option: </p>
<p> name</p>
<dl>
<dt>
</dt><dd> Show the name</dd></dl>
<p> description</p>
<dl>
<dt>
</dt><dd> Show the description</dd></dl>
<p> application</p>
<dl>
<dt>
</dt><dd> Show the application or runtime ID</dd></dl>
<p> arch</p>
<dl>
<dt>
</dt><dd> Show the architecture</dd></dl>
<p> branch</p>
<dl>
<dt>
</dt><dd> Show the branch</dd></dl>
<p> runtime</p>
<dl>
<dt>
</dt><dd> Show the used runtime</dd></dl>
<p> version</p>
<dl>
<dt>
</dt><dd> Show the version</dd></dl>
<p> ref</p>
<dl>
<dt>
</dt><dd> Show the ref</dd></dl>
<p> origin</p>
<dl>
<dt>
</dt><dd> Show the origin remote</dd></dl>
<p> installation</p>
<dl>
<dt>
</dt><dd> Show the installation</dd></dl>
<p> active</p>
<dl>
<dt>
</dt><dd> Show the active commit</dd></dl>
<p> latest</p>
<dl>
<dt>
</dt><dd> Show the latest commit</dd></dl>
<p> size</p>
<dl>
<dt>
</dt><dd> Show the installed size</dd></dl>
<p> options</p>
<dl>
<dt>
</dt><dd> Show options</dd></dl>
<p> all</p>
<dl>
<dt>
</dt><dd> Show all columns</dd></dl>
<p> help</p>
<dl>
<dt>
</dt><dd> Show the list of available columns</dd></dl>
<p> Note that field names can be abbreviated to a unique prefix.</p>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user &#8211;columns=app list</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
<code>Application</code>
org.gnome.Builder
org.freedesktop.glxgears
org.gnome.MyApp
org.gnome.gedit
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1) </p>
<h2>Index</h2>
