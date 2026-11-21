---

title: "grub2-editenv(1)"
name: "grub2-editenv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-editenv/"
description: "grub-editenv — Manage the GRUB environment block."
---

<h2>NAME</h2>
<p> <code>grub-editenv</code> &#8212; Manage the GRUB environment block. </p>
<p> <code>grub-editenv</code> [-v | &#8211;verbose] [<i>FILE</i>]</p>
<dl>
<dt>
</dt><dd> &lt;create | list | set <i>NAME</i>=<i>VALUE</i> | unset <i>NAME</i>&gt; </dd>
</dl>
<p> <code>grub-editenv</code> is a command line tool to manage GRUB&#8217;s stored environment. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code></dt>
<dd> Print verbose messages. </dd>
<dt><code>FILE</code></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> File name to use for grub environment. Default is /boot/grub/grubenv .</dd></dl>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>create</code></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> Create a blank environment block file.</dd></dl>
<dt><code>list</code></dt>
<dd>
</dd><dl>
<dt>
</dt><dd> List the current variables.</dd></dl>
<dt><code>set</code> [<i>NAME</i>=<i>VALUE</i> &#8230;]</dt>
<dd> Set variables. </dd>
<dt><code>unset [</code><i>NAME</i> &#8230;]</dt>
<dd> Delete variables. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
