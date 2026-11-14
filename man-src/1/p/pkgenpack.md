---
title: "pkgenpack(1)"
name: "pkgenpack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkgenpack/"
description: "pkgenpack – PackageKit Pack Generator"
---

<h2 class="name">NAME</h2>
<p> pkgenpack &#8211; PackageKit Pack Generator </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkgenpack</code> [<code>&#8211;help</code>] [<code>&#8211;verbose</code>] [<code>&#8211;with-package-list</code>] [<code>&#8211;output</code>] [<code>&#8211;package</code>] [<code>&#8211;updates</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>pkgenpack</code> command. </p>
<p> <code>pkgenpack</code> is the command line client for PackageKit for creating service packs.</p>
<h2>WHAT IS A SERVICE PACK?</h2>
<p> A service pack is a tarball which contains a set of packages and their dependencies. The user can reduce the dependencies to be packed using the &#8211;with-package-list option. Along with the dependencies, a service pack has a file named metadata.conf which contains the information about the distribution and creation date of the pack.</p>
<h2>CREATING A SERVICE PACK?</h2>
<p> A service pack is created using the command <code>pkgenpack</code>.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show extra debugging information.</dl>
<p> <code>&#8211;with-package-list</code></p>
<dl>
<dt>
<dd> Set the filename of dependencies to be excluded. </p>
<p> Generally, the file list of packages is generated when doing a PackageKit refresh on the target system. If not specified, <code>pkgenpack</code> uses /var/lib/PackageKit/system.package-list by default.</dl>
<p> <code>&#8211;output</code></p>
<dl>
<dt>
<dd> The directory to put the pack file, or the current directory if omitted.</dl>
<p> <code>&#8211;package</code></p>
<dl>
<dt>
<dd> The package to be put into the ServicePack.</dl>
<p> <code>&#8211;update</code></p>
<dl>
<dt>
<dd> Put all updates available in the ServicePack.</dl>
<h2>NAMING A SERVICE PACK</h2>
<p> The only valid extension for a service pack is &quot;.servicepack&quot;.</p>
<h2>EXAMPLES</h2>
<p> 1. Tim is facing problems with his Internet connection at home. He needs a service pack with valgrind and it&#8217;s dependencies for his system. He asks James to generate a pack for him. Both know James&#8217;s system should contain similar packages as Tim&#8217;s system, as both of them have installed Fedora 9 two days ago. </p>
<p> James simply runs: </p>
<dl>
<dt>
<dd>
<pre><code>
[james[at] jamesbook:~] $ pkgenpack-- output = / media / USB / TimPacks-- package = valgrind
</code></pre>
</dl>
<p> This generates a file /media/USB/TimPacks/valgrind-fedora-9-i686.servicepack on the USB key Tim gave to James. Tim can now go home, insert the USB key and double clicks on the valgrind-fedora-9-i686.servicepack file to be prompted to install these packages. </p>
<p> 2. Bill wants to create a service pack named kdegames-fedora-9-i686.servicepack for his new system which does not have an internet connection. He generates a list of packages on his system using <code>pkcon list-create</code> and copies that list to his USB key. He then gives that USB to Rishi who has a good internet connectivity. Rishi runs the following command on his system: </p>
<dl>
<dt>
<dd>
[rishi[at] devils &#8211; temple:~] $ pkgenpack&#8211; with &#8211; package &#8211; list = / media / USB / bill.package &#8211; list&#8211; output = / home / rishi / Desktop&#8211; program = kdegames
</dl>
<p> This generates a service pack, kdegames-fedora-9-i686.servicepack, on Rishi&#8217;s Desktop, which can be distributed to Bill and users with similar requirements.</p>
<h2>INSTALLING A SERVICE PACK</h2>
<p> Service Packs can be installed using pkcon. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
[hacker[at] tim - lounge:~] $ pkcon install / media / USB / TimPacks / valgrind - fedora - 9 - i686.servicepack
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code>pkmon</code> (1). <code><a href="/docs/linux/man/1-pkcon/">pkcon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shishir Goel crazyontheedge [at] gmail.com and Richard Hughes richard [at] hughsie.com.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Shishir Goel </p>
<h2>Index</h2>
