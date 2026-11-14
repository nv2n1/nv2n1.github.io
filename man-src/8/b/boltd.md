---
title: "boltd(8)"
name: "boltd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-boltd/"
description: "boltd – thunderbolt device managing system daemon"
---

<p>boltd &#8211; thunderbolt device managing system daemon</p>
<h2>Synopsis</h2>
<p><code>boltd</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>boltd is the thunderbolt device manager daemon. Its goal is to enable the secure and convenient use of thunderbolt devices by using the security features of modern thunderbolt controllers. It provides the org.freedesktop.bolt name on the system bus. boltd is autostarted via systemd/udev if a thunderbolt device is connected. </p>
<p> The thunderbolt I/O technology works by bridging PCIe between the controllers on each end of the connection, which in turn means that devices connected via Thunderbolt are ultimately connected via PCIe. Therefore thunderbolt can achieve very high connection speeds, fast enough to even drive external graphics cards. The downside is that it also makes certain attacks possible. To mitigate these security problems, the latest version &#8212; known as Thunderbolt 3 &#8212; supports different <code>security levels</code>: </p>
<p> <code>none</code></p>
<dl>
<dd>No security. The behavior is identical to previous Thunderbolt versions.</dl>
<p> <code>dponly</code></p>
<dl>
<dd>No PCIe tunnels are created at all, but DisplayPort tunnels are allowed and will work.</dl>
<p> <code>user</code></p>
<dl>
<dd>Connected devices must be authorized by the user. Only then will the PCIe tunnels be activated.</dl>
<p> <code>secure</code></p>
<dl>
<dd>Basically the same as user mode, but additionally a key will be written to the device the first time the device is connected. This key will then be used to verify the identity of the connected device.</dl>
<p> <code>usbonly</code></p>
<dl>
<dd>One PCIe tunnel is created to a usb controller in a thunderbolt dock; no other downstream PCIe tunnels are authorized (needs 4.17 kernel and recent hardware).</dl>
<p> The primary task of <code>boltd</code> is to authorize thunderbolt peripherals if the security level is either user or secure. It provides a D-Bus API to list devices, enroll them (authorize and store them in the local database) and forget them again (remove previously enrolled devices). It also emits signals if new devices are connected (or removed). During enrollment devices can be set to be automatically authorized as soon as they are connected. A command line tool, called <a href="/docs/linux/man/1-boltctl/">boltctl</a>(1), can be used to control the daemon and perform all the above mentioned tasks. </p>
<p> The pre-boot access control list (<code>BootACL</code>) feature is active when supported by the firmware and when <i>boltd</i> is running on a new enough Linux kernel (&gt;= 4.17). The <i>BootACL</i> is a list of UUIDs, that can be written to the thunderbolt controller. If enabled in the BIOS, all devices in that list will be authorized by the firmware during pre-boot, which means these devices can be used in the BIOS setup and also during Linux early boot. NB: <code>no device verification</code> is done, even when the security level is set to <i>secure</i> mode in the BIOS, i.e. the maximal effective security level for devices in the <i>BootACL</i> is only <i>user</i>. If <i>BootACL</i> support is present, all new devices will be automatically added. Devices that are <i>forgotten</i> (removed from <i>boltd</i>) will also be removed from the <i>BootACL</i>. When a controller is offline, changes to the <i>BootACL</i> will be written to a journal and synchronized back when the controller is online again. </p>
<p> <i>IOMMU</i> support: if the hardware and firmware support using the input-output memory management unit (IOMMU) to restrict direct memory access to certain safe regions, boltd will detect that feature and change its behavior: As long as iommu support is active, as indicated by the iommu_dma_protection sysfs attribute of the domain controller, new devices will be automatically enrolled with the <i>iommu</i> policy and existing devices with <i>iommu</i> (or <i>auto</i>) policy will be automatically authorized by boltd without any user interaction. When iommu is not active, devices that were enrolled with the <i>iommu</i> policy will not be authorized automatically. The status of iommu support can be inspected by using <code>boltctl domains</code>.</p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code></p>
<dl>
<dd>Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Shows the version number and exits.</dl>
<p> <code>-r, &#8211;replace</code></p>
<dl>
<dd>Replace the currently running boltd instance.</dl>
<p> <code>&#8211;journal</code></p>
<dl>
<dd>Force logging to the journal.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Print debug output.</dl>
<h2>Environment</h2>
<p><code>RUNTIME_DIRECTORY</code></p>
<dl>
<dd>Specifies the path where the daemon stores data that only has to live as long as the current boot. Will be set automatically when started via systemd (&gt;= 240). If not set the default path for runtime data is <i>/run/boltd</i>.</dl>
<p> <code>STATE_DIRECTORY</code></p>
<dl>
<dd>Specifies the path where the daemon stores device information, including the keys used for authorization. Overwrites the path that was set at compile time. Will be set automatically when started via systemd (&gt;= 240).</dl>
<p> <code>BOLT_DBPATH</code></p>
<dl>
<dd>Same as STATE_DIRECTORY but takes precedence over that, if set.</dl>
<h2>Exit Status</h2>
<p>On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>Author</h2>
<p>Written by Christian Kellner &lt;ckellner [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-boltctl/">boltctl</a>(1) </p>
