---
title: "dpkg-architecture(1)"
name: "dpkg-architecture"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-architecture/"
description: "dpkg-architecture – set and determine the architecture for package building"
---

<h2 class="name">NAME</h2>
<p> dpkg-architecture &#8211; set and determine the architecture for package building </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-architecture</code> [<i>option</i>&#8230;] [<i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-architecture</code> provides a facility to determine and set the build and host architecture for package building. </p>
<p> The build architecture is always determined by either the <font SIZE="-1"><code>DEB_BUILD_ARCH</code></font> variable if set (and <code>&#8211;force</code> not being specified) or by an external call to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), and cannot be set at the command line. </p>
<p> You can specify the host architecture by providing one or both of the options <code>&#8211;host-arch</code> and <code>&#8211;host-type</code>, otherwise the <font SIZE="-1"><code>DEB_HOST_ARCH</code></font> variable is used if set (and <code>&#8211;force</code> not being specified). The default is determined by an external call to <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), or the same as the build architecture if <font SIZE="-1"><code>CC</code></font> or gcc are both not available. One out of <code>&#8211;host-arch</code> and <code>&#8211;host-type</code> is sufficient, the value of the other will be set to a usable default. Indeed, it is often better to only specify one, because <code>dpkg-architecture</code> will warn you if your choice does not match the default.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Print the environment variables, one each line, in the format <i>VARIABLE=value</i>. This is the default action.</p>
<dt><code>-e</code>, <code>&#8211;equal</code> <i>architecture</i></p>
<dd> Check for equality of architecture (since dpkg 1.13.13). It compares the current or specified Debian host architecture against <i>architecture</i>, to check if they are equal. This action will not expand the architecture wildcards. Command finishes with an exit status of 0 if matched, 1 if not matched.</p>
<dt><code>-i</code>, <code>&#8211;is</code> <i>architecture-wildcard</i></p>
<dd> Check for identity of architecture (since dpkg 1.13.13). It compares the current or specified Debian host architecture against <i>architecture-wildcard</i> after having expanded it as an architecture wildcard, to check if they match. Command finishes with an exit status of 0 if matched, 1 if not matched.</p>
<dt><code>-q</code>, <code>&#8211;query</code> <i>variable-name</i></p>
<dd> Print the value of a single variable.</p>
<dt><code>-s</code>, <code>&#8211;print-set</code></p>
<dd> Print an export command. This can be used to set the environment variables using the <font SIZE="-1">POSIX</font> shell or make <code>eval</code>, depending on the output format.</p>
<dt><code>-u</code>, <code>&#8211;print-unset</code></p>
<dd> Print a similar command to <code>&#8211;print-set</code> but to unset all variables.</p>
<dt><code>-c</code>, <code>&#8211;command</code> <i>command-string</i></p>
<dd> Execute a <i>command-string</i> in an environment which has all variables set to the determined value.</p>
<dt><code>-L</code>, <code>&#8211;list-known</code></p>
<dd> Print a list of valid architecture names. Possibly restricted by one or more of the matching options <code>&#8211;match-wildcard</code>, <code>&#8211;match-bits</code> or <code>&#8211;match-endian</code> (since dpkg 1.17.14).</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;host-arch</code> <i>architecture</i></p>
<dd> Set the host Debian architecture.</p>
<dt><code>-t</code>, <code>&#8211;host-type</code> <i>gnu-system-type</i></p>
<dd> Set the host <font SIZE="-1">GNU</font> system type.</p>
<dt><code>-A</code>, <code>&#8211;target-arch</code> <i>architecture</i></p>
<dd> Set the target Debian architecture (since dpkg 1.17.14).</p>
<dt><code>-T</code>, <code>&#8211;target-type</code> <i>gnu-system-type</i></p>
<dd> Set the target <font SIZE="-1">GNU</font> system type (since dpkg 1.17.14).</p>
<dt><code>-W</code>, <code>&#8211;match-wildcard</code> <i>architecture-wildcard</i></p>
<dd> Restrict the architectures listed by <code>&#8211;list-known</code> to ones matching the specified architecture wildcard (since dpkg 1.17.14).</p>
<dt><code>-B</code>, <code>&#8211;match-bits</code> <i>architecture-bits</i></p>
<dd> Restrict the architectures listed by <code>&#8211;list-known</code> to ones with the specified <font SIZE="-1">CPU</font> bits (since dpkg 1.17.14). Either <code>32</code> or <code>64</code>.</p>
<dt><code>-E</code>, <code>&#8211;match-endian</code> <i>architecture-endianness</i></p>
<dd> Restrict the architectures listed by <code>&#8211;list-known</code> to ones with the specified endianness (since dpkg 1.17.14). Either <code>little</code> or <code>big</code>.</p>
<dt><code>&#8211;print-format</code> <i>format</i></p>
<dd> Sets the output format for <code>&#8211;print-set</code> and <code>&#8211;print-unset</code> (since dpkg 1.20.6), to either <code>shell</code> (default) or <code>make</code>.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Values set by existing environment variables with the same name as used by the scripts are honored (i.e. used by <code>dpkg-architecture</code>), except if this force flag is present. This allows the user to override a value even when the call to <code>dpkg-architecture</code> is buried in some other script (for example <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1)).</dl>
<h2>TERMS</h2>
<dl>
<dt>build machine</p>
<dd> The machine the package is built on.</p>
<dt>host machine</p>
<dd> The machine the package is built for.</p>
<dt>target machine</p>
<dd> The machine the compiler is building for, or the emulator will run code for. This is only needed when building a cross-toolchain (or emulator), one that will be built on the build architecture, to be run on the host architecture, and to build (or run emulated) code for the target architecture.</p>
<dt>Debian architecture</p>
<dd> The Debian architecture string, which specifies the binary tree in the <font SIZE="-1">FTP</font> archive. Examples: i386, sparc, hurd-i386.</p>
<dt>Debian architecture tuple</p>
<dd> A Debian architecture tuple is the fully qualified architecture with all its components spelled out. This differs with Debian architectures in that at least the <i>cpu</i> component does not embed the <i>abi</i>. The current tuple has the form <i>abi</i>&#8211;<i>libc</i>&#8211;<i>os</i>&#8211;<i>cpu</i>. Examples: base-gnu-linux-amd64, eabihf-musl-linux-arm.</p>
<dt>Debian architecture wildcard</p>
<dd> A Debian architecture wildcard is a special architecture string that will match any real architecture being part of it. The general form is a Debian architecture tuple with four or less elements, and with at least one of them being <code>any</code>. Missing elements of the tuple are prefixed implicitly as <code>any</code>, and thus the following pairs are equivalent:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>any</code>&#8211;<code>any</code>&#8211;<code>any</code>&#8211;<code>any</code> = <code>any</code></p>
<dd>
<dt><code>any</code>&#8211;<code>any</code>&#8211;<i>os</i>&#8211;<code>any</code> = <i>os</i>&#8211;<code>any</code></p>
<dd>
<dt><code>any</code>&#8211;<i>libc</i>&#8211;<code>any</code>&#8211;<code>any</code> = <i>libc</i>&#8211;<code>any</code>&#8211;<code>any</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples: linux-any, any-i386, hurd-any, eabi-any-any-arm, musl-any-any.</dl>
<dt><font SIZE="-1">GNU</font> system type</p>
<dd> An architecture specification string consisting of two parts separated by a hyphen: cpu and system. Examples: i586-linux-gnu, sparc-linux-gnu, i686-gnu, x86_64-netbsd.</p>
<dt>multiarch triplet</p>
<dd> The clarified <font SIZE="-1">GNU</font> system type, used for filesystem paths. This triplet does not change even when the baseline <font SIZE="-1">ISA</font> gets bumped, so that the resulting paths are stable over time. The only current difference with the <font SIZE="-1">GNU</font> system type is that the <font SIZE="-1">CPU</font> part for i386 based systems is always i386. Examples: i386-linux-gnu, x86_64-linux-gnu. Example paths: /lib/powerpc64le-linux-gnu/, /usr/lib/i386-kfreebsd-gnu/.</dl>
<h2>VARIABLES</h2>
<p> The following variables are read from the environment (unless <code>&#8211;force</code> has been specified) and set by <code>dpkg-architecture</code> (see the <font SIZE="-1"><code>TERMS</code></font> section for a description of the naming scheme):</p>
<dl>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH</code></font></p>
<dd> The Debian architecture of the build machine.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_ABI</code></font></p>
<dd> The Debian <font SIZE="-1">ABI</font> name of the build machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_LIBC</code></font></p>
<dd> The Debian libc name of the build machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_OS</code></font></p>
<dd> The Debian system name of the build machine (since dpkg 1.13.2).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_CPU</code></font></p>
<dd> The Debian <font SIZE="-1">CPU</font> name of the build machine (since dpkg 1.13.2).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_BITS</code></font></p>
<dd> The pointer size of the build machine (in bits; since dpkg 1.15.4).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_ARCH_ENDIAN</code></font></p>
<dd> The endianness of the build machine (little / big; since dpkg 1.15.4).</p>
<dt><font SIZE="-1"><code>DEB_BUILD_GNU_CPU</code></font></p>
<dd> The <font SIZE="-1">GNU CPU</font> part of <font SIZE="-1"><code>DEB_BUILD_GNU_TYPE</code></font>.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_GNU_SYSTEM</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system part of <font SIZE="-1"><code>DEB_BUILD_GNU_TYPE</code></font>.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_GNU_TYPE</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system type of the build machine.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_MULTIARCH</code></font></p>
<dd> The clarified <font SIZE="-1">GNU</font> system type of the build machine, used for filesystem paths (since dpkg 1.16.0).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH</code></font></p>
<dd> The Debian architecture of the host machine.</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_ABI</code></font></p>
<dd> The Debian <font SIZE="-1">ABI</font> name of the host machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_LIBC</code></font></p>
<dd> The Debian libc name of the host machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_OS</code></font></p>
<dd> The Debian system name of the host machine (since dpkg 1.13.2).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_CPU</code></font></p>
<dd> The Debian <font SIZE="-1">CPU</font> name of the host machine (since dpkg 1.13.2).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_BITS</code></font></p>
<dd> The pointer size of the host machine (in bits; since dpkg 1.15.4).</p>
<dt><font SIZE="-1"><code>DEB_HOST_ARCH_ENDIAN</code></font></p>
<dd> The endianness of the host machine (little / big; since dpkg 1.15.4).</p>
<dt><font SIZE="-1"><code>DEB_HOST_GNU_CPU</code></font></p>
<dd> The <font SIZE="-1">GNU CPU</font> part of <font SIZE="-1"><code>DEB_HOST_GNU_TYPE</code></font>.</p>
<dt><font SIZE="-1"><code>DEB_HOST_GNU_SYSTEM</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system part of <font SIZE="-1"><code>DEB_HOST_GNU_TYPE</code></font>.</p>
<dt><font SIZE="-1"><code>DEB_HOST_GNU_TYPE</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system type of the host machine.</p>
<dt><font SIZE="-1"><code>DEB_HOST_MULTIARCH</code></font></p>
<dd> The clarified <font SIZE="-1">GNU</font> system type of the host machine, used for filesystem paths (since dpkg 1.16.0).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH</code></font></p>
<dd> The Debian architecture of the target machine (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_ABI</code></font></p>
<dd> The Debian <font SIZE="-1">ABI</font> name of the target machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_LIBC</code></font></p>
<dd> The Debian libc name of the target machine (since dpkg 1.18.11).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_OS</code></font></p>
<dd> The Debian system name of the target machine (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_CPU</code></font></p>
<dd> The Debian <font SIZE="-1">CPU</font> name of the target machine (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_BITS</code></font></p>
<dd> The pointer size of the target machine (in bits; since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_ARCH_ENDIAN</code></font></p>
<dd> The endianness of the target machine (little / big; since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_GNU_CPU</code></font></p>
<dd> The <font SIZE="-1">GNU CPU</font> part of <font SIZE="-1"><code>DEB_TARGET_GNU_TYPE</code></font> (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_GNU_SYSTEM</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system part of <font SIZE="-1"><code>DEB_TARGET_GNU_TYPE</code></font> (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_GNU_TYPE</code></font></p>
<dd> The <font SIZE="-1">GNU</font> system type of the target machine (since dpkg 1.17.14).</p>
<dt><font SIZE="-1"><code>DEB_TARGET_MULTIARCH</code></font></p>
<dd> The clarified <font SIZE="-1">GNU</font> system type of the target machine, used for filesystem paths (since dpkg 1.17.14).</dl>
<h2>FILES</h2>
<h3>Architecture tables</h3>
<p> All these files have to be present for <code>dpkg-architecture</code> to work. Their location can be overridden at runtime with the environment variable <font SIZE="-1"><code>DPKG_DATADIR</code></font>. These tables contain a format <code>Version</code> pseudo-field on their first line to mark their format, so that parsers can check if they understand it, such as &#8220;# Version=1.0&#8221;.</p>
<dl>
<dt><i>/usr/share/dpkg/cputable</i></p>
<dd> Table of known <font SIZE="-1">CPU</font> names and mapping to their <font SIZE="-1">GNU</font> name. Format version 1.0 (since dpkg 1.13.2).</p>
<dt><i>/usr/share/dpkg/ostable</i></p>
<dd> Table of known operating system names and mapping to their <font SIZE="-1">GNU</font> name. Format version 2.0 (since dpkg 1.18.11).</p>
<dt><i>/usr/share/dpkg/tupletable</i></p>
<dd> Mapping between Debian architecture tuples and Debian architecture names. Format version 1.0 (since dpkg 1.18.11).</p>
<dt><i>/usr/share/dpkg/abitable</i></p>
<dd> Table of Debian architecture <font SIZE="-1">ABI</font> attribute overrides. Format version 2.0 (since dpkg 1.18.11).</dl>
<h3>Packaging support</h3>
<dl>
<dt><i>/usr/share/dpkg/architecture.mk</i></p>
<dd> Makefile snippet that properly sets and exports all the variables that <code>dpkg-architecture</code> outputs (since dpkg 1.16.1).</dl>
<h2>EXAMPLES</h2>
<p> <code>dpkg-buildpackage</code> accepts the <code>-a</code> option and passes it to <code>dpkg-architecture</code>. Other examples: </p>
<pre>
 CC=i386-gnu-gcc dpkg-architecture -c debian/rules build
 eval $(dpkg-architecture -u)
</pre>
<p> Check if the current or specified host architecture is equal to an architecture: </p>
<pre>
 dpkg-architecture -elinux-alpha
 dpkg-architecture -amips -elinux-mips
</pre>
<p> Check if the current or specified host architecture is a Linux system: </p>
<pre>
 dpkg-architecture -ilinux-any
 dpkg-architecture -ai386 -ilinux-any
</pre>
<h3>Usage in debian/rules</h3>
<p> The environment variables set by <code>dpkg-architecture</code> are passed to <i>debian/rules</i> as make variables (see make documentation). However, you should not rely on them, as this breaks manual invocation of the script. Instead, you should always initialize them using <code>dpkg-architecture</code> with the <code>-q</code> option. Here are some examples, which also show how you can improve the cross compilation support in your package: </p>
<p> Retrieving the <font SIZE="-1">GNU</font> system type and forwarding it to ./configure: </p>
<pre><code>
DEB_BUILD_GNU_TYPE ? = $(shell dpkg - architecture - qDEB_BUILD_GNU_TYPE)
                         DEB_HOST_GNU_TYPE
                     ? = $(shell dpkg - architecture - qDEB_HOST_GNU_TYPE)
                           [...] ifeq($(DEB_BUILD_GNU_TYPE), $(DEB_HOST_GNU_TYPE))
                               confflags += --build = $(DEB_HOST_GNU_TYPE) else confflags += --build = $(DEB_BUILD_GNU_TYPE)-- host = $(DEB_HOST_GNU_TYPE)
                                                                                                                                          endif
                                                                                                                                              [...]
                                                                                                                                                  ./
                                                                                                                                      configure $(confflags)
</code></pre>
<p> Doing something only for a specific architecture: </p>
<pre>
 DEB_HOST_ARCH ?= $(shell dpkg-architecture -qDEB_HOST_ARCH)
 ifeq ($(DEB_HOST_ARCH),alpha)
   [...]
 endif
</pre>
<p> or if you only need to check the <font SIZE="-1">CPU</font> or <font SIZE="-1">OS</font> type, use the <font SIZE="-1"><code>DEB_HOST_ARCH_CPU</code></font> or <font SIZE="-1"><code>DEB_HOST_ARCH_OS</code></font> variables. </p>
<p> Note that you can also rely on an external Makefile snippet to properly set all the variables that <code>dpkg-architecture</code> can provide: </p>
<pre><code>
include / usr / share / dpkg / architecture.mk ifeq($(DEB_HOST_ARCH), alpha)[...] endif
</code></pre>
<p> In any case, you should never use <code>dpkg &#8211;print-architecture</code> to get architecture information during a package build.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_DATADIR</code></font></p>
<dd> If set, it will be used as the <code>dpkg</code> data directory, where the architecture tables are located (since dpkg 1.14.17). Defaults to &laquo;/usr/share/dpkg&raquo;.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>NOTES</h2>
<p> All long command and option names available only since dpkg 1.17.17.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1). </p>
<h2>Index</h2>
