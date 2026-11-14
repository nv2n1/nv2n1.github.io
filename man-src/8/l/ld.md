---
title: "ld(8)"
name: "ld"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ld/"
description: "ld.so, ld-linux.so* – dynamic linker/loader"
---

<p>ld.so, ld-linux.so* &#8211; dynamic linker/loader</p>
<h2>Synopsis</h2>
<p>The dynamic linker can be run either indirectly by running some dynamically linked program or library (in which case no command-line options to the dynamic linker can be passed and, in the ELF case, the dynamic linker which is stored in the <code>.interp</code> section of the program is executed) or directly by running: </p>
<p> <i>/lib/ld-linux.so.*</i> [OPTIONS] [PROGRAM [ARGUMENTS]]</p>
<h2>Description</h2>
<p>The programs <code>ld.so</code> and <code>ld-linux.so*</code> find and load the shared libraries needed by a program, prepare the program to run, and then run it. </p>
<p> Linux binaries require dynamic linking (linking at run time) unless the <code>-static</code> option was given to <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) during compilation. </p>
<p> The program <code>ld.so</code> handles a.out binaries, a format used long ago; <code>ld-linux.so*</code> handles ELF (<i>/lib/ld-linux.so.1</i> for libc5, <i>/lib/ld-linux.so.2</i> for glibc2), which everybody has been using for years now. Otherwise, both have the same behavior, and use the same support files and programs <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8) and <i>/etc/ld.so.conf</i>. </p>
<p> When resolving library dependencies, the dynamic linker first inspects each dependency string to see if it contains a slash (this can occur if a library pathname containing slashes was specified at link time). If a slash is found, then the dependency string is interpreted as a (relative or absolute) pathname, and the library is loaded using that pathname. </p>
<p> If a library dependency does not contain a slash, then it is searched for in the following order:</p>
<dl>
<dt>o</p>
<dd>(ELF only) Using the directories specified in the DT_RPATH dynamic section attribute of the binary if present and DT_RUNPATH attribute does not exist. Use of DT_RPATH is deprecated.</p>
<dt>o</p>
<dd>Using the environment variable <code>LD_LIBRARY_PATH</code>. Except if the executable is a set-user-ID/set-group-ID binary, in which case it is ignored.</p>
<dt>o</p>
<dd>(ELF only) Using the directories specified in the DT_RUNPATH dynamic section attribute of the binary if present.</p>
<dt>o</p>
<dd>From the cache file <i>/etc/ld.so.cache</i>, which contains a compiled list of candidate libraries previously found in the augmented library path. If, however, the binary was linked with the <code>-z nodeflib</code> linker option, libraries in the default library paths are skipped. Libraries installed in hardware capability directories (see below) are preferred to other libraries.</p>
<dt>o</p>
<dd>In the default path <i>/lib</i>, and then <i>/usr/lib</i>. If the binary was linked with the <code>-z nodeflib</code> linker option, this step is skipped.</dl>
<h3>Rpath token expansion</h3>
<p><code>ld.so</code> understands certain strings in an rpath specification (DT_RPATH or DT_RUNPATH); those strings are substituted as follows</p>
<dl>
<dt><i>$ORIGIN</i> (or equivalently <i>${ORIGIN}</i>)</p>
<dd>This expands to the directory containing the application executable. Thus, an application located in <i>somedir/app</i> could be compiled with </p>
<p>&nbsp;<wbr>gcc -Wl,-rpath,&#8217;$ORIGIN/../lib&#8217; </p>
<p> so that it finds an associated shared library in <i>somedir/lib</i> no matter where <i>somedir</i> is located in the directory hierarchy. This facilitates the creation of &quot;turn-key&quot; applications that do not need to be installed into special directories, but can instead be unpacked into any directory and still find their own shared libraries.</p>
<dt><i>$LIB</i> (or equivalently <i>${LIB}</i>)</p>
<dd>This expands to <i>lib</i> or <i>lib64</i> depending on the architecture (e.g., on x86-64, it expands to <i>lib64</i> and on x86-32, it expands to <i>lib</i>).</p>
<dt><i>$PLATFORM</i> (or equivalently <i>${PLATFORM}</i>)</p>
<dd>This expands to a string corresponding to the processor type of the host system (e.g., &quot;x86_64&quot;). On some architectures, the Linux kernel doesn&#8217;t provide a platform string to the dynamic linker. The value of this string is taken from the <code>AT_PLATFORM</code> value in the auxiliary vector (see <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)).</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;list</code></p>
<dd>List all dependencies and how they are resolved.</p>
<dt><code>&#8211;verify</code></p>
<dd>Verify that program is dynamically linked and this dynamic linker can handle it.</p>
<dt><code>&#8211;library-path PATH</code></p>
<dd>Use PATH instead of <code>LD_LIBRARY_PATH</code> environment variable setting (see below).</p>
<dt><code>&#8211;inhibit-rpath LIST</code></p>
<dd>Ignore RPATH and RUNPATH information in object names in LIST. This option is ignored if <code>ld.so</code> is set-user-ID or set-group-ID.</p>
<dt><code>&#8211;audit LIST</code></p>
<dd>Use objects named in LIST as auditors.</dl>
<h2>Hardware Capabilities</h2>
<p>Some libraries are compiled using hardware-specific instructions which do not exist on every CPU. Such libraries should be installed in directories whose names define the required hardware capabilities, such as <i>/usr/lib/sse2/</i>. The dynamic linker checks these directories against the hardware of the machine and selects the most suitable version of a given library. Hardware capability directories can be cascaded to combine CPU features. The list of supported hardware capability names depends on the CPU. The following names are currently recognized:</p>
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
<h2>Environment</h2>
<p>Among the more important environment variables are the following:</p>
<dl>
<dt><code>LD_ASSUME_KERNEL</code></p>
<dd>(glibc since 2.2.3) Each shared library can inform the dynamic linker of the minimum kernel ABI version that it requires. (This requirement is encoded in an ELF note section that is viewable via <i>readelf -n</i> as a section labeled <code>NT_GNU_ABI_TAG</code>.) At run time, the dynamic linker determines the ABI version of the running kernel and will reject loading shared libraries that specify minimum ABI versions that exceed that ABI version. </p>
<p> <code>LD_ASSUME_KERNEL</code> can be used to cause the dynamic linker to assume that it is running on a system with a different kernel ABI version. For example, the following command line causes the dynamic linker to assume it is running on Linux 2.2.5 when loading the shared libraries required by <i>myprog</i>: </p>
<pre>$ <code>LD_ASSUME_KERNEL=2.2.5 ./myprog</code></pre>
<p>On systems that provide multiple versions of a shared library (in different directories in the search path) that have different minimum kernel ABI version requirements, <code>LD_ASSUME_KERNEL</code> can be used to select the version of the library that is used (dependent on the directory search order). Historically, the most common use of the <code>LD_ASSUME_KERNEL</code> feature was to manually select the older LinuxThreads POSIX threads implementation on systems that provided both LinuxThreads and NPTL (which latter was typically the default on such systems); see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7).</p>
<dt><code>LD_BIND_NOT</code></p>
<dd>(glibc since 2.2) Don&#8217;t update the Global Offset Table (GOT) and Procedure Linkage Table (PLT) when resolving a symbol.</p>
<dt><code>LD_BIND_NOW</code></p>
<dd>(libc5; glibc since 2.1.1) If set to a nonempty string, causes the dynamic linker to resolve all symbols at program startup instead of deferring function call resolution to the point when they are first referenced. This is useful when using a debugger.</p>
<dt><code>LD_LIBRARY_PATH</code></p>
<dd>A colon-separated list of directories in which to search for ELF libraries at execution-time. Similar to the <code>PATH</code> environment variable. Ignored in set-user-ID and set-group-ID programs.</p>
<dt><code>LD_PRELOAD</code></p>
<dd>A list of additional, user-specified, ELF shared libraries to be loaded before all others. The items of the list can be separated by spaces or colons. This can be used to selectively override functions in other shared libraries. The libraries are searched for using the rules given under DESCRIPTION. For set-user-ID/set-group-ID ELF binaries, preload pathnames containing slashes are ignored, and libraries in the standard search directories are loaded only if the set-user-ID permission bit is enabled on the library file.</p>
<dt><code>LD_TRACE_LOADED_OBJECTS</code></p>
<dd>(ELF only) If set to a nonempty string, causes the program to list its dynamic library dependencies, as if run by <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), instead of running normally.</dl>
<p> Then there are lots of more or less obscure variables, many obsolete or only for internal use.</p>
<dl>
<dt><code>LD_AOUT_LIBRARY_PATH</code></p>
<dd>(libc5) Version of <code>LD_LIBRARY_PATH</code> for a.out binaries only. Old versions of ld-linux.so.1 also supported <code>LD_ELF_LIBRARY_PATH</code>.</p>
<dt><code>LD_AOUT_PRELOAD</code></p>
<dd>(libc5) Version of <code>LD_PRELOAD</code> for a.out binaries only. Old versions of ld-linux.so.1 also supported <code>LD_ELF_PRELOAD</code>.</p>
<dt><code>LD_AUDIT</code></p>
<dd>(glibc since 2.4) A colon-separated list of user-specified, ELF shared objects to be loaded before all others in a separate linker namespace (i.e., one that does not intrude upon the normal symbol bindings that would occur in the process). These libraries can be used to audit the operation of the dynamic linker. <code>LD_AUDIT</code> is ignored for set-user-ID/set-group-ID binaries. </p>
<p> The dynamic linker will notify the audit libraries at so-called auditing checkpoints&#8212;for example, loading a new library, resolving a symbol, or calling a symbol from another shared object&#8212;by calling an appropriate function within the audit library. For details, see <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a></code>(7). The auditing interface is largely compatible with that provided on Solaris, as described in its <i>Linker and Libraries Guide</i>, in the chapter <i>Runtime Linker Auditing Interface</i>.</p>
<dt><code>LD_BIND_NOT</code></p>
<dd>(glibc since 2.1.95) Do not update the GOT (global offset table) and PLT (procedure linkage table) after resolving a symbol.</p>
<dt><code>LD_DEBUG</code></p>
<dd>(glibc since 2.1) Output verbose debugging information about the dynamic linker. If set to <code>all</code> prints all debugging information it has, if set to <code>help</code> prints a help message about which categories can be specified in this environment variable. Since glibc 2.3.4, <code>LD_DEBUG</code> is ignored for set-user-ID/set-group-ID binaries.</p>
<dt><code>LD_DEBUG_OUTPUT</code></p>
<dd>(glibc since 2.1) File in which <code>LD_DEBUG</code> output should be written. The default is standard error. <code>LD_DEBUG_OUTPUT</code> is ignored for set-user-ID/set-group-ID binaries.</p>
<dt><code>LD_DYNAMIC_WEAK</code></p>
<dd>(glibc since 2.1.91) Allow weak symbols to be overridden (reverting to old glibc behavior). For security reasons, since glibc 2.3.4, <code>LD_DYNAMIC_WEAK</code> is ignored for set-user-ID/set-group-ID binaries.</p>
<dt><code>LD_HWCAP_MASK</code></p>
<dd>(glibc since 2.1) Mask for hardware capabilities.</p>
<dt><code>LD_KEEPDIR</code></p>
<dd>(a.out only)(libc5) Don&#8217;t ignore the directory in the names of a.out libraries to be loaded. Use of this option is strongly discouraged.</p>
<dt><code>LD_NOWARN</code></p>
<dd>(a.out only)(libc5) Suppress warnings about a.out libraries with incompatible minor version numbers.</p>
<dt><code>LD_ORIGIN_PATH</code></p>
<dd>(glibc since 2.1) Path where the binary is found (for non-set-user-ID programs). For security reasons, since glibc 2.4, <code>LD_ORIGIN_PATH</code> is ignored for set-user-ID/set-group-ID binaries.</p>
<dt><code>LD_POINTER_GUARD</code></p>
<dd>(glibc since 2.4) Set to 0 to disable pointer guarding. Any other value enables pointer guarding, which is also the default. Pointer guarding is a security mechanism whereby some pointers to code stored in writable program memory (return addresses saved by <code><a href="/docs/linux/man/3-setjmp/">setjmp</a></code>(3) or function pointers used by various glibc internals) are mangled semi-randomly to make it more difficult for an attacker to hijack the pointers for use in the event of a buffer overrun or stack-smashing attack.</p>
<dt><code>LD_PROFILE</code></p>
<dd>(glibc since 2.1) Shared object to be profiled, specified either as a pathname or a soname. Profiling output is written to the file whose name is: &quot;<i>$LD_PROFILE_OUTPUT</i>/<i>$LD_PROFILE</i>.profile&quot;.</p>
<dt><code>LD_PROFILE_OUTPUT</code></p>
<dd>(glibc since 2.1) Directory where <code>LD_PROFILE</code> output should be written. If this variable is not defined, or is defined as an empty string, then the default is <i>/var/tmp</i>. <code>LD_PROFILE_OUTPUT</code> is ignored for set-user-ID and set-group-ID programs, which always use <i>/var/profile</i>.</p>
<dt><code>LD_SHOW_AUXV</code></p>
<dd>(glibc since 2.1) Show auxiliary array passed up from the kernel. For security reasons, since glibc 2.3.5, <code>LD_SHOW_AUXV</code> is ignored for set-user-ID/set-group-ID binaries.</p>
<dt><code>LD_USE_LOAD_BIAS</code></p>
<dd>By default (i.e., if this variable is not defined) executables and prelinked shared objects will honor base addresses of their dependent libraries and (nonprelinked) position-independent executables (PIEs) and other shared objects will not honor them. If <code>LD_USE_LOAD_BIAS</code> is defined wit the value, both executables and PIEs will honor the base addresses. If <code>LD_USE_LOAD_BIAS</code> is defined with the value 0, neither executables nor PIEs will honor the base addresses. This variable is ignored by set-user-ID and set-group-ID programs.</p>
<dt><code>LD_VERBOSE</code></p>
<dd>(glibc since 2.1) If set to a nonempty string, output symbol versioning information about the program if the <code>LD_TRACE_LOADED_OBJECTS</code> environment variable has been set.</p>
<dt><code>LD_WARN</code></p>
<dd>(ELF only)(glibc since 2.1.3) If set to a nonempty string, warn about unresolved symbols.</p>
<dt><code>LDD_ARGV0</code></p>
<dd>(libc5) <i>argv</i>[0] to be used by <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1) when none is present.</dl>
<h2>Files</h2>
<dl>
<dt><i>/lib/ld.so</i></p>
<dd>a.out dynamic linker/loader</p>
<dt><i>/lib/ld-linux.so.</i>{<i>1</i>,<i>2</i>}</p>
<dd>ELF dynamic linker/loader</p>
<dt><i>/etc/ld.so.cache</i></p>
<dd>File containing a compiled list of directories in which to search for libraries and an ordered list of candidate libraries.</p>
<dt><i>/etc/ld.so.preload</i></p>
<dd>File containing a whitespace-separated list of ELF shared libraries to be loaded before the program.</p>
<dt><code>lib*.so*</code></p>
<dd>shared libraries</dl>
<h2>Notes</h2>
<p>The <code>ld.so</code> functionality is available for executables compiled using libc version 4.4.3 or greater. ELF functionality is available since Linux 1.1.52 and libc5.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/7-rtld-audit/">rtld-audit</a></code>(7), <code><a href="/docs/linux/man/8-ldconfig/">ldconfig</a></code>(8), <code><a href="/docs/linux/man/8-sln/">sln</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.69 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
