---
title: "dssi_analyse_plugin(1)"
name: "dssi_analyse_plugin"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dssi_analyse_plugin/"
description: "dssi_analyse_plugin – describe a DSSI plugin"
---

<h2 class="name">NAME</h2>
<p> dssi_analyse_plugin &#8211; describe a DSSI plugin </p>
<h2>SYNOPSIS</h2>
<p> <code>dssi_analyse_plugin</code> [-v|&#8211;verbose] [<i>path</i>]&lt;<i>libname</i>&gt;[:&lt;<i>label</i>&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dssi_analyse_plugin</code> lists information about DSSI plugins within a specified DSSI shared library <i>libname</i>. If <i>label</i> is given, only information for the plugin labeled <i>label</i> will be listed, otherwise, all plugins in the shared library will be listed. If <i>path</i> is not given, the shared library is searched for in the colon-separated list of directories specified in the environment variable <code>DSSI_PATH</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> <code>-v</code></p>
<dt>
<dd> <code>&#8211;verbose</code> Causes <code>dssi_analyse_plugin</code> to be more verbose in its reporting. In particular, it will list the default program names for each plugin, if any.</dl>
<h2>EXAMPLES</h2>
<p> The following command will show information about all of the plugins in the shared library /usr/local/lib/dssi/calf.so, including default program names: $ dssi_analyse_plugin -v /usr/local/lib/dssi/calf.so The following command will look for the shared library trivial_sampler.so using <code>DSSI_PATH</code>, and display information about the mono_sampler plugin: $ dssi_analyse_plugin trivial_sampler.so:mono_sampler</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DSSI_PATH</code></p>
<dd> A colon-separated list of directories to scan for DSSI plugins.</dl>
<h2>CONFORMING TO</h2>
<p> DSSI RFC version 1.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dssi_list_plugins/">dssi_list_plugins</a></code>(1), <a rel="nofollow" href="http://dssi.sourceforge.net/">http://dssi.sourceforge.net/</a> </p>
<h2>Index</h2>
