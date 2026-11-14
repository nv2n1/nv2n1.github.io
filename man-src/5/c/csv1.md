---
title: "csv1(5)"
name: "csv1"
section: "5"
letter: "c"
url: "/docs/linux/man/5-csv1/"
description: "csv1 – Format of the csv1 zone file that MaraDNS uses"
---

<p>csv1 &#8211; Format of the csv1 zone file that MaraDNS uses</p>
<h2>Special Note</h2>
<p>The csv1 zone file format is supported primarily for MaraDNS users who already have zone files in the csv1 format. MaraDNS now supports a csv2 zone file format. Note that the csv1 zone file format will continue to function as long as I am MaraDNSaq maintainer.</p>
<h2>Special Characters</h2>
<dl>
<dt>|</p>
<dd>This delimits fields</p>
<dt>#</p>
<dd>This signifies a comment. Lines starting with this are ignored, otherwise it has no significance</p>
<dt>%</p>
<dd>This, in domain names, signifies that the rest of the domain name should be the name of this zone</p>
<dt>*</p>
<dd>This is translated to mean &quot;any host name that otherwise does not resolve&quot;. It must be at the beginning of a domain name.</p>
<dt>\</p>
<dd>This is used an an escape character, either to escape octal values such as aq%aq for %, or to escape the aq%aq character so it has no special meaning, or to escape the backslash character.</dl>
<h2>Notes On Processing</h2>
<p>All domain-name labels are converted to their lower-case equivalents before processing is done. This is because domain-name literals in the database with one or more upper-case letters in them are case-sensitive. This is my way to resolve RFC1035 schizophrenic desire to both allow binary domain labels, and its desire to be case-insensitive. </p>
<p> The file must first have a SOA record, followed by one or more NS records, followed by other records. The initial NS and SOA records must be RR for this zone. NS records after any non-NS record must be part of another zone. The resolution algorithm will not break if non-CNAME records share records with a CNAME record, but this is not a good idea to do.</p>
<h2>Rr Format</h2>
<p>A domain name is a one-letter designation of its type, followed by the domain name separated by dots, ending with either a % or a trailing dot. If the domain name does not end with a % or trailing dot, an error is returned.</p>
<h2>Supported Rr Types</h2>
<p>MaraDNS only supports the following types of resource records (RRs) in csv1 files. More resource records types are supported in csv2 zone files; see <code><a href="/docs/linux/man/5-csv2/">csv2</a>(5)</code> for details. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Letter<tt>&nbsp;<wbr></tt>Type<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>RFC1035 section 3.2.2 value</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>N<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>C<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>CNAME<tt>&nbsp;<wbr>&nbsp;<wbr></tt>5</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>S<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SOA<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>6</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PTR<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>12</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>@<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>15</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>T<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>TXT<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>16</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>any<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>determined in third field of line</p>
<h2>Format Of Supported Rr Types</h2>
<p>Here are the formats, shown by letter name: </p>
<pre>A: Has three fields
field one: the domain name
field two: the ttl for the name in seconds
field three: the ip address, in dotted decimal notation
Example:
Ahost.example.com.|7200|10.1.2.3</pre>
<p>A records are described with grueling detail in RFC1035. In short, an A record is an IP address for a given host name. </p>
<pre>N: Has three fields
field one: the domain name of the record
field two: the ttl for the name in seconds
field three: the domain name this NS points to. 
Example:
Nexample.com.|86400|ns.example.com.</pre>
<p>NS (N here) records are described in RFC1035 </p>
<pre>C: Has three fields
field one: the domain name of the record
field two: the ttl for the name in seconds
field three: the domain this CNAME record points to
Example:
Calias.example.org.|3200|realname.example.org.</pre>
<p>CNAME (which C is short for) records are described in RFC1035 </p>
<pre>S: Has nine fields
field one: the domain name of the record
field two: the TTL of the record
field three: the origin of the domain. In other words, the name of the
 primary name server for the domain.
field four: the email address for this domain (in the RFC822, not 
 BIND format)
field five: the serial for the domain
field six: the refresh (how often to see updates) for the domain
field seven: the retry (how often to try when down) for the domain
field eight: the expire (how long before the slave gives up) for the 
 domain
field nine: the minimum (and default) TTL for the domain
Example:
Sexample.net.|86400|%|hostmaster@%|19771108|7200|3600|604800|1800</pre>
<p>SOA (S here) records are described in RFC1035 </p>
<pre>P: has three fields
field one: the IP we wish to point to (in in-addr.arpa form)
field two: the ttl for the name in seconds
field three: the FQDN for the IP in question 
Example:
P3.2.1.10.in-addr.arpa.|86400|ns.example.com.</pre>
<p>PTR (P here) records, which are used for reverse DNS lookups, are described in RFC1035. Note that one needs control of the appropriate in-addr.arpa subdomain to make PTR records visible on the internet at large. </p>
<pre>@: has four fields
field one: The host that people send email to
field two: the ttl for this record
field three: The preference for this MX host
field four: The name of this MX host
Example:
@example.com.|86400|10|mail.example.com.</pre>
<p>MX (@ here) records are described in RFC1035 </p>
<pre>T: has three fields
field one: The host someone wants to get additional information about
field two: the ttl for this record
field three: The desired text. Any data becomes the record up until a 
 new line is reached. The new line is not part of the TXT 
 record
Example:
Texample.com.|86400|Example.com: Buy example products online</pre>
<p>TXT (T here) records are described in RFC1035 </p>
<pre>U: has four fields
field one: The host someone wants a data type normally unsupported by 
 MaraDNS for
field two: the ttl for this record
field three: The numeric code for this data type (33 for SRV, etc.)
field four: The raw binary data for this data type
Example:
Uexample.com.|3600|40|Kitchen sink data</pre>
<p>The above example is a &quot;Kitchen Sink&quot; RR (see draft-ietf-dnsind-kitchen-sink-02.txt) with a &quot;meaning&quot; of 8, a &quot;coding&quot; of 1, a &quot;subcoding&quot; of 2, and a data string of &quot;Kitchen sink data&quot;. Since this particular data type is not formallized in a RFC at this time, the most appropriate method of storing this data is by using the catch-all &quot;unsupported&quot; syntax.</p>
<h2>Example Csv1 Zone File</h2>
<pre># Example CSV1 zone file
# This is what is known as a SOA record. All zone files need to have one
# of these
S%|86400|%|hostmaster@%|19771108|7200|3600|604800|1800
# These are known as authoritative NS records. All zone files need
# one or more of these
N%|86400|ns1.%
N%|86400|ns2.%
# Some IP addresses
Ans1.%|86400|10.0.0.1
Ans2.%|86400|192.168.0.1
A%|86400|10.1.2.3
Amx.%|86400|10.1.2.4
# An aqIN MXaq record
@%|86400|10|mx.%</pre>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Author</h2>
<p>Sam Trenholme <a rel="nofollow" href="http://www.samiam.org/">http://www.samiam.org/</a></p>
