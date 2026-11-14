---
title: "gai-conf(5)"
name: "gai-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gai-conf/"
description: "gai.conf –"
---

<p>gai.conf &#8211; </p>
<p> <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3) configuration file</p>
<h2>Description</h2>
<p>A call to <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) might return multiple answers. According to RFC 3484 these answers must be sorted so that the answer with the highest success rate is first in the list. The RFC provides an algorithm for the sorting. The static rules are not always adequate, though. For this reason, the RFC also requires that system administrators should have the possibility to dynamically change the sorting. For the glibc implementation, this can be achieved with the <i>/etc/gai.conf</i> file. </p>
<p> Each line in the configuration file consists of a keyword and its parameters. White spaces in any place are ignored. Lines starting with &#8216;#&#8217; are comments and are ignored. </p>
<p> The keywords currently recognized are:</p>
<dl>
<dt><code>label</code> <i>netmask</i> <i>precedence</i></p>
<dd>The value is added to the label table used in the RFC 3484 sorting. If any <code>label</code> definition is present in the configuration file, the default table is not used. All the label definitions of the default table which are to be maintained have to be duplicated. Following the keyword, the line has to contain a network mask and a precedence value.</p>
<dt><code>precedence</code> <i>netmask</i> <i>precedence</i></p>
<dd>This keyword is similar to <code>label</code>, but instead the value is added to the precedence table as specified in RFC 3484. Once again, the presence of a single <code>precedence</code> line in the configuration file causes the default table to not be used.</p>
<dt><code>reload</code> &lt;<code>yes</code>|<code>no</code>&gt;</p>
<dd>This keyword controls whether a process checks whether the configuration file has been changed since the last time it was read. If the value is &quot;<code>yes</code>&quot;, the file is reread. This might cause problems in multithreaded applications and is generally a bad idea. The default is &quot;<code>no</code>&quot;.</p>
<dt><code>scopev4</code> <i>mask</i> <i>value</i></p>
<dd>Add another rule to the RFC 3484 scope table for IPv4 address. By default, the scope IDs described in section 3.2 in RFC 3438 are used. Changing these defaults should hardly ever be necessary.</dl>
<h2>Files</h2>
<p><i>/etc/gai.conf</i></p>
<h2>Versions</h2>
<p>The <i>gai.conf</i> file is supported by glibc since version 2.5.</p>
<h2>Examples</h2>
<p>The default table according to RFC 3484 would be specified with the following configuration file: </p>
<p> label ::1/128 0 label ::/0 1 label 2002::/16 2 label ::/96 3 label ::ffff:0:0/96 4 precedence ::1/128 50 precedence ::/0 40 precedence 2002::/16 30 precedence ::/96 20 precedence ::ffff:0:0/96 10</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), RFC 3484</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
