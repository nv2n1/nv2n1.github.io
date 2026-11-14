---
title: "flatpak-build-sign(1)"
name: "flatpak-build-sign"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-sign/"
description: "flatpak-build-sign – Sign an application or runtime"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-sign &#8211; Sign an application or runtime </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-sign</code> [OPTION&#8230;] LOCATION ID [BRANCH]</dl>
<h2>DESCRIPTION</h2>
<dd>Signs the commit for a specified application or runtime in a local repository. LOCATION is the location of the repository. ID is the name of the application, or runtime if &#8211;runtime is specified. If BRANCH is not specified, it is assumed to be &quot;master&quot;. </p>
<p> Applications can also be signed during build-export, but it is sometimes useful to add additional signatures later.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;gpg-sign=KEYID</code></p>
<dl>
<dt>
<dd> Sign the commit with this GPG key. This option can be used multiple times.</dl>
<p> <code>&#8211;gpg-homedir=PATH</code></p>
<dl>
<dt>
<dd> GPG Homedir to use when looking for keyrings</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Sign a runtime instead of an app.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to use. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build-sign &#8211;gpg-sign=D8BA6573DDD2418027736F1BC33B315E53C1E9D6 /some/repo org.my.App</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), </p>
<h2>Index</h2>
