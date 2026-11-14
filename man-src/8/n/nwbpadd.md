---
title: "nwbpadd(8)"
name: "nwbpadd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwbpadd/"
description: "nwbpadd – Set the value of a NetWare Bindery Property"
---

<p>nwbpadd &#8211; Set the value of a NetWare Bindery Property</p>
<h2>Synopsis</h2>
<p><code>nwbpadd</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-p</code> <i>property</i> ] <code>value</code> </p>
<h2>Description</h2>
<p><code>nwbpadd</code> sets the value of a ITEM type property, and adds bindery objects to a SET type property. <code>nwbpadd</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd><code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwbpadd prompts for a password.</dl>
<p> <code>-n</code></p>
<dl>
<dd><code>-n</code> should be given if no password is required for the login.</dl>
<p> <code>-C</code></p>
<dl>
<dd>By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<p> <code>-o</code> <i>object name</i></p>
<dl>
<dd>The name of the object to be touched.</dl>
<p> <code>-t</code> <i>object type</i></p>
<dl>
<dd>The type of the object. <i>Object type</i> must be specified as a decimal value. Common values are 1 for user objects, 2 for group objects and 3 for print queues. Other values are allowed, but are usually used for specialized applications.</dl>
<p> <code>-p</code> <i>property</i></p>
<dl>
<dd>The name of the property to be set.</dl>
<p> <code>value</code></p>
<dl>
<dd>If property is of type SET, value is an object id in hexadecimal notation. Otherwise, value is either a string value to be written, or a count of bytes to be written. The latter is assumed if more than one value argument is given. The count is decimal, and the following arguments are interpreted as bytes in hexadecimal notation. </p>
<p> Examples: </p>
<p> All these examples assume the existence of the file $HOME/.nwclient. Otherwise, the server and user would have to be specified. </p>
<p> nwbpadd -o linus -t 1 -p groups_i\&#8217;m_in 030a0002 </p>
<p> In this example, user linus is added to the group whose ID is 030a0002. Please note that the &#8216; has to be quoted. </p>
<p> nwbpadd -o linus -t 1 -p identification &quot;Linus Torvalds&quot; </p>
<p> User linus is given his real name :-). </p>
<p> nwbpadd -o linus -t 1 -p revision -v 04 00 00 01 0b </p>
<p> A new 4-byte binary value 0x0000010b (hi-lo order, no byte-swapping) is added to the &quot;REVISION&quot; property of the user &quot;linus&quot;. </p>
</dl>
<h2>Authors</h2>
<p>nwbpadd was written by Volker Lendecke with the corresponding Caldera utility in mind. See the Changes file of ncpfs for other contributors.</p>
