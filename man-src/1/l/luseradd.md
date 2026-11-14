---
title: "luseradd(1)"
name: "luseradd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luseradd/"
description: "luseradd – Add an user"
---

<h2 class="name">NAME</h2>
<p> luseradd &#8211; Add an user</p>
<h2>SYNOPSIS</h2>
<p> luseradd [<i>OPTION</i>]&#8230; <i>user</i> </p>
<h2>DESCRIPTION</h2>
<p> Adds an user with name <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;gecos</code>=<i>gecos</i></p>
<dd> Set the GECOS field to <i>gecos</i>. The GECOS field is traditionally used to store user&#8217;s real name and other information. </p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>directory</i></p>
<dd> Set user&#8217;s home directory to <i>directory</i>. If this option is not present, a default specified by <code>libuser</code> configuration is used. </p>
<dt><code>-g</code>, <code>&#8211;gid</code>=<i>group</i></p>
<dd> Set user&#8217;s primary group to <i>group</i>. <i>group</i> can either be a group ID of an existing group, or a group name; if <i>group</i> is a group name and the group does not exist, it is created. If the <code>&#8211;gid</code> option is not specified, the default group name is <i>user</i>. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-k</code>, <code>&#8211;skeleton</code>=<i>directory</i></p>
<dd> Populate the newly created user&#8217;s home directory with a copy of <i>directory</i>. If this option is not present, a default directory specified by <code>libuser</code> configuration, or <code>/etc/skel</code> if <code>libuser</code> configuration does not specify a default, is used. </p>
<dt><code>-M</code>, <code>&#8211;nocreatehome</code></p>
<dd> Don&#8217;t create a home directory and a mail spool for the newly created user. </p>
<dt><code>-n</code>, <code>&#8211;nocreategroup</code></p>
<dd> If a group is not specified using <code>-g</code>, use group name &quot;users&quot; instead of <i>user</i>. Note that despite the name of the option, the group will still be created if it does not exist. </p>
<dt><code>-P</code>, <code>&#8211;plainpassword</code>=<i>password</i></p>
<dd> Set <i>user</i>&#8216;s password to <i>password</i>. Note that the password can be viewed while running <code>luseradd</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>encrypted</i></p>
<dd> Set <i>user</i>&#8216;s password to the password represented by the hash <i>encrypted</i>. Note that the hash can be viewed while running <code>luseradd</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-r</code>, <code>&#8211;reserved</code></p>
<dd> The user is a system user. Users that are not marked as system user usually have automatically selected user IDs above a certain value (configured as <code>LU_UIDNUMBER</code> in <code><a href="/docs/linux/man/5-libuser-conf/">libuser.conf</a></code>(5)). This information is also passed to the <code>libuser</code> backends. This option implies the <code>-M</code> option. </p>
<dt><code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></p>
<dd> Set user&#8217;s login shell to <i>shell</i>. If this option is not present, a default specified by <code>libuser</code> configuration is used. </p>
<dt><code>-u</code>, <code>&#8211;uid</code>=<i>uid</i></p>
<dd> Use user ID <i>uid</i> for the newly created user. An user ID is selected automatically if this option is not present. </p>
<dt><code>&#8211;commonname</code>=<i>name</i></p>
<dd> Use common name <i>name</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;givenname</code>=<i>name</i></p>
<dd> Use given name <i>name</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;homephone</code>=<i>phone</i></p>
<dd> Use home telephone number <i>phone</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;roomnumber</code>=<i>room</i></p>
<dd> Use room number <i>room</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;surname</code>=<i>name</i></p>
<dd> Use surname <i>name</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
<dt><code>&#8211;telephonenumber</code>=<i>phone</i></p>
<dd> Use telephone number <i>phone</i> for the newly created user. This attribute is only supported in some backends (e.g.LDAP), and its support may have further limitations (e.g. LDAP schema rules). </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
