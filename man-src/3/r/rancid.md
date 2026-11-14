---
title: "rancid(3)"
name: "rancid"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rancid/"
description: "rancid – rancid perl module"
---

<p>rancid &#8211; rancid perl module</p>
<h2>Introduction</h2>
<p>The <code>rancid</code> library provides functions for handling rancid.types configuration files, loading modules, and the basic global variables, variables from parsing rancid.types files, and output handling functions that are common to all rancid device modules, all of which are &quot;exported&quot; (in perl terms) for use by those that import the module. Specifically, the library is used by <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), but it could be used by any perl program for site-specific handling or additional automata. </p>
<dl>
<dt><code>RunCommand(*INPUT, *OUTPUT, command)</code></p>
<dd>Parse a single command that returns no required info; the output is dropped. This could be used as the processing function in a command definition in a rancid.types file.</dl>
<p> Output handling functions: </p>
<dl>
<dt><code>ProcessHistory([tag], [sort_function], [sort_function_argument], string)</code></p>
<dd>If the optional tag string and sort_function arguments are omitted, the string is output immediately. Otherwise, the strings are accumulated in a hash, by the hash key sort_function_argument, each time <code>ProcessHistory()</code> is called until the tag or sort_function changes, at which time the queue is flushed and the new string is handled. If sort_function had been supplied, it is called with the hash as its argument. </p>
<p> Note that if the hash key sort_function_argument exists, the new strings is appended to the existing hash value.</p>
<dt><code>keysort(%hash)</code></p>
<dd>A sort routine that will sort on the keys of a hash as if it were a normal array. For example: </p>
<pre>ProcessHistory(&quot;TAG&quot;,&quot;keysort&quot;,&quot;B0&quot;,&quot;!
&quot;);
ProcessHistory(&quot;TAG&quot;,&quot;keysort&quot;,&quot;D0&quot;,&quot;!
&quot;);</pre>
<p>B0 and D0 are the sort keys.</p>
<dt><code>valsort(%hash)</code></p>
<dd>A sort routine that will sort on the values of a hash as if it were a normal array. </p>
<pre>ProcessHistory(&quot;TAG&quot;,&quot;valsort&quot;,&quot;&quot;,&quot;!B0
&quot;);
ProcessHistory(&quot;TAG&quot;,&quot;valsort&quot;,&quot;&quot;,&quot;!D0
&quot;);</pre>
<dt><code>numsort(%hash)</code></p>
<dd>A numerical sort routine (ascending).</p>
<dt><code>ipsort(IPv4/v6 dotted-quad)</code></p>
<dd>A sort routine that will sort on the ip address when the IP address is anywhere in the strings. </p>
<pre>ProcessHistory(&quot;TAG&quot;,&quot;ipsort&quot;,&quot;192.168.0.0&quot;,&quot;!B0
&quot;);
ProcessHistory(&quot;TAG&quot;,&quot;ipsort&quot;,&quot;192.168.1.0&quot;,&quot;!D0
&quot;);</pre>
<dt><code>sortbyipaddr(XXX)</code></p>
<dd>A sort routine that will sort based upon IPv4/v6 addresses.</dl>
<p> Please see the library code for exported variables.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), <code><a href="/docs/linux/man/5-rancid-types-conf/">rancid.types.conf</a></code>(5) </p>
