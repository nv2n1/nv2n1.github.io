---
title: "crypttab(5)"
name: "crypttab"
section: "5"
letter: "c"
url: "/docs/linux/man/5-crypttab/"
description: "crypttab – static information about encrypted filesystems"
---

<p>crypttab &#8211; static information about encrypted filesystems</p>
<h2>Description</h2>
<p>The file /etc/crypttab contains descriptive information about encrypted filesystems. crypttab is only read by programs (e.g. <code>cryptdisks_start</code> and <code>cryptdisks_stop</code>), and not written; it is the duty of the system administrator to properly create and maintain this file. Each filesystem is described on a separate line; fields on each line are separated by tabs or spaces. Lines starting with &#8220;#&#8221; are comments, empty lines are ignored. The order of records in crypttab is important because the init scripts sequentially iterate through crypttab doing their thing. </p>
<p> The first field, <i>target</i>, describes the mapped device name. It must be a plain filename without any directory components. A mapped device which encrypts/decrypts data to/from the <i>source device</i> will be created at /dev/mapper/target by <code>cryptsetup</code>. </p>
<p> The second field, <i>source device</i>, describes either the block special device or file that contains the encrypted data. Instead of giving the <i>source device</i> explicitly, the UUID (resp. LABEL, PARTUUID and PARTLABEL) is supported as well, using &#8220;UUID=&lt;uuid&gt;&#8221; (resp. &#8220;LABEL=&lt;label&gt;&#8221;, &#8220;PARTUUID=&lt;partuuid&gt;&#8221; and &#8220;PARTLABEL=&lt;partlabel&gt;&#8221;). </p>
<p> The third field, <i>key file</i>, describes the file to use as a key for decrypting the data of the <i>source device</i>. In case of a <i>keyscript</i>, the value of this field is given as argument to the keyscript. Values with spaces and special characters need to be escaped using octal sequences, like for <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5). Note that the <i>entire</i> key file will be used as the passphrase; the passphrase must <i>not</i> be followed by a newline character. </p>
<p> It can also be a device name (e.g. /dev/urandom), note however that LUKS requires a persistent key and therefore does <i>not</i> support random data keys. </p>
<p> If the <i>key file</i> is the string <i>none</i>, a passphrase will be read interactively from the console. In this case, the options check, checkargs and tries may be useful. </p>
<p> The fourth field, <i>options</i>, describes the cryptsetup options associated with the encryption process. At minimum, the field should contain either the string <i>luks</i> respectively <i>tcrypt</i> or the <i>cipher</i>, <i>hash</i> and <i>size</i> options. Some options can be changed on active devices using <code>cryptsetup refresh [&lt;options&gt;] &lt;name&gt;</code>. Moreover some options can be permanently written to the metada of LUKS2 headers using the <code>&#8211;persistent</code> option flag. </p>
<p> Options are in the format: <i>key</i>=<i>value</i> [,<i>key</i>=<i>value</i> &#8230;]. The supported options are described below. </p>
<p> Note that all four fields are mandatory and that a missing field will lead to unspecified behaviour.</p>
<h2>On Different Crypttab Formats</h2>
<p>Please note that there are several independent cryptsetup wrappers with their own <i>crypttab</i> format. This manpage covers Debian&#8217;s implementation for <i>initramfs</i> scripts and <i>SysVinit</i> init scripts. <i>systemd</i> brings its own <i>crypttab</i> implementation. We try to cover the differences between the <i>systemd</i> and our implementation in this manpage, but if in doubt, better check the <i>systemd</i> <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) manpage, e.g. online at m[blue]<code><a rel="nofollow" href="https://www.freedesktop.org/software/systemd/man/crypttab.html">https://www.freedesktop.org/software/systemd/man/crypttab.html</a></code>m[].</p>
<h2>Options</h2>
<p><i>cipher</i>=&lt;cipher&gt;</p>
<dl>
<dd>Encryption algorithm (ignored for LUKS and TCRYPT devices). See <code>cryptsetup -c</code>.</dl>
<p> <i>size</i>=&lt;size&gt;</p>
<dl>
<dd>Encryption key size (ignored for LUKS and TCRYPT devices). See <code>cryptsetup -s</code>.</dl>
<p> <i>sector-size</i>=&lt;bytes&gt;</p>
<dl>
<dd>Sector size. See <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8) for possible values and the default value of this option.</dl>
<p> <i>hash</i>=&lt;hash&gt;</p>
<dl>
<dd>Hash algorithm (ignored for LUKS and TCRYPT devices). See <code>cryptsetup -h</code>.</dl>
<p> <i>offset</i>=&lt;offset&gt;</p>
<dl>
<dd>Start offset (ignored for LUKS and TCRYPT devices). Uses <code>cryptsetup -o</code>.</dl>
<p> <i>skip</i>=&lt;skip&gt;</p>
<dl>
<dd>Skip sectors at the beginning (ignored for LUKS and TCRYPT devices). Uses <code>cryptsetup -p</code>.</dl>
<p> <i>keyfile-offset</i>=&lt;keyfile-offset&gt;</p>
<dl>
<dd>Specifies the number of bytes to skip at the start of the key file.</dl>
<p> <i>keyfile-size</i>=&lt;keyfile-size&gt;</p>
<dl>
<dd>Specifies the maximum number of bytes to read from the key file. The default is to read the whole file up to the compiled-in maximum, that can be queried with <code>cryptsetup &#8211;help</code>. This option is ignored for plain dm-crypt devices, as the key file size is then given by the encryption key size (option <i>size</i>).</dl>
<p> <i>keyslot</i>=&lt;slot&gt;, <i>key-slot</i>=&lt;slot&gt;</p>
<dl>
<dd>Key slot (ignored for non-LUKS devices). See <code>cryptsetup -S</code>.</dl>
<p> <i>header</i>=&lt;path&gt;</p>
<dl>
<dd>Detached header file (ignored for plain dm-crypt devices). See <code>cryptsetup &#8211;header</code>.</dl>
<p> <i>verify</i></p>
<dl>
<dd>Verify password. Uses <code>cryptsetup -y</code>.</dl>
<p> <i>readonly</i>, <i>read-only</i></p>
<dl>
<dd>Set up a read-only mapping.</dl>
<p> <i>tries</i>=&lt;num&gt;</p>
<dl>
<dd>Try to unlock the device &lt;num&gt; before failing. It&#8217;s particularly useful when using a passphrase or a <i>keyscript</i> that asks for interactive input. If you want to disable retries, pass &#8220;tries=1&#8221;. Default is &#8220;3&#8221;. Setting &#8220;tries=0&#8221; means infinitive retries.</dl>
<p> <i>discard</i></p>
<dl>
<dd>Allow using of discards (TRIM) requests for device. </p>
<p> Starting with Debian 10 (Buster), this option is added per default to new dm-crypt devices by the Debian Installer. If you don&#8217;t care about leaking access patterns (filesystem type, used space) and don&#8217;t have hidden truecrypt volumes inside this volume, then it should be safe to enable this option. See the following warning for further information. </p>
<p> <code>WARNING</code>: Assess the specific security risks carefully before enabling this option. For example, allowing discards on encrypted devices may lead to the leak of information about the ciphertext device (filesystem type, used space etc.) if the discarded blocks can be located easily on the device later.</dl>
<p> <i>luks</i></p>
<dl>
<dd>Force LUKS mode. When this mode is used, the following options are ignored since they are provided by the LUKS header on the device: <i>cipher=</i>, <i>hash=</i>, <i>size=</i></dl>
<p> <i>plain</i></p>
<dl>
<dd>Force plain encryption mode.</dl>
<p> <i>tcrypt</i></p>
<dl>
<dd>Use TrueCrypt encryption mode. When this mode is used, the following options are ignored since they are provided by the TrueCrypt header on the device or do not apply: <i>cipher=</i>, <i>hash=</i>, <i>keyfile-offset=</i>, <i>keyfile-size=</i>, <i>size=</i></dl>
<p> <i>veracrypt</i>, <i>tcrypt-veracrypt</i></p>
<dl>
<dd>Use VeraCrypt extension to TrueCrypt device. Only useful in conjunction with <i>tcrypt</i> option (ignored for non-TrueCrypt devices).</dl>
<p> <i>tcrypthidden</i>, <i>tcrypt-hidden</i></p>
<dl>
<dd>Use hidden TCRYPT header (ignored for non-TCRYPT devices).</dl>
<p> <i>swap</i></p>
<dl>
<dd>Run <code>mkswap</code> on the created device. </p>
<p> This option is ignored for <i>initramfs</i> devices.</dl>
<p> <i>tmp</i>=&lt;tmpfs&gt;</p>
<dl>
<dd>Run <code>mkfs</code> with filesystem type &lt;tmpfs&gt; on the created device. Default is ext4. </p>
<p> This option is ignored for <i>initramfs</i> devices.</dl>
<p> <i>check</i>=&lt;check&gt;</p>
<dl>
<dd>Check the content of the target device by a suitable program; if the check fails, the device is removed. If a program is provided as an argument, it is run, giving the decrypted volume (target device) as first argument, and the value of the checkargs option as second argument. Cryptdisks/cryptroot searches for the given program in /lib/cryptsetup/checks/ first, but full path to program is supported as well. </p>
<p> Default is set in /etc/default/cryptdisks (blkid). </p>
<p> This option is specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>checkargs</i>=&lt;arguments&gt;</p>
<dl>
<dd>Give &lt;arguments&gt; as the second argument to the check script. See the CHECKSCRIPTS section for more information. </p>
<p> This option is specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>initramfs</i></p>
<dl>
<dd>The initramfs hook processes the root device, any resume devices and any devices with the <i>initramfs</i> option set. These devices are processed within the initramfs stage of boot. As an example, that allows the use of remote unlocking using dropbear. </p>
<p> This option is specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>noearly</i></p>
<dl>
<dd>The cryptsetup init scripts are invoked twice during the boot process &#8211; once before lvm, raid, etc. are started and once again after that. Sometimes you need to start your encrypted disks in a special order. With this option the device is ignored during the first invocation of the cryptsetup init scripts. </p>
<p> This option is ignored for <i>initramfs</i> devices and specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>noauto</i></p>
<dl>
<dd>Entirely ignore the device at the boot process. It&#8217;s still possible to map the device manually using cryptdisks_start. </p>
<p> This option is ignored for <i>initramfs</i> devices and specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>loud</i></p>
<dl>
<dd>Be loud. Print warnings if a device does not exist. This option overwrites the option <i>loud</i>. </p>
<p> This option is ignored for <i>initramfs</i> devices and specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>quiet</i></p>
<dl>
<dd>Be quiet. Don&#8217;t print warnings if a device does not exist. This option overwrites the option <i>loud</i>. </p>
<p> This option is ignored for <i>initramfs</i> devices and specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>.</dl>
<p> <i>keyscript</i>=&lt;path&gt;</p>
<dl>
<dd>The executable at the indicated path is executed with the value of the <i>third field</i> as only argument. The keyscript output is passed to cryptsetup as decyption key. When used in initramfs, the executable either needs to be self-contained (i.e. does&#8217;nt rely on any external program which is not present in the initramfs environment) or the dependencies have to added to the initramfs image by other means. </p>
<p> LIMITATIONS: All binaries and files on which the keyscript depends must be available at the time of execution. Special care needs to be taken for encrypted filesystems like /usr or /var. As an example, unlocking encrypted /usr must not depend on binaries from /usr/(s)bin. </p>
<p> This option is specific to the Debian <i>crypttab</i> format. It&#8217;s not supported by <i>systemd</i>. </p>
<p> WARNING: With systemd as init system, this option might be ignored. At the time this is written (December 2016), the systemd cryptsetup helper doesn&#8217;t support the keyscript option to /etc/crypttab. For the time being, the only option to use keyscripts along with systemd is to force processing of the corresponding crypto devices in the initramfs. See the &#8216;initramfs&#8217; option for further information. </p>
<p> All fields of the appropriate crypttab entry are available to the keyscript as exported environment variables: </p>
<p> CRYPTTAB_NAME</p>
<dl>
<dd>The target name</dl>
<p> CRYPTTAB_SOURCE</p>
<dl>
<dd>The source device</dl>
<p> CRYPTTAB_KEY</p>
<dl>
<dd>The key file</dl>
<p> CRYPTTAB_OPTIONS</p>
<dl>
<dd>A list of exported crypttab options</dl>
<p> CRYPTTAB_OPTION_&lt;option&gt;</p>
<dl>
<dd>The value of the appropriate crypttab option, with value set to &#8216;yes&#8217; in case the option is merely a flag. For option aliases, such as &#8216;readonly&#8217; and &#8216;read-only&#8217;, the variable name refers to the first alternative listed (thus &#8216;CRYPTTAB_OPTION_readonly&#8217; in that case). If the crypttab option name contains &#8216;-&#8216; characters, then they are replaced with &#8216;_&#8217; in the exported variable name. For instance, the value of the &#8216;CRYPTTAB_OPTION_keyfile_offset&#8217; environment variable is set to the value of the &#8216;keyfile-offset&#8217; crypttab option.</dl>
<p> CRYPTTAB_TRIED</p>
<dl>
<dd>Number of previous tries since start of cryptdisks (counts until maximum number of tries is reached).</dl>
</dl>
<h2>Checkscripts</h2>
<p><i>blkid</i></p>
<dl>
<dd>Checks for any known filesystem. Supports a filesystem type as argument via &lt;checkargs&gt;: </p>
<dl>
<dd>&bull; no checkargs &#8211; succeeds if any valid filesystem is found on the device.</dl>
<dl>
<dd>&bull; &quot;none&quot; &#8211; succeeds if no valid filesystem is found on the device.</dl>
<dl>
<dd>&bull; &quot;ext4&quot; [or another filesystem type like xfs, swap, crypto_LUKS, &#8230;] &#8211; succeeds if ext4 filesystem is found on the device.</dl>
</dl>
<p> <i>un_blkid</i></p>
<dl>
<dd>Checks for no known filesystem. Supports a filesystem type as argument via &lt;checkargs&gt;: </p>
<dl>
<dd>&bull; no checkargs &#8211; succeeds if no valid filesystem is found on the device.</dl>
<dl>
<dd>&bull; &quot;ext4&quot; [or another filesystem type like xfs, swap, crypto_LUKS, &#8230;] &#8211; succeeds if no ext4 filesystem is found on the device.</dl>
</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre># Encrypted swap device
cswap /dev/sda6 /dev/urandom cipher=aes-xts-plain64,size=256,hash=sha1,swap
# Encrypted LUKS disk with interactive password, identified by its UUID, discard enabled
cdisk0 UUID=12345678-9abc-def012345-6789abcdef01 none luks,discard
# Encrypted TCRYPT disk with interactive password, discard enabled
tdisk0 /dev/sr0 none tcrypt,discard
# Encrypted ext4 disk with interactive password, discard enabled
# - retry 5 times if the check fails
cdisk1 /dev/sda2 none discard,cipher=aes-xts-plain64,size=256,hash=sha1,checkargs=ext4,tries=5
# Encrypted disk with interactive password, discard enabled
# - use a nondefault check script
# - no retries
cdisk2 /dev/sdc1 none discard,cipher=aes-xts-plain64,size=256,hash=sha1,check=customscript,tries=1
# Encrypted disk with interactive password, discard enabled
# - Twofish as the cipher, RIPEMD-160 as the hash
cdisk3 /dev/sda3 none dscard,cipher=twofish,size=256,hash=ripemd160</pre>
</dl>
<h2>Environment</h2>
<p><i>CRYPTDISKS_ENABLE</i></p>
<dl>
<dd>Set to <i>yes</i> to run cryptdisks initscripts at startup. Set to <i>no</i> to disable cryptdisks initscripts. Default is <i>yes</i>.</dl>
<p> <i>CRYPTDISKS_MOUNT</i></p>
<dl>
<dd>Specifies the mountpoints that are mounted before cryptdisks is invoked. Takes mountpoints configured in /etc/fstab as arguments. Separate mountpoints by space. This is useful for keys on removable devices, such as cdrom, usbstick, flashcard, etc. Default is unset.</dl>
<p> <i>CRYPTDISKS_CHECK</i></p>
<dl>
<dd>Specifies the default checkscript to be run against the target device, after cryptdisks has been invoked. The target device is passed as the first and only argument to the checkscript. Takes effect if the <i>check</i> option is given in crypttab with no value. See documentation for <i>check</i> option above for more information.</dl>
<h2>Known Upgrade Issues</h2>
<p>The upstream defaults for encryption cipher, hash and keysize have changed several times in the past, and they&#8217;re expected to change again in future, for example if security issues arise. On LUKS devices, the used settings are stored in the LUKS header, and thus don&#8217;t need to be configured in /etc/crypttab. For plain dm-crypt devices, no information about used cipher, hash and keysize are available at all. Therefore we strongly suggest to configure the cipher, hash and keysize in /etc/crypttab for plain dm-crypt devices, even if they match the current default.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8), <code><a href="/docs/linux/man/8-cryptdisks_start/">cryptdisks_start</a></code>(8), <code><a href="/docs/linux/man/8-cryptdisks_stop/">cryptdisks_stop</a></code>(8), /usr/share/doc/cryptsetup-initramfs/README.initramfs.gz</p>
<h2>Author</h2>
<p>This manual page was originally written by Bastian Kleineidam &lt;calvin [at] debian.org&gt; for the Debian distribution of cryptsetup. It has been further improved by Michael Gebetsroither &lt;michael.geb [at] gmx.at&gt;, David Härdeman &lt;david [at] hardeman.nu&gt; and Jonas Meurer &lt;jonas [at] freesources.org&gt;.</p>
