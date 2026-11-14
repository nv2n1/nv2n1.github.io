---
title: "dh-autoreconf(7)"
name: "dh-autoreconf"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dh-autoreconf/"
description: "dh-autoreconf – debhelper add-on to run autoreconf during build"
---

<p>dh-autoreconf &#8211; debhelper add-on to run autoreconf during build</p>
<h2>Description</h2>
<p>The dh-autoreconf package provides a sequence addon for debhelper 7 and is enabled by default since compatibility level 10. For earlier compatibility levels it can be enabled in the following way: </p>
<pre> #!/usr/bin/make -f
 %:
 dh $@ --with autoreconf</pre>
<p>This will call dh_autoreconf prior to dh_auto_configure and will call dh_autoreconf_clean before dh_clean. </p>
<p> For more information on how to control the autoreconf process or how to other possible options, read the <i><a href="/docs/linux/man/1-dh_autoreconf/">dh_autoreconf</a></i>(1) and <i><a href="/docs/linux/man/1-dh_autoreconf_clean/">dh_autoreconf_clean</a></i>(1) manual pages.</p>
<h2>Cdbs Integration</h2>
<p>This package also provides <i>/usr/share/cdbs/1/rules/autoreconf.mk</i> for packages using <font SIZE="-1"><code>CDBS</code></font>. The variable <tt>&quot;DEB_DH_AUTORECONF_ARGS&quot;</tt> can be used to pass extra arguments to dh_autoreconf, and the variable <tt>&quot;DEB_DH_AUTORECONF_CLEAN_ARGS&quot;</tt> to pass arguments to dh_autoreconf_clean. See their manual pages for information on available arguments.</p>
<h2>Tips And Examples</h2>
<h3><font SIZE="-1">PATCHING LTMAIN.SH FOR</font> AS-NEEDED <font SIZE="-1">LINKER FLAGS</font></h3>
<p>You can add support for -Wl,&#8211;as-needed to ltmain.sh (at least for those ltmain.sh scripts changed during autoreconf) by passing the argument <code>&#8211;as-needed</code> to dh_autoreconf, as demonstrated in the following example: </p>
<pre> override_dh_autoreconf:
 dh_autoreconf --as-needed</pre>
<p>and for <font SIZE="-1">CDBS,</font> by adding it to the correct variable such as: </p>
<pre> DEB_DH_AUTORECONF_ARGS = --as-needed</pre>
<p>For more information about this feature, see <i><a href="/docs/linux/man/1-dh_autoreconf/">dh_autoreconf</a></i>(1)</p>
<h3><font SIZE="-1">RUNNING MULTIPLE COMMANDS WITH DH_AUTORECONF</font></h3>
<p>Please note that you may run dh_autoreconf only once. If you need to run multiple commands, you can put the commands into a script or your debian/rules file and then pass the name of your script to dh_autoreconf. For example, if your script is called debian/autogen.sh, you can put the following into your debian/rules if you use dh: </p>
<pre> override_dh_autoreconf:
 dh_autoreconf debian/autogen.sh</pre>
<p>Or, if you use <font SIZE="-1">CDBS:</font> </p>
<pre> DEB_DH_AUTORECONF_ARGS += debian/autogen.sh</pre>
<h2>Caveats</h2>
<p>dh_autoreconf is mostly a superset of the dh_update_autotools_config debhelper command included in debhelper since version 9.20160115. When using the dh sequencer, dh_update_autotools_config is run before dh_autoreconf and updates the config.guess and config.sub files. This is required in cases where autoreconf does not update config.guess and config.sub itself. </p>
<p> From time to time, there might be a short breakage for those using automatic ltmain.sh patching, when the patch no longer applies to the ltmain.sh. </p>
<p> You can only run dh_autoreconf once. Future versions may be able to be run multiple times, but this requires slightly more planning.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7), <i><a href="/docs/linux/man/1-dh/">dh</a></i>(1), <i><a href="/docs/linux/man/1-dh_autoreconf/">dh_autoreconf</a></i>(1), <i><a href="/docs/linux/man/1-dh_autoreconf_clean/">dh_autoreconf_clean</a></i>(1)</p>
<h2>Author</h2>
<p>Julian Andres Klode &lt;jak [at] debian.org&gt;</p>
