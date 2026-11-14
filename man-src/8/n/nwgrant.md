---
title: "nwgrant(8)"
name: "nwgrant"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwgrant/"
description: "nwgrant – Add Trustee Rights to a directory"
---

<p>nwgrant &#8211; Add Trustee Rights to a directory</p>
<h2>Synopsis</h2>
<p><code>nwgrant</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-r</code> <i>rights</i> ] <code>file/directory</code> </p>
<h2>Description</h2>
<p><code>nwgrant</code> adds the specified bindery object with the corresponding trustee rights to the directory. <code>nwgrant</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd><code>-h</code> is used to print out a short help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dd><code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user</i></p>
<dl>
<dd><code>user</code> is the user name to use for login.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dd><code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwgrant prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dd><code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dd>By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-o</code> <i>object name</i></p>
<dl>
<dd>The name of the object to be added as trustee.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dd>The type of the object. <i>Object type</i> must be specified as a decimal value. Common values are 1 for user objects, 2 for group objects and 3 for print queues. Other values are allowed, but are usually used for specialized applications. If you do not specify <i>object type</i>, <i>object name</i> is taken as NDS name.</dl>
<p> <code>-r</code> <i>rights</i></p>
<dl>
<dd>You must tell <code>nwgrant</code> which rights it should grant to the bindery object. The new rights for the object is specified by <i>rights,</i> which can be either a hexadecimal number representing the sum of all the individual rights to be granted or a string containing characters representing each right. If rights are represented in string format then the string must be bounded with square brackets. Characters within the brackets may be in any order and in either case. Spaces are allowed between the brackets &#8211; in which case the entire string should be quoted. Hexadecimal and character values for the rights are shown in this table: </p>
<p>&nbsp;<wbr>00&nbsp;<wbr>=&nbsp;<wbr>no access<br />
&nbsp;<wbr>01&nbsp;<wbr>=&nbsp;<wbr>read access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>R<br />
&nbsp;<wbr>02&nbsp;<wbr>=&nbsp;<wbr>write access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>W<br />
&nbsp;<wbr>08&nbsp;<wbr>=&nbsp;<wbr>create access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>C<br />
&nbsp;<wbr>10&nbsp;<wbr>=&nbsp;<wbr>delete access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>E<br />
&nbsp;<wbr>20&nbsp;<wbr>=&nbsp;<wbr>ownership access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>A<br />
&nbsp;<wbr>40&nbsp;<wbr>=&nbsp;<wbr>search access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>F<br />
&nbsp;<wbr>80&nbsp;<wbr>=&nbsp;<wbr>modify access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>M<br />
100&nbsp;<wbr>=&nbsp;<wbr>supervisory access&nbsp;<wbr>=&nbsp;<wbr>S </p>
<p> for a possible total of &quot;1fb&quot; or &quot;[SRWCEMFA]&quot; for all rights.</dl>
<p> <code>file/directory</code></p>
<dl>
<dd>You must specify the directory to which to add the object as trustee. This has to be done in fully qualified NetWare notation. </p>
<p> Example: </p>
<p> nwgrant -S NWSERVER -o linus -t 1 -r fb &#8216;data:home\linus&#8217; </p>
<p> With this example, user linus is given all rights except supervisory to his home directory on the data volume. This example assumes the existence of the file $HOME/.nwclient. </p>
<p> nwgrant -o linus -t 1 -r fb /home/linus/ncpfs/data/home/linus </p>
<p> With this example, user linus is given all rights except supervisory to his home directory on the data volume. This example assumes that NWSERVER is already mounted on /home/linus/ncpfs mountpoint. </p>
</dl>
<h2>Authors</h2>
<p>nwgrant was written by Volker Lendecke with the corresponding NetWare utility in mind. See the Changes file of ncpfs for other contributors.</p>
