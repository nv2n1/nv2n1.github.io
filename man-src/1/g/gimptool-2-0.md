---
title: "gimptool-2-0(1)"
name: "gimptool-2-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimptool-2-0/"
description: "gimptool-2.0 – script to perform various GIMPy functions"
---

<p>gimptool-2.0 &#8211; script to perform various GIMPy functions </p>
<h2>Synopsis</h2>
<p><code>gimptool-2.0</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;help] [&#8211;quiet] [&#8211;silent] [-n] [&#8211;just-print] [&#8211;dry-run] [&#8211;recon] [&#8211;msvc-syntax] [&#8211;bindir] [&#8211;sbindir] [&#8211;libexecdir] [&#8211;datadir] [&#8211;sysconfdir] [&#8211;sharedstatedir] [&#8211;localstatedir] [&#8211;libdir] [&#8211;infodir] [&#8211;mandir] [&#8211;includedir] [&#8211;gimpplugindir] [&#8211;gimpdatadir] [&#8211;libs] [&#8211;libs-noui] [&#8211;cflags] [&#8211;cflags-noi] [&#8211;build <i>plug-in.c</i>] [&#8211;build-strip <i>plug-in.c</i>] [&#8211;install <i>plug-in.c</i>] [&#8211;install-strip <i>plug-in.c</i>] [&#8211;install-admin <i>plug-in.c</i>] [&#8211;install-bin <i>plug-in</i>] [&#8211;install-admin-strip <i>plug-in.c</i>] [&#8211;install-bin-strip <i>plug-in</i>] [&#8211;install-admin-bin <i>plug-in</i>] [&#8211;install-script <i>script.scm</i>] [&#8211;install-admin-script <i>script.scm</i>] [&#8211;uninstall-bin <i>plug-in</i>] [&#8211;uninstall-admin-bin <i>plug-in</i>] [&#8211;uninstall-script <i>script.scm</i>] [&#8211;uninstall-admin-script <i>script.scm</i>] </p>
<h2>Description</h2>
<p><i>gimptool-2.0</i> is a tool that can, among other things, build plug-ins or scripts and install them if they are distributed in one source file. </p>
<p> <i>gimptool-2.0</i> can also be used by programs that need to know what libraries and include-paths <i>GIMP</i> was compiled with. <i>gimptool-2.0</i> uses <i>pkg-config</i> for this task. For use in Makefiles, it is recommended that you use <i>pkg-config</i> directly instead of calling <i>gimptool-2.0</i>. </p>
<h2>Options</h2>
<p><i>gimptool-2.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Print the currently installed version of <i>GIMP</i> on the standard output.</p>
<dt><code>&#8211;help</code></p>
<dd>Print out the help blurb, showing commonly used commandline options.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Run quietly without echoing any of the build commands.</p>
<dt><code>&#8211;silent</code></p>
<dd>Run silently without echoing any of the build commands. Same as &#8211;quiet.</p>
<dt><code>-n</code></p>
<dd>Test mode. Print the commands but don&#8217;t actually execute them. Useful for making dry runs for testing.</p>
<dt><code>&#8211;just-print</code></p>
<dd>Test mode. Print the commands but don&#8217;t actually execute them. Same as -n.</p>
<dt><code>&#8211;dry-run</code></p>
<dd>Test mode. Print the commands but don&#8217;t actually execute them. Same as -n.</p>
<dt><code>&#8211;recon</code></p>
<dd>Test mode. Print the commands but don&#8217;t actually execute them. Same as -n.</p>
<dt><code>&#8211;msvc-syntax</code></p>
<dd>Useful on Windows. Outputs the compiler and linker flags in the syntax used by Microsoft&#8217;s toolchain. Passed to the pkg-config command that does most of <i>gimptool-2.0</i>&#8216;s work.</p>
<dt><code>&#8211;bindir</code></p>
<dd>Outputs the bindir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;sbindir</code></p>
<dd>Outputs the sbindir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;libexecdir</code></p>
<dd>Outputs the libexecdir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;datadir</code></p>
<dd>Outputs the datadir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;sysconfdir</code></p>
<dd>Outputs the sysconfdir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;sharedstatedir</code></p>
<dd>Outputs the sharedstatedir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;localstatedir</code></p>
<dd>Outputs the localstatedir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;libdir</code></p>
<dd>Outputs the libdir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;infodir</code></p>
<dd>Outputs the infodir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;mandir</code></p>
<dd>Outputs the mandir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;includedir</code></p>
<dd>Outputs the includedir used to install the <i>GIMP</i>.</p>
<dt><code>&#8211;gimpdatadir</code></p>
<dd>Outputs the actual directory where the <i>GIMP</i> data files were installed.</p>
<dt><code>&#8211;gimpplugindir</code></p>
<dd>Outputs the actual directory where the <i>GIMP</i> plug-ins were installed.</p>
<dt><code>&#8211;build </code><i>plug-in.c</i></p>
<dd>Compile and link <i>plug-in.c</i> into a <i>GIMP</i> plug-in.</p>
<dt><code>&#8211;build-strip </code><i>plug-in.c</i></p>
<dd>Compile,link, and strip <i>plug-in.c</i> into a <i>GIMP</i> plug-in.</p>
<dt><code>&#8211;install </code><i>plug-in.c</i></p>
<dd>Compile, link, and install <i>plug-in.c</i> into the user&#8217;s personal <i>GIMP</i> plug-in directory (<code>$HOME</code>/.gimp-2.8/plug-ins)</p>
<dt><code>&#8211;install-strip </code><i>plug-in.c</i></p>
<dd>Compile, link,strip, and install <i>plug-in.c</i> into the user&#8217;s personal <i>GIMP</i> plug-in directory (<code>$HOME</code>/.gimp-2.8/plug-ins)</p>
<dt><code>&#8211;install-admin </code><i>plug-in.c</i></p>
<dd>Compile, link, and install <i>plug-in.c</i> into the system-wide <i>GIMP</i> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</p>
<dt><code>&#8211;install-bin </code><i>plug-in</i></p>
<dd>Install <i>plug-in</i> into the user&#8217;s personal <i>GIMP</i> plug-in directory (<code>$HOME</code>/.gimp-2.8/plug-ins)</p>
<dt><code>&#8211;install-admin-bin </code><i>plug-in</i></p>
<dd>Install <i>plug-in</i> into the system-wide <i>GIMP</i> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</p>
<dt><code>&#8211;install-bin-strip </code><i>plug-in</i></p>
<dd>Install stripped <i>plug-in</i> into the user&#8217;s personal <i>GIMP</i> plug-in directory (<code>$HOME</code>/.gimp-2.8/plug-ins)</p>
<dt><code>&#8211;install-admin-bin-strip </code><i>plug-in</i></p>
<dd>Install stripped <i>plug-in</i> into the system-wide <i>GIMP</i> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</p>
<dt><code>&#8211;install-script </code><i>script.scm</i></p>
<dd>Install <i>script.scm</i> into the user&#8217;s personal <i>GIMP</i> script directory (<code>$HOME</code>/.gimp-2.8/scripts)</p>
<dt><code>&#8211;install-admin-script </code><i>script.scm</i></p>
<dd>Install <i>script.scm</i> into the system-wide <i>GIMP</i> script directory (/usr/share/gimp/2.0/scripts)</p>
<dt><code>&#8211;uninstall-bin </code><i>plug-in</i></p>
<dd>Uninstall <i>plug-in</i> from the user&#8217;s personal <i>GIMP</i> plug-in directory (<code>$HOME</code>/.gimp-2.8/plug-ins)</p>
<dt><code>&#8211;uninstall-admin-bin </code><i>plug-in</i></p>
<dd>Uninstall <i>plug-in</i> from the system-wide <i>GIMP</i> plug-in directory (/usr/lib64/gimp/2.0/plug-ins)</p>
<dt><code>&#8211;uninstall-script </code><i>script.scm</i></p>
<dd>Uninstall <i>script.scm</i> from the user&#8217;s personal <i>GIMP</i> script directory (<code>$HOME</code>/.gimp-2.8/scripts)</p>
<dt><code>&#8211;uninstall-admin-script </code><i>script.scm</i></p>
<dd>Uninstall <i>script.scm</i> from the system-wide <i>GIMP</i> script directory (/usr/share/gimp/2.0/scripts)</p>
<dt><code>&#8211;libs</code></p>
<dd>Print the linker flags that are necessary to link a <i>GIMP</i> plug-in.</p>
<dt><code>&#8211;libs-noui</code></p>
<dd>Print the linker flags that are necessary to link a <i>GIMP</i> plug-in, for plug-ins that do not require the GTK+ libraries.</p>
<dt><code>&#8211;cflags</code></p>
<dd>Print the compiler flags that are necessary to compile a <i>GIMP</i> plug-in.</p>
<dt><code>&#8211;clags-noui</code></p>
<dd>Print the compiler flags that are necessary to compile a <i>GIMP</i> plug-in for plug-ins that do not require the GTK+ libraries.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd>If specified, use PREFIX instead of the installation prefix that <i>GIMP</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd>If specified, use PREFIX instead of the installation exec prefix that <i>GIMP</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>CC</code></p>
<dd>to get the name of the desired C compiler.</p>
<dt><code>CFLAGS</code></p>
<dd>to get the preferred flags to pass to the C compiler for plug-in building.</p>
<dt><code>LDFLAGS</code></p>
<dd>to get the preferred flags for passing to the linker.</p>
<dt><code>LIBS</code></p>
<dd>for passing extra libs that may be needed in the build process. For example, LIBS=-lintl .</p>
<dt><code>PKG_CONFIG</code></p>
<dd>to get the location of the <i>pkg-config</i> program that is used to determine details about your glib, pango, gtk+ and gimp installation. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), <code><a href="/docs/linux/man/5-gimprc/">gimprc</a></code>(5), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) </p>
<h2>Authors</h2>
<p>gimptool was written by Manish Singh (yosh [at] gimp.org) and is based on gtk-config by Owen Taylor (owen [at] gtk.org). </p>
<p> This man page was written by Ben Gertzfield (che [at] debian.org), and tweaked by Manish Singh (yosh [at] gimp.org), Adrian Likins (adrian [at] gimp.org) and Marc Lehmann (pcg [at] goof.com&gt;).</p>
