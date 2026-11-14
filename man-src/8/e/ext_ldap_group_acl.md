---
title: "ext_ldap_group_acl(8)"
name: "ext_ldap_group_acl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ext_ldap_group_acl/"
description: "ext_ldap_group_acl – Squid LDAP external acl group helper"
---

<p>ext_ldap_group_acl &#8211; Squid LDAP external acl group helper </p>
<p> Version 2.18</p>
<h2>Synopsis</h2>
<p><code>ext_ldap_group_acl</code> <code>-b</code> base-DN <code>-f</code> filter <code>[</code> options <code>] [</code> server <code>[ &#8216;:&#8217; </code> port <code>] |</code> URI <code>] &#8230;</code></p>
<h2>Description</h2>
<p><code>ext_ldap_group_acl</code> allows Squid to connect to a LDAP directory to authorize users via LDAP groups. LDAP options are specified as parameters on the command line, while the username(s) and group(s) to be checked against the LDAP directory are specified on subsequent lines of input to the helper, one username/group pair per line separated by a space. </p>
<p> As expected by the <code>external_acl_type</code> construct of Squid, after specifying a username and group followed by a new line, this helper will produce either <code>OK</code> or <code>ERR</code> on the following line to show if the user is a member of the specified group. </p>
<p> The program operates by searching with a search filter based on the users user name and requested group, and if a match is found it is determined that the user belongs to the group.</p>
<h2>Options</h2>
<dl>
<dt><code>-a </code><i>never|always|search|find</i></p>
<dd>When to dereference aliases. Defaults to &#8216;never&#8217;</p>
<dd><code>never</code> dereference aliases (default), <code>always</code> dereference aliases, only while <code>search</code>ing or only to <code>find</code> the base object</p>
<dt><code>-b </code><i>basedn </i></p>
<dd><code>REQUIRED.</code> Specifies the base DN under which the groups are located.</p>
<dt><code>-B </code><i>basedn </i></p>
<dd>Specifies the base DN under which the users are located (if different)</p>
<dt><code>-c</code><i> connect_timeout</i></p>
<dd>Specify timeout used when connecting to LDAP servers (requires Netscape LDAP API libraries)</p>
<dt><code>-d</code></p>
<dd>Debug mode where each step taken will get reported in detail. Useful for understanding what goes wrong if the result is not what was expected.</p>
<dt><code>-D </code><i>binddn </i><code>-w </code><i>password</i></p>
<dd>The DN and password to bind as while performing searches. Required if the LDAP directory does not allow anonymous searches.</p>
<dd>As the password needs to be printed in plain text in your Squid configuration and will be sent on the command line to the helper it is strongly recommended to use a account with minimal associated privileges. This to limit the damage in case someone could get hold of a copy of your Squid configuration file or extracts the password used from a process listing.</p>
<dt><code>-D </code><i>binddn </i><code>-W </code><i>secretfile </i></p>
<dd>The DN and the name of a file containing the password to bind as while performing searches.</p>
<dd>Less insecure version of the former parameter pair with two advantages: The password does not occur in the process listing, and the password is not being compromised if someone gets the squid configuration file without getting the secretfile.</p>
<dt><code>-E </code><i>certpath</i></p>
<dd>Enable LDAP over SSL (requires Netscape LDAP API libraries)</p>
<dt><code>-f </code><i>filter</i></p>
<dd>LDAP search filter used to search the LDAP directory for any matching group memberships. In the filter <code>%u</code> will be replaced by the user name (or DN if the <code>-F</code> or <code>-u</code> options are used) and <code>%g</code> by the requested group name.</p>
<dt><code>-F </code><i>filter</i></p>
<dd>LDAP search filter used to search the LDAP directory for any matching users. In the filter <code>%s</code> will be replaced by the user name. If <code>%</code> is to be included literally in the filter then use <code>%%</code></p>
<dt><code>-g</code></p>
<dd>Specifies that the first query argument sent to the helper by Squid is a extension to the basedn and will be temporarily added in front of the global basedn for this query.</p>
<dt><code>-h</code><i> ldapserver</i></p>
<dd>Specify the LDAP server to connect to</p>
<dt><code>-H</code><i> ldapuri</i></p>
<dd>Specity the LDAP server to connect to by a LDAP URI (requires OpenLDAP libraries)</p>
<dt><code>-K</code></p>
<dd>Strip Kerberos Realm component from user names (@ separated)</p>
<dt><code>-p</code><i> ldapport</i></p>
<dd>Specify an alternate TCP port where the LDAP server is listening if other than the default LDAP port 389.</p>
<dt><code>-P</code></p>
<dd>Use a persistent LDAP connection. Normally the LDAP connection is only open while verifying a users group membership to preserve resources at the LDAP server. This option causes the LDAP connection to be kept open, allowing it to be reused for further user validations. Recommended for larger installations.</p>
<dt><code>-R</code></p>
<dd>Do not follow referrals</p>
<dt><code>-s </code><i>base|one|sub</i></p>
<dd>search scope. Defaults to <code>sub</code></p>
<dd><code>base</code> object only,</p>
<dd><code>one</code> level below the base object or</p>
<dd><code>sub</code>tree below the base object</p>
<dt><code>-S</code></p>
<dd>Strip NT domain name component from user names (/ or \ separated)</p>
<dt><code>-t</code><i> search_timeout</i></p>
<dd>Specify time limit on LDAP search operations</p>
<dt><code>-u </code><i>attr</i></p>
<dd>LDAP attribute used to construct the user DN from the user name and base dn without needing to search for the user. A maximum of 16 occurrences of <code>%s</code> are supported.</p>
<dt><code>-v</code><i> 2|3</i></p>
<dd>LDAP protocol version. Defaults to <code>3 </code> if not specified.</p>
<dt><code>-Z</code></p>
<dd>Use TLS encryption</dl>
<h2>Configuration</h2>
<p>This helper is intended to be used as an <code>external_acl_type</code> helper in <code>squid.conf .</code></p>
<dl>
<dd><code>external_acl_type ldap_group %LOGIN /path/to/ext_ldap_group_acl &#8230;</code><br />
 <code>acl group1 external ldap_group Group1</code><br />
 <code>acl group2 external ldap_group Group2</code></dl>
<p> <code>NOTE:</code> When constructing search filters it is recommended to first test the filter using <code>ldapsearch</code> to verify that the filter matches what you expect before you attempt to use <code>ext_ldap_group_acl</code></p>
<h2>Author</h2>
<p>This program was written by <i>Flavio Pescuma &lt;flavio [at] marasystems.com&gt;</i> <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i> </p>
<p> Based on prior work in <code>squid_ldap_auth</code> by <i>Glen Newton &lt;glen.newton [at] nrc.ca&gt;</i> </p>
<p> This manual was written by <i>Henrik Nordstrom &lt;hno [at] marasystems.com&gt;</i></p>
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
<p> Or contact your favorite LDAP list/friend if the question is more related to LDAP than Squid.</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/8-basic_ldap_auth/">basic_ldap_auth</a></code>(8), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 Your favorite LDAP documentation<br />
 <code>RFC2254</code> &#8211; The String Representation of LDAP Search Filters,<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
