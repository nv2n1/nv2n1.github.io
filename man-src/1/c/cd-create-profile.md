---
title: "cd-create-profile(1)"
name: "cd-create-profile"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-create-profile/"
description: "cd-create-profile – Color Manager Profile Creation Tool"
---

<h2 class="name">NAME</h2>
<p> cd-create-profile &#8211; Color Manager Profile Creation Tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cd-create-profile</code> [<code>&#8211;verbose</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>cd-create-profile</code> command. </p>
<p> <code>cd-create-profile</code> allows an administrator to create ICC profiles on their system.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;). A summary of options is included below. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>&#8211;description (optional)</code></p>
<dl>
<dt>
<dd> Sets the profile description.</dl>
<p> <code>&#8211;copyright (optional)</code></p>
<dl>
<dt>
<dd> Sets the profile copyright.</dl>
<p> <code>&#8211;model (optional)</code></p>
<dl>
<dt>
<dd> Sets the profile model.</dl>
<p> <code>&#8211;manufacturer (optional)</code></p>
<dl>
<dt>
<dd> Sets the profile manufacturer.</dl>
<p> <code>&#8211;srgb-palette</code></p>
<dl>
<dt>
<dd> Specifies a comma separated values file that is used for the named color. </p>
<p> The format of the CSV file must be &quot;Color Name&quot;,0-255(red),0-255(green),0-255(blue).</dl>
<p> <code>&#8211;output</code></p>
<dl>
<dt>
<dd> Specifies the output ICC filename.</dl>
<p> <code>&#8211;nc-prefix (optional)</code></p>
<dl>
<dt>
<dd> Specifies the named color palette prefix.</dl>
<p> <code>&#8211;nc-suffix (optional)</code></p>
<dl>
<dt>
<dd> Specifies the named color palette suffix.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Richard Hughes &lt;richard [at] hughsie.com&gt;. </p>
<h2>Index</h2>
