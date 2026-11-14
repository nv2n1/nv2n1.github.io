---
title: "postgrey(8)"
name: "postgrey"
section: "8"
letter: "p"
url: "/docs/linux/man/8-postgrey/"
description: "postgrey – Postfix Greylisting Policy Server"
---

<p>postgrey &#8211; Postfix Greylisting Policy Server</p>
<h2>Synopsis</h2>
<p><code>postgrey</code> [<i>options</i>&#8230;] </p>
<pre><code>-h, --help              display this help and exit
     --version           output version information and exit
 -v, --verbose           increase verbosity level
     --syslog-facility   Syslog facility to use (default mail)
 -q, --quiet             decrease verbosity level
 -u, --unix=PATH         listen on unix socket PATH
 -i, --inet=[HOST:]PORT  listen on PORT, localhost if HOST is not specified
 -d, --daemonize         run in the background
     --pidfile=PATH      put daemon pid into this file
     --user=USER         run as USER (default: postgrey)
     --group=GROUP       run as group GROUP (default: postgrey)
     --dbdir=PATH        put db files in PATH (default: /var/spool/postfix/postgrey)
     --delay=N           greylist for N seconds (default: 300)
     --max-age=N         delete entries older than N days since the last time
                         that they have been seen (default: 35)
     --retry-window=N    allow only N days for the first retrial (default: 2)
                         append 'h' if you want to specify it in hours
     --greylist-action=A if greylisted, return A to Postfix (default: DEFER_IF_PERMIT)
     --greylist-text=TXT response when a mail is greylisted
                         (default: Greylisted + help url, see below)
     --lookup-by-subnet  strip the last 8 bits from IP addresses (default)
     --lookup-by-host    do not strip the last 8 bits from IP addresses
     --privacy           store data using one-way hash functions
     --hostname=NAME     set the hostname (default: `hostname`)
     --exim              don't reuse a socket for more than one query (exim compatible)
     --whitelist-clients=FILE     default: /etc/postfix/postgrey_whitelist_clients
     --whitelist-recipients=FILE  default: /etc/postfix/postgrey_whitelist_recipients
     --auto-whitelist-clients=N   whitelist host after first successful delivery
                                  N is the minimal count of mails before a client is
                                  whitelisted (turned on by default with value 5)
                                  specify N=0 to disable.
     --listen-queue-size=N        allow for N waiting connections to our socket
     --x-greylist-header=TXT      header when a mail was delayed by greylisting
                                  default: X-Greylist: delayed &lt;seconds&gt; seconds by postgrey-&lt;version&gt; at &lt;server&gt;;
&lt;date&gt;

    Note that the-- whitelist - x options can be specified multiple times,
    and that per default / etc / postfix / postgrey_whitelist_clients.local is also read, so that you can put there local entries.</code></pre>
<h2>Description</h2>
<p>Postgrey is a Postfix policy server implementing greylisting. </p>
<p> When a request for delivery of a mail is received by Postfix via <font SIZE="-1">SMTP,</font> the triplet <tt>&quot;CLIENT_IP&quot;</tt> / <tt>&quot;SENDER&quot;</tt> / <tt>&quot;RECIPIENT&quot;</tt> is built. If it is the first time that this triplet is seen, or if the triplet was first seen less than <i>delay</i> seconds (300 is the default), then the mail gets rejected with a temporary error. Hopefully spammers or viruses will not try again later, as it is however required per <font SIZE="-1">RFC.</font> </p>
<p> Note that you shouldn&#8217;t use the &#8211;lookup-by-host option unless you know what you are doing: there are a lot of mail servers that use a pool of addresses to send emails, so that they can change <font SIZE="-1">IP</font> every time they try again. That&#8217;s why without this option postgrey will strip the last byte of the <font SIZE="-1">IP</font> address when doing lookups in the database.</p>
<h3>Installation</h3>
<dl>
<dt>&bull;</p>
<dd>Create a <tt>&quot;postgrey&quot;</tt> user and the directory where to put the database <i>dbdir</i> (default: <tt>&quot;/var/spool/postfix/postgrey&quot;</tt>)</p>
<dt>&bull;</p>
<dd>Write an init script to start postgrey at boot and start it. Like this for example: </p>
<pre> postgrey --inet=10023 -d</pre>
<p><i>contrib/postgrey.init</i> in the postgrey source distribution includes a LSB-compliant init script by Adrian von Bidder for the Debian system.</p>
<dt>&bull;</p>
<dd>Put something like this in /etc/main.cf: </p>
<pre> smtpd_recipient_restrictions =
 permit_mynetworks
 ...
 reject_unauth_destination
 check_policy_service inet:127.0.0.1:10023</pre>
<dt>&bull;</p>
<dd>Install the provided postgrey_whitelist_clients and postgrey_whitelist_recipients in /etc/postfix.</p>
<dt>&bull;</p>
<dd>Put in /etc/postfix/postgrey_whitelist_recipients users that do not want greylisting.</dl>
<h3>Whitelists</h3>
<p>Whitelists allow you to specify client addresses or recipient address, for which no greylisting should be done. Per default postgrey will read the following files: </p>
<pre> /etc/postfix/postgrey_whitelist_clients
 /etc/postfix/postgrey_whitelist_clients.local
 /etc/postfix/postgrey_whitelist_recipients</pre>
<p>You can specify alternative paths with the &#8211;whitelist-x options. </p>
<p> Postgrey whitelists follow similar syntax rules as Postfix access tables. The following can be specified for <code>recipient addresses</code>:</p>
<dl>
<dt>domain.addr</p>
<dd><tt>&quot;domain.addr&quot;</tt> domain and subdomains.</p>
<dt>name@</p>
<dd><tt>&quot;name@.*&quot;</tt> and extended addresses <tt>&quot;name+blabla@.*&quot;</tt>.</p>
<dt>name [at] domain.addr</p>
<dd><tt>&quot;name [at] domain.addr&quot;</tt> and extended addresses.</p>
<dt>/regexp/</p>
<dd>anything that matches <tt>&quot;regexp&quot;</tt> (the full address is matched).</dl>
<p> The following can be specified for <code>client addresses</code>:</p>
<dl>
<dt>domain.addr</p>
<dd><tt>&quot;domain.addr&quot;</tt> domain and subdomains.</p>
<dt><font SIZE="-1">IP1.IP2.IP3.IP4</font></p>
<dd><font SIZE="-1">IP</font> address <font SIZE="-1">IP1.IP2.IP3.IP4.</font> You can also leave off one number, in which case only the first specified numbers will be checked.</p>
<dt><font SIZE="-1">IP1.IP2.IP3.IP4/MASK</font></p>
<dd>CIDR-syle network. Example: 192.168.1.0/24</p>
<dt>/regexp/</p>
<dd>anything that matches <tt>&quot;regexp&quot;</tt> (the full address is matched).</dl>
<h3>Auto-whitelisting clients</h3>
<p>With the option &#8211;auto-whitelist-clients a client <font SIZE="-1">IP</font> address will be automatically whitelisted if the following conditions are met:</p>
<dl>
<dt>&bull;</p>
<dd>At least 5 successfull attempts of delivering a mail (after greylisting was done). That number can be changed by specifying a number after the &#8211;auto-whitelist-clients argument. Only one attempt per hour counts.</p>
<dt>&bull;</p>
<dd>The client was last seen before &#8211;max-age days (35 per default).</dl>
<h3>Greylist Action</h3>
<p>To set the action to be returned to postfix when a message fails postgrey&#8217;s tests and should be deferred, use the &#8211;greylist-action=ACTION option. </p>
<p> By default, postgrey returns <font SIZE="-1">DEFER_IF_PERMIT,</font> which causes postfix to check the rest of the restrictions and defer the message only if it would otherwise be accepted. A delay action of 451 causes postfix to always defer the message with an <font SIZE="-1">SMTP</font> reply code of 451 (temp fail). </p>
<p> See the postfix manual page <i><a href="/docs/linux/man/5-access/">access</a></i>(5) for a discussion of the actions allowed.</p>
<h3>Greylist Text</h3>
<p>When a message is greylisted, an error message like this will be sent at the SMTP-level: </p>
<pre> Greylisted, see <a rel="nofollow" href="http://postgrey.schweikert.ch/help/example.com.html">http://postgrey.schweikert.ch/help/example.com.html</a></pre>
<p>Usually no user should see that error message and the idea of that <font SIZE="-1">URL</font> is to provide some help to system administrators seeing that message or users of broken mail clients which try to send mails directly and get a greylisting error. Note that the default help-URL contains the original recipient domain (example.com), so that domain-specific help can be presented to the user (on the default page it is said to contact postmaster [at] example.com) </p>
<p> You can change the text (and <font SIZE="-1">URL</font>) with the <code>&#8211;greylist-text</code> parameter. The following special variables will be replaced in the text:</p>
<dl>
<dt>%s</p>
<dd>How many seconds left until the greylisting is over (300).</p>
<dt>%r</p>
<dd>Mail-domain of the recipient (example.com).</dl>
<h3>Greylist Header</h3>
<p>When a message is greylisted, an additional header can be prepended to the header section of the mail: </p>
<pre> X-Greylist: delayed %t seconds by postgrey-%v at %h; %d</pre>
<p>You can change the text with the <code>&#8211;x-greylist-header</code> parameter. The following special variables will be replaced in the text:</p>
<dl>
<dt>%t</p>
<dd>How many seconds the mail has been delayed due to greylisting.</p>
<dt>%v</p>
<dd>The version of postgrey.</p>
<dt>%d</p>
<dd>The date.</p>
<dt>%h</p>
<dd>The host.</dl>
<h3>Privacy</h3>
<p>The &#8211;privacy option enable the use of a <font SIZE="-1">SHA1</font> hash function to store IPs and emails in the greylisting database. This will defeat straight forward attempts to retrieve mail user behaviours.</p>
<h3><font SIZE="-1">SEE ALSO</font></h3>
<p>See &lt;<a rel="nofollow" href="http://www.greylisting.org/">http://www.greylisting.org/</a>&gt; for a description of what greylisting is and &lt;<a rel="nofollow" href="http://www.postfix.org/SMTPD_POLICY_README.html">http://www.postfix.org/SMTPD_POLICY_README.html</a>&gt; for a description of how Postfix policy servers work.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2004-2007 by <font SIZE="-1">ETH</font> Zurich. All rights reserved. Copyright (c) 2007 by Open Systems <font SIZE="-1">AG.</font> All rights reserved.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>Author</h2>
<p>David Schweikert&nbsp;<wbr>&lt;david [at] schweikert.ch&gt;</p>
