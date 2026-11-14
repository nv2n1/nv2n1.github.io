---
title: "udisks(8)"
name: "udisks"
section: "8"
letter: "u"
url: "/docs/linux/man/8-udisks/"
description: "udisks – Disk Manager"
---

<p>udisks &#8211; Disk Manager</p>
<h2>Description</h2>
<p>udisks provides interfaces to enumerate and perform operations on disks and storage devices. Any application (including unprivileged ones) can access the <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8) daemon via the name <i>org.freedesktop.UDisks2</i> on the m[blue]<code>system message bus</code>m[]<font SIZE="-2">[1]</font>. In addition to the D-Bus API, a library, libudisks2 is also provided. This library can be used from C/C++ and any high-level language with m[blue]<code>GObjectIntrospection</code>m[]<font SIZE="-2">[2]</font> support such as Javascript and Python. udisks is only indirectly involved in what devices and objects are shown in the user interface.</p>
<h2>Access Control</h2>
<p>By default, logged-in users in active log-in sessions are permitted to perform operations (for example, mounting, unlocking or modifying) on devices attached to the seat their session is on. Access-control is fine-grained and based on <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), see the &#8220;Authorization Checks&#8221; chapter in the udisks documentation for more information. Note that the x-udisks-auth option can be used in the /etc/fstab and /etc/crypttab files to specify that additional authorization is required to mount resp. unlock the device (typically requiring the user to authenticate as an administrator).</p>
<h2>Drive Configuration</h2>
<p>At start-up and when a drive is connected, <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8) will apply configuration stored in the file /etc/udisks2/IDENTIFIER.conf where <i>IDENTIFIER</i> is the value of the Drive:Id property for the drive. If the file changes on disk its new contents will also be applied to the drive. Typically, users or administrators will never need to edit drive configuration files as they are effectively managed through graphical applications such as <code><a href="/docs/linux/man/1-gnome-disks/">gnome-disks</a></code>(1). Manually editing configuration files is however supported &#8212; the file format is a simple <i>.ini-like format</i> (see the m[blue]<code>Desktop Entry Specification</code>m[]<font SIZE="-2">[3]</font> for the exact syntax). New groups and keys may be added in the future.</p>
<h3>ATA group</h3>
<p>The ATA group is for settings that apply to drives using the ATA command-set. The following keys are supported: </p>
<p> <code>StandbyTimeout</code></p>
<dl>
<dd>The standby timeout. A value of zero means &quot;timeouts are disabled&quot;: the device will not automatically enter standby mode. Values from 1 to 240 specify multiples of 5 seconds, yielding timeouts from 5 seconds to 20 minutes. Values from 241 to 251 specify from 1 to 11 units of 30 minutes, yielding timeouts from 30 minutes to 5.5 hours. A value of 252 signifies a timeout of 21 minutes. A value of 253 sets a vendor-defined timeout period between 8 and 12 hours, and the value 254 is reserved. 255 is interpreted as 21 minutes plus 15 seconds. Note that some older drives may have very different interpretations of these values. This is similar to the <code>-S</code> option in <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8).</dl>
<p> <code>APMLevel</code></p>
<dl>
<dd>The Advanced Power Management level. A low value means aggressive power management and a high value means better performance. Possible settings range from values 1 through 127 (which permit spin-down), and values 128 through 254 (which do not permit spin-down). The highest degree of power management is attained with a setting of 1, and the highest I/O performance with a setting of 254. A value of 255 can be used to disable Advanced Power Management altogether on the drive (not all drives support disabling it, but most do). This is similar to the <code>-B</code> option in <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8).</dl>
<p> <code>AAMLevel</code></p>
<dl>
<dd>The Automatic Acoustic Management level. Most modern harddisk drives have the ability to speed down the head movements to reduce their noise output. The possible values are between 0 and 254. 128 is the most quiet (and therefore slowest) setting and 254 the fastest (and loudest). Some drives have only two levels (quiet / fast), while others may have different levels between 128 and 254. At the moment, most drives only support 3 options, off, quiet, and fast. These have been assigned the values 0, 128, and 254 at present, respectively, but integer space has been incorporated for future expansion, should this change. This is similar to the <code>-M</code> option in <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8).</dl>
<p> <code>WriteCacheEnabled</code></p>
<dl>
<dd>A boolean specifying whether to enable or disable the Write Cache. Valid values for this key are &#8220;true&#8221; and &#8220;false&#8221;. This is similar to the <code>-W</code> option in <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8). This key was added in 2.1.</dl>
<p> <code>ReadLookaheadEnabled</code></p>
<dl>
<dd>A boolean specifying whether to enable or disable the Read Look-ahead. Valid values for this key are &#8220;true&#8221; and &#8220;false&#8221;. This is similar to the <code>-A</code> option in <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8). This key was added in 2.6.0.</dl>
<h2>Device Information</h2>
<p>udisks relies on recent versions of <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) and the Linux kernel. Influential device properties in the udev database include: </p>
<p> <code>UDISKS_SYSTEM</code></p>
<dl>
<dd>If set, this overrides the value of the HintSystem property.</dl>
<p> <code>UDISKS_IGNORE</code></p>
<dl>
<dd>If set, this overrides the value of the HintIgnore property.</dl>
<p> <code>UDISKS_AUTO</code></p>
<dl>
<dd>If set, this overrides the value of the HintAuto property.</dl>
<p> <code>UDISKS_CAN_POWER_OFF</code></p>
<dl>
<dd>If set, this overrides the value of the CanPowerOff property.</dl>
<p> <code>UDISKS_NAME</code></p>
<dl>
<dd>The name to use for the device when presenting it in an user interface. This corresponds to the HintName property.</dl>
<p> <code>UDISKS_ICON_NAME</code></p>
<dl>
<dd>The icon to use for the device when presenting it in an user interface. If set, the name must adhere to the m[blue]<code>freedesktop.org icon theme specification</code>m[]<font SIZE="-2">[4]</font>. This corresponds to the HintIconName property.</dl>
<p> <code>UDISKS_SYMBOLIC_ICON_NAME</code></p>
<dl>
<dd>The icon to use for the device when presenting it in an user interface using a symbolic icon. If set, the name must adhere to the m[blue]<code>freedesktop.org icon theme specification</code>m[]<font SIZE="-2">[4]</font>. This corresponds to the HintSymbolicIconName property.</dl>
<p> <code>UDISKS_FILESYSTEM_SHARED</code></p>
<dl>
<dd>If set to 1, the filesystem on the device will be mounted in a shared directory (e.g. /media/VolumeName) instead of a private directory (e.g. /run/media/$USER/VolumeName) when the Filesystem.Mount() method is handled.</dl>
<p> <code>ID_SEAT</code></p>
<dl>
<dd>The physical seat the device is attached to. If unset or set to the empty string, &#8220;seat0&#8221; (the first seat) is assumed.</dl>
<h2>Api Stability</h2>
<p>udisks guarantees a stable D-Bus API within the same major version and this guarantee also extends to the client-side library libudisks2. Additionally, several major versions of udisks can be installed and operate at the same time although interoperability may be limited &#8211; for example, a device mounted using the udisks N.x API may require additional authorization if attempting to unmount it through the the (N-1).x API. </p>
<p> The udisks developers do not anticipate breaking API but does reserve the right to do so and if it happens, promises to bump the major version and ensure the new major version of udisks is parallel-installable with any older major version. However, note that programs, man pages and other artifacts may change name (for example, adopt a &#8220;2&#8221; suffix) to make room for the next major version. Therefore, applications can not rely on tools like e.g. <code><a href="/docs/linux/man/1-udisksctl/">udisksctl</a></code>(1) to be available. Additionally, there is no guarantee that the options, command-line switches etc. of command-line tools or similar will remain stable. </p>
<p> Instead, applications should only use the D-Bus API, the libudisks2 library or tools such as <code><a href="/docs/linux/man/1-dbus-send/">dbus-send</a></code>(1) or <code><a href="/docs/linux/man/1-gdbus/">gdbus</a></code>(1) to interact with <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8).</p>
<h2>Audience</h2>
<p>The intended audience of udisks include operating system developers working on the higher-level parts of the operating system, for example the desktop shell (such as m[blue]<code>GNOME</code>m[]<font SIZE="-2">[5]</font>) and disk management applications (e.g. GNOME&#8217;s m[blue]<code>Disks</code>m[]<font SIZE="-2">[6]</font> application). Software on this level typically depend on a specific (major) version of udisks and may even have support for previous versions of udisks or alternative interfaces performing the same role as udisks. </p>
<p> While udisks indeed provides a stable API and a clear upgrade path, it may not be an appropriate dependency for third party applications. For example, if the operating system switches to udisks version N.x and an application is still using the udisks (N-1).x API, the application will not work unless udisks (N-1).x is installed. While this situation is still workable (since both udisks N.x and udisks (N-1).x can be installed) it may not be desirable to ask the user to install the old version &#8211; in fact, the operating system vendor may not even provide a packaged version of the old version. Hence, if an application does not want to tie itself to a specific version of the operating system, it should not use udisks. </p>
<p> Viable alternatives to udisks are APIs that are guaranteed to be around for longer time-frames, including: </p>
<dl>
<dd>&bull; Low-level APIs and commands such as e.g. m[blue]<code>sysfs</code>m[]<font SIZE="-2">[7]</font>, m[blue]<code>libudev</code>m[]<font SIZE="-2">[8]</font>, m[blue]<code>/proc/self/mountinfo</code>m[]<font SIZE="-2">[9]</font> and m[blue]<code>util-linux</code>m[]<font SIZE="-2">[10]</font>.</dl>
<dl>
<dd>&bull; High-level APIs such as m[blue]<code>GVolumeMonitor</code>m[]<font SIZE="-2">[11]</font>.</dl>
<p> In particular, for desktop applications it is a much better idea to use something like GVolumeMonitor since it will make the application show the same devices as the desktop shell (e.g. file manager, file chooser and so on) is showing.</p>
<h2>Author</h2>
<p>This man page was originally written for UDisks2 by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/storaged-project/udisks/issues">https://github.com/storaged-project/udisks/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/8-udisksd/">udisksd</a></code>(8), <code><a href="/docs/linux/man/1-udisksctl/">udisksctl</a></code>(1), <code><a href="/docs/linux/man/8-umount-udisks2/">umount.udisks2</a></code>(8), <code><a href="/docs/linux/man/1-gnome-disks/">gnome-disks</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>system message bus</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/dbus">http://www.freedesktop.org/wiki/Software/dbus</a></dl>
<dt> 2.</p>
<dd>GObjectIntrospection</p>
<dl>
<dd><a rel="nofollow" href="https://live.gnome.org/GObjectIntrospection">https://live.gnome.org/GObjectIntrospection</a></dl>
<dt> 3.</p>
<dd>Desktop Entry Specification</p>
<dl>
<dd><a rel="nofollow" href="http://freedesktop.org/wiki/Specifications/desktop-entry-spec">http://freedesktop.org/wiki/Specifications/desktop-entry-spec</a></dl>
<dt> 4.</p>
<dd>freedesktop.org icon theme specification</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/icon-theme-spec">http://www.freedesktop.org/wiki/Specifications/icon-theme-spec</a></dl>
<dt> 5.</p>
<dd>GNOME</p>
<dl>
<dd><a rel="nofollow" href="http://www.gnome.org">http://www.gnome.org</a></dl>
<dt> 6.</p>
<dd>Disks</p>
<dl>
<dd><a rel="nofollow" href="https://live.gnome.org/Design/Apps/Disks">https://live.gnome.org/Design/Apps/Disks</a></dl>
<dt> 7.</p>
<dd>sysfs</p>
<dl>
<dd><a rel="nofollow" href="http://en.wikipedia.org/wiki/Sysfs">http://en.wikipedia.org/wiki/Sysfs</a></dl>
<dt> 8.</p>
<dd>libudev</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/software/systemd/man/libudev.html">https://www.freedesktop.org/software/systemd/man/libudev.html</a></dl>
<dt> 9.</p>
<dd>/proc/self/mountinfo</p>
<dl>
<dd><a rel="nofollow" href="http://www.kernel.org/doc/Documentation/filesystems/proc.txt">http://www.kernel.org/doc/Documentation/filesystems/proc.txt</a></dl>
<dt>10.</p>
<dd>util-linux</p>
<dl>
<dd><a rel="nofollow" href="http://en.wikipedia.org/wiki/Util-linux">http://en.wikipedia.org/wiki/Util-linux</a></dl>
<dt>11.</p>
<dd>GVolumeMonitor</p>
<dl>
<dd><a rel="nofollow" href="http://developer.gnome.org/gio/stable/volume_mon.html">http://developer.gnome.org/gio/stable/volume_mon.html</a></dl>
