---
title: "vlock-plugins(5)"
name: "vlock-plugins"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vlock-plugins/"
description: "vlock-plugins – plugin support for vlock"
---

<p>vlock-plugins &#8211; plugin support for vlock</p>
<h2>Description</h2>
<p>If <a href="/docs/linux/man/8-vlock-main/">vlock-main</a>(8) is compiled with plugin support its default features are very limited: it can only lock the current session and ask for authenticiaton. However it is possible to extend this functions through plugins. These plugins are loaded when vlock-main starts and can provide hooks that are called at certain points during the lifetime of the vlock-main process. </p>
<h2>Default Plugins</h2>
<p>The following plugins are provided when installing vlock with default options: </p>
<p> <code>all</code></p>
<dl>
<dd>This plugin locks all sessions by disabling console switching. It is also loaded when giving the <code>-a,&#8211;all</code> option to <a href="/docs/linux/man/1-vlock/">vlock</a>(1). </p>
</dl>
<p> <code>new</code></p>
<dl>
<dd>This plugin switches to a new virtual console before disabling console switching through the &quot;all&quot; plugin. It is also loaded when giving the <code>-n,&#8211;new</code> option to <a href="/docs/linux/man/1-vlock/">vlock</a>(1).</dl>
<p> <code>nosysrq</code></p>
<dl>
<dd>Linux only. This plugin disables the Linux SysRQ mechanism before the console switching is locked by the &quot;all&quot; plugin. It is also loaded when giving the <code>-s,&#8211;disable-sysrq</code> option to <a href="/docs/linux/man/1-vlock/">vlock</a>(1).</dl>
<h2>Additional Plugins</h2>
<p>The following plugins are only available if explicitly selected at build time: </p>
<p> <code>caca</code></p>
<dl>
<dd>This plugin runs a random libcaca screensaver when the screen is locked.</dl>
<h2>Writing Plugins</h2>
<p>For information about writing plugins see the PLUGINS file in the vlock source distribution.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vlock/">vlock</a></code>(1), <code><a href="/docs/linux/man/8-vlock-main/">vlock-main</a></code>(8)</p>
<h2>Authors</h2>
<p>Frank Benkstein &lt;frank-vlock [at] benkstein.net&gt;</p>
