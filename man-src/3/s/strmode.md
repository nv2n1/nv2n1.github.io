---
title: "strmode(3)"
name: "strmode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strmode/"
description: "strmode – convert inode status information into a symbolic string"
---

<p><code>strmode</code> &#8211; convert inode status information into a symbolic string</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/string.h Ft void Fn strmode mode_t mode char *bp</p>
<h2>Description</h2>
<p>The Fn strmode function converts a file Fa mode (the type and permission information associated with an inode, see <a href="/docs/linux/man/2-stat/">stat</a>(2)) into a symbolic string which is stored in the location referenced by Fa bp . This stored string is eleven characters in length plus a trailing <code>NUL</code> The first character is the inode type, and will be one of the following: </p>
<dt><code>&#8211;</code></p>
<dd>regular file</p>
<dt><code>b</code></p>
<dd>block special</p>
<dt><code>c</code></p>
<dd>character special</p>
<dt><code>d</code></p>
<dd>directory</p>
<dt><code>l</code></p>
<dd>symbolic link</p>
<dt><code>p</code></p>
<dd>fifo</p>
<dt><code>s</code></p>
<dd>socket</p>
<dt><code>w</code></p>
<dd>whiteout</p>
<dt><code>?</code></p>
<dd>unknown inode type</dl>
<p> The next nine characters encode three sets of permissions, in three characters each. The first three characters are the permissions for the owner of the file, the second three for the group the file belongs to, and the third for the &#8220;other&#8221;, or default, set of users. Permission checking is done as specifically as possible. If read permission is denied to the owner of a file in the first set of permissions, the owner of the file will not be able to read the file. This is true even if the owner is in the file&#8217;s group and the group permissions allow reading or the &#8220;other&#8221; permissions allow reading. If the first character of the three character set is an &#8220;r&#8221;, the file is readable for that set of users; if a dash &#8220;-&#8221;, it is not readable. If the second character of the three character set is a &#8220;w&#8221;, the file is writable for that set of users; if a dash &#8220;-&#8221;, it is not writable. The third character is the first of the following characters that apply:</p>
<dl>
<dt><code>S</code></p>
<dd>If the character is part of the owner permissions and the file is not executable or the directory is not searchable by the owner, and the set-user-id bit is set.</p>
<dt><code>S</code></p>
<dd>If the character is part of the group permissions and the file is not executable or the directory is not searchable by the group, and the set-group-id bit is set.</p>
<dt><code>T</code></p>
<dd>If the character is part of the other permissions and the file is not executable or the directory is not searchable by others, and the &#8220;sticky&#8221; (<code>S_ISVTX</code> ) bit is set.</p>
<dt><code>s</code></p>
<dd>If the character is part of the owner permissions and the file is executable or the directory searchable by the owner, and the set-user-id bit is set.</p>
<dt><code>s</code></p>
<dd>If the character is part of the group permissions and the file is executable or the directory searchable by the group, and the set-group-id bit is set.</p>
<dt><code>t</code></p>
<dd>If the character is part of the other permissions and the file is executable or the directory searchable by others, and the &#8220;sticky&#8221; (<code>S_ISVTX</code> ) bit is set.</p>
<dt><code>x</code></p>
<dd>The file is executable or the directory is searchable.</p>
<dt><code>&#8211;</code></p>
<dd>None of the above apply.</dl>
<p> The last character is a plus sign &#8220;+&#8221; if any there are any alternate or additional access control methods associated with the inode, otherwise it will be a space.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-chmod/">chmod</a>(1), <a href="/docs/linux/man/1-find/">find</a>(1), <a href="/docs/linux/man/2-stat/">stat</a>(2), <a href="/docs/linux/man/3-getmode/">getmode</a>(3), <a href="/docs/linux/man/3-setmode/">setmode</a>(3)</p>
<h2>History</h2>
<p>The Fn strmode function first appeared in BSD 4.4</p>
