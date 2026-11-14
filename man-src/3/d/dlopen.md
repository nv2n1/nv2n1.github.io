---
title: "dlopen(3)"
name: "dlopen"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlopen/"
description: "dlclose, dlopen, dlmopen – open and close a shared object"
---

<h2 class="name">NAME</h2>
<p> dlclose, dlopen, dlmopen &#8211; open and close a shared object </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;dlfcn.h&gt;</code> </p>
<p> <code>void *dlopen(const char *</code><i>filename</i><code>, int </code><i>flags</i><code>);</code> </p>
<p> <code>int dlclose(void *</code><i>handle</i><code>);</code> </p>
<p> <code>#define _GNU_SOURCE</code><br />
 <code>#include &lt;dlfcn.h&gt;</code> </p>
<p> <code>void *dlmopen(Lmid_t </code><i>lmid</i><code>, const char *</code><i>filename</i><code>, int </code><i>flags</i><code>);</code> </p>
<p> Link with <i>-ldl</i>.</p>
<h2>DESCRIPTION</h2>
<h3>dlopen()</h3>
<p> The function <code>dlopen</code>() loads the dynamic shared object (shared library) file named by the null-terminated string <i>filename</i> and returns an opaque &quot;handle&quot; for the loaded object. This handle is employed with other functions in the dlopen API, such as <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3), <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3), and <code>dlclose</code>(). </p>
<p> If <i>filename</i> is NULL, then the returned handle is for the main program. If <i>filename</i> contains a slash (&quot;/&quot;), then it is interpreted as a (relative or absolute) pathname. Otherwise, the dynamic linker searches for the object as follows (see <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) for further details):</p>
<dl>
<dt>o</p>
<dd> (ELF only) If the calling object (i.e., the shared library or executable from which <code>dlopen</code>() is called) contains a DT_RPATH tag, and does not contain a DT_RUNPATH tag, then the directories listed in the DT_RPATH tag are searched.</p>
<dt>o</p>
<dd> If, at the time that the program was started, the environment variable <code>LD_LIBRARY_PATH</code> was defined to contain a colon-separated list of directories, then these are searched. (As a security measure, this variable is ignored for set-user-ID and set-group-ID programs.)</p>
<dt>o</p>
<dd> (ELF only) If the calling object contains a DT_RUNPATH tag, then the directories listed in that tag are searched.</p>
<dt>o</p>
<dd> The cache file <i>/etc/ld.so.cache</i> (maintained by <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8)) is checked to see whether it contains an entry for <i>filename</i>.</p>
<dt>o</p>
<dd> The directories <i>/lib</i> and <i>/usr/lib</i> are searched (in that order).</dl>
<p> If the object specified by <i>filename</i> has dependencies on other shared objects, then these are also automatically loaded by the dynamic linker using the same rules. (This process may occur recursively, if those objects in turn have dependencies, and so on.) </p>
<p> One of the following two values must be included in <i>flags</i>:</p>
<dl>
<dt><code>RTLD_LAZY</code></p>
<dd> Perform lazy binding. Resolve symbols only as the code that references them is executed. If the symbol is never referenced, then it is never resolved. (Lazy binding is performed only for function references; references to variables are always immediately bound when the shared object is loaded.) Since glibc 2.1.1, this flag is overridden by the effect of the <code>LD_BIND_NOW</code> environment variable.</p>
<dt><code>RTLD_NOW</code></p>
<dd> If this value is specified, or the environment variable <code>LD_BIND_NOW</code> is set to a nonempty string, all undefined symbols in the shared object are resolved before <code>dlopen</code>() returns. If this cannot be done, an error is returned.</dl>
<p> Zero or more of the following values may also be ORed in <i>flags</i>:</p>
<dl>
<dt><code>RTLD_GLOBAL</code></p>
<dd> The symbols defined by this shared object will be made available for symbol resolution of subsequently loaded shared objects.</p>
<dt><code>RTLD_LOCAL</code></p>
<dd> This is the converse of <code>RTLD_GLOBAL</code>, and the default if neither flag is specified. Symbols defined in this shared object are not made available to resolve references in subsequently loaded shared objects.</p>
<dt><code>RTLD_NODELETE</code> (since glibc 2.2)</p>
<dd> Do not unload the shared object during <code>dlclose</code>(). Consequently, the object&#8217;s static and global variables are not reinitialized if the object is reloaded with <code>dlopen</code>() at a later time.</p>
<dt><code>RTLD_NOLOAD</code> (since glibc 2.2)</p>
<dd> Don&#8217;t load the shared object. This can be used to test if the object is already resident (<code>dlopen</code>() returns NULL if it is not, or the object&#8217;s handle if it is resident). This flag can also be used to promote the flags on a shared object that is already loaded. For example, a shared object that was previously loaded with <code>RTLD_LOCAL</code> can be reopened with <code>RTLD_NOLOAD | RTLD_GLOBAL</code>.</p>
<dt><code>RTLD_DEEPBIND</code> (since glibc 2.3.4)</p>
<dd> Place the lookup scope of the symbols in this shared object ahead of the global scope. This means that a self-contained object will use its own symbols in preference to global symbols with the same name contained in objects that have already been loaded.</dl>
<p> If <i>filename</i> is NULL, then the returned handle is for the main program. When given to <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3), this handle causes a search for a symbol in the main program, followed by all shared objects loaded at program startup, and then all shared objects loaded by <code>dlopen</code>() with the flag <code>RTLD_GLOBAL</code>. </p>
<p> Symbol references in the shared object are resolved using (in order): symbols in the link map of objects loaded for the main program and its dependencies; symbols in shared objects (and their dependencies) that were previously opened with <code>dlopen</code>() using the <code>RTLD_GLOBAL</code> flag; and definitions in the shared object itself (and any dependencies that were loaded for that object). </p>
<p> Any global symbols in the executable that were placed into its dynamic symbol table by <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) can also be used to resolve references in a dynamically loaded shared object. Symbols may be placed in the dynamic symbol table either because the executable was linked with the flag &quot;-rdynamic&quot; (or, synonymously, &quot;&#8211;export-dynamic&quot;), which causes all of the executable&#8217;s global symbols to be placed in the dynamic symbol table, or because <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) noted a dependency on a symbol in another object during static linking. </p>
<p> If the same shared object is opened again with <code>dlopen</code>(), the same object handle is returned. The dynamic linker maintains reference counts for object handles, so a dynamically loaded shared object is not deallocated until <code>dlclose</code>() has been called on it as many times as <code>dlopen</code>() has succeeded on it. Constructors (see below) are called only when the object is actually loaded into memory (i.e., when the reference count increases to 1). </p>
<p> A subsequent <code>dlopen</code>() call that loads the same shared object with <code>RTLD_NOW</code> may force symbol resolution for a shared object earlier loaded with <code>RTLD_LAZY</code>. Similarly, an object that was previously opened with <code>RTLD_LOCAL</code> can be promoted to <code>RTLD_GLOBAL</code> in a subsequent <code>dlopen</code>(). </p>
<p> If <code>dlopen</code>() fails for any reason, it returns NULL.</p>
<h3>dlmopen()</h3>
<p> This function performs the same task as <code>dlopen</code>()&#8212;the <i>filename</i> and <i>flags</i> arguments, as well as the return value, are the same, except for the differences noted below. </p>
<p> The <code>dlmopen</code>() function differs from <code>dlopen</code>() primarily in that it accepts an additional argument, <i>lmid</i>, that specifies the link-map list (also referred to as a <i>namespace</i>) in which the shared object should be loaded. (By comparison, <code>dlopen</code>() adds the dynamically loaded shared object to the same namespace as the shared object from which the <code>dlopen</code>() call is made.) The <i>Lmid_t</i> type is an opaque handle that refers to a namespace. </p>
<p> The <i>lmid</i> argument is either the ID of an existing namespace (which can be obtained using the <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3) <code>RTLD_DI_LMID</code> request) or one of the following special values:</p>
<dl>
<dt><code>LM_ID_BASE</code></p>
<dd> Load the shared object in the initial namespace (i.e., the application&#8217;s namespace).</p>
<dt><code>LM_ID_NEWLM</code></p>
<dd> Create a new namespace and load the shared object in that namespace. The object must have been correctly linked to reference all of the other shared objects that it requires, since the new namespace is initially empty.</dl>
<p> If <i>filename</i> is NULL, then the only permitted value for <i>lmid</i> is <code>LM_ID_BASE</code>.</p>
<h3>dlclose()</h3>
<p> The function <code>dlclose</code>() decrements the reference count on the dynamically loaded shared object referred to by <i>handle</i>. </p>
<p> If the object&#8217;s reference count drops to zero and no symbols in this object are required by other objects, then the object is unloaded after first calling any destructors defined for the object. (Symbols in this object might be required in another object because this object was opened with the <code>RTLD_GLOBAL</code> flag and one of its symbols satisfied a relocation in another object.) </p>
<p> All shared objects that were automatically loaded when <code>dlopen</code>() was invoked on the object referred to by <i>handle</i> are recursively closed in the same manner. </p>
<p> A successful return from <code>dlclose</code>() does not guarantee that the symbols associated with <i>handle</i> are removed from the caller&#8217;s address space. In addition to references resulting from explicit <code>dlopen</code>() calls, a shared object may have been implicitly loaded (and reference counted) because of dependencies in other shared objects. Only when all references have been released can the shared object be removed from the address space.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dlopen</code>() and <code>dlmopen</code>() return a non-NULL handle for the loaded object. On error (file could not be found, was not readable, had the wrong format, or caused errors during loading), these functions return NULL. </p>
<p> On success, <code>dlclose</code>() returns 0; on error, it returns a nonzero value. </p>
<p> Errors from these functions can be diagnosed using <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3).</p>
<h2>VERSIONS</h2>
<p> <code>dlopen</code>() and <code>dlclose</code>() are present in glibc 2.0 and later. <code>dlmopen</code>() first appeared in glibc 2.3.4.</p>
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
<td> <code>dlopen</code>(), <code>dlmopen</code>(), <code>dlclose</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001 describes <code>dlclose</code>() and <code>dlopen</code>(). The <code>dlmopen</code>() function is a GNU extension. </p>
<p> The <code>RTLD_NOLOAD</code>, <code>RTLD_NODELETE</code>, and <code>RTLD_DEEPBIND</code> flags are GNU extensions; the first two of these flags are also present on Solaris.</p>
<h2>NOTES</h2>
<h3>dlmopen() and namespaces</h3>
<p> A link-map list defines an isolated namespace for the resolution of symbols by the dynamic linker. Within a namespace, dependent shared objects are implicitly loaded according to the usual rules, and symbol references are likewise resolved according to the usual rules, but such resolution is confined to the definitions provided by the objects that have been (explicitly and implicitly) loaded into the namespace. </p>
<p> The <code>dlmopen</code>() function permits object-load isolation&#8212;the ability to load a shared object in a new namespace without exposing the rest of the application to the symbols made available by the new object. Note that the use of the <code>RTLD_LOCAL</code> flag is not sufficient for this purpose, since it prevents a shared object&#8217;s symbols from being available to <i>any</i> other shared object. In some cases, we may want to make the symbols provided by a dynamically loaded shared object available to (a subset of) other shared objects without exposing those symbols to the entire application. This can be achieved by using a separate namespace and the <code>RTLD_GLOBAL</code> flag. </p>
<p> The <code>dlmopen</code>() function also can be used to provide better isolation than the <code>RTLD_LOCAL</code> flag. In particular, shared objects loaded with <code>RTLD_LOCAL</code> may be promoted to <code>RTLD_GLOBAL</code> if they are dependencies of another shared object loaded with <code>RTLD_GLOBAL</code>. Thus, <code>RTLD_LOCAL</code> is insufficient to isolate a loaded shared object except in the (uncommon) case where one has explicit control over all shared object dependencies. </p>
<p> Possible uses of <code>dlmopen</code>() are plugins where the author of the plugin-loading framework can&#8217;t trust the plugin authors and does not wish any undefined symbols from the plugin framework to be resolved to plugin symbols. Another use is to load the same object more than once. Without the use of <code>dlmopen</code>(), this would require the creation of distinct copies of the shared object file. Using <code>dlmopen</code>(), this can be achieved by loading the same shared object file into different namespaces. </p>
<p> The glibc implementation supports a maximum of 16 namespaces.</p>
<h3>Initialization and finalization functions</h3>
<p> Shared objects may export functions using the <code>__attribute__((constructor))</code> and <code>__attribute__((destructor))</code> function attributes. Constructor functions are executed before <code>dlopen</code>() returns, and destructor functions are executed before <code>dlclose</code>() returns. A shared object may export multiple constructors and destructors, and priorities can be associated with each function to determine the order in which they are executed. See the <code>gcc</code> info pages (under &quot;Function attributes&quot;) for further information. </p>
<p> An older method of (partially) achieving the same result is via the use of two special symbols recognized by the linker: <code>_init</code> and <code>_fini</code>. If a dynamically loaded shared object exports a routine named <code>_init</code>(), then that code is executed after loading a shared object, before <code>dlopen</code>() returns. If the shared object exports a routine named <code>_fini</code>(), then that routine is called just before the object is unloaded. In this case, one must avoid linking against the system startup files, which contain default versions of these files; this can be done by using the <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) <i>-nostartfiles</i> command-line option. </p>
<p> Use of <code>_init</code> and <code>_fini</code> is now deprecated in favor of the aforementioned constructors and destructors, which among other advantages, permit multiple initialization and finalization functions to be defined. </p>
<p> Since glibc 2.2.3, <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) can be used to register an exit handler that is automatically called when a shared object is unloaded.</p>
<h3>History</h3>
<p> These functions are part of the dlopen API, derived from SunOS.</p>
<h2>BUGS</h2>
<p> As at glibc 2.24, specifying the <code>RTLD_GLOBAL</code> flag when calling <code>dlmopen</code>() generates an error. Furthermore, specifying <code>RTLD_GLOBAL</code> when calling <code>dlopen</code>() results in a program crash (<code>SIGSEGV</code>) if the call is made from any object loaded in a namespace other than the initial namespace.</p>
<h2>EXAMPLES</h2>
<p> The program below loads the (glibc) math library, looks up the address of the <code><a href="/docs/linux/man/3-cos/">cos</a></code>(3) function, and prints the cosine of 2.0. The following is an example of building and running the program: </p>
<p> $ <code>cc dlopen_demo.c -ldl</code> $ <code>./a.out</code> -0.416147</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;dlfcn.h&gt; #include &lt;gnu/lib-names.h&gt; /* Defines LIBM_SO (which will be a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;string such as&nbsp;&quot;libm.so.6&quot;)&nbsp;*/ int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*handle;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double&nbsp;(*cosine)(double);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*error; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle&nbsp;=&nbsp;dlopen(LIBM_SO, RTLD_LAZY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!handle)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s
&quot;, dlerror());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dlerror();&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Clear any existing error&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cosine&nbsp;=&nbsp;(double&nbsp;(*)(double))&nbsp;dlsym(handle,&nbsp;&quot;cos&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;According to the ISO C standard, casting between function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointers and&nbsp;&#8216;void&nbsp;*&#8217;, as done above, produces undefined results.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1-2001 and POSIX.1-2008 accepted this state of affairs and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proposed the following workaround: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*(void&nbsp;**)&nbsp;(&amp;cosine)&nbsp;=&nbsp;dlsym(handle,&nbsp;&quot;cos&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This&nbsp;(clumsy)&nbsp;cast conforms with the ISO C standard and will<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;avoid any compiler warnings. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The 2013 Technical Corrigendum 1 to POSIX.1-2008 improved matters<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;by requiring that conforming implementations support casting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;void&nbsp;*&#8217;&nbsp;to a function pointer.&nbsp;<wbr>&nbsp;Nevertheless, some compilers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(e.g., gcc with the&nbsp;&#8216;-pedantic&#8217;&nbsp;option)&nbsp;may complain about the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cast used in this program.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;error&nbsp;=&nbsp;dlerror();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(error&nbsp;!=&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s
&quot;, error);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%f
&quot;,&nbsp;(*cosine)(2.0));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dlclose(handle);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/1-pldd/">pldd</a></code>(1), <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3), <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlerror/">dlerror</a></code>(3), <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3), <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3), <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a></code>(7), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8) </p>
<p> gcc info pages, ld info pages</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
