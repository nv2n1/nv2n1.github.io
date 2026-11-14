---
title: "networks(5)"
name: "networks"
section: "5"
letter: "n"
url: "/docs/linux/man/5-networks/"
description: "networks – network name information"
---

<p>networks &#8211; network name information</p>
<h2>Description</h2>
<p>The file <i>/etc/networks</i> is a plain ASCII file that describes known DARPA networks and symbolic names for these networks. Each line represents a network and has the following structure: </p>
<dl>
<dd><i>name number aliases &#8230;</i></dl>
<p> where the fields are delimited by spaces or tabs. Empty lines are ignored. The hash character (<code>#</code>) indicates the start of a comment: this character, and the remaining characters up to the end of the current line, are ignored by library functions that process the file. </p>
<p> The field descriptions are:</p>
<dl>
<dt><i>name</i></p>
<dd>The symbolic name for the network. Network names can contain any printable characters except white-space characters or the comment character.</p>
<dt><i>number</i></p>
<dd>The official number for this network in numbers-and-dots notation (see <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3)). The trailing &quot;.0&quot; (for the host component of the network address) may be omitted.</p>
<dt><i>aliases</i></p>
<dd>Optional aliases for the network.</dl>
<p> This file is read by the <code><a href="/docs/linux/man/8-route/">route</a></code>(8) and <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8) utilities. Only Class A, B or C networks are supported, partitioned networks (i.e., network/26 or network/28) are not supported by this file.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/networks</i></p>
<dd>The networks definition file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getnetbyaddr/">getnetbyaddr</a></code>(3), <code><a href="/docs/linux/man/3-getnetbyname/">getnetbyname</a></code>(3), <code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
