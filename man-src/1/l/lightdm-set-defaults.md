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
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>-k, &#8211;keep-old</code></dt>
<dd> Only update if no default already set</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> Enable debugging messages</dd>
<dt><code>-r, &#8211;remove</code></dt>
<dd> Remove default value if it&#8217;s the current one</dd>
<dt><code>-s, &#8211;session=SESSION_NAME</code></dt>
<dd> Set the default session to SESSION_NAME</dd>
<dt><code>-g, &#8211;greeter=GREETER_NAME</code></dt>
<dd> Set the default greeter to GREETER_NAME</dd>
<dt><code>-a, &#8211;autologin=USERNAME</code></dt>
<dd> Set the autologin user to USERNAME</dd>
<dt><code>-i, &#8211;hide-users=&lt;true|false&gt;</code></dt>
<dd> Set greeter-hide-users to true or false.</dd>
<dt><code>-m, &#8211;show-manual-login=&lt;true|false&gt;</code></dt>
<dd> Set show-manual-login to true or false.</dd>
<dt><code>-R, &#8211;show-remote-login=&lt;true|false&gt;</code></dt>
<dd> Set show-manual-login to true or false.</dd>
<dt><code>-l, &#8211;allow-guest=&lt;true|false&gt;</code></dt>
<dd> Set allow-guest to true or false.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/lightdm/lightdm.conf</code></dt>
<dd> Configuration </dd>
</dl>
