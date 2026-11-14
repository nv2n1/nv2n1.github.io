---
title: "tcplay(8)"
name: "tcplay"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcplay/"
description: "tcplay – tool to manage TrueCrypt volumes"
---

<p><code>tcplay</code> &#8211; tool to manage TrueCrypt volumes</p>
<h2>Synopsis</h2>
<p>&#8211;<code>c</code> &#8211;<code>d </code><i>device</i> [-<code>g</code> ] [-<code>z</code> ] [-<code>w</code> ] [-<code>a </code><i>pbkdf_hash</i> ] [-<code>b </code><i>cipher</i> ] [-<code>f </code><i>keyfile_hidden</i> ] [-<code>k </code><i>keyfile</i> ] [-<code>x </code><i>pbkdf_hash</i> ] [-<code>y </code><i>cipher</i> ]<br />
 &#8211;<code>i</code> &#8211;<code>d </code><i>device</i> [-<code>e</code> ] [-<code>f </code><i>keyfile_hidden</i> ] [-<code>k </code><i>keyfile</i> ] [-<code>s </code><i>system_device</i> ] [-<code>-fde</code> ] [-<code>-use-backup</code> ] [-<code>-use-hdr-file </code><i>hdr_file</i> ] [-<code>-use-hidden-hdr-file </code><i>hdr_file</i> ]<br />
 &#8211;<code>j </code><i>mapping</i><br />
 &#8211;<code>m </code><i>mapping</i> &#8211;<code>d </code><i>device</i> [-<code>e</code> ] [-<code>f </code><i>keyfile_hidden</i> ] [-<code>k </code><i>keyfile</i> ] [-<code>s </code><i>system_device</i> ] [-<code>t</code> ] [-<code>-fde</code> ] [-<code>-use-backup</code> ] [-<code>-use-hdr-file </code><i>hdr_file</i> ] [-<code>-use-hidden-hdr-file </code><i>hdr_file</i> ]<br />
 &#8211;<code>-modify</code> &#8211;<code>d </code><i>device</i> [-<code>k </code><i>keyfile</i> ] [-<code>-new-keyfile </code><i>new_keyfile</i> ] [-<code>-new-pbkdf-prf </code><i>pbkdf_hash</i> ] [-<code>s </code><i>system_device</i> ] [-<code>-fde</code> ] [-<code>-use-backup</code> ] [-<code>-use-hdr-file </code><i>hdr_file</i> ] [-<code>-use-hidden-hdr-file </code><i>hdr_file</i> ] [-<code>-save-hdr-backup </code><i>hdr_file</i> ] [-<code>w</code> ]<br />
 &#8211;<code>-modify</code> &#8211;<code>d </code><i>device</i> [-<code>k </code><i>keyfile</i> ] &#8211;<code>-restore-from-backup-hdr</code> [-<code>w</code> ]<br />
 &#8211;<code>u </code><i>mapping</i><br />
 &#8211;<code>h | v</code></p>
<h2>Description</h2>
<p>The utility provides full support for creating and opening/mapping TrueCrypt-compatible volumes. It supports the following commands, each with a set of options detailed further below:</p>
<dl>
<dt><code>-c , &#8211;create</code></p>
<dd>Create a new encrypted TrueCrypt volume on the device specified by &#8211;<code>-device</code></p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print help message and exit.</p>
<dt><code>-i , &#8211;info</code></p>
<dd>Print out information about the encrypted device specified by &#8211;<code>-device</code></p>
<dt><code>-j </code><i>mapping , &#8211;</i><code>-info-mapped = </code><i>mapping</i></p>
<dd>Print out information about the mapped tcplay volume specified by <i>mapping</i> Information such as key CRC and the PBKDF2 PRF is not available via this command.</p>
<dt><code>&#8211;modify</code></p>
<dd>Modify the volume header. This mode allows changing passphrase, keyfiles, PBKDF2 PRF as well as restoring from a backup header.</p>
<dt><code>-m </code><i>mapping , &#8211;</i><code>-map = </code><i>mapping</i></p>
<dd>Map the encrypted TrueCrypt volume on the device specified by &#8211;<code>-device</code> as a <a href="/docs/linux/man/4-dm/">dm</a>(4) mapping called <i>mapping</i> The <i>mapping</i> argument should not contain any spaces or special characters.</p>
<dt><code>-u </code><i>mapping , &#8211;</i><code>-unmap = </code><i>mapping</i></p>
<dd>Removes (unmaps) the <a href="/docs/linux/man/4-dm/">dm</a>(4) mapping specified by <i>mapping</i> as well as any related cascade mappings. If you mapped a volume using full disk encryption and created mapping for individual partitions using <a href="/docs/linux/man/8-kpartx/">kpartx</a>(8), you must remove these prior to unmapping the volume.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Print version message and exit.</dl>
<p> Options common to all commands are:</p>
<dl>
<dt><code>-d </code><i>device , &#8211;</i><code>-device = </code><i>device</i></p>
<dd>Specifies the disk <i>device</i> on which the TrueCrypt volume resides/will reside. This option is mandatory for all commands.</p>
<dt><code>-f </code><i>keyfile_hidden , &#8211;</i><code>-keyfile-hidden = </code><i>keyfile_hidden</i></p>
<dd>Specifies a keyfile to use in addition to the passphrase when either creating a hidden volume or when protecting a hidden volume while mapping or querying the outer volume. If you only intend to map a hidden volume, the &#8211;<code>-keyfile</code> option has to be used. This option can appear multiple times; if so, multiple keyfiles will be used. This option is not valid in the &#8211;<code>-modify</code> mode.</p>
<dt><code>-k </code><i>keyfile , &#8211;</i><code>-keyfile = </code><i>keyfile</i></p>
<dd>Specifies a <i>keyfile</i> to use in addition to the passphrase. This option can appear multiple times; if so, multiple keyfiles will be used.</dl>
<p> Additional options for the &#8211;<code>-create</code> command are:</p>
<dl>
<dt><code>-a </code><i>pbkdf_hash , &#8211;</i><code>-pbkdf-prf = </code><i>pbkdf_hash</i></p>
<dd>Specifies which hash algorithm to use for the PBKDF2 password derivation. To see which algorithms are supported, specify &#8211;<code>-pbkdf-prf = help</code></p>
<dt><code>-b </code><i>cipher , &#8211;</i><code>-cipher = </code><i>cipher</i></p>
<dd>Specifies which cipher algorithm or cascade of ciphers to use to encrypt the new volume. To see which algorithms are supported, specify &#8211;<code>-cipher = help</code></p>
<dt><code>-g, &#8211;hidden</code></p>
<dd>Specifies that the newly created volume will contain a hidden volume. The keyfiles applied to the passphrase for the hidden volume are those specified by &#8211;<code>-keyfile-hidden</code> The user will be prompted for the size of the hidden volume interactively.</p>
<dt><code>-w, &#8211;weak-keys</code></p>
<dd>Use <a href="/docs/linux/man/4-urandom/">urandom</a>(4) for key material instead of a strong entropy source. This is in general a really bad idea and should only be used for testing.</p>
<dt><code>-x </code><i>pbkdf_hash , &#8211;</i><code>-pbkdf-prf-hidden = </code><i>pbkdf_hash</i></p>
<dd>Specifies which hash algorithm to use for the PBKDF2 password derivation for the hidden volume. Only valid in conjunction with &#8211;<code>-hidden</code> If no algorithm is specified, the same as for the outer volume will be used. To see which algorithms are supported, specify &#8211;<code>-pbkdf-prf-hidden = help</code></p>
<dt><code>-y </code><i>cipher , &#8211;</i><code>-cipher-hidden = </code><i>cipher</i></p>
<dd>Specifies which cipher algorithm or cascade of ciphers to use to encrypt the hidden volume on the new TrueCrypt volume. Only valid in conjunction with &#8211;<code>-hidden</code> If no cipher is specified, the same as for the outer volume will be used. To see which algorithms are supported, specify &#8211;<code>-cipher-hidden = help</code></p>
<dt><code>-z, &#8211;insecure-erase</code></p>
<dd>Skips the secure erase of the disk. Use this option carefully as it is a security risk!</dl>
<p> Additional options for the &#8211;<code>-info</code> &#8211;<code>-map</code> and &#8211;<code>-modify</code> commands are:</p>
<dl>
<dt><code>-e, &#8211;protect-hidden</code></p>
<dd>Specifies that an outer volume will be queried or mapped, but its reported size will be adjusted accordingly to the size of the hidden volume contained in it. Both the hidden volume and outer volume passphrase and keyfiles will be required. This option only applies to the &#8211;<code>-info</code> and &#8211;<code>-map</code> commands.</p>
<dt><code>-s </code><i>system_device , &#8211;</i><code>-system-encryption = </code><i>system_device</i></p>
<dd>This option is required if you are attempting to access a device that uses system encryption, for example an encrypted <code>Windows</code> system partition. It does not apply to disks using full disk encryption. The &#8211;<code>-device</code> option will point at the actual encrypted partition, while the <i>system_device</i> argument will point to the parent device (i.e. underlying physical disk) of the encrypted partition.</p>
<dt><code>&#8211;fde</code></p>
<dd>This option is intended to be used with disks using full disk encryption (FDE). When a disk has been encrypted using TrueCrypt&#8217;s FDE, the complete disk is encrypted except for the first 63 sectors. The &#8211;<code>-device</code> option should point to the whole disk device, not to any particular partition. The resultant mapping will cover the whole disk, and will not appear as separate partitions. To access individual partitions after mapping, <a href="/docs/linux/man/8-kpartx/">kpartx</a>(8) can be used.</p>
<dt><code>&#8211;use-backup</code></p>
<dd>This option is intended to be used when the primary headers of a volume have been corrupted. This option will force to use the backup headers, which are located at the end of the device, to access the volume.</dl>
<p> Additional options only for the &#8211;<code>-map</code> command are:</p>
<dl>
<dt><code>-t , &#8211;allow-trim</code></p>
<dd>This option enables TRIM (discard) support on the mapped volume.</dl>
<p> Additional options only for the &#8211;<code>-modify</code> command are:</p>
<dl>
<dt><code>&#8211;new-pbkdf-prf = </code><i>pbkdf_hash</i></p>
<dd>Specifies which hash algorithm to use for the PBKDF2 password derivation on reencrypting the volume header. If this option is not specified, the reencrypted header will use the current PRF. To see which algorithms are supported, specify &#8211;<code>-pbkdf-prf = help</code></p>
<dt><code>&#8211;new-keyfile = </code><i>keyfile</i></p>
<dd>Specifies a <i>keyfile</i> to use in addition to the new passphrase on reencrypting the volume header. This option can appear multiple times; if so, multiple keyfiles will be used.</p>
<dt><code>&#8211;restore-from-backup-hdr</code></p>
<dd>If this option is specified, neither &#8211;<code>-new-pbkdf-prf</code> nor &#8211;<code>-new-keyfile</code> should be specified. This option implies &#8211;<code>-use-backup</code> Use this option to restore the volume headers from the backup header.</dl>
<p> Sending a <code>SIGINFO</code> or <code>SIGUSR1</code> signal to a running process makes it print progress on slower tasks such as gathering entropy or wiping the volume.</p>
<h2>Notes</h2>
<p>TrueCrypt limits passphrases to 64 characters (including the terminating null character). To be compatible with it, does the same. All passphrases (excluding keyfiles) are trimmed to 64 characters. Similarly, keyfiles are limited to a size of 1 MB, but up to 256 keyfiles can be used.</p>
<h2>Plausible Deniability</h2>
<p>offers plausible deniability. Hidden volumes are created within an outer volume. Which volume is accessed solely depends on the passphrase and keyfile(s) used. If the passphrase and keyfiles for the outer volume are specified, no information about the existance of the hidden volume is exposed. Without knowledge of the passphrase and keyfile(s) of the hidden volume its existence remains unexposed. The hidden volume can be protected when mapping the outer volume by using the &#8211;<code>-protect-hidden</code> option and specifying the passphrase and keyfiles for both the outer and hidden volumes.</p>
<h2>Examples</h2>
<p>Create a new TrueCrypt volume on /dev/vn0 using the cipher cascade of AES and Twofish and the Whirlpool hash algorithm for PBKDF2 password derivation and two keyfiles, one.key and two.key </p>
<blockquote><p> <code>&#8211;create</code> &#8211;<code>-device = /dev/vn0</code> &#8211;<code>-cipher = AES-256-XTS,TWOFISH-256-XTS</code> &#8211;<code>-pbkdf-prf = whirlpool</code> &#8211;<code>-keyfile = one.key</code> &#8211;<code>-keyfile = two.key</code> </p></blockquote>
<p> Map the outer volume on the TrueCrypt volume on /dev/vn0 as <code>truecrypt1</code> but protect the hidden volume, using the keyfile hidden.key from being overwritten: </p>
<blockquote><p> <code>&#8211;map = truecrypt1</code> &#8211;<code>-device = /dev/vn0</code> &#8211;<code>-protect-hidden</code> &#8211;<code>-keyfile-hidden = hidden.key</code> </p></blockquote>
<p> Map the hidden volume on the TrueCrypt volume on /dev/vn0 as <code>truecrypt2</code> using the keyfile hidden.key </p>
<blockquote><p> <code>&#8211;map = truecrypt2</code> &#8211;<code>-device = /dev/vn0</code> &#8211;<code>-keyfile = hidden.key</code> </p></blockquote>
<p> Map and mount the volume in the file secvol on Linux: </p>
<blockquote><p> <code>losetup /dev/loop1 secvol</code> </p></blockquote>
<blockquote><p> <code>&#8211;map = secv</code> &#8211;<code>-device = /dev/loop1</code> </p></blockquote>
<blockquote><p> <code>mount /dev/mapper/secv /mnt</code> </p></blockquote>
<p> Similarly on Dx : </p>
<blockquote><p> <code>vnconfig vn1 secvol</code> </p></blockquote>
<blockquote><p> <code>&#8211;map = secv</code> &#8211;<code>-device = /dev/vn1</code> </p></blockquote>
<blockquote><p> <code>mount /dev/mapper/secv /mnt</code> </p></blockquote>
<p> Unmapping the volume <code>truecrypt2</code> on both Linux and Dx after unmounting: </p>
<blockquote><p> <code>dmsetup remove truecrypt2</code> </p></blockquote>
<p> Or alternatively: </p>
<blockquote><p> <code>&#8211;unmap = truecrypt2</code> </p></blockquote>
<p> A hidden volume whose existance can be plausibly denied and its outer volume can for example be created with </p>
<blockquote><p> <code>&#8211;create</code> &#8211;<code>-hidden</code> &#8211;<code>-device = /dev/loop0</code> &#8211;<code>-cipher = AES-256-XTS,TWOFISH-256-XTS</code> &#8211;<code>-pbkdf-prf = whirlpool</code> &#8211;<code>-keyfile = one.key</code> &#8211;<code>-cipher-hidden = AES-256-XTS</code> &#8211;<code>-pbkdf-prf-hidden = whirlpool</code> &#8211;<code>-keyfile-hidden = hidden.key</code> </p></blockquote>
<p> will prompt the user for the passphrase for both the outer and hidden volume as well as the size of the hidden volume inside the outer volume. The hidden volume will be created inside the area spanned by the outer volume. The hidden volume can optionally use a different cipher and prf function as specified by the &#8211;<code>-cipher-hidden</code> and &#8211;<code>-pbkdf-prf-hidden</code> options. Which volume is later accessed depends only on which passphrase and keyfile(s) are being used, so that the existance of the hidden volume remains unknown without knowledge of the passphrase and keyfile it is protected by since it is located within the outer volume. To map the outer volume without potentially damaging the hidden volume, the passphrase and keyfile(s) of the hidden volume must be known and provided alongside the &#8211;<code>-protect-hidden</code> option. </p>
<p> A disk encrypted using full disk encryption can be mapped using </p>
<blockquote><p> <code>&#8211;map = tcplay_sdb</code> &#8211;<code>-device = /dev/sdb</code> &#8211;<code>-fde</code> </p></blockquote>
<p> To access individual partitions on the now mapped disk, the following command will generate mappings for each individual partition on the encrypted disk: </p>
<blockquote><p> <code>kpartx &#8211;av /dev/mapper/tcplay_sdb</code> </p></blockquote>
<p> To restore the main volume header from the backup header, the following command can be used: </p>
<blockquote><p> <code>&#8211;modify</code> &#8211;<code>-device = /dev/sdb</code> &#8211;<code>-restore-from-backup-hdr</code> </p></blockquote>
<p> As with most other commands, which header is saved (used as source) depends on the passphrase and keyfiles used. </p>
<p> To save a backup copy of a header, the following command can be used: </p>
<blockquote><p> <code>&#8211;modify</code> &#8211;<code>-device = /dev/sdb</code> &#8211;<code>-save-hdr-backup = /tmp/sdb_backup_header.hdr</code> </p></blockquote>
<p> As with most other commands, which header is saved (used as source) depends on the passphrase and keyfiles used. </p>
<p> To restore a header from a backup header file, the following command can be used: </p>
<blockquote><p> <code>&#8211;modify</code> <code>-use-hdr-file = /tmp/sdb_backup_header.hdr</code> </p></blockquote>
<p> Similarly, to restore a hidden header from a backup header file: </p>
<blockquote><p> <code>&#8211;modify</code> <code>-use-hidden-hdr-file = /tmp/sdb_backup_hidden_header.hdr</code> </p></blockquote>
<p> Which header is used as the source of the operation will still depend on the passphrase and keyfiles used. Even if you use the &#8211;<code>-use-hidden-hdr-file</code> option, if you specify the passphrase and keyfiles for the main header, the main header will be used instead.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-crypttab/">crypttab</a>(5), <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8), <a href="/docs/linux/man/8-dmsetup/">dmsetup</a>(8), <a href="/docs/linux/man/8-kpartx/">kpartx</a>(8)</p>
<h2>History</h2>
<p>The utility appeared in Dx 2.11 .</p>
<h2>Authors</h2>
<p>An Alex Hornung</p>
