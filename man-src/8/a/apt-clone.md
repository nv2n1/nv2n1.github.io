---
title: "apt-clone(8)"
name: "apt-clone"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-clone/"
description: "apt-clone – manual page for apt-clone 0.2"
---

<p>apt-clone &#8211; manual page for apt-clone 0.2</p>
<h2>Description</h2>
<p>usage: apt-clone [-h] [&#8211;debug] {info,clone,restore,restore-new-distro} &#8230; Clone/restore package info of a debian based system or chroot environment.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show help message for apt-clone. Alternatively &#8211;help will output command specific help for any of the {info,clone,restore,restore-new-distro} commands.</p>
<dt><code>&#8211;debug</code></p>
<dd>enable debug output</dl>
<h3>Commands:</h3>
<dl>
<dd>{info,clone,restore,restore-new-distro}</p>
<dt>info</p>
<dd>Show info about a apt-clone archive.</p>
<dt>clone</p>
<dd>Create a clone-file into &lt;destination&gt;. A alternative source dir can be specified with <code>&#8211;source</code>.</p>
<dt>restore</p>
<dd>Restore a clone file from &lt;source&gt;. A alternative destination can be given with <code>&#8211;destination</code>.</p>
<dt>restore-new-distro</p>
<dd>Restore a clone file from &lt;source&gt; to &lt;destination&gt; and try upgrading along the way. this can be used so that the current release is cloned, a new install is done and then the old clone is installed. </p>
