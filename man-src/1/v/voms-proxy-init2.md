---
title: "voms-proxy-init2(1)"
name: "voms-proxy-init2"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voms-proxy-init2/"
description: "voms-proxy-init – create a proxy with VOMS extensions"
---

<h2>NAME</h2>
<p> voms-proxy-init &#8211; create a proxy with VOMS extensions</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>voms-proxy-init</code> [options] </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The voms-proxy-init generates a proxy with the VOMS information included in a non critical extension. </p>
<h2>OPTIONS</h2>
<p> Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. The options from -help to -out are present for compatibility with grid-proxy-init, and have the exact same meaning. The meaning of the other ones is the following. </p>
<p> <code>-help</code> </p>
<p> <code>-usage</code> Displays usage </p>
<p> <code>-version</code> </p>
<p> Displays version </p>
<p> <code>-debug</code> Enables extra debug output </p>
<p> <code>-quiet</code> </p>
<p> <code>-q</code> Quiet mode, minimal output </p>
<p> <code>-verify</code> Verifies proxy </p>
<p> <code>-pwstdin</code> Allows passphrase from stdin </p>
<p> <code>-limited</code> Creates a limited proxy </p>
<p> <code>-hours</code> <i>H</i> Proxy is valid for H hours (default:12) This option is deprecated and is only present for compatibility with grid-proxy-init, since this option does not set the validity of the credentials returned by VOMS. Use -valid instead. </p>
<p> <code>-vomslife</code> <i>H</i> Tries to get a pseudo cert with information valid for H hours. The default is &quot;as long as the proxy certificate&quot;. The special value 0 means as long as the server will allow. This option is deprecated, since it does not set the validity of the generated proxy. Use -valid instead. </p>
<p> <code>-valid</code> <i>HH:MM</i> This option attempts to set the validity for both the proxy and the credentials returned by the VOMS server. The latter validity may however be shortened due to server policy. This option obsoletes both -hours and -vomslife, and should be used in preference to both </p>
<p> <code>-bits</code> <i>B</i> Number of bits in key {0|512|1024|2048|4096}. 0 is a special value which means: same number of bits as in the issuing certificate. </p>
<p> <code>-cert</code> <i>certfile</i> Non-standard location of user certificate </p>
<p> <code>-key</code> <i>keyfile</i> Non-standard location of user key </p>
<p> <code>-certdir</code> <i>certdir</i> Non standard location where the trusted CAs certificates are kept. </p>
<p> <code>-out</code> <i>proxyfile</i> Location of new proxy cert </p>
<p> <code>-voms</code> <i>voms[:command]</i> Specifies the VOMS server to contact using the nickname voms. It also allows to send a specific command to the server. The default command is :all, and it gets all group membership information. Other commands are :/Role=rolename which grants the rolename VO-wide role if the server allows it, and :/group/Role=rolename which grants the role rolename only in the group /group, again only if the server allows it. </p>
<p> Example : voms-proxy-init &#8211;voms myVO:/myVO/Role=VO-Admin </p>
<p> <code>-order</code> <i>fqan</i> Specified fqans, if present, are put on top of the list of attributes returned by the server in the order in which they are passed (using more -order call). The order of the others is not specified. If some of the fqans are not returned no warning is given. Capability selection is not supported. </p>
<p> <code>-include</code> <i>file</i> Includes file in the certificate (in a non critical extension) </p>
<p> <code>-conf</code> <i>file</i> Read options from file. </p>
<p> <code>-confile</code> <i>file</i> </p>
<p> <code>-userconf</code> <i>file</i> </p>
<p> <code>-vomses</code> <i>file</i> Specifies the name of a configuration file from which a list of nicknames is read. The format of the file is the following: nick host port subject vo where nick is the nickname, host and port are the hostname and port of the server to contact, subject is the subject of the server&#8217;s certificate, while vo is the name of the VO that owns the server. The default filenames are $PREFIX/etc/vomses and $HOME/.voms/vomses. </p>
<p> Moreover, permissions must be 644 if a file is specified, and 755 if a directory is specified </p>
<p> The three options are synonyms. -confile and -userconf are deprecated. -vomses should be used instead. </p>
<p> <code>-policy</code> The file containing the policy expression. </p>
<p> <code>-policy-language</code><i> pl</i> </p>
<p> <code>-pl</code><i> pl</i> The language in which the policy is expressed. Default is IMPERSONATION_PROXY. </p>
<p> <code>-path-length</code> Maximum depth of proxy certfificate that can be signed from this. </p>
<p> <code>-globus</code> <i>version</i> Underlying Globus version. This will influence the default value of the <code>-proxyver</code>. </p>
<p> <code>-proxyver</code> Version of the proxy certificate to create. May be 2, 3 or 4. Default value is decided upon underlying globus version. </p>
<p> <code>-rfc</code> This option is a synonym of <code>-proxyver 4</code> and it generates a RFC-compliant proxy. </p>
<p> <code>-old</code> This option is a synonym of <code>-proxyver 2</code> and it generates a legacy proxy. </p>
<p> <code>-target</code> <i>hostname</i> This option targets the generated AC to a specific host. This option may be specified multiple times to allow for multiple hosts. </p>
<p> <code>-timeout</code> <i>seconds</i> This option allows to specify the maximum number of seconds that voms-proxy-init will wait while trying to establish a connection with the server. Its default value is -1 (unlimited). </p>
<p> <code>-noregen</code> Use existing proxy to contact the server and to sing the new proxy. </p>
<p> <code>-separate</code> <i>file</i> Saves the voms credential on file file. </p>
<p> <code>-ignorewarn</code> Ignore all warnings. They are not shown to the user. </p>
<p> <code>-failonwarn</code> Warnings become failures. The program will translates all warnings into errors and will react accordingly, by returning a failure itself. </p>
<p> <code>-list</code> Instead of producing an attribute certificate, this optin will print on screen a list of all attributes available to the user. </p>
<p> <code>-includeac</code> <i>file</i> Adds the VOMS AC in file to the proxy. </p>
<h2>BUGS</h2>
<p> EGEE Bug Tracking Tool: <i><a rel="nofollow" href="https://savannah.cern.ch/projects/jra1mdw/">https://savannah.cern.ch/projects/jra1mdw/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1) </p>
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
