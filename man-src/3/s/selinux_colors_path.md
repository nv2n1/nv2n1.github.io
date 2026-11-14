---
title: "selinux_colors_path(3)"
name: "selinux_colors_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_colors_path/"
description: "selinux_colors_path – Return a path to the active SELinux policy color configuration file"
---

<p>selinux_colors_path &#8211; Return a path to the active SELinux policy color configuration file </p>
<h2>Synopsis</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>const char *selinux_colors_path(void);</code></p>
<h2>Description</h2>
<p> <code>selinux_colors_path</code>() returns the path to the active policy color configuration file. </p>
<p> The path is built from the path returned by <code><a href="/docs/linux/man/3-selinux_policy_root/">selinux_policy_root</a></code>(3) with <i>/secolor.conf</i> appended. </p>
<p> This optional configuration file whose format is shown in <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5), controls the colors to be associated with the <i>raw</i> context components of the <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3) function when information is to be displayed by an SELinux color-aware application.</p>
<h2>Return Value</h2>
<p> On success, the path to the active policy color configuration file is returned. If a path is not available NULL is returned.</p>
<h2>Errors</h2>
<p> None.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_policy_root/">selinux_policy_root</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5), <code><a href="/docs/linux/man/3-selinux_raw_context_to_color/">selinux_raw_context_to_color</a></code>(3), <code><a href="/docs/linux/man/5-secolor-conf/">secolor.conf</a></code>(5)</p>
