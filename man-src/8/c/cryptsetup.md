---
title: "cryptsetup(8)"
name: "cryptsetup"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cryptsetup/"
description: "cryptsetup – manage plain dm-crypt and LUKS encrypted volumes"
---

<p>cryptsetup &#8211; manage plain dm-crypt and LUKS encrypted volumes</p>
<h2>Synopsis</h2>
<p><code>cryptsetup &lt;options&gt; &lt;action&gt; &lt;action args&gt;</code></p>
<h2>Description</h2>
<p>cryptsetup is used to conveniently setup dm-crypt managed device-mapper mappings. These include plain dm-crypt volumes and LUKS volumes. The difference is that LUKS uses a metadata header and can hence offer more features than plain dm-crypt. On the other hand, the header is visible and vulnerable to damage. In addition, cryptsetup provides limited support for the use of loop-AES volumes and for TrueCrypt compatible volumes. </p>
<h2>Plain Dm-Crypt Or Luks?</h2>
<p>Unless you understand the cryptographic background well, use LUKS. With plain dm-crypt there are a number of possible user errors that massively decrease security. While LUKS cannot fix them all, it can lessen the impact for many of them.</p>
<h2>Warnings</h2>
<p>A lot of good information on the risks of using encrypted storage, on handling problems and on security aspects can be found in the <i>Cryptsetup FAQ</i>. Read it. Nonetheless, some risks deserve to be mentioned here. </p>
<p> <code>Backup:</code> Storage media die. Encryption has no influence on that. Backup is mandatory for encrypted data as well, if the data has any worth. See the Cryptsetup FAQ for advice on how to do a backup of an encrypted volume. </p>
<p> <code>Character encoding:</code> If you enter a passphrase with special symbols, the passphrase can change depending on character encoding. Keyboard settings can also change, which can make blind input hard or impossible. For example, switching from some ASCII 8-bit variant to UTF-8 can lead to a different binary encoding and hence different passphrase seen by cryptsetup, even if what you see on the terminal is exactly the same. It is therefore highly recommended to select passphrase characters only from 7-bit ASCII, as the encoding for 7-bit ASCII stays the same for all ASCII variants and UTF-8. </p>
<p> <code>LUKS header:</code> If the header of a LUKS volume gets damaged, all data is permanently lost unless you have a header-backup. If a key-slot is damaged, it can only be restored from a header-backup or if another active key-slot with known passphrase is undamaged. Damaging the LUKS header is something people manage to do with surprising frequency. This risk is the result of a trade-off between security and safety, as LUKS is designed for fast and secure wiping by just overwriting header and key-slot area. </p>
<p> <code>Previously used partitions:</code> If a partition was previously used, it is a very good idea to wipe filesystem signatures, data, etc. before creating a LUKS or plain dm-crypt container on it. For a quick removal of filesystem signatures, use &quot;wipefs&quot;. Take care though that this may not remove everything. In particular, MD RAID signatures at the end of a device may survive. It also does not remove data. For a full wipe, overwrite the whole partition before container creation. If you do not know how to do that, the cryptsetup FAQ describes several options.</p>
<h2>Basic Commands</h2>
<p>The following are valid actions for all supported device types. </p>
<p> <i>open</i> &lt;device&gt; &lt;name&gt; &#8211;type &lt;device_type&gt;</p>
<dl>
<dd>Opens (creates a mapping with) &lt;name&gt; backed by device &lt;device&gt;. </p>
<p> Device type can be <i>plain</i>, <i>luks</i> (default), <i>luks1</i>, <i>luks2</i>, <i>loopaes</i> or <i>tcrypt</i>. </p>
<p> For backward compatibility there are <code>open</code> command aliases: </p>
<p> <code>create</code> (argument-order &lt;name&gt; &lt;device&gt;): open &#8211;type plain<br />
 <code>plainOpen</code>: open &#8211;type plain<br />
 <code>luksOpen</code>: open &#8211;type luks<br />
 <code>loopaesOpen</code>: open &#8211;type loopaes<br />
 <code>tcryptOpen</code>: open &#8211;type tcrypt </p>
<p> <code>&lt;options&gt;</code> are type specific and are described below for individual device types. For <code>create</code>, the order of the &lt;name&gt; and &lt;device&gt; options is inverted for historical reasons, all other aliases use the standard <code>&lt;device&gt; &lt;name&gt;</code> order.</dl>
<p> <i>close</i> &lt;name&gt;</p>
<dl>
<dd>Removes the existing mapping &lt;name&gt; and wipes the key from kernel memory. </p>
<p> For backward compatibility there are <code>close</code> command aliases: <code>remove</code>, <code>plainClose</code>, <code>luksClose</code>, <code>loopaesClose</code>, <code>tcryptClose</code> (all behaves exactly the same, device type is determined automatically from active device). </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;deferred] </p>
</dl>
<p> <i>status</i> &lt;name&gt;</p>
<dl>
<dd>Reports the status for the mapping &lt;name&gt;.</dl>
<p> <i>resize</i> &lt;name&gt;</p>
<dl>
<dd>Resizes an active mapping &lt;name&gt;. </p>
<p> If &#8211;size (in 512-bytes sectors) or &#8211;device-size are not specified, the size is computed from the underlying device. For LUKS it is the size of the underlying device without the area reserved for LUKS header (see data payload offset in <code>luksDump</code> command). For plain crypt device, the whole device size is used. </p>
<p> Note that this does not change the raw device geometry, it just changes how many sectors of the raw device are represented in the mapped device. </p>
<p> If cryptsetup detected volume key for active device loaded in kernel keyring service, resize action would first try to retrieve the key using a token and only if it failed it&#8217;d ask for a passphrase to unlock a keyslot (LUKS) or to derive a volume key again (plain mode). The kernel keyring is used by default for LUKS2 devices. </p>
<p> With LUKS2 device additional <code>&lt;options&gt;</code> can be [&#8211;token-id, &#8211;token-only, &#8211;key-slot, &#8211;key-file, &#8211;keyfile-size, &#8211;keyfile-offset, &#8211;timeout, &#8211;disable-locks, &#8211;disable-keyring]. </p>
</dl>
<p> <i>refresh</i> &lt;name&gt;</p>
<dl>
<dd>Refreshes parameters of active mapping &lt;name&gt;. </p>
<p> Updates parameters of active device &lt;name&gt; without need to deactivate the device (and umount filesystem). Currently it supports parameters refresh on following devices: LUKS1, LUKS2 (including authenticated encryption), plain crypt and loopaes. </p>
<p> Mandatory parametrs are identical to those of an open action for respective device type. </p>
<p> You may change following parameters on all devices &#8211;perf-same_cpu_crypt, &#8211;perf-submit_from_crypt_cpus and &#8211;allow-discards. </p>
<p> Refreshing device without any optional parameter will refresh the device with default setting (respective to device type). </p>
<p> <code>LUKS2 only:</code> </p>
<p> &#8211;integrity-no-journal parameter affects only LUKS2 devices with underlying dm-integrity device. </p>
<p> Adding option &#8211;persistent stores any combination of device parameters above in LUKS2 metadata (only after successful refresh operation). </p>
<p> &#8211;disable-keyring parameter refreshes a device with volume key passed in dm-crypt driver. </p>
</dl>
<p> <i>reencrypt</i> &lt;device&gt; or &#8211;active-name &lt;name&gt; [&lt;new_name&gt;]</p>
<dl>
<dd>Run resilient reencryption (LUKS2 device only). </p>
<p> There are 3 basic modes of operation: </p>
<p> &bull; device reencryption (<i>reencrypt</i>) </p>
<p> &bull; device encryption (<i>reencrypt</i> &#8211;encrypt) </p>
<p> &bull; device decryption (<i>reencrypt</i> &#8211;decrypt) </p>
<p> &lt;device&gt; or &#8211;active-name &lt;name&gt; is mandatory parameter. </p>
<p> With &lt;device&gt; parameter cryptsetup looks up active &lt;device&gt; dm mapping. If no active mapping is detected, it starts offline reencryption otherwise online reencryption takes place. </p>
<p> Reencryption process may be safely interrupted by a user via SIGTERM signal (ctrl+c). </p>
<p> To resume already initialized or interrupted reencryption, just run the cryptsetup <i>reencrypt</i> command again to continue the reencryption operation. Reencryption may be resumed with different &#8211;resilience or &#8211;hotzone-size unless implicit datashift resilience mode is used (reencrypt &#8211;encrypt with &#8211;reduce-device-size option). </p>
<p> If the reencryption process was interrupted abruptly (reencryption process crash, system crash, poweroff) it may require recovery. The recovery is currently run automatically on next activation (action <i>open</i>) when needed. </p>
<p> Optional parameter &lt;new_name&gt; takes effect only with &#8211;encrypt option and it activates device &lt;new_name&gt; immediately after encryption initialization gets finished. That&#8217;s useful when device needs to be ready as soon as possible and mounted (used) before full data area encryption is completed. </p>
<p> Action supports following additional <code>&lt;options&gt;</code> [&#8211;encrypt, &#8211;decrypt, &#8211;device-size, &#8211;resilience, &#8211;resilience-hash, &#8211;hotzone-size, &#8211;init-only, &#8211;resume-only, &#8211;reduce-device-size]. </p>
</dl>
<h2>Plain Mode</h2>
<p>Plain dm-crypt encrypts the device sector-by-sector with a single, non-salted hash of the passphrase. No checks are performed, no metadata is used. There is no formatting operation. When the raw device is mapped (opened), the usual device operations can be used on the mapped device, including filesystem creation. Mapped devices usually reside in /dev/mapper/&lt;name&gt;. </p>
<p> The following are valid plain device type actions: </p>
<p> <i>open</i> &#8211;type plain &lt;device&gt; &lt;name&gt;<br />
 <i>create</i> &lt;name&gt; &lt;device&gt; (<code>OBSOLETE syntax</code>)</p>
<dl>
<dd>Opens (creates a mapping with) &lt;name&gt; backed by device &lt;device&gt;. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;hash, &#8211;cipher, &#8211;verify-passphrase, &#8211;sector-size, &#8211;key-file, &#8211;keyfile-offset, &#8211;key-size, &#8211;offset, &#8211;skip, &#8211;size, &#8211;readonly, &#8211;shared, &#8211;allow-discards, &#8211;refresh] </p>
<p> Example: &#8216;cryptsetup open &#8211;type plain /dev/sda10 e1&#8217; maps the raw encrypted device /dev/sda10 to the mapped (decrypted) device /dev/mapper/e1, which can then be mounted, fsck-ed or have a filesystem created on it.</dl>
<h2>Luks Extension</h2>
<p>LUKS, the Linux Unified Key Setup, is a standard for disk encryption. It adds a standardized header at the start of the device, a key-slot area directly behind the header and the bulk data area behind that. The whole set is called a &#8216;LUKS container&#8217;. The device that a LUKS container resides on is called a &#8216;LUKS device&#8217;. For most purposes, both terms can be used interchangeably. But note that when the LUKS header is at a nonzero offset in a device, then the device is not a LUKS device anymore, but has a LUKS container stored in it at an offset. </p>
<p> LUKS can manage multiple passphrases that can be individually revoked or changed and that can be securely scrubbed from persistent media due to the use of anti-forensic stripes. Passphrases are protected against brute-force and dictionary attacks by PBKDF2, which implements hash iteration and salting in one function. </p>
<p> LUKS2 is a new version of header format that allows additional extensions like different PBKDF algorithm or authenticated encryption. You can format device with LUKS2 header if you specify <i>&#8211;type luks2</i> in <i>luksFormat</i> command. For activation, the format is already recognized automatically. </p>
<p> Each passphrase, also called a <code>key</code> in this document, is associated with one of 8 key-slots. Key operations that do not specify a slot affect the first slot that matches the supplied passphrase or the first empty slot if a new passphrase is added. </p>
<p> The <code>&lt;device&gt;</code> parameter can also be specified by a LUKS UUID in the format UUID=&lt;uuid&gt;. Translation to real device name uses symlinks in /dev/disk/by-uuid directory. </p>
<p> To specify a detached header, the <code>&#8211;header</code> parameter can be used in all LUKS commands and always takes precedence over the positional <code>&lt;device&gt;</code> parameter. </p>
<p> The following are valid LUKS actions: </p>
<p> <i>luksFormat</i> &lt;device&gt; [&lt;key file&gt;]</p>
<dl>
<dd>Initializes a LUKS partition and sets the initial passphrase (for key-slot 0), either via prompting or via &lt;key file&gt;. Note that if the second argument is present, then the passphrase is taken from the file given there, without the need to use the &#8211;key-file option. Also note that for both forms of reading the passphrase from a file you can give &#8216;-&#8216; as file name, which results in the passphrase being read from stdin and the safety-question being skipped. </p>
<p> You can only call luksFormat on a LUKS device that is not mapped. </p>
<p> To use LUKS2, specify <i>&#8211;type luks2</i>. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;hash, &#8211;cipher, &#8211;verify-passphrase, &#8211;key-size, &#8211;key-slot, &#8211;key-file (takes precedence over optional second argument), &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;use-random | &#8211;use-urandom, &#8211;uuid, &#8211;master-key-file, &#8211;iter-time, &#8211;header, &#8211;pbkdf-force-iterations, &#8211;force-password, &#8211;disable-locks]. </p>
<p> For LUKS2, additional <code>&lt;options&gt;</code> can be [&#8211;integrity, &#8211;integrity-no-wipe, &#8211;sector-size, &#8211;label, &#8211;subsystem, &#8211;pbkdf, &#8211;pbkdf-memory, &#8211;pbkdf-parallel, &#8211;disable-locks, &#8211;disable-keyring, &#8211;luks2-metadata-size, &#8211;luks2-keyslots-size, &#8211;keyslot-cipher, &#8211;keyslot-key-size]. </p>
<p> <code>WARNING:</code> Doing a luksFormat on an existing LUKS container will make all data the old container permanently irretrievable unless you have a header backup.</dl>
<p> <i>open</i> &#8211;type luks &lt;device&gt; &lt;name&gt;<br />
 <i>luksOpen</i> &lt;device&gt; &lt;name&gt; (<code>old syntax</code>)</p>
<dl>
<dd>Opens the LUKS device &lt;device&gt; and sets up a mapping &lt;name&gt; after successful verification of the supplied passphrase. </p>
<p> First, the passphrase is searched in LUKS tokens. If it&#8217;s not found in any token and also the passphrase is not supplied via &#8211;key-file, the command prompts for it interactively. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;readonly, &#8211;test-passphrase, &#8211;allow-discards, &#8211;header, &#8211;key-slot, &#8211;master-key-file, &#8211;token-id, &#8211;token-only, &#8211;disable-keyring, &#8211;disable-locks, &#8211;type, &#8211;refresh, &#8211;serialize-memory-hard-pbkdf].</dl>
<p> <i>luksSuspend</i> &lt;name&gt;</p>
<dl>
<dd>Suspends an active device (all IO operations will block and accesses to the device will wait indefinitely) and wipes the encryption key from kernel memory. Needs kernel 2.6.19 or later. </p>
<p> After this operation you have to use <i>luksResume</i> to reinstate the encryption key and unblock the device or <i>close</i> to remove the mapped device. </p>
<p> <code>WARNING:</code> never suspend the device on which the cryptsetup binary resides. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;header, &#8211;disable-locks].</dl>
<p> <i>luksResume</i> &lt;name&gt;</p>
<dl>
<dd>Resumes a suspended device and reinstates the encryption key. Prompts interactively for a passphrase if &#8211;key-file is not given. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-size, &#8211;header, &#8211;disable-keyring, &#8211;disable-locks, &#8211;type]</dl>
<p> <i>luksAddKey</i> &lt;device&gt; [&lt;key file with new key&gt;]</p>
<dl>
<dd>Adds a new passphrase. An existing passphrase must be supplied interactively or via &#8211;key-file. The new passphrase to be added can be specified interactively or read from the file given as positional argument. </p>
<p> <code>NOTE:</code> with &#8211;unbound option the action creates new unbound LUKS2 keyslot. The keyslot cannot be used for device activation. If you don&#8217;t pass new key via &#8211;master-key-file option, new random key is generated. Existing passphrase for any active keyslot is not required. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;new-keyfile-offset, &#8211;new-keyfile-size, &#8211;key-slot, &#8211;master-key-file, &#8211;force-password, &#8211;header, &#8211;disable-locks, &#8211;iter-time, &#8211;pbkdf, &#8211;pbkdf-force-iterations, &#8211;unbound, &#8211;type, &#8211;keyslot-cipher, &#8211;keyslot-key-size].</dl>
<p> <i>luksRemoveKey</i> &lt;device&gt; [&lt;key file with passphrase to be removed&gt;]</p>
<dl>
<dd>Removes the supplied passphrase from the LUKS device. The passphrase to be removed can be specified interactively, as the positional argument or via &#8211;key-file. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;header, &#8211;disable-locks, &#8211;type] </p>
<p> <code>WARNING:</code> If you read the passphrase from stdin (without further argument or with &#8216;-&#8216; as an argument to &#8211;key-file), batch-mode (-q) will be implicitly switched on and no warning will be given when you remove the last remaining passphrase from a LUKS container. Removing the last passphrase makes the LUKS container permanently inaccessible.</dl>
<p> <i>luksChangeKey</i> &lt;device&gt; [&lt;new key file&gt;]</p>
<dl>
<dd>Changes an existing passphrase. The passphrase to be changed must be supplied interactively or via &#8211;key-file. The new passphrase can be supplied interactively or in a file given as positional argument. </p>
<p> If a key-slot is specified (via &#8211;key-slot), the passphrase for that key-slot must be given and the new passphrase will overwrite the specified key-slot. If no key-slot is specified and there is still a free key-slot, then the new passphrase will be put into a free key-slot before the key-slot containing the old passphrase is purged. If there is no free key-slot, then the key-slot with the old passphrase is overwritten directly. </p>
<p> <code>WARNING:</code> If a key-slot is overwritten, a media failure during this operation can cause the overwrite to fail after the old passphrase has been wiped and make the LUKS container inaccessible. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;new-keyfile-offset, &#8211;iter-time, &#8211;pbkdf, &#8211;pbkdf-force-iterations, &#8211;new-keyfile-size, &#8211;key-slot, &#8211;force-password, &#8211;header, &#8211;disable-locks, &#8211;type, &#8211;keyslot-cipher, &#8211;keyslot-key-size].</dl>
<p> <i>luksConvertKey</i> &lt;device&gt;</p>
<dl>
<dd>Converts an existing LUKS2 keyslot to new pbkdf parameters. The passphrase for keyslot to be converted must be supplied interactively or via &#8211;key-file. If no &#8211;pbkdf parameters are specified LUKS2 default pbkdf values will apply. </p>
<p> If a keyslot is specified (via &#8211;key-slot), the passphrase for that keyslot must be given. If no keyslot is specified and there is still a free keyslot, then the new parameters will be put into a free keyslot before the keyslot containing the old parameters is purged. If there is no free keyslot, then the keyslot with the old parameters is overwritten directly. </p>
<p> <code>WARNING:</code> If a keyslot is overwritten, a media failure during this operation can cause the overwrite to fail after the old parameters have been wiped and make the LUKS container inaccessible. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;key-slot, &#8211;header, &#8211;disable-locks, &#8211;iter-time, &#8211;pbkdf, &#8211;pbkdf-force-iterations, &#8211;pbkdf-memory, &#8211;pbkdf-parallel, &#8211;keyslot-cipher, &#8211;keyslot-key-size].</dl>
<p> <i>luksKillSlot</i> &lt;device&gt; &lt;key slot number&gt;</p>
<dl>
<dd>Wipe the key-slot number &lt;key slot&gt; from the LUKS device. Except running in batch-mode (-q) a remaining passphrase must be supplied, either interactively or via &#8211;key-file. This command can remove the last remaining key-slot, but requires an interactive confirmation when doing so. Removing the last passphrase makes a LUKS container permanently inaccessible. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;header, &#8211;disable-locks, &#8211;type]. </p>
<p> <code>WARNING:</code> If you read the passphrase from stdin (without further argument or with &#8216;-&#8216; as an argument to &#8211;key-file), batch-mode (-q) will be implicitly switched on and no warning will be given when you remove the last remaining passphrase from a LUKS container. Removing the last passphrase makes the LUKS container permanently inaccessible. </p>
<p> <code>NOTE:</code> If there is no passphrase provided (on stdin or through &#8211;key-file argument) and batch-mode (-q) is active, the key-slot is removed without any other warning. </p>
</dl>
<p> <i>erase</i> &lt;device&gt;<br />
 <i>luksErase</i> &lt;device&gt;</p>
<dl>
<dd>Erase all keyslots and make the LUKS container permanently inaccessible. You do not need to provide any password for this operation. </p>
<p> <code>WARNING:</code> This operation is irreversible.</dl>
<p> <i>luksUUID</i> &lt;device&gt;</p>
<dl>
<dd>Print the UUID of a LUKS device.<br />
 Set new UUID if <i>&#8211;uuid</i> option is specified.</dl>
<p> <i>isLuks</i> &lt;device&gt;</p>
<dl>
<dd>Returns true, if &lt;device&gt; is a LUKS device, false otherwise. Use option -v to get human-readable feedback. &#8216;Command successful.&#8217; means the device is a LUKS device. </p>
<p> By specifying &#8211;type you may query for specific LUKS version.</dl>
<p> <i>luksDump</i> &lt;device&gt;</p>
<dl>
<dd>Dump the header information of a LUKS device. </p>
<p> If the &#8211;dump-master-key option is used, the LUKS device master key is dumped instead of the keyslot info. Together with &#8211;master-key-file option, master key is dumped to a file instead of standard output. Beware that the master key cannot be changed without reencryption and can be used to decrypt the data stored in the LUKS container without a passphrase and even without the LUKS header. This means that if the master key is compromised, the whole device has to be erased to prevent further access. Use this option carefully. </p>
<p> To dump the master key, a passphrase has to be supplied, either interactively or via &#8211;key-file. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;dump-master-key, &#8211;key-file, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;header, &#8211;disable-locks, &#8211;master-key-file, &#8211;type]. </p>
<p> <code>WARNING:</code> If &#8211;dump-master-key is used with &#8211;key-file and the argument to &#8211;key-file is &#8216;-&#8216;, no validation question will be asked and no warning given.</dl>
<p> <i>luksHeaderBackup</i> &lt;device&gt; &#8211;header-backup-file &lt;file&gt;</p>
<dl>
<dd>Stores a binary backup of the LUKS header and keyslot area.<br />
 Note: Using &#8216;-&#8216; as filename writes the header backup to a file named &#8216;-&#8216;. </p>
<p> <code>WARNING:</code> This backup file and a passphrase valid at the time of backup allows decryption of the LUKS data area, even if the passphrase was later changed or removed from the LUKS device. Also note that with a header backup you lose the ability to securely wipe the LUKS device by just overwriting the header and key-slots. You either need to securely erase all header backups in addition or overwrite the encrypted data area as well. The second option is less secure, as some sectors can survive, e.g. due to defect management.</dl>
<p> <i>luksHeaderRestore</i> &lt;device&gt; &#8211;header-backup-file &lt;file&gt;</p>
<dl>
<dd>Restores a binary backup of the LUKS header and keyslot area from the specified file.<br />
 Note: Using &#8216;-&#8216; as filename reads the header backup from a file named &#8216;-&#8216;. </p>
<p> <code>WARNING:</code> Header and keyslots will be replaced, only the passphrases from the backup will work afterward. </p>
<p> This command requires that the master key size and data offset of the LUKS header already on the device and of the header backup match. Alternatively, if there is no LUKS header on the device, the backup will also be written to it.</dl>
<p> <i>token</i> &lt;add|remove|import|export&gt; &lt;device&gt;</p>
<dl>
<dd>Action <i>add</i> creates new keyring token to enable auto-activation of the device. For the auto-activation, the passphrase must be stored in keyring with the specified description. Usually, the passphrase should be stored in <i>user</i> or <i>user-session</i> keyring. The <i>token</i> command is supported only for LUKS2. </p>
<p> For adding new keyring token, option &#8211;key-description is mandatory. Also, new token is assigned to key slot specified with &#8211;key-slot option or to all active key slots in the case &#8211;key-slot option is omitted. </p>
<p> To remove existing token, specify the token ID which should be removed with &#8211;token-id option. </p>
<p> <code>WARNING:</code> The action <i>token remove</i> removes any token type, not just <i>keyring</i> type from token slot specified by &#8211;token-id option. </p>
<p> Action <i>import</i> can store arbitrary valid token json in LUKS2 header. It may be passed via standard input or via file passed in &#8211;json-file option. If you specify &#8211;key-slot then successfully imported token is also assigned to the key slot. </p>
<p> Action <i>export</i> writes requested token json to a file passed with &#8211;json-file or to standard output. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;header, &#8211;token-id, &#8211;key-slot, &#8211;key-description, &#8211;disable-locks, &#8211;disable-keyring, &#8211;json-file].</dl>
<p> <i>convert</i> &lt;device&gt; &#8211;type &lt;format&gt;</p>
<dl>
<dd>Converts the device between LUKS1 and LUKS2 format (if possible). The conversion will not be performed if there is an additional LUKS2 feature or LUKS1 has unsupported header size. </p>
<p> Conversion (both directions) must be performed on inactive device. There must not be active dm-crypt mapping established for LUKS header requested for conversion. </p>
<p> <code>&#8211;type</code> option is mandatory with following accepted values: <i>luks1</i> or <i>luks2</i>. </p>
<p> <code>WARNING:</code> The <i>convert</i> action can destroy the LUKS header in the case of a crash during conversion or if a media error occurs. Always create a header backup before performing this operation! </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;header, &#8211;type].</dl>
<p> <i>config</i> &lt;device&gt;</p>
<dl>
<dd>Set permanent configuration options (store to LUKS header). The <i>config</i> command is supported only for LUKS2. </p>
<p> The permanent options can be <i>&#8211;priority</i> to set priority (normal, prefer, ignore) for keyslot (specified by <i>&#8211;key-slot</i>) or <i>&#8211;label</i> and <i>&#8211;subsystem</i>. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;priority, &#8211;label, &#8211;subsystem, &#8211;key-slot, &#8211;header]. </p>
</dl>
<h2>loop-AES EXTENSION</h2>
<p>cryptsetup supports mapping loop-AES encrypted partition using a compatibility mode. </p>
<p> <i>open</i> &#8211;type loopaes &lt;device&gt; &lt;name&gt; &#8211;key-file &lt;keyfile&gt;<br />
 <i>loopaesOpen</i> &lt;device&gt; &lt;name&gt; &#8211;key-file &lt;keyfile&gt; (<code>old syntax</code>)</p>
<dl>
<dd>Opens the loop-AES &lt;device&gt; and sets up a mapping &lt;name&gt;. </p>
<p> If the key file is encrypted with GnuPG, then you have to use &#8211;key-file=- and decrypt it before use, e.g. like this:<br />
 gpg &#8211;decrypt &lt;keyfile&gt; | cryptsetup loopaesOpen &#8211;key-file=- &lt;device&gt; &lt;name&gt; </p>
<p> <code>WARNING:</code> The loop-AES extension cannot use the direct input of key file on real terminal because the keys are separated by end-of-line and only part of the multi-key file would be read.<br />
 If you need it in script, just use the pipe redirection:<br />
 echo $keyfile | cryptsetup loopaesOpen &#8211;key-file=- &lt;device&gt; &lt;name&gt; </p>
<p> Use <code>&#8211;keyfile-size</code> to specify the proper key length if needed. </p>
<p> Use <code>&#8211;offset</code> to specify device offset. Note that the units need to be specified in number of 512 byte sectors. </p>
<p> Use <code>&#8211;skip</code> to specify the IV offset. If the original device used an offset and but did not use it in IV sector calculations, you have to explicitly use <code>&#8211;skip 0</code> in addition to the offset parameter. </p>
<p> Use <code>&#8211;hash</code> to override the default hash function for passphrase hashing (otherwise it is detected according to key size). </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;key-size, &#8211;offset, &#8211;skip, &#8211;hash, &#8211;readonly, &#8211;allow-discards, &#8211;refresh].</dl>
<p> See also section 7 of the FAQ and <code><a rel="nofollow" href="http://loop-aes.sourceforge.net">http://loop-aes.sourceforge.net</a></code> for more information regarding loop-AES.</p>
<h2>TCRYPT (TrueCrypt-compatible and VeraCrypt) EXTENSION</h2>
<p>cryptsetup supports mapping of TrueCrypt, tcplay or VeraCrypt (with <code>&#8211;veracrypt</code> option) encrypted partition using a native Linux kernel API. Header formatting and TCRYPT header change is not supported, cryptsetup never changes TCRYPT header on-device. </p>
<p> TCRYPT extension requires kernel userspace crypto API to be available (introduced in Linux kernel 2.6.38). If you are configuring kernel yourself, enable &quot;User-space interface for symmetric key cipher algorithms&quot; in &quot;Cryptographic API&quot; section (CRYPTO_USER_API_SKCIPHER .config option). </p>
<p> Because TCRYPT header is encrypted, you have to always provide valid passphrase and keyfiles. </p>
<p> Cryptsetup should recognize all header variants, except legacy cipher chains using LRW encryption mode with 64 bits encryption block (namely Blowfish in LRW mode is not recognized, this is limitation of kernel crypto API). </p>
<p> To recognize a VeraCrypt device use the <code>&#8211;veracrypt</code> option. VeraCrypt is just extension of TrueCrypt header with increased iteration count so unlocking can take quite a lot of time (in comparison with TCRYPT device). </p>
<p> To open a VeraCrypt device with a custom Personal Iteration Multiplier (PIM) value, <code>additionally to &#8211;veracrypt </code> use either the <code>&#8211;veracrypt-pim=&lt;PIM&gt;</code> option to directly specify the PIM on the command- line or use <code>&#8211;veracrypt-query-pim</code> to be prompted for the PIM. </p>
<p> The PIM value affects the number of iterations applied during key derivation. Please refer to <code><a rel="nofollow" href="https://www.veracrypt.fr/en/Personal%20Iterations%20Multiplier%20%28PIM%29.html">https://www.veracrypt.fr/en/Personal%20Iterations%20Multiplier%20%28PIM%29.html</a></code> for more detailed information. </p>
<p> <code>NOTE:</code> Activation with <code>tcryptOpen</code> is supported only for cipher chains using LRW or XTS encryption modes. </p>
<p> The <code>tcryptDump</code> command should work for all recognized TCRYPT devices and doesn&#8217;t require superuser privilege. </p>
<p> To map system device (device with boot loader where the whole encrypted system resides) use <code>&#8211;tcrypt-system</code> option. You can use partition device as the parameter (parameter must be real partition device, not an image in a file), then only this partition is mapped. </p>
<p> If you have the whole TCRYPT device as a file image and you want to map multiple partition encrypted with system encryption, please create loopback mapping with partitions first (<code>losetup -P</code>, see <a href="/docs/linux/man/8-losetup/">losetup</a>(8) man page for more info), and use loop partition as the device parameter. </p>
<p> If you use the whole base device as a parameter, one device for the whole system encryption is mapped. This mode is available only for backward compatibility with older cryptsetup versions which mapped TCRYPT system encryption using the whole device. </p>
<p> To use hidden header (and map hidden device, if available), use <code>&#8211;tcrypt-hidden</code> option. </p>
<p> To explicitly use backup (secondary) header, use <code>&#8211;tcrypt-backup</code> option. </p>
<p> <code>NOTE:</code> There is no protection for a hidden volume if the outer volume is mounted. The reason is that if there were any protection, it would require some metadata describing what to protect in the outer volume and the hidden volume would become detectable. </p>
<p> <i>open</i> &#8211;type tcrypt &lt;device&gt; &lt;name&gt;<br />
 <i>tcryptOpen</i> &lt;device&gt; &lt;name&gt; (<code>old syntax</code>)</p>
<dl>
<dd>Opens the TCRYPT (a TrueCrypt-compatible) &lt;device&gt; and sets up a mapping &lt;name&gt;. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;key-file, &#8211;tcrypt-hidden, &#8211;tcrypt-system, &#8211;tcrypt-backup, &#8211;readonly, &#8211;test-passphrase, &#8211;allow-discards, &#8211;veracrypt, &#8211;veracrypt-pim, &#8211;veracrypt-query-pim]. </p>
<p> The keyfile parameter allows a combination of file content with the passphrase and can be repeated. Note that using keyfiles is compatible with TCRYPT and is different from LUKS keyfile logic. </p>
<p> <code>WARNING:</code> Option <code>&#8211;allow-discards</code> cannot be combined with option <code>&#8211;tcrypt-hidden</code>. For normal mapping, it can cause the <code>destruction of hidden volume</code> (hidden volume appears as unused space for outer volume so this space can be discarded). </p>
</dl>
<p> <i>tcryptDump</i> &lt;device&gt;</p>
<dl>
<dd>Dump the header information of a TCRYPT device. </p>
<p> If the &#8211;dump-master-key option is used, the TCRYPT device master key is dumped instead of TCRYPT header info. Beware that the master key (or concatenated master keys if cipher chain is used) can be used to decrypt the data stored in the TCRYPT container without a passphrase. This means that if the master key is compromised, the whole device has to be erased to prevent further access. Use this option carefully. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;dump-master-key, &#8211;key-file, &#8211;tcrypt-hidden, &#8211;tcrypt-system, &#8211;tcrypt-backup]. </p>
<p> The keyfile parameter allows a combination of file content with the passphrase and can be repeated.</dl>
<p> See also <code><a rel="nofollow" href="https://en.wikipedia.org/wiki/TrueCrypt">https://en.wikipedia.org/wiki/TrueCrypt</a></code> for more information regarding TrueCrypt. </p>
<p> Please note that cryptsetup does not use TrueCrypt code, please report all problems related to this compatibility extension to the cryptsetup project.</p>
<h2>Miscellaneous</h2>
<p><i>repair</i> &lt;device&gt;</p>
<dl>
<dd>Tries to repair the device metadata if possible. Currently supported only for LUKS device type. </p>
<p> This command is useful to fix some known benign LUKS metadata header corruptions. Only basic corruptions of unused keyslot are fixable. This command will only change the LUKS header, not any key-slot data. You may enforce LUKS version by adding &#8211;type option. </p>
<p> <code>WARNING:</code> Always create a binary backup of the original header before calling this command.</dl>
<p> <i>benchmark</i> &lt;options&gt;</p>
<dl>
<dd>Benchmarks ciphers and KDF (key derivation function). Without parameters, it tries to measure few common configurations. </p>
<p> To benchmark other ciphers or modes, you need to specify <code>&#8211;cipher</code> and <code>&#8211;key-size</code> options or <code>&#8211;hash</code> for KDF test. </p>
<p> <code>NOTE:</code> This benchmark is using memory only and is only informative. You cannot directly predict real storage encryption speed from it. </p>
<p> For testing block ciphers, this benchmark requires kernel userspace crypto API to be available (introduced in Linux kernel 2.6.38). If you are configuring kernel yourself, enable &quot;User-space interface for symmetric key cipher algorithms&quot; in &quot;Cryptographic API&quot; section (CRYPTO_USER_API_SKCIPHER .config option). </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;cipher, &#8211;key-size, &#8211;hash].</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;verbose, -v</code></p>
<dd>Print more information on command execution.</p>
<dt><code>&#8211;debug or &#8211;debug-json</code></p>
<dd>Run in debug mode with full diagnostic logs. Debug output lines are always prefixed by &#8216;#&#8217;. If &#8211;debug-json is used, additional LUKS2 JSON data structures are printed.</p>
<dt><code>&#8211;type &lt;device-type&gt;</code></p>
<dd>Specifies required device type, for more info read <i>BASIC COMMANDS</i> section.</p>
<dt><code>&#8211;hash, -h </code><i>&lt;hash-spec&gt;</i></p>
<dd>Specifies the passphrase hash for <i>open</i> (for plain and loopaes device types). </p>
<p> Specifies the hash used in the LUKS key setup scheme and volume key digest for <i>luksFormat</i>. The specified hash is used as hash-parameter for PBKDF2 and for the AF splitter. </p>
<p> The specified hash name is passed to the compiled-in crypto backend. Different backends may support different hashes. For <i>luksFormat</i>, the hash algorithm must provide at least 160 bits of output, which excludes, e.g., MD5. Do not use a non-crypto hash like <code>&quot;crc32&quot;</code> as this breaks security. </p>
<p> Values compatible with old version of cryptsetup are <code>&quot;ripemd160&quot;</code> for <i>open &#8211;type plain</i> and <code>&quot;sha1&quot;</code> for <i>luksFormat</i>. </p>
<p> Use <i>cryptsetup &#8211;help</i> to show the defaults.</p>
<dt><code>&#8211;cipher, -c </code><i>&lt;cipher-spec&gt;</i></p>
<dd>Set the cipher specification string. </p>
<p> <i>cryptsetup &#8211;help</i> shows the compiled-in defaults. The current default in the distributed sources is &quot;aes-cbc-essiv:sha256&quot; for plain dm-crypt and &quot;aes-xts-plain64&quot; for LUKS. </p>
<p> If a hash is part of the cipher specification, then it is used as part of the IV generation. For example, ESSIV needs a hash function, while &quot;plain64&quot; does not and hence none is specified. </p>
<p> For XTS mode you can optionally set a key size of 512 bits with the -s option. Key size for XTS mode is twice that for other modes for the same security level. </p>
<p> XTS mode requires kernel 2.6.24 or later and plain64 requires kernel 2.6.33 or later. More information can be found in the FAQ.</p>
<dt><code>&#8211;verify-passphrase, -y</code></p>
<dd>When interactively asking for a passphrase, ask for it twice and complain if both inputs do not match. Advised when creating a regular mapping for the first time, or when running <i>luksFormat</i>. Ignored on input from file or stdin.</p>
<dt><code>&#8211;key-file, -d </code><i>name</i></p>
<dd>Read the passphrase from file. </p>
<p> If the name given is &quot;-&quot;, then the passphrase will be read from stdin. In this case, reading will not stop at newline characters. </p>
<p> With LUKS, passphrases supplied via &#8211;key-file are always the existing passphrases requested by a command, except in the case of <i>luksFormat</i> where &#8211;key-file is equivalent to the positional key file argument. </p>
<p> If you want to set a new passphrase via key file, you have to use a positional argument to <i>luksAddKey</i>. </p>
<p> See section <code>NOTES ON PASSPHRASE PROCESSING</code> for more information.</p>
<dt><code>&#8211;keyfile-offset </code><i>value</i></p>
<dd>Skip <i>value</i> bytes at the beginning of the key file. Works with all commands that accept key files.</p>
<dt><code>&#8211;keyfile-size, -l </code><i>value</i></p>
<dd>Read a maximum of <i>value</i> bytes from the key file. The default is to read the whole file up to the compiled-in maximum that can be queried with &#8211;help. Supplying more data than the compiled-in maximum aborts the operation. </p>
<p> This option is useful to cut trailing newlines, for example. If &#8211;keyfile-offset is also given, the size count starts after the offset. Works with all commands that accept key files.</p>
<dt><code>&#8211;new-keyfile-offset </code><i>value</i></p>
<dd>Skip <i>value</i> bytes at the start when adding a new passphrase from key file with <i>luksAddKey</i>.</p>
<dt><code>&#8211;new-keyfile-size </code><i>value</i></p>
<dd>Read a maximum of <i>value</i> bytes when adding a new passphrase from key file with <i>luksAddKey</i>. The default is to read the whole file up to the compiled-in maximum length that can be queried with &#8211;help. Supplying more than the compiled in maximum aborts the operation. When &#8211;new-keyfile-offset is also given, reading starts after the offset.</p>
<dt><code>&#8211;master-key-file</code></p>
<dd>Use a master key stored in a file. </p>
<p> For <i>luksFormat</i> this allows creating a LUKS header with this specific master key. If the master key was taken from an existing LUKS header and all other parameters are the same, then the new header decrypts the data encrypted with the header the master key was taken from. </p>
<p> Action <i>luksDump</i> together with &#8211;dump-master-key option: The volume (master) key is stored in a file instead of being printed out to standard output. </p>
<p> <code>WARNING:</code> If you create your own master key, you need to make sure to do it right. Otherwise, you can end up with a low-entropy or otherwise partially predictable master key which will compromise security. </p>
<p> For <i>luksAddKey</i> this allows adding a new passphrase without having to know an existing one. </p>
<p> For <i>open</i> this allows one to open the LUKS device without giving a passphrase.</p>
<dt><code>&#8211;dump-master-key</code></p>
<dd>For <i>luksDump</i> this option includes the master key in the displayed information. Use with care, as the master key can be used to bypass the passphrases, see also option &#8211;master-key-file.</p>
<dt><code>&#8211;json-file</code></p>
<dd>Read token json from a file or write token to it. See <i>token</i> action for more information. &#8211;json-file=- reads json from standard input or writes it to standard output respectively.</p>
<dt><code>&#8211;use-random</code></p>
<dd>
<dt><code>&#8211;use-urandom</code></p>
<dd>For <i>luksFormat</i> these options define which kernel random number generator will be used to create the master key (which is a long-term key). </p>
<p> See <code>NOTES ON RANDOM NUMBER GENERATORS</code> for more information. Use <i>cryptsetup &#8211;help</i> to show the compiled-in default random number generator. </p>
<p> <code>WARNING:</code> In a low-entropy situation (e.g. in an embedded system), both selections are problematic. Using /dev/urandom can lead to weak keys. Using /dev/random can block a long time, potentially forever, if not enough entropy can be harvested by the kernel.</p>
<dt><code>&#8211;key-slot, -S &lt;0-7&gt;</code></p>
<dd>For LUKS operations that add key material, this options allows you to specify which key slot is selected for the new key. This option can be used for <i>luksFormat</i>, and <i>luksAddKey</i>.<br />
 In addition, for <i>open</i>, this option selects a specific key-slot to compare the passphrase against. If the given passphrase would only match a different key-slot, the operation fails.</p>
<dt><code>&#8211;key-size, -s &lt;bits&gt;</code></p>
<dd>Sets key size in bits. The argument has to be a multiple of 8. The possible key-sizes are limited by the cipher and mode used. </p>
<p> See /proc/crypto for more information. Note that key-size in /proc/crypto is stated in bytes. </p>
<p> This option can be used for <i>open &#8211;type plain</i> or <i>luksFormat</i>. All other LUKS actions will use the key-size specified in the LUKS header. Use <i>cryptsetup &#8211;help</i> to show the compiled-in defaults.</p>
<dt><code>&#8211;size, -b &lt;number of 512 byte sectors&gt;</code></p>
<dd>Set the size of the device in sectors of 512 bytes. This option is only relevant for the <i>open</i> and <i>resize</i> actions.</p>
<dt><code>&#8211;offset, -o &lt;number of 512 byte sectors&gt;</code></p>
<dd>Start offset in the backend device in 512-byte sectors. This option is only relevant for the <i>open</i> action with plain or loopaes device types or for LUKS devices in <i>luksFormat</i>. </p>
<p> For LUKS, the &#8211;offset option sets the data offset (payload) of data device and must be be aligned to 4096-byte sectors (must be multiple of 8). This option cannot be combined with &#8211;align-payload option.</p>
<dt><code>&#8211;skip, -p &lt;number of 512 byte sectors&gt;</code></p>
<dd>Start offset used in IV calculation in 512-byte sectors (how many sectors of the encrypted data to skip at the beginning). This option is only relevant for the <i>open</i> action with plain or loopaes device types. </p>
<p> Hence, if &#8211;offset <i>n</i>, and &#8211;skip <i>s</i>, sector <i>n</i> (the first sector of the encrypted device) will get a sector number of <i>s</i> for the IV calculation.</p>
<dt><code>&#8211;device-size </code><i>size[units]</i></p>
<dd>Instead of real device size, use specified value. </p>
<p> With <i>reencrypt</i> action it means that only specified area (from the start of the device to the specified size) will be reencrypted. </p>
<p> With <i>resize</i> action it sets new size of the device. </p>
<p> If no unit suffix is specified, the size is in bytes. </p>
<p> Unit suffix can be S for 512 byte sectors, K/M/G/T (or KiB,MiB,GiB,TiB) for units with 1024 base or KB/MB/GB/TB for 1000 base (SI scale). </p>
<p> <code>WARNING:</code> This is destructive operation when used with reencrypt command.</p>
<dt><code>&#8211;readonly, -r</code></p>
<dd>set up a read-only mapping.</p>
<dt><code>&#8211;shared</code></p>
<dd>Creates an additional mapping for one common ciphertext device. Arbitrary mappings are supported. This option is only relevant for the <i>open &#8211;type plain</i> action. Use &#8211;offset, &#8211;size and &#8211;skip to specify the mapped area.</p>
<dt><code>&#8211;pbkdf &lt;PBKDF spec&gt;</code></p>
<dd>Set Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. The PBKDF can be: <i>pbkdf2</i> (for PBKDF2 according to RFC2898), <i>argon2i</i> for Argon2i or <i>argon2id</i> for Argon2id (see <a rel="nofollow" href="https://www.cryptolux.org/index.php/Argon2">https://www.cryptolux.org/index.php/Argon2</a> for more info). </p>
<p> For LUKS1, only PBKDF2 is accepted (no need to use this option). The default PBKDF2 for LUKS2 is set during compilation time and is available in <i>cryptsetup &#8211;help</i> output. </p>
<p> A PBKDF is used for increasing dictionary and brute-force attack cost for keyslot passwords. The parameters can be time, memory and parallel cost. </p>
<p> For PBKDF2, only time cost (number of iterations) applies. For Argon2i/id, there is also memory cost (memory required during the process of key derivation) and parallel cost (number of threads that run in parallel during the key derivation. </p>
<p> Note that increasing memory cost also increases time, so the final parameter values are measured by a benchmark. The benchmark tries to find iteration time (<i>&#8211;iter-time</i>) with required memory cost <i>&#8211;pbkdf-memory</i>. If it is not possible, the memory cost is decreased as well. The parallel cost <i>&#8211;pbkdf-parallel</i> is constant, is is checked against available CPU cores (if not available, it is decreased) and the maximum parallel cost is 4. </p>
<p> You can see all PBKDF parameters for particular LUKS2 keyslot with <i>luksDump</i> command. </p>
<p> <code>NOTE:</code> If you do not want to use benchmark and want to specify all parameters directly, use <i>&#8211;pbkdf-force-iterations</i> with <i>&#8211;pbkdf-memory</i> and <i>&#8211;pbkdf-parallel</i>. This will override the values without benchmarking. Note it can cause extremely long unlocking time. Use only is specified cases, for example, if you know that the formatted device will be used on some small embedded system. In this case, the LUKS PBKDF2 digest will be set to the minimum iteration count.</p>
<dt><code>&#8211;iter-time, -i &lt;number of milliseconds&gt;</code></p>
<dd>The number of milliseconds to spend with PBKDF passphrase processing. This option is only relevant for LUKS operations that set or change passphrases, such as <i>luksFormat</i> or <i>luksAddKey</i>. Specifying 0 as parameter selects the compiled-in default.</p>
<dt><code>&#8211;pbkdf-memory &lt;number&gt;</code></p>
<dd>Set the memory cost for PBKDF (for Argon2i/id the number represents kilobytes). Note that it is maximal value, PBKDF benchmark or available physical memory can decrease it. This option is not available for PBKDF2.</p>
<dt><code>&#8211;pbkdf-parallel &lt;number&gt;</code></p>
<dd>Set the parallel cost for PBKDF (number of threads, up to 4). Note that it is maximal value, it is decreased automatically if CPU online count is lower. This option is not available for PBKDF2.</p>
<dt><code>&#8211;pbkdf-force-iterations &lt;num&gt;</code></p>
<dd>Avoid PBKDF benchmark and set time cost (iterations) directly. It can be used for LUKS/LUKS2 device only. See <i>&#8211;pbkdf</i> option for more info.</p>
<dt><code>&#8211;batch-mode, -q</code></p>
<dd>Suppresses all confirmation questions. Use with care! </p>
<p> If the -y option is not specified, this option also switches off the passphrase verification for <i>luksFormat</i>.</p>
<dt><code>&#8211;progress-frequency &lt;seconds&gt;</code></p>
<dd>Print separate line every &lt;seconds&gt; with wipe progress.</p>
<dt><code>&#8211;timeout, -t &lt;number of seconds&gt;</code></p>
<dd>The number of seconds to wait before timeout on passphrase input via terminal. It is relevant every time a passphrase is asked, for example for <i>open</i>, <i>luksFormat</i> or <i>luksAddKey</i>. It has no effect if used in conjunction with &#8211;key-file.<br />
 This option is useful when the system should not stall if the user does not input a passphrase, e.g. during boot. The default is a value of 0 seconds, which means to wait forever.</p>
<dt><code>&#8211;tries, -T</code></p>
<dd>How often the input of the passphrase shall be retried. This option is relevant every time a passphrase is asked, for example for <i>open</i>, <i>luksFormat</i> or <i>luksAddKey</i>. The default is 3 tries.</p>
<dt><code>&#8211;align-payload &lt;number of 512 byte sectors&gt;</code></p>
<dd>Align payload at a boundary of <i>value</i> 512-byte sectors. This option is relevant for <i>luksFormat</i>. </p>
<p> If not specified, cryptsetup tries to use the topology info provided by the kernel for the underlying device to get the optimal alignment. If not available (or the calculated value is a multiple of the default) data is by default aligned to a 1MiB boundary (i.e. 2048 512-byte sectors). </p>
<p> For a detached LUKS header, this option specifies the offset on the data device. See also the &#8211;header option. </p>
<p> <code>WARNING:</code> This option is DEPRECATED and has often unexpected impact to the data offset and keyslot area size (for LUKS2) due to the complex rounding. For fixed data device offset use <i>&#8211;offset</i> option instead. </p>
<dt><code>&#8211;uuid=</code><i>UUID</i></p>
<dd>Use the provided <i>UUID</i> for the <i>luksFormat</i> command instead of generating a new one. Changes the existing UUID when used with the <i>luksUUID</i> command. </p>
<p> The UUID must be provided in the standard UUID format, e.g. 12345678-1234-1234-1234-123456789abc.</p>
<dt><code>&#8211;allow-discards</code></p>
<dd>Allow the use of discard (TRIM) requests for the device. This option is only relevant for <i>open</i> action. </p>
<p> <code>WARNING:</code> This command can have a negative security impact because it can make filesystem-level operations visible on the physical device. For example, information leaking filesystem type, used space, etc. may be extractable from the physical device if the discarded blocks can be located later. If in doubt, do not use it. </p>
<p> A kernel version of 3.1 or later is needed. For earlier kernels, this option is ignored.</p>
<dt><code>&#8211;perf-same_cpu_crypt</code></p>
<dd>Perform encryption using the same cpu that IO was submitted on. The default is to use an unbound workqueue so that encryption work is automatically balanced between available CPUs. This option is only relevant for <i>open</i> action. </p>
<p> <code>NOTE:</code> This option is available only for low-level dm-crypt performance tuning, use only if you need a change to default dm-crypt behaviour. Needs kernel 4.0 or later.</p>
<dt><code>&#8211;perf-submit_from_crypt_cpus</code></p>
<dd>Disable offloading writes to a separate thread after encryption. There are some situations where offloading write bios from the encryption threads to a single thread degrades performance significantly. The default is to offload write bios to the same thread. This option is only relevant for <i>open</i> action. </p>
<p> <code>NOTE:</code> This option is available only for low-level dm-crypt performance tuning, use only if you need a change to default dm-crypt behaviour. Needs kernel 4.0 or later.</p>
<dt><code>&#8211;test-passphrase</code></p>
<dd>Do not activate the device, just verify passphrase. This option is only relevant for <i>open</i> action (the device mapping name is not mandatory if this option is used).</p>
<dt><code>&#8211;header</code> &lt;device or file storing the LUKS header&gt;</p>
<dd>Use a detached (separated) metadata device or file where the LUKS header is stored. This option allows one to store ciphertext and LUKS header on different devices. </p>
<p> This option is only relevant for LUKS devices and can be used with the <i>luksFormat</i>, <i>open</i>, <i>luksSuspend</i>, <i>luksResume</i>, <i>status</i> and <i>resize</i> commands. </p>
<p> For <i>luksFormat</i> with a file name as the argument to &#8211;header, the file will be automatically created if it does not exist. See the cryptsetup FAQ for header size calculation. </p>
<p> For other commands that change the LUKS header (e.g. <i>luksAddKey</i>), specify the device or file with the LUKS header directly as the LUKS device. </p>
<p> If used with <i>luksFormat</i>, the &#8211;align-payload option is taken as absolute sector alignment on ciphertext device and can be zero. </p>
<p> <code>WARNING:</code> There is no check whether the ciphertext device specified actually belongs to the header given. In fact, you can specify an arbitrary device as the ciphertext device for <i>open</i> with the &#8211;header option. Use with care.</p>
<dt><code>&#8211;header-backup-file &lt;file&gt;</code></p>
<dd>Specify file with header backup for <i>luksHeaderBackup</i> or <i>luksHeaderRestore</i> actions.</p>
<dt><code>&#8211;force-password</code></p>
<dd>Do not use password quality checking for new LUKS passwords. </p>
<p> This option applies only to <i>luksFormat</i>, <i>luksAddKey</i> and <i>luksChangeKey</i> and is ignored if cryptsetup is built without password quality checking support. </p>
<p> For more info about password quality check, see the manual page for <code><a href="/docs/linux/man/5-pwquality-conf/">pwquality.conf</a>(5)</code> and <code><a href="/docs/linux/man/5-passwdqc-conf/">passwdqc.conf</a>(5)</code>.</p>
<dt><code>&#8211;deferred</code></p>
<dd>Defers device removal in <i>close</i> command until the last user closes it.</p>
<dt><code>&#8211;disable-locks</code></p>
<dd>Disable lock protection for metadata on disk. This option is valid only for LUKS2 and ignored for other formats. </p>
<p> <code>WARNING:</code> Do not use this option unless you run cryptsetup in a restricted environment where locking is impossible to perform (where /run directory cannot be used).</p>
<dt><code>&#8211;disable-keyring</code></p>
<dd>Do not load volume key in kernel keyring and store it directly in the dm-crypt target instead. This option is supported only for the LUKS2 format.</p>
<dt><code>&#8211;key-description &lt;text&gt;</code></p>
<dd>Set key description in keyring for use with <i>token</i> command.</p>
<dt><code>&#8211;priority &lt;normal|prefer|ignore&gt;</code></p>
<dd>Set a priority for LUKS2 keyslot. The <i>prefer</i> priority marked slots are tried before <i>normal</i> priority. The <i>ignored</i> priority means, that slot is never used, if not explicitly requested by <i>&#8211;key-slot</i> option.</p>
<dt><code>&#8211;token-id</code></p>
<dd>Specify what token to use in actions <i>token</i>, <i>open</i> or <i>resize</i>. If omitted, all available tokens will be checked before proceeding further with passphrase prompt.</p>
<dt><code>&#8211;token-only</code></p>
<dd>Do not proceed further with action (any of <i>token</i>, <i>open</i> or <i>resize</i>) if token activation failed. Without the option, action asks for passphrase to proceed further.</p>
<dt><code>&#8211;sector-size &lt;bytes&gt;</code></p>
<dd>Set sector size for use with disk encryption. It must be power of two and in range 512 &#8211; 4096 bytes. The default is 512 bytes sectors. This option is available only in the LUKS2 mode. </p>
<p> Note that if sector size is higher than underlying device hardware sector and there is not integrity protection that uses data journal, using this option can increase risk on incomplete sector writes during a power fail. </p>
<p> If used together with <i>&#8211;integrity</i> option and dm-integrity journal, the atomicity of writes is guaranteed in all cases (but it cost write performance &#8211; data has to be written twice). </p>
<p> Increasing sector size from 512 bytes to 4096 bytes can provide better performance on most of the modern storage devices and also with some hw encryption accelerators.</p>
<dt><code>&#8211;persistent</code></p>
<dd>If used with LUKS2 devices and activation commands like <i>open</i>, the specified activation flags are persistently written into metadata and used next time automatically even for normal activation. (No need to use cryptab or other system configuration files.) Only <i>&#8211;allow-discards</i>, <i>&#8211;perf-same_cpu_crypt</i>, <i>&#8211;perf-submit_from_crypt_cpus</i> and <i>&#8211;integrity-no-journal</i> can be stored persistently.</p>
<dt><code>&#8211;refresh</code></p>
<dd>Refreshes an active device with new set of parameters. See action <i>refresh</i> description for more details.</p>
<dt><code>&#8211;label &lt;LABEL&gt;</code></p>
<dd><code>&#8211;subsystem &lt;SUBSYSTEM&gt;</code> Set label and subsystem description for LUKS2 device, can be used in <i>config</i> and <i>format</i> actions. The label and subsystem are optional fields and can be later used in udev scripts for triggering user actions once device marked by these labels is detected.</p>
<dt><code>&#8211;integrity &lt;integrity algorithm&gt;</code></p>
<dd>Specify integrity algorithm to be used for authenticated disk encryption in LUKS2. </p>
<p> <code>WARNING: This extension is EXPERIMENTAL</code> and requires dm-integrity kernel target (available since kernel version 4.12). For native AEAD modes, also enable &quot;User-space interface for AEAD cipher algorithms&quot; in &quot;Cryptographic API&quot; section (CONFIG_CRYPTO_USER_API_AEAD .config option). </p>
<p> For more info, see <i>AUTHENTICATED DISK ENCRYPTION</i> section.</p>
<dt><code>&#8211;luks2-metadata-size &lt;size&gt;</code></p>
<dd>This option can be used to enlarge the LUKS2 metadata (JSON) area. The size includes 4096 bytes for binary metadata (usable JSON area is smaller of the binary area). According to LUKS2 specification, only these values are valid: 16, 32, 64, 128, 256, 512, 1024, 2048 and 4096 kB The &lt;size&gt; can be specified with unit suffix (for example 128k).</p>
<dt><code>&#8211;luks2-keyslots-size &lt;size&gt;</code></p>
<dd>This option can be used to set specific size of the LUKS2 binary keyslot area (key material is encrypted there). The value must be aligned to multiple of 4096 bytes with maximum size 128MB. The &lt;size&gt; can be specified with unit suffix (for example 128k).</p>
<dt><code>&#8211;keyslot-cipher &lt;cipher-spec&gt;</code></p>
<dd>This option can be used to set specific cipher encryption for the LUKS2 keyslot area.</p>
<dt><code>&#8211;keyslot-key-size &lt;bits&gt;</code></p>
<dd>This option can be used to set specific key size for the LUKS2 keyslot area.</p>
<dt><code>&#8211;integrity-no-journal</code></p>
<dd>Activate device with integrity protection without using data journal (direct write of data and integrity tags). Note that without journal power fail can cause non-atomic write and data corruption. Use only if journalling is performed on a different storage layer.</p>
<dt><code>&#8211;integrity-no-wipe</code></p>
<dd>Skip wiping of device authentication (integrity) tags. If you skip this step, sectors will report invalid integrity tag until an application write to the sector. </p>
<p> <code>NOTE:</code> Even some writes to the device can fail if the write is not aligned to page size and page-cache initiates read of a sector with invalid integrity tag.</p>
<dt><code>&#8211;unbound</code></p>
<dd>Creates new LUKS2 unbound keyslot. See <i>luksAddKey</i> action for more details.</p>
<dt><code>&#8211;tcrypt-hidden</code></p>
<dd><code>&#8211;tcrypt-system</code> <code>&#8211;tcrypt-backup</code> Specify which TrueCrypt on-disk header will be used to open the device. See <i>TCRYPT</i> section for more info.</p>
<dt><code>&#8211;veracrypt</code></p>
<dd>Allow VeraCrypt compatible mode. Only for TCRYPT extension. See <i>TCRYPT</i> section for more info.</p>
<dt><code>&#8211;veracrypt-pim</code></p>
<dd><code>&#8211;veracrypt-query-pim</code> Use a custom Personal Iteration Multiplier (PIM) for VeraCrypt device. See <i>TCRYPT</i> section for more info.</p>
<dt><code>&#8211;serialize-memory-hard-pbkdf</code></p>
<dd>Use a global lock to serialize unlocking of keyslots using memory-hard PBKDF. </p>
<p> <code>NOTE:</code> This is (ugly) workaround for a specific situation when multiple devices are activated in parallel and system instead of reporting out of memory starts unconditionally stop processes using out-of-memory killer. </p>
<p> <code>DO NOT USE</code> this switch until you are implementing boot environment with parallel devices activation!</p>
<dt><code>&#8211;encrypt</code></p>
<dd>Initialize (and run) device encryption (<i>reencrypt</i> action parameter)</p>
<dt><code>&#8211;decrypt</code></p>
<dd>Initialize (and run) device decryption (<i>reencrypt</i> action parameter)</p>
<dt><code>&#8211;init-only</code></p>
<dd>Initialize reencryption (any variant) operation in LUKS2 metadata only and exit. If any reencrypt operation is already initialized in metadata, the command with &#8211;init-only parameter fails.</p>
<dt><code>&#8211;resume-only</code></p>
<dd>Resume reencryption (any variant) operation already described in LUKS2 metadata. If no reencrypt operation is initialized, the command with &#8211;resume-only parameter fails. Useful for resuming reencrypt operation without accidentally triggering new reencryption operation.</p>
<dt><code>&#8211;resilience &lt;mode&gt;</code></p>
<dd>Reencryption resilience mode can be one of <i>checksum</i>, <i>journal</i> or <i>none</i>. </p>
<p> <i>checksum</i>: default mode, where individual checksums of ciphertext hotzone sectors are stored, so the recovery process can detect which sectors where already reencrypted. It requires that the device sector write is atomic. </p>
<p> <i>journal</i>: the hotzone is journaled in the binary area (so the data are written twice). </p>
<p> <i>none</i>: performance mode. There is no protection and the only way it&#8217;s safe to interrupt the reencryption is similar to old offline reencryption utility. (ctrl+c). </p>
<p> The option is ignored if reencryption with datashift mode is in progress.</p>
<dt><code>&#8211;resilience-hash &lt;hash&gt;</code></p>
<dd>The hash algorithm used with &quot;&#8211;resilience checksum&quot; only. The default hash is sha256. With other resilience modes, the hash parameter is ignored.</p>
<dt><code>&#8211;hotzone-size &lt;size&gt;</code></p>
<dd>This option can be used to set an upper limit on the size of reencryption area (hotzone). The &lt;size&gt; can be specified with unit suffix (for example 50M). Note that actual hotzone size may be less than specified &lt;size&gt; due to other limitations (free space in keyslots area or available memory).</p>
<dt><code>&#8211;reduce-device-size &lt;size&gt;</code></p>
<dd>Initialize LUKS2 reencryption with data device size reduction (currently only &#8211;encrypt variant is supported). </p>
<p> Last &lt;size&gt; sectors of &lt;device&gt; will be used to properly initialize device reencryption. That means any data at last &lt;size&gt; sectors will be lost. </p>
<p> It could be useful if you added some space to underlying partition or logical volume (so last &lt;size&gt; sectors contains no data). </p>
<p> Recommended minimal size is twice the default LUKS2 header size (&#8211;reduce-device-size 32M) for &#8211;encrypt use case. Be sure to have enough (at least &#8211;reduce-device-size value of free space at the end of &lt;device&gt;). </p>
<p> WARNING: This is a destructive operation and cannot be reverted. Use with extreme care &#8211; accidentally overwritten filesystems are usually unrecoverable.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the program version.</p>
<dt><code>&#8211;usage</code></p>
<dd>Show short option help.</p>
<dt><code>&#8211;help, -?</code></p>
<dd>Show help text and default parameters.</dl>
<h2>Return Codes</h2>
<p>Cryptsetup returns 0 on success and a non-zero value on error. </p>
<p> Error codes are: 1 wrong parameters, 2 no permission (bad passphrase), 3 out of memory, 4 wrong device specified, 5 device already exists or device is busy.</p>
<h2>Notes On Passphrase Processing For Plain Mode</h2>
<p>Note that no iterated hashing or salting is done in plain mode. If hashing is done, it is a single direct hash. This means that low-entropy passphrases are easy to attack in plain mode. </p>
<p> <code>From a terminal</code>: The passphrase is read until the first newline, i.e. &#8216;
&#8217;. The input without the newline character is processed with the default hash or the hash specified with &#8211;hash. The hash result will be truncated to the key size of the used cipher, or the size specified with -s. </p>
<p> <code>From stdin</code>: Reading will continue until a newline (or until the maximum input size is reached), with the trailing newline stripped. The maximum input size is defined by the same compiled-in default as for the maximum key file size and can be overwritten using &#8211;keyfile-size option. </p>
<p> The data read will be hashed with the default hash or the hash specified with &#8211;hash. The hash result will be truncated to the key size of the used cipher, or the size specified with -s. </p>
<p> Note that if &#8211;key-file=- is used for reading the key from stdin, trailing newlines are not stripped from the input. </p>
<p> If &quot;plain&quot; is used as argument to &#8211;hash, the input data will not be hashed. Instead, it will be zero padded (if shorter than the key size) or truncated (if longer than the key size) and used directly as the binary key. This is useful for directly specifying a binary key. No warning will be given if the amount of data read from stdin is less than the key size. </p>
<p> <code>From a key file</code>: It will be truncated to the key size of the used cipher or the size given by -s and directly used as a binary key. </p>
<p> <code>WARNING</code>: The &#8211;hash argument is being ignored. The &#8211;hash option is usable only for stdin input in plain mode. </p>
<p> If the key file is shorter than the key, cryptsetup will quit with an error. The maximum input size is defined by the same compiled-in default as for the maximum key file size and can be overwritten using &#8211;keyfile-size option.</p>
<h2>Notes On Passphrase Processing For Luks</h2>
<p>LUKS uses PBKDF2 to protect against dictionary attacks and to give some protection to low-entropy passphrases (see RFC 2898 and the cryptsetup FAQ). </p>
<p> <code>From a terminal</code>: The passphrase is read until the first newline and then processed by PBKDF2 without the newline character. </p>
<p> <code>From stdin</code>: LUKS will read passphrases from stdin up to the first newline character or the compiled-in maximum key file length. If &#8211;keyfile-size is given, it is ignored. </p>
<p> <code>From key file</code>: The complete keyfile is read up to the compiled-in maximum size. Newline characters do not terminate the input. The &#8211;keyfile-size option can be used to limit what is read. </p>
<p> <code>Passphrase processing</code>: Whenever a passphrase is added to a LUKS header (luksAddKey, luksFormat), the user may specify how much the time the passphrase processing should consume. The time is used to determine the iteration count for PBKDF2 and higher times will offer better protection for low-entropy passphrases, but open will take longer to complete. For passphrases that have entropy higher than the used key length, higher iteration times will not increase security. </p>
<p> The default setting of one or two seconds is sufficient for most practical cases. The only exception is a low-entropy passphrase used on a device with a slow CPU, as this will result in a low iteration count. On a slow device, it may be advisable to increase the iteration time using the &#8211;iter-time option in order to obtain a higher iteration count. This does slow down all later luksOpen operations accordingly.</p>
<h2>Incoherent Behavior For Invalid Passphrases/Keys</h2>
<p>LUKS checks for a valid passphrase when an encrypted partition is unlocked. The behavior of plain dm-crypt is different. It will always decrypt with the passphrase given. If the given passphrase is wrong, the device mapped by plain dm-crypt will essentially still contain encrypted data and will be unreadable.</p>
<h2>Notes On Supported Ciphers, Modes, Hashes And Key Sizes</h2>
<p>The available combinations of ciphers, modes, hashes and key sizes depend on kernel support. See /proc/crypto for a list of available options. You might need to load additional kernel crypto modules in order to get more options. </p>
<p> For the &#8211;hash option, if the crypto backend is libgcrypt, then all algorithms supported by the gcrypt library are available. For other crypto backends, some algorithms may be missing.</p>
<h2>Notes On Passphrases</h2>
<p>Mathematics can&#8217;t be bribed. Make sure you keep your passphrases safe. There are a few nice tricks for constructing a fallback, when suddenly out of the blue, your brain refuses to cooperate. These fallbacks need LUKS, as it&#8217;s only possible with LUKS to have multiple passphrases. Still, if your attacker model does not prevent it, storing your passphrase in a sealed envelope somewhere may be a good idea as well.</p>
<h2>Notes On Random Number Generators</h2>
<p>Random Number Generators (RNG) used in cryptsetup are always the kernel RNGs without any modifications or additions to data stream produced. </p>
<p> There are two types of randomness cryptsetup/LUKS needs. One type (which always uses /dev/urandom) is used for salts, the AF splitter and for wiping deleted keyslots. </p>
<p> The second type is used for the volume (master) key. You can switch between using /dev/random and /dev/urandom here, see &#8211;use-random and &#8211;use-urandom options. Using /dev/random on a system without enough entropy sources can cause luksFormat to block until the requested amount of random data is gathered. In a low-entropy situation (embedded system), this can take a very long time and potentially forever. At the same time, using /dev/urandom in a low-entropy situation will produce low-quality keys. This is a serious problem, but solving it is out of scope for a mere man-page. See <a href="/docs/linux/man/4-urandom/">urandom</a>(4) for more information.</p>
<h2>Authenticated Disk Encryption (Experimental)</h2>
<p>Since Linux kernel version 4.12 dm-crypt supports authenticated disk encryption. </p>
<p> Normal disk encryption modes are length-preserving (plaintext sector is of the same size as a ciphertext sector) and can provide only confidentiality protection, but not cryptographically sound data integrity protection. </p>
<p> Authenticated modes require additional space per-sector for authentication tag and use Authenticated Encryption with Additional Data (AEAD) algorithms. </p>
<p> If you configure LUKS2 device with data integrity protection, there will be an underlying dm-integrity device, which provides additional per-sector metadata space and also provide data journal protection to ensure atomicity of data and metadata update. Because there must be additional space for metadata and journal, the available space for the device will be smaller than for length-preserving modes. </p>
<p> The dm-crypt device then resides on top of such a dm-integrity device. All activation and deactivation of this device stack is performed by cryptsetup, there is no difference in using <i>luksOpen</i> for integrity protected devices. If you want to format LUKS2 device with data integrity protection, use <i>&#8211;integrity</i> option. </p>
<p> Some integrity modes requires two independent keys (key for encryption and for authentication). Both these keys are stored in one LUKS keyslot. </p>
<p> <code>WARNING:</code> All support for authenticated modes is experimental and there are only some modes available for now. Note that there are a very few authenticated encryption algorithms that are suitable for disk encryption.</p>
<h2>Notes On Loopback Device Use</h2>
<p>Cryptsetup is usually used directly on a block device (disk partition or LVM volume). However, if the device argument is a file, cryptsetup tries to allocate a loopback device and map it into this file. This mode requires Linux kernel 2.6.25 or more recent which supports the loop autoclear flag (loop device is cleared on the last close automatically). Of course, you can always map a file to a loop-device manually. See the cryptsetup FAQ for an example. </p>
<p> When device mapping is active, you can see the loop backing file in the status command output. Also see <a href="/docs/linux/man/8-losetup/">losetup</a>(8).</p>
<h2>LUKS2 header locking</h2>
<p>The LUKS2 on-disk metadata is updated in several steps and to achieve proper atomic update, there is a locking mechanism. For an image in file, code uses <i><a href="/docs/linux/man/2-flock/">flock</a>(2)</i> system call. For a block device, lock is performed over a special file stored in a locking directory (by default <i>/run/lock/cryptsetup</i>). The locking directory should be created with the proper security context by the distribution during the boot-up phase. Only LUKS2 uses locks, other formats do not use this mechanism.</p>
<h2>Deprecated Actions</h2>
<p>The <i>reload</i> action is no longer supported. Please use <i><a href="/docs/linux/man/8-dmsetup/">dmsetup</a>(8)</i> if you need to directly manipulate with the device mapping table. </p>
<p> The <i>luksDelKey</i> was replaced with <i>luksKillSlot</i>.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs, including ones in the documentation, on the cryptsetup mailing list at &lt;dm-crypt [at] saout.de&gt; or in the &#8216;Issues&#8217; section on LUKS website. Please attach the output of the failed command with the &#8211;debug option added.</p>
<h2>Authors</h2>
<p>cryptsetup originally written by Jana Saout &lt;jana [at] saout.de&gt;<br />
 The LUKS extensions and original man page were written by Clemens Fruhwirth &lt;clemens [at] endorphin.org&gt;.<br />
 Man page extensions by Milan Broz &lt;gmazyland [at] gmail.com&gt;.<br />
 Man page rewrite and extension by Arno Wagner &lt;arno [at] wagner.name&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004 Jana Saout<br />
 Copyright &#169; 2004-2006 Clemens Fruhwirth<br />
 Copyright &#169; 2012-2014 Arno Wagner<br />
 Copyright &#169; 2009-2019 Red Hat, Inc.<br />
 Copyright &#169; 2009-2019 Milan Broz </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>The LUKS website at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup/">https://gitlab.com/cryptsetup/cryptsetup/</a></code> The cryptsetup FAQ, contained in the distribution package and online at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions">https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions</a></code> The cryptsetup mailing list and list archive, see FAQ entry 1.6. The LUKS on-disk format specification available at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup/wikis/Specification">https://gitlab.com/cryptsetup/cryptsetup/wikis/Specification</a></code> </p>
