---
title: "dlinfo(3)"
name: "dlinfo"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlinfo/"
description: "dlinfo – obtain information about a dynamically loaded object"
---

<h2 class="name">NAME</h2>
<p> dlinfo &#8211; obtain information about a dynamically loaded object </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE
#include &lt;dlfcn.h&gt;
#include &lt;link.h&gt;
int dlinfo(void *handle, int request, void *info);
Link with - ldl.
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dlinfo</code>() function obtains information about the dynamically loaded object referred to by <i>handle</i> (typically obtained by an earlier call to <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) or <code><a href="/docs/linux/man/3-dlmopen/">dlmopen</a></code>(3)). The <i>request</i> argument specifies which information is to be returned. The <i>info</i> argument is a pointer to a buffer used to store information returned by the call; the type of this argument depends on <i>request</i>. </p>
<p> The following values are supported for <i>request</i> (with the corresponding type for <i>info</i> shown in parentheses):</p>
<dl>
<dt><code>RTLD_DI_LMID</code> (<i>Lmid_t *</i>)</p>
<dd> Obtain the ID of the link-map list (namespace) in which <i>handle</i> is loaded.</p>
<dt><code>RTLD_DI_LINKMAP</code> (<i>struct link_map **</i>)</p>
<dd> Obtain a pointer to the <i>link_map</i> structure corresponding to <i>handle</i>. The <i>info</i> argument points to a pointer to a <i>link_map</i> structure, defined in <i>&lt;link.h&gt;</i> as:</p>
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
<dt><code>RTLD_DI_ORIGIN</code> (<i>char *</i>)</p>
<dd> Copy the pathname of the origin of the shared object corresponding to <i>handle</i> to the location pointed to by <i>info</i>.</p>
<dt><code>RTLD_DI_SERINFO</code> (<i>Dl_serinfo *</i>)</p>
<dd> Obtain the library search paths for the shared object referred to by <i>handle</i>. The <i>info</i> argument is a pointer to a <i>Dl_serinfo</i> that contains the search paths. Because the number of search paths may vary, the size of the structure pointed to by <i>info</i> can vary. The <code>RTLD_DI_SERINFOSIZE</code> request described below allows applications to size the buffer suitably. The caller must perform the following steps:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Use a <code>RTLD_DI_SERINFOSIZE</code> request to populate a <i>Dl_serinfo</i> structure with the size (<i>dls_size</i>) of the structure needed for the subsequent <code>RTLD_DI_SERINFO</code> request.</p>
<dt>2.</p>
<dd> Allocate a <i>Dl_serinfo</i> buffer of the correct size (<i>dls_size</i>).</p>
<dt>3.</p>
<dd> Use a further <code>RTLD_DI_SERINFOSIZE</code> request to populate the <i>dls_size</i> and <i>dls_cnt</i> fields of the buffer allocated in the previous step.</p>
<dt>4.</p>
<dd> Use a <code>RTLD_DI_SERINFO</code> to obtain the library search paths.</dl>
</dl>
<dt>
<dd> The <i>Dl_serinfo</i> structure is defined as follows:</p>
<dt>
<dd> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t dls_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size in bytes of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the whole buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int dls_cnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in&nbsp;&#8216;dls_serpath&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Dl_serpath dls_serpath[1];&nbsp;/*&nbsp;Actually longer,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;dls_cnt&#8217;&nbsp;elements&nbsp;*/ } Dl_serinfo;</p>
<dt>
<dd> Each of the <i>dls_serpath</i> elements in the above structure is a structure of the following form:</p>
<dt>
<dd> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*dls_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Name of library search<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;path directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int dls_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Indicates where this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;directory came from&nbsp;*/ } Dl_serpath;</p>
<dt>
<dd> The <i>dls_flags</i> field is currently unused, and always contains zero.</p>
<dt><code>RTLD_DI_SERINFOSIZE</code> (<i>Dl_serinfo *</i>)</p>
<dd> Populate the <i>dls_size</i> and <i>dls_cnt</i> fields of the <i>Dl_serinfo</i> structure pointed to by <i>info</i> with values suitable for allocating a buffer for use in a subsequent <code>RTLD_DI_SERINFO</code> request.</p>
<dt><code>RTLD_DI_TLS_MODID</code> (<i>size_t *</i>, since glibc 2.4)</p>
<dd> Obtain the module ID of this shared object&#8217;s TLS (thread-local storage) segment, as used in TLS relocations. If this object does not define a TLS segment, zero is placed in <i>*info</i>.</p>
<dt><code>RTLD_DI_TLS_DATA</code> (<i>void **</i>, since glibc 2.4)</p>
<dd> Obtain a pointer to the calling thread&#8217;s TLS block corresponding to this shared object&#8217;s TLS segment. If this object does not define a PT_TLS segment, or if the calling thread has not allocated a block for it, NULL is placed in <i>*info</i>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>dlinfo</code>() returns 0. On failure, it returns -1; the cause of the error can be diagnosed using <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> <code>dlinfo</code>() first appeared in glibc 2.3.3.</p>
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
<td> <code>dlinfo</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a nonstandard GNU extension.</p>
<h2>NOTES</h2>
<p> This function derives from the Solaris function of the same name and also appears on some other systems. The sets of requests supported by the various implementations overlaps only partially.</p>
<h2>EXAMPLES</h2>
<p> The program below opens a shared objects using <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) and then uses the <code>RTLD_DI_SERINFOSIZE</code> and <code>RTLD_DI_SERINFO</code> requests to obtain the library search path list for the library. Here is an example of what we might see when running the program: </p>
<p> $ <code>./a.out /lib64/libm.so.6</code> dls_serpath[0].dls_name = /lib64 dls_serpath[1].dls_name = /usr/lib64</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;dlfcn.h&gt; #include &lt;link.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*handle;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Dl_serinfo serinfo;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Dl_serinfo&nbsp;*sip; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;libpath&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain a handle for shared object specified on command line&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle&nbsp;=&nbsp;dlopen(argv[1], RTLD_NOW);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(handle&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;dlopen()&nbsp;failed:&nbsp;%s
&quot;, dlerror());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Discover the size of the buffer that we must pass to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;RTLD_DI_SERINFO&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(dlinfo(handle, RTLD_DI_SERINFOSIZE,&nbsp;&amp;serinfo)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;RTLD_DI_SERINFOSIZE failed:&nbsp;%s
&quot;, dlerror());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate the buffer for use with RTLD_DI_SERINFO&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sip&nbsp;=&nbsp;malloc(serinfo.dls_size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sip&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize the&nbsp;&#8216;dls_size&#8217;&nbsp;and&nbsp;&#8216;dls_cnt&#8217;&nbsp;fields in the newly<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocated buffer&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(dlinfo(handle, RTLD_DI_SERINFOSIZE, sip)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;RTLD_DI_SERINFOSIZE failed:&nbsp;%s
&quot;, dlerror());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Fetch and print library search list&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(dlinfo(handle, RTLD_DI_SERINFO, sip)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;RTLD_DI_SERINFO failed:&nbsp;%s
&quot;, dlerror());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;serinfo.dls_cnt;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;dls_serpath[%d].dls_name&nbsp;=&nbsp;%s
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j, sip-&gt;dls_serpath[j].dls_name); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3), <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
