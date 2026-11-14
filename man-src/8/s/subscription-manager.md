---
title: "subscription-manager(8)"
name: "subscription-manager"
section: "8"
letter: "s"
url: "/docs/linux/man/8-subscription-manager/"
description: "subscription-manager – Registers systems to a subscription management service and then attaches and manages subscriptions for software products."
---

<p>subscription-manager &#8211; Registers systems to a subscription management service and then attaches and manages subscriptions for software products. </p>
<h2>Synopsis</h2>
<p>subscription-manager <i>command [options]</i> </p>
<h2>Description</h2>
<p><code>subscription-manager</code> is a client program that registers a system with a subscription management service such as the Customer Portal Subscription Management service or on-premise Subscription Asset Manager. Red Hat provides content updates and support by issuing <i>subscriptions</i> for its products. These subscriptions are applied to systems; once a subscription for a product is attached to a system, that system is allowed to install, update, and receive support for that software product. IT administrators need to track these subscriptions and how they are attached. This subscription management is a feature available for Red Hat platforms version 5.7 (and later) and version 6.1 (and later). For RHEL systems, content is delivered through the Red Hat Customer Portal. Subscriptions and systems are managed globally through the Red Hat subscription management service, which is integrated with the Customer Portal. Subscriptions are managed for the local system by using the Red Hat Subscription Manager tool. Subscription Manager is a local client which connects a system with the subscription management service. <code>subscription-manager</code> is the command-line based client for the Red Hat Subscription Manager tool. Subscription Manager performs several key operations:</p>
<dl>
<dd>* It registers systems to the Red Hat subscription management service and adds the system to the inventory. Once a system is registered, it can receive updates based on its subscriptions to any kind of software products.</p>
<dd>* It lists both available and used subscriptions.</p>
<dd>* It allows administrators to both attach specific subscriptions to a system and remove those subscriptions.</dl>
<p> Subscription Manager can be used to auto-attach subscriptions to a system, as well. The <code>subscription-manager</code> command can even be invoked as part of a kickstart process. Available subscriptions are based on the specific information about the system&#8217;s architecture. A subscription is only considered <i>available</i> if the platform and hardware can support that specific product. Subscription Manager also collects and summarizes system facts related to its hardware, operating system, and other characteristics. These facts can be edited in the Subscription Manager configuration and displayed through Subscription Manager. There is also a Subscription Manager GUI, which can be invoked simply by running <code>subscription-manager-gui</code> from the command line. Subscription management is only available for RHEL 5.7/6.1 and later systems. Older systems should register to Red Hat Network Classic using the <code>rhn_register</code> command. </p>
<h2>Commands And Options</h2>
<p><code>subscription-manager</code> has specific options available for each command, depending on what operation is being performed. Subscription Manager commands are related to the different subscription operations: </p>
<dl>
<dd>1. register </p>
<dd>2. unregister </p>
<dd>3. attach </p>
<dd>4. auto-attach </p>
<dd>5. remove </p>
<dd>6. release </p>
<dd>7. service-level </p>
<dd>8. import </p>
<dd>9. redeem </p>
<dd>10. list </p>
<dd>11. refresh </p>
<dd>12. environments </p>
<dd>13. repos </p>
<dd>14. orgs </p>
<dd>15. plugins </p>
<dd>16. identity </p>
<dd>17. facts </p>
<dd>18. clean </p>
<dd>19. config </p>
<dd>20. version </p>
<dd>21. status </p>
<dd>22. deprecated commands: subscribe, unsubscribe, and activate </p>
<dd>23. repo-override </p>
</dl>
<h3>Common Options</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the specific help information for the given command. </p>
<dt><code>&#8211;proxy=PROXY</code></p>
<dd>Uses an HTTP proxy. The <i>PROXY</i> name has the format <i>hostname:port.</i> </p>
<dt><code>&#8211;proxyuser=PROXYUSERNAME</code></p>
<dd>Gives the username to use to authenticate to the HTTP proxy. </p>
<dt><code>&#8211;proxypass=PROXYPASSWORD</code></p>
<dd>Gives the password to use to authenticate to the HTTP proxy. </p>
</dl>
<h3>Register Options</h3>
<p>The <code>register</code> command registers a new system to the subscription management service. </p>
<dl>
<dt><code>&#8211;username=USERNAME</code></p>
<dd>Gives the username for the account which is registering the system; this user account is usually tied to the user account for the content delivery system which supplies the content. Optional, for user-based authentication. </p>
<dt><code>&#8211;password=PASSWORD</code></p>
<dd>Gives the user account password. </p>
<dt><code>&#8211;serverurl=SERVER_HOSTNAME</code></p>
<dd>Passes the name of the subscription service with which to register the system. The default value, if this is not given, is the Customer Portal Subscription Management service, <code>subscription.rhsm.redhat.com.</code> If there is an on-premise subscription service such as Subscription Asset Manager, this parameter can be used to submit the hostname of the subscription service. For Subscription Asset Manager, if the Subscription Manager tool is configured with the Subscription Asset Manager RPM, then the default value for the <code>&#8211;serverurl</code> parameter is for the on-premise Subscription Asset Manager server. </p>
<dt><code>&#8211;baseurl=<a rel="nofollow" href="https://CONTENT_SERVICE:PORT/PREFIX">https://CONTENT_SERVICE:PORT/PREFIX</a></code></p>
<dd>Passes the name of the content delivery service to configure the yum service to use to pull down packages. If there is an on-premise subscription service such as Subscription Asset Manager or CloudForms System Engine, this parameter can be used to submit the URL of the content repository, in the form <i><a rel="nofollow" href="https://server_name:port/prefix.">https://server_name:port/prefix.</a></i> For example, <code><a rel="nofollow" href="https://sam.example.com:8088/sam.">https://sam.example.com:8088/sam.</a></code> </p>
<dt><code>&#8211;name=SYSTEM_NAME</code></p>
<dd>Sets the name of the system to register. This defaults to the hostname. </p>
<dt><code>&#8211;consumerid=CONSUMERID</code></p>
<dd>References an existing system inventory ID to resume using a previous registration for this system. The ID is used as an inventory number for the system in the subscription management service database. If the system&#8217;s identity is lost or corrupted, this option allows it to resume using its previous identity and subscriptions. </p>
<dt><code>&#8211;activationkey=KEYS</code></p>
<dd>Gives a comma-separated list of product keys to use to redeem or apply specific subscriptions to the system. This is used for preconfigured systems which may already have products installed. Activation keys are issued by an on-premise subscription management service, such as Subscription Asset Manager.</p>
<dd>When the <code>&#8211;activationkey</code> option is used, it is not necessary to use the <code>&#8211;username</code> and <code>&#8211;password</code> options, because the authentication information is implicit in the activation key.</p>
<dd>For example:</p>
<dl>
<dd>
<pre>subscription-manager register --org=&quot;IT Dept&quot; --activationkey=1234abcd</pre>
</dl>
<dt><code>&#8211;auto-attach</code></p>
<dd>Automatically attaches compatible subscriptions to this system. </p>
<dt><code>&#8211;servicelevel=LEVEL</code></p>
<dd>Sets the preferred service level to use with subscriptions added to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. </p>
<dt><code>&#8211;force</code></p>
<dd>Registers the system even if it is already registered. Normally, any register operations will fail if the system is already registered. With <code>&#8211;force,</code> the existing system entry is unregistered first, all of its subscriptions are returned to the pool, and then the system is registered as a new entry. </p>
<dt><code>&#8211;org=ORG</code></p>
<dd>Assigns the system to an organization. Infrastructures which are managed on-site may be <i>multi-tenant,</i> meaning that there are multiple organizations within one customer unit. A system may be assigned manually to one of these organizations. When a system is registered with the Customer Portal, this is not required. When a system is registered with an on-premise application such as Subscription Asset Manager, this argument <i>is</i> required, unless there is only a single organization configured. </p>
<dt><code>&#8211;environment=ENV</code></p>
<dd>Registers the system to an environment within an organization. </p>
<dt><code>&#8211;release=VERSION</code></p>
<dd>Shortcut for &quot;release &#8211;set=VERSION&quot; </p>
<dt><code>&#8211;type=CONSUMERTYPE</code></p>
<dd>Sets the type of unit to register. Most units in the inventory will use the default value of <code>system.</code> For development or test units, this can be <code>person</code> , which indicates a personal (rather than organizational) unit. Another type of unit can be <code>candlepin</code> for a local content service or <code>domain</code> for an IP domain. </p>
</dl>
<h3>Unregister Options</h3>
<p>The <code>unregister</code> command removes a system&#8217;s subscriptions and removes it from the subscription management service. </p>
<p> This command has no options.</p>
<h3>Attach Options</h3>
<p>The <code>attach</code> command applies a specific subscription to the system. </p>
<dl>
<dt><code>&#8211;auto</code></p>
<dd>Automatically attaches the best-matched compatible subscription or subscriptions to the system. This is the default unless <code>&#8211;pool</code> or <code>&#8211;file</code> are used. </p>
<dt><code>&#8211;pool=POOLID</code></p>
<dd>Gives the ID for the subscriptions pool (collection of products) to attach to the system. This overrides the default of &#8211;auto. </p>
<dt><code>&#8211;file=FILE</code></p>
<dd>Specifies a file from which to read whitespace-delimited pool IDs. If FILE is &quot;-&quot;, the pool IDs will be read from stdin. This overrides the default of <code>&#8211;auto.</code> </p>
<dt><code>&#8211;quantity=NUMBER</code></p>
<dd>Attaches a specified number of subscriptions to the system. Subscriptions may have certain limits on them, like the number of sockets on the system or the number of allowed virtual guests. It is possible to attach multiple subscriptions (or <i>stacking</i> subscriptions) to cover the number of sockets, guests, or other characteristics. May not be used with an auto-attach. </p>
<dt><code>&#8211;servicelevel=LEVEL</code></p>
<dd>Sets the preferred service level to use with subscriptions automatically attached to the system. Service levels are commonly premium, standard, and none, though other levels may be available depending on the product and the contract. This option cannot be used when attaching specific pools via <code>&#8211;pool</code> or <code>&#8211;file.</code> </p>
</dl>
<h3>Auto-Attach Options</h3>
<p>The <code>auto-attach</code> command sets whether the ability to check, attach, and update subscriptions occurs automatically on the system. Auto-attaching subscriptions checks the currently-installed products, attached subscriptions, and any changes in available subscriptions every four hours using the <code>rhsmcertd</code> daemon. </p>
<dl>
<dt><code>&#8211;enable</code></p>
<dd>Enables the auto-attach option for the system. If there is any change in the subscriptions for the system, any subscriptions expire, or any new products are installed, then <code>subscription-manager</code> detects the changes and automatically attaches the appropriate subscriptions so that the system remains covered. </p>
<dt><code>&#8211;disable</code></p>
<dd>Disables the auto-attach option for the system. If auto-attach is disabled, then any changes in installed products or subscriptions for the system (including expired subscriptions) must be addressed manually by the administrator. </p>
<dt><code>&#8211;show</code></p>
<dd>Shows whether auto-attach is enabled on the systems. </p>
</dl>
<h3>Remove Options</h3>
<p>The <code>remove</code> command removes a subscription from the system. (This does not uninstall the associated products.) </p>
<dl>
<dt><code>&#8211;serial=SERIALNUMBER</code></p>
<dd>Gives the serial number of the subscription certificate for the specific product to remove from the system. Subscription certificates attached to a system are in a certificate, in <code>/etc/pki/entitlement/&lt;serial_number&gt;.pem.</code> To remove multiple subscriptions, use the <code>&#8211;serial</code> option multiple times. </p>
<dt><code>&#8211;pool=POOLID</code></p>
<dd>Removes all subscription certificates for the specified pool id from the system. To remove multiple sets of subscriptions, use the <code>&#8211;pool</code> option multiple times. </p>
<dt><code>&#8211;all</code></p>
<dd>Removes <i>all</i> of the subscriptions attached to a system. </p>
</dl>
<h3>Release Options</h3>
<p>The <code>release</code> command sets a sticky OS version to use when installing or updating packages. This sets a preference for the minor version of the OS, such as 6.2 or 6.3. This can prevent unplanned or unsupported operating system version upgrades when an IT environment must maintain a certified configuration. </p>
<dl>
<dt><code>&#8211;list</code></p>
<dd>Lists the available OS versions. If a release preference is not set, then there is a message saying it is not set. </p>
<dt><code>&#8211;set=RELEASE</code></p>
<dd>Sets the minor (Y-stream) release version to use, such as 6.3. </p>
<dt><code>&#8211;unset</code></p>
<dd>Removes any previously set release version preference. </p>
</dl>
<h3>Service-Level Options</h3>
<p>The <code>service-level</code> command displays the current configured service level <i>preference</i> for products installed on the system. For example, if the service-level preference is standard, then a subscription with a standard service level is selected when auto-attaching subscriptions to the system. </p>
<dl>
<dt><code>&#8211;serverurl=SERVER_URL</code></p>
<dd>Server URL in the form of <a rel="nofollow" href="https://hostname:port/prefix">https://hostname:port/prefix</a> </p>
<dt><code>&#8211;insecure</code></p>
<dd>Do not check the server SSL certificate against available certificate authorities </p>
<dt><code>&#8211;show</code></p>
<dd>Shows the system&#8217;s current service-level preference. If a service level is not set, then there is a message saying it is not set. </p>
<dt><code>&#8211;list</code></p>
<dd>Lists the available service levels. </p>
<dt><code>&#8211;set=SERVICE_LEVEL</code></p>
<dd>Service level to apply to this system </p>
<dt><code>&#8211;unset</code></p>
<dd>Removes any previously set service-level preference. </p>
</dl>
<h3>Import Options</h3>
<p>The <code>import</code> command imports and applies a subscription certificate for the system which was generated externally, such as in the Customer Portal, and then copied over to the system. Importing can be necessary if a system is preconfigured in the subscription management service or if it is offline or unable to access the subscription management service but it has the proper, relevant subscriptions attached to the system. </p>
<dl>
<dt><code>&#8211;certificate=CERTIFICATE_FILE</code></p>
<dd>Points to a certificate PEM file which contains the subscription certificate. This can be used multiple times to import multiple subscription certificates. </p>
</dl>
<h3>Redeem Options</h3>
<p>The <code>redeem</code> command is used for systems that are purchased from third-party vendors that include a subscription. The redemption process essentially auto-attaches the preselected subscription that the vendor supplied to the system. </p>
<dl>
<dt><code>&#8211;email=EMAIL</code></p>
<dd>Gives the email account to send the redemption notification message to. </p>
<dt><code>&#8211;locale=LOCALE</code></p>
<dd>Sets the locale to use for the message. If none is given, then it defaults to the local system&#8217;s locale. </p>
<dt><code>&#8211;org=ORG</code></p>
<dd>Identifies the organization which issued the subscription being redeemed. </p>
</dl>
<h3>List Options</h3>
<p>The <code>list</code> command lists all of the subscriptions that are compatible with a system. The options allow the list to be filtered by subscriptions that are used by the system or unused subscriptions that are available to the system. </p>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Lists all possible subscriptions that have been purchased, even if they don&#8217;t match the architecture of the system. This is used with the <code>&#8211;available</code> option. </p>
<dt><code>&#8211;available</code></p>
<dd>Lists available subscriptions which are not yet attached to the system. </p>
<dt><code>&#8211;consumed</code></p>
<dd>Lists all of the subscriptions currently attached to the system. </p>
<dt><code>&#8211;installed</code></p>
<dd>Lists products which are currently installed on the system which may (or may not) have subscriptions associated with them, as well as products with attached subscriptions which may (or may not) be installed. </p>
<dt><code>&#8211;ondate=YYYY-MM-DD</code></p>
<dd>Sets the date to use to search for active and available subscriptions. The default (if not explicitly passed) is today&#8217;s date; using a later date looks for subscriptions which will be active then. This is only used with the <code>&#8211;available</code> option. </p>
<dt><code>&#8211;no-overlap</code></p>
<dd>Shows pools which provide products that are not already covered; only used with <code>&#8211;available</code> option. </p>
<dt><code>&#8211;match-installed</code></p>
<dd>Shows only subscriptions matching products that are currently installed; only used with <code>&#8211;available</code> option. </p>
<dt><code>&#8211;matches=SEARCH</code></p>
<dd>Limits the output of &#8211;installed, &#8211;available and &#8211;consumed to only subscriptions or products which contain SEARCH in the subscription or product information, varying with the list requested and the server version.<br />
 SEARCH may contain the wildcards ? or * to match a single character or zero or more characters, respectively. The wildcard characters may be escaped with a backslash to represent a literal question mark or asterisk. Likewise, to represent a backslash, it must be escaped with another backslash. </p>
<dt><code>&#8211;pool-only</code></p>
<dd>Limits the output of &#8211;available and &#8211;consumed such that only the pool IDs are displayed. No labels or errors will be printed if this option is specified. </p>
</dl>
<h3>Refresh Options</h3>
<p>The <code>refresh</code> command pulls the latest subscription data from the server. Normally, the system polls the subscription management service at a set interval (4 hours by default) to check for any changes in the available subscriptions. The <code>refresh</code> command checks with the subscription management service right then, outside the normal interval. </p>
<p> This command has no options.</p>
<h3>Environments Options</h3>
<p>The <code>environments</code> command lists all of the environments that have been configured for an organization. This command is only used for organizations which have a locally-hosted subscription or content service of some kind, like Subscription Asset Manager. The concept of environments &#8212; and therefore this command &#8212; have no meaning for environments which use the Customer Portal Subscription Management services. </p>
<dl>
<dt><code>&#8211;username=USERNAME</code></p>
<dd>Gives the username for the account to use to connect to the organization account. </p>
<dt><code>&#8211;password=PASSWORD</code></p>
<dd>Gives the user account password. </p>
<dt><code>&#8211;org=ORG</code></p>
<dd>Identifies the organization for which to list the configured environments. </p>
</dl>
<h3>Repos Options</h3>
<p>The <code>repos</code> command lists all of the repositories that are available to a system. This command is only used for organizations which have a locally-hosted content service of some kind, like Subscription Asset Manager. With Red Hat&#8217;s hosted content service, there is only one central repository. </p>
<dl>
<dt><code>&#8211;list</code></p>
<dd>Lists all of the repositories that are provided by the content service used by the system. </p>
<dt><code>&#8211;list-enabled</code></p>
<dd>Lists all of the enabled repositories that are provided by the content service used by the system. </p>
<dt><code>&#8211;list-disabled</code></p>
<dd>Lists all of the disabled repositories that are provided by the content service used by the system. </p>
<dt><code>&#8211;enable=REPO_ID</code></p>
<dd>Enables the specified repository, which is made available by the content sources identified in the system subscriptions. To enable multiple repositories, use this argument multiple times. Wild cards * and ? are supported. </p>
<dt><code>&#8211;disable=REPO_ID</code></p>
<dd>Disables the specified repository, which is made available by the content sources identified in the system subscriptions. To disable multiple repositories, use this argument multiple times. Wild cards * and ? are supported. </p>
</dl>
<h3>Orgs Options</h3>
<p>The <code>orgs</code> command lists all of the organizations which are available to the specified user account. A multi-tenant infrastructure may have multiple organizations within a single customer, and users may be restricted to access only a subset of the total number of organizations. </p>
<dl>
<dt><code>&#8211;username=USERNAME</code></p>
<dd>Gives the username for the account to use to connect to the organization account. </p>
<dt><code>&#8211;password=PASSWORD</code></p>
<dd>Gives the user account password. </p>
<dt><code>&#8211;serverurl=SERVER_HOSTNAME</code></p>
<dd>Passes the name of the subscription service to use to list all available organizations. The <code>orgs</code> command will list all organizations for the specified service for which the user account is granted access. The default value, if this is not given, is the Customer Portal Subscription Management service, <code><a rel="nofollow" href="https://subscription.rhsm.redhat.com:443.">https://subscription.rhsm.redhat.com:443.</a></code> If there is an on-premise subscription service such as Subscription Asset Manager, this parameter can be used to submit the hostname of the subscription service, in the form <i>[protocol://]servername[:port][/prefix]</i>. For Subscription Asset Manager, if the Subscription Manager tool is configured with the Subscription Asset Manager RPM, then the default value for the <code>&#8211;serverurl</code> parameter is for the on-premise Subscription Asset Manager server. </p>
</dl>
<h3>Plugin Options</h3>
<p>The <code>plugins</code> command lists the available subscription-manager plugins. </p>
<dl>
<dt><code>&#8211;list</code></p>
<dd>List the available subscription-manager plugins. </p>
<dt><code>&#8211;listslots</code></p>
<dd>List the available plugin slots </p>
<dt><code>&#8211;listhooks</code></p>
<dd>List the available plugin slots and the hooks that handle them. </p>
<dt><code>&#8211;verbose</code></p>
<dd>Show additional info about the plugins, such as the plugin configuration values. </p>
</dl>
<h3>Repo-Override Options</h3>
<p>The <code>repo-override</code> command allows the user to manage custom content repository settings </p>
<dl>
<dt><code>&#8211;repo</code></p>
<dd>The repository to modify (can be specified more than once) </p>
<dt><code>&#8211;add=NAME:VALUE</code></p>
<dd>Adds a named override with the provided value to repositories specified with the <code>&#8211;repo</code> option </p>
<dt><code>&#8211;remove=NAME</code></p>
<dd>Removes a named override from the repositories specified with the <code>&#8211;repo</code> option </p>
<dt><code>&#8211;remove-all</code></p>
<dd>Removes all overrides from repositories specified with the <code>&#8211;repo</code> option </p>
<dt><code>&#8211;list</code></p>
<dd>Lists all overrides from repositories specified with the <code>&#8211;repo</code> option </p>
</dl>
<h3>Identity Options</h3>
<p>The <code>identity</code> command handles the UUID of a system, which identifies the system to the subscription management service after registration. This command can simply return the UUID or it can be used to restore the registration of a previously-registered system to the subscription management service. </p>
<dl>
<dt><code>&#8211;regenerate</code></p>
<dd>Requests that the subscription management service issue a new identity certificate for the system, using an existing UUID in the original identity certificate. If this is used alone, then the <code>identity</code> command also uses the original identity certificate to bind to the subscription management service, using certificate-based authentication. </p>
<dt><code>&#8211;username=USERNAME</code></p>
<dd>Gives the username for the account which is registering the system; this user account is usually tied to the user account for the content delivery system which supplies the content. Optional, for user-based authentication. </p>
<dt><code>&#8211;password=PASSWORD</code></p>
<dd>Gives the user account password. Optional, for user-based authentication. </p>
<dt><code>&#8211;force</code></p>
<dd>Regenerates the identity certificate for the system using username/password authentication. This is used with the <code>&#8211;regenerate</code> option. <code>&#8211;regenerate</code> alone will use an existing identity certificate to authenticate to the subscription management service. If the certificate is missing or corrupted or in other circumstances, then it may be better to use user authentication rather than certificate-based authentication. In that case, the <code>&#8211;force</code> option requires the username or password to be given either as an argument or in response to a prompt. </p>
</dl>
<h3>Facts Options</h3>
<p>The <code>facts</code> command lists the system information, like the release version, number of CPUs, and other architecture information. </p>
<dl>
<dt><code>&#8211;list</code></p>
<dd>Lists the system information. These are simple <i>attribute: value</i> pairs that reflect much of the information in the <code>/etc/sysconfig</code> directory </p>
<pre>cpu.architecture: x86_64
cpu.core(s)_per_socket: 1
cpu.cpu(s): 2
cpu.cpu_family: 6
cpu.cpu_mhz: 1861.776
cpu.cpu_op-mode(s): 64-bit
cpu.cpu_socket(s): 2
cpu.hypervisor_vendor: KVM
cpu.model: 2
cpu.numa_node(s): 1
cpu.numa_node0_cpu(s): 0,1
cpu.stepping: 3
cpu.thread(s)_per_core: 1
cpu.vendor_id: GenuineIntel
cpu.virtualization_type: full
distribution.id: Santiago
distribution.name: Red Hat Enterprise Linux Workstation
distribution.version: 6.1
----</pre>
<dt><code>&#8211;update</code></p>
<dd>Updates the system information. This is particularly important whenever there is a hardware change (such as adding a CPU) or a system upgrade because these changes can affect the subscriptions that are compatible with the system. </p>
</dl>
<h3>Clean Options</h3>
<p>The <code>clean</code> command removes all of the subscription and identity data from the local system <i>without affecting the system information in the subscription management service.</i> This means that any of the subscriptions applied to the system are not available for other systems to use. The <code>clean</code> command is useful in cases where the local subscription information is corrupted or lost somehow, and the system will be re-registered using the <code>register &#8211;consumerid=EXISTING_ID</code> command. </p>
<p> This command has no options.</p>
<h3>Config Options</h3>
<p>The <code>config</code> command changes the <code>rhsm.conf</code> configuration file used by Subscription Manager. Almost all of the connection information used by Subscription Manager to access the subscription management service, content server, and any proxies is set in the configuration file, as well as general configuration parameters like the frequency Subscription Manager checks for subscriptions updates. There are major divisions in the <code>rhsm.conf</code> file, such as <code>[server]</code> which is used to configure the subscription management service. When changing the Subscription Manager configuration, the settings are identified with the format <i>section.name</i> and then the new value. For example: </p>
<dl>
<dd>
<pre>server.hostname=newsubscription.example.com</pre>
</dl>
<dl>
<dt><code>&#8211;list</code></p>
<dd>Prints the current configuration for Subscription Manager. </p>
<dt><code>&#8211;remove=section.name</code></p>
<dd>Deletes the current value for the parameter without supplying a new parameter. A blank value tells Subscription Manager to use service default values for that parameter. If there are no defaults, then the feature is ignored. </p>
<dt><code>&#8211;section.name=VALUE</code></p>
<dd>Sets a parameter to a new, specified value. This is commonly used for connection settings:</p>
<dd>* server.hostname (subscription management service)</p>
<dd>* server.proxy</p>
<dd>* server.proxy_port</p>
<dd>* server.proxy_user</p>
<dd>* server.proxy_password</p>
<dd>* rhsm.baseurl (content server)</p>
<dd>* rhsm.certFrequency </p>
</dl>
<h3>Version Options</h3>
<p>The <code>version</code> command displays information about the current Subscription Manager package, the subscription service the system is registered to (if it is currently registered), and the subscription management server that the system is configured to use. For example: </p>
<dl>
<dd>
<pre>[root [at] server ~]# subscription-manager version
server type: Red Hat Subscription Management
subscription management server: 0.9.18-1
subscription management rules: 5.9
subscription-manager: 1.12.1-1.git.28.5cd97a5.fc20
python-rhsm: 1.11.4-1.git.1.2f38ded.fc20</pre>
</dl>
<p> This command has no options.</p>
<h3>Status Options</h3>
<p>The <code>status</code> command shows the current status of the products and attached subscriptions for the system. If some products are not fully covered or subscriptions have expired, then the <code>status</code> command shows why subscriptions are not current and returns an error code. </p>
<dl>
<dd>
<pre>[root [at] server ~]# subscription-manager status
+-------------------------------------------+
 System Status Details
+-------------------------------------------+
Overall Status: Current</pre>
</dl>
<dl>
<dt><code>&#8211;ondate=DATE</code></p>
<dd>Shows the system status for a specific date <i>in the future</i>. The format of the date is <i>YYYY-MM-DD</i>. </p>
<dl>
<dd>
<pre>[root [at] server ~]# subscription-manager status --ondate=2014-01-01
+-------------------------------------------+
 System Status Details
+-------------------------------------------+
Overall Status: Insufficient</pre>
</dl>
</dl>
<h3>Deprecated Commands</h3>
<p>As the structures of subscription configuration have changed, some of the original management commands have become obsolete. These commands have been replaced with updated commands. </p>
<dl>
<dt><code>subscribe</code></p>
<dd>This has been replaced with attach. A similar registration option, <code>&#8211;subscribe</code>, has also be replaced with <code>&#8211;auto-attach</code>. </p>
<dt><code>unsubscribe</code></p>
<dd>This has been replaced with <code>remove</code>. </p>
<dt><code>activate</code></p>
<dd>This has been replaced with <code>redeem</code>. </p>
</dl>
<h2>Usage</h2>
<p><code>subscription-manager</code> has two major tasks: </p>
<dl>
<dd>1. Handling the registration for a given system to a subscription management service </p>
<dd>2. Handling the product subscriptions for installed products on a system </p>
</dl>
<p> <code>subscription-manager</code> makes it easier for network administrators to maintain parity between software subscriptions and updates and their installed products by tracking and managing what subscriptions are attached to a system and when those subscriptions expire or are exceeded.</p>
<h3>Registering And Unregistering Machines</h3>
<p>A system is either <i>registered</i> to a subscription management service &#8212; which makes all of the subscriptions available to the system &#8212; or it is not registered. Unregistered systems necessarily lack valid software subscriptions because there is no way to record that the subscriptions have been used nor any way to renew them. </p>
<p> The default subscription management service in the Subscription Manager configuration is the Customer Portal Subscription Management service. The configuration file can be edited before the system is registered to point to an on-premise subscription management service like Subscription Asset Manager. </p>
<p> Systems are usually registered to a subscription management service as part of their initial configuration, such as the firstboot or kickstart process. However, systems can be registered manually after they are configured, can be removed from a content service, or re-registered. </p>
<p> If a system has never been registered (not even during firstboot), then the <code>register</code> command will register the system with whatever subscription management service is configured in the <code>/etc/rhsm/rhsm.conf</code> file. This command requires, at a minimum, the username and password for an account to connect to the subscription management service. If the credentials aren&#8217;t passed with the command, then <code>subscription-manager</code> prompts for the username and password interactively. </p>
<p> When there is a single organization or when using the Customer Portal Subscription Management service, all that is required is the username/password set. For example: </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin --password=secret</pre>
</dl>
<p> With on-premise subscription services, such as Subscription Asset Manager, the infrastructure is more complex. The local administrator can define independent groups called <i>organizations</i> which represent physical or organizational divisions (<code>&#8211;org</code>). Those organizations can be subdivided into <i>environments</i> (<code>&#8211;environment</code>). Optionally, the information about what subscription service (<code>&#8211;serverurl</code>) and content delivery network (<code>&#8211;baseurl</code>) to use for the system registration can also be passed (which overrides the Red Hat Subscription Manager settings). The server and content URLs are usually configured in the Subscription Manager configuration before registering a system. </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin --password=secret
--org=&quot;IT Dept&quot; --environment=&quot;local dev&quot; --serverurl=local-cloudforms.example.com --baseurl=<a rel="nofollow" href="https://local-cloudforms.example.com:8088/cfFe">https://local-cloudforms.example.com:8088/cfFe</a></pre>
</dl>
<p> If a system is in a multi-tenant environment and the organization is <i>not</i> provided with the registration request, registration fails with a remote server error. In the <code>rhsm.log,</code> there will be errors about being unable to load the owners interface. </p>
<p> Some information is assigned automatically. Subscription Manager automatically generates a unique ID for the system which is used by the subscription management service and it assigns a unit type, which indicates what kinds of software are available for the system. The name for the entry can be manually assigned (for use within an on-premise subscription service, for instance). A handful of subscriptions (such as specialized servers for content or identity management) have their own specific unit type. For example: </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin
--password=secret --type=system --name=server1
--org=&quot;IT Dept&quot;</pre>
</dl>
<p> If a system is registered and then somehow its subscription information is lost &#8212; a drive crashes or the certificates are deleted or corrupted &#8212; the system can be re-registered, with all of its subscriptions restored, by registering with the existing ID. </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin
--password=secret --consumerid=1234abcd</pre>
</dl>
<p> A system uses an SSL client certificate (its identity certificate) to authenticate to the subscriptions system to check for updates or changes to subscriptions. If the identity certificate is lost or corrupted, it can be regenerated using the <code>identity</code> command. </p>
<dl>
<dd>
<pre>subscription-manager identity --regenerate</pre>
</dl>
<p> Using the <code>&#8211;force</code> option will prompt for the username and password for the account, if one isn&#8217;t given, and then return the new inventory ID and the hostname of the registered system. </p>
<pre>subscription-manager identity --force
Username: jsmith
Password:
eff9a4c9-3579-49e5-a52f-83f2db29ab52 server.example.com</pre>
<p>A system is unregistered and removed from the subscription management service simply by running the <code>unregister</code> command. Unregistering a system and removing its attached subscriptions can free up subscriptions when a system is taken offline or moved to a different department. </p>
<dl>
<dd>
<pre>subscription-manager unregister</pre>
</dl>
<p> An option with registration, <code>&#8211;auto-attach,</code> will automatically attach the subscriptions pool which best matches the system architecture and configuration to the newly-registered system. This option attaches subscriptions as part of the registration process, rather than separately managing subscriptions. </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin --password=secret
--auto-attach</pre>
</dl>
<p> Auto-attach also supports an option to set a preferred service level with the selected subscriptions, the <code>&#8211;servicelevel</code> option. In this case, the <code>&#8211;servicelevel</code> option sets a preference that helps the auto-attach process select appropriate subscriptions. For example, if the preferred service level for a production server is premium, and there are three matching subscriptions with different service levels (none, standard, and premium), the auto-attach process selects the subscription which offers a premium service level. </p>
<dl>
<dd>
<pre>subscription-manager register --username=admin --password=secret
--auto-attach --servicelevel=premium</pre>
</dl>
<h3>Listing, Attaching, And Removing Subscriptions For Products</h3>
<p>A <i>subscription</i> is essentially the right to install, use, and receive updates for a Red Hat product. (Sometimes multiple individual software products are bundled together into a single subscription.) When a system is registered, the subscription management service is aware of the system and has a list of all of the possible product subscriptions that the system can install and use. A subscription is applied to a system when the system is <i>attached</i> to the subscription pool that makes that product available. A system releases or <i>removes</i> that subscription (meaning, it removes that subscription so that another system can use that subscription count). </p>
<p> <code>list</code> command shows you what subscriptions are available specifically to the system (meaning subscriptions which are active, have available quantities, and match the hardware and architecture) or all subscriptions for the organization. Using the <code>&#8211;ondate</code> option shows subscriptions that are or will be active at a specific time (otherwise, it shows subscriptions which are active today). </p>
<dl>
<dd>
<pre>subscription-manager list --available --ondate=2012-01-31
+-------------------------------------------+
 Available Subscriptions
+-------------------------------------------+
Subscription Name: Red Hat Enterprise Linux
SKU: SYS0395
Pool Id: 8a85f981302cbaf201302d899adf05a9
Quantity: 249237
Service Level: None
Service Type: None
Multi-Entitlement: No
Ends: 01/01/2022
Machine Type: physical</pre>
</dl>
<p> The <code>list</code> command can also be used to show what products you currently have installed, as a way of tracking what products you have versus what subscriptions you have on the system. </p>
<dl>
<dd>
<pre>subscription-manager list --installed
+-------------------------------------------+
 Installed Product Status
+-------------------------------------------+
ProductName: Red Hat Enterprise Linux Server
Product ID: 69
Version: 6.3
Arch: x86_64
Status: Subscribed
Started: 07/26/2012
Ends: 08/31/2015</pre>
</dl>
<p> The <code>list</code> can be filtered to only include products or subscriptions that match the query string provided to <code>&#8211;matches</code> option. </p>
<dl>
<dd>
<pre>subscription-manager list --installed --matches=&quot;*Server*&quot;
+-------------------------------------------+
 Installed Product Status
+-------------------------------------------+
ProductName: Red Hat Enterprise Linux Server
Product ID: 69
Version: 6.3
Arch: x86_64
Status: Subscribed
Started: 07/26/2012
Ends: 08/31/2015</pre>
</dl>
<p> Attaching a subscription requires the ID for the subscription pool (the <i>&#8211;pool</i> option). For example: </p>
<dl>
<dd>
<pre>subscription-manager attach
--pool=ff8080812bc382e3012bc3845da100d2</pre>
</dl>
<p> As with the <code>register</code> command, the system can be auto-attached to the best-fitting subscriptions. This is the default action and is equivalent to using the <code>&#8211;auto</code> option: </p>
<dl>
<dd>
<pre>subscription-manager attach</pre>
</dl>
<p> Auto-attach also supports an option to set a preferred service level with the selected subscriptions, the <code>&#8211;servicelevel</code> option. In this case, the <code>&#8211;servicelevel</code> option sets a preference that helps the auto-attach process select appropriate subscriptions. For example, if the preferred service level for a production server is premium, and there are three matching subscriptions with different service levels (none, standard, and premium), the auto-attach process selects the subscription which offers a premium subscription. </p>
<dl>
<dd>
<pre>subscription-manager attach --servicelevel=premium</pre>
</dl>
<p> Some subscriptions define a count based on attributes of the system itself, like the number of sockets or the number of virtual guests on a host. You can combine multiple subscriptions together to cover the count. For example, if there is a four socket server, you can use two subscriptions for &quot;RHEL Server for Two Sockets&quot; to cover the socket count. To specify the number of subscriptions to use, use the <code>&#8211;quantity</code> option. For example: </p>
<dl>
<dd>
<pre>subscription-manager attach
--pool=ff8080812bc382e3012bc3845da100d2
--quantity=2</pre>
</dl>
<p> Removing subscription from a system releases the subscription back into the pool. The system remains registered with the subscription management service. Each product has an identifying X.509 certificate installed with it. To remove a subscription for a specific product, specify the serial number (or numbers, in multiple <code>&#8211;serial</code> options) of the certificate: </p>
<dl>
<dd>
<pre>subscription-manager remove --serial=1128750306742160</pre>
</dl>
<p> Giving the <code>remove</code> command with the <code>&#8211;all</code> option removes every subscription the system has used.</p>
<h3>Redeeming Existing Subscriptions</h3>
<p>Sometimes, a system may come preconfigured with products and subscriptions. Rather than attaching a pool and claiming a subscription, this system simply needs to <i>redeem</i> its existing subscriptions. </p>
<p> After registration, subscriptions on preconfigured systems can be claimed using the <code>redeem</code> command, which essentially auto-attaches the system to its preexisting subscriptions. </p>
<dl>
<dd>
<pre>subscription-manager redeem --email=admin [at] example.com --org=&quot;IT Dept&quot;</pre>
</dl>
<h3>VIEWING LOCAL SUBSCRIPTION &amp; CONTENT PROVIDER INFORMATION</h3>
<p>Red Hat has a hosted environment, through the Customer Portal, that provides centralized access to subscription management and content repositories. However, organizations can use other tools &#8212; like Subscription Manager &#8212; for content hosting and subscription management. With a local content provider, the organization, environments, repositories, and other structural configuration is performed in the content provider. Red Hat Subscription Manager can be used to display this information, using the <code>environments, orgs,</code> and <code>repos</code> commands. </p>
<dl>
<dd>
<pre>subscription-manager repos --list
subscription-manager environments --username=jsmith
--password=secret --org=prod
subscription-manager orgs --username=jsmith
--password=secret</pre>
</dl>
<h3>Changing Subscription Manager Configuration</h3>
<p>The Subscription Manager CLI and GUI both use the <code>/etc/rhsm/rhsm.conf</code> file for configuration, including what content and subscription management services to use and management settings like auto-attaching. This configuration file can be edited directly, or it can be edited using the <code>config</code> command. Parameters and values are passed as arguments with the <code>config</code> command in the format <i>&#8211;section.parameter=value</i> , where <i>section</i> is the configuration section in the file: server, rhsm, rhsmcertd or logging. </p>
<p> For example, to change the hostname of the subscription management service host: </p>
<dl>
<dd>
<pre>subscription-manager config --server.hostname=myserver.example.com</pre>
</dl>
<p> The entries in the <code>logging</code> section are somewhat special. The keys in this section are a name of a logger. The values are the logging level. </p>
<p> Valid levels are one of: <code>DEBUG</code> , <code>INFO</code> , <code>WARNING</code> , <code>ERROR</code> , or <code>CRITICAL</code> </p>
<p> Valid logger names are the full module path of any Subscription Manager module. For example: <code>subscription_manager</code> or subscription_manager.managercli </p>
<p> There are three main top-level loggers: subscription_manager, rhsm, and rhsm-app. All logger names begin with one of the above. </p>
<p> To set the default log level for all loggers (that are not otherwise set in the logging section), edit the <code>default_log_level</code> key in /etc/rhsm/rhsm.conf</p>
<h3>Updating Facts</h3>
<p>The information about a system, such as its hardware and CPU, its operating system versions, and memory, are collected by Subscription Manager in a list of <i>facts.</i> Subscription Manager uses these facts to determine what purchased subscriptions are compatible with the system. Whenever these facts change (such as installing an additional CPU), the facts can be updated immediately using the <code>facts</code> command. </p>
<dl>
<dd>
<pre>subscription-manager facts --update</pre>
</dl>
<p> The collected facts can also be overridden by creating a JSON file in the <code>/etc/rhsm/facts/</code> directory. These have simple formats that define a fact and value: </p>
<dl>
<dd>
<pre>{&quot;fact1&quot;: &quot;value1&quot;,&quot;fact2&quot;: &quot;value2&quot;}</pre>
</dl>
<p> Any fact override file must have a <code>.facts</code> extension. </p>
<p> When these fact files are added, running the <code>facts</code> command will update the collected facts with the new, manual facts or values.</p>
<h3>Subscriptions And Kickstart</h3>
<p>The <code>subscription-manager</code> tool can be run as a post-install script as part of the kickstart installation process. This allows subscription management (registering and applying subscriptions) to be automated along with installation. For example: </p>
<dl>
<dd>
<pre>%post --log=/root/ks-post.log
/usr/sbin/subscription-manager register --username admin --password secret --org 'east colo' --auto-attach --servicelevel=premium --force</pre>
</dl>
<h2>Network Information</h2>
<p>The <code>subscription-manager</code> tool uses outgoing HTTPS requests. In the default configuration it will use HTTPS on port 443 to the subscription servers <code>subscription.rhsm.redhat.com</code> and to the content delivery service <code>cdn.redhat.com.</code> </p>
<p> For information about the network addresses that <code>subscription-manager</code> and the <code>subscription-manager yum plugin</code> use see <a rel="nofollow" href="https://access.redhat.com/site/articles/414963">https://access.redhat.com/site/articles/414963</a></p>
<h2>Files</h2>
<dl>
<dd>* /etc/pki/consumer/*.pem</p>
<dd>* /etc/pki/entitlement/&lt;serial&gt;.pem</p>
<dd>* /etc/pki/product/*.pem</p>
<dd>* /etc/rhsm/rhsm.conf</p>
<dd>* /etc/rhsm/facts/*.facts </p>
</dl>
<h2>Authors</h2>
<p>Deon Lackey, &lt;dlackey [at] redhat.com&gt;, and Pradeep Kilambi, &lt;pkilambi [at] redhat.com&gt;</p>
