---
title: "apol(1)"
name: "apol"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apol/"
description: "apol – SELinux policy analysis tool"
---

<h2>NAME</h2>
<p> apol &#8211; SELinux policy analysis tool</p>
<h2>SYNOPSIS</h2>
<p> <code>apol</code> [OPTIONS] [POLICY &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>apol</code> is a graphical tool that allows the user to inspect aspects of a SELinux policy. The tool allows the user to browse policy components (types, classes, roles, users, etc.), rules (TE, RBAC, MLS), and file system contexts. The tool also provides in depth analyses of domain transitions, information flows, and relabeling permissions.</p>
<h2>POLICY</h2>
<p> <code>apol</code> supports loading a SELinux policy in one of four formats.</p>
<dl>
<dt>source</p>
<dd> A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</p>
<dt>binary</p>
<dd> A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</p>
<dt>modular</p>
<dd> A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</p>
<dt>policy list</p>
<dd> A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dl>
<p> If a policy is not given on the command line then <code>apol</code> will begin with none loaded.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Print help information and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version information and exit.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2001-2007 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-seinfo/">seinfo</a>(1), <a href="/docs/linux/man/1-sesearch/">sesearch</a>(1), <a href="/docs/linux/man/1-sechecker/">sechecker</a>(1), <a href="/docs/linux/man/1-indexcon/">indexcon</a>(1) </p>
<h2>Index</h2>
