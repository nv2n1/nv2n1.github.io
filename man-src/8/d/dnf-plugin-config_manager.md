---
title: "dnf-plugin-config_manager(8)"
name: "dnf-plugin-config_manager"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-config_manager/"
description: "dnf.plugin.config_manager – DNF config-manager Plugin"
---

<p>dnf.plugin.config_manager &#8211; DNF config-manager Plugin </p>
<p> Manage main DNF configuration options, toggle which repositories are enabled or disabled, and add new repositories.</p>
<h2>Synopsis</h2>
<p><code>dnf config-manager [options] &lt;repo&gt;&#8230;</code></p>
<h2>Arguments</h2>
<dl>
<dt><code>&lt;repo&gt;</code></p>
<dd>Display / modify specified repository. If not specified display / modify main DNF configuration.</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help-cmd</code></p>
<dd>Show this help.</p>
<dt><code>&#8211;add-repo=URL</code></p>
<dd>Add (and enable) the repo from the specified file or url.</p>
<dt><code>&#8211;dump</code></p>
<dd>Print dump of current configuration values to stdout.</p>
<dt><code>&#8211;set-disabled</code></p>
<dd>Disable the specified repos (automatically saves).</p>
<dt><code>&#8211;set-enabled</code></p>
<dd>Enable the specified repos (automatically saves).</p>
<dt><code>&#8211;save</code></p>
<dd>Save the current options (useful with &#8211;setopt).</dl>
<h2>Examples</h2>
<dl>
<dt><code>dnf config-manager &#8211;add-repo <a rel="nofollow" href="http://example.com/some/additional.repo">http://example.com/some/additional.repo</a></code></p>
<dd>Download additional.repo and store it in repodir.</p>
<dt><code>dnf config-manager &#8211;add-repo <a rel="nofollow" href="http://example.com/different/repo">http://example.com/different/repo</a></code></p>
<dd>Create new repo file with <i><a rel="nofollow" href="http://example.com/different/repo">http://example.com/different/repo</a></i> as baseurl and enable it.</p>
<dt><code>dnf config-manager</code></p>
<dd>Display main DNF configuration.</p>
<dt><code>dnf config-manager repo</code></p>
<dd>Display configuration of repo.</p>
<dt><code>dnf config-manager &#8211;set-enabled repo</code></p>
<dd>Enable repo and make the change permanent.</p>
<dt><code>dnf config-manager &#8211;setopt proxy=<a rel="nofollow" href="http://proxy.example.com:3128/">http://proxy.example.com:3128/</a> repo1 repo2 &#8211;save</code></p>
<dd>Update proxy setting in repo1 and repo2 and make the change permanent.</dl>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
