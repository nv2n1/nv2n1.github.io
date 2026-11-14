---
title: "pkidaemon(1)"
name: "pkidaemon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkidaemon/"
description: "pkidaemon – provides status management of PKI instances"
---

<h2 class="name">NAME</h2>
<p> <code>pkidaemon</code> &#8211; provides status management of PKI instances</p>
<h2>SYNOPSIS</h2>
<pre><code>
pkidaemon{start | status}[instance - name]
</code></pre>
<dl>
<dt><code>Note:</code> Although this tool currently resides in the <code>/usr/bin</code> directory, proper use of it requires it to be run with super user privileges.</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>pkidaemon</code> command with the &#8216;status&#8217; argument provides a way to display the status of all existing PKI instances on a machine. Optionally, an individual PKI instance may be specified by using an optional <code>[instance-name]</code>. </p>
<p> The <code>pkidaemon</code> &#8216;start&#8217; argument is currently only used internally by the systemctl scripts. </p>
<h2>OPTIONS</h2>
<p> As stated above, the only optional argument to <code>pkidaemon</code> is <code>[instance-name]</code>. If a valid instance name is specified, only the status of that instance will be displayed. </p>
<h2>EXAMPLES</h2>
<p> For the following examples, two instances were installed. The first contained a CA, KRA, OCSP, TKS and TPS in a shared PKI instance named &#8216;pki-tomcat&#8217;, while the second simply contained a CA running on different ports and named &#8216;pki-tomcat-2&#8217;. </p>
<p> For the OCSP &#8216;Unsecure URL&#8217; and the OCSP &#8216;Secure EE URL&#8217; which both specify a static string of &#8216;&lt;ocsp request blob&gt;&#8217;, the intention is for the user to replace this static string with an actual OCSP request blob relevant to their particular deployment. </p>
<h3>Listing the status of all local PKI instances on this machine:</h3>
<p> <code># pkidaemon status</code> </p>
<p> REPORT STATUS OF &#8216;tomcat&#8217; INSTANCE(S): </p>
<p> Status for pki-tomcat: pki-tomcat is running .. </p>
<p>&nbsp;<wbr>[CA Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/ca/ee/ca">http://pki.example.com:8080/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/agent/ca">https://pki.example.com:8443/ca/agent/ca</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/ee/ca">https://pki.example.com:8443/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/services">https://pki.example.com:8443/ca/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca">https://pki.example.com:8443/ca</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[KRA Status Definitions]<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra/agent/kra">https://pki.example.com:8443/kra/agent/kra</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra/services">https://pki.example.com:8443/kra/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra">https://pki.example.com:8443/kra</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[OCSP Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/ocsp/ee/ocsp/">http://pki.example.com:8080/ocsp/ee/ocsp/</a>&lt;ocsp request blob&gt;<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/agent/ocsp">https://pki.example.com:8443/ocsp/agent/ocsp</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/ee/ocsp/">https://pki.example.com:8443/ocsp/ee/ocsp/</a>&lt;ocsp request blob&gt;<br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/services">https://pki.example.com:8443/ocsp/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp">https://pki.example.com:8443/ocsp</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[TKS Status Definitions]<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks/agent/tks">https://pki.example.com:8443/tks/agent/tks</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks/services">https://pki.example.com:8443/tks/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks">https://pki.example.com:8443/tks</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[TPS Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/tps">http://pki.example.com:8080/tps</a><br />
&nbsp;<wbr>Secure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tps">https://pki.example.com:8443/tps</a><br />
&nbsp;<wbr>Unsecure PHONE HOME&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/tps/phoneHome">http://pki.example.com:8080/tps/phoneHome</a><br />
&nbsp;<wbr>Secure PHONE HOME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tps/phoneHome">https://pki.example.com:8443/tps/phoneHome</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[CA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>Root CA&nbsp;<wbr>(Security Domain) </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[KRA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>KRA </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[OCSP Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>OCSP </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[TKS Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>TKS </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[TPS Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>TPS </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p> Status for pki-tomcat-2: pki-tomcat-2 is running .. </p>
<p>&nbsp;<wbr>[CA Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:18080/ca/ee/ca">http://pki.example.com:18080/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/agent/ca">https://pki.example.com:18443/ca/agent/ca</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/ee/ca">https://pki.example.com:18443/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/services">https://pki.example.com:18443/ca/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca">https://pki.example.com:18443/ca</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>18005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[CA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat-2 </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>Root CA&nbsp;<wbr>(Security Domain) </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p> FINISHED REPORTING STATUS OF &#8216;tomcat&#8217; INSTANCE(S). </p>
<h3>Listing the status of the PKI instance named &#8216;pki-tomcat&#8217;:</h3>
<p> <code># pkidaemon status pki-tomcat</code> </p>
<p> Status for pki-tomcat: pki-tomcat is running .. </p>
<p>&nbsp;<wbr>[CA Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/ca/ee/ca">http://pki.example.com:8080/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/agent/ca">https://pki.example.com:8443/ca/agent/ca</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/ee/ca">https://pki.example.com:8443/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca/services">https://pki.example.com:8443/ca/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ca">https://pki.example.com:8443/ca</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[KRA Status Definitions]<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra/agent/kra">https://pki.example.com:8443/kra/agent/kra</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra/services">https://pki.example.com:8443/kra/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/kra">https://pki.example.com:8443/kra</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[OCSP Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/ocsp/ee/ocsp/">http://pki.example.com:8080/ocsp/ee/ocsp/</a>&lt;ocsp request blob&gt;<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/agent/ocsp">https://pki.example.com:8443/ocsp/agent/ocsp</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/ee/ocsp/">https://pki.example.com:8443/ocsp/ee/ocsp/</a>&lt;ocsp request blob&gt;<br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp/services">https://pki.example.com:8443/ocsp/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/ocsp">https://pki.example.com:8443/ocsp</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[TKS Status Definitions]<br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks/agent/tks">https://pki.example.com:8443/tks/agent/tks</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks/services">https://pki.example.com:8443/tks/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tks">https://pki.example.com:8443/tks</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[TPS Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/tps">http://pki.example.com:8080/tps</a><br />
&nbsp;<wbr>Secure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tps">https://pki.example.com:8443/tps</a><br />
&nbsp;<wbr>Unsecure PHONE HOME&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:8080/tps/phoneHome">http://pki.example.com:8080/tps/phoneHome</a><br />
&nbsp;<wbr>Secure PHONE HOME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443/tps/phoneHome">https://pki.example.com:8443/tps/phoneHome</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>8005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[CA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>Root CA&nbsp;<wbr>(Security Domain) </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[KRA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>KRA </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[OCSP Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>OCSP </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[TKS Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>TKS </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<p>&nbsp;<wbr>[TPS Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>TPS </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:8443">https://pki.example.com:8443</a><br />
&nbsp;<wbr>==================================================================== </p>
<h3>Listing the status of the PKI instance named &#8216;pki-tomcat-2&#8217;:</h3>
<p> <code># pkidaemon status pki-tomcat-2</code> </p>
<p> Status for pki-tomcat-2: pki-tomcat-2 is running .. </p>
<p>&nbsp;<wbr>[CA Status Definitions]<br />
&nbsp;<wbr>Unsecure URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="http://pki.example.com:18080/ca/ee/ca">http://pki.example.com:18080/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Agent URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/agent/ca">https://pki.example.com:18443/ca/agent/ca</a><br />
&nbsp;<wbr>Secure EE URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/ee/ca">https://pki.example.com:18443/ca/ee/ca</a><br />
&nbsp;<wbr>Secure Admin URL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca/services">https://pki.example.com:18443/ca/services</a><br />
&nbsp;<wbr>PKI Console Command&nbsp;<wbr>=&nbsp;<wbr>pkiconsole&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443/ca">https://pki.example.com:18443/ca</a><br />
&nbsp;<wbr>Tomcat Port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>18005&nbsp;<wbr>(for shutdown) </p>
<p>&nbsp;<wbr>[CA Configuration Definitions]<br />
&nbsp;<wbr>PKI Instance Name:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pki-tomcat-2 </p>
<p>&nbsp;<wbr>PKI Subsystem Type:&nbsp;<wbr>&nbsp;<wbr>Root CA&nbsp;<wbr>(Security Domain) </p>
<p>&nbsp;<wbr>Registered PKI Security Domain Information:<br />
&nbsp;<wbr>====================================================================<br />
&nbsp;<wbr>Name:&nbsp;<wbr>&nbsp;<wbr>example.com Security Domain<br />
&nbsp;<wbr>URL:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://pki.example.com:18443">https://pki.example.com:18443</a><br />
&nbsp;<wbr>==================================================================== </p>
<h2>BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a> </p>
<h2>AUTHORS</h2>
<p> Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. <code>pkidaemon</code> was written by the Certificate Server project. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8),</code> <code><a href="/docs/linux/man/8-pkidestroy/">pkidestroy</a>(8),</code> <code><a href="/docs/linux/man/5-pki_default-cfg/">pki_default.cfg</a>(5),</code> <code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code> </p>
<h2>Index</h2>
