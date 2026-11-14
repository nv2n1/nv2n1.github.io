---
title: "sqlgrey(1)"
name: "sqlgrey"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlgrey/"
description: "sqlgrey – Postfix Greylisting Policy Server"
---

<h2 class="name">NAME</h2>
<p> sqlgrey &#8211; Postfix Greylisting Policy Server </p>
<h2>SYNOPSIS</h2>
<p> <code>sqlgrey</code> [<i>options</i>&#8230;] </p>
<pre><code>
 -h, --help                 display this help and exit
     --man                  display man page
     --version              output version information and exit
 -d, --daemonize            run in the background
 -p, --pidfile=FILE         write process ID to FILE
                            (overrides 'pidfile' in configfile)
 -k, --kill                 kill a running sqlgrey
                            (identified by 'pidfile' content)
 -f, --configfile=FILE      read config from FILE
                            (default /etc/sqlgrey/sqlgrey.conf)
                            expecting config_param=value lines,
                            - spaces are ignored,
                            - '#' is used for comments
</code></pre>
<p> See the default config file at /etc/sqlgrey/sqlgrey.conf for runtime parameters. If you got sqlgrey from sources, read the <font SIZE="-1">HOWTO</font> file in the compressed archive. If it came prepackaged, look into the documentation tree for this file: /usr/share/doc/sqlgrey-&lt;version&gt;/ on most Linux distributions for example.</p>
<h2>DESCRIPTION</h2>
<p> Sqlgrey is a Postfix policy server implementing greylisting. </p>
<p> When a request for delivery of a mail is received by Postfix via <font SIZE="-1">SMTP,</font> the triplet <tt>&quot;CLIENT_IP&quot;</tt> / <tt>&quot;SENDER&quot;</tt> / <tt>&quot;RECIPIENT&quot;</tt> is built. If it is the first time that this triplet is seen, or if the triplet was first seen less than <i>reconnect-delay</i> minutes (1 is the default), then the mail gets rejected with a temporary error. Hopefully spammers or viruses will not try again later, as it is however required per <font SIZE="-1">RFC.</font> </p>
<p> In order to alleviate the reconnect delay, sqlgrey uses a 2-level auto-white-list (<font SIZE="-1">AWL</font>) system:</p>
<dl>
<dt>&bull;</p>
<dd> As soon as a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;SENDER&quot;</tt> is accepted, it is added to an <font SIZE="-1">AWL.</font> The couple expires when it isn&#8217;t seen for more than <i>awl-age</i> days (60 is the default).</p>
<dt>&bull;</p>
<dd> If <i>group-domain-level</i> <tt>&quot;SENDER&quot;</tt>s (2 is the default) from the same domain or more use the same <tt>&quot;CLIENT IP&quot;</tt>, another <font SIZE="-1">AWL</font> is used based on a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;DOMAIN&quot;</tt> couple. This couple expires after awl-age days too. This <font SIZE="-1">AWL</font> is meant to be used on high throughput sites in order to :</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> minimize the amount of data stored in database,</p>
<dt>&bull;</p>
<dd> minimize the amount of processing required to find an entry in the <font SIZE="-1">AWL.</font></p>
<dt>&bull;</p>
<dd> don&#8217;t impose any further mail delay when a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;DOMAIN&quot;</tt> couple is known.</dl>
</dl>
<dl>
<dt>
<dd>
<p> It can be disabled by setting <i>group-domain-level</i> to 0.</dl>
</dl>
<p> General idea: </p>
<p> When a <font SIZE="-1">SMTP</font> client has been accepted once, if the <font SIZE="-1">IP</font> isn&#8217;t dynamic, greylisting the <font SIZE="-1">IP</font> again is only a waste of time when it sends another e-mail. As we already know that this <font SIZE="-1">IP</font> runs an RFC-compliant <font SIZE="-1">MTA </font>(at least the 4xx error code handling) and will get the new e-mail through anyway. </p>
<p> In the case of mail relays, these AWLs works very well as the same senders and mail domains are constantly coming through the same <font SIZE="-1">IP</font> addresses -&gt; the e-mails are quickly accepted on the first try. In the case of individual <font SIZE="-1">SMTP</font> servers, this works well if the <font SIZE="-1">IP</font> is fixed too. When using a floating <font SIZE="-1">IP</font> address, the AWLs are defeated, but it should be the least common case by far. </p>
<p> Why do we put the domain in the <font SIZE="-1">AWL</font> and not the <font SIZE="-1">IP</font> only ? If we did only store <font SIZE="-1">IP</font> addresses, polluting the <font SIZE="-1">AWL</font> would be far too easy. It would only take one correctly configured <font SIZE="-1">MTA</font> sending one e-mail from one <font SIZE="-1">IP</font> one single time to put it in a whitelist used whatever future mails from this <font SIZE="-1">IP</font> look like. </p>
<p> With this <font SIZE="-1">AWL</font> system, one single mail can only allow whitelisting of mails from a single sender from the same <font SIZE="-1">IP&#8230;</font></p>
<h2>INSTALLATION</h2>
<dl>
<dt>&bull;</p>
<dd> Create a <tt>&quot;sqlgrey&quot;</tt> user. This will be the user the daemon runs as.</p>
<dt>&bull;</p>
<dd> When using a full-fledge <font SIZE="-1">SGBD </font>(MySQL and PostgreSQL, not SQLite), create a &#8216;sqlgrey&#8217; db user and a &#8216;sqlgrey&#8217; database. Grant access to the newly created database to sqlgrey.</p>
<dt>&bull;</p>
<dd> Use the packaged init script to start sqlgrey at boot and start it manually.</dl>
<h2>CONFIGURATION</h2>
<h3>General</h3>
<dl>
<dt>&bull;</p>
<dd> Start by adding check_policy_service after reject_unauth_destination in /etc/postfix/main.cf : </p>
<pre>
 smtpd_recipient_restrictions =
               ...
               reject_unauth_destination
               check_policy_service inet:127.0.0.1:2501
</pre>
<dt>&bull;</p>
<dd> Be aware that some servers do not behave correctly and do not resend mails (as required by the standard) or use unique return addresses. This is the reason why you should maintain whitelists for them. </p>
<p> SQLgrey comes with a comprehensive whitelisting system. It can even be configured to fetch up-to-date whitelists from a repository. See the <font SIZE="-1">HOWTO</font> for the details.</dl>
<h3>Disabling greylisting for some users</h3>
<p> If you want to disable greylisting for some users you can configure Postfix like this: </p>
<p> /etc/postfix/sqlgrey_recipient_access:<br />
&nbsp;<wbr>&nbsp;<wbr>i_like_spam [at] ee.ethz.ch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">OK</font> </p>
<p> Then you&#8217;ll add a check_recipient_access in main.cf before the check_policy_service :<br />
&nbsp;<wbr>smtpd_recipient_restrictions&nbsp;<wbr>=<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>reject_unauth_destination<br />
&nbsp;<wbr>check_client_access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hash:/etc/postfix/sqlgrey_client_access<br />
&nbsp;<wbr>check_recipient_access hash:/etc/postfix/sqlgrey_recipient_access<br />
&nbsp;<wbr>check_policy_service inet:127.0.0.1:10023</p>
<h2>SEE ALSO</h2>
<p> See &lt;<a rel="nofollow" href="http://www.greylisting.org/">http://www.greylisting.org/</a>&gt; for a description of what greylisting is and &lt;<a rel="nofollow" href="http://www.postfix.org/SMTPD_POLICY_README.html">http://www.postfix.org/SMTPD_POLICY_README.html</a>&gt; for a description of how Postfix policy servers work.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 by Lionel Bouton.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, <font SIZE="-1">MA 02111-1307 USA</font></p>
<h2>AUTHOR</h2>
<p> Lionel Bouton&nbsp;<wbr>&lt;lionel-dev [at] bouton.name&gt; </p>
<h2>Index</h2>
