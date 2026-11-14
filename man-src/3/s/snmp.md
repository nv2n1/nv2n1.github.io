---
title: "snmp(3)"
name: "snmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp/"
description: "SNMP – The Perl5 ‘SNMP’ Extension Module for the Net-SNMP SNMP package."
---

<p>SNMP &#8211; The Perl5 &#8216;SNMP&#8217; Extension Module for the Net-SNMP SNMP package. </p>
<h2>Synopsis</h2>
<pre> use SNMP;
 ...
 $sess = new SNMP::Session(DestHost =&gt; localhost, Community =&gt; public);
 $val = $sess-&gt;get('sysDescr.0');
 ...
 $vars = new SNMP::VarList([sysDescr,0], [sysContact,0], [sysLocation,0]);
 @vals = $sess-&gt;get($vars);
 ...
 $vb = new SNMP::Varbind();
 do {
 $val = $sess-&gt;getnext($vb);
 print &quot;@{$vb}
&quot;;
 } until ($sess-&gt;{ErrorNum});
 ...
 $SNMP::save_descriptions = 1;
 SNMP::initMib(); # assuming mib is not already loaded
 print &quot;$SNMP::MIB{sysDescr}{description}
&quot;;</pre>
<h2>Description</h2>
<p>Note: The perl <font SIZE="-1">SNMP 5.0</font> module which comes with net-snmp 5.0 and higher is different than previous versions in a number of ways. Most importantly, it behaves like a proper net-snmp application and calls init_snmp properly, which means it will read configuration files and use those defaults where appropriate automatically parse <font SIZE="-1">MIB</font> files, etc. This will likely affect your perl applications if you have, for instance, default values set up in your snmp.conf file (as the perl module will now make use of those defaults). The documentation, however, has sadly not been updated yet (aside from this note), nor is the read_config default usage implementation fully complete. </p>
<p> The basic operations of the <font SIZE="-1">SNMP</font> protocol are provided by this module through an object oriented interface for modularity and ease of use. The primary class is SNMP::Session which encapsulates the persistent aspects of a connection between the management application and the managed agent. Internally the class is implemented as a blessed hash reference. This class supplies &#8216;get&#8217;, &#8216;getnext&#8217;, &#8216;set&#8217;, &#8216;fget&#8217;, and &#8216;fgetnext&#8217; method calls. The methods take a variety of input argument formats and support both synchronous and asynchronous operation through a polymorphic <font SIZE="-1">API </font>(i.e., method behaviour varies dependent on args passed &#8211; see below).</p>
<h2>SNMP::Session</h2>
<p><tt>$sess</tt> = new SNMP::Session(DestHost =&gt; &#8216;host&#8217;, &#8230;) </p>
<p> The following arguments may be passed to new as a hash.</p>
<h3>Basic Options</h3>
<dl COMPACT>
<dt>DestHost</p>
<dd>Hostname or <font SIZE="-1">IP</font> address of the <font SIZE="-1">SNMP</font> agent you want to talk to. Specified in Net-SNMP formatted agent addresses. These addresses typically look like one of the following: </p>
<pre> localhost
 tcp:localhost
 tls:localhost
 tls:localhost:9876
 udp6:[::1]:9876
 unix:/some/path/to/file/socket</pre>
<p>Defaults to &#8216;localhost&#8217;.</p>
<dt>Version</p>
<dd><font SIZE="-1">SNMP</font> version to use. </p>
<p> The default is taken from library configuration &#8211; probably 3 [1, 2 (same as 2c), 2c, 3].</p>
<dt>Timeout</p>
<dd>The number of micro-seconds to wait before resending a request. </p>
<p> The default is &#8216;1000000&#8217;</p>
<dt>Retries</p>
<dd>The number of times to retry a request. </p>
<p> The default is &#8216;5&#8217;</p>
<dt>RetryNoSuch</p>
<dd>If enabled <font SIZE="-1">NOSUCH</font> errors in &#8216;get&#8217; pdus will be repaired, removing the varbind in error, and resent &#8211; undef will be returned for all <font SIZE="-1">NOSUCH</font> varbinds, when set to &#8216;0&#8217; this feature is disabled and the entire get request will fail on any <font SIZE="-1">NOSUCH</font> error (applies to v1 only) </p>
<p> The default is &#8216;0&#8217;.</dl>
<h3>SNMPv3/TLS Options</h3>
<dl COMPACT>
<dt>OurIdentity</p>
<dd>Our X.509 identity to use, which should either be a fingerprint or the filename that holds the certificate.</p>
<dt>TheirIdentity</p>
<dd>The remote server&#8217;s identity to connect to, specified as eihter a fingerprint or a file name. Either this must be specified, or the hostname below along with a trust anchor.</p>
<dt>TheirHostname</p>
<dd>The remote server&#8217;s hostname that is expected. If their certificate was signed by a <font SIZE="-1">CA</font> then their hostname presented in the certificate must match this value or the connection fails to be established (to avoid man-in-the-middle attacks).</p>
<dt>TrustCert</p>
<dd>A trusted certificate to use a trust anchor (like a <font SIZE="-1">CA</font> certificate) for verifying a remote server&#8217;s certificate. If a <font SIZE="-1">CA</font> certificate is used to validate a certificate then the TheirHostname parameter must also be specified to ensure their presente hostname in the certificate matches.</dl>
<h3>SNMPv3/USM Options</h3>
<dl COMPACT>
<dt>SecName</p>
<dd>The SNMPv3 security name to use (most for SNMPv3 with <font SIZE="-1">USM</font>). </p>
<p> The default is &#8216;initial&#8217;.</p>
<dt>SecLevel</p>
<dd>The SNMPv3 security level to use [noAuthNoPriv, authNoPriv, authPriv] (v3) </p>
<p> The default is &#8216;noAuthNoPriv&#8217;.</p>
<dt>SecEngineId</p>
<dd>The SNMPv3 security engineID to use (if the snmpv3 security model needs it; for example <font SIZE="-1">USM</font>). </p>
<p> The default is &lt;none&gt;, security engineID and it will be probed if not supplied (v3)</p>
<dt>ContextEngineId</p>
<dd>The SNMPv3 context engineID to use. </p>
<p> The default is the &lt;none&gt; and will be set either to the SecEngineId value if set or discovered or will be discovered in other ways if using <font SIZE="-1">TLS </font>(<font SIZE="-1">RFC5343</font> based discovery).</p>
<dt>Context</p>
<dd>The SNMPv3 context name to use. </p>
<p> The default is &#8221; (an empty string)</p>
<dt>AuthProto</p>
<dd>The SNMPv3/USM authentication protocol to use [<font SIZE="-1">MD5, SHA</font>]. </p>
<p> The default is &#8216;<font SIZE="-1">MD5</font>&#8216;.</p>
<dt>AuthPass</p>
<dd>The SNMPv3/USM authentication passphrase to use. </p>
<p> default &lt;none&gt;, authentication passphrase</p>
<dt>PrivProto</p>
<dd>The SNMPv3/USM privacy protocol to use [<font SIZE="-1">DES, AES</font>]. </p>
<p> The default is &#8216;<font SIZE="-1">DES</font>&#8216;.</p>
<dt>PrivPass</p>
<dd>The SNMPv3/USM privacy passphrase to use. </p>
<p> default &lt;none&gt;, privacy passphrase (v3)</p>
<dt>AuthMasterKey</p>
<dd>
<dt>PrivMasterKey</p>
<dd>
<dt>AuthLocalizedKey</p>
<dd>
<dt>PrivLocalizedKey</p>
<dd>Directly specified SNMPv3 <font SIZE="-1">USM</font> user keys (used if you want to specify the keys instead of deriving them from a password as above).</dl>
<h3>SNMPv1 and SNMPv2c Options</h3>
<dl COMPACT>
<dt>Community</p>
<dd>For SNMPv1 and SNMPv2c, the clear-text community name to use. </p>
<p> The default is &#8216;public&#8217;.</dl>
<h3>Other Configuration Options</h3>
<dl COMPACT>
<dt>VarFormats</p>
<dd>default &#8216;undef&#8217;, used by &#8216;fget[next]&#8217;, holds an hash reference of output value formatters, (e.g., {&lt;obj&gt; =&gt; &lt;sub-ref&gt;, &#8230; }, &lt;obj&gt; must match the &lt;obj&gt; and format used in the get operation. A special &lt;obj&gt;, &#8216;*&#8217;, may be used to apply all &lt;obj&gt;s, the supplied sub is called to translate the value to a new format. The sub is called passing the Varbind as the arg</p>
<dt>TypeFormats</p>
<dd>default &#8216;undef&#8217;, used by &#8216;fget[next]&#8217;, holds an hash reference of output value formatters, (e.g., {&lt;type&gt; =&gt; &lt;sub-ref&gt;, &#8230; }, the supplied sub is called to translate the value to a new format, unless a VarFormat mathces first (e.g., <tt>$sess</tt>-&gt;{TypeFormats}{<font SIZE="-1">INTEGER</font>} = \&amp;<i>mapEnum()</i>; although this can be done more efficiently by enabling <tt>$SNMP::use_enums</tt> or session creation param &#8216;UseEnums&#8217;)</p>
<dt>UseLongNames</p>
<dd>defaults to the value of SNMP::use_long_names at time of session creation. set to non-zero to have &lt;tags&gt; for &#8216;getnext&#8217; methods generated preferring longer Mib name convention (e.g., system.sysDescr vs just sysDescr)</p>
<dt>UseSprintValue</p>
<dd>defaults to the value of SNMP::use_sprint_value at time of session creation. set to non-zero to have return values for &#8216;get&#8217; and &#8216;getnext&#8217; methods formatted with the libraries snprint_value function. This will result in certain data types being returned in non-canonical format Note: values returned with this option set may not be appropriate for &#8216;set&#8217; operations (see discussion of value formats in &lt;vars&gt; description section)</p>
<dt>UseEnums</p>
<dd>defaults to the value of SNMP::use_enums at time of session creation. set to non-zero to have integer return values converted to enumeration identifiers if possible, these values will also be acceptable when supplied to &#8216;set&#8217; operations</p>
<dt>UseNumeric</p>
<dd>defaults to the value of SNMP::use_numeric at time of session creation. set to non-zero to have &lt;tags&gt; for get methods returned as numeric <font SIZE="-1">OID</font>&#8216;s rather than descriptions. UseLongNames will be set so that the full <font SIZE="-1">OID</font> is returned to the caller.</p>
<dt>BestGuess</p>
<dd>defaults to the value of SNMP::best_guess at time of session creation. this setting controls how &lt;tags&gt; are parsed. setting to 0 causes a regular lookup. setting to 1 causes a regular expression match (defined as -Ib in snmpcmd) and setting to 2 causes a random access lookup (defined as -IR in snmpcmd).</p>
<dt>NonIncreasing</p>
<dd>defaults to the value of SNMP::non_increasing at time of session creation. this setting controls if a non-increasing <font SIZE="-1">OID</font> during bulkwalk will causes an error. setting to 0 causes the default behaviour (which may, in very badly performing agents, result in a never-ending loop). setting to 1 causes an error (<font SIZE="-1">OID</font> not increasing) when this error occur.</p>
<dt>ErrorStr</p>
<dd>read-only, holds the error message assoc. w/ last request</p>
<dt>ErrorNum</p>
<dd>read-only, holds the snmp_err or staus of last request</p>
<dt>ErrorInd</p>
<dd>read-only, holds the snmp_err_index when appropriate</dl>
<p> Private variables:</p>
<dl COMPACT>
<dt>DestAddr</p>
<dd>internal field used to hold the translated DestHost field</p>
<dt>SessPtr</p>
<dd>internal field used to cache a created session structure</p>
<dt>RemotePort</p>
<dd>Obsolete. Please use the DestHost specifier to indicate the hostname and port combination instead of this paramet.</dl>
<h3>SNMP::Session methods</h3>
<dl COMPACT>
<dt>$sess-&gt;update(&lt;fields&gt;)</p>
<dd>Updates the SNMP::Session object with the values fields passed in as a hash list (similar to new(&lt;fields&gt;)) <code>(</code><font SIZE="-1"><code>WARNING</code></font><code>! not fully implemented)</code></p>
<dt>$sess-&gt;get(&lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>do <font SIZE="-1">SNMP GET,</font> multiple &lt;vars&gt; formats accepted. for syncronous operation &lt;vars&gt; will be updated with value(s) and type(s) and will also return retrieved value(s). If &lt;callback&gt; supplied method will operate asynchronously</p>
<dt>$sess-&gt;fget(&lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>do <font SIZE="-1">SNMP GET</font> like &#8216;get&#8217; and format the values according the handlers specified in <tt>$sess</tt>-&gt;{VarFormats} and <tt>$sess</tt>-&gt;{TypeFormats}</p>
<dt>$sess-&gt;getnext(&lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>do <font SIZE="-1">SNMP GETNEXT,</font> multiple &lt;vars&gt; formats accepted, returns retrieved value(s), &lt;vars&gt; passed as arguments are updated to indicate next lexicographical &lt;obj&gt;,&lt;iid&gt;,&lt;val&gt;, and &lt;type&gt; </p>
<p> Note: simple string &lt;vars&gt;,(e.g., &#8216;sysDescr.0&#8217;) form is not updated. If &lt;callback&gt; supplied method will operate asynchronously</p>
<dt>$sess-&gt;fgetnext(&lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>do <font SIZE="-1">SNMP GETNEXT</font> like getnext and format the values according the handlers specified in <tt>$sess</tt>-&gt;{VarFormats} and <tt>$sess</tt>-&gt;{TypeFormats}</p>
<dt>$sess-&gt;set(&lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>do <font SIZE="-1">SNMP SET,</font> multiple &lt;vars&gt; formats accepted. the value field in all &lt;vars&gt; formats must be in a canonical format (i.e., well known format) to ensure unambiguous translation to <font SIZE="-1">SNMP MIB</font> data value (see discussion of canonical value format &lt;vars&gt; description section), returns snmp_errno. If &lt;callback&gt; supplied method will operate asynchronously</p>
<dt>$sess-&gt;getbulk(&lt;non-repeaters&gt;, &lt;max-repeaters&gt;, &lt;vars&gt;)</p>
<dd>do an <font SIZE="-1">SNMP GETBULK,</font> from the list of Varbinds, the single next lexico instance is fetched for the first n Varbinds as defined by &lt;non-repeaters&gt;. For remaining Varbinds, the m lexico instances are retrieved each of the remaining Varbinds, where m is &lt;max-repeaters&gt;.</p>
<dt>$sess-&gt;bulkwalk(&lt;non-repeaters&gt;, &lt;max-repeaters&gt;, &lt;vars&gt; [,&lt;callback&gt;])</p>
<dd>Do a &#8220;bulkwalk&#8221; of the list of Varbinds. This is done by sending a <font SIZE="-1">GETBULK</font> request (see <i>getbulk()</i> above) for the Varbinds. For each requested variable, the response is examined to see if the next lexico instance has left the requested sub-tree. Any further instances returned for this variable are ignored, and the walk for that sub-tree is considered complete. </p>
<p> If any sub-trees were not completed when the end of the responses is reached, another request is composed, consisting of the remaining variables. This process is repeated until all sub-trees have been completed, or too many packets have been exchanged (to avoid loops). </p>
<p> The <i>bulkwalk()</i> method returns an array containing an array of Varbinds, one for each requested variable, in the order of the variable requests. Upon error, <i>bulkwalk()</i> returns undef and sets <tt>$sess</tt>-&gt;ErrorStr and <tt>$sess</tt>-&gt;ErrorNum. If a callback is supplied, <i>bulkwalk()</i> returns the <font SIZE="-1">SNMP</font> request id, and returns immediately. The callback will be called with the supplied argument list and the returned variables list. </p>
<p> Note: Because the client must &#8220;discover&#8221; that the tree is complete by comparing the returned variables with those that were requested, there is a potential &#8220;gotcha&#8221; when using the max-repeaters value. Consider the following code to print a list of interfaces and byte counts: </p>
<pre> $numInts = $sess-&gt;get('ifNumber.0');
 ($desc, $in, $out) = $sess-&gt;bulkwalk(0, $numInts,
 [['ifDescr'], ['ifInOctets'], ['ifOutOctets']]);
 for $i (0..($numInts - 1)) {
 printf &quot;Interface %4s: %s inOctets, %s outOctets
&quot;,
 $$desc[$i]-&gt;val, $$in[$i]-&gt;val, $$out[$i]-&gt;val;
 }</pre>
<p>This code will produce *two* requests to the agent &#8212; the first to get the interface values, and the second to discover that all the information was in the first packet. To get around this, use &#8216;$numInts + 1&#8217; for the max_repeaters value. This asks the agent to include one additional (unrelated) variable that signals the end of the sub-tree, allowing <i>bulkwalk()</i> to determine that the request is complete.</p>
<dt>$results = $sess-&gt;gettable(&lt;<font SIZE="-1">TABLE OID</font>&gt;, &lt;OPTIONgt)</p>
<dd>This will retrieve an entire table of data and return a hash reference to that data. The returned hash reference will have indexes of the <font SIZE="-1">OID</font> suffixes for the index data as the key. The value for each entry will be another hash containing the data for a given row. The keys to that hash will be the column names, and the values will be the data. </p>
<p> Example: </p>
<pre> #!/usr/bin/perl
 use SNMP;
 use Data::Dumper;
 my $s = new SNMP::Session(DestHost =&gt; 'localhost');
 print Dumper($s-&gt;gettable('ifTable'));</pre>
<p>On my machine produces: </p>
<pre> $VAR1 = {
 '6' =&gt; {
 'ifMtu' =&gt; '1500',
 'ifPhysAddress' =&gt; 'PV',
 # ...
 'ifInUnknownProtos' =&gt; '0'
 },
 '4' =&gt; {
 'ifMtu' =&gt; '1480',
 'ifPhysAddress' =&gt; '',
 # ...
 'ifInUnknownProtos' =&gt; '0'
 },
 # ...
 };</pre>
<p>By default, it will try to do as optimized retrieval as possible. It&#8217;ll request multiple columns at once, and use <font SIZE="-1">GETBULK</font> if possible. A few options may be specified by passing in an <i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i> hash containing various parameters:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>noindexes =&gt; 1</p>
<dd>Instructs the code not to parse the indexes and place the results in the second hash. If you don&#8217;t need the index data, this will be faster.</p>
<dt>columns =&gt; [ colname1, &#8230; ]</p>
<dd>This specifies which columns to collect. By default, it will try to collect all the columns defined in the <font SIZE="-1">MIB</font> table.</p>
<dt>repeat =&gt; <i></i><font SIZE="-1"><i>COUNT</i></font><i></i></p>
<dd>Specifies a <font SIZE="-1">GETBULK</font> repeat <i></i><font SIZE="-1"><i>COUNT</i></font><i></i>. <font SIZE="-1">IE,</font> it will request this many varbinds back per column when using the <font SIZE="-1">GETBULK</font> operation. Shortening this will mean smaller packets which may help going through some systems. By default, this value is calculated and attempts to guess at what will fit all the results into 1000 bytes. This calculation is fairly safe, hopefully, but you can either raise or lower the number using this option if desired. In lossy networks, you want to make sure that the packets don&#8217;t get fragmented and lowering this value is one way to help that.</p>
<dt>nogetbulk =&gt; 1</p>
<dd>Force the use of <font SIZE="-1">GETNEXT</font> rather than <font SIZE="-1">GETBULK. </font>(always true for SNMPv1, as it doesn&#8217;t have <font SIZE="-1">GETBULK</font> anyway). Some agents are great implementers of <font SIZE="-1">GETBULK</font> and this allows you to force the use of <font SIZE="-1">GETNEXT</font> operations instead.</p>
<dt>callback =&gt; \&amp;subroutine</p>
<dd>
<dt>callback =&gt; [\&amp;subroutine, optarg1, optarg2, &#8230;]</p>
<dd>If a callback is specified, gettable will return quickly without returning results. When the results are finally retrieved the callback subroutine will be called (see the other sections defining callback behaviour and how to make use of SNMP::MainLoop which is required fro this to work). An additional argument of the normal hash result will be added to the callback subroutine arguments. </p>
<p> Note 1: internally, the gettable function uses it&#8217;s own callbacks which are passed to getnext/getbulk as appropriate. </p>
<p> Note 2: callback support is only available in the <font SIZE="-1">SNMP</font> module version 5.04 and above. To test for this in code intending to support both versions prior to 5.04 and 5.04 and up, the following should work: </p>
<pre> if ($response = $sess-&gt;gettable('ifTable', callback =&gt; \&amp;my_sub)) {
 # got a response, gettable doesn't support callback
 my_sub($response);
 $no_mainloop = 1;
 }</pre>
<p>Deciding on whether to use SNMP::MainLoop is left as an exercise to the reader since it depends on whether your code uses other callbacks as well.</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h2>SNMP::TrapSession</h2>
<p><tt>$sess</tt> = new SNMP::Session(DestHost =&gt; &#8216;host&#8217;, &#8230;) </p>
<p> supports all applicable fields from SNMP::Session (see above)</p>
<h3>SNMP::TrapSession methods</h3>
<dl COMPACT>
<dt>$sess-&gt;trap(enterprise, agent, generic, specific, uptime, &lt;vars&gt;)</p>
<dd>
<pre> $sess-&gt;trap(enterprise=&gt;'.1.3.6.1.4.1.2021', # or 'ucdavis' [default]
 agent =&gt; '127.0.0.1', # or 'localhost',[dflt 1st intf on host]
 generic =&gt; specific, # can be omitted if 'specific' supplied
 specific =&gt; 5, # can be omitted if 'generic' supplied
 uptime =&gt; 1234, # dflt to localhost uptime (0 on win32)
 [[ifIndex, 1, 1],[sysLocation, 0, &quot;here&quot;]]); # optional vars
 # always last</pre>
<dt>trap(oid, uptime, &lt;vars&gt;) &#8211; v2 format</p>
<dd>
<pre> $sess-&gt;trap(oid =&gt; 'snmpRisingAlarm',
 uptime =&gt; 1234,
 [[ifIndex, 1, 1],[sysLocation, 0, &quot;here&quot;]]); # optional vars
 # always last</pre>
</dl>
<h2>Acceptable variable formats:</h2>
<p>&lt;vars&gt; may be one of the following forms:</p>
<dl COMPACT>
<dt>SNMP::VarList</p>
<dd>represents an array of <font SIZE="-1">MIB</font> objects to get or set, implemented as a blessed reference to an array of SNMP::Varbinds, (e.g., [&lt;varbind1&gt;, &lt;varbind2&gt;, &#8230;])</p>
<dt>SNMP::Varbind</p>
<dd>represents a single <font SIZE="-1">MIB</font> object to get or set, implemented as a blessed reference to a 4 element array; [&lt;obj&gt;, &lt;iid&gt;, &lt;val&gt;, &lt;type&gt;].</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&lt;obj&gt;</p>
<dd>one of the following forms:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1)</p>
<dd>leaf identifier (e.g., &#8216;sysDescr&#8217;) assumed to be unique for practical purposes</p>
<dt>2)</p>
<dd>fully qualified identifier (e.g., &#8216;.iso.org.dod.internet.mgmt.mib-2.system.sysDescr&#8217;)</p>
<dt>3)</p>
<dd>fully qualified, dotted-decimal, numeric <font SIZE="-1">OID </font>(e.g., &#8216;.1.3.6.1.2.1.1.1&#8217;)</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>&lt;iid&gt;</p>
<dd>the dotted-decimal, instance identifier. for scalar <font SIZE="-1">MIB</font> objects use &#8216;0&#8217;</p>
<dt>&lt;val&gt;</p>
<dd>the <font SIZE="-1">SNMP</font> data value retrieved from or being set to the agents <font SIZE="-1">MIB.</font> for (f)get(next) operations &lt;val&gt; may have a variety of formats as determined by session and package settings. However for set operations the &lt;val&gt; format must be canonical to ensure unambiguous translation. The canonical forms are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">OBJECTID</font></p>
<dd>dotted-decimal (e.g., .1.3.6.1.2.1.1.1)</p>
<dt><font SIZE="-1">OCTETSTR</font></p>
<dd>perl scalar containing octets</p>
<dt><font SIZE="-1">INTEGER</font></p>
<dd>decimal signed integer (or enum)</p>
<dt><font SIZE="-1">NETADDR</font></p>
<dd>dotted-decimal</p>
<dt><font SIZE="-1">IPADDR</font></p>
<dd>dotted-decimal</p>
<dt><font SIZE="-1">COUNTER</font></p>
<dd>decimal unsigned integer</p>
<dt><font SIZE="-1">COUNTER64</font></p>
<dd>decimal unsigned integer</p>
<dt><font SIZE="-1">GAUGE</font></p>
<dd>decimal unsigned integer</p>
<dt><font SIZE="-1">UINTEGER</font></p>
<dd>decimal unsigned integer</p>
<dt><font SIZE="-1">TICKS</font></p>
<dd>decimal unsigned integer</p>
<dt><font SIZE="-1">OPAQUE</font></p>
<dd>perl scalar containing octets</p>
<dt><font SIZE="-1">NULL</font></p>
<dd>perl scalar containing nothing</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>&lt;type&gt;</p>
<dd><font SIZE="-1">SNMP</font> data type (see list above), this field is populated by &#8216;get&#8217; and &#8216;getnext&#8217; operations. In some cases the programmer needs to populate this field when passing to a &#8216;set&#8217; operation. this field need not be supplied when the attribute indicated by &lt;tag&gt; is already described by loaded Mib modules. for &#8216;set&#8217;s, if a numeric <font SIZE="-1">OID</font> is used and the object is not currently in the loaded Mib, the &lt;type&gt; field must be supplied</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>simple string</p>
<dd>light weight form of &lt;var&gt; used to &#8216;set&#8217; or &#8216;get&#8217; a single attribute without constructing an SNMP::Varbind. stored in a perl scalar, has the form &#8216;&lt;tag&gt;.&lt;iid&gt;&#8217;, (e.g., &#8216;sysDescr.0&#8217;). for &#8216;set&#8217; operations the value is passed as a second arg. Note: This argument form is not updated in get[next] operations as are the other forms.</dl>
<h2>Acceptable callback formats</h2>
<p>&lt;callback&gt; may be one of the following forms:</p>
<dl COMPACT>
<dt>without arguments</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>\&amp;subname</p>
<dd>
<dt>sub { &#8230; }</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>or with arguments</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>[ \&amp;subname, $arg1, &#8230; ]</p>
<dd>
<dt>[ sub { &#8230; }, $arg1, &#8230; ]</p>
<dd>
<dt>[ &quot;method&quot;, $obj, $arg1, &#8230; ]</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<p> callback will be called when response is received or timeout occurs. the last argument passed to callback will be a SNMP::VarList reference. In case of timeout the last argument will be undef.</p>
<dl COMPACT>
<dt>&amp;SNMP::MainLoop([&lt;timeout&gt;, [&lt;callback&gt;]])</p>
<dd>to be used with async SNMP::Session calls. MainLoop must be called after initial async calls so return packets from the agent will not be processed. If no args supplied this function enters an infinite loop so program must be exited in a callback or externally interrupted. If &lt;timeout(sic)</p>
<dt>&amp;<i>SNMP::finish()</i></p>
<dd>This function, when called from an <i>SNMP::MainLoop()</i> callback function, will cause the current <i>SNMP::MainLoop()</i> to return after the callback is completed. <i>finish()</i> can be used to terminate an otherwise-infinite MainLoop. A new <i>MainLoop()</i> instance can then be started to handle further requests.</dl>
<h2>SNMP package variables and functions</h2>
<dl COMPACT>
<dt>$SNMP::VERSION</p>
<dd>the current version specifier (e.g., 3.1.0)</p>
<dt>$SNMP::auto_init_mib</p>
<dd>default &#8216;1&#8217;, set to 0 to disable automatic reading of the <font SIZE="-1">MIB</font> upon session creation. set to non-zero to call initMib at session creation which will result in <font SIZE="-1">MIB</font> loading according to Net-SNMP env. variables (see man mib_api)</p>
<dt>$SNMP::verbose</p>
<dd>default &#8216;0&#8217;, controls warning/info output of <font SIZE="-1">SNMP</font> module, 0 =&gt; no output, 1 =&gt; enables warning/info output from <font SIZE="-1">SNMP</font> module itself (is also controlled by SNMP::debugging &#8211; see below)</p>
<dt>$SNMP::use_long_names</p>
<dd>default &#8216;0&#8217;, set to non-zero to enable the use of longer Mib identifiers. see translateObj. will also influence the formatting of &lt;tag&gt; in varbinds returned from &#8216;getnext&#8217; operations. Can be set on a per session basis (UseLongNames)</p>
<dt>$SNMP::use_sprint_value</p>
<dd>default &#8216;0&#8217;, set to non-zero to enable formatting of response values using the snmp libraries snprint_value function. can also be set on a per session basis (see UseSprintValue) Note: returned values may not be suitable for &#8216;set&#8217; operations</p>
<dt>$SNMP::use_enums</p>
<dd>default &#8216;0&#8217;,set non-zero to return values as enums and allow sets using enums where appropriate. integer data will still be accepted for set operations. can also be set on a per session basis (see UseEnums)</p>
<dt>$SNMP::use_numeric</p>
<dd>default to &#8216;0&#8217;,set to non-zero to have &lt;tags&gt; for &#8216;get&#8217; methods returned as numeric <font SIZE="-1">OID</font>&#8216;s rather than descriptions. UseLongNames will be set so that the entire <font SIZE="-1">OID</font> will be returned. Set on a per-session basis (see UseNumeric).</p>
<dt>$SNMP::best_guess</p>
<dd>default &#8216;0&#8217;. This setting controls how &lt;tags&gt; are parsed. Setting to 0 causes a regular lookup. Setting to 1 causes a regular expression match (defined as -Ib in snmpcmd) and setting to 2 causes a random access lookup (defined as -IR in snmpcmd). Can also be set on a per session basis (see BestGuess)</p>
<dt>$SNMP::save_descriptions</p>
<dd>default &#8216;0&#8217;,set non-zero to have mib parser save attribute descriptions. must be set prior to mib initialization</p>
<dt>$SNMP::debugging</p>
<dd>default &#8216;0&#8217;, controls debugging output level within <font SIZE="-1">SNMP</font> module and libsnmp</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1.</p>
<dd>enables &#8216;SNMP::verbose&#8217; (see above)</p>
<dt>2.</p>
<dd>level 1 plus <i><a href="/docs/linux/man/1-snmp_set_do_debugging/">snmp_set_do_debugging</a></i>(1)</p>
<dt>3.</p>
<dd>level 2 plus <i><a href="/docs/linux/man/1-snmp_set_dump_packet/">snmp_set_dump_packet</a></i>(1)</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>$SNMP::dump_packet</p>
<dd>default &#8216;0&#8217;, set [non-]zero to independently set <i>snmp_set_dump_packet()</i></p>
<dt><i>SNMP::register_debug_tokens()</i></p>
<dd>Allows to register one or more debug tokens, just like the -D option of snmpd. Each debug token enables a group of debug statements. An example: SNMP::register_debug_tokens(&#8220;tdomain,netsnmp_unix&#8221;);</dl>
<h2>%Snmp::Mib</h2>
<p>a tied hash to access parsed <font SIZE="-1">MIB</font> information. After the <font SIZE="-1">MIB</font> has been loaded this hash allows access to to the parsed in <font SIZE="-1">MIB</font> meta-data(the structure of the <font SIZE="-1">MIB </font>(i.e., schema)). The hash returns blessed references to <font SIZE="-1">SNMP::MIB::NODE</font> objects which represent a single <font SIZE="-1">MIB</font> attribute. The nodes can be fetched with multiple &#8216;key&#8217; formats &#8211; the leaf name (e.g.,sysDescr) or fully/partially qualified name (e.g., system.sysDescr) or fully qualified numeric <font SIZE="-1">OID.</font> The returned node object supports the following fields:</p>
<dl COMPACT>
<dt>objectID</p>
<dd>dotted decimal fully qualified <font SIZE="-1">OID</font></p>
<dt>label</p>
<dd>leaf textual identifier (e.g., &#8216;sysDescr&#8217;)</p>
<dt>subID</p>
<dd>leaf numeric <font SIZE="-1">OID</font> component of objectID (e.g., &#8216;1&#8217;)</p>
<dt>moduleID</p>
<dd>textual identifier for module (e.g., &#8216;<font SIZE="-1">RFC1213-MIB</font>&#8216;)</p>
<dt>parent</p>
<dd>parent node</p>
<dt>children</p>
<dd>array reference of children nodes</p>
<dt>nextNode</p>
<dd>next lexico node <code>(</code><font SIZE="-1"><code>BUG</code></font><code>!does not return in lexico order)</code></p>
<dt>type</p>
<dd>returns application type (see getType for values)</p>
<dt>access</p>
<dd>returns <font SIZE="-1">ACCESS </font>(ReadOnly, ReadWrite, WriteOnly, NoAccess, Notify, Create)</p>
<dt>status</p>
<dd>returns <font SIZE="-1">STATUS </font>(Mandatory, Optional, Obsolete, Deprecated)</p>
<dt>syntax</p>
<dd>returns &#8216;textualConvention&#8217; if defined else &#8216;type&#8217;</p>
<dt>textualConvention</p>
<dd>returns TEXTUAL-CONVENTION</p>
<dt>TCDescription</p>
<dd>returns the TEXTUAL-CONVENTION&#8217;s <font SIZE="-1">DESCRIPTION</font> field.</p>
<dt>units</p>
<dd>returns <font SIZE="-1">UNITS</font></p>
<dt>hint</p>
<dd>returns <font SIZE="-1">HINT</font></p>
<dt>enums</p>
<dd>returns hash ref {tag =&gt; num, &#8230;}</p>
<dt>ranges</p>
<dd>returns array ref of hash ref [{low =&gt; num, high =&gt; num}, &#8230;]</p>
<dt>description</p>
<dd>returns <font SIZE="-1">DESCRIPTION </font>($SNMP::save_descriptions must be set prior to <font SIZE="-1">MIB</font> initialization/parsing)</p>
<dt>reference</p>
<dd>returns the <font SIZE="-1">REFERENCE</font> clause</p>
<dt>indexes</p>
<dd>returns the objects in the <font SIZE="-1">INDEX</font> clause</p>
<dt>implied</p>
<dd>returns true if the last object in the <font SIZE="-1">INDEX</font> is <font SIZE="-1">IMPLIED</font></dl>
<h2>MIB Functions</h2>
<dl COMPACT>
<dt>&amp;SNMP::setMib(&lt;file&gt;)</p>
<dd>allows dynamic parsing of the mib and explicit specification of mib file independent of environment variables. called with no args acts like initMib, loading MIBs indicated by environment variables (see Net-SNMP mib_api docs). passing non-zero second arg forces previous mib to be freed and replaced <code>(Note: second arg not working since freeing previous Mib is more involved than before)</code>.</p>
<dt>&amp;<i>SNMP::initMib()</i></p>
<dd>calls library init_mib function if Mib not already loaded &#8211; does nothing if Mib already loaded. will parse directories and load modules according to environment variables described in Net-SNMP documentations. (see man mib_api, <font SIZE="-1">MIBDIRS, MIBS, MIBFILE</font>(S), etc.)</p>
<dt>&amp;SNMP::addMibDirs(&lt;dir&gt;,&#8230;)</p>
<dd>calls library add_mibdir for each directory supplied. will cause directory(s) to be added to internal list and made available for searching in subsequent loadModules calls</p>
<dt>&amp;SNMP::addMibFiles(&lt;file&gt;,&#8230;)</p>
<dd>calls library read_mib function. The file(s) supplied will be read and all Mib module definitions contained therein will be added to internal mib tree structure</p>
<dt>&amp;SNMP::loadModules(&lt;mod&gt;,&#8230;)</p>
<dd>calls library read_module function. The module(s) supplied will be searched for in the current mibdirs and and added to internal mib tree structure. Passing special &lt;mod&gt;, &#8216;<font SIZE="-1">ALL</font>&#8216;, will cause all known modules to be loaded.</p>
<dt>&amp;SNMP::unloadModules(&lt;mod&gt;,&#8230;)</p>
<dd><code>*Not Implemented*</code></p>
<dt>&amp;SNMP::translateObj(&lt;var&gt;[,arg,[arg]])</p>
<dd>will convert a text obj tag to an <font SIZE="-1">OID</font> and vice-versa. Any iid suffix is retained numerically. Default behaviour when converting a numeric <font SIZE="-1">OID</font> to text form is to return leaf identifier only (e.g.,&#8217;sysDescr&#8217;) but when <tt>$SNMP::use_long_names</tt> is non-zero or a non-zero second arg is supplied it will return a longer textual identifier. An optional third argument of non-zero will cause the module name to be prepended to the text name (e.g. &#8216;SNMPv2-MIB::sysDescr&#8217;). When converting a text obj, the <tt>$SNMP::best_guess</tt> option is used. If no Mib is loaded when called and <tt>$SNMP::auto_init_mib</tt> is enabled then the Mib will be loaded. Will return &#8216;undef&#8217; upon failure.</p>
<dt>&amp;SNMP::getType(&lt;var&gt;)</p>
<dd>return <font SIZE="-1">SNMP</font> data type for given textual identifier <font SIZE="-1">OBJECTID, OCTETSTR, INTEGER, NETADDR, IPADDR, COUNTER GAUGE, TIMETICKS, OPAQUE,</font> or undef</p>
<dt>&amp;SNMP::mapEnum(&lt;var&gt;)</p>
<dd>converts integer value to enumertion tag defined in Mib or converts tag to integer depending on input. the function will return the corresponding integer value *or* tag for a given <font SIZE="-1">MIB</font> attribute and value. The function will sense which direction to perform the conversion. Various arg formats are supported</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>$val = SNMP::mapEnum($varbind);</p>
<dd>where <tt>$varbind</tt> is SNMP::Varbind or equiv. note: <tt>$varbind</tt> will be updated</p>
<dt>$val = SNMP::mapEnum(&#8216;ipForwarding&#8217;, &#8216;forwarding&#8217;);</p>
<dd>
<dt>$val = SNMP::mapEnum(&#8216;ipForwarding&#8217;, 1);</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h2>Exported SNMP utility functions</h2>
<p>Note: utility functions do not support async operation yet.</p>
<dl COMPACT>
<dt>&amp;<i>snmp_get()</i></p>
<dd>takes args of SNMP::Session::new followed by those of SNMP::Session::get</p>
<dt>&amp;<i>snmp_getnext()</i></p>
<dd>takes args of SNMP::Session::new followed by those of SNMP::Session::getnext</p>
<dt>&amp;<i>snmp_set()</i></p>
<dd>takes args of SNMP::Session::new followed by those of SNMP::Session::set</p>
<dt>&amp;<i>snmp_trap()</i></p>
<dd>takes args of SNMP::TrapSession::new followed by those of SNMP::TrapSession::trap</dl>
<h2>Trouble Shooting</h2>
<p>If problems occur there are number areas to look at to narrow down the possibilities. </p>
<p> The first step should be to test the Net-SNMP installation independently from the Perl5 <font SIZE="-1">SNMP</font> interface. </p>
<p> Try running the apps from the Net-SNMP distribution. </p>
<p> Make sure your agent (snmpd) is running and properly configured with read-write access for the community you are using. </p>
<p> Ensure that your MIBs are installed and enviroment variables are set appropriately (see man mib_api) </p>
<p> Be sure to remove old net-snmp installations and ensure headers and libraries from old <font SIZE="-1">CMU</font> installations are not being used by mistake. </p>
<p> If the problem occurs during compilation/linking check that the snmp library being linked is actually the Net-SNMP library (there have been name conflicts with existing snmp libs). </p>
<p> Also check that the header files are correct and up to date. </p>
<p> Sometimes compiling the Net-SNMP library with &#8216;position-independent-code&#8217; enabled is required (<font SIZE="-1">HPUX</font> specifically). </p>
<p> If you cannot resolve the problem you can post to comp.lang.perl.modules or net-snmp-users [at] net-snmp-users@lists.sourceforge.net </p>
<p> please give sufficient information to analyze the problem (<font SIZE="-1">OS</font> type, versions for OS/Perl/Net-SNMP/compiler, complete error output, etc.)</p>
<h2>Acknowledgements</h2>
<p>Many thanks to all those who supplied patches, suggestions and feedback. </p>
<pre> Joe Marzot (the original author)
 Wes Hardaker and the net-snmp-coders
 Dave Perkins
 Marcel Wiget
 David Blackburn
 John Stofell
 Gary Hayward
 Claire Harrison
 Achim Bohnet
 Doug Kingston
 Jacques Vidrine
 Carl Jacobsen
 Wayne Marquette
 Scott Schumate
 Michael Slifcak
 Srivathsan Srinivasagopalan
 Bill Fenner
 Jef Peeraer
 Daniel Hagerty
 Karl &quot;Rat&quot; Schilke and Electric Lightwave, Inc.
 Perl5 Porters
 Alex Burger</pre>
<p>Apologies to any/all who&#8217;s patch/feature/request was not mentioned or included &#8211; most likely it was lost when paying work intruded on my fun. Please try again if you do not see a desired feature. This may actually turn out to be a decent package with such excellent help and the fact that I have more time to work on it than in the past.</p>
<h2>Author</h2>
<p>bugs, comments, questions to net-snmp-users [at] lists.sourceforge.net</p>
<h2>Copyright</h2>
<pre> Copyright (c) 1995-2000 G. S. Marzot. All rights reserved.
 This program is free software; you can redistribute it and/or
 modify it under the same terms as Perl itself.
 Copyright (c) 2001-2002 Networks Associates Technology, Inc. All
 Rights Reserved. This program is free software; you can
 redistribute it and/or modify it under the same terms as Perl
 itself.</pre>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl COMPACT>
<dt>Around line 1722:</p>
<dd>&#8216;=item&#8217; outside of any &#8216;=over&#8217;</p>
<dt>Around line 1728:</p>
<dd>You forgot a &#8216;=back&#8217; before &#8216;=head2&#8217; </p>
</dl>
