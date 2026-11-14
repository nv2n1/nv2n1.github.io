---
title: "htdbm(1)"
name: "htdbm"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htdbm/"
description: "htdbm – Manipulate DBM password databases"
---

<h2 class="name">NAME</h2>
<p> htdbm &#8211; Manipulate DBM password databases</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>htdbm</code> [ &#8211;<code>T</code><i>DBTYPE</i> ] [ &#8211;<code>i</code> ] [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>filename</i> <i>username</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>b</code> [ &#8211;<code>T</code><i>DBTYPE</i> ] [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>filename</i> <i>username</i> <i>password</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>n</code> [ &#8211;<code>i</code> ] [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>username</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>nb</code> [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>username</i> <i>password</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>v</code> [ &#8211;<code>T</code><i>DBTYPE</i> ] [ &#8211;<code>i</code> ] [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>filename</i> <i>username</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>vb</code> [ &#8211;<code>T</code><i>DBTYPE</i> ] [ &#8211;<code>c</code> ] [ &#8211;<code>m</code> | &#8211;<code>B</code> | &#8211;<code>d</code> | &#8211;<code>s</code> | &#8211;<code>p</code> ] [ &#8211;<code>C</code> <i>cost</i> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] <i>filename</i> <i>username</i> <i>password</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>x</code> [ &#8211;<code>T</code><i>DBTYPE</i> ] <i>filename</i> <i>username</i><br />
&nbsp; </p>
<p> <code>htdbm</code> &#8211;<code>l</code> [ &#8211;<code>T</code><i>DBTYPE</i> ]<br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>htdbm</code> is used to manipulate the DBM format files used to store usernames and password for basic authentication of HTTP users via mod_authn_dbm. See the dbmmanage documentation for more information about these DBM files.<br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-b</code></p>
<dd> Use batch mode; <i>i.e.</i>, get the password from the command line rather than prompting for it. This option should be used with extreme care, since <code>the password is clearly visible</code> on the command line. For script use see the <code>-i</code> option.</p>
<dt><code>-i</code></p>
<dd> Read the password from stdin without verification (for script usage).</p>
<dt><code>-c</code></p>
<dd> Create the <i>passwdfile</i>. If <i>passwdfile</i> already exists, it is rewritten and truncated. This option cannot be combined with the <code>-n</code> option.</p>
<dt><code>-n</code></p>
<dd> Display the results on standard output rather than updating a database. This option changes the syntax of the command line, since the <i>passwdfile</i> argument (usually the first one) is omitted. It cannot be combined with the <code>-c</code> option.</p>
<dt><code>-m</code></p>
<dd> Use MD5 encryption for passwords. On Windows and Netware, this is the default.</p>
<dt><code>-B</code></p>
<dd> Use bcrypt encryption for passwords. This is currently considered to be very secure.</p>
<dt><code>-C</code></p>
<dd> This flag is only allowed in combination with <code>-B</code> (bcrypt encryption). It sets the computing time used for the bcrypt algorithm (higher is more secure but slower, default: 5, valid: 4 to 31).</p>
<dt><code>-d</code></p>
<dd> Use <code>crypt()</code> encryption for passwords. The default on all platforms but Windows and Netware. Though possibly supported by <code>htdbm</code> on all platforms, it is not supported by the httpd server on Windows and Netware. This algorithm is <code>insecure</code> by today&#8217;s standards.</p>
<dt><code>-s</code></p>
<dd> Use SHA encryption for passwords. Facilitates migration from/to Netscape servers using the LDAP Directory Interchange Format (ldif). This algorithm is <code>insecure</code> by today&#8217;s standards.</p>
<dt><code>-p</code></p>
<dd> Use plaintext passwords. Though <code>htdbm</code> will support creation on all platforms, the httpd daemon will only accept plain text passwords on Windows and Netware.</p>
<dt><code>-l</code></p>
<dd> Print each of the usernames and comments from the database on stdout.</p>
<dt><code>-v</code></p>
<dd> Verify the username and password. The program will print a message indicating whether the supplied password is valid. If the password is invalid, the program exits with error code 3.</p>
<dt><code>-x</code></p>
<dd> Delete user. If the username exists in the specified DBM file, it will be deleted.</p>
<dt><code>-t</code></p>
<dd> Interpret the final parameter as a comment. When this option is specified, an additional string can be appended to the command line; this string will be stored in the &quot;Comment&quot; field of the database, associated with the specified username.</p>
<dt><i>filename</i></p>
<dd> The filename of the DBM format file. Usually without the extension <code>.db</code>, <code>.pag</code>, or <code>.dir</code>. If <code>-c</code> is given, the DBM file is created if it does not already exist, or updated if it does exist.</p>
<dt><i>username</i></p>
<dd> The username to create or update in <i>passwdfile</i>. If <i>username</i> does not exist in this file, an entry is added. If it does exist, the password is changed.</p>
<dt><i>password</i></p>
<dd> The plaintext password to be encrypted and stored in the DBM file. Used only with the <code>-b</code> flag.</p>
<dt><code>-T</code><i>DBTYPE</i></p>
<dd> Type of DBM file (SDBM, GDBM, DB, or &quot;default&quot;).<br />
&nbsp;</dl>
<h2>BUGS</h2>
<p>&nbsp; </p>
<p> One should be aware that there are a number of different DBM file formats in existence, and with all likelihood, libraries for more than one format may exist on your system. The three primary examples are SDBM, NDBM, GNU GDBM, and Berkeley/Sleepycat DB 2/3/4. Unfortunately, all these libraries use different file formats, and you must make sure that the file format used by <i>filename</i> is the same format that <code>htdbm</code> expects to see. <code>htdbm</code> currently has no way of determining what type of DBM file it is looking at. If used against the wrong format, will simply return nothing, or may create a different DBM file with a different name, or at worst, it may corrupt the DBM file if you were attempting to write to it.<br />
&nbsp; </p>
<p> One can usually use the <code>file</code> program supplied with most Unix systems to see what format a DBM file is in.<br />
&nbsp;</p>
<h2>EXIT STATUS</h2>
<p>&nbsp; </p>
<p> <code>htdbm</code> returns a zero status (&quot;true&quot;) if the username and password have been successfully added or updated in the DBM File. <code>htdbm</code> returns <code>1</code> if it encounters some problem accessing files, <code>2</code> if there was a syntax problem with the command line, <code>3</code> if the password was entered interactively and the verification entry didn&#8217;t match, <code>4</code> if its operation was interrupted, <code>5</code> if a value is too long (username, filename, password, or final computed record), <code>6</code> if the username contains illegal characters (see the Restrictions section), and <code>7</code> if the file is not a valid DBM password file.<br />
&nbsp;</p>
<h2>EXAMPLES</h2>
<p>&nbsp; </p>
<pre>
      htdbm /usr/local/etc/apache/.htdbm-users jsmith
    
</pre>
<p>&nbsp; </p>
<p> Adds or modifies the password for user <code>jsmith</code>. The user is prompted for the password. If executed on a Windows system, the password will be encrypted using the modified Apache MD5 algorithm; otherwise, the system&#8217;s <code>crypt()</code> routine will be used. If the file does not exist, <code>htdbm</code> will do nothing except return an error.<br />
&nbsp; </p>
<pre>
      htdbm -c /home/doe/public_html/.htdbm jane
    
</pre>
<p>&nbsp; </p>
<p> Creates a new file and stores a record in it for user <code>jane</code>. The user is prompted for the password. If the file exists and cannot be read, or cannot be written, it is not altered and <code>htdbm</code> will display a message and return an error status.<br />
&nbsp; </p>
<pre>
      htdbm -mb /usr/web/.htdbm-all jones Pwd4Steve
    
</pre>
<p>&nbsp; </p>
<p> Encrypts the password from the command line (<code>Pwd4Steve</code>) using the MD5 algorithm, and stores it in the specified file.<br />
&nbsp;</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p>&nbsp; </p>
<p> Web password files such as those managed by <code>htdbm</code> should <i>not</i> be within the Web server&#8217;s URI space &#8212; that is, they should not be fetchable with a browser.<br />
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
<p> On the Windows platform, passwords encrypted with <code>htdbm</code> are limited to no more than <code>255</code> characters in length. Longer passwords will be truncated to 255 characters.<br />
&nbsp; </p>
<p> The MD5 algorithm used by <code>htdbm</code> is specific to the Apache software; passwords encrypted using it will not be usable with other Web servers.<br />
&nbsp; </p>
<p> Usernames are limited to <code>255</code> bytes and may not include the character <code>:</code>.<br />
&nbsp; </p>
<h2>Index</h2>
