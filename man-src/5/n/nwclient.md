---
title: "nwclient(5)"
name: "nwclient"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nwclient/"
description: "nwclient – configuration file for NWClient program suite"
---

<p>nwclient &#8211; configuration file for NWClient program suite</p>
<h2>Description</h2>
<p>This manual page describes the rather simple format of the file <code>$HOME/.nwclient,</code> the configuration file for the NWClient program suite.</p>
<h2>File Format</h2>
<p>The file <code>$HOME/.nwclient</code> consists of several lines, each describing a NWClient connection. Lines beginning with # and empty lines are ignored as comments. </p>
<p> Because you can store passwords in .nwclient, the user programs will only scan .nwclient when only the file owner has access rights to the file. The file must be have permissions 0600. </p>
<p> To specify a NWClient connection, the name of the file server, the user name to be used and a password is necessary. The server name and the user name are specified as SERVER/USER, and the password is separated by a blank. The password field can be omitted. In this case the user programs will ask you for a password. If you specify the password to be just a dash, then no password is used. </p>
<p> The first valid specification has a special meaning: If the user does not name a server on the command line, the first specification is used as a &#8216;preferred connection&#8217;. </p>
<p> An example might be the following: </p>
<p>#&nbsp;<wbr>The preferred connection, the user is asked<br />
#&nbsp;<wbr>for a password<br />
FS311/ME<br />
#&nbsp;<wbr>And a passwordless account on another server&nbsp;<wbr><br />
CD-SERV/GUEST &#8211; </p>
<p> With these lines in $HOME/.nwclient, calling &#8216;ncpmount /mnt&#8217; will mount the the file server FS311 with user name ME on /mnt after asking the user for a password. </p>
<p> <i>ncpmount -S cd-serv /cd</i> will silently mount the server cd-serv on /cd. </p>
<p> <code>nprint</code>, <code>pqlist</code> and other user programs that require a valid login also look up <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. </p>
<p> Please note that the access permissions of .nwclient MUST be 600, for security reasons.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/1-nprint/">nprint</a>(1)</code> </p>
