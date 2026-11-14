---
title: "system(1)"
name: "system"
section: "1"
letter: "s"
url: "/docs/linux/man/1-system/"
description: "system.rootdaemonrc, .rootdaemonrc – access control directives for ROOT daemons"
---

<h2 class="name">NAME</h2>
<p> system.rootdaemonrc, .rootdaemonrc &#8211; access control directives for ROOT daemons </p>
<h2>LOCATIONS</h2>
<pre>
<code>ROOTDAEMORC, $HOME/.rootdaemonrc</code>
<code>/etc/root/system.rootdaemonrc, $ROOTSYS/etc/system.rootdaemonrc</code>
</pre>
<h2>DESCRIPTION</h2>
<p> This manual page documents the format of directives specifying access control directives for ROOT daemons. These directives are read from a text file whose full path is taken from the environment variable <code>ROOTDAEMONRC</code>. If such a variable in undefined, the daemon looks for a file named <code>.rootdaemonrc</code> in the $HOME directory of the user starting the daemon; if this file does not exists either, the file <code>system.rootdaemonrc</code>, located under <code>/etc/root</code> or <code>$ROOTSYS/etc</code>, is used. If none of these file exists (or is readable), the daemon makes use of a default built-in directive derived from the configuration options of the installation. </p>
<h2>FORMAT</h2>
<dl>
<dt><code>* </code></p>
<dd> lines starting with &#8216;#&#8217; are comment lines.</p>
<dt><code>* </code></p>
<dd> hosts can specified either with their name (e.g. pcepsft43), their FQDN (e.g. pcepsft43.cern.ch) or their IP address (e.g. 137.138.99.73).</p>
<dt><code>* </code></p>
<dd> host names can be followed by :rootd, :proofd or :sockd to define directives applying only to the given service; &#8216;sockd&#8217; applies to servers run from interactive sessions (TServerSocket class)</p>
<dt><code>* </code></p>
<dd> directives applying to all host can be specified either by &#8216;default&#8217; or &#8216;*&#8217;</p>
<dt><code>* </code></p>
<dd> the &#8216;*&#8217; character can be used in any field of the name to indicate a set of machines or domains, e.g. pcepsft*.cern.ch applies to all &#8216;pcepsft&#8217; machines in the domain &#8216;cern.ch&#8217;. (to indicate all &#8216;lxplus&#8217; machines you should use &#8216;lxplus*.cern.ch&#8217; because internally the generic lxplus machine has a real name of the form lxplusnnn.cern.ch; you can also use &#8216;lxplus&#8217; if you don&#8217;t care about domain name checking).</p>
<dt><code>* </code></p>
<dd> a whole domain can be indicated by its name, e.g. &#8216;cern.ch&#8217;, &#8216;cnaf.infn.it&#8217; or &#8216;.ch&#8217;</p>
<dt><code>* </code></p>
<dd> truncated IP address can also be used to indicate a set of machines; they are interpreted as the very first or very last part of the address; for example, to select 137.138.99.73, any of these is valid: &#8216;137.138.99&#8217;, &#8216;137.138&#8217;, &#8216;137`, &#8216;99.73&#8217;; or with wild cards: &#8216;137.13*&#8217; or &#8216;*.99.73`; however, &#8216;138.99&#8217; is invalid because ambiguous.</p>
<dt><code>* </code></p>
<dd> the information following the name or IP address indicates, in order of preference, the short names or the internal codes of authentication methods accepted for requests coming from the specified host(s); the ones implemented so far are: </p>
<p>Method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nickname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>code </p>
<p>UsrPwd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>usrpwd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0<br />
SRP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>srp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1<br />
Kerberos&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>krb5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2<br />
Globus&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>globus&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3<br />
SSH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ssh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4<br />
UidGid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uidgid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(insecure) </p>
<p> (The insecure method is intended to speed up access within a cluster protected by other means from outside attacks; should not be used for inter-cluster or inter-domain authentication). Methods non specified explicitly are not accepted. For the insecure method it is possible to give access only to a specific list of users by specifying the usernames after the method separated by colons (:) example: </p>
<p>uidgid:user1:user2:user3 </p>
<p> will allow uidgid access only to users user1, user2 and user3. This is useful to give easy access to data servers. It is also possible to deny access to a user by using a &#8216;-&#8216; in front of the name: </p>
<p>uidgid:-user4</p>
<dt><code>* </code></p>
<dd> Lines ending with &#8221; are followed by additional information for the host on the next line; the name of the host should not be repeated. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Valid examples: </p>
<dl>
<dt><code>default none</code></p>
<dd> All requests are denied unless specified by dedicated directives. </p>
<dt><code>default 0 ssh</code></p>
<dd> Authentication mechanisms allowed by default are &#8216;usrpwd&#8217; (code 0) and &#8216;ssh&#8217; </p>
<dt><code>137.138. 0 4</code></p>
<dd> Authentication mechanisms allowed from host in the domain 137.138. (cern.ch) are &#8216;usrpwd&#8217; (code 0) and &#8216;ssh&#8217; </p>
<dt><code>pceple19.cern.ch 4 1 3 2 5 0</code></p>
<dd> All mechanisms are accepted for requests coming from host pceple19.cern.ch . </p>
<dt><code>lxplus*.cern.ch 4 1 globus 0:qwerty:uytre</code></p>
<dd> Requests from the lxplus cluster can authenticate using &#8216;ssh&#8217;, &#8216;srp&#8217; and &#8216;globus&#8217;; users &#8216;qwerty&#8217; and &#8216;uytre&#8217; can also use &#8216;usrpwd&#8217; . </p>
<dt><code>pcep*.cern.ch:rootd 0:-qwerty 4</code></p>
<dd> Requests from the pcep*.cern.ch nodes can authenticate using &#8216;usrpwd&#8217; and &#8216;ssh&#8217; when accessing the &#8216;rootd&#8217; daemon ; user &#8216;qwerty&#8217; can only use &#8216;ssh&#8217;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rootd/">rootd</a></i>(1), <i><a href="/docs/linux/man/1-proofd/">proofd</a></i>(1) </p>
<p> For more information on the <code>ROOT</code> system, please refer to <i><a rel="nofollow" href="http://root.cern.ch/">http://root.cern.ch/</a></i> . </p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun </code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by G. Ganis &lt;g.ganis [at] cern.ch&gt; . </p>
<h2>Index</h2>
