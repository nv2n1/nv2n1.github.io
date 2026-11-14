---
title: "sepolicy-interface(8)"
name: "sepolicy-interface"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-interface/"
description: "sepolicy-interface – Print interface information based on the installed SELinux Policy"
---

<p>sepolicy-interface &#8211; Print interface information based on the installed SELinux Policy </p>
<h2>Synopsis</h2>
<p><code>sepolicy interface [-h] [-c] [-v] [-a | -u | -l | -i INTERFACE [INTERFACE &#8230; ]]</code> </p>
<h2>Description</h2>
<p>Use sepolicy interface to print interfaces information based on SELinux Policy. </p>
<h2>Options</h2>
<dl>
<dt><i>-a, &#8211;list_admin</i></p>
<dd>List all domains with admin interface</p>
<dt><i>-c, &#8211;compile</i></p>
<dd>Test compile of interfaces</p>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-i, &#8211;interface</i></p>
<dd>Interface(s) to be displayed</p>
<dt><i>-l, &#8211;list</i></p>
<dd>List all interfaces</p>
<dt><i>-u, &#8211;list_user</i></p>
<dd>List all domains with SELinux user role interface</p>
<dt><i>-v, &#8211;verbose</i></p>
<dd>Display extended information about the interface including parameters and desctiprion if available. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8) </p>
