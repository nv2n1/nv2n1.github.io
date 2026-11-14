---
title: "yadifa-rc(5)"
name: "yadifa-rc"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yadifa-rc/"
description: "yadifa.rc is the configuration file for yadifa(8)."
---

<p>yadifa.rc is the configuration file for <i><a href="/docs/linux/man/8-yadifa/">yadifa</a></i>(8). </p>
<h2>Synopsis</h2>
<p>${HOME}/.yadifa.rc </p>
<h2>Description</h2>
<p>The configuration of yadifa has several containers:</p>
<dl>
<dt><code>&lt;yadifa&gt;</code></p>
<dd>&nbsp;<wbr>General container&nbsp;<wbr></p>
<dt><code>&lt;key&gt;</code></p>
<dd>&nbsp;<wbr>TSIG keys&nbsp;<wbr></dl>
<p> The configuration supports included files.<br />
 example: include /home/yadifa/yadifa-keys.conf The configuration files can be nested. The configuration consists of:</p>
<dl>
<dt><code>*</code></p>
<dd>Container, which starts with &lt;container name&gt; and ends with &lt;/container name&gt;</p>
<dt><code>*</code></p>
<dd>Variable name</p>
<dt><code>*</code></p>
<dd>1 or 2 arguments</p>
<dt><code>*</code></p>
<dd>Arguments can contain 1 or more comma separated values.</dl>
<p> eg. </p>
<pre>&lt;container&gt;
 # variable argument
 variable value1 
 # variable argument1 argument2
 variable value1 value2
 # variable argument1
 variable value1,value2
&lt;/container&gt;</pre>
<h2>Examples</h2>
<p>Examples of containers defined for a configuration file.</p>
<dl>
<dt><code>*</code></p>
<dd>YADIFA, General</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Config with Key</p>
<dl>
<dd>
<pre># start .yadifa.rc
&lt;yadifa&gt;
 server &quot;192.0.2.1 port 53&quot;
 tsig-key-name Admin-key
&lt;/yadifa&gt;
# end .yadifa.rc</pre>
<dl>
<dt><code>*</code></p>
<dd>KEY, TSIG-key configuration
</dl>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Admin-key key definition (the name is arbitrary) </p>
<pre>&lt;key&gt;
 name Admin-key
 algorithm hmac-md5
 secret WorthlessKeyForExample==
&lt;/key&gt;</pre>
</dl>
</dl>
<dl>
<dd>
<h2>Files</h2>
<dl>
<dt>yadifa</p>
<dd>&nbsp;<wbr>The name server remote client.&nbsp;<wbr></p>
<dt>$HOME/.yadifa.rc</p>
<dd>&nbsp;<wbr>default rcfile.&nbsp;<wbr></dl>
<dl>
<dt>yadifa.rc.5</p>
<dd>&nbsp;<wbr>This man page.&nbsp;<wbr></p>
<dt>yadifa.8</p>
<dd>&nbsp;<wbr>Man page for yadifa.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-yadifa/">yadifa</a></i>(8) </p>
<h2>Notes</h2>
<p>Since unquoted leading whitespace is generally ignored in the .yadifa.rc you can indent everything to taste. </p>
<h2>Changes</h2>
<p>Please check the file README from the sources.</p>
<h2>Version</h2>
<p>Version: 2.2.3 of 2016-12-15.</p>
<h2>Mailing Lists</h2>
<p>There exists a mailinglist for questions relating to any program in the yadifa package: </p>
<dl>
<dt><code>*</code></p>
<dd><code>yadifa-users [at] mailinglists.yadifa.eu</code><br />
 for submitting questions/answers.</dl>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-users">http://www.yadifa.eu/mailing-list-users</a></code><br />
 for subscription requests.</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to via:</p>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-announcements">http://www.yadifa.eu/mailing-list-announcements</a></code></dl>
<p> (this is a readonly list).</p>
<h2>License And Copyright</h2>
<dl>
<dt>Copyright</p>
<dd>(C)2011-2016, EURid<br />
 B-1831 Diegem, Belgium<br />
 <code>info [at] yadifa.eu</code></dl>
<h2>Authors</h2>
<p>Gery Van Emelen<br />
 Email: <code>Gery.VanEmelen [at] EURid.eu</code><br />
 Eric Diaz Fernandez<br />
 Email: <code>Eric.DiazFernandez [at] EURid.eu</code> </p>
<p> WWW: <code><a rel="nofollow" href="http://www.EURid.eu">http://www.EURid.eu</a></code></p>
