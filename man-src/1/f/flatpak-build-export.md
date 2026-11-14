---
title: "flatpak-build-export(1)"
name: "flatpak-build-export"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-export/"
description: "flatpak-build-export – Create a repository from a build directory"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-export &#8211; Create a repository from a build directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-export</code> [OPTION&#8230;] LOCATION DIRECTORY [BRANCH]</dl>
<h2>DESCRIPTION</h2>
<dd>Creates or updates a repository with an application build. LOCATION is the location of the repository. DIRECTORY must be a finalized build directory. If BRANCH is not specified, it is assumed to be &quot;master&quot;. </p>
<p> If LOCATION exists, it is assumed to be an OSTree repository, otherwise a new OSTree repository is created at this location. The repository can be inspected with the <code>ostree</code> tool. </p>
<p> The contents of DIRECTORY are committed on the branch with name app/APPNAME/ARCH/BRANCH, where ARCH is the architecture of the runtime that the application is using. A commit filter is used to enforce that only the contents of the files/ and export/ subdirectories and the metadata file are included in the commit, anything else is ignored. </p>
<p> When exporting a flatpak to be published to the internet, <code>&#8211;collection-id=COLLECTION-ID</code> should be specified as a globally unique reverse DNS value to identify the collection of flatpaks this will be added to. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration. </p>
<p> The build-update-repo command should be used to update repository metadata whenever application builds are added to a repository.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>-s</code>, <code>&#8211;subject=SUBJECT</code></p>
<dl>
<dt>
<dd> One line subject for the commit message.</dl>
<p> <code>-b</code>, <code>&#8211;body=BODY</code></p>
<dl>
<dt>
<dd> Full description for the commit message.</dl>
<p> <code>&#8211;collection-id=COLLECTION-ID</code></p>
<dl>
<dt>
<dd> Set as the collection ID of the repository. Setting a globally unique collection ID allows the apps in the repository to be shared over peer to peer systems without needing further configuration. If exporting to an existing repository, the collection ID must match the existing configured collection ID for that repository.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> Specify the architecture component of the branch to export. Only host compatible architectures can be specified; see <code>flatpak &#8211;supported-arches</code> for valid values.</dl>
<p> <code>&#8211;exclude=PATTERN</code></p>
<dl>
<dt>
<dd> Exclude files matching PATTERN from the commit. This option can be used multiple times.</dl>
<p> <code>&#8211;include=PATTERN</code></p>
<dl>
<dt>
<dd> Don&#8217;t exclude files matching PATTERN from the commit, even if they match the <code>&#8211;export</code> patterns. This option can be used multiple times.</dl>
<p> <code>&#8211;metadata=FILENAME</code></p>
<dl>
<dt>
<dd> Use the specified filename as metadata in the exported app instead of the default file (called metadata). This is useful if you want to commit multiple things from a single build tree, typically used in combination with <code>&#8211;files</code> and <code>&#8211;exclude</code>.</dl>
<p> <code>&#8211;files=SUBDIR</code></p>
<dl>
<dt>
<dd> Use the files in the specified subdirectory as the file contents, rather than the regular files directory.</dl>
<p> <code>&#8211;timestamp=DATE</code></p>
<dl>
<dt>
<dd> Use the specified ISO 8601 formatted date or NOW, for the current time, in the commit metadata and, if <code>&#8211;update-appstream</code> is used, the appstream data.</dl>
<p> <code>&#8211;end-of-life=REASON</code></p>
<dl>
<dt>
<dd> Mark the build as end-of-life. REASON is a message that may be shown to users installing this build.</dl>
<p> <code>&#8211;end-of-life-rebase=ID</code></p>
<dl>
<dt>
<dd> Mark the build as end-of-life. Unlike <code>&#8211;end-of-life</code>, this one takes an ID that supersedes the current one. By the user&#8217;s request, the application data may be preserved for the new application.</dl>
<p> <code>&#8211;disable-fsync</code></p>
<dl>
<dt>
<dd> Don&#8217;t fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.</dl>
<p> <code>&#8211;update-appstream</code></p>
<dl>
<dt>
<dd> Update the appstream branch after the build.</dl>
<p> <code>&#8211;no-update-summary</code></p>
<dl>
<dt>
<dd> Don&#8217;t update the summary file after the new commit is added. This means the repository will not be useful for serving over http until build-update-repo has been run. This is useful is you want to do multiple repo operations before finally updating the summary.</dl>
<p> <code>&#8211;gpg-sign=KEYID</code></p>
<dl>
<dt>
<dd> Sign the commit with this GPG key. This option can be used multiple times.</dl>
<p> <code>&#8211;gpg-homedir=PATH</code></p>
<dl>
<dt>
<dd> GPG Homedir to use when looking for keyrings</dl>
<p> <code>-r</code>, <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Export a runtime instead of an app (this uses the usr subdir as files).</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build-export ~/repos/gnome-calculator/ ~/build/gnome-calculator/ org.gnome.Calculator</code> </p>
<dl>
<dt>
<dd>
<pre>
Commit: 9d0044ea480297114d03aec85c3d7ae3779438f9d2cb69d717fb54237acacb8c
Metadata Total: 605
Metadata Written: 5
Content Total: 1174
Content Written: 1
Content Bytes Written: 305
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-sign/">flatpak-build-sign</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-update-repo/">flatpak-build-update-repo</a></code>(1) </p>
<h2>Index</h2>
