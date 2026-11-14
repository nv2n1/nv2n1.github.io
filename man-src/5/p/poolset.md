---
title: "poolset(5)"
name: "poolset"
section: "5"
letter: "p"
url: "/docs/linux/man/5-poolset/"
---

poolset - persistent memory pool configuration file format

<h2>Synopsis</h2>

<dl><dd><pre>mypool.set</pre></dl>

<h2>Description</h2>

Depending on the configuration of the system, the available non-volatile memory space may be divided into multiple memory devices. In such case, the maximum size of the transactional object store could be limited by the capacity of a single memory device. Therefore, <a HREF="/docs/linux/man/7-libpmemobj/">libpmemobj</a>(7), <a HREF="/docs/linux/man/7-libpmemblk/">libpmemblk</a>(7) and <a HREF="/docs/linux/man/7-libpmemlog/">libpmemlog</a>(7) allow building object stores spanning multiple memory devices by creation of persistent memory pools consisting of multiple files, where each part of such a pool set may be stored on a different pmem-aware filesystem. 

 To improve reliability and eliminate single point of failure, <a HREF="/docs/linux/man/7-libpmemobj/">libpmemobj</a>(7) also allows all the data written to a persistent memory pool to be copied to local or remote pool replicas, thereby providing backup for the persistent memory pool by producing a mirrored pool set. In practice, the pool replicas may be considered as binary copies of the "master" pool set. Data replication is not supported in <a HREF="/docs/linux/man/7-libpmemblk/">libpmemblk</a>(7) and <a HREF="/docs/linux/man/7-libpmemlog/">libpmemlog</a>(7). 

 The set file for each type of pool is a plain text file. Lines in the file are formatted as follows:
<dl><dt>&bull;
<dd>The first line of the file must be the literal string "PMEMPOOLSET"
<dt>&bull;
<dd>The pool parts are specified, one per line, in the format:
<dl><dd>size pathname</dl><dt>&bull;
<dd>Replica sections, if any, start with the literal string "REPLICA". See REPLICAS, below, for further details.
<dt>&bull;
<dd>Pool set options, if any, start with literal string OPTION. See POOL SET OPTIONS below for details.
<dt>&bull;
<dd>Lines starting with "#" are considered comments and are ignored.</dl>
 

 The size must be compliant with the format specified in IEC 80000-13, IEEE 1541 or the Metric Interchange Format. These standards accept SI units with obligatory B - kB, MB, GB, ... (multiplier by 1000) suffixes, and IEC units with optional "iB" - KiB, MiB, GiB, ..., K, M, G, ... - (multiplier by 1024) suffixes. 

 pathname must be an absolute pathname. 

 The pathname of a part can point to a Device DAX. Device DAX is the device-centric analogue of Filesystem DAX. It allows memory ranges to be allocated and mapped without need of an intervening file system. 

 Pools created on Device DAX have additional options and restrictions:
<dl><dt>&bull;
<dd>The size may be set to "AUTO", in which case the size of the device will be automatically resolved at pool creation time.
<dt>&bull;
<dd>To concatenate more than one Device DAX device into a single pool set, the configured internal alignment of the devices must be 4KiB, unless the SINGLEHDR or NOHDRS option is used in the pool set file. See POOL SET OPTIONS below for details.</dl>
 

 Please see <a HREF="/docs/linux/man/1-ndctl-create-namespace/">ndctl-create-namespace</a>(1) for more information on Device DAX, including how to configure desired alignment. 

 The minimum file size of each part of the pool set is defined as follows:
<dl><dt>&bull;
<dd>For block pools, as PMEMBLK_MIN_PART in &lt;libpmemblk.h&gt;
<dt>&bull;
<dd>For object pools, as PMEMOBJ_MIN_PART in &lt;libpmemobj.h&gt;
<dt>&bull;
<dd>For log pools, as PMEMLOG_MIN_PART in &lt;libpmemlog.h&gt;</dl>
 

 The net pool size of the pool set is equal to:
<dl><dd><pre>net_pool_size&nbsp;=&nbsp;sum_over_all_parts(page_aligned_part_size - 4KiB)&nbsp;+&nbsp;4KiB</pre></dl>
 

 where
<dl><dd><pre>page_aligned_part_size&nbsp;=&nbsp;part_size&nbsp;&amp;&nbsp;~(page_size - 1)</pre></dl>
 

 Note that page size is OS specific. For more information please see <a HREF="/docs/linux/man/3-sysconf/">sysconf</a>(3). 

 The minimum net pool size of a pool set is defined as follows:
<dl><dt>&bull;
<dd>For block pools, as PMEMBLK_MIN_POOL in &lt;libpmemblk.h&gt;
<dt>&bull;
<dd>For object pools, as PMEMOBJ_MIN_POOL in &lt;libpmemobj.h&gt;
<dt>&bull;
<dd>For log pools, as PMEMLOG_MIN_POOL in &lt;libpmemlog.h&gt;</dl>
 

 Here is an example "mypool.set" file:
<dl><dd><pre>PMEMPOOLSET
OPTION NOHDRS
100G&nbsp;/mountpoint0/myfile.part0
200G&nbsp;/mountpoint1/myfile.part1
400G&nbsp;/mountpoint2/myfile.part2</pre></dl>
 

 The files in the set may be created by running one of the following commands. To create a block pool:
<dl><dd><pre>$&nbsp;pmempool create blk&nbsp;&lt;bsize&gt;&nbsp;mypool.set</pre></dl>
 

 To create a log pool:
<dl><dd><pre>$&nbsp;pmempool create log mypool.set</pre></dl>

<h2>Replicas</h2>

Sections defining replica sets are optional. There may be multiple replica sections. 

 Local replica sections begin with a line containing only the literal string "REPLICA", followed by one or more pool part lines as described above. 

 Remote replica sections consist of the REPLICA keyword, followed on the same line by the address of a remote host and a relative path to a remote pool set file:
<dl><dd><pre>REPLICA&nbsp;[&lt;user&gt;@]&lt;hostname&gt;&nbsp;[&lt;relative-path&gt;/]&lt;remote-pool-set-file&gt;</pre><dt>&bull;
<dd>hostname must be in the format recognized by the <a HREF="/docs/linux/man/1-ssh/">ssh</a>(1) remote login client
<dt>&bull;
<dd>pathname is relative to the root config directory on the target node - see <a HREF="/docs/linux/man/7-librpmem/">librpmem</a>(7)</dl>
 

 There are no other lines in the remote replica section - the REPLICA line defines a remote replica entirely. 

 Here is an example "myobjpool.set" file with replicas:
<dl><dd><pre>PMEMPOOLSET
100G&nbsp;/mountpoint0/myfile.part0
200G&nbsp;/mountpoint1/myfile.part1
400G&nbsp;/mountpoint2/myfile.part2
#&nbsp;local replica
REPLICA
500G&nbsp;/mountpoint3/mymirror.part0
200G&nbsp;/mountpoint4/mymirror.part1&nbsp;
#&nbsp;remote replica
REPLICA user [at] example.com remote-objpool.set</pre></dl>
 

 The files in the object pool set may be created by running the following command:
<dl><dd><pre>$&nbsp;pmempool create --layout=&quot;mylayout&quot;&nbsp;obj myobjpool.set</pre></dl>
 

 Remote replica cannot have replicas, i.e. a remote pool set file cannot define any replicas.

<h2>Pool Set Options</h2>

Pool set options can appear anywhere after the line with PMEMPOOLSET string. Pool set file can contain several pool set options. The following options are supported:
<dl><dt>&bull;
<dd>SINGLEHDR
<dt>&bull;
<dd>NOHDRS</dl>
 

 If the SINGLEHDR option is used, only the first part in each replica contains the pool part internal metadata. In that case the effective size of a replica is the sum of sizes of all its part files decreased once by 4096 bytes. 

 The NOHDRS option can appear only in the remote pool set file, when librpmem does not serve as a means of replication for libpmemobj pool. In that case none of the pool parts contains internal metadata. The effective size of such a replica is the sum of sizes of all its part files. 

 Options SINGLEHDR and NOHDRS are mutually exclusive. If both are specified in a pool set file, creating or opening the pool will fail with an error. 

 When using the SINGLEHDR or NOHDRS option, one can concatenate more than one Device DAX devices with any internal alignments in one replica. 

 The SINGLEHDR option concerns only replicas that are local to the pool set file. That is if one wants to create a pool set with the SINGLEHDR option and with remote replicas, one has to add this option to the local pool set file as well as to every single remote pool set file. 

 Using the SINGLEHDR and NOHDRS options has important implications for data integrity checking and recoverability in case of a pool set damage. See pmempool_sync() API for more information about pool set recovery.

<h2>Directories</h2>

Providing a directory as a part's pathname allows the pool to dynamically create files and consequently removes the user-imposed limit on the size of the pool. 

 The size argument of a part in a directory poolset becomes the size of the address space reservation required for the pool. In other words, the size argument is the maximum theoretical size of the mapping. This value can be freely increased between instances of the application, but decreasing it below the real required space will result in an error when attempting to open the pool. 

 The directory must NOT contain user created files with extension .pmem, otherwise the behavior is undefined. If a file created by the library within the directory is in any way altered (resized, renamed) the behavior is undefined. 

 A directory poolset must exclusively use directories to specify paths - combining files and directories will result in an error. A single replica can consist of one or more directories. If there are multiple directories, the address space reservation is equal to the sum of the sizes. 

 The order in which the files are created is unspecified, but the library will try to maintain equal usage of the directories. 

 By default pools grow in 128 megabyte increments. 

 Only poolsets with the SINGLEHDR option can safely use directories.

<h2>Notes</h2>

Creation of all the parts of the pool set and the associated replica sets can be done with the <a HREF="/docs/linux/man/3-pmemobj_create/">pmemobj_create</a>(3), <a HREF="/docs/linux/man/3-pmemblk_create/">pmemblk_create</a>(3) or <a HREF="/docs/linux/man/3-pmemlog_create/">pmemlog_create</a>(3) function, or by using the <a HREF="/docs/linux/man/1-pmempool/">pmempool</a>(1) utility. 

 Restoring data from a local or remote replica can be done by using the <a HREF="/docs/linux/man/1-pmempool-sync/">pmempool-sync</a>(1) command or the pmempool_sync() API from the <a HREF="/docs/linux/man/7-libpmempool/">libpmempool</a>(7) library. 

 Modifications of a pool set file configuration can be done by using the <a HREF="/docs/linux/man/1-pmempool-transform/">pmempool-transform</a>(1) command or the pmempool_transform() API from the <a HREF="/docs/linux/man/7-libpmempool/">libpmempool</a>(7) library. 

 When creating a pool set consisting of multiple files, or when creating a replicated pool set, the path argument passed to <a HREF="/docs/linux/man/3-pmemobj_create/">pmemobj_create</a>(3), <a HREF="/docs/linux/man/3-pmemblk_create/">pmemblk_create</a>(3) or <a HREF="/docs/linux/man/3-pmemlog_create/">pmemlog_create</a>(3) must point to the special set file that defines the pool layout and the location of all the parts of the pool set. 

 When opening a pool set consisting of multiple files, or when opening a replicated pool set, the path argument passed to <a HREF="/docs/linux/man/3-pmemobj_open/">pmemobj_open</a>(3), <a HREF="/docs/linux/man/3-pmemblk_open/">pmemblk_open</a>(3) or <a HREF="/docs/linux/man/3-pmemlog_open/">pmemlog_open</a>(3) must point to the same set file that was used for pool set creation.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-ndctl-create-namespace/">ndctl-create-namespace</a>(1), <a HREF="/docs/linux/man/3-pmemblk_create/">pmemblk_create</a>(3), <a HREF="/docs/linux/man/3-pmemlog_create/">pmemlog_create</a>(3), <a HREF="/docs/linux/man/3-pmemobj_create/">pmemobj_create</a>(3), <a HREF="/docs/linux/man/3-sysconf/">sysconf</a>(3), <a HREF="/docs/linux/man/7-libpmemblk/">libpmemblk</a>(7), <a HREF="/docs/linux/man/7-libpmemlog/">libpmemlog</a>(7), <a HREF="/docs/linux/man/7-libpmemobj/">libpmemobj</a>(7) and &lt;<a rel="nofollow" HREF="https://pmem.io">https://pmem.io</a>&gt; 
