---
title: "rlm_sql_log(5)"
name: "rlm_sql_log"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_sql_log/"
description: "rlm_sql_log – FreeRADIUS Module"
---

<p>rlm_sql_log &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <code>rlm_sql_log</code> module appends the SQL queries in a log file which is read later by the scripts/radsqlrelay Perl program. </p>
<p> The purpose of this module is to de-couple the storage of long-term accounting data in SQL from &quot;live&quot; information needed by the RADIUS server as it&#8217;s running. If you are not using SQL for simultaneous login restrictions (i.e. &quot;sql&quot; is not listed in the &quot;session&quot; section of &quot;radiusd.conf&quot;), then this module allows you to log SQL queries to a file, and then process them at your leisure. </p>
<p> The benefit of this approach is that for a busy server, the overhead of performing SQL qeuries may be significant. Also, if the SQL databases are large (as is typical for ones storing months of data), the INSERTs and UPDATEs may take a relatively long time. Rather than slowing down the RADIUS server by having it interact with a database, you can just log the queries to a file, and then run those queries on another machine, or at a time when the RADIUS server is typically lightly loaded. </p>
<p> If the &quot;sql&quot; module is listed in the &quot;session&quot; section of &quot;radiusd.conf&quot;, then a similar system can still be used. In that case, one database would be used to maintain &quot;live&quot; session information. That database would be small, fast, and information would be deleted from it when a user logs out. A second database would store long-term accounting information, as described above.</p>
<h2>Limitations</h2>
<p>This module only performs the dynamic expansion of the variables found in the SQL statements. No operation is executed on the database server. (this would be done later by an external program) That means the module is useful only with non-&quot;SELECT&quot; statements.</p>
<h2>Configuration</h2>
<p>The main configuration items to be aware of are the path of the log file and the different SQL queries.</p>
<dl>
<dt>path</p>
<dd>An entry named &quot;path&quot; sets the full path of the file where the SQL queries are recorded. (this variable is run through dynamic string expansion, and can include FreeRADIUS variables to create a dynamic filename)</p>
<dt>Accounting queries</p>
<dd>When a accounting record is processed, the module searches a config entry keyed by the Acct-Status-Type attribute present in the packet. For example, the SQL to be run on an accounting start must be named &quot;Start&quot; in the configuration for the module. Other usual values for Acct-Status-Type are &quot;Stop&quot;, &quot;Alive&quot;, &quot;Accounting-On&quot;, etc. See the VALUEs for Acct-Status-Type in the dictionary.rfc2866 file.</p>
<dt>Post-Auth query</p>
<dd>An entry named &quot;Post-Auth&quot; sets the query to run during the post-authentication stage. This query is mainly used to log sessions where there may not be a later accounting packet.</dl>
<dl>
<dd>
<pre>modules {
 ...
<br>
 sql_log {
<br>
 path = &quot;${radacctdir}/sql-relay&quot;
<br>
 acct_table = &quot;radacct&quot;
<br>
 postauth_table = &quot;radpostauth&quot;
<br>
 sql_user_name = &quot;%{%{User-Name}:-DEFAULT}&quot;
<br>
<br>
 Start = &quot;INSERT INTO ${acct_table} ...&quot;
<br>
 Stop = &quot;UPDATE ${acct_table} SET ...&quot;
<br>
 Alive = &quot;UPDATE ${acct_table} SET ...&quot;
<br>
<br>
 Post-Auth = &quot;INSERT INTO ${postauth_table} ...&quot;
<br>
 }
<br>
 ...
<br>
}
<br>
accounting {
 ...
<br>
 sql_log
 ...
<br>
}
<br>
<br>
post-auth {
 ...
<br>
 sql_log
 ...
<br>
}</pre>
</dl>
<h2>Sections</h2>
<p><code>accounting,</code> <code>post-auth</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radsqlrelay/">radsqlrelay</a></code>(8), <code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Nicolas Baradakis &lt;nicolas.baradakis [at] cegetel.net&gt;</p>
