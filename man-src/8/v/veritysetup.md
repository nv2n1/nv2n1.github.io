---
title: "veritysetup(8)"
name: "veritysetup"
section: "8"
letter: "v"
url: "/docs/linux/man/8-veritysetup/"
description: "veritysetup – manage dm-verity (block level verification) volumes"
---

<p>veritysetup &#8211; manage dm-verity (block level verification) volumes</p>
<h2>Synopsis</h2>
<p><code>veritysetup &lt;options&gt; &lt;action&gt; &lt;action args&gt;</code></p>
<h2>Description</h2>
<p>Veritysetup is used to configure dm-verity managed device-mapper mappings. </p>
<p> Device-mapper verity target provides read-only transparent integrity checking of block devices using kernel crypto API. </p>
<p> The dm-verity devices are always read-only. </p>
<p> Veritysetup supports these operations: </p>
<p> <i>format</i> &lt;data_device&gt; &lt;hash_device&gt;</p>
<dl>
<dd>Calculates and permanently stores hash verification data for data_device. Hash area can be located on the same device after data if specified by &#8211;hash-offset option. </p>
<p> Note you need to provide root hash string for device verification or activation. Root hash must be trusted. </p>
<p> The data or hash device argument can be block device or file image. If hash device path doesn&#8217;t exist, it will be created as file. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;hash, &#8211;no-superblock, &#8211;format, &#8211;data-block-size, &#8211;hash-block-size, &#8211;data-blocks, &#8211;hash-offset, &#8211;salt, &#8211;uuid]</dl>
<p> <i>open</i> &lt;data_device&gt; &lt;name&gt; &lt;hash_device&gt; &lt;root_hash&gt; <i>create</i> &lt;name&gt; &lt;data_device&gt; &lt;hash_device&gt; &lt;root_hash&gt;</p>
<dl>
<dd>Creates a mapping with &lt;name&gt; backed by device &lt;data_device&gt; and using &lt;hash_device&gt; for in-kernel verification. </p>
<p> The &lt;root_hash&gt; is a hexadecimal string. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;hash-offset, &#8211;no-superblock, &#8211;ignore-corruption or &#8211;restart-on-corruption, &#8211;ignore-zero-blocks] </p>
<p> If option &#8211;no-superblock is used, you have to use as the same options as in initial format operation.</dl>
<p> <i>verify</i> &lt;data_device&gt; &lt;hash_device&gt; &lt;root_hash&gt;</p>
<dl>
<dd>Verifies data on data_device with use of hash blocks stored on hash_device. </p>
<p> This command performs userspace verification, no kernel device is created. </p>
<p> The &lt;root_hash&gt; is a hexadecimal string. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;hash-offset, &#8211;no-superblock] </p>
<p> If option &#8211;no-superblock is used, you have to use as the same options as in initial format operation.</dl>
<p> <i>close</i> &lt;name&gt;</p>
<dl>
<dd>Removes existing mapping &lt;name&gt;. </p>
<p> For backward compatibility there is <code>remove</code> command alias for <code>close</code> command.</dl>
<p> <i>status</i> &lt;name&gt;</p>
<dl>
<dd>Reports status for the active verity mapping &lt;name&gt;.</dl>
<p> <i>dump</i> &lt;hash_device&gt;</p>
<dl>
<dd>Reports parameters of verity device from on-disk stored superblock. </p>
<p> <code>&lt;options&gt;</code> can be [&#8211;no-superblock]</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;verbose, -v</code></p>
<dd>Print more information on command execution.</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode with full diagnostic logs. Debug output lines are always prefixed by &#8216;#&#8217;.</p>
<dt><code>&#8211;no-superblock</code></p>
<dd>Create or use dm-verity without permanent on-disk superblock.</p>
<dt><code>&#8211;format=number</code></p>
<dd>Specifies the hash version type. Format type 0 is original Chrome OS version. Format type 1 is current version.</p>
<dt><code>&#8211;data-block-size=bytes</code></p>
<dd>Used block size for the data device. (Note kernel supports only page-size as maximum here.)</p>
<dt><code>&#8211;hash-block-size=bytes</code></p>
<dd>Used block size for the hash device. (Note kernel supports only page-size as maximum here.)</p>
<dt><code>&#8211;data-blocks=blocks</code></p>
<dd>Size of data device used in verification. If not specified, the whole device is used.</p>
<dt><code>&#8211;hash-offset=bytes</code></p>
<dd>Offset of hash area/superblock on hash_device. Value must be aligned to disk sector offset.</p>
<dt><code>&#8211;salt=hex string</code></p>
<dd>Salt used for format or verification. Format is a hexadecimal string.</p>
<dt><code>&#8211;uuid=UUID</code></p>
<dd>Use the provided UUID for format command instead of generating new one. </p>
<p> The UUID must be provided in standard UUID format, e.g. 12345678-1234-1234-1234-123456789abc.</p>
<dt><code>&#8211;ignore-corruption, &#8211;restart-on-corruption</code></p>
<dd>Defines what to do if data integrity problem is detected (data corruption). </p>
<p> Without these options kernel fails the IO operation with I/O error. With &#8211;ignore-corruption option the corruption is only logged. With &#8211;restart-on-corruption the kernel is restarted immediately. (You have to provide way how to avoid restart loops.) </p>
<p> <code>WARNING:</code> Use these options only for very specific cases. These options are available since Linux kernel version 4.1.</p>
<dt><code>&#8211;ignore-zero-blocks</code></p>
<dd>Instruct kernel to not verify blocks that are expected to contain zeroes and always directly return zeroes instead. </p>
<p> <code>WARNING:</code> Use this option only in very specific cases. This option is available since Linux kernel version 4.5.</p>
<dt><code>&#8211;hash=hash</code></p>
<dd>Hash algorithm for dm-verity. For default see &#8211;help option.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the program version.</p>
<dt><code>&#8211;fec-device=fec_device</code></p>
<dd>Use forward error correction (FEC) to recover from corruption if hash verification fails. Use encoding data from the specified device. </p>
<p> The fec device argument can be block device or file image. For format, if fec device path doesn&#8217;t exist, it will be created as file. </p>
<p> Note: block sizes for data and hash devices must match. Also, if the verity data_device is encrypted the fec_device should be too.</p>
<dt><code>&#8211;fec-offset=bytes</code></p>
<dd>This is the offset, in bytes, from the start of the FEC device to the beginning of the encoding data.</p>
<dt><code>&#8211;fec-roots=num</code></p>
<dd>Number of generator roots. This equals to the number of parity bytes in the encoding data. In RS(M, N) encoding, the number of roots is M-N. M is 255 and M-N is between 2 and 24 (including).</p>
<dt></dl>
<h2>Return Codes</h2>
<dd>Veritysetup returns 0 on success and a non-zero value on error. </p>
<p> Error codes are:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 wrong parameters<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 no permission<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 out of memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 wrong device specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 device already exists or device is busy.</p>
<h2>Examples</h2>
<p><code>veritysetup &#8211;data-blocks=256 format &lt;data_device&gt; &lt;hash_device&gt;</code> Calculates and stores verification data on hash_device for the first 256 blocks (of block-size). If hash_device does not exist, it is created (as file image). <code>veritysetup format &lt;data_device&gt; &lt;hash_device&gt;</code> Calculates and stores verification data on hash_device for the whole data_device. <code>veritysetup &#8211;data-blocks=256 &#8211;hash-offset=1052672 format &lt;device&gt; &lt;device&gt;</code> Verification data (hashes) is stored on the same device as data (starting at hash-offset). Hash-offset must be greater than number of blocks in data-area. <code>veritysetup &#8211;data-blocks=256 &#8211;hash-offset=1052672 create test-device &lt;device&gt; &lt;device&gt; &lt;root_hash&gt;</code> Activates the verity device named test-device. Options &#8211;data-blocks and &#8211;hash-offset are the same as in the format command. The &lt;root_hash&gt; was calculated in format command. <code>veritysetup &#8211;data-blocks=256 &#8211;hash-offset=1052672 verify &lt;data_device&gt; &lt;hash_device&gt; &lt;root_hash&gt;</code> Verifies device without activation (in userspace). <code>veritysetup &#8211;fec-device=&lt;fec_device&gt; &#8211;fec-roots=10 format &lt;data_device&gt; &lt;hash_device&gt;</code> Calculates and stores verification and encoding data for data_device. </p>
<h2>Reporting Bugs</h2>
<p>Report bugs, including ones in the documentation, on the cryptsetup mailing list at &lt;dm-crypt [at] saout.de&gt; or in the &#8216;Issues&#8217; section on LUKS website. Please attach the output of the failed command with the &#8211;debug option added.</p>
<h2>Authors</h2>
<p>The first implementation of veritysetup was written by Chrome OS authors. </p>
<p> This version is based on verification code written by Mikulas Patocka &lt;mpatocka [at] redhat.com&gt; and rewritten for libcryptsetup by Milan Broz &lt;gmazyland [at] gmail.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012-2018 Red Hat, Inc.<br />
 Copyright &#169; 2012-2018 Milan Broz </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p>The project website at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup">https://gitlab.com/cryptsetup/cryptsetup</a></code> The verity on-disk format specification available at <code><a rel="nofollow" href="https://gitlab.com/cryptsetup/cryptsetup/wikis/DMVerity">https://gitlab.com/cryptsetup/cryptsetup/wikis/DMVerity</a></code> </p>
