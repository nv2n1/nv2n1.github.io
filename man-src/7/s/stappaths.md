---
title: "stappaths(7)"
name: "stappaths"
section: "7"
letter: "s"
url: "/docs/linux/man/7-stappaths/"
description: "stappaths – systemtap configurable file paths"
---

<p>stappaths &#8211; systemtap configurable file paths </p>
<h2>Description</h2>
<p>This manual page was generated on 2017-08-03 for systemtap 3.1. The following section will list the main paths in systemtap that are important to know and may be required to reference.</p>
<dl>
<dt>/usr/share/systemtap/tapset/</p>
<dd>The directory for the standard probe-alias / function tapset library, unless overridden by the <i>SYSTEMTAP_TAPSET</i> environment variable or the <i>XDG_DATA_DIRS</i> environment variable. These are described in the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap), <i>probe::*</i>(3stap), and <i>function::*</i>(3stap) manual pages.</p>
<dt>/usr/share/systemtap/runtime/</p>
<dd>The runtime sources, unless overridden by the <i>SYSTEMTAP_RUNTIME</i> environment variable.</p>
<dt>/usr/bin/staprun</p>
<dd>The auxiliary program supervising module loading, interaction, and unloading.</p>
<dt>/usr/libexec/systemtap/stapio</p>
<dd>The auxiliary program for module input and output handling.</p>
<dt>/usr/include/sys/sdt.h</p>
<dd>Location of the &lt;sys/sdt.h&gt; headers.</p>
<dt>Kernel debuginfo Path: /usr/lib/debug/lib/modules/$(uname -r)/</p>
<dd>The location of kernel debugging information when packaged into the <i>kernel-debuginfo</i> RPM, unless overridden by the <i>SYSTEMTAP_DEBUGINFO_PATH</i> environment variable. The default value for this variable is <i>+:.debug:/usr/lib/debug:build</i>. elfutils searches vmlinux in this path and it interprets the path as a base directory of which various subdirectories will be searched for finding debuginfo for the kernel, kernel modules, and user-space binaries. By default, systemtap will also look for vmlinux in these locations: </p>
<dl>
<dd>
<pre>/boot/vmlinux-`uname -r` 
/lib/modules/`uname -r`/vmlinux
/lib/modules/`uname -r`/vmlinux.debug
/lib/modules/`uname -r`/build/vmlinux
/lib/modules/`uname -r`/.debug/vmlinux.debug
/usr/lib/debug/lib/modules/`uname -r`/vmlinux.debug
/var/cache/abrt-di/usr/debug/lib/modules/`uname -r`/
/var/cache/abrt-di/usr/lib/debug/lib/modules/`uname -r`/vmlinux.debug</pre>
</dl>
<dd>Corresponding source files are usually located under /usr/src/debug/. Further file information on user-space applications can be determined per-basis using rpm -ql &lt;package&gt;-debuginfo. For supported user-space applications information please visit the systemtap wiki.</p>
<dt>$HOME/.systemtap</p>
<dd>Systemtap data directory for cached systemtap files, unless overridden by the <i>SYSTEMTAP_DIR</i> environment variable.</p>
<dt>/tmp/stapXXXXXX</p>
<dd>Temporary directory for systemtap files, including translated C code and kernel object.</p>
<dt>/lib/modules/VERSION/build</p>
<dd>The location of kernel module building infrastructure.</p>
<dt>/usr/share/doc/systemtap*/examples</p>
<dd>Examples with greater detail can be found here. Each example comes with a .txt or .meta file explaining what the example, sample or demo does and how it is ordinarily run. See also <i><a rel="nofollow" href="http://sourceware.org/systemtap/examples/">http://sourceware.org/systemtap/examples/</a></i></p>
<dt>$SYSTEMTAP_DIR/ssl/server</p>
<dd>User&#8217;s server-side SSL certificate database. If SYSTEMTAP_DIR is not set, the default is $HOME/.systemtap.</p>
<dt>$SYSTEMTAP_DIR/ssl/client</p>
<dd>User&#8217;s private client-side SSL certificate database. If SYSTEMTAP_DIR is not set, the default is $HOME/.systemtap.</p>
<dt>/etc/systemtap/ssl/client</p>
<dd>Global client-side SSL certificate database.</p>
<dt>/etc/systemtap/staprun/</p>
<dd><i>staprun</i>&#8216;s trusted signer certificate database.</p>
<dt>/etc/sysconfig/stap-server/</p>
<dd>stap-server service global configuration file.</p>
<dt>/etc/stap-server/conf.d/*.conf</p>
<dd>stap-server service configuration files for default servers.</p>
<dt>/var/run/stap-server/</p>
<dd>stap-server service default location of status files for running servers.</p>
<dt>/var/log/stap-server/log</p>
<dd>stap-server service default log file. </p>
<h2>Files</h2>
<p><i>/usr/share/systemtap/tapset</i></p>
<h2>See Also</h2>
<pre><i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/8-staprun/">staprun</a></i>(8),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapvars/">stapvars</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/8-stap-server/">stap-server</a></i>(8),
<i><a href="//www.systutorials.com/docs/linux/man/1-awk/">awk</a></i>(1),
<i><a href="//www.systutorials.com/docs/linux/man/1-gdb/">gdb</a></i>(1)</pre>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
