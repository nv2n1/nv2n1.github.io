---
title: "default-conf(5)"
name: "default-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-default-conf/"
description: "default.conf – IPA configuration file"
---

<p>default.conf &#8211; IPA configuration file</p>
<h2>Synopsis</h2>
<p>/etc/ipa/default.conf, ~/.ipa/default.conf, /etc/ipa/server.conf, /etc/ipa/cli.conf</p>
<h2>Description</h2>
<p>The <i>default.conf </i>configuration file is used to set system-wide defaults to be applied when running IPA clients and servers. </p>
<p> Users may create an optional configuration file in <i>~/.ipa/default.conf</i> which will be merged into the system-wide defaults file. </p>
<p> The following files are read, in order: </p>
<pre> ~/.ipa/default.conf
 /etc/ipa/&lt;context&gt;.conf
 /etc/ipa/default.conf
 built-in constants</pre>
<p>The IPA server does not read ~/.ipa/default.conf. </p>
<p> The first setting wins.</p>
<h2>Syntax</h2>
<p>The configuration options are not case sensitive. The values may be case sensitive, depending on the option. </p>
<p> Blank lines are ignored. Lines beginning with # are comments and are ignored. </p>
<p> Valid lines consist of an option name, an equals sign and a value. Spaces surrounding equals sign are ignored. An option terminates at the end of a line. </p>
<p> Values should not be quoted, the quotes will not be stripped. </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Wrong &#8211; don&#8217;t include quotes<br />
&nbsp;<wbr>verbose&nbsp;<wbr>=&nbsp;<wbr>&quot;True&quot; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Right &#8211; Properly formatted options<br />
&nbsp;<wbr>verbose&nbsp;<wbr>=&nbsp;<wbr>True<br />
&nbsp;<wbr>verbose=True </p>
<p> Options must appear in the section named [global]. There are no other sections defined or used currently. </p>
<p> Options may be defined that are not used by IPA. Be careful of misspellings, they will not be rejected.</p>
<h2>Options</h2>
<p>The following options are relevant for the server:</p>
<dl>
<dt><code>basedn</code> &lt;base&gt;</p>
<dd>Specifies the base DN to use when performing LDAP operations. The base must be in DN format (dc=example,dc=com).</p>
<dt><code>ca_agent_port &lt;port&gt;</code></p>
<dd>Specifies the secure CA agent port. The default is 8443.</p>
<dt><code>ca_ee_port &lt;port&gt;</code></p>
<dd>Specifies the secure CA end user port. The default is 8443.</p>
<dt><code>ca_host &lt;hostname&gt;</code></p>
<dd>Specifies the hostname of the dogtag CA server. The default is the hostname of the IPA server.</p>
<dt><code>ca_port &lt;port&gt;</code></p>
<dd>Specifies the insecure CA end user port. The default is 8080.</p>
<dt><code>context &lt;context&gt;</code></p>
<dd>Specifies the context that IPA is being executed in. IPA may operate differently depending on the context. The current defined contexts are cli and server. Additionally this value is used to load /etc/ipa/<code>context</code>.conf to provide context-specific configuration. For example, if you want to always perform client requests in verbose mode but do not want to have verbose enabled on the server, add the verbose option to <i>/etc/ipa/cli.conf</i>.</p>
<dt><code>debug &lt;boolean&gt;</code></p>
<dd>When True provides detailed information. Specifically this set the global log level to &quot;debug&quot;. Default is False.</p>
<dt><code>dogtag_version &lt;version&gt;</code></p>
<dd>Stores the version of Dogtag. Value 9 is assumed if not specified otherwise.</p>
<dt><code>domain &lt;domain&gt;</code></p>
<dd>The domain of the IPA server e.g. example.com.</p>
<dt><code>enable_ra &lt;boolean&gt;</code></p>
<dd>Specifies whether the CA is acting as an RA agent, such as when dogtag is being used as the Certificate Authority. This setting only applies to the IPA server configuration.</p>
<dt><code>fallback &lt;boolean&gt;</code></p>
<dd>Specifies whether an IPA client should attempt to fall back and try other services if the first connection fails.</p>
<dt><code>host &lt;hostname&gt;</code></p>
<dd>Specifies the local system hostname.</p>
<dt><code>in_server &lt;boolean&gt;</code></p>
<dd>Specifies whether requests should be forwarded to an IPA server or handled locally. This is used internally by IPA in a similar way as context. The same IPA framework is used by the ipa command-line tool and the server. This setting tells the framework whether it should execute the command as if on the server or forward it via XML-RPC to a remote server.</p>
<dt><code>in_tree &lt;boolean&gt;</code></p>
<dd>This is used in development and is generally a detected value. It means that the code is being executed within a source tree.</p>
<dt><code>interactive &lt;boolean&gt;</code></p>
<dd>Specifies whether values should be prompted for or not. The default is True.</p>
<dt><code>ldap_uri &lt;URI&gt;</code></p>
<dd>Specifies the URI of the IPA LDAP server to connect to. The URI scheme may be one of <code>ldap</code> or <code>ldapi</code>. The default is to use ldapi, e.g. <a href="ldapi://%2fvar%2frun%2fslapd-EXAMPLE-COM.socket">ldapi://%2fvar%2frun%2fslapd-EXAMPLE-COM.socket</a></p>
<dt><code>log_logger_XXX &lt;comma separated list of regexps&gt;</code></p>
<dd>loggers matching regexp will be assigned XXX level.</p>
<dd>Logger levels can be explicitly specified for specific loggers as opposed to a global logging level. Specific loggers are indicated by a list of regular expressions bound to a level. If a logger&#8217;s name matches the regexp then it is assigned that level. This config item must begin with &quot;log_logger_level_&quot; and then be followed by a symbolic or numeric log level, for example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>log_logger_level_debug&nbsp;<wbr>=&nbsp;<wbr>ipalib\.dn\..*</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>log_logger_level_35&nbsp;<wbr>=&nbsp;<wbr>ipalib\.plugins\.dogtag</p>
<dd>The first line says any logger belonging to the ipalib.dn module will have it&#8217;s level configured to debug.</p>
<dd>The second line say the ipa.plugins.dogtag logger will be configured to level 35.</p>
<dd>This config item is useful when you only want to see the log output from one or more selected loggers. Turning on the global debug flag will produce an enormous amount of output. This allows you to leave the global debug flag off and selectively enable output from a specific logger. Typically loggers are bound to classes and plugins.</p>
<dd>Note: logger names are a dot (&#8216;.&#8217;) separated list forming a path in the logger tree. The dot character is also a regular expression metacharacter (matches any character) therefore you will usually need to escape the dot in the logger names by preceding it with a backslash.</p>
<dt><code>mode &lt;mode&gt;</code></p>
<dd>Specifies the mode the server is running in. The currently support values are <code>production</code> and <code>development</code>. When running in production mode some self-tests are skipped to improve performance.</p>
<dt><code>mount_ipa &lt;URI&gt;</code></p>
<dd>Specifies the mount point that the development server will register. The default is /ipa/</p>
<dt><code>prompt_all &lt;boolean&gt;</code></p>
<dd>Specifies that all options should be prompted for in the IPA client, even optional values. Default is False.</p>
<dt><code>ra_plugin &lt;name&gt;</code></p>
<dd>Specifies the name of the CA back end to use. The current options are <code>dogtag</code> and <code>none</code>. This is a server-side setting. Changing this value is not recommended as the CA back end is only set up during initial installation.</p>
<dt><code>realm &lt;realm&gt;</code></p>
<dd>Specifies the Kerberos realm.</p>
<dt><code>session_auth_duration &lt;time duration spec&gt;</code></p>
<dd>Specifies the length of time authentication credentials cached in the session are valid. After the duration expires credentials will be automatically reacquired. Examples are &quot;2 hours&quot;, &quot;1h:30m&quot;, &quot;10 minutes&quot;, &quot;5min, 30sec&quot;.</p>
<dt><code>session_duration_type &lt;inactivity_timeout|from_start&gt;</code></p>
<dd>Specifies how the expiration of a session is computed. With <code>inactivity_timeout</code> the expiration time is advanced by the value of session_auth_duration everytime the user accesses the service. With <code>from_start</code> the session expiration is the start of the user&#8217;s session plus the value of session_auth_duration.</p>
<dt><code>server &lt;hostname&gt;</code></p>
<dd>Specifies the IPA Server hostname.</p>
<dt><code>skip_version_check &lt;boolean&gt;</code></p>
<dd>Skip client vs. server API version checking. Can lead to errors/strange behavior when newer clients talk to older servers. Use with caution.</p>
<dt><code>startup_timeout &lt;time in seconds&gt;</code></p>
<dd>Controls the amount of time waited when starting a service. The default value is 120 seconds.</p>
<dt><code>startup_traceback &lt;boolean&gt;</code></p>
<dd>If the IPA server fails to start and this value is True the server will attempt to generate a python traceback to make identifying the underlying problem easier.</p>
<dt><code>validate_api &lt;boolean&gt;</code></p>
<dd>Used internally in the IPA source package to verify that the API has not changed. This is used to prevent regressions. If it is true then some errors are ignored so enough of the IPA framework can be loaded to verify all of the API, even if optional components are not installed. The default is False.</p>
<dt><code>verbose &lt;boolean&gt;</code></p>
<dd>When True provides more information. Specifically this sets the global log level to &quot;info&quot;.</p>
<dt><code>wait_for_dns &lt;number of attempts&gt;</code></p>
<dd>Controls whether the IPA commands dnsrecord-{add,mod,del} work synchronously or not. The DNS commands will repeat DNS queries up to the specified number of attempts until the DNS server returns an up-to-date answer to a query for modified records. Delay between retries is one second.</p>
<dd>The DNS commands will raise a DNSDataMismatch exception if the answer doesn&#8217;t match the expected value even after the specified number of attempts.</p>
<dd>The DNS queries will be sent to the resolver configured in /etc/resolv.conf on the IPA server.</p>
<dd>Do not enable this in production! This will cause problems if the resolver on IPA server uses a caching server instead of a local authoritative server or e.g. if DNS answers are modified by DNS64. The default is disabled (the option is not present).</p>
<dt><code>xmlrpc_uri &lt;URI&gt;</code></p>
<dd>Specifies the URI of the XML-RPC server for a client. This may be used by IPA, and is used by some external tools, such as ipa-getcert. Example: <a rel="nofollow" href="https://ipa.example.com/ipa/xml">https://ipa.example.com/ipa/xml</a></p>
<dt><code>jsonrpc_uri &lt;URI&gt;</code></p>
<dd>Specifies the URI of the JSON server for a client. This is used by IPA. If not given, it is derived from xmlrpc_uri. Example: <a rel="nofollow" href="https://ipa.example.com/ipa/json">https://ipa.example.com/ipa/json</a></p>
<dt><code>rpc_protocol &lt;URI&gt;</code></p>
<dd>Specifies the type of RPC calls IPA makes: &#8216;jsonrpc&#8217; or &#8216;xmlrpc&#8217;. Defaults to &#8216;jsonrpc&#8217;.</p>
<dt>The following define the containers for the IPA server. Containers define where in the DIT that objects can be found. The full location is the value of container + basedn.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>container_accounts: cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_applications: cn=applications,cn=configs,cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_automount: cn=automount<br />
&nbsp;<wbr>&nbsp;<wbr>container_configs: cn=configs,cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_dns: cn=dns<br />
&nbsp;<wbr>&nbsp;<wbr>container_group: cn=groups,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_hbac: cn=hbac<br />
&nbsp;<wbr>&nbsp;<wbr>container_hbacservice: cn=hbacservices,cn=hbac<br />
&nbsp;<wbr>&nbsp;<wbr>container_hbacservicegroup: cn=hbacservicegroups,cn=hbac<br />
&nbsp;<wbr>&nbsp;<wbr>container_host: cn=computers,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_hostgroup: cn=hostgroups,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_netgroup: cn=ng,cn=alt<br />
&nbsp;<wbr>&nbsp;<wbr>container_permission: cn=permissions,cn=pbac<br />
&nbsp;<wbr>&nbsp;<wbr>container_policies: cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_policygroups: cn=policygroups,cn=configs,cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_policylinks: cn=policylinks,cn=configs,cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_privilege: cn=privileges,cn=pbac<br />
&nbsp;<wbr>&nbsp;<wbr>container_rolegroup: cn=roles,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_roles: cn=roles,cn=policies<br />
&nbsp;<wbr>&nbsp;<wbr>container_service: cn=services,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_sudocmd: cn=sudocmds,cn=sudo<br />
&nbsp;<wbr>&nbsp;<wbr>container_sudocmdgroup: cn=sudocmdgroups,cn=sudo<br />
&nbsp;<wbr>&nbsp;<wbr>container_sudorule: cn=sudorules,cn=sudo<br />
&nbsp;<wbr>&nbsp;<wbr>container_user: cn=users,cn=accounts<br />
&nbsp;<wbr>&nbsp;<wbr>container_vault: cn=vaults,cn=kra<br />
&nbsp;<wbr>&nbsp;<wbr>container_virtual: cn=virtual operations,cn=etc </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/ipa/default.conf</i></p>
<dd>system-wide IPA configuration file</p>
<dt><i>$HOME/.ipa/default.conf</i></p>
<dd>user IPA configuration file</p>
<dt>It is also possible to define context-specific configuration files. The <code>context</code> is set when the IPA api is initialized. The two currently defined contexts in IPA are <code>cli</code> and <code>server</code>. This is helpful, for example, if you only want <code>debug</code> enabled on the server and not in the client. If this is set to True in <i>default.conf</i> it will affect both the ipa client tool and the IPA server. If it is only set in <i>server.conf</i> then only the server will have <code>debug</code> set. These files will be loaded if they exist:</p>
<dd>
<dt><i>/etc/ipa/cli.conf</i></p>
<dd>system-wide IPA client configuration file</p>
<dt><i>/etc/ipa/server.conf</i></p>
<dd>system-wide IPA server configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipa/">ipa</a></code>(1) </p>
