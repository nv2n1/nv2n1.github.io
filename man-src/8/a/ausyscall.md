---
title: "ausyscall(8)"
name: "ausyscall"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ausyscall/"
description: "ausyscall – a program that allows mapping syscall names and numbers"
---

<p>ausyscall &#8211; a program that allows mapping syscall names and numbers</p>
<h2>Synopsis</h2>
<p><code>ausyscall [arch] name | number | &#8211;dump | &#8211;exact</code></p>
<h2>Description</h2>
<p><code>ausyscall</code> is a program that prints out the mapping from syscall name to number and reverse for the given arch. The arch can be anything returned by `uname -m`. If arch is not given, the program will take a guess based on the running image. You may give the syscall name or number and it will find the opposite. You can also dump the whole table with the &#8211;dump option. By default a syscall name lookup will be a substring match meaning that it will try to match all occurrences of the given name with syscalls. So giving a name of chown will match both fchown and chown as any other syscall with chown in its name. If this behavior is not desired, pass the &#8211;exact flag and it will do an exact string match. </p>
<p> This program can be used to verify syscall numbers on a biarch platform for rule optimization. For example, suppose you had an auditctl rule: </p>
<p> <code>-a always, exit -S open -F exit=-EPERM -k fail-open</code> </p>
<p> If you wanted to verify that both 32 and 64 bit programs would be audited, run &quot;ausyscall i386 open&quot; and then &quot;ausyscall x86_64 open&quot;. Look at the returned numbers. If they are different, you will have to write two auditctl rules to get complete coverage. </p>
<pre><code>-a always,exit -F arch=b32 -S open -F exit=-EPERM -k fail-open</code>
<code>-a always,exit -F arch=b64 -S open -F exit=-EPERM -k fail-open</code></pre>
<p>For more information about a specific syscall, use the man program and pass the number 2 as an argument to make sure that you get the syscall information rather than a shell script program or glibc function call of the same name. For example, if you wanted to learn about the open syscall, type: man 2 open.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;dump</code></p>
<dd>Print all syscalls for the given arch</p>
<dt><code>&#8211;exact</code></p>
<dd>Instead of doing a partial word match, match the given syscall name exactly. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
