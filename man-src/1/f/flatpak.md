---
title: "flatpak(1)"
name: "flatpak"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak/"
description: "flatpak – Build, install and run applications and runtimes"
---

<h2 class="name">NAME</h2>
<p> flatpak &#8211; Build, install and run applications and runtimes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak</code> [OPTION&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<dd>Flatpak is a tool for managing applications and the runtimes they use. In the Flatpak model, applications can be built and distributed independently from the host system they are used on, and they are isolated from the host system (&#8216;sandboxed&#8217;) to some degree, at runtime. </p>
<p> Flatpak can operate in system-wide or per-user mode. The system-wide data (runtimes, applications and configuration) is located in $prefix/var/lib/flatpak/, and the per-user data is in $HOME/.local/share/flatpak/. Below these locations, there is a local repository in the repo/ subdirectory and installed runtimes and applications are in the corresponding runtime/ and app/ subdirectories. </p>
<p> System-wide remotes can be statically preconfigured by dropping flatpakrepo files into /etc/flatpak/remotes.d/. </p>
<p> In addition to the system-wide installation in $prefix/var/lib/flatpak/, which is always considered the default one unless overridden, more system-wide installations can be defined via configuration files in /etc/flatpak/installations.d/, which must define at least the id of the installation and the absolute path to it. Other optional parameters like DisplayName, Priority or StorageType are also supported. </p>
<p> Flatpak uses OSTree to distribute and deploy data. The repositories it uses are OSTree repositories and can be manipulated with the <code>ostree</code> utility. Installed runtimes and applications are OSTree checkouts. </p>
<p> Basic commands for building flatpaks such as build-init, build and build-finish are included in the flatpak utility. For higher-level build support, see the separate <code><a href="/docs/linux/man/1-flatpak-builder/">flatpak-builder</a></code>(1) tool.</p>
<h2>OPTIONS</h2>
<p> The following global options are understood. Individual commands have their own options. </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show debug information during command processing. Use -vv for more detail.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Show OSTree debug information during command processing.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>&#8211;default-arch</code></p>
<dl>
<dt>
<dd> Print the default arch and exit.</dl>
<p> <code>&#8211;supported-arches</code></p>
<dl>
<dt>
<dd> Print the supported arches in priority order and exit.</dl>
<p> <code>&#8211;gl-drivers</code></p>
<dl>
<dt>
<dd> Print the list of active gl drivers and exit.</dl>
<p> <code>&#8211;installations</code></p>
<dl>
<dt>
<dd> Print paths of system installations and exit.</dl>
<h2>COMMANDS</h2>
<p> Commands for managing installed applications and runtimes: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1)</p>
<dl>
<dt>
<dd> Install an application or a runtime from a remote or bundle.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-update/">flatpak-update</a></code>(1)</p>
<dl>
<dt>
<dd> Update an installed application or runtime.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-uninstall/">flatpak-uninstall</a></code>(1)</p>
<dl>
<dt>
<dd> Uninstall an installed application or runtime.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-mask/">flatpak-mask</a></code>(1)</p>
<dl>
<dt>
<dd> Mask out updates and automatic installation</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-list/">flatpak-list</a></code>(1)</p>
<dl>
<dt>
<dd> List installed applications and/or runtimes.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-info/">flatpak-info</a></code>(1)</p>
<dl>
<dt>
<dd> Show information for an installed application or runtime.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-history/">flatpak-history</a></code>(1)</p>
<dl>
<dt>
<dd> Show history.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-config/">flatpak-config</a></code>(1)</p>
<dl>
<dt>
<dd> Manage flatpak configuration.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-repair/">flatpak-repair</a></code>(1)</p>
<dl>
<dt>
<dd> Repair flatpak installation.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-create-usb/">flatpak-create-usb</a></code>(1)</p>
<dl>
<dt>
<dd> Copy apps and/or runtimes onto removable media.</dl>
<p> Commands for finding applications and runtimes: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-search/">flatpak-search</a></code>(1)</p>
<dl>
<dt>
<dd> Search for applications and runtimes.</dl>
<p> Commands for running applications: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-run/">flatpak-run</a></code>(1)</p>
<dl>
<dt>
<dd> Run an application.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-kill/">flatpak-kill</a></code>(1)</p>
<dl>
<dt>
<dd> Stop a running application.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1)</p>
<dl>
<dt>
<dd> Override permissions for an application.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-make-current/">flatpak-make-current</a></code>(1)</p>
<dl>
<dt>
<dd> Specify the default version to run.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-enter/">flatpak-enter</a></code>(1)</p>
<dl>
<dt>
<dd> Enter the namespace of a running application.</dl>
<p> Commands for managing file access: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-document-export/">flatpak-document-export</a></code>(1)</p>
<dl>
<dt>
<dd> Grant an application access to a specific file.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-document-unexport/">flatpak-document-unexport</a></code>(1)</p>
<dl>
<dt>
<dd> Revoke access to a specific file.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-document-info/">flatpak-document-info</a></code>(1)</p>
<dl>
<dt>
<dd> Show information about a specific file.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-documents/">flatpak-documents</a></code>(1)</p>
<dl>
<dt>
<dd> List exported files.</dl>
<p> Commands for managing the dynamic permission store: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-permission-remove/">flatpak-permission-remove</a></code>(1)</p>
<dl>
<dt>
<dd> Remove item from permission store.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-permissions/">flatpak-permissions</a></code>(1)</p>
<dl>
<dt>
<dd> List permissions.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-permission-show/">flatpak-permission-show</a></code>(1)</p>
<dl>
<dt>
<dd> Show app permissions.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-permission-reset/">flatpak-permission-reset</a></code>(1)</p>
<dl>
<dt>
<dd> Reset app permissions.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-permission-set/">flatpak-permission-set</a></code>(1)</p>
<dl>
<dt>
<dd> Set app permissions.</dl>
<p> Commands for managing remote repositories: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1)</p>
<dl>
<dt>
<dd> List all configured remote repositories.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-remote-add/">flatpak-remote-add</a></code>(1)</p>
<dl>
<dt>
<dd> Add a new remote repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1)</p>
<dl>
<dt>
<dd> Modify properties of a configured remote repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-remote-delete/">flatpak-remote-delete</a></code>(1)</p>
<dl>
<dt>
<dd> Delete a configured remote repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-remote-ls/">flatpak-remote-ls</a></code>(1)</p>
<dl>
<dt>
<dd> List contents of a configured remote repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-remote-info/">flatpak-remote-info</a></code>(1)</p>
<dl>
<dt>
<dd> Show information about a ref in a configured remote repository.</dl>
<p> Commands for building applications: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1)</p>
<dl>
<dt>
<dd> Initialize a build directory.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1)</p>
<dl>
<dt>
<dd> Run a build command in a build directory.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1)</p>
<dl>
<dt>
<dd> Finalizes a build directory for export.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1)</p>
<dl>
<dt>
<dd> Export a build directory to a repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-bundle/">flatpak-build-bundle</a></code>(1)</p>
<dl>
<dt>
<dd> Create a bundle file from a ref in a local repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-import-bundle/">flatpak-build-import-bundle</a></code>(1)</p>
<dl>
<dt>
<dd> Import a file bundle into a local repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-sign/">flatpak-build-sign</a></code>(1)</p>
<dl>
<dt>
<dd> Sign an application or runtime after its been exported.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-update-repo/">flatpak-build-update-repo</a></code>(1)</p>
<dl>
<dt>
<dd> Update the summary file in a repository.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-build-commit-from/">flatpak-build-commit-from</a></code>(1)</p>
<dl>
<dt>
<dd> Create a new commit based on an existing ref.</dl>
<p> <code><a href="/docs/linux/man/1-flatpak-repo/">flatpak-repo</a></code>(1)</p>
<dl>
<dt>
<dd> Print information about a repo.</dl>
<p> Commands available inside the sandbox: </p>
<p> <code><a href="/docs/linux/man/1-flatpak-spawn/">flatpak-spawn</a></code>(1)</p>
<dl>
<dt>
<dd> Run a command in another sandbox.</dl>
<h2>FILE FORMATS</h2>
<p> File formats that are used by Flatpak commands: </p>
<p> <code><a href="/docs/linux/man/5-flatpak-flatpakref/">flatpak-flatpakref</a></code>(5)</p>
<dl>
<dt>
<dd> Reference to a remote for an application or runtime</dl>
<p> <code><a href="/docs/linux/man/5-flatpak-flatpakrepo/">flatpak-flatpakrepo</a></code>(5)</p>
<dl>
<dt>
<dd> Reference to a remote</dl>
<p> <code><a href="/docs/linux/man/5-flatpak-remote/">flatpak-remote</a></code>(5)</p>
<dl>
<dt>
<dd> Configuration for a remote</dl>
<p> <code><a href="/docs/linux/man/5-flatpak-installation/">flatpak-installation</a></code>(5)</p>
<dl>
<dt>
<dd> Configuration for an installation location</dl>
<p> <code><a href="/docs/linux/man/5-flatpak-metadata/">flatpak-metadata</a></code>(5)</p>
<dl>
<dt>
<dd> Information about an application or runtime</dl>
<h2>ENVIRONMENT</h2>
<p> Besides standard environment variables such as <code>XDG_DATA_DIRS</code> and <code>XDG_DATA_HOME</code>, flatpak is consulting some of its own. </p>
<p> <code>FLATPAK_USER_DIR</code></p>
<dl>
<dt>
<dd> The location of the per-user installation. If this is not set, $XDG_DATA_HOME/flatpak is used.</dl>
<p> <code>FLATPAK_SYSTEM_DIR</code></p>
<dl>
<dt>
<dd> The location of the default system-wide installation. If this is not set, /var/lib/flatpak is used (unless overridden at build time by &#8211;localstatedir or &#8211;with-system-install-dir).</dl>
<p> <code>FLATPAK_SYSTEM_CACHE_DIR</code></p>
<dl>
<dt>
<dd> The location where temporary child repositories will be created during pulls into the system-wide installation. If this is not set, a directory in /var/tmp/ is used. This is useful because it is more likely to be on the same filesystem as the system repository (thus increasing the chances for e.g. reflink copying), and we can avoid filling the user&#8217;s home directory with temporary data.</dl>
<p> <code>FLATPAK_CONFIG_DIR</code></p>
<dl>
<dt>
<dd> The location of flatpak site configuration. If this is not set, /etc/flatpak is used (unless overridden at build time by &#8211;sysconfdir).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/5-ostree-repo/">ostree.repo</a></code>(5), <code><a href="/docs/linux/man/5-flatpak-remote/">flatpak-remote</a></code>(5), <code><a href="/docs/linux/man/5-flatpak-installation/">flatpak-installation</a></code>(5), m[blue]<code><a rel="nofollow" href="https://www.flatpak.org">https://www.flatpak.org</a></code>m[] </p>
<h2>Index</h2>
