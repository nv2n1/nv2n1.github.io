---
title: "lightdm-set-defaults(1)"
name: "lightdm-set-defaults"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lightdm-set-defaults/"
description: "lightdm-set-defaults – sets configuration options for lightdm"
---

<h2>NAME</h2>
<p> lightdm-set-defaults &#8211; sets configuration options for lightdm</p>
<h2>SYNOPSIS</h2>
<p> <code>lightdm-set-defaults</code> [ <i>OPTION</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lightdm-set-defaults</code> sets configuration options for lightdm. Requires root permissions to run.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-k, &#8211;keep-old</code></p>
<dd> Only update if no default already set</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable debugging messages</p>
<dt><code>-r, &#8211;remove</code></p>
<dd> Remove default value if it&#8217;s the current one</p>
<dt><code>-s, &#8211;session=SESSION_NAME</code></p>
<dd> Set the default session to SESSION_NAME</p>
<dt><code>-g, &#8211;greeter=GREETER_NAME</code></p>
<dd> Set the default greeter to GREETER_NAME</p>
<dt><code>-a, &#8211;autologin=USERNAME</code></p>
<dd> Set the autologin user to USERNAME</p>
<dt><code>-i, &#8211;hide-users=&lt;true|false&gt;</code></p>
<dd> Set greeter-hide-users to true or false.</p>
<dt><code>-m, &#8211;show-manual-login=&lt;true|false&gt;</code></p>
<dd> Set show-manual-login to true or false.</p>
<dt><code>-R, &#8211;show-remote-login=&lt;true|false&gt;</code></p>
<dd> Set show-manual-login to true or false.</p>
<dt><code>-l, &#8211;allow-guest=&lt;true|false&gt;</code></p>
<dd> Set allow-guest to true or false.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/lightdm/lightdm.conf</code></p>
<dd> Configuration </p>
</dl>
<h2>Index</h2>
