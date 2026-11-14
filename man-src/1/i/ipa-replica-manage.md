---
title: "ipa-replica-manage(1)"
name: "ipa-replica-manage"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-replica-manage/"
description: "ipa-replica-manage – Manage an IPA replica"
---

<h2>NAME</h2>
<p> ipa-replica-manage &#8211; Manage an IPA replica</p>
<h2>SYNOPSIS</h2>
<p> ipa-replica-manage [<i>OPTION</i>]&#8230; [COMMAND]</p>
<h2>DESCRIPTION</h2>
<p> Manages the replication agreements of an IPA server. </p>
<p> To manage IPA replication agreements in a domain at domain level 1, use IPA CLI or Web UI, see `ipa help topology` for additional information. </p>
<p> The available commands are:</p>
<dl>
<dt><code>connect</code> [SERVER_A] &lt;SERVER_B&gt;</p>
<dd> &#8211; Adds a new replication agreement between SERVER_A/localhost and SERVER_B. At domain level 1 applicable only for winsync agreements.</p>
<dt><code>disconnect</code> [SERVER_A] &lt;SERVER_B&gt;</p>
<dd> &#8211; Removes a replication agreement between SERVER_A/localhost and SERVER_B. At domain level 1 applicable only for winsync agreements.</p>
<dt><code>del</code> &lt;SERVER&gt;</p>
<dd> &#8211; Removes all replication agreements and data about SERVER. At domain level 1 it removes data and agreements for both suffixes &#8211; domain and ca.</p>
<dt><code>list</code> [SERVER]</p>
<dd> &#8211; Lists all the servers or the list of agreements of SERVER</p>
<dt><code>re-initialize</code></p>
<dd> &#8211; Forces a full re-initialization of the IPA server retrieving data from the server specified with the &#8211;from option</p>
<dt><code>force-sync</code></p>
<dd> &#8211; Immediately flush any data to be replicated from a server specified with the &#8211;from option</p>
<dt><code>list-ruv</code></p>
<dd> &#8211; List the replication IDs on this server.</p>
<dt><code>clean-ruv</code> [REPLICATION_ID]</p>
<dd> &#8211; Run the CLEANALLRUV task to remove a replication ID.</p>
<dt><code>clean-dangling-ruv</code></p>
<dd> &#8211; Cleans all RUVs and CS-RUVs that are left in the system from uninstalled replicas.</p>
<dt><code>abort-clean-ruv</code> [REPLICATION_ID]</p>
<dd> &#8211; Abort a running CLEANALLRUV task. With &#8211;force option the task does not wait for all the replica servers to have been sent the abort task, or be online, before completing.</p>
<dt><code>list-clean-ruv</code></p>
<dd> &#8211; List all running CLEANALLRUV and abort CLEANALLRUV tasks.</p>
<dt><code>dnarange-show [SERVER]</code></p>
<dd> &#8211; List the DNA ranges</p>
<dt><code>dnarange-set SERVER START-END</code></p>
<dd> &#8211; Set the DNA range on a master</p>
<dt><code>dnanextrange-show [SERVER]</code></p>
<dd> &#8211; List the next DNA ranges</p>
<dt><code>dnanextrange-set SERVER START-END</code></p>
<dd> &#8211; Set the DNA next range on a master</p>
<dt>The connect and disconnect options are used to manage the replication topology. When a replica is created it is only connected with the master that created it. The connect option may be used to connect it to other existing replicas.</p>
<dd>
<dt>The disconnect option cannot be used to remove the last link of a replica. To remove a replica from the topology use the del option.</p>
<dd>
<dt>If a replica is deleted and then re-added within a short time-frame then the 389-ds instance on the master that created it should be restarted before re-installing the replica. The master will have the old service principals cached which will cause replication to fail.</p>
<dd>
<dt>Each IPA master server has a unique replication ID. This ID is used by 389-ds-base when storing information about replication status. The output consists of the masters and their respective replication ID. See <code>clean-ruv</code></p>
<dd>
<dt>When a master is removed, all other masters need to remove its replication ID from the list of masters. Normally this occurs automatically when a master is deleted with ipa-replica-manage. If one or more masters was down or unreachable when ipa-replica-manage was executed then this replica ID may still exist. The clean-ruv command may be used to clean up an unused replication ID.</p>
<dd>
<dt><code>NOTE</code>: clean-ruv is <code>VERY DANGEROUS</code>. Execution against the wrong replication ID can result in inconsistent data on that master. The master should be re-initialized from another if this happens.</p>
<dd>
<dt>The replication topology is examined when a master is deleted and will attempt to prevent a master from being orphaned. For example, if your topology is A &lt;-&gt; B &lt;-&gt; C and you attempt to delete master B it will fail because that would leave masters and A and C orphaned.</p>
<dd>
<dt>The list of masters is stored in cn=masters,cn=ipa,cn=etc,dc=example,dc=com. This should be cleaned up automatically when a master is deleted. If it occurs that you have deleted the master and all the agreements but these entries still exist then you will not be able to re-install IPA on it, the installation will fail with:</p>
<dd>
<dt>An IPA master host cannot be deleted or disabled using standard commands (host-del, for example).</p>
<dd>
<dt>An orphaned master may be cleaned up using the del directive with the &#8211;cleanup option. This will remove the entries from cn=masters,cn=ipa,cn=etc that otherwise prevent host-del from working, its dna profile, s4u2proxy configuration, service principals and remove it from the default DUA profile defaultServerList.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code> <i>HOST</i>, <code>&#8211;host</code>=<i>HOST</i></p>
<dd> The IPA server to manage. The default is the machine on which the command is run Not honoured by the re-initialize command.</p>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i></p>
<dd> The Directory Manager password to use for authentication</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Provide additional information</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Ignore some types of errors, don&#8217;t prompt when deleting a master</p>
<dt><code>-c</code>, <code>&#8211;cleanup</code></p>
<dd> When deleting a master with the &#8211;force flag, remove leftover references to an already deleted master.</p>
<dt><code>&#8211;no-lookup</code></p>
<dd> Do not perform DNS lookup checks.</p>
<dt><code>&#8211;binddn</code>=<i>ADMIN_DN</i></p>
<dd> Bind DN to use with remote server (default is cn=Directory Manager) &#8211; Be careful to quote this value on the command line</p>
<dt><code>&#8211;bindpw</code>=<i>ADMIN_PWD</i></p>
<dd> Password for Bind DN to use with remote server (default is the DM_PASSWORD above)</p>
<dt><code>&#8211;winsync</code></p>
<dd> Specifies to create/use a Windows Sync Agreement</p>
<dt><code>&#8211;cacert</code>=<i>/path/to/cacertfile</i></p>
<dd> Full path and filename of CA certificate to use with TLS/SSL to the remote server &#8211; this CA certificate will be installed in the directory server&#8217;s certificate database</p>
<dt><code>&#8211;win-subtree</code>=<i>cn=Users,dc=example,dc=com</i></p>
<dd> DN of Windows subtree containing the users you want to sync (default cn=Users,&lt;domain suffix&gt; &#8211; this is typically what Windows AD uses as the default value) &#8211; Be careful to quote this value on the command line</p>
<dt><code>&#8211;passsync</code>=<i>PASSSYNC_PWD</i></p>
<dd> Password for the IPA system user used by the Windows PassSync plugin to synchronize passwords. Required when using &#8211;winsync. This does not mean you have to use the PassSync service.</p>
<dt><code>&#8211;from</code>=<i>SERVER</i></p>
<dd> The server to pull the data from, used by the re-initialize and force-sync commands.</p>
<dt></dl>
<h2>RANGES</h2>
<dd> IPA uses the 389-ds Distributed Numeric Assignment (DNA) Plugin to allocate POSIX ids for users and groups. A range is created when IPA is installed and half the range is assigned to the first IPA master for the purposes of allocation.</p>
<dl>
<dt>New IPA masters do not automatically get a DNA range assignment. A range assignment is done only when a user or POSIX group is added on that master.</p>
<dd>
<dt>The DNA plugin also supports an &quot;on-deck&quot; or next range configuration. When the primary range is exhaused, rather than going to another master to ask for more, it will use its on-deck range if one is defined. Each master can have only one range and one on-deck range defined.</p>
<dd>
<dt>When a master is removed an attempt is made to save its DNA range(s) onto another master in its on-deck range. IPA will not attempt to extend or merge ranges. If there are no available on-deck range slots then this is reported to the user. The range is effectively lost unless it is manually merged into the range of another master.</p>
<dd>
<dt>The DNA range and on-deck (next) values can be managed using the dnarange-set and dnanextrange-set commands. The rules for managing these ranges are:</p>
<dd> &#8211; The range must be completely contained within a local range as defined by the ipa idrange command. </p>
<p> &#8211; The range cannot overlap the DNA range or on-deck range on another IPA master. </p>
<p> &#8211; The range cannot overlap the ID range of an AD Trust. </p>
<p> &#8211; The primary DNA range cannot be removed. </p>
<p> &#8211; An on-deck range range can be removed by setting it to 0-0. The assumption is that the range will be manually moved or merged elsewhere.</p>
<dt>The range and next range of a specific master can be displayed by passing the FQDN of that master to the dnarange-show or dnanextrange-show command.</p>
<dd>
<dt>Performing range changes as a delegated administrator (e.g. not using the Directory Manager password) requires additional 389-ds ACIs. These are installed in upgraded masters but not existing ones. The changs are made in cn=config which is not replicated. The result is that DNA ranges cannot be managed on non-upgraded masters as a delegated administrator.</p>
<dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>List all masters:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage list<br />
&nbsp;<wbr>srv1.example.com: master<br />
&nbsp;<wbr>srv2.example.com: master<br />
&nbsp;<wbr>srv3.example.com: master<br />
&nbsp;<wbr>srv4.example.com: master</p>
<dt>List a server&#8217;s replication agreements.</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage list srv1.example.com<br />
&nbsp;<wbr>srv2.example.com: replica<br />
&nbsp;<wbr>srv3.example.com: replica</p>
<dt>Re-initialize a replica:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage re-initialize &#8211;from srv2.example.com </p>
<p> This will re-initialize the data on the server where you execute the command, retrieving the data from the srv2.example.com replica</p>
<dt>Add a new replication agreement:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage connect srv2.example.com srv4.example.com</p>
<dt>Remove an existing replication agreement:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage disconnect srv1.example.com srv3.example.com</p>
<dt>Completely remove a replica:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage del srv4.example.com</p>
<dt>Using connect/disconnect you can manage the replication topology.</p>
<dd>
<dt>List the replication IDs in use:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage list-ruv<br />
&nbsp;<wbr>Replica Update Vectors:<br />
&nbsp;<wbr>&nbsp;<wbr>srv1.example.com:389: 7<br />
&nbsp;<wbr>&nbsp;<wbr>srv2.example.com:389: 4<br />
&nbsp;<wbr>Certificate Server Replica Update Vectors:<br />
&nbsp;<wbr>&nbsp;<wbr>srv1.example.com:389: 9</p>
<dt>Remove references to an orphaned and deleted master:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage del &#8211;force &#8211;cleanup master.example.com</dl>
<h2>WINSYNC</h2>
<p> Creating a Windows AD Synchronization agreement is similar to creating an IPA replication agreement, there are just a couple of extra steps. </p>
<p> A special user entry is created for the PassSync service. The DN of this entry is uid=passsync,cn=sysaccounts,cn=etc,&lt;basedn&gt;. You are not required to use PassSync to use a Windows synchronization agreement but setting a password for the user is required. </p>
<p> The following examples use the AD administrator account as the synchronization user. This is not mandatory but the user must have read-access to the subtree. </p>
<dl>
<dt>1. Transfer the base64-encoded Windows AD CA Certificate to your IPA Server</p>
<dd>
<dt>2. Remove any existing kerberos credentials</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>kdestroy</p>
<dt>3. Add the winsync replication agreement</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage connect &#8211;winsync &#8211;passsync=&lt;bindpwd_for_syncuser_that will_be_used_for_agreement&gt;&nbsp;<wbr>&#8211;cacert=/path/to/adscacert/WIN-CA.cer &#8211;binddn&nbsp;<wbr>&quot;cn=administrator,cn=users,dc=ad,dc=example,dc=com&quot;&nbsp;<wbr>&#8211;bindpw&nbsp;<wbr>&lt;ads_administrator_password&gt;&nbsp;<wbr>-v&nbsp;<wbr>&lt;adserver.fqdn&gt;</p>
<dt>You will be prompted to supply the Directory Manager&#8217;s password.</p>
<dd>
<dt>Create a winsync replication agreement:</p>
<dd>
<p>&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage connect &#8211;winsync &#8211;passsync=MySecret &#8211;cacert=/root/WIN-CA.cer &#8211;binddn &quot;cn=administrator,cn=users,dc=ad,dc=example,dc=com&quot; &#8211;bindpw MySecret -v windows.ad.example.com </p>
<dt>Remove a winsync replication agreement:</p>
<dd>
&nbsp;<wbr>#&nbsp;<wbr>ipa-replica-manage disconnect windows.ad.example.com</dl>
<h2>PASSSYNC</h2>
<p> PassSync is a Windows service that runs on AD Domain Controllers to intercept password changes. It sends these password changes to the IPA LDAP server over TLS. These password changes bypass normal IPA password policy settings and the password is not set to immediately expire. This is because by the time IPA receives the password change it has already been accepted by AD so it is too late to reject it.</p>
<dl>
<dt>IPA maintains a list of DNs that are exempt from password policy. A special user is added automatically when a winsync replication agreement is created. The DN of this user is added to the exemption list stored in passSyncManagersDNs in the entry cn=ipa_pwd_extop,cn=plugins,cn=config.</p>
<dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
