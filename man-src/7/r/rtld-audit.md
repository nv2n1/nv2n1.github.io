---
title: "rtld-audit(7)"
name: "rtld-audit"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rtld-audit/"
description: "rtld-audit – auditing API for the dynamic linker"
---

<p>rtld-audit &#8211; auditing API for the dynamic linker</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE             /* See feature_test_macros(7) */
#include &lt;link.h&gt;</code></pre>
<h2>Description</h2>
<p>The GNU dynamic linker (run-time linker) provides an auditing API that allows an application to be notified when various dynamic linking events occur. This API is very similar to the auditing interface provided by the Solaris run-time linker. The necessary constants and prototypes are defined by including <i>&lt;link.h&gt;</i>. To use this interface, the programmer creates a shared library that implements a standard set of function names. Not all of the functions need to be implemented: in most cases, if the programmer is not interested in a particular class of auditing event, then no implementation needs to be provided for the corresponding auditing function. To employ the auditing interface, the environment variable <code>LD_AUDIT</code> must be defined to contain a colon-separated list of shared libraries, each of which can implement (parts of) the auditing API. When an auditable event occurs, the corresponding function is invoked in each library, in the order that the libraries are listed.</p>
<h3>la_version()</h3>
<pre><code>unsigned int la_version(unsigned int </code><i>version</i><code>);</code></pre>
<p>This is the only function that <i>must</i> be defined by an auditing library: it performs the initial handshake between the dynamic linker and the auditing library. When invoking this function, the dynamic linker passes, in <i>version</i>, the highest version of the auditing interface that the linker supports. A typical implementation of this function simply returns the constant <code>LAV_CURRENT</code>, which indicates the version of <i>&lt;link.h&gt;</i> that was used to build the audit module. If the dynamic linker does not support this version of the audit interface, it will refuse to activate this audit module. If the function returns zero, the dynamic linker also does not activate this audit module. In order to enable backwards compatibility with older dynamic linkers, an audit module can examine the <i>version</i> argument and return an earlier version than <code>LAV_CURRENT</code>, assuming the module can adjust its implementation to match the requirements of the previous version of the audit interface. The <code>la_version</code> function should not return the value of <i>version</i> without further checks because it could correspond to an interface that does not match the <i>&lt;link.h&gt;</i> definitions used to build the audit module.</p>
<h3>la_objsearch()</h3>
<pre><code>char *la_objsearch(const char *</code><i>name</i><code>, uintptr_t *</code><i>cookie</i><code>,</code>
<code> unsigned int </code><i>flag</i><code>);</code></pre>
<p>The dynamic linker invokes this function to inform the auditing library that it is about to search for a shared object. The <i>name</i> argument is the filename or pathname that is to be searched for. <i>cookie</i> identifies the shared object that initiated the search. <i>flag</i> is set to one of the following values:</p>
<dl>
<dt><code>LA_SER_ORIG</code></p>
<dd>This is the original name that is being searched for. Typically, this name comes from an ELF <code>DT_NEEDED</code> entry, or is the <i>filename</i> argument given to <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3).</p>
<dt><code>LA_SER_LIBPATH</code></p>
<dd><i>name</i> was created using a directory specified in <code>LD_LIBRARY_PATH</code>.</p>
<dt><code>LA_SER_RUNPATH</code></p>
<dd><i>name</i> was created using a directory specified in an ELF <code>DT_RPATH</code> or <code>DT_RUNPATH</code> list.</p>
<dt><code>LA_SER_CONFIG</code></p>
<dd><i>name</i> was found via the <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8) cache (<i>/etc/ld.so.cache</i>).</p>
<dt><code>LA_SER_DEFAULT</code></p>
<dd><i>name</i> was found via a search of one of the default directories.</p>
<dt><code>LA_SER_SECURE</code></p>
<dd><i>name</i> is specific to a secure object (unused on Linux).</dl>
<p> As its function result, <code>la_objsearch</code>() returns the pathname that the dynamic linker should use for further processing. If NULL is returned, then this pathname is ignored for further processing. If this audit library simply intends to monitor search paths, then <i>name</i> should be returned.</p>
<h3>la_activity()</h3>
<pre><code>void la_activity( uintptr_t *</code><i>cookie</i><code>, unsigned int flag</code><i>);</i></pre>
<p>The dynamic linker calls this function to inform the auditing library that link-map activity is occurring. <i>cookie</i> identifies the object at the head of the link map. When the dynamic linker invokes this function, <i>flag</i> is set to one of the following values:</p>
<dl>
<dt><code>LA_ACT_ADD</code></p>
<dd>New objects are being added to the link map.</p>
<dt><code>LA_ACT_DELETE</code></p>
<dd>Objects are being removed from the link map.</p>
<dt><code>LA_ACT_CONSISTENT</code></p>
<dd>Link-map activity has been completed: the map is once again consistent.</dl>
<h3>la_objopen()</h3>
<pre><code>unsigned int la_objopen(struct link_map *</code><i>map</i><code>, Lmid_t </code><i>lmid</i><code>,</code>
<code> uintptr_t *</code><i>cookie</i><code>);</code></pre>
<p>The dynamic linker calls this function when a new shared object is loaded. The <i>map</i> argument is a pointer to a link-map structure that describes the object. The <i>lmid</i> field has one of the following values</p>
<dl>
<dt><code>LM_ID_BASE</code></p>
<dd>Link map is part of the initial namespace.</p>
<dt><code>LM_ID_NEWLM</code></p>
<dd>Link map is part of a new namespace requested via <code><a href="/docs/linux/man/3-dlmopen/">dlmopen</a></code>(3).</dl>
<p> <i>cookie</i> is a pointer to an identifier for this object. The identifier is provided to later calls to functions in the auditing library in order to identify this object. This identifier is initialized to point to object&#8217;s link map, but the audit library can change the identifier to some other value that it may prefer to use to identify the object. As its return value, <code>la_objopen</code>() returns a bit mask created by ORing zero or more of the following constants, which allow the auditing library to select the objects to be monitored by <code>la_symbind*</code>():</p>
<dl>
<dt><code>LA_FLG_BINDTO</code></p>
<dd>Audit symbol bindings to this object.</p>
<dt><code>LA_FLG_BINDFROM</code></p>
<dd>Audit symbol bindings from this object.</dl>
<p> A return value of 0 from <code>la_objopen</code>() indicates that no symbol bindings should be audited for this object.</p>
<h3>la_objclose()</h3>
<pre><code>unsigned int la_objclose(uintptr_t *</code><i>cookie</i><code>);</code></pre>
<p>The dynamic linker invokes this function after any finalization code for the object has been executed, before the object is unloaded. The <i>cookie</i> argument is the identifier obtained from a previous invocation of <code>la_objopen</code>(). In the current implementation, the value returned by <code>la_objclose</code>() is ignored.</p>
<h3>la_preinit()</h3>
<pre><code>void la_preinit(uintptr_t *</code><i>cookie</i><code>);</code></pre>
<p>The dynamic linker invokes this function after all shared objects have been loaded, before control is passed to the application (i.e., before calling <i>main</i>()). Note that <i>main</i>() may still later dynamically load objects using <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3).</p>
<h3>la_symbind*()</h3>
<pre><code>uintptr_t la_symbind32(Elf32_Sym *</code><i>sym</i><code>, unsigned int </code><i>ndx</i><code>,</code>
<code> uintptr_t *</code><i>refcook</i><code>, uintptr_t *</code><i>defcook</i><code>,</code>
<code> unsigned int *</code><i>flags</i><code>, const char *</code><i>symname</i><code>);</code>
<code>uintptr_t la_symbind64(Elf64_Sym *</code><i>sym</i><code>, unsigned int </code><i>ndx</i><code>,</code>
<code> uintptr_t *</code><i>refcook</i><code>, uintptr_t *</code><i>defcook</i><code>,</code>
<code> unsigned int *</code><i>flags</i><code>, const char *</code><i>symname</i><code>);</code></pre>
<p>The dynamic linker invokes one of these functions when a symbol binding occurs between two shared objects that have been marked for auditing notification by <code>la_objopen</code>(). The <code>la_symbind32</code>() function is employed on 32-bit platforms; the <code>la_symbind64</code>() function is employed on 64-bit platforms. The <i>sym</i> argument is a pointer to a structure that provides information about the symbol being bound. The structure definition is shown in <i>&lt;elf.h&gt;</i>. Among the fields of this structure, <i>st_value</i> indicates the address to which the symbol is bound. The <i>ndx</i> argument gives the index of the symbol in the symbol table of the bound shared object. The <i>refcook</i> argument identifies the shared object that is making the symbol reference; this is the same identifier that is provided to the <code>la_objopen</code>() function that returned <code>LA_FLG_BINDFROM</code>. The <i>defcook</i> argument identifies the shared object that defines the referenced symbol; this is the same identifier that is provided to the <code>la_objopen</code>() function that returned <code>LA_FLG_BINDTO</code>. The <i>symname</i> argument points a string containing the name of the symbol. The <i>flags</i> argument is a bit mask that both provides information about the symbol and can be used to modify further auditing of this PLT (Procedure Linkage Table) entry. The dynamic linker may supply the following bit values in this argument:</p>
<dl>
<dt><code>LA_SYMB_DLSYM</code></p>
<dd>The binding resulted from a call to <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3).</p>
<dt><code>LA_SYMB_ALTVALUE</code></p>
<dd>A previous <code>la_symbind*</code>() call returned an alternate value for this symbol.</dl>
<p> By default, if the auditing library implements <code>la_pltenter</code>() and <code>la_pltexit</code>() functions (see below), then these functions are invoked, after <code>la_symbind</code>(), for PLT entries, each time the symbol is referenced. The following flags can be ORed into <i>*flags</i> to change this default behavior:</p>
<dl>
<dt><code>LA_SYMB_NOPLTENTER</code></p>
<dd>Don&#8217;t call <code>la_pltenter</code>() for this symbol.</p>
<dt><code>LA_SYMB_NOPLTEXIT</code></p>
<dd>Don&#8217;t call <code>la_pltexit</code>() for this symbol.</dl>
<p> The return value of <code>la_symbind32</code>() and <code>la_symbind64</code>() is the address to which control should be passed after the function returns. If the auditing library is simply monitoring symbol bindings, then it should return <i>sym-&gt;st_value</i>. A different value may be returned if the library wishes to direct control to an alternate location.</p>
<h3>la_pltenter()</h3>
<p>The precise name and argument types for this function depend on the hardware platform. (The appropriate definition is supplied by <i>&lt;link.h&gt;</i>.) Here is the definition for x86-32: </p>
<pre><code>Elf32_Addr la_i86_gnu_pltenter(Elf32_Sym *</code><i>sym</i><code>, unsigned int </code><i>ndx</i><code>,</code>
<code> uintptr_t *</code><i>refcook</i><code>, uintptr_t *</code><i>defcook</i><code>,</code>
<code> La_i86_regs *</code><i>regs</i><code>, unsigned int *</code><i>flags</i><code>,</code>
<code> const char *</code><i>symname</i><code>, long *</code><i>framesizep</i><code>);</code></pre>
<p>This function is invoked just before a PLT entry is called, between two shared objects that have been marked for binding notification. The <i>sym</i>, <i>ndx</i>, <i>refcook</i>, <i>defcook</i>, and <i>symname</i> are as for <code>la_symbind*</code>(). The <i>regs</i> argument points to a structure (defined in <i>&lt;link.h&gt;</i>) containing the values of registers to be used for the call to this PLT entry. The <i>flags</i> argument points to a bit mask that conveys information about, and can be used to modify subsequent auditing of, this PLT entry, as for <code>la_symbind*</code>(). The <i>framesizep</i> argument points to a <i>long int</i> buffer that can be used to explicitly set the frame size used for the call to this PLT entry. If different <code>la_pltenter</code>() invocations for this symbol return different values, then the maximum returned value is used. The <code>la_pltexit</code>() function is called only if this buffer is explicitly set to a suitable value. The return value of <code>la_pltenter</code>() is as for <code>la_symbind*</code>().</p>
<h3>la_pltexit()</h3>
<p>The precise name and argument types for this function depend on the hardware platform. (The appropriate definition is supplied by <i>&lt;link.h&gt;</i>.) Here is the definition for x86-32: unsigned int la_i86_gnu_pltexit(Elf32_Sym *sym, unsigned int ndx,<br />
                                uintptr_t *refcook, uintptr_t *defcook,<br />
                                const La_i86_regs *inregs, La_i86_retval *outregs,<br />
                                const char *symname); This function is called when a PLT entry, made between two shared objects that have been marked for binding notification, returns. The function is called just before control returns to the caller of the PLT entry. The <i>sym</i>, <i>ndx</i>, <i>refcook</i>, <i>defcook</i>, and <i>symname</i> are as for <code>la_symbind*</code>(). The <i>inregs</i> argument points to a structure (defined in <i>&lt;link.h&gt;</i>) containing the values of registers used for the call to this PLT entry. The <i>outregs</i> argument points to a structure (defined in <i>&lt;link.h&gt;</i>) containing return values for the call to this PLT entry. These values can be modified by the caller, and the changes will be visible to the caller of the PLT entry. In the current GNU implementation, the return value of <code>la_pltexit</code>() is ignored.</p>
<h2>Conforming To</h2>
<p>This API is nonstandard, but very similar to the Solaris API, described in the Solaris <i>Linker and Libraries Guide</i>, in the chapter <i>Runtime Linker Auditing Interface</i>.</p>
<h2>Notes</h2>
<p>Note the following differences from the Solaris dynamic linker auditing API:</p>
<dl>
<dt>*</p>
<dd>The Solaris <code>la_objfilter</code>() interface is not supported by the GNU implementation.</p>
<dt>*</p>
<dd>The Solaris <code>la_symbind32</code>() and <code>la_pltexit</code>() functions do not provide a <i>symname</i> argument.</p>
<dt>*</p>
<dd>The Solaris <code>la_pltexit</code>() function does not provide <i>inregs</i> and <i>outregs</i> arguments (but does provide a <i>retval</i> argument with the function return value).</dl>
<h2>Bugs</h2>
<p>In glibc versions up to and include 2.9, specifying more than one audit library in <code>LD_AUDIT</code> results in a run-time crash. This is reportedly fixed in glibc 2.10.</p>
<h2>Examples</h2>
<p>#include &lt;link.h&gt;<br />
#include &lt;stdio.h&gt;<br />
unsigned int<br />
la_version(unsigned int version)<br />
{<br />
    printf(&quot;la_version(): version = %u; LAV_CURRENT = %u
&quot;,<br />
           version, LAV_CURRENT);<br />
    return LAV_CURRENT;<br />
}<br />
char *<br />
la_objsearch(const char *name, uintptr_t *cookie, unsigned int flag)<br />
{<br />
    printf(&quot;la_objsearch(): name = %s; cookie = %p&quot;, name, cookie);<br />
    printf(&quot;; flag = %s
&quot;,<br />
           (flag == LA_SER_ORIG) ? &quot;LA_SER_ORIG&quot; : (flag == LA_SER_LIBPATH) ? &quot;LA_SER_LIBPATH&quot;<br />
                                               : (flag == LA_SER_RUNPATH)   ? &quot;LA_SER_RUNPATH&quot;<br />
                                               : (flag == LA_SER_DEFAULT)   ? &quot;LA_SER_DEFAULT&quot;<br />
                                               : (flag == LA_SER_CONFIG)    ? &quot;LA_SER_CONFIG&quot;<br />
                                               : (flag == LA_SER_SECURE)    ? &quot;LA_SER_SECURE&quot;<br />
                                                                            : &quot;???&quot;);<br />
    return name;<br />
}<br />
void la_activity(uintptr_t *cookie, unsigned int flag)<br />
{<br />
    printf(&quot;la_activity(): cookie = %p; flag = %s
&quot;, cookie,<br />
           (flag == LA_ACT_CONSISTENT) ? &quot;LA_ACT_CONSISTENT&quot; : (flag == LA_ACT_ADD)  ? &quot;LA_ACT_ADD&quot;<br />
                                                           : (flag == LA_ACT_DELETE) ? &quot;LA_ACT_DELETE&quot;<br />
                                                                                     : &quot;???&quot;);<br />
}<br />
unsigned int<br />
la_objopen(struct link_map *map, Lmid_t lmid, uintptr_t *cookie)<br />
{<br />
    printf(&quot;la_objopen(): loading \&quot;%s\&quot;; lmid = %s; cookie=%p
&quot;,<br />
           map-&gt;l_name,<br />
           (lmid == LM_ID_BASE) ? &quot;LM_ID_BASE&quot; : (lmid == LM_ID_NEWLM) ? &quot;LM_ID_NEWLM&quot;<br />
                                                                       : &quot;???&quot;,<br />
           cookie);<br />
    return LA_FLG_BINDTO | LA_FLG_BINDFROM;<br />
}<br />
unsigned int<br />
la_objclose(uintptr_t *cookie)<br />
{<br />
    printf(&quot;la_objclose(): %p
&quot;, cookie);<br />
    return 0;<br />
}<br />
void la_preinit(uintptr_t *cookie)<br />
{<br />
    printf(&quot;la_preinit(): %p
&quot;, cookie);<br />
}<br />
uintptr_t<br />
la_symbind32(Elf32_Sym *sym, unsigned int ndx, uintptr_t *refcook,<br />
             uintptr_t *defcook, unsigned int *flags, const char *symname)<br />
{<br />
    printf(&quot;la_symbind32(): symname = %s; sym-&gt;st_value = %p
&quot;,<br />
           symname, sym-&gt;st_value);<br />
    printf(&quot;        ndx = %u; flags = %#x&quot;, ndx, *flags);<br />
    printf(&quot;; refcook = %p; defcook = %p
&quot;, refcook, defcook);<br />
    return sym-&gt;st_value;<br />
}<br />
uintptr_t<br />
la_symbind64(Elf64_Sym *sym, unsigned int ndx, uintptr_t *refcook,<br />
             uintptr_t *defcook, unsigned int *flags, const char *symname)<br />
{<br />
    printf(&quot;la_symbind64(): symname = %s; sym-&gt;st_value = %p
&quot;,<br />
           symname, sym-&gt;st_value);<br />
    printf(&quot;        ndx = %u; flags = %#x&quot;, ndx, *flags);<br />
    printf(&quot;; refcook = %p; defcook = %p
&quot;, refcook, defcook);<br />
    return sym-&gt;st_value;<br />
} Elf32_Addr la_i86_gnu_pltenter(Elf32_Sym *sym, unsigned int ndx,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uintptr_t&nbsp;*refcook, uintptr_t&nbsp;*defcook, La_i86_regs&nbsp;*regs,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;*flags, const char&nbsp;*symname, long&nbsp;*framesizep) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;la_i86_gnu_pltenter():&nbsp;%s&nbsp;(%p)
&quot;, symname, sym-&gt;st_value); </p>
<pre><code>return sym-&gt;st_value;
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
