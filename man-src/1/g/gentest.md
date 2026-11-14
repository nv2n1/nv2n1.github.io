---
title: "gentest(1)"
name: "gentest"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gentest/"
description: "gentest – Run random generic SMB operations against two SMB servers and show the differences in behavior"
---

<h2 class="name">NAME</h2>
<p> gentest &#8211; Run random generic SMB operations against two SMB servers and show the differences in behavior </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gentest</code> {//server1/share1} {//server2/share2} {-U user%pass} {-U user%pass} [-s seed] [-o numops] [-a] [-A] [-i FILE] [-O] [-S FILE] [-L] [-F] [-C] [-X]</dl>
<h2>DESCRIPTION</h2>
<dd>gentest is a utility for detecting differences in behaviour between SMB servers. It will run a random set of generic operations against <i>//server1/share1</i> and then the same random set against <i>//server2/share2</i> and display the differences in the responses it gets. </p>
<p> This utility is used by the Samba team to find differences in behaviour between Samba and Windows servers.</p>
<h2>OPTIONS</h2>
<p> -U user%pass</p>
<dl>
<dt>
<dd> Specify the user and password to use when logging on on the shares. This parameter is mandatory and has to be specified twice.</dl>
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
<p> -i FILE</p>
<dl>
<dt>
<dd> Specify a file containing the names of fields that have to be ignored (such as time fields). See below for a description of the file format.</dl>
<p> -O</p>
<dl>
<dt>
<dd> Enable oplocks.</dl>
<p> -S FILE</p>
<dl>
<dt>
<dd> Set preset seeds file. The default is gentest_seeds.dat.</dl>
<p> -L</p>
<dl>
<dt>
<dd> Use preset seeds</dl>
<p> -F</p>
<dl>
<dt>
<dd> Fast reconnect (just close files)</dl>
<p> -C</p>
<dl>
<dt>
<dd> Continuous analysis mode</dl>
<p> -X</p>
<dl>
<dt>
<dd> Analyse even when the test succeeded.</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> Samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> gentest was written by Andrew Tridgell. </p>
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
