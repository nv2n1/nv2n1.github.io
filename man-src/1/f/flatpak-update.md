---
title: "flatpak-update(1)"
name: "flatpak-update"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-update/"
description: "flatpak-update – Update an application or runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-update &#8211; Update an application or runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak update</code> [OPTION&#8230;] [REF&#8230;]</p>
<dt> <code>flatpak update</code> [OPTION&#8230;] &#8211;appstream [REMOTE]</dl>
<h2>DESCRIPTION</h2>
<dd>Updates applications and runtimes. REF is a reference to the application or runtime to update. If no REF is given, everything is updated, as well as appstream info for all remotes. </p>
<p> Each REF argument is a full or partial identifier in the flatpak ref format, which looks like &quot;(app|runtime)/ID/ARCH/BRANCH&quot;. All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches an error message will list the alternatives. </p>
<p> By default this looks for both apps and runtimes with the given REF, but you can limit this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> option, or by supplying the initial element in the REF. </p>
<p> Normally, this command updates the application to the tip of its branch. But it is possible to check out another commit, with the &#8211;commit option. </p>
<p> If the configured remote for a ref being updated has a collection ID configured on it, flatpak will search mounted filesystems such as USB drives as well as Avahi services advertised on the local network for the needed refs, in order to support offline updates. See <code><a href="/docs/linux/man/1-ostree-find-remotes/">ostree-find-remotes</a></code>(1) for more information. </p>
<p> Note that updating a runtime is different from installing a different branch, and runtime updates are expected to keep strict compatibility. If an application update does cause a problem, it is possible to go back to the previous version, with the <code>&#8211;commit</code> option. </p>
<p> Unless overridden with the <code>&#8211;user</code>, <code>&#8211;system</code> or <code>&#8211;installation</code> option, this command updates any matching refs in the standard system-wide installation and the per-user one.</p>
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
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to update for. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;subpath=PATH</code></p>
<dl>
<dt>
<dd> Install only a subpath of the ref. This is mainly used to install a subset of locales. This can be added multiple times to install multiple subpaths. If this is not specified the subpaths specified at install time are reused.</dl>
<p> <code>&#8211;commit=COMMIT</code></p>
<dl>
<dt>
<dd> Update to this commit, instead of the tip of the branch. You can find commits using <code>flatpak remote-info &#8211;log REMOTE REF</code>.</dl>
<p> <code>&#8211;no-deploy</code></p>
<dl>
<dt>
<dd> Download the latest version, but don&#8217;t deploy it.</dl>
<p> <code>&#8211;no-pull</code></p>
<dl>
<dt>
<dd> Don&#8217;t download the latest version, deploy whatever is locally available.</dl>
<p> <code>&#8211;no-related</code></p>
<dl>
<dt>
<dd> Don&#8217;t download related extensions, such as the locale data.</dl>
<p> <code>&#8211;no-deps</code></p>
<dl>
<dt>
<dd> Don&#8217;t update or install runtime dependencies when installing.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Only look for an app with the given name.</dl>
<p> <code>&#8211;appstream</code></p>
<dl>
<dt>
<dd> Update appstream for REMOTE, or all remotes if no remote is specified.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Only look for a runtime with the given name.</dl>
<p> <code>-y</code>, <code>&#8211;assumeyes</code></p>
<dl>
<dt>
<dd> Automatically answer yes to all questions (or pick the most prioritized answer). This is useful for automation.</dl>
<p> <code>&#8211;noninteractive</code></p>
<dl>
<dt>
<dd> Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.</dl>
<p> <code>&#8211;force-remove</code></p>
<dl>
<dt>
<dd> Remove old files even if they&#8217;re in use by a running application.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user update org.gnome.gedit</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-list/">flatpak-list</a></code>(1), <code><a href="/docs/linux/man/1-ostree-find-remotes/">ostree-find-remotes</a></code>(1) </p>
<h2>Index</h2>
