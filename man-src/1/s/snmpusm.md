---
title: "snmpusm(1)"
name: "snmpusm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpusm/"
description: "snmpusm – creates and maintains SNMPv3 users on a network entity"
---

<h2>NAME</h2>
<p> snmpusm &#8211; creates and maintains SNMPv3 users on a network entity</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpusm</code> [COMMON OPTIONS] [-Cw] AGENT <code>create</code> USER [CLONEFROM-USER]<br />
 <code>snmpusm</code> [COMMON OPTIONS] AGENT <code>delete</code> USER<br />
 <code>snmpusm</code> [COMMON OPTIONS] AGENT <code>cloneFrom</code> USER CLONEFROM-USER<br />
 <code>snmpusm</code> [COMMON OPTIONS] [-Ca] [-Cx] AGENT <code>passwd</code> OLD-PASSPHRASE NEW-PASSPHRASE [USER]<br />
 <code>snmpusm</code> [COMMON OPTIONS] &lt;-Ca | -Cx&gt; -Ck AGENT <code>passwd</code> OLD-KEY-OR-PASSPHRASE NEW-KEY-OR-PASSPHRASE [USER]<br />
 <code>snmpusm</code> [COMMON OPTIONS] [-Ca] [-Cx] AGENT <code>changekey</code> [USER] </p>
<h2>DESCRIPTION</h2>
<p> <code>snmpusm</code> is an SNMP application that can be used to do simple maintenance on the users known to an SNMP agent, by manipulating the agent&#8217;s User-based Security Module (USM) table. The user needs write access to the usmUserTable MIB table. This tool can be used to create, delete, clone, and change the passphrase of users configured on a running SNMP agent. </p>
<h2>OPTIONS</h2>
<p> Common options for all <code>snmpusm</code> commands:</p>
<dl>
<dt><code>-CE</code><i> ENGINE-ID</i></p>
<dd> Set usmUserEngineID to be used as part of the index of the usmUserTable. Default is to use the contextEngineID (set via -E or probed) as the usmUserEngineID.</p>
<dt><code>-Cp</code><i> STRING</i></p>
<dd> Set the usmUserPublic value of the (new) user to the specified STRING.</dl>
<p> Options for the <code>passwd </code> and <code>changekey</code> commands:</p>
<dl>
<dt><code>-Ca</code></p>
<dd> Change the authentication key.</p>
<dt><code>-Cx</code></p>
<dd> Change the privacy key.</p>
<dt><code>-Ck</code></p>
<dd> Allows one to use localized key (must start with 0x) instead of passphrase. When this option is used, either the -Ca or -Cx option (but not both) must also be used. </p>
</dl>
<h2>CREATING USERS</h2>
<p> An unauthenticated SNMPv3 user can be created using the command</p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] AGENT create USER</dl>
<p> This constructs an (inactive) entry in the usmUserTable, with no authentication or privacy settings. In principle, this user should be useable for &#8216;noAuthNoPriv&#8217; requests, but in practise the Net-SNMP agent will not allow such an entry to be made active. The user can be created via the createAndWait operation instead by using the -Ca flag. This will prevent the user from being marked as active in any agent until explicitly activated later via the activate command. </p>
<p> In order to activate this entry, it is necessary to &quot;clone&quot; an existing user, using the command</p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] AGENT cloneFrom USER CLONEFROM-USER</dl>
<p> The USER entry then inherits the same authentication and privacy settings (including pass phrases) as the CLONEFROM user. </p>
<p> These two steps can be combined into one, by using the command</p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] AGENT create USER CLONEFROM-USER </p>
</dl>
<p> The two forms of the <code>create</code> sub-command require that the user being created does not already exist. The <code>cloneFrom</code> sub-command requires that the user being cloned to <i>does</i> already exist. </p>
<p> Cloning is the only way to specify which authentication and privacy protocols to use for a given user, and it is only possible to do this once. Subsequent attempts to reclone onto the same user will appear to succeed, but will be silently ignored. This (somewhat unexpected) behaviour is mandated by the SNMPv3 USM specifications (RFC 3414). To change the authentication and privacy settings for a given user, it is necessary to delete and recreate the user entry. This is <i>not</i> necessary for simply changing the pass phrases (see below). This means that the agent must be initialized with at least one user for each combination of authentication and privacy protocols. See the <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> manual page for details of the <code>createUser</code> configuration directive. </p>
<h2>DELETING USERS</h2>
<p> A user can be deleted from the usmUserTable using the command</p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] AGENT delete USER </p>
</dl>
<h2>CHANGING PASS PHRASES</h2>
<p> User profiles contain private keys that are never transmitted over the wire in clear text (regardless of whether the administration requests are encrypted or not). To change the secret key for a user, it is necessary to specify the user&#8217;s old passphrase as well as the new one. This uses the command</p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] [-Ca] [-Cx] AGENT passwd OLD-PASSPHRASE NEW-PASSPHRASE [USER] </p>
</dl>
<p> After cloning a new user entry from the appropriate template, you should immediately change the new user&#8217;s passphrase. </p>
<p> If USER is not specified, this command will change the passphrase of the (SNMPv3) user issuing the command. If the -Ca or -Cx options are specified, then only the authentication or privacy keys are changed. If these options are not specified, then both the authentication and privacy keys are changed. </p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] [-Ca] [-Cx] AGENT changekey [USER] </p>
</dl>
<p> This command changes the key in a perfect-forward-secrecy compliant way through a diffie-helman exchange. The remote agent must support the SNMP-USM-DH-OBJECTS-MIB for this command to work. The resulting keys are printed to the console and may be then set in future command invocations using the &#8211;defAuthLocalizedKey and &#8211;defPrivLocalizedKey options or in your snmp.conf file using the defAuthLocalizedKey and defPrivLocalizedKey keywords. </p>
<p> Note that since these keys are randomly generated based on a diffie helman exchange, they are no longer derived from a more easily typed password. They are, however, much more secure. </p>
<p> To change from a localized key back to a password, the following variant of the <code>passwd</code> sub-command is used: </p>
<dl>
<dt>
<dd> <code>snmpusm</code> [COMMON OPTIONS] &lt;-Ca | -Cx&gt; -Ck AGENT passwd OLD-KEY-OR-PASSPHRASE NEW-KEY-OR-PASSPHRASE [USER] </p>
</dl>
<p> Either the -Ca or the -Cx option must be specified. The OLD-KEY-OR-PASSPHRASE and/or NEW-KEY-OR-PASSPHRASE arguments can either be a passphrase or a localized key starting with &quot;0x&quot;, e.g. as printed out by the <code>changekey</code> sub-command. </p>
<p> Note that <code>snmpusm</code> REQUIRES an argument specifying the agent to query as described in the .I <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) manual page.</p>
<h2>EXAMPLES</h2>
<p> Let&#8217;s assume for our examples that the following VACM and USM configurations lines were in the snmpd.conf file for a Net-SNMP agent. These lines set up a default user called &quot;initial&quot; with the authentication passphrase &quot;setup_passphrase&quot; so that we can perform the initial setup of an agent: </p>
<dl>
<dt>
<dd>
<pre>
# VACM configuration entries
rwuser initial
# lets add the new user we'll create too:
rwuser wes
# USM configuration entries
createUser initial MD5 setup_passphrase DES
</pre>
</dl>
<p> Note: the &quot;initial&quot; user&#8217;s setup should be removed after creating a real user that you grant administrative privileges to (like the user &quot;wes&quot; we&#8217;ll be creating in this example. </p>
<p> Note: passphrases must be 8 characters <i>minimum</i> in length.</p>
<h3>Create a new user</h3>
<p> snmpusm -v3 -u initial -n &quot;&quot; -l authNoPriv -a MD5 -A setup_passphrase localhost create wes initial</p>
<dl>
<dt>
<dd> Creates a new user, here named &quot;wes&quot; using the user &quot;initial&quot; to do it. &quot;wes&quot; is cloned from &quot;initial&quot; in the process, so he inherits that user&#8217;s passphrase (&quot;setup_passphrase&quot;).</dl>
<h3>Change the user&#8217;s passphrase</h3>
<p> snmpusm -v 3 -u wes -n &quot;&quot; -l authNoPriv -a MD5 -A setup_passphrase localhost passwd setup_passphrase new_passphrase</p>
<dl>
<dt>
<dd> After creating the user &quot;wes&quot; with the same passphrase as the &quot;initial&quot; user, we need to change his passphrase for him. The above command changes it from &quot;setup_passphrase&quot;, which was inherited from the initial user, to &quot;new_passphrase&quot;.</dl>
<h3>Test the new user</h3>
<p> snmpget -v 3 -u wes -n &quot;&quot; -l authNoPriv -a MD5 -A new_passphrase localhost sysUpTime.0</p>
<dl>
<dt>
<dd> If the above commands were successful, this command should have properly performed an authenticated SNMPv3 GET request to the agent.</dl>
<p> Now, go remove the vacm &quot;group&quot; snmpd.conf entry for the &quot;initial&quot; user and you have a valid user &#8216;wes&#8217; that you can use for future transactions instead of initial. </p>
<h2>WARNING</h2>
<p> Manipulating the usmUserTable using this command can <i>only</i> be done using SNMPv3. This command will not work with the community-based versions, even if they have write access to the table. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), RFC 3414 </p>
<h2>Index</h2>
