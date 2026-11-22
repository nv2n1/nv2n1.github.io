---
title: "teamnl(8)"
name: "teamnl"
section: "8"
letter: "t"
url: "/docs/linux/man/8-teamnl/"
description: "teamnl — team network device Netlink interface tool"
---

<p>teamnl &#8212; team network device Netlink interface tool</p>
<h2>Synopsis</h2>
<p><code>teamnl</code> [<code>-p</code> <i>port_name</i>] [<code>-a</code> <i>array_index</i>] <i>team_device command </i>[<i>command_args</i>&#8230;]<br/>
 <code>teamnl</code> <code>-h</code></p>
<h2>Description</h2>
<p>teamnl is a tool enabling interaction with a team device via the team driver Netlink interface. This tools serves mainly for debugging purposes. Note that it makes no sense to use this tool to change options on team device controlled by a teamd instance.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print help text to console and exit.</dd>
<dt><code>-p ifname</code><i>, &#8211;port_name ifname</i></dt>
<dd>Select per-port option of provided interface name.</dd>
<dt><code>-a index</code><i>, &#8211;array_index index</i></dt>
<dd>Select array option of provided array index.</dd></dl>
<h2>Command</h2>
<dl>
<dt><code>ports</code></dt>
<dd>Dumps team ports.</dd>
<dt><code>option</code></dt>
<dd>Dumps team options.</dd>
<dt><code>getoption </code><i>opt_name</i></dt>
<dd>Gets option by selected name.</dd>
<dt><code>setoption </code><i>opt_name opt_value</i></dt>
<dd>Sets option by selected name.</dd>
<dt><code>monitor </code><i>opt_style</i></dt>
<dd>Monitors changes made to options, ports and interface information. Style can be either &quot;changed&quot; (default) or &quot;all&quot;.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-teamd/">teamd</a></code>(8), <code><a href="/docs/linux/man/8-teamdctl/">teamdctl</a></code>(8), <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libteam.</p>
