---
title: "flatpak-build-bundle(1)"
name: "flatpak-build-bundle"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-bundle/"
description: "flatpak-build-bundle – Create a single-file bundle from a local repository"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-bundle &#8211; Create a single-file bundle from a local repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-bundle</code> [OPTION&#8230;] LOCATION FILENAME NAME [BRANCH]</dl>
<h2>DESCRIPTION</h2>
<dd>Creates a single-file named FILENAME for the application (or runtime) named NAME in the repository at LOCATION. If a BRANCH is specified, this branch of the application is used. </p>
<p> The collection ID set on the repository at LOCATION (if set) will be used for the bundle. </p>
<p> The format of the bundle file is that of an ostree static delta (against an empty base) with some flatpak specific metadata for the application icons and appdata.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Export a runtime instead of an application.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The arch to create a bundle for. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>&#8211;repo-url=URL</code></p>
<dl>
<dt>
<dd> The URL for the repository from which the application can be updated. Installing the bundle will automatically configure a remote for this URL.</dl>
<p> <code>&#8211;runtime-repo=URL</code></p>
<dl>
<dt>
<dd> The URL for a .flatpakrepo file that contains the information about the repository that supplies the runtimes required by the app.</dl>
<p> <code>&#8211;gpg-keys=FILE</code></p>
<dl>
<dt>
<dd> Add the GPG key from FILE (use &#8211; for stdin).</dl>
<p> <code>&#8211;gpg-homedir=PATH</code></p>
<dl>
<dt>
<dd> GPG Homedir to use when looking for keyrings.</dl>
<p> <code>&#8211;from-commit=COMMIT</code></p>
<dl>
<dt>
<dd> The OSTree commit to create a delta bundle from.</dl>
<p> <code>&#8211;oci</code></p>
<dl>
<dt>
<dd> Export to an OCI image instead of a Flatpak bundle.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build-bundle /var/lib/flatpak/repo gnome-calculator.flatpak org.gnome.Calculator stable</code> </p>
<p> <code>$ flatpak build-bundle ~/.local/share/flatpak/repo gnome-calculator.flatpak org.gnome.Calculator stable</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-import-bundle/">flatpak-build-import-bundle</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-update-repo/">flatpak-build-update-repo</a></code>(1) </p>
<h2>Index</h2>
