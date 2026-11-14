---
title: "dladdr(3)"
name: "dladdr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dladdr/"
description: "dladdr, dladdr1 – translate address to symbolic information"
---

<h2 class="name">NAME</h2>
<p> dladdr, dladdr1 &#8211; translate address to symbolic information </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE
#include &lt;dlfcn.h&gt;
int dladdr(void *addr, Dl_info *info);
int dladdr1(void *addr, Dl_info *info, void **extra_info, int flags);
Link with - ldl.
</code></pre>
<h2>DESCRIPTION</h2>
<p> The function <code>dladdr</code>() determines whether the address specified in <i>addr</i> is located in one of the shared objects loaded by the calling application. If it is, then <code>dladdr</code>() returns information about the shared object and symbol that overlaps <i>addr</i>. This information is returned in a <i>Dl_info</i> structure: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;*dli_fname;&nbsp;<wbr>&nbsp;/*&nbsp;Pathname of shared object that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;contains address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dli_fbase;&nbsp;<wbr>&nbsp;/*&nbsp;Base address at which shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;object is loaded&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;*dli_sname;&nbsp;<wbr>&nbsp;/*&nbsp;Name of symbol whose definition<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overlaps&nbsp;<i>addr</i>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*dli_saddr;&nbsp;<wbr>&nbsp;/*&nbsp;Exact address of symbol named<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in&nbsp;<i>dli_sname</i>&nbsp;*/ } Dl_info; </p>
<p> If no symbol matching <i>addr</i> could be found, then <i>dli_sname</i> and <i>dli_saddr</i> are set to NULL. </p>
<p> The function <code>dladdr1</code>() is like <code>dladdr</code>(), but returns additional information via the argument <i>extra_info</i>. The information returned depends on the value specified in <i>flags</i>, which can have one of the following values:</p>
<dl>
<dt><code>RTLD_DL_LINKMAP</code></p>
<dd> Obtain a pointer to the link map for the matched file. The <i>extra_info</i> argument points to a pointer to a <i>link_map</i> structure (i.e., <i>struct link_map&nbsp;**</i>), defined in <i>&lt;link.h&gt;</i> as:</p>
<dt>
<dd> struct link_map {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfW(Addr)&nbsp;l_addr;&nbsp;<wbr>&nbsp;/*&nbsp;Difference between the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address in the ELF file and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the address in memory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*l_name;&nbsp;<wbr>&nbsp;/*&nbsp;Absolute pathname where<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;object was found&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfW(Dyn)&nbsp;*l_ld;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Dynamic section of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shared object&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct link_map&nbsp;*l_next,&nbsp;*l_prev;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Chain of loaded objects&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Plus additional fields private to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implementation&nbsp;*/ };</p>
<dt><code>RTLD_DL_SYMENT</code></p>
<dd> Obtain a pointer to the ELF symbol table entry of the matching symbol. The <i>extra_info</i> argument is a pointer to a symbol pointer: <i>const ElfW(Sym) **</i>. The <i>ElfW</i>() macro definition turns its argument into the name of an ELF data type suitable for the hardware architecture. For example, on a 64-bit platform, <i>ElfW(Sym)</i> yields the data type name <i>Elf64_Sym</i>, which is defined in <i>&lt;elf.h&gt;</i> as:</p>
<dt>
<dd> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Word&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Symbol name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_info;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Symbol type and binding&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_other;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Symbol visibility&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Section st_shndx;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Section index&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Symbol value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Xword&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Symbol size&nbsp;*/ } Elf64_Sym;</p>
<dt>
<dd> The <i>st_name</i> field is an index into the string table.</p>
<dt>
<dd> The <i>st_info</i> field encodes the symbol&#8217;s type and binding. The type can be extracted using the macro <code>ELF64_ST_TYPE(st_info)</code> (or <code>ELF32_ST_TYPE()</code> on 32-bit platforms), which yields one of the following values: </p>
<table>
<tr VALIGN=top>
<td><code>Value</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_NOTYPE</code></td>
<td>Symbol type is unspecified
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_OBJECT</code></td>
<td>Symbol is a data object
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_FUNC</code></td>
<td>Symbol is a code object
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_SECTION</code></td>
<td>Symbol associated with a section
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_FILE</code></td>
<td>Symbol&#8217;s name is filename
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_COMMON</code></td>
<td>Symbol is a common data object
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_TLS</code></td>
<td>Symbol is thread-local data object
</td>
</tr>
<tr VALIGN=top>
<td><code>STT_GNU_IFUNC</code></td>
<td>Symbol is indirect code object
</td>
</tr>
</table>
<dt>
<dd> The symbol binding can be extracted from the <i>st_info</i> field using the macro <code>ELF64_ST_BIND(st_info)</code> (or <code>ELF32_ST_BIND()</code> on 32-bit platforms), which yields one of the following values: </p>
<table>
<tr VALIGN=top>
<td><code>Value</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>STB_LOCAL</code></td>
<td>Local symbol
</td>
</tr>
<tr VALIGN=top>
<td><code>STB_GLOBAL</code></td>
<td>Global symbol
</td>
</tr>
<tr VALIGN=top>
<td><code>STB_WEAK</code></td>
<td>Weak symbol
</td>
</tr>
<tr VALIGN=top>
<td><code>STB_GNU_UNIQUE</code></td>
<td>Unique symbol
</td>
</tr>
</table>
<dt>
<dd> The <i>st_other</i> field contains the symbol&#8217;s visibility, which can be extracted using the macro <code>ELF64_ST_VISIBILITY(st_info)</code> (or <code>ELF32_ST_VISIBILITY()</code> on 32-bit platforms), which yields one of the following values: </p>
<table>
<tr VALIGN=top>
<td><code>Value</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>STV_DEFAULT</code></td>
<td>Default symbol visibility rules
</td>
</tr>
<tr VALIGN=top>
<td><code>STV_INTERNAL</code></td>
<td>Processor-specific hidden class
</td>
</tr>
<tr VALIGN=top>
<td><code>STV_HIDDEN</code></td>
<td>Symbol unavailable in other modules
</td>
</tr>
<tr VALIGN=top>
<td><code>STV_PROTECTED</code></td>
<td>Not preemptible, not exported
</td>
</tr>
</table>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, these functions return a nonzero value. If the address specified in <i>addr</i> could be matched to a shared object, but not to a symbol in the shared object, then the <i>info-&gt;dli_sname</i> and <i>info-&gt;dli_saddr</i> fields are set to NULL. </p>
<p> If the address specified in <i>addr</i> could not be matched to a shared object, then these functions return 0. In this case, an error message is <i>not</i> available via <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> <code>dladdr</code>() is present in glibc 2.0 and later. <code>dladdr1</code>() first appeared in glibc 2.3.3.</p>
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
<td> <code>dladdr</code>(), <code>dladdr1</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard GNU extensions that are also present on Solaris.</p>
<h2>BUGS</h2>
<p> Sometimes, the function pointers you pass to <code>dladdr</code>() may surprise you. On some architectures (notably i386 and x86-64), <i>dli_fname</i> and <i>dli_fbase</i> may end up pointing back at the object from which you called <code>dladdr</code>(), even if the function used as an argument should come from a dynamically linked library. </p>
<p> The problem is that the function pointer will still be resolved at compile time, but merely point to the <i>plt</i> (Procedure Linkage Table) section of the original object (which dispatches the call after asking the dynamic linker to resolve the symbol). To work around this, you can try to compile the code to be position-independent: then, the compiler cannot prepare the pointer at compile time any more and <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) will generate code that just loads the final symbol address from the <i>got</i> (Global Offset Table) at run time before passing it to <code>dladdr</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3), <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
