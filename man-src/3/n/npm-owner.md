---
title: "npm-owner(3)"
name: "npm-owner"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-owner/"
description: "npm-owner — Manage package owners"
---

<p><code>npm-owner</code> &#8212; Manage package owners</p>
<h2>Synopsis</h2>
<pre>npm.commands.owner(args, callback)</pre>
<h2>Description</h2>
<p>The first element of the &#8216;args&#8217; parameter defines what to do, and the subsequent elements depend on the action. Possible values for the action are (order of parameters are given in parenthesis):</p>
<dl>
<dt>&bull;</p>
<dd>ls (package): List all the users who have access to modify a package and push new versions. Handy when you need to know who to bug for help.</p>
<dt>&bull;</p>
<dd>add (user, package): Add a new user as a maintainer of a package. This user is enabled to modify metadata, publish new versions, and add other owners.</p>
<dt>&bull;</p>
<dd>rm (user, package): Remove a user from the package owner list. This immediately revokes their privileges.</p>
<dd></dl>
<p> Note that there is only one level of access. Either you can modify a package, or you can&#8217;t. Future versions may contain more fine-grained access levels, but that is not implemented at this time.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm apihelp publish</p>
<dt>&bull;</p>
<dd>npm help registry</p>
<dd>
