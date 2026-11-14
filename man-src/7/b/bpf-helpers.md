---
title: "bpf-helpers(7)"
name: "bpf-helpers"
section: "7"
letter: "b"
url: "/docs/linux/man/7-bpf-helpers/"
description: "BPF-HELPERS – list of eBPF helper functions"
---

<p>BPF-HELPERS &#8211; list of eBPF helper functions</p>
<h2>Description</h2>
<p>The extended Berkeley Packet Filter (eBPF) subsystem consists in programs written in a pseudo-assembly language, then attached to one of the several kernel hooks and run in reaction of specific events. This framework differs from the older, &quot;classic&quot; BPF (or &quot;cBPF&quot;) in several aspects, one of them being the ability to call special functions (or &quot;helpers&quot;) from within a program. These functions are restricted to a white-list of helpers defined in the kernel. </p>
<p> These helpers are used by eBPF programs to interact with the system, or with the context in which they work. For instance, they can be used to print debugging messages, to get the time since the system was booted, to interact with eBPF maps, or to manipulate network packets. Since there are several eBPF program types, and that they do not run in the same context, each program type can only call a subset of those helpers. </p>
<p> Due to eBPF conventions, a helper can not have more than five arguments. </p>
<p> Internally, eBPF programs call directly into the compiled helper functions without requiring any foreign-function interface. As a result, calling helpers introduces no overhead, thus offering excellent performance. </p>
<p> This document is an attempt to list and document the helpers available to eBPF developers. They are sorted by chronological order (the oldest helpers in the kernel at the top).</p>
<h2>Helpers</h2>
<dl>
<dt><code>void *bpf_map_lookup_elem(struct bpf_map *</code><i>map</i><code>, const void *</code><i>key</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Perform a lookup in <i>map</i> for an entry associated to <i>key</i>.</p>
<dt><code>Return</code></p>
<dd>Map value associated to <i>key</i>, or <code>NULL</code> if no entry was found.</p>
<dt><code>long bpf_map_update_elem(struct bpf_map *</code><i>map</i><code>, const void *</code><i>key</i><code>, const void *</code><i>value</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Add or update the value of the entry associated to <i>key</i> in <i>map</i> with <i>value</i>. <i>flags</i> is one of:</p>
<dt><code>BPF_NOEXIST</code></p>
<dd>The entry for <i>key</i> must not exist in the map.</p>
<dt><code>BPF_EXIST</code></p>
<dd>The entry for <i>key</i> must already exist in the map.</p>
<dt><code>BPF_ANY</code></p>
<dd>No condition on the existence of the entry for <i>key</i>. </p>
<p> Flag value <code>BPF_NOEXIST</code> cannot be used for maps of types <code>BPF_MAP_TYPE_ARRAY</code> or <code>BPF_MAP_TYPE_PERCPU_ARRAY</code> (all elements always exist), the helper would return an error.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_map_delete_elem(struct bpf_map *</code><i>map</i><code>, const void *</code><i>key</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Delete entry with <i>key</i> from <i>map</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_probe_read(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For tracing programs, safely attempt to read <i>size</i> bytes from kernel space address <i>unsafe_ptr</i> and store the data in <i>dst</i>. </p>
<p> Generally, use <code>bpf_probe_read_user</code>() or <code>bpf_probe_read_kernel</code>() instead.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u64 bpf_ktime_get_ns(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return the time elapsed since system boot, in nanoseconds. Does not include time the system was suspended. See: <code>clock_gettime</code>(<code>CLOCK_MONOTONIC</code>)</p>
<dt><code>Return</code></p>
<dd>Current <i>ktime</i>.</p>
<dt><code>long bpf_trace_printk(const char *</code><i>fmt</i><code>, u32</code> <i>fmt_size</i><code>, &#8230;)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is a &quot;printk()-like&quot; facility for debugging. It prints a message defined by format <i>fmt</i> (of size <i>fmt_size</i>) to file <i>/sys/kernel/debug/tracing/trace</i> from DebugFS, if available. It can take up to three additional <code>u64</code> arguments (as an eBPF helpers, the total number of arguments is limited to five). </p>
<p> Each time the helper is called, it appends a line to the trace. Lines are discarded while <i>/sys/kernel/debug/tracing/trace</i> is open, use <i>/sys/kernel/debug/tracing/trace_pipe</i> to avoid this. The format of the trace is customizable, and the exact output one will get depends on the options set in <i>/sys/kernel/debug/tracing/trace_options</i> (see also the <i>README</i> file under the same directory). However, it usually defaults to something like: </p>
<pre>telnet-470 [001] .N.. 419421.045894: 0x00000001: &lt;formatted msg&gt;</pre>
<p>In the above:</p>
<dt>&bull;</p>
<dd><code>telnet</code> is the name of the current task.</p>
<dt>&bull;</p>
<dd><code>470</code> is the PID of the current task.</p>
<dt>&bull;</p>
<dd><code>001</code> is the CPU number on which the task is running.</p>
<dt>&bull;</p>
<dd>In <code>.N..</code>, each character refers to a set of options (whether irqs are enabled, scheduling options, whether hard/softirqs are running, level of preempt_disabled respectively). <code>N</code> means that <code>TIF_NEED_RESCHED</code> and <code>PREEMPT_NEED_RESCHED</code> are set.</p>
<dt>&bull;</p>
<dd><code>419421.045894</code> is a timestamp.</p>
<dt>&bull;</p>
<dd><code>0x00000001</code> is a fake value used by BPF for the instruction pointer register.</p>
<dt>&bull;</p>
<dd><code>&lt;formatted msg&gt;</code> is the message formatted with <i>fmt</i>. </p>
<p> The conversion specifiers supported by <i>fmt</i> are similar, but more limited than for printk(). They are <code>%d</code>, <code>%i</code>, <code>%u</code>, <code>%x</code>, <code>%ld</code>, <code>%li</code>, <code>%lu</code>, <code>%lx</code>, <code>%lld</code>, <code>%lli</code>, <code>%llu</code>, <code>%llx</code>, <code>%p</code>, <code>%s</code>. No modifier (size of field, padding with zeroes, etc.) is available, and the helper will return <code>-EINVAL</code> (but print nothing) if it encounters an unknown specifier. </p>
<p> Also, note that <code>bpf_trace_printk</code>() is slow, and should only be used for debugging purposes. For this reason, a notice block (spanning several lines) is printed to kernel logs and states that the helper should not be used &quot;for production use&quot; the first time this helper is used (or more precisely, when <code>trace_printk</code>() buffers are allocated). For passing values to user space, perf events should be preferred.</p>
<dt><code>Return</code></p>
<dd>The number of bytes written to the buffer, or a negative error in case of failure.</p>
<dt><code>u32 bpf_get_prandom_u32(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get a pseudo-random number. </p>
<p> From a security point of view, this helper uses its own pseudo-random internal state, and cannot be used to infer the seed of other random functions in the kernel. However, it is essential to note that the generator used by the helper is not cryptographically secure.</p>
<dt><code>Return</code></p>
<dd>A random 32-bit unsigned value.</p>
<dt><code>u32 bpf_get_smp_processor_id(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get the SMP (symmetric multiprocessing) processor id. Note that all programs run with preemption disabled, which means that the SMP processor id is stable during all the execution of the program.</p>
<dt><code>Return</code></p>
<dd>The SMP id of the processor running the program.</p>
<dt><code>long bpf_skb_store_bytes(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, const void *</code><i>from</i><code>, u32</code> <i>len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Store <i>len</i> bytes from address <i>from</i> into the packet associated to <i>skb</i>, at <i>offset</i>. <i>flags</i> are a combination of <code>BPF_F_RECOMPUTE_CSUM</code> (automatically recompute the checksum for the packet after storing the bytes) and <code>BPF_F_INVALIDATE_HASH</code> (set <i>skb</i><code>-&gt;hash</code>, <i>skb</i><code>-&gt;swhash</code> and <i>skb</i><code>-&gt;l4hash</code> to 0). </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_l3_csum_replace(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, u64</code> <i>from</i><code>, u64</code> <i>to</i><code>, u64</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Recompute the layer 3 (e.g. IP) checksum for the packet associated to <i>skb</i>. Computation is incremental, so the helper must know the former value of the header field that was modified (<i>from</i>), the new value of this field (<i>to</i>), and the number of bytes (2 or 4) for this field, stored in <i>size</i>. Alternatively, it is possible to store the difference between the previous and the new values of the header field in <i>to</i>, by setting <i>from</i> and <i>size</i> to 0. For both methods, <i>offset</i> indicates the location of the IP checksum within the packet. </p>
<p> This helper works in combination with <code>bpf_csum_diff</code>(), which does not update the checksum in-place, but offers more flexibility and can handle sizes larger than 2 or 4 for the checksum to update. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_l4_csum_replace(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, u64</code> <i>from</i><code>, u64</code> <i>to</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Recompute the layer 4 (e.g. TCP, UDP or ICMP) checksum for the packet associated to <i>skb</i>. Computation is incremental, so the helper must know the former value of the header field that was modified (<i>from</i>), the new value of this field (<i>to</i>), and the number of bytes (2 or 4) for this field, stored on the lowest four bits of <i>flags</i>. Alternatively, it is possible to store the difference between the previous and the new values of the header field in <i>to</i>, by setting <i>from</i> and the four lowest bits of <i>flags</i> to 0. For both methods, <i>offset</i> indicates the location of the IP checksum within the packet. In addition to the size of the field, <i>flags</i> can be added (bitwise OR) actual flags. With <code>BPF_F_MARK_MANGLED_0</code>, a null checksum is left untouched (unless <code>BPF_F_MARK_ENFORCE</code> is added as well), and for updates resulting in a null checksum the value is set to <code>CSUM_MANGLED_0</code> instead. Flag <code>BPF_F_PSEUDO_HDR</code> indicates the checksum is to be computed against a pseudo-header. </p>
<p> This helper works in combination with <code>bpf_csum_diff</code>(), which does not update the checksum in-place, but offers more flexibility and can handle sizes larger than 2 or 4 for the checksum to update. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_tail_call(void *</code><i>ctx</i><code>, struct bpf_map *</code><i>prog_array_map</i><code>, u32</code> <i>index</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This special helper is used to trigger a &quot;tail call&quot;, or in other words, to jump into another eBPF program. The same stack frame is used (but values on stack and in registers for the caller are not accessible to the callee). This mechanism allows for program chaining, either for raising the maximum number of available eBPF instructions, or to execute given programs in conditional blocks. For security reasons, there is an upper limit to the number of successive tail calls that can be performed. </p>
<p> Upon call of this helper, the program attempts to jump into a program referenced at index <i>index</i> in <i>prog_array_map</i>, a special map of type <code>BPF_MAP_TYPE_PROG_ARRAY</code>, and passes <i>ctx</i>, a pointer to the context. </p>
<p> If the call succeeds, the kernel immediately runs the first instruction of the new program. This is not a function call, and it never returns to the previous program. If the call fails, then the helper has no effect, and the caller continues to run its subsequent instructions. A call can fail if the destination program for the jump does not exist (i.e. <i>index</i> is superior to the number of entries in <i>prog_array_map</i>), or if the maximum number of tail calls has been reached for this chain of programs. This limit is defined in the kernel by the macro <code>MAX_TAIL_CALL_CNT</code> (not accessible to user space), which is currently set to 32.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_clone_redirect(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>ifindex</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Clone and redirect the packet associated to <i>skb</i> to another net device of index <i>ifindex</i>. Both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress path otherwise). This is the only flag supported for now. </p>
<p> In comparison with <code>bpf_redirect</code>() helper, <code>bpf_clone_redirect</code>() has the associated cost of duplicating the packet buffer, but this can be executed out of the eBPF program. Conversely, <code>bpf_redirect</code>() is more efficient, but it is handled through an action code where the redirection happens only after the eBPF program has returned. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u64 bpf_get_current_pid_tgid(void)</code></p>
<dd>
<dt><code>Return</code></p>
<dd>A 64-bit integer containing the current tgid and pid, and created as such: <i>current_task</i><code>-&gt;tgid &lt;&lt; 32 |</code> <i>current_task</i><code>-&gt;pid</code>.</p>
<dt><code>u64 bpf_get_current_uid_gid(void)</code></p>
<dd>
<dt><code>Return</code></p>
<dd>A 64-bit integer containing the current GID and UID, and created as such: <i>current_gid</i> <code>&lt;&lt; 32 |</code> <i>current_uid</i>.</p>
<dt><code>long bpf_get_current_comm(void *</code><i>buf</i><code>, u32</code> <i>size_of_buf</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Copy the <code>comm</code> attribute of the current task into <i>buf</i> of <i>size_of_buf</i>. The <code>comm</code> attribute contains the name of the executable (excluding the path) for the current task. The <i>size_of_buf</i> must be strictly positive. On success, the helper makes sure that the <i>buf</i> is NUL-terminated. On failure, it is filled with zeroes.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u32 bpf_get_cgroup_classid(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve the classid for the current task, i.e. for the net_cls cgroup to which <i>skb</i> belongs. </p>
<p> This helper can be used on TC egress path, but not on ingress. </p>
<p> The net_cls cgroup provides an interface to tag network packets based on a user-provided identifier for all traffic coming from the tasks belonging to the related cgroup. See also the related kernel documentation, available from the Linux sources in file <i>Documentation/admin-guide/cgroup-v1/net_cls.rst</i>. </p>
<p> The Linux kernel has two versions for cgroups: there are cgroups v1 and cgroups v2. Both are available to users, who can use a mixture of them, but note that the net_cls cgroup is for cgroup v1 only. This makes it incompatible with BPF programs run on cgroups, which is a cgroup-v2-only feature (a socket can only hold data for one version of cgroups at a time). </p>
<p> This helper is only available is the kernel was compiled with the <code>CONFIG_CGROUP_NET_CLASSID</code> configuration option set to &quot;<code>y</code>&quot; or to &quot;<code>m</code>&quot;.</p>
<dt><code>Return</code></p>
<dd>The classid, or 0 for the default unconfigured classid.</p>
<dt><code>long bpf_skb_vlan_push(struct sk_buff *</code><i>skb</i><code>, __be16</code> <i>vlan_proto</i><code>, u16</code> <i>vlan_tci</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Push a <i>vlan_tci</i> (VLAN tag control information) of protocol <i>vlan_proto</i> to the packet associated to <i>skb</i>, then update the checksum. Note that if <i>vlan_proto</i> is different from <code>ETH_P_8021Q</code> and <code>ETH_P_8021AD</code>, it is considered to be <code>ETH_P_8021Q</code>. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_vlan_pop(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Pop a VLAN header from the packet associated to <i>skb</i>. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_get_tunnel_key(struct sk_buff *</code><i>skb</i><code>, struct bpf_tunnel_key *</code><i>key</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get tunnel metadata. This helper takes a pointer <i>key</i> to an empty <code>struct bpf_tunnel_key</code> of <code>size</code>, that will be filled with tunnel metadata for the packet associated to <i>skb</i>. The <i>flags</i> can be set to <code>BPF_F_TUNINFO_IPV6</code>, which indicates that the tunnel is based on IPv6 protocol instead of IPv4. </p>
<p> The <code>struct bpf_tunnel_key</code> is an object that generalizes the principal parameters used by various tunneling protocols into a single struct. This way, it can be used to easily make a decision based on the contents of the encapsulation header, &quot;summarized&quot; in this struct. In particular, it holds the IP address of the remote end (IPv4 or IPv6, depending on the case) in <i>key</i><code>-&gt;remote_ipv4</code> or <i>key</i><code>-&gt;remote_ipv6</code>. Also, this struct exposes the <i>key</i><code>-&gt;tunnel_id</code>, which is generally mapped to a VNI (Virtual Network Identifier), making it programmable together with the <code>bpf_skb_set_tunnel_key</code>() helper. </p>
<p> Let&#8217;s imagine that the following code is part of a program attached to the TC ingress interface, on one end of a GRE tunnel, and is supposed to filter out all messages coming from remote ends with IPv4 address other than 10.0.0.1: </p>
<pre>int ret;
struct bpf_tunnel_key key = {};
ret = bpf_skb_get_tunnel_key(skb, &amp;key, sizeof(key), 0);
if (ret &lt; 0)
 return TC_ACT_SHOT; // drop packet
if (key.remote_ipv4 != 0x0a000001)
 return TC_ACT_SHOT; // drop packet
return TC_ACT_OK; // accept packet</pre>
<p>This interface can also be used with all encapsulation devices that can operate in &quot;collect metadata&quot; mode: instead of having one network device per specific configuration, the &quot;collect metadata&quot; mode only requires a single device where the configuration can be extracted from this helper. </p>
<p> This can be used together with various tunnels such as VXLan, Geneve, GRE or IP in IP (IPIP).</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_set_tunnel_key(struct sk_buff *</code><i>skb</i><code>, struct bpf_tunnel_key *</code><i>key</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Populate tunnel metadata for packet associated to <i>skb.</i> The tunnel metadata is set to the contents of <i>key</i>, of <i>size</i>. The <i>flags</i> can be set to a combination of the following values:</p>
<dt><code>BPF_F_TUNINFO_IPV6</code></p>
<dd>Indicate that the tunnel is based on IPv6 protocol instead of IPv4.</p>
<dt><code>BPF_F_ZERO_CSUM_TX</code></p>
<dd>For IPv4 packets, add a flag to tunnel metadata indicating that checksum computation should be skipped and checksum set to zeroes.</p>
<dt><code>BPF_F_DONT_FRAGMENT</code></p>
<dd>Add a flag to tunnel metadata indicating that the packet should not be fragmented.</p>
<dt><code>BPF_F_SEQ_NUMBER</code></p>
<dd>Add a flag to tunnel metadata indicating that a sequence number should be added to tunnel header before sending the packet. This flag was added for GRE encapsulation, but might be used with other protocols as well in the future. </p>
<p> Here is a typical usage on the transmit path: </p>
<pre>struct bpf_tunnel_key key;
 populate key ...
bpf_skb_set_tunnel_key(skb, &amp;key, sizeof(key), 0);
bpf_clone_redirect(skb, vxlan_dev_ifindex, 0);</pre>
<p>See also the description of the <code>bpf_skb_get_tunnel_key</code>() helper for additional information.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u64 bpf_perf_event_read(struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Read the value of a perf event counter. This helper relies on a <i>map</i> of type <code>BPF_MAP_TYPE_PERF_EVENT_ARRAY</code>. The nature of the perf event counter is selected when <i>map</i> is updated with perf event file descriptors. The <i>map</i> is an array whose size is the number of available CPUs, and each cell contains a value relative to one CPU. The value to retrieve is indicated by <i>flags</i>, that contains the index of the CPU to look up, masked with <code>BPF_F_INDEX_MASK</code>. Alternatively, <i>flags</i> can be set to <code>BPF_F_CURRENT_CPU</code> to indicate that the value for the current CPU should be retrieved. </p>
<p> Note that before Linux 4.13, only hardware perf event can be retrieved. </p>
<p> Also, be aware that the newer helper <code>bpf_perf_event_read_value</code>() is recommended over <code>bpf_perf_event_read</code>() in general. The latter has some ABI quirks where error and counter value are used as a return code (which is wrong to do since ranges may overlap). This issue is fixed with <code>bpf_perf_event_read_value</code>(), which at the same time provides more features over the <code>bpf_perf_event_read</code>() interface. Please refer to the description of <code>bpf_perf_event_read_value</code>() for details.</p>
<dt><code>Return</code></p>
<dd>The value of the perf event counter read from the map, or a negative error code in case of failure.</p>
<dt><code>long bpf_redirect(u32</code> <i>ifindex</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Redirect the packet to another net device of index <i>ifindex</i>. This helper is somewhat similar to <code>bpf_clone_redirect</code>(), except that the packet is not cloned, which provides increased performance. </p>
<p> Except for XDP, both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress path otherwise). Currently, XDP only supports redirection to the egress interface, and accepts no flag at all. </p>
<p> The same effect can also be attained with the more generic <code>bpf_redirect_map</code>(), which uses a BPF map to store the redirect target instead of providing it directly to the helper.</p>
<dt><code>Return</code></p>
<dd>For XDP, the helper returns <code>XDP_REDIRECT</code> on success or <code>XDP_ABORTED</code> on error. For other program types, the values are <code>TC_ACT_REDIRECT</code> on success or <code>TC_ACT_SHOT</code> on error.</p>
<dt><code>u32 bpf_get_route_realm(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve the realm or the route, that is to say the <code>tclassid</code> field of the destination for the <i>skb</i>. The identifier retrieved is a user-provided tag, similar to the one used with the net_cls cgroup (see description for <code>bpf_get_cgroup_classid</code>() helper), but here this tag is held by a route (a destination entry), not by a task. </p>
<p> Retrieving this identifier works with the clsact TC egress hook (see also <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a>(8)</code>), or alternatively on conventional classful egress qdiscs, but not on TC ingress path. In case of clsact TC egress hook, this has the advantage that, internally, the destination entry has not been dropped yet in the transmit path. Therefore, the destination entry does not need to be artificially held via <code>netif_keep_dst</code>() for a classful qdisc until the <i>skb</i> is freed. </p>
<p> This helper is available only if the kernel was compiled with <code>CONFIG_IP_ROUTE_CLASSID</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>The realm of the route for the packet associated to <i>skb</i>, or 0 if none was found.</p>
<dt><code>long bpf_perf_event_output(void *</code><i>ctx</i><code>, struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>, void *</code><i>data</i><code>, u64</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Write raw <i>data</i> blob into a special BPF perf event held by <i>map</i> of type <code>BPF_MAP_TYPE_PERF_EVENT_ARRAY</code>. This perf event must have the following attributes: <code>PERF_SAMPLE_RAW</code> as <code>sample_type</code>, <code>PERF_TYPE_SOFTWARE</code> as <code>type</code>, and <code>PERF_COUNT_SW_BPF_OUTPUT</code> as <code>config</code>. </p>
<p> The <i>flags</i> are used to indicate the index in <i>map</i> for which the value must be put, masked with <code>BPF_F_INDEX_MASK</code>. Alternatively, <i>flags</i> can be set to <code>BPF_F_CURRENT_CPU</code> to indicate that the index of the current CPU core should be used. </p>
<p> The value to write, of <i>size</i>, is passed through eBPF stack and pointed by <i>data</i>. </p>
<p> The context of the program <i>ctx</i> needs also be passed to the helper. </p>
<p> On user space, a program willing to read the values needs to call <code>perf_event_open</code>() on the perf event (either for one or for all CPUs) and to store the file descriptor into the <i>map</i>. This must be done before the eBPF program can send data into it. An example is available in file <i>samples/bpf/trace_output_user.c</i> in the Linux kernel source tree (the eBPF program counterpart is in <i>samples/bpf/trace_output_kern.c</i>). </p>
<p> <code>bpf_perf_event_output</code>() achieves better performance than <code>bpf_trace_printk</code>() for sharing data with user space, and is much better suitable for streaming data from eBPF programs. </p>
<p> Note that this helper is not restricted to tracing use cases and can be used with programs attached to TC or XDP as well, where it allows for passing data to user space listeners. Data can be:</p>
<dt>&bull;</p>
<dd>Only custom structs,</p>
<dt>&bull;</p>
<dd>Only the packet payload, or</p>
<dt>&bull;</p>
<dd>A combination of both.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_load_bytes(const void *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, void *</code><i>to</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper was provided as an easy way to load data from a packet. It can be used to load <i>len</i> bytes from <i>offset</i> from the packet associated to <i>skb</i>, into the buffer pointed by <i>to</i>. </p>
<p> Since Linux 4.7, usage of this helper has mostly been replaced by &quot;direct packet access&quot;, enabling packet data to be manipulated with <i>skb</i><code>-&gt;data</code> and <i>skb</i><code>-&gt;data_end</code> pointing respectively to the first byte of packet data and to the byte after the last byte of packet data. However, it remains useful if one wishes to read large quantities of data at once from a packet into the eBPF stack.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_get_stackid(void *</code><i>ctx</i><code>, struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Walk a user or a kernel stack and return its id. To achieve this, the helper needs <i>ctx</i>, which is a pointer to the context on which the tracing program is executed, and a pointer to a <i>map</i> of type <code>BPF_MAP_TYPE_STACK_TRACE</code>. </p>
<p> The last argument, <i>flags</i>, holds the number of stack frames to skip (from 0 to 255), masked with <code>BPF_F_SKIP_FIELD_MASK</code>. The next bits can be used to set a combination of the following flags:</p>
<dt><code>BPF_F_USER_STACK</code></p>
<dd>Collect a user space stack instead of a kernel stack.</p>
<dt><code>BPF_F_FAST_STACK_CMP</code></p>
<dd>Compare stacks by hash only.</p>
<dt><code>BPF_F_REUSE_STACKID</code></p>
<dd>If two different stacks hash into the same <i>stackid</i>, discard the old one. </p>
<p> The stack id retrieved is a 32 bit long integer handle which can be further combined with other data (including other stack ids) and used as a key into maps. This can be useful for generating a variety of graphs (such as flame graphs or off-cpu graphs). </p>
<p> For walking a stack, this helper is an improvement over <code>bpf_probe_read</code>(), which can be used with unrolled loops but is not efficient and consumes a lot of eBPF instructions. Instead, <code>bpf_get_stackid</code>() can collect up to <code>PERF_MAX_STACK_DEPTH</code> both kernel and user frames. Note that this limit can be controlled with the <code>sysctl</code> program, and that it should be manually increased in order to profile long user stacks (such as stacks for Java programs). To do so, use: </p>
<pre># sysctl kernel.perf_event_max_stack=&lt;new value&gt;</pre>
<dt><code>Return</code></p>
<dd>The positive or null stack id on success, or a negative error in case of failure.</p>
<dt><code>s64 bpf_csum_diff(__be32 *</code><i>from</i><code>, u32</code> <i>from_size</i><code>, __be32 *</code><i>to</i><code>, u32</code> <i>to_size</i><code>, __wsum</code> <i>seed</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Compute a checksum difference, from the raw buffer pointed by <i>from</i>, of length <i>from_size</i> (that must be a multiple of 4), towards the raw buffer pointed by <i>to</i>, of size <i>to_size</i> (same remark). An optional <i>seed</i> can be added to the value (this can be cascaded, the seed may come from a previous call to the helper). </p>
<p> This is flexible enough to be used in several ways:</p>
<dt>&bull;</p>
<dd>With <i>from_size</i> == 0, <i>to_size</i> &gt; 0 and <i>seed</i> set to checksum, it can be used when pushing new data.</p>
<dt>&bull;</p>
<dd>With <i>from_size</i> &gt; 0, <i>to_size</i> == 0 and <i>seed</i> set to checksum, it can be used when removing data from a packet.</p>
<dt>&bull;</p>
<dd>With <i>from_size</i> &gt; 0, <i>to_size</i> &gt; 0 and <i>seed</i> set to 0, it can be used to compute a diff. Note that <i>from_size</i> and <i>to_size</i> do not need to be equal. </p>
<p> This helper can be used in combination with <code>bpf_l3_csum_replace</code>() and <code>bpf_l4_csum_replace</code>(), to which one can feed in the difference computed with <code>bpf_csum_diff</code>().</p>
<dt><code>Return</code></p>
<dd>The checksum result, or a negative error code in case of failure.</p>
<dt><code>long bpf_skb_get_tunnel_opt(struct sk_buff *</code><i>skb</i><code>, void *</code><i>opt</i><code>, u32</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve tunnel options metadata for the packet associated to <i>skb</i>, and store the raw tunnel option data to the buffer <i>opt</i> of <i>size</i>. </p>
<p> This helper can be used with encapsulation devices that can operate in &quot;collect metadata&quot; mode (please refer to the related note in the description of <code>bpf_skb_get_tunnel_key</code>() for more details). A particular example where this can be used is in combination with the Geneve encapsulation protocol, where it allows for pushing (with <code>bpf_skb_get_tunnel_opt</code>() helper) and retrieving arbitrary TLVs (Type-Length-Value headers) from the eBPF program. This allows for full customization of these headers.</p>
<dt><code>Return</code></p>
<dd>The size of the option data retrieved.</p>
<dt><code>long bpf_skb_set_tunnel_opt(struct sk_buff *</code><i>skb</i><code>, void *</code><i>opt</i><code>, u32</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Set tunnel options metadata for the packet associated to <i>skb</i> to the option data contained in the raw buffer <i>opt</i> of <i>size</i>. </p>
<p> See also the description of the <code>bpf_skb_get_tunnel_opt</code>() helper for additional information.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_change_proto(struct sk_buff *</code><i>skb</i><code>, __be16</code> <i>proto</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Change the protocol of the <i>skb</i> to <i>proto</i>. Currently supported are transition from IPv4 to IPv6, and from IPv6 to IPv4. The helper takes care of the groundwork for the transition, including resizing the socket buffer. The eBPF program is expected to fill the new headers, if any, via <code>skb_store_bytes</code>() and to recompute the checksums with <code>bpf_l3_csum_replace</code>() and <code>bpf_l4_csum_replace</code>(). The main case for this helper is to perform NAT64 operations out of an eBPF program. </p>
<p> Internally, the GSO type is marked as dodgy so that headers are checked and segments are recalculated by the GSO/GRO engine. The size for GSO target is adapted as well. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_change_type(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>type</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Change the packet type for the packet associated to <i>skb</i>. This comes down to setting <i>skb</i><code>-&gt;pkt_type</code> to <i>type</i>, except the eBPF program does not have a write access to <i>skb</i><code>-&gt;pkt_type</code> beside this helper. Using a helper here allows for graceful handling of errors. </p>
<p> The major use case is to change incoming <i>skb*s to **PACKET_HOST*</i> in a programmatic way instead of having to recirculate via <code>redirect</code>(&#8230;, <code>BPF_F_INGRESS</code>), for example. </p>
<p> Note that <i>type</i> only allows certain values. At this time, they are:</p>
<dt><code>PACKET_HOST</code></p>
<dd>Packet is for us.</p>
<dt><code>PACKET_BROADCAST</code></p>
<dd>Send packet to all.</p>
<dt><code>PACKET_MULTICAST</code></p>
<dd>Send packet to group.</p>
<dt><code>PACKET_OTHERHOST</code></p>
<dd>Send packet to someone else.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_under_cgroup(struct sk_buff *</code><i>skb</i><code>, struct bpf_map *</code><i>map</i><code>, u32</code> <i>index</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Check whether <i>skb</i> is a descendant of the cgroup2 held by <i>map</i> of type <code>BPF_MAP_TYPE_CGROUP_ARRAY</code>, at <i>index</i>.</p>
<dt><code>Return</code></p>
<dd>The return value depends on the result of the test, and can be:</p>
<dt>&bull;</p>
<dd>0, if the <i>skb</i> failed the cgroup2 descendant test.</p>
<dt>&bull;</p>
<dd>1, if the <i>skb</i> succeeded the cgroup2 descendant test.</p>
<dt>&bull;</p>
<dd>A negative error code, if an error occurred.</p>
<dt><code>u32 bpf_get_hash_recalc(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve the hash of the packet, <i>skb</i><code>-&gt;hash</code>. If it is not set, in particular if the hash was cleared due to mangling, recompute this hash. Later accesses to the hash can be done directly with <i>skb</i><code>-&gt;hash</code>. </p>
<p> Calling <code>bpf_set_hash_invalid</code>(), changing a packet prototype with <code>bpf_skb_change_proto</code>(), or calling <code>bpf_skb_store_bytes</code>() with the <code>BPF_F_INVALIDATE_HASH</code> are actions susceptible to clear the hash and to trigger a new computation for the next call to <code>bpf_get_hash_recalc</code>().</p>
<dt><code>Return</code></p>
<dd>The 32-bit hash.</p>
<dt><code>u64 bpf_get_current_task(void)</code></p>
<dd>
<dt><code>Return</code></p>
<dd>A pointer to the current task struct.</p>
<dt><code>long bpf_probe_write_user(void *</code><i>dst</i><code>, const void *</code><i>src</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Attempt in a safe way to write <i>len</i> bytes from the buffer <i>src</i> to <i>dst</i> in memory. It only works for threads that are in user context, and <i>dst</i> must be a valid user space address. </p>
<p> This helper should not be used to implement any kind of security mechanism because of TOC-TOU attacks, but rather to debug, divert, and manipulate execution of semi-cooperative processes. </p>
<p> Keep in mind that this feature is meant for experiments, and it has a risk of crashing the system and running programs. Therefore, when an eBPF program using this helper is attached, a warning including PID and process name is printed to kernel logs.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_current_task_under_cgroup(struct bpf_map *</code><i>map</i><code>, u32</code> <i>index</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Check whether the probe is being run is the context of a given subset of the cgroup2 hierarchy. The cgroup2 to test is held by <i>map</i> of type <code>BPF_MAP_TYPE_CGROUP_ARRAY</code>, at <i>index</i>.</p>
<dt><code>Return</code></p>
<dd>The return value depends on the result of the test, and can be:</p>
<dt>&bull;</p>
<dd>0, if the <i>skb</i> task belongs to the cgroup2.</p>
<dt>&bull;</p>
<dd>1, if the <i>skb</i> task does not belong to the cgroup2.</p>
<dt>&bull;</p>
<dd>A negative error code, if an error occurred.</p>
<dt><code>long bpf_skb_change_tail(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Resize (trim or grow) the packet associated to <i>skb</i> to the new <i>len</i>. The <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> The basic idea is that the helper performs the needed work to change the size of the packet, then the eBPF program rewrites the rest via helpers like <code>bpf_skb_store_bytes</code>(), <code>bpf_l3_csum_replace</code>(), <code>bpf_l3_csum_replace</code>() and others. This helper is a slow path utility intended for replies with control messages. And because it is targeted for slow path, the helper itself can afford to be slow: it implicitly linearizes, unclones and drops offloads from the <i>skb</i>. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_pull_data(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Pull in non-linear data in case the <i>skb</i> is non-linear and not all of <i>len</i> are part of the linear section. Make <i>len</i> bytes from <i>skb</i> readable and writable. If a zero value is passed for <i>len</i>, then the whole length of the <i>skb</i> is pulled. </p>
<p> This helper is only needed for reading and writing with direct packet access. </p>
<p> For direct packet access, testing that offsets to access are within packet boundaries (test on <i>skb</i><code>-&gt;data_end</code>) is susceptible to fail if offsets are invalid, or if the requested data is in non-linear parts of the <i>skb</i>. On failure the program can just bail out, or in the case of a non-linear buffer, use a helper to make the data available. The <code>bpf_skb_load_bytes</code>() helper is a first solution to access the data. Another one consists in using <code>bpf_skb_pull_data</code> to pull in once the non-linear parts, then retesting and eventually access the data. </p>
<p> At the same time, this also makes sure the <i>skb</i> is uncloned, which is a necessary condition for direct write. As this needs to be an invariant for the write part only, the verifier detects writes and adds a prologue that is calling <code>bpf_skb_pull_data()</code> to effectively unclone the <i>skb</i> from the very beginning in case it is indeed cloned. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>s64 bpf_csum_update(struct sk_buff *</code><i>skb</i><code>, __wsum</code> <i>csum</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Add the checksum <i>csum</i> into <i>skb</i><code>-&gt;csum</code> in case the driver has supplied a checksum for the entire packet into that field. Return an error otherwise. This helper is intended to be used in combination with <code>bpf_csum_diff</code>(), in particular when the checksum needs to be updated after data has been written into the packet through direct packet access.</p>
<dt><code>Return</code></p>
<dd>The checksum on success, or a negative error code in case of failure.</p>
<dt><code>void bpf_set_hash_invalid(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Invalidate the current <i>skb</i><code>-&gt;hash</code>. It can be used after mangling on headers through direct packet access, in order to indicate that the hash is outdated and to trigger a recalculation the next time the kernel tries to access this hash or when the <code>bpf_get_hash_recalc</code>() helper is called.</p>
<dt><code>long bpf_get_numa_node_id(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return the id of the current NUMA node. The primary use case for this helper is the selection of sockets for the local NUMA node, when the program is attached to sockets using the <code>SO_ATTACH_REUSEPORT_EBPF</code> option (see also <code><a href="/docs/linux/man/7-socket/">socket</a>(7)</code>), but the helper is also available to other eBPF program types, similarly to <code>bpf_get_smp_processor_id</code>().</p>
<dt><code>Return</code></p>
<dd>The id of current NUMA node.</p>
<dt><code>long bpf_skb_change_head(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Grows headroom of packet associated to <i>skb</i> and adjusts the offset of the MAC header accordingly, adding <i>len</i> bytes of space. It automatically extends and reallocates memory as required. </p>
<p> This helper can be used on a layer 3 <i>skb</i> to push a MAC header for redirection into a layer 2 device. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_xdp_adjust_head(struct xdp_buff *</code><i>xdp_md</i><code>, int</code> <i>delta</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Adjust (move) <i>xdp_md</i><code>-&gt;data</code> by <i>delta</i> bytes. Note that it is possible to use a negative value for <i>delta</i>. This helper can be used to prepare the packet for pushing or popping headers. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_probe_read_str(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Copy a NUL terminated string from an unsafe kernel address <i>unsafe_ptr</i> to <i>dst</i>. See <code>bpf_probe_read_kernel_str</code>() for more details. </p>
<p> Generally, use <code>bpf_probe_read_user_str</code>() or <code>bpf_probe_read_kernel_str</code>() instead.</p>
<dt><code>Return</code></p>
<dd>On success, the strictly positive length of the string, including the trailing NUL character. On error, a negative value.</p>
<dt><code>u64 bpf_get_socket_cookie(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>If the <code>struct sk_buff</code> pointed by <i>skb</i> has a known socket, retrieve the cookie (generated by the kernel) of this socket. If no cookie has been set yet, generate a new cookie. Once generated, the socket cookie remains stable for the life of the socket. This helper can be useful for monitoring per socket networking traffic statistics as it provides a global socket identifier that can be assumed unique.</p>
<dt><code>Return</code></p>
<dd>A 8-byte long non-decreasing number on success, or 0 if the socket field is missing inside <i>skb</i>.</p>
<dt><code>u64 bpf_get_socket_cookie(struct bpf_sock_addr *</code><i>ctx</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Equivalent to bpf_get_socket_cookie() helper that accepts <i>skb</i>, but gets socket from <code>struct bpf_sock_addr</code> context.</p>
<dt><code>Return</code></p>
<dd>A 8-byte long non-decreasing number.</p>
<dt><code>u64 bpf_get_socket_cookie(struct bpf_sock_ops *</code><i>ctx</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Equivalent to <code>bpf_get_socket_cookie</code>() helper that accepts <i>skb</i>, but gets socket from <code>struct bpf_sock_ops</code> context.</p>
<dt><code>Return</code></p>
<dd>A 8-byte long non-decreasing number.</p>
<dt><code>u32 bpf_get_socket_uid(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Return</code></p>
<dd>The owner UID of the socket associated to <i>skb</i>. If the socket is <code>NULL</code>, or if it is not a full socket (i.e. if it is a time-wait or a request socket instead), <code>overflowuid</code> value is returned (note that <code>overflowuid</code> might also be the actual UID value for the socket).</p>
<dt><code>long bpf_set_hash(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>hash</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Set the full hash for <i>skb</i> (set the field <i>skb</i><code>-&gt;hash</code>) to value <i>hash</i>.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_setsockopt(void *</code><i>bpf_socket</i><code>, int</code> <i>level</i><code>, int</code> <i>optname</i><code>, void *</code><i>optval</i><code>, int</code> <i>optlen</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Emulate a call to <code>setsockopt()</code> on the socket associated to <i>bpf_socket</i>, which must be a full socket. The <i>level</i> at which the option resides and the name <i>optname</i> of the option must be specified, see <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2)</code> for more information. The option value of length <i>optlen</i> is pointed by <i>optval</i>. </p>
<p> <i>bpf_socket</i> should be one of the following:</p>
<dt>&bull;</p>
<dd><code>struct bpf_sock_ops</code> for <code>BPF_PROG_TYPE_SOCK_OPS</code>.</p>
<dt>&bull;</p>
<dd><code>struct bpf_sock_addr</code> for <code>BPF_CGROUP_INET4_CONNECT</code> and <code>BPF_CGROUP_INET6_CONNECT</code>. </p>
<p> This helper actually implements a subset of <code>setsockopt()</code>. It supports the following <i>level</i>s:</p>
<dt>&bull;</p>
<dd><code>SOL_SOCKET</code>, which supports the following <i>optname</i>s: <code>SO_RCVBUF</code>, <code>SO_SNDBUF</code>, <code>SO_MAX_PACING_RATE</code>, <code>SO_PRIORITY</code>, <code>SO_RCVLOWAT</code>, <code>SO_MARK</code>, <code>SO_BINDTODEVICE</code>, <code>SO_KEEPALIVE</code>.</p>
<dt>&bull;</p>
<dd><code>IPPROTO_TCP</code>, which supports the following <i>optname</i>s: <code>TCP_CONGESTION</code>, <code>TCP_BPF_IW</code>, <code>TCP_BPF_SNDCWND_CLAMP</code>, <code>TCP_SAVE_SYN</code>, <code>TCP_KEEPIDLE</code>, <code>TCP_KEEPINTVL</code>, <code>TCP_KEEPCNT</code>, <code>TCP_SYNCNT</code>, <code>TCP_USER_TIMEOUT</code>.</p>
<dt>&bull;</p>
<dd><code>IPPROTO_IP</code>, which supports <i>optname</i> <code>IP_TOS</code>.</p>
<dt>&bull;</p>
<dd><code>IPPROTO_IPV6</code>, which supports <i>optname</i> <code>IPV6_TCLASS</code>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_adjust_room(struct sk_buff *</code><i>skb</i><code>, s32</code> <i>len_diff</i><code>, u32</code> <i>mode</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Grow or shrink the room for data in the packet associated to <i>skb</i> by <i>len_diff</i>, and according to the selected <i>mode</i>. </p>
<p> By default, the helper will reset any offloaded checksum indicator of the skb to CHECKSUM_NONE. This can be avoided by the following flag:</p>
<dt>&bull;</p>
<dd><code>BPF_F_ADJ_ROOM_NO_CSUM_RESET</code>: Do not reset offloaded checksum data of the skb to CHECKSUM_NONE. </p>
<p> There are two supported modes at this time:</p>
<dt>&bull;</p>
<dd><code>BPF_ADJ_ROOM_MAC</code>: Adjust room at the mac layer (room space is added or removed below the layer 2 header).</p>
<dt>&bull;</p>
<dd><code>BPF_ADJ_ROOM_NET</code>: Adjust room at the network layer (room space is added or removed below the layer 3 header). </p>
<p> The following flags are supported at this time:</p>
<dt>&bull;</p>
<dd><code>BPF_F_ADJ_ROOM_FIXED_GSO</code>: Do not adjust gso_size. Adjusting mss in this way is not allowed for datagrams.</p>
<dt>&bull;</p>
<dd><code>BPF_F_ADJ_ROOM_ENCAP_L3_IPV4</code>, <code>BPF_F_ADJ_ROOM_ENCAP_L3_IPV6</code>: Any new space is reserved to hold a tunnel header. Configure skb offsets and other fields accordingly.</p>
<dt>&bull;</p>
<dd><code>BPF_F_ADJ_ROOM_ENCAP_L4_GRE</code>, <code>BPF_F_ADJ_ROOM_ENCAP_L4_UDP</code>: Use with ENCAP_L3 flags to further specify the tunnel type.</p>
<dt>&bull;</p>
<dd><code>BPF_F_ADJ_ROOM_ENCAP_L2</code>(<i>len</i>): Use with ENCAP_L3/L4 flags to further specify the tunnel type; <i>len</i> is the length of the inner MAC header. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_redirect_map(struct bpf_map *</code><i>map</i><code>, u32</code> <i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Redirect the packet to the endpoint referenced by <i>map</i> at index <i>key</i>. Depending on its type, this <i>map</i> can contain references to net devices (for forwarding packets through other ports), or to CPUs (for redirecting XDP frames to another CPU; but this is only implemented for native XDP (with driver support) as of this writing). </p>
<p> The lower two bits of <i>flags</i> are used as the return code if the map lookup fails. This is so that the return value can be one of the XDP program return codes up to <code>XDP_TX</code>, as chosen by the caller. Any higher bits in the <i>flags</i> argument must be unset. </p>
<p> See also <code>bpf_redirect</code>(), which only supports redirecting to an ifindex, but doesn&#8217;t require a map to do so.</p>
<dt><code>Return</code></p>
<dd><code>XDP_REDIRECT</code> on success, or the value of the two lower bits of the <i>flags</i> argument on error.</p>
<dt><code>long bpf_sk_redirect_map(struct sk_buff *</code><i>skb</i><code>, struct bpf_map *</code><i>map</i><code>, u32</code> <i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Redirect the packet to the socket referenced by <i>map</i> (of type <code>BPF_MAP_TYPE_SOCKMAP</code>) at index <i>key</i>. Both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress path otherwise). This is the only flag supported for now.</p>
<dt><code>Return</code></p>
<dd><code>SK_PASS</code> on success, or <code>SK_DROP</code> on error.</p>
<dt><code>long bpf_sock_map_update(struct bpf_sock_ops *</code><i>skops</i><code>, struct bpf_map *</code><i>map</i><code>, void *</code><i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Add an entry to, or update a <i>map</i> referencing sockets. The <i>skops</i> is used as a new value for the entry associated to <i>key</i>. <i>flags</i> is one of:</p>
<dt><code>BPF_NOEXIST</code></p>
<dd>The entry for <i>key</i> must not exist in the map.</p>
<dt><code>BPF_EXIST</code></p>
<dd>The entry for <i>key</i> must already exist in the map.</p>
<dt><code>BPF_ANY</code></p>
<dd>No condition on the existence of the entry for <i>key</i>. </p>
<p> If the <i>map</i> has eBPF programs (parser and verdict), those will be inherited by the socket being added. If the socket is already attached to eBPF programs, this results in an error.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_xdp_adjust_meta(struct xdp_buff *</code><i>xdp_md</i><code>, int</code> <i>delta</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Adjust the address pointed by <i>xdp_md</i><code>-&gt;data_meta</code> by <i>delta</i> (which can be positive or negative). Note that this operation modifies the address stored in <i>xdp_md</i><code>-&gt;data</code>, so the latter must be loaded only after the helper has been called. </p>
<p> The use of <i>xdp_md</i><code>-&gt;data_meta</code> is optional and programs are not required to use it. The rationale is that when the packet is processed with XDP (e.g. as DoS filter), it is possible to push further meta data along with it before passing to the stack, and to give the guarantee that an ingress eBPF program attached as a TC classifier on the same device can pick this up for further post-processing. Since TC works with socket buffers, it remains possible to set from XDP the <code>mark</code> or <code>priority</code> pointers, or other pointers for the socket buffer. Having this scratch space generic and programmable allows for more flexibility as the user is free to store whatever meta data they need. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_perf_event_read_value(struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>, struct bpf_perf_event_value *</code><i>buf</i><code>, u32</code> <i>buf_size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Read the value of a perf event counter, and store it into <i>buf</i> of size <i>buf_size</i>. This helper relies on a <i>map</i> of type <code>BPF_MAP_TYPE_PERF_EVENT_ARRAY</code>. The nature of the perf event counter is selected when <i>map</i> is updated with perf event file descriptors. The <i>map</i> is an array whose size is the number of available CPUs, and each cell contains a value relative to one CPU. The value to retrieve is indicated by <i>flags</i>, that contains the index of the CPU to look up, masked with <code>BPF_F_INDEX_MASK</code>. Alternatively, <i>flags</i> can be set to <code>BPF_F_CURRENT_CPU</code> to indicate that the value for the current CPU should be retrieved. </p>
<p> This helper behaves in a way close to <code>bpf_perf_event_read</code>() helper, save that instead of just returning the value observed, it fills the <i>buf</i> structure. This allows for additional data to be retrieved: in particular, the enabled and running times (in <i>buf</i><code>-&gt;enabled</code> and <i>buf</i><code>-&gt;running</code>, respectively) are copied. In general, <code>bpf_perf_event_read_value</code>() is recommended over <code>bpf_perf_event_read</code>(), which has some ABI issues and provides fewer functionalities. </p>
<p> These values are interesting, because hardware PMU (Performance Monitoring Unit) counters are limited resources. When there are more PMU based perf events opened than available counters, kernel will multiplex these events so each event gets certain percentage (but not all) of the PMU time. In case that multiplexing happens, the number of samples or counter value will not reflect the case compared to when no multiplexing occurs. This makes comparison between different runs difficult. Typically, the counter value should be normalized before comparing to other experiments. The usual normalization is done as follows. </p>
<pre>normalized_counter = counter * t_enabled / t_running</pre>
<p>Where t_enabled is the time enabled for event and t_running is the time running for event since last normalization. The enabled and running times are accumulated since the perf event open. To achieve scaling factor between two invocations of an eBPF program, users can use CPU id as the key (which is typical for perf array usage model) to remember the previous value and do the calculation inside the eBPF program.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_perf_prog_read_value(struct bpf_perf_event_data *</code><i>ctx</i><code>, struct bpf_perf_event_value *</code><i>buf</i><code>, u32</code> <i>buf_size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For en eBPF program attached to a perf event, retrieve the value of the event counter associated to <i>ctx</i> and store it in the structure pointed by <i>buf</i> and of size <i>buf_size</i>. Enabled and running times are also stored in the structure (see description of helper <code>bpf_perf_event_read_value</code>() for more details).</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_getsockopt(void *</code><i>bpf_socket</i><code>, int</code> <i>level</i><code>, int</code> <i>optname</i><code>, void *</code><i>optval</i><code>, int</code> <i>optlen</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Emulate a call to <code>getsockopt()</code> on the socket associated to <i>bpf_socket</i>, which must be a full socket. The <i>level</i> at which the option resides and the name <i>optname</i> of the option must be specified, see <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a>(2)</code> for more information. The retrieved value is stored in the structure pointed by <i>opval</i> and of length <i>optlen</i>. </p>
<p> <i>bpf_socket</i> should be one of the following:</p>
<dt>&bull;</p>
<dd><code>struct bpf_sock_ops</code> for <code>BPF_PROG_TYPE_SOCK_OPS</code>.</p>
<dt>&bull;</p>
<dd><code>struct bpf_sock_addr</code> for <code>BPF_CGROUP_INET4_CONNECT</code> and <code>BPF_CGROUP_INET6_CONNECT</code>. </p>
<p> This helper actually implements a subset of <code>getsockopt()</code>. It supports the following <i>level</i>s:</p>
<dt>&bull;</p>
<dd><code>IPPROTO_TCP</code>, which supports <i>optname</i> <code>TCP_CONGESTION</code>.</p>
<dt>&bull;</p>
<dd><code>IPPROTO_IP</code>, which supports <i>optname</i> <code>IP_TOS</code>.</p>
<dt>&bull;</p>
<dd><code>IPPROTO_IPV6</code>, which supports <i>optname</i> <code>IPV6_TCLASS</code>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_override_return(struct pt_regs *</code><i>regs</i><code>, u64</code> <i>rc</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Used for error injection, this helper uses kprobes to override the return value of the probed function, and to set it to <i>rc</i>. The first argument is the context <i>regs</i> on which the kprobe works. </p>
<p> This helper works by setting the PC (program counter) to an override function which is run in place of the original probed function. This means the probed function is not run at all. The replacement function just returns with the required value. </p>
<p> This helper has security implications, and thus is subject to restrictions. It is only available if the kernel was compiled with the <code>CONFIG_BPF_KPROBE_OVERRIDE</code> configuration option, and in this case it only works on functions tagged with <code>ALLOW_ERROR_INJECTION</code> in the kernel code. </p>
<p> Also, the helper is only available for the architectures having the CONFIG_FUNCTION_ERROR_INJECTION option. As of this writing, x86 architecture is the only one to support this feature.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_sock_ops_cb_flags_set(struct bpf_sock_ops *</code><i>bpf_sock</i><code>, int</code> <i>argval</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Attempt to set the value of the <code>bpf_sock_ops_cb_flags</code> field for the full TCP socket associated to <i>bpf_sock_ops</i> to <i>argval</i>. </p>
<p> The primary use of this field is to determine if there should be calls to eBPF programs of type <code>BPF_PROG_TYPE_SOCK_OPS</code> at various points in the TCP code. A program of the same type can change its value, per connection and as necessary, when the connection is established. This field is directly accessible for reading, but this helper must be used for updates in order to return an error if an eBPF program tries to set a callback that is not supported in the current kernel. </p>
<p> <i>argval</i> is a flag array which can combine these flags:</p>
<dt>&bull;</p>
<dd><code>BPF_SOCK_OPS_RTO_CB_FLAG</code> (retransmission time out)</p>
<dt>&bull;</p>
<dd><code>BPF_SOCK_OPS_RETRANS_CB_FLAG</code> (retransmission)</p>
<dt>&bull;</p>
<dd><code>BPF_SOCK_OPS_STATE_CB_FLAG</code> (TCP state change)</p>
<dt>&bull;</p>
<dd><code>BPF_SOCK_OPS_RTT_CB_FLAG</code> (every RTT) </p>
<p> Therefore, this function can be used to clear a callback flag by setting the appropriate bit to zero. e.g. to disable the RTO callback:</p>
<dt><code>bpf_sock_ops_cb_flags_set(bpf_sock,</code></p>
<dd><code>bpf_sock-&gt;bpf_sock_ops_cb_flags &amp; ~BPF_SOCK_OPS_RTO_CB_FLAG)</code> </p>
<p> Here are some examples of where one could call such eBPF program:</p>
<dt>&bull;</p>
<dd>When RTO fires.</p>
<dt>&bull;</p>
<dd>When a packet is retransmitted.</p>
<dt>&bull;</p>
<dd>When the connection terminates.</p>
<dt>&bull;</p>
<dd>When a packet is sent.</p>
<dt>&bull;</p>
<dd>When a packet is received.</p>
<dt><code>Return</code></p>
<dd>Code <code>-EINVAL</code> if the socket is not a full TCP socket; otherwise, a positive number containing the bits that could not be set is returned (which comes down to 0 if all bits were set as required).</p>
<dt><code>long bpf_msg_redirect_map(struct sk_msg_buff *</code><i>msg</i><code>, struct bpf_map *</code><i>map</i><code>, u32</code> <i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing policies at the socket level. If the message <i>msg</i> is allowed to pass (i.e. if the verdict eBPF program returns <code>SK_PASS</code>), redirect it to the socket referenced by <i>map</i> (of type <code>BPF_MAP_TYPE_SOCKMAP</code>) at index <i>key</i>. Both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress path otherwise). This is the only flag supported for now.</p>
<dt><code>Return</code></p>
<dd><code>SK_PASS</code> on success, or <code>SK_DROP</code> on error.</p>
<dt><code>long bpf_msg_apply_bytes(struct sk_msg_buff *</code><i>msg</i><code>, u32</code> <i>bytes</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For socket policies, apply the verdict of the eBPF program to the next <i>bytes</i> (number of bytes) of message <i>msg</i>. </p>
<p> For example, this helper can be used in the following cases:</p>
<dt>&bull;</p>
<dd>A single <code>sendmsg</code>() or <code>sendfile</code>() system call contains multiple logical messages that the eBPF program is supposed to read and for which it should apply a verdict.</p>
<dt>&bull;</p>
<dd>An eBPF program only cares to read the first <i>bytes</i> of a <i>msg</i>. If the message has a large payload, then setting up and calling the eBPF program repeatedly for all bytes, even though the verdict is already known, would create unnecessary overhead. </p>
<p> When called from within an eBPF program, the helper sets a counter internal to the BPF infrastructure, that is used to apply the last verdict to the next <i>bytes</i>. If <i>bytes</i> is smaller than the current data being processed from a <code>sendmsg</code>() or <code>sendfile</code>() system call, the first <i>bytes</i> will be sent and the eBPF program will be re-run with the pointer for start of data pointing to byte number <i>bytes</i> <code>+ 1</code>. If <i>bytes</i> is larger than the current data being processed, then the eBPF verdict will be applied to multiple <code>sendmsg</code>() or <code>sendfile</code>() calls until <i>bytes</i> are consumed. </p>
<p> Note that if a socket closes with the internal counter holding a non-zero value, this is not a problem because data is not being buffered for <i>bytes</i> and is sent as it is received.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_msg_cork_bytes(struct sk_msg_buff *</code><i>msg</i><code>, u32</code> <i>bytes</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For socket policies, prevent the execution of the verdict eBPF program for message <i>msg</i> until <i>bytes</i> (byte number) have been accumulated. </p>
<p> This can be used when one needs a specific number of bytes before a verdict can be assigned, even if the data spans multiple <code>sendmsg</code>() or <code>sendfile</code>() calls. The extreme case would be a user calling <code>sendmsg</code>() repeatedly with 1-byte long message segments. Obviously, this is bad for performance, but it is still valid. If the eBPF program needs <i>bytes</i> bytes to validate a header, this helper can be used to prevent the eBPF program to be called again until <i>bytes</i> have been accumulated.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_msg_pull_data(struct sk_msg_buff *</code><i>msg</i><code>, u32</code> <i>start</i><code>, u32</code> <i>end</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For socket policies, pull in non-linear data from user space for <i>msg</i> and set pointers <i>msg</i><code>-&gt;data</code> and <i>msg</i><code>-&gt;data_end</code> to <i>start</i> and <i>end</i> bytes offsets into <i>msg</i>, respectively. </p>
<p> If a program of type <code>BPF_PROG_TYPE_SK_MSG</code> is run on a <i>msg</i> it can only parse data that the (<code>data</code>, <code>data_end</code>) pointers have already consumed. For <code>sendmsg</code>() hooks this is likely the first scatterlist element. But for calls relying on the <code>sendpage</code> handler (e.g. <code>sendfile</code>()) this will be the range (<code>0</code>, <code>0</code>) because the data is shared with user space and by default the objective is to avoid allowing user space to modify data while (or after) eBPF verdict is being decided. This helper can be used to pull in data and to set the start and end pointer to given values. Data will be copied if necessary (i.e. if data was not linear and if start and end pointers do not point to the same chunk). </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_bind(struct bpf_sock_addr *</code><i>ctx</i><code>, struct sockaddr *</code><i>addr</i><code>, int</code> <i>addr_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Bind the socket associated to <i>ctx</i> to the address pointed by <i>addr</i>, of length <i>addr_len</i>. This allows for making outgoing connection from the desired IP address, which can be useful for example when all processes inside a cgroup should use one single IP address on a host that has multiple IP configured. </p>
<p> This helper works for IPv4 and IPv6, TCP and UDP sockets. The domain (<i>addr</i><code>-&gt;sa_family</code>) must be <code>AF_INET</code> (or <code>AF_INET6</code>). It&#8217;s advised to pass zero port (<code>sin_port</code> or <code>sin6_port</code>) which triggers IP_BIND_ADDRESS_NO_PORT-like behavior and lets the kernel efficiently pick up an unused port as long as 4-tuple is unique. Passing non-zero port might lead to degraded performance.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_xdp_adjust_tail(struct xdp_buff *</code><i>xdp_md</i><code>, int</code> <i>delta</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Adjust (move) <i>xdp_md</i><code>-&gt;data_end</code> by <i>delta</i> bytes. It is possible to both shrink and grow the packet tail. Shrink done via <i>delta</i> being a negative integer. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_get_xfrm_state(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>index</i><code>, struct bpf_xfrm_state *</code><i>xfrm_state</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve the XFRM state (IP transform framework, see also <code><a href="/docs/linux/man/8-ip-xfrm/">ip-xfrm</a>(8)</code>) at <i>index</i> in XFRM &quot;security path&quot; for <i>skb</i>. </p>
<p> The retrieved value is stored in the <code>struct bpf_xfrm_state</code> pointed by <i>xfrm_state</i> and of length <i>size</i>. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> This helper is available only if the kernel was compiled with <code>CONFIG_XFRM</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_get_stack(void *</code><i>ctx</i><code>, void *</code><i>buf</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return a user or a kernel stack in bpf program provided buffer. To achieve this, the helper needs <i>ctx</i>, which is a pointer to the context on which the tracing program is executed. To store the stacktrace, the bpf program provides <i>buf</i> with a nonnegative <i>size</i>. </p>
<p> The last argument, <i>flags</i>, holds the number of stack frames to skip (from 0 to 255), masked with <code>BPF_F_SKIP_FIELD_MASK</code>. The next bits can be used to set the following flags:</p>
<dt><code>BPF_F_USER_STACK</code></p>
<dd>Collect a user space stack instead of a kernel stack.</p>
<dt><code>BPF_F_USER_BUILD_ID</code></p>
<dd>Collect buildid+offset instead of ips for user stack, only valid if <code>BPF_F_USER_STACK</code> is also specified. </p>
<p> <code>bpf_get_stack</code>() can collect up to <code>PERF_MAX_STACK_DEPTH</code> both kernel and user frames, subject to sufficient large buffer size. Note that this limit can be controlled with the <code>sysctl</code> program, and that it should be manually increased in order to profile long user stacks (such as stacks for Java programs). To do so, use: </p>
<pre># sysctl kernel.perf_event_max_stack=&lt;new value&gt;</pre>
<dt><code>Return</code></p>
<dd>A non-negative value equal to or less than <i>size</i> on success, or a negative error in case of failure.</p>
<dt><code>long bpf_skb_load_bytes_relative(const void *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, void *</code><i>to</i><code>, u32</code> <i>len</i><code>, u32</code> <i>start_header</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is similar to <code>bpf_skb_load_bytes</code>() in that it provides an easy way to load <i>len</i> bytes from <i>offset</i> from the packet associated to <i>skb</i>, into the buffer pointed by <i>to</i>. The difference to <code>bpf_skb_load_bytes</code>() is that a fifth argument <i>start_header</i> exists in order to select a base offset to start from. <i>start_header</i> can be one of:</p>
<dt><code>BPF_HDR_START_MAC</code></p>
<dd>Base offset to load data from is <i>skb</i>&#8216;s mac header.</p>
<dt><code>BPF_HDR_START_NET</code></p>
<dd>Base offset to load data from is <i>skb</i>&#8216;s network header. </p>
<p> In general, &quot;direct packet access&quot; is the preferred method to access packet data, however, this helper is in particular useful in socket filters where <i>skb</i><code>-&gt;data</code> does not always point to the start of the mac header and where &quot;direct packet access&quot; is not available.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_fib_lookup(void *</code><i>ctx</i><code>, struct bpf_fib_lookup *</code><i>params</i><code>, int</code> <i>plen</i><code>, u32</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Do FIB lookup in kernel tables using parameters in <i>params</i>. If lookup is successful and result shows packet is to be forwarded, the neighbor tables are searched for the nexthop. If successful (ie., FIB lookup shows forwarding and nexthop is resolved), the nexthop address is returned in ipv4_dst or ipv6_dst based on family, smac is set to mac address of egress device, dmac is set to nexthop mac address, rt_metric is set to metric from route (IPv4/IPv6 only), and ifindex is set to the device index of the nexthop from the FIB lookup. </p>
<p> <i>plen</i> argument is the size of the passed in struct. <i>flags</i> argument can be a combination of one or more of the following values:</p>
<dt><code>BPF_FIB_LOOKUP_DIRECT</code></p>
<dd>Do a direct table lookup vs full lookup using FIB rules.</p>
<dt><code>BPF_FIB_LOOKUP_OUTPUT</code></p>
<dd>Perform lookup from an egress perspective (default is ingress). </p>
<p> <i>ctx</i> is either <code>struct xdp_md</code> for XDP programs or <code>struct sk_buff</code> tc cls_act programs.</p>
<dt><code>Return</code></p>
<dd>
<dt>&bull;</p>
<dd>&lt; 0 if any input argument is invalid</p>
<dt>&bull;</p>
<dd>0 on success (packet is forwarded, nexthop neighbor exists)</p>
<dt>&bull;</p>
<dd>&gt; 0 one of <code>BPF_FIB_LKUP_RET_</code> codes explaining why the packet is not forwarded or needs assist from full stack</p>
<dt><code>long bpf_sock_hash_update(struct bpf_sock_ops *</code><i>skops</i><code>, struct bpf_map *</code><i>map</i><code>, void *</code><i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Add an entry to, or update a sockhash <i>map</i> referencing sockets. The <i>skops</i> is used as a new value for the entry associated to <i>key</i>. <i>flags</i> is one of:</p>
<dt><code>BPF_NOEXIST</code></p>
<dd>The entry for <i>key</i> must not exist in the map.</p>
<dt><code>BPF_EXIST</code></p>
<dd>The entry for <i>key</i> must already exist in the map.</p>
<dt><code>BPF_ANY</code></p>
<dd>No condition on the existence of the entry for <i>key</i>. </p>
<p> If the <i>map</i> has eBPF programs (parser and verdict), those will be inherited by the socket being added. If the socket is already attached to eBPF programs, this results in an error.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_msg_redirect_hash(struct sk_msg_buff *</code><i>msg</i><code>, struct bpf_map *</code><i>map</i><code>, void *</code><i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing policies at the socket level. If the message <i>msg</i> is allowed to pass (i.e. if the verdict eBPF program returns <code>SK_PASS</code>), redirect it to the socket referenced by <i>map</i> (of type <code>BPF_MAP_TYPE_SOCKHASH</code>) using hash <i>key</i>. Both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress path otherwise). This is the only flag supported for now.</p>
<dt><code>Return</code></p>
<dd><code>SK_PASS</code> on success, or <code>SK_DROP</code> on error.</p>
<dt><code>long bpf_sk_redirect_hash(struct sk_buff *</code><i>skb</i><code>, struct bpf_map *</code><i>map</i><code>, void *</code><i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing policies at the skb socket level. If the sk_buff <i>skb</i> is allowed to pass (i.e. if the verdict eBPF program returns <code>SK_PASS</code>), redirect it to the socket referenced by <i>map</i> (of type <code>BPF_MAP_TYPE_SOCKHASH</code>) using hash <i>key</i>. Both ingress and egress interfaces can be used for redirection. The <code>BPF_F_INGRESS</code> value in <i>flags</i> is used to make the distinction (ingress path is selected if the flag is present, egress otherwise). This is the only flag supported for now.</p>
<dt><code>Return</code></p>
<dd><code>SK_PASS</code> on success, or <code>SK_DROP</code> on error.</p>
<dt><code>long bpf_lwt_push_encap(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>type</i><code>, void *</code><i>hdr</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Encapsulate the packet associated to <i>skb</i> within a Layer 3 protocol header. This header is provided in the buffer at address <i>hdr</i>, with <i>len</i> its size in bytes. <i>type</i> indicates the protocol of the header and can be one of:</p>
<dt><code>BPF_LWT_ENCAP_SEG6</code></p>
<dd>IPv6 encapsulation with Segment Routing Header (<code>struct ipv6_sr_hdr</code>). <i>hdr</i> only contains the SRH, the IPv6 header is computed by the kernel.</p>
<dt><code>BPF_LWT_ENCAP_SEG6_INLINE</code></p>
<dd>Only works if <i>skb</i> contains an IPv6 packet. Insert a Segment Routing Header (<code>struct ipv6_sr_hdr</code>) inside the IPv6 header.</p>
<dt><code>BPF_LWT_ENCAP_IP</code></p>
<dd>IP encapsulation (GRE/GUE/IPIP/etc). The outer header must be IPv4 or IPv6, followed by zero or more additional headers, up to <code>LWT_BPF_MAX_HEADROOM</code> total bytes in all prepended headers. Please note that if <code>skb_is_gso</code>(<i>skb</i>) is true, no more than two headers can be prepended, and the inner header, if present, should be either GRE or UDP/GUE. </p>
<p> <code>BPF_LWT_ENCAP_SEG6</code>* types can be called by BPF programs of type <code>BPF_PROG_TYPE_LWT_IN</code>; <code>BPF_LWT_ENCAP_IP</code> type can be called by bpf programs of types <code>BPF_PROG_TYPE_LWT_IN</code> and <code>BPF_PROG_TYPE_LWT_XMIT</code>. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_lwt_seg6_store_bytes(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, const void *</code><i>from</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Store <i>len</i> bytes from address <i>from</i> into the packet associated to <i>skb</i>, at <i>offset</i>. Only the flags, tag and TLVs inside the outermost IPv6 Segment Routing Header can be modified through this helper. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_lwt_seg6_adjust_srh(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>offset</i><code>, s32</code> <i>delta</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Adjust the size allocated to TLVs in the outermost IPv6 Segment Routing Header contained in the packet associated to <i>skb</i>, at position <i>offset</i> by <i>delta</i> bytes. Only offsets after the segments are accepted. <i>delta</i> can be as well positive (growing) as negative (shrinking). </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_lwt_seg6_action(struct sk_buff *</code><i>skb</i><code>, u32</code> <i>action</i><code>, void *</code><i>param</i><code>, u32</code> <i>param_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Apply an IPv6 Segment Routing action of type <i>action</i> to the packet associated to <i>skb</i>. Each action takes a parameter contained at address <i>param</i>, and of length <i>param_len</i> bytes. <i>action</i> can be one of:</p>
<dt><code>SEG6_LOCAL_ACTION_END_X</code></p>
<dd>End.X action: Endpoint with Layer-3 cross-connect. Type of <i>param</i>: <code>struct in6_addr</code>.</p>
<dt><code>SEG6_LOCAL_ACTION_END_T</code></p>
<dd>End.T action: Endpoint with specific IPv6 table lookup. Type of <i>param</i>: <code>int</code>.</p>
<dt><code>SEG6_LOCAL_ACTION_END_B6</code></p>
<dd>End.B6 action: Endpoint bound to an SRv6 policy. Type of <i>param</i>: <code>struct ipv6_sr_hdr</code>.</p>
<dt><code>SEG6_LOCAL_ACTION_END_B6_ENCAP</code></p>
<dd>End.B6.Encap action: Endpoint bound to an SRv6 encapsulation policy. Type of <i>param</i>: <code>struct ipv6_sr_hdr</code>. </p>
<p> A call to this helper is susceptible to change the underlying packet buffer. Therefore, at load time, all checks on pointers previously done by the verifier are invalidated and must be performed again, if the helper is used in combination with direct packet access.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_rc_repeat(void *</code><i>ctx</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing IR decoding, to report a successfully decoded repeat key message. This delays the generation of a key up event for previously generated key down event. </p>
<p> Some IR protocols like NEC have a special IR message for repeating last button, for when a button is held down. </p>
<p> The <i>ctx</i> should point to the lirc sample as passed into the program. </p>
<p> This helper is only available is the kernel was compiled with the <code>CONFIG_BPF_LIRC_MODE2</code> configuration option set to &quot;<code>y</code>&quot;.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_rc_keydown(void *</code><i>ctx</i><code>, u32</code> <i>protocol</i><code>, u64</code> <i>scancode</i><code>, u32</code> <i>toggle</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing IR decoding, to report a successfully decoded key press with <i>scancode</i>, <i>toggle</i> value in the given <i>protocol</i>. The scancode will be translated to a keycode using the rc keymap, and reported as an input key down event. After a period a key up event is generated. This period can be extended by calling either <code>bpf_rc_keydown</code>() again with the same values, or calling <code>bpf_rc_repeat</code>(). </p>
<p> Some protocols include a toggle bit, in case the button was released and pressed again between consecutive scancodes. </p>
<p> The <i>ctx</i> should point to the lirc sample as passed into the program. </p>
<p> The <i>protocol</i> is the decoded protocol number (see <code>enum rc_proto</code> for some predefined values). </p>
<p> This helper is only available is the kernel was compiled with the <code>CONFIG_BPF_LIRC_MODE2</code> configuration option set to &quot;<code>y</code>&quot;.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>u64 bpf_skb_cgroup_id(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return the cgroup v2 id of the socket associated with the <i>skb</i>. This is roughly similar to the <code>bpf_get_cgroup_classid</code>() helper for cgroup v1 by providing a tag resp. identifier that can be matched on or used for map lookups e.g. to implement policy. The cgroup v2 id of a given path in the hierarchy is exposed in user space through the f_handle API in order to get to the same 64-bit id. </p>
<p> This helper can be used on TC egress path, but not on ingress, and is available only if the kernel was compiled with the <code>CONFIG_SOCK_CGROUP_DATA</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>The id is returned or 0 in case the id could not be retrieved.</p>
<dt><code>u64 bpf_get_current_cgroup_id(void)</code></p>
<dd>
<dt><code>Return</code></p>
<dd>A 64-bit integer containing the current cgroup id based on the cgroup within which the current task is running.</p>
<dt><code>void *bpf_get_local_storage(void *</code><i>map</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get the pointer to the local storage area. The type and the size of the local storage is defined by the <i>map</i> argument. The <i>flags</i> meaning is specific for each map type, and has to be 0 for cgroup local storage. </p>
<p> Depending on the BPF program type, a local storage area can be shared between multiple instances of the BPF program, running simultaneously. </p>
<p> A user should care about the synchronization by himself. For example, by using the <code>BPF_STX_XADD</code> instruction to alter the shared data.</p>
<dt><code>Return</code></p>
<dd>A pointer to the local storage area.</p>
<dt><code>long bpf_sk_select_reuseport(struct sk_reuseport_md *</code><i>reuse</i><code>, struct bpf_map *</code><i>map</i><code>, void *</code><i>key</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Select a <code>SO_REUSEPORT</code> socket from a <code>BPF_MAP_TYPE_REUSEPORT_ARRAY</code> <i>map</i>. It checks the selected socket is matching the incoming request in the socket buffer.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u64 bpf_skb_ancestor_cgroup_id(struct sk_buff *</code><i>skb</i><code>, int</code> <i>ancestor_level</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return id of cgroup v2 that is ancestor of cgroup associated with the <i>skb</i> at the <i>ancestor_level</i>. The root cgroup is at <i>ancestor_level</i> zero and each step down the hierarchy increments the level. If <i>ancestor_level</i> == level of cgroup associated with <i>skb</i>, then return value will be same as that of <code>bpf_skb_cgroup_id</code>(). </p>
<p> The helper is useful to implement policies based on cgroups that are upper in hierarchy than immediate cgroup associated with <i>skb</i>. </p>
<p> The format of returned id and helper limitations are same as in <code>bpf_skb_cgroup_id</code>().</p>
<dt><code>Return</code></p>
<dd>The id is returned or 0 in case the id could not be retrieved.</p>
<dt><code>struct bpf_sock *bpf_sk_lookup_tcp(void *</code><i>ctx</i><code>, struct bpf_sock_tuple *</code><i>tuple</i><code>, u32</code> <i>tuple_size</i><code>, u64</code> <i>netns</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Look for TCP socket matching <i>tuple</i>, optionally in a child network namespace <i>netns</i>. The return value must be checked, and if non-<code>NULL</code>, released via <code>bpf_sk_release</code>(). </p>
<p> The <i>ctx</i> should point to the context of the program, such as the skb or socket (depending on the hook in use). This is used to determine the base network namespace for the lookup. </p>
<p> <i>tuple_size</i> must be one of:</p>
<dt><code>sizeof</code>(<i>tuple</i><code>-&gt;ipv4</code>)</p>
<dd>Look for an IPv4 socket.</p>
<dt><code>sizeof</code>(<i>tuple</i><code>-&gt;ipv6</code>)</p>
<dd>Look for an IPv6 socket. </p>
<p> If the <i>netns</i> is a negative signed 32-bit integer, then the socket lookup table in the netns associated with the <i>ctx</i> will be used. For the TC hooks, this is the netns of the device in the skb. For socket hooks, this is the netns of the socket. If <i>netns</i> is any other signed 32-bit value greater than or equal to zero then it specifies the ID of the netns relative to the netns associated with the <i>ctx</i>. <i>netns</i> values beyond the range of 32-bit integers are reserved for future use. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> This helper is available only if the kernel was compiled with <code>CONFIG_NET</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>Pointer to <code>struct bpf_sock</code>, or <code>NULL</code> in case of failure. For sockets with reuseport option, the <code>struct bpf_sock</code> result is from <i>reuse</i><code>-&gt;socks</code>[] using the hash of the tuple.</p>
<dt><code>struct bpf_sock *bpf_sk_lookup_udp(void *</code><i>ctx</i><code>, struct bpf_sock_tuple *</code><i>tuple</i><code>, u32</code> <i>tuple_size</i><code>, u64</code> <i>netns</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Look for UDP socket matching <i>tuple</i>, optionally in a child network namespace <i>netns</i>. The return value must be checked, and if non-<code>NULL</code>, released via <code>bpf_sk_release</code>(). </p>
<p> The <i>ctx</i> should point to the context of the program, such as the skb or socket (depending on the hook in use). This is used to determine the base network namespace for the lookup. </p>
<p> <i>tuple_size</i> must be one of:</p>
<dt><code>sizeof</code>(<i>tuple</i><code>-&gt;ipv4</code>)</p>
<dd>Look for an IPv4 socket.</p>
<dt><code>sizeof</code>(<i>tuple</i><code>-&gt;ipv6</code>)</p>
<dd>Look for an IPv6 socket. </p>
<p> If the <i>netns</i> is a negative signed 32-bit integer, then the socket lookup table in the netns associated with the <i>ctx</i> will be used. For the TC hooks, this is the netns of the device in the skb. For socket hooks, this is the netns of the socket. If <i>netns</i> is any other signed 32-bit value greater than or equal to zero then it specifies the ID of the netns relative to the netns associated with the <i>ctx</i>. <i>netns</i> values beyond the range of 32-bit integers are reserved for future use. </p>
<p> All values for <i>flags</i> are reserved for future usage, and must be left at zero. </p>
<p> This helper is available only if the kernel was compiled with <code>CONFIG_NET</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>Pointer to <code>struct bpf_sock</code>, or <code>NULL</code> in case of failure. For sockets with reuseport option, the <code>struct bpf_sock</code> result is from <i>reuse</i><code>-&gt;socks</code>[] using the hash of the tuple.</p>
<dt><code>long bpf_sk_release(struct bpf_sock *</code><i>sock</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Release the reference held by <i>sock</i>. <i>sock</i> must be a non-<code>NULL</code> pointer that was returned from <code>bpf_sk_lookup_xxx</code>().</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_map_push_elem(struct bpf_map *</code><i>map</i><code>, const void *</code><i>value</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Push an element <i>value</i> in <i>map</i>. <i>flags</i> is one of:</p>
<dt><code>BPF_EXIST</code></p>
<dd>If the queue/stack is full, the oldest element is removed to make room for this.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_map_pop_elem(struct bpf_map *</code><i>map</i><code>, void *</code><i>value</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Pop an element from <i>map</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_map_peek_elem(struct bpf_map *</code><i>map</i><code>, void *</code><i>value</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get an element from <i>map</i> without removing it.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_msg_push_data(struct sk_msg_buff *</code><i>msg</i><code>, u32</code> <i>start</i><code>, u32</code> <i>len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For socket policies, insert <i>len</i> bytes into <i>msg</i> at offset <i>start</i>. </p>
<p> If a program of type <code>BPF_PROG_TYPE_SK_MSG</code> is run on a <i>msg</i> it may want to insert metadata or options into the <i>msg</i>. This can later be read and used by any of the lower layer BPF hooks. </p>
<p> This helper may fail if under memory pressure (a malloc fails) in these cases BPF programs will get an appropriate error and BPF programs will need to handle them.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_msg_pop_data(struct sk_msg_buff *</code><i>msg</i><code>, u32</code> <i>start</i><code>, u32</code> <i>len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Will remove <i>len</i> bytes from a <i>msg</i> starting at byte <i>start</i>. This may result in <code>ENOMEM</code> errors under certain situations if an allocation and copy are required due to a full ring buffer. However, the helper will try to avoid doing the allocation if possible. Other errors can occur if input parameters are invalid either due to <i>start</i> byte not being valid part of <i>msg</i> payload and/or <i>pop</i> value being to large.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_rc_pointer_rel(void *</code><i>ctx</i><code>, s32</code> <i>rel_x</i><code>, s32</code> <i>rel_y</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper is used in programs implementing IR decoding, to report a successfully decoded pointer movement. </p>
<p> The <i>ctx</i> should point to the lirc sample as passed into the program. </p>
<p> This helper is only available is the kernel was compiled with the <code>CONFIG_BPF_LIRC_MODE2</code> configuration option set to &quot;<code>y</code>&quot;.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_spin_lock(struct bpf_spin_lock *</code><i>lock</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Acquire a spinlock represented by the pointer <i>lock</i>, which is stored as part of a value of a map. Taking the lock allows to safely update the rest of the fields in that value. The spinlock can (and must) later be released with a call to <code>bpf_spin_unlock</code>(<i>lock</i>). </p>
<p> Spinlocks in BPF programs come with a number of restrictions and constraints:</p>
<dt>&bull;</p>
<dd><code>bpf_spin_lock</code> objects are only allowed inside maps of types <code>BPF_MAP_TYPE_HASH</code> and <code>BPF_MAP_TYPE_ARRAY</code> (this list could be extended in the future).</p>
<dt>&bull;</p>
<dd>BTF description of the map is mandatory.</p>
<dt>&bull;</p>
<dd>The BPF program can take ONE lock at a time, since taking two or more could cause dead locks.</p>
<dt>&bull;</p>
<dd>Only one <code>struct bpf_spin_lock</code> is allowed per map element.</p>
<dt>&bull;</p>
<dd>When the lock is taken, calls (either BPF to BPF or helpers) are not allowed.</p>
<dt>&bull;</p>
<dd>The <code>BPF_LD_ABS</code> and <code>BPF_LD_IND</code> instructions are not allowed inside a spinlock-ed region.</p>
<dt>&bull;</p>
<dd>The BPF program MUST call <code>bpf_spin_unlock</code>() to release the lock, on all execution paths, before it returns.</p>
<dt>&bull;</p>
<dd>The BPF program can access <code>struct bpf_spin_lock</code> only via the <code>bpf_spin_lock</code>() and <code>bpf_spin_unlock</code>() helpers. Loading or storing data into the <code>struct bpf_spin_lock</code> <i>lock</i><code>;</code> field of a map is not allowed.</p>
<dt>&bull;</p>
<dd>To use the <code>bpf_spin_lock</code>() helper, the BTF description of the map value must be a struct and have <code>struct bpf_spin_lock</code> <i>anyname</i><code>;</code> field at the top level. Nested lock inside another struct is not allowed.</p>
<dt>&bull;</p>
<dd>The <code>struct bpf_spin_lock</code> <i>lock</i> field in a map value must be aligned on a multiple of 4 bytes in that value.</p>
<dt>&bull;</p>
<dd>Syscall with command <code>BPF_MAP_LOOKUP_ELEM</code> does not copy the <code>bpf_spin_lock</code> field to user space.</p>
<dt>&bull;</p>
<dd>Syscall with command <code>BPF_MAP_UPDATE_ELEM</code>, or update from a BPF program, do not update the <code>bpf_spin_lock</code> field.</p>
<dt>&bull;</p>
<dd><code>bpf_spin_lock</code> cannot be on the stack or inside a networking packet (it can only be inside of a map values).</p>
<dt>&bull;</p>
<dd><code>bpf_spin_lock</code> is available to root only.</p>
<dt>&bull;</p>
<dd>Tracing programs and socket filter programs cannot use <code>bpf_spin_lock</code>() due to insufficient preemption checks (but this may change in the future).</p>
<dt>&bull;</p>
<dd><code>bpf_spin_lock</code> is not allowed in inner maps of map-in-map.</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>long bpf_spin_unlock(struct bpf_spin_lock *</code><i>lock</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Release the <i>lock</i> previously locked by a call to <code>bpf_spin_lock</code>(<i>lock</i>).</p>
<dt><code>Return</code></p>
<dd>0</p>
<dt><code>struct bpf_sock *bpf_sk_fullsock(struct bpf_sock *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper gets a <code>struct bpf_sock</code> pointer such that all the fields in this <code>bpf_sock</code> can be accessed.</p>
<dt><code>Return</code></p>
<dd>A <code>struct bpf_sock</code> pointer on success, or <code>NULL</code> in case of failure.</p>
<dt><code>struct bpf_tcp_sock *bpf_tcp_sock(struct bpf_sock *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>This helper gets a <code>struct bpf_tcp_sock</code> pointer from a <code>struct bpf_sock</code> pointer.</p>
<dt><code>Return</code></p>
<dd>A <code>struct bpf_tcp_sock</code> pointer on success, or <code>NULL</code> in case of failure.</p>
<dt><code>long bpf_skb_ecn_set_ce(struct sk_buff *</code><i>skb</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Set ECN (Explicit Congestion Notification) field of IP header to <code>CE</code> (Congestion Encountered) if current value is <code>ECT</code> (ECN Capable Transport). Otherwise, do nothing. Works with IPv6 and IPv4.</p>
<dt><code>Return</code></p>
<dd>1 if the <code>CE</code> flag is set (either by the current helper call or because it was already present), 0 if it is not set.</p>
<dt><code>struct bpf_sock *bpf_get_listener_sock(struct bpf_sock *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return a <code>struct bpf_sock</code> pointer in <code>TCP_LISTEN</code> state. <code>bpf_sk_release</code>() is unnecessary and not allowed.</p>
<dt><code>Return</code></p>
<dd>A <code>struct bpf_sock</code> pointer on success, or <code>NULL</code> in case of failure.</p>
<dt><code>struct bpf_sock *bpf_skc_lookup_tcp(void *</code><i>ctx</i><code>, struct bpf_sock_tuple *</code><i>tuple</i><code>, u32</code> <i>tuple_size</i><code>, u64</code> <i>netns</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Look for TCP socket matching <i>tuple</i>, optionally in a child network namespace <i>netns</i>. The return value must be checked, and if non-<code>NULL</code>, released via <code>bpf_sk_release</code>(). </p>
<p> This function is identical to <code>bpf_sk_lookup_tcp</code>(), except that it also returns timewait or request sockets. Use <code>bpf_sk_fullsock</code>() or <code>bpf_tcp_sock</code>() to access the full structure. </p>
<p> This helper is available only if the kernel was compiled with <code>CONFIG_NET</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>Pointer to <code>struct bpf_sock</code>, or <code>NULL</code> in case of failure. For sockets with reuseport option, the <code>struct bpf_sock</code> result is from <i>reuse</i><code>-&gt;socks</code>[] using the hash of the tuple.</p>
<dt><code>long bpf_tcp_check_syncookie(struct bpf_sock *</code><i>sk</i><code>, void *</code><i>iph</i><code>, u32</code> <i>iph_len</i><code>, struct tcphdr *</code><i>th</i><code>, u32</code> <i>th_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Check whether <i>iph</i> and <i>th</i> contain a valid SYN cookie ACK for the listening socket in <i>sk</i>. </p>
<p> <i>iph</i> points to the start of the IPv4 or IPv6 header, while <i>iph_len</i> contains <code>sizeof</code>(<code>struct iphdr</code>) or <code>sizeof</code>(<code>struct ip6hdr</code>). </p>
<p> <i>th</i> points to the start of the TCP header, while <i>th_len</i> contains <code>sizeof</code>(<code>struct tcphdr</code>).</p>
<dt><code>Return</code></p>
<dd>0 if <i>iph</i> and <i>th</i> are a valid SYN cookie ACK, or a negative error otherwise.</p>
<dt><code>long bpf_sysctl_get_name(struct bpf_sysctl *</code><i>ctx</i><code>, char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get name of sysctl in /proc/sys/ and copy it into provided by program buffer <i>buf</i> of size <i>buf_len</i>. </p>
<p> The buffer is always NUL terminated, unless it&#8217;s zero-sized. </p>
<p> If <i>flags</i> is zero, full name (e.g. &quot;net/ipv4/tcp_mem&quot;) is copied. Use <code>BPF_F_SYSCTL_BASE_NAME</code> flag to copy base name only (e.g. &quot;tcp_mem&quot;).</p>
<dt><code>Return</code></p>
<dd>Number of character copied (not including the trailing NUL). </p>
<p> <code>-E2BIG</code> if the buffer wasn&#8217;t big enough (<i>buf</i> will contain truncated name in this case).</p>
<dt><code>long bpf_sysctl_get_current_value(struct bpf_sysctl *</code><i>ctx</i><code>, char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get current value of sysctl as it is presented in /proc/sys (incl. newline, etc), and copy it as a string into provided by program buffer <i>buf</i> of size <i>buf_len</i>. </p>
<p> The whole value is copied, no matter what file position user space issued e.g. sys_read at. </p>
<p> The buffer is always NUL terminated, unless it&#8217;s zero-sized.</p>
<dt><code>Return</code></p>
<dd>Number of character copied (not including the trailing NUL). </p>
<p> <code>-E2BIG</code> if the buffer wasn&#8217;t big enough (<i>buf</i> will contain truncated name in this case). </p>
<p> <code>-EINVAL</code> if current value was unavailable, e.g. because sysctl is uninitialized and read returns -EIO for it.</p>
<dt><code>long bpf_sysctl_get_new_value(struct bpf_sysctl *</code><i>ctx</i><code>, char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get new value being written by user space to sysctl (before the actual write happens) and copy it as a string into provided by program buffer <i>buf</i> of size <i>buf_len</i>. </p>
<p> User space may write new value at file position &gt; 0. </p>
<p> The buffer is always NUL terminated, unless it&#8217;s zero-sized.</p>
<dt><code>Return</code></p>
<dd>Number of character copied (not including the trailing NUL). </p>
<p> <code>-E2BIG</code> if the buffer wasn&#8217;t big enough (<i>buf</i> will contain truncated name in this case). </p>
<p> <code>-EINVAL</code> if sysctl is being read.</p>
<dt><code>long bpf_sysctl_set_new_value(struct bpf_sysctl *</code><i>ctx</i><code>, const char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Override new value being written by user space to sysctl with value provided by program in buffer <i>buf</i> of size <i>buf_len</i>. </p>
<p> <i>buf</i> should contain a string in same form as provided by user space on sysctl write. </p>
<p> User space may write new value at file position &gt; 0. To override the whole sysctl value file position should be set to zero.</p>
<dt><code>Return</code></p>
<dd>0 on success. </p>
<p> <code>-E2BIG</code> if the <i>buf_len</i> is too big. </p>
<p> <code>-EINVAL</code> if sysctl is being read.</p>
<dt><code>long bpf_strtol(const char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>, u64</code> <i>flags</i><code>, long *</code><i>res</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Convert the initial part of the string from buffer <i>buf</i> of size <i>buf_len</i> to a long integer according to the given base and save the result in <i>res</i>. </p>
<p> The string may begin with an arbitrary amount of white space (as determined by <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3)) followed by a single optional &#8216;<code>&#8211;</code>&#8216; sign. </p>
<p> Five least significant bits of <i>flags</i> encode base, other bits are currently unused. </p>
<p> Base must be either 8, 10, 16 or 0 to detect it automatically similar to user space <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3).</p>
<dt><code>Return</code></p>
<dd>Number of characters consumed on success. Must be positive but no more than <i>buf_len</i>. </p>
<p> <code>-EINVAL</code> if no valid digits were found or unsupported base was provided. </p>
<p> <code>-ERANGE</code> if resulting value was out of range.</p>
<dt><code>long bpf_strtoul(const char *</code><i>buf</i><code>, size_t</code> <i>buf_len</i><code>, u64</code> <i>flags</i><code>, unsigned long *</code><i>res</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Convert the initial part of the string from buffer <i>buf</i> of size <i>buf_len</i> to an unsigned long integer according to the given base and save the result in <i>res</i>. </p>
<p> The string may begin with an arbitrary amount of white space (as determined by <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3)). </p>
<p> Five least significant bits of <i>flags</i> encode base, other bits are currently unused. </p>
<p> Base must be either 8, 10, 16 or 0 to detect it automatically similar to user space <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3).</p>
<dt><code>Return</code></p>
<dd>Number of characters consumed on success. Must be positive but no more than <i>buf_len</i>. </p>
<p> <code>-EINVAL</code> if no valid digits were found or unsupported base was provided. </p>
<p> <code>-ERANGE</code> if resulting value was out of range.</p>
<dt><code>void *bpf_sk_storage_get(struct bpf_map *</code><i>map</i><code>, struct bpf_sock *</code><i>sk</i><code>, void *</code><i>value</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Get a bpf-local-storage from a <i>sk</i>. </p>
<p> Logically, it could be thought of getting the value from a <i>map</i> with <i>sk</i> as the <code>key</code>. From this perspective, the usage is not much different from <code>bpf_map_lookup_elem</code>(<i>map</i>, <code>&amp;</code><i>sk</i>) except this helper enforces the key must be a full socket and the map must be a <code>BPF_MAP_TYPE_SK_STORAGE</code> also. </p>
<p> Underneath, the value is stored locally at <i>sk</i> instead of the <i>map</i>. The <i>map</i> is used as the bpf-local-storage &quot;type&quot;. The bpf-local-storage &quot;type&quot; (i.e. the <i>map</i>) is searched against all bpf-local-storages residing at <i>sk</i>. </p>
<p> An optional <i>flags</i> (<code>BPF_SK_STORAGE_GET_F_CREATE</code>) can be used such that a new bpf-local-storage will be created if one does not exist. <i>value</i> can be used together with <code>BPF_SK_STORAGE_GET_F_CREATE</code> to specify the initial value of a bpf-local-storage. If <i>value</i> is <code>NULL</code>, the new bpf-local-storage will be zero initialized.</p>
<dt><code>Return</code></p>
<dd>A bpf-local-storage pointer is returned on success. </p>
<p> <code>NULL</code> if not found or there was an error in adding a new bpf-local-storage.</p>
<dt><code>long bpf_sk_storage_delete(struct bpf_map *</code><i>map</i><code>, struct bpf_sock *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Delete a bpf-local-storage from a <i>sk</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success. </p>
<p> <code>-ENOENT</code> if the bpf-local-storage cannot be found.</p>
<dt><code>long bpf_send_signal(u32</code> <i>sig</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Send signal <i>sig</i> to the process of the current task. The signal may be delivered to any of this process&#8217;s threads.</p>
<dt><code>Return</code></p>
<dd>0 on success or successfully queued. </p>
<p> <code>-EBUSY</code> if work queue under nmi is full. </p>
<p> <code>-EINVAL</code> if <i>sig</i> is invalid. </p>
<p> <code>-EPERM</code> if no permission to send the <i>sig</i>. </p>
<p> <code>-EAGAIN</code> if bpf program can try again.</p>
<dt><code>s64 bpf_tcp_gen_syncookie(struct bpf_sock *</code><i>sk</i><code>, void *</code><i>iph</i><code>, u32</code> <i>iph_len</i><code>, struct tcphdr *</code><i>th</i><code>, u32</code> <i>th_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Try to issue a SYN cookie for the packet with corresponding IP/TCP headers, <i>iph</i> and <i>th</i>, on the listening socket in <i>sk</i>. </p>
<p> <i>iph</i> points to the start of the IPv4 or IPv6 header, while <i>iph_len</i> contains <code>sizeof</code>(<code>struct iphdr</code>) or <code>sizeof</code>(<code>struct ip6hdr</code>). </p>
<p> <i>th</i> points to the start of the TCP header, while <i>th_len</i> contains the length of the TCP header.</p>
<dt><code>Return</code></p>
<dd>On success, lower 32 bits hold the generated SYN cookie in followed by 16 bits which hold the MSS value for that cookie, and the top 16 bits are unused. </p>
<p> On failure, the returned value is one of the following: </p>
<p> <code>-EINVAL</code> SYN cookie cannot be issued due to error </p>
<p> <code>-ENOENT</code> SYN cookie should not be issued (no SYN flood) </p>
<p> <code>-EOPNOTSUPP</code> kernel configuration does not enable SYN cookies </p>
<p> <code>-EPROTONOSUPPORT</code> IP packet version is not 4 or 6</p>
<dt><code>long bpf_skb_output(void *</code><i>ctx</i><code>, struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>, void *</code><i>data</i><code>, u64</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Write raw <i>data</i> blob into a special BPF perf event held by <i>map</i> of type <code>BPF_MAP_TYPE_PERF_EVENT_ARRAY</code>. This perf event must have the following attributes: <code>PERF_SAMPLE_RAW</code> as <code>sample_type</code>, <code>PERF_TYPE_SOFTWARE</code> as <code>type</code>, and <code>PERF_COUNT_SW_BPF_OUTPUT</code> as <code>config</code>. </p>
<p> The <i>flags</i> are used to indicate the index in <i>map</i> for which the value must be put, masked with <code>BPF_F_INDEX_MASK</code>. Alternatively, <i>flags</i> can be set to <code>BPF_F_CURRENT_CPU</code> to indicate that the index of the current CPU core should be used. </p>
<p> The value to write, of <i>size</i>, is passed through eBPF stack and pointed by <i>data</i>. </p>
<p> <i>ctx</i> is a pointer to in-kernel struct sk_buff. </p>
<p> This helper is similar to <code>bpf_perf_event_output</code>() but restricted to raw_tracepoint bpf programs.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_probe_read_user(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Safely attempt to read <i>size</i> bytes from user space address <i>unsafe_ptr</i> and store the data in <i>dst</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_probe_read_kernel(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Safely attempt to read <i>size</i> bytes from kernel space address <i>unsafe_ptr</i> and store the data in <i>dst</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_probe_read_user_str(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Copy a NUL terminated string from an unsafe user address <i>unsafe_ptr</i> to <i>dst</i>. The <i>size</i> should include the terminating NUL byte. In case the string length is smaller than <i>size</i>, the target is not padded with further NUL bytes. If the string length is larger than <i>size</i>, just <i>size</i>-1 bytes are copied and the last byte is set to NUL. </p>
<p> On success, the length of the copied string is returned. This makes this helper useful in tracing programs for reading strings, and more importantly to get its length at runtime. See the following snippet: </p>
<pre>SEC(&quot;kprobe/sys_open&quot;)
void bpf_sys_open(struct pt_regs *ctx)
{
 char buf[PATHLEN]; // PATHLEN is defined to 256
 int res = bpf_probe_read_user_str(buf, sizeof(buf),
 ctx-&gt;di);
 // Consume buf, for example push it to
 // userspace via bpf_perf_event_output(); we
 // can use res (the string length) as event
 // size, after checking its boundaries.
}</pre>
<p>In comparison, using <code>bpf_probe_read_user</code>() helper here instead to read the string would require to estimate the length at compile time, and would often result in copying more memory than necessary. </p>
<p> Another useful use case is when parsing individual process arguments or individual environment variables navigating <i>current</i><code>-&gt;mm-&gt;arg_start</code> and <i>current</i><code>-&gt;mm-&gt;env_start</code>: using this helper and the return value, one can quickly iterate at the right offset of the memory area.</p>
<dt><code>Return</code></p>
<dd>On success, the strictly positive length of the string, including the trailing NUL character. On error, a negative value.</p>
<dt><code>long bpf_probe_read_kernel_str(void *</code><i>dst</i><code>, u32</code> <i>size</i><code>, const void *</code><i>unsafe_ptr</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Copy a NUL terminated string from an unsafe kernel address <i>unsafe_ptr</i> to <i>dst</i>. Same semantics as with <code>bpf_probe_read_user_str</code>() apply.</p>
<dt><code>Return</code></p>
<dd>On success, the strictly positive length of the string, including the trailing NUL character. On error, a negative value.</p>
<dt><code>long bpf_tcp_send_ack(void *</code><i>tp</i><code>, u32</code> <i>rcv_nxt</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Send out a tcp-ack. <i>tp</i> is the in-kernel struct <code>tcp_sock</code>. <i>rcv_nxt</i> is the ack_seq to be sent out.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>long bpf_send_signal_thread(u32</code> <i>sig</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Send signal <i>sig</i> to the thread corresponding to the current task.</p>
<dt><code>Return</code></p>
<dd>0 on success or successfully queued. </p>
<p> <code>-EBUSY</code> if work queue under nmi is full. </p>
<p> <code>-EINVAL</code> if <i>sig</i> is invalid. </p>
<p> <code>-EPERM</code> if no permission to send the <i>sig</i>. </p>
<p> <code>-EAGAIN</code> if bpf program can try again.</p>
<dt><code>u64 bpf_jiffies64(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Obtain the 64bit jiffies</p>
<dt><code>Return</code></p>
<dd>The 64 bit jiffies</p>
<dt><code>long bpf_read_branch_records(struct bpf_perf_event_data *</code><i>ctx</i><code>, void *</code><i>buf</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>For an eBPF program attached to a perf event, retrieve the branch records (<code>struct perf_branch_entry</code>) associated to <i>ctx</i> and store it in the buffer pointed by <i>buf</i> up to size <i>size</i> bytes.</p>
<dt><code>Return</code></p>
<dd>On success, number of bytes written to <i>buf</i>. On error, a negative value. </p>
<p> The <i>flags</i> can be set to <code>BPF_F_GET_BRANCH_RECORDS_SIZE</code> to instead return the number of bytes required to store all the branch entries. If this flag is set, <i>buf</i> may be NULL. </p>
<p> <code>-EINVAL</code> if arguments invalid or <code>size</code> not a multiple of <code>sizeof</code>(<code>struct perf_branch_entry</code>). </p>
<p> <code>-ENOENT</code> if architecture does not support branch records.</p>
<dt><code>long bpf_get_ns_current_pid_tgid(u64</code> <i>dev</i><code>, u64</code> <i>ino</i><code>, struct bpf_pidns_info *</code><i>nsdata</i><code>, u32</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Returns 0 on success, values for <i>pid</i> and <i>tgid</i> as seen from the current <i>namespace</i> will be returned in <i>nsdata</i>.</p>
<dt><code>Return</code></p>
<dd>0 on success, or one of the following in case of failure: </p>
<p> <code>-EINVAL</code> if dev and inum supplied don&#8217;t match dev_t and inode number with nsfs of current task, or if dev conversion to dev_t lost high bits. </p>
<p> <code>-ENOENT</code> if pidns does not exists for the current task.</p>
<dt><code>long bpf_xdp_output(void *</code><i>ctx</i><code>, struct bpf_map *</code><i>map</i><code>, u64</code> <i>flags</i><code>, void *</code><i>data</i><code>, u64</code> <i>size</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Write raw <i>data</i> blob into a special BPF perf event held by <i>map</i> of type <code>BPF_MAP_TYPE_PERF_EVENT_ARRAY</code>. This perf event must have the following attributes: <code>PERF_SAMPLE_RAW</code> as <code>sample_type</code>, <code>PERF_TYPE_SOFTWARE</code> as <code>type</code>, and <code>PERF_COUNT_SW_BPF_OUTPUT</code> as <code>config</code>. </p>
<p> The <i>flags</i> are used to indicate the index in <i>map</i> for which the value must be put, masked with <code>BPF_F_INDEX_MASK</code>. Alternatively, <i>flags</i> can be set to <code>BPF_F_CURRENT_CPU</code> to indicate that the index of the current CPU core should be used. </p>
<p> The value to write, of <i>size</i>, is passed through eBPF stack and pointed by <i>data</i>. </p>
<p> <i>ctx</i> is a pointer to in-kernel struct xdp_buff. </p>
<p> This helper is similar to <code>bpf_perf_eventoutput</code>() but restricted to raw_tracepoint bpf programs.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>u64 bpf_get_netns_cookie(void *</code><i>ctx</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Retrieve the cookie (generated by the kernel) of the network namespace the input <i>ctx</i> is associated with. The network namespace cookie remains stable for its lifetime and provides a global identifier that can be assumed unique. If <i>ctx</i> is NULL, then the helper returns the cookie for the initial network namespace. The cookie itself is very similar to that of <code>bpf_get_socket_cookie</code>() helper, but for network namespaces instead of sockets.</p>
<dt><code>Return</code></p>
<dd>A 8-byte long opaque number.</p>
<dt><code>u64 bpf_get_current_ancestor_cgroup_id(int</code> <i>ancestor_level</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return id of cgroup v2 that is ancestor of the cgroup associated with the current task at the <i>ancestor_level</i>. The root cgroup is at <i>ancestor_level</i> zero and each step down the hierarchy increments the level. If <i>ancestor_level</i> == level of cgroup associated with the current task, then return value will be the same as that of <code>bpf_get_current_cgroup_id</code>(). </p>
<p> The helper is useful to implement policies based on cgroups that are upper in hierarchy than immediate cgroup associated with the current task. </p>
<p> The format of returned id and helper limitations are same as in <code>bpf_get_current_cgroup_id</code>().</p>
<dt><code>Return</code></p>
<dd>The id is returned or 0 in case the id could not be retrieved.</p>
<dt><code>long bpf_sk_assign(struct sk_buff *</code><i>skb</i><code>, struct bpf_sock *</code><i>sk</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Helper is overloaded depending on BPF program type. This description applies to <code>BPF_PROG_TYPE_SCHED_CLS</code> and <code>BPF_PROG_TYPE_SCHED_ACT</code> programs. </p>
<p> Assign the <i>sk</i> to the <i>skb</i>. When combined with appropriate routing configuration to receive the packet towards the socket, will cause <i>skb</i> to be delivered to the specified socket. Subsequent redirection of <i>skb</i> via <code>bpf_redirect</code>(), <code>bpf_clone_redirect</code>() or other methods outside of BPF may interfere with successful delivery to the socket. </p>
<p> This operation is only valid from TC ingress path. </p>
<p> The <i>flags</i> argument must be zero.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure: </p>
<p> <code>-EINVAL</code> if specified <i>flags</i> are not supported. </p>
<p> <code>-ENOENT</code> if the socket is unavailable for assignment. </p>
<p> <code>-ENETUNREACH</code> if the socket is unreachable (wrong netns). </p>
<p> <code>-EOPNOTSUPP</code> if the operation is not supported, for example a call from outside of TC ingress. </p>
<p> <code>-ESOCKTNOSUPPORT</code> if the socket type is not supported (reuseport).</p>
<dt><code>long bpf_sk_assign(struct bpf_sk_lookup *</code><i>ctx</i><code>, struct bpf_sock *</code><i>sk</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Helper is overloaded depending on BPF program type. This description applies to <code>BPF_PROG_TYPE_SK_LOOKUP</code> programs. </p>
<p> Select the <i>sk</i> as a result of a socket lookup. </p>
<p> For the operation to succeed passed socket must be compatible with the packet description provided by the <i>ctx</i> object. </p>
<p> L4 protocol (<code>IPPROTO_TCP</code> or <code>IPPROTO_UDP</code>) must be an exact match. While IP family (<code>AF_INET</code> or <code>AF_INET6</code>) must be compatible, that is IPv6 sockets that are not v6-only can be selected for IPv4 packets. </p>
<p> Only TCP listeners and UDP unconnected sockets can be selected. <i>sk</i> can also be NULL to reset any previous selection. </p>
<p> <i>flags</i> argument can combination of following values:</p>
<dt>&bull;</p>
<dd><code>BPF_SK_LOOKUP_F_REPLACE</code> to override the previous socket selection, potentially done by a BPF program that ran before us.</p>
<dt>&bull;</p>
<dd><code>BPF_SK_LOOKUP_F_NO_REUSEPORT</code> to skip load-balancing within reuseport group for the socket being selected. </p>
<p> On success <i>ctx-&gt;sk</i> will point to the selected socket.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative errno in case of failure.</p>
<dt>&bull;</p>
<dd><code>-EAFNOSUPPORT</code> if socket family (<i>sk-&gt;family</i>) is not compatible with packet family (<i>ctx-&gt;family</i>).</p>
<dt>&bull;</p>
<dd><code>-EEXIST</code> if socket has been already selected, potentially by another program, and <code>BPF_SK_LOOKUP_F_REPLACE</code> flag was not specified.</p>
<dt>&bull;</p>
<dd><code>-EINVAL</code> if unsupported flags were specified.</p>
<dt>&bull;</p>
<dd><code>-EPROTOTYPE</code> if socket L4 protocol (<i>sk-&gt;protocol</i>) doesn&#8217;t match packet protocol (<i>ctx-&gt;protocol</i>).</p>
<dt>&bull;</p>
<dd><code>-ESOCKTNOSUPPORT</code> if socket is not in allowed state (TCP listening or UDP unconnected).</p>
<dt><code>u64 bpf_ktime_get_boot_ns(void)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return the time elapsed since system boot, in nanoseconds. Does include the time the system was suspended. See: <code>clock_gettime</code>(<code>CLOCK_BOOTTIME</code>)</p>
<dt><code>Return</code></p>
<dd>Current <i>ktime</i>.</p>
<dt><code>long bpf_seq_printf(struct seq_file *</code><i>m</i><code>, const char *</code><i>fmt</i><code>, u32</code> <i>fmt_size</i><code>, const void *</code><i>data</i><code>, u32</code> <i>data_len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd><code>bpf_seq_printf</code>() uses seq_file <code>seq_printf</code>() to print out the format string. The <i>m</i> represents the seq_file. The <i>fmt</i> and <i>fmt_size</i> are for the format string itself. The <i>data</i> and <i>data_len</i> are format string arguments. The <i>data</i> are a <code>u64</code> array and corresponding format string values are stored in the array. For strings and pointers where pointees are accessed, only the pointer values are stored in the <i>data</i> array. The <i>data_len</i> is the size of <i>data</i> in bytes. </p>
<p> Formats <code>%s</code>, <code>%p{i,I}{4,6}</code> requires to read kernel memory. Reading kernel memory may fail due to either invalid address or valid address but requiring a major memory fault. If reading kernel memory fails, the string for <code>%s</code> will be an empty string, and the ip address for <code>%p{i,I}{4,6}</code> will be 0. Not returning error to bpf program is consistent with what <code>bpf_trace_printk</code>() does for now.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure: </p>
<p> <code>-EBUSY</code> if per-CPU memory copy buffer is busy, can try again by returning 1 from bpf program. </p>
<p> <code>-EINVAL</code> if arguments are invalid, or if <i>fmt</i> is invalid/unsupported. </p>
<p> <code>-E2BIG</code> if <i>fmt</i> contains too many format specifiers. </p>
<p> <code>-EOVERFLOW</code> if an overflow happened: The same object will be tried again.</p>
<dt><code>long bpf_seq_write(struct seq_file *</code><i>m</i><code>, const void *</code><i>data</i><code>, u32</code> <i>len</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd><code>bpf_seq_write</code>() uses seq_file <code>seq_write</code>() to write the data. The <i>m</i> represents the seq_file. The <i>data</i> and <i>len</i> represent the data to write in bytes.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure: </p>
<p> <code>-EOVERFLOW</code> if an overflow happened: The same object will be tried again.</p>
<dt><code>u64 bpf_sk_cgroup_id(struct bpf_sock *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return the cgroup v2 id of the socket <i>sk</i>. </p>
<p> <i>sk</i> must be a non-<code>NULL</code> pointer to a full socket, e.g. one returned from <code>bpf_sk_lookup_xxx</code>(), <code>bpf_sk_fullsock</code>(), etc. The format of returned id is same as in <code>bpf_skb_cgroup_id</code>(). </p>
<p> This helper is available only if the kernel was compiled with the <code>CONFIG_SOCK_CGROUP_DATA</code> configuration option.</p>
<dt><code>Return</code></p>
<dd>The id is returned or 0 in case the id could not be retrieved.</p>
<dt><code>u64 bpf_sk_ancestor_cgroup_id(struct bpf_sock *</code><i>sk</i><code>, int</code> <i>ancestor_level</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return id of cgroup v2 that is ancestor of cgroup associated with the <i>sk</i> at the <i>ancestor_level</i>. The root cgroup is at <i>ancestor_level</i> zero and each step down the hierarchy increments the level. If <i>ancestor_level</i> == level of cgroup associated with <i>sk</i>, then return value will be same as that of <code>bpf_sk_cgroup_id</code>(). </p>
<p> The helper is useful to implement policies based on cgroups that are upper in hierarchy than immediate cgroup associated with <i>sk</i>. </p>
<p> The format of returned id and helper limitations are same as in <code>bpf_sk_cgroup_id</code>().</p>
<dt><code>Return</code></p>
<dd>The id is returned or 0 in case the id could not be retrieved.</p>
<dt><code>long bpf_ringbuf_output(void *</code><i>ringbuf</i><code>, void *</code><i>data</i><code>, u64</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Copy <i>size</i> bytes from <i>data</i> into a ring buffer <i>ringbuf</i>. If <code>BPF_RB_NO_WAKEUP</code> is specified in <i>flags</i>, no notification of new data availability is sent. If <code>BPF_RB_FORCE_WAKEUP</code> is specified in <i>flags</i>, notification of new data availability is sent unconditionally.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure.</p>
<dt><code>void *bpf_ringbuf_reserve(void *</code><i>ringbuf</i><code>, u64</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Reserve <i>size</i> bytes of payload in a ring buffer <i>ringbuf</i>.</p>
<dt><code>Return</code></p>
<dd>Valid pointer with <i>size</i> bytes of memory available; NULL, otherwise.</p>
<dt><code>void bpf_ringbuf_submit(void *</code><i>data</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Submit reserved ring buffer sample, pointed to by <i>data</i>. If <code>BPF_RB_NO_WAKEUP</code> is specified in <i>flags</i>, no notification of new data availability is sent. If <code>BPF_RB_FORCE_WAKEUP</code> is specified in <i>flags</i>, notification of new data availability is sent unconditionally.</p>
<dt><code>Return</code></p>
<dd>Nothing. Always succeeds.</p>
<dt><code>void bpf_ringbuf_discard(void *</code><i>data</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Discard reserved ring buffer sample, pointed to by <i>data</i>. If <code>BPF_RB_NO_WAKEUP</code> is specified in <i>flags</i>, no notification of new data availability is sent. If <code>BPF_RB_FORCE_WAKEUP</code> is specified in <i>flags</i>, notification of new data availability is sent unconditionally.</p>
<dt><code>Return</code></p>
<dd>Nothing. Always succeeds.</p>
<dt><code>u64 bpf_ringbuf_query(void *</code><i>ringbuf</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Query various characteristics of provided ring buffer. What exactly is queries is determined by <i>flags</i>:</p>
<dt>&bull;</p>
<dd><code>BPF_RB_AVAIL_DATA</code>: Amount of data not yet consumed.</p>
<dt>&bull;</p>
<dd><code>BPF_RB_RING_SIZE</code>: The size of ring buffer.</p>
<dt>&bull;</p>
<dd><code>BPF_RB_CONS_POS</code>: Consumer position (can wrap around).</p>
<dt>&bull;</p>
<dd><code>BPF_RB_PROD_POS</code>: Producer(s) position (can wrap around). </p>
<p> Data returned is just a momentary snapshot of actual values and could be inaccurate, so this facility should be used to power heuristics and for reporting, not to make 100% correct calculation.</p>
<dt><code>Return</code></p>
<dd>Requested value, or 0, if <i>flags</i> are not recognized.</p>
<dt><code>long bpf_csum_level(struct sk_buff *</code><i>skb</i><code>, u64</code> <i>level</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Change the skbs checksum level by one layer up or down, or reset it entirely to none in order to have the stack perform checksum validation. The level is applicable to the following protocols: TCP, UDP, GRE, SCTP, FCOE. For example, a decap of | ETH | IP | UDP | GUE | IP | TCP | into | ETH | IP | TCP | through <code>bpf_skb_adjust_room</code>() helper with passing in <code>BPF_F_ADJ_ROOM_NO_CSUM_RESET</code> flag would require one call to <code>bpf_csum_level</code>() with <code>BPF_CSUM_LEVEL_DEC</code> since the UDP header is removed. Similarly, an encap of the latter into the former could be accompanied by a helper call to <code>bpf_csum_level</code>() with <code>BPF_CSUM_LEVEL_INC</code> if the skb is still intended to be processed in higher layers of the stack instead of just egressing at tc. </p>
<p> There are three supported level settings at this time:</p>
<dt>&bull;</p>
<dd><code>BPF_CSUM_LEVEL_INC</code>: Increases skb-&gt;csum_level for skbs with CHECKSUM_UNNECESSARY.</p>
<dt>&bull;</p>
<dd><code>BPF_CSUM_LEVEL_DEC</code>: Decreases skb-&gt;csum_level for skbs with CHECKSUM_UNNECESSARY.</p>
<dt>&bull;</p>
<dd><code>BPF_CSUM_LEVEL_RESET</code>: Resets skb-&gt;csum_level to 0 and sets CHECKSUM_NONE to force checksum validation by the stack.</p>
<dt>&bull;</p>
<dd><code>BPF_CSUM_LEVEL_QUERY</code>: No-op, returns the current skb-&gt;csum_level.</p>
<dt><code>Return</code></p>
<dd>0 on success, or a negative error in case of failure. In the case of <code>BPF_CSUM_LEVEL_QUERY</code>, the current skb-&gt;csum_level is returned or the error code -EACCES in case the skb is not subject to CHECKSUM_UNNECESSARY.</p>
<dt><code>struct tcp6_sock *bpf_skc_to_tcp6_sock(void *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Dynamically cast a <i>sk</i> pointer to a <i>tcp6_sock</i> pointer.</p>
<dt><code>Return</code></p>
<dd><i>sk</i> if casting is valid, or NULL otherwise.</p>
<dt><code>struct tcp_sock *bpf_skc_to_tcp_sock(void *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Dynamically cast a <i>sk</i> pointer to a <i>tcp_sock</i> pointer.</p>
<dt><code>Return</code></p>
<dd><i>sk</i> if casting is valid, or NULL otherwise.</p>
<dt><code>struct tcp_timewait_sock *bpf_skc_to_tcp_timewait_sock(void *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Dynamically cast a <i>sk</i> pointer to a <i>tcp_timewait_sock</i> pointer.</p>
<dt><code>Return</code></p>
<dd><i>sk</i> if casting is valid, or NULL otherwise.</p>
<dt><code>struct tcp_request_sock *bpf_skc_to_tcp_request_sock(void *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Dynamically cast a <i>sk</i> pointer to a <i>tcp_request_sock</i> pointer.</p>
<dt><code>Return</code></p>
<dd><i>sk</i> if casting is valid, or NULL otherwise.</p>
<dt><code>struct udp6_sock *bpf_skc_to_udp6_sock(void *</code><i>sk</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Dynamically cast a <i>sk</i> pointer to a <i>udp6_sock</i> pointer.</p>
<dt><code>Return</code></p>
<dd><i>sk</i> if casting is valid, or NULL otherwise.</p>
<dt><code>long bpf_get_task_stack(struct task_struct *</code><i>task</i><code>, void *</code><i>buf</i><code>, u32</code> <i>size</i><code>, u64</code> <i>flags</i><code>)</code></p>
<dd>
<dt><code>Description</code></p>
<dd>Return a user or a kernel stack in bpf program provided buffer. To achieve this, the helper needs <i>task</i>, which is a valid pointer to struct task_struct. To store the stacktrace, the bpf program provides <i>buf</i> with a nonnegative <i>size</i>. </p>
<p> The last argument, <i>flags</i>, holds the number of stack frames to skip (from 0 to 255), masked with <code>BPF_F_SKIP_FIELD_MASK</code>. The next bits can be used to set the following flags:</p>
<dt><code>BPF_F_USER_STACK</code></p>
<dd>Collect a user space stack instead of a kernel stack.</p>
<dt><code>BPF_F_USER_BUILD_ID</code></p>
<dd>Collect buildid+offset instead of ips for user stack, only valid if <code>BPF_F_USER_STACK</code> is also specified. </p>
<p> <code>bpf_get_task_stack</code>() can collect up to <code>PERF_MAX_STACK_DEPTH</code> both kernel and user frames, subject to sufficient large buffer size. Note that this limit can be controlled with the <code>sysctl</code> program, and that it should be manually increased in order to profile long user stacks (such as stacks for Java programs). To do so, use: </p>
<pre># sysctl kernel.perf_event_max_stack=&lt;new value&gt;</pre>
<dt><code>Return</code></p>
<dd>A non-negative value equal to or less than <i>size</i> on success, or a negative error in case of failure.</dl>
<h2>Examples</h2>
<p>Example usage for most of the eBPF helpers listed in this manual page are available within the Linux kernel sources, at the following locations:</p>
<dl>
<dt>&bull;</p>
<dd><i>samples/bpf/</i></p>
<dt>&bull;</p>
<dd><i>tools/testing/selftests/bpf/</i></dl>
<h2>License</h2>
<p>eBPF programs can have an associated license, passed along with the bytecode instructions to the kernel when the programs are loaded. The format for that string is identical to the one in use for kernel modules (Dual licenses, such as &quot;Dual BSD/GPL&quot;, may be used). Some helper functions are only accessible to programs that are compatible with the GNU Privacy License (GPL). </p>
<p> In order to use such helpers, the eBPF program must be loaded with the correct license string passed (via <code>attr</code>) to the <code>bpf</code>() system call, and this generally translates into the C source code of the program containing a line similar to the following: </p>
<pre>char ____license[] __attribute__((section(&quot;license&quot;), used)) = &quot;GPL&quot;;</pre>
<h2>Implementation</h2>
<p>This manual page is an effort to document the existing eBPF helper functions. But as of this writing, the BPF sub-system is under heavy development. New eBPF program or map types are added, along with new helper functions. Some helpers are occasionally made available for additional program types. So in spite of the efforts of the community, this page might not be up-to-date. If you want to check by yourself what helper functions exist in your kernel, or what types of programs they can support, here are some files among the kernel tree that you may be interested in:</p>
<dl>
<dt>&bull;</p>
<dd><i>include/uapi/linux/bpf.h</i> is the main BPF header. It contains the full list of all helper functions, as well as many other BPF definitions including most of the flags, structs or constants used by the helpers.</p>
<dt>&bull;</p>
<dd><i>net/core/filter.c</i> contains the definition of most network-related helper functions, and the list of program types from which they can be used.</p>
<dt>&bull;</p>
<dd><i>kernel/trace/bpf_trace.c</i> is the equivalent for most tracing program-related helpers.</p>
<dt>&bull;</p>
<dd><i>kernel/bpf/verifier.c</i> contains the functions used to check that valid types of eBPF maps are used with a given helper function.</p>
<dt>&bull;</p>
<dd><i>kernel/bpf/</i> directory contains other files in which additional helpers are defined (for cgroups, sockmaps, etc.).</p>
<dt>&bull;</p>
<dd>The bpftool utility can be used to probe the availability of helper functions on the system (as well as supported program and map types, and a number of other parameters). To do so, run <code>bpftool feature probe</code> (see <code><a href="/docs/linux/man/8-bpftool-feature/">bpftool-feature</a></code>(8) for details). Add the <code>unprivileged</code> keyword to list features available to unprivileged users. </p>
<p> Compatibility between helper functions and program types can generally be found in the files where helper functions are defined. Look for the <code>struct bpf_func_proto</code> objects and for functions returning them: these functions contain a list of helpers that a given program type can call. Note that the <code>default:</code> label of the <code>switch &#8230; case</code> used to filter helpers can call other functions, themselves allowing access to additional helpers. The requirement for GPL license is also in those <code>struct bpf_func_proto</code>. </p>
<p> Compatibility between helper functions and map types can be found in the <code>check_map_func_compatibility</code>() function in file <i>kernel/bpf/verifier.c</i>. </p>
<p> Helper functions that invalidate the checks on <code>data</code> and <code>data_end</code> pointers for network processing are listed in function <code>bpf_helper_changes_pkt_data</code>() in file <i>net/core/filter.c</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2), <code><a href="/docs/linux/man/8-bpftool/">bpftool</a></code>(8), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
