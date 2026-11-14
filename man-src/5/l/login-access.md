---
title: "login-access(5)"
name: "login-access"
section: "5"
letter: "l"
url: "/docs/linux/man/5-login-access/"
description: "login.access – login access control table"
---

<p><code>login.access</code> &#8211; login access control table</p>
<h2>Description</h2>
<p>The <code>login.access</code> file specifies on which ttys or from which hosts certain users are allowed to login. </p>
<p> At login, the /etc/login.access file is checked for the first entry that matches a specific user/host or user/tty combination. That entry can either allow or deny login access to that user. </p>
<p> Each entry have three fields separated by colon: </p>
<ul>
<li> The first field indicates the permission given if the entry matches. It can be either &#8220;+&#8221; (allow access) or &#8220;-&#8221; (deny access) .
<li> The second field is a comma separated list of users or groups for which the current entry applies. NIS netgroups can used (if configured) if preceeded by @. The magic string ALL matches all users. A group will match if the user is a member of that group, or it is the user&#8217;s primary group.
<li> The third field is a list of ttys, or network names. A network name can be either a hostname, a domain (indicated by a starting period), or a netgroup. As with the user list, ALL matches anything. LOCAL matches a string not containing a period. </ul>
<p> If the string EXCEPT is found in either the user or from list, the rest of the list are exceptions to the list before EXCEPT.</p>
<h2>Bugs</h2>
<p>If there&#8217;s a user and a group with the same name, there is no way to make the group match if the user also matches.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-login/">login</a>(1)</p>
<h2>Authors</h2>
<p>The Fn login_access function was written by Wietse Venema. This manual page was written for Heimdal.</p>
