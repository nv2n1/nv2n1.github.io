---
title: "netrc(5)"
name: "netrc"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netrc/"
description: "netrc – user configuration for ftp"
---

<p>Linux NetKit (0.17)</p>
<h2>Name</h2>
<p><code>netrc</code> &#8211; user configuration for ftp</p>
<h2>Synopsis</h2>
<p><code>~/.netrc</code></p>
<h2>Description</h2>
<p>This file contains configuration and autologin information for the File Transfer Protocol client <a href="/docs/linux/man/1-ftp/">ftp</a>(1). The .netrc file contains login and initialization information used by the auto-login process. It resides in the user&#8217;s home directory. The following tokens are recognized; they may be separated by spaces, tabs, or new-lines:</p>
<dl>
<dt><code>machine </code><i>name</i></p>
<dd>Identify a remote machine <i>name</i> The auto-login process searches the .netrc file for a <code>machine</code> token that matches the remote machine specified on the <code>ftp</code> command line or as an <code>open</code> command argument. Once a match is made, the subsequent .netrc tokens are processed, stopping when the end of file is reached or another <code>machine</code> or a <code>default</code> token is encountered.</p>
<dt><code>default</code></p>
<dd>This is the same as <code>machine</code> <i>name</i> except that <code>default</code> matches any name. There can be only one <code>default</code> token, and it must be after all <code>machine</code> tokens. This is normally used as: </p>
<blockquote><p><tt>default login anonymous password user [at] site</tt></p></blockquote>
<p> thereby giving the user <i>automatic</i> anonymous ftp login to machines not specified in .netrc This can be overridden by using the &#8211;<code>n</code> flag to disable auto-login.</p>
<dt><code>login </code><i>name</i></p>
<dd>Identify a user on the remote machine. If this token is present, the auto-login process will initiate a login using the specified <i>name</i></p>
<dt><code>password </code><i>string</i></p>
<dd>Supply a password. If this token is present, the auto-login process will supply the specified string if the remote server requires a password as part of the login process. Note that if this token is present in the .netrc file for any user other than <i>anonymous </i> <code>ftp</code> will abort the auto-login process if the .netrc is readable by anyone besides the user.</p>
<dt><code>account </code><i>string</i></p>
<dd>Supply an additional account password. If this token is present, the auto-login process will supply the specified string if the remote server requires an additional account password, or the auto-login process will initiate an <code>ACCT</code> command if it does not.</p>
<dt><code>macdef </code><i>name</i></p>
<dd>Define a macro. This token functions like the <code>ftp</code> <code>macdef</code> command functions. A macro is defined with the specified name; its contents begin with the next .netrc line and continue until a null line (consecutive new-line characters) is encountered. If a macro named <code>init</code> is defined, it is automatically executed as the last step in the auto-login process.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/8-ftpd/">ftpd</a>(8) </p>
