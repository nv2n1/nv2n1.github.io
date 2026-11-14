---
title: "askmara(1)"
name: "askmara"
section: "1"
letter: "a"
url: "/docs/linux/man/1-askmara/"
description: "askmara – do simple dns queries"
---

<h2 class="name">NAME</h2>
<p> askmara &#8211; do simple dns queries </p>
<h2>DESCRIPTION</h2>
<p> <code>askmara</code> queries the user-specified dns server for records, and outputs the reply in a csv2-compatible format (csv2 is the format of zone files that <code>maradns</code> uses).</p>
<h2>USAGE</h2>
<p> <code>askmara</code> [-n] [ -v | -t timeout] query [ server ]</p>
<h2>OPTIONS</h2>
<dl>
<dt>-t</p>
<dd> If this is present, the following argument is the askmara timeout, in seconds. Note that <code>askmara</code> can not both have a user-defined timeout and verbose output.</p>
<dt>-v</p>
<dd> If this is set, <code>askmara</code> will verbosely output the complete reply that the server sent. Note that this verbose output is not csv2-compatible.</p>
<dt>-n</p>
<dd> If this is set, <code>askmara</code>, when sending out a query, will not request DNS recursion; in other words, askmara will request that the remote DNS server not contact other DNS server to answer the query in question.</p>
<dt>query</p>
<dd> dns record to be queried. The query has two sections: The type of record we desire, and the hostname we want this record for.</dl>
<p> The type of query can have two forms: A one-letter mnemonic, or a numeric rtype followed by a colon. This is immediately concatenated by the full name of the host name we wish to look up. </p>
<p> For example, to ask for the IP of aqexample.com.aq, we can use the one-letter mnemonic, in the form aqAexample.com.aq, or we can use the numeric RR followed by a colon, giving the query aq1:example.com.aq (since A has the record type of one). Note that the query name needs the trailing dot at the end. </p>
<p> Askmara supports a handful one-letter mnemonics, as follows: </p>
<p> <code>A</code> signifies a request for an A (ipv4 address) RR </p>
<p> <code>N</code> signifies a NS RR </p>
<p> <code>C</code> signifies that we are asking for a CNAME RR </p>
<p> <code>S</code> signifies that we want a SOA RR </p>
<p> <code>P</code> signifies that we want a PTR RR </p>
<p> <code>@</code> signifies that we mant a MX RR </p>
<p> <code>T</code> signifies that we want a TXT RR </p>
<p> <code>Z</code> signifies that we want to ask for all RRs.</p>
<dl>
<dt>server</p>
<dd> IP address of the dns server to be queried. If no server is given, askmara will query 127.0.0.1.</dl>
<h2>EXAMPLES</h2>
<p> Asking the server with the ip 127.0.0.1 for the IP address of example.com: </p>
<pre>
askmara Aexample.com.
</pre>
<p> Asking the server with the ip 198.41.0.4 for the IP address of example.com: </p>
<pre>
askmara Aexample.com. 198.41.0.4
</pre>
<p> Asking the server with the ip address 127.0.0.1 for the IP address of example.com, using the rr_number:query format: </p>
<pre>
askmara 1:example.com. 
</pre>
<p> Asking the server with the ip address 127.0.0.1 for a SRV record. In particular, we ask for the &quot;http over tcp&quot; service for example.net. Since askmara doesnaqt have a mnemonic for SRV record types, we use the numeric code (33 for SRV): </p>
<pre>
askmara 33:_http._tcp.example.net.
</pre>
<p> Asking the server with the ip address 127.0.0.1 for the AAAA (ipv6 ip) record for example.net: </p>
<pre>
askmara 28:example.net. 
</pre>
<p> Note that the output will be a raw DNS packet in both the SRV and AAAA examples.</p>
<h2>BUGS</h2>
<p> When askmara is asked for an SOA record, the output of <code>askmara</code> closely resembles the format of a csv2 file, but can not be parsed as a csv2 file without modification. </p>
<p> askmara outputs multi-chunk (&quot;character-string&quot;) TXT records incorrectly (it only outputs the first chunk).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-maradns/">maradns</a>(8)</code> </p>
<p> <a rel="nofollow" href="http://www.maradns.org">http://www.maradns.org</a></p>
<h2>LEGAL DISCLAIMER</h2>
<p> THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>AUTHOR</h2>
<p> MaraDNS is written by Sam Trenholme. Jaakko Niemi used 5 minutes to roll this manpage together, which Sam has subsequently revised. </p>
<h2>Index</h2>
