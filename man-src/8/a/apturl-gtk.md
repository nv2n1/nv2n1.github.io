---
title: "apturl-gtk(8)"
name: "apturl-gtk"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apturl-gtk/"
description: "apturl – graphical apt-protocol interpreting package installer"
---

<p>apturl &#8211; graphical apt-protocol interpreting package installer</p>
<h2>Synopsis</h2>
<p><code>apturl</code> [<code>options&#8230;</code>] &lt;<code>URL</code>&gt; </p>
<h2>Description</h2>
<p><code>apturl</code> is a simple graphical application that takes an URL (following the apt-protocol) as a command line option, parses it and carries out the operations that the URL describes (that is, it asks the user if he wants the indicated packages to be installed and if the answer is positive does so). </p>
<h2>Usage</h2>
<p><code>apturl</code> just needs an URL conforming with the apt-protocol in order to work. Additionally, it recognizes the following options:</p>
<dl>
<dt><code>-p, &#8211;http-proxy</code></p>
<dd>Use the given HTTP proxy in order to download the packages. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>apturl apt:pidgin,pidgin-plugin-pack</p>
<dd>Installs Pidgin and Pidgin Plugin Pack (if the user confirms).</p>
<dt>apturl apt:freevial?section=universe</p>
<dd>Enables the &quot;universe&quot; component and installs package Freevial.</p>
<dt>apturl apt:adobe-flashplugin?channel=lucid-partner</p>
<dd>Enables the &quot;partner&quot; repository and installs package adobe-flashplugin. Available repositories are listed in /usr/share/app-install/channels/.</p>
<dt>apturl apt+<a rel="nofollow" href="http://launchpad.net/~mvo/ppa?package=2vcard">http://launchpad.net/~mvo/ppa?package=2vcard</a></p>
<dd>Installs 2vcard from the indicated PPA (if the user confirms), and afterward asks if the PPA should be removed again or it should remain enabled.<br />
 Warning: This is currently disabled because of security concerns. </p>
<h2>Exit Codes</h2>
<dl>
<dt>0</p>
<dd>All requested packages have been successfully installed or were already installed.</p>
<dt>1</p>
<dd>The user aborted the installation of one or more packages.</p>
<dt>2</p>
<dd>There was an error doing the requested operations, or the user aborted the installation while Synaptic (and not apturl itself) was working.</p>
<dt>3</p>
<dd>The arguments with which <code>apturl</code> was called were incorrect (e.g., it was called without any argument or the given URL was wrong). </p>
</dl>
<h2>Bugs</h2>
<p>Please report any bug on <a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/apturl.">https://bugs.launchpad.net/ubuntu/+source/apturl.</a> </p>
<h2>See Also</h2>
<p><code>synaptic</code> </p>
<h2>Authors</h2>
<p><code>apturl</code> was written by Michael Vogt &lt;michael.vogt [at] ubuntu.com&gt; for Canonical, Ltd. and this manual page by Siegfried-A. Gevatter &lt;rainct [at] ubuntu.com&gt;. </p>
<p> It is released under the GNU General Public License, version 2 or any later version published by the Free Software Foundation.</p>
