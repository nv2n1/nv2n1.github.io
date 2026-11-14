---
title: "guestfs-internals(1)"
name: "guestfs-internals"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-internals/"
description: "guestfs-internals – architecture and internals of libguestfs"
---

<h2 class="name">NAME</h2>
<p> guestfs-internals &#8211; architecture and internals of libguestfs </p>
<h2>DESCRIPTION</h2>
<p> This manual page is for hackers who want to understand how libguestfs works internally. This is just a description of how libguestfs works now, and it may change at any time in the future.</p>
<h2>ARCHITECTURE</h2>
<p> Internally, libguestfs is implemented by running an appliance (a special type of small virtual machine) using <code><a href="/docs/linux/man/1-qemu/">qemu</a></code>(1). Qemu runs as a child process of the main program. </p>
<pre>
 ┌───────────────────┐
 │ main program      │
 │                   │
 │                   │           child process / appliance
 │                   │          ┌──────────────────────────┐
 │                   │          │ qemu                     │
 ├───────────────────┤   RPC    │      ┌─────────────────┐ │
 │ libguestfs  &#x25c0;╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍&#x25b6; guestfsd        │ │
 │                   │          │      ├─────────────────┤ │
 └───────────────────┘          │      │ Linux kernel    │ │
                                │      └────────┬────────┘ │
                                └───────────────│──────────┘
                                                │
                                                │ virtio-scsi
                                         ┌──────┴──────┐
                                         │  Device or  │
                                         │  disk image │
                                         └─────────────┘
</pre>
<p> The library, linked to the main program, creates the child process and hence the appliance in the &#8220;guestfs_launch&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) function. </p>
<p> Inside the appliance is a Linux kernel and a complete stack of userspace tools (such as <font SIZE="-1">LVM</font> and ext2 programs) and a small controlling daemon called &#8220;guestfsd&#8221;. The library talks to &#8220;guestfsd&#8221; using remote procedure calls (<font SIZE="-1">RPC</font>). There is a mostly one-to-one correspondence between libguestfs <font SIZE="-1">API</font> calls and <font SIZE="-1">RPC</font> calls to the daemon. Lastly the disk image(s) are attached to the qemu process which translates device access by the appliance’s Linux kernel into accesses to the image. </p>
<p> A common misunderstanding is that the appliance &#8220;is&#8221; the virtual machine. Although the disk image you are attached to might also be used by some virtual machine, libguestfs doesn&#8217;t know or care about this. (But you will care if both libguestfs’s qemu process and your virtual machine are trying to update the disk image at the same time, since these usually results in massive disk corruption).</p>
<h2>STATE MACHINE</h2>
<p> libguestfs uses a state machine to model the child process: </p>
<pre>
                         |
          guestfs_create / guestfs_create_flags
                         |
                         |
                     ____V_____
                    /          \
                    |  CONFIG  |
                    \__________/
                       ^   ^  \
                       |    \  \ guestfs_launch
                       |    _\__V______
                       |   /           \
                       |   | LAUNCHING |
                       |   \___________/
                       |       /
                       |  guestfs_launch
                       |     /
                     __|____V
                    /        \
                    | READY  |
                    \________/
</pre>
<p> The normal transitions are (1) <font SIZE="-1">CONFIG</font> (when the handle is created, but there is no child process), (2) <font SIZE="-1">LAUNCHING</font> (when the child process is booting up), (3) <font SIZE="-1">READY</font> meaning the appliance is up, actions can be issued to, and carried out by, the child process. </p>
<p> The guest may be killed by &#8220;guestfs_kill_subprocess&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), or may die asynchronously at any time (eg. due to some internal error), and that causes the state to transition back to <font SIZE="-1">CONFIG.</font> </p>
<p> Configuration commands for qemu such as &#8220;guestfs_set_path&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) can only be issued when in the <font SIZE="-1">CONFIG</font> state. </p>
<p> The <font SIZE="-1">API</font> offers one call that goes from <font SIZE="-1">CONFIG</font> through <font SIZE="-1">LAUNCHING</font> to <font SIZE="-1">READY.</font> &#8220;guestfs_launch&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) blocks until the child process is <font SIZE="-1">READY</font> to accept commands (or until some failure or timeout). &#8220;guestfs_launch&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) internally moves the state from <font SIZE="-1">CONFIG</font> to <font SIZE="-1">LAUNCHING</font> while it is running. </p>
<p> <font SIZE="-1">API</font> actions such as &#8220;guestfs_mount&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) can only be issued when in the <font SIZE="-1">READY</font> state. These <font SIZE="-1">API</font> calls block waiting for the command to be carried out. There are no non-blocking versions, and no way to issue more than one command per handle at the same time. </p>
<p> Finally, the child process sends asynchronous messages back to the main program, such as kernel log messages. You can register a callback to receive these messages.</p>
<h2>INTERNALS</h2>
<h3><font SIZE="-1">APPLIANCE BOOT PROCESS</font></h3>
<p> This process has evolved and continues to evolve. The description here corresponds only to the current version of libguestfs and is provided for information only. </p>
<p> In order to follow the stages involved below, enable libguestfs debugging (set the environment variable <tt>&quot;LIBGUESTFS_DEBUG=1&quot;</tt>).</p>
<dl>
<dt>Create the appliance</p>
<dd> <tt>&quot;supermin --build&quot;</tt> is invoked to create the kernel, a small initrd and the appliance. </p>
<p> The appliance is cached in <i>/var/tmp/.guestfs-&lt;</i><font SIZE="-1"><i>UID</i></font><i>&gt;</i> (or in another directory if <tt>&quot;LIBGUESTFS_CACHEDIR&quot;</tt> or <tt>&quot;TMPDIR&quot;</tt> are set). </p>
<p> For a complete description of how the appliance is created and cached, read the <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1) man page.</p>
<dt>Start qemu and boot the kernel</p>
<dd> qemu is invoked to boot the kernel.</p>
<dt>Run the initrd</p>
<dd> <tt>&quot;supermin --build&quot;</tt> builds a small initrd. The initrd is not the appliance. The purpose of the initrd is to load enough kernel modules in order that the appliance itself can be mounted and started. </p>
<p> The initrd is a cpio archive called <i>/var/tmp/.guestfs-&lt;</i><font SIZE="-1"><i>UID</i></font><i>&gt;/appliance.d/initrd</i>. </p>
<p> When the initrd has started you will see messages showing that kernel modules are being loaded, similar to this: </p>
<pre>
 supermin: ext2 mini initrd starting up
 supermin: mounting /sys
 supermin: internal insmod libcrc32c.ko
 supermin: internal insmod crc32c-intel.ko
</pre>
<dt>Find and mount the appliance device</p>
<dd> The appliance is a sparse file containing an ext2 filesystem which contains a familiar (although reduced in size) Linux operating system. It would normally be called <i>/var/tmp/.guestfs-&lt;</i><font SIZE="-1"><i>UID</i></font><i>&gt;/appliance.d/root</i>. </p>
<p> The regular disks being inspected by libguestfs are the first devices exposed by qemu (eg. as <i>/dev/vda</i>). </p>
<p> The last disk added to qemu is the appliance itself (eg. <i>/dev/vdb</i> if there was only one regular disk). </p>
<p> Thus the final job of the initrd is to locate the appliance disk, mount it, and switch root into the appliance, and run <i>/init</i> from the appliance. </p>
<p> If this works successfully you will see messages such as: </p>
<pre>
 supermin: picked /sys/block/vdb/dev as root device
 supermin: creating /dev/root as block special 252:16
 supermin: mounting new root on /root
 supermin: chroot
 Starting /init script ...
</pre>
<p> Note that <tt>&quot;Starting /init script ...&quot;</tt> indicates that the appliance&#8217;s init script is now running.</p>
<dt>Initialize the appliance</p>
<dd> The appliance itself now initializes itself. This involves starting certain processes like <tt>&quot;udev&quot;</tt>, possibly printing some debug information, and finally running the daemon (<tt>&quot;guestfsd&quot;</tt>).</p>
<dt>The daemon</p>
<dd> Finally the daemon (<tt>&quot;guestfsd&quot;</tt>) runs inside the appliance. If it runs you should see: </p>
<pre>
 verbose daemon enabled
</pre>
<p> The daemon expects to see a named virtio-serial port exposed by qemu and connected on the other end to the library. </p>
<p> The daemon connects to this port (and hence to the library) and sends a four byte message <tt>&quot;GUESTFS_LAUNCH_FLAG&quot;</tt>, which initiates the communication protocol (see below).</dl>
<h3><font SIZE="-1">COMMUNICATION PROTOCOL</font></h3>
<p> Don’t rely on using this protocol directly. This section documents how it currently works, but it may change at any time. </p>
<p> The protocol used to talk between the library and the daemon running inside the qemu virtual machine is a simple <font SIZE="-1">RPC</font> mechanism built on top of <font SIZE="-1">XDR</font> (<font SIZE="-1">RFC 1014, RFC 1832, RFC 4506</font>). </p>
<p> The detailed format of structures is in <i>common/protocol/guestfs_protocol.x</i> (note: this file is automatically generated). </p>
<p> There are two broad cases, ordinary functions that don’t have any <tt>&quot;FileIn&quot;</tt> and <tt>&quot;FileOut&quot;</tt> parameters, which are handled with very simple request/reply messages. Then there are functions that have any <tt>&quot;FileIn&quot;</tt> or <tt>&quot;FileOut&quot;</tt> parameters, which use the same request and reply messages, but they may also be followed by files sent using a chunked encoding. </p>
<p> <i></i><font SIZE="-1"><i>ORDINARY FUNCTIONS</i></font><i> (</i><font SIZE="-1"><i>NO FILEIN/FILEOUT PARAMS</i></font><i>)</i> </p>
<p> For ordinary functions, the request message is: </p>
<pre>
 total length (header + arguments,
      but not including the length word itself)
 struct guestfs_message_header (encoded as XDR)
 struct guestfs_&lt;foo&gt;_args (encoded as XDR)
</pre>
<p> The total length field allows the daemon to allocate a fixed size buffer into which it slurps the rest of the message. As a result, the total length is limited to <tt>&quot;GUESTFS_MESSAGE_MAX&quot;</tt> bytes (currently 4MB), which means the effective size of any request is limited to somewhere under this size. </p>
<p> Note also that many functions don’t take any arguments, in which case the <tt>&quot;guestfs_</tt>foo<tt>_args&quot;</tt> is completely omitted. </p>
<p> The header contains the procedure number (<tt>&quot;guestfs_proc&quot;</tt>) which is how the receiver knows what type of args structure to expect, or none at all. </p>
<p> For functions that take optional arguments, the optional arguments are encoded in the <tt>&quot;guestfs_</tt>foo<tt>_args&quot;</tt> structure in the same way as ordinary arguments. A bitmask in the header indicates which optional arguments are meaningful. The bitmask is also checked to see if it contains bits set which the daemon does not know about (eg. if more optional arguments were added in a later version of the library), and this causes the call to be rejected. </p>
<p> The reply message for ordinary functions is: </p>
<pre>
 total length (header + ret,
      but not including the length word itself)
 struct guestfs_message_header (encoded as XDR)
 struct guestfs_&lt;foo&gt;_ret (encoded as XDR)
</pre>
<p> As above the <tt>&quot;guestfs_</tt>foo<tt>_ret&quot;</tt> structure may be completely omitted for functions that return no formal return values. </p>
<p> As above the total length of the reply is limited to <tt>&quot;GUESTFS_MESSAGE_MAX&quot;</tt>. </p>
<p> In the case of an error, a flag is set in the header, and the reply message is slightly changed: </p>
<pre>
 total length (header + error,
      but not including the length word itself)
 struct guestfs_message_header (encoded as XDR)
 struct guestfs_message_error (encoded as XDR)
</pre>
<p> The <tt>&quot;guestfs_message_error&quot;</tt> structure contains the error message as a string. </p>
<p> <i></i><font SIZE="-1"><i>FUNCTIONS THAT HAVE FILEIN PARAMETERS</i></font><i></i> </p>
<p> A <tt>&quot;FileIn&quot;</tt> parameter indicates that we transfer a file <i>into</i> the guest. The normal request message is sent (see above). However this is followed by a sequence of file chunks. </p>
<pre><code>
 total length (header + arguments,
      but not including the length word itself,
      and not including the chunks)
 struct guestfs_message_header (encoded as XDR)
 struct guestfs_&lt;foo&gt;_args (encoded as XDR)
 sequence of chunks for FileIn param #0
 sequence of chunks for FileIn param #1 etc.
</code></pre>
<p> The &#8220;sequence of chunks&#8221; is: </p>
<p>length of chunk(not including length word itself) struct guestfs_chunk(encoded as XDR)<br />
    length of chunk<br />
    struct guestfs_chunk(encoded as XDR)&#8230; length of chunk<br />
    struct guestfs_chunk(with data.data_len == 0)</p>
<p> The final chunk has the <tt>&quot;data_len&quot;</tt> field set to zero. Additionally a flag is set in the final chunk to indicate either successful completion or early cancellation. </p>
<p> At time of writing there are no functions that have more than one FileIn parameter. However this is (theoretically) supported, by sending the sequence of chunks for each FileIn parameter one after another (from left to right). </p>
<p> Both the library (sender) <i>and</i> the daemon (receiver) may cancel the transfer. The library does this by sending a chunk with a special flag set to indicate cancellation. When the daemon sees this, it cancels the whole <font SIZE="-1">RPC,</font> does <i>not</i> send any reply, and goes back to reading the next request. </p>
<p> The daemon may also cancel. It does this by writing a special word <tt>&quot;GUESTFS_CANCEL_FLAG&quot;</tt> to the socket. The library listens for this during the transfer, and if it gets it, it will cancel the transfer (it sends a cancel chunk). The special word is chosen so that even if cancellation happens right at the end of the transfer (after the library has finished writing and has started listening for the reply), the &#8220;spurious&#8221; cancel flag will not be confused with the reply message. </p>
<p> This protocol allows the transfer of arbitrary sized files (no 32 bit limit), and also files where the size is not known in advance (eg. from pipes or sockets). However the chunks are rather small (<tt>&quot;GUESTFS_MAX_CHUNK_SIZE&quot;</tt>), so that neither the library nor the daemon need to keep much in memory. </p>
<p> <i></i><font SIZE="-1"><i>FUNCTIONS THAT HAVE FILEOUT PARAMETERS</i></font><i></i> </p>
<p> The protocol for FileOut parameters is exactly the same as for FileIn parameters, but with the roles of daemon and library reversed. </p>
<pre><code>
 total length (header + ret,
      but not including the length word itself,
      and not including the chunks)
 struct guestfs_message_header (encoded as XDR)
 struct guestfs_&lt;foo&gt;_ret (encoded as XDR)
 sequence of chunks for FileOut param #0
 sequence of chunks for FileOut param #1 etc.
</code></pre>
<p> <i></i><font SIZE="-1"><i>INITIAL MESSAGE</i></font><i></i> </p>
<p> When the daemon launches it sends an initial word (<tt>&quot;GUESTFS_LAUNCH_FLAG&quot;</tt>) which indicates that the guest and daemon is alive. This is what &#8220;guestfs_launch&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) waits for. </p>
<p> <i></i><font SIZE="-1"><i>PROGRESS NOTIFICATION MESSAGES</i></font><i></i> </p>
<p> The daemon may send progress notification messages at any time. These are distinguished by the normal length word being replaced by <tt>&quot;GUESTFS_PROGRESS_FLAG&quot;</tt>, followed by a fixed size progress message. </p>
<p> The library turns them into progress callbacks (see &#8220;<font SIZE="-1">GUESTFS_EVENT_PROGRESS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)) if there is a callback registered, or discards them if not. </p>
<p> The daemon self-limits the frequency of progress messages it sends (see <tt>&quot;daemon/proto.c:notify_progress&quot;</tt>). Not all calls generate progress messages.</p>
<h3><font SIZE="-1">FIXED APPLIANCE</font></h3>
<p> When libguestfs (or libguestfs tools) are run, they search a path looking for an appliance. The path is built into libguestfs, or can be set using the <tt>&quot;LIBGUESTFS_PATH&quot;</tt> environment variable. </p>
<p> Normally a supermin appliance is located on this path (see &#8220;<font SIZE="-1">SUPERMIN APPLIANCE&#8221;</font> in <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1)). libguestfs reconstructs this into a full appliance by running <tt>&quot;supermin --build&quot;</tt>. </p>
<p> However, a simpler &#8220;fixed appliance&#8221; can also be used. libguestfs detects this by looking for a directory on the path containing all the following files:</p>
<dl>
<dt>&bull;</p>
<dd> <i>kernel</i></p>
<dt>&bull;</p>
<dd> <i>initrd</i></p>
<dt>&bull;</p>
<dd> <i>root</i></p>
<dt>&bull;</p>
<dd> <i></i><font SIZE="-1"><i>README</i></font><i>.fixed</i> (note that it <code>must</code> be present as well)</dl>
<p> If the fixed appliance is found, libguestfs skips supermin entirely and just runs the virtual machine (using qemu or the current backend, see &#8220;<font SIZE="-1">BACKEND&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)) with the kernel, initrd and root disk from the fixed appliance. </p>
<p> Thus the fixed appliance can be used when a platform or a Linux distribution does not support supermin. You build the fixed appliance on a platform that does support supermin using <code><a href="/docs/linux/man/1-libguestfs-make-fixed-appliance/">libguestfs-make-fixed-appliance</a></code>(1), copy it over, and use that to run libguestfs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1), <code><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></code>(3), <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1), <code><a href="/docs/linux/man/1-libguestfs-make-fixed-appliance/">libguestfs-make-fixed-appliance</a></code>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">AUTHORS</a></p>
<dd>
<dt><a href="#lbAL">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAM">LICENSE</a></p>
<dd>
<dt><a href="#lbAN">BUGS</a></p>
<dd></dl>
