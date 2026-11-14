---
title: "chcat(8)"
name: "chcat"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chcat/"
description: "chcat – change file SELinux security category"
---

<p>chcat &#8211; change file SELinux security category</p>
<h2>Synopsis</h2>
<p><code>chcat</code> <i>category file</i>&#8230;<br />
 <code>chcat -l </code> <i>category user</i>&#8230;<br />
 <code>chcat</code> <i>[[+|-]category&#8230;] file</i>&#8230;<br />
 <code>chcat -l </code> <i>[[+|-]category&#8230;] user</i>&#8230;<br />
 <code>chcat</code> [<i>-d</i>] <i>file</i>&#8230;<br />
 <code>chcat -l </code> [<i>-d</i>] <i>user</i>&#8230;<br />
 <code>chcat</code> <i>-L</i> [ -l ] [ user &#8230; ]</p>
<h2>Description</h2>
<p>Change/Remove the security <i>category</i> for each <i>file</i> or <i>user</i>. </p>
<p> Use +/- to add/remove categories from a <i>file</i> or <i>user</i>. </p>
<p> <code>Note:</code> When removing a category you must specify &#8216;&#8211;&#8216; on the command line before using the -Category syntax. This tells the command that you have finished entering options and are now specifying a category name instead. </p>
<dl>
<dt><code>-d</code></p>
<dd>delete the category from each FILE/USER.</p>
<dt><code>-L</code></p>
<dd>list available categories.</p>
<dt><code>-l</code></p>
<dd>Tells chcat to operate on users instead of files.</dl>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/1-chcon/">chcon</a>(1), <a href="/docs/linux/man/8-selinux/">selinux</a>(8), <a href="/docs/linux/man/8-semanage/">semanage</a>(8)</p>
<dd></dl>
<p> When operating on files this script wraps the chcon command.</p>
<h2>Files</h2>
<p>/etc/selinux/{SELINUXTYPE}/setrans.conf<br />
 /etc/selinux/{SELINUXTYPE}/seusers</p>
