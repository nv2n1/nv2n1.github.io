---
title: "flatpak-repair(1)"
name: "flatpak-repair"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-repair/"
description: "flatpak-repair – Repair a flatpak installation"
---

<h2 class="name">NAME</h2>
<p> flatpak-repair &#8211; Repair a flatpak installation </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak repair</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Repair a flatpak installation by pruning and reinstalling invalid objects. The repair command does all of the following: </p>
<dl>
<dt>
<dd> &bull; Scan all locally available refs, removing any that don&#8217;t correspond to a deployed ref.</dl>
<dl>
<dt>
<dd> &bull; Verify each commit they point to, removing any invalid objects and noting any missing objects.</dl>
<dl>
<dt>
<dd> &bull; Remove any refs that had an invalid object, and any non-partial refs that had missing objects.</dl>
<dl>
<dt>
<dd> &bull; Prune all objects not referenced by a ref, which gets rid of any possibly invalid non-scanned objects.</dl>
<dl>
<dt>
<dd> &bull; Enumerate all deployed refs and re-install any that are not in the repo (or are partial for a non-subdir deploy).</dl>
<p> Note that <code>flatpak repair</code> has to be run with root privileges to operate on the system installation. </p>
<p> An alternative command for repairing OSTree repositories is ostree fsck.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Repair per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Repair system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Repair the system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using &#8211;installation=default is equivalent to using &#8211;system.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Only report inconsistencies, don&#8217;t make any changes</dl>
<p> <code>&#8211;reinstall-all</code></p>
<dl>
<dt>
<dd> Reinstall all refs, regardless of whether they were removed from the repo or not</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ sudo flatpak repair</code> </p>
<p> <code>$ flatpak repair &#8211;user</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-ostree-fsck/">ostree-fsck</a></code>(1) </p>
<h2>Index</h2>
