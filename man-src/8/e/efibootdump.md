---
title: "efibootdump(8)"
name: "efibootdump"
section: "8"
letter: "e"
url: "/docs/linux/man/8-efibootdump/"
description: "efibootdump – dump a boot entries from a variable or a file"
---

<p>efibootdump &#8211; dump a boot entries from a variable or a file</p>
<h2>Synopsis</h2>
<p><code>efibootdump</code> [<code>-?</code>|<code>&#8211;help</code>] [<code>&#8211;usage</code>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[<code>-f</code> <i>&lt;file1&gt;</i> [&#8230; <code>-f</code> <i>&lt;fileN&gt;</i>]]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[[<code>-g</code> <i>{guid}</i>] <i>&lt;name0&gt;</i> [&#8230; [<i>&lt;nameN&gt;</i>]]]</p>
<h2>Description</h2>
<p><code>efibootdump</code> is a userspace application used to display individual UEFI boot options, from a file or a UEFI variable. This allows e.g. saved files from efivarfs to be displayed, as well as variables on the running machine. </p>
<h2>Options</h2>
<p>The following is a list of options accepted by efibootmgr:</p>
<dl>
<dt><code>-g | &#8211;guid</code> <i>{guid}</i></p>
<dd>Any variables specified by name have the specified GUID.</p>
<dt><code>-f | &#8211;file</code> <i>&lt;file&gt;</i></p>
<dd>Read a single boot variable from the specified file.</p>
<dt><i>&lt;nameN&gt;</i></p>
<dd>Display the specified variable on the local machine. If no GUID is specified, EFI Global Variable is the default.</dl>
<h2>Bugs</h2>
<p>Please direct any bugs, features, patches, etc. to the Red Hat bootloader team at <a rel="nofollow" href="https://github.com/rhboot/efibootmgr">https://github.com/rhboot/efibootmgr</a> .</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-efibootmgr/">efibootmgr</a>(8) </p>
