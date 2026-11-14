---
title: "seinfo(1)"
name: "seinfo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-seinfo/"
description: "seinfo – SELinux policy query tool"
---

<h2>NAME</h2>
<p> seinfo &#8211; SELinux policy query tool</p>
<h2>SYNOPSIS</h2>
<p> <code>seinfo</code> [OPTIONS] [EXPRESSION] [POLICY &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>seinfo</code> allows the user to query the components of a SELinux policy.</p>
<h2>POLICY</h2>
<p> <code>seinfo</code> supports loading a SELinux policy in one of four formats.</p>
<dl>
<dt>source</p>
<dd> A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</p>
<dt>binary</p>
<dd> A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</p>
<dt>modular</p>
<dd> A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</p>
<dt>policy list</p>
<dd> A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dl>
<p> If no policy file is provided, <code>seinfo</code> will search for the system default policy: checking first for a source policy, next for a binary policy matching the running kernel&#8217;s preferred version, and finally for the highest version that can be found. In the latter case, the policy will be downgraded to match the running system. If no policy can be found, <code>seinfo</code> will print an error message and exit.</p>
<h2>EXPRESSIONS</h2>
<p> One or more of the following component types can be queried. Each option may only be specified once. If an option is provided multiple times, the last instance will be used. Some components support the -x flag to print expanded information about that component; if a particular component specified does not support expanded information, the flag will be ignored for that component (see -x below). If no expressions are provided, policy statistics will be printed (see &#8211;stats below).</p>
<dl>
<dt>-c[NAME], &#8211;class[=NAME]</p>
<dd> Print a list of object classes or, if NAME is provided, print the object class NAME. With -x, print a list of permissions for each displayed object class.</p>
<dt>&#8211;sensitivity[=NAME]</p>
<dd> Print a list of sensitivities or, if NAME is provided, print the sensitivity NAME. With -x, print the corresponding level statement for each displayed sensitivity.</p>
<dt>&#8211;category[=NAME]</p>
<dd> Print a list of categories or, if NAME is provided, print the category NAME. With -x, print a list of sensitivities with which each displayed category may be associated.</p>
<dt>-t[NAME], &#8211;type[=NAME]</p>
<dd> Print a list of types (not including aliases or attributes) or, if NAME is provided, print the type NAME. With -x, print a list of attributes which include each displayed type.</p>
<dt>-a[NAME], &#8211;attribute[=NAME]</p>
<dd> Print a list of type attributes or, if NAME is provided, print the attribute NAME. With -x, print a list of types assigned to each displayed attribute.</p>
<dt>-r[NAME], &#8211;role[=NAME]</p>
<dd> Print a list of roles or, if NAME is provided, print the role NAME. With -x, print a list of types assigned to each displayed role.</p>
<dt>-u[NAME], &#8211;user[=NAME]</p>
<dd> Print a list of users or, if NAME is provided, print the user NAME. With -x, print a list of roles assigned to each displayed user.</p>
<dt>-b[NAME], &#8211;bool[=NAME]</p>
<dd> Print a list of conditional booleans or, if NAME is provided, print the boolean NAME. With -x, print the default state of each displayed conditional boolean.</p>
<dt>&#8211;initialsid[=NAME]</p>
<dd> Print a list of initial SIDs or, if NAME is provided, print the initial SID NAME. With -x, print the context assigned to each displayed SID.</p>
<dt>&#8211;fs_use[=TYPE]</p>
<dd> Print a list of fs_use statements or, if TYPE is provided, print the statement for filesystem TYPE. There is no expanded information for this component.</p>
<dt>&#8211;genfscon[=TYPE]</p>
<dd> Print a list of genfscon statements or, if TYPE is provided, print the statement for the filesystem TYPE. There is no expanded information for this component.</p>
<dt>&#8211;netifcon[=NAME]</p>
<dd> Print a list of netif contexts or, if NAME is provided, print the statement for interface NAME. There is no expanded information for this component.</p>
<dt>&#8211;nodecon[=ADDR]</p>
<dd> Print a list of node contexts or, if ADDR is provided, print the statement for the node with address ADDR. There is no expanded information for this component.</p>
<dt>&#8211;polcap</p>
<dd> Print policy capabilities.</p>
<dt>&#8211;permissive</p>
<dd> Print permissive types.</p>
<dt>&#8211;portcon[=PORT]</p>
<dd> Print a list of port contexts or, if PORT is provided, print the statement for port PORT. There is no expanded information for this component.</p>
<dt>&#8211;protocol=PROTO</p>
<dd> Print only portcon statements for the protocol PROTO. This option is ignored if portcon statements are not printed or if no statement exists for the requested port.</p>
<dt>&#8211;constrain</p>
<dd> Print a list of constraints. There is no expanded information for this component.</p>
<dt>&#8211;all</p>
<dd> Print all components.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-x, &#8211;expand</p>
<dd> Print additional details for each component matching the expression. These details include the types assigned to an attribute or role and the permissions for an object class. This option is not available for all component types; see the description of each component for the details this option will provide.</p>
<dt>&#8211;stats</p>
<dd> Print policy statistics including policy type and version information and counts of all components and rules.</p>
<dt>-l, &#8211;line-breaks</p>
<dd> Print line breaks when displaying constraint statements.</p>
<dt>-h, &#8211;help</p>
<dd> Print help information and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version information and exit.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2003-2010 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sesearch/">sesearch</a>(1), <a href="/docs/linux/man/1-apol/">apol</a>(1) </p>
<h2>Index</h2>
