---
title: "bpf(2)"
name: "bpf"
section: "2"
letter: "b"
url: "/docs/linux/man/2-bpf/"
description: "bpf – perform a command on an extended BPF map or program"
---

<h2 class="name">NAME</h2>
<p> bpf &#8211; perform a command on an extended BPF map or program </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/bpf.h&gt;
int bpf(int cmd, union bpf_attr *attr, unsigned int size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bpf</code>() system call performs a range of operations related to extended Berkeley Packet Filters. Extended BPF (or eBPF) is similar to the original (&quot;classic&quot;) BPF (cBPF) used to filter network packets. For both cBPF and eBPF programs, the kernel statically analyzes the programs before loading them, in order to ensure that they cannot harm the running system. </p>
<p> eBPF extends cBPF in multiple ways, including the ability to call a fixed set of in-kernel helper functions (via the <code>BPF_CALL</code> opcode extension provided by eBPF) and access shared data structures such as eBPF maps.</p>
<h3>Extended BPF Design/Architecture</h3>
<p> eBPF maps are a generic data structure for storage of different data types. Data types are generally treated as binary blobs, so a user just specifies the size of the key and the size of the value at map-creation time. In other words, a key/value for a given map can have an arbitrary structure. </p>
<p> A user process can create multiple maps (with key/value-pairs being opaque bytes of data) and access them via file descriptors. Different eBPF programs can access the same maps in parallel. It&#8217;s up to the user process and eBPF program to decide what they store inside maps. </p>
<p> There&#8217;s one special map type, called a program array. This type of map stores file descriptors referring to other eBPF programs. When a lookup in the map is performed, the program flow is redirected in-place to the beginning of another eBPF program and does not return back to the calling program. The level of nesting has a fixed limit of 32, so that infinite loops cannot be crafted. At run time, the program file descriptors stored in the map can be modified, so program functionality can be altered based on specific requirements. All programs referred to in a program-array map must have been previously loaded into the kernel via <code>bpf</code>(). If a map lookup fails, the current program continues its execution. See <code>BPF_MAP_TYPE_PROG_ARRAY</code> below for further details. </p>
<p> Generally, eBPF programs are loaded by the user process and automatically unloaded when the process exits. In some cases, for example, <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8), the program will continue to stay alive inside the kernel even after the process that loaded the program exits. In that case, the tc subsystem holds a reference to the eBPF program after the file descriptor has been closed by the user-space program. Thus, whether a specific program continues to live inside the kernel depends on how it is further attached to a given kernel subsystem after it was loaded via <code>bpf</code>(). </p>
<p> Each eBPF program is a set of instructions that is safe to run until its completion. An in-kernel verifier statically determines that the eBPF program terminates and is safe to execute. During verification, the kernel increments reference counts for each of the maps that the eBPF program uses, so that the attached maps can&#8217;t be removed until the program is unloaded. </p>
<p> eBPF programs can be attached to different events. These events can be the arrival of network packets, tracing events, classification events by network queueing disciplines (for eBPF programs attached to a <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) classifier), and other types that may be added in the future. A new event triggers execution of the eBPF program, which may store information about the event in eBPF maps. Beyond storing data, eBPF programs may call a fixed set of in-kernel helper functions. </p>
<p> The same eBPF program can be attached to multiple events and different eBPF programs can access the same map: </p>
<p> tracing tracing tracing packet packet packet event A event B event C on eth0 on eth1 on eth2<br />
&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ha<br />
&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;&#8211;&gt;&nbsp;tracing&nbsp;&lt;&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tracing&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;socket&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tc ingress&nbsp;<wbr>&nbsp;<wbr>&nbsp;tc egress<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classifier&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&#8212;&nbsp;<wbr>&nbsp;&#8212;&#8211;|&nbsp;<wbr>&nbsp;|&#8212;&#8212;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;map_1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;| map_4 |&#8211;</p>
<h3>Arguments</h3>
<p> The operation to be performed by the <code>bpf</code>() system call is determined by the <i>cmd</i> argument. Each operation takes an accompanying argument, provided via <i>attr</i>, which is a pointer to a union of type <i>bpf_attr</i> (see below). The <i>size</i> argument is the size of the union pointed to by <i>attr</i>. </p>
<p> The value provided in <i>cmd</i> is one of the following:</p>
<dl>
<dt><code>BPF_MAP_CREATE</code></p>
<dd> Create a map and return a file descriptor that refers to the map. The close-on-exec file descriptor flag (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) is automatically enabled for the new file descriptor.</p>
<dt><code>BPF_MAP_LOOKUP_ELEM</code></p>
<dd> Look up an element by key in a specified map and return its value.</p>
<dt><code>BPF_MAP_UPDATE_ELEM</code></p>
<dd> Create or update an element (key/value pair) in a specified map.</p>
<dt><code>BPF_MAP_DELETE_ELEM</code></p>
<dd> Look up and delete an element by key in a specified map.</p>
<dt><code>BPF_MAP_GET_NEXT_KEY</code></p>
<dd> Look up an element by key in a specified map and return the key of the next element.</p>
<dt><code>BPF_PROG_LOAD</code></p>
<dd> Verify and load an eBPF program, returning a new file descriptor associated with the program. The close-on-exec file descriptor flag (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) is automatically enabled for the new file descriptor.</p>
<dt>
<dd> The <i>bpf_attr</i> union consists of various anonymous structures that are used by different <code>bpf</code>() commands:</dl>
<p> union bpf_attr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Used by BPF_MAP_CREATE&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;size of key in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_size;&nbsp;<wbr>&nbsp;/*&nbsp;size of value in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_entries;&nbsp;/*&nbsp;maximum number of entries<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in a map&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Used by BPF_MAP_*_ELEM and BPF_MAP_GET_NEXT_KEY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;commands&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 next_key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Used by BPF_PROG_LOAD&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;insn_cnt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 insns;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&#8216;const struct bpf_insn&nbsp;*&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 license;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&#8216;const char&nbsp;*&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;log_level;&nbsp;<wbr>&nbsp;/*&nbsp;verbosity level of verifier&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;log_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;size of user buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__aligned_u64 log_buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user supplied&nbsp;&#8216;char&nbsp;*&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;kern_version;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;checked when prog_type=kprobe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 4.1)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; } __attribute__((<a href="/docs/linux/man/8-aligned/">aligned</a>(8)));</p>
<h3>eBPF maps</h3>
<p> Maps are a generic data structure for storage of different types of data. They allow sharing of data between eBPF kernel programs, and also between kernel and user-space applications. </p>
<p> Each map type has the following attributes:</p>
<dl>
<dt>*</p>
<dd> type</p>
<dt>*</p>
<dd> maximum number of elements</p>
<dt>*</p>
<dd> key size in bytes</p>
<dt>*</p>
<dd> value size in bytes</dl>
<p> The following wrapper functions demonstrate how various <code>bpf</code>() commands can be used to access the maps. The functions use the <i>cmd</i> argument to invoke different operations.</p>
<dl>
<dt><code>BPF_MAP_CREATE</code></p>
<dd> The <code>BPF_MAP_CREATE</code> command creates a new map, returning a new file descriptor that refers to the map.</p>
<dt>
<dd> int bpf_create_map(enum bpf_map_type map_type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int key_size,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int value_size,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int max_entries) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.map_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;map_type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.key_size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;key_size,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.value_size&nbsp;<wbr>&nbsp;=&nbsp;value_size,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.max_entries&nbsp;=&nbsp;max_entries<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_MAP_CREATE,&nbsp;&amp;attr, sizeof(attr)); }</p>
<dt>
<dd> The new map has the type specified by <i>map_type</i>, and attributes as specified in <i>key_size</i>, <i>value_size</i>, and <i>max_entries</i>. On success, this operation returns a file descriptor. On error, -1 is returned and <i>errno</i> is set to <code>EINVAL</code>, <code>EPERM</code>, or <code>ENOMEM</code>.</p>
<dt>
<dd> The <i>key_size</i> and <i>value_size</i> attributes will be used by the verifier during program loading to check that the program is calling <code>bpf_map_*_elem</code>() helper functions with a correctly initialized <i>key</i> and to check that the program doesn&#8217;t access the map element <i>value</i> beyond the specified <i>value_size</i>. For example, when a map is created with a <i>key_size</i> of 8 and the eBPF program calls</p>
<dt>
<dd> bpf_map_lookup_elem(map_fd, fp &#8211; 4)</p>
<dt>
<dd> the program will be rejected, since the in-kernel helper function</p>
<dt>
<dd> bpf_map_lookup_elem(map_fd, void *key)</p>
<dt>
<dd> expects to read 8 bytes from the location pointed to by <i>key</i>, but the <i>fp &#8211; 4</i> (where <i>fp</i> is the top of the stack) starting address will cause out-of-bounds stack access.</p>
<dt>
<dd> Similarly, when a map is created with a <i>value_size</i> of 1 and the eBPF program contains</p>
<dt>
<dd> value = bpf_map_lookup_elem(&#8230;); *(u32 *) value = 1;</p>
<dt>
<dd> the program will be rejected, since it accesses the <i>value</i> pointer beyond the specified 1 byte <i>value_size</i> limit.</p>
<dt>
<dd> Currently, the following values are supported for <i>map_type</i>:</p>
<dt>
<dd> enum bpf_map_type {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_UNSPEC,&nbsp;<wbr>&nbsp;/*&nbsp;Reserve 0 as invalid map type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_HASH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_ARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_PROG_ARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_PERF_EVENT_ARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_PERCPU_HASH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_PERCPU_ARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_STACK_TRACE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_CGROUP_ARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_LRU_HASH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_LRU_PERCPU_HASH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_LPM_TRIE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_ARRAY_OF_MAPS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_HASH_OF_MAPS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_DEVMAP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_SOCKMAP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_CPUMAP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_XSKMAP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_SOCKHASH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_CGROUP_STORAGE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_REUSEPORT_SOCKARRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_QUEUE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MAP_TYPE_STACK,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See&nbsp;/usr/include/linux/bpf.h for the full list.&nbsp;*/ };</p>
<dt>
<dd> <i>map_type</i> selects one of the available map implementations in the kernel. For all map types, eBPF programs access maps with the same <code>bpf_map_lookup_elem</code>() and <code>bpf_map_update_elem</code>() helper functions. Further details of the various map types are given below.</p>
<dt><code>BPF_MAP_LOOKUP_ELEM</code></p>
<dd> The <code>BPF_MAP_LOOKUP_ELEM</code> command looks up an element with a given <i>key</i> in the map referred to by the file descriptor <i>fd</i>.</p>
<dt>
<dd> int bpf_lookup_elem(int fd, const void *key, void *value) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.map_fd&nbsp;=&nbsp;fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.value&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(value),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_MAP_LOOKUP_ELEM,&nbsp;&amp;attr, sizeof(attr)); }</p>
<dt>
<dd> If an element is found, the operation returns zero and stores the element&#8217;s value into <i>value</i>, which must point to a buffer of <i>value_size</i> bytes.</p>
<dt>
<dd> If no element is found, the operation returns -1 and sets <i>errno</i> to <code>ENOENT</code>.</p>
<dt><code>BPF_MAP_UPDATE_ELEM</code></p>
<dd> The <code>BPF_MAP_UPDATE_ELEM</code> command creates or updates an element with a given <i>key/value</i> in the map referred to by the file descriptor <i>fd</i>.</p>
<dt>
<dd> int bpf_update_elem(int fd, const void *key, const void *value,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t flags) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.map_fd&nbsp;=&nbsp;fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.value&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(value),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.flags&nbsp;<wbr>&nbsp;=&nbsp;flags,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_MAP_UPDATE_ELEM,&nbsp;&amp;attr, sizeof(attr)); }</p>
<dt>
<dd> The <i>flags</i> argument should be specified as one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>BPF_ANY</code></p>
<dd> Create a new element or update an existing element.</p>
<dt><code>BPF_NOEXIST</code></p>
<dd> Create a new element only if it did not exist.</p>
<dt><code>BPF_EXIST</code></p>
<dd> Update an existing element.</dl>
</dl>
<dt>
<dd> On success, the operation returns zero. On error, -1 is returned and <i>errno</i> is set to <code>EINVAL</code>, <code>EPERM</code>, <code>ENOMEM</code>, or <code>E2BIG</code>. <code>E2BIG</code> indicates that the number of elements in the map reached the <i>max_entries</i> limit specified at map creation time. <code>EEXIST</code> will be returned if <i>flags</i> specifies <code>BPF_NOEXIST</code> and the element with <i>key</i> already exists in the map. <code>ENOENT</code> will be returned if <i>flags</i> specifies <code>BPF_EXIST</code> and the element with <i>key</i> doesn&#8217;t exist in the map.</p>
<dt><code>BPF_MAP_DELETE_ELEM</code></p>
<dd> The <code>BPF_MAP_DELETE_ELEM</code> command deletes the element whose key is <i>key</i> from the map referred to by the file descriptor <i>fd</i>.</p>
<dt>
<dd> int bpf_delete_elem(int fd, const void *key) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.map_fd&nbsp;=&nbsp;fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_MAP_DELETE_ELEM,&nbsp;&amp;attr, sizeof(attr)); }</p>
<dt>
<dd> On success, zero is returned. If the element is not found, -1 is returned and <i>errno</i> is set to <code>ENOENT</code>.</p>
<dt><code>BPF_MAP_GET_NEXT_KEY</code></p>
<dd> The <code>BPF_MAP_GET_NEXT_KEY</code> command looks up an element by <i>key</i> in the map referred to by the file descriptor <i>fd</i> and sets the <i>next_key</i> pointer to the key of the next element.</p>
<dt>
<dd> int bpf_get_next_key(int fd, const void *key, void *next_key) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.map_fd&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.next_key&nbsp;=&nbsp;ptr_to_u64(next_key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_MAP_GET_NEXT_KEY,&nbsp;&amp;attr, sizeof(attr)); }</p>
<dt>
<dd> If <i>key</i> is found, the operation returns zero and sets the <i>next_key</i> pointer to the key of the next element. If <i>key</i> is not found, the operation returns zero and sets the <i>next_key</i> pointer to the key of the first element. If <i>key</i> is the last element, -1 is returned and <i>errno</i> is set to <code>ENOENT</code>. Other possible <i>errno</i> values are <code>ENOMEM</code>, <code>EFAULT</code>, <code>EPERM</code>, and <code>EINVAL</code>. This method can be used to iterate over all elements in the map.</p>
<dt><code>close(map_fd)</code></p>
<dd> Delete the map referred to by the file descriptor <i>map_fd</i>. When the user-space program that created a map exits, all maps will be deleted automatically (but see NOTES).</dl>
<h3>eBPF map types</h3>
<p> The following map types are supported:</p>
<dl>
<dt><code>BPF_MAP_TYPE_HASH</code></p>
<dd> Hash-table maps have the following characteristics:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Maps are created and destroyed by user-space programs. Both user-space and eBPF programs can perform lookup, update, and delete operations.</p>
<dt>*</p>
<dd> The kernel takes care of allocating and freeing key/value pairs.</p>
<dt>*</p>
<dd> The <code>map_update_elem</code>() helper will fail to insert new element when the <i>max_entries</i> limit is reached. (This ensures that eBPF programs cannot exhaust memory.)</p>
<dt>*</p>
<dd> <code>map_update_elem</code>() replaces existing elements atomically.</dl>
</dl>
<dt>
<dd> Hash-table maps are optimized for speed of lookup.</p>
<dt><code>BPF_MAP_TYPE_ARRAY</code></p>
<dd> Array maps have the following characteristics:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Optimized for fastest possible lookup. In the future the verifier/JIT compiler may recognize lookup() operations that employ a constant key and optimize it into constant pointer. It is possible to optimize a non-constant key into direct pointer arithmetic as well, since pointers and <i>value_size</i> are constant for the life of the eBPF program. In other words, <code>array_map_lookup_elem</code>() may be &#8216;inlined&#8217; by the verifier/JIT compiler while preserving concurrent access to this map from user space.</p>
<dt>*</p>
<dd> All array elements pre-allocated and zero initialized at init time</p>
<dt>*</p>
<dd> The key is an array index, and must be exactly four bytes.</p>
<dt>*</p>
<dd> <code>map_delete_elem</code>() fails with the error <code>EINVAL</code>, since elements cannot be deleted.</p>
<dt>*</p>
<dd> <code>map_update_elem</code>() replaces elements in a <code>nonatomic</code> fashion; for atomic updates, a hash-table map should be used instead. There is however one special case that can also be used with arrays: the atomic built-in <code>__sync_fetch_and_add()</code> can be used on 32 and 64 bit atomic counters. For example, it can be applied on the whole value itself if it represents a single counter, or in case of a structure containing multiple counters, it could be used on individual counters. This is quite often useful for aggregation and accounting of events.</dl>
</dl>
<dt>
<dd> Among the uses for array maps are the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> As &quot;global&quot; eBPF variables: an array of 1 element whose key is (index) 0 and where the value is a collection of &#8216;global&#8217; variables which eBPF programs can use to keep state between events.</p>
<dt>*</p>
<dd> Aggregation of tracing events into a fixed set of buckets.</p>
<dt>*</p>
<dd> Accounting of networking events, for example, number of packets and packet sizes.</dl>
</dl>
<dt><code>BPF_MAP_TYPE_PROG_ARRAY</code> (since Linux 4.2)</p>
<dd> A program array map is a special kind of array map whose map values contain only file descriptors referring to other eBPF programs. Thus, both the <i>key_size</i> and <i>value_size</i> must be exactly four bytes. This map is used in conjunction with the <code>bpf_tail_call</code>() helper.</p>
<dt>
<dd> This means that an eBPF program with a program array map attached to it can call from kernel side into</p>
<dt>
<dd> void bpf_tail_call(void *context, void *prog_map,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int index);</p>
<dt>
<dd> and therefore replace its own program flow with the one from the program at the given program array slot, if present. This can be regarded as kind of a jump table to a different eBPF program. The invoked program will then reuse the same stack. When a jump into the new program has been performed, it won&#8217;t return to the old program anymore.</p>
<dt>
<dd> If no eBPF program is found at the given index of the program array (because the map slot doesn&#8217;t contain a valid program file descriptor, the specified lookup index/key is out of bounds, or the limit of 32 nested calls has been exceed), execution continues with the current eBPF program. This can be used as a fall-through for default cases.</p>
<dt>
<dd> A program array map is useful, for example, in tracing or networking, to handle individual system calls or protocols in their own subprograms and use their identifiers as an individual map index. This approach may result in performance benefits, and also makes it possible to overcome the maximum instruction limit of a single eBPF program. In dynamic environments, a user-space daemon might atomically replace individual subprograms at run-time with newer versions to alter overall program behavior, for instance, if global policies change.</dl>
<h3>eBPF programs</h3>
<p> The <code>BPF_PROG_LOAD</code> command is used to load an eBPF program into the kernel. The return value for this command is a new file descriptor associated with this eBPF program. </p>
<p> char bpf_log_buf[LOG_BUF_SIZE]; </p>
<p> int bpf_prog_load(enum bpf_prog_type type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct bpf_insn&nbsp;*insns, int insn_cnt,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;*license) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union bpf_attr attr&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.prog_type&nbsp;=&nbsp;type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.insns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(insns),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.insn_cnt&nbsp;<wbr>&nbsp;=&nbsp;insn_cnt,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.license&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(license),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.log_buf&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;ptr_to_u64(bpf_log_buf),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.log_size&nbsp;<wbr>&nbsp;=&nbsp;LOG_BUF_SIZE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.log_level&nbsp;=&nbsp;1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return bpf(BPF_PROG_LOAD,&nbsp;&amp;attr, sizeof(attr)); } </p>
<p> <i>prog_type</i> is one of the available program types:</p>
<dl>
<dt>
<dd> enum bpf_prog_type {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_UNSPEC,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Reserve 0 as invalid<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;program type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SOCKET_FILTER,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_KPROBE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SCHED_CLS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SCHED_ACT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_TRACEPOINT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_XDP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_PERF_EVENT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_CGROUP_SKB,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_CGROUP_SOCK,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_LWT_IN,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_LWT_OUT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_LWT_XMIT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SOCK_OPS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SK_SKB,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_CGROUP_DEVICE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SK_MSG,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_RAW_TRACEPOINT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_CGROUP_SOCK_ADDR,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_LWT_SEG6LOCAL,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_LIRC_MODE2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_SK_REUSEPORT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_PROG_TYPE_FLOW_DISSECTOR,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See&nbsp;/usr/include/linux/bpf.h for the full list.&nbsp;*/ };</dl>
<p> For further details of eBPF program types, see below. </p>
<p> The remaining fields of <i>bpf_attr</i> are set as follows:</p>
<dl>
<dt>*</p>
<dd> <i>insns</i> is an array of <i>struct bpf_insn</i> instructions.</p>
<dt>*</p>
<dd> <i>insn_cnt</i> is the number of instructions in the program referred to by <i>insns</i>.</p>
<dt>*</p>
<dd> <i>license</i> is a license string, which must be GPL compatible to call helper functions marked <i>gpl_only</i>. (The licensing rules are the same as for kernel modules, so that also dual licenses, such as &quot;Dual BSD/GPL&quot;, may be used.)</p>
<dt>*</p>
<dd> <i>log_buf</i> is a pointer to a caller-allocated buffer in which the in-kernel verifier can store the verification log. This log is a multi-line string that can be checked by the program author in order to understand how the verifier came to the conclusion that the eBPF program is unsafe. The format of the output can change at any time as the verifier evolves.</p>
<dt>*</p>
<dd> <i>log_size</i> size of the buffer pointed to by <i>log_buf</i>. If the size of the buffer is not large enough to store all verifier messages, -1 is returned and <i>errno</i> is set to <code>ENOSPC</code>.</p>
<dt>*</p>
<dd> <i>log_level</i> verbosity level of the verifier. A value of zero means that the verifier will not provide a log; in this case, <i>log_buf</i> must be a NULL pointer, and <i>log_size</i> must be zero.</dl>
<p> Applying <code><a href="/docs/linux/man/2-close/">close</a></code>(2) to the file descriptor returned by <code>BPF_PROG_LOAD</code> will unload the eBPF program (but see NOTES). </p>
<p> Maps are accessible from eBPF programs and are used to exchange data between eBPF programs and between eBPF programs and user-space programs. For example, eBPF programs can process various events (like kprobe, packets) and store their data into a map, and user-space programs can then fetch data from the map. Conversely, user-space programs can use a map as a configuration mechanism, populating the map with values checked by the eBPF program, which then modifies its behavior on the fly according to those values.</p>
<h3>eBPF program types</h3>
<p> The eBPF program type (<i>prog_type</i>) determines the subset of kernel helper functions that the program may call. The program type also determines the program input (context)&#8212;the format of <i>struct bpf_context</i> (which is the data blob passed into the eBPF program as the first argument). </p>
<p> For example, a tracing program does not have the exact same subset of helper functions as a socket filter program (though they may have some helpers in common). Similarly, the input (context) for a tracing program is a set of register values, while for a socket filter it is a network packet. </p>
<p> The set of functions available to eBPF programs of a given type may increase in the future. </p>
<p> The following program types are supported:</p>
<dl>
<dt><code>BPF_PROG_TYPE_SOCKET_FILTER</code> (since Linux 3.19)</p>
<dd> Currently, the set of functions for <code>BPF_PROG_TYPE_SOCKET_FILTER</code> is:</p>
<dt>
<dd> bpf_map_lookup_elem(map_fd, void *key)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;look up key in a map_fd&nbsp;*/ bpf_map_update_elem(map_fd, void *key, void *value)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;update key/value&nbsp;*/ bpf_map_delete_elem(map_fd, void *key)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;delete key in a map_fd&nbsp;*/</p>
<dt>
<dd> The <i>bpf_context</i> argument is a pointer to a <i>struct __sk_buff</i>.</p>
<dt><code>BPF_PROG_TYPE_KPROBE</code> (since Linux 4.1)</p>
<dd> [To be documented]</p>
<dt><code>BPF_PROG_TYPE_SCHED_CLS</code> (since Linux 4.1)</p>
<dd> [To be documented]</p>
<dt><code>BPF_PROG_TYPE_SCHED_ACT</code> (since Linux 4.1)</p>
<dd> [To be documented]</dl>
<h3>Events</h3>
<p> Once a program is loaded, it can be attached to an event. Various kernel subsystems have different ways to do so. </p>
<p> Since Linux 3.19, the following call will attach the program <i>prog_fd</i> to the socket <i>sockfd</i>, which was created by an earlier call to <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2): </p>
<p> setsockopt(sockfd, SOL_SOCKET, SO_ATTACH_BPF,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;prog_fd, sizeof(prog_fd)); </p>
<p> Since Linux 4.1, the following call may be used to attach the eBPF program referred to by the file descriptor <i>prog_fd</i> to a perf event file descriptor, <i>event_fd</i>, that was created by a previous call to <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2): </p>
<p> ioctl(event_fd, PERF_EVENT_IOC_SET_BPF, prog_fd);</p>
<h2>RETURN VALUE</h2>
<p> For a successful call, the return value depends on the operation:</p>
<dl>
<dt><code>BPF_MAP_CREATE</code></p>
<dd> The new file descriptor associated with the eBPF map.</p>
<dt><code>BPF_PROG_LOAD</code></p>
<dd> The new file descriptor associated with the eBPF program.</p>
<dt>All other commands</p>
<dd> Zero.</dl>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>E2BIG</code></p>
<dd> The eBPF program is too large or a map reached the <i>max_entries</i> limit (maximum number of elements).</p>
<dt><code>EACCES</code></p>
<dd> For <code>BPF_PROG_LOAD</code>, even though all program instructions are valid, the program has been rejected because it was deemed unsafe. This may be because it may have accessed a disallowed memory region or an uninitialized stack/register or because the function constraints don&#8217;t match the actual types or because there was a misaligned memory access. In this case, it is recommended to call <code>bpf</code>() again with <i>log_level = 1</i> and examine <i>log_buf</i> for the specific reason provided by the verifier.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not an open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> One of the pointers (<i>key</i> or <i>value</i> or <i>log_buf</i> or <i>insns</i>) is outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>cmd</i> is not recognized by this kernel.</p>
<dt><code>EINVAL</code></p>
<dd> For <code>BPF_MAP_CREATE</code>, either <i>map_type</i> or attributes are invalid.</p>
<dt><code>EINVAL</code></p>
<dd> For <code>BPF_MAP_*_ELEM</code> commands, some of the fields of <i>union bpf_attr</i> that are not used by this command are not set to zero.</p>
<dt><code>EINVAL</code></p>
<dd> For <code>BPF_PROG_LOAD</code>, indicates an attempt to load an invalid program. eBPF programs can be deemed invalid due to unrecognized instructions, the use of reserved fields, jumps out of range, infinite loops or calls of unknown functions.</p>
<dt><code>ENOENT</code></p>
<dd> For <code>BPF_MAP_LOOKUP_ELEM</code> or <code>BPF_MAP_DELETE_ELEM</code>, indicates that the element with the given <i>key</i> was not found.</p>
<dt><code>ENOMEM</code></p>
<dd> Cannot allocate sufficient memory.</p>
<dt><code>EPERM</code></p>
<dd> The call was made without sufficient privilege (without the <code>CAP_SYS_ADMIN</code> capability).</dl>
<h2>VERSIONS</h2>
<p> The <code>bpf</code>() system call first appeared in Linux 3.18.</p>
<h2>CONFORMING TO</h2>
<p> The <code>bpf</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Prior to Linux 4.4, all <code>bpf</code>() commands require the caller to have the <code>CAP_SYS_ADMIN</code> capability. From Linux 4.4 onwards, an unprivileged user may create limited programs of type <code>BPF_PROG_TYPE_SOCKET_FILTER</code> and associated maps. However they may not store kernel pointers within the maps and are presently limited to the following helper functions:</p>
<dl>
<dt>*</p>
<dd> get_random</p>
<dt>*</p>
<dd> get_smp_processor_id</p>
<dt>*</p>
<dd> tail_call</p>
<dt>*</p>
<dd> ktime_get_ns</dl>
<p> Unprivileged access may be blocked by writing the value 1 to the file <i>/proc/sys/kernel/unprivileged_bpf_disabled</i>. </p>
<p> eBPF objects (maps and programs) can be shared between processes. For example, after <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child inherits file descriptors referring to the same eBPF objects. In addition, file descriptors referring to eBPF objects can be transferred over UNIX domain sockets. File descriptors referring to eBPF objects can be duplicated in the usual way, using <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) and similar calls. An eBPF object is deallocated only after all file descriptors referring to the object have been closed. </p>
<p> eBPF programs can be written in a restricted C that is compiled (using the <code>clang</code> compiler) into eBPF bytecode. Various features are omitted from this restricted C, such as loops, global variables, variadic functions, floating-point numbers, and passing structures as function arguments. Some examples can be found in the <i>samples/bpf/*_kern.c</i> files in the kernel source tree. </p>
<p> The kernel contains a just-in-time (JIT) compiler that translates eBPF bytecode into native machine code for better performance. In kernels before Linux 4.15, the JIT compiler is disabled by default, but its operation can be controlled by writing one of the following integer strings to the file <i>/proc/sys/net/core/bpf_jit_enable</i>:</p>
<dl>
<dt>0</p>
<dd> Disable JIT compilation (default).</p>
<dt>1</p>
<dd> Normal compilation.</p>
<dt>2</p>
<dd> Debugging mode. The generated opcodes are dumped in hexadecimal into the kernel log. These opcodes can then be disassembled using the program <i>tools/net/bpf_jit_disasm.c</i> provided in the kernel source tree.</dl>
<p> Since Linux 4.15, the kernel may configured with the <code>CONFIG_BPF_JIT_ALWAYS_ON</code> option. In this case, the JIT compiler is always enabled, and the <i>bpf_jit_enable</i> is initialized to 1 and is immutable. (This kernel configuration option was provided as a mitigation for one of the Spectre attacks against the BPF interpreter.) </p>
<p> The JIT compiler for eBPF is currently available for the following architectures:</p>
<dl>
<dt>*</p>
<dd> x86-64 (since Linux 3.18; cBPF since Linux 3.0);</p>
<dt>*</p>
<dd> ARM32 (since Linux 3.18; cBPF since Linux 3.4);</p>
<dt>*</p>
<dd> SPARC 32 (since Linux 3.18; cBPF since Linux 3.5);</p>
<dt>*</p>
<dd> ARM-64 (since Linux 3.18);</p>
<dt>*</p>
<dd> s390 (since Linux 4.1; cBPF since Linux 3.7);</p>
<dt>*</p>
<dd> PowerPC 64 (since Linux 4.8; cBPF since Linux 3.1);</p>
<dt>*</p>
<dd> SPARC 64 (since Linux 4.12);</p>
<dt>*</p>
<dd> x86-32 (since Linux 4.18);</p>
<dt>*</p>
<dd> MIPS 64 (since Linux 4.18; cBPF since Linux 3.16);</p>
<dt>*</p>
<dd> riscv (since Linux 5.1).</dl>
<h2>EXAMPLES</h2>
<p> /* bpf+sockets example:<br />
&nbsp;*&nbsp;1. create array map of 256 elements<br />
&nbsp;*&nbsp;2. load program that counts number of packets received<br />
&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r0&nbsp;=&nbsp;skb-&gt;data[ETH_HLEN&nbsp;+&nbsp;offsetof(struct iphdr, protocol)]<br />
&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map[r0]++<br />
&nbsp;*&nbsp;3. attach prog_fd to raw socket via setsockopt()<br />
&nbsp;*&nbsp;4. print number of received TCP/UDP packets every second<br />
&nbsp;*/ int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sock, map_fd, prog_fd, key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long long value&nbsp;=&nbsp;0, tcp_cnt, udp_cnt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_fd&nbsp;=&nbsp;bpf_create_map(BPF_MAP_TYPE_ARRAY, sizeof(key),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(value), 256);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(map_fd&nbsp;&lt;&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;failed to create map&nbsp;&#8216;%s&#8217;
&quot;, strerror(errno));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;likely not run as root&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct bpf_insn prog[]&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MOV64_REG(BPF_REG_6, BPF_REG_1),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r6&nbsp;=&nbsp;r1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_LD_ABS(BPF_B, ETH_HLEN&nbsp;+&nbsp;offsetof(struct iphdr, protocol)),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r0&nbsp;=&nbsp;ip-&gt;proto&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STX_MEM(BPF_W, BPF_REG_10, BPF_REG_0, -4),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;*(u32&nbsp;*)(fp &#8211; 4)&nbsp;=&nbsp;r0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MOV64_REG(BPF_REG_2, BPF_REG_10),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r2&nbsp;=&nbsp;fp&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_ALU64_IMM(BPF_ADD, BPF_REG_2, -4),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r2&nbsp;=&nbsp;r2 &#8211; 4&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_LD_MAP_FD(BPF_REG_1, map_fd),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r1&nbsp;=&nbsp;map_fd&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_CALL_FUNC(BPF_FUNC_map_lookup_elem),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r0&nbsp;=&nbsp;map_lookup(r1, r2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_JMP_IMM(BPF_JEQ, BPF_REG_0, 0, 2),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if&nbsp;(r0&nbsp;==&nbsp;0)&nbsp;goto pc+2&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MOV64_IMM(BPF_REG_1, 1),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r1&nbsp;=&nbsp;1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_XADD(BPF_DW, BPF_REG_0, BPF_REG_1, 0, 0),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;lock&nbsp;*(u64&nbsp;*)&nbsp;r0&nbsp;+=&nbsp;r1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_MOV64_IMM(BPF_REG_0, 0),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r0&nbsp;=&nbsp;0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_EXIT_INSN(),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;return r0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_fd&nbsp;=&nbsp;bpf_prog_load(BPF_PROG_TYPE_SOCKET_FILTER, prog,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(prog)&nbsp;/&nbsp;sizeof(prog[0]),&nbsp;&quot;GPL&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sock&nbsp;=&nbsp;open_raw_sock(&quot;lo&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(setsockopt(sock, SOL_SOCKET, SO_ATTACH_BPF,&nbsp;&amp;prog_fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(prog_fd))&nbsp;==&nbsp;0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key&nbsp;=&nbsp;IPPROTO_TCP;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(bpf_lookup_elem(map_fd,&nbsp;&amp;key,&nbsp;&amp;tcp_cnt)&nbsp;==&nbsp;0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key&nbsp;=&nbsp;IPPROTO_UDP;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert(bpf_lookup_elem(map_fd,&nbsp;&amp;key,&nbsp;&amp;udp_cnt)&nbsp;==&nbsp;0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;TCP&nbsp;%lld UDP&nbsp;%lld packets
&quot;, tcp_cnt, udp_cnt);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/1-sleep/">sleep</a>(1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> Some complete working code can be found in the <i>samples/bpf</i> directory in the kernel source tree.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2), <code><a href="/docs/linux/man/7-bpf-helpers/">bpf-helpers</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8) </p>
<p> Both classic and extended BPF are explained in the kernel source file <i>Documentation/networking/filter.txt</i>.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
