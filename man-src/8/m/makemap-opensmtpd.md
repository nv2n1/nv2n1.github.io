---
title: "makemap-opensmtpd(8)"
name: "makemap-opensmtpd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makemap-opensmtpd/"
description: "makemap – create database maps for smtpd"
---

<p><code>makemap</code> &#8211; create database maps for smtpd</p>
<h2>Synopsis</h2>
<p><code>makemap</code> [<code>-U</code>] [<code>-d</code> <i>dbtype</i>] [<code>-o</code> <i>dbfile</i>] [<code>-t</code> <i>type</i>] <i>file</i></p>
<h2>Description</h2>
<p>Maps provide a generic interface for associating textual key to a value. Such associations may be accessed through a plaintext file, database, or DNS. The format of these file types is described below. <code>makemap</code> itself creates the database maps used by keyed map lookups specified in <code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5). </p>
<p> <code>makemap</code> reads input from <i>file</i> and writes data to a file whose name is made by adding a &#8220;.db&#8221; suffix to <i>file</i>. The current line can be extended over multiple lines using a backslash (Sq \.) Comments can be put anywhere in the file using a hash mark (Sq #,) and extend to the end of the current line. Care should be taken when commenting out multi-line text: the comment is effective until the end of the entire block. In all cases, <code>makemap</code> reads lines consisting of words separated by whitespace. The first word of a line is the database key; the remainder represents the mapped value. The database key and value may optionally be separated by the colon character. </p>
<p> The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>-d</code> <i>dbtype</i></p>
<dd>Specify the format of the database. Available formats are <i>hash</i> and <i>btree</i>. The default value is <i>hash</i>.</p>
<dt><code>-o</code> <i>dbfile</i></p>
<dd>Write the generated database to <i>dbfile</i>.</p>
<dt><code>-t</code> <i>type</i></p>
<dd>Specify the format of the resulting map file. The default map format is suitable for storing simple, unstructured, key-to-value string associations. However, if the mapped value has special meaning, as in the case of the virtual domains file, a suitable <i>type</i> must be provided. The available output types are:</p>
<dl>
<dd>
<dl>
<dt><code>aliases</code></p>
<dd>The mapped value is a comma-separated list of mail destinations. This format can be used for building user aliases and user mappings for virtual domain files.</p>
<dt><code>set</code></p>
<dd>There is no mapped value &#8211; a map of this type will only allow for the lookup of keys. This format can be used for building primary domain maps.</dl>
</dl>
<dt><code>-U</code></p>
<dd>Instead of generating a database map from text input, dump the contents of a database map as text with the key and value separated with a tab.</dl>
</dl>
<h2>Primary Domains</h2>
<p>Primary domains can be kept in tables. To create a primary domain table, add each primary domain on a single line by itself. </p>
<p> In addition to adding an entry to the primary domain map, one must add a filter rule that accepts mail for the domain map, for example:</p>
<dl>
<dd>
<pre>table domains &quot;/etc/opensmtpd/domains&quot;
accept for domain &lt;domains&gt; deliver to mbox
</dl></pre>
<h2>Virtual Domains</h2>
<p>Virtual domains may also be kept in tables. To create a virtual domain table, add each virtual domain on a single line by itself. </p>
<p> Virtual domains expect a mapping of virtual users to real users in order to determine if a recipient is accepted or not. The mapping format is an extension to <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), which allows the use of &#8220;user [at] domain.tld&#8221; to accept user only on the specified domain, &#8220;user&#8221; to accept the user for any of the virtual domains, &#8220;@domain.tld&#8221; to provide a catch-all for the specified domain and &#8220;@&#8221; to provide a global catch-all for all domains. <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) will perform the lookups in that specific order. </p>
<p> To create single virtual address, add &#8220;user [at] example.com user&#8221; to the users map. To handle all mail destined to any user at example.com, add &#8220;@example.com user&#8221; to the virtual map. </p>
<p> In addition to adding an entry to the virtual map, one must add a filter rule that accepts mail for virtual domains, for example:</p>
<dl>
<dd>
<pre>table vdomains &quot;/etc/opensmtpd/vdomains&quot;
table vusers &quot;/etc/opensmtpd/users&quot;
accept for domain &lt;vdomains&gt; virtual &lt;vusers&gt; deliver to mbox
accept for domain example.org virtual &lt;vusers&gt; deliver to mbox
</dl></pre>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/etc/opensmtpd/aliases</code></p>
<dd>List of user mail aliases.</p>
<dt><code>/etc/opensmtpd/secrets</code></p>
<dd>List of remote host credentials.</dl>
</dl>
<h2>Exit Status</h2>
<p>The <code>makemap</code> utility exits 0 on success, and &gt;0 if an error occurs. makemap</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/5-smtpd-conf/">smtpd.conf</a></code>(5), <code><a href="/docs/linux/man/5-table/">table</a></code>(5), <code><a href="/docs/linux/man/8-newaliases/">newaliases</a></code>(8), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>History</h2>
<p>The <code>makemap</code> command first appeared in OpenBSD 4.6 as a replacement for the equivalent command shipped with sendmail.</p>
