---
title: "deb-src-rules(5)"
name: "deb-src-rules"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-src-rules/"
description: "deb-src-rules – Debian source package rules file"
---

<p>deb-src-rules &#8211; Debian source package rules file</p>
<h2>Synopsis</h2>
<p><code>debian/rules</code></p>
<h2>Description</h2>
<p>This file contains the instructions necessary to build the binary packages from the source package. </p>
<p> The <i>debian/rules</i> file is an executable Makefile, with a shebang that is usually set to &#8220;#!/usr/bin/make -f&#8221;. </p>
<p> It must support the following make targets:</p>
<dl>
<dt><code>clean</code></p>
<dd>Clean up the source tree, by undoing any change done by any of the build and binary targets. This target will be called with root privileges.</p>
<dt><code>build-indep</code></p>
<dd>Build architecture independent files required to build any architecture independent binary package. If there are no architecture independent binary packages to generate, the target must still exist but do nothing. This target must not require root privileges.</p>
<dt><code>build-arch</code></p>
<dd>Build architecture dependent files required to build any architecture dependent binary package. If there are no architecture dependent binary packages to generate, the target must still exist but do nothing. This target must not require root privileges.</p>
<dt><code>build</code></p>
<dd>Build architecture independent and dependent files, either by depending (at least transitively) on <code>build-indep</code> and/or <code>build-arch</code> or by inlining what those targets would do. This target must not require root privileges.</p>
<dt><code>binary-indep</code></p>
<dd>Build architecture independent binary packages. This target must depend (at least transitively) on either <code>build-indep</code> or <code>build</code>. This target will be called with root privileges.</p>
<dt><code>binary-arch</code></p>
<dd>Build architecture dependent binary packages. This target must depend (at least transitively) on either <code>build-arch</code> or <code>build</code>. This target will be called with root privileges.</p>
<dt><code>binary</code></p>
<dd>Build architecture independent and dependent binary packages, either by depending (at least transitively) on <code>binary-indep</code> and/or <code>binary-arch</code> or by inlining what those targets would do. This target will be called with root privileges.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-architecture/">dpkg-architecture</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-vendor/">dpkg-vendor</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-distaddfile/">dpkg-distaddfile</a></code>(1). </p>
