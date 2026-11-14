---
title: "rlm_sql(5)"
name: "rlm_sql"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_sql/"
description: "rlm_sql – FreeRADIUS Module"
---

<p>rlm_sql &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_sql</i> module provides an SQL interface to retrieve authorization information and store accounting information. It can be used in conjunction with, or in lieu of the files and detail modules. The SQL module has drivers to support the following SQL databases: </p>
<dl>
<dd>
<pre><br>
 db2
<br>
 iodbc
<br>
 mysql
<br>
 oracle
<br>
 postgresql
<br>
 sybase
<br>
 unixodbc
<br></pre>
</dl>
<p> Due to the size of the configuration variables, the sql module is usually configured in a separate file, which is included in the main radiusd.conf via an include directive. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>driver</p>
<dd>This variable specifies the driver to be loaded.</p>
<dt>server</p>
<dd>
<dt>login</p>
<dd>
<dt>password</p>
<dd>These specify the servername, username, and password the module will use to connect to the database.</p>
<dt>radius_db</p>
<dd>The name of the database where the radius tables are stored.</p>
<dt>acct_table1</p>
<dd>
<dt>acct_table2</p>
<dd>These specify the tables names for accounting records. acct_table1 specifies the table where Start records are stored. acct_table2 specifies the table where Stop records are stored. In most cases, this should be the same table.</p>
<dt>postauth_table</p>
<dd>The name of the table to store post-authentication data.</p>
<dt>authcheck_table</p>
<dd>
<dt>authreply_table</p>
<dd>The tables where individual Check-Items and Reply-Items are stored.</p>
<dt>groupcheck_table</p>
<dd>
<dt>groupreply_table</p>
<dd>The tables where group Check-Items and Reply-Items are stored.</p>
<dt>usergroup_table</p>
<dd>The table where username to group relationships are stored.</p>
<dt>deletestatlesessions</p>
<dd>This option is set to &#8216;yes&#8217; or &#8216;no&#8217;. If you are doing Simultaneous-Use checking, and this is set to yes, stale sessions ( defined as sessions for which a Stop record was not received ) will be cleared.</p>
<dt>logfile</p>
<dd>This option is useful for debugging sql problems. If logfile is set then all sql queries for the containing section are written to the file specified. This is useful for debugging and bulk inserts.</p>
<dt>num_sql_socks</p>
<dd>The number of sql connections to make to the database.</p>
<dt>connect_failure_retry_delay</p>
<dd>The number of seconds to wait before attempting to reconnect to a failed database connection.</p>
<dt>sql_user_name</p>
<dd>This is the definition of the SQL-User-Name attribute. This is set once, so that you can use %{SQL-User-Name} in the SQL queries, rather than the nested username substitution. This ensures that Username is parsed consistently for all SQL queries executed.</p>
<dt>default_user_profile</p>
<dd>This is the default profile name that will be applied to all users if set. This is not set by default.</p>
<dt>query_on_not_found</p>
<dd>This option is set to &#8216;yes&#8217; or &#8216;no&#8217;. If set to yes, then the default user profile is returned if no specific match was found for the user.</p>
<dt>authorize_check_query</p>
<dd>
<dt>authorize_reply_query</p>
<dd>These queries are run during the authorization stage to extract the user authorization information from the ${authcheck_table} and ${authreply_table}.</p>
<dt>authorize_group_check_query</p>
<dd>
<dt>authorize_group_reply_query</p>
<dd>These queries are run during the authorization stage to extract the group authorization information from the ${groupcheck_table} and ${groupreply_table}.</p>
<dt>accounting_onoff_query</p>
<dd>The query to be run when receiving an Accounting On or Accounting Off packet.</p>
<dt>accounting_update_query</p>
<dd>
<dt>accounting_update_query_alt</p>
<dd>The query to be run when receiving an Accounting Update packet. If the primary query fails, the alt query is run.</p>
<dt>accounting_start_query</p>
<dd>
<dt>accounting_start_query_alt</p>
<dd>The query to be run when receiving an Accounting Start packet. If the primary query fails, the alt query is run.</p>
<dt>accounting_stop_query</p>
<dd>
<dt>accounting_stop_query_alt</p>
<dd>The query to be run when receiving an Accounting Stop packet. If the primary query fails, the alt query is run.</p>
<dt>simul_count_query</p>
<dd>The query to be run to return the number simultaneous sessions for the purposes of limiting Simultaneous Use.</p>
<dt>simul_verify_query</p>
<dd>The query to return the detail information needed to confirm that all suspected connected sessions are valid, and are not stale sessions.</p>
<dt>group_membership_query</p>
<dd>The query to run to check user group membership.</p>
<dt>postauth_query</p>
<dd>The query to run during the post-authentication stage.</dl>
<h2>Configuration</h2>
<p>Due to the size of the configuration for this module, it is not included in this manual page. Please review the supplied configuration files for example queries and configuration details.</p>
<h2>Sections</h2>
<p><code>authorization,</code> <code>accounting,</code> <code>checksimul,</code> <code>post-authentication</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf,</i> <i>/etc/raddb/sql.conf,</i> <i>/etc/raddb/sql/&lt;DB&gt;/dialup.conf,</i> <i>/etc/raddb/sql/&lt;DB&gt;/schema.sql,</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5),</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
