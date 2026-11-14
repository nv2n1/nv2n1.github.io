---
title: "targets(5)"
name: "targets"
section: "5"
letter: "t"
url: "/docs/linux/man/5-targets/"
description: "targets – configuration file for iSCSI targets"
---

<p><code>targets</code> &#8211; configuration file for iSCSI targets</p>
<h2>Synopsis</h2>
<p><code>targets</code></p>
<h2>Description</h2>
<p>The <code>targets</code> file describes the iSCSI storage which is presented to iSCSI initiators by the iscsi-target8 service. A description of the iSCSI protocol can be found in <i>&quot;Internet Small Computer Systems Interface \*(tNRFC\*(sP 3720&quot; .</i> </p>
<p> Each line in the file (other than comment lines that begin with a `#&#8217; specifies an extent, a device (made up of extents or other devices), or a target to present to the initiator. </p>
<p> Each definition, an extent, a device, and a target, is specified on a single whitespace delimited line. </p>
<p> The <i>extent</i> definition specifies a piece of storage that will be used as storage, and presented to initiators. It is the basic definition for an iSCSI target. Each target must contain at least one extent definition. The first field in the definition is the extent name, which must begin with the word &#8220;extent&#8221; and be followed by a number. The next field is the file or Nx device which will be used as persistent storage. The next field is the offset (in bytes) of the start of the extent. This field is usually 0. The fourth field in the definition is the size of the extent. The basic unit is bytes, and the shorthand <i>KB</i> <i>MB</i> <i>GB</i> and <i>TB</i> can be used for kilobytes (1024 bytes), megabytes (1024 kilobytes), gigabytes (1024 megabytes), and terabytes (1024 gigabytes) respectively. It is possible to use the word &#8220;size&#8221; to use the full size of the pre-existing regular file given in the extent name. </p>
<p> The <i>device</i> definition specifies a LUN or device, and is made up of extents and other devices. It is possible to create hierarchies of devices using the device definition. The first field in the definition is the device name, which must begin with the word &#8220;device&#8221; and be followed by a number. The next field is the type of resilience that is to be provided by the device. For simple devices, <i>RAID0</i> suffices. Greater resilience can be gained by using the <i>RAID1</i> resilience field. Following the resilience field is a list of extents or other devices. Large devices can be created by using multiple RAID0 extents, in which case each extent will be concatenated. Resilient devices can be created by using multiple RAID1 devices or extents, in which case data will be written to each of the devices or extents in turn. If RAID1 resilience is used, all the extents or sub-devices must be the same size. Please note that RAID1 recovery is not yet supported by the iscsi-target8 utility. An extent or sub-device may only be used once. </p>
<p> The <i>target</i> definition specifies an iSCSI target, which is presented to the iSCSI initiator. Multiple targets can be specified. The first field in the definition is the target name, which must begin with either of the words &#8220;target&#8221; or &#8220;lun&#8221; and be followed by a number. Optionally, if a target is followed by an &#8220;=&#8221; sign and some text, the text is taken to be that of the iSCSI Qualified Name of the target. This IQN is used by the initiator to connect to the appropriate target. The next field is a selector for whether the storage should be presented as writable, or merely as read-only storage. The field of &#8220;rw&#8221; denotes read-write storage, whilst &#8220;ro&#8221; denotes read-only storage. The next field is the device or extent name that will be used as persistent storage for this target. The fourth field is a slash-notation netmask which will be used, during the discovery phase, to control the network addresses to which targets will be presented. The magic values &#8220;any&#8221; and &#8220;all&#8221; will expand to be the same as &#8220;0/0&#8221; If an attempt is made to discover a target which is not allowed by the netmask, a warning will be issued using <a href="/docs/linux/man/3-syslog/">syslog</a>(3) to make administrators aware of this attempt. The administrator can still use tcp wrapper functionality, as found in hosts_access5 and hosts.deny5 to allow or deny discovery attempts from initiators as well as using the inbuilt netmask functionality.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/iscsi/targets </code></p>
<dd>the list of exported storage <code>targets</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-syslog/">syslog</a>(3), hosts_access5, hosts.deny5, iscsi-target8</p>
<h2>History</h2>
<p>The <code>targets</code> file first appeared in Nx 4.0 .</p>
