---
title: "integritysetup(8)"
name: "integritysetup"
section: "8"
letter: "i"
url: "/docs/linux/man/8-integritysetup/"
description: "integritysetup – manage dm-integrity (block level integrity) volumes"
---

<p>integritysetup &#8211; manage dm-integrity (block level integrity) volumes</p>
<h2>Synopsis</h2>
<p><code>integritysetup &lt;options&gt; &lt;action&gt; &lt;action args&gt;</code></p>
<h2>Description</h2>
<p>Integritysetup is used to configure dm-integrity managed device-mapper mappings. Device-mapper integrity target provides read-write transparent integrity checking of block devices. The dm-integrity target emulates additional data integrity field per-sector. You can use this additional field directly with integritysetup utility, or indirectly (for authenticated encryption) through cryptsetup. Integritysetup supports these operations: <i>format</i> &lt;device&gt;</p>
<dl>
<dd>Formats &lt;device&gt; (calculates space and dm-integrity superblock and wipes the device). <code>&lt;options&gt;</code> can be [&#8211;data-device, &#8211;batch-mode, &#8211;no-wipe, &#8211;journal-size, &#8211;interleave-sectors, &#8211;tag-size, &#8211;integrity, &#8211;integrity-key-size, &#8211;integrity-key-file, &#8211;sector-size, &#8211;progress-frequency]  <i>open</i> &lt;device&gt; &lt;name&gt;<br />
 <i>create</i> &lt;name&gt; &lt;device&gt; (<code>OBSOLETE syntax</code>)</p>
<dl>
<dd>Open a mapping with &lt;name&gt; backed by device &lt;device&gt;. <code>&lt;options&gt;</code> can be [&#8211;data-device, &#8211;batch-mode, &#8211;journal-watermark, &#8211;journal-commit-time, &#8211;buffer-sectors, &#8211;integrity, &#8211;integrity-key-size, &#8211;integrity-key-file, &#8211;integrity-no-journal, &#8211;integrity-recalculate, &#8211;integrity-recovery-mode]  <i>close</i> &lt;name&gt;</p>
<dl>
<dd>Removes existing mapping &lt;name&gt;. For backward compatibility, there is <code>remove</code> command alias for the <code>close</code> command.</dl>
<p> <i>status</i> &lt;name&gt;</p>
<dl>
<dd>Reports status for the active integrity mapping &lt;name&gt;.</dl>
<p> <i>dump</i> &lt;device&gt;</p>
<dl>
<dd>Reports parameters from on-disk stored superblock. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;verbose, -v</code></p>
<dd>Print more information on command execution.</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode with full diagnostic logs. Debug output lines are always prefixed by &#8216;#&#8217;.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the program version.</p>
<dt><code>&#8211;batch-mode</code></p>
<dd>Do not ask for confirmation.</p>
<dt><code>&#8211;progress-frequency &lt;seconds&gt;</code></p>
<dd>Print separate line every &lt;seconds&gt; with wipe progress.</p>
<dt><code>&#8211;no-wipe</code></p>
<dd>Do not wipe the device after format. A device that is not initially wiped will contain invalid checksums.</p>
<dt><code>&#8211;journal-size, -j BYTES</code></p>
<dd>Size of the journal.</p>
<dt><code>&#8211;interleave-sectors SECTORS</code></p>
<dd>The number of interleaved sectors.</p>
<dt><code>&#8211;integrity-recalculate</code></p>
<dd>Automatically recalculate integrity tags in kernel on activation. The device can be used during automatic integrity recalculation but becomes fully integrity protected only after the background operation is finished. This option is available since the Linux kernel version 4.19.</p>
<dt><code>&#8211;journal-watermark PERCENT</code></p>
<dd>Journal watermark in percents. When the size of the journal exceeds this watermark, the journal flush will be started.</p>
<dt><code>&#8211;journal-commit-time MS</code></p>
<dd>Commit time in milliseconds. When this time passes (and no explicit flush operation was issued), the journal is written.</p>
<dt><code>&#8211;tag-size, -t BYTES</code></p>
<dd>Size of the integrity tag per-sector (here the integrity function will store authentication tag). </p>
<p> <code>NOTE:</code> The size can be smaller that output size of the hash function, in that case only part of the hash will be stored.</p>
<dt><code>&#8211;data-device</code></p>
<dd>Specify a separate data device that contains existing data. The &lt;device&gt; then will contain calculated integrity tags and journal for this data device.</p>
<dt><code>&#8211;sector-size, -s BYTES</code></p>
<dd>Sector size (power of two: 512, 1024, 2048, 4096).</p>
<dt><code>&#8211;buffer-sectors SECTORS</code></p>
<dd>The number of sectors in one buffer. </p>
<p> The tag area is accessed using buffers, the large buffer size means that the I/O size will be larger, but there could be less I/Os issued.</p>
<dt><code>&#8211;integrity, -I ALGORITHM</code></p>
<dd>Use internal integrity calculation (standalone mode). The integrity algorithm can be CRC (crc32c/crc32) or hash function (sha1, sha256). </p>
<p> For HMAC (hmac-sha256) you have also to specify an integrity key and its size.</p>
<dt><code>&#8211;integrity-key-size BYTES</code></p>
<dd>The size of the data integrity key.</p>
<dt><code>&#8211;integrity-key-file FILE</code></p>
<dd>The file with the integrity key.</p>
<dt><code>&#8211;integrity-no-journal, -D</code></p>
<dd>Disable journal for integrity device.</p>
<dt><code>&#8211;integrity-bitmap-mode. -B</code></p>
<dd>Use alternate bitmap mode (available since Linux kernel 5.2) where dm-integrity uses bitmap instead of a journal. If a bit in the bitmap is 1, the corresponding region&#8217;s data and integrity tags are not synchronized &#8211; if the machine crashes, the unsynchronized regions will be recalculated. The bitmap mode is faster than the journal mode, because we don&#8217;t have to write the data twice, but it is also less reliable, because if data corruption happens when the machine crashes, it may not be detected.</p>
<dt><code>&#8211;bitmap-sectors-per-bit SECTORS</code></p>
<dd>Number of 512-byte sectors per bitmap bit, the value must be power of two.</p>
<dt><code>&#8211;bitmap-flush-time MS</code></p>
<dd>Bitmap flush time in milliseconds.</p>
<dd><code>WARNING:</code> In case of a crash, it is possible that the data and integrity tag doesn&#8217;t match if the journal is disabled.</p>
<dt><code>&#8211;integrity-recovery-mode. -R</code></p>
<dd>Recovery mode (no journal, no tag checking).</p>
<dd><code>NOTE:</code> The following options are intended for testing purposes only. Using journal encryption does not make sense without encryption the data, these options are internally used in authenticated disk encryption with <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8)</code>.</p>
<dt><code>&#8211;journal-integrity ALGORITHM</code></p>
<dd>Integrity algorithm for journal area. See &#8211;integrity option for detailed specification.</p>
<dt><code>&#8211;journal-integrity-key-size BYTES</code></p>
<dd>The size of the journal integrity key.</p>
<dt><code>&#8211;journal-integrity-key-file FILE</code></p>
<dd>The file with the integrity key.</p>
<dt><code>&#8211;journal-crypt ALGORITHM</code></p>
<dd>Encryption algorithm for journal data area. You can use a block cipher here such as cbc(aes) or a stream cipher, for example, chacha20 or ctr(aes).</p>
<dt><code>&#8211;journal-crypt-key-size BYTES</code></p>
<dd>The size of the journal encryption key.</p>
<dt><code>&#8211;journal-crypt-key-file FILE</code></p>
<dd>The file with the journal encryption key.</p>
<dt>The dm-integrity target is available since Linux kernel version 4.12.</p>
<dd>
<dt><code>NOTE:</code></p>
<dd>Format and activation of an integrity device always require superuser privilege because the superblock is calculated and handled in dm-integrity kernel target. </p>
</dl>
<h2>Return Codes</h2>
<p>Integritysetup returns 0 on success and a non-zero value on error. </p>
<p> Error codes are:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 wrong parameters<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 no permission<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 out of memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 wrong device specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 device already exists, or device is busy.</p>
<h2>Examples</h2>
<p>Format the device with default standalone mode (CRC32C): <code>integritysetup format &lt;device&gt;</code> Open the device with default parameters: <code>integritysetup open &lt;device&gt; test</code> Format the device in standalone mode for use with HMAC(SHA256): <code>integritysetup format &lt;device&gt; &#8211;tag-size 32 &#8211;integrity hmac-sha256 &#8211;integrity-key-file &lt;keyfile&gt; &#8211;integrity-key-size &lt;key_bytes&gt;</code> Open (activate) the device with HMAC(SHA256) and HMAC key in file: <code>integritysetup open &lt;device&gt; test &#8211;integrity hmac-sha256 &#8211;integrity-key-file &lt;keyfile&gt; &#8211;integrity-key-size &lt;key_bytes&gt;</code> Dump dm-integrity superblock information: <code>integritysetup dump &lt;device&gt;</code> </p>
<h2>Reporting Bugs</h2>
<p>Report bugs, including ones in the documentation, on the cryptsetup mailing list at &lt;dm-crypt [at] saout.de&gt; or in the &#8216;Issues&#8217; section on LUKS website. Please attach the output of the failed command with the &#8211;debug option added.</p>
<h2>Authors</h2>
<p>The integritysetup tool is written by Milan Broz &lt;gmazyland [at] gmail.com&gt; and is part of the cryptsetup project.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2016-2019 Red Hat, Inc.<br />
 Copyright &#169; 2016-2019 Milan Broz </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>The project website at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup">https://gitlab.com/cryptsetup/cryptsetup</a></code> The integrity on-disk format specification available at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup/wikis/DMIntegrity">https://gitlab.com/cryptsetup/cryptsetup/wikis/DMIntegrity</a></code> </p>
