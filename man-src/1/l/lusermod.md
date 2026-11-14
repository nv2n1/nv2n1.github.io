---
title: "lusermod(1)"
name: "lusermod"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lusermod/"
description: "lusermod – Modify an user"
---

<h2 class="name">NAME</h2>
<p> lusermod &#8211; Modify an user</p>
<h2>SYNOPSIS</h2>
<p> lusermod [<i>OPTION</i>]&#8230; <i>user</i> </p>
<h2>DESCRIPTION</h2>
<p> Modifies the user with name <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;gecos</code>=<i>gecos</i></p>
<dd> Set <i>user</i>&#8216;s GECOS field to <i>gecos</i>. The GECOS field is traditionally used to store user&#8217;s real name and other information. </p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>directory</i></p>
<dd> Set <i>user</i>&#8216;s home directory to <i>directory</i>. </p>
<dt><code>-g</code>, <code>&#8211;gid</code>=<i>gid</i></p>
<dd> Change <i>user</i>&#8216;s primary group ID to <i>gid</i>. If group with ID <i>gid</i> does not exist, a warning is printed, but the operation is performed anyway. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-L</code>, <code>&#8211;lock</code></p>
<dd> Lock <i>user</i>&#8216;s account. This prevents logging in using <i>user</i>&#8216;s password. </p>
<dt><code>-l</code>, <code>&#8211;login</code>=<i>name</i></p>
<dd> Rename <i>user</i> to <i>name</i>. </p>
<dt><code>-m</code>, <code>&#8211;movedirectory</code></p>
<dd> After changing <i>user</i>&#8216;s home directory (using the <code>-d</code> option), move the old home directory to the new location. </p>
<dt><code>-P</code>, <code>&#8211;plainpassword</code>=<i>password</i></p>
<dd> Set <i>user</i>&#8216;s password to <i>password</i>. Note that the password can be viewed while running <code>lusermod</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>encrypted</i></p>
<dd> Set <i>user</i>&#8216;s password to the password represented by the hash <i>encrypted</i>. Note that the hash can be viewed while running <code>lusermod</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></p>
<dd> Set <i>user</i>&#8216;s login shell to <i>shell</i>. </p>
<dt><code>-U</code>, <code>&#8211;unlock</code></p>
<dd> Unlock <i>user</i>&#8216;s account. </p>
<dt><code>-u</code>, <code>&#8211;uid</code>=<i>uid</i></p>
<dd> Change <i>user</i>&#8216;s user ID to <i>uid</i>. </p>
<dt><code>&#8211;commonname</code>=<i>name</i></p>
<dd> Set <i>user</i>&#8216;s common name to <i>name</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;givenname</code>=<i>name</i></p>
<dd> Set <i>user</i>&#8216;s given name to <i>name</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;homephone</code>=<i>phone</i></p>
<dd> Set <i>user</i>&#8216;s home telephone number to <i>phone</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;roomnumber</code>=<i>room</i></p>
<dd> Set <i>user</i>&#8216;s room number to <i>room</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;surname</code>=<i>name</i></p>
<dd> Set <i>user</i>&#8216;s surname to <i>name</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;telephonenumber</code>=<i>phone</i></p>
<dd> Set <i>user</i>&#8216;s telephone number to <i>phone</i>. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
