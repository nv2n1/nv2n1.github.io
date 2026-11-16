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
<dt>&bull;</dt>
<dd>The <code>copr</code> command is used to add or remove Copr repositories to the local system</dd>
<dt>&bull;</dt>
<dd>The <code>playground</code> is used to enable or disable the Playground repository</dd></dl>
<h2>Synopsis</h2>
<p><code>dnf copr [enable|disable|list|search] &lt;parameters&gt;</code> </p>
<p> <code>dnf playground [enable|disable|upgrade]</code></p>
<h2>Arguments (Copr)</h2>
<dl>
<dt><code>enable name/project [chroot]</code></dt>
<dd>Enable the <code>name/project</code> Copr repository with the optional <code>chroot</code>.</dd>
<dt><code>disable name/project</code></dt>
<dd>Disable the <code>name/project</code> Copr repository.</dd>
<dt><code>list name</code></dt>
<dd>List available Copr repositories for a given <code>name</code>.</dd>
<dt><code>search project</code></dt>
<dd>Search for a given <code>project</code>.</dd></dl>
<h2>Arguments (Playground)</h2>
<dl>
<dt><code>enable</code></dt>
<dd>Enable the Playground repository.</dd>
<dt><code>disable</code></dt>
<dd>Disable the Playground repository.</dd>
<dt><code>upgrade</code></dt>
<dd>Upgrade the Playground repository settings (same as <code>disable</code> and then <code>enable</code>).</dd></dl>
<h2>Examples</h2>
<dl>
<dt><code>copr enable rhscl/perl516 epel-6-x86_64</code></dt>
<dd>Enable the <code>rhscl/perl516</code> Copr repository, using the <code>epel-6-x86_64</code> chroot.</dd>
<dt><code>copr disable rhscl/perl516</code></dt>
<dd>Disable the <code>rhscl/perl516</code> Copr repository</dd>
<dt><code>copr list rita</code></dt>
<dd>List available Copr projects for user <code>rita</code>.</dd>
<dt><code>copr search tests</code></dt>
<dd>Search for Copr projects named <code>tests</code>.</dd></dl>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
