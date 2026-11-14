---
title: "voms-proxy-list(1)"
name: "voms-proxy-list"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voms-proxy-list/"
description: "voms-proxy-list – Shows a list of all availabel attributes from a specified server"
---

<h2>NAME</h2>
<p> voms-proxy-list &#8211; Shows a list of all availabel attributes from a specified server</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>voms-proxy-list</code> [options] </p>
</dl>
<h2>DESCRIPTION</h2>
<dd>The voms-proxy-list prints on screen a list of all available attributes from a specified proxy server. </p>
<h2>OPTIONS</h2>
<p> Options may be specified indifferently with either a &quot;-&quot; or &quot;&#8211;&quot; prefix. The options from -help to -out are present for compatibility with grid-proxy-init, and have the exact same meaning. The meaning of the other ones is the following. </p>
<p> <code>-help</code> Displays usage </p>
<p> <code>-version</code> Displays version </p>
<p> <code>-debug</code> Enables extra debug output </p>
<p> <code>-q</code> Quiet mode, minimal output </p>
<p> <code>-verify</code> Verifies certificate to make proxy for </p>
<p> <code>-pwstdin</code> Allows passphrase from stdin </p>
<p> <code>-cert</code> <i>certfile</i> Non-standard location of user certificate </p>
<p> <code>-key</code> <i>keyfile</i> Non-standard location of user key </p>
<p> <code>-certdir</code> <i>certdir</i> Non standard location where the trusted CAs certificates are kept. </p>
<p> <code>-out</code> <i>proxyfile</i> Location of new proxy cert </p>
<p> <code>-voms</code> <i>voms</i> Specifies the VOMS server to contact using the nickname voms. </p>
<p> Example : voms-proxy-list &#8211;voms myVO </p>
<p> <code>-conf</code> <i>file</i> Read options from file. </p>
<p> <code>-confile</code> <i>file</i> </p>
<p> <code>-userconf</code> <i>file</i> </p>
<p> <code>-vomses</code> <i>file</i> Specifies the name of a configuration file from which a list of nicknames is read. The format of the file is the following: nick host port subject vo Where nick is the nickname, host and port are the hostname and port of the server to contact, subject is the subject of the server&#8217;s certificate, while vo is the name of the VO that owns the server. The default filenames are $PREFIX/etc/vomses and $HOME/.glite/vomses. </p>
<p> Moreover, permissions must be 644 if a file is specified, and 755 if a directory is specified </p>
<p> The three options are synonyms. -confile and -userconf are deprecated. -vomses should be used instead. </p>
<p> <code>-globus</code> <i>version</i> Underlying Globus version. </p>
<p> <code>-noregen</code> Use existing proxy to contact the server and to sing the new proxy. </p>
<p> <code>-ignorewarn</code> Ignore all warnings. They are not shown to the user. </p>
<p> <code>-failonwarn</code> Warnings become failures. The program will translates all warnings into errors and will react accordingly, by returning a failure itself. </p>
<p> <code>-list</code> Instead of producing an attribute certificate, this optin will print on screen a list of all attributes available to the user. This is a no-op </p>
<h2>BUGS</h2>
<p> EGEE Bug Tracking Tool: <i><a rel="nofollow" href="https://savannah.cern.ch/projects/jra1mdw/">https://savannah.cern.ch/projects/jra1mdw/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-voms-proxy-list/">voms-proxy-list</a>(1), <a href="/docs/linux/man/1-voms-proxy-init/">voms-proxy-init</a>(1), <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1) </p>
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
