---
title: "cimuser(8)"
name: "cimuser"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimuser/"
description: "cimuser – add, modify, remove, or list CIM users"
---

<p>cimuser &#8211; add, modify, remove, or list CIM users</p>
<h2>Synopsis</h2>
<p><code>cimuser</code> <code>-a</code> <code>-u</code> username [ <code>-w</code> password ] <code>cimuser</code> <code>-m</code> <code>-u</code> username [ <code>-w</code> old password ] [ <code>-n</code> new password ] <code>cimuser</code> <code>-r</code> <code>-u</code> username <code>cimuser</code> <code>-l</code> <code>cimuser</code> <code>-h</code> <code>cimuser</code> <code>&#8211;help</code> <code>cimuser</code> <code>&#8211;version</code> </p>
<h2>Remarks</h2>
<p>This command can be executed only by privileged user(s).</p>
<h2>Description</h2>
<p>The <code>cimuser </code> command command provides a command line interface to manage CIM users. If the password is not specified at the command line, the user will be prompted for it. If more than 8 characters are entered for the password, then the first eight characters will be used. There is no default authorization permissions set for newly added users. For more information on adding authorization information see <a href="/docs/linux/man/8-cimauth/">cimauth</a>(8).</p>
<h3>Options</h3>
<p>The <code>cimuser</code> command recognizes the following options:</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>Add a new CIM user.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display command usage information.</p>
<dt><code>-l</code></p>
<dd>List the names of CIM users.</p>
<dt><code>-m</code></p>
<dd>Modify a CIM user password.</p>
<dt><code>-n</code></p>
<dd>Supply a new password for the specified user name. WARNING: Passwords should not be specified on the command line on a multi-user system, since command-line options are typically world-readable for a short window of time. If no password is provided on the command line, <code>cimuser </code> will prompt for one.</p>
<dt><code>-r</code></p>
<dd>Remove the specified CIM user.</p>
<dt><code>-u</code></p>
<dd>Specify a CIM user name.</p>
<dt><code>&#8211;version</code></p>
<dd>Display CIM Server version number.</p>
<dt><code>-w</code></p>
<dd>Supply a password for the specified user name. WARNING: Passwords should not be specified on the command line on a multi-user system, since command-line options are typically world-readable for a short window of time. If no password is provided on the command line, <code>cimuser </code> will prompt for one.</dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to stderr and an error value of 1 is returned. The following return values are returned:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Successful completion</p>
<dt><code>1</code></p>
<dd>Error</dl>
</dl>
<h2>Usage Note</h2>
<p>The <code>cimuser </code> command requires that the CIM Server is running.</p>
<h2>Examples</h2>
<p>The following command adds user &quot;guest&quot;, a new CIM user. The password for this user is &quot;guest&quot;.</p>
<dl>
<dd><code>cimuser -a -u guest -w guest</code></dl>
<p> The following command adds user &quot;guest&quot;, a new CIM user. Since the password is not specified on the command line, the user will be prompted for it.</p>
<dl>
<dd><code>cimuser -a -u guest </code> Please enter your password: Please re-enter your password:  The following command modifies the password for user &quot;guest&quot;, with the new password &quot;bar&quot;.</p>
<dl>
<dd><code>cimuser -m -u guest -w foo -n bar</code></dl>
<p> The following command removes the CIM user &quot;guest&quot;.</p>
<dl>
<dd><code>cimuser -r -u guest</code></dl>
<p> The following command displays the list of CIM user names.</p>
<dl>
<dd><code>cimuser -l</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8), <a href="/docs/linux/man/8-cimconfig/">cimconfig</a>(8). </p>
