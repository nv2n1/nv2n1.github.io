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
<dt><i>-c, &#8211;class</i></dt>
<dd>Specify the SELinux class which the source domain will attempt to communicate with the target domain. (Default file)</dd>
<dt><i>-h, &#8211;help </i></dt>
<dd>Display help message</dd>
<dt><i>-s, &#8211;source</i></dt>
<dd>Specify the source SELinux domain type.</dd>
<dt><i>-S, &#8211;sourceaccess</i></dt>
<dd>Specify the list of accesses used by the source SELinux domain type to communicate with the target domain. Default Open, Write.</dd>
<dt><i>-t, &#8211;target</i></dt>
<dd>Specify the target SELinux domain type.</dd>
<dt><i>-T, &#8211;targetaccess</i></dt>
<dd>Specify the list of accesses used by the target SELinux domain type to receive communications from the source domain. Default Open, Read. </dd>
</dl>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sepolicy/">sepolicy</a>(8), <a href="/docs/linux/man/8-selinux/">selinux</a>(8) </p>
