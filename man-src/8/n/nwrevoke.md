---
title: "nwrevoke(8)"
name: "nwrevoke"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwrevoke/"
description: "nwrevoke – Revoke a Trustee Right from a directory"
---

<p>nwrevoke &#8211; Revoke a Trustee Right from a directory</p>
<h2>Synopsis</h2>
<p><code>nwrevoke</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-r</code> <i>rights</i> ] <code>file/directory</code> </p>
<h2>Description</h2>
<p><code>nwrevoke</code> revokes the specified bindery object with the corresponding trustee rights from the directory. <code>nwrevoke</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd><code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwrevoke prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dd><code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dd>By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C</code>.</dl>
<p> <code>-o</code> <i>object name</i></p>
<dl>
<dd>The name of the object to be added as trustee.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dd>The type of the object. <i>Object type</i> must be specified as a decimal value. Common values are 1 for user objects, 2 for group objects and 3 for print queues. Other values are allowed, but are usually used for specialized applications. If <i>object type</i> is not specified, <i>object name</i> is taken as <code>NDS</code> name.</dl>
<p> <code>file/directory</code></p>
<dl>
<dd>You must specify the file/directory from which to remove the object as trustee. If you specified <code>-S</code>, it must be fully qualified NetWare notation for DOS namespace. Otherwise it must be file or directory mounted to your system using ncpfs. </p>
<p> Example: </p>
<p> nwrevoke -S NWSERVER -o linus -t 1 &#8216;src:bsd_src&#8217; </p>
<p> With this example, user linus is removed as trustee from the bsd_src directory on the src volume on server NWSERVER. </p>
<p> nwrevoke -o linus -t 1 /home/vana/ncpfs/nwserver/src/bsd_src </p>
<p> With this example, user linus is removed as trustee from the bsd_src directory. </p>
</dl>
<h2>Authors</h2>
<p>nwrevoke was written by Volker Lendecke with the corresponding NetWare utility in mind. See the Changes file of ncpfs for other contributors.</p>
