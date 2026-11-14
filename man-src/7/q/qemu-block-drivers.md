---
title: "qemu-block-drivers(7)"
name: "qemu-block-drivers"
section: "7"
letter: "q"
url: "/docs/linux/man/7-qemu-block-drivers/"
description: "qemu-block-drivers – QEMU block drivers reference"
---

<p>qemu-block-drivers &#8211; QEMU block drivers reference</p>
<h2>Synopsis</h2>
<p><font SIZE="-1">QEMU</font> block driver reference manual</p>
<h2>Description</h2>
<p><i>Disk image file formats</i> <font SIZE="-1">QEMU</font> supports many image file formats that can be used with VMs as well as with any of the tools (like <tt>&quot;qemu-img&quot;</tt>). This includes the preferred formats raw and qcow2 as well as formats that are supported for compatibility with older <font SIZE="-1">QEMU</font> versions or other hypervisors. Depending on the image format, different options can be passed to <tt>&quot;qemu-img create&quot;</tt> and <tt>&quot;qemu-img convert&quot;</tt> using the <tt>&quot;-o&quot;</tt> option. This section describes each format and the options that are supported for it.</p>
<dl>
<dt><code>raw</code></p>
<dd>Raw disk image format. This format has the advantage of being simple and easily exportable to all other emulators. If your file system supports <i>holes</i> (for example in ext2 or ext3 on Linux or <font SIZE="-1">NTFS</font> on Windows), then only the written sectors will reserve space. Use <tt>&quot;qemu-img info&quot;</tt> to know the real size used by the image or <tt>&quot;ls -ls&quot;</tt> on Unix/Linux. Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;preallocation&quot;</p>
<dd>Preallocation mode (allowed values: <tt>&quot;off&quot;</tt>, <tt>&quot;falloc&quot;</tt>, <tt>&quot;full&quot;</tt>). <tt>&quot;falloc&quot;</tt> mode preallocates space for image by calling <code>posix_fallocate()</code>. <tt>&quot;full&quot;</tt> mode preallocates space for image by writing data to underlying storage. This data may or may not be zero, depending on the storage location.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>qcow2</code></p>
<dd><font SIZE="-1">QEMU</font> image format, the most versatile format. Use it to have smaller images (useful if your filesystem does not supports holes, for example on Windows), zlib based compression and support of multiple <font SIZE="-1">VM</font> snapshots. Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;compat&quot;</p>
<dd>Determines the qcow2 version to use. <tt>&quot;compat=0.10&quot;</tt> uses the traditional image format that can be read by any <font SIZE="-1">QEMU</font> since 0.10. <tt>&quot;compat=1.1&quot;</tt> enables image format extensions that only <font SIZE="-1">QEMU 1.1</font> and newer understand (this is the default). Amongst others, this includes zero clusters, which allow efficient copy-on-read for sparse images.</p>
<dt>&quot;backing_file&quot;</p>
<dd>File name of a base image (see <code>create</code> subcommand)</p>
<dt>&quot;backing_fmt&quot;</p>
<dd>Image format of the base image</p>
<dt>&quot;encryption&quot;</p>
<dd>This option is deprecated and equivalent to <tt>&quot;encrypt.format=aes&quot;</tt></p>
<dt>&quot;encrypt.format&quot;</p>
<dd>If this is set to <tt>&quot;luks&quot;</tt>, it requests that the qcow2 payload (not qcow2 header) be encrypted using the <font SIZE="-1">LUKS</font> format. The passphrase to use to unlock the <font SIZE="-1">LUKS</font> key slot is given by the <tt>&quot;encrypt.key-secret&quot;</tt> parameter. <font SIZE="-1">LUKS</font> encryption parameters can be tuned with the other <tt>&quot;encrypt.*&quot;</tt> parameters. If this is set to <tt>&quot;aes&quot;</tt>, the image is encrypted with 128-bit AES-CBC. The encryption key is given by the <tt>&quot;encrypt.key-secret&quot;</tt> parameter. This encryption format is considered to be flawed by modern cryptography standards, suffering from a number of design problems:</p>
<dl>
<dd>
<dl>
<dt>-&lt;The AES-CBC cipher is used with predictable initialization vectors based&gt;</p>
<dd>on the sector number. This makes it vulnerable to chosen plaintext attacks which can reveal the existence of encrypted data.</p>
<dt>-&lt;The user passphrase is directly used as the encryption key. A poorly&gt;</p>
<dd>chosen or short passphrase will compromise the security of the encryption.</p>
<dt>-&lt;In the event of the passphrase being compromised there is no way to&gt;</p>
<dd>change the passphrase to protect data in any qcow images. The files must be cloned, using a different encryption passphrase in the new file. The original file must then be securely erased using a program like shred, though even this is ineffective with many modern storage technologies.</dl>
</dl>
<dl>
<dd>The use of this is no longer supported in system emulators. Support only remains in the command line utilities, for the purposes of data liberation and interoperability with old versions of <font SIZE="-1">QEMU.</font> The <tt>&quot;luks&quot;</tt> format should be used instead.</dl>
<dt>&quot;encrypt.key-secret&quot;</p>
<dd>Provides the <font SIZE="-1">ID</font> of a <tt>&quot;secret&quot;</tt> object that contains the passphrase (<tt>&quot;encrypt.format=luks&quot;</tt>) or encryption key (<tt>&quot;encrypt.format=aes&quot;</tt>).</p>
<dt>&quot;encrypt.cipher-alg&quot;</p>
<dd>Name of the cipher algorithm and key length. Currently defaults to <tt>&quot;aes-256&quot;</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.cipher-mode&quot;</p>
<dd>Name of the encryption mode to use. Currently defaults to <tt>&quot;xts&quot;</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.ivgen-alg&quot;</p>
<dd>Name of the initialization vector generator algorithm. Currently defaults to <tt>&quot;plain64&quot;</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.ivgen-hash-alg&quot;</p>
<dd>Name of the hash algorithm to use with the initialization vector generator (if required). Defaults to <tt>&quot;sha256&quot;</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.hash-alg&quot;</p>
<dd>Name of the hash algorithm to use for <font SIZE="-1">PBKDF</font> algorithm Defaults to <tt>&quot;sha256&quot;</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.iter-time&quot;</p>
<dd>Amount of time, in milliseconds, to use for <font SIZE="-1">PBKDF</font> algorithm per key slot. Defaults to <tt>2000</tt>. Only used when <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;cluster_size&quot;</p>
<dd>Changes the qcow2 cluster size (must be between 512 and 2M). Smaller cluster sizes can improve the image file size whereas larger cluster sizes generally provide better performance.</p>
<dt>&quot;preallocation&quot;</p>
<dd>Preallocation mode (allowed values: <tt>&quot;off&quot;</tt>, <tt>&quot;metadata&quot;</tt>, <tt>&quot;falloc&quot;</tt>, <tt>&quot;full&quot;</tt>). An image with preallocated metadata is initially larger but can improve performance when the image needs to grow. <tt>&quot;falloc&quot;</tt> and <tt>&quot;full&quot;</tt> preallocations are like the same options of <tt>&quot;raw&quot;</tt> format, but sets up metadata also.</p>
<dt>&quot;lazy_refcounts&quot;</p>
<dd>If this option is set to <tt>&quot;on&quot;</tt>, reference count updates are postponed with the goal of avoiding metadata I/O and improving performance. This is particularly interesting with <code>cache=writethrough</code> which doesn&#8217;t batch metadata updates. The tradeoff is that after a host crash, the reference count tables must be rebuilt, i.e. on the next open an (automatic) <tt>&quot;qemu-img check -r all&quot;</tt> is required, which may take some time. This option can only be enabled if <tt>&quot;compat=1.1&quot;</tt> is specified.</p>
<dt>&quot;nocow&quot;</p>
<dd>If this option is set to <tt>&quot;on&quot;</tt>, it will turn off <font SIZE="-1">COW</font> of the file. It&#8217;s only valid on btrfs, no effect on other file systems. Btrfs has low performance when hosting a <font SIZE="-1">VM</font> image file, even more when the guest on the <font SIZE="-1">VM</font> also using btrfs as file system. Turning off <font SIZE="-1">COW</font> is a way to mitigate this bad performance. Generally there are two ways to turn off <font SIZE="-1">COW</font> on btrfs: a) Disable it by mounting with nodatacow, then all newly created files will be <font SIZE="-1">NOCOW.</font> b) For an empty file, add the <font SIZE="-1">NOCOW</font> file attribute. That&#8217;s what this option does. Note: this option is only valid to new or empty files. If there is an existing file which is <font SIZE="-1">COW</font> and has data blocks already, it couldn&#8217;t be changed to <font SIZE="-1">NOCOW</font> by setting <tt>&quot;nocow=on&quot;</tt>. One can issue <tt>&quot;lsattr filename&quot;</tt> to check if the <font SIZE="-1">NOCOW</font> flag is set or not (Capital &#8216;C&#8217; is <font SIZE="-1">NOCOW</font> flag).</dl>
</dl>
<dl>
<dd></dl>
<dt><code>qed</code></p>
<dd>Old <font SIZE="-1">QEMU</font> image format with support for backing files and compact image files (when your filesystem or transport medium does not support holes). When converting <font SIZE="-1">QED</font> images to qcow2, you might want to consider using the <tt>&quot;lazy_refcounts=on&quot;</tt> option to get a more QED-like behaviour. Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;backing_file&quot;</p>
<dd>File name of a base image (see <code>create</code> subcommand).</p>
<dt>&quot;backing_fmt&quot;</p>
<dd>Image file format of backing file (optional). Useful if the format cannot be autodetected because it has no header, like some vhd/vpc files.</p>
<dt>&quot;cluster_size&quot;</p>
<dd>Changes the cluster size (must be power-of-2 between 4K and 64K). Smaller cluster sizes can improve the image file size whereas larger cluster sizes generally provide better performance.</p>
<dt>&quot;table_size&quot;</p>
<dd>Changes the number of clusters per L1/L2 table (must be power-of-2 between 1 and 16). There is normally no need to change this value but this option can be used for performance benchmarking.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>qcow</code></p>
<dd>Old <font SIZE="-1">QEMU</font> image format with support for backing files, compact image files, encryption and compression. Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;backing_file&quot;</p>
<dd>File name of a base image (see <code>create</code> subcommand)</p>
<dt>&quot;encryption&quot;</p>
<dd>This option is deprecated and equivalent to <tt>&quot;encrypt.format=aes&quot;</tt></p>
<dt>&quot;encrypt.format&quot;</p>
<dd>If this is set to <tt>&quot;aes&quot;</tt>, the image is encrypted with 128-bit AES-CBC. The encryption key is given by the <tt>&quot;encrypt.key-secret&quot;</tt> parameter. This encryption format is considered to be flawed by modern cryptography standards, suffering from a number of design problems enumerated previously against the <tt>&quot;qcow2&quot;</tt> image format. The use of this is no longer supported in system emulators. Support only remains in the command line utilities, for the purposes of data liberation and interoperability with old versions of <font SIZE="-1">QEMU.</font> Users requiring native encryption should use the <tt>&quot;qcow2&quot;</tt> format instead with <tt>&quot;encrypt.format=luks&quot;</tt>.</p>
<dt>&quot;encrypt.key-secret&quot;</p>
<dd>Provides the <font SIZE="-1">ID</font> of a <tt>&quot;secret&quot;</tt> object that contains the encryption key (<tt>&quot;encrypt.format=aes&quot;</tt>).</dl>
</dl>
<dl>
<dd></dl>
<dt><code>luks</code></p>
<dd><font SIZE="-1">LUKS</font> v1 encryption format, compatible with Linux dm-crypt/cryptsetup Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;key-secret&quot;</p>
<dd>Provides the <font SIZE="-1">ID</font> of a <tt>&quot;secret&quot;</tt> object that contains the passphrase.</p>
<dt>&quot;cipher-alg&quot;</p>
<dd>Name of the cipher algorithm and key length. Currently defaults to <tt>&quot;aes-256&quot;</tt>.</p>
<dt>&quot;cipher-mode&quot;</p>
<dd>Name of the encryption mode to use. Currently defaults to <tt>&quot;xts&quot;</tt>.</p>
<dt>&quot;ivgen-alg&quot;</p>
<dd>Name of the initialization vector generator algorithm. Currently defaults to <tt>&quot;plain64&quot;</tt>.</p>
<dt>&quot;ivgen-hash-alg&quot;</p>
<dd>Name of the hash algorithm to use with the initialization vector generator (if required). Defaults to <tt>&quot;sha256&quot;</tt>.</p>
<dt>&quot;hash-alg&quot;</p>
<dd>Name of the hash algorithm to use for <font SIZE="-1">PBKDF</font> algorithm Defaults to <tt>&quot;sha256&quot;</tt>.</p>
<dt>&quot;iter-time&quot;</p>
<dd>Amount of time, in milliseconds, to use for <font SIZE="-1">PBKDF</font> algorithm per key slot. Defaults to <tt>2000</tt>.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>vdi</code></p>
<dd>VirtualBox 1.1 compatible image format. Supported options:</p>
<dl>
<dd>
<dl>
<dt>&quot;static&quot;</p>
<dd>If this option is set to <tt>&quot;on&quot;</tt>, the image is created with metadata preallocation.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>vmdk</code></p>
<dd>VMware 3 and 4 compatible image format. </p>
<pre><code>Supported options:


&quot;backing_file&quot;




File name of a base image (see create subcommand).
&quot;compat6&quot;




Create a VMDK version 6 image (instead of version 4)
&quot;hwversion&quot;




Specify vmdk virtual hardware version. Compat6 flag cannot be enabled
if hwversion is specified.
&quot;subformat&quot;




Specifies which VMDK subformat to use. Valid options are
&quot;monolithicSparse&quot; (default),
&quot;monolithicFlat&quot;,
&quot;twoGbMaxExtentSparse&quot;,
&quot;twoGbMaxExtentFlat&quot; and
&quot;streamOptimized&quot;.






vpc


VirtualPC compatible image format (VHD).
Supported options:


&quot;subformat&quot;




Specifies which VHD subformat to use. Valid options are
&quot;dynamic&quot; (default) and &quot;fixed&quot;.






VHDX


Hyper-V compatible image format (VHDX).
Supported options:


&quot;subformat&quot;




Specifies which VHDX subformat to use. Valid options are
&quot;dynamic&quot; (default) and &quot;fixed&quot;.
&quot;block_state_zero&quot;




Force use of payload blocks of type 'ZERO'.  Can be set to &quot;on&quot; (default)
or &quot;off&quot;.  When set to &quot;off&quot;, new blocks will be created as
&quot;PAYLOAD_BLOCK_NOT_PRESENT&quot;, which means parsers are free to return
arbitrary data for those blocks.  Do not set to &quot;off&quot; when using
&quot;qemu-img convert&quot; with &quot;subformat=dynamic&quot;.
&quot;block_size&quot;




Block size;
min 1 MB, max 256 MB.0 means auto - calculate based on image size.&quot;log_size&quot;

                                    Log size;
min 1 MB.</code></pre>
<p> Read-only formats More disk image file formats are supported in a read-only mode.</p>
<dl>
<dt><code>bochs</code></p>
<dd>Bochs images of <tt>&quot;growing&quot;</tt> type.</p>
<dt><code>cloop</code></p>
<dd>Linux Compressed Loop image, useful only to reuse directly compressed CD-ROM images present for example in the Knoppix CD-ROMs.</p>
<dt><code>dmg</code></p>
<dd>Apple disk image.</p>
<dt><code>parallels</code></p>
<dd>Parallels disk image format.</dl>
<p> <i>Using host drives</i> In addition to disk image files, <font SIZE="-1">QEMU</font> can directly access host devices. We describe here the usage for <font SIZE="-1">QEMU</font> version &gt;= 0.8.3. Linux On Linux, you can directly use the host device filename instead of a disk image filename provided you have enough privileges to access it. For example, use <i>/dev/cdrom</i> to access to the <font SIZE="-1">CDROM.</font></p>
<dl>
<dt>&quot;CD&quot;</p>
<dd>You can specify a <font SIZE="-1">CDROM</font> device even if no <font SIZE="-1">CDROM</font> is loaded. <font SIZE="-1">QEMU</font> has specific code to detect <font SIZE="-1">CDROM</font> insertion or removal. <font SIZE="-1">CDROM</font> ejection by the guest <font SIZE="-1">OS</font> is supported. Currently only data CDs are supported.</p>
<dt>&quot;Floppy&quot;</p>
<dd>You can specify a floppy device even if no floppy is loaded. Floppy removal is currently not detected accurately (if you change floppy without doing floppy access while the floppy is not loaded, the guest <font SIZE="-1">OS</font> will think that the same floppy is loaded). Use of the host&#8217;s floppy device is deprecated, and support for it will be removed in a future release.</p>
<dt>&quot;Hard disks&quot;</p>
<dd>Hard disks can be used. Normally you must specify the whole disk (<i>/dev/hdb</i> instead of <i>/dev/hdb1</i>) so that the guest <font SIZE="-1">OS</font> can see it as a partitioned disk. <font SIZE="-1">WARNING:</font> unless you know what you do, it is better to only make READ-ONLY accesses to the hard disk otherwise you may corrupt your host data (use the <code>-snapshot</code> command line option or modify the device permissions accordingly).</dl>
<p> Windows</p>
<dl>
<dt>&quot;CD&quot;</p>
<dd>The preferred syntax is the drive letter (e.g. <i>d:</i>). The alternate syntax <i>\.\d:</i> is supported. <i>/dev/cdrom</i> is supported as an alias to the first <font SIZE="-1">CDROM</font> drive. Currently there is no specific code to handle removable media, so it is better to use the <tt>&quot;change&quot;</tt> or <tt>&quot;eject&quot;</tt> monitor commands to change or eject media.</p>
<dt>&quot;Hard disks&quot;</p>
<dd>Hard disks can be used with the syntax: <i>\.\PhysicalDriveN</i> where <i>N</i> is the drive number (0 is the first hard disk). <font SIZE="-1">WARNING:</font> unless you know what you do, it is better to only make READ-ONLY accesses to the hard disk otherwise you may corrupt your host data (use the <code>-snapshot</code> command line so that the modifications are written in a temporary file).</dl>
<p> Mac <font SIZE="-1">OS X</font> <i>/dev/cdrom</i> is an alias to the first <font SIZE="-1">CDROM.</font> Currently there is no specific code to handle removable media, so it is better to use the <tt>&quot;change&quot;</tt> or <tt>&quot;eject&quot;</tt> monitor commands to change or eject media. <i>Virtual </i><font SIZE="-1"><i>FAT</i></font><i> disk images</i> <font SIZE="-1">QEMU</font> can automatically create a virtual <font SIZE="-1">FAT</font> disk image from a directory tree. In order to use it, just type: </p>
<pre> qemu-system-x86_64 linux.img -hdb fat:/my_directory</pre>
<p>Then you access access to all the files in the <i>/my_directory</i> directory without having to copy them in a disk image or to export them via <font SIZE="-1">SAMBA</font> or <font SIZE="-1">NFS.</font> The default access is <i>read-only</i>. Floppies can be emulated with the <tt>&quot;:floppy:&quot;</tt> option: </p>
<pre> qemu-system-x86_64 linux.img -fda fat:floppy:/my_directory</pre>
<p>A read/write support is available for testing (beta stage) with the <tt>&quot;:rw:&quot;</tt> option: </p>
<pre> qemu-system-x86_64 linux.img -fda fat:floppy:rw:/my_directory</pre>
<p>What you should <i>never</i> do:</p>
<dl>
<dt>*&lt;use non-ASCII filenames ;&gt;</p>
<dd>
<dt>*&lt;use &quot;-snapshot&quot; together with &quot;:rw:&quot; ;&gt;</p>
<dd>
<dt>*&lt;expect it to work when loadvm&#8217;ing ;&gt;</p>
<dd>
<dt>*&lt;write to the <font SIZE="-1">FAT</font> directory on the host system while accessing it with the guest system.&gt;</p>
<dd></dl>
<p> <i></i><font SIZE="-1"><i>NBD</i></font><i> access</i> <font SIZE="-1">QEMU</font> can access directly to block device exported using the Network Block Device protocol. </p>
<pre> qemu-system-x86_64 linux.img -hdb <a href="nbd://my_nbd_server.mydomain.org:1024/">nbd://my_nbd_server.mydomain.org:1024/</a></pre>
<p>If the <font SIZE="-1">NBD</font> server is located on the same host, you can use an unix socket instead of an inet socket: </p>
<pre> qemu-system-x86_64 linux.img -hdb nbd+<a href="unix://?socket=/tmp/my_socket">unix://?socket=/tmp/my_socket</a></pre>
<p>In this case, the block device must be exported using qemu-nbd: </p>
<pre> qemu-nbd --socket=/tmp/my_socket my_disk.qcow2</pre>
<p>The use of qemu-nbd allows sharing of a disk between several guests: </p>
<pre> qemu-nbd --socket=/tmp/my_socket --share=2 my_disk.qcow2</pre>
<p>and then you can use it with two guests: </p>
<pre> qemu-system-x86_64 linux1.img -hdb nbd+<a href="unix://?socket=/tmp/my_socket">unix://?socket=/tmp/my_socket</a>
 qemu-system-x86_64 linux2.img -hdb nbd+<a href="unix://?socket=/tmp/my_socket">unix://?socket=/tmp/my_socket</a></pre>
<p>If the nbd-server uses named exports (supported since <font SIZE="-1">NBD 2.9.18,</font> or with <font SIZE="-1">QEMU</font>&#8216;s own embedded <font SIZE="-1">NBD</font> server), you must specify an export name in the <font SIZE="-1">URI:</font> </p>
<pre> qemu-system-x86_64 -cdrom <a href="nbd://localhost/debian-500-ppc-netinst">nbd://localhost/debian-500-ppc-netinst</a>
 qemu-system-x86_64 -cdrom <a href="nbd://localhost/openSUSE-11.1-ppc-netinst">nbd://localhost/openSUSE-11.1-ppc-netinst</a></pre>
<p>The <font SIZE="-1">URI</font> syntax for <font SIZE="-1">NBD</font> is supported since <font SIZE="-1">QEMU 1.3.</font> An alternative syntax is also available. Here are some example of the older syntax: </p>
<pre> qemu-system-x86_64 linux.img -hdb nbd:my_nbd_server.mydomain.org:1024
 qemu-system-x86_64 linux2.img -hdb nbd:unix:/tmp/my_socket
 qemu-system-x86_64 -cdrom nbd:localhost:10809:exportname=debian-500-ppc-netinst</pre>
<p><i>Sheepdog disk images</i> Sheepdog is a distributed storage system for <font SIZE="-1">QEMU.</font> It provides highly available block level storage volumes that can be attached to QEMU-based virtual machines. You can create a Sheepdog disk image with the command: </p>
<pre> qemu-img create sheepdog:///&lt;image&gt; &lt;size&gt;</pre>
<p>where <i>image</i> is the Sheepdog image name and <i>size</i> is its size. To import the existing <i>filename</i> to Sheepdog, you can use a convert command. </p>
<pre> qemu-img convert &lt;filename&gt; sheepdog:///&lt;image&gt;</pre>
<p>You can boot from the Sheepdog disk image with the command: </p>
<pre> qemu-system-x86_64 sheepdog:///&lt;image&gt;</pre>
<p>You can also create a snapshot of the Sheepdog image like qcow2. </p>
<pre> qemu-img snapshot -c &lt;tag&gt; sheepdog:///&lt;image&gt;</pre>
<p>where <i>tag</i> is a tag name of the newly created snapshot. To boot from the Sheepdog snapshot, specify the tag name of the snapshot. </p>
<pre> qemu-system-x86_64 sheepdog:///&lt;image&gt;#&lt;tag&gt;</pre>
<p>You can create a cloned image from the existing snapshot. </p>
<pre> qemu-img create -b sheepdog:///&lt;base&gt;#&lt;tag&gt; sheepdog:///&lt;image&gt;</pre>
<p>where <i>base</i> is an image name of the source snapshot and <i>tag</i> is its tag name. You can use an unix socket instead of an inet socket: </p>
<pre> qemu-system-x86_64 sheepdog+<a href="unix:///">unix:///</a>&lt;image&gt;?socket=&lt;path&gt;</pre>
<p>If the Sheepdog daemon doesn&#8217;t run on the local host, you need to specify one of the Sheepdog servers to connect to. </p>
<pre> qemu-img create sheepdog://&lt;hostname&gt;:&lt;port&gt;/&lt;image&gt; &lt;size&gt;
 qemu-system-x86_64 sheepdog://&lt;hostname&gt;:&lt;port&gt;/&lt;image&gt;</pre>
<p><i>iSCSI LUNs</i> iSCSI is a popular protocol used to access <font SIZE="-1">SCSI</font> devices across a computer network. There are two different ways iSCSI devices can be used by <font SIZE="-1">QEMU.</font> The first method is to mount the iSCSI <font SIZE="-1">LUN</font> on the host, and make it appear as any other ordinary <font SIZE="-1">SCSI</font> device on the host and then to access this device as a /dev/sd device from <font SIZE="-1">QEMU.</font> How to do this differs between host OSes. The second method involves using the iSCSI initiator that is built into <font SIZE="-1">QEMU.</font> This provides a mechanism that works the same way regardless of which host <font SIZE="-1">OS</font> you are running <font SIZE="-1">QEMU</font> on. This section will describe this second method of using iSCSI together with <font SIZE="-1">QEMU.</font> In <font SIZE="-1">QEMU,</font> iSCSI devices are described using special iSCSI URLs </p>
<pre> URL syntax:
 <a href="iscsi://[">iscsi://[</a>&lt;username&gt;[%&lt;password&gt;]@]&lt;host&gt;[:&lt;port&gt;]/&lt;target-iqn-name&gt;/&lt;lun&gt;</pre>
<p>Username and password are optional and only used if your target is set up using <font SIZE="-1">CHAP</font> authentication for access control. Alternatively the username and password can also be set via environment variables to have these not show up in the process list </p>
<pre> export LIBISCSI_CHAP_USERNAME=&lt;username&gt;
 export LIBISCSI_CHAP_PASSWORD=&lt;password&gt;
 iscsi://&lt;host&gt;/&lt;target-iqn-name&gt;/&lt;lun&gt;</pre>
<p>Various session related parameters can be set via special options, either in a configuration file provided via &#8216;-readconfig&#8217; or directly on the command line. If the initiator-name is not specified qemu will use a default name of &#8216;iqn.2008-11.org.linux-kvm[:&lt;uuid&gt;&#8217;] where &lt;uuid&gt; is the <font SIZE="-1">UUID</font> of the virtual machine. If the <font SIZE="-1">UUID</font> is not specified qemu will use &#8216;iqn.2008-11.org.linux-kvm[:&lt;name&gt;&#8217;] where &lt;name&gt; is the name of the virtual machine. </p>
<pre> Setting a specific initiator name to use when logging in to the target
 -iscsi initiator-name=iqn.qemu.test:my-initiator
 
 Controlling which type of header digest to negotiate with the target
 -iscsi header-digest=CRC32C|CRC32C-NONE|NONE-CRC32C|NONE</pre>
<p>These can also be set via a configuration file [iscsi]<br />
user = &quot;CHAP username&quot;<br />
password = &quot;CHAP password&quot;<br />
initiator-name = &quot;iqn.qemu.test:my-initiator&quot;<br />
# header digest is one of CRC32C|CRC32C-NONE|NONE-CRC32C|NONE<br />
header-digest = &quot;CRC32C&quot; Setting the target name allows different options for different targets [iscsi &quot;iqn.target.name&quot;]<br />
user = &quot;CHAP username&quot;<br />
password = &quot;CHAP password&quot;<br />
initiator-name = &quot;iqn.qemu.test:my-initiator&quot;<br />
# header digest is one of CRC32C|CRC32C-NONE|NONE-CRC32C|NONE<br />
header-digest = &quot;CRC32C&quot; Howto use a configuration file to set iSCSI configuration options: </p>
<pre> cat &gt;iscsi.conf &lt;&lt;EOF
 [iscsi]
 user = &quot;me&quot;
 password = &quot;my password&quot;
 initiator-name = &quot;iqn.qemu.test:my-initiator&quot;
 header-digest = &quot;CRC32C&quot;
 EOF
 
 qemu-system-x86_64 -drive file=<a href="iscsi://127.0.0.1/iqn.qemu.test/1">iscsi://127.0.0.1/iqn.qemu.test/1</a> \
 -readconfig iscsi.conf</pre>
<p>How to set up a simple iSCSI target on loopback and access it via <font SIZE="-1">QEMU:</font> </p>
<pre> This example shows how to set up an iSCSI target with one CDROM and one DISK
 using the Linux STGT software target. This target is available on Red Hat based
 systems as the package 'scsi-target-utils'.
 
 tgtd --iscsi portal=127.0.0.1:3260
 tgtadm --lld iscsi --op new --mode target --tid 1 -T iqn.qemu.test
 tgtadm --lld iscsi --mode logicalunit --op new --tid 1 --lun 1 \
 -b /IMAGES/disk.img --device-type=disk
 tgtadm --lld iscsi --mode logicalunit --op new --tid 1 --lun 2 \
 -b /IMAGES/cd.iso --device-type=cd
 tgtadm --lld iscsi --op bind --mode target --tid 1 -I ALL
 
 qemu-system-x86_64 -iscsi initiator-name=iqn.qemu.test:my-initiator \
 -boot d -drive file=<a href="iscsi://127.0.0.1/iqn.qemu.test/1">iscsi://127.0.0.1/iqn.qemu.test/1</a> \
 -cdrom <a href="iscsi://127.0.0.1/iqn.qemu.test/2">iscsi://127.0.0.1/iqn.qemu.test/2</a></pre>
<p><i>GlusterFS disk images</i> GlusterFS is a user space distributed file system. You can boot from the GlusterFS disk image with the command: </p>
<pre> URI:
 qemu-system-x86_64 -drive file=gluster[+&lt;type&gt;]://[&lt;host&gt;[:&lt;port&gt;]]/&lt;volume&gt;/&lt;path&gt;
 [?socket=...][,file.debug=9][,file.logfile=...]
 
 JSON:
 qemu-system-x86_64 'json:{&quot;driver&quot;:&quot;qcow2&quot;,
 &quot;file&quot;:{&quot;driver&quot;:&quot;gluster&quot;,
 &quot;volume&quot;:&quot;testvol&quot;,&quot;path&quot;:&quot;a.img&quot;,&quot;debug&quot;:9,&quot;logfile&quot;:&quot;...&quot;,
 &quot;server&quot;:[{&quot;type&quot;:&quot;tcp&quot;,&quot;host&quot;:&quot;...&quot;,&quot;port&quot;:&quot;...&quot;},
 {&quot;type&quot;:&quot;unix&quot;,&quot;socket&quot;:&quot;...&quot;}]}}'</pre>
<p><i>gluster</i> is the protocol. <i>type</i> specifies the transport type used to connect to gluster management daemon (glusterd). Valid transport types are tcp and unix. In the <font SIZE="-1">URI</font> form, if a transport type isn&#8217;t specified, then tcp type is assumed. <i>host</i> specifies the server where the volume file specification for the given volume resides. This can be either a hostname or an ipv4 address. If transport type is unix, then <i>host</i> field should not be specified. Instead <i>socket</i> field needs to be populated with the path to unix domain socket. <i>port</i> is the port number on which glusterd is listening. This is optional and if not specified, it defaults to port 24007. If the transport type is unix, then <i>port</i> should not be specified. <i>volume</i> is the name of the gluster volume which contains the disk image. <i>path</i> is the path to the actual disk image that resides on gluster volume. <i>debug</i> is the logging level of the gluster protocol driver. Debug levels are 0-9, with 9 being the most verbose, and 0 representing no debugging output. The default level is 4. The current logging levels defined in the gluster source are 0 &#8211; None, 1 &#8211; Emergency, 2 &#8211; Alert, 3 &#8211; Critical, 4 &#8211; Error, 5 &#8211; Warning, 6 &#8211; Notice, 7 &#8211; Info, 8 &#8211; Debug, 9 &#8211; Trace <i>logfile</i> is a commandline option to mention log file path which helps in logging to the specified file and also help in persisting the gfapi logs. The default is stderr. You can create a GlusterFS disk image with the command: </p>
<pre> qemu-img create gluster://&lt;host&gt;/&lt;volume&gt;/&lt;path&gt; &lt;size&gt;</pre>
<p>Examples </p>
<pre> qemu-system-x86_64 -drive file=gluster://1.2.3.4/testvol/a.img
 qemu-system-x86_64 -drive file=gluster+<a href="tcp://1.2.3.4/testvol/a.img">tcp://1.2.3.4/testvol/a.img</a>
 qemu-system-x86_64 -drive file=gluster+<a href="tcp://1.2.3.4:24007/testvol/dir/a.img">tcp://1.2.3.4:24007/testvol/dir/a.img</a>
 qemu-system-x86_64 -drive file=gluster+<a href="tcp://[1:2:3:4:5:6:7:8]/testvol/dir/a.img">tcp://[1:2:3:4:5:6:7:8]/testvol/dir/a.img</a>
 qemu-system-x86_64 -drive file=gluster+<a href="tcp://[1:2:3:4:5:6:7:8]:24007/testvol/dir/a.img">tcp://[1:2:3:4:5:6:7:8]:24007/testvol/dir/a.img</a>
 qemu-system-x86_64 -drive file=gluster+<a href="tcp://server.domain.com:24007/testvol/dir/a.img">tcp://server.domain.com:24007/testvol/dir/a.img</a>
 qemu-system-x86_64 -drive file=gluster+<a href="unix:///testvol/dir/a.img?socket=/tmp/glusterd.socket">unix:///testvol/dir/a.img?socket=/tmp/glusterd.socket</a>
 qemu-system-x86_64 -drive file=gluster+<a href="rdma://1.2.3.4:24007/testvol/a.img">rdma://1.2.3.4:24007/testvol/a.img</a>
 qemu-system-x86_64 -drive file=gluster://1.2.3.4/testvol/a.img,file.debug=9,file.logfile=/var/log/qemu-gluster.log
 qemu-system-x86_64 'json:{&quot;driver&quot;:&quot;qcow2&quot;,
 &quot;file&quot;:{&quot;driver&quot;:&quot;gluster&quot;,
 &quot;volume&quot;:&quot;testvol&quot;,&quot;path&quot;:&quot;a.img&quot;,
 &quot;debug&quot;:9,&quot;logfile&quot;:&quot;/var/log/qemu-gluster.log&quot;,
 &quot;server&quot;:[{&quot;type&quot;:&quot;tcp&quot;,&quot;host&quot;:&quot;1.2.3.4&quot;,&quot;port&quot;:24007},
 {&quot;type&quot;:&quot;unix&quot;,&quot;socket&quot;:&quot;/var/run/glusterd.socket&quot;}]}}'
 qemu-system-x86_64 -drive driver=qcow2,file.driver=gluster,file.volume=testvol,file.path=/path/a.img,
 file.debug=9,file.logfile=/var/log/qemu-gluster.log,
 file.server.0.type=tcp,file.server.0.host=1.2.3.4,file.server.0.port=24007,
 file.server.1.type=unix,file.server.1.socket=/var/run/glusterd.socket</pre>
<p><i>Secure Shell (ssh) disk images</i> You can access disk images located on a remote ssh server by using the ssh protocol: </p>
<pre> qemu-system-x86_64 -drive file=<a href="ssh://[">ssh://[</a>&lt;user&gt;@]&lt;server&gt;[:&lt;port&gt;]/&lt;path&gt;[?host_key_check=&lt;host_key_check&gt;]</pre>
<p>Alternative syntax using properties: </p>
<pre> qemu-system-x86_64 -drive file.driver=ssh[,file.user=&lt;user&gt;],file.host=&lt;server&gt;[,file.port=&lt;port&gt;],file.path=&lt;path&gt;[,file.host_key_check=&lt;host_key_check&gt;]</pre>
<p><i>ssh</i> is the protocol. <i>user</i> is the remote user. If not specified, then the local username is tried. <i>server</i> specifies the remote ssh server. Any ssh server can be used, but it must implement the sftp-server protocol. Most Unix/Linux systems should work without requiring any extra configuration. <i>port</i> is the port number on which sshd is listening. By default the standard ssh port (22) is used. <i>path</i> is the path to the disk image. The optional <i>host_key_check</i> parameter controls how the remote host&#8217;s key is checked. The default is <tt>&quot;yes&quot;</tt> which means to use the local <i>.ssh/known_hosts</i> file. Setting this to <tt>&quot;no&quot;</tt> turns off known-hosts checking. Or you can check that the host key matches a specific fingerprint: <tt>&quot;host_key_check=md5:78:45:8e:14:57:4f:d5:45:83:0a:0e:f3:49:82:c9:c8&quot;</tt> (<tt>&quot;sha1:&quot;</tt> can also be used as a prefix, but note that OpenSSH tools only use <font SIZE="-1">MD5</font> to print fingerprints). Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future. Note: Many ssh servers do not support an <tt>&quot;fsync&quot;</tt>-style operation. The ssh driver cannot guarantee that disk flush requests are obeyed, and this causes a risk of disk corruption if the remote server or network goes down during writes. The driver will print a warning when <tt>&quot;fsync&quot;</tt> is not supported: warning: ssh server <tt>&quot;ssh.example.com:22&quot;</tt> does not support fsync With sufficiently new versions of libssh and OpenSSH, <tt>&quot;fsync&quot;</tt> is supported. <i>NVMe disk images</i> <font SIZE="-1">NVM</font> Express (NVMe) storage controllers can be accessed directly by a userspace driver in <font SIZE="-1">QEMU.</font> This bypasses the host kernel file system and block layers while retaining <font SIZE="-1">QEMU</font> block layer functionalities, such as block jobs, I/O throttling, image formats, etc. Disk I/O performance is typically higher than with <tt>&quot;-drive file=/dev/sda&quot;</tt> using either thread pool or linux-aio. The controller will be exclusively used by the <font SIZE="-1">QEMU</font> process once started. To be able to share storage between multiple VMs and other applications on the host, please use the file based protocols. Before starting <font SIZE="-1">QEMU,</font> bind the host NVMe controller to the host vfio-pci driver. For example: </p>
<pre> # modprobe vfio-pci
 # lspci -n -s 0000:06:0d.0
 06:0d.0 0401: 1102:0002 (rev 08)
 # echo 0000:06:0d.0 &gt; /sys/bus/pci/devices/0000:06:0d.0/driver/unbind
 # echo 1102 0002 &gt; /sys/bus/pci/drivers/vfio-pci/new_id
 
 # qemu-system-x86_64 -drive file=nvme://&lt;host&gt;:&lt;bus&gt;:&lt;slot&gt;.&lt;func&gt;/&lt;namespace&gt;</pre>
<p>Alternative syntax using properties: </p>
<pre> qemu-system-x86_64 -drive file.driver=nvme,file.device=&lt;host&gt;:&lt;bus&gt;:&lt;slot&gt;.&lt;func&gt;,file.namespace=&lt;namespace&gt;</pre>
<p><i>host</i>:<i>bus</i>:<i>slot</i>.<i>func</i> is the NVMe controller&#8217;s <font SIZE="-1">PCI</font> device address on the host. <i>namespace</i> is the NVMe namespace number, starting from 1. <i>Disk image file locking</i> By default, <font SIZE="-1">QEMU</font> tries to protect image files from unexpected concurrent access, as long as it&#8217;s supported by the block protocol driver and host operating system. If multiple <font SIZE="-1">QEMU</font> processes (including <font SIZE="-1">QEMU</font> emulators and utilities) try to open the same image with conflicting accessing modes, all but the first one will get an error. This feature is currently supported by the file protocol on Linux with the Open File Descriptor (<font SIZE="-1">OFD</font>) locking <font SIZE="-1">API,</font> and can be configured to fall back to <font SIZE="-1">POSIX</font> locking if the <font SIZE="-1">POSIX</font> host doesn&#8217;t support Linux <font SIZE="-1">OFD</font> locking. To explicitly enable image locking, specify &#8220;locking=on&#8221; in the file protocol driver options. If <font SIZE="-1">OFD</font> locking is not possible, a warning will be printed and the <font SIZE="-1">POSIX</font> locking <font SIZE="-1">API</font> will be used. In this case there is a risk that the lock will get silently lost when doing hot plugging and block jobs, due to the shortcomings of the <font SIZE="-1">POSIX</font> locking <font SIZE="-1">API.</font> <font SIZE="-1">QEMU</font> transparently handles lock handover during shared storage migration. For shared virtual disk images between multiple VMs, the &#8220;share-rw&#8221; device option should be used. By default, the guest has exclusive write access to its disk image. If the guest can safely share the disk image with other writers the <tt>&quot;-device ...,share-rw=on&quot;</tt> parameter can be used. This is only safe if the guest is running software, such as a cluster file system, that coordinates disk accesses to avoid corruption. Note that share-rw=on only declares the guest&#8217;s ability to share the disk. Some <font SIZE="-1">QEMU</font> features, such as image file formats, require exclusive write access to the disk image and this is unaffected by the share-rw=on option. Alternatively, locking can be fully disabled by &#8220;locking=off&#8221; block device option. In the command line, the option is usually in the form of &#8220;file.locking=off&#8221; as the protocol driver is normally placed as a &#8220;file&#8221; child under a format driver. For example: </p>
<pre><code>&quot;-blockdev driver=qcow2,file.filename=/path/to/image,file.locking=off,file.driver=file&quot;</code></pre>
<p> To check if image locking is active, check the output of the &#8220;lslocks&#8221; command on host and see if there are locks held by the <font SIZE="-1">QEMU</font> process on the image file. More than one byte could be locked by the <font SIZE="-1">QEMU</font> instance, each byte of which reflects a particular permission that is acquired or protected by the running block driver.</p>
<h2>See Also</h2>
<p>The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.</p>
<h2>Author</h2>
<p>Fabrice Bellard and the <font SIZE="-1">QEMU</font> Project developers</p>
