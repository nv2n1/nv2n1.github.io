---

title: "masktest(1)"
name: "masktest"
section: "1"
letter: "m"
url: "/docs/linux/man/1-masktest/"
description: "masktest – Find differences in wildcard matching between Samba’s implementation and that of a remote server."
---

<p> masktest &#8211; Find differences in wildcard matching between Samba&#8217;s implementation and that of a remote server. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>masktest</code> {//server/share} [-U user%pass] [-d debuglevel] [-W workgroup] [-n numloops] [-s seed] [-a] [-E] [-M max protocol] [-f filechars] [-m maskchars] [-v]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>masktest is a utility for detecting differences in behaviour between Samba&#8217;s own implementation and that of a remote server. It will run generate random filenames/masks and check if these match the same files they do on the remote file as they do on the local server. It will display any differences it finds. </dd>
<p> This utility is used by the Samba team to find differences in behaviour between Samba and Windows servers.</p>
<h2>OPTIONS</h2>
<p> -U user%pass</p>
<dl>
<dt>
</dt><dd> Specify the user and password to use when logging on on the shares. This parameter can be specified twice (once for the first server, once for the second).</dd></dl>
<p> -s seed</p>
<dl>
<dt>
</dt><dd> Seed the random number generator with the specified value.</dd></dl>
<p> -n numops</p>
<dl>
<dt>
</dt><dd> Set the number of operations to perform.</dd></dl>
<p> -a</p>
<dl>
<dt>
</dt><dd> Print the operations that are performed.</dd></dl>
<p> -M max_protocol</p>
<dl>
<dt>
</dt><dd> Maximum protocol to use.</dd></dl>
<p> -f</p>
<dl>
<dt>
</dt><dd> Specify characters that can be used when generating file names. Default: abcdefghijklm.</dd></dl>
<p> -E</p>
<dl>
<dt>
</dt><dd> Abort when difference in behaviour is found.</dd></dl>
<p> -m maskchars</p>
<dl>
<dt>
</dt><dd> Specify characters used for wildcards.</dd></dl>
<p> -v</p>
<dl>
<dt>
</dt><dd> Be verbose</dd></dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> Samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[][1] suite, which is developed by the global m[blue]<code>Samba Team</code>m[][2]. </p>
<p> masktest was written by Andrew Tridgell. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Samba</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dd></dl>
<dt> 2.</dt>
<dd> Samba Team</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dd></dl>
</dl>
