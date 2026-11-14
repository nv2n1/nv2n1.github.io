---
title: "urandom(4)"
name: "urandom"
section: "4"
letter: "u"
url: "/docs/linux/man/4-urandom/"
description: "random, urandom – kernel random number source devices"
---

<p>random, urandom &#8211; kernel random number source devices</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/random.h&gt;
int ioctl(fd, RNDrequest, param);</code></pre>
<h2>Description</h2>
<p>The character special files <i>/dev/random</i> and <i>/dev/urandom</i> (present since Linux 1.3.30) provide an interface to the kernel&#8217;s random number generator. The file <i>/dev/random</i> has major device number 1 and minor device number 8. The file <i>/dev/urandom</i> has major device number 1 and minor device number 9. </p>
<p> The random number generator gathers environmental noise from device drivers and other sources into an entropy pool. The generator also keeps an estimate of the number of bits of noise in the entropy pool. From this entropy pool, random numbers are created. </p>
<p> Linux 3.17 and later provides the simpler and safer <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) interface which requires no special files; see the <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) manual page for details. </p>
<p> When read, the <i>/dev/urandom</i> device returns random bytes using a pseudorandom number generator seeded from the entropy pool. Reads from this device do not block (i.e., the CPU is not yielded), but can incur an appreciable delay when requesting large amounts of data. </p>
<p> When read during early boot time, <i>/dev/urandom</i> may return data prior to the entropy pool being initialized. If this is of concern in your application, use <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) or <i>/dev/random</i> instead. </p>
<p> The <i>/dev/random</i> device is a legacy interface which dates back to a time where the cryptographic primitives used in the implementation of <i>/dev/urandom</i> were not widely trusted. It will return random bytes only within the estimated number of bits of fresh noise in the entropy pool, blocking if necessary. <i>/dev/random</i> is suitable for applications that need high quality randomness, and can afford indeterminate delays. </p>
<p> When the entropy pool is empty, reads from <i>/dev/random</i> will block until additional environmental noise is gathered. If <code><a href="/docs/linux/man/2-open/">open</a></code>(2) is called for <i>/dev/random</i> with the <code>O_NONBLOCK</code> flag, a subsequent <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will not block if the requested number of bytes is not available. Instead, the available bytes are returned. If no byte is available, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will return -1 and <i>errno</i> will be set to <code>EAGAIN</code>. </p>
<p> The <code>O_NONBLOCK</code> flag has no effect when opening <i>/dev/urandom</i>. When calling <code><a href="/docs/linux/man/2-read/">read</a></code>(2) for the device <i>/dev/urandom</i>, reads of up to 256 bytes will return as many bytes as are requested and will not be interrupted by a signal handler. Reads with a buffer over this limit may return less than the requested number of bytes or fail with the error <code>EINTR</code>, if interrupted by a signal handler. </p>
<p> Since Linux 3.16, a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from <i>/dev/urandom</i> will return at most 32 MB. A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from <i>/dev/random</i> will return at most 512 bytes (340 bytes on Linux kernels before version 2.6.12). </p>
<p> Writing to <i>/dev/random</i> or <i>/dev/urandom</i> will update the entropy pool with the data written, but this will not result in a higher entropy count. This means that it will impact the contents read from both files, but it will not make reads from <i>/dev/random</i> faster.</p>
<h3>Usage</h3>
<p>The <i>/dev/random</i> interface is considered a legacy interface, and <i>/dev/urandom</i> is preferred and sufficient in all use cases, with the exception of applications which require randomness during early boot time; for these applications, <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) must be used instead, because it will block until the entropy pool is initialized. </p>
<p> If a seed file is saved across reboots as recommended below, the output is cryptographically secure against attackers without local root access as soon as it is reloaded in the boot sequence, and perfectly adequate for network encryption session keys. (All major Linux distributions have saved the seed file across reboots since 2000 at least.) Since reads from <i>/dev/random</i> may block, users will usually want to open it in nonblocking mode (or perform a read with timeout), and provide some sort of user notification if the desired entropy is not immediately available.</p>
<h3>Configuration</h3>
<p>If your system does not have <i>/dev/random</i> and <i>/dev/urandom</i> created already, they can be created with the following commands: </p>
<p> mknod -m 666 /dev/random c 1 8 mknod -m 666 /dev/urandom c 1 9 chown root:root /dev/random /dev/urandom </p>
<p> When a Linux system starts up without much operator interaction, the entropy pool may be in a fairly predictable state. This reduces the actual amount of noise in the entropy pool below the estimate. In order to counteract this effect, it helps to carry entropy pool information across shut-downs and start-ups. To do this, add the lines to an appropriate script which is run during the Linux system start-up sequence: </p>
<p> echo &quot;Initializing random number generator&#8230;&quot; random_seed=/var/run/random-seed # Carry a random seed from start-up to start-up # Load and then save the whole entropy pool if [ -f $random_seed ]; then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cat&nbsp;$random_seed&nbsp;&gt;/dev/urandom else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;touch&nbsp;$random_seed fi chmod 600 $random_seed poolfile=/proc/sys/kernel/random/poolsize [ -r $poolfile ] &amp;&amp; bits=$(cat $poolfile) || bits=4096 bytes=$(expr $bits / 8) dd if=/dev/urandom of=$random_seed count=1 bs=$bytes </p>
<p> Also, add the following lines in an appropriate script which is run during the Linux system shutdown: </p>
<p> # Carry a random seed from shut-down to start-up # Save the whole entropy pool echo &quot;Saving random seed&#8230;&quot; random_seed=/var/run/random-seed touch $random_seed chmod 600 $random_seed poolfile=/proc/sys/kernel/random/poolsize [ -r $poolfile ] &amp;&amp; bits=$(cat $poolfile) || bits=4096 bytes=$(expr $bits / 8) dd if=/dev/urandom of=$random_seed count=1 bs=$bytes </p>
<p> In the above examples, we assume Linux 2.6.0 or later, where <i>/proc/sys/kernel/random/poolsize</i> returns the size of the entropy pool in bits (see below).</p>
<h3>/proc interfaces</h3>
<p>The files in the directory <i>/proc/sys/kernel/random</i> (present since 2.3.16) provide additional information about the <i>/dev/random</i> device:</p>
<dl>
<dt><i>entropy_avail</i></p>
<dd>This read-only file gives the available entropy, in bits. This will be a number in the range 0 to 4096.</p>
<dt><i>poolsize</i></p>
<dd>This file gives the size of the entropy pool. The semantics of this file vary across kernel versions:</p>
<dl>
<dd>
<dl>
<dt>Linux 2.4:</p>
<dd>This file gives the size of the entropy pool in <i>bytes</i>. Normally, this file will have the value 512, but it is writable, and can be changed to any value for which an algorithm is available. The choices are 32, 64, 128, 256, 512, 1024, or 2048.</p>
<dt>Linux 2.6 and later:</p>
<dd>This file is read-only, and gives the size of the entropy pool in <i>bits</i>. It contains the value 4096.</dl>
</dl>
<dt><i>read_wakeup_threshold</i></p>
<dd>This file contains the number of bits of entropy required for waking up processes that sleep waiting for entropy from <i>/dev/random</i>. The default is 64.</p>
<dt><i>write_wakeup_threshold</i></p>
<dd>This file contains the number of bits of entropy below which we wake up processes that do a <code><a href="/docs/linux/man/2-select/">select</a></code>(2) or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) for write access to <i>/dev/random</i>. These values can be changed by writing to the files.</p>
<dt><i>uuid</i> and <i>boot_id</i></p>
<dd>These read-only files contain random strings like 6fd5a44b-35f4-4ad4-a9b9-6b9be13e1fe9. The former is generated afresh for each read, the latter was generated once.</dl>
<h3><a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) interface</h3>
<p>The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests are defined on file descriptors connected to either <i>/dev/random</i> or <i>/dev/urandom</i>. All requests performed will interact with the input entropy pool impacting both <i>/dev/random</i> and <i>/dev/urandom</i>. The <code>CAP_SYS_ADMIN</code> capability is required for all requests except <code>RNDGETENTCNT</code>.</p>
<dl>
<dt><code>RNDGETENTCNT</code></p>
<dd>Retrieve the entropy count of the input pool, the contents will be the same as the <i>entropy_avail</i> file under proc. The result will be stored in the int pointed to by the argument.</p>
<dt><code>RNDADDTOENTCNT</code></p>
<dd>Increment or decrement the entropy count of the input pool by the value pointed to by the argument.</p>
<dt><code>RNDGETPOOL</code></p>
<dd>Removed in Linux 2.6.9.</p>
<dt><code>RNDADDENTROPY</code></p>
<dd>Add some additional entropy to the input pool, incrementing the entropy count. This differs from writing to <i>/dev/random</i> or <i>/dev/urandom</i>, which only adds some data but does not increment the entropy count. The following structure is used:</p>
<dd>struct rand_pool_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;entropy_count;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;buf[0]; };</p>
<dd>Here <i>entropy_count</i> is the value added to (or subtracted from) the entropy count, and <i>buf</i> is the buffer of size <i>buf_size</i> which gets added to the entropy pool.</p>
<dt><code>RNDZAPENTCNT</code>, <code>RNDCLEARPOOL</code></p>
<dd>Zero the entropy count of all pools and add some system data (such as wall clock) to the pools.</dl>
<h2>Files</h2>
<p><i>/dev/random</i><br />
 <i>/dev/urandom</i></p>
<h2>Notes</h2>
<p>For an overview and comparison of the various interfaces that can be used to obtain randomness, see <code><a href="/docs/linux/man/7-random/">random</a></code>(7).</p>
<h2>Bugs</h2>
<p>During early boot time, reads from <i>/dev/urandom</i> may return data prior to the entropy pool being initialized.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2), <code><a href="/docs/linux/man/7-random/">random</a></code>(7) </p>
<p> RFC 1750, &quot;Randomness Recommendations for Security&quot;</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
