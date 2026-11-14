---
title: "snmpvacm(1)"
name: "snmpvacm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpvacm/"
description: "snmpvacm – creates and maintains SNMPv3 View-based Access Control entries on a network entity"
---

<h2>NAME</h2>
<p> snmpvacm &#8211; creates and maintains SNMPv3 View-based Access Control entries on a network entity</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>createSec2Group</code> MODEL SECURITYNAME GROUPNAME<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>deleteSec2Group</code> MODEL SECURITYNAME<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>createView</code> [-Ce] NAME SUBTREE MASK<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>deleteView</code> NAME SUBTREE<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>createAccess</code> GROUPNAME [CONTEXTPREFIX] MODEL LEVEL CONTEXTMATCH READVIEW WRITEVIEW NOTIFYVIEW<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>deleteAccess</code> GROUPNAME [CONTEXTPREFIX] MODEL LEVEL<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>createAuth</code> GROUPNAME [CONTEXTPREFIX] MODEL LEVEL AUTHTYPE CONTEXTMATCH VIEW<br />
 <code>snmpvacm</code> [COMMON OPTIONS] AGENT <code>deleteAuth</code> GROUPNAME [CONTEXTPREFIX] MODEL LEVEL AUTHTYPE </p>
<h2>DESCRIPTION</h2>
<p> <code>snmpvacm</code> is an SNMP application that can be used to do simple maintenance on the View-based Control Module (VACM) tables of an SNMP agent. The SNMPv3 VACM specifications (see RFC2575) define assorted tables to specify groups of users, MIB views, and authorised access settings. These <code>snmpvacm</code> commands effectively create or delete rows in the appropriate one of these tables, and match the equivalent configure directives which are documented in the <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> man page. </p>
<p> A fuller explanation of how these operate can be found in the project FAQ.</p>
<h2>SUB-COMMANDS</h2>
<h3>createSec2Group MODEL SECURITYNAME GROUPNAME</h3>
<p> Create an entry in the SNMPv3 security name to group table. This table allows a single access control entry to be applied to a number of users (or &#8216;principals&#8217;), and is indexed by the security model and security name values. </p>
<p> MODEL</p>
<dl>
<dt>
<dd> An integer representing the security model, taking one of the following values:<br />
 1 &#8211; reserved for SNMPv1<br />
 2 &#8211; reserved for SNMPv2c<br />
 3 &#8211; User-based Security Model (USM) </p>
</dl>
<p> SECURITYNAME</p>
<dl>
<dt>
<dd> A string representing the security name for a principal (represented in a security-model-independent format). For USM-based requests, the security name is the same as the username. </p>
</dl>
<p> GROUPNAME</p>
<dl>
<dt>
<dd> A string identifying the group that this entry (i.e. security name/model pair) should belong to. This group name will then be referenced in the access table (see <code>createAccess</code> below).</dl>
<h3>deleteSec2Group MODEL SECURITYNAME</h3>
<p> Delete an entry from the SNMPv3 security name to group table, thus removing access control settings for the given principal. The entry to be removed is indexed by the MODEL and SECURITYNAME values, which should match those used in the corresponding <code>createSec2Group</code> command (or equivalent). </p>
<h3>createView [-Ce] NAME SUBTREE MASK</h3>
<p> Create an entry in the SNMPv3 MIB view table. A MIB view consists of a family of view subtrees which may be individually included in or (occasionally) excluded from the view. Each view subtree is defined by a combination of an OID subtree together with a bit string mask. The view table is indexed by the view name and subtree OID values. </p>
<p> [-Ce]</p>
<dl>
<dt>
<dd> An optional flag to indicate that this view subtree should be excluded from the named view. If not specified, the default is to include the subtree in the view. When constructing a view from a mixture of included and excluded subtrees, the excluded subtrees should be defined first &#8211; particularly if the named view is already referenced in one or more access entries.</dl>
<p> NAME</p>
<dl>
<dt>
<dd> A string identifying a particular MIB view, of which this OID subtree/mask forms part (possibly the only part).</dl>
<p> SUBTREE</p>
<dl>
<dt>
<dd> The OID defining the root of the subtree to add to (or exclude from) the named view.</dl>
<p> MASK</p>
<dl>
<dt>
<dd> A bit mask indicating which sub-identifiers of the associated subtree OID should be regarded as significant. </p>
</dl>
<h3>deleteView NAME SUBTREE</h3>
<p> Delete an entry from the SNMPv3 view table, thus removing the subtree from the given MIB view. Removing the final (or only) subtree will result in the deletion of the view. The entry to be removed is indexed by the NAME and SUBTREE values, which should match those used in the corresponding <code>createView</code> command (or equivalent). </p>
<p> When removing subtrees from a mixed view (i.e. containing both included and excluded subtrees), the included subtrees should be removed first. </p>
<h3>createAccess GROUPNAME [CONTEXTPREFIX] MODEL LEVEL CONTEXTMATCH READVIEW WRITEVIEW NOTIFYVIEW</h3>
<p> Create an entry in the SNMPv3 access table, thus allowing a certain level of access to particular MIB views for the principals in the specified group (given suitable security model and levels in the request). The access table is indexed by the group name, context prefix, security model and security level values. </p>
<p> GROUPNAME</p>
<dl>
<dt>
<dd> The name of the group that this access entry applies to (as set up by a <code>createSec2Group</code> command, or equivalent)</dl>
<p> CONTEXTPREFIX</p>
<dl>
<dt>
<dd> A string representing a context name (or collection of context names) which this access entry applies to. The interpretation of this string depends on the value of the CONTEXTMATCH field (see below).</p>
<dt>
<dd> If omitted, this will default to the null context &quot;&quot;.</dl>
<p> MODEL</p>
<dl>
<dt>
<dd> An integer representing the security model, taking one of the following values:<br />
 1 &#8211; reserved for SNMPv1<br />
 2 &#8211; reserved for SNMPv2c<br />
 3 &#8211; User-based Security Model (USM)</dl>
<p> LEVEL</p>
<dl>
<dt>
<dd> An integer representing the minimal security level, taking one of the following values:<br />
 1 &#8211; noAuthNoPriv<br />
 2 &#8211; authNoPriv<br />
 3 &#8211; authPriv</p>
<dt>
<dd> This access entry will be applied to requests of this level or higher (where authPriv is higher than authNoPriv which is in turn higher than noAuthNoPriv).</dl>
<p> CONTEXTMATCH</p>
<dl>
<dt>
<dd> Indicates how to interpret the CONTEXTPREFIX value. If this field has the value &#8216;1&#8217; (representing &#8216;exact&#8217;) then the context name of a request must match the CONTEXTPREFIX value exactly for this access entry to be applicable to that request.</p>
<dt>
<dd> If this field has the value &#8216;2&#8217; (representing &#8216;prefix&#8217;) then the initial substring of the context name of a request must match the CONTEXTPREFIX value for this access entry to be applicable to that request. This provides a simple form of wildcarding.</dl>
<p> READVIEW</p>
<dl>
<dt>
<dd> The name of the MIB view (as set up by <code>createView</code> or equivalent) defining the MIB objects for which this request may request the current values.</p>
<dt>
<dd> If there is no view with this name, then read access is not granted.</dl>
<p> WRITEVIEW</p>
<dl>
<dt>
<dd> The name of the MIB view (as set up by <code>createView</code> or equivalent) defining the MIB objects for which this request may potentially SET new values.</p>
<dt>
<dd> If there is no view with this name, then read access is not granted.</dl>
<p> NOTIFYVIEW</p>
<dl>
<dt>
<dd> The name of the MIB view (as set up by <code>createView</code> or equivalent) defining the MIB objects which may be included in notification request.</p>
<dt>
<dd> Note that this aspect of access control is not currently supported. </p>
</dl>
<h3>deleteAccess GROUPNAME [CONTEXTPREFIX] MODEL LEVEL</h3>
<p> Delete an entry from the SNMPv3 access table, thus removing the specified access control settings. The entry to be removed is indexed by the group name, context prefix, security model and security level values, which should match those used in the corresponding <code>createAccess</code> command (or equivalent). </p>
<h3>createAuth GROUPNAME [CONTEXTPREFIX] MODEL LEVEL AUTHTYPE CONTEXTMATCH VIEW</h3>
<p> Create an entry in the Net-SNMP extension to the standard access table, thus allowing a certain type of access to the MIB view for the principals in the specified group. The interpretation of GROUPNAME, CONTEXTPREFIX, MODEL, LEVEL and CONTEXTMATCH are the same as for the <code>createAccess</code> directive. The extension access table is indexed by the group name, context prefix, security model, security level and authtype values. </p>
<p> AUTHTYPE</p>
<dl>
<dt>
<dd> The style of access that this entry should be applied to. See <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> and <i><a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)</i> for details of valid tokens.</dl>
<p> VIEW</p>
<dl>
<dt>
<dd> The name of the MIB view (as set up by <code>createView</code> or equivalent) defining the MIB objects for which this style of access is authorized. </p>
</dl>
<h3>deleteAuth GROUPNAME [CONTEXTPREFIX] MODEL LEVEL AUTHTYPE</h3>
<p> Delete an entry from the extension access table, thus removing the specified access control settings. The entry to be removed is indexed by the group name, context prefix, security model, security level and authtype values, which should match those used in the corresponding <code>createAuth</code> command (or equivalent). </p>
<p> Note that <code>snmpget</code> REQUIRES an argument specifying the agent to query as described in the .I <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) manual page. </p>
<h2>EXAMPLES</h2>
<p> Given a pre-existing user <i>dave</i> (which could be set up using the <i><a href="/docs/linux/man/1-snmpusm/">snmpusm</a>(1)</i> command), we could configure full read-write access to the whole OID tree using the commands: </p>
<dl>
<dt>
<dd> snmpvacm localhost createSec2Group 3 dave RWGroup</p>
<dt>
<dd> snmpvacm localhost createView all .1 80</p>
<dt>
<dd> snmpvacm localhost createAccess RWGroup 3 1 1 all all none</dl>
<p> This creates a new security group named &quot;RWGroup&quot; containing the SNMPv3 user &quot;dave&quot;, a new view &quot;all&quot; containing the full OID tree based on <i><a href="/docs/linux/man/1--iso/">.iso</a>(1)</i> , and then allows those users in the group &quot;RWGroup&quot; (i.e. &quot;dave&quot;) both read- and write-access to the view &quot;all&quot; (i.e. the full OID tree) when using authenticated SNMPv3 requests. </p>
<p> As a second example, we could set up read-only access to a portion of the OID tree using the commands: </p>
<dl>
<dt>
<dd> snmpvacm localhost createSec2Group 3 wes ROGroup</p>
<dt>
<dd> snmpvacm localhost createView sysView system fe</p>
<dt>
<dd> snmpvacm localhost createAccess ROGroup 3 0 1 sysView none none</dl>
<p> This creates a new security group named &quot;ROGroup&quot; containing the (pre-existing) user &quot;wes&quot;, a new view &quot;sysView&quot; containing just the OID tree based on <i><a href="/docs/linux/man/1--iso/">.iso</a>(1)<a href="/docs/linux/man/3--org/">.org</a>(3)<a href="/docs/linux/man/6--dod/">.dod</a>(6)<a href="/docs/linux/man/1--inet/">.inet</a>(1)<a href="/docs/linux/man/2--mgmt/">.mgmt</a>(2)<a href="/docs/linux/man/1--mib-2/">.mib-2</a>(1)<a href="/docs/linux/man/1--system/">.system</a>(1)</i> , and then allows those users in the group &quot;ROGroup&quot; (i.e. &quot;wes&quot;) read-access, but not write-access to the view &quot;sysView&quot; (i.e. the system group). </p>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned: </p>
<p> 0 &#8211; Successful completion </p>
<p> 1 &#8211; A usage syntax error (which displays a suitable usage message) or a request timeout. </p>
<p> 2 &#8211; An error occurred while executing the command (which also displays a suitable error message). </p>
<h2>LIMITATIONS</h2>
<p> This utility does not support the configuration of new community strings, so is only of use for setting up new access control for SNMPv3 requests. It can be used to amend the access settings for existing community strings, but not to set up new ones. </p>
<p> The use of numeric parameters for <code>secLevel</code> and <code>contextMatch</code> parameters is less than intuitive. These commands do not provide the full flexibility of the equivalent config file directives. </p>
<p> There is (currently) no equivalent to the one-shot configure directives <i>rouser</i> and <i>rwuser.</i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpusm/">snmpusm</a>(1), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), RFC 2575, Net-SNMP project FAQ </p>
<h2>Index</h2>
