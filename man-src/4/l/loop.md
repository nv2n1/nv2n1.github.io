---
title: "loop(4)"
name: "loop"
section: "4"
letter: "l"
url: "/docs/linux/man/4-loop/"
description: "loop, loop-control – loop devices"
---

<p>loop, loop-control &#8211; loop devices</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/loop.h&gt;</code></pre>
<h2>Description</h2>
<p>The loop device is a block device that maps its data blocks not to a physical device such as a hard disk or optical disk drive, but to the blocks of a regular file in a filesystem or to another block device. This can be useful for example to provide a block device for a filesystem image stored in a file, so that it can be mounted with the <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) command. You could do </p>
<p> $ <code>dd if=/dev/zero of=file.img bs=1MiB count=10</code> $ <code>sudo losetup /dev/loop4 file.img</code> $ <code>sudo mkfs -t ext4 /dev/loop4</code> $ <code>sudo mkdir /myloopdev</code> $ <code>sudo mount /dev/loop4 /myloopdev</code> </p>
<p> See <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8) for another example. </p>
<p> A transfer function can be specified for each loop device for encryption and decryption purposes. </p>
<p> The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations are provided by the loop block device:</p>
<dl>
<dt><code>LOOP_SET_FD</code></p>
<dd>Associate the loop device with the open file whose file descriptor is passed as the (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument.</p>
<dt><code>LOOP_CLR_FD</code></p>
<dd>Disassociate the loop device from any file descriptor.</p>
<dt><code>LOOP_SET_STATUS</code></p>
<dd>Set the status of the loop device using the (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. This argument is a pointer to a <i>loop_info</i> structure, defined in <i>&lt;linux/loop.h&gt;</i> as:</p>
<dd>struct loop_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_number;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_device;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long lo_inode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_rdevice;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_encrypt_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_encrypt_key_size;&nbsp;<wbr>&nbsp;/*&nbsp;ioctl w/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/w&nbsp;(r/o before<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Linux 2.6.25)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lo_name[LO_NAME_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char lo_encrypt_key[LO_KEY_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl w/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long lo_init[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reserved[4]; };</p>
<dd>The encryption type (<i>lo_encrypt_type</i>) should be one of <code>LO_CRYPT_NONE</code>, <code>LO_CRYPT_XOR</code>, <code>LO_CRYPT_DES</code>, <code>LO_CRYPT_FISH2</code>, <code>LO_CRYPT_BLOW</code>, <code>LO_CRYPT_CAST128</code>, <code>LO_CRYPT_IDEA</code>, <code>LO_CRYPT_DUMMY</code>, <code>LO_CRYPT_SKIPJACK</code>, or (since Linux 2.6.0) <code>LO_CRYPT_CRYPTOAPI</code>.</p>
<dd>The <i>lo_flags</i> field is a bit mask that can include zero or more of the following:</p>
<dl>
<dd>
<dl>
<dt><code>LO_FLAGS_READ_ONLY</code></p>
<dd>The loopback device is read-only.</p>
<dt><code>LO_FLAGS_AUTOCLEAR</code> (since Linux 2.6.25)</p>
<dd>The loopback device will autodestruct on last close.</p>
<dt><code>LO_FLAGS_PARTSCAN</code> (since Linux 3.2)</p>
<dd>Allow automatic partition scanning.</p>
<dt><code>LO_FLAGS_DIRECT_IO</code> (since Linux 4.10)</p>
<dd>Use direct I/O mode to access the backing file.</dl>
</dl>
<dd>The only <i>lo_flags</i> that can be modified by <code>LOOP_SET_STATUS</code> are <code>LO_FLAGS_AUTOCLEAR</code> and <code>LO_FLAGS_PARTSCAN</code>.</p>
<dt><code>LOOP_GET_STATUS</code></p>
<dd>Get the status of the loop device. The (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument must be a pointer to a <i>struct loop_info</i>.</p>
<dt><code>LOOP_CHANGE_FD</code> (since Linux 2.6.5)</p>
<dd>Switch the backing store of the loop device to the new file identified file descriptor specified in the (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument, which is an integer. This operation is possible only if the loop device is read-only and the new backing store is the same size and type as the old backing store.</p>
<dt><code>LOOP_SET_CAPACITY</code> (since Linux 2.6.30)</p>
<dd>Resize a live loop device. One can change the size of the underlying backing store and then use this operation so that the loop driver learns about the new size. This operation takes no argument.</p>
<dt><code>LOOP_SET_DIRECT_IO</code> (since Linux 4.10)</p>
<dd>Set DIRECT I/O mode on the loop device, so that it can be used to open backing file. The (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is an unsigned long value. A nonzero represents direct I/O mode.</p>
<dt><code>LOOP_SET_BLOCK_SIZE</code> (since Linux 4.14)</p>
<dd>Set the block size of the loop device. The (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is an unsigned long value. This value must be a power of two in the range [512,pagesize]; otherwise, an <code>EINVAL</code> error results.</p>
<dt><code>LOOP_CONFIGURE</code> (since Linux 5.8)</p>
<dd>Setup and configure all loop device parameters in a single step using the (third) <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. This argument is a pointer to a <i>loop_config</i> structure, defined in <i>&lt;linux/loop.h&gt;</i> as:</p>
<dd>struct loop_config {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;block_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct loop_info64&nbsp;<wbr>&nbsp;info;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__reserved[8]; };</p>
<dd>In addition to doing what <code>LOOP_SET_STATUS</code> can do, <code>LOOP_CONFIGURE</code> can also be used to do the following:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>set the correct block size immediately by setting <i>loop_config.block_size</i>;</p>
<dt>*</p>
<dd>explicitly request direct I/O mode by setting <code>LO_FLAGS_DIRECT_IO</code> in <i>loop_config.info.lo_flags</i>; and</p>
<dt>*</p>
<dd>explicitly request read-only mode by setting <code>LO_FLAGS_READ_ONLY</code> in <i>loop_config.info.lo_flags</i>.</dl>
</dl>
</dl>
<p> Since Linux 2.6, there are two new <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations:</p>
<dl>
<dt><code>LOOP_SET_STATUS64</code>, <code>LOOP_GET_STATUS64</code></p>
<dd>These are similar to <code>LOOP_SET_STATUS</code> and <code>LOOP_GET_STATUS</code> described above but use the <i>loop_info64</i> structure, which has some additional fields and a larger range for some other fields:</p>
<dd>struct loop_info64 {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_device;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_inode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_rdevice;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_sizelimit;&nbsp;<wbr>&nbsp;/*&nbsp;bytes, 0&nbsp;==&nbsp;max available&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t lo_number;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t lo_encrypt_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t lo_encrypt_key_size;&nbsp;/*&nbsp;ioctl w/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t lo_flags;&nbsp;i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ioctl r/w&nbsp;(r/o before<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Linux 2.6.25)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;lo_file_name[LO_NAME_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;lo_crypt_name[LO_NAME_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;lo_encrypt_key[LO_KEY_SIZE];&nbsp;/*&nbsp;ioctl w/o&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lo_init[2]; };</dl>
<h3>/dev/loop-control</h3>
<p>Since Linux 3.1, the kernel provides the <i>/dev/loop-control</i> device, which permits an application to dynamically find a free device, and to add and remove loop devices from the system. To perform these operations, one first opens <i>/dev/loop-control</i> and then employs one of the following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations:</p>
<dl>
<dt><code>LOOP_CTL_GET_FREE</code></p>
<dd>Allocate or find a free loop device for use. On success, the device number is returned as the result of the call. This operation takes no argument.</p>
<dt><code>LOOP_CTL_ADD</code></p>
<dd>Add the new loop device whose device number is specified as a long integer in the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. On success, the device index is returned as the result of the call. If the device is already allocated, the call fails with the error <code>EEXIST</code>.</p>
<dt><code>LOOP_CTL_REMOVE</code></p>
<dd>Remove the loop device whose device number is specified as a long integer in the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. On success, the device number is returned as the result of the call. If the device is in use, the call fails with the error <code>EBUSY</code>.</dl>
<h2>Files</h2>
<dl>
<dt><i>/dev/loop*</i></p>
<dd>The loop block special device files.</dl>
<h2>Examples</h2>
<p>The program below uses the <i>/dev/loop-control</i> device to find a free loop device, opens the loop device, opens a file to be used as the underlying storage for the device, and then associates the loop device with the backing store. The following shell session demonstrates the use of the program: </p>
<pre><code>$ dd if=/dev/zero of=file.img bs=1MiB count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB) copied, 0.00609385 s, 1.7 GB/s
$ sudo ./mnt_loop file.img
loopname = /dev/loop5



Program source



#include &lt;fcntl.h&gt;
#include &lt;linux/loop.h&gt;
#include &lt;sys/ioctl.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#define errExit(msg)    do { perror(msg); exit(EXIT_FAILURE); \
} while (0)
int
main(int argc, char *argv[])
{
    int loopctlfd, loopfd, backingfile;
    long devnr;
    char loopname[4096];
    if (argc != 2) {
        fprintf(stderr, &quot;Usage: %s backing-file
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    loopctlfd = open(&quot;/dev/loop-control&quot;, O_RDWR);
    if (loopctlfd == -1)
    errExit(&quot;open: /dev/loop-control&quot;);
    devnr = ioctl(loopctlfd, LOOP_CTL_GET_FREE);
    if (devnr == -1)
    errExit(&quot;ioctl-LOOP_CTL_GET_FREE&quot;);
    sprintf(loopname, &quot;/dev/loop%ld&quot;, devnr);
    printf(&quot;loopname = %s
&quot;, loopname);
    loopfd = open(loopname, O_RDWR);
    if (loopfd == -1)
    errExit(&quot;open: loopname&quot;);
    backingfile = open(argv[1], O_RDWR);
    if (backingfile == -1)
    errExit(&quot;open: backing-file&quot;);
    if (ioctl(loopfd, LOOP_SET_FD, backingfile) == -1)
    errExit(&quot;ioctl-LOOP_SET_FD&quot;);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
