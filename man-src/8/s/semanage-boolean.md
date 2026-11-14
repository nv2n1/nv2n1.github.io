---
title: "semanage-boolean(8)"
name: "semanage-boolean"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semanage-boolean/"
description: "semanage-boolean – SELinux Policy Management boolean tool"
---

<p>semanage-boolean &#8211; SELinux Policy Management boolean tool</p>
<h2>Synopsis</h2>
<p><code>semanage boolean [-h] [-n] [-N] [-S STORE] [ &#8211;extract | &#8211;deleteall | &#8211;list [-C] | &#8211;modify ( &#8211;on | &#8211;off ) boolean ]</code> </p>
<h2>Description</h2>
<p>semanage is used to configure certain elements of SELinux policy without requiring modification to or recompilation from policy sources. semanage boolean command controls the settings of booleans in SELinux policy. booleans are if-then-else rules written in SELinux Policy. They can be used to customize the way that SELinux Policy rules effect a confined domain.</p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>show this help message and exit</p>
<dt><i>-n, &#8211;noheading</i></p>
<dd>Do not print heading when listing the specified object type</p>
<dt><i>-N, &#8211;noreload</i></p>
<dd>Do not reload policy after commit</p>
<dt><i>-S STORE, &#8211;store STORE</i></p>
<dd>Select an alternate SELinux Policy Store to manage</p>
<dt><i>-C, &#8211;locallist</i></p>
<dd>List local customizations</p>
<dt><i>-m, &#8211;modify</i></p>
<dd>Modify a record of the specified object type</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List records of the specified object type</p>
<dt><i>-E, &#8211;extract</i></p>
<dd>Extract customizable commands, for use within a transaction</p>
<dt><i>-D, &#8211;deleteall</i></p>
<dd>Remove all local customizations</p>
<dt><i>-1, &#8211;on</i></p>
<dd>Enable the boolean</p>
<dt><i>-0, &#8211;off</i></p>
<dd>Disable the boolean </p>
</dl>
<h2>Example</h2>
<pre>Turn on the apache can send mail boolan
# semanage boolean -m --on httpd_can_sendmail
List customized booleans
# semanage boolean -l -C</pre>
<h2>See Also</h2>
<p><code>selinux (8),</code> <code>semanage (8)</code> <code>setsebool (8)</code> <code>getsebool (8)</code> </p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
