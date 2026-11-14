---
title: "spufs(2)"
name: "spufs"
section: "2"
letter: "s"
url: "/docs/linux/man/2-spufs/"
description: "spufs – the SPU file system"
---

<h2>NAME</h2>
<p> spufs &#8211; the SPU file system </p>
<h2>DESCRIPTION</h2>
<p> The SPU file system is used on PowerPC machines that implement the Cell Broadband Engine Architecture in order to access Synergistic Processor Units (SPUs). </p>
<p> The file system provides a name space similar to posix shared memory or message queues. Users that have write permissions on the file system can use <code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2) to establish SPU contexts in the spufs root. </p>
<p> Every SPU context is represented by a directory containing a predefined set of files. These files can be used for manipulating the state of the logical SPU. Users can change permissions on those files, but not actually add or remove files. </p>
<h2>MOUNT OPTIONS</h2>
<dl>
<dt><code>uid=&lt;uid&gt;</code></p>
<dd> set the user owning the mount point, the default is 0 (root).</p>
<dt><code>gid=&lt;gid&gt;</code></p>
<dd> set the group owning the mount point, the default is 0 (root). </p>
</dl>
<h2>FILES</h2>
<p> The files in <i>spufs</i> mostly follow the standard behavior for regular system calls like <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2), but often support only a subset of the operations supported on regular file systems. This list details the supported operations and the deviations from the behaviour in the respective man pages. </p>
<p> All files that support the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) operation also support <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2) and all files that support the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operation also support <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2). All files support the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) family of operations, but only the st_mode, st_nlink, st_uid and st_gid fields of <code>struct stat</code> contain reliable information. </p>
<p> All files support the <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)/<code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2) and <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2)/<code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2) operations, but will not be able to grant permissions that contradict the possible operations, e.g. read access on the <code>wbox</code> file. </p>
<p> The current set of files is: </p>
<h3>/mem</h3>
<p> the contents of the local storage memory of the SPU. This can be accessed like a regular shared memory file and contains both code and data in the address space of the SPU. The possible operations on an open <code>mem</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2)</p>
<dd> These operate as documented, with the exception that <code><a href="/docs/linux/man/2-seek/">seek</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2) and <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2) are not supported beyond the end of the file. The file size is the size of the local storage of the SPU, which normally is 256 kilobytes.</p>
<dt><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)</p>
<dd> Mapping <code>mem</code> into the process address space gives access to the SPU local storage within the process address space. Only MAP_SHARED mappings are allowed. </p>
</dl>
<h3>/mbox</h3>
<p> The first SPU to CPU communication mailbox. This file is read-only and can be read in units of 32 bits. The file can only be used in non-blocking mode and it even poll() will not block on it. The possible operations on an open <code>mbox</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>read</code> returns -1 and sets errno to EINVAL. If there is no data available in the mail box, the return value is set to -1 and errno becomes EAGAIN. When data has been read successfully, four bytes are placed in the data buffer and the value four is returned. </p>
</dl>
<h3>/ibox</h3>
<p> The second SPU to CPU communication mailbox. This file is similar to the first mailbox file, but can be read in blocking I/O mode, and the poll familiy of system calls can be used to wait for it. The possible operations on an open <code>ibox</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>read</code> returns -1 and sets errno to EINVAL. If there is no data available in the mail box and the file descriptor has been opened with O_NONBLOCK, the return value is set to -1 and errno becomes EAGAIN. </p>
<p> If there is no data available in the mail box and the file descriptor has been opened without O_NONBLOCK, the call will block until the SPU writes to its interrupt mailbox channel. When data has been read successfully, four bytes are placed in the data buffer and the value four is returned.</p>
<dt><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)</p>
<dd> Poll on the <code>ibox</code> file returns (POLLIN | POLLRDNORM) whenever data is available for reading. </p>
</dl>
<h3>/wbox</h3>
<p> The CPU to SPU communation mailbox. It is write-only can can be written in units of 32 bits. If the mailbox is full, write() will block and poll can be used to wait for it becoming empty again. The possible operations on an open <code>wbox</code> file are: <code><a href="/docs/linux/man/2-write/">write</a></code>(2) If a count smaller than four is requested, <code>write</code> returns -1 and sets errno to EINVAL. If there is no space available in the mail box and the file descriptor has been opened with O_NONBLOCK, the return value is set to -1 and errno becomes EAGAIN. </p>
<p> If there is no space available in the mail box and the file descriptor has been opened without O_NONBLOCK, the call will block until the SPU reads from its PPE mailbox channel. When data has been read successfully, four bytes are placed in the data buffer and the value four is returned.</p>
<dl>
<dt><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)</p>
<dd> Poll on the <code>ibox</code> file returns (POLLOUT | POLLWRNORM) whenever space is available for writing. </p>
</dl>
<h3>/mbox_stat</h3>
<h3>/ibox_stat</h3>
<h3>/wbox_stat</h3>
<p> Read-only files that contain the length of the current queue, i.e. how many words can be read from mbox or ibox or how many words can be written to wbox without blocking. The files can be read only in 4-byte units and return a big-endian binary integer number. The possible operations on an open <code>*box_stat</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>read</code> returns -1 and sets errno to EINVAL. Otherwise, a four byte value is placed in the data buffer, containing the number of elements that can be read from (for <code>mbox_stat</code> and <code>ibox_stat)</code> or written to (for <code>wbox_stat)</code> the respective mail box without blocking or resulting in EAGAIN. </p>
</dl>
<h3>/npc</h3>
<h3>/decr</h3>
<h3>/decr_status</h3>
<h3>/spu_tag_mask</h3>
<h3>/event_mask</h3>
<h3>/srr0</h3>
<p> Internal registers of the SPU. The representation is an ASCII string with the numeric value of the next instruction to be executed. These can be used in read/write mode for debugging, but normal operation of programs should not rely on them because access to any of them except npc requires an SPU context save and is therefore very inefficient. </p>
<p> The contents of these files are:</p>
<dl>
<dt><code>npc</code></p>
<dd> Next Program Counter</p>
<dt><code>decr</code></p>
<dd> SPU Decrementer</p>
<dt><code>decr_status</code></p>
<dd> Decrementer Status</p>
<dt><code>spu_tag_mask</code></p>
<dd> MFC tag mask for SPU DMA</p>
<dt><code>event_mask</code></p>
<dd> Event mask for SPU interrupts</p>
<dt><code>srr0</code></p>
<dd> Interrupt Return address register</dl>
<p> The possible operations on an open <code>npc,</code> <code>decr,</code> <code>decr_status,</code> <code>spu_tag_mask,</code> <code>event_mask</code> or <code>srr0</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> When the count supplied to the <code>read</code> call is shorter than the required length for the pointer value plus a newline character, subsequent reads from the same file descriptor will result in completing the string, regardless of changes to the register by a running SPU task. When a complete string has been read, all subsequent read operations will return zero bytes and a new file descriptor needs to be opened to read the value again.</p>
<dt><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<dd> A <code>write</code> operation on the file results in setting the register to the value given in the string. The string is parsed from the beginning to the first non-numeric character or the end of the buffer. Subsequent writes to the same file descriptor overwrite the previous setting. </p>
</dl>
<h3>/fpcr</h3>
<p> This file gives access to the Floating Point Status and Control Register as a four byte long file. The operations on the <code>fpcr</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>read</code> returns -1 and sets errno to EINVAL. Otherwise, a four byte value is placed in the data buffer, containing the current value of the fpcr register.</p>
<dt><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>write</code> returns -1 and sets errno to EINVAL. Otherwise, a four byte value is copied from the data buffer, updating the value of the fpcr register. </p>
</dl>
<h3>/signal1</h3>
<h3>/signal2</h3>
<p> The two signal notification channels of an SPU. These are read-write files that operate on a 32 bit word. Writing to one of these files triggers an interrupt on the SPU. The value writting to the signal files can be read from the SPU through a channel read or from host user space through the file. After the value has been read by the SPU, it is reset to zero. The possible operations on an open <code>signal1</code> or <code>signal2</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>read</code> returns -1 and sets errno to EINVAL. Otherwise, a four byte value is placed in the data buffer, containing the current value of the specified signal notification register.</p>
<dt><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<dd> If a count smaller than four is requested, <code>write</code> returns -1 and sets errno to EINVAL. Otherwise, a four byte value is copied from the data buffer, updating the value of the specified signal notification register. The signal notification register will either be replaced with the input data or will be updated to the bitwise OR or the old value and the input data, depending on the contents of the signal1_type, or signal2_type respectively, file. </p>
</dl>
<h3>/signal1_type</h3>
<h3>/signal2_type</h3>
<p> These two files change the behavior of the signal1 and signal2 notification files. The contain a numerical ASCII string which is read as either &quot;1&quot; or &quot;0&quot;. In mode 0 (overwrite), the hardware replaces the contents of the signal channel with the data that is written to it. in mode 1 (logical OR), the hardware accumulates the bits that are subsequently written to it. The possible operations on an open <code>signal1_type</code> or <code>signal2_type</code> file are:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> When the count supplied to the <code>read</code> call is shorter than the required length for the digit plus a newline character, subsequent reads from the same file descriptor will result in completing the string. When a complete string has been read, all subsequent read operations will return zero bytes and a new file descriptor needs to be opened to read the value again.</p>
<dt><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<dd> A <code>write</code> operation on the file results in setting the register to the value given in the string. The string is parsed from the beginning to the first non-numeric character or the end of the buffer. Subsequent writes to the same file descriptor overwrite the previous setting. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>/etc/fstab entry</code></p>
<dd> none <tt>&nbsp;<wbr></tt>/spu <tt>&nbsp;<wbr>&nbsp;<wbr></tt>spufs <tt>&nbsp;<wbr></tt>gid=spu <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
</dl>
<h2>AUTHORS</h2>
<p> Arnd Bergmann &lt;arndb [at] de.ibm.com&gt;, Mark Nutter &lt;mnutter [at] us.ibm.com&gt;, Ulrich Weigand &lt;Ulrich.Weigand [at] de.ibm.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2), <code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2), <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7) </p>
<h2>Index</h2>
