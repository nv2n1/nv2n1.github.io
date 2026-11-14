---
title: "udisksctl(1)"
name: "udisksctl"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udisksctl/"
description: "udisksctl – The udisks command line tool"
---

<h2 class="name">NAME</h2>
<p> udisksctl &#8211; The udisks command line tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>udisksctl</code> status</p>
<dt> <code>udisksctl</code> info {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i> | &#8211;drive&nbsp;<i>DRIVE</i>}</p>
<dt> <code>udisksctl</code> mount {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;filesystem-type&nbsp;<i>TYPE</i>] [&#8211;options&nbsp;<i>OPTIONS</i>&#8230;] [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> unmount {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;force] [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> unlock {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;no-user-interaction] [&#8211;key-file&nbsp;<i>PATH</i>] [&#8211;read-only]</p>
<dt> <code>udisksctl</code> lock {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> loop-setup &#8211;file&nbsp;<i>PATH</i> [&#8211;read-only] [&#8211;offset&nbsp;<i>OFFSET</i>] [&#8211;size&nbsp;<i>SIZE</i>] [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> loop-delete {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> power-off {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> smart-simulate &#8211;file&nbsp;<i>PATH</i> {&#8211;object-path&nbsp;<i>OBJECT</i> | &#8211;block-device&nbsp;<i>DEVICE</i>} [&#8211;no-user-interaction]</p>
<dt> <code>udisksctl</code> monitor</p>
<dt> <code>udisksctl</code> dump</p>
<dt> <code>udisksctl</code> help</dl>
<h2>DESCRIPTION</h2>
<p> <code>udisksctl</code></p>
<dd>is a command-line program used to interact with the <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8) daemon process.</p>
<h2>COMMANDS</h2>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Shows high-level information about disk drives and block devices.</dl>
<p> <code>info</code></p>
<dl>
<dt>
<dd> Shows detailed information about <i>OBJECT</i>, <i>DEVICE</i> or <i>DRIVE</i>.</dl>
<p> <code>mount</code></p>
<dl>
<dt>
<dd> Mounts a device. The device will be mounted in a subdirectory in the /run/media hierarchy &#8211; upon successful completion, the mount point will be printed to standard output. </p>
<p> <code>-t</code>, <code>&#8211;filesystem-type</code></p>
<dl>
<dt>
<dd> Filesystem type to use. If not specified, autodetected filesystem type will be used.</dl>
<p> <code>-o</code>, <code>&#8211;options</code></p>
<dl>
<dt>
<dd> The device will be mounted with a safe set of default options. You can influence the options passed to the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command using this option. Note that only safe options are allowed &#8211; requests with inherently unsafe options such as <i>suid</i> or <i>dev</i> that would allow the caller to gain additional privileges, are rejected.</dl>
</dl>
<p> <code>unmount</code></p>
<dl>
<dt>
<dd> Unmounts a device. This only works if the device is mounted. The option <code>&#8211;force</code> can be used to request that the device is unmounted even if active references exists. </p>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Lazy unmount. Detach the filesystem from the file hierarchy now, and clean up all references to this filesystem as soon as it is not busy anymore.</dl>
</dl>
<p> <code>unlock</code></p>
<dl>
<dt>
<dd> Unlocks an encrypted device. The passphrase will be requested from the controlling terminal and upon successful completion, the cleartext device will be printed to standard output. </p>
<p> <code>&#8211;key-file=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Read passphrase from the given file.</dl>
</dl>
<p> <code>lock</code></p>
<dl>
<dt>
<dd> Locks a device. This only works if the device is a cleartext device backed by a cryptotext device.</dl>
<p> <code>loop-setup</code></p>
<dl>
<dt>
<dd> Sets up a loop device backed by <i>FILE</i>. </p>
<p> <code>-f</code>, <code>&#8211;file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> File to set up a loop device for.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dt>
<dd> Set up a read-only loop device.</dl>
<p> <code>-o</code>, <code>&#8211;offset=</code><i>OFFSET</i></p>
<dl>
<dt>
<dd> The data start is moved <i>OFFSET</i> bytes into the specified file.</dl>
<p> <code>-s</code>, <code>&#8211;size=</code><i>SIZE</i></p>
<dl>
<dt>
<dd> The data end is set to no more than <i>SIZE</i> bytes after the data start.</dl>
</dl>
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
<dd> Sets SMART data from the libatasmart blob given by <i>FILE</i> &#8211; see /usr/share/doc/libatasmart-devel-VERSION/ for blobs shipped with libatasmart. This is a debugging feature used to check that applications act correctly when a disk is failing. </p>
<p> <code>-f</code>, <code>&#8211;file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> File with the libatasmart blob.</dl>
</dl>
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
<h2>DEVICE SPECIFICATION</h2>
<p> For commands that require a device as an argument following options can be used to specify it. </p>
<p> <code>-b</code>, <code>&#8211;block-device=</code><i>DEVICE</i></p>
<dl>
<dt>
<dd> Specify a device by its device file path. For example <i>/dev/sda</i>.</dl>
<p> <code>-p</code>, <code>&#8211;object-path=</code><i>OBJECT</i></p>
<dl>
<dt>
<dd> Specify a device by the UDisks internal object path without the /org/freedesktop/UDisks2 prefix. For example <i>block_devices/sda</i> for the /dev/sda disk.</dl>
<p> <code>-d</code>, <code>&#8211;drive=</code><i>DRIVE</i></p>
<dl>
<dt>
<dd> Specify a drive by name, for example <i>VirtIO_Disk</i>. This can be currently used only together with the <code>info</code> command.</dl>
<h2>COMMON OPTIONS</h2>
<p> The option <code>&#8211;no-user-interaction</code> can be used to request that no interaction (such as the user being presented with an authentication dialog) must occur when checking with <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) whether the caller is authorized to perform the requested action.</p>
<h2>AUDIENCE</h2>
<p> This program does not assume that the caller is the super user &#8211; it is intended to be used by unprivileged users and authorizations are checked by the udisks daemon using <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8). Additionally, this program is not intended to be used by scripts or other programs &#8211; options/commands may change in incompatible ways in the future even in maintenance releases. See the &#8220;API STABILITY&#8221; section of <code><a href="/docs/linux/man/8-udisks/">udisks</a></code>(8) for more information.</p>
<h2>BASH COMPLETION</h2>
<p> <code>udisksctl</code> ships with a bash completion script to complete commands, objects, block devices and some options.</p>
<h2>AUTHOR</h2>
<p> This man page was originally written for UDisks2 by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/udisks/issues">https://github.com/storaged-project/udisks/issues</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-udisks/">udisks</a></code>(8), <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8), <code><a href="/docs/linux/man/8-umount-udisks2/">umount.udisks2</a></code>(8), <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) </p>
<h2>Index</h2>
