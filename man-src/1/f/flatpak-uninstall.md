---
title: "flatpak-uninstall(1)"
name: "flatpak-uninstall"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-uninstall/"
description: "flatpak-uninstall – Uninstall an application or runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-uninstall &#8211; Uninstall an application or runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak uninstall</code> [OPTION&#8230;] [REF&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Uninstalls an application or runtime. REF is a reference to the application or runtime to uninstall. </p>
<p> Each REF argument is a full or partial identifier in the flatpak ref format, which looks like &quot;(app|runtime)/ID/ARCH/BRANCH&quot;. All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches you will be prompted to choose between them. You will also be prompted if REF doesn&#8217;t match any installed ref exactly but is similar (e.g. &quot;gedit&quot; is similar to &quot;org.gnome.gedit&quot;). </p>
<p> By default this looks for both installed apps and runtimes with the given REF, but you can limit this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> option, or by supplying the initial element in the REF. </p>
<p> Normally, this command removes the ref for this application/runtime from the local OSTree repository and purges any objects that are no longer needed to free up disk space. If the same application is later reinstalled, the objects will be pulled from the remote repository again. The <code>&#8211;keep-ref</code> option can be used to prevent this. </p>
<p> When <code>&#8211;delete-data</code> is specified while removing an app, its data directory in ~/.var/app and any permissions it might have are removed. When <code>&#8211;delete-data</code> is used without a REF, all &#8216;unowned&#8217; app data is removed. </p>
<p> Unless overridden with the <code>&#8211;system</code>, <code>&#8211;user</code>, or <code>&#8211;installation</code> options, this command searches both the system-wide installation and the per-user one for REF and errors out if it exists in more than one.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;keep-ref</code></p>
<dl>
<dt>
<dd> Keep the ref for the application and the objects belonging to it in the local repository.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Uninstalls from a per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Uninstalls from the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Uninstalls from a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to uninstall, instead of the architecture of the host system. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Remove all refs on the system.</dl>
<p> <code>&#8211;unused</code></p>
<dl>
<dt>
<dd> Remove unused refs on the system.</dl>
<p> <code>-y</code>, <code>&#8211;assumeyes</code></p>
<dl>
<dt>
<dd> Automatically answer yes to all questions. This is useful for automation.</dl>
<p> <code>&#8211;noninteractive</code></p>
<dl>
<dt>
<dd> Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Only look for an app with the given name.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Only look for a runtime with the given name.</dl>
<p> <code>&#8211;no-related</code></p>
<dl>
<dt>
<dd> Don&#8217;t uninstall related extensions, such as the locale data.</dl>
<p> <code>&#8211;force-remove</code></p>
<dl>
<dt>
<dd> Remove files even if they&#8217;re in use by a running application.</dl>
<p> <code>&#8211;delete-data</code></p>
<dl>
<dt>
<dd> Remove app data in ~/.var/app and in the permission store.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user uninstall org.gnome.gedit</code> </p>
<h2>Index</h2>
