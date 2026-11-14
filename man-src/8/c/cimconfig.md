---
title: "cimconfig(8)"
name: "cimconfig"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimconfig/"
description: "cimconfig – get, set, unset, or list CIM Server configuration properties"
---

<p>cimconfig &#8211; get, set, unset, or list CIM Server configuration properties</p>
<h2>Synopsis</h2>
<p><code>cimconfig</code> <code>-g</code> name [ <code>-c</code> ] [ <code>-d</code> ] [ <code>-p</code> ] <code>cimconfig</code> <code>-s</code> name=value [ <code>-c</code> ] [ <code>-p</code> ] <code>cimconfig</code> <code>-u</code> name [ <code>-c</code> ] [ <code>-p</code> ] <code>cimconfig</code> <code>-l</code> [ <code>-c</code> | <code>-p</code> ] <code>cimconfig</code> <code>-h</code> <code>cimconfig</code> <code>&#8211;help</code> <code>cimconfig</code> <code>&#8211;H name</code> | <code>&quot;All&quot;</code> <code>cimconfig</code> <code>&#8211;version</code> </p>
<h2>Description</h2>
<p>The <code>cimconfig </code> command manages CIM Server configuration properties. The operations are executed on the local host by submitting requests to the CIM Server. An operation on a current configuration property takes effect immediately, and an operation on a planned configuration property takes effect the next time the CIM Server is started with <code>cimserver (8) .</code> Modifications to a configuration property via <code>cimconfig </code> remain in effect until changed via another <code>cimconfig </code> command. Configuration properties may also be modified temporarily via the <code>cimserver (8)</code> command, in which case, the modification of the configuration property remains in effect for that execution of the <code>cimserver (8)</code> command only. A default value is associated with each configuration property. Each configuration property is initially assigned its default value, until modified by a <code>cimconfig </code> command or <code>cimserver (8)</code> command. Dynamic configuration properties are those whose current values may be set while the CIM server is running. The following configuration properties are available: <code>authorizedUserGroups</code></p>
<dl>
<dd><code>Description:</code> If set, the value is interpreted as a list of comma-separated user groups whose members may issue CIM requests. A user who is not a member of any of these groups is restricted from issuing CIM requests, with the exception of privileged users (superuser). If unset, any user may issue CIM requests. Note: This configuration property operates in conjunction with other CIM request authorization conditions rather than overriding them.</p>
<dd><code>Default Value: </code>(None)</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableAssociationTraversal</code></p>
<dl>
<dd><code>Description:</code> If True, the CIM Server will support the four association traversal operators: Associators, AssociatorNames, References, and ReferenceNames.</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableAuditLog</code></p>
<dl>
<dd><code>Description:</code> If True, audit log entries for certain types of CIM Server activities will be written to the system log. Examples of audited activities include a CIM Server configuration change, a Provider registration change, an authentication attempt and a modification to the CIM Schema or a CIM Instance. An audit log entry describes the who, what, and when associated with an audited activity.</p>
<dd><code>Default Value: </code>False</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>enableIndicationService</code></p>
<dl>
<dd><code>Description:</code> If True, the CIM Server will support CIM Indications.</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableHttpConnection</code></p>
<dl>
<dd><code>Description:</code> If True, allows connections to the CIM Server using the HTTP protocol</p>
<dd><code>Default Value: </code>False</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableHttpsConnection</code></p>
<dl>
<dd><code>Description:</code> If True, allows connections to the CIM Server using the HTTPS protocol (HTTP using Secure Socket Layer encryption)</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableNamespaceAuthorization</code></p>
<dl>
<dd><code>Description:</code> If True, the CIM Server restricts access to namespaces based on configured user authorizations [user authorizations may be configured using <code>cimauth (8)</code> ]</p>
<dd><code>Default Value: </code>False</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableRemotePrivilegedUserAccess</code></p>
<dl>
<dd><code>Description:</code> If True, the CIM Server allows access by a privileged user from a remote system. Many management operations require privileged user access. Disabling remote access by privileged user could significantly affect functionality</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>enableSubscriptionsForNonprivilegedUsers</code></p>
<dl>
<dd><code>Description:</code> If True, nonprivileged user of the system will be allowed to manipulate indication subscriptions, indication filters, and listener destination instances otherwise privileged access is required.</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>forceProviderProcesses</code></p>
<dl>
<dd><code>Description:</code> If true, the CIM Server runs Providers in separate processes rather than loading and calling Provider libraries directly within the CIM Server process.</p>
<dd><code>Default Value: </code>True</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>hostname</code></p>
<dl>
<dd><code>Description:</code> Can be used to override the local system supplied hostname (without domain) the CIM Server uses to build objects. If not set, querying this configuration option will report the system supplied hostname and behavior is not changed. Setting this value to a valid hostname on CIM Server startup or as planned value will force the server to assume the configured name as the local hosts name. Setting this allows the administrator to set the name that operations such as associator, reference etc. return with object paths. When setting this option, <code>fullyQualifiedHostName</code> should be set also.</p>
<dd>In common setups it is not recommended to explicitly set this value. Some scenarios scenarios in which changing the default value makes sense include:</p>
<dd>&#8211; The case where what the CIM Server shall return to clients for host name is NOT the name of the current host but some administrator defined name (ex. system behind a firewall or some redirector).</p>
<dd>&#8211; Embedded systems that have a system set hostname which is not valid and needs to be overridden by CIM administrator without changing the actual IP configuration.</p>
<dd><code>Default Value: </code>(blank)</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>fullyQualifiedHostName</code></p>
<dl>
<dd><code>Description:</code> Can be used to override the local system supplied fully qualified hostname (with domain) the CIM Server is using to build objects. If not set, querying this configuration option will report the system supplied fully qualified hostname and behavior is not changed. Setting this value to a valid hostname on CIM Server startup or as planned value will force the server to assume the configured name as the local hosts name with domain. Setting this allows the administrator to set the name that indication operations and the CIM_ObjectManager assume for SystemName returned as instance and key properties.</p>
<dt>In</p>
<dd>Some scenarios scenarios in which changing the default value makes sense include:</p>
<dd>&#8211; The case where what the CIM Server shall return to clients for host name is NOT the name of the current host but some administrator defined name (ex. system behind a firewall or some redirector).</p>
<dd>&#8211; Embedded systems that have a system set hostname which is not valid and needs to be overridden by CIM administrator without changing the actual IP configuration.</p>
<dd><code>Default Value: </code>(blank)</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>idleConnectionTimeout</code></p>
<dl>
<dd><code>Description:</code> If set to a positive integer, this value specifies a minimum timeout value for idle client connections. If set to zero, idle client connections do not time out.</p>
<dd>A client connection is considered idle when it is not in the process of sending a request and the CIM Server is not processing a request from that connection. An idle connection timeout allows reclamation of the system resources allocated for idle CIM Server connections. Note that the CIM Server may allow an idle connection to persist longer than the configured timeout value based on server activity.</p>
<dd>Some client applications may not behave correctly if a connection timeout is introduced. Client compatibility should be considered when configuring an idle connection timeout value. The idle connection time is computed using the system clock. Thus, resetting the system clock may cause unexpected timeout behavior.</p>
<dd><code>Default Value: </code>0</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>listenAddress</code></p>
<dl>
<dd><code>Description:</code> Network interfaces, if specified, <code><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8) </code> should listen to for connection requests. It accepts a comma seperated list(without space) of network interfaces. Both ipv4 and ipv6 addresses is accepted. Default value of &quot;All&quot; make cimserver to listen to all the available network interfaces. Examples include:</p>
<dd><code>&#8211;</code>listenAddress=All</p>
<dd><code>&#8211;</code>listenAddress=121.12.33.112</p>
<dd><code>&#8211;</code>listenAddress=121.33.21.26,127.0.0.1,fe80::fe62:9346%eth0</p>
<dd><code>Default Value: </code>All</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No  <code>maxFailedProviderModuleRestarts</code></p>
<dl>
<dd><code>Description:</code> If set to a positive integer, this value specifies the number of times a failed provider module with indications enabled are restarted automatically before being moved to Degraded state. If set to zero, failed provider module is not restarted with indications enabled automatically and will be moved to Degraded state immediately.</p>
<dd>This option controls the automatic re-enabling of the failed provider module with indications enabled. If the provider module with indications enabled fails very frequently, it affects the CIMServer normal operations because CIMServer would be busy reloading the provider module every time it fails. This option would be helpful if a long running indication provider crashes and the management application wants to receive the indications from the provider while provider fix is being delivered.</p>
<dd>In case of provider module grouping, if one of the indication provider crashes, it affects all indication providers in the provider modules of the group.</p>
<dd>Note that this is the facility provided by the CIMServer for temporary recovery of the provider and the ultimate goal SHALL be to fix the faulty provider.</p>
<dd><code>Default Value: </code>3</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>maxIndicationDeliveryRetryAttempts</code></p>
<dl>
<dd><code>Description:</code>If set to a positive integer, value defines the number of times indication service will enable the reliableIndication feature and try to deliver an indication to a particular listener destination.This does not effect the original delivery attempt. A value of 0 disables reliable indication feature completely, and cimserver will deliver the indication once.</p>
<dd>This value is used to set the CIM_IndicationService.DeliveryRetryAttempts property. See CIM_IndicationService.DeliveryRetryAttempts property for more details.</p>
<dd><code>Default Value: </code>3</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>minIndicationDeliveryRetryInterval</code></p>
<dl>
<dd><code>Description:</code>If set to a positive integer, this value defines the minimal time interval in seconds for the indication service to wait before retrying to deliver an indication to a listener destination that previously failed. Cimserver may take longer due to QoS or other processing.</p>
<dd>This value is used to initialize the property CIM_IndicationService.DeliveryRetryInterval. See CIM_IndicationService.DeliveryRetryInterval property for more details.</p>
<dd><code>Default Value: </code>30</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>shutdownTimeout</code></p>
<dl>
<dd><code>Description:</code> When a <code>cimserver -s</code> shutdown command is issued, specifies the maximum time in seconds for the CIM Server to complete outstanding CIM operation requests before shutting down; if the specified timeout period expires, the CIM Server will shut down, even if there are still CIM operations in progress. Minimum value is 2 seconds.</p>
<dd><code>Default Value: </code>30</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>slpProviderStartupTimeout</code></p>
<dl>
<dd><code>Description:</code> Timeout value in milli seconds used to specify how long the registration with an SLP SA may take. Registration will be retried three times.</p>
<dd>This value only needs to be increased in case that the loading of a set of providers whose implementation of a registered profile takes very long.</p>
<dd><code>Default Value: </code>300000</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>socketWriteTimeout</code></p>
<dl>
<dd><code>Description:</code> Specifies the number of seconds the CIM Server will wait for a client connection to be ready to receive data. If the CIM Server is unable to write to a connection in this time, the connection is closed.</p>
<dd>A client connection can become unable to receive data if the client fails to read the data that has already been sent. This timeout allows the CIM Server to reclaim resources that are allocated to a malfunctioning client.</p>
<dd>One might consider increasing this timeout value if the CIM Server prematurely closes connections with well-behaved clients.</p>
<dd><code>Default Value: </code>20</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>sslClientVerificationMode </code></p>
<dl>
<dd><code>Description:</code> Defines the desired level of support for certificate-based authentication. It can be set to <code>required, optional</code> or <code>disabled.</code> If set to <code>required,</code> the CIM Server will require all clients connecting over HTTPS to authenticate using a certificate. If the client certificate is not sent or not trusted the connection will be rejected. If set to <code>optional,</code> the CIM Server will allow, but not require, HTTPS clients to authenticate using a certificate. If the client does not send a certificate, the CIM Server will attempt to authenticate the client using HTTP basic authentication. If set to <code>disabled,</code> the CIM Server will not allow HTTPS clients to authenticate using a certificate. Basic authentication will be used to authenticate all HTTPS clients. This property is only used if <code>enableHttpsConnection</code> is true.</p>
<dd><code>Default Value: </code>disabled</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>traceFileSizeKBytes</code></p>
<dl>
<dd><code>Description:</code>Defines the size of the tracefile in Kilo bytes. The trace file will be rolled once its size exceeds the specified size.&quot;</p>
<dd><code>Default Value: </code>1048576</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>numberOfTraceFiles</code></p>
<dl>
<dd><code>Description:</code>Specifies the number of the tracefiles for rolling.</p>
<dd><code>Default Value: </code>3</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>Yes</dl>
<p> <code>sslCipherSuite</code></p>
<dl>
<dd><code>Description:</code> String containing OpenSSL cipher specifications to configure the cipher suite the client is permitted to negotiate with the server during the SSL handshake phase. The value should be mentioned between single quotes since it can contain special characters like .+, !, -.</p>
<dd><code>Default Value: </code>DEFAULT&nbsp;<wbr>(The default cipher list of OpenSSL)</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>sslBackwardCompatibility</code></p>
<dl>
<dd><code>Description:</code>This setting specifies whether the ssl supports SSLv3. Ideally for security Compilance purposes it is by default set to false.</p>
<dd><code>Default Value: </code>false</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>webRoot</code></p>
<dl>
<dd><code>Description:</code>Points to a location where the static web pages to be served by the pegasus webserver are stored.</p>
<dd><code>Default Value: </code>/var/tog-pegasus/www</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>indexFile</code></p>
<dl>
<dd><code>Description:</code>Specifies the name of index file used by pegasus webserver, default to index.html, This file should be available at the webRoot path.</p>
<dd><code>Default Value: </code>index.html</p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> <code>mimeTypesFile </code></p>
<dl>
<dd><code>Description:</code> Refers to the file which holds the mime types being served by the pegasus webserver.</p>
<dd><code>Default Value: /var/tog-pegasus/www/mimeTypes.txt</code></p>
<dd><code>Dynamic:</code>&nbsp;<wbr>No</dl>
<p> If both the <code>enableHttpsConnection</code> and <code>enableHttpConnection</code> properties are set to <code>False , </code> neither HTTP nor HTTPS connections will be allowed. On some platforms, the OpenPegasus CIM Server has been enhanced to include support for a local (single system), non-standard protocol. This allows the OpenPegasus CIM Server to continue to receive and process requests from local OpenPegasus CIM Clients even if both HTTP ports are disabled. If a local protocol is not supported, the CIM Server will be shut down and disabled from automatically being re-started. The current and planned values of the configuration properties are stored in the files <code>/var/opt/tog-pegasus/cimserver_current.conf</code> and <code>/var/opt/tog-pegasus/cimserver_planned.conf ,</code> respectively. The configuration properties may only be modified via the <code>cimconfig</code> and <code>cimserver (8)</code> commands; the files must not be edited directly.</p>
<h3>Options</h3>
<p>The <code>cimconfig</code> command recognizes the following options:</p>
<dl>
<dd>
<dl>
<dt><code>-g</code> configuration_property</p>
<dd>Gets the specified value (current, planned and/or default) of the specified configuration property. By default, gets the current value.</p>
<dt><code>-s</code> configuration_property = value</p>
<dd>Sets the specified value (current and/or planned) of the specified configuration property to <i>R value . </i> By default, sets the current value.</p>
<dt><code>-u</code> configuration_property</p>
<dd>Unsets the specified value (current and/or planned) of the specified configuration property, and resets it to its default value. By default, unsets the current value and resets it to its default value.</p>
<dt><code>-l</code></p>
<dd>Lists all the specified (current or planned) configuration property name and value pairs in the CIM Server. By default, lists only the names of all the current configuration properties.</p>
<dt><code>-c</code></p>
<dd>Specifies that the operation (get, set, unset, or list) be performed on the current configuration properties. For set or unset operations, returns an error when the CIM Server is not running or the specified property is not a dynamic property.</p>
<dt><code>-p</code></p>
<dd>Specifies that the operation (get, set, unset, or list) be performed on the planned configuration properties. For set and unset operations, operates on the value of the specified property in the planned configuration file if the CIM Server is not running.</p>
<dt><code>-d</code></p>
<dd>Specifies that the get operation be performed on the default configuration properties. Returns an error when the CIM Server is not running.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display the command usage message.</p>
<dt><code>-H name</code>|<code>AllFP</code></p>
<dd>Display detailed help information on the configuraton property defined by the name parameter or on all properties if the keyword &quot;All&quot; is used.</dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to stderr and an error value of 1 is returned. The following return values are returned:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Successful completion</p>
<dt><code>1</code></p>
<dd>Error</dl>
</dl>
<h2>Examples</h2>
<p>Get the current value for the configuration property <code>shutdownTimeout .</code></p>
<dl>
<dd><code>cimconfig -g shutdownTimeout -c</code></dl>
<p> Get the planned value for the configuration property <code>shutdownTimeout .</code></p>
<dl>
<dd><code>cimconfig -g shutdownTimeout -p</code></dl>
<p> Get the default value for the configuration property <code>shutdownTimeout .</code></p>
<dl>
<dd><code>cimconfig -g shutdownTimeout -d</code></dl>
<p> Set the current value of the property <code>shutdownTimeout</code> to the new value 15.</p>
<dl>
<dd><code>cimconfig -s shutdownTimeout=15 -c</code></dl>
<p> Set the planned value of the property <code>shutdownTimeout , </code> to the new value 5.</p>
<dl>
<dd><code>cimconfig -s shutdownTimeout=5 -p</code></dl>
<p> Reset the current value of the property <code>shutdownTimeout</code> to its default value.</p>
<dl>
<dd><code>cimconfig -u shutdownTimeout -c</code></dl>
<p> Reset the planned value of the property <code>shutdownTimeout </code> to its default value.</p>
<dl>
<dd><code>cimconfig -u shutdownTimeout -p</code></dl>
<p> List all the current configuration property names.</p>
<dl>
<dd><code>cimconfig -l</code></dl>
<p> List all the current configuration property names and their values.</p>
<dl>
<dd><code>cimconfig -l -c</code></dl>
<p> List all the planned configuration property names and their values.</p>
<dl>
<dd><code>cimconfig -l -p</code></dl>
<h2>Files</h2>
<dl>
<dd><code>/var/opt/tog-pegasus/cimserver_current.conf</code> Current configuration</p>
<dt><code>/var/opt/tog-pegasus/cimserver_planned.conf</code></p>
<dd>Planned configuration</dl>
<h2>See Also</h2>
<p>cimserver (8), cimauth (8). </p>
