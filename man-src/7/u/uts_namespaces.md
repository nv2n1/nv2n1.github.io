---
title: "uts_namespaces(7)"
name: "uts_namespaces"
section: "7"
letter: "u"
url: "/docs/linux/man/7-uts_namespaces/"
description: "uts_namespaces – overview of Linux UTS namespaces"
---

<p>uts_namespaces &#8211; overview of Linux UTS namespaces</p>
<h2>Description</h2>
<p>UTS namespaces provide isolation of two system identifiers: the hostname and the NIS domain name. These identifiers are set using <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) and <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2), and can be retrieved using <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2), <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), and <code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2). Changes made to these identifiers are visible to all other processes in the same UTS namespace, but are not visible to processes in other UTS namespaces. </p>
<p> When a process creates a new UTS namespace using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWUTS</code> flag, the hostname and domain of the new UTS namespace are copied from the corresponding values in the caller&#8217;s UTS namespace. </p>
<p> Use of UTS namespaces requires a kernel that is configured with the <code>CONFIG_UTS_NS</code> option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2), <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
