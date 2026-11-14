---
title: "simc_lsmplugin(1)"
name: "simc_lsmplugin"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simc_lsmplugin/"
description: "simc_lsmplugin — LibstorageMgmt Simulator C Plugin"
---

<h2>NAME</h2>
<p> simc_lsmplugin &#8212; LibstorageMgmt Simulator C Plugin </p>
<h2>DESCRIPTION</h2>
<p> LibStorageMgmt simulator C plugin is for development use. The plugin simulates an array which supports most features of the library. The simulator is memory based, state will be discarded once the plugin exits. The &#8216;simc_lsmplugin&#8217; executable file is for the libStorageMgmt daemon to execute when client user specifies simc plugin in the URI. </p>
<p> Since every command of lsmcli is a standalone libStorageMgmt session, this plugin is essentially useless for this purpose. In this use case, the libStorageMgmt simulator plugin <code><a href="/docs/linux/man/1-sim_lsmplugin/">sim_lsmplugin</a>(1)</code> is suggested. </p>
<p> This plugin is written in pure C and is intended to be an example of a C plugin for the library. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    simc://
</pre>
<p> No password is required for this plugin. No URI parameters are supported by this plugin. </p>
<h2>FIREWALL RULES</h2>
<p> This plugin requires not network access. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1), <code><a href="/docs/linux/man/1-sim_lsmplugin/">sim_lsmplugin</a></code>(1) </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
