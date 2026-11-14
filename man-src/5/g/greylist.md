---
title: "greylist(5)"
name: "greylist"
section: "5"
letter: "g"
url: "/docs/linux/man/5-greylist/"
description: "greylist.conf – milter-greylist configuration file"
---

<p><code>greylist.conf</code> &#8211; milter-greylist configuration file</p>
<h2>Description</h2>
<p><code>greylist.conf </code> configures <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> operation. The format is simple: each line contains a keyword and optional arguments. Any line starting with a # is considered as a comment and is ignored. Blank lines are ignored as well. Comments at the end of lines are accepted in some situations, but do not take them as granted. A statement can be continued on the next line by using a backslash. Anything after the backslash will be ignored.</p>
<h2>Whitelist</h2>
<p>The primary use of <code>greylist.conf</code> is to setup <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> whitelist. It also offers a handy blacklist feature. Access-lists (ACL) are used to do that. ACL enable the administrator to specify complex conditions on sender IP, sender DNS address, sender e-mail address, and recipient e-mail address. If support for DNSRBL was built-in, it is even possible to use DNSRBL in ACL. </p>
<p> An access-list entry starts with the <i>racl</i> keyword followed by an optional id quoted string, then the <i>greylist</i>, <i>whitelist</i>, or <i>blacklist</i> keyword, and by any set of the following clauses: <i>addr</i>, <i>domain</i>, <i>from</i>, <i>rcpt</i>, <i>rcptcount</i>, <i>helo</i>, <i>sm_macro</i>, <i>time</i>, <i>auth</i>, <i>tls</i>, <i>spf</i> (if build with SPF support), <i>geoip</i> (if build with GeoIP support), <i>p0f</i> (if build with p0f support), <i>ldapcheck</i> (if build with &#8211;with-openldap), <i>urlcheck</i> (if built with &#8211;with-libcurl), and <i>dnsrbl</i> (if built with &#8211;enable-dnsrbl). A message will match an ACL entry when it complies with all of its clauses. </p>
<p> Clauses can be negated, by prefixing them by the <i>not</i> keyword.</p>
<dl>
<dt><i>addr</i></p>
<dd>This clause is used to specify a netblock of source IP addresses. The syntax is an IP address followed by a slash and a CIDR netmask. Here is an example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist addr 127.0.0.0/8<br />
&nbsp;<wbr>&nbsp;<wbr>racl whitelist addr 192.168.3.0/24<br />
&nbsp;<wbr>&nbsp;<wbr>racl whitelist addr ::1</p>
<dd>If the netmask is ommitted, /32 is assumed for an IPv4 address and /128 is assumed for an IPv6 address.</p>
<dd>You should at least whitelist localhost (127.0.0.1/8), and if you have some user clients connecting to the machine, you should whitelist the addresses they connect from if you don&#8217;t want them to get error messages when sending e-mail.</p>
<dt><i>domain</i></p>
<dd>This clause selects source machines based on their DNS name, performing a suffix search. For instance, this will whitelist any machine in the <i>example.net</i> domain:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist domain example.net</p>
<dd>Suffix search matching means, for example, that gle.com will match google.com. If you want domain names to match on subdomain boundaries (e.g. gle.com will match mail.gle.com and gle.com but not google.com) then enable <i>domainexact</i></dl>
<p> The name resolution is made by Sendmail, which hands it to <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code>. As a result, it is impossible to use DNS aliases here. On the other hand, this will work even if your DNS resolver is not thread-safe.</p>
<dl>
<dt><i>from</i></p>
<dd>This is used to select sender e-mail addresses. You should not use that feature, because sender e-mail addresses can be trivially forged. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist from postmaster [at] example.com</p>
<dt><i>rcpt</i></p>
<dd>This is used to select recipient addresses. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl greylist rcpt John.Doe [at] example.net</p>
<dt><i>rcptcount</i></p>
<dd>Followed by an operator and a recipient count, this is used to select the amount of recipients. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl blacklist rcptcount&nbsp;<wbr>&gt;=&nbsp;<wbr>25 msg&nbsp;<wbr>&quot;No more than 25 recipients, please&quot;</p>
<dt><i>helo</i></p>
<dd>Followed by a quoted string or a regular expression, this can be used to filter on the HELO string.</p>
<dt><i>sm_macro </i></p>
<dd>This is used to select a Sendmail macro value. See the section on that topic for more information.</p>
<dt><i>time</i></p>
<dd>This is used to specify a time set. It should be followed by a quoted string of <code><a href="/docs/linux/man/5-crontab/">crontab</a>(5)</code>-like time specification. Here is an example that whitelists mail addressed to a single recipient during office hours (from 8:00 to 16:59 from monday to friday):</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist time&nbsp;<wbr>&quot;*&nbsp;<wbr>8-16&nbsp;<wbr>*&nbsp;<wbr>*&nbsp;<wbr>1-5&quot;&nbsp;<wbr>rcpt info [at] example.net</p>
<dt><i>geoip</i></p>
<dd>This is used to specify a country, as reported by GeoIP. The country code must be upper case, and is only available if <code>milter-greylist</code> was built with GeoIP support. The <i>geoipdb </i> statement can be used to specify the location of GeoIP database.</p>
<dt><i>p0f</i></p>
<dd>This is used to match against the remote system OS fingerprint genre and detail,obtained from p0f. It is only available if <code>milter-greylist</code> was built with p0f support. <i>p0f</i> clauses can be used with a quoted string for case-insensitive substring match, or against regular expressions. The <i>p0fsock</i> statement can be used to speficy the location of the p0f socket.</p>
<dt><i>auth</i></p>
<dd>This is used to select a user that succeeded SMTP AUTH. In order to select any user that succeeds SMTP AUTH, you can use a regular expression matching, like below;</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist auth&nbsp;<wbr>/.*/</p>
<dd>Using such a clause automatically disable global STARTTLS and SMTP AUTH whitelisting, like if the <i>noauth</i> keyword would have been used.</p>
<dt><i>tls</i></p>
<dd>This is used to select the distinguished name (DN) of a user that succeeded STARTTLS. Using such a clause automatically disable global STARTTLS and SMTP AUTH whitelisting, like if the <i>noauth</i> keyword would have been used.</p>
<dt><i>spf</i></p>
<dd>This is used to test SPF status. Possible values are <i>pass</i>, <i>softfail</i>, <i>fail</i>, <i>unknown</i>, <i>error</i>, <i>none</i>, and <i>self</i>. The first six values are plain SPF validation status. The <i>self</i> value is a special test that checks the server&#8217;s local IP address against the sender&#8217;s SPF record. If that test validates, odds are good that the sender SPF record is wide open, and this is hint that SPF should not be trusted.</p>
<dd>Absence of any value after the <i>spf</i> keyword is a synonym for <i>spf pass</i>. This is present for backward compatibility.</p>
<dd>The <i>spf</i> clause is only available if SPF support was compiled in. Using it will disable global SPF whitelisting, like if the <i>nospf</i> keyword would have been used.</p>
<dt><i>ldapcheck</i></p>
<dd>This is used to query an LDAP directory. See the section on that topic for more information.</p>
<dt><i>urlcheck</i></p>
<dd>This is used to query an external configuration source through an URL. See the section on that topic for more information.</p>
<dt><i>dnsrbl</i></p>
<dd>This is used to select a DNSRBL. See the section on that topic for more information.</dl>
<p> The <i>domain</i>, <i>from</i>, and <i>rcpt</i> clauses may be used with regular expressions. The regular expressions must be enclosed by slashes (/). No escaping is available to provide a slash inside a regular expression, so just do not use it. Regular expressions follow the format described in <code><a href="/docs/linux/man/7-re_format/">re_format</a>(7)</code>. Here is an example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl greylist rcpt&nbsp;<wbr>/.*@example\.net/ </p>
<p> When regular expressions are not used, <i>from</i>, and <i>rcpt</i> perform a case insensitive substring match with leading and trailing brackets, spaces and tabs stripped out. <i>domain</i> performs a case insensitive suffix match. This means, for example, that gle.com will match google.com. If you want domain names to match on subdomain boundaries (e.g. gle.com will match mail.gle.com and gle.com but not google.com) then enable <i>domainexact</i> </p>
<p> An ACL entry can also hold various optional parameter used on match: <i>delay</i>, <i>autowhite</i>, <i>flushaddr</i>, <i>nolog</i>, <i>code</i>, <i>ecode</i>, <i>report</i>, <i>addheader</i>, and <i>msg</i></p>
<dl>
<dt><i>delay</i></p>
<dd>Specify the greylisting delay used before the message can be accepted. This overrides the <i>greylist</i> global setting, and it only makes sense on an <i>racl greylist</i> entry.</p>
<dt><i>autowhite</i></p>
<dd>Specify the autowhitelisting duration for messages matching this ACL. This overrides the <i>autowhite</i> global setting, and it only makes sense on an <i>racl greylist</i> entry. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl greylist rcpt JDoe [at] example.net delay 15m autowhite 3d<br />
&nbsp;<wbr>&nbsp;<wbr>racl greylist rcpt root [at] example.net delay 1h autowhite 3d</p>
<dt><i>flushaddr</i></p>
<dd>If a message matches the rule, any entry in the greylist or autowhite databases matching the sender IP is removed. Used with a DNSRBL blacklist ACL, it is useful for freeing the database from entries set up by a machine which is known to be a spamer. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl blacklist dnsrbl&nbsp;<wbr>&quot;known-spamers&quot;&nbsp;<wbr>flushaddr</p>
<dt><i>nolog</i></p>
<dd>Do not generate syslog message if this rule matches. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl whitelist default nolog</p>
<dt><i>code</i></p>
<dd>
<dt><i>ecode</i></p>
<dd>
<dt><i>msg</i></p>
<dd>These 3 values can be used to choose the SMTP code, extended code and reply message for temporary failures and rejects. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>racl blacklist dnsrbl&nbsp;<wbr>&quot;spamstomp&quot;&nbsp;<wbr>msg&nbsp;<wbr>&quot;IP caught by spamstomp&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>racl greylist default code&nbsp;<wbr>&quot;451&quot;&nbsp;<wbr>ecode&nbsp;<wbr>&quot;4.7.1&quot;</p>
<dd>The <i>msg</i> strings accepts format string substitution as documented in the <code>FORMAT STRINGS </code> section. For instance, <i>%A</i> gets substituted by the ACL line number.</p>
<dd>None of the last 3 values makes sense for a whitelist entry.</p>
<dt><i>report</i></p>
<dd>This value overrides the text displayed in the <i>X-Greylist </i> header, for messages that <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> lets pass through, either because they are whitelisted, or because they passed greylisting (see <code>REPORTING</code>). This string can be substituted as documented in the <code>FORMAT STRINGS</code> section.</p>
<dt><i>addheader</i></p>
<dd>This quoted string is a RFC822 header that gets added to the message. Format string substitution is supported. No check is done for header length standard compliance, so make sure the substituted string is shorter than 2048 characters.</dl>
<p> Entries in the access-list are evaluated sequentially, so order is very important. The first matching entry is used to decide if a message will be whitelisted or greylisted. A special <i>default</i> clause can be used in the last ACL entry as a wildcard. Here are a few complete ACL examples: </p>
<p> Example 1: </p>
<pre>racl whitelist from friend [at] toto.com rcpt grandma [at] example.com
racl whitelist from other.friend [at] example.net rcpt grandma [at] example.com
racl greylist rcpt grandma [at] example.com
racl whitelist default</pre>
<p>Example 2: </p>
<pre>racl whitelist addr 193.54.0.0/16 domain friendly.com
racl greylist rcpt user1 [at] atmine.com
racl greylist rcpt user2 [at] atmine.com
racl greylist rcpt user3 [at] atmine.com
racl whitelist default</pre>
<p>Example 3: </p>
<pre>racl whitelist rcpt /.*@.*otherdomain\.org/
racl whitelist addr 192.168.42.0/24 rcpt user1 [at] mydomain.org
racl whitelist from friend [at] example.net rcpt /.*@.*mydomain\.org/
racl whitelist rcpt user2 [at] mydomain.org
racl greylist rcpt /.*@.*mydomain\.org/
racl whitelist default</pre>
<h2>Data-Stage Acl</h2>
<p>ACL using the <i>racl</i> keyword are evaluated at the RCPT stage of the SMTP transaction. It is also possible to have ACL evaluated at the DATA stage of the SMTP transaction, using the <i>dacl </i> keyword, provided the message went through RCPT-stage ACL, and possibly greylisting. Note that you canot use the <i>greylist</i> action at DATA-stage if the RCPT-stage ACL that matched had a <i>greylist</i> action itself. The following clauses can be used to work on message content:</p>
<dl>
<dt><i>dkim</i></p>
<dd>DKIM status (if build with DKIM support). Possible values are <i>pass</i>, <i>fail</i>, <i>unknown</i>, <i>error</i>, and <i>none</i>,</p>
<dt><i>header</i></p>
<dd>String or regular expression searched in message headers</p>
<dt><i>body</i></p>
<dd>String or regular expression searched in message body</p>
<dt><i>msgsize</i></p>
<dd>Operator followed by a message size (k or M suffix allowed for kilobytes or megabytes). Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>dacl blacklist msgsize&nbsp;<wbr>&gt;=&nbsp;<wbr>4M msg&nbsp;<wbr>&quot;No more than 4 MB please&quot;</p>
<dt><i>spamd</i></p>
<dd>SpamAssassin score (if build with SpamAssassin support). If used without comparison operator <i>spamd</i> is true if the score is above threshold. The <i>spamdsock</i> keyword can be used to specify the location of the spamd socket.</p>
<dd>Example 1: </p>
<pre> spamdsock unix &quot;/var/spamassassin/spamd.sock&quot;
 racl whitelist default 
 dacl greylist spamd</pre>
<dd>Example 2: </p>
<pre> spamdsock inet &quot;127.0.0.1:783&quot;
 racl whitelist default 
 dacl blacklist spamd &gt; 15 msg &quot;Your message is considered spam.&quot;
 dacl greylist spamd &gt; 10 delay 2h
 dacl greylist spamd &gt; 5 delay 1h</pre>
</dl>
<p> Note that if there are multiple recipient, a <i>rcpt</i> clause at DATA stage evalutes to true if it matches any of them. If you want to match an exact set of recipients, you can use multiple <i>rcpt</i> clauses along with a <i>rcptcount</i> clause.</p>
<h2>Lists</h2>
<p>It is often useful to group several users or sender IP addresses in a single ACL. This can be done with lists. Lists must be first defined and given a name before they can be used in ACL entries. Here is an example:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>list&nbsp;<wbr>&quot;my users&quot;&nbsp;<wbr>rcpt&nbsp;<wbr>{&nbsp;<wbr>user1 [at] example.com user2 [at] example.com&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>list&nbsp;<wbr>&quot;local&quot;&nbsp;<wbr>addr&nbsp;<wbr>{&nbsp;<wbr>192.0.2.0/24 10.0.0.0/8&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl whitelist list&nbsp;<wbr>&quot;local&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>racl greylist list&nbsp;<wbr>&quot;my users&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>racl whitelist default </p>
</dl>
<h2>Backward Compatibility</h2>
<p>Previous versions of <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> used <i>addr</i>, <i>domain</i>, <i>from</i>, and <i>rcpt</i> lines, without the <i>racl</i> keyword. Access-list management is intended to replace them. These lines are still accepted by <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code>, but they are deprecated. <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> handles them as access-list entries with a single clause. They are added at the head of the access-list so the use of these keywords and access-lists may lead to unspecified behaviour. Do not mix them. </p>
<p> test mode (using <code>-T</code>) is also deprecated. Access-list semantics do not depend on this flag. </p>
<p> <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> also used to only have a RCPT-stage ACL, which was configured through <i>acl</i> statements. These have been replaced by <i>racl</i> statements (as opposed to <i>dacl</i> statements for DATA-stage ACL). <i>acl</i> statements are still accepted for backward compatibility and are a synonym for <i>racl</i> statements.</p>
<h2>Mx Sync</h2>
<p>Synchronization of the greylist among multiple MX is configured using the <i>peer </i> keyword. List each other MX IP addresses using the <i>peer </i> keyword. Here is an example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.18<br />
&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.17<br />
&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.22 timeout 7<br />
&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.38 timeout 5m </p>
<p> You can list the local machine in the peer statements, it will be ignored. </p>
<p> The <i>timeout</i> clause sets a peer communication timeout to have proper retrial in case of slow MX peer. The default value is 3 seconds. The special value of 0 disables the connection retrials. </p>
<p> By default, milter-greylist will listen on all interfaces using TCP port 5252 or the port number given by service named mxglsync if defined in <i>/etc/services</i> or other directory service. This behaviour can be changed by using the <i>syncaddr</i> keyword. Here are a few examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>syncaddr&nbsp;<wbr>*<br />
&nbsp;<wbr>&nbsp;<wbr>syncaddr&nbsp;<wbr>*&nbsp;<wbr>port 7689<br />
&nbsp;<wbr>&nbsp;<wbr>syncaddr 192.0.2.2 port 9785<br />
&nbsp;<wbr>&nbsp;<wbr>syncaddr 2001:db8::1:c3b5:123<br />
&nbsp;<wbr>&nbsp;<wbr>syncaddr 2001:db8::1:c3b5:123 port 1234 </p>
<p> Using &#8216;*&#8217; as the address means to bind to all local interfaces&#8217; addresses. Note that if you are not using the default port, all MXs must use the same port number. </p>
<p> For outbound connections the system is selecting one of the possible adresses. If you want to use a specific ip you can use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>syncsrcaddr 123.456.78.9</p>
<h2>Text Dump</h2>
<p><code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> uses a text dump of its database to resume operation after a crash. The dump is performed at regular time interval, but as it is a heavy operation, you might want to configure a particular time interval, using the <i>dumpfreq</i> option. </p>
<p> If the <i>dumpfreq</i> value is too small, it will kill performance. If it is too high, you will loose a bigger part of the database on a crash. </p>
<p> Set <i>dumpfreq</i> to 0 to get a dump on each change (kills performance), Set it to -1 to never dump to a file (unsafe as you lose the whole greylist on each crash), or give a time value for the delay between dumps. The time is given in seconds, except if a unit is given: m for minutes, h for hours, and d for days. </p>
<p> You may further improve the performance of the dump operation at the expense of humanly readable timestamp which by default appears as a comment at the end of each line in the dumpfile. You may disable generation of this comment by specifying <i>dump_no_time_translation</i> option in the configuration file. This is specifficaly recommended if your dumpfile grows to 100&#8217;s of megabytes &#8211; it can reduce the time needed for the dump operation by the order of magnitude!</p>
<h2>Reporting</h2>
<p>By default, <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> will add a <i>X-Greylist</i> header to any message it handles. The header shows what happened to the message: delayed or not delayed, and why. The following options can be used in <code>greylist.conf</code> to alter this behavior:</p>
<dl>
<dt><i>report none</i></p>
<dd>Never add a <i>X-Greylist</i> header.</p>
<dt><i>report delays</i></p>
<dd>Only add a header if the message was delayed.</p>
<dt><i>report nodelays</i></p>
<dd>Add a header if the message was not delayed. The header explains why the message was not delayed.</p>
<dt><i>report all</i></p>
<dd>Always add a header. This is the default.</dl>
<h2>Sender Callback Systems</h2>
<p>Sender callback systems are another anti-spam measure that attempts to send a DSN to the sender address before accepting a message. If that fails, then the sender address is wrong and the message is rejected. Such systems usually stop their callback check at the RCPT stage of the SMTP transaction. </p>
<p> Greylisting temporarily rejects at the RCPT stage, so sender callback and greylisting love to fight each other. <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> proposes a workaround to that problem with the <i>delayedreject</i> option. For messages coming from &lt;&gt; (that is, for DSN), it will cause the temporary reject to happen at the DATA stage of the SMTP transaction instead of the RCPT stage. That way, <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> will cope much better with sender callback systems. </p>
<p> This has a minor drawback (and this is why it is not enabled by default): for a multi recipient DSN, whitelisted recipient will not be honoured: the message will be delayed for everyone.</p>
<h2>Sendmail Macros</h2>
<p>Any sendmail macro can be used as a clause in the access list. You need to define a (macro, value) pair using the <i>sm_macro</i> keyword before using it. Here is an example that uses the <i>{client_resolve}</i> macro to apply a larger greylisting delay to hosts that have a bogus reverse DNS:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>sm_macro&nbsp;<wbr>&quot;maybe_forged&quot;&nbsp;<wbr>&quot;{client_resolve}&quot;&nbsp;<wbr>&quot;FORGED&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl greylist sm_macro&nbsp;<wbr>&quot;maybe_forged&quot;&nbsp;<wbr>delay 1h<br />
&nbsp;<wbr>&nbsp;<wbr>racl greylist default delay 15m</dl>
<p> A regular expression can be used as the macro value. It must be surrounded with slashes and not by quotes. The special value <i>unset</i> can also be used to match an unset macro:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>sm_macro&nbsp;<wbr>&quot;not_foo&quot;&nbsp;<wbr>&quot;{foo}&quot;&nbsp;<wbr>unset</dl>
<p> Note that any Sendmail macro that is not exported using the <i>Milter.macros.envrcpt </i> setting of <i>sendmail.cf</i> will be seen as unset from milter-greylist.</p>
<h2>Dnsrbl</h2>
<p>DNS Reverse Black List can be used to toggle an ACL. They must be defined and named before they can be used. Here is an example which uses a bigger greylisting delay for hosts caught in the SORBS dynamic pool DNRSBL (this will include DSL and cable customers pools, which are well known to be massively infected by spamwares):</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;SORBS DUN&quot;&nbsp;<wbr>dnsbl.sorbs.net 127.0.0.10/32 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl greylist dnsrbl&nbsp;<wbr>&quot;SORBS DUN&quot;&nbsp;<wbr>delay 1h<br />
&nbsp;<wbr>&nbsp;<wbr>racl greylist default delay 15m</dl>
<p> The definition of a DNSRBL starts by the <i>dnsrbl</i> keyword, followed by the quoted name of the DNSRBL, the DNS domain on which addresses should be looked up, and the answer we should consider as a positive hit. </p>
<p> DNSRBL support is only available if enabled through the &#8211;enable-dnsrbl config flag. Please make sure <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> is linked against a thread-safe DNS resolver, otherwise it shall crash.</p>
<h2>URL checks</h2>
<p><code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8) </code> is able to query external sources of information through various URL, if it was built with &#8211;with-libcurl. Here is an example:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>urlcheck&nbsp;<wbr>&quot;glusr&quot;&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.example.net/mgl-config?rcpt=%r">http://www.example.net/mgl-config?rcpt=%r</a>&quot;&nbsp;<wbr>5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl greylist urlcheck&nbsp;<wbr>&quot;glusr&quot;&nbsp;<wbr>delay 15m&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>racl whitelist default</dl>
<p> The trailing 5 at the end of the <i>urlcheck</i> definition is the maximum number of simultaneous connections we want to launch on this URL. For each message, the URL will be querried, with % format tags being subtituted. For instance, <i>%r</i> is substituted by the recipient. See the <code>FORMAT STRINGS</code> section for the complete list of substitutions. </p>
<p> <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8) </code> expects an answer containing a list of 
 terminated lines, with <i>key: value </i> pairs. The most basic answer to get a match is:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>milterGreylistStatus: Ok</dl>
<p> <i>TRUE </i> can be used as an alias for <i>Ok</i> here. </p>
<p> The answer can be more complex, with keys that will overload the ACL settings:</p>
<dl>
<dt><i>milterGreylistDelay </i></p>
<dd>The greylisting delay to use (time unit suffix allowed).</p>
<dt><i>milterGreylistAutowhite</i></p>
<dd>The autowhite delay to use (time unit suffix allowed).</p>
<dt><i>milterGreylistFlushAddr</i></p>
<dd>The value is ignored. If this key is present, then the IP address for the sender machine will be flushed from greylist and autowhite databases.</p>
<dt><i>milterGreylistCode</i></p>
<dd>The SMTP code to return (e.g.: 551).</p>
<dt><i>milterGreylistECode</i></p>
<dd>The SMTP extended code to return (e.g.: 5.7.1)</p>
<dt><i>milterGreylistMsg</i></p>
<dd>The string to return with SMTP codes.</p>
<dt><i>milterGreylistReport</i></p>
<dd>The string to display in the <i>X-Greylist </i> header.</p>
<dt><i>milterGreylistIgnore</i></p>
<dd>This line will be ignored, without warnings in the logs.</p>
<dt><i>milterGreylistAction</i></p>
<dd>This feature is nifty but use it with caution, as it makes the access list a bit difficult to understand. By specifying the values <i>greylist</i>, <i>whitelist</i>, or <i>blacklist</i>, it is possible to overload the ACL action itself.</dl>
<p> The ACL will match if any of the above key is returned: <i>milterGreylistStatus</i> is not mandatory. </p>
<p> If you use an URL check in a DATA stage ACL, you can post the message header and body to the URL. This is done by appending the <i>postmsg</i> keyword to the <i>urlcheck </i> statement, like in the example above:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>urlcheck&nbsp;<wbr>&quot;extfilter&quot;&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.example.net/f.cgi">http://www.example.net/f.cgi</a>&quot;&nbsp;<wbr>5 postmsg </p>
<p>&nbsp;<wbr>&nbsp;<wbr>dacl blacklist urlcheck&nbsp;<wbr>&quot;extfilter&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>dacl whitelist default</dl>
<p> It is also possible to gather the properties returned by the URL and reuse them in the ACL. This behavior is enabled by the <i>getprop</i> keyword at the end of <i>urlcheck </i> definition. If this option is enabled, the gathered properties can be accessed in the current and following ACL by prefixing them by a dollar ($). If the <i>clear</i> keyword is added, then properties will be cleaned up before handling a new recipient. This avoids properties for several recipients to mix. Finally, the <i>fork</i> keyword instructs <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> to fork a separate instance of itself for performing the queries. Use it if you encounter thread-safety problems. <i>fork</i> is not compatible with <i>postmsg</i>. </p>
<p> Here is an example that will use various DNSRBL depending on a per-recipient setting stored in the <i>dnsrbl</i> attribute of a LDAP directory.</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL2&quot;&nbsp;<wbr>&quot;rbl.example.net&quot;&nbsp;<wbr>&quot;127.0.0.2&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL3&quot;&nbsp;<wbr>&quot;rbl.example.net&quot;&nbsp;<wbr>&quot;127.0.0.3&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL4&quot;&nbsp;<wbr>&quot;rbl.example.net&quot;&nbsp;<wbr>&quot;127.0.0.4&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>urlcheck&nbsp;<wbr>&quot;userconf&quot;&nbsp;<wbr>&quot;<a href="ldap://localhost/dc=example,dc=net?milterGreylistStatus,dnsrbl?one?mail=%r">ldap://localhost/dc=example,dc=net?milterGreylistStatus,dnsrbl?one?mail=%r</a>&quot;&nbsp;<wbr>5 getprop clear </p>
<p>&nbsp;<wbr>&nbsp;<wbr>racl blacklist urlcheck&nbsp;<wbr>&quot;userconf&quot;&nbsp;<wbr>$dnsrbl&nbsp;<wbr>&quot;RBL2&quot;&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL2&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>racl blacklist&nbsp;<wbr>$dnsrbl&nbsp;<wbr>&quot;RBL3&quot;&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL3&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>racl blacklist&nbsp;<wbr>$dnsrbl&nbsp;<wbr>&quot;RBL4&quot;&nbsp;<wbr>dnsrbl&nbsp;<wbr>&quot;RBL4&quot;</dl>
<p> Note that when matching gathered properties, format strings and regex can be used.</p>
<h2>Ldap Checks</h2>
<p>If milter-greylist was built with &#8211;with-openldap, then you can also use <i>ldapcheck</i> for pulling information from an LDAP directory. This works exactly like <i>urlcheck</i>, except that properties are always collected: the only available option is <i>clear</i>. </p>
<p> A list of LDAP URL to use can be specified with the <i>ldapconf </i> keyword. The network timeout is optional.</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>ldapconf&nbsp;<wbr>&quot;<a href="ldap://localhost">ldap://localhost</a>&nbsp;<wbr><a href="ldaps://ldap.example.net">ldaps://ldap.example.net</a>&quot;&nbsp;<wbr>timeout 2s</dl>
<p> When <i>ldaps://</i> is used, the system&#8217;s <i>ldap.conf</i> file is used to locate x509 certificates. </p>
<p> When defining LDAP queries with the <i>ldapcheck</i> statement, note that the scheme and host part of the URL are ignored. Servers listed in <i>ldapconf</i> are used instead.</p>
<h2>Custom Reports</h2>
<p>The <i>stat</i> keyword can be used to specify a custom report for milter-greylist activity. It should be supplied with an output (either file or external command) and a format string. Here is an example:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>stat&nbsp;<wbr>&quot;&gt;&gt;/var/log/milter-greylist.log&quot;&nbsp;<wbr>&quot;%T{%T},%i,%f,%r,%A
&quot;</dl>
<p> If the output starts by <i>&gt;&gt;</i> or <i>&gt;</i> then it is a file. Use <i>&gt;&gt; </i> to append to an existing file, and use <i>&gt; </i> to overwrite it. If the output starts by a <i>|</i> then the output is a shell command, like in the example below:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>stat&nbsp;<wbr>&quot;|logger -p local7.info&quot;&nbsp;<wbr>&quot;%T{%T},%i,%f,%r,%A
&quot;</dl>
<p> The format string gets substituted as URL checks format string: %r gets substituted by the recipient, %f by the sender, and so on. See the <code>FORMAT STRINGS</code> section for a complete list of available substitutions.</p>
<h2>Command-Line Flag Equivalents</h2>
<p>Most <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> command-line options have equivalent options that can be set in the configuration file. Note that if a command line option is supplied, it will always override the configuration file. </p>
<p> If a command-line equivalent keyword is used more than once, the last keyword will override the previous ones.</p>
<dl>
<dt><i>verbose</i></p>
<dd>Enable debug output. This is equivalent to the <code>-v</code> flag.</p>
<dt><i>quiet</i></p>
<dd>Do not tell clients how much time remains before their e-mail will be accepted. This is equivalent to the <code>-q</code> flag.</p>
<dt><i>nodetach</i></p>
<dd>Do not fork and go into the background. This is equivalent to the <code>-D</code> flag.</p>
<dt><i>noauth</i></p>
<dd>Greylist clients regardless if they succeeded SMTP AUTH or STARTTLS. Equivalent to the <code>-A</code> flag.</p>
<dt><i>noaccessdb</i></p>
<dd>Normally <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> will whitelist a message if <code><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</code> defines a ${greylist} macro set to WHITE. This enables complex whitelisting rules based on the Sendmail access DB. This option inhibits this behavior.</p>
<dt><i>nospf</i></p>
<dd>Greylist clients regardless if they are SPF-compliant. Equivalent to the <code>-S</code> flag.</p>
<dt><i>testmode</i></p>
<dd>Enable test mode. Equivalent to the <code>-T</code> flag. This option is deprecated.</p>
<dt><i>greylist</i></p>
<dd>The argument sets how much time <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> will want the client to wait between the first attempt and the time the message is accepted. The time is given in seconds, except if a unit is given: m for minutes, h for hours, and d for days. The <i>greylist </i> keyword is equivalent to the <code>-w </code> option. Here is an example that sets the delay to 45 minutes:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>greylist 45m</p>
<dt><i>autowhite</i></p>
<dd>This sets the auto-whitelisting duration, equivalent to the <code>-a</code> command-line option. As for the <i>greylist</i> keyword, units can be supplied. Here is an example for a 3 day long auto-whitelisting:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>autowhite 3d</p>
<dt><i>pidfile</i></p>
<dd>This causes <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> to write its PID into the file given as argument, like the <code>-P</code> command line argument does. The path to the file must be absolute and it must be enclosed in quotes. Here is an example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>pidfile&nbsp;<wbr>&quot;/var/run/greylist.pid&quot;</p>
<dt><i>dumpfile</i></p>
<dd>This chooses the location of the greylist dump file, like the <code>-d</code> command line option does. The path must be absolute and enclosed in quotes. It can optionally be followed by an octal permission mode. Example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>dumpfile&nbsp;<wbr>&quot;/var/lib/milter-greylist/db/greylist.db&quot;&nbsp;<wbr>640</p>
<dt><i>subnetmatch</i></p>
<dd>This is equivalent to the <code>-L </code> command line option. It takes a slash followed by a CIDR mask as argument, and it commands the subnet matching feature. Example, for a class C wide matching:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>subnetmatch&nbsp;<wbr>/24</p>
<dt><i>subnetmatch6</i></p>
<dd>This is equivalent to the <code>-M</code> command line option. It takes a slash followed by a prefixlen as argument, and it commands the subnet matching feature. Example, for a subnet wide matching:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>subnetmatch6&nbsp;<wbr>/64</p>
<dt><i>socket</i></p>
<dd>Like the <code>-p</code> command line option, this keyword is used to specify the socket used to communicate with <code><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</code>. It must be enclosed in quotes and can optionally be followed by an octal permission mode (valid values are 666, 660 or 600, other values cause an error):</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>socket&nbsp;<wbr>&quot;/var/run/milter-greylist/milter-greylist.sock&quot;&nbsp;<wbr>660</p>
<dt><i>user</i></p>
<dd>This keyword should be followed by a quoted user login and optionally a colon followed by a groupname. Like the <code>-u</code> option, this is used to run <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code> as a non root user. Here is an example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>user&nbsp;<wbr>&quot;smmsp&quot;</dl>
<h2>Miscellaneous</h2>
<p>These options have no command line equivalent:</p>
<dl>
<dt><i>logfac</i></p>
<dd>Sets the syslog facility for messages. Can be set to any of the standard facilities: <i>kern</i>, <i>user</i>, <i>mail</i>, <i>daemon</i>, <i>auth</i>, <i>syslog</i>, <i>lpr</i>, <i>news</i>, <i>uucp</i>, <i>cron</i>, <i>authpriv</i>, <i>ftp</i>, <i>local0</i>, <i>local1</i>, <i>local2</i>, <i>local3</i>, <i>local4</i>, <i>local5</i>, <i>local6</i>, <i>local7</i>. Can also be set to <i>none</i> to disable syslog output completely.</p>
<dt><i>timeout</i></p>
<dd>is used to control how long greylist tuples are retained in the database. Value is in seconds, except if a suffix is given (m for minutes, h for hours, d for days). Default is 5 days.</p>
<dt><i>extendedregex</i></p>
<dd>Use extended regular expressions instead of basic regular expressions.</p>
<dt><i>maxpeek</i></p>
<dd>Limit (in bytes) how much of messages are examined for header and body searches.</p>
<dt><i>lazyaw</i></p>
<dd>Make auto-whitelist look at just the IP instead of the (sender IP, sender e-mail address, recipient e-mail address) tuple.</p>
<dt><i>domainexact</i></p>
<dd>match on subdomain boundaries instead of the default suffix matching. E.g. if <i>domainexact</i> is not enabled (the default) then gle.com will match google.com in addtion to gle.com. If <i>domainexact</i> is enabled then, domain names will match on subdomain boundaries (e.g. gle.com will match mail.gle.com and gle.com but not google.com)</p>
<dt><i>drac db</i></p>
<dd>Tell where the DRAC DB file is. This is only available if DRAC support was compiled in. Here is an example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>drac db&nbsp;<wbr>&quot;/usr/local/etc/drac.db&quot;</p>
<dt><i>nodrac</i></p>
<dd>Disable DRAC.</p>
<dt><i>logexpired</i></p>
<dd>This option causes greylist entries that expire to be logged via syslog. This allows you to easily collect the IP addresses and sender names and use them for blacklisting, SPAM scoring, etc. Normally, expirations are only logged if the <code>debug</code> option is set, but that generates a lot of extra messages.</dl>
<p> The configuration file is reloaded automatically once it is modified when new e-mail arrives. Most configuration keywords will take effect immediately, except the following, which will only take effect after a restart of <code><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8)</code>: <i>nodetach</i>, <i>pidfile</i>, <i>socket</i>, and <i>user</i>. </p>
<p> The <i>dumpfreq</i> option can be changed dynamically, but the change will only take effect after the next dump.</p>
<h2>Format Strings</h2>
<p>Various statements in the configuration file accept format strings, where the following % prefixed tokens are substituted. Here is the complete list of available substitutions (Note that some substitutions are not relevant in any context).</p>
<dl>
<dt><i>%r </i></p>
<dd>the message recipient e-mail address</p>
<dt><i>%f</i></p>
<dd>the message sender e-mail address</p>
<dt><i>%i</i></p>
<dd>the sender machine IP address</p>
<dt><i>%I</i></p>
<dd>the sender machine IP address masked by a CIDR. Example: <i>%I{/24}</i></p>
<dt><i>%d</i></p>
<dd>the sender machine DNS address</p>
<dt><i>%h</i></p>
<dd>the SMTP transaction HELO string</p>
<dt><i>%mr</i></p>
<dd>the mailbox part of %r (before the @ sign)</p>
<dt><i>%sr</i></p>
<dd>the site part of %r (after the @ sign)</p>
<dt><i>%mf</i></p>
<dd>the mailbox part of %f (before the @ sign)</p>
<dt><i>%sf</i></p>
<dd>the site part of %f (after the @ sign)</p>
<dt><i>%md</i></p>
<dd>the machine part of %d (before the first . sign)</p>
<dt><i>%sd</i></p>
<dd>the site part of %d (after the first . sign)</p>
<dt><i>%Xc</i></p>
<dd>the SMTP code returned</p>
<dt><i>%Xe</i></p>
<dd>the SMTP extended code returned</p>
<dt><i>%Xm</i></p>
<dd>the SMTP message returned</p>
<dt><i>%Xh</i></p>
<dd>the message displayed in the X-Greylist header</p>
<dt><i>%D</i></p>
<dd>Comma-separated list of DNSRBL for which the sender host matched</p>
<dt><i>%M</i></p>
<dd>a sendmail macro value. Examples: <i>%Mj</i> or <i>%M{if_addr}</i></p>
<dt><i>%g</i></p>
<dd>a regex backreference. For instance, <i>%g{\2}</i> is substituted by the string maching the second parenthesis group in all ACL regex clauses</p>
<dt><i>%T</i></p>
<dd>a brace-enclosed <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3) </code> format string that will be substituted by the system time. Example: <i>%T{%Y%m%d:%H%M%S}</i></p>
<dt><i>%v</i></p>
<dd>milter-greylist&#8217;s version</p>
<dt><i>%G</i></p>
<dd>Offset to GMT (e.g.: -0100)</p>
<dt><i>%C</i></p>
<dd>Sender IP country code, as reported by GeoIP. This is only available if <code>milter-greylist</code> was built with GeoIP support</p>
<dt><i>%Fx</i></p>
<dd>p0f OS fingerprint genre and detail. This is only available if <code>milter-greylist</code> was built with p0f support.</p>
<dt><i>%V</i></p>
<dd>Shortcut to &quot;milter-greylist-%v (%Mj [%M{if_addr}]); %T{%a, %d %b %Y %T} %G (%T{%Z})&quot;</p>
<dt><i>%S </i></p>
<dd>the action performed: <i>accept</i>, <i>tempfail</i>, or <i>reject</i>.</p>
<dt><i>%A</i></p>
<dd>the line number of the ACL that caused the action.</p>
<dt><i>%a</i></p>
<dd>the id string of the ACL that caused the action. If no id was given, the line number is used instead.</p>
<dt><i>%Et</i></p>
<dd>total elapsed time in seconds before a greylisted message has been accepted</p>
<dt><i>%Eh</i></p>
<dd>hours elapsed</p>
<dt><i>%Em</i></p>
<dd>minutes elapsed (modulo one hour)</p>
<dt><i>%Es</i></p>
<dd>seconds elapsed (modulo one minute)</p>
<dt><i>%E</i></p>
<dd>shortcut to %Eh:%Em:Es</p>
<dt><i>%Rt</i></p>
<dd>total remaining time in seconds before a greylisted message will be accepted</p>
<dt><i>%Rh</i></p>
<dd>hours remaining</p>
<dt><i>%Rm</i></p>
<dd>minutes remaining (modulo one hour)</p>
<dt><i>%Rs</i></p>
<dd>seconds remaining (modulo one minute)</p>
<dt><i>%R</i></p>
<dd>shortcut to %Rh:%Rm:Rs</p>
<dt><i>%%</i></p>
<dd>a single % character</dl>
<h2>Authors</h2>
<p>Emmanuel Dreyfus &lt;manu [at] netbsd.org&gt; </p>
<p> <code>milter-greylist</code> received many contributions from (in alphabetical order): Aida Shinra, Adam Katz, Alexander Lobodzinski, Alexandre Cherif, Alexey Popov, Andrew McGill, Attila Bruncsak, Benoit Branciard, Bernhard Schneider, Bob Smith, Constantine A. Murenin, Christian Pelissier, Cyril Guibourg, Dan Hollis, Elrond, Enrico Scholz, Eugene Crosser, Fabien Tassin, Fredrik Pettai, Gary Aitken, Georg Horn, Gert Doering, Greg Troxel, Guido Kerkewitz, Hajimu Umemoto, Hideki ONO, Ivan F. Martinez, Jacques Beigbeder, Jean Benoit, Jeff Rife, Jobst Schmalenbach, Joe Pruett, Joel Bertrand, Johann E. Klasek, Johann Klasek, John Thiltges, Klas Heggemann, Laurence Moindrot, Lev Walkin, Manuel Badzong, Martin Paul, Matt Kettler, Mattheu Herrb, Matthias Scheler, Matthieu Herrb, Michael Fromme, Moritz Both, Nerijus Baliunas, Pavel Cahyna, Per Holm, Petr Kristof, Ralf S. Engelschall, Ranko Zivojnovic, Remy Card, Rick Adams, Rogier Maas, Romain Kang, Rudy Eschauzier, Stephane Lentz, Thomas Scheunemann, Tim Mooney, Wolfgang Solfrank, and Yaroslav Boychuk. </p>
<p> Thanks to Helmut Messerer and Thomas Pfau for their feedback on the first releases of this software.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-milter-greylist/">milter-greylist</a>(8), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8).</p>
<dl>
<dt>Evan Harris&#8217;s paper:</p>
<dd><i><a rel="nofollow" href="http://projects.puremagic.com/greylisting/">http://projects.puremagic.com/greylisting/</a></i></p>
<dt>milter-greylist&#8217;s web site:</p>
<dd><i><a rel="nofollow" href="http://hcpnet.free.fr/milter-greylist/">http://hcpnet.free.fr/milter-greylist/</a></i> </p>
