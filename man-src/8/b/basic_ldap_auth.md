---
title: "basic_ldap_auth(8)"
name: "basic_ldap_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_ldap_auth/"
description: "basic_ldap_auth – LDAP authentication helper for Squid"
---

<p>basic_ldap_auth &#8211; LDAP authentication helper for Squid</p>
<h2>Synopsis</h2>
<p><code>basic_ldap_auth</code> <code>-b base DN</code> <code>attribute</code> <code>]&nbsp;<wbr>[</code> options <code>]&nbsp;<wbr>[</code> LDAP server name <code>[:</code> port <code>]|</code> URI <code>]&#8230;</code><br />
 <code>basic_ldap_auth</code> <code>-b base DN</code> <code>LDAP search filter</code> <code>options</code> <code>]&nbsp;<wbr>[</code> LDAP server name <code>[:</code> port <code>]|</code> URI <code>]&#8230;</code></p>
<h2>Description</h2>
<p><code>basic_ldap_auth</code> allows Squid to connect to a LDAP directory to validate the user name and password of Basic HTTP authentication. LDAP options are specified as parameters on the command line, while the username(s) and password(s) to be checked against the LDAP directory are specified on subsequent lines of input to the helper, one username/password pair per line separated by a space. </p>
<p> As expected by the basic authentication construct of Squid, after specifying a username and password followed by a new line, this helper will produce either <code>OK</code> or <code>ERR</code> on the following line to show if the specified credentials are correct according to the LDAP directory. </p>
<p> The program has two major modes of operation. In the default mode of operation the users DN is constructed using the base DN and user attribute. In the other mode of operation a search filter is used to locate valid user DN&#8217;s below the base DN.</p>
<h2>Options</h2>
<dl>
<dt><code>-b basedn</code></p>
<dd><code>REQUIRED.</code> Specifies the base DN under which the users are located.</p>
<dt><code>-f filter</code></p>
<dd>LDAP search <code>filter</code> to locate the user DN. Required if the users are in a hierarchy below the base DN, or if the login name is not what builds the user specific part of the users DN.<br />
 The search filter can contain up to 15 occurrences of <code>%s</code> which will be replaced by the username, as in <code>for RFC2037 directories. For a detailed description of LDAP search</code> filter syntax see RFC2254.<br />
 Will crash if other <code>%</code> values than <code>%s</code> are used, or if more than 15 <code>%s</code> are used.</p>
<dt><code>-u userattr</code></p>
<dd>Specifies the name of the DN attribute that contains the username/login. Combined with the base DN to construct the users DN when no search filter is specified ( <code>-f</code> option). Defaults to <code>uid</code><br />
 <code>Note:</code> This can only be done if all your users are located directly under the same position in the LDAP tree and the login name is used for naming each user object. If your LDAP tree does not match these criterias or if you want to filter who are valid users then you need to use a search filter to search for your users DN ( <code>-f</code> option).</p>
<dt><code>-U passwordattr</code></p>
<dd>Use <i>ldap_compare</i> instead of <i>ldap_simple_bind</i> to verify the users password. <code>passwordattr</code> is the LDAP attribute storing the users password.</p>
<dt><code>-s base|one|sub</code></p>
<dd>Search scope when performing user DN searches specified by the <code>-f</code> option. Defaults to <code>sub</code> </p>
<dd><code>base</code> object only,</p>
<dd><code>one</code> level below the base object or</p>
<dd><code>sub</code>tree below the base object</p>
<dt><code>-D binddn -w password</code></p>
<dd>The DN and password to bind as while performing searches. Required by the <code>-f</code> flag if the directory does not allow anonymous searches.<br />
 As the password needs to be printed in plain text in your Squid configuration it is strongly recommended to use a account with minimal associated privileges. This to limit the damage in case someone could get hold of a copy of your Squid configuration file.</p>
<dt><code>-D binddn -W secretfile </code></p>
<dd>The DN and the name of a file containing the password to bind as while performing searches.<br />
 Less insecure version of the former parameter pair with two advantages: The password does not occur in the process listing, and the password is not being compromised if someone gets the squid configuration file without getting the secretfile.</p>
<dt><code>-P</code></p>
<dd>Use a persistent LDAP connection. Normally the LDAP connection is only open while validating a username to preserve resources at the LDAP server. This option causes the LDAP connection to be kept open, allowing it to be reused for further user validations. Recommended for larger installations.</p>
<dt><code>-O</code></p>
<dd>Only bind once per LDAP connection. Some LDAP servers do not allow re-binding as another user after a successful <i>ldap_bind.</i> The use of this option always opens a new connection for each login attempt. If combined with the <code>-P</code> option for persistent LDAP connection then the connection used for searching for the user DN is kept persistent but a new connection is opened to verify each users password once the DN is found.</p>
<dt><code>-R</code></p>
<dd>Do not follow referrals</p>
<dt><code>-a never|always|search|find</code></p>
<dd>when to dereference aliases. Defaults to <code>never</code></p>
<dd><code>never</code> dereference aliases (default), <code>always</code> dereference aliases, only while <code>search ing</code> or only to <code>find</code> the base object.</p>
<dt><code>-H ldap_uri</code></p>
<dd>Specity the LDAP server to connect to by LDAP URI (requires OpenLDAP libraries). Servers can also be specified last on the command line.</p>
<dt><code>-h ldap_server</code></p>
<dd>Specify the LDAP server to connect to. Servers can also be specified last on the command line.</p>
<dt><code>-p ldap_port</code></p>
<dd>Specify an alternate TCP port where the LDAP server is listening if other than the default LDAP port 389. Can also be specified within the server specification by using servername:port syntax.</p>
<dt><code>-v 2|3</code></p>
<dd>LDAP protocol version. Defaults to <code>3</code> if not specified.</p>
<dt><code>-Z</code></p>
<dd>Use TLS encryption</p>
<dt><code>-S certpath</code></p>
<dd>Enable LDAP over SSL (requires Netscape LDAP API libraries)</p>
<dt><code>-c connect_timeout</code></p>
<dd>Specify <code>timeout</code> used when connecting to LDAP servers (requires Netscape LDAP API libraries)</p>
<dt><code>-t search_timeout</code></p>
<dd>Specify time limit on LDAP search operations</p>
<dt><code>-d</code></p>
<dd>Debug mode where each step taken will get reported in detail. Useful for understanding what goes wrong if the results is not what is expected.</dl>
<h2>Configuration</h2>
<p>For directories using the RFC2307 layout with a single domain, all you need to specify is usually the base DN under where your users are located and the server name:</p>
<dl>
<dd>
<dl>
<dd><code>basic_ldap_auth -b ou=people,dc=your,dc=domain ldapserver</code></dl>
</dl>
<p> If you have sub-domains then you need to use a search filter approach to locate your user DNs as these can no longer be constructed directly from the base DN and login name alone:</p>
<dl>
<dd>
<dl>
<dd><code>basic_ldap_auth -b dc=your,dc=domain -f uid=%s ldapserver</code></dl>
</dl>
<p> And similarly if you only want to allow access to users having a specific attribute</p>
<dl>
<dd>
<dl>
<dd><code>basic_ldap_auth -b dc=your,dc=domain -f (&amp;(uid=%s)(specialattribute=value)) ldapserver</code></dl>
</dl>
<p> Or if the user attribute of the user DN is <code>cn</code> instead of <code>uid</code> and you do not want to have to search for the users then you could use something like the following example for Active Directory:</p>
<dl>
<dd>
<dl>
<dd><code>basic_ldap_auth -u cn -b cn=Users,dc=your,dc=domain ldapserver</code></dl>
</dl>
<p> If you want to search for the user DN and your directory does not allow anonymous searches then you must also use the <code>-D</code> and <code>-w</code> flags to specify a user DN and password to log in as to perform the searches, as in the following complex Active Directory example</p>
<dl>
<dd>
<dl>
<dd><code>basic_ldap_auth -P -R -b dc=your,dc=domain -D cn=squid,cn=users,dc=your,dc=domain -w secretsquidpassword -f (&amp;(userPrincipalName=%s)(objectClass=Person)) activedirectoryserver</code></dl>
</dl>
<p> <code>NOTE:</code> When constructing search filters it is strongly recommended to test the filter using <code>ldapsearch</code> before you attempt to use <code>basic_ldap_auth.</code> This to verify that the filter matches what you expect.</p>
<h2>Author</h2>
<p>This program is written by <i>Glenn Newton &lt;gnewton [at] wapiti.cisti.nrc.ca&gt;</i> <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i> This manual is written by <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt; </p>
<p> Or to your favorite LDAP list/friend if the question is more related to LDAP than Squid.</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 Your favorite LDAP documentation.<br />
 <code>RFC2254</code> &#8211; The String Representation of LDAP Search Filters,<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
