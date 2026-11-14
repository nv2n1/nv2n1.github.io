---
title: "htpasswd(1)"
name: "htpasswd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htpasswd/"
description: "htpasswd – Manage user files for basic authentication"
---

<h2 class="name">NAME</h2>
<p> htpasswd &#8211; Manage user files for basic authentication</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>htpasswd</code> [ &#8211;<code>c</code> ] [ &#8211;<code>i</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>D</code> ] [ &#8211;<code>v</code> ] <i>passwdfile</i> <i>username</i><br />
&nbsp; </p>
<p> <code>htpasswd</code> &#8211;<code>b</code> [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>D</code> ] [ &#8211;<code>v</code> ] <i>passwdfile</i> <i>username</i> <i>password</i><br />
&nbsp; </p>
<p> <code>htpasswd</code> &#8211;<code>n</code> [ &#8211;<code>i</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] <i>username</i><br />
&nbsp; </p>
<p> <code>htpasswd</code> &#8211;<code>nb</code> [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] <i>username</i> <i>password</i><br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>htpasswd</code> is used to create and update the flat-files used to store usernames and password for basic authentication of HTTP users. If <code>htpasswd</code> cannot access a file, such as not being able to write to the output file or not being able to read the file in order to update it, it returns an error status and makes no changes.<br />
&nbsp; </p>
<p> Resources available from the Apache HTTP server can be restricted to just the users listed in the files created by <code>htpasswd</code>. This program can only manage usernames and passwords stored in a flat-file. It can encrypt and display password information for use in other types of data stores, though. To use a DBM database see dbmmanage or htdbm.<br />
&nbsp; </p>
<p> <code>htpasswd</code> encrypts passwords using either bcrypt, a version of MD5 modified for Apache, SHA1, or the system&#8217;s <code>crypt()</code> routine. Files managed by <code>htpasswd</code> may contain a mixture of different encoding types of passwords; some user records may have bcrypt or MD5-encrypted passwords while others in the same file may have passwords encrypted with <code>crypt()</code>.<br />
&nbsp; </p>
<p> This manual page only lists the command line arguments. For details of the directives necessary to configure user authentication in httpd see the Apache manual, which is part of the Apache distribution or can be found at <a rel="nofollow" href="http://httpd.apache.org/.">http://httpd.apache.org/.</a><br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-b</code></p>
<dd> Use batch mode; <i>i.e.</i>, get the password from the command line rather than prompting for it. This option should be used with extreme care, since <code>the password is clearly visible</code> on the command line. For script use see the <code>-i</code> option. Available in 2.4.4 and later.</p>
<dt><code>-i</code></p>
<dd> Read the password from stdin without verification (for script usage).</p>
<dt><code>-c</code></p>
<dd> Create the <i>passwdfile</i>. If <i>passwdfile</i> already exists, it is rewritten and truncated. This option cannot be combined with the <code>-n</code> option.</p>
<dt><code>-n</code></p>
<dd> Display the results on standard output rather than updating a file. This is useful for generating password records acceptable to Apache for inclusion in non-text data stores. This option changes the syntax of the command line, since the <i>passwdfile</i> argument (usually the first one) is omitted. It cannot be combined with the <code>-c</code> option.</p>
<dt><code>-m</code></p>
<dd> Use MD5 encryption for passwords. This is the default (since version 2.2.18).</p>
<dt><code>-B</code></p>
<dd> Use bcrypt encryption for passwords. This is currently considered to be very secure.</p>
<dt><code>-C</code></p>
<dd> This flag is only allowed in combination with <code>-B</code> (bcrypt encryption). It sets the computing time used for the bcrypt algorithm (higher is more secure but slower, default: 5, valid: 4 to 17).</p>
<dt><code>-d</code></p>
<dd> Use <code>crypt()</code> encryption for passwords. This is not supported by the httpd server on Windows and Netware. This algorithm limits the password length to 8 characters. This algorithm is <code>insecure</code> by today&#8217;s standards. It used to be the default algorithm until version 2.2.17.</p>
<dt><code>-s</code></p>
<dd> Use SHA encryption for passwords. Facilitates migration from/to Netscape servers using the LDAP Directory Interchange Format (ldif). This algorithm is <code>insecure</code> by today&#8217;s standards.</p>
<dt><code>-p</code></p>
<dd> Use plaintext passwords. Though <code>htpasswd</code> will support creation on all platforms, the httpd daemon will only accept plain text passwords on Windows and Netware.</p>
<dt><code>-D</code></p>
<dd> Delete user. If the username exists in the specified htpasswd file, it will be deleted.</p>
<dt><code>-v</code></p>
<dd> Verify password. Verify that the given password matches the password of the user stored in the specified htpasswd file. Available in 2.4.5 and later.</p>
<dt><i>passwdfile</i></p>
<dd> Name of the file to contain the user name and password. If <code>-c</code> is given, this file is created if it does not already exist, or rewritten and truncated if it does exist.</p>
<dt><i>username</i></p>
<dd> The username to create or update in <i>passwdfile</i>. If <i>username</i> does not exist in this file, an entry is added. If it does exist, the password is changed.</p>
<dt><i>password</i></p>
<dd> The plaintext password to be encrypted and stored in the file. Only used with the <code>-b</code> flag.<br />
&nbsp;</dl>
<h2>EXIT STATUS</h2>
<p>&nbsp; </p>
<p> <code>htpasswd</code> returns a zero status (&quot;true&quot;) if the username and password have been successfully added or updated in the <i>passwdfile</i>. <code>htpasswd</code> returns <code>1</code> if it encounters some problem accessing files, <code>2</code> if there was a syntax problem with the command line, <code>3</code> if the password was entered interactively and the verification entry didn&#8217;t match, <code>4</code> if its operation was interrupted, <code>5</code> if a value is too long (username, filename, password, or final computed record), <code>6</code> if the username contains illegal characters (see the Restrictions section), and <code>7</code> if the file is not a valid password file.<br />
&nbsp;</p>
<h2>EXAMPLES</h2>
<p>&nbsp; </p>
<pre>
      htpasswd /usr/local/etc/apache/.htpasswd-users jsmith
    
</pre>
<p>&nbsp; </p>
<p> Adds or modifies the password for user <code>jsmith</code>. The user is prompted for the password. The password will be encrypted using the modified Apache MD5 algorithm. If the file does not exist, <code>htpasswd</code> will do nothing except return an error.<br />
&nbsp; </p>
<pre>
      htpasswd -c /home/doe/public_html/.htpasswd jane
    
</pre>
<p>&nbsp; </p>
<p> Creates a new file and stores a record in it for user <code>jane</code>. The user is prompted for the password. If the file exists and cannot be read, or cannot be written, it is not altered and <code>htpasswd</code> will display a message and return an error status.<br />
&nbsp; </p>
<pre>
      htpasswd -db /usr/web/.htpasswd-all jones Pwd4Steve
    
</pre>
<p>&nbsp; </p>
<p> Encrypts the password from the command line (<code>Pwd4Steve</code>) using the <code>crypt()</code> algorithm, and stores it in the specified file.<br />
&nbsp;</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p>&nbsp; </p>
<p> Web password files such as those managed by <code>htpasswd</code> should <i>not</i> be within the Web server&#8217;s URI space &#8212; that is, they should not be fetchable with a browser.<br />
&nbsp; </p>
<p> This program is not safe as a setuid executable. Do <i>not</i> make it setuid.<br />
&nbsp; </p>
<p> The use of the <code>-b</code> option is discouraged, since when it is used the unencrypted password appears on the command line.<br />
&nbsp; </p>
<p> When using the <code>crypt()</code> algorithm, note that only the first 8 characters of the password are used to form the password. If the supplied password is longer, the extra characters will be silently discarded.<br />
&nbsp; </p>
<p> The SHA encryption format does not use salting: for a given password, there is only one encrypted representation. The <code>crypt()</code> and MD5 formats permute the representation by prepending a random salt string, to make dictionary attacks against the passwords more difficult.<br />
&nbsp; </p>
<p> The SHA and <code>crypt()</code> formats are insecure by today&#8217;s standards.<br />
&nbsp;</p>
<h2>RESTRICTIONS</h2>
<p>&nbsp; </p>
<p> On the Windows platform, passwords encrypted with <code>htpasswd</code> are limited to no more than <code>255</code> characters in length. Longer passwords will be truncated to 255 characters.<br />
&nbsp; </p>
<p> The MD5 algorithm used by <code>htpasswd</code> is specific to the Apache software; passwords encrypted using it will not be usable with other Web servers.<br />
&nbsp; </p>
<p> Usernames are limited to <code>255</code> bytes and may not include the character <code>:</code>.<br />
&nbsp; </p>
<p> The cost of computing a bcrypt password hash value increases with the number of rounds specified by the <code>-C</code> option. The <code>apr-util</code> library enforces a maximum number of rounds of 17 in version <code>1.6.0</code> and later.<br />
&nbsp; </p>
<h2>Index</h2>
