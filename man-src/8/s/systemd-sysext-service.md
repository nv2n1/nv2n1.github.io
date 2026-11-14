---
title: "systemd-sysext-service(8)"
name: "systemd-sysext-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-sysext-service/"
description: "systemd-sysext, systemd-sysext.service – Activates System Extension Images"
---

<p>systemd-sysext, systemd-sysext.service &#8211; Activates System Extension Images</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-sysext</code> [OPTIONS&#8230;]</dl>
<pre><dd>systemd-sysext.service</pre>
<h2>Description</h2>
<p><code>systemd-sysext</code> activates/deactivates system extension images. System extension images may &#8211; dynamically at runtime &#8212; extend the /usr/ and /opt/ directory hierarchies with additional files. This is particularly useful on immutable system images where a /usr/ and/or /opt/ hierarchy residing on a read-only file system shall be extended temporarily at runtime without making any persistent modifications. </p>
<p> System extension images should contain files and directories similar in fashion to regular operating system tree. When one or more system extension images are activated, their /usr/ and /opt/ hierarchies are combined via &quot;overlayfs&quot; with the same hierarchies of the host OS, and the host /usr/ and /opt/ overmounted with it (&quot;merging&quot;). When they are deactivated, the mount point is disassembled &#8212; again revealing the unmodified original host version of the hierarchy (&quot;unmerging&quot;). Merging thus makes the extension&#8217;s resources suddenly appear below the /usr/ and /opt/ hierarchies as if they were included in the base OS image itself. Unmerging makes them disappear again, leaving in place only the files that were shipped with the base OS image itself. </p>
<p> Files and directories contained in the extension images outside of the /usr/ and /opt/ hierarchies are <i>not</i> merged, and hence have no effect when included in a system extension image. In particular, files in the /etc/ and /var/ included in a system extension image will <i>not</i> appear in the respective hierarchies after activation. </p>
<p> System extension images are strictly read-only, and the host /usr/ and /opt/ hierarchies become read-only too while they are activated. </p>
<p> System extensions are supposed to be purely additive, i.e. they are supposed to include only files that do not exist in the underlying basic OS image. However, the underlying mechanism (overlayfs) also allows removing files, but it is recommended not to make use of this. </p>
<p> System extension images may be provided in the following formats: </p>
<dl>
<dd>1. Plain directories or btrfs subvolumes containing the OS tree</dl>
<dl>
<dd>2. Disk images with a GPT disk label, following the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font></dl>
<dl>
<dd>3. Disk images lacking a partition table, with a naked Linux file system (e.g. squashfs or ext4)</dl>
<p> These image formats are the same ones that <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) supports via it&#8217;s <code>&#8211;directory=</code>/<code>&#8211;image=</code> switches and those that the service manager supports via <code>RootDirectory=</code>/<code>RootImage=</code>. Similar to them they may optionally carry Verity authentication information. </p>
<p> System extensions are automatically looked for in the directories /etc/extensions/, /run/extensions/, /var/lib/extensions/, /usr/lib/extensions/ and /usr/local/lib/extensions/. The first two listed directories are not suitable for carrying large binary images, however are still useful for carrying symlinks to them. The primary place for installing system extensions is /var/lib/extensions/. Any directories found in these search directories are considered directory based extension images, any files with the .raw suffix are considered disk image based extension images. </p>
<p> During boot OS extension images are activated automatically, if the systemd-sysext.service is enabled. Note that this service runs only after the underlying file systems where system extensions are searched are mounted. This means they are not suitable for shipping resources that are processed by subsystems running in earliest boot. Specifically, OS extension images are not suitable for shipping system services or <code><a href="/docs/linux/man/8-systemd-sysusers/">systemd-sysusers</a></code>(8) definitions. See m[blue]<code>Portable Services</code>m[]<font SIZE="-2">[2]</font> for a simple mechanism for shipping system services in disk images, in a similar fashion to OS extensions. Note the different isolation on these two mechanisms: while system extension directly extend the underlying OS image with additional files that appear in a way very similar to as if they were shipped in the OS image itself and thus imply no security isolation, portable services imply service level sandboxing in one way or another. The systemd-sysext.service service is guaranteed to finish start-up before basic.target is reached; i.e. at the time regular services initialize (those which do not use <i>DefaultDependencies=no</i>), the files and directories system extensions provide are available in /usr/ and /opt/ and may be accessed. </p>
<p> Note that there is no concept of enabling/disabling installed system extension images: all installed extension images are automatically activated at boot. </p>
<p> A simple mechanism for version compatibility is enforced: a system extension image must carry a /usr/lib/extension-release.d/extension-release.<i>$name</i> file, which must match its image name, that is compared with the host os-release file: the contained <i>ID=</i> fields have to match, as well as the <i>SYSEXT_LEVEL=</i> field (if defined). If the latter is not defined, the <i>VERSION_ID=</i> field has to match instead. System extensions should not ship a /usr/lib/os-release file (as that would be merged into the host /usr/ tree, overriding the host OS version data, which is not desirable). The extension-release file follows the same format and semantics, and carries the same content, as the os-release file of the OS, but it describes the resources carried in the extension image.</p>
<h2>Uses</h2>
<p>The primary use case for system images are immutable environments where debugging and development tools shall optionally be made available, but not included in the immutable base OS image itself (e.g. <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1) and <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) shall be an optionally installable addition in order to make debugging/development easier). System extension images should not be misunderstood as a generic software packaging framework, as no dependency scheme is available: system extensions should carry all files they need themselves, except for those already shipped in the underlying host system image. Typically, system extension images are built at the same time as the base OS image &#8212; within the same build system. </p>
<p> Another use case for the system extension concept is temporarily overriding OS supplied resources with newer ones, for example to install a locally compiled development version of some low-level component over the immutable OS image without doing a full OS rebuild or modifying the nominally immutable image. (e.g. &quot;install&quot; a locally built package with <code>DESTDIR=/var/lib/extensions/mytest make install &amp;&amp; systemd-sysext refresh</code>, making it available in /usr/ as if it was installed in the OS image itself.) This case works regardless if the underlying host /usr/ is managed as immutable disk image or is a traditional package manager controlled (i.e. writable) tree.</p>
<h2>Commands</h2>
<p>The following commands are understood: </p>
<p> <code>status</code></p>
<dl>
<dd>When invoked without any command verb, or when <code>status</code> is specified the current merge status is shown, separately for both /usr/ and /opt/.</dl>
<p> <code>merge</code></p>
<dl>
<dd>Merges all currently installed system extension images into /usr/ and /opt/, by overmounting these hierarchies with an &quot;overlayfs&quot; file system combining the underlying hierarchies with those included in the extension images. This command will fail if the hierarchies are already merged.</dl>
<p> <code>unmerge</code></p>
<dl>
<dd>Unmerges all currently installed system extension images from /usr/ and /opt/, by unmounting the &quot;overlayfs&quot; file systems created by <code>merge</code> prior.</dl>
<p> <code>refresh</code></p>
<dl>
<dd>A combination of <code>unmerge</code> and <code>merge</code>: if already mounted the existing &quot;overlayfs&quot; instance is unmounted temporarily, and then replaced by a new version. This command is useful after installing/removing system extension images, in order to update the &quot;overlayfs&quot; file system accordingly. If no system extensions are installed when this command is executed, the equivalent of <code>unmerge</code> is executed, without establishing any new &quot;overlayfs&quot; instance. Note that currently there&#8217;s a brief moment where neither the old nor the new &quot;overlayfs&quot; file system is mounted. This implies that all resources supplied by a system extension will briefly disappear &#8212; even if it exists continuously during the refresh operation.</dl>
<p> <code>list</code></p>
<dl>
<dd>A brief list of installed extension images is shown.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Options</h2>
<p><code>&#8211;root=</code></p>
<dl>
<dd>Operate relative to the specified root directory, i.e. establish the &quot;overlayfs&quot; mount not on the top-level host /usr/ and /opt/ hierarchies, but below some specified root directory.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dd>When merging system extensions into /usr/ and /opt/, ignore version incompatibilities, i.e. force merging regardless of whether the version information included in the extension images matches the host or not.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dd>Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dd>Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>&#8211;json=</code><i>MODE</i></p>
<dl>
<dd>Shows output formatted as JSON. Expects one of &quot;short&quot; (for the shortest possible output without any redundant whitespace or line breaks), &quot;pretty&quot; (for a pretty version of the same, with indentation and line breaks) or &quot;off&quot; (to turn off JSON output, the default).</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Discoverable Partitions Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/DISCOVERABLE_PARTITIONS">https://systemd.io/DISCOVERABLE_PARTITIONS</a></dl>
<dt> 2.</p>
<dd>Portable Services</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/PORTABLE_SERVICES">https://systemd.io/PORTABLE_SERVICES</a></dl>
