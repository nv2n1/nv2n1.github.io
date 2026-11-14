---
title: "locktest(1)"
name: "locktest"
section: "1"
letter: "l"
url: "/docs/linux/man/1-locktest/"
description: "locktest – Find differences in locking between two SMB servers"
---

<h2 class="name">NAME</h2>
<p> locktest &#8211; Find differences in locking between two SMB servers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>locktest</code> {//server1/share1} {//server2/share2} [-U user%pass] [-U user%pass] [-s seed] [-o numops] [-a] [-O] [-E] [-Z] [-R range] [-B base] [-M min]</dl>
<h2>DESCRIPTION</h2>
<dd>locktest is a utility for detecting differences in behaviour in locking between SMB servers. It will run a random set of locking operations against <i>//server1/share1</i> and then the same random set against <i>//server2/share2</i> and display the differences in the responses it gets. </p>
<p> This utility is used by the Samba team to find differences in behaviour between Samba and Windows servers.</p>
<h2>OPTIONS</h2>
<p> -U user%pass</p>
<dl>
<dt>
<dd> Specify the user and password to use when logging on on the shares. This parameter can be specified twice (once for the first server, once for the second).</dl>
<p> -s seed</p>
<dl>
<dt>
<dd> Seed the random number generator with the specified value.</dl>
<p> -o numops</p>
<dl>
<dt>
<dd> Set the number of operations to perform.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Print the operations that are performed.</dl>
<p> -A</p>
<dl>
<dt>
<dd> Backtrack to find minimal number of operations required to make the response to a certain call differ.</dl>
<p> -O</p>
<dl>
<dt>
<dd> Enable oplocks.</dl>
<p> -u</p>
<dl>
<dt>
<dd> Hide unlock fails.</dl>
<p> -E</p>
<dl>
<dt>
<dd> enable exact error code checking</dl>
<p> -Z</p>
<dl>
<dt>
<dd> enable the zero/zero lock</dl>
<p> -R range</p>
<dl>
<dt>
<dd> set lock range</dl>
<p> -B base</p>
<dl>
<dt>
<dd> set lock base</dl>
<p> -M min</p>
<dl>
<dt>
<dd> set min lock length</dl>
<p> -k</p>
<dl>
<dt>
<dd> Use kerberos</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> Samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> locktest was written by Andrew Tridgell. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Samba</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dl>
<dt> 2.</p>
<dd> Samba Team</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dl>
</dl>
<h2>Index</h2>
