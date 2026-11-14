---
title: "newuidmap(1)"
name: "newuidmap"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newuidmap/"
description: "newuidmap – set the uid mapping of a user namespace"
---

<h2 class="name">NAME</h2>
<p> newuidmap &#8211; set the uid mapping of a user namespace </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>newuidmap</code> <i>pid</i> <i>uid</i> <i>loweruid</i> <i>count</i> [<i>uid</i>&nbsp;<wbr><i>loweruid</i>&nbsp;<wbr><i>count</i>&nbsp;<wbr>[&nbsp;<wbr><i>&#8230;</i>&nbsp;<wbr>]]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>newuidmap</code> sets /proc/[pid]/uid_map based on it&#8217;s command line arguments and the uids allowed in /etc/subuid. </p>
<p> After the pid argument, <code>newuidmap</code> expects sets of 3 integers: </p>
<p> uid</p>
<dl>
<dt>
<dd> Begining of the range of UIDs inside the user namespace.</dl>
<p> loweruid</p>
<dl>
<dt>
<dd> Begining of the range of UIDs outside the user namespace.</dl>
<p> count</p>
<dl>
<dt>
<dd> Length of the ranges (both inside and outside the user namespace).</dl>
<p> <code>newuidmap</code> verifies that the caller is the owner of the process indicated by <code>pid</code> and that for each of the above sets, each of the UIDs in the range [loweruid, loweruid+count] is allowed to the caller according to /etc/subuid before setting /proc/[pid]/uid_map. </p>
<p> Note that newuidmap may be used only once for a given process.</p>
<h2>OPTIONS</h2>
<p> There currently are no options to the <code>newuidmap</code> command.</p>
<h2>FILES</h2>
<p> /etc/subuid</p>
<dl>
<dt>
<dd> List of users subordinate user IDs.</dl>
<p> /proc/[pid]/uid_map</p>
<dl>
<dt>
<dd> Mapping of uids from one between user namespaces.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-newusers/">newusers</a></code>(8), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/8-useradd/">useradd</a></code>(8), <code><a href="/docs/linux/man/8-usermod/">usermod</a></code>(8), <code><a href="/docs/linux/man/8-userdel/">userdel</a></code>(8). </p>
<h2>Index</h2>
