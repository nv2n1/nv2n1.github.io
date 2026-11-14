---
title: "voms-proxy-info2(1)"
name: "voms-proxy-info2"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voms-proxy-info2/"
description: "voms-proxy-info – prints informations about a proxy with VOMS extensions"
---

<h2>NAME</h2>
<p> voms-proxy-info &#8211; prints informations about a proxy with VOMS extensions</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>voms-proxy-info</code> [options] </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The voms-proxy-info command pritns information about a proxy, including information about the VOMS extension. </p>
<h2>OPTIONS</h2>
<p> Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. The options from -help to -out are present for compatibility with grid-proxy-init, and have the exact same meaning. The meaning of the other ones is the following. </p>
<p> <code>-help</code> </p>
<p> <code>-usage</code> Displays usage. </p>
<p> <code>-version</code> Displays version. </p>
<p> <code>-debug</code> Enables extra debug output. This is for bug reports only. Users must not rely on the extra output printed by this option. </p>
<p> <code>-file</code> <i>proxyfile</i> The name of the file containing the proxy, in case it is in a non-standard place. </p>
<p> <code>-chain</code> Prints informations about the proxy&#8217;s certificate chain. </p>
<p> <code>-subject</code> Prints the DN of the proxy&#8217;s subject. </p>
<p> <code>-issuer</code> Prints the DN of the proxy&#8217;s issuer. </p>
<p> <code>-identity</code> Prints the DN of the iodentity represented by the proxy. This is synonimous </p>
<p> <code>-type</code> Print the proxy&#8217;s type (limited or not) </p>
<p> <code>-strength</code> Prints the proxy&#8217;s strength. I.e. the number of bits in the key. </p>
<p> <code>-valid</code> Print validity times. </p>
<p> <code>-timeleft</code> Prints how much time is left (in seconds) instead of the end time of the proxy. This option implies -valid </p>
<p> <code>-all</code> Prints everything. </p>
<p> <code>-fqan</code> Prints the VOMS attributes in the FQAN format. Default </p>
<p>&nbsp;<wbr><code>-exists</code>&nbsp;<wbr>&nbsp;<wbr><i>-bits N</i>&nbsp;<wbr>&nbsp;<wbr><i>-hours H</i>&nbsp;<wbr>Verifies if the proxy is valid for at least other H hours and has a key of at least N bits. </p>
<p>&nbsp;<wbr><code>-acexists</code>&nbsp;<wbr>&nbsp;<wbr><i>voname</i>&nbsp;<wbr>Verifies if an AC for the VO specified is present in the proxy. </p>
<p> <code>-conf</code> <i>file</i> Read options from file. </p>
<p> <code>-text</code> Prints the certificate to standard output. </p>
<p> <code>-path</code> Prints the full path name of the proxy file. </p>
<p> <code>-vo</code> Prints the names of the VOs whose AC are present in the proxy </p>
<p> <code>-acsubject</code> Prints the subject of the owners of the ACs in the proxy. </p>
<p> <code>-acissuer</code> Prints the issuer of the owners of the ACs in the proxy. </p>
<p> <code>-actimeleft</code> Prints how much time is left (in seconds) instead of the end time of the AC. </p>
<p> <code>-serial</code> Prints the serial number of each AC present in the proxy. </p>
<p> <code>-dont-verify-ac</code> Skips the AC verification step. Warning! Data printed when this option is specified may not be reliable. </p>
<p> <code>-targets</code> Prints the list of hosts to which the AC has been targeted. </p>
<p> <code>-included-file</code> In case the proxy included a user-specified file, this option prints it to screen. </p>
<p> <code>-uri</code> Prints the URI of the serve which issued this AC. </p>
<p> <code>-keyusage</code> Print the content of the KeyUsage extension of the certificate. </p>
<h2>BUGS</h2>
<p> EGEE Bug Tracking Tool: <i><a rel="nofollow" href="https://savannah.cern.ch/projects/jra1mdw/">https://savannah.cern.ch/projects/jra1mdw/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-voms-proxy-init/">voms-proxy-init</a>(1), <a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1) </p>
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
