---
title: "sepolicy-communicate(8)"
name: "sepolicy-communicate"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sepolicy-communicate/"
description: "sepolicy-communicate – Generate a report showing if two SELinux Policy Domains can communicate"
---

<p>sepolicy-communicate &#8211; Generate a report showing if two SELinux Policy Domains can communicate </p>
<h2>Synopsis</h2>
<p><code>sepolicy communicate [-h] -s SOURCE -t TARGET [-c TCLASS] [-S SOURCEACCESS] [-T TARGETACCESS]</code> </p>
<h2>Description</h2>
<p>Use sepolicy communicate to examine SELinux Policy to if a source SELinux Domain can communicate with a target SELinux Domain. The default command looks to see if there are any file types that the source domain can write, which the target domain can read. </p>
<h2>Options</h2>
<dl>
<dt><i>-c, &#8211;class</i></p>
<dd>Specify the SELinux class which the source domain will attempt to communicate with the target domain. (Default file)</p>
<dt><i>-h, &#8211;help </i></p>
<dd>Display help message</p>
<dt><i>-s, &#8211;source</i></p>
<dd>Specify the source SELinux domain type.</p>
<dt><i>-S, &#8211;sourceaccess</i></p>
<dd>Specify the list of accesses used by the source SELinux domain type to communicate with the target domain. Default Open, Write.</p>
<dt><i>-t, &#8211;target</i></p>
<dd>Specify the target SELinux domain type.</p>
<dt><i>-T, &#8211;targetaccess</i></p>
<dd>Specify the list of accesses used by the target SELinux domain type to receive communications from the source domain. Default Open, Read. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8) </p>
