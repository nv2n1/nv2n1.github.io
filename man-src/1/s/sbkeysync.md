---
title: "sbkeysync(1)"
name: "sbkeysync"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbkeysync/"
description: "sbkeysync – UEFI secure boot key synchronization tool"
---

<h2 class="name">NAME</h2>
<p> sbkeysync &#8211; UEFI secure boot key synchronization tool </p>
<h2>SYNOPSIS</h2>
<p> <code>sbkeysync</code> [<i>,options/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Update EFI key databases from the filesystem</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;efivars-path</code> &lt;dir&gt;</dt>
<dd> Path to efivars mountpoint (or regular directory for testing)</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Print verbose progress information</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> Don&#8217;t update firmware key databases</dd>
<dt><code>&#8211;pk</code></dt>
<dd> Set PK</dd>
<dt><code>&#8211;keystore</code> &lt;dir&gt;</dt>
<dd> Read keys from &lt;dir&gt;/{db,dbx,KEK}/* (can be specified multiple times, first dir takes precedence)</dd>
<dt><code>&#8211;no-default-keystores</code></dt>
<dd> Don&#8217;t read keys from the default</dd>
<dt>
</dt><dd> keystore dirs </dd>
</dl>
