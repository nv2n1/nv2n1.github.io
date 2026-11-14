---
title: "dpkg-buildflags(1)"
name: "dpkg-buildflags"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-buildflags/"
description: "dpkg-buildflags – returns build flags to use during package build"
---

<h2 class="name">NAME</h2>
<p> dpkg-buildflags &#8211; returns build flags to use during package build </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-buildflags</code> [<i>option</i>&#8230;] [<i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-buildflags</code> is a tool to retrieve compilation flags to use during build of Debian packages. </p>
<p> The default flags are defined by the vendor but they can be extended/overridden in several ways:</p>
<dl>
<dt>1.</p>
<dd> system-wide with <code>/etc/dpkg/buildflags.conf</code>;</p>
<dt>2.</p>
<dd> for the current user with $XDG_CONFIG_HOME<code>/dpkg/buildflags.conf</code> where $XDG_CONFIG_HOME defaults to $HOME<code>/.config</code>;</p>
<dt>3.</p>
<dd> temporarily by the user with environment variables (see section <font SIZE="-1"><code>ENVIRONMENT</code></font>);</p>
<dt>4.</p>
<dd> dynamically by the package maintainer with environment variables set via <code>debian/rules</code> (see section <font SIZE="-1"><code>ENVIRONMENT</code></font>).</dl>
<p> The configuration files can contain four types of directives:</p>
<dl>
<dt><font SIZE="-1"><code>SET</code></font> <i>flag value</i></p>
<dd> Override the flag named <i>flag</i> to have the value <i>value</i>.</p>
<dt><font SIZE="-1"><code>STRIP</code></font> <i>flag value</i></p>
<dd> Strip from the flag named <i>flag</i> all the build flags listed in <i>value</i>.</p>
<dt><font SIZE="-1"><code>APPEND</code></font> <i>flag value</i></p>
<dd> Extend the flag named <i>flag</i> by appending the options given in <i>value</i>. A space is prepended to the appended value if the flag&#8217;s current value is non-empty.</p>
<dt><font SIZE="-1"><code>PREPEND</code></font> <i>flag value</i></p>
<dd> Extend the flag named <i>flag</i> by prepending the options given in <i>value</i>. A space is appended to the prepended value if the flag&#8217;s current value is non-empty.</dl>
<p> The configuration files can contain comments on lines starting with a hash (#). Empty lines are also ignored.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;dump</code></p>
<dd> Print to standard output all compilation flags and their values. It prints one flag per line separated from its value by an equal sign (&#8220;<i>flag</i>=<i>value</i>&#8220;). This is the default action.</p>
<dt><code>&#8211;list</code></p>
<dd> Print the list of flags supported by the current vendor (one per line). See the <font SIZE="-1"><code>SUPPORTED FLAGS</code></font> section for more information about them.</p>
<dt><code>&#8211;status</code></p>
<dd> Display any information that can be useful to explain the behaviour of <code>dpkg-buildflags</code> (since dpkg 1.16.5): relevant environment variables, current vendor, state of all feature flags. Also print the resulting compiler flags with their origin. </p>
<p> This is intended to be run from <code>debian/rules</code>, so that the build log keeps a clear trace of the build flags used. This can be useful to diagnose problems related to them.</p>
<dt><code>&#8211;export=</code><i>format</i></p>
<dd> Print to standard output commands that can be used to export all the compilation flags for some particular tool. If the <i>format</i> value is not given, <code>sh</code> is assumed. Only compilation flags starting with an upper case character are included, others are assumed to not be suitable for the environment. Supported formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sh</code></p>
<dd> Shell commands to set and export all the compilation flags in the environment. The flag values are quoted so the output is ready for evaluation by a shell.</p>
<dt><code>cmdline</code></p>
<dd> Arguments to pass to a build program&#8217;s command line to use all the compilation flags (since dpkg 1.17.0). The flag values are quoted in shell syntax.</p>
<dt><code>configure</code></p>
<dd> This is a legacy alias for <code>cmdline</code>.</p>
<dt><code>make</code></p>
<dd> Make directives to set and export all the compilation flags in the environment. Output can be written to a Makefile fragment and evaluated using an <code>include</code> directive.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;get</code> <i>flag</i></p>
<dd> Print the value of the flag on standard output. Exits with 0 if the flag is known otherwise exits with 1.</p>
<dt><code>&#8211;origin</code> <i>flag</i></p>
<dd> Print the origin of the value that is returned by <code>&#8211;get</code>. Exits with 0 if the flag is known otherwise exits with 1. The origin can be one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>vendor</code></p>
<dd> the original flag set by the vendor is returned;</p>
<dt><code>system</code></p>
<dd> the flag is set/modified by a system-wide configuration;</p>
<dt><code>user</code></p>
<dd> the flag is set/modified by a user-specific configuration;</p>
<dt><code>env</code></p>
<dd> the flag is set/modified by an environment-specific configuration.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;query</code></p>
<dd> Print any information that can be useful to explain the behaviour of the program: current vendor, relevant environment variables, feature areas, state of all feature flags, and the compiler flags with their origin (since dpkg 1.19.0). </p>
<p> For example: </p>
<pre>
 Vendor: Debian
 Environment:
  DEB_CFLAGS_SET=-O0 -Wall
 Area: qa
 Features:
  bug=no
  canary=no
 Area: reproducible
 Features:
  timeless=no
 Flag: CFLAGS
 Value: -O0 -Wall
 Origin: env
 Flag: CPPFLAGS
 Value: -D_FORTIFY_SOURCE=2
 Origin: vendor
</pre>
<dt><code>&#8211;query-features</code> <i>area</i></p>
<dd> Print the features enabled for a given area (since dpkg 1.16.2). The only currently recognized areas on Debian and derivatives are <code>future</code>, <code>qa</code>, <code>reproducible</code>, <code>sanitize</code> and <code>hardening</code>, see the <font SIZE="-1"><code>FEATURE AREAS</code></font> section for more details. Exits with 0 if the area is known otherwise exits with 1. </p>
<p> The output is in <font SIZE="-1">RFC822</font> format, with one section per feature. For example: </p>
<pre>
 Feature: pie
 Enabled: yes
 Feature: stackprotector
 Enabled: yes
</pre>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>SUPPORTED FLAGS</h2>
<dl>
<dt><font SIZE="-1"><code>ASFLAGS</code></font></p>
<dd> Options for the assembler. Default value: empty. Since dpkg 1.21.0.</p>
<dt><font SIZE="-1"><code>CFLAGS</code></font></p>
<dd> Options for the C compiler. The default value set by the vendor includes <code>-g</code> and the default optimization level (<code>-O2</code> usually, or <code>-O0</code> if the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable defines <i>noopt</i>).</p>
<dt><font SIZE="-1"><code>CPPFLAGS</code></font></p>
<dd> Options for the C preprocessor. Default value: empty.</p>
<dt><font SIZE="-1"><code>CXXFLAGS</code></font></p>
<dd> Options for the C<font SIZE="-2">++</font> compiler. Same as <font SIZE="-1"><code>CFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>OBJCFLAGS</code></font></p>
<dd> Options for the Objective C compiler. Same as <font SIZE="-1"><code>CFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>OBJCXXFLAGS</code></font></p>
<dd> Options for the Objective C<font SIZE="-2">++</font> compiler. Same as <font SIZE="-1"><code>CXXFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>GCJFLAGS</code></font></p>
<dd> Options for the <font SIZE="-1">GNU</font> Java compiler (gcj). A subset of <font SIZE="-1"><code>CFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>DFLAGS</code></font></p>
<dd> Options for the D compiler (ldc or gdc). Since dpkg 1.20.6.</p>
<dt><font SIZE="-1"><code>FFLAGS</code></font></p>
<dd> Options for the Fortran 77 compiler. A subset of <font SIZE="-1"><code>CFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>FCFLAGS</code></font></p>
<dd> Options for the Fortran 9x compiler. Same as <font SIZE="-1"><code>FFLAGS</code></font>.</p>
<dt><font SIZE="-1"><code>LDFLAGS</code></font></p>
<dd> Options passed to the compiler when linking executables or shared objects (if the linker is called directly, then <code>-Wl</code> and <code>,</code> have to be stripped from these options). Default value: empty.</dl>
<p> New flags might be added in the future if the need arises (for example to support other languages).</p>
<h2>FEATURE AREAS</h2>
<p> Each area feature can be enabled and disabled in the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> and <font SIZE="-1"><code>DEB_BUILD_MAINT_OPTIONS</code></font> environment variable&#8217;s area value with the &#8216;<code>+</code>&#8216; and &#8216;<code>&#8211;</code>&#8216; modifier. For example, to enable the <code>hardening</code> &#8220;pie&#8221; feature and disable the &#8220;fortify&#8221; feature you can do this in <code>debian/rules</code>: </p>
<pre>
    export DEB_BUILD_MAINT_OPTIONS=hardening=+pie,-fortify
</pre>
<p> The special feature <code>all</code> (valid in any area) can be used to enable or disable all area features at the same time. Thus disabling everything in the <code>hardening</code> area and enabling only &#8220;format&#8221; and &#8220;fortify&#8221; can be achieved with: </p>
<pre>
    export DEB_BUILD_MAINT_OPTIONS=hardening=-all,+format,+fortify
</pre>
<h3>future</h3>
<p> Several compile-time options (detailed below) can be used to enable features that should be enabled by default, but cannot due to backwards compatibility reasons.</p>
<dl>
<dt><code>lfs</code></p>
<dd> This setting (disabled by default) enables Large File Support on 32-bit architectures where their <font SIZE="-1">ABI</font> does not include <font SIZE="-1">LFS</font> by default, by adding <code>-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64</code> to <font SIZE="-1"><code>CPPFLAGS</code></font>.</dl>
<h3>qa</h3>
<p> Several compile-time options (detailed below) can be used to help detect problems in the source code or build system.</p>
<dl>
<dt><code>bug</code></p>
<dd> This setting (disabled by default) adds any warning option that reliably detects problematic source code. The warnings are fatal. The only currently supported flags are <font SIZE="-1"><code>CFLAGS</code></font> and <font SIZE="-1"><code>CXXFLAGS</code></font> with flags set to <code>-Werror=array-bounds</code>, <code>-Werror=clobbered</code>, <code>-Werror=implicit-function-declaration</code> and <code>-Werror=volatile-register-var</code>.</p>
<dt><code>canary</code></p>
<dd> This setting (disabled by default) adds dummy canary options to the build flags, so that the build logs can be checked for how the build flags propagate and to allow finding any omission of normal build flag settings. The only currently supported flags are <font SIZE="-1"><code>CPPFLAGS</code></font>, <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font> and <font SIZE="-1"><code>OBJCXXFLAGS</code></font> with flags set to <code>-D__DEB_CANARY_</code><i>flag</i>_<i>random-id</i><code>__</code>, and <font SIZE="-1"><code>LDFLAGS</code></font> set to <code>-Wl,-z,deb-canary-</code><i>random-id</i>.</dl>
<h3>optimize</h3>
<p> Several compile-time options (detailed below) can be used to help optimize a resulting binary (since dpkg 1.21.0). <code>Note</code>: enabling <code>all</code> these options can result in unreproducible binary artifacts.</p>
<dl>
<dt>lto</p>
<dd> This setting (since dpkg 1.21.0; disabled by default) enables Link Time Optimization by adding <code>-flto=auto -ffat-lto-objects</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font>, <font SIZE="-1"><code>FCFLAGS</code></font> and <font SIZE="-1"><code>LDFLAGS</code></font>.</dl>
<h3>optimize</h3>
<p> Several compile-time options (detailed below) can be used to help optimize a resulting binary (since dpkg 1.21.0). <code>Note</code>: enabling <code>all</code> these options can result in unreproducible binary artifacts.</p>
<dl>
<dt>lto</p>
<dd> This setting (since dpkg 1.21.0; disabled by default) enables Link Time Optimization by adding <code>-flto=auto -ffat-lto-objects</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font>.</dl>
<h3>sanitize</h3>
<p> Several compile-time options (detailed below) can be used to help sanitize a resulting binary against memory corruptions, memory leaks, use after free, threading data races and undefined behavior bugs. <code>Note</code>: these options should <code>not</code> be used for production builds as they can reduce reliability for conformant code, reduce security or even functionality.</p>
<dl>
<dt><code>address</code></p>
<dd> This setting (disabled by default) adds <code>-fsanitize=address</code> to <font SIZE="-1"><code>LDFLAGS</code></font> and <code>-fsanitize=address -fno-omit-frame-pointer</code> to <font SIZE="-1"><code>CFLAGS</code></font> and <font SIZE="-1"><code>CXXFLAGS</code></font>.</p>
<dt><code>thread</code></p>
<dd> This setting (disabled by default) adds <code>-fsanitize=thread</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font> and <font SIZE="-1"><code>LDFLAGS</code></font>.</p>
<dt><code>leak</code></p>
<dd> This setting (disabled by default) adds <code>-fsanitize=leak</code> to <font SIZE="-1"><code>LDFLAGS</code></font>. It gets automatically disabled if either the <code>address</code> or the <code>thread</code> features are enabled, as they imply it.</p>
<dt><code>undefined</code></p>
<dd> This setting (disabled by default) adds <code>-fsanitize=undefined</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font> and <font SIZE="-1"><code>LDFLAGS</code></font>.</dl>
<h3>hardening</h3>
<p> Several compile-time options (detailed below) can be used to help harden a resulting binary against memory corruption attacks, or provide additional warning messages during compilation. Except as noted below, these are enabled by default for architectures that support them.</p>
<dl>
<dt><code>format</code></p>
<dd> This setting (enabled by default) adds <code>-Wformat -Werror=format-security</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font> and <font SIZE="-1"><code>OBJCXXFLAGS</code></font>. This will warn about improper format string uses, and will fail when format functions are used in a way that represent possible security problems. At present, this warns about calls to <code>printf</code> and <code>scanf</code> functions where the format string is not a string literal and there are no format arguments, as in <code>printf(foo);</code> instead of <code>printf(&#8220;%s&#8221;, foo);</code> This may be a security hole if the format string came from untrusted input and contains &#8216;%n&#8217;.</p>
<dt><code>fortify</code></p>
<dd> This setting (enabled by default) adds <code>-D_FORTIFY_SOURCE=2</code> to <font SIZE="-1"><code>CPPFLAGS</code></font>. During code generation the compiler knows a great deal of information about buffer sizes (where possible), and attempts to replace insecure unlimited length buffer function calls with length-limited ones. This is especially useful for old, crufty code. Additionally, format strings in writable memory that contain &#8216;%n&#8217; are blocked. If an application depends on such a format string, it will need to be worked around. </p>
<p> Note that for this option to have any effect, the source must also be compiled with <code>-O1</code> or higher. If the environment variable <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> contains <i>noopt</i>, then <code>fortify</code> support will be disabled, due to new warnings being issued by glibc 2.16 and later.</p>
<dt><code>stackprotector</code></p>
<dd> This setting (enabled by default if stackprotectorstrong is not in use) adds <code>-fstack-protector &#8211;param=ssp-buffer-size=4</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font>. This adds safety checks against stack overwrites. This renders many potential code injection attacks into aborting situations. In the best case this turns code injection vulnerabilities into denial of service or into non-issues (depending on the application). </p>
<p> This feature requires linking against glibc (or another provider of <code>__stack_chk_fail</code>), so needs to be disabled when building with <code>-nostdlib</code> or <code>-ffreestanding</code> or similar.</p>
<dt><code>stackprotectorstrong</code></p>
<dd> This setting (enabled by default) adds <code>-fstack-protector-strong</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font>. This is a stronger variant of <code>stackprotector</code>, but without significant performance penalties. </p>
<p> Disabling <code>stackprotector</code> will also disable this setting. </p>
<p> This feature has the same requirements as <code>stackprotector</code>, and in addition also requires gcc 4.9 and later.</p>
<dt><code>relro</code></p>
<dd> This setting (enabled by default) adds <code>-Wl,-z,relro</code> to <font SIZE="-1"><code>LDFLAGS</code></font>. During program load, several <font SIZE="-1">ELF</font> memory sections need to be written to by the linker. This flags the loader to turn these sections read-only before turning over control to the program. Most notably this prevents <font SIZE="-1">GOT</font> overwrite attacks. If this option is disabled, <code>bindnow</code> will become disabled as well.</p>
<dt><code>bindnow</code></p>
<dd> This setting (disabled by default) adds <code>-Wl,-z,now</code> to <font SIZE="-1"><code>LDFLAGS</code></font>. During program load, all dynamic symbols are resolved, allowing for the entire <font SIZE="-1">PLT</font> to be marked read-only (due to <code>relro</code> above). The option cannot become enabled if <code>relro</code> is not enabled.</p>
<dt><code>pie</code></p>
<dd> This setting (with no global default since dpkg 1.18.23, as it is enabled by default now by gcc on the amd64, arm64, armel, armhf, hurd-i386, i386, kfreebsd-amd64, kfreebsd-i386, mips, mipsel, mips64el, powerpc, ppc64, ppc64el, riscv64, s390x, sparc and sparc64 Debian architectures) adds the required options to enable or disable <font SIZE="-1">PIE</font> via gcc specs files, if needed, depending on whether gcc injects on that architecture the flags by itself or not. When the setting is enabled and gcc injects the flags, it adds nothing. When the setting is enabled and gcc does not inject the flags, it adds <code>-fPIE</code> (via <i>/usr/share/dpkg/pie-compiler.specs</i>) to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font>, and <code>-fPIE -pie</code> (via <i>/usr/share/dpkg/pie-link.specs</i>) to <font SIZE="-1"><code>LDFLAGS</code></font>. When the setting is disabled and gcc injects the flags, it adds <code>-fno-PIE</code> (via <i>/usr/share/dpkg/no-pie-compile.specs</i>) to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font>, and <code>-fno-PIE -no-pie</code> (via <i>/usr/share/dpkg/no-pie-link.specs</i>) to <font SIZE="-1"><code>LDFLAGS</code></font>. </p>
<p> Position Independent Executable are needed to take advantage of Address Space Layout Randomization, supported by some kernel versions. While <font SIZE="-1">ASLR</font> can already be enforced for data areas in the stack and heap (brk and mmap), the code areas must be compiled as position-independent. Shared libraries already do this (<code>-fPIC</code>), so they gain <font SIZE="-1">ASLR</font> automatically, but binary .text regions need to be build <font SIZE="-1">PIE</font> to gain <font SIZE="-1">ASLR.</font> When this happens, <font SIZE="-1">ROP</font> (Return Oriented Programming) attacks are much harder since there are no static locations to bounce off of during a memory corruption attack. </p>
<p> <font SIZE="-1">PIE</font> is not compatible with <code>-fPIC</code>, so in general care must be taken when building shared objects. But because the <font SIZE="-1">PIE</font> flags emitted get injected via gcc specs files, it should always be safe to unconditionally set them regardless of the object type being compiled or linked. </p>
<p> Static libraries can be used by programs or other shared libraries. Depending on the flags used to compile all the objects within a static library, these libraries will be usable by different sets of objects:</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> Cannot be linked into a <font SIZE="-1">PIE</font> program, nor a shared library.</p>
<dt><code>-fPIE</code></p>
<dd> Can be linked into any program, but not a shared library (recommended).</p>
<dt><code>-fPIC</code></p>
<dd> Can be linked into any program and shared library.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If there is a need to set these flags manually, bypassing the gcc specs injection, there are several things to take into account. Unconditionally and explicitly passing <code>-fPIE</code>, <code>-fpie</code> or <code>-pie</code> to a build-system using libtool is safe as these flags will get stripped when building shared libraries. Otherwise on projects that build both programs and shared libraries you might need to make sure that when building the shared libraries <code>-fPIC</code> is always passed last (so that it overrides any previous <code>-PIE</code>) to compilation flags such as <font SIZE="-1"><code>CFLAGS</code></font>, and <code>-shared</code> is passed last (so that it overrides any previous <code>-pie</code>) to linking flags such as <font SIZE="-1"><code>LDFLAGS</code></font>. <code>Note:</code> This should not be needed with the default gcc specs machinery. </p>
<p> Additionally, since <font SIZE="-1">PIE</font> is implemented via a general register, some register starved architectures (but not including i386 anymore since optimizations implemented in gcc &gt;= 5) can see performance losses of up to 15% in very text-segment-heavy application workloads; most workloads see less than 1%. Architectures with more general registers (e.g. amd64) do not see as high a worst-case penalty.</dl>
</dl>
<h3>reproducible</h3>
<p> The compile-time options detailed below can be used to help improve build reproducibility or provide additional warning messages during compilation. Except as noted below, these are enabled by default for architectures that support them.</p>
<dl>
<dt><code>timeless</code></p>
<dd> This setting (enabled by default) adds <code>-Wdate-time</code> to <font SIZE="-1"><code>CPPFLAGS</code></font>. This will cause warnings when the <code>__TIME__</code>, <code>__DATE__</code> and <code>__TIMESTAMP__</code> macros are used.</p>
<dt><code>fixfilepath</code></p>
<dd> This setting (enabled by default) adds <code>-ffile-prefix-map=</code><i></i><font SIZE="-1"><i>BUILDPATH</i></font><i></i><code>=.</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font> where <font SIZE="-1"><code>BUILDPATH</code></font> is set to the top-level directory of the package being built. This has the effect of removing the build path from any generated file. </p>
<p> If both <code>fixdebugpath</code> and <code>fixfilepath</code> are set, this option takes precedence, because it is a superset of the former.</p>
<dt><code>fixdebugpath</code></p>
<dd> This setting (enabled by default) adds <code>-fdebug-prefix-map=</code><i></i><font SIZE="-1"><i>BUILDPATH</i></font><i></i><code>=.</code> to <font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>OBJCFLAGS</code></font>, <font SIZE="-1"><code>OBJCXXFLAGS</code></font>, <font SIZE="-1"><code>GCJFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font> and <font SIZE="-1"><code>FCFLAGS</code></font> where <font SIZE="-1"><code>BUILDPATH</code></font> is set to the top-level directory of the package being built. This has the effect of removing the build path from any generated debug symbols.</dl>
<h2>ENVIRONMENT</h2>
<p> There are 2 sets of environment variables doing the same operations, the first one (<font SIZE="-1">DEB_</font><i>flag</i>_<i>op</i>) should never be used within <code>debian/rules</code>. It&#8217;s meant for any user that wants to rebuild the source package with different build flags. The second set (<font SIZE="-1">DEB_</font><i>flag</i>_MAINT_<i>op</i>) should only be used in <code>debian/rules</code> by package maintainers to change the resulting build flags.</p>
<dl>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_SET</code></p>
<dd>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_MAINT_SET</code></p>
<dd> This variable can be used to force the value returned for the given <i>flag</i>.</p>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_STRIP</code></p>
<dd>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_MAINT_STRIP</code></p>
<dd> This variable can be used to provide a space separated list of options that will be stripped from the set of flags returned for the given <i>flag</i>.</p>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_APPEND</code></p>
<dd>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_MAINT_APPEND</code></p>
<dd> This variable can be used to append supplementary options to the value returned for the given <i>flag</i>.</p>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_PREPEND</code></p>
<dd>
<dt><font SIZE="-1"><code>DEB_</code></font><i>flag</i><code>_MAINT_PREPEND</code></p>
<dd> This variable can be used to prepend supplementary options to the value returned for the given <i>flag</i>.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font></p>
<dd>
<dt><font SIZE="-1"><code>DEB_BUILD_MAINT_OPTIONS</code></font></p>
<dd> These variables can be used by a user or maintainer to disable/enable various area features that affect build flags. The <font SIZE="-1"><code>DEB_BUILD_MAINT_OPTIONS</code></font> variable overrides any setting in the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> feature areas. See the <font SIZE="-1"><code>FEATURE AREAS</code></font> section for details.</p>
<dt><font SIZE="-1"><code>DEB_VENDOR</code></font></p>
<dd> This setting defines the current vendor. If not set, it will discover the current vendor by reading <code>/etc/dpkg/origins/default</code>.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_PATH</code></font></p>
<dd> This variable sets the build path (since dpkg 1.18.8) to use in features such as <code>fixdebugpath</code> so that they can be controlled by the caller. This variable is currently Debian and derivatives-specific.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>FILES</h2>
<h3>Configuration files</h3>
<dl>
<dt><code>/etc/dpkg/buildflags.conf</code></p>
<dd> System wide configuration file.</p>
<dt>$XDG_CONFIG_HOME<code>/dpkg/buildflags.conf</code> or</p>
<dd>
<dt>$HOME<code>/.config/dpkg/buildflags.conf</code></p>
<dd> User configuration file.</dl>
<h3>Packaging support</h3>
<dl>
<dt><code>/usr/share/dpkg/buildflags.mk</code></p>
<dd> Makefile snippet that will load (and optionally export) all flags supported by <code>dpkg-buildflags</code> into variables (since dpkg 1.16.1).</dl>
<h2>EXAMPLES</h2>
<p> To pass build flags to a build command in a Makefile: </p>
<pre>
 $(MAKE) $(shell dpkg-buildflags --export=cmdline)
 ./configure $(shell dpkg-buildflags --export=cmdline)
</pre>
<p> To set build flags in a shell script or shell fragment, <code>eval</code> can be used to interpret the output and to export the flags in the environment: </p>
<pre>
 eval &quot;$(dpkg-buildflags --export=sh)&quot; &amp;&amp; make
</pre>
<p> or to set the positional parameters to pass to a command: </p>
<pre><code>
 eval "set -- $(dpkg-buildflags --export=cmdline)"
 for dir in a b c;
 do
     (cd $dir &amp;&amp;./ configure "$@" &amp;&amp; make);
 done
</code></pre>
<h3>Usage in debian/rules</h3>
<p> You should call <code>dpkg-buildflags</code> or include <code>buildflags.mk</code> from the <code>debian/rules</code> file to obtain the needed build flags to pass to the build system. Note that older versions of <code>dpkg-buildpackage</code> (before dpkg 1.16.1) exported these flags automatically. However, you should not rely on this, since this breaks manual invocation of <code>debian/rules</code>. </p>
<p> For packages with autoconf-like build systems, you can pass the relevant options to configure or <code><a href="/docs/linux/man/1-make/">make</a></code>(1) directly, as shown above. </p>
<p> For other build systems, or when you need more fine-grained control about which flags are passed where, you can use <code>&#8211;get</code>. Or you can include <code>buildflags.mk</code> instead, which takes care of calling <code>dpkg-buildflags</code> and storing the build flags in make variables. </p>
<p> If you want to export all buildflags into the environment (where they can be picked up by your build system): </p>
<pre>
 DPKG_EXPORT_BUILDFLAGS = 1
 include /usr/share/dpkg/buildflags.mk
</pre>
<p> For some extra control over what is exported, you can manually export the variables (as none are exported by default): </p>
<pre>
 include /usr/share/dpkg/buildflags.mk
 export CPPFLAGS CFLAGS LDFLAGS
</pre>
<p> And you can of course pass the flags to commands manually: </p>
<pre>
 include /usr/share/dpkg/buildflags.mk
 build-arch:
        $(CC) -o hello hello.c $(CPPFLAGS) $(CFLAGS) $(LDFLAGS)
</pre>
<h2>Index</h2>
