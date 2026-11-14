---
title: "cryptsetup-reencrypt(8)"
name: "cryptsetup-reencrypt"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cryptsetup-reencrypt/"
description: "cryptsetup-reencrypt – tool for offline LUKS device re-encryption"
---

<p>cryptsetup-reencrypt &#8211; tool for offline LUKS device re-encryption</p>
<h2>Synopsis</h2>
<p><code>cryptsetup-reencrypt &lt;options&gt; &lt;device&gt;</code></p>
<h2>Description</h2>
<p>Cryptsetup-reencrypt can be used to change reencryption parameters which otherwise require full on-disk data change (re-encryption). You can regenerate <code>volume key</code> (the real key used in on-disk encryption unclocked by passphrase), <code>cipher</code>, <code>cipher mode</code>. Cryptsetup-reencrypt reencrypts data on LUKS device in-place. During reencryption process the LUKS device is marked unavailable. <i>NOTE</i>: If you&#8217;re looking for LUKS2 online reencryption manual please read <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8) man page instead (see reencrypt action). This page is for legacy offline reencryption utility only. <i>WARNING</i>: The cryptsetup-reencrypt program is not resistant to hardware or kernel failures during reencryption (you can lose your data in this case). <i>ALWAYS BE SURE YOU HAVE RELIABLE BACKUP BEFORE USING THIS TOOL.</i><br />
 The reencryption can be temporarily suspended (by TERM signal or by using ctrl+c) but you need to retain temporary files named LUKS-&lt;uuid&gt;.[log|org|new]. LUKS device is unavailable until reencryption is finished though. Current working directory must be writable and temporary files created during reencryption must be present. For more info about LUKS see <a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8). </p>
<h2>Options</h2>
<dl>
<dt>To start (or continue) re-encryption for &lt;device&gt; use:</p>
<dd></dl>
<p> <i>cryptsetup-reencrypt</i> &lt;device&gt; </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;batch-mode, &#8211;block-size, &#8211;cipher | &#8211;keep-key, &#8211;debug, &#8211;device-size, &#8211;hash, &#8211;header, &#8211;iter-time | &#8211;pbkdf-force-iterations, &#8211;key-file, &#8211;key-size, &#8211;key-slot, &#8211;keyfile-offset, &#8211;keyfile-size, &#8211;master-key-file, &#8211;tries, &#8211;pbkdf, &#8211;pbkdf-memory, &#8211;pbkdf-parallel, &#8211;progress-frequency, &#8211;use-directio, &#8211;use-random | &#8211;use-urandom, &#8211;use-fsync, &#8211;uuid, &#8211;verbose, &#8211;write-log] </p>
<p> To encrypt data on (not yet encrypted) device, use <i>&#8211;new</i> in combination with <i>&#8211;reduce-device-size</i> or with <i>&#8211;header</i> option for detached header. </p>
<p> To remove encryption from device, use <i>&#8211;decrypt</i>. </p>
<p> For detailed description of encryption and key file options see <i><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8)</i> man page.</p>
<dl>
<dt><code>&#8211;batch-mode, -q</code></p>
<dd>Suppresses all warnings and reencryption progress output.</p>
<dt><code>&#8211;block-size, -B </code><i>value</i></p>
<dd>Use re-encryption block size of &lt;value&gt; in MiB. </p>
<p> Values can be between 1 and 64 MiB.</p>
<dt><code>&#8211;cipher, -c </code><i>&lt;cipher-spec&gt;</i></p>
<dd>Set the cipher specification string.</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode with full diagnostic logs. Debug output lines are always prefixed by &#8216;#&#8217;.</p>
<dt><code>&#8211;decrypt</code></p>
<dd>Remove encryption (decrypt already encrypted device and remove LUKS header). </p>
<p> <code>WARNING:</code> This is destructive operation and cannot be reverted.</p>
<dt><code>&#8211;device-size </code><i>size[units]</i></p>
<dd>Instead of real device size, use specified value. </p>
<p> It means that only specified area (from the start of the device to the specified size) will be reencrypted. </p>
<p> If no unit suffix is specified, the size is in bytes. </p>
<p> Unit suffix can be S for 512 byte sectors, K/M/G/T (or KiB,MiB,GiB,TiB) for units with 1024 base or KB/MB/GB/TB for 1000 base (SI scale). </p>
<p> <code>WARNING:</code> This is destructive operation.</p>
<dt><code>&#8211;hash, -h </code><i>&lt;hash-spec&gt;</i></p>
<dd>Specifies the hash used in the LUKS1 key setup scheme and volume key digest. </p>
<p> <code>NOTE:</code> if this parameter is not specified, default hash algorithm is always used for new LUKS1 device header. </p>
<p> <code>NOTE:</code> with LUKS2 format this option is only relevant when new keyslot pbkdf algorithm is set to PBKDF2 (see <i>&#8211;pbkdf</i>).</p>
<dt><code>&#8211;header</code> <i>&lt;LUKS header file&gt;</i></p>
<dd>Use a detached (separated) metadata device or file where the LUKS header is stored. This option allows one to store ciphertext and LUKS header on different devices. </p>
<p> <code>WARNING:</code> There is no check whether the ciphertext device specified actually belongs to the header given. If used with <i>&#8211;new</i> option, the header file will created (or overwritten). Use with care.</p>
<dt><code>&#8211;iter-time, -i </code><i>&lt;milliseconds&gt;</i></p>
<dd>The number of milliseconds to spend with PBKDF2 passphrase processing for the new LUKS header.</p>
<dt><code>&#8211;keep-key</code></p>
<dd>Do not change encryption key, just reencrypt the LUKS header and keyslots. </p>
<p> This option can be combined only with <i>&#8211;hash</i>, <i>&#8211;iter-time</i>, <i>&#8211;pbkdf-force-iterations</i>, <i>&#8211;pbkdf</i> (LUKS2 only), <i>&#8211;pbkdf-memory</i> (Argon2i/id and LUKS2 only) and <i>&#8211;pbkdf-parallel</i> (Argon2i/id and LUKS2 only) options.</p>
<dt><code>&#8211;key-file, -d </code><i>name</i></p>
<dd>Read the passphrase from file. </p>
<p> <code>WARNING:</code> &#8211;key-file option can be used only if there is only one active keyslot, or alternatively, also if &#8211;key-slot option is specified (then all other keyslots will be disabled in new LUKS device). </p>
<p> If this option is not used, cryptsetup-reencrypt will ask for all active keyslot passphrases.</p>
<dt><code>&#8211;key-size, -s </code><i>&lt;bits&gt;</i></p>
<dd>Set key size in bits. The argument has to be a multiple of 8. </p>
<p> The possible key-sizes are limited by the cipher and mode used. </p>
<p> If you are increasing key size, there must be enough space in the LUKS header for enlarged keyslots (data offset must be large enough) or reencryption cannot be performed. </p>
<p> If there is not enough space for keyslots with new key size, you can destructively shrink device with &#8211;reduce-device-size option.</p>
<dt><code>&#8211;key-slot, -S &lt;0-MAX&gt;</code></p>
<dd>Specify which key slot is used. For LUKS1, max keyslot number is 7. For LUKS2, it&#8217;s 31. </p>
<p> <code>WARNING:</code> All other keyslots will be disabled if this option is used.</p>
<dt><code>&#8211;keyfile-offset </code><i>value</i></p>
<dd>Skip <i>value</i> bytes at the beginning of the key file.</p>
<dt><code>&#8211;keyfile-size, -l</code></p>
<dd>Read a maximum of <i>value</i> bytes from the key file. Default is to read the whole file up to the compiled-in maximum.</p>
<dt><code>&#8211;master-key-file</code></p>
<dd>Use new volume (master) key stored in a file.</p>
<dt><code>&#8211;new, -N</code></p>
<dd>Create new header (encrypt not yet encrypted device). </p>
<p> This option must be used together with &#8211;reduce-device-size. </p>
<p> <code>WARNING:</code> This is destructive operation and cannot be reverted.</p>
<dt><code>&#8211;pbkdf</code></p>
<dd>Set Password-Based Key Derivation Function (PBKDF) algorithm for LUKS keyslot. The PBKDF can be: <i>pbkdf2</i>, <i>argon2i</i> for Argon2i or <i>argon2id</i> for Argon2id. </p>
<p> For LUKS1, only <i>pbkdf2</i> is accepted (no need to use this option).</p>
<dt><code>&#8211;pbkdf-force-iterations &lt;num&gt;</code></p>
<dd>Avoid PBKDF benchmark and set time cost (iterations) directly.</p>
<dt><code>&#8211;pbkdf-memory &lt;number&gt;</code></p>
<dd>Set the memory cost for PBKDF (for Argon2i/id the number represents kilobytes). Note that it is maximal value, PBKDF benchmark or available physical memory can decrease it. This option is not available for PBKDF2.</p>
<dt><code>&#8211;pbkdf-parallel &lt;number&gt;</code></p>
<dd>Set the parallel cost for PBKDF (number of threads, up to 4). Note that it is maximal value, it is decreased automatically if CPU online count is lower. This option is not available for PBKDF2.</p>
<dt><code>&#8211;progress-frequency &lt;seconds&gt;</code></p>
<dd>Print separate line every &lt;seconds&gt; with reencryption progress.</p>
<dt><code>&#8211;reduce-device-size </code><i>size[units]</i></p>
<dd>Enlarge data offset to specified value by shrinking device size. </p>
<p> This means that last sectors on the original device will be lost, ciphertext data will be effectively shifted by specified number of sectors. </p>
<p> It can be useful if you e.g. added some space to underlying partition (so last sectors contains no data). </p>
<p> For units suffix see &#8211;device-size parameter description. </p>
<p> You cannot shrink device more than by 64 MiB (131072 sectors). </p>
<p> <code>WARNING:</code> This is destructive operation and cannot be reverted. Use with extreme care &#8211; shrunk filesystems are usually unrecoverable.</p>
<dt><code>&#8211;tries, -T</code></p>
<dd>Number of retries for invalid passphrase entry.</p>
<dt><code>&#8211;type &lt;type&gt;</code></p>
<dd>Use only while encrypting not yet encrypted device (see &#8211;new). </p>
<p> Specify LUKS version when performing in-place encryption. If the parameter is omitted default value (LUKS1) is used. Type may be one of: <code>luks</code> (default), <code>luks1</code> or <code>luks2</code>.</p>
<dt><code>&#8211;use-directio</code></p>
<dd>Use direct-io (O_DIRECT) for all read/write data operations related to block device undergoing reencryption. </p>
<p> Useful if direct-io operations perform better than normal buffered operations (e.g. in virtual environments).</p>
<dt><code>&#8211;use-fsync</code></p>
<dd>Use fsync call after every written block. This applies for reencryption log files as well.</p>
<dt><code>&#8211;use-random</code></p>
<dd>
<dt><code>&#8211;use-urandom</code></p>
<dd>Define which kernel random number generator will be used to create the volume key.</p>
<dt><code>&#8211;uuid </code><i>&lt;uuid&gt;</i></p>
<dd>Use only while resuming an interrupted decryption process (see &#8211;decrypt). </p>
<p> To find out what <i>&lt;uuid&gt;</i> to pass look for temporary files LUKS-&lt;uuid&gt;.[|log|org|new] of the interrupted decryption process.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd>Print more information on command execution.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the program version.</p>
<dt><code>&#8211;write-log</code></p>
<dd>Update log file after every block write. This can slow down reencryption but will minimize data loss in the case of system crash. </p>
</dl>
<h2>Return Codes</h2>
<p>Cryptsetup-reencrypt returns 0 on success and a non-zero value on error. </p>
<p> Error codes are: 1 wrong parameters, 2 no permission, 3 out of memory, 4 wrong device specified, 5 device already exists or device is busy.</p>
<h2>Examples</h2>
<dl>
<dt>Reencrypt /dev/sdb1 (change volume key)</p>
<dd>cryptsetup-reencrypt /dev/sdb1</p>
<dt>Reencrypt and also change cipher and cipher mode</p>
<dd>cryptsetup-reencrypt /dev/sdb1 -c aes-xts-plain64</p>
<dt>Add LUKS encryption to not yet encrypted device</p>
<dd>First, be sure you have space added to disk. Or alternatively shrink filesystem in advance.<br />
 Here we need 4096 512-bytes sectors (enough for 2&#215;128 bit key). fdisk -u /dev/sdb # move sdb1 partition end + 4096 sectors (or use resize2fs or tool for your filesystem and shrink it) cryptsetup-reencrypt /dev/sdb1 &#8211;new &#8211;reduce-device-size 4096S</p>
<dt>Remove LUKS encryption completely</p>
<dd>cryptsetup-reencrypt /dev/sdb1 &#8211;decrypt </p>
<h2>Reporting Bugs</h2>
<p>Report bugs, including ones in the documentation, on the cryptsetup mailing list at &lt;dm-crypt [at] saout.de&gt; or in the &#8216;Issues&#8217; section on LUKS website. Please attach the output of the failed command with the &#8211;debug option added.</p>
<h2>Authors</h2>
<p>Cryptsetup-reencrypt was written by Milan Broz &lt;gmazyland [at] gmail.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012-2019 Milan Broz<br />
 Copyright &#169; 2012-2019 Red Hat, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>The project website at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup">https://gitlab.com/cryptsetup/cryptsetup</a></code> </p>
