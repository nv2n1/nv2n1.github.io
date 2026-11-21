---

title: "deja-dup(1)"
name: "deja-dup"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deja-dup/"
description: "deja-dup – a desktop backup tool"
---

<p> deja-dup &#8211; a desktop backup tool </p>
<h2>SYNOPSIS</h2>
<p> <code>deja-dup</code> [OPTIONS…]<br />
 <code>deja-dup</code> &#8211;backup<br />
 <code>deja-dup</code> &#8211;restore [FILES…]<br />
 <code>deja-dup</code> &#8211;restore-missing DIRECTORY</p>
<h2>DESCRIPTION</h2>
<p> Déjà Dup is a simple backup tool. It hides the complexity of backing up the Right Way (encrypted, off-site, and regular) and uses duplicity as the backend.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version</dd>
<dt><code>&#8211;restore</code></dt>
<dd> Restore given files</dd>
<dt><code>&#8211;backup</code></dt>
<dd> Immediately start a backup</dd>
<dt><code>&#8211;restore-missing</code></dt>
<dd> Restore deleted files</dd>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></dt>
<dd> X display to use</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-duplicity/">duplicity</a></code>(1) </p>
