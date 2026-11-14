---
title: "hwloc_get_proc_membind(3)"
name: "hwloc_get_proc_membind"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_proc_membind/"
description: "hwlocality_membinding – Memory binding"
---

<h2 class="name">NAME</h2>
<p> hwlocality_membinding &#8211; Memory binding </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_membind_policy_t</code> { <code>HWLOC_MEMBIND_DEFAULT</code>, <code>HWLOC_MEMBIND_FIRSTTOUCH</code>, <code>HWLOC_MEMBIND_BIND</code>, <code>HWLOC_MEMBIND_INTERLEAVE</code>, <code>HWLOC_MEMBIND_REPLICATE</code>, <code>HWLOC_MEMBIND_NEXTTOUCH</code>, <code>HWLOC_MEMBIND_MIXED</code> } </p>
<p> enum <code>hwloc_membind_flags_t</code> { <code>HWLOC_MEMBIND_PROCESS</code>, <code>HWLOC_MEMBIND_THREAD</code>, <code>HWLOC_MEMBIND_STRICT</code>, <code>HWLOC_MEMBIND_MIGRATE</code>, <code>HWLOC_MEMBIND_NOCPUBIND</code> } </p>
<h3>Functions</h3>
<p> int <code>hwloc_set_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_set_membind</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_get_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> int <code>hwloc_get_membind</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> int <code>hwloc_set_proc_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_set_proc_membind</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_get_proc_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> int <code>hwloc_get_proc_membind</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> int <code>hwloc_set_area_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, const void *addr, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_set_area_membind</code> (<code>hwloc_topology_t</code> topology, const void *addr, size_t len, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_get_area_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, const void *addr, size_t len, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> int <code>hwloc_get_area_membind</code> (<code>hwloc_topology_t</code> topology, const void *addr, size_t len, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> *policy, int flags) </p>
<p> void * <code>hwloc_alloc</code> (<code>hwloc_topology_t</code> topology, size_t len) </p>
<p> void * <code>hwloc_alloc_membind_nodeset</code> (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> void * <code>hwloc_alloc_membind</code> (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> static void * <code>hwloc_alloc_membind_policy_nodeset</code> (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> static void * <code>hwloc_alloc_membind_policy</code> (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_membind_policy_t</code> policy, int flags) </p>
<p> int <code>hwloc_free</code> (<code>hwloc_topology_t</code> topology, void *addr, size_t len) </p>
<h2>Detailed Description</h2>
<p> Memory binding can be done three ways: </p>
<dl>
<dt>&bull;</p>
<dd> explicit memory allocation thanks to <code>hwloc_alloc_membind()</code> and friends: the binding will have effect on the memory allocated by these functions.</p>
<dt>&bull;</p>
<dd> implicit memory binding through binding policy: <code>hwloc_set_membind()</code> and friends only define the current policy of the process, which will be applied to the subsequent calls to malloc() and friends.</p>
<dt>&bull;</p>
<dd> migration of existing memory ranges, thanks to <code>hwloc_set_area_membind()</code> and friends, which move already-allocated data.</dl>
<p> Not all operating systems support all three ways. <code>hwloc_topology_get_support()</code> may be used to query about the actual memory binding support in the currently used operating system. </p>
<p> When the requested binding operation is not available and the <code>HWLOC_MEMBIND_STRICT</code> flag was passed, the function returns -1. errno will be set to ENOSYS when the system does support the specified action or policy (e.g., some systems only allow binding memory on a per-thread basis, whereas other systems only allow binding memory for all threads in a process). errno will be set to EXDEV when the requested cpuset can not be enforced (e.g., some systems only allow binding memory to a single NUMA node). </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> was not passed, the function may fail as well, or the operating system may use a slightly different operation (with side-effects, smaller binding set, etc.) when the requested operation is not exactly supported. </p>
<p> The most portable form that should be preferred over the others whenever possible is as follows. It allocates some memory hopefully bound to the specified set. To do so, hwloc will possibly have to change the current memory binding policy in order to actually get the memory bound, if the OS does not provide any other way to simply allocate bound memory without changing the policy for all allocations. That is the difference with <code>hwloc_alloc_membind()</code>, which will never change the current memory binding policy. </p>
<pre>
hwloc_alloc_membind_policy(topology, size, set,
                           HWLOC_MEMBIND_BIND, 0);
</pre>
<p> Each hwloc memory binding function is available in two forms: one that takes a CPU set argument and another that takes a NUMA memory node set argument (see <code>Object Sets (hwloc_cpuset_t and hwloc_nodeset_t)</code> and <code>The bitmap API</code> for a discussion of CPU sets and NUMA memory node sets). The names of the latter form end with _nodeset. It is also possible to convert between CPU set and node set using <code>hwloc_cpuset_to_nodeset()</code> or <code>hwloc_cpuset_from_nodeset()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> Some example codes are available under doc/examples/ in the source tree.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> On some operating systems, memory binding affects the CPU binding; see <code>HWLOC_MEMBIND_NOCPUBIND</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_membind_flags_t</code></h3>
<p> Memory binding flags. These flags can be used to refine the binding policy. All flags can be logically OR&#8217;ed together with the exception of <code>HWLOC_MEMBIND_PROCESS</code> and <code>HWLOC_MEMBIND_THREAD</code>; these two flags are mutually exclusive. </p>
<p> Not all systems support all kinds of binding. <code>hwloc_topology_get_support()</code> may be used to query about the actual memory binding support in the currently used operating system. See the &#8216;Detailed Description&#8217; section of <code>Memory binding</code> for a description of errors that can occur. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_MEMBIND_PROCESS </i></p>
<dd> Set policy for all threads of the specified (possibly multithreaded) process. This flag is mutually exclusive with <code>HWLOC_MEMBIND_THREAD</code>.</p>
<dt><i>HWLOC_MEMBIND_THREAD </i></p>
<dd> Set policy for a specific thread of the current process. This flag is mutually exclusive with <code>HWLOC_MEMBIND_PROCESS</code>.</p>
<dt><i>HWLOC_MEMBIND_STRICT </i></p>
<dd> Request strict binding from the OS. The function will fail if the binding can not be guaranteed / completely enforced.</dl>
<p> This flag has slightly different meanings depending on which function it is used with.</p>
<dl>
<dt><i>HWLOC_MEMBIND_MIGRATE </i></p>
<dd> Migrate existing allocated memory. If the memory cannot be migrated and the <code>HWLOC_MEMBIND_STRICT</code> flag is passed, an error will be returned.</p>
<dt><i>HWLOC_MEMBIND_NOCPUBIND </i></p>
<dd> Avoid any effect on CPU binding. On some operating systems, some underlying memory binding functions also bind the application to the corresponding CPU(s). Using this flag will cause hwloc to avoid using OS functions that could potentially affect CPU bindings. Note, however, that using NOCPUBIND may reduce hwloc&#8217;s overall memory binding support. Specifically: some of hwloc&#8217;s memory binding functions may fail with errno set to ENOSYS when used with NOCPUBIND.</dl>
<h3>enum <code>hwloc_membind_policy_t</code></h3>
<p> Memory binding policy. These constants can be used to choose the binding policy. Only one policy can be used at a time (i.e., the values cannot be OR&#8217;ed together). </p>
<p> Not all systems support all kinds of binding. <code>hwloc_topology_get_support()</code> may be used to query about the actual memory binding policy support in the currently used operating system. See the &#8216;Detailed Description&#8217; section of <code>Memory binding</code> for a description of errors that can occur. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_MEMBIND_DEFAULT </i></p>
<dd> Reset the memory allocation policy to the system default. Depending on the operating system, this may correspond to <code>HWLOC_MEMBIND_FIRSTTOUCH</code> (Linux), or <code>HWLOC_MEMBIND_BIND</code> (AIX, HP-UX, OSF, Solaris, Windows).</p>
<dt><i>HWLOC_MEMBIND_FIRSTTOUCH </i></p>
<dd> Allocate memory but do not immediately bind it to a specific locality. Instead, each page in the allocation is bound only when it is first touched. Pages are individually bound to the local NUMA node of the first thread that touches it. If there is not enough memory on the node, allocation may be done in the specified cpuset before allocating on other nodes.</p>
<dt><i>HWLOC_MEMBIND_BIND </i></p>
<dd> Allocate memory on the specified nodes.</p>
<dt><i>HWLOC_MEMBIND_INTERLEAVE </i></p>
<dd> Allocate memory on the given nodes in an interleaved / round-robin manner. The precise layout of the memory across multiple NUMA nodes is OS/system specific. Interleaving can be useful when threads distributed across the specified NUMA nodes will all be accessing the whole memory range concurrently, since the interleave will then balance the memory references.</p>
<dt><i>HWLOC_MEMBIND_REPLICATE </i></p>
<dd> Replicate memory on the given nodes; reads from this memory will attempt to be serviced from the NUMA node local to the reading thread. Replicating can be useful when multiple threads from the specified NUMA nodes will be sharing the same read-only data. This policy can only be used with existing memory allocations (i.e., the hwloc_set_*membind*() functions); it cannot be used with functions that allocate new memory (i.e., the hwloc_alloc*() functions).</p>
<dt><i>HWLOC_MEMBIND_NEXTTOUCH </i></p>
<dd> For each page bound with this policy, by next time it is touched (and next time only), it is moved from its current location to the local NUMA node of the thread where the memory reference occurred (if it needs to be moved at all).</p>
<dt><i>HWLOC_MEMBIND_MIXED </i></p>
<dd> Returned by get_membind() functions when multiple threads or parts of a memory area have differing memory binding policies.</dl>
<h2>Function Documentation</h2>
<h3>void* hwloc_alloc (<code>hwloc_topology_t</code> topology, size_t len)</h3>
<p> Allocate some memory. This is equivalent to malloc(), except that it tries to allocate page-aligned memory from the OS. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The allocated memory should be freed with <code>hwloc_free()</code>.</dl>
<h3>void* hwloc_alloc_membind (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Allocate some memory on memory nodes near the given physical cpuset cpuset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL with errno set to ENOSYS if the action is not supported and <code>HWLOC_MEMBIND_STRICT</code> is given </p>
<p> NULL with errno set to EXDEV if the binding cannot be enforced and <code>HWLOC_MEMBIND_STRICT</code> is given </p>
<p> NULL with errno set to ENOMEM if the memory allocation failed even before trying to bind.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The allocated memory should be freed with <code>hwloc_free()</code>.</dl>
<h3>void* hwloc_alloc_membind_nodeset (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Allocate some memory on the given physical nodeset nodeset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL with errno set to ENOSYS if the action is not supported and <code>HWLOC_MEMBIND_STRICT</code> is given </p>
<p> NULL with errno set to EXDEV if the binding cannot be enforced and <code>HWLOC_MEMBIND_STRICT</code> is given </p>
<p> NULL with errno set to ENOMEM if the memory allocation failed even before trying to bind.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The allocated memory should be freed with <code>hwloc_free()</code>.</dl>
<h3>static void* hwloc_alloc_membind_policy (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_membind_policy_t</code> policy, int flags) [inline], [static]</h3>
<p> Allocate some memory on the memory nodes near given cpuset cpuset. This is similar to <code>hwloc_alloc_membind_policy_nodeset()</code>, but for a given cpuset.</p>
<h3>static void* hwloc_alloc_membind_policy_nodeset (<code>hwloc_topology_t</code> topology, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags) [inline], [static]</h3>
<p> Allocate some memory on the given nodeset nodeset. This is similar to <code>hwloc_alloc_membind()</code> except that it is allowed to change the current memory binding policy, thus providing more binding support, at the expense of changing the current state.</p>
<h3>int hwloc_free (<code>hwloc_topology_t</code> topology, void * addr, size_t len)</h3>
<p> Free memory that was previously allocated by <code>hwloc_alloc()</code> or <code>hwloc_alloc_membind()</code>.</p>
<h3>int hwloc_get_area_membind (<code>hwloc_topology_t</code> topology, const void * addr, size_t len, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the CPUs near the physical NUMA node(s) and binding policy of the memory identified by (addr, len ). This function has two output parameters: cpuset and policy. The values returned in these parameters depend on both the flags passed in and the memory binding policies and nodesets of the pages in the address range. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is specified, the target pages are first checked to see if they all have the same memory binding policy and nodeset. If they do not, -1 is returned and errno is set to EXDEV. If they are identical across all pages, the policy is returned in policy. cpuset is set to the union of CPUs near the NUMA node(s) in the nodeset. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is not specified, the union of all NUMA node(s) containing pages in the address range is calculated. cpuset is then set to the CPUs near the NUMA node(s) in this union. If all pages in the target have the same policy, it is returned in policy. Otherwise, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL.</p>
<h3>int hwloc_get_area_membind_nodeset (<code>hwloc_topology_t</code> topology, const void * addr, size_t len, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the physical NUMA node(s) and binding policy of the memory identified by (addr, len ). This function has two output parameters: nodeset and policy. The values returned in these parameters depend on both the flags passed in and the memory binding policies and nodesets of the pages in the address range. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is specified, the target pages are first checked to see if they all have the same memory binding policy and nodeset. If they do not, -1 is returned and errno is set to EXDEV. If they are identical across all pages, the nodeset and policy are returned in nodeset and policy, respectively. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is not specified, nodeset is set to the union of all NUMA node(s) containing pages in the address range. If all pages in the target have the same policy, it is returned in policy. Otherwise, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL.</p>
<h3>int hwloc_get_membind (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the default memory binding policy and physical locality of the current process or thread (the locality is returned in cpuset as CPUs near the locality&#8217;s actual NUMA node(s)). This function has two output parameters: cpuset and policy. The values returned in these parameters depend on both the flags passed in and the current memory binding policies and nodesets in the queried target. </p>
<p> Passing the <code>HWLOC_MEMBIND_PROCESS</code> flag specifies that the query target is the current policies and nodesets for all the threads in the current process. Passing <code>HWLOC_MEMBIND_THREAD</code> specifies that the query target is the current policy and nodeset for only the thread invoking this function. </p>
<p> If neither of these flags are passed (which is the most portable method), the process is assumed to be single threaded. This allows hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> <code>HWLOC_MEMBIND_STRICT</code> is only meaningful when <code>HWLOC_MEMBIND_PROCESS</code> is also specified. In this case, hwloc will check the default memory policies and nodesets for all threads in the process. If they are not identical, -1 is returned and errno is set to EXDEV. If they are identical, the policy is returned in policy. cpuset is set to the union of CPUs near the NUMA node(s) in the nodeset. </p>
<p> Otherwise, if <code>HWLOC_MEMBIND_PROCESS</code> is specified (and <code>HWLOC_MEMBIND_STRICT</code> is <i>not</i> specified), the default nodeset from each thread is logically OR&#8217;ed together. cpuset is set to the union of CPUs near the NUMA node(s) in the resulting nodeset. If all threads&#8217; default policies are the same, policy is set to that policy. If they are different, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> In the <code>HWLOC_MEMBIND_THREAD</code> case (or when neither <code>HWLOC_MEMBIND_PROCESS</code> or <code>HWLOC_MEMBIND_THREAD</code> is specified), there is only one nodeset and policy. The policy is returned in policy; cpuset is set to the union of CPUs near the NUMA node(s) in the nodeset. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL.</p>
<h3>int hwloc_get_membind_nodeset (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the default memory binding policy and physical locality of the current process or thread. This function has two output parameters: nodeset and policy. The values returned in these parameters depend on both the flags passed in and the current memory binding policies and nodesets in the queried target. </p>
<p> Passing the <code>HWLOC_MEMBIND_PROCESS</code> flag specifies that the query target is the current policies and nodesets for all the threads in the current process. Passing <code>HWLOC_MEMBIND_THREAD</code> specifies that the query target is the current policy and nodeset for only the thread invoking this function. </p>
<p> If neither of these flags are passed (which is the most portable method), the process is assumed to be single threaded. This allows hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> <code>HWLOC_MEMBIND_STRICT</code> is only meaningful when <code>HWLOC_MEMBIND_PROCESS</code> is also specified. In this case, hwloc will check the default memory policies and nodesets for all threads in the process. If they are not identical, -1 is returned and errno is set to EXDEV. If they are identical, the values are returned in nodeset and policy. </p>
<p> Otherwise, if <code>HWLOC_MEMBIND_PROCESS</code> is specified (and <code>HWLOC_MEMBIND_STRICT</code> is <i>not</i> specified), nodeset is set to the logical OR of all threads&#8217; default nodeset. If all threads&#8217; default policies are the same, policy is set to that policy. If they are different, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> In the <code>HWLOC_MEMBIND_THREAD</code> case (or when neither <code>HWLOC_MEMBIND_PROCESS</code> or <code>HWLOC_MEMBIND_THREAD</code> is specified), there is only one nodeset and policy; they are returned in nodeset and policy, respectively. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL.</p>
<h3>int hwloc_get_proc_membind (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the default memory binding policy and physical locality of the specified process (the locality is returned in cpuset as CPUs near the locality&#8217;s actual NUMA node(s)). This function has two output parameters: cpuset and policy. The values returned in these parameters depend on both the flags passed in and the current memory binding policies and nodesets in the queried target. </p>
<p> Passing the <code>HWLOC_MEMBIND_PROCESS</code> flag specifies that the query target is the current policies and nodesets for all the threads in the specified process. If <code>HWLOC_MEMBIND_PROCESS</code> is not specified (which is the most portable method), the process is assumed to be single threaded. This allows hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> Note that it does not make sense to pass <code>HWLOC_MEMBIND_THREAD</code> to this function. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is specified, hwloc will check the default memory policies and nodesets for all threads in the specified process. If they are not identical, -1 is returned and errno is set to EXDEV. If they are identical, the policy is returned in policy. cpuset is set to the union of CPUs near the NUMA node(s) in the nodeset. </p>
<p> Otherwise, the default nodeset from each thread is logically OR&#8217;ed together. cpuset is set to the union of CPUs near the NUMA node(s) in the resulting nodeset. If all threads&#8217; default policies are the same, policy is set to that policy. If they are different, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms.</dl>
<h3>int hwloc_get_proc_membind_nodeset (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> * policy, int flags)</h3>
<p> Query the default memory binding policy and physical locality of the specified process. This function has two output parameters: nodeset and policy. The values returned in these parameters depend on both the flags passed in and the current memory binding policies and nodesets in the queried target. </p>
<p> Passing the <code>HWLOC_MEMBIND_PROCESS</code> flag specifies that the query target is the current policies and nodesets for all the threads in the specified process. If <code>HWLOC_MEMBIND_PROCESS</code> is not specified (which is the most portable method), the process is assumed to be single threaded. This allows hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> Note that it does not make sense to pass <code>HWLOC_MEMBIND_THREAD</code> to this function. </p>
<p> If <code>HWLOC_MEMBIND_STRICT</code> is specified, hwloc will check the default memory policies and nodesets for all threads in the specified process. If they are not identical, -1 is returned and errno is set to EXDEV. If they are identical, the values are returned in nodeset and policy. </p>
<p> Otherwise, nodeset is set to the logical OR of all threads&#8217; default nodeset. If all threads&#8217; default policies are the same, policy is set to that policy. If they are different, policy is set to <code>HWLOC_MEMBIND_MIXED</code>. </p>
<p> If any other flags are specified, -1 is returned and errno is set to EINVAL. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms.</dl>
<h3>int hwloc_set_area_membind (<code>hwloc_topology_t</code> topology, const void * addr, size_t len, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Bind the already-allocated memory identified by (addr, len) to the NUMA node(s) near physical cpuset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<h3>int hwloc_set_area_membind_nodeset (<code>hwloc_topology_t</code> topology, const void * addr, size_t len, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Bind the already-allocated memory identified by (addr, len) to the NUMA node(s) in physical nodeset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<h3>int hwloc_set_membind (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Set the default memory binding policy of the current process or thread to prefer the NUMA node(s) near the specified physical cpuset. If neither <code>HWLOC_MEMBIND_PROCESS</code> nor <code>HWLOC_MEMBIND_THREAD</code> is specified, the current process is assumed to be single-threaded. This is the most portable form as it permits hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<h3>int hwloc_set_membind_nodeset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Set the default memory binding policy of the current process or thread to prefer the NUMA node(s) specified by physical nodeset. If neither <code>HWLOC_MEMBIND_PROCESS</code> nor <code>HWLOC_MEMBIND_THREAD</code> is specified, the current process is assumed to be single-threaded. This is the most portable form as it permits hwloc to use either process-based OS functions or thread-based OS functions, depending on which are available. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<h3>int hwloc_set_proc_membind (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_cpuset_t</code> cpuset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Set the default memory binding policy of the specified process to prefer the NUMA node(s) near the specified physical cpuset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms.</dl>
<h3>int hwloc_set_proc_membind_nodeset (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_nodeset_t</code> nodeset, <code>hwloc_membind_policy_t</code> policy, int flags)</h3>
<p> Set the default memory binding policy of the specified process to prefer the NUMA node(s) specified by physical nodeset. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbBB">Author</a></p>
<dd></dl>
