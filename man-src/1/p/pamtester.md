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
<p> <code>pamtester</code> [-v] [-I <i>item</i>=<i>value</i>] [-E <i>var</i>=<i>value</i>] <i>service</i> <i>user</i> <i>operation</i> [<i>operation</i> &#8230;]</p>
<p> Test pluggable authentication module (PAM) facility. </p>
<p> <i>service</i> is the PAM service name. <i>user</i> is the name of the user account to operate with the PAM facility. The following operations are supported.</p>
<dl>
<dt>authenticate</dt>
<dd> Authenticate <i>user</i>. A conversation may subsequently take place to prompt user input to retrieve necessary authentication information.</dd>
<dt>acct_mgmt</dt>
<dd> Perform account management on <i>user</i>. A conversation may subsequently take place to prompt user input for necessary authentication information.</dd>
<dt>open_session</dt>
<dd> Open a new session for <i>user</i>.</dd>
<dt>close_session</dt>
<dd> Close the current session for <i>user</i>.</dd>
<dt>chauthtok</dt>
<dd> Change the authentication token currently assigned to <i>user</i>. Conversation may subsequently take place to prompt user input for necessary authentication information.</dd></dl>
<p> Note that some operations may eventually need additional privileges to fulfill the request depending on the service configuration. </p>
<p> Any operation may also be followed by the option flags that are provided between the pair of parenthesis. Flags are all named and combinable or inversible with bitwise operators; &quot;|&quot; (OR), &quot;&amp;&quot; (AND), &quot;^&quot; (XOR) and &quot;~&quot; (NOT) are accepted.</p>
<dl>
<dt>
</dt><dd> authenticate(PAM_SILENT | PAM_DISALLOW_NULL_AUTHTOK)</dd></dl>
<p> The list of allowed options is shown below:</p>
<dl>
<dt>&#8211;</dt>
<dd> PAM_SILENT</dd>
<dt>&#8211;</dt>
<dd> PAM_DISALLOW_NULL_AUTHTOK</dd>
<dt>&#8211;</dt>
<dd> PAM_ESTABLISH_CRED</dd>
<dt>&#8211;</dt>
<dd> PAM_REINITIALIZE_CRED</dd>
<dt>&#8211;</dt>
<dd> PAM_REFRESH_CRED</dd>
<dt>&#8211;</dt>
<dd> PAM_CHANGE_EXPIRED_AUTHTOK</dd></dl>
<p> Additional authentication information such as the name of the remote user, the remote host and the tty can be supplied via <i>-I</i> (<i>&#8211;item</i>) option. </p>
<p> The following types of information are supported:</p>
<dl>
<dt>&#8211;</dt>
<dd> service</dd>
<dt>&#8211;</dt>
<dd> user</dd>
<dt>&#8211;</dt>
<dd> prompt</dd>
<dt>&#8211;</dt>
<dd> tty</dd>
<dt>&#8211;</dt>
<dd> ruser</dd>
<dt>&#8211;</dt>
<dd> rhost </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Turn on verbose mode.</dd>
<dt><code>-I</code> <i>item</i>=<i>value</i>, <code>&#8211;item</code> <i>item</i>=<i>value</i></dt>
<dd> Provide additional information to authentication module.</dd>
<dt><code>-E</code> <i>var</i>=<i>value</i>, <code>&#8211;env</code> <i>var</i>=<i>value</i></dt>
<dd> Set environment variable <i>var</i> to <i>value</i></dd></dl>
<h2>AUTHOR</h2>
<p> Written by Moriyoshi Koizumi &lt;moriyoshi [at] users.sourceforge.net&gt;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;pamtester-bugs [at] lists.sourceforge.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004 &#8211; 2005 Moriyoshi Koizumi. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7) </p>
