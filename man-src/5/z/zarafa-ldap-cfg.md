---
title: "zarafa-ldap-cfg(5)"
name: "zarafa-ldap-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-ldap-cfg/"
description: "zarafa-ldap.cfg – The Zarafa LDAP configuration file"
---

<p>zarafa-ldap.cfg &#8211; The Zarafa LDAP configuration file</p>
<h2>Synopsis</h2>
<p><code>ldap.cfg</code></p>
<h2>Description</h2>
<p>The ldap.cfg is a configuration file for LDAP user plugin. All options to correctly retrieve user and group information can be set here.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<p> <code>propmap</code></p>
<dl>
<dd>Propmap delivers the capabilities to map additional attributes to addressbook properties (e.g. firstname, lastname, telephonenumber). </p>
<p> In the propmap the configuration names must be the hex propery tag of the requested property. The value given to the configuration name must be the LDAP attribute to which the property should be mapped. </p>
<p> Example: !propmap ldap.propmap.cfg</dl>
<h2>Explanation Of Each Parameter</h2>
<p><code>ldap_host</code></p>
<dl>
<dd>The hostname or ip-adress of the LDAP server. </p>
<p> Default: <i>localhost</i></dl>
<p> <code>ldap_port</code></p>
<dl>
<dd>The port number of the LDAP server. LDAP normally runs on port 389. </p>
<p> Default: <i>389</i></dl>
<p> <code>ldap_protocol</code></p>
<dl>
<dd>The protocol to be used to connect to the LDAP server. Can be either &#8216;ldap&#8217; or &#8216;ldaps&#8217; for SSL connections. You will probably have to specify port 636 for ldap_port also. Zarafa will not use STARTTLS for such an SSL connection but instead will connect directly to an SSL encrypted port. </p>
<p> Default: <i>ldap</i></dl>
<p> <code>ldap_uri</code></p>
<dl>
<dd>Instead of using ldap_host, ldap_port and ldap_protocol, you may also use ldap_uri which should specify the URI of the LDAP server like &#8216;<a href="ldap://server:389'.">ldap://server:389&#8242;.</a> If ldap_uri is set, the values of ldap_host, ldap_port and ldap_protocol are ignored. You may also specify multiple space-separated LDAP server URI&#8217;s. </p>
<p> Default:</dl>
<p> <code>ldap_server_charset</code></p>
<dl>
<dd>The charset that the LDAP server uses to store strings. All strings sent to the LDAP server or retrieved from the server will be interpreted in this charset. In most setups, utf-8 is used, but may also be iso-8859-15. All charsets supported by the system iconv() are supported here. </p>
<p> Default: <i>utf-8</i></dl>
<p> <code>ldap_bind_user</code></p>
<dl>
<dd>The bind dn as to connect to the LDAP server. Leave empty to connect anonymous. </p>
<p> Default value is empty.</dl>
<p> <code>ldap_bind_passwd</code></p>
<dl>
<dd>When ldap_bind_user is a valid DN, this should be filled in too. </p>
<p> Default value is empty.</dl>
<p> <code>ldap_network_timeout</code></p>
<dl>
<dd>The timeout for network operations in seconds. </p>
<p> Default: <i>30</i></dl>
<p> <code>ldap_last_modification_attribute</code></p>
<dl>
<dd>This value is used to detect changes in the item in the LDAP server. Since it is a standard LDAP attribute, you should never have to change this. It is mainly used for addressbook synchronisation between your server and your offline data. </p>
<p> Default: <i>modifyTimeStamp</i></dl>
<p> <code>ldap_page_size</code></p>
<dl>
<dd>Limit result sets in pages of this size, downloading fewer results at a time from the LDAP server. </p>
<p> Default: <i>1000</i></dl>
<p> <code>ldap_search_base</code></p>
<dl>
<dd>This is the subtree entry where all objects are defined in the LDAP server. </p>
<p> Default: <i>dc=zarafa,dc=com</i></dl>
<p> <code>ldap_object_type_attribute</code></p>
<dl>
<dd>An object is defined by this attribute what type it is, eg. user, group, etc. Every object type should have a unique value in this attribute in order to define what which enrty is. </p>
<p> The value of this attribute must be specified in the ldap_*_type_attribute_value settings. Each of those settings may specify multiple values for the type attribute, separated by comma&#8217;s. All of these values must be present in the objects type attribute for a match to be made and the object to be recognised as that type. </p>
<p> It is possible for ambiguities to arise by setting the same string for multiple ldap_*_type_attribute_value settings. This ambiguity will be resolved by preferring objects with more matching values. If the ambiguity cannot be resolved in this way, then the first possibility is chosen from the list (addresslist, tenant, dynamic group, group, contact, user). </p>
<p> Default: <i>objectClass</i></dl>
<p> <code>ldap_user_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines a user. </p>
<p> Default for OpenLDAP: <i>posixAccount</i> </p>
<p> Default for ADS: <i>user</i></dl>
<p> <code>ldap_group_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines a group. </p>
<p> Default for OpenLDAP: <i>posixGroup</i> </p>
<p> Default for ADS: <i>group</i></dl>
<p> <code>ldap_contact_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines a contact. </p>
<p> Default for OpenLDAP: <i>inetOrgPerson</i> </p>
<p> Default for ADS: <i>contact</i></dl>
<p> <code>ldap_company_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines a tenant. This option is only used in multi-tenancy installations. </p>
<p> Default for OpenLDAP: <i>organizationalUnit</i> </p>
<p> Default for ADS: <i>zarafa-company</i></dl>
<p> <code>ldap_addresslist_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines an addresslist. </p>
<p> Default: <i>zarafa-addresslist</i></dl>
<p> <code>ldap_dynamicgroup_type_attribute_value</code></p>
<dl>
<dd>The value in <code>ldap_object_type_attribute</code> which defines a dynamic group. </p>
<p> Default: <i>zarafa-dynamicgroup</i></dl>
<p> <code>ldap_user_search_filter</code></p>
<dl>
<dd>Adds an extra filter to the user search. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa users. </p>
<p> Default for OpenLDAP is empty. </p>
<p> Default for ADS: <i>(objectCategory=Person)</i></dl>
<p> <code>ldap_user_unique_attribute</code></p>
<dl>
<dd>This is the unique attribute of a user which is never going to change, unless the user is removed from LDAP. When this value changes, Zarafa will remove the previous user and store from the database, and create a new user with this unique value. </p>
<p> Default for OpenLDAP: <i>uidNumber</i> </p>
<p> Default for ADS: <i>objectGuid</i></dl>
<p> <code>ldap_user_unique_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_user_unique_attribute</code>. This value can be <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>binary</i></dl>
<p> <code>ldap_fullname_attribute</code></p>
<dl>
<dd>This value is the fullname of a user. It will be used on outgoing messages, and store names. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_loginname_attribute</code></p>
<dl>
<dd>This value is the loginname of a user. This is what the user uses to login on zarafa. The DAgent will use this value to open the store of the user. </p>
<p> Default for OpenLDAP: <i>uid</i> </p>
<p> Default for ADS: <i>sAMAccountName</i></dl>
<p> <code>ldap_password_attribute</code></p>
<dl>
<dd>This value is the password of a user. When using <code>ldap_authentication_method</code> = <i>password</i>, this value will be checked. The <code>ldap_bind_user</code> should have enough access rights to read the password field. </p>
<p> Default for OpenLDAP: <i>userPassword</i> </p>
<p> Default for ADS: <i>unicodePwd</i></dl>
<p> <code>ldap_authentication_method</code></p>
<dl>
<dd>This value can be <i>bind</i> or <i>password</i>. When set to bind, the plugin will authenticate by opening a new connection to the LDAP server as the user with the given password. When set to password, the plugin will read and match the password field from the LDAP server itself. When set to password, the <code>ldap_bind_user</code> should have enough access rights to read the password field. </p>
<p> Default for OpenLDAP: <i>bind</i> </p>
<p> Default for ADS: <i>bind</i></dl>
<p> <code>ldap_emailaddress_attribute</code></p>
<dl>
<dd>This value is the email address of a user. It will be used to set the From on outgoing messages. </p>
<p> Default: <i>mail</i></dl>
<p> <code>ldap_emailaliases_attribute</code></p>
<dl>
<dd>This value is the email aliases of a user. It can be used to find extra valid email accounts for incoming email. These email addresses cannot be used for outgoing email. </p>
<p> Default: <i>zarafaAliases</i></dl>
<p> <code>ldap_isadmin_attribute</code></p>
<dl>
<dd>This value indicates if a user has administrator rights. 0 or not presents means no. 1 means yes. In multi-tenancy environment a value of 1 means that the user is administrator over his own tenant. A value of 2 means he is administrator over all companies within the environment. </p>
<p> Default: <i>zarafaAdmin</i></dl>
<p> <code>ldap_nonactive_attribute</code></p>
<dl>
<dd>This value indicates if a user is nonactive. Nonactive users cannot login, but the store can be used as a shared store for other users. </p>
<p> Setting this value to 1 will make a mailbox nonactive. The nonactive attribute provided by the Zarafa schema for nonactive users is <i>zarafaSharedStoreOnly</i> </p>
<p> Default: <i>zarafaSharedStoreOnly</i></dl>
<p> <code>ldap_resource_type_attribute</code></p>
<dl>
<dd>This attribute can change the type of a non-active user. The value of this attribute can be <i>room</i> or <i>equipment</i> to make it such a resource. If this attribute is not present, or not one of the previously described values, the user will be a normal non-active user. </p>
<p> Default: <i>zarafaResourceType</i></dl>
<p> <code>ldap_resource_capacity_attribute</code></p>
<dl>
<dd>Resources often have a limited capacity. Use this attribute to control this value. user. </p>
<p> Default: <i>zarafaResourceCapacity</i></dl>
<p> <code>ldap_sendas_attribute</code></p>
<dl>
<dd>This attribute contains the list of users for which the user can use the sendas feature. </p>
<p> Default: <i>zarafaSendAsPrivilege</i></dl>
<p> <code>ldap_sendas_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_sendas_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>dn</i></dl>
<p> <code>ldap_sendas_relation_attribute</code></p>
<dl>
<dd>This value is used to find the users in the sendas list. </p>
<p> Defaults to empty value, using the <code>ldap_user_unique_attribute</code> setting. By using the DN, you can also add groups to the sendas list. </p>
<p> Default for OpenLDAP is empty. </p>
<p> Default for ADS: <i>distinguishedName</i></dl>
<p> <code>ldap_user_certificate_attribute</code></p>
<dl>
<dd>The attribute which contains the user&#8217;s public certificate to be used for encrypted S/MIME messages. Both Active Directory and OpenLDAP use the same ldap attribute by default. The format of the certificate should be the binary DER format. </p>
<p> Default: <i>userCertificate</i></dl>
<p> <code>ldap_group_search_filter</code></p>
<dl>
<dd>Adds an extra filter to the group search. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa groups. </p>
<p> Default for OpenLDAP is empty. </p>
<p> Default for ADS: <i>(objectCategory=Group)</i></dl>
<p> <code>ldap_group_unique_attribute</code></p>
<dl>
<dd>This is the unique attribute of a group which is never going to change, unless the group is removed from LDAP. When this value changes, Zarafa will remove the previous group from the database, and create a new group with this unique value. </p>
<p> Default for OpenLDAP: <i>gidNumber</i> </p>
<p> Default for ADS: <i>objectSid</i></dl>
<p> <code>ldap_group_unique_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_group_unique_attribute</code> this value can be <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>binary</i></dl>
<p> <code>ldap_groupname_attribute</code></p>
<dl>
<dd>This value is the name of a group. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_groupmembers_attribute</code></p>
<dl>
<dd>This value is the member list of a group. </p>
<p> Default for OpenLDAP: <i>memberUid</i> </p>
<p> Default for ADS: <i>member</i></dl>
<p> <code>ldap_groupmembers_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_groupmembers_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>dn</i></dl>
<p> <code>ldap_groupmembers_relation_attribute</code></p>
<dl>
<dd>This value is used to find the users in a group if <code>ldap_groupmembers_attribute_type</code> is <i>text</i>. </p>
<p> Defaults to empty value, using the <code>ldap_user_unique_attribute</code> setting. </p>
<p> Default is empty.</dl>
<p> <code>ldap_group_security_attribute</code></p>
<dl>
<dd>If this attribute is present, you can make a group a security group. These groups can be used to place permissions on folders. </p>
<p> Default for OpenLDAP: <i>zarafaSecurityGroup</i> </p>
<p> Default for ADS: <i>groupType</i></dl>
<p> <code>ldap_group_security_attribute_type</code></p>
<dl>
<dd>The type of the <code>ldap_group_security_attribute</code> is very different for ADS and OpenLDAP. The value of this option can be <i>boolean</i> or <i>ads</i>. The ads option only looks at the highest bit in the numeric value of the groupType attribute. </p>
<p> Default for OpenLDAP: <i>boolean</i> </p>
<p> Default for ADS: <i>ads</i></dl>
<p> <code>ldap_company_search_filter</code></p>
<dl>
<dd>Add an extra filter to the tenant search. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa companies. </p>
<p> Default for OpenLDAP is empty. </p>
<p> Default for ADS: <i>(objectCategory=Company)</i></dl>
<p> <code>ldap_company_unique_attribute</code></p>
<dl>
<dd>This is the unique attribute of a tenant which is never going to change, unless the tenant is removed from LDAP. When this value changes, Zarafa will remove the previous tenant from the database, and create a new tenant with this unique value. </p>
<p> Default for OpenLDAP: <i>ou</i> </p>
<p> Default for ADS: <i>objectSid</i></dl>
<p> <code>ldap_company_unique_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_company_unique_attribute</code> this value can be <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>binary</i></dl>
<p> <code>ldap_companyname_attribute</code></p>
<dl>
<dd>This value is the name of a tenant. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_company_view_attribute</code></p>
<dl>
<dd>This attribute contains the list of tenants which can view the members of the tenant where this attribute is set on. tenants which are not listed in this attribute cannot see the presence of the tenant space itself nor its members. </p>
<p> Default: <i>zarafaViewPrivilege</i></dl>
<p> <code>ldap_company_view_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_company_view_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>dn</i></dl>
<p> <code>ldap_company_view_relation_attribute</code></p>
<dl>
<dd>The attribute of the tenant which is listed in <code>ldap_company_view_attribute</code>. </p>
<p> Default: Empty, using the <code>ldap_company_unique_attribute</code></dl>
<p> <code>ldap_company_admin_attribute</code></p>
<dl>
<dd>This attribute contains the list of users outside of the selected tenant space who are administrator over the selected tenant space. Note that local users should not be listed as administrator here, those users need the <code>ldap_isadmin_attribute</code> attribute. </p>
<p> Default: <i>zarafaAdminPrivilege</i></dl>
<p> <code>ldap_company_admin_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_company_admin_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>dn</i></dl>
<p> <code>ldap_company_admin_relation_attribute</code></p>
<dl>
<dd>The attribute of the user which is listed in <code>ldap_company_admin_attribute</code>. </p>
<p> Default: Empty, using the <code>ldap_user_unique_attribute</code></dl>
<p> <code>ldap_company_system_admin_attribute</code></p>
<dl>
<dd>This attribute contains the user who acts as the system administrator of this tenatn space. This can either be a local user or a user from a different tenant space. At the moment this user is set as the sender of quota warning emails. </p>
<p> Default: <i>zarafaSystemAdmin</i></dl>
<p> <code>ldap_company_system_admin_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_company_system_admin_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. </p>
<p> Default for OpenLDAP: <i>text</i> </p>
<p> Default for ADS: <i>dn</i></dl>
<p> <code>ldap_company_system_admin_relation_attribute</code></p>
<dl>
<dd>The attribute of the user which is listed in <code>ldap_system_admin_attribute</code>. </p>
<p> Default: Empty, using the <code>ldap_user_unique_attribute</code></dl>
<p> <code>ldap_addresslist_search_filter</code></p>
<dl>
<dd>Add a filter to the addresslist search. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa addresslists. </p>
<p> Default: <i>(objectClass=zarafa-addresslist)</i></dl>
<p> <code>ldap_addresslist_unique_attribute</code></p>
<dl>
<dd>This is the unique attribute of a addresslist which is never going to change, unless the addresslist is removed from LDAP. When this value changes, Zarafa will remove the previous addresslist from the database, and create a new addresslist with this unique value. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_addresslist_unique_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_addresslist_unique_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. On LDAP this value should be <i>text</i>. On ADS this value should be <i>dn</i> </p>
<p> Default: <i>text</i></dl>
<p> <code>ldap_addresslist_filter_attribute</code></p>
<dl>
<dd>This is the name of the attribute on the addresslist object that specifies the filter to be applied for this addresslist. All users matching this filter AND matching the default ldap_user_search_filter will be included in the addresslist. </p>
<p> Default: <i>zarafaFilter</i></dl>
<p> <code>ldap_addresslist_search_base_attribute</code></p>
<dl>
<dd>This is the name of the attribute on the addresslist object that specifies the search base to be applied for this addresslist. </p>
<p> Default: <i>zarafaBase</i></dl>
<p> <code>ldap_addresslist_name_attribute</code></p>
<dl>
<dd>The attribute containing the name of the addresslist </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_dynamicgroup_search_filter</code></p>
<dl>
<dd>Add an extra filter to the dynamicgroup search. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa dynamic groups. </p>
<p> Default is empty.</dl>
<p> <code>ldap_dynamicgroup_unique_attribute</code></p>
<dl>
<dd>This is the unique attribute of a dynamicgroup which is never going to change, unless the dynamicgroup is removed from LDAP. When this value changes, Zarafa will remove the previous dynamicgroup from the database, and create a new dynamicgroup with this unique value. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_dynamicgroup_unique_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_dynamicgroup_unique_attribute</code> this value can be <i>binary</i> or <i>text</i>. On LDAP this value should be <i>text</i>. On ADS this value should be <i>binary</i> </p>
<p> Default: <i>text</i></dl>
<p> <code>ldap_dynamicgroup_filter_attribute</code></p>
<dl>
<dd>This is the name of the attribute on the dynamicgroup object that specifies the filter to be applied for this dynamicgroup. All users matching this filter AND matching the default search filters for objects will be included in the dynamicgroup. </p>
<p> Default: <i>zarafaFilter</i></dl>
<p> <code>ldap_dynamicgroup_search_base_attribute</code></p>
<dl>
<dd>This is the name of the attribute on the dynamicgroup object that specifies the search base to be applied for this dynamicgroup. </p>
<p> Default: <i>zarafaBase</i></dl>
<p> <code>ldap_dynamicgroup_name_attribute</code></p>
<dl>
<dd>The attribute containing the name of the dynamicgroup. </p>
<p> Default: <i>cn</i></dl>
<p> <code>ldap_quotaoverride_attribute</code></p>
<dl>
<dd>Default: <i>zarafaQuotaOverride</i></dl>
<p> <code>ldap_warnquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaQuotaWarn</i></dl>
<p> <code>ldap_softquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaQuotaSoft</i></dl>
<p> <code>ldap_hardquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaQuotaHard</i></dl>
<p> <code>ldap_userdefault_quotaoverride_attribute</code></p>
<dl>
<dd>Default: <i>zarafaUserDefaultQuotaOverride</i></dl>
<p> <code>ldap_userdefault_warnquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaUserDefaultQuotaWarn</i></dl>
<p> <code>ldap_userdefault_softquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaUserDefaultQuotaSoft</i></dl>
<p> <code>ldap_userdefault_hardquota_attribute</code></p>
<dl>
<dd>Default: <i>zarafaUserDefaultQuotaHard</i></dl>
<p> <code>ldap_quota_multiplier</code></p>
<dl>
<dd>This value is used to multiply the quota values to bytes. When the values in LDAP are in Kb, use 1024 here. </p>
<p> Default: <i>1</i></dl>
<p> <code>ldap_quota_userwarning_recipients_attribute</code></p>
<dl>
<dd>This attribute contains the list of users who will recieve an email when a user exceeds his quota. User who exceeds his quota will be automatically added to the recipients list, this list only indicates who else will be notified. </p>
<p> Default: <i>zarafaQuotaUserWarningRecipients</i></dl>
<p> <code>ldap_quota_userwarning_recipients_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_quota_userwarning_recipients_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. On LDAP this value should be <i>text</i>. On ADS this value should be <i>dn</i> </p>
<p> Default: <i>text</i></dl>
<p> <code>ldap_quota_userwarning_recipients_relation_attribute</code></p>
<dl>
<dd>The attribute of the user which is listed in <code>ldap_quota_userwarning_recipients_attribute</code> </p>
<p> Default: Empty, using <i>ldap_user_unique_attribute</i></dl>
<p> <code>ldap_quota_companywarning_recipients_attribute</code></p>
<dl>
<dd>This attribute contains the list of users who will recieve an email when a tenant exceeds its quota. The system administrator of the tenant that is over quota will automatically be added to the recipients list, this list only indicates who else will be notified. </p>
<p> Default: <i>zarafaQuotaCompanyWarningRecipients</i></dl>
<p> <code>ldap_quota_companywarning_recipients_attribute_type</code></p>
<dl>
<dd>Contents type for the <code>ldap_quota_companywarning_recipients_attribute</code> this value can be <i>dn</i>, <i>binary</i> or <i>text</i>. On LDAP this value should be <i>text</i>. On ADS this value should be <i>dn</i> </p>
<p> Default: <i>text</i></dl>
<p> <code>ldap_quota_companywarning_recipients_relation_attribute</code></p>
<dl>
<dd>The attribute of the user which is listed in <code>ldap_quota_companywarning_recipients_attribute</code> </p>
<p> Default: Empty, using <i>ldap_user_unique_attribute</i></dl>
<p> <code>ldap_addressbook_hide_attribute</code></p>
<dl>
<dd>The attribute indicating the object must be hidden from the addressbook. The object will still be detected as zarafa user and is allowed to login and work as regular zarafa user, but will not be visible in the addressbook for other users. </p>
<p> Default: <i>zarafaHidden</i></dl>
<p> <code>ldap_object_search_filter</code></p>
<dl>
<dd>When searching in the addressbook, this filter will be used. Normally, the zarafa server will only search in the unique attribute, loginname, fullname and emailaddress. You might want to search in more fields, like &#8216;lastname&#8217;. Zarafa also uses a postfix wildcard only. Using the &#8216;*&#8217; wildcard with prefixes makes a search slower, but can return more results. </p>
<p> Hint: Use the zarafaAccount attribute in the filter to differentiate between non-zarafa and zarafa objects. </p>
<p> You can set a custom search filter here. &#8216;%s&#8217; will be replaced with the string being searched. </p>
<p> Active Directory has a shortcut for searching in the addressbook using the &#8216;anr&#8217; attribute. This is recommended on ADS installations. </p>
<p> Default: </p>
<p> Recommended for ADS installations: <i>(anr=%s)</i> </p>
<p> Optional for OpenLDAP installations: <i>(|(mail=%s*)(uid=%s*)(cn=*%s*)(fullname=*%s*)(givenname=*%s*)(lastname=*%s*)(sn=*%s*))</i></dl>
<p> <code>ldap_filter_cutoff_elements</code></p>
<dl>
<dd>When the ldap plugin retrieves information from the LDAP Server, large queries can be created to retrieve data for multiple objects at once. These large queries can perform badly on some LDAP server implementations. This option limits the number of elements that can be retrieved in one search filter and therefore limits the size of the filter. Instead, a broader search filter is created which retrieves all objects from the LDAP server. This results in slightly higher processing overhead and network activity, but with the bonus that the query can be served by the LDAP server much faster (a factor of 40 in 5000-object queries has been observed). </p>
<p> Setting this value to 0 will never limit the filter, setting it to a value of 1 will always limit the filter (since all queries will be retrieving one or more objects). </p>
<p> Default: <i>1000</i></dl>
<h2>Files</h2>
<p>/etc/zarafa/server.cfg</p>
<dl>
<dd>The server configuration file.</dl>
<p> /etc/zarafa/ldap.cfg</p>
<dl>
<dd>The Zarafa LDAP configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) </p>
