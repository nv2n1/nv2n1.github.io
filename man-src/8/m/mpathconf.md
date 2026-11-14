---
title: "mpathconf(8)"
name: "mpathconf"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mpathconf/"
description: "mpathconf – A tool for configuring device-mapper-multipath"
---

<p>mpathconf &#8211; A tool for configuring device-mapper-multipath</p>
<h2>Synopsis</h2>
<p><code>mpathconf</code> [<code>commands</code>] [<code>options</code>]</p>
<h2>Description</h2>
<p><code>mpathconf</code> is a utility that creates or modifies <code>/etc/multipath.conf.</code> It can enable or disable multipathing and configure some common options. <code>mpathconf</code> can also load the <code>dm_multipath</code> module, start and stop the <code>multipathd</code> daemon, and configure the <code>multipathd</code> service to start automatically or not. If <code>mpathconf</code> is called with no commands, it will display the current configuration. </p>
<p> The default options for mpathconf are <code>&#8211;with_module</code> The <code>&#8211;with_multipathd</code> option is not set by default. Enabling multipathing will load the <code>dm_multipath</code> module but it will not immediately start it. This is so that users can manually edit their config file if necessary, before starting <code>multipathd.</code> </p>
<p> If <code>/etc/multipath.conf</code> already exists, mpathconf will edit it. If it does not exist, mpathconf will use <code>/usr/share/doc/device-mapper-multipath-0.4.9/multipath.conf</code> as the starting file. This file has <code>user_friendly_names</code> set. If this file does not exist, mpathconf will create <code>/etc/multipath.conf</code> from scratch. For most users, this means that <code>user_friendly_names</code> will be set by default, unless they use the <code>&#8211;user_friendly_names n</code> command.</p>
<h2>Commands</h2>
<dl>
<dt><code>&#8211;enable</code></p>
<dd>Removes any line that blacklists all device nodes from the <code>/etc/multipath.conf</code> blacklist section.</p>
<dt><code>&#8211;disable</code></p>
<dd>Adds a line that blacklists all device nodes to the <code>/etc/multipath.conf</code> blacklist section. If no blacklist section exists, it will create one.</p>
<dt><code>&#8211;user_friendly_name </code> { <code>y</code> | <code>n</code> }</p>
<dd>If set to <code>y</code>, this adds the line <code>user_friendly_names yes</code> to the <code>/etc/multipath.conf</code> defaults section. If set to <code>n</code>, this removes the line, if present. This command can be used along with any other command.</p>
<dt><code>&#8211;find_multipaths</code> { <code>y</code> | <code>n</code> }</p>
<dd>If set to <code>y</code>, this adds the line <code>find_multipaths yes</code> to the <code>/etc/multipath.conf</code> defaults section. If set to <code>n</code>, this removes the line, if present. This command can be used aldong with any other command.</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;with_module</code> { <code>y</code> | <code>n</code> }</p>
<dd>If set to <code>y</code>, this runs <code>modprobe dm_multipath</code> to install the multipath modules. This option only works with the <code>&#8211;enable</code> command. This option is set to <code>y</code> by default.</p>
<dt><code>&#8211;with_multipathd { y</code> | <code>n</code> }</p>
<dd>If set to <code>y</code>, this runs <code>service multipathd start</code> to start the multipathd daemon on <code>&#8211;enable</code>, <code>service multipathd stop</code> to stop the multipathd daemon on <code>&#8211;disable</code>, and <code>service multipathd reload</code> to reconfigure multipathd on <code>&#8211;user_frindly_names</code> and <code>&#8211;find_multipaths</code>. This option is set to <code>n</code> by default.</dl>
<h2>Files</h2>
<p><code>/etc/multipath.conf</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-multipath-conf/">multipath.conf</a></code>(5), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/8-multipath/">multipath</a></code>(8), <code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8), <code><a href="/docs/linux/man/8-service/">service</a></code>(8),</p>
<h2>Author</h2>
<p>Benjamin Marzinski &lt;bmarzins [at] redhat.com&gt;</p>
