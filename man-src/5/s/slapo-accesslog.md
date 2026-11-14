---
title: "slapo-accesslog(5)"
name: "slapo-accesslog"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-accesslog/"
description: "slapo-accesslog – Access Logging overlay to slapd"
---

<p>slapo-accesslog &#8211; Access Logging overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Access Logging overlay can be used to record all accesses to a given backend database on another database. This allows all of the activity on a given database to be reviewed using arbitrary LDAP queries, instead of just logging to local flat text files. Configuration options are available for selecting a subset of operation types to log, and to automatically prune older log records from the logging database. Log records are stored with audit schema (see below) to assure their readability whether viewed as LDIF or in raw form.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the Access Logging overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>logdb &lt;suffix&gt;</code></p>
<dd>Specify the suffix of a database to be used for storing the log records. The specified database must be defined elsewhere in the configuration. The access controls on the log database should prevent general access. The suffix entry of the log database will be created automatically by this overlay. The log entries will be generated as the immediate children of the suffix entry.</p>
<dt><code>logops &lt;operations&gt;</code></p>
<dd>Specify which types of operations to log. The valid operation types are abandon, add, bind, compare, delete, extended, modify, modrdn, search, and unbind. Aliases for common sets of operations are also available:</p>
<dl>
<dd>
<dl>
<dt><code>writes</code></p>
<dd>add, delete, modify, modrdn</p>
<dt><code>reads</code></p>
<dd>compare, search</p>
<dt><code>session</code></p>
<dd>abandon, bind, unbind</p>
<dt><code>all</code></p>
<dd>all operations</dl>
</dl>
<dt><code>logbase &lt;operations&gt; &lt;baseDN&gt;</code></p>
<dd>Specify a set of operations that will only be logged if they occur under a specific subtree of the database. The operation types are as above for the <code>logops</code> setting, and delimited by a &#8216;|&#8217; character.</p>
<dt><code>logold &lt;filter&gt;</code></p>
<dd>Specify a filter for matching against Deleted and Modified entries. If the entry matches the filter, the old contents of the entry will be logged along with the current request.</p>
<dt><code>logoldattr &lt;attr&gt; &#8230;</code></p>
<dd>Specify a list of attributes whose old contents are always logged in Modify and ModRDN requests. Usually only the contents of attributes that were actually modified will be logged; by default no old attributes are logged for ModRDN requests.</p>
<dt><code>logpurge &lt;age&gt; &lt;interval&gt;</code></p>
<dd>Specify the maximum age for log entries to be retained in the database, and how often to scan the database for old entries. Both the <code>age</code> and <code>interval</code> are specified as a time span in days, hours, minutes, and seconds. The time format is [ddd+]hh:mm[:ss] i.e., the days and seconds components are optional but hours and minutes are required. Except for days, which can be up to 5 digits, each numeric field must be exactly two digits. For example</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>logpurge 2+00:00 1+00:00</p>
<dd></dl>
</dl>
<p> would specify that the log database should be scanned every day for old entries, and entries older than two days should be deleted. When using a log database that supports ordered indexing on generalizedTime attributes, specifying an eq index on the <code>reqStart</code> attribute will greatly benefit the performance of the purge operation.</dl>
<dt><code>logsuccess TRUE | FALSE</code></p>
<dd>If set to TRUE then log records will only be generated for successful requests, i.e., requests that produce a result code of 0 (LDAP_SUCCESS). If FALSE, log records are generated for all requests whether they succeed or not. The default is FALSE. </p>
</dl>
<h2>Examples</h2>
<pre> database bdb
 suffix dc=example,dc=com
 ...
 overlay accesslog
 logdb cn=log
 logops writes reads
 logbase search|compare ou=testing,dc=example,dc=com
 logold (objectclass=person)
 database bdb
 suffix cn=log
 ...
 index reqStart eq
 access to *
 by dn.base=&quot;cn=admin,dc=example,dc=com&quot; read</pre>
<h2>Schema</h2>
<p>The <code>accesslog</code> overlay utilizes the &quot;audit&quot; schema described herein. This schema is specifically designed for <code>accesslog</code> auditing and is not intended to be used otherwise. It is also noted that the schema described here is <i>a work in</i> <i>progress</i>, and hence subject to change without notice. The schema is loaded automatically by the overlay. </p>
<p> The schema includes a number of object classes and associated attribute types as described below. </p>
<p> There is a basic <code>auditObject</code> class from which two additional classes, <code>auditReadObject</code> and <code>auditWriteObject</code> are derived. Object classes for each type of LDAP operation are further derived from these classes. This object class hierarchy is designed to allow flexible yet efficient searches of the log based on either a specific operation type&#8217;s class, or on more general classifications. The definition of the <code>auditObject</code> class is as follows: </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.1<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditObject&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;OpenLDAP request auditing&#8217;<br />
&nbsp;<wbr>SUP top STRUCTURAL<br />
&nbsp;<wbr>MUST&nbsp;<wbr>(&nbsp;<wbr>reqStart&nbsp;<wbr>$&nbsp;<wbr>reqType&nbsp;<wbr>$&nbsp;<wbr>reqSession&nbsp;<wbr>)<br />
&nbsp;<wbr>MAY&nbsp;<wbr>(&nbsp;<wbr>reqDN&nbsp;<wbr>$&nbsp;<wbr>reqAuthzID&nbsp;<wbr>$&nbsp;<wbr>reqControls&nbsp;<wbr>$&nbsp;<wbr>reqRespControls&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>reqEnd&nbsp;<wbr>$&nbsp;<wbr>reqResult&nbsp;<wbr>$&nbsp;<wbr>reqMessage&nbsp;<wbr>$&nbsp;<wbr>reqReferral&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> Note that all of the OIDs used in the logging schema currently reside under the OpenLDAP Experimental branch. It is anticipated that they will migrate to a Standard branch in the future. </p>
<p> An overview of the attributes follows: <code>reqStart</code> and <code>reqEnd</code> provide the start and end time of the operation, respectively. They use generalizedTime syntax. The <code>reqStart</code> attribute is also used as the RDN for each log entry. </p>
<p> The <code>reqType</code> attribute is a simple string containing the type of operation being logged, e.g. <code>add</code>, <code>delete</code>, <code>search</code>, etc. For extended operations, the type also includes the OID of the extended operation, e.g. <code>extended(1.1.1.1)</code> </p>
<p> The <code>reqSession</code> attribute is an implementation-specific identifier that is common to all the operations associated with the same LDAP session. Currently this is slapd&#8217;s internal connection ID, stored in decimal. </p>
<p> The <code>reqDN</code> attribute is the distinguishedName of the target of the operation. E.g., for a Bind request, this is the Bind DN. For an Add request, this is the DN of the entry being added. For a Search request, this is the base DN of the search. </p>
<p> The <code>reqAuthzID</code> attribute is the distinguishedName of the user that performed the operation. This will usually be the same name as was established at the start of a session by a Bind request (if any) but may be altered in various circumstances. </p>
<p> The <code>reqControls</code> and <code>reqRespControls</code> attributes carry any controls sent by the client on the request and returned by the server in the response, respectively. The attribute values are just uninterpreted octet strings. </p>
<p> The <code>reqResult</code> attribute is the numeric LDAP result code of the operation, indicating either success or a particular LDAP error code. An error code may be accompanied by a text error message which will be recorded in the <code>reqMessage</code> attribute. </p>
<p> The <code>reqReferral</code> attribute carries any referrals that were returned with the result of the request. </p>
<p> Operation-specific classes are defined with additional attributes to carry all of the relevant parameters associated with the operation: </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.4<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditAbandon&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Abandon operation&#8217;<br />
&nbsp;<wbr>SUP auditObject STRUCTURAL<br />
&nbsp;<wbr>MUST reqId&nbsp;<wbr>)</dl>
<p> For the <code>Abandon</code> operation the <code>reqId</code> attribute contains the message ID of the request that was abandoned. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.5<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditAdd&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Add operation&#8217;<br />
&nbsp;<wbr>SUP auditWriteObject STRUCTURAL<br />
&nbsp;<wbr>MUST reqMod&nbsp;<wbr>)</dl>
<p> The <code>Add</code> class inherits from the <code>auditWriteObject</code> class. The Add and Modify classes are very similar. The <code>reqMod</code> attribute carries all of the attributes of the original entry being added. (Or in the case of a Modify operation, all of the modifications being performed.) The values are formatted as</p>
<dl>
<dd>
<dl>
<dt>attribute:&lt;+|-|=|#&gt; [ value]</p>
<dd></dl>
</dl>
<p> Where &#8216;+&#8217; indicates an Add of a value, &#8216;-&#8216; for Delete, &#8216;=&#8217; for Replace, and &#8216;#&#8217; for Increment. In an Add operation, all of the reqMod values will have the &#8216;+&#8217; designator. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.6<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditBind&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Bind operation&#8217;<br />
&nbsp;<wbr>SUP auditObject STRUCTURAL<br />
&nbsp;<wbr>MUST&nbsp;<wbr>(&nbsp;<wbr>reqVersion&nbsp;<wbr>$&nbsp;<wbr>reqMethod&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> The <code>Bind</code> class includes the <code>reqVersion</code> attribute which contains the LDAP protocol version specified in the Bind as well as the <code>reqMethod</code> attribute which contains the Bind Method used in the Bind. This will be the string <code>SIMPLE</code> for LDAP Simple Binds or <code>SASL(&lt;mech&gt;)</code> for SASL Binds. Note that unless configured as a global overlay, only Simple Binds using DNs that reside in the current database will be logged. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.7<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditCompare&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Compare operation&#8217;<br />
&nbsp;<wbr>SUP auditObject STRUCTURAL<br />
&nbsp;<wbr>MUST reqAssertion&nbsp;<wbr>)</dl>
<p> For the <code>Compare</code> operation the <code>reqAssertion</code> attribute carries the Attribute Value Assertion used in the compare request. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.8<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditDelete&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Delete operation&#8217;<br />
&nbsp;<wbr>SUP auditWriteObject STRUCTURAL<br />
&nbsp;<wbr>MAY reqOld&nbsp;<wbr>)</dl>
<p> The <code>Delete</code> operation needs no further parameters. However, the <code>reqOld</code> attribute may optionally be used to record the contents of the entry prior to its deletion. The values are formatted as</p>
<dl>
<dd>
<dl>
<dt>attribute: value</p>
<dd></dl>
</dl>
<p> The <code>reqOld</code> attribute is only populated if the entry being deleted matches the configured <code>logold</code> filter. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.9<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditModify&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Modify operation&#8217;<br />
&nbsp;<wbr>SUP auditWriteObject STRUCTURAL<br />
&nbsp;<wbr>MAY reqOld MUST reqMod&nbsp;<wbr>)</dl>
<p> The <code>Modify</code> operation contains a description of modifications in the <code>reqMod</code> attribute, which was already described above in the Add operation. It may optionally contain the previous contents of any modified attributes in the <code>reqOld</code> attribute, using the same format as described above for the Delete operation. The <code>reqOld</code> attribute is only populated if the entry being modified matches the configured <code>logold</code> filter. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.10<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditModRDN&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;ModRDN operation&#8217;<br />
&nbsp;<wbr>SUP auditWriteObject STRUCTURAL<br />
&nbsp;<wbr>MUST&nbsp;<wbr>(&nbsp;<wbr>reqNewRDN&nbsp;<wbr>$&nbsp;<wbr>reqDeleteOldRDN&nbsp;<wbr>)<br />
&nbsp;<wbr>MAY&nbsp;<wbr>(&nbsp;<wbr>reqNewSuperior&nbsp;<wbr>$&nbsp;<wbr>reqOld&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> The <code>ModRDN</code> class uses the <code>reqNewRDN</code> attribute to carry the new RDN of the request. The <code>reqDeleteOldRDN</code> attribute is a Boolean value showing <code>TRUE</code> if the old RDN was deleted from the entry, or <code>FALSE</code> if the old RDN was preserved. The <code>reqNewSuperior</code> attribute carries the DN of the new parent entry if the request specified the new parent. The <code>reqOld</code> attribute is only populated if the entry being modified matches the configured <code>logold</code> filter and contains attributes in the <code>logoldattr</code> list. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.11<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditSearch&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Search operation&#8217;<br />
&nbsp;<wbr>SUP auditReadObject STRUCTURAL<br />
&nbsp;<wbr>MUST&nbsp;<wbr>(&nbsp;<wbr>reqScope&nbsp;<wbr>$&nbsp;<wbr>reqDerefAliases&nbsp;<wbr>$&nbsp;<wbr>reqAttrsOnly&nbsp;<wbr>)<br />
&nbsp;<wbr>MAY&nbsp;<wbr>(&nbsp;<wbr>reqFilter&nbsp;<wbr>$&nbsp;<wbr>reqAttr&nbsp;<wbr>$&nbsp;<wbr>reqEntries&nbsp;<wbr>$&nbsp;<wbr>reqSizeLimit&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>reqTimeLimit&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> For the <code>Search</code> class the <code>reqScope</code> attribute contains the scope of the original search request, using the values specified for the LDAP URL format. I.e. <code>base</code>, <code>one</code>, <code>sub</code>, or <code>subord</code>. The <code>reqDerefAliases</code> attribute is one of <code>never</code>, <code>finding</code>, <code>searching</code>, or <code>always</code>, denoting how aliases will be processed during the search. The <code>reqAttrsOnly</code> attribute is a Boolean value showing <code>TRUE </code> if only attribute names were requested, or <code>FALSE</code> if attributes and their values were requested. The <code>reqFilter</code> attribute carries the filter used in the search request. The <code>reqAttr</code> attribute lists the requested attributes if specific attributes were requested. The <code>reqEntries</code> attribute is the integer count of how many entries were returned by this search request. The <code>reqSizeLimit</code> and <code>reqTimeLimit</code> attributes indicate what limits were requested on the search operation. </p>
<dl>
<dd>( 1.3.6.1.4.1.4203.666.11.5.2.12<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;auditExtended&#8217;<br />
&nbsp;<wbr>DESC&nbsp;<wbr>&#8216;Extended operation&#8217;<br />
&nbsp;<wbr>SUP auditObject STRUCTURAL<br />
&nbsp;<wbr>MAY reqData&nbsp;<wbr>)</dl>
<p> The <code>Extended</code> class represents an LDAP Extended Operation. As noted above, the actual OID of the operation is included in the <code>reqType</code> attribute of the parent class. If any optional data was provided with the request, it will be contained in the <code>reqData</code> attribute as an uninterpreted octet string.</p>
<h2>Notes</h2>
<p>The Access Log implemented by this overlay may be used for a variety of other tasks, e.g. as a ChangeLog for a replication mechanism, as well as for security/audit logging purposes. </p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5). </p>
<h2>Acknowledgements</h2>
<p>This module was written in 2005 by Howard Chu of Symas Corporation.</p>
