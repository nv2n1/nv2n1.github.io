---
title: "dpkg-checkbuilddeps(1)"
name: "dpkg-checkbuilddeps"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-checkbuilddeps/"
description: "dpkg-checkbuilddeps – check build dependencies and conflicts"
---

<h2 class="name">NAME</h2>
<p> dpkg-checkbuilddeps &#8211; check build dependencies and conflicts </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-checkbuilddeps</code> [<i>option</i>&#8230;] [<i>control-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program checks the installed packages in the system against the build dependencies and build conflicts listed in the control file. If any are not met, it displays them and exits with a nonzero return code. </p>
<p> By default, <code>debian/control</code> is read, but an alternate control filename may be specified on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir=</code><i>dir</i></p>
<dd> Change the location of the <code>dpkg</code> database (since dpkg 1.14.0). The default location is <i>/var/lib/dpkg</i>.</p>
<dt><code>-A</code></p>
<dd> Ignore <code>Build-Depends-Arch</code> and <code>Build-Conflicts-Arch</code> lines (since dpkg 1.16.4). Use when only arch-indep packages will be built, or combine with <code>-B</code> when only a source package is to be built.</p>
<dt><code>-B</code></p>
<dd> Ignore <code>Build-Depends-Indep</code> and <code>Build-Conflicts-Indep</code> lines. Use when only arch-dep packages will be built, or combine with <code>-A</code> when only a source package is to be built.</p>
<dt><code>-I</code></p>
<dd> Ignore built-in build depends and conflicts (since dpkg 1.18.2). These are implicit dependencies that are usually required on a specific distribution, the so called Build-Essential package set.</p>
<dt><code>-d</code> <i>build-depends-string</i></p>
<dd>
<dt><code>-c</code> <i>build-conflicts-string</i></p>
<dd> Use the given build dependencies/conflicts instead of those contained in the <i>debian/control</i> file (since dpkg 1.14.17).</p>
<dt><code>-a</code> <i>arch</i></p>
<dd> Check build dependencies/conflicts assuming that the package described in the control file is to be built for the given host architecture instead of the architecture of the current system (since dpkg 1.16.2).</p>
<dt><code>-P</code> <i>profile</i>[<code>,</code>&#8230;]</p>
<dd> Check build dependencies/conflicts assuming that the package described in the control file is to be built for the given build profile(s) (since dpkg 1.17.2). The argument is a comma-separated list of profile names.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font></p>
<dd> If set, it will be used as the active build profile(s) for the package being built. It is a space separated list of profile names. Overridden by the <code>-P</code> option.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default). </p>
</dl>
<h2>Index</h2>
