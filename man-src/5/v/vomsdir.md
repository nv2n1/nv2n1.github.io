---
title: "vomsdir(5)"
name: "vomsdir"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vomsdir/"
description: "vomsdir – The structure of the vomsdir VOMS server trust anchor directory"
---

<p>vomsdir &#8211; The structure of the vomsdir VOMS server trust anchor directory</p>
<h2>Synopsis</h2>
<p><code>/etc/grid-security/vomsdir</code></p>
<h2>Description</h2>
<p>This manual page describes the structure of the <i>vomsdir</i> VOMS server trust anchor directory. The function of this directory is to keep local information about trusted VOMS servers which is used to verify the signatures on the attributes issued by VOMS servers. </p>
<p> The <i>vomsdir</i> directory is structured as follows: </p>
<dl>
<dd>
<pre>&lt;vomsdir&gt;
 |
 |--vo1
 |
 |--vo2
 |
 |--vo3
 |</pre>
</dl>
<p> A subdirectory is created for each of the trusted VOs. Inside each VO directory two types of files can be found: </p>
<dl>
<dd>&bull; </p>
<p> <code>LSC files</code> An LSC file contains a description of the certificate chain of the certificate used by a VOMS server to sign VOMS attributes.</dl>
<dl>
<dd>&bull; </p>
<p> <code>X509 certificates</code> The certificate used by a VOMS server to sign attributes.</dl>
<p> These files are commonly named using the following pattern: </p>
<dl>
<dd>
<pre>&lt;hostname&gt;.lsc
&lt;hostname&gt;.pem</pre>
</dl>
<p> Where hostname is the host where the VOMS server is running. </p>
<p> When both lsc and pem files are present for a given VO and hostname, the lsc file takes precedence.</p>
<h3>LSC file syntax</h3>
<p>The LSC file contains a list of X.509 subject strings, one on each line, encoded in OpenSSL slash-separated syntax, describing the certificate chain (up and including the CA that issued the certificate). For instance, the voms.cnaf.infn.it VOMS server has the following LSC file: </p>
<dl>
<dd>
<pre>/C=IT/O=INFN/OU=Host/L=CNAF/CN=voms.cnaf.infn.it
/C=IT/O=INFN/CN=INFN CA</pre>
</dl>
<h2>Examples</h2>
<p>Assuming locally two VOs are trusted, the <code>cms</code> VO and the <code>cdf</code> VO, the <code>/etc/grid-security/vomsdir</code> directory will be structured as follows: </p>
<dl>
<dd>
<pre>/etc/grid-security/vomsdir
/etc/grid-security/vomsdir/cms
/etc/grid-security/vomsdir/cdf</pre>
</dl>
<p> The <code>/etc/grid-security/vomsdir/cms</code> directory will contain the following files: </p>
<dl>
<dd>
<pre>lcg-voms.cern.ch.lsc
voms.cern.ch.lsc</pre>
</dl>
<p> The <code>/etc/grid-security/vomsdir/cdf</code> directory will contain the following files: </p>
<dl>
<dd>
<pre>voms-01.pd.infn.it.lsc
voms.cnaf.infn.it.lsc
voms.fnal.gov.lsc</pre>
</dl>
<p> The LSC files will contain descriptions of the certificate chains used by VOMS servers to sign attribute certificates.</p>
<h2>Bugs</h2>
<p>To report bugs or ask for support, use GGUS: <a rel="nofollow" href="https://ggus.eu/pages/home.php">https://ggus.eu/pages/home.php</a></p>
<h2>Authors</h2>
<p>Andrea Ceccanti &lt;andrea.ceccanti [at] cnaf.infn.it&gt; </p>
<p> Daniele Andreotti &lt;daniele.andreotti [at] cnaf.infn.it&gt; </p>
<p> Valerio Venturi &lt;valerio.venturi [at] cnaf.infn.it&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1), <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/5-voms-lsc/">voms-lsc</a>(5)</p>
<h2>Copying</h2>
<p>Copyright 2012 Istituto Nazionale di Fisica Nucleare </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at </p>
<dl>
<dd>
<pre><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></pre>
</dl>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
