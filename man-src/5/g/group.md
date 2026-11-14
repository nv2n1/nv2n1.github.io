---
title: "group(5)"
name: "group"
section: "5"
letter: "g"
url: "/docs/linux/man/5-group/"
description: "group – user group file"
---

<p>group &#8211; user group file</p>
<h2>Description</h2>
<p>The <i>/etc/group</i> file is a text file that defines the groups on the system. There is one entry per line, with the following format: </p>
<p> group_name:password:GID:user_list </p>
<p> The fields are as follows:</p>
<dl>
<dt><i>group_name</i></p>
<dd>the name of the group.</p>
<dt><i>password</i></p>
<dd>the (encrypted) group password. If this field is empty, no password is needed.</p>
<dt><i>GID</i></p>
<dd>the numeric group ID.</p>
<dt><i>user_list</i></p>
<dd>a list of the usernames that are members of this group, separated by commas.</dl>
<h2>Files</h2>
<p><i>/etc/group</i></p>
<h2>Bugs</h2>
<p>As the 4.2BSD <code><a href="/docs/linux/man/3-initgroups/">initgroups</a></code>(3) man page says: no one seems to keep <i>/etc/group</i> up-to-date.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chgrp/">chgrp</a></code>(1), <code><a href="/docs/linux/man/1-gpasswd/">gpasswd</a></code>(1), <code><a href="/docs/linux/man/1-groups/">groups</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1), <code><a href="/docs/linux/man/1-sg/">sg</a></code>(1), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/5-gshadow/">gshadow</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/8-vigr/">vigr</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
