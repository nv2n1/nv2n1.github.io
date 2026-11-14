---
title: "ld-linux-so(8)"
name: "ld-linux-so"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ld-linux-so/"
description: "ld.so, ld-linux.so – dynamic linker/loader"
---

<p>ld.so, ld-linux.so &#8211; dynamic linker/loader</p>
<h2>Synopsis</h2>
<p>The dynamic linker can be run either indirectly by running some dynamically linked program or shared object (in which case no command-line options to the dynamic linker can be passed and, in the ELF case, the dynamic linker which is stored in the <code>.interp</code> section of the program is executed) or directly by running: </p>
<p> <i>/lib/ld-linux.so.*</i> [OPTIONS] [PROGRAM [ARGUMENTS]]</p>
<h2>Description</h2>
<p>The programs <code>ld.so</code> and <code>ld-linux.so*</code> find and load the shared objects (shared libraries) needed by a program, prepare the program to run, and then run it. </p>
<p> Linux binaries require dynamic linking (linking at run time) unless the <code>-static</code> option was given to <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) during compilation. </p>
<p> The program <code>ld.so</code> handles a.out binaries, a binary format used long ago. The program <code>ld-linux.so*</code> (<i>/lib/ld-linux.so.1</i> for libc5, <i>/lib/ld-linux.so.2</i> for glibc2) handles binaries that are in the more modern ELF format. Both programs have the same behavior, and use the same support files and programs (<code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8), and <i>/etc/ld.so.conf</i>). </p>
<p> When resolving shared object dependencies, the dynamic linker first inspects each dependency string to see if it contains a slash (this can occur if a shared object pathname containing slashes was specified at link time). If a slash is found, then the dependency string is interpreted as a (relative or absolute) pathname, and the shared object is loaded using that pathname. </p>
<p> If a shared object dependency does not contain a slash, then it is searched for in the following order:</p>
<dl>
<dt>o</p>
<dd>Using the directories specified in the DT_RPATH dynamic section attribute of the binary if present and DT_RUNPATH attribute does not exist. Use of DT_RPATH is deprecated.</p>
<dt>o</p>
<dd>Using the environment variable <code>LD_LIBRARY_PATH</code>, unless the executable is being run in secure-execution mode (see below), in which case this variable is ignored.</p>
<dt>o</p>
<dd>Using the directories specified in the DT_RUNPATH dynamic section attribute of the binary if present. Such directories are searched only to find those objects required by DT_NEEDED (direct dependencies) entries and do not apply to those objects&#8217; children, which must themselves have their own DT_RUNPATH entries. This is unlike DT_RPATH, which is applied to searches for all children in the dependency tree.</p>
<dt>o</p>
<dd>From the cache file <i>/etc/ld.so.cache</i>, which contains a compiled list of candidate shared objects previously found in the augmented library path. If, however, the binary was linked with the <code>-z nodeflib</code> linker option, shared objects in the default paths are skipped. Shared objects installed in hardware capability directories (see below) are preferred to other shared objects.</p>
<dt>o</p>
<dd>In the default path <i>/lib</i>, and then <i>/usr/lib</i>. (On some 64-bit architectures, the default paths for 64-bit shared objects are <i>/lib64</i>, and then <i>/usr/lib64</i>.) If the binary was linked with the <code>-z nodeflib</code> linker option, this step is skipped.</dl>
<h3>Dynamic string tokens</h3>
<p>In several places, the dynamic linker expands dynamic string tokens:</p>
<dl>
<dt>o</p>
<dd>In the environment variables <code>LD_LIBRARY_PATH</code>, <code>LD_PRELOAD</code>, and <code>LD_AUDIT</code>,</p>
<dt>o</p>
<dd>inside the values of the dynamic section tags <code>DT_NEEDED</code>, <code>DT_RPATH</code>, <code>DT_RUNPATH</code>, <code>DT_AUDIT</code>, and <code>DT_DEPAUDIT</code> of ELF binaries,</p>
<dt>o</p>
<dd>in the arguments to the <code>ld.so</code> command line options <code>&#8211;audit</code>, <code>&#8211;library-path</code>, and <code>&#8211;preload</code> (see below), and</p>
<dt>o</p>
<dd>in the filename arguments to the <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) and <code><a href="/docs/linux/man/3-dlmopen/">dlmopen</a></code>(3) functions.</dl>
<p> The substituted tokens are as follows:</p>
<dl>
<dt><i>$ORIGIN</i> (or equivalently <i>${ORIGIN}</i>)</p>
<dd>This expands to the directory containing the program or shared object. Thus, an application located in <i>somedir/app</i> could be compiled with</p>
<dd>gcc -Wl,-rpath,&#8217;$ORIGIN/../lib&#8217;</p>
<dd>so that it finds an associated shared object in <i>somedir/lib</i> no matter where <i>somedir</i> is located in the directory hierarchy. This facilitates the creation of &quot;turn-key&quot; applications that do not need to be installed into special directories, but can instead be unpacked into any directory and still find their own shared objects.</p>
<dt><i>$LIB</i> (or equivalently <i>${LIB}</i>)</p>
<dd>This expands to <i>lib</i> or <i>lib64</i> depending on the architecture (e.g., on x86-64, it expands to <i>lib64</i> and on x86-32, it expands to <i>lib</i>).</p>
<dt><i>$PLATFORM</i> (or equivalently <i>${PLATFORM}</i>)</p>
<dd>This expands to a string corresponding to the processor type of the host system (e.g., &quot;x86_64&quot;). On some architectures, the Linux kernel doesn&#8217;t provide a platform string to the dynamic linker. The value of this string is taken from the <code>AT_PLATFORM</code> value in the auxiliary vector (see <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)).</dl>
<p> Note that the dynamic string tokens have to be quoted properly when set from a shell, to prevent their expansion as shell or environment variables.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;audit</code><i> list</i></p>
<dd>Use objects named in <i>list</i> as auditors. The objects in <i>list</i> are delimited by colons.</p>
<dt><code>&#8211;inhibit-cache</code></p>
<dd>Do not use <i>/etc/ld.so.cache</i>.</p>
<dt><code>&#8211;library-path</code><i> path</i></p>
<dd>Use <i>path</i> instead of <code>LD_LIBRARY_PATH</code> environment variable setting (see below). The names <i>ORIGIN</i>, <i>LIB</i>, and <i>PLATFORM</i> are interpreted as for the <code>LD_LIBRARY_PATH</code> environment variable.</p>
<dt><code>&#8211;inhibit-rpath</code><i> list</i></p>
<dd>Ignore RPATH and RUNPATH information in object names in <i>list</i>. This option is ignored when running in secure-execution mode (see below). The objects in <i>list</i> are delimited by colons or spaces.</p>
<dt><code>&#8211;list</code></p>
<dd>List all dependencies and how they are resolved.</p>
<dt><code>&#8211;preload</code> <i>list</i> (since glibc 2.30)</p>
<dd>Preload the objects specified in <i>list</i>. The objects in <i>list</i> are delimited by colons or spaces. The objects are preloaded as explained in the description of the <code>LD_PRELOAD</code> environment variable below.</p>
<dd>By contrast with <code>LD_PRELOAD</code>, the <code>&#8211;preload</code> option provides a way to perform preloading for a single executable without affecting preloading performed in any child process that executes a new program.</p>
<dt><code>&#8211;verify</code></p>
<dd>Verify that program is dynamically linked and this dynamic linker can handle it.</dl>
<h2>Environment</h2>
<p>Various environment variables influence the operation of the dynamic linker.</p>
<h3>Secure-execution mode</h3>
<p>For security reasons, if the dynamic linker determines that a binary should be run in secure-execution mode, the effects of some environment variables are voided or modified, and furthermore those environment variables are stripped from the environment, so that the program does not even see the definitions. Some of these environment variables affect the operation of the dynamic linker itself, and are described below. Other environment variables treated in this way include: <code>GCONV_PATH</code>, <code>GETCONF_DIR</code>, <code>HOSTALIASES</code>, <code>LOCALDOMAIN</code>, <code>LOCPATH</code>, <code>MALLOC_TRACE</code>, <code>NIS_PATH</code>, <code>NLSPATH</code>, <code>RESOLV_HOST_CONF</code>, <code>RES_OPTIONS</code>, <code>TMPDIR</code>, and <code>TZDIR</code>. </p>
<p> A binary is executed in secure-execution mode if the <code>AT_SECURE</code> entry in the auxiliary vector (see <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)) has a nonzero value. This entry may have a nonzero value for various reasons, including:</p>
<dl>
<dt>*</p>
<dd>The process&#8217;s real and effective user IDs differ, or the real and effective group IDs differ. This typically occurs as a result of executing a set-user-ID or set-group-ID program.</p>
<dt>*</p>
<dd>A process with a non-root user ID executed a binary that conferred capabilities to the process.</p>
<dt>*</p>
<dd>A nonzero value may have been set by a Linux Security Module.</dl>
<h3>Environment variables</h3>
<p>Among the more important environment variables are the following:</p>
<dl>
<dt><code>LD_ASSUME_KERNEL</code> (since glibc 2.2.3)</p>
<dd>Each shared object can inform the dynamic linker of the minimum kernel ABI version that it requires. (This requirement is encoded in an ELF note section that is viewable via <i>readelf -n</i> as a section labeled <code>NT_GNU_ABI_TAG</code>.) At run time, the dynamic linker determines the ABI version of the running kernel and will reject loading shared objects that specify minimum ABI versions that exceed that ABI version.</p>
<dd><code>LD_ASSUME_KERNEL</code> can be used to cause the dynamic linker to assume that it is running on a system with a different kernel ABI version. For example, the following command line causes the dynamic linker to assume it is running on Linux 2.2.5 when loading the shared objects required by <i>myprog</i>:</p>
<dd>$ <code>LD_ASSUME_KERNEL=2.2.5 ./myprog</code></p>
<dd>On systems that provide multiple versions of a shared object (in different directories in the search path) that have different minimum kernel ABI version requirements, <code>LD_ASSUME_KERNEL</code> can be used to select the version of the object that is used (dependent on the directory search order).</p>
<dd>Historically, the most common use of the <code>LD_ASSUME_KERNEL</code> feature was to manually select the older LinuxThreads POSIX threads implementation on systems that provided both LinuxThreads and NPTL (which latter was typically the default on such systems); see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7).</p>
<dt><code>LD_BIND_NOW</code> (since glibc 2.1.1)</p>
<dd>If set to a nonempty string, causes the dynamic linker to resolve all symbols at program startup instead of deferring function call resolution to the point when they are first referenced. This is useful when using a debugger.</p>
<dt><code>LD_LIBRARY_PATH</code></p>
<dd>A list of directories in which to search for ELF libraries at execution time. The items in the list are separated by either colons or semicolons, and there is no support for escaping either separator. A zero-length directory name indicates the current working directory.</p>
<dd>This variable is ignored in secure-execution mode.</p>
<dd>Within the pathnames specified in <code>LD_LIBRARY_PATH</code>, the dynamic linker expands the tokens <i>$ORIGIN</i>, <i>$LIB</i>, and <i>$PLATFORM</i> (or the versions using curly braces around the names) as described above in <i>Dynamic string tokens</i>. Thus, for example, the following would cause a library to be searched for in either the <i>lib</i> or <i>lib64</i> subdirectory below the directory containing the program to be executed:</p>
<dd>$ <code>LD_LIBRARY_PATH=&#8217;$ORIGIN/$LIB&#8217; prog</code></p>
<dd>(Note the use of single quotes, which prevent expansion of <i>$ORIGIN</i> and <i>$LIB</i> as shell variables!)</p>
<dt><code>LD_PRELOAD</code></p>
<dd>A list of additional, user-specified, ELF shared objects to be loaded before all others. This feature can be used to selectively override functions in other shared objects.</p>
<dd>The items of the list can be separated by spaces or colons, and there is no support for escaping either separator. The objects are searched for using the rules given under DESCRIPTION. Objects are searched for and added to the link map in the left-to-right order specified in the list.</p>
<dd>In secure-execution mode, preload pathnames containing slashes are ignored. Furthermore, shared objects are preloaded only from the standard search directories and only if they have set-user-ID mode bit enabled (which is not typical).</p>
<dd>Within the names specified in the <code>LD_PRELOAD</code> list, the dynamic linker understands the tokens <i>$ORIGIN</i>, <i>$LIB</i>, and <i>$PLATFORM</i> (or the versions using curly braces around the names) as described above in <i>Dynamic string tokens</i>. (See also the discussion of quoting under the description of <code>LD_LIBRARY_PATH</code>.)</p>
<dd>There are various methods of specifying libraries to be preloaded, and these are handled in the following order:</p>
<dl>
<dd>
<dl>
<dt>(1)</p>
<dd>The <code>LD_PRELOAD</code> environment variable.</p>
<dt>(2)</p>
<dd>The <code>&#8211;preload</code> command-line option when invoking the dynamic linker directly.</p>
<dt>(3)</p>
<dd>The <i>/etc/ld.so.preload</i> file (described below).</dl>
</dl>
<dt><code>LD_TRACE_LOADED_OBJECTS</code></p>
<dd>If set (to any value), causes the program to list its dynamic dependencies, as if run by <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), instead of running normally.</dl>
<p> Then there are lots of more or less obscure variables, many obsolete or only for internal use.</p>
<dl>
<dt><code>LD_AUDIT</code> (since glibc 2.4)</p>
<dd>A list of user-specified, ELF shared objects to be loaded before all others in a separate linker namespace (i.e., one that does not intrude upon the normal symbol bindings that would occur in the process) These objects can be used to audit the operation of the dynamic linker. The items in the list are colon-separated, and there is no support for escaping the separator.</p>
<dd><code>LD_AUDIT</code> is ignored in secure-execution mode.</p>
<dd>The dynamic linker will notify the audit shared objects at so-called auditing checkpoints&#8212;for example, loading a new shared object, resolving a symbol, or calling a symbol from another shared object&#8212;by calling an appropriate function within the audit shared object. For details, see <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a></code>(7). The auditing interface is largely compatible with that provided on Solaris, as described in its <i>Linker and Libraries Guide</i>, in the chapter <i>Runtime Linker Auditing Interface</i>.</p>
<dd>Within the names specified in the <code>LD_AUDIT</code> list, the dynamic linker understands the tokens <i>$ORIGIN</i>, <i>$LIB</i>, and <i>$PLATFORM</i> (or the versions using curly braces around the names) as described above in <i>Dynamic string tokens</i>. (See also the discussion of quoting under the description of <code>LD_LIBRARY_PATH</code>.)</p>
<dd>Since glibc 2.13, in secure-execution mode, names in the audit list that contain slashes are ignored, and only shared objects in the standard search directories that have the set-user-ID mode bit enabled are loaded.</p>
<dt><code>LD_BIND_NOT</code> (since glibc 2.1.95)</p>
<dd>If this environment variable is set to a nonempty string, do not update the GOT (global offset table) and PLT (procedure linkage table) after resolving a function symbol. By combining the use of this variable with <code>LD_DEBUG</code> (with the categories <i>bindings</i> and <i>symbols</i>), one can observe all run-time function bindings.</p>
<dt><code>LD_DEBUG</code> (since glibc 2.1)</p>
<dd>Output verbose debugging information about operation of the dynamic linker. The content of this variable is one of more of the following categories, separated by colons, commas, or (if the value is quoted) spaces:</p>
<dl>
<dd>
<dl>
<dt><i>help</i></p>
<dd>Specifying <i>help</i> in the value of this variable does not run the specified program, and displays a help message about which categories can be specified in this environment variable.</p>
<dt><i>all</i></p>
<dd>Print all debugging information (except <i>statistics</i> and <i>unused</i>; see below).</p>
<dt><i>bindings</i></p>
<dd>Display information about which definition each symbol is bound to.</p>
<dt><i>files</i></p>
<dd>Display progress for input file.</p>
<dt><i>libs</i></p>
<dd>Display library search paths.</p>
<dt><i>reloc</i></p>
<dd>Display relocation processing.</p>
<dt><i>scopes</i></p>
<dd>Display scope information.</p>
<dt><i>statistics</i></p>
<dd>Display relocation statistics.</p>
<dt><i>symbols</i></p>
<dd>Display search paths for each symbol look-up.</p>
<dt><i>unused</i></p>
<dd>Determine unused DSOs.</p>
<dt><i>versions</i></p>
<dd>Display version dependencies.</dl>
</dl>
<dd>Since glibc 2.3.4, <code>LD_DEBUG</code> is ignored in secure-execution mode, unless the file <i>/etc/suid-debug</i> exists (the content of the file is irrelevant).</p>
<dt><code>LD_DEBUG_OUTPUT</code> (since glibc 2.1)</p>
<dd>By default, <code>LD_DEBUG</code> output is written to standard error. If <code>LD_DEBUG_OUTPUT</code> is defined, then output is written to the pathname specified by its value, with the suffix &quot;.&quot; (dot) followed by the process ID appended to the pathname.</p>
<dd><code>LD_DEBUG_OUTPUT</code> is ignored in secure-execution mode.</p>
<dt><code>LD_DYNAMIC_WEAK</code> (since glibc 2.1.91)</p>
<dd>By default, when searching shared libraries to resolve a symbol reference, the dynamic linker will resolve to the first definition it finds.</p>
<dd>Old glibc versions (before 2.2), provided a different behavior: if the linker found a symbol that was weak, it would remember that symbol and keep searching in the remaining shared libraries. If it subsequently found a strong definition of the same symbol, then it would instead use that definition. (If no further symbol was found, then the dynamic linker would use the weak symbol that it initially found.)</p>
<dd>The old glibc behavior was nonstandard. (Standard practice is that the distinction between weak and strong symbols should have effect only at static link time.) In glibc 2.2, the dynamic linker was modified to provide the current behavior (which was the behavior that was provided by most other implementations at that time).</p>
<dd>Defining the <code>LD_DYNAMIC_WEAK</code> environment variable (with any value) provides the old (nonstandard) glibc behavior, whereby a weak symbol in one shared library may be overridden by a strong symbol subsequently discovered in another shared library. (Note that even when this variable is set, a strong symbol in a shared library will not override a weak definition of the same symbol in the main program.)</p>
<dd>Since glibc 2.3.4, <code>LD_DYNAMIC_WEAK</code> is ignored in secure-execution mode.</p>
<dt><code>LD_HWCAP_MASK</code> (since glibc 2.1)</p>
<dd>Mask for hardware capabilities.</p>
<dt><code>LD_ORIGIN_PATH</code> (since glibc 2.1)</p>
<dd>Path where the binary is found.</p>
<dd>Since glibc 2.4, <code>LD_ORIGIN_PATH</code> is ignored in secure-execution mode.</p>
<dt><code>LD_POINTER_GUARD</code> (glibc from 2.4 to 2.22)</p>
<dd>Set to 0 to disable pointer guarding. Any other value enables pointer guarding, which is also the default. Pointer guarding is a security mechanism whereby some pointers to code stored in writable program memory (return addresses saved by <code><a href="/docs/linux/man/3-setjmp/">setjmp</a></code>(3) or function pointers used by various glibc internals) are mangled semi-randomly to make it more difficult for an attacker to hijack the pointers for use in the event of a buffer overrun or stack-smashing attack. Since glibc 2.23, <code>LD_POINTER_GUARD</code> can no longer be used to disable pointer guarding, which is now always enabled.</p>
<dt><code>LD_PROFILE</code> (since glibc 2.1)</p>
<dd>The name of a (single) shared object to be profiled, specified either as a pathname or a soname. Profiling output is appended to the file whose name is: &quot;<i>$LD_PROFILE_OUTPUT</i>/<i>$LD_PROFILE</i>.profile&quot;.</p>
<dd>Since glibc 2.2.5, <code>LD_PROFILE</code> is ignored in secure-execution mode.</p>
<dt><code>LD_PROFILE_OUTPUT</code> (since glibc 2.1)</p>
<dd>Directory where <code>LD_PROFILE</code> output should be written. If this variable is not defined, or is defined as an empty string, then the default is <i>/var/tmp</i>.</p>
<dd><code>LD_PROFILE_OUTPUT</code> is ignored in secure-execution mode; instead <i>/var/profile</i> is always used. (This detail is relevant only before glibc 2.2.5, since in later glibc versions, <code>LD_PROFILE</code> is also ignored in secure-execution mode.)</p>
<dt><code>LD_SHOW_AUXV</code> (since glibc 2.1)</p>
<dd>If this environment variable is defined (with any value), show the auxiliary array passed up from the kernel (see also <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)).</p>
<dd>Since glibc 2.3.4, <code>LD_SHOW_AUXV</code> is ignored in secure-execution mode.</p>
<dt><code>LD_TRACE_PRELINKING</code> (since glibc 2.4)</p>
<dd>If this environment variable is defined, trace prelinking of the object whose name is assigned to this environment variable. (Use <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1) to get a list of the objects that might be traced.) If the object name is not recognized, then all prelinking activity is traced.</p>
<dt><code>LD_USE_LOAD_BIAS</code> (since glibc 2.3.3)</p>
<dd>By default (i.e., if this variable is not defined), executables and prelinked shared objects will honor base addresses of their dependent shared objects and (nonprelinked) position-independent executables (PIEs) and other shared objects will not honor them. If <code>LD_USE_LOAD_BIAS</code> is defined with the value 1, both executables and PIEs will honor the base addresses. If <code>LD_USE_LOAD_BIAS</code> is defined with the value 0, neither executables nor PIEs will honor the base addresses.</p>
<dd>Since glibc 2.3.3, this variable is ignored in secure-execution mode.</p>
<dt><code>LD_VERBOSE</code> (since glibc 2.1)</p>
<dd>If set to a nonempty string, output symbol versioning information about the program if the <code>LD_TRACE_LOADED_OBJECTS</code> environment variable has been set.</p>
<dt><code>LD_WARN</code> (since glibc 2.1.3)</p>
<dd>If set to a nonempty string, warn about unresolved symbols.</p>
<dt><code>LD_PREFER_MAP_32BIT_EXEC</code> (x86-64 only; since glibc 2.23)</p>
<dd>According to the Intel Silvermont software optimization guide, for 64-bit applications, branch prediction performance can be negatively impacted when the target of a branch is more than 4 GB away from the branch. If this environment variable is set (to any value), the dynamic linker will first try to map executable pages using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_32BIT</code> flag, and fall back to mapping without that flag if that attempt fails. NB: MAP_32BIT will map to the low 2 GB (not 4 GB) of the address space.</p>
<dd>Because <code>MAP_32BIT</code> reduces the address range available for address space layout randomization (ASLR), <code>LD_PREFER_MAP_32BIT_EXEC</code> is always disabled in secure-execution mode.</dl>
<h2>Files</h2>
<dl>
<dt><i>/lib/ld.so</i></p>
<dd>a.out dynamic linker/loader</p>
<dt><i>/lib/ld-linux.so.</i>{<i>1</i>,<i>2</i>}</p>
<dd>ELF dynamic linker/loader</p>
<dt><i>/etc/ld.so.cache</i></p>
<dd>File containing a compiled list of directories in which to search for shared objects and an ordered list of candidate shared objects. See <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8).</p>
<dt><i>/etc/ld.so.preload</i></p>
<dd>File containing a whitespace-separated list of ELF shared objects to be loaded before the program. See the discussion of <code>LD_PRELOAD</code> above. If both <code>LD_PRELOAD</code> and <i>/etc/ld.so.preload</i> are employed, the libraries specified by <code>LD_PRELOAD</code> are preloaded first. <i>/etc/ld.so.preload</i> has a system-wide effect, causing the specified libraries to be preloaded for all programs that are executed on the system. (This is usually undesirable, and is typically employed only as an emergency remedy, for example, as a temporary workaround to a library misconfiguration issue.)</p>
<dt><i>lib*.so*</i></p>
<dd>shared objects</dl>
<h2>Notes</h2>
<h3>Hardware capabilities</h3>
<p>Some shared objects are compiled using hardware-specific instructions which do not exist on every CPU. Such objects should be installed in directories whose names define the required hardware capabilities, such as <i>/usr/lib/sse2/</i>. The dynamic linker checks these directories against the hardware of the machine and selects the most suitable version of a given shared object. Hardware capability directories can be cascaded to combine CPU features. The list of supported hardware capability names depends on the CPU. The following names are currently recognized:</p>
<dl>
<dt><code>Alpha</code></p>
<dd>ev4, ev5, ev56, ev6, ev67</p>
<dt><code>MIPS</code></p>
<dd>loongson2e, loongson2f, octeon, octeon2</p>
<dt><code>PowerPC</code></p>
<dd>4xxmac, altivec, arch_2_05, arch_2_06, booke, cellbe, dfp, efpdouble, efpsingle, fpu, ic_snoop, mmu, notb, pa6t, power4, power5, power5+, power6x, ppc32, ppc601, ppc64, smt, spe, ucache, vsx</p>
<dt><code>SPARC</code></p>
<dd>flush, muldiv, stbar, swap, ultra3, v9, v9v, v9v2</p>
<dt><code>s390</code></p>
<dd>dfp, eimm, esan3, etf3enh, g5, highgprs, hpage, ldisp, msa, stfle, z900, z990, z9-109, z10, zarch</p>
<dt><code>x86 (32-bit only)</code></p>
<dd>acpi, apic, clflush, cmov, cx8, dts, fxsr, ht, i386, i486, i586, i686, mca, mmx, mtrr, pat, pbe, pge, pn, pse36, sep, ss, sse, sse2, tm</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/1-pldd/">pldd</a></code>(1), <code><a href="/docs/linux/man/1-sprof/">sprof</a></code>(1), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/5-elf/">elf</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a></code>(7), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8), <code><a href="/docs/linux/man/8-sln/">sln</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
