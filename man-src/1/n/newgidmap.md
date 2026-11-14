---
title: "newgidmap(1)"
name: "newgidmap"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newgidmap/"
description: "newgidmap – set the gid mapping of a user namespace"
---

<h2 class="name">NAME</h2>
<p> newgidmap &#8211; set the gid mapping of a user namespace </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>newgidmap</code> <i>pid</i> <i>gid</i> <i>lowergid</i> <i>count</i> [<i>pid</i>&nbsp;<wbr><i>gid</i>&nbsp;<wbr><i>lowergid</i>&nbsp;<wbr><i>count</i>&nbsp;<wbr>[&nbsp;<wbr><i>&#8230;</i>&nbsp;<wbr>]]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>newgidmap</code> sets /proc/[pid]/gid_map based on it&#8217;s command line arguments and the gids allowed in /etc/subgid. </p>
<p> After the pid argument, <code>newgidmap</code> expects sets of 3 integers: </p>
<p> gid</p>
<dl>
<dt>
<dd> Begining of the range of GIDs inside the user namespace.</dl>
<p> lowergid</p>
<dl>
<dt>
<dd> Begining of the range of GIDs outside the user namespace.</dl>
<p> count</p>
<dl>
<dt>
<dd> Length of the ranges (both inside and outside the user namespace).</dl>
<p> <code>newgidmap</code> verifies that the caller is the owner of the process indicated by <code>pid</code> and that for each of the above sets, each of the GIDs in the range [lowergid, lowergid+count] is allowed to the caller according to /etc/subgid before setting /proc/[pid]/gid_map. </p>
<p> Note that newgidmap may be used only once for a given process.</p>
<h2>OPTIONS</h2>
<p> There currently are no options to the <code>newgidmap</code> command.</p>
<h2>FILES</h2>
<p> /etc/subgid</p>
<dl>
<dt>
<dd> List of users subordinate group IDs.</dl>
<p> /proc/[pid]/gid_map</p>
<dl>
<dt>
<dd> Mapping of gids from one between user namespaces.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-newusers/">newusers</a></code>(8), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8). </p>
<h2>Index</h2>
