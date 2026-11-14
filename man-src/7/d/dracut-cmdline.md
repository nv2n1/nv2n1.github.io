---
title: "dracut-cmdline(7)"
name: "dracut-cmdline"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dracut-cmdline/"
description: "dracut.cmdline – dracut kernel command line options"
---

<p>dracut.cmdline &#8211; dracut kernel command line options</p>
<h2>Description</h2>
<p>The root device used by the kernel is specified in the boot configuration file on the kernel command line, as always. The traditional <i>root=/dev/sda1</i> style device specification is allowed, but not encouraged. The root device should better be identified by LABEL or UUID. If a label is used, as in <i>root=LABEL=&lt;label_of_root&gt;</i> the initramfs will search all available devices for a filesystem with the appropriate label, and mount that device as the root filesystem. <i>root=UUID=&lt;uuidnumber&gt;</i> will mount the partition with that UUID as the root filesystem. In the following all kernel command line parameters, which are processed by dracut, are described. &quot;rd.*&quot; parameters mentioned without &quot;=&quot; are boolean parameters. They can be turned on/off by setting them to {0|1}. If the assignment with &quot;=&quot; is missing &quot;=1&quot; is implied. For example <i>rd.info</i> can be turned off with <i>rd.info=0</i> or turned on with <i>rd.info=1</i> or <i>rd.info</i>. The last value in the kernel command line is the value, which is honored.</p>
<h3>Standard</h3>
<p><code>init=</code><i>&lt;path to real init&gt;</i></p>
<dl>
<dd>specify the path to the init programm to be started after the initramfs has finished</dl>
<p> <code>root=</code><i>&lt;path to blockdevice&gt;</i></p>
<dl>
<dd>specify the block device to use as the root filesystem. <code>Example</code>.</p>
<dl>
<dd>
<pre>root=/dev/sda1
root=/dev/disk/by-path/pci-0000:00:1f.1-scsi-0:0:1:0-part1
root=/dev/disk/by-label/Root
root=LABEL=Root
root=/dev/disk/by-uuid/3f5ad593-4546-4a94-a374-bcfb68aa11f7
root=UUID=3f5ad593-4546-4a94-a374-bcfb68aa11f7
root=PARTUUID=3f5ad593-4546-4a94-a374-bcfb68aa11f7</pre>
</dl>
<p>  <code>rootfstype=</code><i>&lt;filesystem type&gt;</i></p>
<dl>
<dd>&quot;auto&quot; if not specified. <code>Example</code>.</p>
<dl>
<dd>
<pre>rootfstype=ext3</pre>
</dl>
<p>  <code>rootflags=</code><i>&lt;mount options&gt;</i></p>
<dl>
<dd>specify additional mount options for the root filesystem. If not set, <i>/etc/fstab</i> of the real root will be parsed for special mount options and mounted accordingly.</dl>
<p> <code>ro</code></p>
<dl>
<dd>force mounting <i>/</i> and <i>/usr</i> (if it is a separate device) read-only. If none of ro and rw is present, both are mounted according to <i>/etc/fstab</i>.</dl>
<p> <code>rw</code></p>
<dl>
<dd>force mounting <i>/</i> and <i>/usr</i> (if it is a separate device) read-write. See also ro option.</dl>
<p> <code>rootfallback=</code><i>&lt;path to blockdevice&gt;</i></p>
<dl>
<dd>specify the block device to use as the root filesystem, if the normal root cannot be found. This can only be a simple block device with a simple file system, for which the filesystem driver is either compiled in, or added manually to the initramfs. This parameter can be specified multiple times.</dl>
<p> <code>rd.auto</code> <code>rd.auto=1</code></p>
<dl>
<dd>enable autoassembly of special devices like cryptoLUKS, dmraid, mdraid or lvm. Default is off as of dracut version &gt;= 024.</dl>
<p> <code>rd.cmdline=ask</code></p>
<dl>
<dd>prompts the user for additional kernel command line parameters</dl>
<p> <code>rd.fstab=0</code></p>
<dl>
<dd>do not honor special mount options for the root filesystem found in <i>/etc/fstab</i> of the real root.</dl>
<p> <code>resume=</code><i>&lt;path to resume partition&gt;</i></p>
<dl>
<dd>resume from a swap partition <code>Example</code>.</p>
<dl>
<dd>
<pre>resume=/dev/disk/by-path/pci-0000:00:1f.1-scsi-0:0:1:0-part1
resume=/dev/disk/by-uuid/3f5ad593-4546-4a94-a374-bcfb68aa11f7
resume=UUID=3f5ad593-4546-4a94-a374-bcfb68aa11f7</pre>
</dl>
<p>  <code>rd.skipfsck</code></p>
<dl>
<dd>skip fsck for rootfs and <i>/usr</i>. If you&#8217;re mounting <i>/usr</i> read-only and the init system performs fsck before remount, you might want to use this option to avoid duplication.</dl>
<h3>Misc</h3>
<p><code>rd.emergency=</code><i>[reboot|poweroff|halt]</i></p>
<dl>
<dd>specify, what action to execute in case of a critical failure. rd.shell=0 also be specified.</dl>
<p> <code>rd.driver.blacklist=</code><i>&lt;drivername&gt;</i>[,<i>&lt;drivername&gt;</i>,&#8230;]</p>
<dl>
<dd>do not load kernel module &lt;drivername&gt;. This parameter can be specified multiple times.</dl>
<p> <code>rd.driver.pre=</code><i>&lt;drivername&gt;</i>[,<i>&lt;drivername&gt;</i>,&#8230;]</p>
<dl>
<dd>force loading kernel module &lt;drivername&gt;. This parameter can be specified multiple times.</dl>
<p> <code>rd.driver.post=</code><i>&lt;drivername&gt;</i>[,<i>&lt;drivername&gt;</i>,&#8230;]</p>
<dl>
<dd>force loading kernel module &lt;drivername&gt; after all automatic loading modules have been loaded. This parameter can be specified multiple times.</dl>
<p> <code>rd.retry=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>specify how long dracut should wait for devices to appear. The default is 30 seconds. After 2/3 of the time, degraded raids are force started. If you have hardware, which takes a very long time to announce its drives, you might want to extend this value.</dl>
<p> <code>rd.noverifyssl</code></p>
<dl>
<dd>accept self-signed certificates for ssl downloads.</dl>
<p> <code>rd.ctty=</code><i>&lt;terminal device&gt;</i></p>
<dl>
<dd>specify the controlling terminal for the console. This is useful, if you have multiple &quot;console=&quot; arguments.</dl>
<h3>Debug</h3>
<p>If you are dropped to an emergency shell, the file <i>/run/initramfs/rdsosreport.txt</i> is created, which can be safed to a (to be mounted by hand) partition (usually /boot) or a USB stick. Additional debugging info can be produced by adding <code>rd.debug</code> to the kernel command line. <i>/run/initramfs/rdsosreport.txt</i> contains all logs and the output of some tools. It should be attached to any report about dracut problems. <code>rd.info</code></p>
<dl>
<dd>print informational output though &quot;quiet&quot; is set</dl>
<p> <code>rd.shell</code></p>
<dl>
<dd>allow dropping to a shell, if root mounting fails</dl>
<p> <code>rd.debug</code></p>
<dl>
<dd>set -x for the dracut shell. If systemd is active in the initramfs, all output is logged to the systemd journal, which you can inspect with &quot;journalctl -ab&quot;. If systemd is not active, the logs are written to dmesg and <i>/run/initramfs/init.log</i>. If &quot;quiet&quot; is set, it also logs to the console.</dl>
<p> <code>rd.memdebug=[0-4]</code></p>
<dl>
<dd>Print memory usage info at various points, set the verbose level from 0 to 4.</p>
<dl>
<dd>
<pre>Higher level means more debugging output:</pre>
</dl>
<dl>
<dd>
<pre> 0 - no output
 1 - partial /proc/meminfo
 2 - /proc/meminfo
 3 - /proc/meminfo + /proc/slabinfo
 4 - /proc/meminfo + /proc/slabinfo + tracekomem
 NOTE: tracekomem is a shell script utilizing kernel trace to track
 the rough total memory consumption of kernel modules during
 loading. It may override other trace configurations.</pre>
</dl>
</dl>
<p> <code>rd.break</code></p>
<dl>
<dd>drop to a shell at the end</dl>
<p> <code>rd.break=</code><i>{cmdline|pre-udev|pre-trigger|initqueue|pre-mount|mount|pre-pivot|cleanup}</i></p>
<dl>
<dd>drop to a shell on defined breakpoint</dl>
<p> <code>rd.udev.info</code></p>
<dl>
<dd>set udev to loglevel info</dl>
<p> <code>rd.udev.debug</code></p>
<dl>
<dd>set udev to loglevel debug</dl>
<h3>I18N</h3>
<p><code>rd.vconsole.keymap=</code><i>&lt;keymap base file name&gt;</i></p>
<dl>
<dd>keyboard translation table loaded by loadkeys; taken from keymaps directory; will be written as KEYMAP to <i>/etc/vconsole.conf</i> in the initramfs. <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.vconsole.keymap=de-latin1-nodeadkeys</pre>
</dl>
<p>  <code>rd.vconsole.keymap.ext=</code><i>&lt;list of keymap base file names&gt;</i></p>
<dl>
<dd>list of extra keymaps to bo loaded (sep. by space); will be written as EXT_KEYMAP to <i>/etc/vconsole.conf</i> in the initramfs</dl>
<p> <code>rd.vconsole.unicode</code></p>
<dl>
<dd>boolean, indicating UTF-8 mode; will be written as UNICODE to <i>/etc/vconsole.conf</i> in the initramfs</dl>
<p> <code>rd.vconsole.font=</code><i>&lt;font base file name&gt;</i></p>
<dl>
<dd>console font; taken from consolefonts directory; will be written as FONT to <i>/etc/vconsole.conf</i> in the initramfs. <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.vconsole.font=LatArCyrHeb-16</pre>
</dl>
<p>  <code>rd.vconsole.font.map=</code><i>&lt;console map base file name&gt;</i></p>
<dl>
<dd>see description of <i>-m</i> parameter in setfont manual; taken from consoletrans directory; will be written as FONT_MAP to <i>/etc/vconsole.conf</i> in the initramfs</dl>
<p> <code>rd.vconsole.font.unimap=</code><i>&lt;unicode table base file name&gt;</i></p>
<dl>
<dd>see description of <i>-u</i> parameter in setfont manual; taken from unimaps directory; will be written as FONT_UNIMAP to <i>/etc/vconsole.conf</i> in the initramfs</dl>
<p> <code>rd.locale.LANG=</code><i>&lt;locale&gt;</i></p>
<dl>
<dd>taken from the environment; if no UNICODE is defined we set its value in basis of LANG value (whether it ends with &quot;.utf8&quot; (or similar) or not); will be written as LANG to <i>/etc/locale.conf</i> in the initramfs. <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.locale.LANG=pl_PL.utf8</pre>
</dl>
<p>  <code>rd.locale.LC_ALL=</code><i>&lt;locale&gt;</i></p>
<dl>
<dd>taken from the environment; will be written as LC_ALL to <i>/etc/locale.conf</i> in the initramfs</dl>
<h3>Lvm</h3>
<p><code>rd.lvm=0</code></p>
<dl>
<dd>disable LVM detection</dl>
<p> <code>rd.lvm.vg=</code><i>&lt;volume group name&gt;</i></p>
<dl>
<dd>only activate the volume groups with the given name. rd.lvm.vg can be specified multiple times on the kernel command line.</dl>
<p> <code>rd.lvm.lv=</code><i>&lt;logical volume name&gt;</i></p>
<dl>
<dd>only activate the logical volumes with the given name. rd.lvm.lv can be specified multiple times on the kernel command line.</dl>
<p> <code>rd.lvm.conf=0</code></p>
<dl>
<dd>remove any <i>/etc/lvm/lvm.conf</i>, which may exist in the initramfs</dl>
<h3>crypto LUKS</h3>
<p><code>rd.luks=0</code></p>
<dl>
<dd>disable crypto LUKS detection</dl>
<p> <code>rd.luks.uuid=</code><i>&lt;luks uuid&gt;</i></p>
<dl>
<dd>only activate the LUKS partitions with the given UUID. Any &quot;luks-&quot; of the LUKS UUID is removed before comparing to <i>&lt;luks uuid&gt;</i>. The comparisons also matches, if <i>&lt;luks uuid&gt;</i> is only the beginning of the LUKS UUID, so you don&#8217;t have to specify the full UUID. This parameter can be specified multiple times.</dl>
<p> <code>rd.luks.allow-discards=</code><i>&lt;luks uuid&gt;</i></p>
<dl>
<dd>Allow using of discards (TRIM) requests for LUKS partitions with the given UUID. Any &quot;luks-&quot; of the LUKS UUID is removed before comparing to <i>&lt;luks uuid&gt;</i>. The comparisons also matches, if <i>&lt;luks uuid&gt;</i> is only the beginning of the LUKS UUID, so you don&#8217;t have to specify the full UUID. This parameter can be specified multiple times.</dl>
<p> <code>rd.luks.allow-discards</code></p>
<dl>
<dd>Allow using of discards (TRIM) requests on all LUKS partitions.</dl>
<p> <code>rd.luks.crypttab=0</code></p>
<dl>
<dd>do not check, if LUKS partition is in <i>/etc/crypttab</i></dl>
<h3>crypto LUKS &#8211; key on removable device support</h3>
<p><code>rd.luks.key=</code><i>&lt;keypath&gt;</i>:<i>&lt;keydev&gt;</i>:<i>&lt;luksdev&gt;</i></p>
<dl>
<dd><i>keypath</i> is a path to key file to look for. It&#8217;s REQUIRED. When <i>keypath</i> ends with <i>.gpg</i> it&#8217;s considered to be key encrypted symmetrically with GPG. You will be prompted for password on boot. GPG support comes with <i>crypt-gpg</i> module which needs to be added explicitly. <i>keydev</i> is a device on which key file resides. It might be kernel name of devices (should start with &quot;/dev/&quot;), UUID (prefixed with &quot;UUID=&quot;) or label (prefix with &quot;LABEL=&quot;). You don&#8217;t have to specify full UUID. Just its beginning will suffice, even if its ambiguous. All matching devices will be probed. This parameter is recommended, but not required. If not present, all block devices will be probed, which may significantly increase boot time. If <i>luksdev</i> is given, the specified key will only be applied for that LUKS device. Possible values are the same as for <i>keydev</i>. Unless you have several LUKS devices, you don&#8217;t have to specify this parameter. The simplest usage is: <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.luks.key=/foo/bar.key</pre>
</dl>
<p> As you see, you can skip colons in such a case.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 dracut pipes key to cryptsetup with <i>-d &#8211;</i> argument, therefore you need to pipe to crypsetup luksFormat with <i>-d &#8211;</i>, too! Here follows example for key encrypted with GPG:</p>
<dl>
<dd>
<pre>gpg --quiet --decrypt rootkey.gpg | \
cryptsetup -d - -v --cipher serpent-cbc-essiv:sha256 \
--key-size 256 luksFormat /dev/sda3</pre>
</dl>
<p> If you use plain keys, just add path to <i>-d</i> option:</p>
<dl>
<dd>
<pre>cryptsetup -d rootkey.key -v --cipher serpent-cbc-essiv:sha256 \
 --key-size 256 luksFormat /dev/sda3</pre>
</dl>
</dl>
</dl>
<h3>Md Raid</h3>
<p><code>rd.md=0</code></p>
<dl>
<dd>disable MD RAID detection</dl>
<p> <code>rd.md.imsm=0</code></p>
<dl>
<dd>disable MD RAID for imsm/isw raids, use DM RAID instead</dl>
<p> <code>rd.md.ddf=0</code></p>
<dl>
<dd>disable MD RAID for SNIA ddf raids, use DM RAID instead</dl>
<p> <code>rd.md.conf=0</code></p>
<dl>
<dd>ignore mdadm.conf included in initramfs</dl>
<p> <code>rd.md.waitclean=1</code></p>
<dl>
<dd>wait for any resync, recovery, or reshape activity to finish before continuing</dl>
<p> <code>rd.md.uuid=</code><i>&lt;md raid uuid&gt;</i></p>
<dl>
<dd>only activate the raid sets with the given UUID. This parameter can be specified multiple times.</dl>
<h3>Dm Raid</h3>
<p><code>rd.dm=0</code></p>
<dl>
<dd>disable DM RAID detection</dl>
<p> <code>rd.dm.uuid=</code><i>&lt;dm raid uuid&gt;</i></p>
<dl>
<dd>only activate the raid sets with the given UUID. This parameter can be specified multiple times.</dl>
<h3>Fips</h3>
<p><code>rd.fips</code></p>
<dl>
<dd>enable FIPS</dl>
<p> <code>boot=</code><i>&lt;boot device&gt;</i></p>
<dl>
<dd>specify the device, where /boot is located. <code>Example</code>.</p>
<dl>
<dd>
<pre>boot=/dev/sda1
boot=/dev/disk/by-path/pci-0000:00:1f.1-scsi-0:0:1:0-part1
boot=UUID=&lt;uuid&gt;
boot=LABEL=&lt;label&gt;</pre>
</dl>
<p>  <code>rd.fips.skipkernel</code></p>
<dl>
<dd>skip checksum check of the kernel image. Useful, if the kernel image is not in a separate boot partition.</dl>
<h3>Network</h3>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 It is recommended to either bind an interface to a MAC with the <code>ifname</code> argument, or to use the systemd-udevd predictable network interface names. Predictable network interface device names based on:</p>
<dl>
<dd>&bull; firmware/bios-provided index numbers for on-board devices</dl>
<dl>
<dd>&bull; firmware-provided pci-express hotplug slot index number</dl>
<dl>
<dd>&bull; physical/geographical location of the hardware</dl>
<dl>
<dd>&bull; the interface&#8217;s MAC address</dl>
<p> See: m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames">http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames</a></code>m[] Two character prefixes based on the type of interface: en</p>
<dl>
<dd>ethernet</dl>
<p> wl</p>
<dl>
<dd>wlan</dl>
<p> ww</p>
<dl>
<dd>wwan</dl>
<p> Type of names: o&lt;index&gt;</p>
<dl>
<dd>on-board device index number</dl>
<p> s&lt;slot&gt;[f&lt;function&gt;][d&lt;dev_id&gt;]</p>
<dl>
<dd>hotplug slot index number</dl>
<p> x&lt;MAC&gt;</p>
<dl>
<dd>MAC address</dl>
<p> [P&lt;domain&gt;]p&lt;bus&gt;s&lt;slot&gt;[f&lt;function&gt;][d&lt;dev_id&gt;]</p>
<dl>
<dd>PCI geographical location</dl>
<p> [P&lt;domain&gt;]p&lt;bus&gt;s&lt;slot&gt;[f&lt;function&gt;][u&lt;port&gt;][..][c&lt;config&gt;][i&lt;interface&gt;]</p>
<dl>
<dd>USB port number chain</dl>
<p> All multi-function PCI devices will carry the [f&lt;function&gt;] number in the device name, including the function 0 device. When using PCI geography, The PCI domain is only prepended when it is not 0. For USB devices the full chain of port numbers of hubs is composed. If the name gets longer than the maximum number of 15 characters, the name is not exported. The usual USB configuration == 1 and interface == 0 values are suppressed. PCI ethernet card with firmware index &quot;1&quot;</p>
<dl>
<dd>
<dl>
<dd>&bull; eno1</dl>
</dl>
<p> PCI ethernet card in hotplug slot with firmware index number</p>
<dl>
<dd>
<dl>
<dd>&bull; ens1</dl>
</dl>
<p> PCI ethernet multi-function card with 2 ports</p>
<dl>
<dd>
<dl>
<dd>&bull; enp2s0f0</dl>
<dl>
<dd>&bull; enp2s0f1</dl>
</dl>
<p> PCI wlan card</p>
<dl>
<dd>
<dl>
<dd>&bull; wlp3s0</dl>
</dl>
<p> USB built-in 3G modem</p>
<dl>
<dd>
<dl>
<dd>&bull; wwp0s29u1u4i6</dl>
</dl>
<p> USB Android phone</p>
<dl>
<dd>
<dl>
<dd>&bull; enp0s29u1u2</dl>
</dl>
<pre><code>
ip={dhcp|on|any|dhcp6|auto6}</code></pre>
<p> dhcp|on|any</p>
<dl>
<dd>get ip from dhcp server from all interfaces. If root=dhcp, loop sequentially through all interfaces (eth0, eth1, &#8230;) and use the first with a valid DHCP root-path.</dl>
<p> auto6</p>
<dl>
<dd>IPv6 autoconfiguration</dl>
<p> dhcp6</p>
<dl>
<dd>IPv6 DHCP</dl>
</dl>
<p> <code>ip=</code><i>&lt;interface&gt;</i>:<i>{dhcp|on|any|dhcp6|auto6}</i>[:[<i>&lt;mtu&gt;</i>][:<i>&lt;macaddr&gt;</i>]]</p>
<dl>
<dd>This parameter can be specified multiple times. dhcp|on|any|dhcp6</p>
<dl>
<dd>get ip from dhcp server on a specific interface</dl>
<p> auto6</p>
<dl>
<dd>do IPv6 autoconfiguration</dl>
<p> &lt;macaddr&gt;</p>
<dl>
<dd>optionally <code>set</code> &lt;macaddr&gt; on the &lt;interface&gt;. This cannot be used in conjunction with the <code>ifname</code> argument for the same &lt;interface&gt;.</dl>
</dl>
<p> <code>ip=</code><i>&lt;client-IP&gt;</i>:[<i>&lt;peer&gt;</i>]:<i>&lt;gateway-IP&gt;</i>:<i>&lt;netmask&gt;</i>:<i>&lt;client_hostname&gt;</i>:<i>&lt;interface&gt;</i>:<i>{none|off|dhcp|on|any|dhcp6|auto6|ibft}</i>:[:[<i>&lt;mtu&gt;</i>][:<i>&lt;macaddr&gt;</i>]]</p>
<dl>
<dd>explicit network configuration. If you want do define a IPv6 address, put it in brackets (e.g. [2001:DB8::1]). This parameter can be specified multiple times. <i>&lt;peer&gt;</i> is optional and is the address of the remote endpoint for pointopoint interfaces and it may be followed by a slash and a decimal number, encoding the network prefix length. &lt;macaddr&gt;</p>
<dl>
<dd>optionally <code>set</code> &lt;macaddr&gt; on the &lt;interface&gt;. This cannot be used in conjunction with the <code>ifname</code> argument for the same &lt;interface&gt;.</dl>
</dl>
<p> <code>ip=</code><i>&lt;client-IP&gt;</i>:[<i>&lt;peer&gt;</i>]:<i>&lt;gateway-IP&gt;</i>:<i>&lt;netmask&gt;</i>:<i>&lt;client_hostname&gt;</i>:<i>&lt;interface&gt;</i>:<i>{none|off|dhcp|on|any|dhcp6|auto6|ibft}</i>[:[<i>&lt;dns1&gt;</i>][:<i>&lt;dns2&gt;</i>]]</p>
<dl>
<dd>explicit network configuration. If you want do define a IPv6 address, put it in brackets (e.g. [2001:DB8::1]). This parameter can be specified multiple times. <i>&lt;peer&gt;</i> is optional and is the address of the remote endpoint for pointopoint interfaces and it may be followed by a slash and a decimal number, encoding the network prefix length.</dl>
<p> <code>ifname=</code><i>&lt;interface&gt;</i>:<i>&lt;MAC&gt;</i></p>
<dl>
<dd>Assign network device name &lt;interface&gt; (ie &quot;bootnet&quot;) to the NIC with MAC &lt;MAC&gt;.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Do <code>not</code> use the default kernel naming scheme for the interface name, as it can conflict with the kernel names. So, don&#8217;t use &quot;eth[0-9]+&quot; for the interface name. Better name it &quot;bootnet&quot; or &quot;bluesocket&quot;.  <code>rd.route=</code><i>&lt;net&gt;</i>/<i>&lt;netmask&gt;</i>:<i>&lt;gateway&gt;</i>[:<i>&lt;interface&gt;</i>]</p>
<dl>
<dd>Add a static route with route options, which are separated by a colon. IPv6 addresses have to be put in brackets. <code>Example</code>.</p>
<dl>
<dd>
<pre> rd.route=192.168.200.0/24:192.168.100.222:ens10
 rd.route=192.168.200.0/24:192.168.100.222
 rd.route=192.168.200.0/24::ens10
 rd.route=[2001:DB8:3::/8]:[2001:DB8:2::1]:ens10</pre>
</dl>
<p>  <code>bootdev=</code><i>&lt;interface&gt;</i></p>
<dl>
<dd>specify network interface to use routing and netroot information from. Required if multiple ip= lines are used.</dl>
<p> <code>BOOTIF=</code><i>&lt;MAC&gt;</i></p>
<dl>
<dd>specify network interface to use routing and netroot information from.</dl>
<p> <code>rd.bootif=0</code></p>
<dl>
<dd>Disable BOOTIF parsing, which is provided by PXE</dl>
<p> <code>nameserver=</code><i>&lt;IP&gt;</i> [<code>nameserver=</code><i>&lt;IP&gt;</i> &#8230;]</p>
<dl>
<dd>specify nameserver(s) to use</dl>
<p> <code>biosdevname=0</code></p>
<dl>
<dd>boolean, turn off biosdevname network interface renaming</dl>
<p> <code>rd.neednet=1</code></p>
<dl>
<dd>boolean, bring up network even without netroot set</dl>
<p> <code>vlan=</code><i>&lt;vlanname&gt;</i>:<i>&lt;phydevice&gt;</i></p>
<dl>
<dd>Setup vlan device named &lt;vlanname&gt; on &lt;phydeivce&gt;. We support the four styles of vlan names: VLAN_PLUS_VID (vlan0005), VLAN_PLUS_VID_NO_PAD (vlan5), DEV_PLUS_VID (eth0.0005), DEV_PLUS_VID_NO_PAD (eth0.5)</dl>
<p> <code>bond=</code><i>&lt;bondname&gt;</i>[:<i>&lt;bondslaves&gt;</i>:[:<i>&lt;options&gt;</i>]]</p>
<dl>
<dd>Setup bonding device &lt;bondname&gt; on top of &lt;bondslaves&gt;. &lt;bondslaves&gt; is a comma-separated list of physical (ethernet) interfaces. &lt;options&gt; is a comma-separated list on bonding options (modinfo bonding for details) in format compatible with initscripts. If &lt;options&gt; includes multi-valued arp_ip_target option, then its values should be separated by semicolon. Bond without parameters assumes bond=bond0:eth0,eth1:mode=balance-rr</dl>
<p> <code>team=</code><i>&lt;teammaster&gt;</i>:<i>&lt;teamslaves&gt;</i></p>
<dl>
<dd>Setup team device &lt;teammaster&gt; on top of &lt;teamslaves&gt;. &lt;teamslaves&gt; is a comma-separated list of physical (ethernet) interfaces.</dl>
<p> <code>bridge=</code><i>&lt;bridgename&gt;</i>:<i>&lt;ethnames&gt;</i></p>
<dl>
<dd>Setup bridge &lt;bridgename&gt; with &lt;ethnames&gt;. &lt;ethnames&gt; is a comma-separated list of physical (ethernet) interfaces. Bridge without parameters assumes bridge=br0:eth0</dl>
<h3>Nfs</h3>
<p><code>root=</code>[<i>&lt;server-ip&gt;</i>:]<i>&lt;root-dir&gt;</i>[:<i>&lt;nfs-options&gt;</i>]</p>
<dl>
<dd>mount nfs share from &lt;server-ip&gt;:/&lt;root-dir&gt;, if no server-ip is given, use dhcp next_server. If server-ip is an IPv6 address it has to be put in brackets, e.g. [2001:DB8::1]. NFS options can be appended with the prefix &quot;:&quot; or &quot;,&quot; and are seperated by &quot;,&quot;.</dl>
<p> <code>root=</code>nfs:[<i>&lt;server-ip&gt;</i>:]<i>&lt;root-dir&gt;</i>[:<i>&lt;nfs-options&gt;</i>], <code>root=</code>nfs4:[<i>&lt;server-ip&gt;</i>:]<i>&lt;root-dir&gt;</i>[:<i>&lt;nfs-options&gt;</i>], <code>root=</code><i>{dhcp|dhcp6}</i></p>
<dl>
<dd>root=dhcp alone directs initrd to look at the DHCP root-path where NFS options can be specified. <code>Example</code>.</p>
<dl>
<dd>
<pre> root-path=&lt;server-ip&gt;:&lt;root-dir&gt;[,&lt;nfs-options&gt;]
 root-path=nfs:&lt;server-ip&gt;:&lt;root-dir&gt;[,&lt;nfs-options&gt;]
 root-path=nfs4:&lt;server-ip&gt;:&lt;root-dir&gt;[,&lt;nfs-options&gt;]</pre>
</dl>
<p>  <code>root=</code><i>/dev/nfs</i> nfsroot=[<i>&lt;server-ip&gt;</i>:]<i>&lt;root-dir&gt;</i>[:<i>&lt;nfs-options&gt;</i>]</p>
<dl>
<dd><i>Deprecated!</i> kernel Documentation_/filesystems/nfsroot.txt_ defines this method. This is supported by dracut, but not recommended.</dl>
<p> <code>rd.nfs.domain=</code><i>&lt;NFSv4 domain name&gt;</i></p>
<dl>
<dd>Set the NFSv4 domain name. Will overwrite the settings in <i>/etc/idmap.conf</i>.</dl>
<p> <code>rd.net.dhcp.retry=</code><i>&lt;cnt&gt;</i></p>
<dl>
<dd>If this option is set, dracut will try to connect via dhcp &lt;cnt&gt; times before failing. Default is 1.</dl>
<p> <code>rd.net.timeout.dhcp=</code><i>&lt;arg&gt;</i></p>
<dl>
<dd>If this option is set, dhclient is called with &quot;-timeout &lt;arg&gt;&quot;.</dl>
<p> <code>rd.net.timeout.iflink=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until link shows up. Default is 60 seconds.</dl>
<p> <code>rd.net.timeout.ifup=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until link has state &quot;UP&quot;. Default is 20 seconds.</dl>
<p> <code>rd.net.timeout.route=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until route shows up. Default is 20 seconds.</dl>
<p> <code>rd.net.timeout.ipv6dad=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until IPv6 DAD is finished. Default is 50 seconds.</dl>
<p> <code>rd.net.timeout.ipv6auto=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until IPv6 automatic addresses are assigned. Default is 40 seconds.</dl>
<p> <code>rd.net.timeout.carrier=</code><i>&lt;seconds&gt;</i></p>
<dl>
<dd>Wait &lt;seconds&gt; until carrier is recognized. Default is 5 seconds.</dl>
<h3>Cifs</h3>
<p><code>root=</code><a href="cifs://[">cifs://[</a><i>&lt;username&gt;</i>[:<i>&lt;password&gt;</i>]@]<i>&lt;server-ip&gt;</i>:<i>&lt;root-dir&gt;</i></p>
<dl>
<dd>mount cifs share from &lt;server-ip&gt;:/&lt;root-dir&gt;, if no server-ip is given, use dhcp next_server. if server-ip is an IPv6 address it has to be put in brackets, e.g. [2001:DB8::1]. If a username or password are not specified as part of the root, then they must be passed on the command line through cifsuser/cifspass.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Passwords specified on the kernel command line are visible for all users via the file <i>/proc/cmdline</i> and via dmesg or can be sniffed on the network, when using DHCP with DHCP root-path.  <code>cifsuser</code>=<i>&lt;username&gt;</i></p>
<dl>
<dd>Set the cifs username, if not specified as part of the root.</dl>
<p> <code>cifspass</code>=<i>&lt;password&gt;</i></p>
<dl>
<dd>Set the cifs password, if not specified as part of the root.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Passwords specified on the kernel command line are visible for all users via the file <i>/proc/cmdline</i> and via dmesg or can be sniffed on the network, when using DHCP with DHCP root-path.</dl>
</dl>
<h3>iSCSI</h3>
<p><code>root=</code>iscsi:[<i>&lt;username&gt;</i>:<i>&lt;password&gt;</i>[:<i>&lt;reverse&gt;</i>:<i>&lt;password&gt;</i>]@][<i>&lt;servername&gt;</i>]:[<i>&lt;protocol&gt;</i>]:[<i>&lt;port&gt;</i>][:[<i>&lt;iscsi_iface_name&gt;</i>]:[<i>&lt;netdev_name&gt;</i>]]:[<i>&lt;LUN&gt;</i>]:<i>&lt;targetname&gt;</i></p>
<dl>
<dd>protocol defaults to &quot;6&quot;, LUN defaults to &quot;0&quot;. If the &quot;servername&quot; field is provided by BOOTP or DHCP, then that field is used in conjunction with other associated fields to contact the boot server in the Boot stage. However, if the &quot;servername&quot; field is not provided, then the &quot;targetname&quot; field is then used in the Discovery Service stage in conjunction with other associated fields. See m[blue]<code>rfc4173</code>m[]<font SIZE="-2">[1]</font>.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Passwords specified on the kernel command line are visible for all users via the file <i>/proc/cmdline</i> and via dmesg or can be sniffed on the network, when using DHCP with DHCP root-path.  <code>Example</code>.</p>
<dl>
<dd>
<pre>root=iscsi:192.168.50.1::::iqn.2009-06.dracut:target0</pre>
</dl>
<p> If servername is an IPv6 address, it has to be put in brackets: <code>Example</code>.</p>
<dl>
<dd>
<pre>root=iscsi:[2001:DB8::1]::::iqn.2009-06.dracut:target0</pre>
</dl>
<p>  <code>root=</code><i>???</i> <code>netroot=</code>iscsi:[<i>&lt;username&gt;</i>:<i>&lt;password&gt;</i>[:<i>&lt;reverse&gt;</i>:<i>&lt;password&gt;</i>]@][<i>&lt;servername&gt;</i>]:[<i>&lt;protocol&gt;</i>]:[<i>&lt;port&gt;</i>][:[<i>&lt;iscsi_iface_name&gt;</i>]:[<i>&lt;netdev_name&gt;</i>]]:[<i>&lt;LUN&gt;</i>]:<i>&lt;targetname&gt;</i> &#8230;</p>
<dl>
<dd>multiple netroot options allow setting up multiple iscsi disks: <code>Example</code>.</p>
<dl>
<dd>
<pre>root=UUID=12424547
netroot=iscsi:192.168.50.1::::iqn.2009-06.dracut:target0
netroot=iscsi:192.168.50.1::::iqn.2009-06.dracut:target1</pre>
</dl>
<p> If servername is an IPv6 address, it has to be put in brackets: <code>Example</code>.</p>
<dl>
<dd>
<pre>netroot=iscsi:[2001:DB8::1]::::iqn.2009-06.dracut:target0</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Passwords specified on the kernel command line are visible for all users via the file <i>/proc/cmdline</i> and via dmesg or can be sniffed on the network, when using DHCP with DHCP root-path. You may want to use rd.iscsi.firmware.  <code>root=</code><i>???</i> <code>rd.iscsi.initiator=</code><i>&lt;initiator&gt;</i> <code>rd.iscsi.target.name=</code><i>&lt;target name&gt;</i> <code>rd.iscsi.target.ip=</code><i>&lt;target ip&gt;</i> <code>rd.iscsi.target.port=</code><i>&lt;target port&gt;</i> <code>rd.iscsi.target.group=</code><i>&lt;target group&gt;</i> <code>rd.iscsi.username=</code><i>&lt;username&gt;</i> <code>rd.iscsi.password=</code><i>&lt;password&gt;</i> <code>rd.iscsi.in.username=</code><i>&lt;in username&gt;</i> <code>rd.iscsi.in.password=</code><i>&lt;in password&gt;</i></p>
<dl>
<dd>manually specify all iscsistart parameter (see <code>iscsistart &#8211;help</code>)</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Passwords specified on the kernel command line are visible for all users via the file <i>/proc/cmdline</i> and via dmesg or can be sniffed on the network, when using DHCP with DHCP root-path. You may want to use rd.iscsi.firmware.  <code>root=</code><i>???</i> <code>netroot=</code>iscsi <code>rd.iscsi.firmware=1</code></p>
<dl>
<dd>will read the iscsi parameter from the BIOS firmware</dl>
<p> <code>rd.iscsi.param=</code><i>&lt;param&gt;</i></p>
<dl>
<dd>&lt;param&gt; will be passed as &quot;&#8211;param &lt;param&gt;&quot; to iscsistart. This parameter can be specified multiple times. <code>Example</code>. </p>
<pre><code>&quot;netroot=iscsi rd.iscsi.firmware=1 rd.iscsi.param=node.session.timeo.replacement_timeout=30&quot;
</code></pre>
<p> will result in</p>
<dl>
<dd>
<pre>iscsistart -b --param node.session.timeo.replacement_timeout=30</pre>
</dl>
</dl>
<p> <code>rd.iscsi.ibft</code> <code>rd.iscsi.ibft=1</code>: Turn on iBFT autoconfiguration for the interfaces <code>rd.iscsi.waitnet=0</code>: Turn off waiting for all interfaces to be up before trying to login to the iSCSI targets. <code>rd.iscsi.testroute=0</code>: Turn off checking, if the route to the iSCSI target IP is possible before trying to login.</p>
<h3>FCoE</h3>
<p><code>fcoe=</code><i>&lt;edd|interface|MAC&gt;</i>:<i>{dcb|nodcb}</i></p>
<dl>
<dd>Try to connect to a FCoE SAN through the NIC specified by <i>&lt;interface&gt;</i> or <i>&lt;MAC&gt;</i> or EDD settings. For the second argument, currently only nodcb is supported. This parameter can be specified multiple times.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 letters in the MAC-address must be lowercase!</dl>
</dl>
<h3>Nbd</h3>
<p><code>root=</code>??? <code>netroot=</code>nbd:<i>&lt;server&gt;</i>:<i>&lt;port&gt;</i>[:<i>&lt;fstype&gt;</i>[:<i>&lt;mountopts&gt;</i>[:<i>&lt;nbdopts&gt;</i>]]]</p>
<dl>
<dd>mount nbd share from &lt;server&gt;</dl>
<p> <code>root=dhcp</code> with <code>dhcp</code> <code>root-path=</code>nbd:<i>&lt;server&gt;</i>:<i>&lt;port&gt;</i>[:<i>&lt;fstype&gt;</i>[:<i>&lt;mountopts&gt;</i>[:<i>&lt;nbdopts&gt;</i>]]]</p>
<dl>
<dd>root=dhcp alone directs initrd to look at the DHCP root-path where NBD options can be specified. This syntax is only usable in cases where you are directly mounting the volume as the rootfs.</dl>
<h3>Dasd</h3>
<p><code>rd.dasd=</code>&#8230;.</p>
<dl>
<dd>same syntax as the kernel module parameter (s390 only)</dl>
<h3>Zfcp</h3>
<p><code>rd.zfcp=</code><i>&lt;zfcp adaptor device bus ID&gt;</i>,<i>&lt;WWPN&gt;</i>,<i>&lt;FCPLUN&gt;</i></p>
<dl>
<dd>rd.zfcp can be specified multiple times on the kernel command line. <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.zfcp=0.0.4000,0x5005076300C213e9,0x5022000000000000</pre>
</dl>
<p>  <code>rd.zfcp.conf=0</code></p>
<dl>
<dd>ignore zfcp.conf included in the initramfs</dl>
<h3>Znet</h3>
<p><code>rd.znet=</code><i>&lt;nettype&gt;</i>,<i>&lt;subchannels&gt;</i>,<i>&lt;options&gt;</i></p>
<dl>
<dd>rd.znet can be specified multiple times on the kernel command line. <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.znet=qeth,0.0.0600,0.0.0601,0.0.0602,layer2=1,portname=foo
rd.znet=ctc,0.0.0600,0.0.0601,protocol=bar</pre>
</dl>
</dl>
<h3>Booting live images</h3>
<p>Dracut offers multiple options for live booted images: squashfs with read-only filesystem image</p>
<dl>
<dd>The system will boot with a read only filesystem from the squashfs and apply a writable device mapper snapshot over the read only filesystem. Using this method ensures a relatively fast boot and lower RAM usage. Users <code>must be careful</code> to avoid writing too many blocks to the snapshot volume. Once the blocks of the snapshot are exhaused, the live filesystem becomes unusable and requires a reboot. The filesystem structure is expected to be:</p>
<dl>
<dd>
<pre>squashfs.img | Squashfs downloaded via network
 !(mount)
 /LiveOS
 |- ext3fs.img | Filesystem image to mount read-only
 !(mount)
 /bin | Live filesystem
 /boot |
 /dev |
 ... |</pre>
</dl>
<p> Dracut uses this method of live booting by default. No additional command line options are required other than <code>root=live:&lt;URL&gt;</code> to specify the location of your squashed filesystem.</dl>
<p> writable filesystem image</p>
<dl>
<dd>The system will retrieve a compressed filesystem image, connect it to a loopback device, and mount it as a writable volume. More RAM is required during boot but the live filesystem is easier to manage if it becomes full. Users can make a filesystem image of any size and that size will be maintained when the system boots. The filesystem structure is expected to be:</p>
<dl>
<dd>
<pre>rootfs.tgz | Compressed tarball containing fileystem image
 !(unpack)
 /rootfs.img | Filesystem image
 !(mount)
 /bin | Live filesystem
 /boot |
 /dev |
 ... |</pre>
</dl>
<p> To use this boot option, ensure that <code>rd.writable_fsimg=1</code> is in your kernel command line and add the <code>root=live:&lt;URL&gt;</code> to specify the location of your compressed filesystem image tarball.</dl>
<p> <code>root=</code>live:<i>&lt;url&gt;</i></p>
<dl>
<dd>Boots a live image retrieved from <i>&lt;url&gt;</i>. Valid handlers: <i>http, httpd, ftp, tftp</i>. <code>Example</code>.</p>
<dl>
<dd>
<pre>root=live:<a rel="nofollow" href="http://example.com/liveboot.img">http://example.com/liveboot.img</a>
root=live:<a href="ftp://ftp.example.com/liveboot.img">ftp://ftp.example.com/liveboot.img</a></pre>
</dl>
<p>  <code>rd.live.debug=</code>1</p>
<dl>
<dd>Enables debug output from the live boot process.</dl>
<p> <code>rd.live.dir=</code><i>&lt;path&gt;</i></p>
<dl>
<dd>Specifies the directory within the squashfs where the ext3fs.img or rootfs.img can be found. By default, this is <i>LiveOS</i>.</dl>
<p> <code>rd.live.ram=</code>1</p>
<dl>
<dd>Copy the complete image to RAM and use this for booting. This is useful when the image resides on i.e. a DVD which needs to be ejected later on.</dl>
<p> <code>rd.live.overlay=</code><i>&lt;devspec&gt;</i>:_(&lt;pathspec&gt;|auto)<i> Allow the usage of a permanent overlay. </i><i>&lt;devspec&gt;</i><i> specifies the path to a device with a mountable filesystem. </i><i>&lt;pathspec&gt;</i><i> is the path to a file within that filesystem, which shall be used to persist the changes made to the device specified by </i><i></i><code>root=live:</code><i>&lt;url&gt;__</i> option. + <code>Example</code>.</p>
<dl>
<dd>
<pre>rd.live.overlay=/dev/sdb1:persistent-overlay.img</pre>
</dl>
<p> <code>rd.live.overlay.thin=</code>1</p>
<dl>
<dd>Enables the usage of thin snapshots instead of classic dm snapshots. The advantage of thin snapshots is, that they support discards, and will free blocks which are not claimed by the filesystem. In this use case this means, that memory is given back to the kernel, when the filesystem does not claim it anymore.</dl>
<p> <code>rd.writable.fsimg=</code>1</p>
<dl>
<dd>Enables writable filesystem support. The system will boot with a fully writable filesystem without snapshots <i>(see notes above about available live boot options)</i>. You can use the <code>rootflags</code> option to set mount options for the live filesystem as well <i>(see documentation about rootflags in the </i><i></i><code>Standard</code><i> section above)</i>. This implies that the whole image is copied to RAM before the boot continues.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 There must be enough free RAM available to hold the complete image.</dl>
<p> This method is very suitable for diskless boots.</dl>
<h3>Plymouth Boot Splash</h3>
<p><code>plymouth.enable=0</code></p>
<dl>
<dd>disable the plymouth bootsplash completely.</dl>
<p> <code>rd.plymouth=0</code></p>
<dl>
<dd>disable the plymouth bootsplash only for the initramfs.</dl>
<h3>Kernel keys</h3>
<p><code>masterkey=</code><i>&lt;kernel master key path name&gt;</i></p>
<dl>
<dd>Set the path name of the kernel master key. <code>Example</code>.</p>
<dl>
<dd>
<pre>masterkey=/etc/keys/kmk-trusted.blob</pre>
</dl>
<p>  <code>masterkeytype=</code><i>&lt;kernel master key type&gt;</i></p>
<dl>
<dd>Set the type of the kernel master key. <code>Example</code>.</p>
<dl>
<dd>
<pre>masterkeytype=trusted</pre>
</dl>
<p>  <code>evmkey=</code><i>&lt;EVM key path name&gt;</i></p>
<dl>
<dd>Set the path name of the EVM key. <code>Example</code>.</p>
<dl>
<dd>
<pre>evmkey=/etc/keys/evm-trusted.blob</pre>
</dl>
<p>  <code>ecryptfskey=</code><i>&lt;eCryptfs key path name&gt;</i></p>
<dl>
<dd>Set the path name of the eCryptfs key. <code>Example</code>.</p>
<dl>
<dd>
<pre>ecryptfskey=/etc/keys/ecryptfs-trusted.blob</pre>
</dl>
</dl>
<h3>Deprecated, renamed Options</h3>
<p>Here is a list of options, which were used in dracut prior to version 008, and their new replacement. rdbreak</p>
<dl>
<dd>rd.break</dl>
<p> rd_CCW</p>
<dl>
<dd>rd.ccw</dl>
<p> rd_DASD_MOD</p>
<dl>
<dd>rd.dasd</dl>
<p> rd_DASD</p>
<dl>
<dd>rd.dasd</dl>
<p> rdinitdebug rdnetdebug</p>
<dl>
<dd>rd.debug</dl>
<p> rd_NO_DM</p>
<dl>
<dd>rd.dm=0</dl>
<p> rd_DM_UUID</p>
<dl>
<dd>rd.dm.uuid</dl>
<p> rdblacklist</p>
<dl>
<dd>rd.driver.blacklist</dl>
<p> rdinsmodpost</p>
<dl>
<dd>rd.driver.post</dl>
<p> rdloaddriver</p>
<dl>
<dd>rd.driver.pre</dl>
<p> rd_NO_FSTAB</p>
<dl>
<dd>rd.fstab=0</dl>
<p> rdinfo</p>
<dl>
<dd>rd.info</dl>
<p> check</p>
<dl>
<dd>rd.live.check</dl>
<p> rdlivedebug</p>
<dl>
<dd>rd.live.debug</dl>
<p> live_dir</p>
<dl>
<dd>rd.live.dir</dl>
<p> liveimg</p>
<dl>
<dd>rd.live.image</dl>
<p> overlay</p>
<dl>
<dd>rd.live.overlay</dl>
<p> readonly_overlay</p>
<dl>
<dd>rd.live.overlay.readonly</dl>
<p> reset_overlay</p>
<dl>
<dd>rd.live.overlay.reset</dl>
<p> live_ram</p>
<dl>
<dd>rd.live.ram</dl>
<p> rd_NO_CRYPTTAB</p>
<dl>
<dd>rd.luks.crypttab=0</dl>
<p> rd_LUKS_KEYDEV_UUID</p>
<dl>
<dd>rd.luks.keydev.uuid</dl>
<p> rd_LUKS_KEYPATH</p>
<dl>
<dd>rd.luks.keypath</dl>
<p> rd_NO_LUKS</p>
<dl>
<dd>rd.luks=0</dl>
<p> rd_LUKS_UUID</p>
<dl>
<dd>rd.luks.uuid</dl>
<p> rd_NO_LVMCONF</p>
<dl>
<dd>rd.lvm.conf</dl>
<p> rd_LVM_LV</p>
<dl>
<dd>rd.lvm.lv</dl>
<p> rd_NO_LVM</p>
<dl>
<dd>rd.lvm=0</dl>
<p> rd_LVM_SNAPSHOT</p>
<dl>
<dd>rd.lvm.snapshot</dl>
<p> rd_LVM_SNAPSIZE</p>
<dl>
<dd>rd.lvm.snapsize</dl>
<p> rd_LVM_VG</p>
<dl>
<dd>rd.lvm.vg</dl>
<p> rd_NO_MDADMCONF</p>
<dl>
<dd>rd.md.conf=0</dl>
<p> rd_NO_MDIMSM</p>
<dl>
<dd>rd.md.imsm=0</dl>
<p> rd_NO_MD</p>
<dl>
<dd>rd.md=0</dl>
<p> rd_MD_UUID</p>
<dl>
<dd>rd.md.uuid</dl>
<p> rd_NFS_DOMAIN</p>
<dl>
<dd>rd.nfs.domain</dl>
<p> iscsi_initiator</p>
<dl>
<dd>rd.iscsi.initiator</dl>
<p> iscsi_target_name</p>
<dl>
<dd>rd.iscsi.target.name</dl>
<p> iscsi_target_ip</p>
<dl>
<dd>rd.iscsi.target.ip</dl>
<p> iscsi_target_port</p>
<dl>
<dd>rd.iscsi.target.port</dl>
<p> iscsi_target_group</p>
<dl>
<dd>rd.iscsi.target.group</dl>
<p> iscsi_username</p>
<dl>
<dd>rd.iscsi.username</dl>
<p> iscsi_password</p>
<dl>
<dd>rd.iscsi.password</dl>
<p> iscsi_in_username</p>
<dl>
<dd>rd.iscsi.in.username</dl>
<p> iscsi_in_password</p>
<dl>
<dd>rd.iscsi.in.password</dl>
<p> iscsi_firmware</p>
<dl>
<dd>rd.iscsi.firmware=0</dl>
<p> rd_NO_PLYMOUTH</p>
<dl>
<dd>rd.plymouth=0</dl>
<p> rd_retry</p>
<dl>
<dd>rd.retry</dl>
<p> rdshell</p>
<dl>
<dd>rd.shell</dl>
<p> rd_NO_SPLASH</p>
<dl>
<dd>rd.splash</dl>
<p> rdudevdebug</p>
<dl>
<dd>rd.udev.debug</dl>
<p> rdudevinfo</p>
<dl>
<dd>rd.udev.info</dl>
<p> rd_NO_ZFCPCONF</p>
<dl>
<dd>rd.zfcp.conf=0</dl>
<p> rd_ZFCP</p>
<dl>
<dd>rd.zfcp</dl>
<p> rd_ZNET</p>
<dl>
<dd>rd.znet</dl>
<p> KEYMAP</p>
<dl>
<dd>vconsole.keymap</dl>
<p> KEYTABLE</p>
<dl>
<dd>vconsole.keymap</dl>
<p> SYSFONT</p>
<dl>
<dd>vconsole.font</dl>
<p> CONTRANS</p>
<dl>
<dd>vconsole.font.map</dl>
<p> UNIMAP</p>
<dl>
<dd>vconsole.font.unimap</dl>
<p> UNICODE</p>
<dl>
<dd>vconsole.unicode</dl>
<p> EXT_KEYMAP</p>
<dl>
<dd>vconsole.keymap.ext</dl>
<h3>Configuration in the Initramfs</h3>
<p><i>/etc/conf.d/</i></p>
<dl>
<dd>Any files found in <i>/etc/conf.d/</i> will be sourced in the initramfs to set initial values. Command line options will override these values set in the configuration files.</dl>
<p> <i>/etc/cmdline</i></p>
<dl>
<dd>Can contain additional command line options. Deprecated, better use /etc/cmdline.d/*.conf.</dl>
<p> <i>/etc/cmdline.d/*.conf</i></p>
<dl>
<dd>Can contain additional command line options.</dl>
<h2>Author</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) <code><a href="/docs/linux/man/5-dracut-conf/">dracut.conf</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>rfc4173</p>
<dl>
<dd><a rel="nofollow" href="http://tools.ietf.org/html/rfc4173#section-5">http://tools.ietf.org/html/rfc4173#section-5</a></dl>
