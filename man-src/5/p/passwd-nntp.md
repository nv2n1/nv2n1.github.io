---
title: "passwd-nntp(5)"
name: "passwd-nntp"
section: "5"
letter: "p"
url: "/docs/linux/man/5-passwd-nntp/"
---

passwd.nntp - Passwords for connecting to remote NNTP servers

<h2>Description</h2>

The file <i>pathetc</i>/passwd.nntp contains host / name / password triplets for use when authenticating client programs to <font SIZE="-1">NNTP</font> servers. This file is normally interpreted by <i>NNTPsendpassword()</i> in <i><a HREF="/docs/linux/man/3-libinn/">libinn</a></i>(3). Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should consist of three or four fields separated by colons: 

 <pre> host:name:password
 host:name:password:style</pre>The first field is the name of a host, and is matched in a case-insensitive manner. (No detailed matching, such as comparing <font SIZE="-1">IP</font> addresses, is done.) 

 The second field is a user name, and the third is a password. If either the username or password is empty, then that portion of the authentication will not occur. (For example, a server may require only a username, in which case the password is not necessary. Note that a username is mandatory with <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font>.) 

 The optional fourth field specifies the type of authentication to use. At present, the only recognized ``authentication style'' is <tt>&quot;authinfo&quot;</tt>; this is also the default. It means that <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font> commands are used to authenticate to the remote host. (These <font SIZE="-1">NNTP</font> commands are described in <font SIZE="-1">RFC</font>&nbsp;<wbr>4643.) 

 For example: 

 <pre> ## UUNET needs a password, MIT doesn't.
 mit.edu:bbn::authinfo
 uunet.uu.net:bbn:yoyoma:authinfo</pre>This file should not be world-readable.

<h2>History</h2>

Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. 

 <tt>$Id:</tt> passwd.nntp.pod 8822 2009-11-20 17:34:15Z iulius $

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a HREF="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a HREF="/docs/linux/man/3-libinn/">libinn</a></i>(3). 
