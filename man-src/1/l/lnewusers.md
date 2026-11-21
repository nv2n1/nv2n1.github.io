---

title: "lnewusers(1)"
name: "lnewusers"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lnewusers/"
description: "lnewusers – Create new user accounts"
---

<p> lnewusers &#8211; Create new user accounts</p>
<h2>SYNOPSIS</h2>
<p> lnewusers [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> Creates new user accounts using data read from standard input. </p>
<p> The input data consists of lines, each line has 7 colon-separated fields: </p>
<dl>
<dt>User name</dt>
<dd>
</dd><dt>Plaintext password</dt>
<dd>
</dd><dt>User ID</dt>
<dd> <code>lnewusers</code> refuses to create users with user ID 0 (the <code>root</code> user ID). </dd>
<dt>Group</dt>
<dd> If this field is a valid group ID, it is interpreted as a group ID, otherwise as a group name. If the field is empty, a group name equal to user name is used. </dd>
<p> If the specified group does not exist, it is automatically created. If the group is specified with a group ID, the created group has group name equal to the user name. </p>
<dt>GECOS</dt>
<dd> The GECOS field is traditionally used to store user&#8217;s real name and other information. </dd>
<dt>Home directory</dt>
<dd> If this field is empty, a default specified by <code>libuser</code> configuration, or <code>/home/</code><i>username</i> if <code>libuser</code> configuration does not specify a default, is used. </dd>
<dt>Login shell</dt>
<dd> If this field is empty, a default specified by <code>libuser</code> configuration is used. </dd>
</dl>
<p> Errors in user specifications are reported and processing continues on the next line. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>file</i></dt>
<dd> Read account data from <i>file</i> instead of standard input. </dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </dd>
<dt><code>-M</code>, <code>&#8211;nocreatehome</code></dt>
<dd> Don&#8217;t create home directories. </dd>
<dt><code>-n</code>, <code>&#8211;nocreatemail</code></dt>
<dd> Don&#8217;t create mail spool files. </dd>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on fatal error. Errors in user specifications are not reflected in the exit status. </p>
