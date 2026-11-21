---

title: "voms-proxy-info3(1)"
name: "voms-proxy-info3"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voms-proxy-info3/"
description: "voms-proxy-info – prints informations about a proxy with VOMS extensions"
---

<p> voms-proxy-info &#8211; prints informations about a proxy with VOMS extensions </p>
<h2>SYNOPSIS</h2>
<p> <code>voms-proxy-info</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> The voms-proxy-info command prints information about a proxy, including information about the VOMS extension. </p>
<p> The default location of the proxy is </p>
<dl>
<dt>
</dt><dd>
<pre>
 /tmp/x509up_u&lt;user_id&gt;
</pre>
</dd></dl>
<p> where user_id is the effective user id of the user running the command. A non-standard location for the proxy can be specified using the <code>-file</code> option.</p>
<h2>OPTIONS</h2>
<p> Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. </p>
<p> <code>&#8211;acexists &lt;voname&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Returns 0 if AC exists corresponding to voname, 1 otherwise
</pre>
</dd></dl>
<p> <code>&#8211;acissuer</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the DN of AC issuer (certificate signer)
</pre>
</dd></dl>
<p> <code>&#8211;acsubject</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the distinguished name (DN) of AC subject
</pre>
</dd></dl>
<p> <code>&#8211;actimeleft</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints time (in seconds) until AC expires
</pre>
</dd></dl>
<p> <code>&#8211;all</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
All proxy options in a human readable format
</pre>
</dd></dl>
<p> <code>-b,&#8211;bits &lt;B&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
[option to -exists] strength requirement for proxy to be valid
</pre>
</dd></dl>
<p> <code>&#8211;chain</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints information about the whole proxy certificate chain (CA excluded)
</pre>
</dd></dl>
<p> <code>&#8211;conf &lt;file&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Read options from &lt;file&gt;
</pre>
</dd></dl>
<p> <code>&#8211;debug</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Enables extra debug output
</pre>
</dd></dl>
<p> <code>-e,&#8211;exists</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Returns 0 if valid proxy exists, 1 otherwise
</pre>
</dd></dl>
<p> <code>&#8211;file &lt;proxyfile&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Reads information from file &lt;proxyfile&gt;
</pre>
</dd></dl>
<p> <code>&#8211;fqan</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints VOMS fully qualified attribute names (FQANs)
</pre>
</dd></dl>
<p> <code>&#8211;help</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Displays helps and exits
</pre>
</dd></dl>
<p> <code>&#8211;hours &lt;H&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
[option to -exists] time requirement for proxy to be valid (deprecated, use -valid instead)
</pre>
</dd></dl>
<p> <code>&#8211;identity</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the DN of the identity represented by the proxy
</pre>
</dd></dl>
<p> <code>&#8211;issuer</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the proxy issuer DN
</pre>
</dd></dl>
<p> <code>-k,&#8211;keyusage</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints content of the KeyUsage extension
</pre>
</dd></dl>
<p> <code>-p,&#8211;path</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the proxy file pathname
</pre>
</dd></dl>
<p> <code>&#8211;serial</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the AC serial number
</pre>
</dd></dl>
<p> <code>&#8211;strength</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the proxy key size (in bits)
</pre>
</dd></dl>
<p> <code>&#8211;subject</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the proxy subject Distinguished name (DN)
</pre>
</dd></dl>
<p> <code>&#8211;text</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints all information regarding the certificate
</pre>
</dd></dl>
<p> <code>&#8211;timeleft</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints time (in seconds) until proxy expires
</pre>
</dd></dl>
<p> <code>&#8211;type</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the proxy type (full or limited)
</pre>
</dd></dl>
<p> <code>&#8211;uri</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the URI of the VOMS server that issued the attributes
</pre>
</dd></dl>
<p> <code>&#8211;usage</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Displays helps and exits
</pre>
</dd></dl>
<p> <code>&#8211;valid &lt;H:M&gt;</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
[option to -exists] time requirement for proxy to be valid
</pre>
</dd></dl>
<p> <code>&#8211;version</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Displays version
</pre>
</dd></dl>
<p> <code>&#8211;vo</code> </p>
<dl>
<dt>
</dt><dd>
<pre>
Prints the vo name
</pre>
</dd></dl>
<h2>BUGS</h2>
<p> To report bugs or ask for support, use GGUS: <a rel="nofollow" href="https://ggus.eu/pages/home.php">https://ggus.eu/pages/home.php</a></p>
<h2>AUTHORS</h2>
<p> Andrea Ceccanti &lt;andrea.ceccanti [at] cnaf.infn.it&gt; </p>
<p> Daniele Andreotti &lt;daniele.andreotti [at] cnaf.infn.it&gt; </p>
<p> Valerio Venturi &lt;valerio.venturi [at] cnaf.infn.it&gt;</p>
<h2>SEE ALSO</h2>
<p> voms-proxy-destroy(1), voms-proxy-info(1), <a href="/docs/linux/man/5-vomses/">vomses</a>(5), <a href="/docs/linux/man/5-vomsdir/">vomsdir</a>(5)</p>
<h2>COPYING</h2>
<p> Copyright 2012 Istituto Nazionale di Fisica Nucleare </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at </p>
<dl>
<dt>
</dt><dd>
<pre>
<a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>
</pre>
</dd></dl>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. </p>
