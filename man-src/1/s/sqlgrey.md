---

title: "sqlgrey(1)"
name: "sqlgrey"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlgrey/"
description: "sqlgrey – Postfix Greylisting Policy Server"
---

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
<p> See the default config file at /etc/sqlgrey/sqlgrey.conf for runtime parameters. If you got sqlgrey from sources, read the HOWTO file in the compressed archive. If it came prepackaged, look into the documentation tree for this file: /usr/share/doc/sqlgrey-&lt;version&gt;/ on most Linux distributions for example.</p>
<h2>DESCRIPTION</h2>
<p> Sqlgrey is a Postfix policy server implementing greylisting. </p>
<p> When a request for delivery of a mail is received by Postfix via SMTP, the triplet <tt>&quot;CLIENT_IP&quot;</tt> / <tt>&quot;SENDER&quot;</tt> / <tt>&quot;RECIPIENT&quot;</tt> is built. If it is the first time that this triplet is seen, or if the triplet was first seen less than <i>reconnect-delay</i> minutes (1 is the default), then the mail gets rejected with a temporary error. Hopefully spammers or viruses will not try again later, as it is however required per RFC. </p>
<p> In order to alleviate the reconnect delay, sqlgrey uses a 2-level auto-white-list (AWL) system:</p>
<dl>
<dt>&bull;</dt>
<dd> As soon as a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;SENDER&quot;</tt> is accepted, it is added to an AWL. The couple expires when it isn&#8217;t seen for more than <i>awl-age</i> days (60 is the default).</dd>
<dt>&bull;</dt>
<dd> If <i>group-domain-level</i> <tt>&quot;SENDER&quot;</tt>s (2 is the default) from the same domain or more use the same <tt>&quot;CLIENT IP&quot;</tt>, another AWL is used based on a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;DOMAIN&quot;</tt> couple. This couple expires after awl-age days too. This AWL is meant to be used on high throughput sites in order to :</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> minimize the amount of data stored in database,</dd>
<dt>&bull;</dt>
<dd> minimize the amount of processing required to find an entry in the AWL.</dd>
<dt>&bull;</dt>
<dd> don&#8217;t impose any further mail delay when a <tt>&quot;CLIENT IP&quot;</tt> / <tt>&quot;DOMAIN&quot;</tt> couple is known.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> It can be disabled by setting <i>group-domain-level</i> to 0.</dd></dl>
</dl>
<p> General idea: </p>
<p> When a SMTP client has been accepted once, if the IP isn&#8217;t dynamic, greylisting the IP again is only a waste of time when it sends another e-mail. As we already know that this IP runs an RFC-compliant MTA (at least the 4xx error code handling) and will get the new e-mail through anyway. </p>
<p> In the case of mail relays, these AWLs works very well as the same senders and mail domains are constantly coming through the same IP addresses -&gt; the e-mails are quickly accepted on the first try. In the case of individual SMTP servers, this works well if the IP is fixed too. When using a floating IP address, the AWLs are defeated, but it should be the least common case by far. </p>
<p> Why do we put the domain in the AWL and not the IP only ? If we did only store IP addresses, polluting the AWL would be far too easy. It would only take one correctly configured MTA sending one e-mail from one IP one single time to put it in a whitelist used whatever future mails from this IP look like. </p>
<p> With this AWL system, one single mail can only allow whitelisting of mails from a single sender from the same IP&#8230;</p>
<h2>INSTALLATION</h2>
<dl>
<dt>&bull;</dt>
<dd> Create a <tt>&quot;sqlgrey&quot;</tt> user. This will be the user the daemon runs as.</dd>
<dt>&bull;</dt>
<dd> When using a full-fledge SGBD (MySQL and PostgreSQL, not SQLite), create a &#8216;sqlgrey&#8217; db user and a &#8216;sqlgrey&#8217; database. Grant access to the newly created database to sqlgrey.</dd>
<dt>&bull;</dt>
<dd> Use the packaged init script to start sqlgrey at boot and start it manually.</dd></dl>
<h2>CONFIGURATION</h2>
<h3>General</h3>
<dl>
<dt>&bull;</dt>
<dd> Start by adding check_policy_service after reject_unauth_destination in /etc/postfix/main.cf : </dd>
<pre>
 smtpd_recipient_restrictions =
               ...
               reject_unauth_destination
               check_policy_service inet:127.0.0.1:2501
</pre>
<dt>&bull;</dt>
<dd> Be aware that some servers do not behave correctly and do not resend mails (as required by the standard) or use unique return addresses. This is the reason why you should maintain whitelists for them. </dd>
<p> SQLgrey comes with a comprehensive whitelisting system. It can even be configured to fetch up-to-date whitelists from a repository. See the HOWTO for the details.</dl>
<h3>Disabling greylisting for some users</h3>
<p> If you want to disable greylisting for some users you can configure Postfix like this: </p>
<p> /etc/postfix/sqlgrey_recipient_access:<br/>
&nbsp;<wbr>&nbsp;<wbr>i_like_spam [at] ee.ethz.ch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OK </p>
<p> Then you&#8217;ll add a check_recipient_access in main.cf before the check_policy_service :<br/>
&nbsp;<wbr>smtpd_recipient_restrictions&nbsp;<wbr>=<br/>
&nbsp;<wbr>&#8230;<br/>
&nbsp;<wbr>reject_unauth_destination<br/>
&nbsp;<wbr>check_client_access&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hash:/etc/postfix/sqlgrey_client_access<br/>
&nbsp;<wbr>check_recipient_access hash:/etc/postfix/sqlgrey_recipient_access<br/>
&nbsp;<wbr>check_policy_service inet:127.0.0.1:10023</p>
<h2>SEE ALSO</h2>
<p> See &lt;<a rel="nofollow" href="http://www.greylisting.org/">http://www.greylisting.org/</a>&gt; for a description of what greylisting is and &lt;<a rel="nofollow" href="http://www.postfix.org/SMTPD_POLICY_README.html">http://www.postfix.org/SMTPD_POLICY_README.html</a>&gt; for a description of how Postfix policy servers work.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 by Lionel Bouton.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>AUTHOR</h2>
<p> Lionel Bouton&nbsp;<wbr>&lt;lionel-dev [at] bouton.name&gt; </p>
