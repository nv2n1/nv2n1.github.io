---
title: "flatpak-install(1)"
name: "flatpak-install"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-install/"
description: "flatpak-install – Install an application or runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-install &#8211; Install an application or runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak install</code> [OPTION&#8230;] [REMOTE] REF&#8230;</p>
<dt> <code>flatpak install</code> [OPTION&#8230;] [&#8211;from|&#8211;bundle] LOCATION</dl>
<h2>DESCRIPTION</h2>
<dd>Installs an application or runtime. The primary way to install is to specify a REMOTE name as the source and one ore more REFs to specify the application or runtime to install. If REMOTE is omitted, the configured remotes are searched for the first REF and the user is asked to confirm the resulting choice. </p>
<p> Each REF argument is a full or partial identifier in the flatpak ref format, which looks like &quot;(app|runtime)/ID/ARCH/BRANCH&quot;. All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is in the remote, and if there are multiple matches you will be prompted to choose one of them. You will also be prompted with choices if REF doesn&#8217;t match anything in the remote exactly but is similar to one or more refs in the remote (e.g. &quot;devhelp&quot; is similar to &quot;org.gnome.Devhelp&quot;). </p>
<p> By default this looks for both apps and runtimes with the given REF in the specified REMOTE, but you can limit this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> option, or by supplying the initial element in the REF. </p>
<p> If REMOTE is a uri or a path (absolute or relative starting with ./) to a local repository, then that repository will be used as the source, and a temporary remote will be created for the lifetime of the REF. </p>
<p> If the specified REMOTE has a collection ID configured on it, flatpak will search mounted filesystems such as USB drives as well as Avahi services advertised on the local network for the needed refs, in order to support offline updates. See <code><a href="/docs/linux/man/1-ostree-find-remotes/">ostree-find-remotes</a></code>(1) for more information. </p>
<p> The alternative form of the command (with <code>&#8211;from</code> or <code>&#8211;bundle</code>) allows to install directly from a source such as a .flatpak single-file bundle or a .flatpakref application description. The options are optional if the first argument has the expected filename extension. </p>
<p> Note that flatpak allows to have multiple branches of an application and runtimes installed and used at the same time. However, only one version of an application can be current, meaning its exported files (for instance desktop files and icons) are visible to the host. The last installed version is made current by default, but this can manually changed with flatpak make-current. </p>
<p> Unless overridden with the <code>&#8211;user</code> or the <code>&#8211;installation</code> option, this command installs the application or runtime in the default system-wide installation.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;bundle</code></p>
<dl>
<dt>
<dd> Treat LOCATION as a single-bundle file. This is assumed if the argument ends with .flatpak.</dl>
<p> <code>&#8211;from</code></p>
<dl>
<dt>
<dd> Treat LOCATION as an application description file. This is assumed if the argument ends with .flatpakref.</dl>
<p> <code>&#8211;reinstall</code></p>
<dl>
<dt>
<dd> Uninstall first if already installed.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Install the application or runtime in a per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Install the application or runtime in the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Install the application or runtime in a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The default architecture to install for, if not given explicitly in the REF. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;subpath=PATH</code></p>
<dl>
<dt>
<dd> Install only a subpath of REF. This is mainly used to install a subset of locales. This can be added multiple times to install multiple subpaths.</dl>
<p> <code>&#8211;gpg-file=FILE</code></p>
<dl>
<dt>
<dd> Check bundle signatures with GPG key from FILE (- for stdin).</dl>
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
<dd> Don&#8217;t verify runtime dependencies when installing.</dl>
<p> <code>&#8211;or-update</code></p>
<dl>
<dt>
<dd> Normally install just ignores things that are already installed (printing a warning), but if &#8211;or-update is specified it silently turns it into an update operation instead.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Assume that all REFs are apps if not explicitly specified.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Assume that all REFs are runtimes if not explicitly specified.</dl>
<p> <code>-y</code>, <code>&#8211;assumeyes</code></p>
<dl>
<dt>
<dd> Automatically answer yes to all questions (or pick the most prioritized answer). This is useful for automation.</dl>
<p> <code>&#8211;noninteractive</code></p>
<dl>
<dt>
<dd> Produce minimal output and avoid most questions. This is suitable for use in non-interactive situations, e.g. in a build script.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak install gedit</code> </p>
<p> <code>$ flatpak install flathub org.gnome.gedit</code> </p>
<p> <code>$ flatpak &#8211;installation=default install flathub org.gnome.gedit</code> </p>
<p> <code>$ flatpak &#8211;user install flathub org.gnome.gedit//3.30</code> </p>
<p> <code>$ flatpak &#8211;user install <a rel="nofollow" href="https://flathub.org/repo/appstream/org.gnome.gedit.flatpakref">https://flathub.org/repo/appstream/org.gnome.gedit.flatpakref</a></code> </p>
<p> <code>$ flatpak &#8211;system install org.gnome.gedit.flatpakref</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-list/">flatpak-list</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-bundle/">flatpak-build-bundle</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-flatpakref/">flatpak-flatpakref</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-make-current/">flatpak-make-current</a></code>(1), <code><a href="/docs/linux/man/1-ostree-find-remotes/">ostree-find-remotes</a></code>(1) </p>
<h2>Index</h2>
