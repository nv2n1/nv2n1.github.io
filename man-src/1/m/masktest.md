---
title: "masktest(1)"
name: "masktest"
section: "1"
letter: "m"
url: "/docs/linux/man/1-masktest/"
description: "masktest – Find differences in wildcard matching between Samba’s implementation and that of a remote server."
---

<h2 class="name">NAME</h2>
<p> masktest &#8211; Find differences in wildcard matching between Samba&#8217;s implementation and that of a remote server. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>masktest</code> {//server/share} [-U user%pass] [-d debuglevel] [-W workgroup] [-n numloops] [-s seed] [-a] [-E] [-M max protocol] [-f filechars] [-m maskchars] [-v]</dl>
<h2>DESCRIPTION</h2>
<dd>masktest is a utility for detecting differences in behaviour between Samba&#8217;s own implementation and that of a remote server. It will run generate random filenames/masks and check if these match the same files they do on the remote file as they do on the local server. It will display any differences it finds. </p>
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
<p> -n numops</p>
<dl>
<dt>
<dd> Set the number of operations to perform.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Print the operations that are performed.</dl>
<p> -M max_protocol</p>
<dl>
<dt>
<dd> Maximum protocol to use.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Specify characters that can be used when generating file names. Default: abcdefghijklm.</dl>
<p> -E</p>
<dl>
<dt>
<dd> Abort when difference in behaviour is found.</dl>
<p> -m maskchars</p>
<dl>
<dt>
<dd> Specify characters used for wildcards.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Be verbose</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> Samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> masktest was written by Andrew Tridgell. </p>
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
