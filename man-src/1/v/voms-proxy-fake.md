---
title: "voms-proxy-fake(1)"
name: "voms-proxy-fake"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voms-proxy-fake/"
description: "voms-proxy-fake – create a proxy with VOMS extensions"
---

<h2>NAME</h2>
<p> voms-proxy-fake &#8211; create a proxy with VOMS extensions</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>voms-proxy-fake</code> [options] </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The voms-proxy-fake generates a proxy containing arbitrary attributes without contacting the VOMS server. </p>
<h2>OPTIONS</h2>
<p> Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. </p>
<p> <code>-help</code> Displays usage. </p>
<p> <code>-version</code> Displays version. </p>
<p> <code>-debug</code> Enables extra debug output. </p>
<p> <code>-q</code> Quiet mode, minimal output. </p>
<p> <code>-verify</code> Verifies certificate to make proxy for. </p>
<p> <code>-pwstdin</code> Allows passphrase from stdin. </p>
<p> <code>-limited</code> Creates a limited proxy. </p>
<p> <code>-hours</code> <i>H</i> Proxy is valid for H hours (default:12). </p>
<p> <code>-vomslife</code> <i>H</i> Tries to get an AC with information valid for H hours. The default is &quot;as long as the proxy certificate&quot;. The special value 0 means as long as the server will allow. </p>
<p> <code>-bits</code> <i>B</i> Number of bits in key {0|512|1024|2048|4096}. 0 is a special value which means: same number of bits as in the issuing certificate. </p>
<p> <code>-cert</code> <i>certfile</i> Non-standard location of user certificate </p>
<p> <code>-key</code> <i>keyfile</i> Non-standard location of user key </p>
<p> <code>-certdir</code> <i>certdir</i> Location of trusted certificates dir </p>
<p> <code>-out</code> <i>proxyfile</i> Location of new proxy cert </p>
<p> <code>-voms</code> <i>voms[:command]</i> Specifies the fake VOMS server that will appear in the attribute certificate. command is ignored and is present for compatibility with voms-proxy-init. </p>
<p> <code>-include</code> <i>file</i> Includes file in the certificate (in a non critical extension) </p>
<p> <code>-conf</code> <i>file</i> Read options from file. </p>
<p> <code>-policy</code> The file containing the policy expression. </p>
<p> <code>-policy-language</code><i> pl</i> The language in which the policy is expressed. Default is IMPERSONATION_PROXY. </p>
<p> <code>-path-length</code> Maximum depth of proxy certfificate that can be signed from this. </p>
<p> <code>-globus</code> <i>version</i> Underlying Globus version. </p>
<p> <code>-proxyver</code> Version of the proxy certificate to create. May be 2 or 3. Default value is decided upon underlying globus version. </p>
<p> <code>-separate</code> <i>file</i> Saves the voms credential on file file. </p>
<p> <code>-hostcert</code> <i>file</i> The cert that will be used to sign the AC. </p>
<p> <code>-hostkey</code> <i>file</i> The key thet will be used to sign the AC. </p>
<p> <code>-fqan</code> <i>file</i> The string that will be included in the AC as the granted FQAN. </p>
<p> <code>-newformat</code> </p>
<p> This forces the server to generate ACs in the new (correct) format. This is meant as a compatibility feature to ease migration while the servers upgrade to the new version. </p>
<p> <code>-newsubject</code> <i>newdn</i> </p>
<p> The created proxy will have newdn as subject rather than what is would normally have depending on the specific version of proxy created. Non-printable characters may be specified via the &#8216;\XX&#8217; encoding, where XX are two hexadecimal characters. </p>
<p> <code>-newissuer</code> <i>newdn</i> </p>
<p> The created proxy will have newdn as issuer rather than what is would normally have depending on the specific version of proxy created. Non-printable characters may be specified via the &#8216;\XX&#8217; encoding, where XX are two hexadecimal characters. </p>
<p> <code>-newserial</code> <i>newserial</i> </p>
<p> The created proxy will have the newserial as its serial number. The new serial number will have to be specified as an hex representation. Any length is possible. If this option is not specified, voms-proxy-fake will choose the serial number. </p>
<p> <code>-pastac</code> <i>timespec</i> </p>
<p> The created AC will have its validity start in the past, as specified by timespec. </p>
<p> The format of timespec is one of: seconds, hours:minutes, hours:minutes:seconds </p>
<p> <code>-pastproxy</code> <i>timespec</i> </p>
<p> The created proxy will have its validity start in the past as specified by timespec </p>
<p> The format of timespec is one of: seconds, hours:minutes, hours:minutes:seconds </p>
<p> <code>-nscert</code> <i>bit,&#8230;,bit</i> </p>
<p> The created proxy will have the specified bits in the Netscape Certificate Extension. Acceptable values for bit are: client, server, email, objsign, sslCA, emailCA, objCA. The default value is not to have this extension. </p>
<p> <code>-extkeyusage</code> <i>bit,&#8230;,bit</i> </p>
<p> The created proxy will have the specified bits in the Extended Key Usage Extension. Acceptable values for bit are: serverAuth, clientAuth, codeSigning, emailProtection, timeStamping, msCodeInd, msCodeCom, msCTLSign, msSGC, msEFS, nsSGC, deltaCRL. The default value is not to have this extensions. </p>
<p> <code>-keyusage</code> <i>bit,&#8230;,bit</i> </p>
<p> The created proxy will have the specified bits in the Key Usage Extensions. Acceptable values for bit are: digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign, cRLSign, encipherOnly, decipherOnly. The default value is to copy this extensions from the issuer certificate while removing the keyCertSign and nonRepudiation bits if present. </p>
<p> <code>-selfsigned</code> </p>
<p> The created certificate will be a self-signed certificate and have a CA=true bit in the Basic constraints Exception. </p>
<p> <code>-extension</code> <i>oid[/criticality]value</i> </p>
<p> This option allows to specified additional extensions to be put in the created certificate. </p>
<p> oid is the Object Identifier of the extensions. Any OID may be used even if it is not already known in advance. This must always be specified. There is no default. </p>
<p> criticality specifies whether the extensions is critical or not, and it must be either true or false. If absent, it defaults to false. </p>
<p> value is the value of the extensions. It is composed by two subfields, type and content. type is a single charater, and specifies how the content is interpreted. &#8216;:&#8217; means that content is a text string to be included as is. &#8216;~&#8217; means that content is an hex representation of the string. &#8216;+&#8217; means that content is the name of a file which will contain the actual data. </p>
<p> <code>-acextension</code> <i>oid[/criticality]value</i> </p>
<p> This option allows to specified additional extensions to be put in the created attribute certificate. </p>
<p> oid is the Object Identifier of the extensions. Any OID may be used even if it is not already known in advance. This must always be specified. There is no default. </p>
<p> criticality specifies whether the extensions is critical or not, and it must be either true or false. If absent, it defaults to false. </p>
<p> value is the value of the extensions. It is composed by two subfields, type and content. type is a single charater, and specifies how the content is interpreted. &#8216;:&#8217; means that content is a text string to be included as is. &#8216;~&#8217; means that content is an hex representation of the string. &#8216;+&#8217; means that content is the name of a file which will contain the actual data. </p>
<p> <code>-ga</code> <i>id</i> = <i>value</i> <i>[(qualifier)]</i> </p>
<p> This option adds the generic attribute specified to the AC generated. Please note that spaces before and after the &#8216;=&#8217; char are swallowed in the command line. </p>
<p> <code>-voinfo</code> <i>file</i> </p>
<p> The file file contains informations for additional ACs that should be included in the created proxy. ACs specified via the -voinfo option shall be added before ACs specified via the command line options. </p>
<p> The format of the file is the following: </p>
<p> [voname] </p>
<p> parameter=value </p>
<p> parameter=value </p>
<p> &#8230; </p>
<h2>BUGS</h2>
<p> EGEE Bug Tracking Tool: <i><a rel="nofollow" href="https://savannah.cern.ch/projects/jra1mdw/">https://savannah.cern.ch/projects/jra1mdw/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-voms-proxy-fake/">voms-proxy-fake</a>(1), <a href="/docs/linux/man/1-voms-proxy-init/">voms-proxy-init</a>(1), <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1) </p>
<p> EDT Auth Home page: <i><a rel="nofollow" href="http://grid-auth.infn.it">http://grid-auth.infn.it</a></i> </p>
<p> CVSweb: <i><a rel="nofollow" href="http://datagrid.in2p3.fr/cgi-bin/cvsweb.cgi/Auth/voms">http://datagrid.in2p3.fr/cgi-bin/cvsweb.cgi/Auth/voms</a></i> </p>
<p> RPM repository: <i><a rel="nofollow" href="http://datagrid.in2p3.fr/distribution/autobuild/i386-rh7.3">http://datagrid.in2p3.fr/distribution/autobuild/i386-rh7.3</a></i> </p>
<h2>AUTHORS</h2>
<p> Vincenzo Ciaschini &lt;Vincenzo.Ciaschini [at] cnaf.infn.it&gt;. </p>
<p> Valerio Venturi &lt;Valerio.Venturi [at] cnaf.infn.it&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) Members of the EGEE Collaboration. 2004. See the beneficiaries list for details on the copyright holders. </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at </p>
<p> <a rel="nofollow" href="http://www.apache.org">www.apache.org</a>/licenses/LICENSE-2.0: <i><a href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></i> </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. </p>
<h2>Index</h2>
