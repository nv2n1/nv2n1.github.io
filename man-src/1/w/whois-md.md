---
title: "whois-md(1)"
name: "whois-md"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whois-md/"
description: "whois – client for the whois directory service"
---

<p>whois &#8211; client for the whois directory service</p>
<h2>Synopsis</h2>
<p><code>whois</code> [~{~<code>-h</code> | <code>&#8211;host</code>~}~<i>HOST</i>~] [~{~<code>-p</code> | <code>&#8211;port</code>~}~<i>PORT</i>~] [~<code>-abBcdGHKlLmMrRx</code>~] [~<code>-g</code>~<i>SOURCE:FIRST-LAST</i>~] [~<code>-i</code>~<i>ATTR</i>[<i>,ATTR</i>]&#8230;~] [~<code>-s</code>~<i>SOURCE</i>[<i>,SOURCE</i>]&#8230;~] [~<code>-T</code>~<i>TYPE</i>[<i>,TYPE</i>]&#8230;~] [~<code>&#8211;verbose</code>~] <i>OBJECT</i> </p>
<p> <code>whois</code> <code>-q</code> <i>KEYWORD</i> </p>
<p> <code>whois</code> <code>-t</code> <i>TYPE</i> </p>
<p> <code>whois</code> <code>-v</code> <i>TYPE</i> </p>
<p> <code>whois</code> <code>&#8211;help</code> </p>
<p> <code>whois</code> <code>&#8211;version</code> </p>
<h2>Description</h2>
<p><code>whois</code> searches for an object in a <i>RFC 3912</i> database. </p>
<p> This version of the whois client tries to guess the right server to ask for the specified object. If no guess can be made it will connect to <i>whois.networksolutions.com</i> for NIC handles or <i>whois.arin.net</i> for IPv4 addresses and network names. </p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h HOST, &#8211;host HOST</code></dt>
<dd>Connect to HOST.</dd>
<dt><code>-H</code></dt>
<dd>Do not display the legal disclaimers some registries like to show you.</dd>
<dt><code>-p, &#8211;port PORT</code></dt>
<dd>Connect to PORT.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Be verbose.</dd>
<dt><code>&#8211;help</code></dt>
<dd>Display online help.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Display client version information.</dd></dl>
<p> Other options are flags understood by <i>whois.ripe.net</i> and some other RIPE-like servers:</p>
<dl COMPACT>
<dt><code>-a</code></dt>
<dd>Also search all the mirrored databases.</dd>
<dt><code>-b</code></dt>
<dd>Return brief IP address ranges with abuse contact.</dd>
<dt><code>-B</code></dt>
<dd>Disable object filtering. (Show the e-mail addresses.)</dd>
<dt><code>-c</code></dt>
<dd>Return the smallest IP address range with a reference to an irt object.</dd>
<dt><code>-d</code></dt>
<dd>Return the reverse DNS delegation object too.</dd>
<dt><code>-g SOURCE:FIRST-LAST</code></dt>
<dd>Search updates from <i>SOURCE</i> database between <i>FIRST</i> and <i>LAST</i> update serial number. It&#8217;s useful to obtain Near Real Time Mirroring stream.</dd>
<dt><code>-G</code></dt>
<dd>Disable grouping of associated objects.</dd>
<dt><code>-i ATTR[,ATTR]&#8230;</code></dt>
<dd>Search objects having associated attributes. <i>ATTR</i> is attribute name. Attribute value is positional <i>OBJECT</i> argument.</dd>
<dt><code>-K</code></dt>
<dd>Return primary key attributes only. Exception is <i>members</i> attribute of <i>set</i> object which is always returned. Another exceptions are all attributes of objects <i>organisation</i>, <i>person</i>, and <i>role</i> that are never returned.</dd>
<dt><code>-l</code></dt>
<dd>Return the one level less specific object.</dd>
<dt><code>-L</code></dt>
<dd>Return all levels of less specific objects.</dd>
<dt><code>-m</code></dt>
<dd>Return all one level more specific objects.</dd>
<dt><code>-M</code></dt>
<dd>Return all levels of more specific objects.</dd>
<dt><code>-q KEYWORD</code></dt>
<dd>Return list of keywords supported by server. <i>KEYWORD</i> can be <i>version</i> for server version, <i>sources</i> for list of source databases, or <i>types</i> for object types.</dd>
<dt><code>-r</code></dt>
<dd>Disable recursive look-up for contact information.</dd>
<dt><code>-R</code></dt>
<dd>Disable following referrals and force showing the object from the local copy in the server.</dd>
<dt><code>-s SOURCE[,SOURCE]&#8230;</code></dt>
<dd>Request the server to search for objects mirrored from <i>SOURCES</i>. Sources are delimited by comma and the order is significant. Use <i>-q sources</i> option to obtain list of valid sources.</dd>
<dt><code>-t TYPE</code></dt>
<dd>Return the template for a object of <i>TYPE</i>.</dd>
<dt><code>-T TYPE[,TYPE]&#8230;</code></dt>
<dd>Restrict the search to objects of <i>TYPE</i>. Multiple types are separated by a comma.</dd>
<dt><code>-v TYPE</code></dt>
<dd>Return the verbose template for a object of <i>TYPE</i>.</dd>
<dt><code>-x</code></dt>
<dd>Search for only exact match on network address prefix.</dd></dl>
<h2>Notes</h2>
<p>Please remember that <i>whois.networksolutions.com</i> by default will only search in the domains database. If you want to search for NIC handles you have to prepend a <i>!</i> character. When you do this, the default server becomes <i>whois.networksolutions.com</i>. </p>
<p> When querying <i>whois.arin.net</i> for IPv4 or IPv6 networks, the CIDR netmask length will be automatically removed from the query string. </p>
<p> When querying <i>whois.nic.ad.jp</i> for AS numbers, the program will automatically convert the request in the appropriate format, inserting a space after the string <i>AS</i>. </p>
<p> When querying <i>whois.denic.de</i> for domain names and no other flags have been specified, the program will automatically add the flag <i>-T dn</i>. </p>
<p> When querying <i>whois.dk-hostmaster.dk</i> for domain names and no other flags have been specified, the program will automatically add the flag <i>&#8211;show-handles</i>. </p>
<p> RIPE-specific command line options are ignored when querying non-RIPE servers. This may or may not be the behaviour intended by the user. When querying a non-standard server, command line options which are not to be interpreted by the client should always follow the <i>&#8212;</i> separator (which marks the beginning of the query string). </p>
<p> If the <i>/etc/whois.conf</i> configuration file exists, it will be consulted to find a server before applying the normal rules. Each line of the file should contain a regular expression to be matched against the query text and the whois server to use, separated by white space. IDN domains must use the ACE format. </p>
<p> The whois protocol does not specify an encoding for characters which cannot be represented by ASCII and implementations vary wildly. If the program knows that a specific server uses a certain encoding, if needed it will transcode the server output to the encoding specified by the current system locale. </p>
<p> Command line arguments will always be interpreted accordingly to the current system locale and converted to the IDN ASCII Compatible Encoding.</p>
<h2>Files</h2>
<p>/etc/whois.conf</p>
<h2>Environment</h2>
<dl COMPACT>
<dt>LANG</dt>
<dd>When querying <i>whois.nic.ad.jp</i> and <i>whois.jprs.jp</i> English text is requested unless the <i>LANG</i> or <i>LC_MESSAGES</i> environment variables specify a Japanese locale.</dd>
<dt>WHOIS_OPTIONS</dt>
<dd>A list of options which will be evaluated before the ones specified on the command line.</dd>
<dt>WHOIS_SERVER</dt>
<dd>This server will be queried if the program cannot guess where some kind of objects are located. If the variable does not exist then <i>whois.arin.net</i> will be queried.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-whois-conf/">whois.conf</a></code>(5) </p>
<p> <i>RFC 3912</i>: WHOIS Protocol Specification </p>
<p> <i>RIPE Database Query Reference Manual:</i> <i>&lt;<a rel="nofollow" href="http://www.ripe.net/data-tools/support/documentation/ripe-database-query-reference-manual">http://www.ripe.net/data-tools/support/documentation/ripe-database-query-reference-manual</a>&gt;</i></p>
<h2>Bugs</h2>
<p>The program may have buffer overflows in the command line parser: be sure to not pass untrusted data to it. It should be rewritten to use a dynamics strings library.</p>
<h2>History</h2>
<p>This program closely tracks the user interface of the whois client developed at RIPE by Ambrose Magee and others on the base of the original BSD client. I also added support for the protocol extensions developed by David Kessens of QWest for the 6bone server.</p>
<h2>Author</h2>
<p><code>Whois</code> and this man page were written by Marco d&#8217;Itri &lt;<i>md [at] linux.it</i>&gt; and are licensed under the terms of the GNU General Public License, version 2 or higher.</p>
