---
title: "autoopts-config(1)"
name: "autoopts-config"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoopts-config/"
description: "autoopts-config – script to get information about installed version of autoopts"
---

<h2>NAME</h2>
<p> autoopts-config &#8211; script to get information about installed version of autoopts</p>
<h2>SYNOPSIS</h2>
<p> <code>autoopts-config</code> <code>{ &lt;value-name&gt; [&#8230;] | everything }</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>autoopts-config</code> is a tool that is used by configure to determine the compile and linker flags that should be used to compile and link programs that use autoopts. <i>value-name</i>s may be preceeded by one or more hyphens. They are silently ignored.</p>
<h2>VALUE NAMES</h2>
<dl>
<dt><code>autogen</code></p>
<dd>
<p> Print the full path name of the autogen executable.<br />
 The unconfigured value is: ${bindir}/autogen${exeext}</p>
<dt><code>bindir</code></p>
<dd>
<p> The destination directory for executable scripts and programs installed by the <i>autogen</i> package.<br />
 The unconfigured value is: @bindir@</p>
<dt><code>cflags</code></p>
<dd>
<p> Print the compiler flags that are necessary to compile an autoopts program.<br />
 The unconfigured value is: -I${includedir}</p>
<dt><code>datadir</code></p>
<dd>
<p> The directory for various data directories.<br />
 The unconfigured value is: @datadir@</p>
<dt><code>datarootdir</code></p>
<dd>
<p> The root directory for various data directories. In this case, there is only one, &quot;datadir&quot;.<br />
 The unconfigured value is: @datarootdir@</p>
<dt><code>dotver</code></p>
<dd>
<p> Print the currently installed version of autoopts, in dotted format.<br />
 The unconfigured value is: @AO_CURRENT@.@AO_REVISION@.@AO_AGE@</p>
<dt><code>everything</code></p>
<dd>
<p> Print the list of all names and values, one per line.</p>
<dt><code>exec_prefix</code></p>
<dd>
<p> The installation root for libraries and executables.<br />
 The unconfigured value is: @exec_prefix@</p>
<dt><code>exeext</code></p>
<dd>
<p> The executable file extension used for the autogen executable.<br />
 The unconfigured value is: @EXEEXT@</p>
<dt><code>includedir</code></p>
<dd>
<p> The directory where the AutoOpts headers are stored. This does not include the &quot;-I&quot; prefix gotten by specifying &quot;cflags&quot;.<br />
 The unconfigured value is: @includedir@</p>
<dt><code>ldflags</code></p>
<dd>
<p> Print the linker flags that are necessary to link an autoopts program in the default installation mode (static or dynamic).<br />
 The unconfigured value is: -L${libdir} -lopts</p>
<dt><code>ldopts</code></p>
<dd>
<p> The linker options to use when linking a program to libopts.<br />
 The unconfigured value is: @AG_LDFLAGS@</p>
<dt><code>libdir</code></p>
<dd>
<p> The libopts installation directory.<br />
 The unconfigured value is: @libdir@</p>
<dt><code>libs</code></p>
<dd>
<p> an alternate spelling of &quot;<i>ldflags</i>&quot;.<br />
 The unconfigured value is: ${ldflags}</p>
<dt><code>libsrc</code></p>
<dd>
<p> The full path of the redistributable, tear-off libopts library source. This file is in gzipped-tarball format.<br />
 The unconfigured value is: ${pkgdatadir}/libopts-${dotver}.tar.gz</p>
<dt><code>package</code></p>
<dd>
<p> The name of the package that provides <code>autoopts</code>. This is always &quot;<i>autogen</i>&quot;.<br />
 The unconfigured value is: @PACKAGE@</p>
<dt><code>pkgdatadir</code></p>
<dd>
<p> The directory containing support files used by autogen.<br />
 The unconfigured value is: ${datadir}/${package}</p>
<dt><code>prefix</code></p>
<dd>
<p> The <i>autogen</i> package installation prefix.<br />
 The unconfigured value is: @prefix@</p>
<dt><code>static_libs</code></p>
<dd>
<p> The name of the AR archive of the libopts object code.<br />
 The unconfigured value is: ${libdir}/libopts.a</p>
<dt><code>version</code></p>
<dd>
<p> Print the currently installed version of autoopts.<br />
 The unconfigured value is: @AO_CURRENT@:@AO_REVISION@:@AO_AGE@</dl>
<h2>SEE ALSO</h2>
<p> <i>Autogen</i> Info system documentation.</p>
<h2>AUTHORS</h2>
<p> AutoGen is the work of Bruce Korb &lt;bkorb [at] gnu.org&gt;.<br />
 Bruce Korb &lt;bkorb [at] gnu.org&gt; and<br />
 Luca Filipozzi &lt;lfilipoz [at] debian.org&gt; created this manpage. </p>
<p> AutoOpts is released under either the GNU General Public License with the Library exception (LGPL), or else the advertising clause free BSD license. Which license used is at the discretion of the licensee. </p>
<h2>Index</h2>
