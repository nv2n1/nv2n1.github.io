---
title: "machine-id(5)"
name: "machine-id"
section: "5"
letter: "m"
url: "/docs/linux/man/5-machine-id/"
description: "machine-id – Local machine ID configuration file"
---

<p>machine-id &#8211; Local machine ID configuration file</p>
<h2>Synopsis</h2>
<p>/etc/machine-id</p>
<h2>Description</h2>
<p>The /etc/machine-id file contains the unique machine ID of the local system that is set during installation or boot. The machine ID is a single newline-terminated, hexadecimal, 32-character, lowercase ID. When decoded from hexadecimal, this corresponds to a 16-byte/128-bit value. This ID may not be all zeros. </p>
<p> The machine ID is usually generated from a random source during system installation or first boot and stays constant for all subsequent boots. Optionally, for stateless systems, it is generated during runtime during early boot if necessary. </p>
<p> The machine ID may be set, for example when network booting, with the <i>systemd.machine_id=</i> kernel command line parameter or by passing the option <code>&#8211;machine-id=</code> to systemd. An ID specified in this manner has higher priority and will be used instead of the ID stored in /etc/machine-id. </p>
<p> The machine ID does not change based on local or network configuration or when hardware is replaced. Due to this and its greater length, it is a more useful replacement for the <code><a href="/docs/linux/man/3-gethostid/">gethostid</a></code>(3) call that POSIX specifies. </p>
<p> This machine ID adheres to the same format and logic as the D-Bus machine ID. </p>
<p> This ID uniquely identifies the host. It should be considered &quot;confidential&quot;, and must not be exposed in untrusted environments, in particular on the network. If a stable unique identifier that is tied to the machine is needed for some application, the machine ID or any part of it must not be used directly. Instead the machine ID should be hashed with a cryptographic, keyed hash function, using a fixed, application-specific key. That way the ID will be properly unique, and derived in a constant way from the machine ID but there will be no way to retrieve the original machine ID from the application-specific one. The <code><a href="/docs/linux/man/3-sd_id128_get_machine_app_specific/">sd_id128_get_machine_app_specific</a></code>(3) API provides an implementation of such an algorithm.</p>
<h2>Initialization</h2>
<p>Each machine should have a non-empty ID in normal operation. The ID of each machine should be unique. To achieve those objectives, /etc/machine-id can be initialized in a few different ways. </p>
<p> For normal operating system installations, where a custom image is created for a specific machine, /etc/machine-id should be populated during installation. </p>
<p> <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1) may be used by installer tools to initialize the machine ID at install time, but /etc/machine-id may also be written using any other means. </p>
<p> For operating system images which are created once and used on multiple machines, for example for containers or in the cloud, /etc/machine-id should be either missing or an empty file in the generic file system image (the difference between the two options is described under &quot;First Boot Semantics&quot; below). An ID will be generated during boot and saved to this file if possible. Having an empty file in place is useful because it allows a temporary file to be bind-mounted over the real file, in case the image is used read-only. </p>
<p> <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) may be used to initialize /etc/machine-id on mounted (but not booted) system images. </p>
<p> When a machine is booted with <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) the ID of the machine will be established. If <i>systemd.machine_id=</i> or <code>&#8211;machine-id=</code> options (see first section) are specified, this value will be used. Otherwise, the value in /etc/machine-id will be used. If this file is empty or missing, systemd will attempt to use the D-Bus machine ID from /var/lib/dbus/machine-id, the value of the kernel command line option <i>container_uuid</i>, the KVM DMI product_uuid or the devicetree vm,uuid (on KVM systems), and finally a randomly generated UUID. </p>
<p> After the machine ID is established, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) will attempt to save it to /etc/machine-id. If this fails, it will attempt to bind-mount a temporary file over /etc/machine-id. It is an error if the file system is read-only and does not contain a (possibly empty) /etc/machine-id file. </p>
<p> <code><a href="/docs/linux/man/8-systemd-machine-id-commit-service/">systemd-machine-id-commit.service</a></code>(8) will attempt to write the machine ID to the file system if /etc/machine-id or /etc/ are read-only during early boot but become writable later on.</p>
<h2>First Boot Semantics</h2>
<p>/etc/machine-id is used to decide whether a boot is the first one. The rules are as follows: </p>
<dl>
<dd>1. If /etc/machine-id does not exist, this is a first boot. During early boot, <code>systemd</code> will write &quot;uninitialized
&quot; to this file and overmount a temporary file which contains the actual machine ID. Later (after first-boot-complete.target has been reached), the real machine ID will be written to disk.</dl>
<dl>
<dd>2. If /etc/machine-id contains the string &quot;uninitialized&quot;, a boot is also considered the first boot. The same mechanism as above applies.</dl>
<dl>
<dd>3. If /etc/machine-id exists and is empty, a boot is <i>not</i> considered the first boot. <code>systemd</code> will still bind-mount a file containing the actual machine-id over it and later try to commit it to disk (if /etc/ is writable).</dl>
<dl>
<dd>4. If /etc/machine-id already contains a valid machine-id, this is not a first boot.</dl>
<p> If by any of the above rules, a first boot is detected, units with <i>ConditionFirstBoot=yes</i> will be run.</p>
<h2>Relation To Osf Uuids</h2>
<p>Note that the machine ID historically is not an OSF UUID as defined by m[blue]<code>RFC 4122</code>m[]<font SIZE="-2">[1]</font>, nor a Microsoft GUID; however, starting with systemd v30, newly generated machine IDs do qualify as Variant 1 Version 4 UUIDs, as per RFC 4122. </p>
<p> In order to maintain compatibility with existing installations, an application requiring a strictly RFC 4122 compliant UUID should decode the machine ID, and then (non-reversibly) apply the following operations to turn it into a valid RFC 4122 Variant 1 Version 4 UUID. With &quot;id&quot; being an unsigned character array: </p>
<dl>
<dd>
<pre>/* Set UUID version to 4 --- truly random generation */
id[6] = (id[6] &amp; 0x0F) | 0x40;
/* Set the UUID variant to DCE */
id[8] = (id[8] &amp; 0x3F) | 0x80;</pre>
</dl>
<p> (This code is inspired by &quot;generate_random_uuid()&quot; of drivers/char/random.c from the Linux kernel sources.)</p>
<h2>History</h2>
<p>The simple configuration file format of /etc/machine-id originates in the /var/lib/dbus/machine-id file introduced by D-Bus. In fact, this latter file might be a symlink to /etc/machine-id.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-machine-id-setup/">systemd-machine-id-setup</a></code>(1), <code><a href="/docs/linux/man/3-gethostid/">gethostid</a></code>(3), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5), <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/3-sd_id128_get_machine/">sd_id128_get_machine</a></code>(3), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 4122</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a></dl>
