---
title: "dlvsym(3)"
name: "dlvsym"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlvsym/"
description: "dlsym, dlvsym – obtain address of a symbol in a shared object or executable"
---

<h2 class="name">NAME</h2>
<p> dlsym, dlvsym &#8211; obtain address of a symbol in a shared object or executable </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;dlfcn.h&gt;</code> </p>
<p> <code>void *dlsym(void *</code><i>handle</i><code>, const char *</code><i>symbol</i><code>);</code> </p>
<p> <code>#define _GNU_SOURCE</code><br />
 <code>#include &lt;dlfcn.h&gt;</code> </p>
<p> <code>void *dlvsym(void *</code><i>handle</i><code>, char *</code><i>symbol</i><code>, char *</code><i>version</i><code>);</code> </p>
<p> Link with <i>-ldl</i>.</p>
<h2>DESCRIPTION</h2>
<p> The function <code>dlsym</code>() takes a &quot;handle&quot; of a dynamic loaded shared object returned by <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) along with a null-terminated symbol name, and returns the address where that symbol is loaded into memory. If the symbol is not found, in the specified object or any of the shared objects that were automatically loaded by <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) when that object was loaded, <code>dlsym</code>() returns NULL. (The search performed by <code>dlsym</code>() is breadth first through the dependency tree of these shared objects.) </p>
<p> In unusual cases (see NOTES) the value of the symbol could actually be NULL. Therefore, a NULL return from <code>dlsym</code>() need not indicate an error. The correct way to distinguish an error from a symbol whose value is NULL is to call <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3) to clear any old error conditions, then call <code>dlsym</code>(), and then call <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3) again, saving its return value into a variable, and check whether this saved value is not NULL. </p>
<p> There are two special pseudo-handles that may be specified in <i>handle</i>:</p>
<dl>
<dt><code>RTLD_DEFAULT</code></p>
<dd> Find the first occurrence of the desired symbol using the default shared object search order. The search will include global symbols in the executable and its dependencies, as well as symbols in shared objects that were dynamically loaded with the <code>RTLD_GLOBAL</code> flag.</p>
<dt><code>RTLD_NEXT</code></p>
<dd> Find the next occurrence of the desired symbol in the search order after the current object. This allows one to provide a wrapper around a function in another shared object, so that, for example, the definition of a function in a preloaded shared object (see <code>LD_PRELOAD</code> in <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)) can find and invoke the &quot;real&quot; function provided in another shared object (or for that matter, the &quot;next&quot; definition of the function in cases where there are multiple layers of preloading).</dl>
<p> The <code>_GNU_SOURCE</code> feature test macro must be defined in order to obtain the definitions of <code>RTLD_DEFAULT</code> and <code>RTLD_NEXT</code> from <i>&lt;dlfcn.h&gt;</i>. </p>
<p> The function <code>dlvsym</code>() does the same as <code>dlsym</code>() but takes a version string as an additional argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the address associated with <i>symbol</i>. On failure, they return NULL; the cause of the error can be diagnosed using <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> <code>dlsym</code>() is present in glibc 2.0 and later. <code>dlvsym</code>() first appeared in glibc 2.1.</p>
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
<td> <code>dlsym</code>(), <code>dlvsym</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001 describes <code>dlsym</code>(). The <code>dlvsym</code>() function is a GNU extension.</p>
<h2>NOTES</h2>
<p> There are several scenarios when the address of a global symbol is NULL. For example, a symbol can be placed at zero address by the linker, via a linker script or with <i>&#8211;defsym</i> command-line option. Undefined weak symbols also have NULL value. Finally, the symbol value may be the result of a GNU indirect function (IFUNC) resolver function that returns NULL as the resolved value. In the latter case, <code>dlsym</code>() also returns NULL without error. However, in the former two cases, the behavior of GNU dynamic linker is inconsistent: relocation processing succeeds and the symbol can be observed to have NULL value, but <code>dlsym</code>() fails and <code>dlerror</code>() indicates a lookup error.</p>
<h3>History</h3>
<p> The <code>dlsym</code>() function is part of the dlopen API, derived from SunOS. That system does not have <code>dlvsym</code>().</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3), <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3), <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
