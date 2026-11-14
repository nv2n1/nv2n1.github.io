---
title: "csv2(5)"
name: "csv2"
section: "5"
letter: "c"
url: "/docs/linux/man/5-csv2/"
description: "csv2 – Description of the csv2 zone file that MaraDNS uses"
---

<p>csv2 &#8211; Description of the csv2 zone file that MaraDNS uses</p>
<h2>Description</h2>
<p>The csv2 zone file format is the zone file format introduced in MaraDNS 1.2. This zone file format uses any kind of whitespace (space, tab, and carriage return), or the aq|aq character, to deliminate fields. </p>
<p> <code>Tilde delimination</code> </p>
<p> In MaraDNS 1.3, the tilde (aq~aq) character is used to deliminate records in csv2 zone files; in order to maintain maximum compatibility with MaraDNS 1.2 zone files, this feature is only enabled if a tilde is placed between the first and second record. Otherwise, tildes are not allowed in zone files (except in comments). </p>
<p> Most MaraDNS 1.2 csv2 zone files without the tilde character are compatible with the 1.3 csv2 parser, unless csv2_tilde_handling is set to 3. All MaraDNS 1.2 csv2 zone files will parse in MaraDNS 1.3 if csv2_tilde_handling has a value of 0. MaraDNS 1.2, starting with 1.2.12.04, also supports the csv2_tilde_handling variable (as long as it has a value of 0); this allows the same configuration and zone files to be used in both MaraDNS 1.2 and MaraDNS 1.3. </p>
<p> <code>Resource record format</code> </p>
<p> This zone file format has records in the following form: </p>
<dl>
<dd>name [+ttl] [rtype] rdata ~</dl>
<p> The name is the name of the record we will add, such as &quot;<a rel="nofollow" href="http://www.example.net">www.example.net</a>.&quot;. This must be placed at the beginning of a line. The rtype is the record type for the record, such as &quot;A&quot; (ipv4 IP address), &quot;MX&quot; (mail exchanger), or &quot;AAAA&quot; (ipv6 IP address). The ttl is how long other DNS servers should store this data in their memory (in seconds); this field needs a aq+aq as its initial character. The rdata is the actual data for this record; the format for the rdata is type-specific. </p>
<p> Anything in square brackets is an optional field. If the ttl is not specified, the ttl is set to the default ttl value (see &quot;Default TTL&quot; below). If the rtype is not specified, it is set to be an &quot;A&quot; (ipv4 address) record. </p>
<p> The zone file supports comments; comments are specified by having a aq#aq anywhere between fields or records; when a aq#aq is seen, the csv2 parser ignores any character it sees (with the exception of the aq{aq, which is not allowed in comments) until a newline. A aq#aq can usually be placed inside a field, and indicates the end of a field when placed there. </p>
<p> A aq{aq character can never be placed in a comment. A aq~aq character is always allowed in a comment, and has no special meaning when placed in a comment. </p>
<p> The following record types are supported; a description of the record data format accommodates the record type: </p>
<p> <code>A</code> </p>
<p> An A record stores an ipv4 address. This is the default record type should the record type not be specified. The record type has one field in it: the IP for the record. Examples: </p>
<pre>a.example.net. 10.11.12.13 ~
b.example.net. A 10.11.12.14 ~
c.example.net. +64000 A 10.11.12.15 ~</pre>
<p><code>PTR</code> </p>
<p> A PTR record stores the name for a given ipv4 or ipv6 address, and is used for reverse DNS lookups. This record type has one field in it: The name for the record in question. Examples: </p>
<pre>13.12.11.10.in-addr.arpa. PTR a.example.net. ~
14.12.11.10.in-addr.arpa. PTR b.example.net. ~
15.12.11.10.in-addr.arpa. +64000 PTR c.example.net. ~</pre>
<p><code>MX</code> </p>
<p> A MX record stores a mail exchange record, and is used for mail delivery. This record type has two fields in it: The priority (or &quot;preference&quot; in traditional DNS parlance) of the MX record (lower numbers get higher priority), and the name of the mail exchanger. Example of mail for example.net being mailed to mail.example.net, which has the IP &quot;10.11.12.16&quot;: </p>
<pre>example.net. MX 10 mail.example.net. ~
mail.example.net. 10.11.12.16 ~</pre>
<p><code>AAAA</code> </p>
<p> An AAAA record stores the ipv6 address for a given name. The IP is in standard ipv6 &quot;colon delimited&quot; format: eight 16-bit hexadecimal numbers are separated by colons. Two colons together indicate multiple streams of all-zero hex numbers. This record has only one field, the v6 IP. Example: </p>
<pre>a.example.net. AAAA 3ffe:ffff:ffe:501:ffff::b:c:d ~</pre>
<p><code>SRV</code> </p>
<p> An SRV record stores a &quot;service&quot; definition. This record has four fields: Priority, weight, port, and target. For more information, please refer to RFC 2782. Example: </p>
<pre>_http._tcp.% SRV 0 0 80 a.% ~</pre>
<p><code>NS</code> </p>
<p> An NS record specifies the name servers for a given zone. If the name servers are not delegation name servers (in other words, if the the name servers are the authoritative name servers for the zone), they need to be at the beginning of the zone, either as the first records in the zone, or right after the SOA record. The NS records are optional; if not present, MaraDNS will make an educated guess of that NS records should be there, based on the IPs the MaraDNS process is bound to. This record has one field: The name of the name server machine. Example: </p>
<pre>example.net. NS ns1.example.net. ~
example.net. NS ns2.example.net. ~</pre>
<p><code>SOA</code> </p>
<p> An SOA record stores the start of authority for a given zone file. This record is optional in a CSV2 zone file; should the record not be in the zone file, MaraDNS will synthesize an appropriate SOA record. This record can only exist once in a zone file: As the first record of the zone file. This record has seven fields: The name of the zone, the email address of the person responsible for the zone, and five numeric fields (serial, refresh, retry, expire, and minimum). Note that the SOA minimum does <i>not</i> affect other TTLs in MaraDNS. Example: </p>
<pre>x.org. SOA x.org. email [at] x.org. 1 7200 3600 604800 1800 ~</pre>
<p>The serial numeric field may be replaced by the string aq/serialaq; this string tells the CSV2 zone parser to synthesize a serial number for the zone based on the timestamp for the zone file. This allows one to have the serial number be automatically updated whenever the zone file is edited. Here is how this special field looks in a SOA record: </p>
<pre>x.org. SOA x.org. email [at] x.org. /serial 7200 3600 604800 1800 ~</pre>
<p>The aq/serialaq string is case-sensitive; only aq/serialaq in all lower case will parse. </p>
<p> <code>TXT</code> </p>
<p> A TXT record stores arbitrary text and/or binary data for a given host name. This record has one field: The text data for the record. </p>
<p> A basic text record can be stored by placing ASCII data between two single quotes, as follows: </p>
<pre>example.com. TXT aqThis is an example text fieldaq ~</pre>
<p>Any binary data can be specified; see the <code><a href="/docs/linux/man/5-csv2_txt/">csv2_txt</a>(5)</code> manual page for full details. </p>
<p> If tildes are used to separate records, a TXT record can not contain a aq|aq (pipe) character, a aq#aq character, nor any ASCII control character; these characters can be added to a TXT record via the use of escape sequences; read the csv2_txt man page for details. </p>
<p> <code>SPF</code> </p>
<p> A SPF record is, with the exception of the numeric rtype, identical to a TXT record. SPF records are designed to make it more difficult to forge email. More information about SPF records can be found in RFC4408, or by performing a web search for aqsender policy frameworkaq. </p>
<p> <code>RAW</code> </p>
<p> The RAW record is a special meta-record that allows any otherwise unsupported record type to be stored in a csv2 zone file. The syntax is: </p>
<pre>RAW [numeric rtype] [data] ~</pre>
<p>The numeric rtype is a decimal number. </p>
<p> The data field can, among other thing, have backslashed hex sequences outside of quotes, concatenated by ASCII data inside quotes, such as the following example: </p>
<pre>example.com. RAW 40 aqKitchen sinkaq@aq dataaq ~</pre>
<p>The above example is a &quot;Kitchen Sink&quot; RR with a &quot;meaning&quot; of 16, a &quot;coding&quot; of 1, a &quot;subcoding&quot; of 2, and a data string of &quot;Kitchen sink@ data&quot; (since hex code 40 corresponds to a @ in ASCII). Note that unquoted hex sequences are concatenated with quoted ASCII data, and that spaces are <i>only</i> inside quoted data. </p>
<p> The format for a data field in a RAW record is almost identical to the format for a TXT data field. Both formats are described in full in the <code><a href="/docs/linux/man/5-csv2_txt/">csv2_txt</a>(5)</code> manual page. </p>
<p> <code>FQDN4</code> </p>
<p> The FQDN4 (short for &quot;Fully Qualified Domain Name for IPv4&quot;) record is a special form of the &quot;A&quot; record (see above) that instructs MaraDNS to automatically create the corresponding PTR record. For example, the following is one way of setting up the reverse DNS lookup for x.example.net: </p>
<pre>x.example.net. A 10.3.28.79 ~
79.28.3.10.in-addr.arpa. PTR x.example.net. ~</pre>
<p>But the above two lines in a zone file can also be represented thusly: </p>
<pre>x.example.net. FQDN4 10.3.28.79 ~</pre>
<p>Note that the csv2 parser does not bother to check that any given IP only has a single FQDN4 record; it is up to the DNS administrator to ensure that a given IP has only one FQDN4 record. In the case of there being multiple FQDN4 records with the same IP, MaraDNS will have multiple entries in the corresponding PTR record, which is usually not the desired behavior. </p>
<p> FQDN4 records are not permitted in a csv2_default_zonefile. If you do not know what a csv2_default_zonefile is, you do not have to worry about this limitation. </p>
<p> <code>CNAME</code> </p>
<p> A CNAME record is a pointer to another host name. The CNAME record, in MaraDNS, affects any record type not already specified for a given host name. While MaraDNS allows CNAME and non-CNAME records to share the same host name, this is considered bad practice and is not compatible with some other DNS servers. </p>
<p> CNAME records are not permitted in a csv2_default_zonefile. If you do not know what a csv2_default_zonefile is, this fact is of no relevance.</p>
<h2>Historical and uncommon resource records</h2>
<p>The following resource records are mainly of historical interest, or are not commonly used. </p>
<p> <code>HINFO</code> </p>
<p> An HINFO record is a description of the CPU (processor) and OS that a given host is using. The format for this record is identical to a TXT record, except that the field must have precisely two chunks. </p>
<p> The first chunk of a HINFO record is the CPU the host is running; the second chunk is the OS the host is running. </p>
<p> Example: </p>
<pre>example.com. HINFO aqIntel Pentium IIIaq;aqCentOS Linux 3.7aq ~</pre>
<p>This resource record is not actively used&#8211;the IANA has a list of CPUs and OSes that this record is supposed to have. However, this list has not been updated since 2002. </p>
<p> <code>WKS</code> </p>
<p> WKS records are historical records which have been superseded by SRV records. The format of the record is an IP, followed by a protocol number (6 means TCP), followed by a list of ports that a given server has available for services. </p>
<p> For example, to advertise that example.net has the IP 10.1.2.3, and has a SSH, HTTP (web), and NNTP server: </p>
<pre>example.net. WKS 10.1.2.3 6 22,80,119 ~</pre>
<p>MaraDNS only allows up to 10 different port numbers in a WKS record, and requires that the listed port numbers are not be higher than 1023. </p>
<p> <code>MD and MF</code> </p>
<p> MD and MF records are RR types that existed before MX records, and were made obsolete by MX records. RFC1035 says that a DNS server can either reject these records or convert these records in to MX records. BIND rejects these records; MaraDNS converts them. </p>
<p> Example: </p>
<pre>example.net. MD a.example.net. ~
example.net. MF b.example.net. ~</pre>
<p>Is equivalent to: </p>
<pre>example.net. MX 0 a.example.net. ~
example.net. MX 10 b.example.net. ~</pre>
<p><code>MB, MG, MINFO, and MR</code> </p>
<p> In the late 1980s, an alternative to MX records was proposed. This alternative utilized MB, MG, MINFO, and MR records. This alternative failed to gather popularity. However, these records were codified in RFC1035, and are supported by MaraDNS. Here is what the records look like: </p>
<pre>example.net. MB mail.example.net. ~
example.net. MG mg [at] example.net. ~
example.net. MINFO rm [at] example.net. re [at] example.net. ~
example.net. MR mr [at] example.net. ~</pre>
<p>More information about these records can be found in RFC1035. </p>
<p> <code>AFSDB, RP, X25, ISDN, and RT</code> </p>
<p> AFSDB, RP, X25, ISDN, and RT are resource records which were proposed in RFC1183. None of these resource records are widely used. </p>
<p> With the exception of the ISDN record, the format of these records is identical to the examples in RFC1183. The format of the ISDN record is identical unless the record has a subaddress (SA). If an ISDN record has a subaddress, it is separated from the ISDN-address by a aq;aq instead of whitespace. </p>
<p> If used, here is how the records would look in a csv2 zone file: </p>
<pre>example.net. AFSDB 1 afsdb.example.net. ~
example.net. RP rp [at] example.net. rp.example.net. ~
example.net. RP rp2 [at] example.net. . ~
example.net. X25 311061700956 ~
example.net. ISDN 150862028003217 ~
example.net. ISDN 150862028003217;004 ~
example.net. RT 10 relay.example.net. ~</pre>
<p><code>NSAP and NSAP-PTR</code> </p>
<p> NSAP and NSAP-PTR records were proposed in RFC1706. A NSAP record is a hexadecimal number preceeded by the string &quot;0x&quot; and with optional dots between bytes. This hexadecimal number is converted in to a binary number by MaraDNS. A NSAP-PTR record is idenical to a PTR record, but has a different RTYPE. </p>
<p> More information about these records can be obtained from RFC1706. </p>
<p> If used, here is how the records would look in a csv2 zone file: </p>
<pre>example.net. NSAP 0x47.0005.80.005a00.0000.0001.e133.ffffff000162.00 ~
example.net. NSAP-PTR nsap.example.net. ~</pre>
<p><code>PX</code> </p>
<p> The PX RR is an obscure RR described in RFC2163. A PX record looks like this in a CSV2 zone file: </p>
<pre>example.net. PX 15 px1.example.net. px2.example.net. ~</pre>
<p><code>GPOS</code> </p>
<p> An GPOS record is a description of the location of a given server. The format for this record is identical to a TXT record, except that the field must have precisely three chunks. </p>
<p> The first chunk of a GPOS record is the longitude; the second chunk is the latitude; the third chunk is the altitude (in meters). </p>
<p> Example: </p>
<pre>example.net. GPOS aq-98.6502aq;aq19.283aq;aq2134aq ~</pre>
<p>More information about this record can be found in RFC1712. </p>
<p> This resource record is not actively used; for the relatively few people who encode their position in DNS, the LOC record is far more common. </p>
<p> <code>LOC</code> </p>
<p> The LOC recource record is an uncommonly used resource record that describes the position of a given server. LOC records are described in RFC1876. </p>
<p> Note that MaraDNSaq LOC parser assumes that the altitude, size, horizontal, and vertical precision numbers are always expressed in meters. Also note that that sub-meter values for size, horizontal, and vertical precision are not allowed. Additionally, the altitude can not be greater than 21374836.47 meters. </p>
<p> Example: </p>
<pre>example.net. LOC 19 31 2.123 N 98 3 4 W 2000m 2m 4m 567m ~</pre>
<h2>Slash Commands</h2>
<p>In addition to being able to have resource records and comments, csv2 zone files can also have special slash commands. These slash commands, with the exception of the aq/serialaq slash command (see &quot;SOA&quot; above), can only be placed where the name for a record would be placed. Like resource records, a tilde is to be placed after the slash command. Note also that slash commands are case-sensitive, and the command in question must be in all-lower-case. </p>
<p> These commands are as follows: </p>
<p> <code>Default TTL</code> </p>
<p> The default TTL is the TTL for a resource record without a TTL specified. This can be changed with the aq/ttlaq slash command. This command takes only a single argument: The time, in seconds, for the new default TTL. The aq/ttlaq slash command only affects the TTL of records that follow the command. A zone file can have multiple aq/ttlaq slash commands. </p>
<p> The default TTL is 86400 seconds (one day) until changed by the aq/ttlaq slash command. </p>
<p> In the following example, a.ttl.example.com will have a TTL of 86400 seconds (as long as the zone file with this record has not previously used the aq/ttlaq slash command), b.ttl.example.com and d.ttl.example.com will have a TTL of 3600 seconds, c.ttl.example.com will have a TTL of 9600 seconds, and e.ttl.example.com will have a TTL of 7200 seconds: </p>
<pre>a.ttl.example.com. 10.0.0.1 ~
/ttl 3600 ~
b.ttl.example.com. 10.0.0.2 ~
c.ttl.example.com. +9600 10.0.0.3 ~
d.ttl.example.com. 10.0.0.4 ~
/ttl 7200 ~
e.ttl.example.com. 10.0.0.5 ~</pre>
<p><code>Origin</code> </p>
<p> It is possible to change the host name suffix that is used to substitute the percent in a csv2 zone file. This suffix is called, for historical and compatibility reasons, &quot;origin&quot;. This is done as the slash command aq/originaq, taking the new origin as the one argument to this function. Note that changing the origin does <i>not</i> change the domain suffix used to determine whether a given domain name is authoritative. </p>
<p> Here is one example usage of the aq/originaq slash command: </p>
<pre>/origin example.com. ~
www.% 10.1.0.1 ~
% MX 10 mail.% ~
mail.% 10.1.0.2 ~
/origin example.org. ~
www.% 10.2.0.1 ~
% MX 10 mail.% ~
mail.% 10.2.0.2 ~</pre>
<p>Which is equivalent to: </p>
<pre><a rel="nofollow" href="http://www.example.com">www.example.com</a>. 10.1.0.1 ~
example.com. MX 10 mail.example.com. ~
mail.example.com. 10.1.0.2 ~
<a rel="nofollow" href="http://www.example.org">www.example.org</a>. 10.2.0.1 ~
example.org. MX 10 mail.example.org. ~
mail.example.org. 10.2.0.2 ~</pre>
<p>It is also possible to make the current origin be part of the new origin: </p>
<pre>/origin example.com. ~
% 10.3.2.1 ~ # example.com now has IP 10.3.2.1
/origin mail.% ~
% 10.3.2.2 ~ # mail.example.com now has IP 10.3.2.2</pre>
<p><code>Opush and Opop</code> </p>
<p> The aq/opushaq and aq/opopaq slash commands use a stack to remember and later recall values for the origin (see origin above). The aq/opushaq command is used just like the aq/originaq command; however, the current origin is placed on a stack instead of discarded. The aq/opopaq command removes (&quot;pops&quot;) the top element from this stack and makes the element the origin. </p>
<p> For example: </p>
<pre>/origin example.com. ~
/opush mail.% ~ # origin is now mail.example.com; example.com is on stack
a.% 10.4.0.1 ~ # a.mail.example.com has IP 10.4.0.1
/opush web.example.com. ~ # mail.example.com and example.com are on stack
a.% 10.5.0.1 ~ # a.web.example.com has IP 10.5.0.1
b.% 10.5.0.2 ~ # b.web.example.com has IP 10.5.0.2
/opop ~ # origin is now mail.example.com again
b.% 10.4.0.2 ~ # b.mail.example.com has IP 10.4.0.2
/opop ~ # origin is now example.com
% MX 10 a.mail.% ~ # example.com. MX 10 a.mail.example.com.
% MX 20 b.mail.% ~ # example.com. MX 20 b.mail.example.com.</pre>
<p>The opush/opop stack can have up to seven elements on it. </p>
<p> <code>Read</code> </p>
<p> The aq/readaq slash commands allows one to have the contents of another file in a zone. The aq/readaq command takes a single argument: A filename that one wishes to read. The filename is only allowed to have letters, numbers, the aq-aq character, the aq_aq character, and the aq.aq character in it. </p>
<p> The file needs to be in the same directory as the zone file. The file will be read with the same privileges as the zone file; content in the file should come from a trusted source or be controlled by the system administrator. </p>
<p> Let us suppose that we have the following in a zone file: </p>
<pre>mail.foo.example.com. 10.3.2.1 ~
/read foo ~
foo.example.com. MX 10 mail.foo.example.com. ~</pre>
<p>And a file foo with the following contents: </p>
<pre>foo.example.com. 10.1.2.3 ~
foo.example.com. TXT aqFoomatic!aq ~</pre>
<p>Then foo.example.com will have an A record with the value 10.1.2.3, a TXT value of aqFoomatic!aq, and a MX record with priority 10 pointing to mail.foo.example.com. mail.foo.example.com will have the IP 10.3.2.1. </p>
<p> Note that no pre-processing nor post-processing of the origin is done by the aq/readaq command; should the file read change the origin, this changed value will affect any records after the aq/readaq command. For example, let us suppose db.example.com looks like this: </p>
<pre>/origin foo.example.com. ~
% TXT aqFoomatic!aq ~
/read foo ~
% MX 10 mail.foo.example.com. ~</pre>
<p>And the file foo looks like this: </p>
<pre>% 10.1.2.3 ~
/origin mail.% ~
% 10.3.2.1 ~</pre>
<p>Then the following records will be created: </p>
<pre>foo.example.com. TXT aqFoomatic!aq ~
foo.example.com. A 10.1.2.3 ~
mail.foo.example.com. A 10.3.2.1 ~
mail.foo.example.com. MX 10 mail.foo.example.com. ~</pre>
<p>To have something that works like aq$INCLUDE filenameaq in a RFC1035 master file, do the following: </p>
<pre>/opush % ~
/read filename ~
/opop ~</pre>
<p>Or, for that matter, the equivalent of aq$INCLUDE filename neworiginaq: </p>
<pre>/opush neworigin. ~
/read filename ~
/opop ~</pre>
<h2>Example Zone File</h2>
<pre># This is an example csv2 zone file
# First of all, csv2 zone files do not need an SOA record; however, if
# one is provided, we will make it the SOA record for our zone
# The SOA record needs to be the first record in the zone if provided
# This is a commented out record and disabled.
#% SOA % email@% 1 7200 3600 604800 1800 ~
# Second of all, csv2 zone files do not need authoritative NS records.
# If they arenaqt there, MaraDNS will synthesize them, based on the IP
# addresses MaraDNS is bound to. (Sheaqs pretty smart about this; if
# Mara is bound to both public and private IPs, only the public IPs will
# be synthesized as NS records)
#% NS a.% ~
#% NS b.% ~
# Here are some A (ipv4 address) records; since this is the most
# common field, the zone file format allows a compact representation
# of it.
a.example.net. 10.10.10.10 ~
# Here, you can see that a single name, &quot;b.example.net.&quot; has multiple IPs
# This can be used as a primitive form of load balancing; MaraDNS will
# rotate the IPs so that first IP seen by a DNS client changes every time
# a query for &quot;b.example.net.&quot; is made
b.example.net. 10.10.10.11 ~
b.example.net. 10.10.10.12 ~
# We can have the label in either case; it makes no difference
Z.EXAMPLE.NET. 10.2.3.4 ~
Y.EXAMPLE.net. 10.3.4.5 ~
# We can use the percent shortcut. When the percent shortcut is present,
# it indicates that the name in question should terminate with the name
# of the zone we are processing.
percent.% a 10.9.8.7 ~
# And we can have star records
#*.example.net. A 10.11.12.13 ~
# We can have a ttl in a record; however the ttl needs a aq+aq before it:
# Note that the ttl has to be in seconds, and is before the RTYPE
d.example.net. +86400 A 10.11.12.13 ~
f.example.net. # As you can see, records can span multiple lines
 A 10.2.19.83 ~
# This allows well-commented records, like this:
c.example.net. # Our C class machine
 +86400 # This record is stored for one day
 A # A record
 10.1.1.1 # Where we are 
 ~ # End of record
# We can even have something similiar to csv1 if we want...
e.example.net.|+86400|a|10.2.3.4|~
h.example.net.|a|10.9.8.7|~
# Here, we see we can specify the ttl but not the rtype if desired
g.example.net.|+86400|10.11.9.8|~
# Here is a MX record
% mx 10 mail.% ~
mail.% +86400 IN A 10.22.23.24 ~
# We even have a bit of ipv6 support
a.example.net. aaaa 3ffe:ffff:1:2:3::4:f ~
# Not to mention support for SRV records
_http._tcp.% srv 0 0 80 a.% ~
# TXT records, naturally
example.net. txt aqThis is some textaq ~
# Starting with MaraDNS 1.2.08, there is also support for SPF records,
# which are identical to TXT records. See RFC4408 for more details.
example.net. spf aqv=spf1 +mx a:colo.example.com/28 -allaq ~</pre>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Author</h2>
<p>Sam Trenholme <a rel="nofollow" href="http://www.samiam.org/">http://www.samiam.org/</a></p>
