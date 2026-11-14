---
title: "zarafa-admin(1)"
name: "zarafa-admin"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-admin/"
description: "zarafa-admin – Manages Zarafa users and stores."
---

<h2 class="name">NAME</h2>
<p> zarafa-admin &#8211; Manages Zarafa users and stores. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-admin</code> <i>ACTION</i> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>This tool can be used to create the public store and to add, update and remove users from Zarafa. The Zarafa server must be running for <code>zarafa-admin</code> to work. </p>
<p> If no action is given, a listing of the possible parameters is printed. When invalid actions or not enough options for an action are given, an error message is printed. </p>
<p> When using LDAP as the users source, create, modify and delete actions are done in the LDAP tree and not using the zarafa-admin tool. Please see the <code>EXTERNAL USERS</code>() section for more information.</p>
<h2>ACTIONS</h2>
<p> zarafa-admin needs an action command with the appropriate options. Valid actions are: </p>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Create a public store. No other options are needed. Only one public store can be created. Successive calls will fail.</dl>
<p> <code>-c</code> <i>username</i></p>
<dl>
<dt>
<dd> Create a new user, <i>-p</i>, <i>-f</i> and <i>-e</i> options are required, <i>-a</i> and <i>-n</i> parameters are optional. To set a password using a password prompt, use the <i>-P</i> option in stead of <i>-p</i>.</dl>
<p> <code>-d</code> <i>username</i></p>
<dl>
<dt>
<dd> Delete a user. No other options are needed. The deleted store of the user will be marked as orphan store and can be restored with <i>&#8211;hook-store</i></dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dt>
<dd> Update user information. Valid parameters are: <i>[-p|-P]</i>, <i>-f</i>, <i>-e</i>, <i>-a</i>, <i>-n</i> and <i>-U</i> to update user information. Use: <i>&#8211;qo</i>, <i>&#8211;qw</i>, <i>&#8211;qs</i> or <i>&#8211;qh</i> to set quota levels. Use 0 with quota options to set as &#8216;unlimited&#8217;. </p>
<p> <i>&#8211;enable-feature</i> and <i>&#8211;disable-feature</i> to enable or disable specific features for users. </p>
<p> This action is also required for all options to control the autoaccept of meeting requests. See the <i>&#8211;mr-accept</i>, <i>&#8211;mr-decline-conflict</i> and <i>&#8211;mr-decline-recurring</i> options.</dl>
<p> <code>-g</code> <i>groupname</i></p>
<dl>
<dt>
<dd> Create a new group. Valid parameters are: <i>-e</i></dl>
<p> <code>&#8211;update-group</code> <i>groupname</i></p>
<dl>
<dt>
<dd> Update group information. Valid parameters are: <i>-e</i></dl>
<p> <code>-G</code> <i>groupname</i></p>
<dl>
<dt>
<dd> Delete a group. No other options are needed.</dl>
<p> <code>-b</code> <i>username</i></p>
<dl>
<dt>
<dd> Add a user to a group. Use the <i>-i</i> to set the groupname.</dl>
<p> <code>-B</code> <i>username</i></p>
<dl>
<dt>
<dd> Remove a user from a group. Use the <i>-i</i> to set the groupname.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> List all users available in Zarafa. When using an external user source, this action will implicitly synchronize all users in the external source, creating, updating and/or removing users and stores.</dl>
<p> <code>-L</code></p>
<dl>
<dt>
<dd> List all groups available in Zarafa. When using an external user source, this action will implicitly synchronize all groups in the external source, creating updating and/or removing groups and memberships.</dl>
<p> <code>&#8211;list-companies</code></p>
<dl>
<dt>
<dd> List all tenans available in Zarafa. When using an external user source, this action will implicitly synchronize all tenants in the external source, creating updating and/or removing companies. </p>
<p> This option is only available in multi-tenancy Zarafa</dl>
<p> <code>&#8211;details</code> <i>name</i></p>
<dl>
<dt>
<dd> Show all the details of a user, showing the fullname, e-mailaddress, active state, administator state, group memberships and quota settings. Optionally use <i>&#8211;type</i> to indicate for what kind of object the details are being requested. </p>
<p> Note: This function does not synchronize with the external user plugin. Thus changes from e.g. LDAP will not be set during this function.</dl>
<p> <code>&#8211;type</code> <i>type</i></p>
<dl>
<dt>
<dd> Additional argument for <i>&#8211;details</i>. The argument with this option indicates for what type of object the details are being requested. Allowed values are <i>&#8216;user&#8217;</i>, <i>&#8216;group&#8217;</i> or <i>&#8216;company&#8217;</i> When this option is not used, it defaults to <i>&#8216;user&#8217;</i></dl>
<p> <code>&#8211;create-company</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Create a new tenant space. </p>
<p> Use: <i>&#8211;qo</i>, <i>&#8211;qw</i>, <i>&#8211;qs</i>, <i>&#8211;qh</i> to set quota levels for the tenant. </p>
<p> Use: <i>&#8211;udqo</i>, <i>&#8211;udqw</i>, <i>&#8211;udqs</i>, <i>&#8211;udqh</i> to set the default quota levels for the users inside the tenant. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;update-company</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Update an existing tenant space. </p>
<p> Use: <i>&#8211;qo</i>, <i>&#8211;qw</i>, <i>&#8211;qs</i>, <i>&#8211;qh</i> to set quota levels for the tenant. </p>
<p> Use: <i>&#8211;udqo</i>, <i>&#8211;udqw</i>, <i>&#8211;udqs</i>, <i>&#8211;udqh</i> to set the default quota levels for the users inside the . </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;delete-company</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Delete company space. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;set-system-admin</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Set system administrator for the tenant specified by <i>-I</i>. </p>
<p> Please be aware that this option does not provide the user with administrator privileges. The system administrator is considered the main contact person for a company, it will for example be used as default sender for quota warning emails. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;add-to-viewlist</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Add tenant <i>&#8216;companyname&#8217;</i> to remote-view list of company specified by <i>-I</i>. After this command the <i>&#8216;companyname&#8217;</i> is capable of viewing all members of the company specified by <i>-I</i>. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;del-from-viewlist</code> <i>companyname</i></p>
<dl>
<dt>
<dd> Delete company <i>&#8216;companyname&#8217;</i> from remote-view list of tenant specified by <i>-I</i>. After this command the <i>&#8216;companyname&#8217;</i> is no longer capable of viewing all members of the tenant specified by <i>-I</i>. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;list-view</code></p>
<dl>
<dt>
<dd> List all tenants in the remote-view list of the tenant specified by <i>-I</i>. The tenants in this list are able to view all members of the specified tenant in their Address Book. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;add-to-adminlist</code> <i>username</i></p>
<dl>
<dt>
<dd> Add user <i>&#8216;username&#8217;</i> to remote-admin list of tenant specified by <i>-I</i>. This is the administrator list for remote administrators, as such it only manages administrators from a different tenant. Users who should be administrator over their own tenant are managed by updating (<code>-u</code>) the user and specifying the <code>-a</code> argument. </p>
<p> Users can only be administrator over a different company when they have also been granted view privileges, can be granted by using the <code>&#8211;add-to-viewlist</code>. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;del-from-adminlist</code> <i>username</i></p>
<dl>
<dt>
<dd> Delete user <i>&#8216;username&#8217;</i> from remote-admin list of company specified by <i>-I</i>. This is the administrator list for remote administrators, as such it only manages administrators from a different tenant. Users who should be administrator over their own tenant are managed by updating (<code>-u</code>) the user and specifying the <code>-a</code> argument. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;list-admin</code></p>
<dl>
<dt>
<dd> List all users in the remote-admin list of the tenant specified by <i>-I</i>. This is the administrator list for remote administrators, as such it only manages administrators from a different tenant. Users who should be administrator over their own tenant are managed by updating (<code>-u</code>) the user and specifying the <code>-a</code> argument. </p>
<p> Users can only be administrator over a different tenant when they have also been granted view privileges, can be granted by using the <code>&#8211;add-to-viewlist</code>. </p>
<p> This option is only available in multi-tenancy Zarafa.</dl>
<p> <code>&#8211;add-userquota-recipient</code> <i>user</i></p>
<dl>
<dt>
<dd> Add <i>&#8216;user&#8217;</i> as recipient to userquota warning emails. You can optionally use <i>-I</i> to set the tenant space to apply the recipient action on.</dl>
<p> <code>&#8211;del-userquota-recipient</code> <i>user</i></p>
<dl>
<dt>
<dd> Delete <i>&#8216;user&#8217;</i> as recipient to userquota warning emails. You can optionally use <i>-I</i> to set the tenant space to apply the recipient action on.</dl>
<p> <code>&#8211;list-userquota-recipients</code></p>
<dl>
<dt>
<dd> List all additional recipients for a userquota warning email. Use <i>-I</i> to request the recipient list for a particular tenant space.</dl>
<p> <code>&#8211;add-companyquota-recipient</code> <i>user</i></p>
<dl>
<dt>
<dd> Add <i>&#8216;user&#8217;</i> as recipient to tenant quota warning emails. You can optionally use <i>-I</i> to set the tenant space to apply the recipient action on.</dl>
<p> <code>&#8211;del-companyquota-recipient</code> <i>user</i></p>
<dl>
<dt>
<dd> Delete <i>&#8216;user&#8217;</i> as recipient to tenant quota warning emails. You can optionally use <i>-I</i> to set the tenant space to apply the recipient action on.</dl>
<p> <code>&#8211;list-companyquota-recipients</code></p>
<dl>
<dt>
<dd> List all additional recipients for a tenant quota warning email. Use <i>-I</i> to request the recipient list for a particular tenant space</dl>
<p> <code>&#8211;list-sendas</code> <i>user</i></p>
<dl>
<dt>
<dd> List all users who are able to directly send an email as <i>user</i>. This has been set in the LDAP server, or with the <code>&#8211;add-sendas</code> command for Unix and DB plugins. Optionally use <i>&#8211;type</i> to indicate for what kind of object the sendas details are being requested.</dl>
<p> <code>&#8211;clear-cache</code></p>
<dl>
<dt>
<dd> Clears the server&#8217;s caches. All data cached inside the zarafa-server is cleared. Although this can never cause any data loss, it can affect the performance of your server, since any data requested after the cache is cleared needs to be re-requested from the database or LDAP server. Normally this option is never needed; it is mostly used as a diagnostics tool. </p>
<p> Optionally use <i>&#8211;clear-cache=</i> to specify a set of purge options. The following options can be used:</p>
<dl>
<dt>
<dd> 0x0000 Release no longer used memory back to the kernel</dl>
<dl>
<dt>
<dd> 0x0001 Purge the quota cache</dl>
<dl>
<dt>
<dd> 0x0002 Purge the quota default cache</dl>
<dl>
<dt>
<dd> 0x0004 Purge the object cache</dl>
<dl>
<dt>
<dd> 0x0008 Purge the store cache</dl>
<dl>
<dt>
<dd> 0x0010 Purge the ACL cache</dl>
<dl>
<dt>
<dd> 0x0020 Purge the cell cache</dl>
<dl>
<dt>
<dd> 0x0040 Purge the index1 cache</dl>
<dl>
<dt>
<dd> 0x0080 Purge the index2 cache</dl>
<dl>
<dt>
<dd> 0x0100 Purge the indexproperty cache</dl>
<dl>
<dt>
<dd> 0x0200 Purge the user object cache</dl>
<dl>
<dt>
<dd> 0x0400 Purge the externid cache</dl>
<dl>
<dt>
<dd> 0x0800 Purge the userdetails cache</dl>
<dl>
<dt>
<dd> 0x1000 Purge the server cache</dl>
</dl>
<p> <code>&#8211;purge-softdelete</code> <i>days</i></p>
<dl>
<dt>
<dd> Starts a softdelete purge on the server, removing all soft-deleted items which have been deleted <i>days</i> days ago, or earlier</dl>
<p> <code>&#8211;purge-deferred</code></p>
<dl>
<dt>
<dd> The server has an optimization in which changes to the tproperties table are not writted directly, but delayed for a more efficient write at a later time. The server auto-purges these regularly. This command allows you to purge all changes pending. It may be useful to run this during low I/O load of your server (eg at night).</dl>
<p> <code>&#8211;list-orphans</code></p>
<dl>
<dt>
<dd> When a user is removed, the store becomes orphaned. This option shows a list of stores that are not hooked to a user. You can use the <code>&#8211;remove-store</code> and <code>&#8211;hook-store</code> from this list.</dl>
<p> <code>&#8211;hook-store</code> <i>store-guid</i></p>
<dl>
<dt>
<dd> You can hook an orphaned store to an existing user, so you may access the store again. Use the <code>-u</code><i>username</i> to specify the user to hook the store to. </p>
<p> You can copy an orphaned store to the public store. Use the <code>&#8211;copyto-public</code> to copy the store to the public folder named &#8216;Admin/deleted stores&#8217;. This folder is then only visible for users with Zarafa admin privileges. </p>
<p> To hook a public store, use <code>&#8211;type</code> group/company to influence the name type in the -u switch. </p>
<p> To hook an archive store, use <code>&#8211;type</code><i>archive</i>.</dl>
<p> <code>&#8211;remove-store</code> <i>store-guid</i></p>
<dl>
<dt>
<dd> Use this action to remove the store from the database. The store is actually just marked as deleted, so the softdelete system can remove the store from the database.</dl>
<p> <code>&#8211;create-store</code> <i>username</i></p>
<dl>
<dt>
<dd> This action will create a store for a newly created user, and is normally called through the createuser script. If the <code>&#8211;list-orphans</code> action listed users without a store, you can create a new store for those users with this command.</dl>
<p> <code>&#8211;unhook-store</code> <i>username</i></p>
<dl>
<dt>
<dd> You can unhook a store from a user, so you can remove the store and create a new one. </p>
<p> To unhook a public store, use the <code>&#8211;type</code> group/company option to influence the name type in the <i>username</i> argument. Use a companyname with type company or &#8216;Everyone&#8217; with type group to unhook the public. </p>
<p> To unhook an archive store, use <code>&#8211;type</code><i>archive</i>.</dl>
<p> <code>&#8211;force-resync</code> <i>usernames</i></p>
<dl>
<dt>
<dd> You can force a resync of cached profiles when the data is out of sync. One or more usernames can be specified. If no usernames are given, all offline profiles can be resynced.</dl>
<p> <code>&#8211;reset-folder-count</code> <i>username</i></p>
<dl>
<dt>
<dd> Reset the counters on all folders in <i>username</i>&#8216;s store.</dl>
<p> <code>&#8211;user-count</code></p>
<dl>
<dt>
<dd> Shows an overview of user counts per type of user, and how much are allowed by your current license.</dl>
<h2>OPTIONS</h2>
<p> The options used by actions are as follows: </p>
<p> <code>-U</code> <i>&#8216;new username&#8217;</i></p>
<dl>
<dt>
<dd> Use this parameter to rename a user. This option is only valid with the <i>-u</i> update action.</dl>
<p> <code>-p</code> <i>password</i></p>
<dl>
<dt>
<dd> Set password for a user. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> Set password for a user. The password can be entered on the password prompt. The password will not be shown. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>-f</code> <i>&#8216;full name&#8217;</i></p>
<dl>
<dt>
<dd> Specify full user name. Use single quotes around the name to pass it as a single parameter. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>-e</code> <i>&#8217;email address&#8217;</i></p>
<dl>
<dt>
<dd> Specify the email address. This address will be used to set the &#8216;From&#8217; email address in outgoing email messages. Use single quotes around the name to pass it as a single parameter. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>-a</code> <i>[yes|y|1|2 / no|n|0]</i></p>
<dl>
<dt>
<dd> Set the user as administrator by passing &#8216;yes&#8217;. When passing &#8216;no&#8217;, administrator rights will be revoked from the user. This option is only valid with the <i>-c</i> create or <i>-u</i> update action. </p>
<p> It is also possible to pass 2 as administrator level, this will make the user a system administrator who can create/modify/delete companies.</dl>
<p> <code>-n</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> Specify a non-active user. This user cannot login, but email can be delivered, and the store can be opened by users with correct rights.</dl>
<p> <code>&#8211;qo</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> Override the default server quota settings for this user. User specific quota levels will used. The default value of this option is &#8216;no&#8217;, always using server quota levels. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>&#8211;qw</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the warning quota level for a user. The user may receive a warning email when this level is reached. See <code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1) for warning emails. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>&#8211;qs</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the soft quota level for a user. The user will be unable to receive new emails, bouncing the email back to the sender. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>&#8211;qh</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the hard quota level for a user. The user will be unable to receive and create new emails. This option is only valid with the <i>-c</i> create or <i>-u</i> update action.</dl>
<p> <code>&#8211;udqo</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> Override the default server quota settings for all user within the specified tenant. default value of this option is &#8216;no&#8217;, always using server quota levels.</dl>
<p> <code>&#8211;udqw</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the warning quota level for all users within the specified tenant. The user may receive a warning email when this level is reached. See <code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1) for warning emails.</dl>
<p> <code>&#8211;udqs</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the soft quota level for all users within the specified tenant. The user will be unable to receive new emails, bouncing the email back to the sender. See <code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1) for warning emails.</dl>
<p> <code>&#8211;udqh</code> <i>value in Mb</i></p>
<dl>
<dt>
<dd> Set the hard quota level for all users within the specified tenant. The user will be unable to receive and create new emails. See <code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1) for warning emails.</dl>
<p> <code>-i</code> <i>groupname</i></p>
<dl>
<dt>
<dd> This sets the groupname for <i>-b</i> and <i>-B</i> actions.</dl>
<p> <code>-I</code> <i>companyname</i></p>
<dl>
<dt>
<dd> This sets the companyname for all user, group and tenant commands. This option is only available for multi-tenancy Zarafa.</dl>
<p> <code>&#8211;mr-accept</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> Specified that meeting requests should automatically be accepted for a user. This means that when a meeting request is sent to this user when specified as being a &#8216;resource&#8217;, the request will directly be honoured and written to the calendar. This is a client-side action and this setting therefore does not affect actual meeting requests being delivered via zarafa-dagent. The user on which to operate is select using the <i>-u</i> switch.</dl>
<p> <code>&#8211;mr-decline-conflict</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> This option only has effect when &#8211;mr-accept=yes is in effect. When specifying &#8211;mr-decline-conflict, meeting requests that conflict with an existing meeting will be declined. The user on which to operate is select using the <i>-u</i> switch.</dl>
<p> <code>&#8211;mr-decline-recurring</code> <i>[yes|y|1 / no|n|0]</i></p>
<dl>
<dt>
<dd> This option only has effect when &#8211;mr-accept=yes is in effect. When specifying &#8211;mr-decline-recurring, meeting requests that are recurring will be declined. The user on which to operate is select using the <i>-u</i> switch.</dl>
<p> <code>&#8211;add-sendas</code> <i>sender</i></p>
<dl>
<dt>
<dd> Add user <i>sender</i> to the list of the senders you&#8217;re updating as a &#8216;send as&#8217; user. The <i>sender</i> can now send mails under the updated user&#8217;s name, unless the updated user sets the <i>sender</i> as a delegate. When the <i>sender</i> is a delegate, the mail will be sent with &#8216;On behalf of&#8217; markings in the email. This option is only valid with the <i>-u</i> and <i>&#8211;update-group </i> update action.</dl>
<p> <code>&#8211;del-sendas</code> <i>sender</i></p>
<dl>
<dt>
<dd> Remove user <i>sender</i> from the list of the senders you&#8217;re updating as a &#8216;send as&#8217; user. This option is only valid with the <i>-u</i> and <i>&#8211;update-group </i>update action.</dl>
<p> <code>&#8211;lang</code> <i>language</i></p>
<dl>
<dt>
<dd> Use <i>language</i> to create new stores; this means that folders in the new store will be in the language specified. Only valid in combination with &#8211;create-store. When this options in not specified, the system default will be selected according the LC_* and LANG environment variables, depending on your OS.</dl>
<p> Other options to control the connection to the zarafa-server are: </p>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa. This option can always be specified.</dl>
<p> <code>&#8211;node</code> <i>name</i></p>
<dl>
<dt>
<dd> Execute the command on cluster node <i>name</i>replaceable&gt;</dl>
<p> <code>&#8211;config</code> <i>file</i></p>
<dl>
<dt>
<dd> Use a configuration file. See the <code>CONFIG</code>() section for more information. </p>
<p> Default: <i>/etc/zarafa/admin.cfg</i></dl>
<h2>CONFIG</h2>
<p> Normally, no configuration file is used or required. If the file <i>/etc/zarafa/admin.cfg</i> exists, it is used as configuration file, but no error checking is performed. This way, you can use any config file from a zarafa program, eg. zarafa-spooler or zarafa-dagent, to load SSL settings. </p>
<p> The following options can be set in the configuation file: </p>
<p> <code>server_socket</code></p>
<dl>
<dt>
<dd> Unix socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>sslkey_file</code></p>
<dl>
<dt>
<dd> Use this file as key to logon to the server. This is only used when server_socket is set to an HTTPS transport. See the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual page on how to setup SSL keys. </p>
<p> Default: value not set.</dl>
<p> <code>sslkey_pass</code></p>
<dl>
<dt>
<dd> The password of the SSL key file that is set in sslkey_file. </p>
<p> Default: value not set.</dl>
<h2>EXAMPLES</h2>
<p> For creating a user: </p>
<p> <code>zarafa-admin</code><code>-c</code><i>loginname</i><code>-p</code><i>password</i><code>-f</code><i>&#8216;Firstname Lastname&#8217;</i><code>-e</code><i>f.lastname [at] tenant.com</i> </p>
<p> For creating a non-login store: </p>
<p> <code>zarafa-admin</code><code>-c</code><i>loginname</i><code>-p</code><i>password</i><code>-f</code><i>&#8216;Firstname Lastname&#8217;</i><code>-e</code><i>f.lastname [at] tenant.com</i><i>-n</i> 1 </p>
<p> For modifying the password and e-mail address: </p>
<p> <code>zarafa-admin</code><code>-u</code><i>loginname</i><code>-p</code><i>newpass</i><code>-e</code><i>fistname [at] tenant.com</i> </p>
<p> For deleting a user: </p>
<p> <code>zarafa-admin</code><code>-d</code><i>loginname</i> </p>
<p> For adding a user to a group: </p>
<p> <code>zarafa-admin</code><code>-b</code><i>loginname</i><code>-i</code><i>groupname</i> </p>
<p> For setting a specific quota level for a user. Warning level to 80 Mb, soft level to 90 Mb and hard level to 100 Mb: </p>
<p> <code>zarafa-admin</code><code>-u</code><i>loginname</i><code>&#8211;qo</code><i>yes</i><code>&#8211;qw</code><i>80</i><code>&#8211;qs</code><i>90</i><code>&#8211;qh</code><i>100</i> </p>
<p> For automatically accepting meeting requests for a user or resource: </p>
<p> <code>zarafa-admin</code><code>-u</code><i>loginname</i><code>&#8211;mr-accept</code><i>y</i><code>&#8211;mr-decline-conflict</code><i>y</i><code>&#8211;mr-decline-recurring</code><i>n</i></p>
<h2>EXTERNAL USERS</h2>
<p> When the users are located in an external database, and the Zarafa server is configured to use these users, a lot of commands from the zarafa-admin tool make no sense anymore. An example of an external database, and currently the only option, is an LDAP database. </p>
<p> The following actions can still be used, all other commands will be automatically triggered by changing the values in the LDAP server. </p>
<p> <code>-s</code>: create public store. </p>
<p> <code>-l</code>: list users known to Zarafa. </p>
<p> <code>-L</code>: list groups known to Zarafa. </p>
<p> <code>&#8211;details</code><i>username</i>: show user details. </p>
<p> <code>&#8211;sync</code>: trigger full synchonise for users and groups from the external source. </p>
<p> When the users change in the external source, the Zarafa server instantly synchronizes to these changes. There are two exceptions that need some extra attention, and these are when users are created or deleted. When a user is created, the <code>createuser_script</code> from the <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) will be started to create a store for a user. Likewise, when deleting a user, the <code>deleteuser_script</code> from the <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) will be started to delete a store from a user. The same is valid for creating and deleting a group and tenant, starting the <code>creategroup_script</code>/<code>createcompany_script</code> and <code>deletegroup_script</code>/<code>deletecompany_script</code> scripts respectively.</p>
<h2>DIAGNOSTICS</h2>
<p> Could not create user/store/public store. </p>
<p> When you get this error, make sure the Zarafa server and database server are running.</p>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) </p>
<h2>Index</h2>
