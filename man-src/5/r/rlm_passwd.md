---
title: "rlm_passwd(5)"
name: "rlm_passwd"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_passwd/"
description: "rlm_passwd – FreeRADIUS Module"
---

<p>rlm_passwd &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_passwd</i> module provides authorization via files similar in format to /etc/passwd. The lm_passwd module allows you to retrieve any account information from any files with passwd-like format (/etc/passwd, /etc/group, smbpasswd, .htpasswd, etc). Every field of the file may be mapped to a RADIUS attribute, with one of the fields used as a key. The module reads the file when it initializes, and caches the data in memory. As a result, it does not support dynamic updates of the files (the server has to be HUP&#8217;d), but it is very fast, even for files with thousands of lines. The configuration item(s):</p>
<dl>
<dt>filename</p>
<dd>The path to the file.</p>
<dt>delimiter&nbsp;<wbr>=&nbsp;<wbr>:</p>
<dd>The character to use as a delimiter between fields. The default is &quot;:&quot;</p>
<dt>hash_size</p>
<dd>The size of the hashtable. If 0, then the passwords are not cached and the passwd file is parsed for every request. We do not recommend such a configuration. A larger hash_size means less probability of collision and faster search in hashtable. Having a hash_size in the range of 30-100% of the number of passwd file records is reasonable.</p>
<dt>allow_multiple_keys</p>
<dd>If set to &#8216;yes&#8217;, and more than one record in file matches the request, then the attributes from all records will be used. If set to &#8216;no&#8217; (the default) the module will warn about duplicated records.</p>
<dt>ignore_nislike</p>
<dd>If set to &#8216;yes&#8217;, then all records from the file beginning with the &#8216;+&#8217; sign will be ignored. The default is &#8216;no&#8217;.</p>
<dt>format</p>
<dd>The format of the fields in the file, given as an example line from the file, with the content of the fields as the RADIUS attributes which the fields map to. The fields are seperated by the &#8216;:&#8217; character.</dl>
<p> The key field is signified by being preceded with a &#8216;*&#8217; character, which indicates that the field has only one key, like the /etc/passwd file. The key field may instead be preceded with &#8216;*,&#8217;, which indicates that the field has multiple possible keys, like the /etc/group file. The other fields signify RADIUS attributes which, by default, are added to the configuration items for a request. To add an attribute to the request (as though it was sent by the NAS), prefix the attribute name in the &quot;format&quot; string with the &#8216;~&#8217; character. To add an attribute to the reply (to be sent back to the NAS) prefix the attribute name in the &quot;format&quot; string with the &#8216;=&#8217; character.</p>
<dl>
<dt>ignore_empty</p>
<dd>This configuration item defaults to &quot;yes&quot;. If there is no value for the attribute, then the attribute is not added. By setting this value to &quot;no&quot;, you can force the attribute to be added, even if there is no value. </p>
<h2>Examples</h2>
<pre><code>format = &quot;~My-Group:::*,User-Name&quot;</code></pre>
<dl>
<dd>Parse a file similar to the /etc/group file. An entry matches a request when the name in a User-Name attribute exists in the comma-seperated list of a line in the file. When an entry matches, a &quot;My-Group&quot; attribute will be created and added to the configuration items for the request. The value of that attribute will be taken from the first field of the matching line in the file.</p>
<dd>The &quot;:::&quot; in the format string means that there are extra two fields in the line, in between the group name and list of user names. Those fields do not map to any RADIUS attribute, and are therefore ignored.</p>
<dd>For this example to work in practice, you will have to add the My-Group attribute to the dictionary file. See the dictionary manual page for details on how this may be done.</dl>
<pre><code>format = &quot;~My-Group:::*,User-Name&quot;</code></pre>
<dl>
<dd>Similar to the previous entry, except the My-Group attribute is added to the request, as though it was sent by the NAS.</dl>
<h2>Sections</h2>
<p><code>authorize</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) <code><a href="/docs/linux/man/5-dictionary/">dictionary</a></code>(5),</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
