---
title: "whois(1)"
name: "whois"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whois/"
description: "whois – client for the whois directory service"
---

<h2 class="name">NAME</h2>
<p> whois &#8211; client for the whois directory service </p>
<h2>SYNOPSIS</h2>
<p> <code>whois</code> [ {~<code>-h</code>~|~<code>&#8211;host</code>~} <i>HOST</i> ] [ {~<code>-p</code>~|~<code>&#8211;port</code>~} <i>PORT</i> ] [~<code>-abBcdGHIKlLmMrRx</code> ] [~<code>-g</code><i>~SOURCE:FIRST-LAST</i> ] [~<code>-i</code>~ <i>ATTR</i>[,<i>ATTR</i>]&#8230;~] [~<code>-s</code>~ <i>SOURCE</i>[,<i>SOURCE</i>]&#8230;~] [~<code>-T</code>~ <i>TYPE</i>[,<i>TYPE</i>]&#8230;~] [~<code>&#8211;verbose</code>~] [~<code>&#8211;no-recursion</code>~] <i>OBJECT</i> </p>
<p> <code>whois</code> <code>-q</code> <i>KEYWORD</i> </p>
<p> <code>whois</code> <code>-t</code> <i>TYPE</i> </p>
<p> <code>whois</code> <code>-v</code> <i>TYPE</i> </p>
<p> <code>whois &#8211;help</code> </p>
<p> <code>whois &#8211;version</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>whois</code> searches for an object in a <i>RFC 3912</i> database. </p>
<p> This version of the whois client tries to guess the right server to ask for the specified object. If no guess can be made it will connect to <i>whois.networksolutions.com</i> for NIC handles or <i>whois.arin.net</i> for IPv4 addresses and network names. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h </code></p>
<dd> <i>HOST</i>, <code>&#8211;host=</code><i>HOST</i> Connect to <i>HOST</i>.</p>
<dt><code>-H</code></p>
<dd> Do not display the legal disclaimers that some registries like to show you.</p>
<dt><code>-p </code></p>
<dd> <i>PORT</i>, <code>&#8211;port=</code><i>PORT</i> Connect to <i>PORT</i>.</p>
<dt><code>-I</code></p>
<dd> First query <i>whois.iana.org</i> and then follow its referral to the whois server authoritative for that request. This works for IP addresses, AS numbers and domains. <code>BEWARE</code>: this implies that the IANA server will receive your complete query.</p>
<dt><code>&#8211;no-recursion</code></p>
<dd> Disable recursion from registry to registrar servers.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>&#8211;help</code></p>
<dd> Display online help.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the program version.</dl>
<p> Other options are flags understood by <i>whois.ripe.net</i> and some other RIPE-like servers:</p>
<dl>
<dt><code>-a</code></p>
<dd> Also search all the mirrored databases.</p>
<dt><code>-b</code></p>
<dd> Return brief IP address ranges with abuse contact.</p>
<dt><code>-B</code></p>
<dd> Disable objects filtering. (Show the e-mail addresses.)</p>
<dt><code>-c</code></p>
<dd> Return the smallest IP address range with a reference to an irt object.</p>
<dt><code>-d</code></p>
<dd> Return the reverse DNS delegation object too.</p>
<dt><code>-g </code></p>
<dd> <i>SOURCE:FIRST-LAST</i> Search updates from <i>SOURCE</i> database between <i>FIRST</i> and <i>LAST</i> update serial number. It is useful to obtain Near Real Time Mirroring stream.</p>
<dt><code>-G</code></p>
<dd> Disable grouping of associated objects.</p>
<dt><code>-i </code></p>
<dd> <i>ATTR[,ATTR]&#8230;</i> Inverse-search objects having associated attributes. <i>ATTR</i> is the attribute name, while the positional <i>OBJECT</i> argument is the attribute value.</p>
<dt><code>-K</code></p>
<dd> Return primary key attributes only. An exception is the <i>members</i> attribute of <i>set</i> objects, which is always returned. Another exception are all attributes of the objects <i>organisation</i>, <i>person</i> and <i>role</i>, that are never returned.</p>
<dt><code>-l</code></p>
<dd> Return the one level less specific object.</p>
<dt><code>-L</code></p>
<dd> Return all levels of less specific objects.</p>
<dt><code>-m</code></p>
<dd> Return all one level more specific objects.</p>
<dt><code>-M</code></p>
<dd> Return all levels of more specific objects.</p>
<dt><code>-q </code></p>
<dd> <i>KEYWORD</i> Return information about the server. <i>KEYWORD</i> can be <i>version</i> for the server version, <i>sources</i> for the list of database sources or <i>types</i> for the list of supported object types.</p>
<dt><code>-r</code></p>
<dd> Disable recursive lookups for contact information.</p>
<dt><code>-R</code></p>
<dd> Disable following referrals and force showing the object from the local copy in the server.</p>
<dt><code>-s </code></p>
<dd> <i>SOURCE[,SOURCE]&#8230;</i> Request the server to search for objects mirrored from <i>SOURCE</i>. Sources are delimited by comma, and the order is significant. Use the <i>-q sources</i> parameter to obtain a list of valid sources.</p>
<dt><code>-t </code></p>
<dd> <i>TYPE</i> Return the template for a object of <i>TYPE</i>.</p>
<dt><code>-T </code></p>
<dd> <i>TYPE[,TYPE]&#8230;</i> Restrict the search to objects of <i>TYPE</i>. Multiple types are separated by a comma.</p>
<dt><code>-v </code></p>
<dd> <i>TYPE</i> Return the verbose template for a object of <i>TYPE</i>.</p>
<dt><code>-x</code></p>
<dd> Search for only exact match on network address prefix.</dl>
<h2>NOTES</h2>
<p> When querying the Verisign gTLDs (e.g. .com, .net&#8230;) thin registry servers for a domain, the program will automatically prepend the <i>domain</i> keyword to only show domain records. The <i>nameserver</i> or <i>registrar</i> keywords must be used to show other kinds of records. </p>
<p> When querying <i>whois.arin.net</i> for IPv4 or IPv6 networks, the CIDR netmask length will be automatically removed from the query string. </p>
<p> When querying <i>whois.nic.ad.jp</i> for AS numbers, the program will automatically convert the request in the appropriate format, inserting a space after the string <i>AS</i>. </p>
<p> When querying <i>whois.denic.de</i> for domain names and no other flags have been specified, the program will automatically add the flag <i>-T dn</i>. </p>
<p> When querying <i>whois.dk-hostmaster.dk</i> for domain names and no other flags have been specified, the program will automatically add the flag <i>&#8211;show-handles</i>. </p>
<p> RIPE-specific command line options are ignored when querying non-RIPE servers. This may or may not be the behaviour intended by the user. When using non-standard query parameters then the command line options which are not to be interpreted by the client must follow the <i>&#8212;</i> separator (which marks the beginning of the query string). </p>
<p> If the <i>/etc/whois.conf</i> configuration file exists, it will be consulted to find a server before applying the normal rules. Each line of the file should contain a regular expression to be matched against the query text and the whois server to use, separated by white space. IDN domains must use the ACE format. </p>
<p> The whois protocol does not specify an encoding for characters which cannot be represented by ASCII and implementations vary wildly. If the program knows that a specific server uses a certain encoding, if needed it will transcode the server output to the encoding specified by the current system locale. </p>
<p> Command line arguments will always be interpreted accordingly to the current system locale and converted to the IDN ASCII Compatible Encoding.</p>
<h2>FILES</h2>
<p> /etc/whois.conf</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>LANG</p>
<dd> When querying <i>whois.nic.ad.jp</i> and <i>whois.jprs.jp</i> English text is requested unless the <i>LANG</i> or <i>LC_MESSAGES</i> environment variables specify a Japanese locale.</p>
<dt>WHOIS_OPTIONS</p>
<dd> A list of options which will be evaluated before the ones specified on the command line.</p>
<dt>WHOIS_SERVER</p>
<dd> This server will be queried if the program cannot guess where some kind of objects are located. If the variable does not exist then <i>whois.arin.net</i> will be queried.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-whois-conf/">whois.conf</a></i>(5). </p>
<p> <i>RFC 3912</i>: WHOIS Protocol Specification. </p>
<p> <i>RIPE Database Query Reference Manual</i>: &lt;<i><a rel="nofollow" href="http://www.ripe.net/data-tools/support/documentation/ripe-database-query-reference-manual">http://www.ripe.net/data-tools/support/documentation/ripe-database-query-reference-manual</a></i>&gt;</p>
<h2>BUGS</h2>
<p> The program may have buffer overflows in the command line parser: be sure to not pass untrusted data to it. It should be rewritten to use a dynamic strings library.</p>
<h2>HISTORY</h2>
<p> This program closely tracks the user interface of the whois client developed at RIPE by Ambrose Magee and others on the base of the original BSD client.</p>
<h2>AUTHOR</h2>
<p> <code>Whois</code> and this man page were written by Marco d&#8217;Itri &lt;<i>md [at] linux.it</i>&gt; and are licensed under the terms of the GNU General Public License, version 2 or higher. </p>
<h2>Index</h2>
