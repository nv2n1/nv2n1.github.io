---
title: "storagectl(1)"
name: "storagectl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-storagectl/"
description: "storagectl – The storaged command line tool"
---

<h2 class="name">NAME</h2>
<p> storagectl &#8211; The storaged command line tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>storagectl</code> status</p>
<dt> <code>storagectl</code> info {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>}</p>
<dt> <code>storagectl</code> mount {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;filesystem-type&nbsp;<wbr><i>TYPE</i>] [&#8211;options&nbsp;<wbr><i>OPTIONS</i>&#8230;] [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> unmount {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;force] [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> unlock {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> lock {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> loop-setup &#8211;file&nbsp;<wbr><i>PATH</i> [&#8211;read-only] [&#8211;offset&nbsp;<wbr><i>OFFSET</i>] [&#8211;size&nbsp;<wbr><i>SIZE</i>] [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> loop-delete {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> power-off {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> smart-simulate &#8211;file&nbsp;<wbr><i>PATH</i> {&#8211;object-path&nbsp;<wbr><i>OBJECT</i> | &#8211;block-device&nbsp;<wbr><i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>storagectl</code> monitor</p>
<dt> <code>storagectl</code> dump</p>
<dt> <code>storagectl</code> help</dl>
<h2>DESCRIPTION</h2>
<p> <code>storagectl</code></p>
<dd>is a command-line program used to interact with the <code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8) daemon process.</p>
<h2>COMMANDS</h2>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Shows high-level information about disk drives and block devices.</dl>
<p> <code>info</code></p>
<dl>
<dt>
<dd> Shows detailed information about <i>OBJECT</i> or <i>DEVICE</i>.</dl>
<p> <code>mount</code></p>
<dl>
<dt>
<dd> Mounts a device. The device will be mounted in a subdirectory in the /media hierarchy &#8211; upon successful completion, the mount point will be printed to standard output. </p>
<p> The device will be mounted with a safe set of default options. You can influence the options passed to the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command with <code>&#8211;options</code>. Note that only safe options are allowed &#8211; requests with inherently unsafe options such as <i>suid</i> or <i>dev</i> that would allow the caller to gain additional privileges, are rejected.</dl>
<p> <code>unmount</code></p>
<dl>
<dt>
<dd> Unmounts a device. This only works if the device is mounted. The option <code>&#8211;force</code> can be used to request that the device is unmounted even if active references exists.</dl>
<p> <code>unlock</code></p>
<dl>
<dt>
<dd> Unlocks an encrypted device. The passphrase will be requested from the controlling terminal and upon successful completion, the cleartext device will be printed to standard output.</dl>
<p> <code>lock</code></p>
<dl>
<dt>
<dd> Locks a device. This only works if the device is a cleartext device backed by a cryptotext device.</dl>
<p> <code>loop-setup</code></p>
<dl>
<dt>
<dd> Sets up a loop device backed by <i>FILE</i>.</dl>
<p> <code>loop-delete</code></p>
<dl>
<dt>
<dd> Tears down a loop device.</dl>
<p> <code>power-off</code></p>
<dl>
<dt>
<dd> Arranges for the drive to be safely removed and powered off. On the OS side this includes ensuring that no process is using the drive, then requesting that in-flight buffers and caches are committed to stable storage. The exact steps for powering off the drive depends on the drive itself and the interconnect used. For drives connected through USB, the effect is that the USB device will be deconfigured followed by disabling the upstream hub port it is connected to. </p>
<p> Note that as some physical devices contain multiple drives (for example 4-in-1 flash card reader USB devices) powering off one drive may affect other drives. As such there are not a lot of guarantees associated with performing this action. Usually the effect is that the drive disappears as if it was unplugged.</dl>
<p> <code>smart-simulate</code></p>
<dl>
<dt>
<dd> Sets SMART data from the libatasmart blob given by <i>FILE</i> &#8211; see /usr/share/doc/libatasmart-devel-VERSION/ for blobs shipped with libatasmart. This is a debugging feature used to check that applications act correctly when a disk is failing.</dl>
<p> <code>monitor</code></p>
<dl>
<dt>
<dd> Monitors the daemon for events.</dl>
<p> <code>dump</code></p>
<dl>
<dt>
<dd> Prints the current state of the daemon.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Prints help and exit.</dl>
<h2>COMMON OPTIONS</h2>
<p> The option <code>&#8211;no-user-interaction</code> can be used to request that no interaction (such as the user being presented with an authentication dialog) must occur when checking with <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) whether the caller is authorized to perform the requested action.</p>
<h2>AUDIENCE</h2>
<p> This program does not assume that the caller is the super user &#8211; it is intended to be used by unprivileged users and authorizations are checked by the storaged daemon using <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8). Additionally, this program is not intended to be used by scripts or other programs &#8211; options/commands may change in incompatible ways in the future even in maintenance releases. See the &#8220;API STABILITY&#8221; section of <code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8) for more information.</p>
<h2>BASH COMPLETION</h2>
<p> <code>storagectl</code> ships with a bash completion script to complete commands, objects, block devices and some options.</p>
<h2>AUTHOR</h2>
<p> This man page was originally written for UDisks2 by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/storaged/issues">https://github.com/storaged-project/storaged/issues</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-storaged/">storaged</a></code>(8), <code><a href="/docs/linux/man/8-umount-storaged/">umount.storaged</a></code>(8), <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) </p>
<h2>Index</h2>
