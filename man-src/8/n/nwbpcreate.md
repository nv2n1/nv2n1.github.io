---
title: "nwbpcreate(8)"
name: "nwbpcreate"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwbpcreate/"
description: "nwbpcreate – Create a NetWare Bindery Propery"
---

<p>nwbpcreate &#8211; Create a NetWare Bindery Propery</p>
<h2>Synopsis</h2>
<p><code>nwbpcreate</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-o</code> <i>object name</i> ] [ <code>-t</code> <i>type</i> ] [ <code>-p</code> <i>property</i> ] [ <code>-s</code> ] [ <code>-r</code> <i>read-flag</i> ] [ <code>-w</code> <i>write-flag</i> ] </p>
<h2>Description</h2>
<p><code>nwbpcreate</code> creates the specified NetWare Bindery Propery. <code>nwbpcreate</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of $HOME/.nwclient MUST be 600 for security reasons. </p>
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
<dd><code>password</code> is the password to use for login. If neither <code>-n</code> nor <code>-P</code> are given, and the user has no open connection to the server, nwbpcreate prompts for a password.</dl>
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
<dd>The name of the property to be created.</dl>
<p> <code>-s</code></p>
<dl>
<dd>By default, <code>nwbpcreate</code> creates properties of type ITEM. If you want to create a property of type SET, such as groups_i\&#8217;m_in, you must use the <code>-s</code> option.</dl>
<p> <code>-r</code> <i>read-flag</i> </p>
<p> <code>-w</code> <i>write-flag</i></p>
<dl>
<dd>Read security and write security may each have one of the following values: </p>
<p>&nbsp;<wbr>ANYONE:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Anyone may access the property<br />
&nbsp;<wbr>LOGGED:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Anyone who is logged in may access the&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property<br />
&nbsp;<wbr>OBJECT:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Anyone who is logged in as the object or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SUPERVISOR equivalent may access the&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property<br />
&nbsp;<wbr>SUPERVISOR: Anyone who is logged in as SUPERVISOR&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>equivalent may access the property<br />
&nbsp;<wbr>NETWARE:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Only the Bindery may access the property</dl>
<h2>Authors</h2>
<p>nwbpcreate was written by Volker Lendecke with the corresponding Caldera utility in mind. See the Changes file of ncpfs for other contributors.</p>
