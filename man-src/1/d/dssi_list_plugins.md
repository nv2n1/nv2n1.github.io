---
title: "dssi_list_plugins(1)"
name: "dssi_list_plugins"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dssi_list_plugins/"
description: "dssi_list_plugins – list available DSSI plugins"
---

<h2 class="name">NAME</h2>
<p> dssi_list_plugins &#8211; list available DSSI plugins </p>
<h2>SYNOPSIS</h2>
<p> <code>dssi_list_plugins</code> [-v|&#8211;verbose]</p>
<h2>DESCRIPTION</h2>
<p> <code>dssi_list_plugins</code> scans a list of directories specified by the environment variable <code>DSSI_PATH</code>, looking for DSSI (or LADSPA) shared libraries. It reports each library found, and lists the plugins contained within the library. It ignores subdirectories and libtool *.la files; otherwise it will complain if any of the files found are not DSSI or LADSPA shared libraries.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> <code>-v</code></p>
<dt>
<dd> <code>&#8211;verbose</code> Causes <code>dssi_list_plugins</code> to be more verbose in its reporting. It will note conditions which are typically ignored by most DSSI hosts, yet may indicate problems, including malformed or unreadable components of <code>DSSI_PATH</code>, directories which contain no plugin libraries, libraries which appear more than once in the <code>DSSI_PATH</code>, and libraries which contain no plugins.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DSSI_PATH</code></p>
<dd> A colon-separated list of directories to scan for DSSI plugins.</dl>
<h2>CONFORMING TO</h2>
<p> DSSI RFC version 1.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dssi_analyse_plugin/">dssi_analyse_plugin</a></code>(1), <a rel="nofollow" href="http://dssi.sourceforge.net/">http://dssi.sourceforge.net/</a> </p>
<h2>Index</h2>
