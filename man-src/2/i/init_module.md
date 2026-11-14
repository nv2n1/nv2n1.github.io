---
title: "init_module(2)"
name: "init_module"
section: "2"
letter: "i"
url: "/docs/linux/man/2-init_module/"
description: "init_module, finit_module – load a kernel module"
---

<h2 class="name">NAME</h2>
<p> init_module, finit_module &#8211; load a kernel module </p>
<h2>SYNOPSIS</h2>
<pre><code>
int init_module(void *module_image, unsigned long len,
                const char *param_values);
int finit_module(int fd, const char *param_values,
                 int flags);
</code></pre>
<p> <i>Note</i>: glibc provides no header file declaration of <code>init_module</code>() and no wrapper function for <code>finit_module</code>(); see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>init_module</code>() loads an ELF image into kernel space, performs any necessary symbol relocations, initializes module parameters to values provided by the caller, and then runs the module&#8217;s <i>init</i> function. This system call requires privilege. </p>
<p> The <i>module_image</i> argument points to a buffer containing the binary image to be loaded; <i>len</i> specifies the size of that buffer. The module image should be a valid ELF image, built for the running kernel. </p>
<p> The <i>param_values</i> argument is a string containing space-delimited specifications of the values for module parameters (defined inside the module using <code>module_param</code>() and <code>module_param_array</code>()). The kernel parses this string and initializes the specified parameters. Each of the parameter specifications has the form: </p>
<p> <i>name</i>[<code>=</code><i>value</i>[<code>,</code><i>value</i>&#8230;]] </p>
<p> The parameter <i>name</i> is one of those defined within the module using <i>module_param</i>() (see the Linux kernel source file <i>include/linux/moduleparam.h</i>). The parameter <i>value</i> is optional in the case of <i>bool</i> and <i>invbool</i> parameters. Values for array parameters are specified as a comma-separated list.</p>
<h3>finit_module()</h3>
<p> The <code>finit_module</code>() system call is like <code>init_module</code>(), but reads the module to be loaded from the file descriptor <i>fd</i>. It is useful when the authenticity of a kernel module can be determined from its location in the filesystem; in cases where that is possible, the overhead of using cryptographically signed modules to determine the authenticity of a module can be avoided. The <i>param_values</i> argument is as for <code>init_module</code>(). </p>
<p> The <i>flags</i> argument modifies the operation of <code>finit_module</code>(). It is a bit mask value created by ORing together zero or more of the following flags:</p>
<dl>
<dt><code>MODULE_INIT_IGNORE_MODVERSIONS</code></p>
<dd> Ignore symbol version hashes.</p>
<dt><code>MODULE_INIT_IGNORE_VERMAGIC</code></p>
<dd> Ignore kernel version magic.</dl>
<p> There are some safety checks built into a module to ensure that it matches the kernel against which it is loaded. These checks are recorded when the module is built and verified when the module is loaded. First, the module records a &quot;vermagic&quot; string containing the kernel version number and prominent features (such as the CPU type). Second, if the module was built with the <code>CONFIG_MODVERSIONS</code> configuration option enabled, a version hash is recorded for each symbol the module uses. This hash is based on the types of the arguments and return value for the function named by the symbol. In this case, the kernel version number within the &quot;vermagic&quot; string is ignored, as the symbol version hashes are assumed to be sufficiently reliable. </p>
<p> Using the <code>MODULE_INIT_IGNORE_VERMAGIC</code> flag indicates that the &quot;vermagic&quot; string is to be ignored, and the <code>MODULE_INIT_IGNORE_MODVERSIONS</code> flag indicates that the symbol version hashes are to be ignored. If the kernel is built to permit forced loading (i.e., configured with <code>CONFIG_MODULE_FORCE_LOAD</code>), then loading continues, otherwise it fails with the error <code>ENOEXEC</code> as expected for malformed modules.</p>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return 0. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADMSG</code> (since Linux 3.7)</p>
<dd> Module signature is misformatted.</p>
<dt><code>EBUSY</code></p>
<dd> Timeout while trying to resolve a symbol reference by this module.</p>
<dt><code>EFAULT</code></p>
<dd> An address argument referred to a location that is outside the process&#8217;s accessible address space.</p>
<dt><code>ENOKEY</code> (since Linux 3.7)</p>
<dd> Module signature is invalid or the kernel does not have a key for this module. This error is returned only if the kernel was configured with <code>CONFIG_MODULE_SIG_FORCE</code>; if the kernel was not configured with this option, then an invalid or unsigned module simply taints the kernel.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>EPERM</code></p>
<dd> The caller was not privileged (did not have the <code>CAP_SYS_MODULE</code> capability), or module loading is disabled (see <i>/proc/sys/kernel/modules_disabled</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</dl>
<p> The following errors may additionally occur for <code>init_module</code>():</p>
<dl>
<dt><code>EEXIST</code></p>
<dd> A module with this name is already loaded.</p>
<dt><code>EINVAL</code></p>
<dd> <i>param_values</i> is invalid, or some part of the ELF image in <i>module_image</i> contains inconsistencies.</p>
<dt><code>ENOEXEC</code></p>
<dd> The binary image supplied in <i>module_image</i> is not an ELF image, or is an ELF image that is invalid or for a different architecture.</dl>
<p> The following errors may additionally occur for <code>finit_module</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> The file referred to by <i>fd</i> is not opened for reading.</p>
<dt><code>EFBIG</code></p>
<dd> The file referred to by <i>fd</i> is too large.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is invalid.</p>
<dt><code>ENOEXEC</code></p>
<dd> <i>fd</i> does not refer to an open file.</dl>
<p> In addition to the above errors, if the module&#8217;s <i>init</i> function is executed and returns an error, then <code>init_module</code>() or <code>finit_module</code>() fails and <i>errno</i> is set to the value returned by the <i>init</i> function.</p>
<h2>VERSIONS</h2>
<p> <code>finit_module</code>() is available since Linux 3.8.</p>
<h2>CONFORMING TO</h2>
<p> <code>init_module</code>() and <code>finit_module</code>() are Linux-specific.</p>
<h2>NOTES</h2>
<p> The <code>init_module</code>() system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc versions before 2.23 did export an ABI for this system call. Therefore, in order to employ this system call, it is (before glibc 2.23) sufficient to manually declare the interface in your code; alternatively, you can invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Glibc does not provide a wrapper for <code>finit_module</code>(); call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Information about currently loaded modules can be found in <i>/proc/modules</i> and in the file trees under the per-module subdirectories under <i>/sys/module</i>. </p>
<p> See the Linux kernel source file <i>include/linux/module.h</i> for some useful background information.</p>
<h3>Linux 2.4 and earlier</h3>
<p> In Linux 2.4 and earlier, the <code>init_module</code>() system call was rather different: </p>
<p> <code> #include &lt;linux/module.h&gt;</code> </p>
<p> <code> int init_module(const char *</code><i>name</i><code>, struct module *</code><i>image</i><code>);</code> </p>
<p> (User-space applications can detect which version of <code>init_module</code>() is available by calling <code>query_module</code>(); the latter call fails with the error <code>ENOSYS</code> on Linux 2.6 and later.) </p>
<p> The older version of the system call loads the relocated module image pointed to by <i>image</i> into kernel space and runs the module&#8217;s <i>init</i> function. The caller is responsible for providing the relocated image (since Linux 2.6, the <code>init_module</code>() system call does the relocation). </p>
<p> The module image begins with a module structure and is followed by code and data as appropriate. Since Linux 2.2, the module structure is defined as follows: </p>
<p> struct module {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_of_struct;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct module&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*next;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usecount;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsyms;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndeps;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct module_symbol&nbsp;*syms;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct module_ref&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*deps;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct module_ref&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*refs;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*init)(void);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*cleanup)(void);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct exception_table_entry&nbsp;*ex_table_start;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct exception_table_entry&nbsp;*ex_table_end; #ifdef __alpha__<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long gp; #endif }; </p>
<p> All of the pointer fields, with the exception of <i>next</i> and <i>refs</i>, are expected to point within the module body and be initialized as appropriate for kernel space, that is, relocated with the rest of the module.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2), <code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
