---
title: "snmpd-conf(5)"
name: "snmpd-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snmpd-conf/"
description: "snmpd.conf – configuration file for the Net-SNMP SNMP agent"
---

<p>snmpd.conf &#8211; configuration file for the Net-SNMP SNMP agent</p>
<h2>Description</h2>
<p>The Net-SNMP agent uses one or more configuration files to control its operation and the management information provided. These files (<code>snmpd.conf</code> and <code>snmpd.local.conf</code>) can be located in one of several locations, as described in the <i><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5) </i> manual page. </p>
<p> The (perl) application <code>snmpconf</code> can be used to generate configuration files for the most common agent requirements. See the <i><a href="/docs/linux/man/1-snmpconf/">snmpconf</a>(1)</i> manual page for more information, or try running the command:</p>
<dl>
<dd>
<dl>
<dt>snmpconf -g basic_setup</p>
<dd></dl>
</dl>
<p> There are a large number of directives that can be specified, but these mostly fall into four distinct categories:</p>
<dl>
<dt>&bull;</p>
<dd>those controlling who can access the agent</p>
<dt>&bull;</p>
<dd>those configuring the information that is supplied by the agent</p>
<dt>&bull;</p>
<dd>those controlling active monitoring of the local system</p>
<dt>&bull;</p>
<dd>those concerned with extending the functionality of the agent.</dl>
<p> Some directives don&#8217;t fall naturally into any of these four categories, but this covers the majority of the contents of a typical <code>snmpd.conf</code> file. A full list of recognised directives can be obtained by running the command:</p>
<dl>
<dd>
<dl>
<dt>snmpd -H</p>
<dd></dl>
</dl>
<h2>Agent Behaviour</h2>
<p>Although most configuration directives are concerned with the MIB information supplied by the agent, there are a handful of directives that control the behaviour of <i>snmpd</i> considered simply as a daemon providing a network service.</p>
<dl>
<dt>agentaddress [&lt;transport-specifier&gt;:]&lt;transport-address&gt;[,&#8230;]</p>
<dd>defines a list of listening addresses, on which to receive incoming SNMP requests. See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</p>
<dd>The default behaviour is to listen on UDP port 161 on all IPv4 interfaces.</p>
<dt>agentgroup {GROUP|#GID}</p>
<dd>changes to the specified group after opening the listening port(s). This may refer to a group by name (GROUP), or a numeric group ID starting with &#8216;#&#8217; (#GID).</p>
<dt>agentuser {USER|#UID}</p>
<dd>changes to the specified user after opening the listening port(s). This may refer to a user by name (USER), or a numeric user ID starting with &#8216;#&#8217; (#UID).</p>
<dt>leave_pidfile yes</p>
<dd>instructs the agent to not remove its pid file on shutdown. Equivalent to specifying &quot;-U&quot; on the command line.</p>
<dt>maxGetbulkRepeats NUM</p>
<dd>Sets the maximum number of responses allowed for a single variable in a getbulk request. Set to 0 to enable the default and set it to -1 to enable unlimited. Because memory is allocated ahead of time, sitting this to unlimited is not considered safe if your user population can not be trusted. A repeat number greater than this will be truncated to this value.</p>
<dd>This is set by default to -1.</p>
<dt>maxGetbulkResponses NUM</p>
<dd>Sets the maximum number of responses allowed for a getbulk request. This is set by default to 100. Set to 0 to enable the default and set it to -1 to enable unlimited. Because memory is allocated ahead of time, sitting this to unlimited is not considered safe if your user population can not be trusted.</p>
<dd>In general, the total number of responses will not be allowed to exceed the maxGetbulkResponses number and the total number returned will be an integer multiple of the number of variables requested times the calculated number of repeats allow to fit below this number.</p>
<dd>Also not that processing of maxGetbulkRepeats is handled first.</dl>
<h3>SNMPv3 Configuration &#8211; Real Security</h3>
<p>SNMPv3 is added flexible security models to the SNMP packet structure so that multiple security solutions could be used. SNMPv3 was original defined with a &quot;User-based Security Model&quot; (USM) [RFC3414] that required maintaining a SNMP-specific user database. This was later determined to be troublesome to maintain and had some minor security issues. The IETF has since added additional security models to tunnel SNMP over SSH [RFC5592] and DTLS/TLS [RFC-to-be]. Net-SNMP contains robust support for SNMPv3/USM, SNMPv3/TLS, and SNMPv3/DTLS. It contains partial support for SNMPv3/SSH as well but has not been as extensively tested. It also contains code for support for an experimental Kerberos based SNMPv3 that never got standardized. </p>
<p> Hopefully more SNMP software and devices will eventually support SNMP over (D)TLS or SSH, but it is likely that devices with original support for SNMP will only contain support for USM users. If your network manager supports SNMP over (D)TLS or SNMP over SSH we suggest you use one of these mechanisms instead of using USM, but as always with Net-SNMP we give you the options to pick from so you can make the choice that is best for you.</p>
<h3>SNMPv3 generic parameters</h3>
<p>These parameters are generic to all the forms of SNMPv3. The SNMPv3 protocol defines &quot;engineIDs&quot; that uniquely identify an agent. The string must be consistent through time and should not change or conflict with another agent&#8217;s engineID. Ever. Internally, Net-SNMP by default creates a unique engineID that is based off of the current system time and a random number. This should be sufficient for most users unless you&#8217;re embedding our agent in a device where these numbers won&#8217;t vary between boxes on the devices initial boot.</p>
<dl>
<dd>EngineIDs are used both as a &quot;context&quot; for selecting information from the device and SNMPv3 with USM uses it to create unique entries for users in its user table.</p>
<dd>The Net-SNMP agent offers the following mechanisms for setting the engineID, but again you should only use them if you know what you&#8217;re doing:</p>
<dt>engineID STRING</p>
<dd>specifies that the engineID should be built from the given text STRING.</p>
<dt>engineIDType 1|2|3</p>
<dd>specifies that the engineID should be built from the IPv4 address (1), IPv6 address (2) or MAC address (3). Note that changing the IP address (or switching the network interface card) may cause problems.</p>
<dt>engineIDNic INTERFACE</p>
<dd>defines which interface to use when determining the MAC address. If <i>engineIDType 3</i> is not specified, then this directive has no effect.</p>
<dd>The default is to use eth0.</dl>
<h3>SNMPv3 over TLS</h3>
<p>SNMPv3 may be tunneled over TLS and DTLS. TLS runs over TCP and DTLS is the UDP equivalent. Wes Hardaker (the founder of Net-SNMP) performed a study and presented it at an IETF meeting that showed that TCP based protocols are sufficient for stable networks but quickly becomes a problem in unstable networks with even moderate levels of packet loss (~ 20-30%). If you are going to use TLS or DTLS, you should use the one appropriate for your networking environment. You should potentially turn them both on so your management system can access either the UDP or the TCP port as needed. </p>
<p> Many of the configuration tokens described below are prefixed with a &#8216;[snmp]&#8217; tag. If you place these tokens in your snmpd.conf file, this take is required. See the <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5) manual page for the meaning of this context switch.</p>
<dl>
<dt>[snmp] localCert &lt;specifier&gt;</p>
<dd>This token defines the default X.509 public key to use as the server&#8217;s identity. It should either be a fingerprint or a filename. To create a public key for use, please run the &quot;net-snmp-cert&quot; utility which will help you create the required certificate.</p>
<dd>The default value for this is the certificate in the &quot;snmpd&quot; named certificate file.</p>
<dt>[snmp] tlsAlgorithms &lt;algorithms&gt;</p>
<dd>This string will select the algorithms to use when negotiating security during (D)TLS session establishment. See the openssl manual page <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1) for details on the format. Examples strings include:</p>
<dl>
<dd>
<pre>DEFAULT
ALL
HIGH
HIGH:!AES128-SHA</pre>
</dl>
<dd>The default value is whatever openssl itself was configured with.</p>
<dt>[snmp] x059CRLFile</p>
<dd>If you are using a Certificate Authority (CA) that publishes a Certificate Revocation List (CRL) then this token can be used to specify the location in the filesystem of a copy of the CRL file. Note that Net-SNMP will not pull a CRL over http and this must be a file, not a URL. Additionally, OpenSSL does not reload a CRL file when it has changed so modifications or updates to the file will only be noticed upon a restart of the snmpd agent. </p>
<dt>certSecName PRIORITY FINGERPRINT OPTIONS</p>
<dd>OPTIONS can be one of &lt;&#8211;sn SECNAME | &#8211;rfc822 | &#8211;dns | &#8211;ip | &#8211;cn | &#8211;any&gt;.</p>
<dd>The certSecName token will specify how to map a certificate field from the client&#8217;s X.509 certificate to a SNMPv3 username. Use the &#8211;sn SECNAME flag to directly specify a securityName for a given certificate. The other flags extract a particular component of the certificate for use as a snmpv3 securityName. These fields are one of: A SubjectAltName containing an rfc822 value (eg hardaker [at] net-snmp.org), A SubjectAltName containing a dns name value (eg foo.net-snmp.org), an IP address (eg 192.0.2.1) or a common name &quot;Wes Hardaker&quot;. The &#8211;any flag specifies that any of the subjecAltName fields may be used. Make sure once a securityName has been selected that it is given authorization via the VACM controls discussed later in this manual page.</p>
<dd>See the <a rel="nofollow" href="http://www.net-snmp.org/wiki/index.php/Using_DTLS">http://www.net-snmp.org/wiki/index.php/Using_DTLS</a> web page for more detailed instructions for setting up (D)TLS.</p>
<dt>trustCert &lt;specifier&gt;</p>
<dd>For X509 to properly verify a certificate, it should be verifiable up until a trust anchor for it. This trust anchor is typically a CA certificate but it could also be a self-signed certificate. The &quot;trustCert&quot; token should be used to load specific trust anchors into the verification engine.</dl>
<p> SNMP over (D)TLS requires the use of the Transport Security Model (TSM), so read the section on the usage of the Transport Security Model as well. Make sure when you configure the VACM to accept connections from (D)TLS that you use the &quot;tsm&quot; security model. E.G.: </p>
<p> rwuser -s tsm hardaker [at] net-snmp.org</p>
<h3>SNMPv3 over SSH Support</h3>
<p>To use SSH, you&#8217;ll need to configure sshd to invoke the sshtosnmp program as well as configure the access control settings to allow access through the tsm security model using the user name provided to snmpd by the ssh transport.</p>
<h3>SNMPv3 with the Transport Security Model (TSM)</h3>
<p>The Transport Security Model [RFC5591] defines a SNMPv3 security system for use with &quot;tunneled&quot; security protocols like TLS, DTLS and SSH. It is a very simple security model that simply lets properly protected packets to pass through into the snmp application. The transport is required to pass a securityName to use to the TSM and the TSM may optionally prefix this with a transport string (see below).</p>
<dl>
<dt>tsmUseTransportPrefix (1|yes|true|0|no|false)</p>
<dd>If set to true, the TSM module will take every securityName passed to it from the transports underneath and prefix it with a string that specifically identities the transport it came from. This is useful to avoid securityName clashes with transports that generate identical security names. For example, if the ssh security transport delivered the security name of &quot;hardaker&quot; for a SSH connection and the TLS security transport also delivered the security name of &quot;hardaker&quot; for a TLS connection then it would be impossible to separate out these two users to provide separate access control rights. With the tsmUseTransportPrefix set to true, however, the securityNames would be prefixed appropriately with one of: &quot;tls:&quot;, &quot;dtls:&quot; or &quot;ssh:&quot;.</dl>
<h3>SNMPv3 with the User-based Security Model (USM)</h3>
<p>SNMPv3 was originally defined using the User-Based Security Model (USM), which contains a private list of users and keys specific to the SNMPv3 protocol. The operational community, however, declared it a pain to manipulate yet another database and would prefer to use existing infrastructure. To that end the IETF created the ISMS working group to battle that problem, and the ISMS working group decided to tunnel SNMP over SSH and DTLS to make use existing user and authentication infrastructures.</p>
<h3>SNMPv3 USM Users</h3>
<p>To use the USM based SNMPv3-specific users, you&#8217;ll need to create them. It is recommended you <code>use the net-snmp-config command</code> to do this, but you can also do it by directly specifying createUser directives yourself instead:</p>
<dl>
<dt>createUser [-e ENGINEID] username (MD5|SHA) authpassphrase [DES|AES] [privpassphrase]</p>
<dd>
<dd>MD5 and SHA are the authentication types to use. DES and AES are the privacy protocols to use. If the privacy passphrase is not specified, it is assumed to be the same as the authentication passphrase. Note that the users created will be useless unless they are also added to the VACM access control tables described above.</p>
<dd>SHA authentication and DES/AES privacy require OpenSSL to be installed and the agent to be built with OpenSSL support. MD5 authentication may be used without OpenSSL.</p>
<dd>Warning: the minimum pass phrase length is 8 characters.</p>
<dd>SNMPv3 users can be created at runtime using the <i><a href="/docs/linux/man/1-snmpusm/">snmpusm</a>(1)</i> command.</p>
<dd>Instead of figuring out how to use this directive and where to put it (see below), just run &quot;net-snmp-config &#8211;create-snmpv3-user&quot; instead, which will add one of these lines to the right place.</p>
<dd>This directive should be placed into the /var/lib/net-snmp/snmpd.conf file instead of the other normal locations. The reason is that the information is read from the file and then the line is removed (eliminating the storage of the master password for that user) and replaced with the key that is derived from it. This key is a localized key, so that if it is stolen it can not be used to access other agents. If the password is stolen, however, it can be.</p>
<dd>If you need to localize the user to a particular EngineID (this is useful mostly in the similar snmptrapd.conf file), you can use the -e argument to specify an EngineID as a hex value (EG, &quot;0x01020304&quot;).</p>
<dd>If you want to generate either your master or localized keys directly, replace the given password with a hexstring (preceded by a &quot;0x&quot;) and precede the hex string by a -m or -l token (respectively). EGs:</p>
<dd>
<dl>
<dd>
<pre>[these keys are *not* secure but are easy to visually parse for
counting purposes. Please generate random keys instead of using
these examples]
createUser myuser SHA -l 0x0001020304050607080900010203040506070809 AES -l 0x00010203040506070809000102030405
createUser myuser SHA -m 0x0001020304050607080900010203040506070809 AES -m 0x0001020304050607080900010203040506070809</pre>
</dl>
<dd>Due to the way localization happens, localized privacy keys are expected to be the length needed by the algorithm (128 bits for all supported algorithms). Master encryption keys, though, need to be the length required by the authentication algorithm not the length required by the encrypting algorithm (MD5: 16 bytes, SHA: 20 bytes).</dl>
<h2>Access Control</h2>
<p><code>snmpd</code> supports the View-Based Access Control Model (VACM) as defined in RFC 2575, to control who can retrieve or update information. To this end, it recognizes various directives relating to access control.</p>
<h3>Traditional Access Control</h3>
<p>Most simple access control requirements can be specified using the directives <i>rouser</i>/<i>rwuser</i> (for SNMPv3) or <i>rocommunity</i>/<i>rwcommunity</i> (for SNMPv1 or SNMPv2c).</p>
<dl>
<dt>rouser [-s SECMODEL] USER [noauth|auth|priv [OID | -V VIEW [CONTEXT]]]</p>
<dd>
<dt>rwuser [-s SECMODEL] USER [noauth|auth|priv [OID | -V VIEW [CONTEXT]]]</p>
<dd>specify an SNMPv3 user that will be allowed read-only (GET and GETNEXT) or read-write (GET, GETNEXT and SET) access respectively. By default, this will provide access to the full OID tree for authenticated (including encrypted) SNMPv3 requests, using the default context. An alternative minimum security level can be specified using <i>noauth</i> (to allow unauthenticated requests), or <i>priv</i> (to enforce use of encryption). The OID field restricts access for that user to the subtree rooted at the given OID, or the named view. An optional context can also be specified, or &quot;context*&quot; to denote a context prefix. If no context field is specified (or the token &quot;*&quot; is used), the directive will match all possible contexts.</p>
<dd>If SECMODEL is specified then it will be the security model required for that user (note that identical user names may come in over different security models and will be appropriately separated via the access control settings). The default security model is &quot;usm&quot; and the other common security models are likely &quot;tsm&quot; when using (D)TLS or SSH support and &quot;ksm&quot; if the Kerberos support has been compiled in.</p>
<dt>rocommunity COMMUNITY [SOURCE [OID | -V VIEW [CONTEXT]]]</p>
<dd>
<dt>rwcommunity COMMUNITY [SOURCE [OID | -V VIEW [CONTEXT]]]</p>
<dd>specify an SNMPv1 or SNMPv2c community that will be allowed read-only (GET and GETNEXT) or read-write (GET, GETNEXT and SET) access respectively. By default, this will provide access to the full OID tree for such requests, regardless of where they were sent from. The SOURCE token can be used to restrict access to requests from the specified system(s) &#8211; see <i>com2sec</i> for the full details. The OID field restricts access for that community to the subtree rooted at the given OID, or named view. Contexts are typically less relevant to community-based SNMP versions, but the same behaviour applies here.</p>
<dt>rocommunity6 COMMUNITY [SOURCE [OID | -V VIEW [CONTEXT]]]</p>
<dd>
<dt>rwcommunity6 COMMUNITY [SOURCE [OID | -V VIEW [CONTEXT]]]</p>
<dd>are directives relating to requests received using IPv6 (if the agent supports such transport domains). The interpretation of the SOURCE, OID, VIEW and CONTEXT tokens are exactly the same as for the IPv4 versions.</dl>
<p> In each case, only one directive should be specified for a given SNMPv3 user, or community string. It is <code>not</code> appropriate to specify both <i>rouser</i> and <i>rwuser</i> directives referring to the same SNMPv3 user (or equivalent community settings). The <i>rwuser</i> directive provides all the access of <i>rouser</i> (as well as allowing SET support). The same holds true for the community-based directives. </p>
<p> More complex access requirements (such as access to two or more distinct OID subtrees, or different views for GET and SET requests) should use one of the other access control mechanisms. Note that if several distinct communities or SNMPv3 users need to be granted the same level of access, it would also be more efficient to use the main VACM configuration directives.</p>
<h3>VACM Configuration</h3>
<p>The full flexibility of the VACM is available using four configuration directives &#8211; <i>com2sec</i>, <i>group</i>, <i>view</i> and <i>access</i>. These provide direct configuration of the underlying VACM tables.</p>
<dl>
<dt>com2sec [-Cn CONTEXT] SECNAME SOURCE COMMUNITY</p>
<dd>
<dt>com2sec6 [-Cn CONTEXT] SECNAME SOURCE COMMUNITY</p>
<dd>map an SNMPv1 or SNMPv2c community string to a security name &#8211; either from a particular range of source addresses, or globally (<i>&quot;default&quot;</i>). A restricted source can either be a specific hostname (or address), or a subnet &#8211; represented as IP/MASK (e.g. 10.10.10.0/255.255.255.0), or IP/BITS (e.g. 10.10.10.0/24), or the IPv6 equivalents.</p>
<dd>The same community string can be specified in several separate directives (presumably with different source tokens), and the first source/community combination that matches the incoming request will be selected. Various source/community combinations can also map to the same security name.</p>
<dd>If a CONTEXT is specified (using <i>-Cn</i>), the community string will be mapped to a security name in the named SNMPv3 context. Otherwise the default context (&quot;&quot;) will be used.</p>
<dt>com2secunix [-Cn CONTEXT] SECNAME SOCKPATH COMMUNITY</p>
<dd>is the Unix domain sockets version of <i>com2sec</i>.</p>
<dt>group GROUP {v1|v2c|usm|tsm|ksm} SECNAME</p>
<dd>maps a security name (in the specified security model) into a named group. Several <i>group</i> directives can specify the same group name, allowing a single access setting to apply to several users and/or community strings.</p>
<dd>Note that groups must be set up for the two community-based models separately &#8211; a single <i>com2sec</i> (or equivalent) directive will typically be accompanied by <code>two</code> <i>group</i> directives.</p>
<dt>view VNAME TYPE OID [MASK]</p>
<dd>defines a named &quot;view&quot; &#8211; a subset of the overall OID tree. This is most commonly a single subtree, but several <i>view</i> directives can be given with the same view name (VNAME), to build up a more complex collection of OIDs. TYPE is either <i>included</i> or <i>excluded</i>, which can again define a more complex view (e.g by excluding certain sensitive objects from an otherwise accessible subtree).</p>
<dd>MASK is a list of hex octets (optionally separated by &#8216;.&#8217; or &#8216;:&#8217;) with the set bits indicating which subidentifiers in the view OID to match against. If not specified, this defaults to matching the OID exactly (all bits set), thus defining a simple OID subtree. So:</p>
<dl>
<dd>
<dl>
<dd>view iso1 included .iso 0xf0<br />
 view iso2 included .iso<br />
 view iso3 included .iso.org.dod.mgmt 0xf0</dl>
</dl>
<dd>would all define the same view, covering the whole of the &#8216;<a href="/docs/linux/man/1-iso/">iso</a>(1)&#8217; subtree (with the third example ignoring the subidentifiers not covered by the mask).</p>
<dd>More usefully, the mask can be used to define a view covering a particular row (or rows) in a table, by matching against the appropriate table index value, but skipping the column subidentifier:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>view ifRow4 included .1.3.6.1.2.1.2.2.1.0.4 0xff:a0</p>
<dd></dl>
</dl>
</dl>
<dd>Note that a mask longer than 8 bits must use &#8216;:&#8217; to separate the individual octets.</p>
<dt>access GROUP CONTEXT {any|v1|v2c|usm|tsm|ksm} LEVEL PREFX READ WRITE NOTIFY</p>
<dd>maps from a group of users/communities (with a particular security model and minimum security level, and in a specific context) to one of three views, depending on the request being processed.</p>
<dd>LEVEL is one of <i>noauth</i>, <i>auth</i>, or <i>priv</i>. PREFX specifies how CONTEXT should be matched against the context of the incoming request, either <i>exact</i> or <i>prefix</i>. READ, WRITE and NOTIFY specifies the view to be used for GET*, SET and TRAP/INFORM requests (althought the NOTIFY view is not currently used). For v1 or v2c access, LEVEL will need to be <i>noauth</i>.</dl>
<h3>Typed-View Configuration</h3>
<p>The final group of directives extend the VACM approach into a more flexible mechanism, which can be applied to other access control requirements. Rather than the fixed three views of the standard VACM mechanism, this can be used to configure various different view types. As far as the main SNMP agent is concerned, the two main view types are <i>read</i> and <i>write</i>, corresponding to the READ and WRITE views of the main <i>access</i> directive. See the &#8216;<a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)&#8217; man page for discussion of other view types.</p>
<dl>
<dt>authcommunity TYPES COMMUNITY [SOURCE [OID | -V VIEW [CONTEXT]]]</p>
<dd>is an alternative to the <i>rocommunity</i>/<i>rwcommunity</i> directives. TYPES will usually be <i>read</i> or <i>read,write</i> respectively. The view specification can either be an OID subtree (as before), or a named view (defined using the <i>view</i> directive) for greater flexibility. If this is omitted, then access will be allowed to the full OID tree. If CONTEXT is specified, access is configured within this SNMPv3 context. Otherwise the default context (&quot;&quot;) is used.</p>
<dt>authuser TYPES [-s MODEL] USER [LEVEL [OID | -V VIEW [CONTEXT]]]</p>
<dd>is an alternative to the <i>rouser</i>/<i>rwuser</i> directives. The fields TYPES, OID, VIEW and CONTEXT have the same meaning as for <i>authcommunity</i>.</p>
<dt>authgroup TYPES [-s MODEL] GROUP [LEVEL [OID | -V VIEW [CONTEXT]]]</p>
<dd>is a companion to the <i>authuser</i> directive, specifying access for a particular group (defined using the <i>group</i> directive as usual). Both <i>authuser</i> and <i>authgroup</i> default to authenticated requests &#8211; LEVEL can also be specified as <i>noauth</i> or <i>priv</i> to allow unauthenticated requests, or require encryption respectively. Both <i>authuser</i> and <i>authgroup</i> directives also default to configuring access for SNMPv3/USM requests &#8211; use the &#8216;-s&#8217; flag to specify an alternative security model (using the same values as for <i>access</i> above).</p>
<dt>authaccess TYPES [-s MODEL] GROUP VIEW [LEVEL [CONTEXT]]</p>
<dd>also configures the access for a particular group, specifying the name and type of view to apply. The MODEL and LEVEL fields are interpreted in the same way as for <i>authgroup</i>. If CONTEXT is specified, access is configured within this SNMPv3 context (or contexts with this prefix if the CONTEXT field ends with &#8216;*&#8217;). Otherwise the default context (&quot;&quot;) is used.</p>
<dt>setaccess GROUP CONTEXT MODEL LEVEL PREFIX VIEW TYPES</p>
<dd>is a direct equivalent to the original <i>access</i> directive, typically listing the view types as <i>read</i> or <i>read,write</i> as appropriate. (or see &#8216;<a href="/docs/linux/man/5-snmptrapd-conf/">snmptrapd.conf</a>(5)&#8217; for other possibilities). All other fields have the same interpretation as with <i>access</i>.</dl>
<h2>System Information</h2>
<p>Most of the information reported by the Net-SNMP agent is retrieved from the underlying system, or dynamically configured via SNMP SET requests (and retained from one run of the agent to the next). However, certain MIB objects can be configured or controlled via the <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> file.</p>
<h3>System Group</h3>
<p>Most of the scalar objects in the &#8216;system&#8217; group can be configured in this way:</p>
<dl>
<dt>sysLocation STRING</p>
<dd>
<dt>sysContact STRING</p>
<dd>
<dt>sysName STRING</p>
<dd>set the system location, system contact or system name (sysLocation.0, sysContact.0 and sysName.0) for the agent respectively. Ordinarily these objects are writable via suitably authorized SNMP SET requests. However, specifying one of these directives makes the corresponding object read-only, and attempts to SET it will result in a <i>notWritable</i> error response.</p>
<dt>sysServices NUMBER</p>
<dd>sets the value of the sysServices.0 object. For a host system, a good value is 72 (application + end-to-end layers). If this directive is not specified, then no value will be reported for the sysServices.0 object.</p>
<dt>sysDescr STRING</p>
<dd>
<dt>sysObjectID OID</p>
<dd>sets the system description or object ID for the agent. Although these MIB objects are not SNMP-writable, these directives can be used by a network administrator to configure suitable values for them.</dl>
<h3>Interfaces Group</h3>
<dl>
<dt>interface NAME TYPE SPEED</p>
<dd>can be used to provide appropriate type and speed settings for interfaces where the agent fails to determine this information correctly. TYPE is a type value as given in the IANAifType-MIB, and can be specified numerically or by name (assuming this MIB is loaded).</p>
<dt>interface_fadeout TIMEOUT</p>
<dd>specifies, for how long the agent keeps entries in ifTable after appropriate interfaces have been removed from system (typically various ppp, tap or tun interfaces). Timeout value is in seconds. Default value is 300 (=5 minutes).</p>
<dt>interface_replace_old yes</p>
<dd>can be used to remove already existing entries in ifTable when an interface with the same name appears on the system. E.g. when ppp0 interface is removed, it is still listed in the table for <i>interface_fadeout</i> seconds. This option ensures, that the old ppp0 interface is removed even before the <i>interface_fadeout</i> timeour when new ppp0 (with different ifIndex) shows up.</dl>
<h3>Host Resources Group</h3>
<p>This requires that the agent was built with support for the <i>host</i> module (which is now included as part of the default build configuration on the major supported platforms).</p>
<dl>
<dt>ignoreDisk STRING</p>
<dd>controls which disk devices are scanned as part of populating the hrDiskStorageTable (and hrDeviceTable). The HostRes implementation code includes a list of disk device patterns appropriate for the current operating system, some of which may cause the agent to block when trying to open the corresponding disk devices. This might lead to a timeout when walking these tables, possibly resulting in inconsistent behaviour. This directive can be used to specify particular devices (either individually or wildcarded) that should not be checked.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Please consult the source (<i>host/hr_disk.c</i>) and check for the <i>Add_HR_Disk_entry</i> calls relevant for a particular O/S to determine the list of devices that will be scanned.</dl>
</dl>
<dd>The pattern can include one or more wildcard expressions. See <i><a href="/docs/linux/man/5-snmpd-examples/">snmpd.examples</a>(5)</i> for illustration of the wildcard syntax.</p>
<dt>skipNFSInHostResources true</p>
<dd>controls whether NFS and NFS-like file systems should be omitted from the hrStorageTable (true or 1) or not (false or 0, which is the default). If the Net-SNMP agent gets hung on NFS-mounted filesystems, you can try setting this to &#8216;1&#8217;.</p>
<dt>storageUseNFS [1|2]</p>
<dd>controls how NFS and NFS-like file systems should be reported in the hrStorageTable. as &#8216;Network Disks&#8217; (1) or &#8216;Fixed Disks&#8217; (2) Historically, the Net-SNMP agent has reported such file systems as &#8216;Fixed Disks&#8217;, and this is still the default behaviour. Setting this directive to &#8216;1&#8217; reports such file systems as &#8216;Network Disks&#8217;, as required by the Host Resources MIB.</p>
<dt>realStorageUnits</p>
<dd>controlls how the agent reports hrStorageAllocationUnits, hrStorageSize and hrStorageUsed in hrStorageTable. For big storage drives with small allocation units the agent re-calculates these values so they all fit Integer32 and hrStorageAllocationUnits x hrStorageSize gives real size of the storage.</p>
<dl>
<dd>
<dl>
<dt>Example:</p>
<dd>Linux xfs 16TB filesystem with 4096 bytes large blocks will be reported as hrStorageAllocationUnits = 8192 and hrStorageSize = 2147483647, so 8192 x 2147483647 gives real size of the filesystem (=16 TB).</dl>
</dl>
<dd>Setting this directive to &#8216;1&#8217; turns off this calculation and the agent reports real hrStorageAllocationUnits, but it might report wrong hrStorageSize for big drives because the value won&#8217;t fit into Integer32. In this case, hrStorageAllocationUnits x hrStorageSize won&#8217;t give real size of the storage.</dl>
<h3>Process Monitoring</h3>
<p>The hrSWRun group of the Host Resources MIB provides information about individual processes running on the local system. The prTable of the UCD-SNMP-MIB complements this by reporting on selected services (which may involve multiple processes). This requires that the agent was built with support for the <i>ucd-snmp/proc</i> module (which is included as part of the default build configuration).</p>
<dl>
<dt>proc NAME [MAX [MIN]]</p>
<dd>monitors the number of processes called NAME (as reported by &quot;/usr/bin/ps -e&quot;) running on the local system.</p>
<dd>If the number of NAMEd processes is less than MIN or greater than MAX, then the corresponding prErrorFlag instance will be set to 1, and a suitable description message reported via the prErrMessage instance.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This situation will <code>not</code> automatically trigger a trap to report the problem &#8211; see the DisMan Event MIB section later.</dl>
</dl>
<dd>If neither MAX nor MIN are specified, they will default to <code>infinity</code> and 1 respectively (&quot;at least one&quot;). If only MAX is specified, MIN will default to 0 (&quot;no more than MAX&quot;). If MAX is 0 (and MIN is not), this indicates infinity (&quot;at least MIN&quot;). If both MAX and MIN are 0, this indicates a process that should <code>not</code> be running.</p>
<dt>procfix NAME PROG ARGS</p>
<dd>registers a command that can be run to fix errors with the given process NAME. This will be invoked when the corresponding prErrFix instance is set to 1.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This command will <code>not</code> be invoked automatically.</dl>
</dl>
<dd>The <i>procfix</i> directive must be specified <code>after</code> the matching <i>proc</i> directive, and cannot be used on its own.</dl>
<p> If no <i>proc</i> directives are defined, then walking the prTable will fail (<i>noSuchObject). </i></p>
<h3>Disk Usage Monitoring</h3>
<p>This requires that the agent was built with support for the <i>ucd-snmp/disk</i> module (which is included as part of the default build configuration).</p>
<dl>
<dt>disk PATH [ MINSPACE | MINPERCENT% ]</p>
<dd>monitors the disk mounted at PATH for available disk space. Disks mounted after the agent has started will not be monitored, unless <i>includeAllDisks</i> option is specified.</p>
<dd>The minimum threshold can either be specified in kB (MINSPACE) or as a percentage of the total disk (MINPERCENT% with a &#8216;%&#8217; character), defaulting to 100kB if neither are specified. If the free disk space falls below this threshold, then the corresponding dskErrorFlag instance will be set to 1, and a suitable description message reported via the dskErrorMsg instance.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This situation will <code>not</code> automatically trigger a trap to report the problem &#8211; see the DisMan Event MIB section later.</dl>
</dl>
<dt>includeAllDisks MINPERCENT%</p>
<dd>configures monitoring of all disks found on the system, using the specified (percentage) threshold. The dskTable is dynamically updated, unmounted disks disappear from the table and newly mounted disks are added to the table. The threshold for individual disks can be adjusted using suitable <i>disk</i> directives (which can come either before or after the <i>includeAllDisks</i> directive).</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Whether <i>disk</i> directives appears before or after <i>includeAllDisks</i> may affect the indexing of the dskTable.</dl>
</dl>
<dd>Only one <i>includeAllDisks</i> directive should be specified &#8211; any subsequent copies will be ignored.</p>
<dd>The list of mounted disks will be determined from HOST-RESOURCES-MIB::hrFSTable.</dl>
<p> If neither any <i>disk</i> directives or <i>includeAllDisks</i> are defined, then walking the dskTable will fail (<i>noSuchObject). </i></p>
<h3>Disk I/O Monitoring</h3>
<p>This requires that the agent was built with support for the <i>ucd-snmp/diskio</i> module (which is not included as part of the default build configuration). </p>
<p> By default, all block devices known to the operating system are included in the diskIOTable. On platforms other than Linux, this module has no configuration directives. </p>
<p> On Linux systems, it is possible to exclude several classes of block devices from the diskIOTable in order to avoid cluttering the table with useless zero statistics for pseudo-devices that often are not in use but are configured by default to exist in most recent Linux distributions.</p>
<dl>
<dt>diskio_exclude_fd yes</p>
<dd>Excludes all Linux floppy disk block devices, whose names start with &quot;fd&quot;, e.g. &quot;fd0&quot;</p>
<dt>diskio_exclude_loop yes</p>
<dd>Excludes all Linux loopback block devices, whose names start with &quot;loop&quot;, e.g. &quot;loop0&quot;</p>
<dt>diskio_exclude_ram yes</p>
<dd>Excludes all LInux ramdisk block devices, whose names start with &quot;ram&quot;, e.g. &quot;ram0&quot;</dl>
<p> On Linux systems, it is possible to report only explicitly whitelisted devices. It may take significant amount of time to process diskIOTable data on systems with tens of thousands of block devices and whitelisting only the important ones avoids large CPU consumption.</p>
<dl>
<dt>diskio &lt;device&gt;</p>
<dd>Enables whitelisting of devices and adds the device to the whitelist. Only explicitly whitelisted devices will be reported. This option may be used multiple times.</dl>
<h3>System Load Monitoring</h3>
<p>This requires that the agent was built with support for either the <i>ucd-snmp/loadave</i> module or the <i>ucd-snmp/memory</i> module respectively (both of which are included as part of the default build configuration).</p>
<dl>
<dt>load MAX1 [MAX5 [MAX15]]</p>
<dd>monitors the load average of the local system, specifying thresholds for the 1-minute, 5-minute and 15-minute averages. If any of these loads exceed the associated maximum value, then the corresponding laErrorFlag instance will be set to 1, and a suitable description message reported via the laErrMessage instance.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This situation will <code>not</code> automatically trigger a trap to report the problem &#8211; see the DisMan Event MIB section later.</dl>
</dl>
<dd>If the MAX15 threshold is omitted, it will default to the MAX5 value. If both MAX5 and MAX15 are omitted, they will default to the MAX1 value. If this directive is not specified, all three thresholds will default to a value of DEFMAXLOADAVE.</p>
<dd>If a threshold value of 0 is given, the agent will not report errors via the relevant laErrorFlag or laErrMessage instances, regardless of the current load.</dl>
<p> Unlike the <i>proc</i> and <i>disk</i> directives, walking the walking the laTable will succeed (assuming the <i>ucd-snmp/loadave</i> module was configured into the agent), even if the <i>load</i> directive is not present.</p>
<dl>
<dt>swap MIN</p>
<dd>monitors the amount of swap space available on the local system. If this falls below the specified threshold (MIN kB), then the <i>memErrorSwap</i> object will be set to 1, and a suitable description message reported via <i>memSwapErrorMsg</i>.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This situation will <code>not</code> automatically trigger a trap to report the problem &#8211; see the DisMan Event MIB section later.</dl>
</dl>
<p> If this directive is not specified, the default threshold is 16 MB.</dl>
<h3>Log File Monitoring</h3>
<p>This requires that the agent was built with support for either the <i>ucd-snmp/file</i> or <i>ucd-snmp/logmatch</i> modules respectively (both of which are included as part of the default build configuration).</p>
<dl>
<dt>file FILE [MAXSIZE]</p>
<dd>monitors the size of the specified file (in kB). If MAXSIZE is specified, and the size of the file exceeds this threshold, then the corresponding fileErrorFlag instance will be set to 1, and a suitable description message reported via the fileErrorMsg instance.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This situation will <code>not</code> automatically trigger a trap to report the problem &#8211; see the DisMan Event MIB section later.</dl>
</dl>
<dd>Note: A maximum of 20 files can be monitored.</p>
<dd>Note: If no <i>file</i> directives are defined, then walking the fileTable will fail (<i>noSuchObject</i>).</p>
<dt>logmatch NAME FILE CYCLETIME REGEX</p>
<dd>monitors the specified file for occurances of the specified pattern REGEX. The file position is stored internally so the entire file is only read initially, every subsequent pass will only read the new lines added to the file since the last read.</p>
<dl>
<dd>
<dl>
<dt>NAME</p>
<dd>name of the logmatch instance (will appear as logMatchName under logMatch/logMatchTable/logMatchEntry/logMatchName in the ucd-snmp MIB tree)</p>
<dt>FILE</p>
<dd>absolute path to the logfile to be monitored. Note that this path can contain date/time directives (like in the UNIX &#8216;date&#8217; command). See the manual page for &#8216;strftime&#8217; for the various directives accepted.</p>
<dt>CYCLETIME</p>
<dd>time interval for each logfile read and internal variable update in seconds. Note: an SNMPGET* operation will also trigger an immediate logfile read and variable update.</p>
<dt>REGEX</p>
<dd>the regular expression to be used. Note: DO NOT enclose the regular expression in quotes even if there are spaces in the expression as the quotes will also become part of the pattern to be matched!</dl>
</dl>
<dd>Example:</p>
<dl>
<dd>
<dl>
<dd>logmatch apache-GETs /usr/local/apache/logs/access.log-%Y-%m-%d 60 GET.*HTTP.*</p>
<dd>This logmatch instance is named &#8216;apache-GETs&#8217;, uses &#8216;GET.*HTTP.*&#8217; as its regular expression and it will monitor the file named (assuming today is May 6th 2009): &#8216;/usr/local/apache/logs/access.log-2009-05-06&#8217;, tomorrow it will look for &#8216;access.log-2009-05-07&#8217;. The logfile is read every 60 seconds.</dl>
</dl>
<dd>Note: A maximum of 250 logmatch directives can be specified.</p>
<dd>Note: If no <i>logmatch</i> directives are defined, then walking the logMatchTable will fail (<i>noSuchObject).</dl>
<p> </i></p>
<h2>Active Monitoring</h2>
<p>The usual behaviour of an SNMP agent is to wait for incoming SNMP requests and respond to them &#8211; if no requests are received, an agent will typically not initiate any actions. This section describes various directives that can configure <i>snmpd</i> to take a more active role.</p>
<h3>Notification Handling</h3>
<dl>
<dt>trapcommunity STRING</p>
<dd>defines the default community string to be used when sending traps. Note that this directive must be used prior to any community-based trap destination directives that need to use it.</p>
<dt>trapsink HOST [COMMUNITY [PORT]]</p>
<dd>
<dt>trap2sink HOST [COMMUNITY [PORT]]</p>
<dd>
<dt>informsink HOST [COMMUNITY [PORT]]</p>
<dd>define the address of a notification receiver that should be sent SNMPv1 TRAPs, SNMPv2c TRAP2s, or SNMPv2 INFORM notifications respectively. See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses. If COMMUNITY is not specified, the most recent <i>trapcommunity</i> string will be used.</p>
<dd>If the transport address does not include an explicit port specification, then PORT will be used. If this is not specified, the well known SNMP trap port (162) will be used.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This mechanism is being deprecated, and the listening port should be specified via the transport specification HOST instead.</dl>
</dl>
<dd>If several sink directives are specified, multiple copies of each notification (in the appropriate formats) will be generated.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>It is <code>not</code> normally appropriate to list two (or all three) sink directives with the same destination.</dl>
</dl>
<dt>trapsess [SNMPCMD_ARGS] HOST</p>
<dd>provides a more generic mechanism for defining notification destinations. <i>SNMPCMD_ARGS</i> should be the command-line options required for an equivalent <i>snmptrap</i> (or <i>snmpinform</i>) command to send the desired notification. The option <i>-Ci</i> can be used (with <i>-v2c</i> or <i>-v3</i>) to generate an INFORM notification rather than an unacknowledged TRAP.</p>
<dd>This is the appropriate directive for defining SNMPv3 trap receivers. See <a rel="nofollow" href="http://www.net-snmp.org/tutorial/tutorial-5/commands/snmptrap-v3.html">http://www.net-snmp.org/tutorial/tutorial-5/commands/snmptrap-v3.html</a> for more information about SNMPv3 notification behaviour.</p>
<dt>authtrapenable {1|2}</p>
<dd>determines whether to generate authentication failure traps (<i><a href="/docs/linux/man/1-enabled/">enabled</a>(1)</i>) or not (<i><a href="/docs/linux/man/2-disabled/">disabled</a>(2)</i> &#8211; the default). Ordinarily the corresponding MIB object (snmpEnableAuthenTraps.0) is read-write, but specifying this directive makes this object read-only, and attempts to set the value via SET requests will result in a <i>notWritable</i> error response.</p>
<dt>v1trapaddress HOST</p>
<dd>defines the agent address, which is inserted into SNMPv1 TRAPs. Arbitrary local IPv4 address is chosen if this option is ommited. This option is useful mainly when the agent is visible from outside world by specific address only (e.g. because of network address translation or firewall).</dl>
<h3>DisMan Event MIB</h3>
<p>The previous directives can be used to configure where traps should be sent, but are not concerned with <i>when</i> to send such traps (or what traps should be generated). This is the domain of the Event MIB &#8211; developed by the Distributed Management (DisMan) working group of the IETF. </p>
<p> This requires that the agent was built with support for the <i>disman/event</i> module (which is now included as part of the default build configuration for the most recent distribution).</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>The behaviour of the latest implementation differs in some minor respects from the previous code &#8211; nothing too significant, but existing scripts may possibly need some minor adjustments.</dl>
</dl>
<dl>
<dt>iquerySecName NAME</p>
<dd>
<dt>agentSecName NAME</p>
<dd>specifies the default SNMPv3 username, to be used when making internal queries to retrieve any necessary information (either for evaluating the monitored expression, or building a notification payload). These internal queries always use SNMPv3, even if normal querying of the agent is done using SNMPv1 or SNMPv2c.</p>
<dd>Note that this user must also be explicitly created (<i>createUser</i>) and given appropriate access rights (e.g. <i>rouser</i>). This directive is purely concerned with defining <i>which</i> user should be used &#8211; not with actually setting this user up.</p>
<dt>monitor [OPTIONS] NAME EXPRESSION</p>
<dd>defines a MIB object to monitor. If the EXPRESSION condition holds (see below), then this will trigger the corresponding event, and either send a notification or apply a SET assignment (or both). Note that the event will only be triggered once, when the expression first matches. This monitor entry will not fire again until the monitored condition first becomes false, and then matches again. NAME is an administrative name for this expression, and is used for indexing the mteTriggerTable (and related tables). Note also that such monitors use an internal SNMPv3 request to retrieve the values being monitored (even if normal agent queries typically use SNMPv1 or SNMPv2c). See the <i>iquerySecName</i> token described above.</p>
<dt><i>EXPRESSION</i></p>
<dd>There are three types of monitor expression supported by the Event MIB &#8211; existence, boolean and threshold tests.</p>
<dl>
<dd>
<dl>
<dt>OID | ! OID | != OID</p>
<dd>defines an <i>existence(0)</i> monitor test. A bare OID specifies a <i>present(0)</i> test, which will fire when (an instance of) the monitored OID is created. An expression of the form <i>! OID</i> specifies an <i><a href="/docs/linux/man/1-absent/">absent</a>(1)</i> test, which will fire when the monitored OID is delected. An expression of the form <i>!= OID</i> specifies a <i><a href="/docs/linux/man/2-changed/">changed</a>(2)</i> test, which will fire whenever the monitored value(s) change. Note that there <code>must</code> be whitespace before the OID token.</p>
<dt>OID OP VALUE</p>
<dd>defines a <i><a href="/docs/linux/man/1-boolean/">boolean</a>(1)</i> monitor test. OP should be one of the defined comparison operators (!=, ==, &lt;, &lt;=, &gt;, &gt;=) and VALUE should be an integer value to compare against. Note that there <code>must</code> be whitespace around the OP token. A comparison such as OID !=0 will not be handled correctly.</p>
<dt>OID MIN MAX [DMIN DMAX]</p>
<dd>defines a <i><a href="/docs/linux/man/2-threshold/">threshold</a>(2)</i> monitor test. MIN and MAX are integer values, specifying lower and upper thresholds. If the value of the monitored OID falls below the lower threshold (MIN) or rises above the upper threshold (MAX), then the monitor entry will trigger the corresponding event.</p>
<dd>Note that the rising threshold event will only be re-armed when the monitored value falls below the <code>lower</code> threshold (MIN). Similarly, the falling threshold event will be re-armed by the upper threshold (MAX).</p>
<dd>The optional parameters DMIN and DMAX configure a pair of similar threshold tests, but working with the delta differences between successive sample values.</dl>
</dl>
<dt><i>OPTIONS</i></p>
<dd>There are various options to control the behaviour of the monitored expression. These include:</p>
<dl>
<dd>
<dl>
<dt>-D</p>
<dd>indicates that the expression should be evaluated using delta differences between sample values (rather than the values themselves).</p>
<dt>-d OID</p>
<dd>
<dt>-di OID</p>
<dd>specifies a discontinuity marker for validating delta differences. A <i>-di</i> object instance will be used exactly as given. A <i>-d</i> object will have the instance subidentifiers from the corresponding (wildcarded) expression object appended. If the <i>-I</i> flag is specified, then there is no difference between these two options.</p>
<dd>This option also implies <i>-D</i>.</p>
<dt>-e EVENT</p>
<dd>specifies the event to be invoked when this monitor entry is triggered. If this option is not given, the monitor entry will generate one of the standard notifications defined in the DISMAN-EVENT-MIB.</p>
<dt>-I</p>
<dd>indicates that the monitored expression should be applied to the specified OID as a single instance. By default, the OID will be treated as a wildcarded object, and the monitor expanded to cover all matching instances.</p>
<dt>-i OID</p>
<dd>
<dt>-o OID</p>
<dd>define additional varbinds to be added to the notification payload when this monitor trigger fires. For a wildcarded expression, the suffix of the matched instance will be added to any OIDs specified using <i>-o</i>, while OIDs specified using <i>-i</i> will be treated as exact instances. If the <i>-I</i> flag is specified, then there is no difference between these two options.</p>
<dd>See <i>strictDisman</i> for details of the ordering of notification payloads.</p>
<dt>-r FREQUENCY</p>
<dd>monitors the given expression every FREQUENCY, where FREQUENCY is in seconds or optionally suffixed by one of s (for seconds), m (for minutes), h (for hours), d (for days), or w (for weeks). By default, the expression will be evaluated every 600s (10 minutes).</p>
<dt>-S</p>
<dd>indicates that the monitor expression should <i>not</i> be evaluated when the agent first starts up. The first evaluation will be done once the first repeat interval has expired.</p>
<dt>-s</p>
<dd>indicates that the monitor expression <i>should</i> be evaluated when the agent first starts up. This is the default behaviour.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Notifications triggered by this initial evaluation will be sent <i>before</i> the coldStart trap.</dl>
</dl>
<dt>-u SECNAME</p>
<dd>specifies a security name to use for scanning the local host, instead of the default <i>iquerySecName</i>. Once again, this user must be explicitly created and given suitable access rights.</dl>
</dl>
<dt>notificationEvent ENAME NOTIFICATION [-m] [-i OID | -o OID ]*</p>
<dd>defines a notification event named ENAME. This can be triggered from a given <i>monitor</i> entry by specifying the option <i>-e ENAME</i> (see above). NOTIFICATION should be the OID of the NOTIFICATION-TYPE definition for the notification to be generated.</p>
<dd>If the <i>-m</i> option is given, the notification payload will include the standard varbinds as specified in the OBJECTS clause of the notification MIB definition. This option must come <code>after</code> the NOTIFICATION OID (and the relevant MIB file must be available and loaded by the agent). Otherwise, these varbinds must be listed explicitly (either here or in the corresponding <i>monitor</i> directive).</p>
<dd>The <i>-i OID</i> and <i>-o OID</i> options specify additional varbinds to be appended to the notification payload, after the standard list. If the monitor entry that triggered this event involved a wildcarded expression, the suffix of the matched instance will be added to any OIDs specified using <i>-o</i>, while OIDs specified using <i>-i</i> will be treated as exact instances. If the <i>-I</i> flag was specified to the <i>monitor</i> directive, then there is no difference between these two options.</p>
<dt>setEvent ENAME [-I] OID = VALUE</p>
<dd>defines a set event named ENAME, assigning the (integer) VALUE to the specified OID. This can be triggered from a given <i>monitor</i> entry by specifying the option <i>-e ENAME</i> (see above).</p>
<dd>If the monitor entry that triggered this event involved a wildcarded expression, the suffix of the matched instance will normally be added to the OID. If the <i>-I</i> flag was specified to either of the <i>monitor</i> or <i>setEvent</i> directives, the specified OID will be regarded as an exact single instance.</p>
<dt>strictDisman yes</p>
<dd>The definition of SNMP notifications states that the varbinds defined in the OBJECT clause should come first (in the order specified), followed by any &quot;extra&quot; varbinds that the notification generator feels might be useful. The most natural approach would be to associate these mandatory varbinds with the <i>notificationEvent</i> entry, and append any varbinds associated with the monitor entry that triggered the notification to the end of this list. This is the default behaviour of the Net-SNMP Event MIB implementation.</p>
<dd>Unfortunately, the DisMan Event MIB specifications actually state that the trigger-related varbinds should come <code>first</code>, followed by the event-related ones. This directive can be used to restore this strictly-correct (but inappropriate) behaviour.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Strict DisMan ordering may result in generating invalid notifications payload lists if the <i>notificationEvent -n</i> flag is used together with <i>monitor -o</i> (or <i>-i</i>) varbind options.</dl>
</dl>
<dd>If no <i>monitor</i> entries specify payload varbinds, then the setting of this directive is irrelevant.</p>
<dt>linkUpDownNotifications yes</p>
<dd>will configure the Event MIB tables to monitor the ifTable for network interfaces being taken up or down, and triggering a <i>linkUp</i> or <i>linkDown</i> notification as appropriate.</p>
<dd>This is exactly equivalent to the configuration:</p>
<dl>
<dd>
<dl>
<dd>
<pre>notificationEvent linkUpTrap linkUp ifIndex ifAdminStatus ifOperStatus
notificationEvent linkDownTrap linkDown ifIndex ifAdminStatus ifOperStatus
monitor -r 60 -e linkUpTrap &quot;Generate linkUp&quot; ifOperStatus != 2
monitor -r 60 -e linkDownTrap &quot;Generate linkDown&quot; ifOperStatus == 2</pre>
</dl>
</dl>
<dt>defaultMonitors yes</p>
<dd>will configure the Event MIB tables to monitor the various UCD-SNMP-MIB tables for problems (as indicated by the appropriate xxErrFlag column objects).</p>
<dd>This is exactly equivalent to the configuration:</p>
<dl>
<dd>
<dl>
<dd>
<pre>monitor -o prNames -o prErrMessage &quot;process table&quot; prErrorFlag != 0
monitor -o memErrorName -o memSwapErrorMsg &quot;memory&quot; memSwapError != 0
monitor -o extNames -o extOutput &quot;extTable&quot; extResult != 0
monitor -o dskPath -o dskErrorMsg &quot;dskTable&quot; dskErrorFlag != 0
monitor -o laNames -o laErrMessage &quot;laTable&quot; laErrorFlag != 0
monitor -o fileName -o fileErrorMsg &quot;fileTable&quot; fileErrorFlag != 0</pre>
</dl>
</dl>
</dl>
<p> In both these latter cases, the snmpd.conf must also contain a <i>iquerySecName</i> directive, together with a corresponding <i>createUser</i> entry and suitable access control configuration.</p>
<h3>DisMan Schedule MIB</h3>
<p>The DisMan working group also produced a mechanism for scheduling particular actions (a specified SET assignment) at given times. This requires that the agent was built with support for the <i>disman/schedule</i> module (which is included as part of the default build configuration for the most recent distribution). </p>
<p> There are three ways of specifying the scheduled action:</p>
<dl>
<dt>repeat FREQUENCY OID = VALUE</p>
<dd>configures a SET assignment of the (integer) VALUE to the MIB instance OID, to be run every FREQUENCY seconds, where FREQUENCY is in seconds or optionally suffixed by one of s (for seconds), m (for minutes), h (for hours), d (for days), or w (for weeks).</p>
<dt>cron MINUTE HOUR DAY MONTH WEEKDAY OID = VALUE</p>
<dd>configures a SET assignment of the (integer) VALUE to the MIB instance OID, to be run at the times specified by the fields MINUTE to WEEKDAY. These follow the same pattern as the equivalent <i><a href="/docs/linux/man/5-crontab/">crontab</a>(5)</i> fields.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>These fields should be specified as a (comma-separated) list of numeric values. Named values for the MONTH and WEEKDAY fields are not supported, and neither are value ranges. A wildcard match can be specified as &#8216;*&#8217;.</dl>
</dl>
<dd>The DAY field can also accept negative values, to indicate days counting backwards from the end of the month.</p>
<dt>at MINUTE HOUR DAY MONTH WEEKDAY OID = VALUE</p>
<dd>configures a one-shot SET assignment, to be run at the first matching time as specified by the fields MINUTE to WEEKDAY. The interpretation of these fields is exactly the same as for the <i>cron</i> directive.</dl>
<h3>Data Delivery via Notfiications</h3>
<p>Note: this functionality is only available if the <i>deliver/deliverByNotify</i> mib module was complied in to the agent </p>
<p> In some situations it may be advantageous to deliver SNMP data over SNMP Notifications (TRAPs and INFORMs) rather than the typical process of having the manager issue requests for the data (via GETs and GETNEXTs). Reasons for doing this are numerous, but frequently corner cases. The most common reason for wanting this behaviour might be to monitor devices that reside behind NATs or Firewalls that prevent incoming SNMP traffic. </p>
<p> It should be noted that although most management software is capable of logging notifications, very little (if any) management software will updated their &quot;knowledge database&quot; based on the contents of SNMP notifications. IE, it won&#8217;t (for example) update the interface traffic counter history that is used to produce graphs. Most larger network management packages have a separate database for storing data received via SNMP requests (GETs and GETNEXTs) vs those received from notifications. Researching the capabilities of your management station software is required before assuming this functionality will solve your data delivery requirements. </p>
<p> Notifications generated via this mechanism will be sent to the standard set of configured notification targets. See the &quot;Notification Handling&quot; section of this document for further information.</p>
<dl>
<dt>deliverByNotify [-p] [-m] [-s MAXSIZE] FREQUENCY OID</p>
<dd>This directive tells the SNMP agent to self-walk the <i>OID</i>, collect all the data and send it out every <i>FREQUENCY</i> seconds, where FREQUENCY is in seconds or optionally suffixed by one of s (for seconds), m (for minutes), h (for hours), d (for days), or w (for weeks). By default scalars are included in the notification that specify the how often the notification will be sent (unless the <i>-p</i> option is specified) and which message number of how many messages a particular notification is (unless <i>-m</i> is specified). To break the notifications into manageable packet sizes, use the <i>-s</i> flag to specify the approximate maximum number of bytes that a notification message should be limited to. If more than <i>MAXSIZE</i> of bytes is needed then multiple notifications will be sent to deliver the data. Note that the calculations for ensuring the maximum size is met are approximations and thus it can be absolutely guaranteed they&#8217;ll be under that size, so leave a padding buffer if it is critical that you avoid fragmentation. A value of -1 indicates force everything into a single message no matter how big it is.</p>
<dd>Example usage: the following will deliver the contents of the ifTable once an hour and the contents of the system group once every 2 hours:</p>
<dl>
<dd>
<pre>deliverByNotify 3600 ifTable
deliverByNotify 7200 system</pre>
</dl>
<dt>deliverByNotifyMaxPacketSize SIZEINBYTES</p>
<dd>Sets the default notification size limit (see the <i>-s</i> flag above).</p>
<dt>deliverByNotifyOid OID</p>
<dd>
<dt>deliverByNotifyFrequencyOid OID</p>
<dd>
<dt>deliverByNotifyMessageNumberOid OID</p>
<dd>
<dt>deliverByNotifyMaxMessageNumberOid OID</p>
<dd>These set the data OID that the notification will be sent under, the scalar OID, the message number OID, and the maximum message number OID. These default to objects in the NET-SNMP-PERIODIC-NOTIFY-MIB.</dl>
<h2>Extending Agent Functionality</h2>
<p>One of the first distinguishing features of the original UCD suite was the ability to extend the functionality of the agent &#8211; not just by recompiling with code for new MIB modules, but also by configuring the running agent to report additional information. There are a number of techniques to support this, including:</p>
<dl>
<dt>&bull;</p>
<dd>running external commands (<i>exec</i>, <i>extend</i>, <i>pass</i>)</p>
<dt>&bull;</p>
<dd>loading new code dynamically (embedded perl, <i>dlmod</i>)</p>
<dt>&bull;</p>
<dd>communicating with other agents (<i>proxy</i>, SMUX, AgentX)</dl>
<h3>Arbitrary Extension Commands</h3>
<p>The earliest extension mechanism was the ability to run arbitrary commands or shell scripts. Such commands do not need to be aware of SNMP operations, or conform to any particular behaviour &#8211; the MIB structures are designed to accommodate any form of command output. Use of this mechanism requires that the agent was built with support for the <i>ucd-snmp/extensible</i> and/or <i>agent/extend</i> modules (which are both included as part of the default build configuration).</p>
<dl>
<dt>exec [MIBOID] NAME PROG ARGS</p>
<dd>
<dt>sh [MIBOID] NAME PROG ARGS</p>
<dd>invoke the named PROG with arguments of ARGS. By default the exit status and first line of output from the command will be reported via the extTable, discarding any additional output.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Entries in this table appear in the order they are read from the configuration file. This means that adding new <i>exec</i> (or <i>sh</i>) directives and restarting the agent, may affect the indexing of other entries.</dl>
</dl>
<dd>The PROG argument for <i>exec</i> directives must be a full path to a real binary, as it is executed via the exec() system call. To invoke a shell script, use the <i>sh</i> directive instead.</p>
<dd>If MIBOID is specified, then the results will be rooted at this point in the OID tree, returning the exit statement as MIBOID.100.0 and the entire command output in a pseudo-table based at MIBNUM.101 &#8211; with one &#8216;row&#8217; for each line of output.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>The layout of this &quot;relocatable&quot; form of <i>exec</i> (or <i>sh</i>) output does not strictly form a valid MIB structure. This mechanism is being deprecated &#8211; please see the <i>extend</i> directive (described below) instead.</dl>
</dl>
<dd>The agent does not cache the exit status or output of the executed program.</p>
<dt>execfix NAME PROG ARGS</p>
<dd>registers a command that can be invoked on demand &#8211; typically to respond to or fix errors with the corresponding <i>exec</i> or <i>sh</i> entry. When the <i>extErrFix</i> instance for a given NAMEd entry is set to the integer value of 1, this command will be called.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This directive can only be used in combination with a corresponding <i>exec</i> or <i>sh</i> directive, which must be defined first. Attempting to define an unaccompanied <i>execfix</i> directive will fail.</dl>
</dl>
</dl>
<p> <i>exec</i> and <i>sh</i> extensions can only be configured via the snmpd.conf file. They cannot be set up via SNMP SET requests.</p>
<dl>
<dt>extend [MIBOID] NAME PROG ARGS</p>
<dd>works in a similar manner to the <i>exec</i> directive, but with a number of improvements. The MIB tables (<i>nsExtendConfigTable</i> etc) are indexed by the NAME token, so are unaffected by the order in which entries are read from the configuration files. There are <i>two</i> result tables &#8211; one (<i>nsExtendOutput1Table</i>) containing the exit status, the first line and full output (as a single string) for each <i>extend</i> entry, and the other (<i>nsExtendOutput2Table</i>) containing the complete output as a series of separate lines.</p>
<dd>If MIBOID is specified, then the configuration and result tables will be rooted at this point in the OID tree, but are otherwise structured in exactly the same way. This means that several separate <i>extend</i> directives can specify the same MIBOID root, without conflicting.</p>
<dd>The exit status and output is cached for each entry individually, and can be cleared (and the caching behaviour configured) using the nsCacheTable.</p>
<dt>extendfix NAME PROG ARGS</p>
<dd>registers a command that can be invoked on demand, by setting the appropriate <i>nsExtendRunType</i> instance to the value <i><a href="/docs/linux/man/3-run-command/">run-command</a>(3)</i>. Unlike the equivalent <i>execfix</i>, this directive does not need to be paired with a corresponding <i>extend</i> entry, and can appear on its own.</dl>
<p> Both <i>extend</i> and <i>extendfix</i> directives can be configured dynamically, using SNMP SET requests to the NET-SNMP-EXTEND-MIB.</p>
<h3>MIB-Specific Extension Commands</h3>
<p>The first group of extension directives invoke arbitrary commands, and rely on the MIB structure (and management applications) having the flexibility to accommodate and interpret the output. This is a convenient way to make information available quickly and simply, but is of no use when implementing specific MIB objects, where the extension must conform to the structure of the MIB (rather than vice versa). The remaining extension mechanisms are all concerned with such MIB-specific situations &#8211; starting with &quot;pass-through&quot; scripts. Use of this mechanism requires that the agent was built with support for the <i>ucd-snmp/pass</i> and <i>ucd-snmp/pass_persist</i> modules (which are both included as part of the default build configuration).</p>
<dl>
<dt>pass [-p priority] MIBOID PROG</p>
<dd>will pass control of the subtree rooted at MIBOID to the specified PROG command. GET and GETNEXT requests for OIDs within this tree will trigger this command, called as:</p>
<dl>
<dd>
<dl>
<dd>PROG -g OID</p>
<dd>PROG -n OID</dl>
</dl>
<dd>respectively, where OID is the requested OID. The PROG command should return the response varbind as three separate lines printed to stdout &#8211; the first line should be the OID of the returned value, the second should be its TYPE (one of the text strings <code>integer, gauge, counter, timeticks, ipaddress, objectid,</code> or <code>string</code> ), and the third should be the value itself.</p>
<dd>If the command cannot return an appropriate varbind &#8211; e.g the specified OID did not correspond to a valid instance for a GET request, or there were no following instances for a GETNEXT &#8211; then it should exit without producing any output. This will result in an SNMP <i>noSuchName</i> error, or a <i>noSuchInstance</i> exception.</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>The SMIv2 type <code>counter64</code> and SNMPv2 <i>noSuchObject</i> exception are not supported.</dl>
</dl>
</dl>
<dd>A SET request will result in the command being called as:</p>
<dl>
<dd>
<dl>
<dd>PROG -s OID TYPE VALUE</dl>
</dl>
<dd>where TYPE is one of the tokens listed above, indicating the type of the value passed as the third parameter.</p>
<dd>If the assignment is successful, the PROG command should exit without producing any output. Errors should be indicated by writing one of the strings <code>not-writable, </code> or <code>wrong-type</code> to stdout, and the agent will generate the appropriate error response.</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>The other SNMPv2 errors are not supported.</dl>
</dl>
</dl>
<dd>In either case, the command should exit once it has finished processing. Each request (and each varbind within a single request) will trigger a separate invocation of the command.</p>
<dd>The default registration priority is 127. This can be changed by supplying the optional -p flag, with lower priority registrations being used in preference to higher priority values.</p>
<dt>pass_persist [-p priority] MIBOID PROG</p>
<dd>will also pass control of the subtree rooted at MIBOID to the specified PROG command. However this command will continue to run after the initial request has been answered, so subsequent requests can be processed without the startup overheads.</p>
<dd>Upon initialization, PROG will be passed the string &quot;PING
&quot; on stdin, and should respond by printing &quot;PONG
&quot; to stdout.</p>
<dd>For GET and GETNEXT requests, PROG will be passed two lines on stdin, the command (<i>get</i> or <i>getnext</i>) and the requested OID. It should respond by printing three lines to stdout &#8211; the OID for the result varbind, the TYPE and the VALUE itself &#8211; exactly as for the <i>pass</i> directive above. If the command cannot return an appropriate varbind, it should print print &quot;NONE
&quot; to stdout (but continue running).</p>
<dd>For SET requests, PROG will be passed three lines on stdin, the command (<i>set</i>) and the requested OID, followed by the type and value (both on the same line). If the assignment is successful, the command should print &quot;DONE
&quot; to stdout. Errors should be indicated by writing one of the strings <code>not-writable, </code> <code>wrong-type,</code> <code>wrong-length,</code> <code>wrong-value</code> or <code>inconsistent-value</code> to stdout, and the agent will generate the appropriate error response. In either case, the command should continue running.</p>
<dd>The registration priority can be changed using the optional -p flag, just as for the <i>pass</i> directive.</dl>
<p> <i>pass</i> and <i>pass_persist</i> extensions can only be configured via the snmpd.conf file. They cannot be set up via SNMP SET requests.</p>
<h3>Embedded Perl Support</h3>
<p>Programs using the previous extension mechanisms can be written in any convenient programming language &#8211; including perl, which is a common choice for pass-through extensions in particular. However the Net-SNMP agent also includes support for embedded perl technology (similar to <i>mod_perl</i> for the Apache web server). This allows the agent to interpret perl scripts directly, thus avoiding the overhead of spawning processes and initializing the perl system when a request is received. </p>
<p> Use of this mechanism requires that the agent was built with support for the embedded perl mechanism, which is not part of the default build environment. It must be explicitly included by specifying the &#8216;&#8211;enable-embedded-perl&#8217; option to the configure script when the package is first built. </p>
<p> If enabled, the following directives will be recognised:</p>
<dl>
<dt>disablePerl true</p>
<dd>will turn off embedded perl support entirely (e.g. if there are problems with the perl installation).</p>
<dt>perlInitFile FILE</p>
<dd>loads the specified initialisation file (if present) immediately before the first <i>perl</i> directive is parsed. If not explicitly specified, the agent will look for the default initialisation file /usr/share/snmp/snmp_perl.pl.</p>
<dd>The default initialisation file creates an instance of a NetSNMP::agent object &#8211; a variable $agent which can be used to register perl-based MIB handler routines.</p>
<dt>perl EXPRESSION</p>
<dd>evaluates the given expression. This would typically register a handler routine to be called when a section of the OID tree was requested:</p>
<dl>
<dd>
<dl>
<dd>
<pre>perl use Data::Dumper;
perl sub myroutine { print &quot;got called: &quot;,Dumper(@_),&quot;
&quot;; }
perl $agent-&gt;register('mylink', '.1.3.6.1.8765', \&amp;myroutine);</pre>
</dl>
</dl>
<dd>This expression could also source an external file:</p>
<dl>
<dd>
<dl>
<dd>perl &#8216;do /path/to/file.pl&#8217;;</dl>
</dl>
<dd>or perform any other perl-based processing that might be required.</dl>
<h3>Dynamically Loadable Modules</h3>
<p>Most of the MIBs supported by the Net-SNMP agent are implemented as C code modules, which were compiled and linked into the agent libraries when the suite was first built. Such implementation modules can also be compiled independently and loaded into the running agent once it has started. Use of this mechanism requires that the agent was built with support for the <i>ucd-snmp/dlmod</i> module (which is included as part of the default build configuration).</p>
<dl>
<dt>dlmod NAME PATH</p>
<dd>will load the shared object module from the file PATH (an absolute filename), and call the initialisation routine <i>init_NAME</i>.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>If the specified PATH is not a fully qualified filename, it will be interpreted relative to /usr/lib(64)/snmp/dlmod, and .so will be appended to the filename.</dl>
</dl>
</dl>
<p> This functionality can also be configured using SNMP SET requests to the UCD-DLMOD-MIB.</p>
<h3>Proxy Support</h3>
<p>Another mechanism for extending the functionality of the agent is to pass selected requests (or selected varbinds) to another SNMP agent, which can be running on the same host (presumably listening on a different port), or on a remote system. This can be viewed either as the main agent delegating requests to the remote one, or acting as a proxy for it. Use of this mechanism requires that the agent was built with support for the <i>ucd-snmp/proxy</i> module (which is included as part of the default build configuration).</p>
<dl>
<dt>proxy [-Cn CONTEXTNAME] [SNMPCMD_ARGS] HOST OID [REMOTEOID]</p>
<dd>will pass any incoming requests under OID to the agent listening on the port specified by the transport address HOST. See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>To proxy the entire MIB tree, use the OID .1.3 (<code>not</code> the top-level .1)</dl>
</dl>
</dl>
<p> The <i>SNMPCMD_ARGS</i> should provide sufficient version and administrative information to generate a valid SNMP request (see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i>).</p>
<dl>
<dt>Note:</p>
<dd>The proxied request will <i>not</i> use the administrative settings from the original request.</dl>
<p> If a CONTEXTNAME is specified, this will register the proxy delegation within the named context in the local agent. Defining multiple <i>proxy</i> directives for the same OID but different contexts can be used to query several remote agents through a single proxy, by specifying the appropriate SNMPv3 context in the incoming request (or using suitable configured community strings &#8211; see the <i>com2sec</i> directive). </p>
<p> Specifying the REMOID parameter will map the local MIB tree rooted at OID to an equivalent subtree rooted at REMOID on the remote agent.</p>
<h3>SMUX Sub-Agents</h3>
<p>The Net-SNMP agent supports the SMUX protocol (RFC 1227) to communicate with SMUX-based subagents (such as <i>gated</i>, <i>zebra</i> or <i>quagga</i>). Use of this mechanism requires that the agent was built with support for the <i>smux</i> module, which is not part of the default build environment, and must be explicitly included by specifying the &#8216;&#8211;with-mib-modules=smux&#8217; option to the configure script when the package is first built.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This extension protocol has been officially deprecated in favour of AgentX (see below).</dl>
</dl>
<dl>
<dt>smuxpeer OID PASS</p>
<dd>will register a subtree for SMUX-based processing, to be authenticated using the password PASS. If a subagent (or &quot;peer&quot;) connects to the agent and registers this subtree then requests for OIDs within it will be passed to that SMUX subagent for processing.</p>
<dd>A suitable entry for an OSPF routing daemon (such as <i>gated</i>, <i>zebra</i> or <i>quagga</i>) might be something like</p>
<dl>
<dd>
<dl>
<dd><i>smuxpeer .1.3.6.1.2.1.14 ospf_pass</i></dl>
</dl>
<dt>smuxsocket &lt;IPv4-address&gt;</p>
<dd>defines the IPv4 address for SMUX peers to communicate with the Net-SNMP agent. The default is to listen on all IPv4 interfaces (&quot;0.0.0.0&quot;), unless the package has been configured with &quot;&#8211;enable-local-smux&quot; at build time, which causes it to only listen on 127.0.0.1 by default. SMUX uses the well-known TCP port 199.</dl>
<p> Note the Net-SNMP agent will only operate as a SMUX <i>master</i> agent. It does not support acting in a SMUX subagent role.</p>
<h3>AgentX Sub-Agents</h3>
<p>The Net-SNMP agent supports the AgentX protocol (RFC 2741) in both master and subagent roles. Use of this mechanism requires that the agent was built with support for the <i>agentx</i> module (which is included as part of the default build configuration), and also that this support is explicitly enabled (e.g. via the <i>snmpd.conf</i> file). </p>
<p> There are two directives specifically relevant to running as an AgentX master agent:</p>
<dl>
<dt>master agentx</p>
<dd>will enable the AgentX functionality and cause the agent to start listening for incoming AgentX registrations. This can also be activated by specifying the &#8216;-x&#8217; command-line option (to specify an alternative listening socket).</p>
<dt>agentXPerms SOCKPERMS [DIRPERMS [USER|UID [GROUP|GID]]]</p>
<dd>Defines the permissions and ownership of the AgentX Unix Domain socket, and the parent directories of this socket. SOCKPERMS and DIRPERMS must be octal digits (see <i><a href="/docs/linux/man/1-chmod/">chmod</a>(1)</i> ). By default this socket will only be accessible to subagents which have the same userid as the agent.</dl>
<p> There is one directive specifically relevant to running as an AgentX sub-agent:</p>
<dl>
<dt>agentXPingInterval NUM</p>
<dd>will make the subagent try and reconnect every NUM seconds to the master if it ever becomes (or starts) disconnected.</dl>
<p> The remaining directives are relevant to both AgentX master and sub-agents:</p>
<dl>
<dt>agentXSocket [&lt;transport-specifier&gt;:]&lt;transport-address&gt;[,&#8230;]</p>
<dd>defines the address the master agent listens at, or the subagent should connect to. The default is the Unix Domain socket &quot;/var/agentx/master&quot;. Another common alternative is tcp:localhost:705. See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of addresses.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Specifying an AgentX socket does <code>not</code> automatically enable AgentX functionality (unlike the &#8216;-x&#8217; command-line option).</dl>
</dl>
<dt>agentXTimeout NUM</p>
<dd>defines the timeout period (NUM seconds) for an AgentX request. Default is 1 second. NUM also be specified with a suffix of one of s (for seconds), m (for minutes), h (for hours), d (for days), or w (for weeks).</p>
<dt>agentXRetries NUM</p>
<dd>defines the number of retries for an AgentX request. Default is 5 retries.</dl>
<p> net-snmp ships with both C and Perl APIs to develop your own AgentX subagent.</p>
<h2>Other Configuration</h2>
<dl>
<dt>override [-rw] OID TYPE VALUE</p>
<dd>This directive allows you to override a particular OID with a different value (and possibly a different type of value). The -rw flag will allow snmp SETs to modify it&#8217;s value as well. (note that if you&#8217;re overriding original functionality, that functionality will be entirely lost. Thus SETS will do nothing more than modify the internal overridden value and will not perform any of the original functionality intended to be provided by the MIB object. It&#8217;s an emulation only.) An example:</p>
<dl>
<dd>
<dl>
<dd>override sysDescr.0 octet_str &quot;my own sysDescr&quot;</dl>
</dl>
<dd>That line will set the sysDescr.0 value to &quot;my own sysDescr&quot; as well as make it modifiable with SNMP SETs as well (which is actually illegal according to the MIB specifications).</p>
<dd>Note that care must be taken when using this. For example, if you try to override a property of the 3rd interface in the ifTable with a new value and later the numbering within the ifTable changes it&#8217;s index ordering you&#8217;ll end up with problems and your modified value won&#8217;t appear in the right place in the table.</p>
<dd>Valid TYPEs are: integer, uinteger, octet_str, object_id, counter, null (for gauges, use &quot;uinteger&quot;; for bit strings, use &quot;octet_str&quot;). Note that setting an object to &quot;null&quot; effectively delete&#8217;s it as being accessible. No VALUE needs to be given if the object type is null.</p>
<dd>More types should be available in the future.</dl>
<p> If you&#8217;re trying to figure out aspects of the various mib modules (possibly some that you&#8217;ve added yourself), the following may help you spit out some useful debugging information. First off, please read the snmpd manual page on the -D flag. Then the following configuration snmpd.conf token, combined with the -D flag, can produce useful output:</p>
<dl>
<dt>injectHandler HANDLER modulename [beforeThis]</p>
<dd>This will insert new handlers into the section of the mib tree referenced by &quot;modulename&quot;. If &quot;beforeThis&quot; is specified then the module will be injected before the named module. This is useful for getting a handler into the exact right position in the chain.</p>
<dd>The types of handlers available for insertion are:</p>
<dl>
<dd>
<dl>
<dt>stash_cache</p>
<dd>Caches information returned from the lower level. This greatly help the performance of the agent, at the cost of caching the data such that its no longer &quot;live&quot; for 30 seconds (in this future, this will be configurable). Note that this means snmpd will use more memory as well while the information is cached. Currently this only works for handlers registered using the table_iterator support, which is only a few mib tables. To use it, you need to make sure to install it before the table_iterator point in the chain, so to do this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>injectHandler stash_cache NAME table_iterator </p>
<p> If you want a table to play with, try walking the nsModuleTable with and without this injected. </p>
<dt>debug</p>
<dd>Prints out lots of debugging information when the -Dhelper:debug flag is passed to the snmpd application. </p>
<dt>read_only</p>
<dd>Forces turning off write support for the given module. </p>
<dt>serialize</p>
<dd>If a module is failing to handle multiple requests properly (using the new 5.0 module API), this will force the module to only receive one request at a time. </p>
<dt>bulk_to_next</p>
<dd>If a module registers to handle getbulk support, but for some reason is failing to implement it properly, this module will convert all getbulk requests to getnext requests before the final module receives it.</dl>
</dl>
<dt>dontLogTCPWrappersConnects</p>
<dd>If the <code>snmpd</code> was compiled with TCP Wrapper support, it logs every connection made to the agent. This setting disables the log messages for accepted connections. Denied connections will still be logged.</p>
<dt>Figuring out module names</p>
<dd>To figure out which modules you can inject things into, run <code>snmpwalk</code> on the nsModuleTable which will give a list of all named modules registered within the agent.</dl>
<h3>Internal Data tables</h3>
<dl>
<dt>table NAME</p>
<dd>
<dt>add_row NAME INDEX(ES) VALUE(S)</p>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt>o</p>
<dd>The Net-SNMP agent can be instructed to re-read the various configuration files, either via an <code>snmpset</code> assignment of <a href="/docs/linux/man/1-integer/">integer</a>(1) to UCD-SNMP-MIB::versionUpdateConfig.0 (.1.3.6.1.4.1.2021.100.11.0), or by sending a <code>kill -HUP</code> signal to the agent process.</p>
<dt>o</p>
<dd>All directives listed with a value of &quot;yes&quot; actually accept a range of boolean values. These will accept any of <i>1</i>, <i>yes</i> or <i>true</i> to enable the corresponding behaviour, or any of <i>0</i>, <i>no</i> or <i>false</i> to disable it. The default in each case is for the feature to be turned off, so these directives are typically only used to enable the appropriate behaviour.</dl>
<h2>Example Configuration File</h2>
<p>See the EXAMPLE.CONF file in the top level source directory for a more detailed example of how the above information is used in real examples.</p>
<h2>Files</h2>
<p>/etc/snmp/snmpd.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-snmpconf/">snmpconf</a>(1), <a href="/docs/linux/man/1-snmpusm/">snmpusm</a>(1), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/8-snmpd/">snmpd</a>(8), EXAMPLE.conf, <a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3). </p>
