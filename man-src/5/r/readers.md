---
title: "readers(5)"
name: "readers"
section: "5"
letter: "r"
url: "/docs/linux/man/5-readers/"
description: "readers.conf – Access control and configuration for nnrpd"
---

<p>readers.conf &#8211; Access control and configuration for nnrpd</p>
<h2>Description</h2>
<p><i>readers.conf</i> in <i>pathetc</i> specifies access control for <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). It controls who is allowed to connect as a news reader and what they&#8217;re allowed to do after they connect. nnrpd reads this file when it starts up. This generally means that any changes take effect immediately on all subsequent connections, but <code>nnrpd</code> may have to be restarted if you use the <code>-D</code> option. (The location <i>pathetc</i>/readers.conf is only the default; the same format applies to any file specified with <tt>&quot;nnrpd -c&quot;</tt>.) </p>
<p> There are two types of entries in <i>readers.conf</i>: parameter/value pairs and configuration groups. Blank lines and anything after a number sign (<tt>&quot;#&quot;</tt>) are ignored, unless the character <tt>&quot;#&quot;</tt> is escaped with <tt>&quot;\&quot;</tt>. The maximum number of characters on each line is 8,191. </p>
<p> Parameter/value pairs consist of a keyword immediately followed by a colon, at least one whitespace character, and a value. The case of the parameter is significant (parameter should generally be in all lowercase), and a parameter may contain any characters except colon, <tt>&quot;#&quot;</tt>, and whitespace. An example: </p>
<pre> hosts: *.example.com</pre>
<p>Values that contain whitespace should be quoted with double quotes, as in: </p>
<pre> hosts: &quot;*.example.com, *.example.net&quot;</pre>
<p>If the parameter does not contain whitespace, such as: </p>
<pre> hosts: *.example.com,*.example.net</pre>
<p>it&#8217;s not necessary to quote it, although you may wish to anyway for clarity. </p>
<p> There is no way to continue a line on the next line, and therefore no way to have a single parameter with a value longer than about 8,180 characters. </p>
<p> Many parameters take a boolean value. For all such parameters, the value may be specified as <tt>&quot;true&quot;</tt>, <tt>&quot;yes&quot;</tt>, or <tt>&quot;on&quot;</tt> to turn it on and may be any of <tt>&quot;false&quot;</tt>, <tt>&quot;no&quot;</tt>, or <tt>&quot;off&quot;</tt> to turn it off. The case of these values is not significant. </p>
<p> There are two basic types of configuration groups, auth and access. The auth group provides mechanisms to establish the identity of the user, who they are. The access group determines, given the user&#8217;s identity, what that user is permitted to do. Writing a <i>readers.conf</i> file for your setup is a two-step process: first assigning an identity to each incoming connection using auth groups, and then giving each identity appropriate privileges with access group. We recommend <i>not</i> intermingling auth groups and access groups in the config file; it is often more sensible (in the absence of the <i>key</i> parameter) to put all of the auth groups first, and all of the access groups below. </p>
<p> A user identity, as established by an auth group, looks like an e-mail address; in other words, it&#8217;s in the form &#8220;&lt;username&gt;@&lt;domain&gt;&#8221; (or sometimes just &#8220;&lt;username&gt;&#8221; if no domain is specified. </p>
<p> If <i>nnrpdauthsender</i> is set in <i>inn.conf</i>, the user identity is also put into the Sender: header of posts made by that user. See the documentation of that option in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for more details. </p>
<p> An auth group definition looks like: </p>
<pre> auth &lt;name&gt; {
 hosts: &lt;host-wildmat&gt;
 auth: &lt;auth-program&gt;
 res: &lt;res-program&gt;
 default: &lt;defuser&gt;
 default-domain: &lt;defdomain&gt;
 # ...possibly other settings
 }</pre>
<p>The &lt;name&gt; is used as a label for the group and is only for documentation purposes. (If your syslog configuration records the <tt>&quot;news.debug&quot;</tt> facility, the &lt;name&gt; will appear in the debugging output of nnrpd. Examining that output can be very helpful in understanding why your configuration doesn&#8217;t do what you expect it to.) </p>
<p> A given auth group applies only to hosts whose name or <font SIZE="-1">IP</font> address matches the wildmat expression given with the hosts: parameter (comma-separated wildmat expressions allowed, but <tt>&quot;@&quot;</tt> is not supported). Rather than wildmat expressions, you may also use <font SIZE="-1">CIDR</font> notation to match any <font SIZE="-1">IP</font> address in a netblock; for example, &#8220;10.10.10.0/24&#8221; will match any <font SIZE="-1">IP</font> address between 10.10.10.0 and 10.10.10.255 inclusive. </p>
<p> If compiled against the <font SIZE="-1">TLS/SSL</font> libraries, an auth group with the <i>require_ssl</i> parameter set to true only applies if the incoming connection is using <font SIZE="-1">TLS</font>, either from the beginning if the <code>-S</code> flag was passed to <code>nnrpd</code> or after a successful use of <font SIZE="-1">STARTTLS</font>. </p>
<p> For any connection from a host that matches that wildmat expression or netblock, each &lt;res-program&gt; (multiple res: lines may be present in a block; they are run in sequence until one succeeds), if any, is run to determine the identity of the user just from the connection information. If all the resolvers fail, or if the res: parameter isn&#8217;t present, the user is assigned an identity of &#8220;&lt;defuser&gt;@&lt;defdomain&gt;&#8221;; in other words, the values of the default: and default-domain: parameters are used. If &lt;res-program&gt; only returns a username, &lt;defdomain&gt; is used as the domain. </p>
<p> If the user later authenticates via the <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font> commands, the provided username and password are passed to each &lt;auth-program&gt; (multiple auth, perl_auth, or python_auth lines may be present in a block; they are run in sequence until one succeeds), if any. If one succeeds and returns a different identity than the one assigned at the time of the connection, it is matched against the available access groups again and the actions the user is authorized to do may change. The most common &lt;auth-program&gt; to use is <code>ckpasswd</code>, which supports several ways of checking passwords including using <font SIZE="-1">PAM</font>. See the <i><a href="/docs/linux/man/8-ckpasswd/">ckpasswd</a></i>(8) man page for more details. </p>
<p> When matching auth groups, the last auth group in the file that matches a given connection and username/password combination is used. </p>
<p> An access group definition usually looks like: </p>
<pre> access &lt;name&gt; {
 users: &lt;identity-wildmat&gt;
 newsgroups: &lt;group-wildmat&gt;
 # ...possibly other settings
 }</pre>
<p>Again, &lt;name&gt; is just for documentation purposes. This says that all users whose identity matches &lt;identity-wildmat&gt; can read and post to all newsgroups matching &lt;group-wildmat&gt; (as before, comma-separated wildmat expressions are allowed, but <tt>&quot;@&quot;</tt> is not supported). Alternately, you can use the form: </p>
<pre> access &lt;name&gt; {
 users: &lt;identity-wildmat&gt;
 read: &lt;read-wildmat&gt;
 post: &lt;post-wildmat&gt;
 }</pre>
<p>and matching users will be able to read any group that matches &lt;read-wildmat&gt; and post to any group that matches &lt;post-wildmat&gt;. You can also set several other things in the access group as well as override various <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) parameters for just a particular group of users. </p>
<p> Just like with auth groups, when matching access groups the last matching one in the file is used to determine the user&#8217;s permissions. There is an exception to this rule: if the auth group which matched the client contains a perl_access: or python_access: parameter, then the script given as argument is used to dynamically generate an access group. This new access group is then used to determine the access rights of the client; the access groups in the file are ignored. </p>
<p> There is one additional special case to be aware of. When forming particularly complex authentication and authorization rules, it is sometimes useful for the identities provided by a given auth group to only apply to particular access groups; in other words, rather than checking the identity against the users: parameter of every access group, it&#8217;s checked against the users: parameter of only some specific access groups. This is done with the key: parameter. For example: </p>
<pre> auth example {
 key: special
 hosts: *.example.com
 default: &lt;SPECIAL&gt;
 }</pre>
<pre> access example {
 key: special
 users: &lt;SPECIAL&gt;
 newsgroups: *
 }</pre>
<p>In this case, the two key: parameters bind this auth group with this access group. For any incoming connection matching &#8220;*.example.com&#8221; (assuming there isn&#8217;t any later auth group that also matches such hosts), no access group that doesn&#8217;t have &#8220;key: special&#8221; will even be considered. Similarly, the above access group will only be checked if the user was authenticated with an auth group containing &#8220;key: special&#8221;. This mechanism normally isn&#8217;t useful; there is almost always a better way to achieve the same result. </p>
<p> Also note in the example that there&#8217;s no default-domain: parameter, which means that no domain is appended to the default username and the identity for such connections is just &#8220;&lt;<font SIZE="-1">SPECIAL</font>&gt;&#8221;. Note that some additional add-ons to <font SIZE="-1">INN</font> may prefer that authenticated identities always return a full e-mail address (including a domain), so you may want to set up your system that way. </p>
<p> Below is the full list of allowable parameters for auth groups and access groups, and after that are some examples that may make this somewhat clearer.</p>
<h2>Auth Group Parameters</h2>
<p>An access group without at least one of the res:, auth:, perl_auth:, python_auth:, or default: parameters makes no sense (and in practice will just be ignored).</p>
<dl>
<dt><code>hosts:</code></p>
<dd>A comma-separated list of remote hosts, wildmat patterns matching either hostnames or <font SIZE="-1">IP</font> addresses, or <font SIZE="-1">IP</font> netblocks specified in <font SIZE="-1">CIDR</font> notation. If a user connects from a host that doesn&#8217;t match this parameter, this auth group will not match the connection and is ignored. </p>
<p> Note that if you have a large number of patterns that can&#8217;t be merged into broader patterns (such as a large number of individual systems scattered around the net that should have access), the hosts: parameter may exceed the maximum line length of 8,192 characters. In that case, you&#8217;ll need to break that auth group into multiple auth groups, each with a portion of the hosts listed in its hosts: parameter, and each assigning the same user identity. </p>
<p> All hosts match if this parameter is not given.</p>
<dt><code>localaddress:</code></p>
<dd>A comma-separated list of local host or address patterns with the same syntax as the same as with the hosts: parameter. If this parameter is specified, its auth group will only match connections made to a matching local interface. (Obviously, this is only useful for servers with multiple interfaces.) </p>
<p> All local addresses match if this parameter is not given.</p>
<dt><code>res:</code></p>
<dd>A simple command line for a user resolver (shell metacharacters are not supported). If a full path is not given, the program executed must be in the <i>pathbin</i>/auth/resolv directory. A resolver is an authentication program which attempts to figure out the identity of the connecting user using nothing but the connection information (in other words, the user has not provided a username and password). An examples of a resolver would be a program that assigns an identity from an ident callback or from the user&#8217;s hostname. </p>
<p> One auth group can have multiple res: parameters, and they will be tried in the order they&#8217;re listed. The results of the first successful one will be used.</p>
<dt><code>auth:</code></p>
<dd>A simple command line for a user authenticator (shell metacharacters are not supported). If a full path is not given, the program executed must be located in the <i>pathbin</i>/auth/passwd directory. An authenticator is a program used to handle a user-supplied username and password, via a mechanism such as <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font>. Like with res:, one auth group can have multiple auth: parameters; they will be tried in order and the results of the first successful one will be used. See also perl_auth: below. </p>
<p> The most common authenticator to use is <i><a href="/docs/linux/man/8-ckpasswd/">ckpasswd</a></i>(8); see its man page for more information.</p>
<dt><code>perl_auth:</code></p>
<dd>A path to a perl script for authentication. The perl_auth: parameter works exactly like auth:, except that it calls the named script using the perl hook rather then an external program. Multiple/mixed use of the auth, perl_auth, and python_auth parameters is permitted within any auth group; each line is tried in the order it appears. perl_auth: has more power than auth: in that it provides the authentication program with additional information about the client and the ability to return an error string and a username. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with Perl support (<code>&#8211;with-perl</code> passed to configure). More information may be found in <i>doc/hook-perl</i>.</p>
<dt><code>python_auth:</code></p>
<dd>A Python script for authentication. The <i>python_auth</i> parameter works exactly like <i>auth</i>, except that it calls the named script (without its <tt>&quot;.py&quot;</tt> extension) using the Python hook rather then an external program. Multiple/mixed use of the <i>auth</i>, <i>perl_auth</i>, and <i>python_auth</i> parameters is permitted within any auth group; each line is tried in the order it appears. <i>python_auth</i> has more power than <i>auth</i> in that it provides the authentication program with additional information about the client and the ability to return an error string and a username. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with Python support (<code>&#8211;with-python</code> passed to <code>configure</code>). More information may be found in <i>doc/hook-python</i>.</p>
<dt><code>default:</code></p>
<dd>The default username for connections matching this auth group. This is the username assigned to the user at connection time if all resolvers fail or if there are no res: parameters. Note that it can be either a bare username, in which case default-domain: (if present) is appended after an <tt>&quot;@&quot;</tt>, or a full identity string containing an <tt>&quot;@&quot;</tt>, in which case it will be used verbatim.</p>
<dt><code>default-domain:</code></p>
<dd>The default domain string for this auth group. If a user resolver or authenticator doesn&#8217;t provide a domain, or if the default username is used and it doesn&#8217;t contain a <tt>&quot;@&quot;</tt>, this domain is used to form the user identity. (Note that for a lot of setups, it&#8217;s not really necessary for user identities to be qualified with a domain name, in which case there&#8217;s no need to use this parameter.)</p>
<dt><code>key:</code></p>
<dd>If this parameter is present, any connection matching this auth group will have its privileges determined only by the subset of access groups containing a matching key parameter.</p>
<dt><code>require_ssl:</code></p>
<dd>If set to true, an incoming connection only matches this auth group if it is encrypted using <font SIZE="-1">TLS/SSL</font>, either from the beginning if the <code>-S</code> flag was passed to <code>nnrpd</code> or after a successful use of <font SIZE="-1">STARTTLS</font>. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with <font SIZE="-1">TLS/SSL</font> support (<code>&#8211;with-openssl</code> passed to configure).</p>
<dt><code>perl_access:</code></p>
<dd>A path to a perl script for dynamically generating an access group. If an auth group matches successfully and contains a perl_access parameter, then the argument perl script will be used to create an access group. This group will then determine the access rights of the client, overriding any access groups in <i>readers.conf</i>. If and only if a sucessful auth group contains the perl_access parameter, <i>readers.conf</i> access groups are ignored and the client&#8217;s rights are instead determined dynamically. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with Perl support (<code>&#8211;with-perl</code> passed to configure). More information may be found in the file <i>doc/hook-perl</i>.</p>
<dt><code>python_access:</code></p>
<dd>A Python script for dynamically generating an access group. If an auth group matches successfully and contains a <i>python_access</i> parameter, then the argument script (without its <tt>&quot;.py&quot;</tt> extension) will be used to create an access group. This group will then determine the access rights of the client, overriding any access groups in <i>readers.conf</i>. If and only if a successful auth group contains the <i>python_access</i> parameter, <i>readers.conf</i> access groups are ignored and the client&#8217;s rights are instead determined dynamically. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with Python support (<code>&#8211;with-python</code> passed to <code>configure</code>). More information may be found in the file <i>doc/hook-python</i>.</p>
<dt><code>python_dynamic:</code></p>
<dd>A Python script for applying access control dynamically on a per newsgroup basis. If an auth group matches successfully and contains a <i>python_dynamic</i> parameter, then the argument script (without its <tt>&quot;.py&quot;</tt> extension) will be used to determine the clients rights each time the user attempts to view a newsgroup, or read or post an article. Access rights as determined by <i>python_dynamic</i> override the values of access group parameters such as <i>newsgroups</i>, <i>read</i> and <i>post</i>. This parameter is only valid if <font SIZE="-1">INN</font> is compiled with Python support (<code>&#8211;with-python</code> passed to <code>configure</code>). More information may be found in the file <i>doc/hook-python</i>.</dl>
<h2>Access Group Parameters</h2>
<dl>
<dt><code>users:</code></p>
<dd>The privileges given by this access group apply to any user identity which matches this comma-separated list of wildmat patterns. If this parameter isn&#8217;t given, the access group applies to all users (and is essentially equivalent to <tt>&quot;users: *&quot;</tt>).</p>
<dt><code>newsgroups:</code></p>
<dd>Users that match this access group are allowed to read and post to all newsgroups matching this comma-separated list of wildmat patterns. The empty string is equivalent to <tt>&quot;newsgroups: *&quot;</tt>; if this parameter is missing, the connection will be rejected (unless read: and/or post: are used instead, see below).</p>
<dt><code>read:</code></p>
<dd>Like the newsgroups: parameter, but the client is only given permission to read the matching newsgroups. This parameter is often used with post: (below) to specify some read-only groups; it cannot be used in the same access group with a newsgroups: parameter. (If read: is used and post: is missing, the client will have only read-only access.)</p>
<dt><code>post:</code></p>
<dd>Like the newsgroups: parameter, but the client is only given permission to post to the matching newsgroups. This parameter is often used with read: (above) to define the patterns for reading and posting separately (usually to give the user permission to read more newsgroups than they&#8217;re permitted to post to). It cannot be used in the same access group with a newsgroups: parameter.</p>
<dt><code>access:</code></p>
<dd>A set of letters specifying the permissions granted to the client. The letters are chosen from the following set:</p>
<dl>
<dd>
<dl>
<dt>R</p>
<dd>The client may read articles.</p>
<dt>P</p>
<dd>The client may post articles.</p>
<dt>I</p>
<dd>The client may inject articles with <font SIZE="-1">IHAVE</font>. Note that in order to inject articles with the <font SIZE="-1">IHAVE</font> the user must also have <font SIZE="-1">POST</font> permission (the <tt>&quot;P&quot;</tt> option).</p>
<dt>A</p>
<dd>The client may post articles with Approved: headers (in other words, may approve articles for moderated newsgroups). By default, this is not allowed.</p>
<dt>N</p>
<dd>The client may use the <font SIZE="-1">NEWNEWS</font> command, overriding the global setting.</p>
<dt>L</p>
<dd>The client may post to newsgroups that are set to disallow local posting (mode <tt>&quot;n&quot;</tt> in the <i><a href="/docs/linux/man/5-active/">active</a></i>(5) file).</dl>
</dl>
<dl>
<dd>Note that if this parameter is given, <i>allownewnews</i> in <i>inn.conf</i> is ignored for connections matching this access group and the ability of the client to use <font SIZE="-1">NEWNEWS</font> is entirely determined by the presence of <tt>&quot;N&quot;</tt> in the access string. If you want to support <font SIZE="-1">NEWNEWS</font>, make sure to include <tt>&quot;N&quot;</tt> in the access string when you use this parameter. </p>
<p> Note that if this parameter is given and <tt>&quot;R&quot;</tt> isn&#8217;t present in the access string, the client cannot read regardless of newsgroups: or read: parameters. Similarly, if this parameter is given and <tt>&quot;P&quot;</tt> isn&#8217;t present, the client cannot post. This use of access: is deprecated and confusing; it&#8217;s strongly recommended that if the access: parameter is used, <tt>&quot;R&quot;</tt> and <tt>&quot;P&quot;</tt> always be included in the access string and newsgroups:, read:, and post: be used to control access. (To grant read access but no posting access, one can have just a read: parameter and no post: parameter.)</dl>
<dt><code>key:</code></p>
<dd>If this parameter is present, this access group is only considered when finding privileges for users matching auth groups with this same key: parameter.</p>
<dt><code>reject_with:</code></p>
<dd>If this parameter is present, a client matching this block will be disconnected with a &#8220;Permission denied&#8221; message containing the contents (a &#8220;reason&#8221; string) of this parameter. Some newsreaders will then display the reason to the user.</p>
<dt><code>max_rate:</code></p>
<dd>If this parameter is present (and nonzero), it is used for <code>nnrpd</code>&#8216;s rate-limiting code. The client will only be able to download at this speed (in bytes/second). Note that if <font SIZE="-1">TLS/SSL</font> is being used, limiting is applied to the pre-encryption datastream.</p>
<dt><code>localtime:</code></p>
<dd>If a Date: header is not included in a posted article, <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) normally adds a new Date: header in <font SIZE="-1">UTC</font>. If this is set to true, the Date: header will be formatted in local time instead. This is a boolean value and the default is false.</p>
<dt><code>newsmaster:</code></p>
<dd>Used as the contact address in the help message returned by <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), if the virtualhost: parameter is set to true.</p>
<dt><code>strippath:</code></p>
<dd>If set to true, any Path: header provided by a user in a post is stripped rather than used as the beginning of the Path: header of the article. This is a boolean value and the default is false.</p>
<dt><code>perlfilter:</code></p>
<dd>If set to false, posts made by these users do not pass through the Perl filter even if it is otherwise enabled. This is a boolean value and the default is true.</p>
<dt><code>pythonfilter:</code></p>
<dd>If set to false, posts made by these users do not pass through the Python filter even if it is otherwise enabled. This is a boolean value and the default is true.</p>
<dt><code>virtualhost:</code></p>
<dd>Set this parameter to true in order to make <code>nnrpd</code> behave as if it is running on a server with a different name than it actually is. If you set this parameter to true, you must also set either pathhost: or domain: in the relevant access group in <i>readers.conf</i> to something different than is set in <i>inn.conf</i>. All articles displayed to clients will then have their Path: and Xref: headers altered to appear to be from the server named in pathhost: or domain: (whichever is set), and posted articles will use that server name in the Path:, Message-ID:, and X-Trace: headers. </p>
<p> Note that setting this parameter requires the server modify all posts before presenting them to the client and therefore may decrease performance slightly.</dl>
<p> In addition, all of the following parameters are valid in access groups and override the global setting in <i>inn.conf</i>. See <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for the descriptions of these parameters: </p>
<pre> addnntppostingdate, addnntppostinghost, backoff_auth, backoff_db,
 backoff_k, backoff_postfast, backoff_postslow, backoff_trigger,
 checkincludedtext, clienttimeout, complaints, domain,
 fromhost, localmaxartsize, moderatormailer, nnrpdauthsender,
 nnrpdcheckart, nnrpdoverstats, nnrpdposthost, nnrpdpostport, organization,
 pathhost, readertrack, spoolfirst, strippostcc.</pre>
<h2>Summary</h2>
<p>Here&#8217;s a basic summary of what happens when a client connects:</p>
<dl>
<dt>*</p>
<dd>All auth groups are scanned and the ones that don&#8217;t match the client (due to <i>hosts</i>, <i>localaddress</i>, <i>require_ssl</i>, etc.) are eliminated.</p>
<dt>*</p>
<dd>The remaining auth groups are scanned from the last to the first, and an attempt is made to apply it to the current connection. This means running res: programs, if any, and otherwise applying default:. The first auth group (starting from the bottom) to return a valid user is kept as the active auth group.</p>
<dt>*</p>
<dd>If no auth groups yield a valid user (none have default: parameters or successful res: programs) but some of the auth groups have auth: lines (indicating a possibility that the user can authenticate and then obtain permissions), the connection is considered to have no valid auth group (which means that the access groups are ignored completely) but the connection isn&#8217;t closed. Instead, 480 is returned for everything until the user authenticates.</p>
<dt>*</p>
<dd>When the user authenticates, the auth groups are rescanned, and only the matching ones which contain at least one auth, perl_auth, or python_auth line are considered. These auth groups are scanned from the last to the first, running auth: programs and perl_auth: or python_auth: scripts. The first auth group (starting from the bottom) to return a valid user is kept as the active auth group.</p>
<dt>*</p>
<dd>Regardless of how an auth group is established, as soon as one is, that auth group is used to assign a user identity by taking the result of the successful res, auth, perl_auth, or python_auth line (or the default: if necessary), and appending the default-domain if necessary. (If the perl_access: or python_access: parameter is present, see below.)</p>
<dt>*</p>
<dd>Finally, an access group is selected by scanning the access groups from bottom up and finding the first match. (If the established auth group contained a perl_access: or python_access line, the dynamically generated access group returned by the script is used instead.) User permissions are granted based on the established access group.</dl>
<h2>Examples</h2>
<p>Probably the simplest useful example of a complete <i>readers.conf</i>, this gives permissions to read and post to all groups to any connections from the &#8220;example.com&#8221; domain, and no privileges for anyone connecting elsewhere: </p>
<pre> auth example.com {
 hosts: &quot;*.example.com, example.com&quot;
 default: &lt;LOCAL&gt;
 }</pre>
<pre> access full {
 newsgroups: *
 }</pre>
<p>Note that the access realm has no users: key and therefore applies to any user identity. The only available auth realm only matches hosts in the &#8220;example.com&#8221; domain, though, so any connections from other hosts will be rejected immediately. </p>
<p> If you have some systems that should only have read-only access to the server, you can modify the example above slightly by adding an additional auth and access group: </p>
<pre> auth lab {
 hosts: &quot;*.lab.example.com&quot;
 default: &lt;LAB&gt;
 }</pre>
<pre> access lab {
 users: &lt;LAB&gt;
 read: *
 }</pre>
<p>If those are put in the file after the above example, they&#8217;ll take precedence (because they&#8217;re later in the file) for any user coming from a machine in the lab.example.com domain, everyone will only have read access, not posting access. </p>
<p> Here&#8217;s a similar example for a news server that accepts connections from anywhere but requires the user to specify a username and password. The username and password are first checked against an external database of usernames and passwords, and then against the system shadow password file: </p>
<pre> auth all {
 auth: &quot;ckpasswd -d &lt;pathdb in inn.conf&gt;/newsusers&quot;
 auth: &quot;ckpasswd -s&quot;
 }</pre>
<pre> access full {
 users: *
 newsgroups: *
 }</pre>
<p>When the user first connects, there are no res: keys and no default, so they don&#8217;t receive any valid identity and the connection won&#8217;t match any access groups (even ones with <tt>&quot;users: *&quot;</tt>). Such users receive nothing but authentication-required responses from nnrpd until they authenticate. </p>
<p> If they then later authenticate, the username and password are checked first by running <code>ckpasswd</code> with the <code>-d</code> option for an external dbm file of encrypted passwords, and then with the <code>-s</code> option to check the shadow password database (note that this option may require ckpasswd to be setgid to a shadow group, and there are security considerations; see <i><a href="/docs/linux/man/8-ckpasswd/">ckpasswd</a></i>(8) for details). If both of those fail, the user will continue to have no identity; otherwise, an identity will be assigned (usually the supplied username, perhaps with a domain appended, although an authenticator technically can provide a completely different username for the identity), and the access group will match, giving full access. </p>
<p> It may be educational to consider how to combine the above examples; general groups always go first. The order of the auth groups actually doesn&#8217;t matter, since the &#8220;hosts: example.com&#8221; one only matches connections before username/password is sent, and the &#8220;auth: ckpasswd&#8221; one only matches after; order would matter if either group applied to both cases. The order of the access groups in this case does matter, provided the newsgroups: lines differ; the access group with no users: line needs to be first, with the &#8220;users: &lt;<font SIZE="-1">LOCAL</font>&gt;&#8221; group after. </p>
<p> Here&#8217;s an example of another common case: a server that only allows connections from a local domain and has an additional hierarchy that&#8217;s password-restricted. </p>
<pre> auth &quot;example.com&quot; {
 hosts: &quot;*.example.com&quot;
 auth: &quot;ckpasswd -d &lt;pathdb in inn.conf&gt;/newsusers&quot;
 default: &quot;anonymous&quot;
 }</pre>
<pre> access regular {
 newsgroups: &quot;*,!example.restricted.*&quot;
 }</pre>
<pre> access full {
 users: &quot;*,!anonymous&quot;
 newsgroups: *
 }</pre>
<p>In this example, unauthenticated users get the identity <tt>&quot;anonymous&quot;</tt>, which matches only the first access group and hence doesn&#8217;t get access to the example.restricted.* hierarchy. Anyone who authenticates using a password in the <i>newsusers</i> file gets full access to all groups. However, note that the only authentication block is limited to hostnames in the example.com domain; connections outside of that domain will never be allowed access or an opportunity to authenticate. </p>
<p> Here&#8217;s a very complicated example. This is for an organization that has an internal hierarchy &#8220;example.*&#8221; only available to local shell users, who are on machines where identd can be trusted. Dialup users must provide a username and password, which is then checked against <font SIZE="-1">RADIUS</font>. Remote users have to use a username and password that&#8217;s checked against a database on the news server. Finally, the admin staff (users &#8220;joe&#8221; and &#8220;jane&#8221;) can post anywhere (including the &#8220;example.admin.*&#8221; groups that are read-only for everyone else), and are exempted from the Perl filter. For an additional twist, posts from dialup users have their Sender: header replaced by their authenticated identity. </p>
<p> Since this organization has some internal moderated newsgroups, the admin staff can also post messages with Approved: headers, but other users cannot. </p>
<pre> auth default {
 auth: &quot;ckpasswd -f &lt;pathdb in inn.conf&gt;/newsusers&quot;
 default: &lt;FAIL&gt;
 default-domain: example.com
 }</pre>
<pre> auth shell {
 hosts: *.shell.example.com
 res: ident
 auth: &quot;ckpasswd -s&quot;
 default: &lt;FAIL&gt;
 default-domain: shell.example.com
 }</pre>
<pre> auth dialup {
 hosts: *.dialup.example.com
 auth: radius
 default: &lt;FAIL&gt;
 default-domain: dialup.example.com
 }</pre>
<pre> access shell {
 users: *@shell.example.com
 read: *
 post: &quot;*, !example.admin.*&quot;
 }</pre>
<pre> access dialup {
 users: *@dialup.example.com
 newsgroups: *,!example.*
 nnrpdauthsender: true
 }</pre>
<pre> access other {
 users: &quot;*@example.com, !&lt;FAIL&gt;@example.com&quot;
 newsgroups: *,!example.*
 }</pre>
<pre> access fail {
 users: &quot;&lt;FAIL&gt;@*&quot;
 newsgroups: !*
 }</pre>
<pre> access admin {
 users: &quot;joe@*,jane@*&quot;
 newsgroups: *
 access: &quot;RPA&quot;
 perlfilter: false
 }</pre>
<p>Note the use of different domains to separate dialup from shell users easily. Another way to do that would be with key: parameters, but this way provides slightly more intuitive identity strings. Note also that the fail access group catches not only failing connections from external users but also failed authentication of shell and dialup users and dialup users before they&#8217;ve authenticated. The identity string given for, say, dialup users before <font SIZE="-1">RADIUS</font> authentication has been attempted matches both the dialup access group and the fail access group, since it&#8217;s &#8220;&lt;<font SIZE="-1">FAIL</font>&gt;@dialup.example.com&#8221;, but the fail group is last so it takes precedence. </p>
<p> The shell auth group has an auth: parameter so that users joe and jane can, if they choose, use username and password authentication to gain their special privileges even if they&#8217;re logged on as a different user on the shell machines (or if ident isn&#8217;t working). When they first connect, they&#8217;d have the default access for that user, but they could then send <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER</font> and <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">PASS</font> in order to get their extended access. </p>
<p> Also note that if the users joe and jane are using their own accounts, they get their special privileges regardless of how they connect, whether the dialups, the shell machines, or even externally with a username and password. </p>
<p> Finally, here&#8217;s a very simple example of a configuration for a public server for a particular hierarchy. </p>
<pre> auth default {
 hosts: *
 default: &lt;PUBLIC&gt;
 }</pre>
<pre> access default {
 users: &lt;PUBLIC&gt;
 newsgroups: example.*
 }</pre>
<p>Notice that clients aren&#8217;t allowed to read any other groups; this keeps them from getting access to administrative groups or reading control messages, just as a precaution. When running a public server like this, be aware that many public hierarchies will later be pulled down and reinjected into the main Usenet, so it&#8217;s highly recommended that you also run a Perl or Python filter to reject any messages crossposted out of your local hierarchy and any messages containing a Supersedes: header. This will keep messages posted to your public hierarchy from hurting any of the rest of Usenet if they leak out.</p>
<h2>Security Considerations</h2>
<p>In general, separate passwords should be used for <font SIZE="-1">NNTP</font> wherever possible; the <font SIZE="-1">NNTP</font> protocol itself does not protect passwords from casual interception, and many implementations (including this one) do not &#8220;lock out&#8221; accounts or otherwise discourage password-guessing attacks. So it is best to ensure that a compromised password has minimal effects. </p>
<p> Authentication using the <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font> commands passes unencrypted over the network. Extreme caution should therefore be used especially with system passwords (e.g. <tt>&quot;auth: ckpasswd -s&quot;</tt>). Passwords can be protected by using <font SIZE="-1">NNTP</font> over <font SIZE="-1">TLS/SSL</font> or through ssh tunnels, and this usage can be enforced by a well-considered server configuration that only permits certain auth groups to be applied in certain cases. Here are some ideas:</p>
<dl>
<dt>*</p>
<dd>To restrict connections on the standard <font SIZE="-1">NNTP</font> port (119) to use <font SIZE="-1">TLS</font> for some (or all) of the auth groups to match, use the <i>require_ssl</i> parameter. Note that a client can use <font SIZE="-1">STARTTLS</font> to negotiate an encrypted connection.</p>
<dt>*</p>
<dd>If you consider your local network (but not the internet) secure, have some auth groups with a restrictive hosts: parameter; they would go above, with ones having global applicability below.</p>
<dt>*</p>
<dd>Consider running <code>nnrpd</code> with the <code>-S</code> flag (either also with <code>-D</code>, or out of &#8220;super-server&#8221; like <code>inetd</code>) on the <font SIZE="-1">NNTPS</font> port (563) for clients that support <font SIZE="-1">TLS/SSL</font>. See <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) for more details about how to configure that. You can use the <i>require_ssl</i> parameter or the <code>-c</code> flag to specify an alternate <i>readers.conf</i> file if you want a substantially different configuration for this case.</p>
<dt>*</p>
<dd>If you want to restrict an auth group to only match loopback connections (for users running newsreaders on localhost or connecting via an ssh tunnel), use the localaddress: parameter.</dl>
<h2>History</h2>
<p>Written by Aidan Cully &lt;aidan [at] panix.com&gt; for InterNetNews. Substantially expanded by Russ Allbery &lt;rra [at] stanford.edu&gt;. </p>
<p> $Id: readers.conf.pod 8479 2009-05-18 20:01:37Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-auth_krb5/">auth_krb5</a></i>(8), <i><a href="/docs/linux/man/8-ckpasswd/">ckpasswd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
