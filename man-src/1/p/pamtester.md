---
title: "pamtester(1)"
name: "pamtester"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtester/"
description: "pamtester – test pluggable authentication module (PAM) facility"
---

<h2>NAME</h2>
<p> pamtester &#8211; test pluggable authentication module (PAM) facility</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtester</code> [-v] [-I <i>item</i>=<i>value</i>] [-E <i>var</i>=<i>value</i>] <i>service</i> <i>user</i> <i>operation</i> [<i>operation</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Test pluggable authentication module (PAM) facility. </p>
<p> <i>service</i> is the PAM service name. <i>user</i> is the name of the user account to operate with the PAM facility. The following operations are supported.</p>
<dl>
<dt>authenticate</p>
<dd> Authenticate <i>user</i>. A conversation may subsequently take place to prompt user input to retrieve necessary authentication information.</p>
<dt>acct_mgmt</p>
<dd> Perform account management on <i>user</i>. A conversation may subsequently take place to prompt user input for necessary authentication information.</p>
<dt>open_session</p>
<dd> Open a new session for <i>user</i>.</p>
<dt>close_session</p>
<dd> Close the current session for <i>user</i>.</p>
<dt>chauthtok</p>
<dd> Change the authentication token currently assigned to <i>user</i>. Conversation may subsequently take place to prompt user input for necessary authentication information.</dl>
<p> Note that some operations may eventually need additional privileges to fulfill the request depending on the service configuration. </p>
<p> Any operation may also be followed by the option flags that are provided between the pair of parenthesis. Flags are all named and combinable or inversible with bitwise operators; &quot;|&quot; (OR), &quot;&amp;&quot; (AND), &quot;^&quot; (XOR) and &quot;~&quot; (NOT) are accepted.</p>
<dl>
<dt>
<dd> authenticate(PAM_SILENT | PAM_DISALLOW_NULL_AUTHTOK)</dl>
<p> The list of allowed options is shown below:</p>
<dl>
<dt>&#8211;</p>
<dd> PAM_SILENT</p>
<dt>&#8211;</p>
<dd> PAM_DISALLOW_NULL_AUTHTOK</p>
<dt>&#8211;</p>
<dd> PAM_ESTABLISH_CRED</p>
<dt>&#8211;</p>
<dd> PAM_REINITIALIZE_CRED</p>
<dt>&#8211;</p>
<dd> PAM_REFRESH_CRED</p>
<dt>&#8211;</p>
<dd> PAM_CHANGE_EXPIRED_AUTHTOK</dl>
<p> Additional authentication information such as the name of the remote user, the remote host and the tty can be supplied via <i>-I</i> (<i>&#8211;item</i>) option. </p>
<p> The following types of information are supported:</p>
<dl>
<dt>&#8211;</p>
<dd> service</p>
<dt>&#8211;</p>
<dd> user</p>
<dt>&#8211;</p>
<dd> prompt</p>
<dt>&#8211;</p>
<dd> tty</p>
<dt>&#8211;</p>
<dd> ruser</p>
<dt>&#8211;</p>
<dd> rhost </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Turn on verbose mode.</p>
<dt><code>-I</code> <i>item</i>=<i>value</i>, <code>&#8211;item</code> <i>item</i>=<i>value</i></p>
<dd> Provide additional information to authentication module.</p>
<dt><code>-E</code> <i>var</i>=<i>value</i>, <code>&#8211;env</code> <i>var</i>=<i>value</i></p>
<dd> Set environment variable <i>var</i> to <i>value</i></dl>
<h2>AUTHOR</h2>
<p> Written by Moriyoshi Koizumi &lt;moriyoshi [at] users.sourceforge.net&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;pamtester-bugs [at] lists.sourceforge.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004 &#8211; 2005 Moriyoshi Koizumi. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7) </p>
<h2>Index</h2>
