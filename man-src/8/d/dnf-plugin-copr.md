---
title: "dnf-plugin-copr(8)"
name: "dnf-plugin-copr"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-copr/"
description: "dnf.plugin.copr – DNF copr Plugin"
---

<p>dnf.plugin.copr &#8211; DNF copr Plugin </p>
<p> Work with Copr &amp; Playground repositories on the local system.</p>
<dl>
<dt>&bull;</p>
<dd>The <code>copr</code> command is used to add or remove Copr repositories to the local system</p>
<dt>&bull;</p>
<dd>The <code>playground</code> is used to enable or disable the Playground repository</dl>
<h2>Synopsis</h2>
<p><code>dnf copr [enable|disable|list|search] &lt;parameters&gt;</code> </p>
<p> <code>dnf playground [enable|disable|upgrade]</code></p>
<h2>Arguments (Copr)</h2>
<dl>
<dt><code>enable name/project [chroot]</code></p>
<dd>Enable the <code>name/project</code> Copr repository with the optional <code>chroot</code>.</p>
<dt><code>disable name/project</code></p>
<dd>Disable the <code>name/project</code> Copr repository.</p>
<dt><code>list name</code></p>
<dd>List available Copr repositories for a given <code>name</code>.</p>
<dt><code>search project</code></p>
<dd>Search for a given <code>project</code>.</dl>
<h2>Arguments (Playground)</h2>
<dl>
<dt><code>enable</code></p>
<dd>Enable the Playground repository.</p>
<dt><code>disable</code></p>
<dd>Disable the Playground repository.</p>
<dt><code>upgrade</code></p>
<dd>Upgrade the Playground repository settings (same as <code>disable</code> and then <code>enable</code>).</dl>
<h2>Examples</h2>
<dl>
<dt><code>copr enable rhscl/perl516 epel-6-x86_64</code></p>
<dd>Enable the <code>rhscl/perl516</code> Copr repository, using the <code>epel-6-x86_64</code> chroot.</p>
<dt><code>copr disable rhscl/perl516</code></p>
<dd>Disable the <code>rhscl/perl516</code> Copr repository</p>
<dt><code>copr list rita</code></p>
<dd>List available Copr projects for user <code>rita</code>.</p>
<dt><code>copr search tests</code></p>
<dd>Search for Copr projects named <code>tests</code>.</dl>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
