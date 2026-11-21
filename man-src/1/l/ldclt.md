---

title: "ldclt(1)"
name: "ldclt"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldclt/"
description: "ldclt – load test program for LDAP"
---

<h2>SYNOPSYS</h2>
<p> <code>ldclt </code> [<i>-qQvV</i>] [<i>-E &lt;max errors&gt;</i>] [<i>-b &lt;base DN&gt;</i>] [<i>-h &lt;host&gt;</i>] [<i>-p &lt;port&gt;</i>] [<i>-t &lt;timeout&gt;</i>] [<i>-D &lt;bind DN&gt;</i>] [<i>-w &lt;passwd&gt;</i>] [<i>-o &lt;SASL option&gt;</i>] [<i>-e &lt;execParams&gt;</i>] [<i>-a &lt;max pending&gt;</i>] [<i>-n &lt;nb threads&gt;</i>] [<i>-i &lt;nb times&gt;</i>] [<i>-N &lt;nb samples&gt;</i>] [<i>-I &lt;err number&gt;</i>] [<i>-T &lt;total&gt;</i>] [<i>-r &lt;low&gt; -R &lt;high&gt;</i>] [<i>-f &lt;filter&gt;</i>] [<i>-s &lt;scope&gt;</i>] [<i>-S &lt;slave&gt;</i>] [<i>-P&lt;master port&gt;</i>] [<i>-W &lt;waitsec&gt;</i>] [<i>-Z &lt;certfile&gt;</i>] </p>
<p> This tool is a LDAP client targeted to validate the reliability of the product under a wide variety of stress conditions. </p>
<h2>OPTIONS</h2>
<p> The valid options are:</p>
<dl>
<dt><code>-a</code></dt>
<dd> Asynchronous mode, with max pending operations.</dd>
<dt><code>-b</code></dt>
<dd> Give the base DN to use. Default &quot;dc=example,dc=com&quot;.</dd>
<dt><code>-D</code></dt>
<dd> Bind DN. See <code>-w</code></dd>
<dt><code>-E</code></dt>
<dd> Max errors allowed. Default 1000.</dd>
<dt><code>-f</code></dt>
<dd> Filter for searches.</dd>
<dt><code>-h</code></dt>
<dd> Host to connect. Default &quot;localhost&quot;.</dd>
<dt><code>-H</code></dt>
<dd> Ldap URL to connect to. Example, <a href="ldap://localhost:389.">ldap://localhost:389.</a> This takes precedence over -h and -p.</dd>
<dt><code>-i</code></dt>
<dd> Number of times inactivity allowed. Default 3 (30 seconds)</dd>
<dt><code>-I</code></dt>
<dd> Ignore errors (cf. <code>-E</code>). Default none.</dd>
<dt><code>-n</code></dt>
<dd> Number of threads. Default 10.</dd>
<dt><code>-N</code></dt>
<dd> Number of samples (10 seconds each). Default infinite.</dd>
<dt><code>-o</code></dt>
<dd> SASL Option.</dd>
<dt><code>-p</code></dt>
<dd> Server port. Default 389.</dd>
<dt><code>-P</code></dt>
<dd> Master port (to check replication). Default 16000.</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode. See option <code>-I</code>.</dd>
<dt><code>-Q</code></dt>
<dd> Super quiet mode.</dd>
<dt><code>-r</code></dt>
<dd> Range&#8217;s low value.</dd>
<dt><code>-R</code></dt>
<dd> Range&#8217;s high value.</dd>
<dt><code>-s</code></dt>
<dd> Scope. May be base, subtree or one. Default subtree.</dd>
<dt><code>-S</code></dt>
<dd> Slave to check.</dd>
<dt><code>-t</code></dt>
<dd> LDAP operations timeout. Default 30 seconds.</dd>
<dt><code>-T</code></dt>
<dd> Total number of operations per thread. Default infinite.</dd>
<dt><code>-v</code></dt>
<dd> Verbose.</dd>
<dt><code>-V</code></dt>
<dd> Very verbose.</dd>
<dt><code>-w</code></dt>
<dd> Bind passwd. See <code>-D</code>.</dd>
<dt><code>-W</code></dt>
<dd> Wait between two operations. Default 0 seconds.</dd>
<dt><code>-Z</code></dt>
<dd> certfile. Turn on SSL and use certfile as the certificate DB</dd>
<dt><code>-e</code></dt>
<dd> Execution parameters:</dd>
<dt>
</dt><dd> <code>add</code> ldap_add() entries.<br />
 <code>append</code> entries to the genldif file.<br />
 <code>ascii</code> ascii 7-bits strings.<br />
 <code>attreplace=name:mask</code> replace attribute of existing entry.<br />
 <code>attrlist=name:name:name</code> specify list of attribs to retrieve<br />
 <code>attrsonly=0|1</code> ldap_search() parameter. Set 0 to read values.<br />
 <code>bindeach</code> ldap_bind() for each operation.<br />
 <code>bindonly</code> only bind/unbind, no other operation is performed.<br />
 <code>close</code> will close() the fd, rather than ldap_unbind().<br />
 <code>cltcertname=name</code> name of the SSL client certificate<br />
 <code>commoncounter</code> all threads share the same counter.<br />
 <code>counteach</code> count each operation not only successful ones.<br />
 <code>delete</code> ldap_delete() entries.<br />
 <code>dontsleeponserverdown</code> will loop very fast if server down.<br />
 <code>emailPerson</code> objectclass=emailPerson (<code>-e</code> add only).<br />
 <code>esearch</code> exact search.<br />
 <code>genldif=filename</code> generates a ldif file<br />
 <code>imagesdir=path</code> specify where are the images.<br />
 <code>incr</code> incremental values.<br />
 <code>inetOrgPerson</code> objectclass=inetOrgPerson (<code>-e</code> add only).<br />
 <code>keydbfile=file</code> filename of the key database<br />
 <code>keydbpin=password</code> password for accessing the key database<br />
 <code>noglobalstats</code> don&#8217;t print periodical global statistics<br />
 <code>noloop</code> does not loop the incremental numbers.<br />
 <code>object=filename</code> build object from input file<br />
 <code>person</code> objectclass=person (<code>-e</code> add only).<br />
 <code>random</code> random filters, etc&#8230;<br />
 <code>randomattrlist=name:name:name</code> random select attrib in the list<br />
 <code>randombase</code> random base DN.<br />
 <code>randombaselow=value</code> low value for random generator.<br />
 <code>randombasehigh=value</code> high value for random generator.<br />
 <code>randombinddn</code> random bind DN.<br />
 <code>randombinddnfromfile=fine</code> retrieve bind DN &amp; passwd from file<br />
 <code>randombinddnlow=value</code> low value for random generator.<br />
 <code>randombinddnhigh=value</code> high value for random generator.<br />
 <code>rdn=attrname:value</code> alternate for <code>-f</code>.<br />
 <code>referral=on|off|rebind</code> change referral behaviour.<br />
 <code>scalab01</code> activates scalab01 scenario.<br />
 <code>scalab01_cnxduration</code> maximum connection duration.<br />
 <code>scalab01_maxcnxnb</code> modem pool size.<br />
 <code>scalab01_wait</code> sleep() between 2 attempts to connect.<br />
 <code>smoothshutdown</code> main thread waits till the worker threads exit.<br />
 <code>string</code> create random strings rather than random numbers.<br />
 <code>v2</code> ldap v2.<br />
 <code>withnewparent</code> rename with newparent specified as argument.<br />
 <code>randomauthid</code> random SASL Authid.<br />
 <code>randomauthidlow=value</code> low value for random SASL Authid.<br />
 <code>randomauthidhigh=value</code> high value for random SASL Authid.</dd></dl>
<h2>AUTHOR</h2>
<p> ldclt was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
