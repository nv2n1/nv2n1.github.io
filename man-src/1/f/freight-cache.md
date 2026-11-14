---
title: "freight-cache(1)"
name: "freight-cache"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freight-cache/"
description: "freight-cache – (re)builds package repositories"
---

<h2>NAME</h2>
<p> <code>freight-cache</code> &#8211; (re)builds package repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>freight cache</code> [<code>-k</code>] [<code>-g</code> <i>email</i>] [<code>-p</code> <i>passphrase file</i>] [<code>-c</code> <i>conf</i>] [<code>-v</code>] [<code>-h</code>] [<i>manager</i>/<i>distro</i>][&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>freight-cache</code> converts each <i>manager</i>/<i>distro</i> given into a package repository (only Debian archives are supported currently). The <i>manager</i> indicates the type of repository (again, <code>apt</code> is the only supported value). The <i>distro</i> is an arbitrary string that should match a release of the target operating system (for example, &quot;lenny&quot; or &quot;lucid&quot;). If none are given, <code>freight-cache</code> converts all <i>manager</i>/<i>distro</i> pairs found in <code>$VARLIB</code>. </p>
<p> Packages are read from the Freight library (<code>$VARLIB</code> in the configuration, see <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5)) and organized into a working repository in the Freight cache (<code>$VARCACHE</code> in the configuration). </p>
<p> Serving the repositories is left as an exercise for the reader. The Freight cache is the only directory that needs to be exposed, so create a virtual host with <code>$VARCACHE</code> as its document root and everything will be fine. </p>
<p> From version 0.0.8 onwards, distros in an APT repository no longer share the contents of the <code>pool/</code>. After upgrading to this version and running <code>freight-cache</code> for all your distros, it is safe and recommended to <code>rm -rf $VARCACHE/pool/main</code> to reset link counts to the proper value.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep unreferenced versions of packages. This is different than keeping multiple versions of a package in the repository, which is supported without any special options.</p>
<dt><code>-g</code> <i>email</i>, <code>&#8211;gpg=</code><i>email</i></p>
<dd> Use an alternate GPG key. May be given multiple times.</p>
<dt><code>-p</code> <i>passphrase file</i>, <code>&#8211;passphrase-file=</code><i>passphrase file</i></p>
<dd> Use an alternate file containing the GPG key passphrase. This file should obviously be protected and only readable by the user running Freight.</p>
<dt><code>-a</code> <i>digest algorithm</i>, <code>&#8211;digest-algo=</code><i>digest algorithm</i></p>
<dd> Message digest algorithm that GPG should use to sign the repository, e.g SHA512</p>
<dt><code>-c</code> <i>conf</i>, <code>&#8211;conf=</code><i>conf</i></p>
<dd> Use an alternate configuration file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/freight.conf</i>, <i>~/.freight.conf</i>, <i>etc/freight.conf</i>, <i>.freight.conf</i></p>
<dd> The default configuration files. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</p>
<dt><i>$VARCACHE</i><code>/pubkey.gpg</code></p>
<dd> The exported public key used for signing each release.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>FREIGHT_CONF</code></p>
<dd> The pathname of an alternate configuration file. See <code><a href="/docs/linux/man/5-freight/">freight</a></code>(5).</dl>
<h2>THEME SONG</h2>
<p> The New Pornographers &#8211; &quot;All the Old Showstoppers&quot;</p>
<h2>AUTHOR</h2>
<p> Richard Crowley <i>r@rcrowley.org</i></p>
<h2>SEE ALSO</h2>
<p> Part of <code><a href="/docs/linux/man/1-freight/">freight</a></code>(1). </p>
<p> <code><a href="/docs/linux/man/1-freight-add/">freight-add</a></code>(1) adds packages to the intermediate &quot;Freight library&quot; that is used by <code>freight-cache</code> to build the actual repositories. </p>
<h2>Index</h2>
