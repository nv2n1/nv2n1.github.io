---
title: "dpkg-repack(1)"
name: "dpkg-repack"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-repack/"
description: "dpkg-repack – put an unpacked .deb file back together"
---

<h2 class="name">NAME</h2>
<p> dpkg-repack &#8211; put an unpacked .deb file back together </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-repack</code> [<code>&#8211;root=dir</code>] [<code>&#8211;arch=architecture</code>] [<code>&#8211;generate</code>] <code>packagename</code> [<code>packagename &#8230;</code>] </p>
<h2>DESCRIPTION</h2>
<p> <i>dpkg-repack</i> creates a .deb file out of a Debian package that has already been installed on your system. </p>
<p> If any changes have been made to the package while it was unpacked (ie, conffiles files in /etc modified), the new package will inherit the changes. (There are exceptions to this, including changes to configuration files that are not conffiles, including those managed by ucf.) </p>
<p> This utility can make it easy to copy packages from one computer to another, or to recreate packages that are installed on your system, but no longer available elsewhere. </p>
<p> Note: <i>dpkg-repack</i> will place the created package in the current directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;root=dir</i></p>
<dd> Take package from filesystem rooted on &lt;dir&gt;. This is useful if, for example, you have another computer nfs mounted on /mnt, then you can use &#8211;root=/mnt to reassemble packages from that computer. </p>
<dt><i>&#8211;arch=architecture</i></p>
<dd> Make the package be for a different architecture. <i>dpkg-repack</i> cannot tell if an installed package is architecture all or is specific to the system&#8217;s architecture, so by default it uses <code>dpkg &#8211;print-architecture</code> to determine the build architecture. If you know the package is architecture all, you can use this option to force <i>dpkg-repack</i> to use the right architecture. </p>
<dt><i>&#8211;generate</i></p>
<dd> Generate a temporary directory suitable for building a package from, but do not actually create the package. This is useful if you want to move files around in the package before building it. The package can be built from this temporary directory by running &quot;dpkg &#8211;build&quot;, passing it the generated directory. </p>
<dt><i>packagename</i></p>
<dd> The name of the package to attempt to repack. Multiple packages can be listed. </p>
</dl>
<h2>BUGS</h2>
<p> This program accesses the dpkg database directly in places, querying for data that cannot be gotten via dpkg. </p>
<p> There is a tricky situation that can occur if you dpkg-repack a package that has modified conffiles. The modified conffiles are packed up. Now if you install the package, dpkg does not realize that the conffiles in it are modified. So if you later upgrade to a new version of the package, dpkg will believe that the old (repacked) package has older conffiles than the new version, and will silently replace the conffiles with those in the package you are upgrading to. </p>
<p> While dpkg-repack can be run under fakeroot and will work most of the time, fakeroot -u must be used if any of the files to be repacked are owned by non-root users. Otherwise the package will have them owned by root. dpkg-repack will warn if you run it under fakeroot without the -u flag. </p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
