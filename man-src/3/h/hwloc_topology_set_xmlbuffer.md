---
title: "hwloc_topology_set_xmlbuffer(3)"
name: "hwloc_topology_set_xmlbuffer"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_set_xmlbuffer/"
description: "hwlocality_configuration – Topology Detection Configuration and Query"
---

<h2 class="name">NAME</h2>
<p> hwlocality_configuration &#8211; Topology Detection Configuration and Query </p>
<h3>Data Structures</h3>
<p> struct <code>hwloc_topology_discovery_support</code> </p>
<p> struct <code>hwloc_topology_cpubind_support</code> </p>
<p> struct <code>hwloc_topology_membind_support</code> </p>
<p> struct <code>hwloc_topology_support</code> </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_topology_flags_e</code> { <code>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM</code>, <code>HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM</code>, <code>HWLOC_TOPOLOGY_FLAG_IO_DEVICES</code>, <code>HWLOC_TOPOLOGY_FLAG_IO_BRIDGES</code>, <code>HWLOC_TOPOLOGY_FLAG_WHOLE_IO</code>, <code>HWLOC_TOPOLOGY_FLAG_ICACHES</code> } </p>
<h3>Functions</h3>
<p> int <code>hwloc_topology_ignore_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> int <code>hwloc_topology_ignore_type_keep_structure</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> int <code>hwloc_topology_ignore_all_keep_structure</code> (<code>hwloc_topology_t</code> topology) </p>
<p> int <code>hwloc_topology_set_flags</code> (<code>hwloc_topology_t</code> topology, unsigned long flags) </p>
<p> unsigned long <code>hwloc_topology_get_flags</code> (<code>hwloc_topology_t</code> topology) </p>
<p> int <code>hwloc_topology_set_pid</code> (<code>hwloc_topology_t</code> restrict topology, hwloc_pid_t pid) </p>
<p> int <code>hwloc_topology_set_fsroot</code> (<code>hwloc_topology_t</code> restrict topology, const char *restrict fsroot_path) </p>
<p> int <code>hwloc_topology_set_synthetic</code> (<code>hwloc_topology_t</code> restrict topology, const char *restrict description) </p>
<p> int <code>hwloc_topology_set_xml</code> (<code>hwloc_topology_t</code> restrict topology, const char *restrict xmlpath) </p>
<p> int <code>hwloc_topology_set_xmlbuffer</code> (<code>hwloc_topology_t</code> restrict topology, const char *restrict buffer, int size) </p>
<p> int <code>hwloc_topology_set_custom</code> (<code>hwloc_topology_t</code> topology) </p>
<p> int <code>hwloc_topology_set_distance_matrix</code> (<code>hwloc_topology_t</code> restrict topology, <code>hwloc_obj_type_t</code> type, unsigned nbobjs, unsigned *os_index, float *distances) </p>
<p> int <code>hwloc_topology_is_thissystem</code> (<code>hwloc_topology_t</code> restrict topology) </p>
<p> const struct <code>hwloc_topology_support</code> * <code>hwloc_topology_get_support</code> (<code>hwloc_topology_t</code> restrict topology) </p>
<p> void <code>hwloc_topology_set_userdata</code> (<code>hwloc_topology_t</code> topology, const void *userdata) </p>
<p> void * <code>hwloc_topology_get_userdata</code> (<code>hwloc_topology_t</code> topology) </p>
<h2>Detailed Description</h2>
<p> Several functions can optionally be called between <code>hwloc_topology_init()</code> and <code>hwloc_topology_load()</code> to configure how the detection should be performed, e.g. to ignore some objects types, define a synthetic topology, etc. </p>
<p> If none of them is called, the default is to detect all the objects of the machine that the caller is allowed to access. </p>
<p> This default behavior may also be modified through environment variables if the application did not modify it already. Setting HWLOC_XMLFILE in the environment enforces the discovery from a XML file as if <code>hwloc_topology_set_xml()</code> had been called. HWLOC_FSROOT switches to reading the topology from the specified Linux filesystem root as if <code>hwloc_topology_set_fsroot()</code> had been called. Finally, HWLOC_THISSYSTEM enforces the return value of <code>hwloc_topology_is_thissystem()</code>.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_topology_flags_e</code></h3>
<p> Flags to be set onto a topology context before load. Flags should be given to <code>hwloc_topology_set_flags()</code>. They may also be returned by <code>hwloc_topology_get_flags()</code>. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM </i></p>
<dd> Detect the whole system, ignore reservations and offline settings. Gather all resources, even if some were disabled by the administrator. For instance, ignore Linux Cgroup/Cpusets and gather all processors and memory nodes, and ignore the fact that some resources may be offline.</dl>
<p> When this flag is not set, PUs that are disallowed are not added to the topology. Parent objects (package, core, cache, etc.) are added only if some of their children are allowed. NUMA nodes are always added but their available memory is set to 0 when disallowed.</p>
<dl>
<dt><i>HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM </i></p>
<dd> Assume that the selected backend provides the topology for the system on which we are running. This forces <code>hwloc_topology_is_thissystem()</code> to return 1, i.e. makes hwloc assume that the selected backend provides the topology for the system on which we are running, even if it is not the OS-specific backend but the XML backend for instance. This means making the binding functions actually call the OS-specific system calls and really do binding, while the XML backend would otherwise provide empty hooks just returning success.</dl>
<p> Setting the environment variable HWLOC_THISSYSTEM may also result in the same behavior. </p>
<p> This can be used for efficiency reasons to first detect the topology once, save it to an XML file, and quickly reload it later through the XML backend, but still having binding functions actually do bind.</p>
<dl>
<dt><i>HWLOC_TOPOLOGY_FLAG_IO_DEVICES </i></p>
<dd> Detect PCI devices. By default, I/O devices are ignored. This flag enables I/O device detection using the pci backend. Only the common PCI devices (GPUs, NICs, block devices, &#8230;) and host bridges (objects that connect the host objects to an I/O subsystem) will be added to the topology. Additionally it also enables MemoryModule misc objects. Uncommon devices and other bridges (such as PCI-to-PCI bridges) will be ignored.</p>
<dt><i>HWLOC_TOPOLOGY_FLAG_IO_BRIDGES </i></p>
<dd> Detect PCI bridges. This flag should be combined with <code>HWLOC_TOPOLOGY_FLAG_IO_DEVICES</code> to enable the detection of both common devices and of all useful bridges (bridges that have at least one device behind them).</p>
<dt><i>HWLOC_TOPOLOGY_FLAG_WHOLE_IO </i></p>
<dd> Detect the whole PCI hierarchy. This flag enables detection of all I/O devices (even the uncommon ones such as DMA channels) and bridges (even those that have no device behind them) using the pci backend. This implies <code>HWLOC_TOPOLOGY_FLAG_IO_DEVICES</code>.</p>
<dt><i>HWLOC_TOPOLOGY_FLAG_ICACHES </i></p>
<dd> Detect instruction caches. This flag enables detection of Instruction caches, instead of only Data and Unified caches.</dl>
<h2>Function Documentation</h2>
<h3>unsigned long hwloc_topology_get_flags (<code>hwloc_topology_t</code> topology)</h3>
<p> Get OR&#8217;ed flags of a topology. Get the OR&#8217;ed set of <code>hwloc_topology_flags_e</code> of a topology. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the flags previously set with <code>hwloc_topology_set_flags()</code>.</dl>
<h3>const struct <code>hwloc_topology_support</code>* hwloc_topology_get_support (<code>hwloc_topology_t</code> restrict topology)</h3>
<p> Retrieve the topology support.</p>
<h3>void* hwloc_topology_get_userdata (<code>hwloc_topology_t</code> topology)</h3>
<p> Retrieve the topology-specific userdata pointer. Retrieve the application-given private data pointer that was previously set with <code>hwloc_topology_set_userdata()</code>.</p>
<h3>int hwloc_topology_ignore_all_keep_structure (<code>hwloc_topology_t</code> topology)</h3>
<p> Ignore all objects that do not bring any structure. Ignore all objects that do not bring any structure: This is equivalent to calling <code>hwloc_topology_ignore_type_keep_structure()</code> for all object types.</p>
<h3>int hwloc_topology_ignore_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type)</h3>
<p> Ignore an object type. Ignore all objects from the given type. The bottom-level type <code>HWLOC_OBJ_PU</code> may not be ignored. The top-level object of the hierarchy will never be ignored, even if this function succeeds. Group objects are always ignored if they do not bring any structure since they are designed to add structure to the topology. I/O objects may not be ignored, topology flags should be used to configure their discovery instead.</p>
<h3>int hwloc_topology_ignore_type_keep_structure (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type)</h3>
<p> Ignore an object type if it does not bring any structure. Ignore all objects from the given type as long as they do not bring any structure: Each ignored object should have a single children or be the only child of its parent. The bottom-level type <code>HWLOC_OBJ_PU</code> may not be ignored. I/O objects may not be ignored, topology flags should be used to configure their discovery instead.</p>
<h3>int hwloc_topology_is_thissystem (<code>hwloc_topology_t</code> restrict topology)</h3>
<p> Does the topology context come from this system? </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if this topology context was built using the system running this program. </p>
<p> 0 instead (for instance if using another file-system root, a XML topology file, or a synthetic topology).</dl>
<h3>int hwloc_topology_set_custom (<code>hwloc_topology_t</code> topology)</h3>
<p> Prepare the topology for custom assembly. The topology then contains a single root object. It must then be built by inserting other topologies with <code>hwloc_custom_insert_topology()</code> or single objects with <code>hwloc_custom_insert_group_object_by_parent()</code>. <code>hwloc_topology_load()</code> must be called to finalize the new topology as usual. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> If nothing is inserted in the topology, <code>hwloc_topology_load()</code> will fail with errno set to EINVAL. </p>
<p> The cpuset and nodeset of the root object are NULL because these sets are meaningless when assembling multiple topologies. </p>
<p> On success, the custom component replaces the previously enabled component (if any), but the topology is not actually modified until <code>hwloc_topology_load()</code>.</dl>
<h3>int hwloc_topology_set_distance_matrix (<code>hwloc_topology_t</code> restrict topology, <code>hwloc_obj_type_t</code> type, unsigned nbobjs, unsigned * os_index, float * distances)</h3>
<p> Provide a distance matrix. Provide the matrix of distances between a set of objects of the given type. The set may or may not contain all the existing objects of this type. The objects are specified by their OS/physical index in the os_index array. The distances matrix follows the same order. The distance from object i to object j in the i*nbobjs+j. </p>
<p> A single latency matrix may be defined for each type. If another distance matrix already exists for the given type, either because the user specified it or because the OS offers it, it will be replaced by the given one. If nbobjs is 0, os_index is NULL and distances is NULL, the existing distance matrix for the given type is removed. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Distance matrices are ignored in multi-node topologies.</dl>
<h3>int hwloc_topology_set_flags (<code>hwloc_topology_t</code> topology, unsigned long flags)</h3>
<p> Set OR&#8217;ed flags to non-yet-loaded topology. Set a OR&#8217;ed set of <code>hwloc_topology_flags_e</code> onto a topology that was not yet loaded. </p>
<p> If this function is called multiple times, the last invokation will erase and replace the set of flags that was previously set. </p>
<p> The flags set in a topology may be retrieved with <code>hwloc_topology_get_flags()</code></p>
<h3>int hwloc_topology_set_fsroot (<code>hwloc_topology_t</code> restrict topology, const char *restrict fsroot_path)</h3>
<p> Change the file-system root path when building the topology from sysfs/procfs. On Linux system, use sysfs and procfs files as if they were mounted on the given fsroot_path instead of the main file-system root. Setting the environment variable HWLOC_FSROOT may also result in this behavior. Not using the main file-system root causes <code>hwloc_topology_is_thissystem()</code> to return 0. </p>
<p> Note that this function does not actually load topology information; it just tells hwloc where to load it from. You&#8217;ll still need to invoke <code>hwloc_topology_load()</code> to actually load the topology information. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS on non-Linux and on Linux systems that do not support it. </p>
<p> -1 with the appropriate errno if fsroot_path cannot be used.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> For convenience, this backend provides empty binding hooks which just return success. To have hwloc still actually call OS-specific hooks, the <code>HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM</code> has to be set to assert that the loaded file is really the underlying system. </p>
<p> On success, the Linux component replaces the previously enabled component (if any), but the topology is not actually modified until <code>hwloc_topology_load()</code>.</dl>
<h3>int hwloc_topology_set_pid (<code>hwloc_topology_t</code> restrict topology, hwloc_pid_t pid)</h3>
<p> Change which process the topology is viewed from. On some systems, processes may have different views of the machine, for instance the set of allowed CPUs. By default, hwloc exposes the view from the current process. Calling <code>hwloc_topology_set_pid()</code> permits to make it expose the topology of the machine from the point of view of another process. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> -1 is returned and errno is set to ENOSYS on platforms that do not support this feature.</dl>
<h3>int hwloc_topology_set_synthetic (<code>hwloc_topology_t</code> restrict topology, const char *restrict description)</h3>
<p> Enable synthetic topology. Gather topology information from the given description, a space-separated string of numbers describing the arity of each level. Each number may be prefixed with a type and a colon to enforce the type of a level. If only some level types are enforced, hwloc will try to choose the other types according to usual topologies, but it may fail and you may have to specify more level types manually. See also the <code>Synthetic topologies</code>. </p>
<p> If description was properly parsed and describes a valid topology configuration, this function returns 0. Otherwise -1 is returned and errno is set to EINVAL. </p>
<p> Note that this function does not actually load topology information; it just tells hwloc where to load it from. You&#8217;ll still need to invoke <code>hwloc_topology_load()</code> to actually load the topology information. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> For convenience, this backend provides empty binding hooks which just return success. </p>
<p> On success, the synthetic component replaces the previously enabled component (if any), but the topology is not actually modified until <code>hwloc_topology_load()</code>.</dl>
<h3>void hwloc_topology_set_userdata (<code>hwloc_topology_t</code> topology, const void * userdata)</h3>
<p> Set the topology-specific userdata pointer. Each topology may store one application-given private data pointer. It is initialized to NULL. hwloc will never modify it. </p>
<p> Use it as you wish, after <code>hwloc_topology_init()</code> and until hwloc_topolog_destroy(). </p>
<p> This pointer is not exported to XML.</p>
<h3>int hwloc_topology_set_xml (<code>hwloc_topology_t</code> restrict topology, const char *restrict xmlpath)</h3>
<p> Enable XML-file based topology. Gather topology information from the XML file given at xmlpath. Setting the environment variable HWLOC_XMLFILE may also result in this behavior. This file may have been generated earlier with <code>hwloc_topology_export_xml()</code> or lstopo file.xml. </p>
<p> Note that this function does not actually load topology information; it just tells hwloc where to load it from. You&#8217;ll still need to invoke <code>hwloc_topology_load()</code> to actually load the topology information. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to EINVAL on failure to read the XML file.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> See also <code>hwloc_topology_set_userdata_import_callback()</code> for importing application-specific object userdata. </p>
<p> For convenience, this backend provides empty binding hooks which just return success. To have hwloc still actually call OS-specific hooks, the <code>HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM</code> has to be set to assert that the loaded file is really the underlying system. </p>
<p> On success, the XML component replaces the previously enabled component (if any), but the topology is not actually modified until <code>hwloc_topology_load()</code>.</dl>
<h3>int hwloc_topology_set_xmlbuffer (<code>hwloc_topology_t</code> restrict topology, const char *restrict buffer, int size)</h3>
<p> Enable XML based topology using a memory buffer (instead of a file, as with <code>hwloc_topology_set_xml()</code>). Gather topology information from the XML memory buffer given at buffer and of length size. This buffer may have been filled earlier with <code>hwloc_topology_export_xmlbuffer()</code>. </p>
<p> Note that this function does not actually load topology information; it just tells hwloc where to load it from. You&#8217;ll still need to invoke <code>hwloc_topology_load()</code> to actually load the topology information. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to EINVAL on failure to read the XML buffer.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> See also <code>hwloc_topology_set_userdata_import_callback()</code> for importing application-specific object userdata. </p>
<p> For convenience, this backend provides empty binding hooks which just return success. To have hwloc still actually call OS-specific hooks, the <code>HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM</code> has to be set to assert that the loaded file is really the underlying system. </p>
<p> On success, the XML component replaces the previously enabled component (if any), but the topology is not actually modified until <code>hwloc_topology_load()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbAZ">Author</a></p>
<dd></dl>
