---
title: "vomses(5)"
name: "vomses"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vomses/"
description: "vomses – The VOMS server contact table"
---

<p>vomses &#8211; The VOMS server contact table</p>
<h2>Synopsis</h2>
<p><code>/etc/vomses</code> </p>
<p> <code>~/.glite/vomses</code></p>
<h2>Description</h2>
<p>This manual page describes the format of <i>vomses</i> files. <i>vomses</i> files contain contact information for VOMS servers and are typically organized in the <code>/etc/vomses</code> directory. A <i>vomses</i> file is a simple text file which contains one or more lines formatted as follows: </p>
<p> &quot;alias&quot; &quot;hostname&quot; &quot;port&quot; &quot;server DN&quot; &quot;vo_name&quot; </p>
<p> Where: </p>
<p> <code>alias</code>: an alias that can be used for this VOMS server (this is typically identical to the vo_name) </p>
<p> <code>hostname</code>: the hostname where the VOMS server is running </p>
<p> <code>vo_name</code>: the name of the VO served by the VOMS server </p>
<p> <code>port</code>: the port where the VOMS server is listening for incoming requests </p>
<p> <code>server DN</code>: the certificate subject of the VOMS server </p>
<p> System wide VOMSES configuration is maintained in the <code>/etc/vomses</code> file or directory. If <code>/etc/vomses</code> is a directory, all the files contained in such directory are parsed looking for VOMS contact information. </p>
<p> A user can define its custom <code>vomses</code> configuration in the <code>~/.glite/vomses</code> file or directory, which will be parsed in the same way as just described.</p>
<h2>Examples</h2>
<p>The following is an example of valid vomes file for the <code>cms</code> VO: </p>
<pre><code>&quot;cms&quot; &quot;lcg-voms.cern.ch&quot; &quot;15002&quot; &quot;/DC=ch/DC=cern/OU=computers/CN=lcg-voms.cern.ch&quot; &quot;cms&quot;
&quot;cms&quot; &quot;voms.cern.ch&quot; &quot;15002&quot; &quot;/DC=ch/DC=cern/OU=computers/CN=voms.cern.ch&quot; &quot;cms&quot;</code></pre>
<h2>Bugs</h2>
<p>To report bugs or ask for support, use GGUS: <a rel="nofollow" href="https://ggus.eu/pages/home.php">https://ggus.eu/pages/home.php</a></p>
<h2>Authors</h2>
<p>Andrea Ceccanti &lt;andrea.ceccanti [at] cnaf.infn.it&gt; </p>
<p> Daniele Andreotti &lt;daniele.andreotti [at] cnaf.infn.it&gt; </p>
<p> Valerio Venturi &lt;valerio.venturi [at] cnaf.infn.it&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-voms-proxy-destroy/">voms-proxy-destroy</a>(1), <a href="/docs/linux/man/1-voms-proxy-info/">voms-proxy-info</a>(1), <a href="/docs/linux/man/5-vomsdir/">vomsdir</a>(5)</p>
<h2>Copying</h2>
<p>Copyright 2012 Istituto Nazionale di Fisica Nucleare </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at </p>
<dl>
<dd>
<pre><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></pre>
</dl>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
