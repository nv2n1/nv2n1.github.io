---
title: "dl_iterate_phdr(3)"
name: "dl_iterate_phdr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dl_iterate_phdr/"
description: "dl_iterate_phdr – walk through list of shared objects"
---

<h2 class="name">NAME</h2>
<p> dl_iterate_phdr &#8211; walk through list of shared objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;link.h&gt;
int dl_iterate_phdr(
    int (*callback)(struct dl_phdr_info *info,
                    size_t size, void *data),
    void *data);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dl_iterate_phdr</code>() function allows an application to inquire at run time to find out which shared objects it has loaded, and the order in which they were loaded. </p>
<p> The <code>dl_iterate_phdr</code>() function walks through the list of an application&#8217;s shared objects and calls the function <i>callback</i> once for each object, until either all shared objects have been processed or <i>callback</i> returns a nonzero value. </p>
<p> Each call to <i>callback</i> receives three arguments: <i>info</i>, which is a pointer to a structure containing information about the shared object; <i>size</i>, which is the size of the structure pointed to by <i>info</i>; and <i>data</i>, which is a copy of whatever value was passed by the calling program as the second argument (also named <i>data</i>) in the call to <code>dl_iterate_phdr</code>(). </p>
<p> The <i>info</i> argument is a structure of the following type: </p>
<p> struct dl_phdr_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfW(Addr)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dlpi_addr;&nbsp;<wbr>&nbsp;/*&nbsp;Base address of object&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dlpi_name;&nbsp;<wbr>&nbsp;/*&nbsp;(Null-terminated)&nbsp;name of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;object&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const ElfW(Phdr)&nbsp;*dlpi_phdr;&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to array of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ELF program headers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for this object&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfW(Half)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dlpi_phnum;&nbsp;/*&nbsp;#&nbsp;of items in&nbsp;<i>dlpi_phdr</i>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The following fields were added in glibc 2.4, after the first<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;version of this structure was available.&nbsp;<wbr>&nbsp;Check the&nbsp;<i>size</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argument passed to the dl_iterate_phdr callback to determine<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;whether or not each later member is available.&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long long dlpi_adds;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Incremented when a new object may<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;have been added&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long long dlpi_subs;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Incremented when an object may<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;have been removed&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t dlpi_tls_modid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If there is a PT_TLS segment, its module<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ID as used in TLS relocations, else zero&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*dlpi_tls_data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The address of the calling thread&#8217;s instance<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of this module&#8217;s PT_TLS segment, if it has<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;one and it has been allocated in the calling<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;thread, otherwise a null pointer&nbsp;*/ }; </p>
<p> (The <i>ElfW</i>() macro definition turns its argument into the name of an ELF data type suitable for the hardware architecture. For example, on a 32-bit platform, <i>ElfW(Addr)</i> yields the data type name <i>Elf32_Addr</i>. Further information on these types can be found in the <i>&lt;elf.h&gt;</i> and <i>&lt;link.h&gt;</i> header files.) </p>
<p> The <i>dlpi_addr</i> field indicates the base address of the shared object (i.e., the difference between the virtual memory address of the shared object and the offset of that object in the file from which it was loaded). The <i>dlpi_name</i> field is a null-terminated string giving the pathname from which the shared object was loaded. </p>
<p> To understand the meaning of the <i>dlpi_phdr</i> and <i>dlpi_phnum</i> fields, we need to be aware that an ELF shared object consists of a number of segments, each of which has a corresponding program header describing the segment. The <i>dlpi_phdr</i> field is a pointer to an array of the program headers for this shared object. The <i>dlpi_phnum</i> field indicates the size of this array. </p>
<p> These program headers are structures of the following form: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word&nbsp;<wbr>&nbsp;p_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Off&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_offset;&nbsp;<wbr>&nbsp;/*&nbsp;Segment file offset&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr&nbsp;<wbr>&nbsp;p_vaddr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment virtual address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr&nbsp;<wbr>&nbsp;p_paddr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment physical address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word&nbsp;<wbr>&nbsp;p_filesz;&nbsp;<wbr>&nbsp;/*&nbsp;Segment size in file&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word&nbsp;<wbr>&nbsp;p_memsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment size in memory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word&nbsp;<wbr>&nbsp;p_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word&nbsp;<wbr>&nbsp;p_align;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Segment alignment&nbsp;*/ } Elf32_Phdr; </p>
<p> Note that we can calculate the location of a particular program header, <i>x</i>, in virtual memory using the formula: </p>
<p> addr == info-&gt;dlpi_addr + info-&gt;dlpi_phdr[x].p_vaddr; </p>
<p> Possible values for <i>p_type</i> include the following (see <i>&lt;elf.h&gt;</i> for further details): </p>
<p> #define PT_LOAD 1 /* Loadable program segment */ #define PT_DYNAMIC 2 /* Dynamic linking information */ #define PT_INTERP 3 /* Program interpreter */ #define PT_NOTE 4 /* Auxiliary information */ #define PT_SHLIB 5 /* Reserved */ #define PT_PHDR 6 /* Entry for header table itself */ #define PT_TLS 7 /* Thread-local storage segment */ #define PT_GNU_EH_FRAME 0x6474e550 /* GCC .eh_frame_hdr segment */ #define PT_GNU_STACK 0x6474e551 /* Indicates stack executability */ #define PT_GNU_RELRO 0x6474e552 /* Read-only after relocation */</p>
<h2>RETURN VALUE</h2>
<p> The <code>dl_iterate_phdr</code>() function returns whatever value was returned by the last call to <i>callback</i>.</p>
<h2>VERSIONS</h2>
<p> <code>dl_iterate_phdr</code>() has been supported in glibc since version 2.2.4.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>dl_iterate_phdr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The <code>dl_iterate_phdr</code>() function is not specified in any standard. Various other systems provide a version of this function, although details of the returned <i>dl_phdr_info</i> structure differ. On the BSDs and Solaris, the structure includes the fields <i>dlpi_addr</i>, <i>dlpi_name</i>, <i>dlpi_phdr</i>, and <i>dlpi_phnum</i> in addition to other implementation-specific fields.</p>
<h2>NOTES</h2>
<p> Future versions of the C library may add further fields to the <i>dl_phdr_info</i> structure; in that event, the <i>size</i> argument provides a mechanism for the callback function to discover whether it is running on a system with added fields. </p>
<p> The first object visited by <i>callback</i> is the main program. For the main program, the <i>dlpi_name</i> field will be an empty string.</p>
<h2>EXAMPLES</h2>
<p> The following program displays a list of pathnames of the shared objects it has loaded. For each shared object, the program lists some information (virtual address, size, flags, and type) for each of the objects ELF segments. </p>
<p> The following shell session demonstrates the output produced by the program on an x86-64 system. The first shared object for which output is displayed (where the name is an empty string) is the main program. </p>
<p> $ <code>./a.out</code> Name: &quot;&quot; (9 segments)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x400040;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1f8]&nbsp;flags: 0x5;&nbsp;PT_PHDR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x400238;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1c]&nbsp;flags: 0x4;&nbsp;PT_INTERP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x400000;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ac4]&nbsp;flags: 0x5;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x600e10;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;240]&nbsp;flags: 0x6;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x600e28;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1d0]&nbsp;flags: 0x6;&nbsp;PT_DYNAMIC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x400254;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;44]&nbsp;flags: 0x4;&nbsp;PT_NOTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x400970;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3c]&nbsp;flags: 0x4;&nbsp;PT_GNU_EH_FRAME<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(nil);&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0]&nbsp;flags: 0x6;&nbsp;PT_GNU_STACK<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8:&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x600e10;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1f0]&nbsp;flags: 0x4;&nbsp;PT_GNU_RELRO Name: &quot;linux-vdso.so.1&quot; (4 segments)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:&nbsp;[0x7ffc6edd1000;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e89]&nbsp;flags: 0x5;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1:&nbsp;[0x7ffc6edd1360;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;110]&nbsp;flags: 0x4;&nbsp;PT_DYNAMIC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2:&nbsp;[0x7ffc6edd17b0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3c]&nbsp;flags: 0x4;&nbsp;PT_NOTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3:&nbsp;[0x7ffc6edd17ec;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3c]&nbsp;flags: 0x4;&nbsp;PT_GNU_EH_FRAME Name: &quot;/lib64/libc.so.6&quot; (10 segments)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:&nbsp;[0x7f55712ce040;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;230]&nbsp;flags: 0x5;&nbsp;PT_PHDR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1:&nbsp;[0x7f557145b980;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1c]&nbsp;flags: 0x4;&nbsp;PT_INTERP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2:&nbsp;[0x7f55712ce000;&nbsp;memsz: 1b6a5c]&nbsp;flags: 0x5;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3:&nbsp;[0x7f55716857a0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;9240]&nbsp;flags: 0x6;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4:&nbsp;[0x7f5571688b80;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1f0]&nbsp;flags: 0x6;&nbsp;PT_DYNAMIC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5:&nbsp;[0x7f55712ce270;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;44]&nbsp;flags: 0x4;&nbsp;PT_NOTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6:&nbsp;[0x7f55716857a0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;78]&nbsp;flags: 0x4;&nbsp;PT_TLS<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7:&nbsp;[0x7f557145b99c;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;544c]&nbsp;flags: 0x4;&nbsp;PT_GNU_EH_FRAME<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8:&nbsp;[0x7f55712ce000;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0]&nbsp;flags: 0x6;&nbsp;PT_GNU_STACK<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;9:&nbsp;[0x7f55716857a0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;3860]&nbsp;flags: 0x4;&nbsp;PT_GNU_RELRO Name: &quot;/lib64/ld-linux-x86-64.so.2&quot; (7 segments)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:&nbsp;[0x7f557168f000;&nbsp;memsz:&nbsp;<wbr>&nbsp;20828]&nbsp;flags: 0x5;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1:&nbsp;[0x7f55718afba0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;15a8]&nbsp;flags: 0x6;&nbsp;PT_LOAD<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2:&nbsp;[0x7f55718afe10;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;190]&nbsp;flags: 0x6;&nbsp;PT_DYNAMIC<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3:&nbsp;[0x7f557168f1c8;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;24]&nbsp;flags: 0x4;&nbsp;PT_NOTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4:&nbsp;[0x7f55716acec4;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;604]&nbsp;flags: 0x4;&nbsp;PT_GNU_EH_FRAME<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5:&nbsp;[0x7f557168f000;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0]&nbsp;flags: 0x6;&nbsp;PT_GNU_STACK<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6:&nbsp;[0x7f55718afba0;&nbsp;memsz:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;460]&nbsp;flags: 0x4;&nbsp;PT_GNU_RELRO</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;link.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;stdint.h&gt; </p>
<p> static int callback(struct dl_phdr_info *info, size_t size, void *data) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int p_type; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Name:&nbsp;\&quot;%s\&quot;&nbsp;(%d segments)
&quot;, info-&gt;dlpi_name,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info-&gt;dlpi_phnum); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;info-&gt;dlpi_phnum;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_type&nbsp;=&nbsp;info-&gt;dlpi_phdr[j].p_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type&nbsp;=&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_LOAD)&nbsp;?&nbsp;&quot;PT_LOAD&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_DYNAMIC)&nbsp;?&nbsp;&quot;PT_DYNAMIC&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_INTERP)&nbsp;?&nbsp;&quot;PT_INTERP&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_NOTE)&nbsp;?&nbsp;&quot;PT_NOTE&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_INTERP)&nbsp;?&nbsp;&quot;PT_INTERP&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_PHDR)&nbsp;?&nbsp;&quot;PT_PHDR&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_TLS)&nbsp;?&nbsp;&quot;PT_TLS&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_GNU_EH_FRAME)&nbsp;?&nbsp;&quot;PT_GNU_EH_FRAME&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_GNU_STACK)&nbsp;?&nbsp;&quot;PT_GNU_STACK&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(p_type&nbsp;==&nbsp;PT_GNU_RELRO)&nbsp;?&nbsp;&quot;PT_GNU_RELRO&quot;&nbsp;: NULL; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%2d:&nbsp;[%14p;&nbsp;memsz:%7jx]&nbsp;flags:&nbsp;%#jx;&nbsp;&quot;, j,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(void&nbsp;*)&nbsp;(info-&gt;dlpi_addr&nbsp;+&nbsp;info-&gt;dlpi_phdr[j].p_vaddr),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;info-&gt;dlpi_phdr[j].p_memsz,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;info-&gt;dlpi_phdr[j].p_flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(type&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, type);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;[other&nbsp;(%#x)]
&quot;, p_type);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dl_iterate_phdr(callback, NULL); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), <code><a href="/docs/linux/man/1-readelf/">readelf</a></code>(1), <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/5-elf/">elf</a></code>(5), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) </p>
<p> <i>Executable and Linking Format Specification</i>, available at various locations online.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
