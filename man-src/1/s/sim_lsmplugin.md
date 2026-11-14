---
title: "sim_lsmplugin(1)"
name: "sim_lsmplugin"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sim_lsmplugin/"
description: "sim_lsmplugin — LibStorageMgmt simulator python plugin"
---

<h2>NAME</h2>
<p> sim_lsmplugin &#8212; LibStorageMgmt simulator python plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt simulator plugin is for development or test use only. The plugin simulates an array which supports most features of the library. State is stored in a file, default is &#8216;/tmp/lsm_sim_data&#8217;. The &#8216;sim_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client user specifies sim plugin in the URI. </p>
<p> This plugin is written in pure Python and is intended to be an example of a python plugin for the library. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    # All that is required
    sim://
    # Optional statefile
    <a href="sim://?statefile=">sim://?statefile=</a>&lt;file path and name&gt;
</pre>
<p> No password is required for this plugin. </p>
<dl>
<dt><code>URI parameters</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>statefile</code></p>
<dd>
<p> Use specified file to store simulator state data. Example URI: </p>
<pre>
    <code><a href="sim://?statefile=/tmp/other_lsm_sim_data">sim://?statefile=/tmp/other_lsm_sim_data</a></code>
</pre>
<p> The statefile is a sqlite3 data base file. </p>
</dl>
</dl>
</dl>
<h2>FIREWALL RULES</h2>
<p> This plugin requires not network access. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1) </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
