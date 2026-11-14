---
title: "nm-settings-nmcli(5)"
name: "nm-settings-nmcli"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nm-settings-nmcli/"
description: "nm-settings-nmcli – Description of settings and properties of NetworkManager connection profiles for nmcli"
---

<p>nm-settings-nmcli &#8211; Description of settings and properties of NetworkManager connection profiles for nmcli</p>
<h2>Description</h2>
<p>NetworkManager is based on a concept of connection profiles, sometimes referred to as connections only. These connection profiles contain a network configuration. When NetworkManager activates a connection profile on a network device the configuration will be applied and an active network connection will be established. Users are free to create as many connection profiles as they see fit. Thus they are flexible in having various network configurations for different networking needs. </p>
<p> NetworkManager provides an API for configuring connection profiles, for activating them to configure the network, and inspecting the current network configuration. The command line tool <i>nmcli</i> is a client application to NetworkManager that uses this API. See <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1) for details. </p>
<p> With commands like nmcli connection add, nmcli connection modify and nmcli connection show, connection profiles can be created, modified and inspected. A profile consists of properties. On D-Bus this follows the format as described by <code><a href="/docs/linux/man/5-nm-settings-dbus/">nm-settings-dbus</a></code>(5), while this manual page describes the settings format how they are expected by <i>nmcli</i>. </p>
<p> The settings and properties shown in tables below list all available connection configuration options. However, note that not all settings are applicable to all connection types. <i>nmcli</i> connection editor has also a built-in <i>describe</i> command that can display description of particular settings and properties of this page. </p>
<p> The <i>setting</i> and <i>property</i> can be abbreviated provided they are unique. The list below also shows aliases that can be used unqualified instead of the full name. For example connection.interface-name and ifname refer to the same property.</p>
<h3>connection setting</h3>
<p>General Connection Profile Settings. </p>
<p> Properties: </p>
<p> <code>auth-retries</code></p>
<dl>
<dd>The number of retries for the authentication. Zero means to try indefinitely; -1 means to use a global default. If the global default is not set, the authentication retries for 3 times before failing the connection. Currently, this only applies to 802-1x authentication. </p>
<p> Format: int32</dl>
<p> <code>autoconnect</code></p>
<dl>
<dd>Alias: autoconnect </p>
<p> Whether or not the connection should be automatically connected by NetworkManager when the resources for the connection are available. TRUE to automatically activate the connection, FALSE to require manual intervention to activate the connection. Autoconnect happens when the circumstances are suitable. That means for example that the device is currently managed and not active. Autoconnect thus never replaces or competes with an already active profile. Note that autoconnect is not implemented for VPN profiles. See &quot;secondaries&quot; as an alternative to automatically connect VPN profiles. </p>
<p> Format: boolean</dl>
<p> <code>autoconnect-priority</code></p>
<dl>
<dd>The autoconnect priority in range -999 to 999. If the connection is set to autoconnect, connections with higher priority will be preferred. The higher number means higher priority. Defaults to 0. Note that this property only matters if there are more than one candidate profile to select for autoconnect. In case of equal priority, the profile used most recently is chosen. </p>
<p> Format: int32</dl>
<p> <code>autoconnect-retries</code></p>
<dl>
<dd>The number of times a connection should be tried when autoactivating before giving up. Zero means forever, -1 means the global default (4 times if not overridden). Setting this to 1 means to try activation only once before blocking autoconnect. Note that after a timeout, NetworkManager will try to autoconnect again. </p>
<p> Format: int32</dl>
<p> <code>autoconnect-slaves</code></p>
<dl>
<dd>Whether or not slaves of this connection should be automatically brought up when NetworkManager activates this connection. This only has a real effect for master connections. The properties &quot;autoconnect&quot;, &quot;autoconnect-priority&quot; and &quot;autoconnect-retries&quot; are unrelated to this setting. The permitted values are: 0: leave slave connections untouched, 1: activate all the slave connections with this connection, -1: default. If -1 (default) is set, global connection.autoconnect-slaves is read to determine the real value. If it is default as well, this fallbacks to 0. </p>
<p> Format: NMSettingConnectionAutoconnectSlaves (int32)</dl>
<p> <code>dns-over-tls</code></p>
<dl>
<dd>Whether DNSOverTls (dns-over-tls) is enabled for the connection. DNSOverTls is a technology which uses TLS to encrypt dns traffic. The permitted values are: &quot;yes&quot; (2) use DNSOverTls and disabled fallback, &quot;opportunistic&quot; (1) use DNSOverTls but allow fallback to unencrypted resolution, &quot;no&quot; (0) don&#8217;t ever use DNSOverTls. If unspecified &quot;default&quot; depends on the plugin used. Systemd-resolved uses global setting. This feature requires a plugin which supports DNSOverTls. Otherwise, the setting has no effect. One such plugin is dns-systemd-resolved. </p>
<p> Format: int32</dl>
<p> <code>gateway-ping-timeout</code></p>
<dl>
<dd>If greater than zero, delay success of IP addressing until either the timeout is reached, or an IP gateway replies to a ping. </p>
<p> Format: uint32</dl>
<p> <code>id</code></p>
<dl>
<dd>Alias: con-name </p>
<p> A human readable unique identifier for the connection, like &quot;Work Wi-Fi&quot; or &quot;T-Mobile 3G&quot;. </p>
<p> Format: string</dl>
<p> <code>interface-name</code></p>
<dl>
<dd>Alias: ifname </p>
<p> The name of the network interface this connection is bound to. If not set, then the connection can be attached to any interface of the appropriate type (subject to restrictions imposed by other settings). For software devices this specifies the name of the created device. For connection types where interface names cannot easily be made persistent (e.g. mobile broadband or USB Ethernet), this property should not be used. Setting this property restricts the interfaces a connection can be used with, and if interface names change or are reordered the connection may be applied to the wrong interface. </p>
<p> Format: string</dl>
<p> <code>lldp</code></p>
<dl>
<dd>Whether LLDP is enabled for the connection. </p>
<p> Format: int32</dl>
<p> <code>llmnr</code></p>
<dl>
<dd>Whether Link-Local Multicast Name Resolution (LLMNR) is enabled for the connection. LLMNR is a protocol based on the Domain Name System (DNS) packet format that allows both IPv4 and IPv6 hosts to perform name resolution for hosts on the same local link. The permitted values are: &quot;yes&quot; (2) register hostname and resolving for the connection, &quot;no&quot; (0) disable LLMNR for the interface, &quot;resolve&quot; (1) do not register hostname but allow resolving of LLMNR host names If unspecified, &quot;default&quot; ultimately depends on the DNS plugin (which for systemd-resolved currently means &quot;yes&quot;). This feature requires a plugin which supports LLMNR. Otherwise, the setting has no effect. One such plugin is dns-systemd-resolved. </p>
<p> Format: int32</dl>
<p> <code>master</code></p>
<dl>
<dd>Alias: master </p>
<p> Interface name of the master device or UUID of the master connection. </p>
<p> Format: string</dl>
<p> <code>mdns</code></p>
<dl>
<dd>Whether mDNS is enabled for the connection. The permitted values are: &quot;yes&quot; (2) register hostname and resolving for the connection, &quot;no&quot; (0) disable mDNS for the interface, &quot;resolve&quot; (1) do not register hostname but allow resolving of mDNS host names and &quot;default&quot; (-1) to allow lookup of a global default in NetworkManager.conf. If unspecified, &quot;default&quot; ultimately depends on the DNS plugin (which for systemd-resolved currently means &quot;no&quot;). This feature requires a plugin which supports mDNS. Otherwise, the setting has no effect. One such plugin is dns-systemd-resolved. </p>
<p> Format: int32</dl>
<p> <code>metered</code></p>
<dl>
<dd>Whether the connection is metered. When updating this property on a currently activated connection, the change takes effect immediately. </p>
<p> Format: NMMetered (int32)</dl>
<p> <code>mud-url</code></p>
<dl>
<dd>If configured, set to a Manufacturer Usage Description (MUD) URL that points to manufacturer-recommended network policies for IoT devices. It is transmitted as a DHCPv4 or DHCPv6 option. The value must be a valid URL starting with &quot;https://&quot;. The special value &quot;none&quot; is allowed to indicate that no MUD URL is used. If the per-profile value is unspecified (the default), a global connection default gets consulted. If still unspecified, the ultimate default is &quot;none&quot;. </p>
<p> Format: string</dl>
<p> <code>multi-connect</code></p>
<dl>
<dd>Specifies whether the profile can be active multiple times at a particular moment. The value is of type NMConnectionMultiConnect. </p>
<p> Format: int32</dl>
<p> <code>permissions</code></p>
<dl>
<dd>An array of strings defining what access a given user has to this connection. If this is NULL or empty, all users are allowed to access this connection; otherwise users are allowed if and only if they are in this list. When this is not empty, the connection can be active only when one of the specified users is logged into an active session. Each entry is of the form &quot;[type]:[id]:[reserved]&quot;; for example, &quot;user:dcbw:blah&quot;. At this time only the &quot;user&quot; [type] is allowed. Any other values are ignored and reserved for future use. [id] is the username that this permission refers to, which may not contain the &quot;:&quot; character. Any [reserved] information present must be ignored and is reserved for future use. All of [type], [id], and [reserved] must be valid UTF-8. </p>
<p> Format: array of string</dl>
<p> <code>read-only</code></p>
<dl>
<dd>FALSE if the connection can be modified using the provided settings service&#8217;s D-Bus interface with the right privileges, or TRUE if the connection is read-only and cannot be modified. </p>
<p> Format: boolean</dl>
<p> <code>secondaries</code></p>
<dl>
<dd>List of connection UUIDs that should be activated when the base connection itself is activated. Currently, only VPN connections are supported. </p>
<p> Format: array of string</dl>
<p> <code>slave-type</code></p>
<dl>
<dd>Alias: slave-type </p>
<p> Setting name of the device type of this slave&#8217;s master connection (eg, &quot;bond&quot;), or NULL if this connection is not a slave. </p>
<p> Format: string</dl>
<p> <code>stable-id</code></p>
<dl>
<dd>This represents the identity of the connection used for various purposes. It allows to configure multiple profiles to share the identity. Also, the stable-id can contain placeholders that are substituted dynamically and deterministically depending on the context. The stable-id is used for generating IPv6 stable private addresses with ipv6.addr-gen-mode=stable-privacy. It is also used to seed the generated cloned MAC address for ethernet.cloned-mac-address=stable and wifi.cloned-mac-address=stable. It is also used as DHCP client identifier with ipv4.dhcp-client-id=stable and to derive the DHCP DUID with ipv6.dhcp-duid=stable-[llt,ll,uuid]. Note that depending on the context where it is used, other parameters are also seeded into the generation algorithm. For example, a per-host key is commonly also included, so that different systems end up generating different IDs. Or with ipv6.addr-gen-mode=stable-privacy, also the device&#8217;s name is included, so that different interfaces yield different addresses. The per-host key is the identity of your machine and stored in /var/lib/NetworkManager/secret-key. The &#8216;$&#8217; character is treated special to perform dynamic substitutions at runtime. Currently, supported are &quot;${CONNECTION}&quot;, &quot;${DEVICE}&quot;, &quot;${MAC}&quot;, &quot;${BOOT}&quot;, &quot;${RANDOM}&quot;. These effectively create unique IDs per-connection, per-device, per-boot, or every time. Note that &quot;${DEVICE}&quot; corresponds to the interface name of the device and &quot;${MAC}&quot; is the permanent MAC address of the device. Any unrecognized patterns following &#8216;$&#8217; are treated verbatim, however are reserved for future use. You are thus advised to avoid &#8216;$&#8217; or escape it as &quot;$$&quot;. For example, set it to &quot;${CONNECTION}-${BOOT}-${DEVICE}&quot; to create a unique id for this connection that changes with every reboot and differs depending on the interface where the profile activates. If the value is unset, a global connection default is consulted. If the value is still unset, the default is similar to &quot;${CONNECTION}&quot; and uses a unique, fixed ID for the connection. </p>
<p> Format: string</dl>
<p> <code>timestamp</code></p>
<dl>
<dd>The time, in seconds since the Unix Epoch, that the connection was last _successfully_ fully activated. NetworkManager updates the connection timestamp periodically when the connection is active to ensure that an active connection has the latest timestamp. The property is only meant for reading (changes to this property will not be preserved). </p>
<p> Format: uint64</dl>
<p> <code>type</code></p>
<dl>
<dd>Alias: type </p>
<p> Base type of the connection. For hardware-dependent connections, should contain the setting name of the hardware-type specific setting (ie, &quot;802-3-ethernet&quot; or &quot;802-11-wireless&quot; or &quot;bluetooth&quot;, etc), and for non-hardware dependent connections like VPN or otherwise, should contain the setting name of that setting type (ie, &quot;vpn&quot; or &quot;bridge&quot;, etc). </p>
<p> Format: string</dl>
<p> <code>uuid</code></p>
<dl>
<dd>A universally unique identifier for the connection, for example generated with libuuid. It should be assigned when the connection is created, and never changed as long as the connection still applies to the same network. For example, it should not be changed when the &quot;id&quot; property or NMSettingIP4Config changes, but might need to be re-created when the Wi-Fi SSID, mobile broadband network provider, or &quot;type&quot; property changes. The UUID must be in the format &quot;2815492f-7e56-435e-b2e9-246bd7cdc664&quot; (ie, contains only hexadecimal characters and &quot;-&quot;). </p>
<p> Format: string</dl>
<p> <code>wait-device-timeout</code></p>
<dl>
<dd>Timeout in milliseconds to wait for device at startup. During boot, devices may take a while to be detected by the driver. This property will cause to delay NetworkManager-wait-online.service and nm-online to give the device a chance to appear. This works by waiting for the given timeout until a compatible device for the profile is available and managed. The value 0 means no wait time. The default value is -1, which currently has the same meaning as no wait time. </p>
<p> Format: int32</dl>
<p> <code>zone</code></p>
<dl>
<dd>The trust level of a the connection. Free form case-insensitive string (for example &quot;Home&quot;, &quot;Work&quot;, &quot;Public&quot;). NULL or unspecified zone means the connection will be placed in the default zone as defined by the firewall. When updating this property on a currently activated connection, the change takes effect immediately. </p>
<p> Format: string</dl>
<h3>6lowpan setting</h3>
<p>6LoWPAN Settings. </p>
<p> Properties: </p>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID from which this 6LowPAN interface should be created. </p>
<p> Format: string</dl>
<h3>802-1x setting</h3>
<p>IEEE 802.1x Authentication Settings. </p>
<p> Properties: </p>
<p> <code>altsubject-matches</code></p>
<dl>
<dd>List of strings to be matched against the altSubjectName of the certificate presented by the authentication server. If the list is empty, no verification of the server certificate&#8217;s altSubjectName is performed. </p>
<p> Format: array of string</dl>
<p> <code>anonymous-identity</code></p>
<dl>
<dd>Anonymous identity string for EAP authentication methods. Used as the unencrypted identity with EAP types that support different tunneled identity like EAP-TTLS. </p>
<p> Format: string</dl>
<p> <code>auth-timeout</code></p>
<dl>
<dd>A timeout for the authentication. Zero means the global default; if the global default is not set, the authentication timeout is 25 seconds. </p>
<p> Format: int32</dl>
<p> <code>ca-cert</code></p>
<dl>
<dd>Contains the CA certificate if used by the EAP method specified in the &quot;eap&quot; property. Certificate data is specified using a &quot;scheme&quot;; three are currently supported: blob, path and pkcs#11 URL. When using the blob scheme this property should be set to the certificate&#8217;s DER encoded data. When using the path scheme, this property should be set to the full UTF-8 encoded path of the certificate, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. This property can be unset even if the EAP method supports CA certificates, but this allows man-in-the-middle attacks and is NOT recommended. Note that enabling NMSetting8021x:system-ca-certs will override this setting to use the built-in path, if the built-in path is not a directory. </p>
<p> Format: byte array</dl>
<p> <code>ca-cert-password</code></p>
<dl>
<dd>The password used to access the CA certificate stored in &quot;ca-cert&quot; property. Only makes sense if the certificate is stored on a PKCS#11 token that requires a login. </p>
<p> Format: string</dl>
<p> <code>ca-cert-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;ca-cert-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>ca-path</code></p>
<dl>
<dd>UTF-8 encoded path to a directory containing PEM or DER formatted certificates to be added to the verification chain in addition to the certificate specified in the &quot;ca-cert&quot; property. If NMSetting8021x:system-ca-certs is enabled and the built-in CA path is an existing directory, then this setting is ignored. </p>
<p> Format: string</dl>
<p> <code>client-cert</code></p>
<dl>
<dd>Contains the client certificate if used by the EAP method specified in the &quot;eap&quot; property. Certificate data is specified using a &quot;scheme&quot;; two are currently supported: blob and path. When using the blob scheme (which is backwards compatible with NM 0.7.x) this property should be set to the certificate&#8217;s DER encoded data. When using the path scheme, this property should be set to the full UTF-8 encoded path of the certificate, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. </p>
<p> Format: byte array</dl>
<p> <code>client-cert-password</code></p>
<dl>
<dd>The password used to access the client certificate stored in &quot;client-cert&quot; property. Only makes sense if the certificate is stored on a PKCS#11 token that requires a login. </p>
<p> Format: string</dl>
<p> <code>client-cert-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;client-cert-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>domain-match</code></p>
<dl>
<dd>Constraint for server domain name. If set, this list of FQDNs is used as a match requirement for dNSName element(s) of the certificate presented by the authentication server. If a matching dNSName is found, this constraint is met. If no dNSName values are present, this constraint is matched against SubjectName CN using the same comparison. Multiple valid FQDNs can be passed as a &quot;;&quot; delimited list. </p>
<p> Format: string</dl>
<p> <code>domain-suffix-match</code></p>
<dl>
<dd>Constraint for server domain name. If set, this FQDN is used as a suffix match requirement for dNSName element(s) of the certificate presented by the authentication server. If a matching dNSName is found, this constraint is met. If no dNSName values are present, this constraint is matched against SubjectName CN using same suffix match comparison. Since version 1.24, multiple valid FQDNs can be passed as a &quot;;&quot; delimited list. </p>
<p> Format: string</dl>
<p> <code>eap</code></p>
<dl>
<dd>The allowed EAP method to be used when authenticating to the network with 802.1x. Valid methods are: &quot;leap&quot;, &quot;md5&quot;, &quot;tls&quot;, &quot;peap&quot;, &quot;ttls&quot;, &quot;pwd&quot;, and &quot;fast&quot;. Each method requires different configuration using the properties of this setting; refer to wpa_supplicant documentation for the allowed combinations. </p>
<p> Format: array of string</dl>
<p> <code>identity</code></p>
<dl>
<dd>Identity string for EAP authentication methods. Often the user&#8217;s user or login name. </p>
<p> Format: string</dl>
<p> <code>optional</code></p>
<dl>
<dd>Whether the 802.1X authentication is optional. If TRUE, the activation will continue even after a timeout or an authentication failure. Setting the property to TRUE is currently allowed only for Ethernet connections. If set to FALSE, the activation can continue only after a successful authentication. </p>
<p> Format: boolean</dl>
<p> <code>pac-file</code></p>
<dl>
<dd>UTF-8 encoded file path containing PAC for EAP-FAST. </p>
<p> Format: string</dl>
<p> <code>password</code></p>
<dl>
<dd>UTF-8 encoded password used for EAP authentication methods. If both the &quot;password&quot; property and the &quot;password-raw&quot; property are specified, &quot;password&quot; is preferred. </p>
<p> Format: string</dl>
<p> <code>password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>password-raw</code></p>
<dl>
<dd>Password used for EAP authentication methods, given as a byte array to allow passwords in other encodings than UTF-8 to be used. If both the &quot;password&quot; property and the &quot;password-raw&quot; property are specified, &quot;password&quot; is preferred. </p>
<p> Format: byte array</dl>
<p> <code>password-raw-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password-raw&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>phase1-auth-flags</code></p>
<dl>
<dd>Specifies authentication flags to use in &quot;phase 1&quot; outer authentication using NMSetting8021xAuthFlags options. The individual TLS versions can be explicitly disabled. If a certain TLS disable flag is not set, it is up to the supplicant to allow or forbid it. The TLS options map to tls_disable_tlsv1_x settings. See the wpa_supplicant documentation for more details. </p>
<p> Format: uint32</dl>
<p> <code>phase1-fast-provisioning</code></p>
<dl>
<dd>Enables or disables in-line provisioning of EAP-FAST credentials when FAST is specified as the EAP method in the &quot;eap&quot; property. Recognized values are &quot;0&quot; (disabled), &quot;1&quot; (allow unauthenticated provisioning), &quot;2&quot; (allow authenticated provisioning), and &quot;3&quot; (allow both authenticated and unauthenticated provisioning). See the wpa_supplicant documentation for more details. </p>
<p> Format: string</dl>
<p> <code>phase1-peaplabel</code></p>
<dl>
<dd>Forces use of the new PEAP label during key derivation. Some RADIUS servers may require forcing the new PEAP label to interoperate with PEAPv1. Set to &quot;1&quot; to force use of the new PEAP label. See the wpa_supplicant documentation for more details. </p>
<p> Format: string</dl>
<p> <code>phase1-peapver</code></p>
<dl>
<dd>Forces which PEAP version is used when PEAP is set as the EAP method in the &quot;eap&quot; property. When unset, the version reported by the server will be used. Sometimes when using older RADIUS servers, it is necessary to force the client to use a particular PEAP version. To do so, this property may be set to &quot;0&quot; or &quot;1&quot; to force that specific PEAP version. </p>
<p> Format: string</dl>
<p> <code>phase2-altsubject-matches</code></p>
<dl>
<dd>List of strings to be matched against the altSubjectName of the certificate presented by the authentication server during the inner &quot;phase 2&quot; authentication. If the list is empty, no verification of the server certificate&#8217;s altSubjectName is performed. </p>
<p> Format: array of string</dl>
<p> <code>phase2-auth</code></p>
<dl>
<dd>Specifies the allowed &quot;phase 2&quot; inner authentication method when an EAP method that uses an inner TLS tunnel is specified in the &quot;eap&quot; property. For TTLS this property selects one of the supported non-EAP inner methods: &quot;pap&quot;, &quot;chap&quot;, &quot;mschap&quot;, &quot;mschapv2&quot; while &quot;phase2-autheap&quot; selects an EAP inner method. For PEAP this selects an inner EAP method, one of: &quot;gtc&quot;, &quot;otp&quot;, &quot;md5&quot; and &quot;tls&quot;. Each &quot;phase 2&quot; inner method requires specific parameters for successful authentication; see the wpa_supplicant documentation for more details. Both &quot;phase2-auth&quot; and &quot;phase2-autheap&quot; cannot be specified. </p>
<p> Format: string</dl>
<p> <code>phase2-autheap</code></p>
<dl>
<dd>Specifies the allowed &quot;phase 2&quot; inner EAP-based authentication method when TTLS is specified in the &quot;eap&quot; property. Recognized EAP-based &quot;phase 2&quot; methods are &quot;md5&quot;, &quot;mschapv2&quot;, &quot;otp&quot;, &quot;gtc&quot;, and &quot;tls&quot;. Each &quot;phase 2&quot; inner method requires specific parameters for successful authentication; see the wpa_supplicant documentation for more details. </p>
<p> Format: string</dl>
<p> <code>phase2-ca-cert</code></p>
<dl>
<dd>Contains the &quot;phase 2&quot; CA certificate if used by the EAP method specified in the &quot;phase2-auth&quot; or &quot;phase2-autheap&quot; properties. Certificate data is specified using a &quot;scheme&quot;; three are currently supported: blob, path and pkcs#11 URL. When using the blob scheme this property should be set to the certificate&#8217;s DER encoded data. When using the path scheme, this property should be set to the full UTF-8 encoded path of the certificate, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. This property can be unset even if the EAP method supports CA certificates, but this allows man-in-the-middle attacks and is NOT recommended. Note that enabling NMSetting8021x:system-ca-certs will override this setting to use the built-in path, if the built-in path is not a directory. </p>
<p> Format: byte array</dl>
<p> <code>phase2-ca-cert-password</code></p>
<dl>
<dd>The password used to access the &quot;phase2&quot; CA certificate stored in &quot;phase2-ca-cert&quot; property. Only makes sense if the certificate is stored on a PKCS#11 token that requires a login. </p>
<p> Format: string</dl>
<p> <code>phase2-ca-cert-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;phase2-ca-cert-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>phase2-ca-path</code></p>
<dl>
<dd>UTF-8 encoded path to a directory containing PEM or DER formatted certificates to be added to the verification chain in addition to the certificate specified in the &quot;phase2-ca-cert&quot; property. If NMSetting8021x:system-ca-certs is enabled and the built-in CA path is an existing directory, then this setting is ignored. </p>
<p> Format: string</dl>
<p> <code>phase2-client-cert</code></p>
<dl>
<dd>Contains the &quot;phase 2&quot; client certificate if used by the EAP method specified in the &quot;phase2-auth&quot; or &quot;phase2-autheap&quot; properties. Certificate data is specified using a &quot;scheme&quot;; two are currently supported: blob and path. When using the blob scheme (which is backwards compatible with NM 0.7.x) this property should be set to the certificate&#8217;s DER encoded data. When using the path scheme, this property should be set to the full UTF-8 encoded path of the certificate, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. This property can be unset even if the EAP method supports CA certificates, but this allows man-in-the-middle attacks and is NOT recommended. </p>
<p> Format: byte array</dl>
<p> <code>phase2-client-cert-password</code></p>
<dl>
<dd>The password used to access the &quot;phase2&quot; client certificate stored in &quot;phase2-client-cert&quot; property. Only makes sense if the certificate is stored on a PKCS#11 token that requires a login. </p>
<p> Format: string</dl>
<p> <code>phase2-client-cert-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;phase2-client-cert-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>phase2-domain-match</code></p>
<dl>
<dd>Constraint for server domain name. If set, this list of FQDNs is used as a match requirement for dNSName element(s) of the certificate presented by the authentication server during the inner &quot;phase 2&quot; authentication. If a matching dNSName is found, this constraint is met. If no dNSName values are present, this constraint is matched against SubjectName CN using the same comparison. Multiple valid FQDNs can be passed as a &quot;;&quot; delimited list. </p>
<p> Format: string</dl>
<p> <code>phase2-domain-suffix-match</code></p>
<dl>
<dd>Constraint for server domain name. If set, this FQDN is used as a suffix match requirement for dNSName element(s) of the certificate presented by the authentication server during the inner &quot;phase 2&quot; authentication. If a matching dNSName is found, this constraint is met. If no dNSName values are present, this constraint is matched against SubjectName CN using same suffix match comparison. Since version 1.24, multiple valid FQDNs can be passed as a &quot;;&quot; delimited list. </p>
<p> Format: string</dl>
<p> <code>phase2-private-key</code></p>
<dl>
<dd>Contains the &quot;phase 2&quot; inner private key when the &quot;phase2-auth&quot; or &quot;phase2-autheap&quot; property is set to &quot;tls&quot;. Key data is specified using a &quot;scheme&quot;; two are currently supported: blob and path. When using the blob scheme and private keys, this property should be set to the key&#8217;s encrypted PEM encoded data. When using private keys with the path scheme, this property should be set to the full UTF-8 encoded path of the key, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. When using PKCS#12 format private keys and the blob scheme, this property should be set to the PKCS#12 data and the &quot;phase2-private-key-password&quot; property must be set to password used to decrypt the PKCS#12 certificate and key. When using PKCS#12 files and the path scheme, this property should be set to the full UTF-8 encoded path of the key, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte, and as with the blob scheme the &quot;phase2-private-key-password&quot; property must be set to the password used to decode the PKCS#12 private key and certificate. </p>
<p> Format: byte array</dl>
<p> <code>phase2-private-key-password</code></p>
<dl>
<dd>The password used to decrypt the &quot;phase 2&quot; private key specified in the &quot;phase2-private-key&quot; property when the private key either uses the path scheme, or is a PKCS#12 format key. </p>
<p> Format: string</dl>
<p> <code>phase2-private-key-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;phase2-private-key-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>phase2-subject-match</code></p>
<dl>
<dd>Substring to be matched against the subject of the certificate presented by the authentication server during the inner &quot;phase 2&quot; authentication. When unset, no verification of the authentication server certificate&#8217;s subject is performed. This property provides little security, if any, and its use is deprecated in favor of NMSetting8021x:phase2-domain-suffix-match. </p>
<p> Format: string</dl>
<p> <code>pin</code></p>
<dl>
<dd>PIN used for EAP authentication methods. </p>
<p> Format: string</dl>
<p> <code>pin-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;pin&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>private-key</code></p>
<dl>
<dd>Contains the private key when the &quot;eap&quot; property is set to &quot;tls&quot;. Key data is specified using a &quot;scheme&quot;; two are currently supported: blob and path. When using the blob scheme and private keys, this property should be set to the key&#8217;s encrypted PEM encoded data. When using private keys with the path scheme, this property should be set to the full UTF-8 encoded path of the key, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte. When using PKCS#12 format private keys and the blob scheme, this property should be set to the PKCS#12 data and the &quot;private-key-password&quot; property must be set to password used to decrypt the PKCS#12 certificate and key. When using PKCS#12 files and the path scheme, this property should be set to the full UTF-8 encoded path of the key, prefixed with the string &quot;file://&quot; and ending with a terminating NUL byte, and as with the blob scheme the &quot;private-key-password&quot; property must be set to the password used to decode the PKCS#12 private key and certificate. WARNING: &quot;private-key&quot; is not a &quot;secret&quot; property, and thus unencrypted private key data using the BLOB scheme may be readable by unprivileged users. Private keys should always be encrypted with a private key password to prevent unauthorized access to unencrypted private key data. </p>
<p> Format: byte array</dl>
<p> <code>private-key-password</code></p>
<dl>
<dd>The password used to decrypt the private key specified in the &quot;private-key&quot; property when the private key either uses the path scheme, or if the private key is a PKCS#12 format key. </p>
<p> Format: string</dl>
<p> <code>private-key-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;private-key-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>subject-match</code></p>
<dl>
<dd>Substring to be matched against the subject of the certificate presented by the authentication server. When unset, no verification of the authentication server certificate&#8217;s subject is performed. This property provides little security, if any, and its use is deprecated in favor of NMSetting8021x:domain-suffix-match. </p>
<p> Format: string</dl>
<p> <code>system-ca-certs</code></p>
<dl>
<dd>When TRUE, overrides the &quot;ca-path&quot; and &quot;phase2-ca-path&quot; properties using the system CA directory specified at configure time with the &#8211;system-ca-path switch. The certificates in this directory are added to the verification chain in addition to any certificates specified by the &quot;ca-cert&quot; and &quot;phase2-ca-cert&quot; properties. If the path provided with &#8211;system-ca-path is rather a file name (bundle of trusted CA certificates), it overrides &quot;ca-cert&quot; and &quot;phase2-ca-cert&quot; properties instead (sets ca_cert/ca_cert2 options for wpa_supplicant). </p>
<p> Format: boolean</dl>
<h3>adsl setting</h3>
<p>ADSL Settings. </p>
<p> Properties: </p>
<p> <code>encapsulation</code></p>
<dl>
<dd>Alias: encapsulation </p>
<p> Encapsulation of ADSL connection. Can be &quot;vcmux&quot; or &quot;llc&quot;. </p>
<p> Format: string</dl>
<p> <code>password</code></p>
<dl>
<dd>Alias: password </p>
<p> Password used to authenticate with the ADSL service. </p>
<p> Format: string</dl>
<p> <code>password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>protocol</code></p>
<dl>
<dd>Alias: protocol </p>
<p> ADSL connection protocol. Can be &quot;pppoa&quot;, &quot;pppoe&quot; or &quot;ipoatm&quot;. </p>
<p> Format: string</dl>
<p> <code>username</code></p>
<dl>
<dd>Alias: username </p>
<p> Username used to authenticate with the ADSL service. </p>
<p> Format: string</dl>
<p> <code>vci</code></p>
<dl>
<dd>VCI of ADSL connection </p>
<p> Format: uint32</dl>
<p> <code>vpi</code></p>
<dl>
<dd>VPI of ADSL connection </p>
<p> Format: uint32</dl>
<h3>bluetooth setting</h3>
<p>Bluetooth Settings. </p>
<p> Properties: </p>
<p> <code>bdaddr</code></p>
<dl>
<dd>Alias: addr </p>
<p> The Bluetooth address of the device. </p>
<p> Format: byte array</dl>
<p> <code>type</code></p>
<dl>
<dd>Alias: bt-type </p>
<p> Either &quot;dun&quot; for Dial-Up Networking connections or &quot;panu&quot; for Personal Area Networking connections to devices supporting the NAP profile. </p>
<p> Format: string</dl>
<h3>bond setting</h3>
<p>Bonding Settings. </p>
<p> Properties: </p>
<p> <code>options</code></p>
<dl>
<dd>Dictionary of key/value pairs of bonding options. Both keys and values must be strings. Option names must contain only alphanumeric characters (ie, [a-zA-Z0-9]). </p>
<p> Format: dict of string to string</dl>
<h3>bridge setting</h3>
<p>Bridging Settings. </p>
<p> Properties: </p>
<p> <code>ageing-time</code></p>
<dl>
<dd>Alias: ageing-time </p>
<p> The Ethernet MAC address aging time, in seconds. </p>
<p> Format: uint32</dl>
<p> <code>forward-delay</code></p>
<dl>
<dd>Alias: forward-delay </p>
<p> The Spanning Tree Protocol (STP) forwarding delay, in seconds. </p>
<p> Format: uint32</dl>
<p> <code>group-address</code></p>
<dl>
<dd>If specified, The MAC address of the multicast group this bridge uses for STP. The address must be a link-local address in standard Ethernet MAC address format, ie an address of the form 01:80:C2:00:00:0X, with X in [0, 4..F]. If not specified the default value is 01:80:C2:00:00:00. </p>
<p> Format: byte array</dl>
<p> <code>group-forward-mask</code></p>
<dl>
<dd>Alias: group-forward-mask </p>
<p> A mask of group addresses to forward. Usually, group addresses in the range from 01:80:C2:00:00:00 to 01:80:C2:00:00:0F are not forwarded according to standards. This property is a mask of 16 bits, each corresponding to a group address in that range that must be forwarded. The mask can&#8217;t have bits 0, 1 or 2 set because they are used for STP, MAC pause frames and LACP. </p>
<p> Format: uint32</dl>
<p> <code>hello-time</code></p>
<dl>
<dd>Alias: hello-time </p>
<p> The Spanning Tree Protocol (STP) hello time, in seconds. </p>
<p> Format: uint32</dl>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, the MAC address of bridge. When creating a new bridge, this MAC address will be set. If this field is left unspecified, the &quot;ethernet.cloned-mac-address&quot; is referred instead to generate the initial MAC address. Note that setting &quot;ethernet.cloned-mac-address&quot; anyway overwrites the MAC address of the bridge later while activating the bridge. Hence, this property is deprecated. Deprecated: 1 </p>
<p> Format: byte array</dl>
<p> <code>max-age</code></p>
<dl>
<dd>Alias: max-age </p>
<p> The Spanning Tree Protocol (STP) maximum message age, in seconds. </p>
<p> Format: uint32</dl>
<p> <code>multicast-hash-max</code></p>
<dl>
<dd>Set maximum size of multicast hash table (value must be a power of 2). </p>
<p> Format: uint32</dl>
<p> <code>multicast-last-member-count</code></p>
<dl>
<dd>Set the number of queries the bridge will send before stopping forwarding a multicast group after a &quot;leave&quot; message has been received. </p>
<p> Format: uint32</dl>
<p> <code>multicast-last-member-interval</code></p>
<dl>
<dd>Set interval (in deciseconds) between queries to find remaining members of a group, after a &quot;leave&quot; message is received. </p>
<p> Format: uint64</dl>
<p> <code>multicast-membership-interval</code></p>
<dl>
<dd>Set delay (in deciseconds) after which the bridge will leave a group, if no membership reports for this group are received. </p>
<p> Format: uint64</dl>
<p> <code>multicast-querier</code></p>
<dl>
<dd>Enable or disable sending of multicast queries by the bridge. If not specified the option is disabled. </p>
<p> Format: boolean</dl>
<p> <code>multicast-querier-interval</code></p>
<dl>
<dd>If no queries are seen after this delay (in deciseconds) has passed, the bridge will start to send its own queries. </p>
<p> Format: uint64</dl>
<p> <code>multicast-query-interval</code></p>
<dl>
<dd>Interval (in deciseconds) between queries sent by the bridge after the end of the startup phase. </p>
<p> Format: uint64</dl>
<p> <code>multicast-query-response-interval</code></p>
<dl>
<dd>Set the Max Response Time/Max Response Delay (in deciseconds) for IGMP/MLD queries sent by the bridge. </p>
<p> Format: uint64</dl>
<p> <code>multicast-query-use-ifaddr</code></p>
<dl>
<dd>If enabled the bridge&#8217;s own IP address is used as the source address for IGMP queries otherwise the default of 0.0.0.0 is used. </p>
<p> Format: boolean</dl>
<p> <code>multicast-router</code></p>
<dl>
<dd>Sets bridge&#8217;s multicast router. Multicast-snooping must be enabled for this option to work. Supported values are: &#8216;auto&#8217;, &#8216;disabled&#8217;, &#8216;enabled&#8217; to which kernel assigns the numbers 1, 0, and 2, respectively. If not specified the default value is &#8216;auto&#8217; (1). </p>
<p> Format: string</dl>
<p> <code>multicast-snooping</code></p>
<dl>
<dd>Alias: multicast-snooping </p>
<p> Controls whether IGMP snooping is enabled for this bridge. Note that if snooping was automatically disabled due to hash collisions, the system may refuse to enable the feature until the collisions are resolved. </p>
<p> Format: boolean</dl>
<p> <code>multicast-startup-query-count</code></p>
<dl>
<dd>Set the number of IGMP queries to send during startup phase. </p>
<p> Format: uint32</dl>
<p> <code>multicast-startup-query-interval</code></p>
<dl>
<dd>Sets the time (in deciseconds) between queries sent out at startup to determine membership information. </p>
<p> Format: uint64</dl>
<p> <code>priority</code></p>
<dl>
<dd>Alias: priority </p>
<p> Sets the Spanning Tree Protocol (STP) priority for this bridge. Lower values are &quot;better&quot;; the lowest priority bridge will be elected the root bridge. </p>
<p> Format: uint32</dl>
<p> <code>stp</code></p>
<dl>
<dd>Alias: stp </p>
<p> Controls whether Spanning Tree Protocol (STP) is enabled for this bridge. </p>
<p> Format: boolean</dl>
<p> <code>vlan-default-pvid</code></p>
<dl>
<dd>The default PVID for the ports of the bridge, that is the VLAN id assigned to incoming untagged frames. </p>
<p> Format: uint32</dl>
<p> <code>vlan-filtering</code></p>
<dl>
<dd>Control whether VLAN filtering is enabled on the bridge. </p>
<p> Format: boolean</dl>
<p> <code>vlan-protocol</code></p>
<dl>
<dd>If specified, the protocol used for VLAN filtering. Supported values are: &#8216;802.1Q&#8217;, &#8216;802.1ad&#8217;. If not specified the default value is &#8216;802.1Q&#8217;. </p>
<p> Format: string</dl>
<p> <code>vlan-stats-enabled</code></p>
<dl>
<dd>Controls whether per-VLAN stats accounting is enabled. </p>
<p> Format: boolean</dl>
<p> <code>vlans</code></p>
<dl>
<dd>Array of bridge VLAN objects. In addition to the VLANs specified here, the bridge will also have the default-pvid VLAN configured by the bridge.vlan-default-pvid property. In nmcli the VLAN list can be specified with the following syntax: $vid [pvid] [untagged] [, $vid [pvid] [untagged]]&#8230; where $vid is either a single id between 1 and 4094 or a range, represented as a couple of ids separated by a dash. </p>
<p> Format: array of vardict</dl>
<h3>bridge-port setting</h3>
<p>Bridge Port Settings. </p>
<p> Properties: </p>
<p> <code>hairpin-mode</code></p>
<dl>
<dd>Alias: hairpin </p>
<p> Enables or disables &quot;hairpin mode&quot; for the port, which allows frames to be sent back out through the port the frame was received on. </p>
<p> Format: boolean</dl>
<p> <code>path-cost</code></p>
<dl>
<dd>Alias: path-cost </p>
<p> The Spanning Tree Protocol (STP) port cost for destinations via this port. </p>
<p> Format: uint32</dl>
<p> <code>priority</code></p>
<dl>
<dd>Alias: priority </p>
<p> The Spanning Tree Protocol (STP) priority of this bridge port. </p>
<p> Format: uint32</dl>
<p> <code>vlans</code></p>
<dl>
<dd>Array of bridge VLAN objects. In addition to the VLANs specified here, the port will also have the default-pvid VLAN configured on the bridge by the bridge.vlan-default-pvid property. In nmcli the VLAN list can be specified with the following syntax: $vid [pvid] [untagged] [, $vid [pvid] [untagged]]&#8230; where $vid is either a single id between 1 and 4094 or a range, represented as a couple of ids separated by a dash. </p>
<p> Format: array of vardict</dl>
<h3>cdma setting</h3>
<p>CDMA-based Mobile Broadband Settings. </p>
<p> Properties: </p>
<p> <code>mtu</code></p>
<dl>
<dd>If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple frames. </p>
<p> Format: uint32</dl>
<p> <code>number</code></p>
<dl>
<dd>The number to dial to establish the connection to the CDMA-based mobile broadband network, if any. If not specified, the default number (#777) is used when required. </p>
<p> Format: string</dl>
<p> <code>password</code></p>
<dl>
<dd>Alias: password </p>
<p> The password used to authenticate with the network, if required. Many providers do not require a password, or accept any password. But if a password is required, it is specified here. </p>
<p> Format: string</dl>
<p> <code>password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>username</code></p>
<dl>
<dd>Alias: user </p>
<p> The username used to authenticate with the network, if required. Many providers do not require a username, or accept any username. But if a username is required, it is specified here. </p>
<p> Format: string</dl>
<h3>dcb setting</h3>
<p>Data Center Bridging Settings. </p>
<p> Properties: </p>
<p> <code>app-fcoe-flags</code></p>
<dl>
<dd>Specifies the NMSettingDcbFlags for the DCB FCoE application. Flags may be any combination of NM_SETTING_DCB_FLAG_ENABLE (0x1), NM_SETTING_DCB_FLAG_ADVERTISE (0x2), and NM_SETTING_DCB_FLAG_WILLING (0x4). </p>
<p> Format: NMSettingDcbFlags (uint32)</dl>
<p> <code>app-fcoe-mode</code></p>
<dl>
<dd>The FCoE controller mode; either &quot;fabric&quot; or &quot;vn2vn&quot;. Since 1.34, NULL is the default and means &quot;fabric&quot;. Before 1.34, NULL was rejected as invalid and the default was &quot;fabric&quot;. </p>
<p> Format: string</dl>
<p> <code>app-fcoe-priority</code></p>
<dl>
<dd>The highest User Priority (0 &#8211; 7) which FCoE frames should use, or -1 for default priority. Only used when the &quot;app-fcoe-flags&quot; property includes the NM_SETTING_DCB_FLAG_ENABLE (0x1) flag. </p>
<p> Format: int32</dl>
<p> <code>app-fip-flags</code></p>
<dl>
<dd>Specifies the NMSettingDcbFlags for the DCB FIP application. Flags may be any combination of NM_SETTING_DCB_FLAG_ENABLE (0x1), NM_SETTING_DCB_FLAG_ADVERTISE (0x2), and NM_SETTING_DCB_FLAG_WILLING (0x4). </p>
<p> Format: NMSettingDcbFlags (uint32)</dl>
<p> <code>app-fip-priority</code></p>
<dl>
<dd>The highest User Priority (0 &#8211; 7) which FIP frames should use, or -1 for default priority. Only used when the &quot;app-fip-flags&quot; property includes the NM_SETTING_DCB_FLAG_ENABLE (0x1) flag. </p>
<p> Format: int32</dl>
<p> <code>app-iscsi-flags</code></p>
<dl>
<dd>Specifies the NMSettingDcbFlags for the DCB iSCSI application. Flags may be any combination of NM_SETTING_DCB_FLAG_ENABLE (0x1), NM_SETTING_DCB_FLAG_ADVERTISE (0x2), and NM_SETTING_DCB_FLAG_WILLING (0x4). </p>
<p> Format: NMSettingDcbFlags (uint32)</dl>
<p> <code>app-iscsi-priority</code></p>
<dl>
<dd>The highest User Priority (0 &#8211; 7) which iSCSI frames should use, or -1 for default priority. Only used when the &quot;app-iscsi-flags&quot; property includes the NM_SETTING_DCB_FLAG_ENABLE (0x1) flag. </p>
<p> Format: int32</dl>
<p> <code>priority-bandwidth</code></p>
<dl>
<dd>An array of 8 uint values, where the array index corresponds to the User Priority (0 &#8211; 7) and the value indicates the percentage of bandwidth of the priority&#8217;s assigned group that the priority may use. The sum of all percentages for priorities which belong to the same group must total 100 percents. </p>
<p> Format: array of uint32</dl>
<p> <code>priority-flow-control</code></p>
<dl>
<dd>An array of 8 boolean values, where the array index corresponds to the User Priority (0 &#8211; 7) and the value indicates whether or not the corresponding priority should transmit priority pause. </p>
<p> Format: array of uint32</dl>
<p> <code>priority-flow-control-flags</code></p>
<dl>
<dd>Specifies the NMSettingDcbFlags for DCB Priority Flow Control (PFC). Flags may be any combination of NM_SETTING_DCB_FLAG_ENABLE (0x1), NM_SETTING_DCB_FLAG_ADVERTISE (0x2), and NM_SETTING_DCB_FLAG_WILLING (0x4). </p>
<p> Format: NMSettingDcbFlags (uint32)</dl>
<p> <code>priority-group-bandwidth</code></p>
<dl>
<dd>An array of 8 uint values, where the array index corresponds to the Priority Group ID (0 &#8211; 7) and the value indicates the percentage of link bandwidth allocated to that group. Allowed values are 0 &#8211; 100, and the sum of all values must total 100 percents. </p>
<p> Format: array of uint32</dl>
<p> <code>priority-group-flags</code></p>
<dl>
<dd>Specifies the NMSettingDcbFlags for DCB Priority Groups. Flags may be any combination of NM_SETTING_DCB_FLAG_ENABLE (0x1), NM_SETTING_DCB_FLAG_ADVERTISE (0x2), and NM_SETTING_DCB_FLAG_WILLING (0x4). </p>
<p> Format: NMSettingDcbFlags (uint32)</dl>
<p> <code>priority-group-id</code></p>
<dl>
<dd>An array of 8 uint values, where the array index corresponds to the User Priority (0 &#8211; 7) and the value indicates the Priority Group ID. Allowed Priority Group ID values are 0 &#8211; 7 or 15 for the unrestricted group. </p>
<p> Format: array of uint32</dl>
<p> <code>priority-strict-bandwidth</code></p>
<dl>
<dd>An array of 8 boolean values, where the array index corresponds to the User Priority (0 &#8211; 7) and the value indicates whether or not the priority may use all of the bandwidth allocated to its assigned group. </p>
<p> Format: array of uint32</dl>
<p> <code>priority-traffic-class</code></p>
<dl>
<dd>An array of 8 uint values, where the array index corresponds to the User Priority (0 &#8211; 7) and the value indicates the traffic class (0 &#8211; 7) to which the priority is mapped. </p>
<p> Format: array of uint32</dl>
<h3>ethtool setting</h3>
<p>Ethtool Ethernet Settings. </p>
<p> Properties: </p>
<p> <code>coalesce-adaptive-rx</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-adaptive-tx</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-pkt-rate-high</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-pkt-rate-low</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-frames</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-frames-high</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-frames-irq</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-frames-low</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-usecs</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-usecs-high</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-usecs-irq</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-rx-usecs-low</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-sample-interval</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-stats-block-usecs</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-frames</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-frames-high</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-frames-irq</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-frames-low</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-usecs</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-usecs-high</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-usecs-irq</code></p>
<dl>
<dd></dl>
<p> <code>coalesce-tx-usecs-low</code></p>
<dl>
<dd></dl>
<p> <code>feature-esp-hw-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-esp-tx-csum-hw-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-fcoe-mtu</code></p>
<dl>
<dd></dl>
<p> <code>feature-gro</code></p>
<dl>
<dd></dl>
<p> <code>feature-gso</code></p>
<dl>
<dd></dl>
<p> <code>feature-highdma</code></p>
<dl>
<dd></dl>
<p> <code>feature-hw-tc-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-l2-fwd-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-loopback</code></p>
<dl>
<dd></dl>
<p> <code>feature-lro</code></p>
<dl>
<dd></dl>
<p> <code>feature-macsec-hw-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-ntuple</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-all</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-fcs</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-gro-hw</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-gro-list</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-udp-gro-forwarding</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-udp_tunnel-port-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-vlan-filter</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-vlan-stag-filter</code></p>
<dl>
<dd></dl>
<p> <code>feature-rx-vlan-stag-hw-parse</code></p>
<dl>
<dd></dl>
<p> <code>feature-rxhash</code></p>
<dl>
<dd></dl>
<p> <code>feature-rxvlan</code></p>
<dl>
<dd></dl>
<p> <code>feature-sg</code></p>
<dl>
<dd></dl>
<p> <code>feature-tls-hw-record</code></p>
<dl>
<dd></dl>
<p> <code>feature-tls-hw-rx-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-tls-hw-tx-offload</code></p>
<dl>
<dd></dl>
<p> <code>feature-tso</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-checksum-fcoe-crc</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-checksum-ip-generic</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-checksum-ipv4</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-checksum-ipv6</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-checksum-sctp</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-esp-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-fcoe-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-gre-csum-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-gre-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-gso-list</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-gso-partial</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-gso-robust</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-ipxip4-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-ipxip6-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-nocache-copy</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-scatter-gather</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-scatter-gather-fraglist</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-sctp-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-tcp-ecn-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-tcp-mangleid-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-tcp-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-tcp6-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-tunnel-remcsum-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-udp-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-udp_tnl-csum-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-udp_tnl-segmentation</code></p>
<dl>
<dd></dl>
<p> <code>feature-tx-vlan-stag-hw-insert</code></p>
<dl>
<dd></dl>
<p> <code>feature-txvlan</code></p>
<dl>
<dd></dl>
<p> <code>pause-autoneg</code></p>
<dl>
<dd>Whether to automatically negotiate on pause frame of flow control mechanism defined by IEEE 802.3x standard.</dl>
<p> <code>pause-rx</code></p>
<dl>
<dd>Whether RX pause should be enabled. Only valid when automatic negotiation is disabled</dl>
<p> <code>pause-tx</code></p>
<dl>
<dd>Whether TX pause should be enabled. Only valid when automatic negotiation is disabled</dl>
<p> <code>ring-rx</code></p>
<dl>
<dd></dl>
<p> <code>ring-rx-jumbo</code></p>
<dl>
<dd></dl>
<p> <code>ring-rx-mini</code></p>
<dl>
<dd></dl>
<p> <code>ring-tx</code></p>
<dl>
<dd></dl>
<h3>gsm setting</h3>
<p>GSM-based Mobile Broadband Settings. </p>
<p> Properties: </p>
<p> <code>apn</code></p>
<dl>
<dd>Alias: apn </p>
<p> The GPRS Access Point Name specifying the APN used when establishing a data session with the GSM-based network. The APN often determines how the user will be billed for their network usage and whether the user has access to the Internet or just a provider-specific walled-garden, so it is important to use the correct APN for the user&#8217;s mobile broadband plan. The APN may only be composed of the characters a-z, 0-9, ., and &#8211; per GSM 03.60 Section 14.9. </p>
<p> Format: string</dl>
<p> <code>auto-config</code></p>
<dl>
<dd>When TRUE, the settings such as APN, username, or password will default to values that match the network the modem will register to in the Mobile Broadband Provider database. </p>
<p> Format: boolean</dl>
<p> <code>device-id</code></p>
<dl>
<dd>The device unique identifier (as given by the WWAN management service) which this connection applies to. If given, the connection will only apply to the specified device. </p>
<p> Format: string</dl>
<p> <code>home-only</code></p>
<dl>
<dd>When TRUE, only connections to the home network will be allowed. Connections to roaming networks will not be made. </p>
<p> Format: boolean</dl>
<p> <code>mtu</code></p>
<dl>
<dd>If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple frames. </p>
<p> Format: uint32</dl>
<p> <code>network-id</code></p>
<dl>
<dd>The Network ID (GSM LAI format, ie MCC-MNC) to force specific network registration. If the Network ID is specified, NetworkManager will attempt to force the device to register only on the specified network. This can be used to ensure that the device does not roam when direct roaming control of the device is not otherwise possible. </p>
<p> Format: string</dl>
<p> <code>number</code></p>
<dl>
<dd>Legacy setting that used to help establishing PPP data sessions for GSM-based modems. Deprecated: 1 </p>
<p> Format: string</dl>
<p> <code>password</code></p>
<dl>
<dd>Alias: password </p>
<p> The password used to authenticate with the network, if required. Many providers do not require a password, or accept any password. But if a password is required, it is specified here. </p>
<p> Format: string</dl>
<p> <code>password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>pin</code></p>
<dl>
<dd>If the SIM is locked with a PIN it must be unlocked before any other operations are requested. Specify the PIN here to allow operation of the device. </p>
<p> Format: string</dl>
<p> <code>pin-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;pin&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>sim-id</code></p>
<dl>
<dd>The SIM card unique identifier (as given by the WWAN management service) which this connection applies to. If given, the connection will apply to any device also allowed by &quot;device-id&quot; which contains a SIM card matching the given identifier. </p>
<p> Format: string</dl>
<p> <code>sim-operator-id</code></p>
<dl>
<dd>A MCC/MNC string like &quot;310260&quot; or &quot;21601&quot; identifying the specific mobile network operator which this connection applies to. If given, the connection will apply to any device also allowed by &quot;device-id&quot; and &quot;sim-id&quot; which contains a SIM card provisioned by the given operator. </p>
<p> Format: string</dl>
<p> <code>username</code></p>
<dl>
<dd>Alias: user </p>
<p> The username used to authenticate with the network, if required. Many providers do not require a username, or accept any username. But if a username is required, it is specified here. </p>
<p> Format: string</dl>
<h3>infiniband setting</h3>
<p>Infiniband Settings. </p>
<p> Properties: </p>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, this connection will only apply to the IPoIB device whose permanent MAC address matches. This property does not change the MAC address of the device (i.e. MAC spoofing). </p>
<p> Format: byte array</dl>
<p> <code>mtu</code></p>
<dl>
<dd>Alias: mtu </p>
<p> If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple frames. </p>
<p> Format: uint32</dl>
<p> <code>p-key</code></p>
<dl>
<dd>Alias: p-key </p>
<p> The InfiniBand P_Key to use for this device. A value of -1 means to use the default P_Key (aka &quot;the P_Key at index 0&quot;). Otherwise, it is a 16-bit unsigned integer, whose high bit is set if it is a &quot;full membership&quot; P_Key. </p>
<p> Format: int32</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: parent </p>
<p> The interface name of the parent device of this device. Normally NULL, but if the &quot;p_key&quot; property is set, then you must specify the base device by setting either this property or &quot;mac-address&quot;. </p>
<p> Format: string</dl>
<p> <code>transport-mode</code></p>
<dl>
<dd>Alias: transport-mode </p>
<p> The IP-over-InfiniBand transport mode. Either &quot;datagram&quot; or &quot;connected&quot;. </p>
<p> Format: string</dl>
<h3>ipv4 setting</h3>
<p>IPv4 Settings. </p>
<p> Properties: </p>
<p> <code>addresses</code></p>
<dl>
<dd>Alias: ip4 </p>
<p> A list of IPv4 addresses and their prefix length. Multiple addresses can be separated by comma. For example &quot;192.168.1.5/24, 10.1.0.5/24&quot;. The addresses are listed in decreasing priority, meaning the first address will be the primary address. </p>
<p> Format: a comma separated list of addresses</dl>
<p> <code>dad-timeout</code></p>
<dl>
<dd>Timeout in milliseconds used to check for the presence of duplicate IP addresses on the network. If an address conflict is detected, the activation will fail. A zero value means that no duplicate address detection is performed, -1 means the default value (either configuration ipvx.dad-timeout override or zero). A value greater than zero is a timeout in milliseconds. The property is currently implemented only for IPv4. </p>
<p> Format: int32</dl>
<p> <code>dhcp-client-id</code></p>
<dl>
<dd>A string sent to the DHCP server to identify the local machine which the DHCP server may use to customize the DHCP lease and options. When the property is a hex string (&#8216;aa:bb:cc&#8217;) it is interpreted as a binary client ID, in which case the first byte is assumed to be the &#8216;type&#8217; field as per RFC 2132 section 9.14 and the remaining bytes may be an hardware address (e.g. &#8217;01:xx:xx:xx:xx:xx:xx&#8217; where 1 is the Ethernet ARP type and the rest is a MAC address). If the property is not a hex string it is considered as a non-hardware-address client ID and the &#8216;type&#8217; field is set to 0. The special values &quot;mac&quot; and &quot;perm-mac&quot; are supported, which use the current or permanent MAC address of the device to generate a client identifier with type ethernet (01). Currently, these options only work for ethernet type of links. The special value &quot;ipv6-duid&quot; uses the DUID from &quot;ipv6.dhcp-duid&quot; property as an RFC4361-compliant client identifier. As IAID it uses &quot;ipv4.dhcp-iaid&quot; and falls back to &quot;ipv6.dhcp-iaid&quot; if unset. The special value &quot;duid&quot; generates a RFC4361-compliant client identifier based on &quot;ipv4.dhcp-iaid&quot; and uses a DUID generated by hashing /etc/machine-id. The special value &quot;stable&quot; is supported to generate a type 0 client identifier based on the stable-id (see connection.stable-id) and a per-host key. If you set the stable-id, you may want to include the &quot;${DEVICE}&quot; or &quot;${MAC}&quot; specifier to get a per-device key. If unset, a globally configured default is used. If still unset, the default depends on the DHCP plugin. </p>
<p> Format: string</dl>
<p> <code>dhcp-fqdn</code></p>
<dl>
<dd>If the &quot;dhcp-send-hostname&quot; property is TRUE, then the specified FQDN will be sent to the DHCP server when acquiring a lease. This property and &quot;dhcp-hostname&quot; are mutually exclusive and cannot be set at the same time. </p>
<p> Format: string</dl>
<p> <code>dhcp-hostname</code></p>
<dl>
<dd>If the &quot;dhcp-send-hostname&quot; property is TRUE, then the specified name will be sent to the DHCP server when acquiring a lease. This property and &quot;dhcp-fqdn&quot; are mutually exclusive and cannot be set at the same time. </p>
<p> Format: string</dl>
<p> <code>dhcp-hostname-flags</code></p>
<dl>
<dd>Flags for the DHCP hostname and FQDN. Currently, this property only includes flags to control the FQDN flags set in the DHCP FQDN option. Supported FQDN flags are NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1), NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) and NM_DHCP_HOSTNAME_FLAG_FQDN_NO_UPDATE (0x4). When no FQDN flag is set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is set, the DHCP FQDN option will contain no flag. Otherwise, if no FQDN flag is set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is not set, the standard FQDN flags are set in the request: NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1), NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) for IPv4 and NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1) for IPv6. When this property is set to the default value NM_DHCP_HOSTNAME_FLAG_NONE (0x0), a global default is looked up in NetworkManager configuration. If that value is unset or also NM_DHCP_HOSTNAME_FLAG_NONE (0x0), then the standard FQDN flags described above are sent in the DHCP requests. </p>
<p> Format: uint32</dl>
<p> <code>dhcp-iaid</code></p>
<dl>
<dd>A string containing the &quot;Identity Association Identifier&quot; (IAID) used by the DHCP client. The property is a 32-bit decimal value or a special value among &quot;mac&quot;, &quot;perm-mac&quot;, &quot;ifname&quot; and &quot;stable&quot;. When set to &quot;mac&quot; (or &quot;perm-mac&quot;), the last 4 bytes of the current (or permanent) MAC address are used as IAID. When set to &quot;ifname&quot;, the IAID is computed by hashing the interface name. The special value &quot;stable&quot; can be used to generate an IAID based on the stable-id (see connection.stable-id), a per-host key and the interface name. When the property is unset, the value from global configuration is used; if no global default is set then the IAID is assumed to be &quot;ifname&quot;. Note that at the moment this property is ignored for IPv6 by dhclient, which always derives the IAID from the MAC address. </p>
<p> Format: string</dl>
<p> <code>dhcp-reject-servers</code></p>
<dl>
<dd>Array of servers from which DHCP offers must be rejected. This property is useful to avoid getting a lease from misconfigured or rogue servers. For DHCPv4, each element must be an IPv4 address, optionally followed by a slash and a prefix length (e.g. &quot;192.168.122.0/24&quot;). This property is currently not implemented for DHCPv6. </p>
<p> Format: array of string</dl>
<p> <code>dhcp-send-hostname</code></p>
<dl>
<dd>If TRUE, a hostname is sent to the DHCP server when acquiring a lease. Some DHCP servers use this hostname to update DNS databases, essentially providing a static hostname for the computer. If the &quot;dhcp-hostname&quot; property is NULL and this property is TRUE, the current persistent hostname of the computer is sent. </p>
<p> Format: boolean</dl>
<p> <code>dhcp-timeout</code></p>
<dl>
<dd>A timeout for a DHCP transaction in seconds. If zero (the default), a globally configured default is used. If still unspecified, a device specific timeout is used (usually 45 seconds). Set to 2147483647 (MAXINT32) for infinity. </p>
<p> Format: int32</dl>
<p> <code>dhcp-vendor-class-identifier</code></p>
<dl>
<dd>The Vendor Class Identifier DHCP option (60). Special characters in the data string may be escaped using C-style escapes, nevertheless this property cannot contain nul bytes. If the per-profile value is unspecified (the default), a global connection default gets consulted. If still unspecified, the DHCP option is not sent to the server. Since 1.28 </p>
<p> Format: string</dl>
<p> <code>dns</code></p>
<dl>
<dd>Array of IP addresses of DNS servers. </p>
<p> Format: array of uint32</dl>
<p> <code>dns-options</code></p>
<dl>
<dd>Array of DNS options as described in man 5 resolv.conf. NULL means that the options are unset and left at the default. In this case NetworkManager will use default options. This is distinct from an empty list of properties. The currently supported options are &quot;attempts&quot;, &quot;debug&quot;, &quot;edns0&quot;, &quot;inet6&quot;, &quot;ip6-bytestring&quot;, &quot;ip6-dotint&quot;, &quot;ndots&quot;, &quot;no-check-names&quot;, &quot;no-ip6-dotint&quot;, &quot;no-reload&quot;, &quot;no-tld-query&quot;, &quot;rotate&quot;, &quot;single-request&quot;, &quot;single-request-reopen&quot;, &quot;timeout&quot;, &quot;trust-ad&quot;, &quot;use-vc&quot;. The &quot;trust-ad&quot; setting is only honored if the profile contributes name servers to resolv.conf, and if all contributing profiles have &quot;trust-ad&quot; enabled. When using a caching DNS plugin (dnsmasq or systemd-resolved in NetworkManager.conf) then &quot;edns0&quot; and &quot;trust-ad&quot; are automatically added. </p>
<p> Format: array of string</dl>
<p> <code>dns-priority</code></p>
<dl>
<dd>DNS servers priority. The relative priority for DNS servers specified by this setting. A lower numerical value is better (higher priority). Negative values have the special effect of excluding other configurations with a greater numerical priority value; so in presence of at least one negative priority, only DNS servers from connections with the lowest priority value will be used. To avoid all DNS leaks, set the priority of the profile that should be used to the most negative value of all active connections profiles. Zero selects a globally configured default value. If the latter is missing or zero too, it defaults to 50 for VPNs (including WireGuard) and 100 for other connections. Note that the priority is to order DNS settings for multiple active connections. It does not disambiguate multiple DNS servers within the same connection profile. When multiple devices have configurations with the same priority, VPNs will be considered first, then devices with the best (lowest metric) default route and then all other devices. When using dns=default, servers with higher priority will be on top of resolv.conf. To prioritize a given server over another one within the same connection, just specify them in the desired order. Note that commonly the resolver tries name servers in /etc/resolv.conf in the order listed, proceeding with the next server in the list on failure. See for example the &quot;rotate&quot; option of the dns-options setting. If there are any negative DNS priorities, then only name servers from the devices with that lowest priority will be considered. When using a DNS resolver that supports Conditional Forwarding or Split DNS (with dns=dnsmasq or dns=systemd-resolved settings), each connection is used to query domains in its search list. The search domains determine which name servers to ask, and the DNS priority is used to prioritize name servers based on the domain. Queries for domains not present in any search list are routed through connections having the &#8216;~.&#8217; special wildcard domain, which is added automatically to connections with the default route (or can be added manually). When multiple connections specify the same domain, the one with the best priority (lowest numerical value) wins. If a sub domain is configured on another interface it will be accepted regardless the priority, unless parent domain on the other interface has a negative priority, which causes the sub domain to be shadowed. With Split DNS one can avoid undesired DNS leaks by properly configuring DNS priorities and the search domains, so that only name servers of the desired interface are configured. </p>
<p> Format: int32</dl>
<p> <code>dns-search</code></p>
<dl>
<dd>Array of DNS search domains. Domains starting with a tilde (&#8216;~&#8217;) are considered &#8216;routing&#8217; domains and are used only to decide the interface over which a query must be forwarded; they are not used to complete unqualified host names. When using a DNS plugin that supports Conditional Forwarding or Split DNS, then the search domains specify which name servers to query. This makes the behavior different from running with plain /etc/resolv.conf. For more information see also the dns-priority setting. </p>
<p> Format: array of string</dl>
<p> <code>gateway</code></p>
<dl>
<dd>Alias: gw4 </p>
<p> The gateway associated with this configuration. This is only meaningful if &quot;addresses&quot; is also set. The gateway&#8217;s main purpose is to control the next hop of the standard default route on the device. Hence, the gateway property conflicts with &quot;never-default&quot; and will be automatically dropped if the IP configuration is set to never-default. As an alternative to set the gateway, configure a static default route with /0 as prefix length. </p>
<p> Format: string</dl>
<p> <code>ignore-auto-dns</code></p>
<dl>
<dd>When &quot;method&quot; is set to &quot;auto&quot; and this property to TRUE, automatically configured name servers and search domains are ignored and only name servers and search domains specified in the &quot;dns&quot; and &quot;dns-search&quot; properties, if any, are used. </p>
<p> Format: boolean</dl>
<p> <code>ignore-auto-routes</code></p>
<dl>
<dd>When &quot;method&quot; is set to &quot;auto&quot; and this property to TRUE, automatically configured routes are ignored and only routes specified in the &quot;routes&quot; property, if any, are used. </p>
<p> Format: boolean</dl>
<p> <code>may-fail</code></p>
<dl>
<dd>If TRUE, allow overall network configuration to proceed even if the configuration specified by this property times out. Note that at least one IP configuration must succeed or overall network configuration will still fail. For example, in IPv6-only networks, setting this property to TRUE on the NMSettingIP4Config allows the overall network configuration to succeed if IPv4 configuration fails but IPv6 configuration completes successfully. </p>
<p> Format: boolean</dl>
<p> <code>method</code></p>
<dl>
<dd>IP configuration method. NMSettingIP4Config and NMSettingIP6Config both support &quot;disabled&quot;, &quot;auto&quot;, &quot;manual&quot;, and &quot;link-local&quot;. See the subclass-specific documentation for other values. In general, for the &quot;auto&quot; method, properties such as &quot;dns&quot; and &quot;routes&quot; specify information that is added on to the information returned from automatic configuration. The &quot;ignore-auto-routes&quot; and &quot;ignore-auto-dns&quot; properties modify this behavior. For methods that imply no upstream network, such as &quot;shared&quot; or &quot;link-local&quot;, these properties must be empty. For IPv4 method &quot;shared&quot;, the IP subnet can be configured by adding one manual IPv4 address or otherwise 10.42.x.0/24 is chosen. Note that the shared method must be configured on the interface which shares the internet to a subnet, not on the uplink which is shared. </p>
<p> Format: string</dl>
<p> <code>never-default</code></p>
<dl>
<dd>If TRUE, this connection will never be the default connection for this IP type, meaning it will never be assigned the default route by NetworkManager. </p>
<p> Format: boolean</dl>
<p> <code>required-timeout</code></p>
<dl>
<dd>The minimum time interval in milliseconds for which dynamic IP configuration should be tried before the connection succeeds. This property is useful for example if both IPv4 and IPv6 are enabled and are allowed to fail. Normally the connection succeeds as soon as one of the two address families completes; by setting a required timeout for e.g. IPv4, one can ensure that even if IP6 succeeds earlier than IPv4, NetworkManager waits some time for IPv4 before the connection becomes active. Note that if &quot;may-fail&quot; is FALSE for the same address family, this property has no effect as NetworkManager needs to wait for the full DHCP timeout. A zero value means that no required timeout is present, -1 means the default value (either configuration ipvx.required-timeout override or zero). </p>
<p> Format: int32</dl>
<p> <code>route-metric</code></p>
<dl>
<dd>The default metric for routes that don&#8217;t explicitly specify a metric. The default value -1 means that the metric is chosen automatically based on the device type. The metric applies to dynamic routes, manual (static) routes that don&#8217;t have an explicit metric setting, address prefix routes, and the default route. Note that for IPv6, the kernel accepts zero (0) but coerces it to 1024 (user default). Hence, setting this property to zero effectively mean setting it to 1024. For IPv4, zero is a regular value for the metric. </p>
<p> Format: int64</dl>
<p> <code>route-table</code></p>
<dl>
<dd>Enable policy routing (source routing) and set the routing table used when adding routes. This affects all routes, including device-routes, IPv4LL, DHCP, SLAAC, default-routes and static routes. But note that static routes can individually overwrite the setting by explicitly specifying a non-zero routing table. If the table setting is left at zero, it is eligible to be overwritten via global configuration. If the property is zero even after applying the global configuration value, policy routing is disabled for the address family of this connection. Policy routing disabled means that NetworkManager will add all routes to the main table (except static routes that explicitly configure a different table). Additionally, NetworkManager will not delete any extraneous routes from tables except the main table. This is to preserve backward compatibility for users who manage routing tables outside of NetworkManager. </p>
<p> Format: uint32</dl>
<p> <code>routes</code></p>
<dl>
<dd>A list of IPv4 destination addresses, prefix length, optional IPv4 next hop addresses, optional route metric, optional attribute. The valid syntax is: &quot;ip[/prefix] [next-hop] [metric] [attribute=val]&#8230;[,ip[/prefix]&#8230;]&quot;. For example &quot;192.0.2.0/24 10.1.1.1 77, 198.51.100.0/24&quot;. </p>
<p> Various attributes are supported: </p>
<dl>
<dd>&bull; &quot;cwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;initcwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;initrwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;lock-cwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-initcwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-initrwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-mtu&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-window&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;mtu&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;onlink&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;scope&quot; &#8211; an unsigned 8 bit integer. IPv4 only.</dl>
<dl>
<dd>&bull; &quot;src&quot; &#8211; an IPv4 address.</dl>
<dl>
<dd>&bull; &quot;table&quot; &#8211; an unsigned 32 bit integer. The default depends on ipv4.route-table.</dl>
<dl>
<dd>&bull; &quot;tos&quot; &#8211; an unsigned 8 bit integer. IPv4 only.</dl>
<dl>
<dd>&bull; &quot;type&quot; &#8211; one of unicast, local, blackhole, unavailable, prohibit. The default is unicast.</dl>
<dl>
<dd>&bull; &quot;window&quot; &#8211; an unsigned 32 bit integer.</dl>
<p> For details see also `man ip-route`. </p>
<p> Format: a comma separated list of routes</dl>
<p> <code>routing-rules</code></p>
<dl>
<dd>A comma separated list of routing rules for policy routing. The format is based on <code>ip rule add</code> syntax and mostly compatible. One difference is that routing rules in NetworkManager always need a fixed priority. </p>
<p> Example: priority 5 from 192.167.4.0/24 table 45 </p>
<p> Format: a comma separated list of routing rules</dl>
<h3>ipv6 setting</h3>
<p>IPv6 Settings. </p>
<p> Properties: </p>
<p> <code>addr-gen-mode</code></p>
<dl>
<dd>Configure method for creating the address for use with RFC4862 IPv6 Stateless Address Autoconfiguration. The permitted values are: NM_SETTING_IP6_CONFIG_ADDR_GEN_MODE_EUI64 (0) or NM_SETTING_IP6_CONFIG_ADDR_GEN_MODE_STABLE_PRIVACY (1). If the property is set to EUI64, the addresses will be generated using the interface tokens derived from hardware address. This makes the host part of the address to stay constant, making it possible to track host&#8217;s presence when it changes networks. The address changes when the interface hardware is replaced. The value of stable-privacy enables use of cryptographically secure hash of a secret host-specific key along with the connection&#8217;s stable-id and the network address as specified by RFC7217. This makes it impossible to use the address track host&#8217;s presence, and makes the address stable when the network interface hardware is replaced. On D-Bus, the absence of an addr-gen-mode setting equals enabling stable-privacy. For keyfile plugin, the absence of the setting on disk means EUI64 so that the property doesn&#8217;t change on upgrade from older versions. Note that this setting is distinct from the Privacy Extensions as configured by &quot;ip6-privacy&quot; property and it does not affect the temporary addresses configured with this option. </p>
<p> Format: int32</dl>
<p> <code>addresses</code></p>
<dl>
<dd>Alias: ip6 </p>
<p> A list of IPv6 addresses and their prefix length. Multiple addresses can be separated by comma. For example &quot;2001:db8:85a3::8a2e:370:7334/64, 2001:db8:85a3::5/64&quot;. The addresses are listed in increasing priority, meaning the last address will be the primary address. </p>
<p> Format: a comma separated list of addresses</dl>
<p> <code>dhcp-duid</code></p>
<dl>
<dd>A string containing the DHCPv6 Unique Identifier (DUID) used by the dhcp client to identify itself to DHCPv6 servers (RFC 3315). The DUID is carried in the Client Identifier option. If the property is a hex string (&#8216;aa:bb:cc&#8217;) it is interpreted as a binary DUID and filled as an opaque value in the Client Identifier option. The special value &quot;lease&quot; will retrieve the DUID previously used from the lease file belonging to the connection. If no DUID is found and &quot;dhclient&quot; is the configured dhcp client, the DUID is searched in the system-wide dhclient lease file. If still no DUID is found, or another dhcp client is used, a global and permanent DUID-UUID (RFC 6355) will be generated based on the machine-id. The special values &quot;llt&quot; and &quot;ll&quot; will generate a DUID of type LLT or LL (see RFC 3315) based on the current MAC address of the device. In order to try providing a stable DUID-LLT, the time field will contain a constant timestamp that is used globally (for all profiles) and persisted to disk. The special values &quot;stable-llt&quot;, &quot;stable-ll&quot; and &quot;stable-uuid&quot; will generate a DUID of the corresponding type, derived from the connection&#8217;s stable-id and a per-host unique key. You may want to include the &quot;${DEVICE}&quot; or &quot;${MAC}&quot; specifier in the stable-id, in case this profile gets activated on multiple devices. So, the link-layer address of &quot;stable-ll&quot; and &quot;stable-llt&quot; will be a generated address derived from the stable id. The DUID-LLT time value in the &quot;stable-llt&quot; option will be picked among a static timespan of three years (the upper bound of the interval is the same constant timestamp used in &quot;llt&quot;). When the property is unset, the global value provided for &quot;ipv6.dhcp-duid&quot; is used. If no global value is provided, the default &quot;lease&quot; value is assumed. </p>
<p> Format: string</dl>
<p> <code>dhcp-hostname</code></p>
<dl>
<dd>If the &quot;dhcp-send-hostname&quot; property is TRUE, then the specified name will be sent to the DHCP server when acquiring a lease. This property and &quot;dhcp-fqdn&quot; are mutually exclusive and cannot be set at the same time. </p>
<p> Format: string</dl>
<p> <code>dhcp-hostname-flags</code></p>
<dl>
<dd>Flags for the DHCP hostname and FQDN. Currently, this property only includes flags to control the FQDN flags set in the DHCP FQDN option. Supported FQDN flags are NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1), NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) and NM_DHCP_HOSTNAME_FLAG_FQDN_NO_UPDATE (0x4). When no FQDN flag is set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is set, the DHCP FQDN option will contain no flag. Otherwise, if no FQDN flag is set and NM_DHCP_HOSTNAME_FLAG_FQDN_CLEAR_FLAGS (0x8) is not set, the standard FQDN flags are set in the request: NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1), NM_DHCP_HOSTNAME_FLAG_FQDN_ENCODED (0x2) for IPv4 and NM_DHCP_HOSTNAME_FLAG_FQDN_SERV_UPDATE (0x1) for IPv6. When this property is set to the default value NM_DHCP_HOSTNAME_FLAG_NONE (0x0), a global default is looked up in NetworkManager configuration. If that value is unset or also NM_DHCP_HOSTNAME_FLAG_NONE (0x0), then the standard FQDN flags described above are sent in the DHCP requests. </p>
<p> Format: uint32</dl>
<p> <code>dhcp-iaid</code></p>
<dl>
<dd>A string containing the &quot;Identity Association Identifier&quot; (IAID) used by the DHCP client. The property is a 32-bit decimal value or a special value among &quot;mac&quot;, &quot;perm-mac&quot;, &quot;ifname&quot; and &quot;stable&quot;. When set to &quot;mac&quot; (or &quot;perm-mac&quot;), the last 4 bytes of the current (or permanent) MAC address are used as IAID. When set to &quot;ifname&quot;, the IAID is computed by hashing the interface name. The special value &quot;stable&quot; can be used to generate an IAID based on the stable-id (see connection.stable-id), a per-host key and the interface name. When the property is unset, the value from global configuration is used; if no global default is set then the IAID is assumed to be &quot;ifname&quot;. Note that at the moment this property is ignored for IPv6 by dhclient, which always derives the IAID from the MAC address. </p>
<p> Format: string</dl>
<p> <code>dhcp-send-hostname</code></p>
<dl>
<dd>If TRUE, a hostname is sent to the DHCP server when acquiring a lease. Some DHCP servers use this hostname to update DNS databases, essentially providing a static hostname for the computer. If the &quot;dhcp-hostname&quot; property is NULL and this property is TRUE, the current persistent hostname of the computer is sent. </p>
<p> Format: boolean</dl>
<p> <code>dhcp-timeout</code></p>
<dl>
<dd>A timeout for a DHCP transaction in seconds. If zero (the default), a globally configured default is used. If still unspecified, a device specific timeout is used (usually 45 seconds). Set to 2147483647 (MAXINT32) for infinity. </p>
<p> Format: int32</dl>
<p> <code>dns</code></p>
<dl>
<dd>Array of IP addresses of DNS servers. </p>
<p> Format: array of byte array</dl>
<p> <code>dns-options</code></p>
<dl>
<dd>Array of DNS options as described in man 5 resolv.conf. NULL means that the options are unset and left at the default. In this case NetworkManager will use default options. This is distinct from an empty list of properties. The currently supported options are &quot;attempts&quot;, &quot;debug&quot;, &quot;edns0&quot;, &quot;inet6&quot;, &quot;ip6-bytestring&quot;, &quot;ip6-dotint&quot;, &quot;ndots&quot;, &quot;no-check-names&quot;, &quot;no-ip6-dotint&quot;, &quot;no-reload&quot;, &quot;no-tld-query&quot;, &quot;rotate&quot;, &quot;single-request&quot;, &quot;single-request-reopen&quot;, &quot;timeout&quot;, &quot;trust-ad&quot;, &quot;use-vc&quot;. The &quot;trust-ad&quot; setting is only honored if the profile contributes name servers to resolv.conf, and if all contributing profiles have &quot;trust-ad&quot; enabled. When using a caching DNS plugin (dnsmasq or systemd-resolved in NetworkManager.conf) then &quot;edns0&quot; and &quot;trust-ad&quot; are automatically added. </p>
<p> Format: array of string</dl>
<p> <code>dns-priority</code></p>
<dl>
<dd>DNS servers priority. The relative priority for DNS servers specified by this setting. A lower numerical value is better (higher priority). Negative values have the special effect of excluding other configurations with a greater numerical priority value; so in presence of at least one negative priority, only DNS servers from connections with the lowest priority value will be used. To avoid all DNS leaks, set the priority of the profile that should be used to the most negative value of all active connections profiles. Zero selects a globally configured default value. If the latter is missing or zero too, it defaults to 50 for VPNs (including WireGuard) and 100 for other connections. Note that the priority is to order DNS settings for multiple active connections. It does not disambiguate multiple DNS servers within the same connection profile. When multiple devices have configurations with the same priority, VPNs will be considered first, then devices with the best (lowest metric) default route and then all other devices. When using dns=default, servers with higher priority will be on top of resolv.conf. To prioritize a given server over another one within the same connection, just specify them in the desired order. Note that commonly the resolver tries name servers in /etc/resolv.conf in the order listed, proceeding with the next server in the list on failure. See for example the &quot;rotate&quot; option of the dns-options setting. If there are any negative DNS priorities, then only name servers from the devices with that lowest priority will be considered. When using a DNS resolver that supports Conditional Forwarding or Split DNS (with dns=dnsmasq or dns=systemd-resolved settings), each connection is used to query domains in its search list. The search domains determine which name servers to ask, and the DNS priority is used to prioritize name servers based on the domain. Queries for domains not present in any search list are routed through connections having the &#8216;~.&#8217; special wildcard domain, which is added automatically to connections with the default route (or can be added manually). When multiple connections specify the same domain, the one with the best priority (lowest numerical value) wins. If a sub domain is configured on another interface it will be accepted regardless the priority, unless parent domain on the other interface has a negative priority, which causes the sub domain to be shadowed. With Split DNS one can avoid undesired DNS leaks by properly configuring DNS priorities and the search domains, so that only name servers of the desired interface are configured. </p>
<p> Format: int32</dl>
<p> <code>dns-search</code></p>
<dl>
<dd>Array of DNS search domains. Domains starting with a tilde (&#8216;~&#8217;) are considered &#8216;routing&#8217; domains and are used only to decide the interface over which a query must be forwarded; they are not used to complete unqualified host names. When using a DNS plugin that supports Conditional Forwarding or Split DNS, then the search domains specify which name servers to query. This makes the behavior different from running with plain /etc/resolv.conf. For more information see also the dns-priority setting. </p>
<p> Format: array of string</dl>
<p> <code>gateway</code></p>
<dl>
<dd>Alias: gw6 </p>
<p> The gateway associated with this configuration. This is only meaningful if &quot;addresses&quot; is also set. The gateway&#8217;s main purpose is to control the next hop of the standard default route on the device. Hence, the gateway property conflicts with &quot;never-default&quot; and will be automatically dropped if the IP configuration is set to never-default. As an alternative to set the gateway, configure a static default route with /0 as prefix length. </p>
<p> Format: string</dl>
<p> <code>ignore-auto-dns</code></p>
<dl>
<dd>When &quot;method&quot; is set to &quot;auto&quot; and this property to TRUE, automatically configured name servers and search domains are ignored and only name servers and search domains specified in the &quot;dns&quot; and &quot;dns-search&quot; properties, if any, are used. </p>
<p> Format: boolean</dl>
<p> <code>ignore-auto-routes</code></p>
<dl>
<dd>When &quot;method&quot; is set to &quot;auto&quot; and this property to TRUE, automatically configured routes are ignored and only routes specified in the &quot;routes&quot; property, if any, are used. </p>
<p> Format: boolean</dl>
<p> <code>ip6-privacy</code></p>
<dl>
<dd>Configure IPv6 Privacy Extensions for SLAAC, described in RFC4941. If enabled, it makes the kernel generate a temporary IPv6 address in addition to the public one generated from MAC address via modified EUI-64. This enhances privacy, but could cause problems in some applications, on the other hand. The permitted values are: -1: unknown, 0: disabled, 1: enabled (prefer public address), 2: enabled (prefer temporary addresses). Having a per-connection setting set to &quot;-1&quot; (unknown) means fallback to global configuration &quot;ipv6.ip6-privacy&quot;. If also global configuration is unspecified or set to &quot;-1&quot;, fallback to read &quot;/proc/sys/net/ipv6/conf/default/use_tempaddr&quot;. Note that this setting is distinct from the Stable Privacy addresses that can be enabled with the &quot;addr-gen-mode&quot; property&#8217;s &quot;stable-privacy&quot; setting as another way of avoiding host tracking with IPv6 addresses. </p>
<p> Format: NMSettingIP6ConfigPrivacy (int32)</dl>
<p> <code>may-fail</code></p>
<dl>
<dd>If TRUE, allow overall network configuration to proceed even if the configuration specified by this property times out. Note that at least one IP configuration must succeed or overall network configuration will still fail. For example, in IPv6-only networks, setting this property to TRUE on the NMSettingIP4Config allows the overall network configuration to succeed if IPv4 configuration fails but IPv6 configuration completes successfully. </p>
<p> Format: boolean</dl>
<p> <code>method</code></p>
<dl>
<dd>IP configuration method. NMSettingIP4Config and NMSettingIP6Config both support &quot;disabled&quot;, &quot;auto&quot;, &quot;manual&quot;, and &quot;link-local&quot;. See the subclass-specific documentation for other values. In general, for the &quot;auto&quot; method, properties such as &quot;dns&quot; and &quot;routes&quot; specify information that is added on to the information returned from automatic configuration. The &quot;ignore-auto-routes&quot; and &quot;ignore-auto-dns&quot; properties modify this behavior. For methods that imply no upstream network, such as &quot;shared&quot; or &quot;link-local&quot;, these properties must be empty. For IPv4 method &quot;shared&quot;, the IP subnet can be configured by adding one manual IPv4 address or otherwise 10.42.x.0/24 is chosen. Note that the shared method must be configured on the interface which shares the internet to a subnet, not on the uplink which is shared. </p>
<p> Format: string</dl>
<p> <code>never-default</code></p>
<dl>
<dd>If TRUE, this connection will never be the default connection for this IP type, meaning it will never be assigned the default route by NetworkManager. </p>
<p> Format: boolean</dl>
<p> <code>ra-timeout</code></p>
<dl>
<dd>A timeout for waiting Router Advertisements in seconds. If zero (the default), a globally configured default is used. If still unspecified, the timeout depends on the sysctl settings of the device. Set to 2147483647 (MAXINT32) for infinity. </p>
<p> Format: int32</dl>
<p> <code>required-timeout</code></p>
<dl>
<dd>The minimum time interval in milliseconds for which dynamic IP configuration should be tried before the connection succeeds. This property is useful for example if both IPv4 and IPv6 are enabled and are allowed to fail. Normally the connection succeeds as soon as one of the two address families completes; by setting a required timeout for e.g. IPv4, one can ensure that even if IP6 succeeds earlier than IPv4, NetworkManager waits some time for IPv4 before the connection becomes active. Note that if &quot;may-fail&quot; is FALSE for the same address family, this property has no effect as NetworkManager needs to wait for the full DHCP timeout. A zero value means that no required timeout is present, -1 means the default value (either configuration ipvx.required-timeout override or zero). </p>
<p> Format: int32</dl>
<p> <code>route-metric</code></p>
<dl>
<dd>The default metric for routes that don&#8217;t explicitly specify a metric. The default value -1 means that the metric is chosen automatically based on the device type. The metric applies to dynamic routes, manual (static) routes that don&#8217;t have an explicit metric setting, address prefix routes, and the default route. Note that for IPv6, the kernel accepts zero (0) but coerces it to 1024 (user default). Hence, setting this property to zero effectively mean setting it to 1024. For IPv4, zero is a regular value for the metric. </p>
<p> Format: int64</dl>
<p> <code>route-table</code></p>
<dl>
<dd>Enable policy routing (source routing) and set the routing table used when adding routes. This affects all routes, including device-routes, IPv4LL, DHCP, SLAAC, default-routes and static routes. But note that static routes can individually overwrite the setting by explicitly specifying a non-zero routing table. If the table setting is left at zero, it is eligible to be overwritten via global configuration. If the property is zero even after applying the global configuration value, policy routing is disabled for the address family of this connection. Policy routing disabled means that NetworkManager will add all routes to the main table (except static routes that explicitly configure a different table). Additionally, NetworkManager will not delete any extraneous routes from tables except the main table. This is to preserve backward compatibility for users who manage routing tables outside of NetworkManager. </p>
<p> Format: uint32</dl>
<p> <code>routes</code></p>
<dl>
<dd>A list of IPv6 destination addresses, prefix length, optional IPv6 next hop addresses, optional route metric, optional attribute. The valid syntax is: &quot;ip[/prefix] [next-hop] [metric] [attribute=val]&#8230;[,ip[/prefix]&#8230;]&quot;. </p>
<p> Various attributes are supported: </p>
<dl>
<dd>&bull; &quot;cwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;from&quot; &#8211; an IPv6 address with optional prefix. IPv6 only.</dl>
<dl>
<dd>&bull; &quot;initcwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;initrwnd&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;lock-cwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-initcwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-initrwnd&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-mtu&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;lock-window&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;mtu&quot; &#8211; an unsigned 32 bit integer.</dl>
<dl>
<dd>&bull; &quot;onlink&quot; &#8211; a boolean value.</dl>
<dl>
<dd>&bull; &quot;src&quot; &#8211; an IPv6 address.</dl>
<dl>
<dd>&bull; &quot;table&quot; &#8211; an unsigned 32 bit integer. The default depends on ipv6.route-table.</dl>
<dl>
<dd>&bull; &quot;type&quot; &#8211; one of unicast, local, blackhole, unavailable, prohibit. The default is unicast.</dl>
<dl>
<dd>&bull; &quot;window&quot; &#8211; an unsigned 32 bit integer.</dl>
<p> For details see also `man ip-route`. </p>
<p> Format: a comma separated list of routes</dl>
<p> <code>routing-rules</code></p>
<dl>
<dd>A comma separated list of routing rules for policy routing. The format is based on <code>ip rule add</code> syntax and mostly compatible. One difference is that routing rules in NetworkManager always need a fixed priority. </p>
<p> Example: priority 5 from 1:2:3::5/128 table 45 </p>
<p> Format: a comma separated list of routing rules</dl>
<p> <code>token</code></p>
<dl>
<dd>Configure the token for draft-chown-6man-tokenised-ipv6-identifiers-02 IPv6 tokenized interface identifiers. Useful with eui64 addr-gen-mode. </p>
<p> Format: string</dl>
<h3>ip-tunnel setting</h3>
<p>IP Tunneling Settings. </p>
<p> Properties: </p>
<p> <code>encapsulation-limit</code></p>
<dl>
<dd>How many additional levels of encapsulation are permitted to be prepended to packets. This property applies only to IPv6 tunnels. </p>
<p> Format: uint32</dl>
<p> <code>flags</code></p>
<dl>
<dd>Tunnel flags. Currently, the following values are supported: NM_IP_TUNNEL_FLAG_IP6_IGN_ENCAP_LIMIT (0x1), NM_IP_TUNNEL_FLAG_IP6_USE_ORIG_TCLASS (0x2), NM_IP_TUNNEL_FLAG_IP6_USE_ORIG_FLOWLABEL (0x4), NM_IP_TUNNEL_FLAG_IP6_MIP6_DEV (0x8), NM_IP_TUNNEL_FLAG_IP6_RCV_DSCP_COPY (0x10), NM_IP_TUNNEL_FLAG_IP6_USE_ORIG_FWMARK (0x20). They are valid only for IPv6 tunnels. </p>
<p> Format: uint32</dl>
<p> <code>flow-label</code></p>
<dl>
<dd>The flow label to assign to tunnel packets. This property applies only to IPv6 tunnels. </p>
<p> Format: uint32</dl>
<p> <code>input-key</code></p>
<dl>
<dd>The key used for tunnel input packets; the property is valid only for certain tunnel modes (GRE, IP6GRE). If empty, no key is used. </p>
<p> Format: string</dl>
<p> <code>local</code></p>
<dl>
<dd>Alias: local </p>
<p> The local endpoint of the tunnel; the value can be empty, otherwise it must contain an IPv4 or IPv6 address. </p>
<p> Format: string</dl>
<p> <code>mode</code></p>
<dl>
<dd>Alias: mode </p>
<p> The tunneling mode, for example NM_IP_TUNNEL_MODE_IPIP (1) or NM_IP_TUNNEL_MODE_GRE (2). </p>
<p> Format: uint32</dl>
<p> <code>mtu</code></p>
<dl>
<dd>If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple fragments. </p>
<p> Format: uint32</dl>
<p> <code>output-key</code></p>
<dl>
<dd>The key used for tunnel output packets; the property is valid only for certain tunnel modes (GRE, IP6GRE). If empty, no key is used. </p>
<p> Format: string</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID the new device will be bound to so that tunneled packets will only be routed via that interface. </p>
<p> Format: string</dl>
<p> <code>path-mtu-discovery</code></p>
<dl>
<dd>Whether to enable Path MTU Discovery on this tunnel. </p>
<p> Format: boolean</dl>
<p> <code>remote</code></p>
<dl>
<dd>Alias: remote </p>
<p> The remote endpoint of the tunnel; the value must contain an IPv4 or IPv6 address. </p>
<p> Format: string</dl>
<p> <code>tos</code></p>
<dl>
<dd>The type of service (IPv4) or traffic class (IPv6) field to be set on tunneled packets. </p>
<p> Format: uint32</dl>
<p> <code>ttl</code></p>
<dl>
<dd>The TTL to assign to tunneled packets. 0 is a special value meaning that packets inherit the TTL value. </p>
<p> Format: uint32</dl>
<h3>macsec setting</h3>
<p>MACSec Settings. </p>
<p> Properties: </p>
<p> <code>encrypt</code></p>
<dl>
<dd>Alias: encrypt </p>
<p> Whether the transmitted traffic must be encrypted. </p>
<p> Format: boolean</dl>
<p> <code>mka-cak</code></p>
<dl>
<dd>Alias: cak </p>
<p> The pre-shared CAK (Connectivity Association Key) for MACsec Key Agreement. </p>
<p> Format: string</dl>
<p> <code>mka-cak-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;mka-cak&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>mka-ckn</code></p>
<dl>
<dd>Alias: ckn </p>
<p> The pre-shared CKN (Connectivity-association Key Name) for MACsec Key Agreement. </p>
<p> Format: string</dl>
<p> <code>mode</code></p>
<dl>
<dd>Alias: mode </p>
<p> Specifies how the CAK (Connectivity Association Key) for MKA (MACsec Key Agreement) is obtained. </p>
<p> Format: int32</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID from which this MACSEC interface should be created. If this property is not specified, the connection must contain an &quot;802-3-ethernet&quot; setting with a &quot;mac-address&quot; property. </p>
<p> Format: string</dl>
<p> <code>port</code></p>
<dl>
<dd>Alias: port </p>
<p> The port component of the SCI (Secure Channel Identifier), between 1 and 65534. </p>
<p> Format: int32</dl>
<p> <code>send-sci</code></p>
<dl>
<dd>Specifies whether the SCI (Secure Channel Identifier) is included in every packet. </p>
<p> Format: boolean</dl>
<p> <code>validation</code></p>
<dl>
<dd>Specifies the validation mode for incoming frames. </p>
<p> Format: int32</dl>
<h3>macvlan setting</h3>
<p>MAC VLAN Settings. </p>
<p> Properties: </p>
<p> <code>mode</code></p>
<dl>
<dd>Alias: mode </p>
<p> The macvlan mode, which specifies the communication mechanism between multiple macvlans on the same lower device. </p>
<p> Format: uint32</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID from which this MAC-VLAN interface should be created. If this property is not specified, the connection must contain an &quot;802-3-ethernet&quot; setting with a &quot;mac-address&quot; property. </p>
<p> Format: string</dl>
<p> <code>promiscuous</code></p>
<dl>
<dd>Whether the interface should be put in promiscuous mode. </p>
<p> Format: boolean</dl>
<p> <code>tap</code></p>
<dl>
<dd>Alias: tap </p>
<p> Whether the interface should be a MACVTAP. </p>
<p> Format: boolean</dl>
<h3>match setting</h3>
<p>Match settings. </p>
<p> Properties: </p>
<p> <code>driver</code></p>
<dl>
<dd>A list of driver names to match. Each element is a shell wildcard pattern. See NMSettingMatch:interface-name for how special characters &#8216;|&#8217;, &#8216;&amp;&#8217;, &#8216;!&#8217; and &#8216;\&#8217; are used for optional and mandatory matches and inverting the pattern. </p>
<p> Format: array of string</dl>
<p> <code>interface-name</code></p>
<dl>
<dd>A list of interface names to match. Each element is a shell wildcard pattern. An element can be prefixed with a pipe symbol (|) or an ampersand (&amp;). The former means that the element is optional and the latter means that it is mandatory. If there are any optional elements, than the match evaluates to true if at least one of the optional element matches (logical OR). If there are any mandatory elements, then they all must match (logical AND). By default, an element is optional. This means that an element &quot;foo&quot; behaves the same as &quot;|foo&quot;. An element can also be inverted with exclamation mark (!) between the pipe symbol (or the ampersand) and before the pattern. Note that &quot;!foo&quot; is a shortcut for the mandatory match &quot;&amp;!foo&quot;. Finally, a backslash can be used at the beginning of the element (after the optional special characters) to escape the start of the pattern. For example, &quot;&amp;\!a&quot; is an mandatory match for literally &quot;!a&quot;. </p>
<p> Format: array of string</dl>
<p> <code>kernel-command-line</code></p>
<dl>
<dd>A list of kernel command line arguments to match. This may be used to check whether a specific kernel command line option is set (or unset, if prefixed with the exclamation mark). The argument must either be a single word, or an assignment (i.e. two words, joined by &quot;=&quot;). In the former case the kernel command line is searched for the word appearing as is, or as left hand side of an assignment. In the latter case, the exact assignment is looked for with right and left hand side matching. Wildcard patterns are not supported. See NMSettingMatch:interface-name for how special characters &#8216;|&#8217;, &#8216;&amp;&#8217;, &#8216;!&#8217; and &#8216;\&#8217; are used for optional and mandatory matches and inverting the match. </p>
<p> Format: array of string</dl>
<p> <code>path</code></p>
<dl>
<dd>A list of paths to match against the ID_PATH udev property of devices. ID_PATH represents the topological persistent path of a device. It typically contains a subsystem string (pci, usb, platform, etc.) and a subsystem-specific identifier. For PCI devices the path has the form &quot;pci-$domain:$bus:$device.$function&quot;, where each variable is an hexadecimal value; for example &quot;pci-0000:0a:00.0&quot;. The path of a device can be obtained with &quot;udevadm info /sys/class/net/$dev | grep ID_PATH=&quot; or by looking at the &quot;path&quot; property exported by NetworkManager (&quot;nmcli -f general.path device show $dev&quot;). Each element of the list is a shell wildcard pattern. See NMSettingMatch:interface-name for how special characters &#8216;|&#8217;, &#8216;&amp;&#8217;, &#8216;!&#8217; and &#8216;\&#8217; are used for optional and mandatory matches and inverting the pattern. </p>
<p> Format: array of string</dl>
<h3>802-11-olpc-mesh setting</h3>
<p>Alias: olpc-mesh </p>
<p> OLPC Wireless Mesh Settings. </p>
<p> Properties: </p>
<p> <code>channel</code></p>
<dl>
<dd>Alias: channel </p>
<p> Channel on which the mesh network to join is located. </p>
<p> Format: uint32</dl>
<p> <code>dhcp-anycast-address</code></p>
<dl>
<dd>Alias: dhcp-anycast </p>
<p> Anycast DHCP MAC address used when requesting an IP address via DHCP. The specific anycast address used determines which DHCP server class answers the request. This is currently only implemented by dhclient DHCP plugin. </p>
<p> Format: byte array</dl>
<p> <code>ssid</code></p>
<dl>
<dd>Alias: ssid </p>
<p> SSID of the mesh network to join. </p>
<p> Format: byte array</dl>
<h3>ovs-bridge setting</h3>
<p>OvsBridge Link Settings. </p>
<p> Properties: </p>
<p> <code>datapath-type</code></p>
<dl>
<dd>The data path type. One of &quot;system&quot;, &quot;netdev&quot; or empty. </p>
<p> Format: string</dl>
<p> <code>fail-mode</code></p>
<dl>
<dd>The bridge failure mode. One of &quot;secure&quot;, &quot;standalone&quot; or empty. </p>
<p> Format: string</dl>
<p> <code>mcast-snooping-enable</code></p>
<dl>
<dd>Enable or disable multicast snooping. </p>
<p> Format: boolean</dl>
<p> <code>rstp-enable</code></p>
<dl>
<dd>Enable or disable RSTP. </p>
<p> Format: boolean</dl>
<p> <code>stp-enable</code></p>
<dl>
<dd>Enable or disable STP. </p>
<p> Format: boolean</dl>
<h3>ovs-dpdk setting</h3>
<p>OvsDpdk Link Settings. </p>
<p> Properties: </p>
<p> <code>devargs</code></p>
<dl>
<dd>Open vSwitch DPDK device arguments. </p>
<p> Format: string</dl>
<p> <code>n-rxq</code></p>
<dl>
<dd>Open vSwitch DPDK number of rx queues. Defaults to zero which means to leave the parameter in OVS unspecified and effectively configures one queue. </p>
<p> Format: uint32</dl>
<h3>ovs-interface setting</h3>
<p>Open vSwitch Interface Settings. </p>
<p> Properties: </p>
<p> <code>type</code></p>
<dl>
<dd>The interface type. Either &quot;internal&quot;, &quot;system&quot;, &quot;patch&quot;, &quot;dpdk&quot;, or empty. </p>
<p> Format: string</dl>
<h3>ovs-patch setting</h3>
<p>OvsPatch Link Settings. </p>
<p> Properties: </p>
<p> <code>peer</code></p>
<dl>
<dd>Specifies the name of the interface for the other side of the patch. The patch on the other side must also set this interface as peer. </p>
<p> Format: string</dl>
<h3>ovs-port setting</h3>
<p>OvsPort Link Settings. </p>
<p> Properties: </p>
<p> <code>bond-downdelay</code></p>
<dl>
<dd>The time port must be inactive in order to be considered down. </p>
<p> Format: uint32</dl>
<p> <code>bond-mode</code></p>
<dl>
<dd>Bonding mode. One of &quot;active-backup&quot;, &quot;balance-slb&quot;, or &quot;balance-tcp&quot;. </p>
<p> Format: string</dl>
<p> <code>bond-updelay</code></p>
<dl>
<dd>The time port must be active before it starts forwarding traffic. </p>
<p> Format: uint32</dl>
<p> <code>lacp</code></p>
<dl>
<dd>LACP mode. One of &quot;active&quot;, &quot;off&quot;, or &quot;passive&quot;. </p>
<p> Format: string</dl>
<p> <code>tag</code></p>
<dl>
<dd>The VLAN tag in the range 0-4095. </p>
<p> Format: uint32</dl>
<p> <code>vlan-mode</code></p>
<dl>
<dd>The VLAN mode. One of &quot;access&quot;, &quot;native-tagged&quot;, &quot;native-untagged&quot;, &quot;trunk&quot; or unset. </p>
<p> Format: string</dl>
<h3>ppp setting</h3>
<p>Point-to-Point Protocol Settings. </p>
<p> Properties: </p>
<p> <code>baud</code></p>
<dl>
<dd>If non-zero, instruct pppd to set the serial port to the specified baudrate. This value should normally be left as 0 to automatically choose the speed. </p>
<p> Format: uint32</dl>
<p> <code>crtscts</code></p>
<dl>
<dd>If TRUE, specify that pppd should set the serial port to use hardware flow control with RTS and CTS signals. This value should normally be set to FALSE. </p>
<p> Format: boolean</dl>
<p> <code>lcp-echo-failure</code></p>
<dl>
<dd>If non-zero, instruct pppd to presume the connection to the peer has failed if the specified number of LCP echo-requests go unanswered by the peer. The &quot;lcp-echo-interval&quot; property must also be set to a non-zero value if this property is used. </p>
<p> Format: uint32</dl>
<p> <code>lcp-echo-interval</code></p>
<dl>
<dd>If non-zero, instruct pppd to send an LCP echo-request frame to the peer every n seconds (where n is the specified value). Note that some PPP peers will respond to echo requests and some will not, and it is not possible to autodetect this. </p>
<p> Format: uint32</dl>
<p> <code>mppe-stateful</code></p>
<dl>
<dd>If TRUE, stateful MPPE is used. See pppd documentation for more information on stateful MPPE. </p>
<p> Format: boolean</dl>
<p> <code>mru</code></p>
<dl>
<dd>If non-zero, instruct pppd to request that the peer send packets no larger than the specified size. If non-zero, the MRU should be between 128 and 16384. </p>
<p> Format: uint32</dl>
<p> <code>mtu</code></p>
<dl>
<dd>If non-zero, instruct pppd to send packets no larger than the specified size. </p>
<p> Format: uint32</dl>
<p> <code>no-vj-comp</code></p>
<dl>
<dd>If TRUE, Van Jacobsen TCP header compression will not be requested. </p>
<p> Format: boolean</dl>
<p> <code>noauth</code></p>
<dl>
<dd>If TRUE, do not require the other side (usually the PPP server) to authenticate itself to the client. If FALSE, require authentication from the remote side. In almost all cases, this should be TRUE. </p>
<p> Format: boolean</dl>
<p> <code>nobsdcomp</code></p>
<dl>
<dd>If TRUE, BSD compression will not be requested. </p>
<p> Format: boolean</dl>
<p> <code>nodeflate</code></p>
<dl>
<dd>If TRUE, &quot;deflate&quot; compression will not be requested. </p>
<p> Format: boolean</dl>
<p> <code>refuse-chap</code></p>
<dl>
<dd>If TRUE, the CHAP authentication method will not be used. </p>
<p> Format: boolean</dl>
<p> <code>refuse-eap</code></p>
<dl>
<dd>If TRUE, the EAP authentication method will not be used. </p>
<p> Format: boolean</dl>
<p> <code>refuse-mschap</code></p>
<dl>
<dd>If TRUE, the MSCHAP authentication method will not be used. </p>
<p> Format: boolean</dl>
<p> <code>refuse-mschapv2</code></p>
<dl>
<dd>If TRUE, the MSCHAPv2 authentication method will not be used. </p>
<p> Format: boolean</dl>
<p> <code>refuse-pap</code></p>
<dl>
<dd>If TRUE, the PAP authentication method will not be used. </p>
<p> Format: boolean</dl>
<p> <code>require-mppe</code></p>
<dl>
<dd>If TRUE, MPPE (Microsoft Point-to-Point Encryption) will be required for the PPP session. If either 64-bit or 128-bit MPPE is not available the session will fail. Note that MPPE is not used on mobile broadband connections. </p>
<p> Format: boolean</dl>
<p> <code>require-mppe-128</code></p>
<dl>
<dd>If TRUE, 128-bit MPPE (Microsoft Point-to-Point Encryption) will be required for the PPP session, and the &quot;require-mppe&quot; property must also be set to TRUE. If 128-bit MPPE is not available the session will fail. </p>
<p> Format: boolean</dl>
<h3>pppoe setting</h3>
<p>PPP-over-Ethernet Settings. </p>
<p> Properties: </p>
<p> <code>parent</code></p>
<dl>
<dd>Alias: parent </p>
<p> If given, specifies the parent interface name on which this PPPoE connection should be created. If this property is not specified, the connection is activated on the interface specified in &quot;interface-name&quot; of NMSettingConnection. </p>
<p> Format: string</dl>
<p> <code>password</code></p>
<dl>
<dd>Alias: password </p>
<p> Password used to authenticate with the PPPoE service. </p>
<p> Format: string</dl>
<p> <code>password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>service</code></p>
<dl>
<dd>Alias: service </p>
<p> If specified, instruct PPPoE to only initiate sessions with access concentrators that provide the specified service. For most providers, this should be left blank. It is only required if there are multiple access concentrators or a specific service is known to be required. </p>
<p> Format: string</dl>
<p> <code>username</code></p>
<dl>
<dd>Alias: username </p>
<p> Username used to authenticate with the PPPoE service. </p>
<p> Format: string</dl>
<h3>proxy setting</h3>
<p>WWW Proxy Settings. </p>
<p> Properties: </p>
<p> <code>browser-only</code></p>
<dl>
<dd>Alias: browser-only </p>
<p> Whether the proxy configuration is for browser only. </p>
<p> Format: boolean</dl>
<p> <code>method</code></p>
<dl>
<dd>Alias: method </p>
<p> Method for proxy configuration, Default is NM_SETTING_PROXY_METHOD_NONE (0) </p>
<p> Format: int32</dl>
<p> <code>pac-script</code></p>
<dl>
<dd>Alias: pac-script </p>
<p> PAC script for the connection. </p>
<p> Format: string</dl>
<p> <code>pac-url</code></p>
<dl>
<dd>Alias: pac-url </p>
<p> PAC URL for obtaining PAC file. </p>
<p> Format: string</dl>
<h3>serial setting</h3>
<p>Serial Link Settings. </p>
<p> Properties: </p>
<p> <code>baud</code></p>
<dl>
<dd>Speed to use for communication over the serial port. Note that this value usually has no effect for mobile broadband modems as they generally ignore speed settings and use the highest available speed. </p>
<p> Format: uint32</dl>
<p> <code>bits</code></p>
<dl>
<dd>Byte-width of the serial communication. The 8 in &quot;8n1&quot; for example. </p>
<p> Format: uint32</dl>
<p> <code>parity</code></p>
<dl>
<dd>Parity setting of the serial port. </p>
<p> Format: NMSettingSerialParity (byte)</dl>
<p> <code>send-delay</code></p>
<dl>
<dd>Time to delay between each byte sent to the modem, in microseconds. </p>
<p> Format: uint64</dl>
<p> <code>stopbits</code></p>
<dl>
<dd>Number of stop bits for communication on the serial port. Either 1 or 2. The 1 in &quot;8n1&quot; for example. </p>
<p> Format: uint32</dl>
<h3>sriov setting</h3>
<p>SR-IOV settings. </p>
<p> Properties: </p>
<p> <code>autoprobe-drivers</code></p>
<dl>
<dd>Whether to autoprobe virtual functions by a compatible driver. If set to NM_TERNARY_TRUE (1), the kernel will try to bind VFs to a compatible driver and if this succeeds a new network interface will be instantiated for each VF. If set to NM_TERNARY_FALSE (0), VFs will not be claimed and no network interfaces will be created for them. When set to NM_TERNARY_DEFAULT (-1), the global default is used; in case the global default is unspecified it is assumed to be NM_TERNARY_TRUE (1). </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>total-vfs</code></p>
<dl>
<dd>The total number of virtual functions to create. Note that when the sriov setting is present NetworkManager enforces the number of virtual functions on the interface (also when it is zero) during activation and resets it upon deactivation. To prevent any changes to SR-IOV parameters don&#8217;t add a sriov setting to the connection. </p>
<p> Format: uint32</dl>
<p> <code>vfs</code></p>
<dl>
<dd>Array of virtual function descriptors. Each VF descriptor is a dictionary mapping attribute names to GVariant values. The &#8216;index&#8217; entry is mandatory for each VF. When represented as string a VF is in the form: &quot;INDEX [ATTR=VALUE[ ATTR=VALUE]&#8230;]&quot;. for example: &quot;2 mac=00:11:22:33:44:55 spoof-check=true&quot;. Multiple VFs can be specified using a comma as separator. Currently, the following attributes are supported: mac, spoof-check, trust, min-tx-rate, max-tx-rate, vlans. The &quot;vlans&quot; attribute is represented as a semicolon-separated list of VLAN descriptors, where each descriptor has the form &quot;ID[.PRIORITY[.PROTO]]&quot;. PROTO can be either &#8216;q&#8217; for 802.1Q (the default) or &#8216;ad&#8217; for 802.1ad. </p>
<p> Format: array of vardict</dl>
<h3>tc setting</h3>
<p>Linux Traffic Control Settings. </p>
<p> Properties: </p>
<p> <code>qdiscs</code></p>
<dl>
<dd>Array of TC queueing disciplines. qdisc is a basic block in the Linux traffic control subsystem </p>
<p> Each qdisc can be specified by the following attributes: </p>
<p> <i>handle HANDLE</i></p>
<dl>
<dd>specifies the qdisc handle. A qdisc, which potentially can have children, gets assigned a major number, called a &#8216;handle&#8217;, leaving the minor number namespace available for classes. The handle is expressed as &#8217;10:&#8217;. It is customary to explicitly assign a handle to qdiscs expected to have children.</dl>
<p> <i>parent HANDLE</i></p>
<dl>
<dd>specifies the handle of the parent qdisc the current qdisc must be attached to.</dl>
<p> <i>root</i></p>
<dl>
<dd>specifies that the qdisc is attached to the root of device.</dl>
<p> <i>KIND</i></p>
<dl>
<dd>this is the qdisc kind. NetworkManager currently supports the following kinds: fq_codel, sfq, tbf. Each qdisc kind has a different set of parameters, described below. There are also some kinds like pfifo, pfifo_fast, prio supported by NetworkManager but their parameters are not supported by NetworkManager.</dl>
<p> Parameters for &#8216;fq_codel&#8217;: </p>
<p> <i>limit U32</i></p>
<dl>
<dd>the hard limit on the real queue size. When this limit is reached, incoming packets are dropped. Default is 10240 packets.</dl>
<p> <i>memory_limit U32</i></p>
<dl>
<dd>sets a limit on the total number of bytes that can be queued in this FQ-CoDel instance. The lower of the packet limit of the limit parameter and the memory limit will be enforced. Default is 32 MB.</dl>
<p> <i>flows U32</i></p>
<dl>
<dd>the number of flows into which the incoming packets are classified. Due to the stochastic nature of hashing, multiple flows may end up being hashed into the same slot. Newer flows have priority over older ones. This parameter can be set only at load time since memory has to be allocated for the hash table. Default value is 1024.</dl>
<p> <i>target U32</i></p>
<dl>
<dd>the acceptable minimum standing/persistent queue delay. This minimum delay is identified by tracking the local minimum queue delay that packets experience. The unit of measurement is microsecond(us). Default value is 5ms.</dl>
<p> <i>interval U32</i></p>
<dl>
<dd>used to ensure that the measured minimum delay does not become too stale. The minimum delay must be experienced in the last epoch of length .B interval. It should be set on the order of the worst-case RTT through the bottleneck to give endpoints sufficient time to react. Default value is 100ms.</dl>
<p> <i>quantum U32</i></p>
<dl>
<dd>the number of bytes used as &#8216;deficit&#8217; in the fair queuing algorithm. Default is set to 1514 bytes which corresponds to the Ethernet MTU plus the hardware header length of 14 bytes.</dl>
<p> <i>ecn BOOL</i></p>
<dl>
<dd>can be used to mark packets instead of dropping them. ecn is turned on by default.</dl>
<p> <i>ce_threshold U32</i></p>
<dl>
<dd>sets a threshold above which all packets are marked with ECN Congestion Experienced. This is useful for DCTCP-style congestion control algorithms that require marking at very shallow queueing thresholds.</dl>
<p> Parameters for &#8216;sfq&#8217;: </p>
<p> <i>divisor U32</i></p>
<dl>
<dd>can be used to set a different hash table size, available from kernel 2.6.39 onwards. The specified divisor must be a power of two and cannot be larger than 65536. Default value: 1024.</dl>
<p> <i>limit U32</i></p>
<dl>
<dd>Upper limit of the SFQ. Can be used to reduce the default length of 127 packets.</dl>
<p> <i>depth U32</i></p>
<dl>
<dd>Limit of packets per flow. Default to 127 and can be lowered.</dl>
<p> <i>perturb_period U32</i></p>
<dl>
<dd>Interval in seconds for queue algorithm perturbation. Defaults to 0, which means that no perturbation occurs. Do not set too low for each perturbation may cause some packet reordering or losses. Advised value: 60 This value has no effect when external flow classification is used. Its better to increase divisor value to lower risk of hash collisions.</dl>
<p> <i>quantum U32</i></p>
<dl>
<dd>Amount of bytes a flow is allowed to dequeue during a round of the round robin process. Defaults to the MTU of the interface which is also the advised value and the minimum value.</dl>
<p> <i>flows U32</i></p>
<dl>
<dd>Default value is 127.</dl>
<p> Parameters for &#8216;tbf&#8217;: </p>
<p> <i>rate U64</i></p>
<dl>
<dd>Bandwidth or rate. These parameters accept a floating point number, possibly followed by either a unit (both SI and IEC units supported), or a float followed by a percent character to specify the rate as a percentage of the device&#8217;s speed.</dl>
<p> <i>burst U32</i></p>
<dl>
<dd>Also known as buffer or maxburst. Size of the bucket, in bytes. This is the maximum amount of bytes that tokens can be available for instantaneously. In general, larger shaping rates require a larger buffer. For 10mbit/s on Intel, you need at least 10kbyte buffer if you want to reach your configured rate! </p>
<p> If your buffer is too small, packets may be dropped because more tokens arrive per timer tick than fit in your bucket. The minimum buffer size can be calculated by dividing the rate by HZ. </p>
<p> Token usage calculations are performed using a table which by default has a resolution of 8 packets. This resolution can be changed by specifying the cell size with the burst. For example, to specify a 6000 byte buffer with a 16 byte cell size, set a burst of 6000/16. You will probably never have to set this. Must be an integral power of 2.</dl>
<p> <i>limit U32</i></p>
<dl>
<dd>Limit is the number of bytes that can be queued waiting for tokens to become available.</dl>
<p> <i>latency U32</i></p>
<dl>
<dd>specifies the maximum amount of time a packet can sit in the TBF. The latency calculation takes into account the size of the bucket, the rate and possibly the peakrate (if set). The latency and limit are mutually exclusive.</dl>
<p> Format: GPtrArray(NMTCQdisc)</dl>
<p> <code>tfilters</code></p>
<dl>
<dd>Array of TC traffic filters. Traffic control can manage the packet content during classification by using filters. </p>
<p> Each tfilters can be specified by the following attributes: </p>
<p> <i>handle HANDLE</i></p>
<dl>
<dd>specifies the tfilters handle. A filter is used by a classful qdisc to determine in which class a packet will be enqueued. It is important to notice that filters reside within qdiscs. Therefore, see qdiscs handle for detailed information.</dl>
<p> <i>parent HANDLE</i></p>
<dl>
<dd>specifies the handle of the parent qdisc the current qdisc must be attached to.</dl>
<p> <i>root</i></p>
<dl>
<dd>specifies that the qdisc is attached to the root of device.</dl>
<p> <i>KIND</i></p>
<dl>
<dd>this is the tfilters kind. NetworkManager currently supports following kinds: mirred, simple. Each filter kind has a different set of actions, described below. There are also some other kinds like matchall, basic, u32 supported by NetworkManager.</dl>
<p> Actions for &#8216;mirred&#8217;: </p>
<p> <i>egress bool</i></p>
<dl>
<dd>Define whether the packet should exit from the interface.</dl>
<p> <i>ingress bool</i></p>
<dl>
<dd>Define whether the packet should come into the interface.</dl>
<p> <i>mirror bool</i></p>
<dl>
<dd>Define whether the packet should be copied to the destination space.</dl>
<p> <i>redirect bool</i></p>
<dl>
<dd>Define whether the packet should be moved to the destination space.</dl>
<p> Action for &#8216;simple&#8217;: </p>
<p> <i>sdata char[32]</i></p>
<dl>
<dd>The actual string to print.</dl>
<p> Format: GPtrArray(NMTCTfilter)</dl>
<h3>team setting</h3>
<p>Teaming Settings. </p>
<p> Properties: </p>
<p> <code>config</code></p>
<dl>
<dd>Alias: config </p>
<p> The JSON configuration for the team network interface. The property should contain raw JSON configuration data suitable for teamd, because the value is passed directly to teamd. If not specified, the default configuration is used. See man teamd.conf for the format details. </p>
<p> Format: string</dl>
<p> <code>link-watchers</code></p>
<dl>
<dd>Link watchers configuration for the connection: each link watcher is defined by a dictionary, whose keys depend upon the selected link watcher. Available link watchers are &#8216;ethtool&#8217;, &#8216;nsna_ping&#8217; and &#8216;arp_ping&#8217; and it is specified in the dictionary with the key &#8216;name&#8217;. Available keys are: ethtool: &#8216;delay-up&#8217;, &#8216;delay-down&#8217;, &#8216;init-wait&#8217;; nsna_ping: &#8216;init-wait&#8217;, &#8216;interval&#8217;, &#8216;missed-max&#8217;, &#8216;target-host&#8217;; arp_ping: all the ones in nsna_ping and &#8216;source-host&#8217;, &#8216;validate-active&#8217;, &#8216;validate-inactive&#8217;, &#8216;send-always&#8217;. See teamd.conf man for more details. </p>
<p> Format: array of vardict</dl>
<p> <code>mcast-rejoin-count</code></p>
<dl>
<dd>Corresponds to the teamd mcast_rejoin.count. </p>
<p> Format: int32</dl>
<p> <code>mcast-rejoin-interval</code></p>
<dl>
<dd>Corresponds to the teamd mcast_rejoin.interval. </p>
<p> Format: int32</dl>
<p> <code>notify-peers-count</code></p>
<dl>
<dd>Corresponds to the teamd notify_peers.count. </p>
<p> Format: int32</dl>
<p> <code>notify-peers-interval</code></p>
<dl>
<dd>Corresponds to the teamd notify_peers.interval. </p>
<p> Format: int32</dl>
<p> <code>runner</code></p>
<dl>
<dd>Corresponds to the teamd runner.name. Permitted values are: &quot;roundrobin&quot;, &quot;broadcast&quot;, &quot;activebackup&quot;, &quot;loadbalance&quot;, &quot;lacp&quot;, &quot;random&quot;. </p>
<p> Format: string</dl>
<p> <code>runner-active</code></p>
<dl>
<dd>Corresponds to the teamd runner.active. </p>
<p> Format: boolean</dl>
<p> <code>runner-agg-select-policy</code></p>
<dl>
<dd>Corresponds to the teamd runner.agg_select_policy. </p>
<p> Format: string</dl>
<p> <code>runner-fast-rate</code></p>
<dl>
<dd>Corresponds to the teamd runner.fast_rate. </p>
<p> Format: boolean</dl>
<p> <code>runner-hwaddr-policy</code></p>
<dl>
<dd>Corresponds to the teamd runner.hwaddr_policy. </p>
<p> Format: string</dl>
<p> <code>runner-min-ports</code></p>
<dl>
<dd>Corresponds to the teamd runner.min_ports. </p>
<p> Format: int32</dl>
<p> <code>runner-sys-prio</code></p>
<dl>
<dd>Corresponds to the teamd runner.sys_prio. </p>
<p> Format: int32</dl>
<p> <code>runner-tx-balancer</code></p>
<dl>
<dd>Corresponds to the teamd runner.tx_balancer.name. </p>
<p> Format: string</dl>
<p> <code>runner-tx-balancer-interval</code></p>
<dl>
<dd>Corresponds to the teamd runner.tx_balancer.interval. </p>
<p> Format: int32</dl>
<p> <code>runner-tx-hash</code></p>
<dl>
<dd>Corresponds to the teamd runner.tx_hash. </p>
<p> Format: array of string</dl>
<h3>team-port setting</h3>
<p>Team Port Settings. </p>
<p> Properties: </p>
<p> <code>config</code></p>
<dl>
<dd>Alias: config </p>
<p> The JSON configuration for the team port. The property should contain raw JSON configuration data suitable for teamd, because the value is passed directly to teamd. If not specified, the default configuration is used. See man teamd.conf for the format details. </p>
<p> Format: string</dl>
<p> <code>lacp-key</code></p>
<dl>
<dd>Corresponds to the teamd ports.PORTIFNAME.lacp_key. </p>
<p> Format: int32</dl>
<p> <code>lacp-prio</code></p>
<dl>
<dd>Corresponds to the teamd ports.PORTIFNAME.lacp_prio. </p>
<p> Format: int32</dl>
<p> <code>link-watchers</code></p>
<dl>
<dd>Link watchers configuration for the connection: each link watcher is defined by a dictionary, whose keys depend upon the selected link watcher. Available link watchers are &#8216;ethtool&#8217;, &#8216;nsna_ping&#8217; and &#8216;arp_ping&#8217; and it is specified in the dictionary with the key &#8216;name&#8217;. Available keys are: ethtool: &#8216;delay-up&#8217;, &#8216;delay-down&#8217;, &#8216;init-wait&#8217;; nsna_ping: &#8216;init-wait&#8217;, &#8216;interval&#8217;, &#8216;missed-max&#8217;, &#8216;target-host&#8217;; arp_ping: all the ones in nsna_ping and &#8216;source-host&#8217;, &#8216;validate-active&#8217;, &#8216;validate-inactive&#8217;, &#8216;send-always&#8217;. See teamd.conf man for more details. </p>
<p> Format: array of vardict</dl>
<p> <code>prio</code></p>
<dl>
<dd>Corresponds to the teamd ports.PORTIFNAME.prio. </p>
<p> Format: int32</dl>
<p> <code>queue-id</code></p>
<dl>
<dd>Corresponds to the teamd ports.PORTIFNAME.queue_id. When set to -1 means the parameter is skipped from the json config. </p>
<p> Format: int32</dl>
<p> <code>sticky</code></p>
<dl>
<dd>Corresponds to the teamd ports.PORTIFNAME.sticky. </p>
<p> Format: boolean</dl>
<h3>tun setting</h3>
<p>Tunnel Settings. </p>
<p> Properties: </p>
<p> <code>group</code></p>
<dl>
<dd>Alias: group </p>
<p> The group ID which will own the device. If set to NULL everyone will be able to use the device. </p>
<p> Format: string</dl>
<p> <code>mode</code></p>
<dl>
<dd>Alias: mode </p>
<p> The operating mode of the virtual device. Allowed values are NM_SETTING_TUN_MODE_TUN (1) to create a layer 3 device and NM_SETTING_TUN_MODE_TAP (2) to create an Ethernet-like layer 2 one. </p>
<p> Format: uint32</dl>
<p> <code>multi-queue</code></p>
<dl>
<dd>Alias: multi-queue </p>
<p> If the property is set to TRUE, the interface will support multiple file descriptors (queues) to parallelize packet sending or receiving. Otherwise, the interface will only support a single queue. </p>
<p> Format: boolean</dl>
<p> <code>owner</code></p>
<dl>
<dd>Alias: owner </p>
<p> The user ID which will own the device. If set to NULL everyone will be able to use the device. </p>
<p> Format: string</dl>
<p> <code>pi</code></p>
<dl>
<dd>Alias: pi </p>
<p> If TRUE the interface will prepend a 4 byte header describing the physical interface to the packets. </p>
<p> Format: boolean</dl>
<p> <code>vnet-hdr</code></p>
<dl>
<dd>Alias: vnet-hdr </p>
<p> If TRUE the IFF_VNET_HDR the tunnel packets will include a virtio network header. </p>
<p> Format: boolean</dl>
<h3>vlan setting</h3>
<p>VLAN Settings. </p>
<p> Properties: </p>
<p> <code>egress-priority-map</code></p>
<dl>
<dd>Alias: egress </p>
<p> For outgoing packets, a list of mappings from Linux SKB priorities to 802.1p priorities. The mapping is given in the format &quot;from:to&quot; where both &quot;from&quot; and &quot;to&quot; are unsigned integers, ie &quot;7:3&quot;. </p>
<p> Format: array of string</dl>
<p> <code>flags</code></p>
<dl>
<dd>Alias: flags </p>
<p> One or more flags which control the behavior and features of the VLAN interface. Flags include NM_VLAN_FLAG_REORDER_HEADERS (0x1) (reordering of output packet headers), NM_VLAN_FLAG_GVRP (0x2) (use of the GVRP protocol), and NM_VLAN_FLAG_LOOSE_BINDING (0x4) (loose binding of the interface to its master device&#8217;s operating state). NM_VLAN_FLAG_MVRP (0x8) (use of the MVRP protocol). The default value of this property is NM_VLAN_FLAG_REORDER_HEADERS, but it used to be 0. To preserve backward compatibility, the default-value in the D-Bus API continues to be 0 and a missing property on D-Bus is still considered as 0. </p>
<p> Format: NMVlanFlags (uint32)</dl>
<p> <code>id</code></p>
<dl>
<dd>Alias: id </p>
<p> The VLAN identifier that the interface created by this connection should be assigned. The valid range is from 0 to 4094, without the reserved id 4095. </p>
<p> Format: uint32</dl>
<p> <code>ingress-priority-map</code></p>
<dl>
<dd>Alias: ingress </p>
<p> For incoming packets, a list of mappings from 802.1p priorities to Linux SKB priorities. The mapping is given in the format &quot;from:to&quot; where both &quot;from&quot; and &quot;to&quot; are unsigned integers, ie &quot;7:3&quot;. </p>
<p> Format: array of string</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID from which this VLAN interface should be created. If this property is not specified, the connection must contain an &quot;802-3-ethernet&quot; setting with a &quot;mac-address&quot; property. </p>
<p> Format: string</dl>
<h3>vpn setting</h3>
<p>VPN Settings. </p>
<p> Properties: </p>
<p> <code>data</code></p>
<dl>
<dd>Dictionary of key/value pairs of VPN plugin specific data. Both keys and values must be strings. </p>
<p> Format: dict of string to string</dl>
<p> <code>persistent</code></p>
<dl>
<dd>If the VPN service supports persistence, and this property is TRUE, the VPN will attempt to stay connected across link changes and outages, until explicitly disconnected. </p>
<p> Format: boolean</dl>
<p> <code>secrets</code></p>
<dl>
<dd>Dictionary of key/value pairs of VPN plugin specific secrets like passwords or private keys. Both keys and values must be strings. </p>
<p> Format: dict of string to string</dl>
<p> <code>service-type</code></p>
<dl>
<dd>Alias: vpn-type </p>
<p> D-Bus service name of the VPN plugin that this setting uses to connect to its network. i.e. org.freedesktop.NetworkManager.vpnc for the vpnc plugin. </p>
<p> Format: string</dl>
<p> <code>timeout</code></p>
<dl>
<dd>Timeout for the VPN service to establish the connection. Some services may take quite a long time to connect. Value of 0 means a default timeout, which is 60 seconds (unless overridden by vpn.timeout in configuration file). Values greater than zero mean timeout in seconds. </p>
<p> Format: uint32</dl>
<p> <code>user-name</code></p>
<dl>
<dd>Alias: user </p>
<p> If the VPN connection requires a user name for authentication, that name should be provided here. If the connection is available to more than one user, and the VPN requires each user to supply a different name, then leave this property empty. If this property is empty, NetworkManager will automatically supply the username of the user which requested the VPN connection. </p>
<p> Format: string</dl>
<h3>vrf setting</h3>
<p>VRF settings. </p>
<p> Properties: </p>
<p> <code>table</code></p>
<dl>
<dd>Alias: table </p>
<p> The routing table for this VRF. </p>
<p> Format: uint32</dl>
<h3>vxlan setting</h3>
<p>VXLAN Settings. </p>
<p> Properties: </p>
<p> <code>ageing</code></p>
<dl>
<dd>Specifies the lifetime in seconds of FDB entries learnt by the kernel. </p>
<p> Format: uint32</dl>
<p> <code>destination-port</code></p>
<dl>
<dd>Alias: destination-port </p>
<p> Specifies the UDP destination port to communicate to the remote VXLAN tunnel endpoint. </p>
<p> Format: uint32</dl>
<p> <code>id</code></p>
<dl>
<dd>Alias: id </p>
<p> Specifies the VXLAN Network Identifier (or VXLAN Segment Identifier) to use. </p>
<p> Format: uint32</dl>
<p> <code>l2-miss</code></p>
<dl>
<dd>Specifies whether netlink LL ADDR miss notifications are generated. </p>
<p> Format: boolean</dl>
<p> <code>l3-miss</code></p>
<dl>
<dd>Specifies whether netlink IP ADDR miss notifications are generated. </p>
<p> Format: boolean</dl>
<p> <code>learning</code></p>
<dl>
<dd>Specifies whether unknown source link layer addresses and IP addresses are entered into the VXLAN device forwarding database. </p>
<p> Format: boolean</dl>
<p> <code>limit</code></p>
<dl>
<dd>Specifies the maximum number of FDB entries. A value of zero means that the kernel will store unlimited entries. </p>
<p> Format: uint32</dl>
<p> <code>local</code></p>
<dl>
<dd>Alias: local </p>
<p> If given, specifies the source IP address to use in outgoing packets. </p>
<p> Format: string</dl>
<p> <code>parent</code></p>
<dl>
<dd>Alias: dev </p>
<p> If given, specifies the parent interface name or parent connection UUID. </p>
<p> Format: string</dl>
<p> <code>proxy</code></p>
<dl>
<dd>Specifies whether ARP proxy is turned on. </p>
<p> Format: boolean</dl>
<p> <code>remote</code></p>
<dl>
<dd>Alias: remote </p>
<p> Specifies the unicast destination IP address to use in outgoing packets when the destination link layer address is not known in the VXLAN device forwarding database, or the multicast IP address to join. </p>
<p> Format: string</dl>
<p> <code>rsc</code></p>
<dl>
<dd>Specifies whether route short circuit is turned on. </p>
<p> Format: boolean</dl>
<p> <code>source-port-max</code></p>
<dl>
<dd>Alias: source-port-max </p>
<p> Specifies the maximum UDP source port to communicate to the remote VXLAN tunnel endpoint. </p>
<p> Format: uint32</dl>
<p> <code>source-port-min</code></p>
<dl>
<dd>Alias: source-port-min </p>
<p> Specifies the minimum UDP source port to communicate to the remote VXLAN tunnel endpoint. </p>
<p> Format: uint32</dl>
<p> <code>tos</code></p>
<dl>
<dd>Specifies the TOS value to use in outgoing packets. </p>
<p> Format: uint32</dl>
<p> <code>ttl</code></p>
<dl>
<dd>Specifies the time-to-live value to use in outgoing packets. </p>
<p> Format: uint32</dl>
<h3>wifi-p2p setting</h3>
<p>Wi-Fi P2P Settings. </p>
<p> Properties: </p>
<p> <code>peer</code></p>
<dl>
<dd>Alias: peer </p>
<p> The P2P device that should be connected to. Currently, this is the only way to create or join a group. </p>
<p> Format: string</dl>
<p> <code>wfd-ies</code></p>
<dl>
<dd>The Wi-Fi Display (WFD) Information Elements (IEs) to set. Wi-Fi Display requires a protocol specific information element to be set in certain Wi-Fi frames. These can be specified here for the purpose of establishing a connection. This setting is only useful when implementing a Wi-Fi Display client. </p>
<p> Format: byte array</dl>
<p> <code>wps-method</code></p>
<dl>
<dd>Flags indicating which mode of WPS is to be used. There&#8217;s little point in changing the default setting as NetworkManager will automatically determine the best method to use. </p>
<p> Format: uint32</dl>
<h3>wimax setting</h3>
<p>WiMax Settings. </p>
<p> Properties: </p>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, this connection will only apply to the WiMAX device whose MAC address matches. This property does not change the MAC address of the device (known as MAC spoofing). Deprecated: 1 </p>
<p> Format: byte array</dl>
<p> <code>network-name</code></p>
<dl>
<dd>Alias: nsp </p>
<p> Network Service Provider (NSP) name of the WiMAX network this connection should use. Deprecated: 1 </p>
<p> Format: string</dl>
<h3>802-3-ethernet setting</h3>
<p>Alias: ethernet </p>
<p> Wired Ethernet Settings. </p>
<p> Properties: </p>
<p> <code>accept-all-mac-addresses</code></p>
<dl>
<dd>When TRUE, setup the interface to accept packets for all MAC addresses. This is enabling the kernel interface flag IFF_PROMISC. When FALSE, the interface will only accept the packets with the interface destination mac address or broadcast. </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>auto-negotiate</code></p>
<dl>
<dd>When TRUE, enforce auto-negotiation of speed and duplex mode. If &quot;speed&quot; and &quot;duplex&quot; properties are both specified, only that single mode will be advertised and accepted during the link auto-negotiation process: this works only for BASE-T 802.3 specifications and is useful for enforcing gigabits modes, as in these cases link negotiation is mandatory. When FALSE, &quot;speed&quot; and &quot;duplex&quot; properties should be both set or link configuration will be skipped. </p>
<p> Format: boolean</dl>
<p> <code>cloned-mac-address</code></p>
<dl>
<dd>Alias: cloned-mac </p>
<p> If specified, request that the device use this MAC address instead. This is known as MAC cloning or spoofing. Beside explicitly specifying a MAC address, the special values &quot;preserve&quot;, &quot;permanent&quot;, &quot;random&quot; and &quot;stable&quot; are supported. &quot;preserve&quot; means not to touch the MAC address on activation. &quot;permanent&quot; means to use the permanent hardware address if the device has one (otherwise this is treated as &quot;preserve&quot;). &quot;random&quot; creates a random MAC address on each connect. &quot;stable&quot; creates a hashed MAC address based on connection.stable-id and a machine dependent key. If unspecified, the value can be overwritten via global defaults, see manual of NetworkManager.conf. If still unspecified, it defaults to &quot;preserve&quot; (older versions of NetworkManager may use a different default value). On D-Bus, this field is expressed as &quot;assigned-mac-address&quot; or the deprecated &quot;cloned-mac-address&quot;. </p>
<p> Format: byte array</dl>
<p> <code>duplex</code></p>
<dl>
<dd>When a value is set, either &quot;half&quot; or &quot;full&quot;, configures the device to use the specified duplex mode. If &quot;auto-negotiate&quot; is &quot;yes&quot; the specified duplex mode will be the only one advertised during link negotiation: this works only for BASE-T 802.3 specifications and is useful for enforcing gigabits modes, as in these cases link negotiation is mandatory. If the value is unset (the default), the link configuration will be either skipped (if &quot;auto-negotiate&quot; is &quot;no&quot;, the default) or will be auto-negotiated (if &quot;auto-negotiate&quot; is &quot;yes&quot;) and the local device will advertise all the supported duplex modes. Must be set together with the &quot;speed&quot; property if specified. Before specifying a duplex mode be sure your device supports it. </p>
<p> Format: string</dl>
<p> <code>generate-mac-address-mask</code></p>
<dl>
<dd>With &quot;cloned-mac-address&quot; setting &quot;random&quot; or &quot;stable&quot;, by default all bits of the MAC address are scrambled and a locally-administered, unicast MAC address is created. This property allows to specify that certain bits are fixed. Note that the least significant bit of the first MAC address will always be unset to create a unicast MAC address. If the property is NULL, it is eligible to be overwritten by a default connection setting. If the value is still NULL or an empty string, the default is to create a locally-administered, unicast MAC address. If the value contains one MAC address, this address is used as mask. The set bits of the mask are to be filled with the current MAC address of the device, while the unset bits are subject to randomization. Setting &quot;FE:FF:FF:00:00:00&quot; means to preserve the OUI of the current MAC address and only randomize the lower 3 bytes using the &quot;random&quot; or &quot;stable&quot; algorithm. If the value contains one additional MAC address after the mask, this address is used instead of the current MAC address to fill the bits that shall not be randomized. For example, a value of &quot;FE:FF:FF:00:00:00 68:F7:28:00:00:00&quot; will set the OUI of the MAC address to 68:F7:28, while the lower bits are randomized. A value of &quot;02:00:00:00:00:00 00:00:00:00:00:00&quot; will create a fully scrambled globally-administered, burned-in MAC address. If the value contains more than one additional MAC addresses, one of them is chosen randomly. For example, &quot;02:00:00:00:00:00 00:00:00:00:00:00 02:00:00:00:00:00&quot; will create a fully scrambled MAC address, randomly locally or globally administered. </p>
<p> Format: string</dl>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, this connection will only apply to the Ethernet device whose permanent MAC address matches. This property does not change the MAC address of the device (i.e. MAC spoofing). </p>
<p> Format: byte array</dl>
<p> <code>mac-address-blacklist</code></p>
<dl>
<dd>If specified, this connection will never apply to the Ethernet device whose permanent MAC address matches an address in the list. Each MAC address is in the standard hex-digits-and-colons notation (00:11:22:33:44:55). </p>
<p> Format: array of string</dl>
<p> <code>mtu</code></p>
<dl>
<dd>Alias: mtu </p>
<p> If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple Ethernet frames. </p>
<p> Format: uint32</dl>
<p> <code>port</code></p>
<dl>
<dd>Specific port type to use if the device supports multiple attachment methods. One of &quot;tp&quot; (Twisted Pair), &quot;aui&quot; (Attachment Unit Interface), &quot;bnc&quot; (Thin Ethernet) or &quot;mii&quot; (Media Independent Interface). If the device supports only one port type, this setting is ignored. </p>
<p> Format: string</dl>
<p> <code>s390-nettype</code></p>
<dl>
<dd>s390 network device type; one of &quot;qeth&quot;, &quot;lcs&quot;, or &quot;ctc&quot;, representing the different types of virtual network devices available on s390 systems. </p>
<p> Format: string</dl>
<p> <code>s390-options</code></p>
<dl>
<dd>Dictionary of key/value pairs of s390-specific device options. Both keys and values must be strings. Allowed keys include &quot;portno&quot;, &quot;layer2&quot;, &quot;portname&quot;, &quot;protocol&quot;, among others. Key names must contain only alphanumeric characters (ie, [a-zA-Z0-9]). Currently, NetworkManager itself does nothing with this information. However, s390utils ships a udev rule which parses this information and applies it to the interface. </p>
<p> Format: dict of string to string</dl>
<p> <code>s390-subchannels</code></p>
<dl>
<dd>Identifies specific subchannels that this network device uses for communication with z/VM or s390 host. Like the &quot;mac-address&quot; property for non-z/VM devices, this property can be used to ensure this connection only applies to the network device that uses these subchannels. The list should contain exactly 3 strings, and each string may only be composed of hexadecimal characters and the period (.) character. </p>
<p> Format: array of string</dl>
<p> <code>speed</code></p>
<dl>
<dd>When a value greater than 0 is set, configures the device to use the specified speed. If &quot;auto-negotiate&quot; is &quot;yes&quot; the specified speed will be the only one advertised during link negotiation: this works only for BASE-T 802.3 specifications and is useful for enforcing gigabit speeds, as in this case link negotiation is mandatory. If the value is unset (0, the default), the link configuration will be either skipped (if &quot;auto-negotiate&quot; is &quot;no&quot;, the default) or will be auto-negotiated (if &quot;auto-negotiate&quot; is &quot;yes&quot;) and the local device will advertise all the supported speeds. In Mbit/s, ie 100 == 100Mbit/s. Must be set together with the &quot;duplex&quot; property when non-zero. Before specifying a speed value be sure your device supports it. </p>
<p> Format: uint32</dl>
<p> <code>wake-on-lan</code></p>
<dl>
<dd>The NMSettingWiredWakeOnLan options to enable. Not all devices support all options. May be any combination of NM_SETTING_WIRED_WAKE_ON_LAN_PHY (0x2), NM_SETTING_WIRED_WAKE_ON_LAN_UNICAST (0x4), NM_SETTING_WIRED_WAKE_ON_LAN_MULTICAST (0x8), NM_SETTING_WIRED_WAKE_ON_LAN_BROADCAST (0x10), NM_SETTING_WIRED_WAKE_ON_LAN_ARP (0x20), NM_SETTING_WIRED_WAKE_ON_LAN_MAGIC (0x40) or the special values NM_SETTING_WIRED_WAKE_ON_LAN_DEFAULT (0x1) (to use global settings) and NM_SETTING_WIRED_WAKE_ON_LAN_IGNORE (0x8000) (to disable management of Wake-on-LAN in NetworkManager). </p>
<p> Format: uint32</dl>
<p> <code>wake-on-lan-password</code></p>
<dl>
<dd>If specified, the password used with magic-packet-based Wake-on-LAN, represented as an Ethernet MAC address. If NULL, no password will be required. </p>
<p> Format: string</dl>
<h3>wireguard setting</h3>
<p>WireGuard Settings. </p>
<p> Properties: </p>
<p> <code>fwmark</code></p>
<dl>
<dd>The use of fwmark is optional and is by default off. Setting it to 0 disables it. Otherwise, it is a 32-bit fwmark for outgoing packets. Note that &quot;ip4-auto-default-route&quot; or &quot;ip6-auto-default-route&quot; enabled, implies to automatically choose a fwmark. </p>
<p> Format: uint32</dl>
<p> <code>ip4-auto-default-route</code></p>
<dl>
<dd>Whether to enable special handling of the IPv4 default route. If enabled, the IPv4 default route from wireguard.peer-routes will be placed to a dedicated routing-table and two policy routing rules will be added. The fwmark number is also used as routing-table for the default-route, and if fwmark is zero, an unused fwmark/table is chosen automatically. This corresponds to what wg-quick does with Table=auto and what WireGuard calls &quot;Improved Rule-based Routing&quot;. Note that for this automatism to work, you usually don&#8217;t want to set ipv4.gateway, because that will result in a conflicting default route. Leaving this at the default will enable this option automatically if ipv4.never-default is not set and there are any peers that use a default-route as allowed-ips. </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>ip6-auto-default-route</code></p>
<dl>
<dd>Like ip4-auto-default-route, but for the IPv6 default route. </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>listen-port</code></p>
<dl>
<dd>The listen-port. If listen-port is not specified, the port will be chosen randomly when the interface comes up. </p>
<p> Format: uint32</dl>
<p> <code>mtu</code></p>
<dl>
<dd>If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple fragments. If zero a default MTU is used. Note that contrary to wg-quick&#8217;s MTU setting, this does not take into account the current routes at the time of activation. </p>
<p> Format: uint32</dl>
<p> <code>peer-routes</code></p>
<dl>
<dd>Whether to automatically add routes for the AllowedIPs ranges of the peers. If TRUE (the default), NetworkManager will automatically add routes in the routing tables according to ipv4.route-table and ipv6.route-table. Usually you want this automatism enabled. If FALSE, no such routes are added automatically. In this case, the user may want to configure static routes in ipv4.routes and ipv6.routes, respectively. Note that if the peer&#8217;s AllowedIPs is &quot;0.0.0.0/0&quot; or &quot;::/0&quot; and the profile&#8217;s ipv4.never-default or ipv6.never-default setting is enabled, the peer route for this peer won&#8217;t be added automatically. </p>
<p> Format: boolean</dl>
<p> <code>private-key</code></p>
<dl>
<dd>The 256 bit private-key in base64 encoding. </p>
<p> Format: string</dl>
<p> <code>private-key-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;private-key&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<h3>802-11-wireless setting</h3>
<p>Alias: wifi </p>
<p> Wi-Fi Settings. </p>
<p> Properties: </p>
<p> <code>ap-isolation</code></p>
<dl>
<dd>Configures AP isolation, which prevents communication between wireless devices connected to this AP. This property can be set to a value different from NM_TERNARY_DEFAULT (-1) only when the interface is configured in AP mode. If set to NM_TERNARY_TRUE (1), devices are not able to communicate with each other. This increases security because it protects devices against attacks from other clients in the network. At the same time, it prevents devices to access resources on the same wireless networks as file shares, printers, etc. If set to NM_TERNARY_FALSE (0), devices can talk to each other. When set to NM_TERNARY_DEFAULT (-1), the global default is used; in case the global default is unspecified it is assumed to be NM_TERNARY_FALSE (0). </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>band</code></p>
<dl>
<dd>802.11 frequency band of the network. One of &quot;a&quot; for 5GHz 802.11a or &quot;bg&quot; for 2.4GHz 802.11. This will lock associations to the Wi-Fi network to the specific band, i.e. if &quot;a&quot; is specified, the device will not associate with the same network in the 2.4GHz band even if the network&#8217;s settings are compatible. This setting depends on specific driver capability and may not work with all drivers. </p>
<p> Format: string</dl>
<p> <code>bssid</code></p>
<dl>
<dd>If specified, directs the device to only associate with the given access point. This capability is highly driver dependent and not supported by all devices. Note: this property does not control the BSSID used when creating an Ad-Hoc network and is unlikely to in the future. </p>
<p> Format: byte array</dl>
<p> <code>channel</code></p>
<dl>
<dd>Wireless channel to use for the Wi-Fi connection. The device will only join (or create for Ad-Hoc networks) a Wi-Fi network on the specified channel. Because channel numbers overlap between bands, this property also requires the &quot;band&quot; property to be set. </p>
<p> Format: uint32</dl>
<p> <code>cloned-mac-address</code></p>
<dl>
<dd>Alias: cloned-mac </p>
<p> If specified, request that the device use this MAC address instead. This is known as MAC cloning or spoofing. Beside explicitly specifying a MAC address, the special values &quot;preserve&quot;, &quot;permanent&quot;, &quot;random&quot; and &quot;stable&quot; are supported. &quot;preserve&quot; means not to touch the MAC address on activation. &quot;permanent&quot; means to use the permanent hardware address of the device. &quot;random&quot; creates a random MAC address on each connect. &quot;stable&quot; creates a hashed MAC address based on connection.stable-id and a machine dependent key. If unspecified, the value can be overwritten via global defaults, see manual of NetworkManager.conf. If still unspecified, it defaults to &quot;preserve&quot; (older versions of NetworkManager may use a different default value). On D-Bus, this field is expressed as &quot;assigned-mac-address&quot; or the deprecated &quot;cloned-mac-address&quot;. </p>
<p> Format: byte array</dl>
<p> <code>generate-mac-address-mask</code></p>
<dl>
<dd>With &quot;cloned-mac-address&quot; setting &quot;random&quot; or &quot;stable&quot;, by default all bits of the MAC address are scrambled and a locally-administered, unicast MAC address is created. This property allows to specify that certain bits are fixed. Note that the least significant bit of the first MAC address will always be unset to create a unicast MAC address. If the property is NULL, it is eligible to be overwritten by a default connection setting. If the value is still NULL or an empty string, the default is to create a locally-administered, unicast MAC address. If the value contains one MAC address, this address is used as mask. The set bits of the mask are to be filled with the current MAC address of the device, while the unset bits are subject to randomization. Setting &quot;FE:FF:FF:00:00:00&quot; means to preserve the OUI of the current MAC address and only randomize the lower 3 bytes using the &quot;random&quot; or &quot;stable&quot; algorithm. If the value contains one additional MAC address after the mask, this address is used instead of the current MAC address to fill the bits that shall not be randomized. For example, a value of &quot;FE:FF:FF:00:00:00 68:F7:28:00:00:00&quot; will set the OUI of the MAC address to 68:F7:28, while the lower bits are randomized. A value of &quot;02:00:00:00:00:00 00:00:00:00:00:00&quot; will create a fully scrambled globally-administered, burned-in MAC address. If the value contains more than one additional MAC addresses, one of them is chosen randomly. For example, &quot;02:00:00:00:00:00 00:00:00:00:00:00 02:00:00:00:00:00&quot; will create a fully scrambled MAC address, randomly locally or globally administered. </p>
<p> Format: string</dl>
<p> <code>hidden</code></p>
<dl>
<dd>If TRUE, indicates that the network is a non-broadcasting network that hides its SSID. This works both in infrastructure and AP mode. In infrastructure mode, various workarounds are used for a more reliable discovery of hidden networks, such as probe-scanning the SSID. However, these workarounds expose inherent insecurities with hidden SSID networks, and thus hidden SSID networks should be used with caution. In AP mode, the created network does not broadcast its SSID. Note that marking the network as hidden may be a privacy issue for you (in infrastructure mode) or client stations (in AP mode), as the explicit probe-scans are distinctly recognizable on the air. </p>
<p> Format: boolean</dl>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, this connection will only apply to the Wi-Fi device whose permanent MAC address matches. This property does not change the MAC address of the device (i.e. MAC spoofing). </p>
<p> Format: byte array</dl>
<p> <code>mac-address-blacklist</code></p>
<dl>
<dd>A list of permanent MAC addresses of Wi-Fi devices to which this connection should never apply. Each MAC address should be given in the standard hex-digits-and-colons notation (eg &quot;00:11:22:33:44:55&quot;). </p>
<p> Format: array of string</dl>
<p> <code>mac-address-randomization</code></p>
<dl>
<dd>One of NM_SETTING_MAC_RANDOMIZATION_DEFAULT (0) (never randomize unless the user has set a global default to randomize and the supplicant supports randomization), NM_SETTING_MAC_RANDOMIZATION_NEVER (1) (never randomize the MAC address), or NM_SETTING_MAC_RANDOMIZATION_ALWAYS (2) (always randomize the MAC address). This property is deprecated for &#8216;cloned-mac-address&#8217;. Deprecated: 1 </p>
<p> Format: uint32</dl>
<p> <code>mode</code></p>
<dl>
<dd>Alias: mode </p>
<p> Wi-Fi network mode; one of &quot;infrastructure&quot;, &quot;mesh&quot;, &quot;adhoc&quot; or &quot;ap&quot;. If blank, infrastructure is assumed. </p>
<p> Format: string</dl>
<p> <code>mtu</code></p>
<dl>
<dd>Alias: mtu </p>
<p> If non-zero, only transmit packets of the specified size or smaller, breaking larger packets up into multiple Ethernet frames. </p>
<p> Format: uint32</dl>
<p> <code>powersave</code></p>
<dl>
<dd>One of NM_SETTING_WIRELESS_POWERSAVE_DISABLE (2) (disable Wi-Fi power saving), NM_SETTING_WIRELESS_POWERSAVE_ENABLE (3) (enable Wi-Fi power saving), NM_SETTING_WIRELESS_POWERSAVE_IGNORE (1) (don&#8217;t touch currently configure setting) or NM_SETTING_WIRELESS_POWERSAVE_DEFAULT (0) (use the globally configured value). All other values are reserved. </p>
<p> Format: uint32</dl>
<p> <code>rate</code></p>
<dl>
<dd>If non-zero, directs the device to only use the specified bitrate for communication with the access point. Units are in Kb/s, ie 5500 = 5.5 Mbit/s. This property is highly driver dependent and not all devices support setting a static bitrate. </p>
<p> Format: uint32</dl>
<p> <code>seen-bssids</code></p>
<dl>
<dd>A list of BSSIDs (each BSSID formatted as a MAC address like &quot;00:11:22:33:44:55&quot;) that have been detected as part of the Wi-Fi network. NetworkManager internally tracks previously seen BSSIDs. The property is only meant for reading and reflects the BSSID list of NetworkManager. The changes you make to this property will not be preserved. </p>
<p> Format: array of string</dl>
<p> <code>ssid</code></p>
<dl>
<dd>Alias: ssid </p>
<p> SSID of the Wi-Fi network. Must be specified. </p>
<p> Format: byte array</dl>
<p> <code>tx-power</code></p>
<dl>
<dd>If non-zero, directs the device to use the specified transmit power. Units are dBm. This property is highly driver dependent and not all devices support setting a static transmit power. </p>
<p> Format: uint32</dl>
<p> <code>wake-on-wlan</code></p>
<dl>
<dd>The NMSettingWirelessWakeOnWLan options to enable. Not all devices support all options. May be any combination of NM_SETTING_WIRELESS_WAKE_ON_WLAN_ANY (0x2), NM_SETTING_WIRELESS_WAKE_ON_WLAN_DISCONNECT (0x4), NM_SETTING_WIRELESS_WAKE_ON_WLAN_MAGIC (0x8), NM_SETTING_WIRELESS_WAKE_ON_WLAN_GTK_REKEY_FAILURE (0x10), NM_SETTING_WIRELESS_WAKE_ON_WLAN_EAP_IDENTITY_REQUEST (0x20), NM_SETTING_WIRELESS_WAKE_ON_WLAN_4WAY_HANDSHAKE (0x40), NM_SETTING_WIRELESS_WAKE_ON_WLAN_RFKILL_RELEASE (0x80), NM_SETTING_WIRELESS_WAKE_ON_WLAN_TCP (0x100) or the special values NM_SETTING_WIRELESS_WAKE_ON_WLAN_DEFAULT (0x1) (to use global settings) and NM_SETTING_WIRELESS_WAKE_ON_WLAN_IGNORE (0x8000) (to disable management of Wake-on-LAN in NetworkManager). </p>
<p> Format: uint32</dl>
<h3>802-11-wireless-security setting</h3>
<p>Alias: wifi-sec </p>
<p> Wi-Fi Security Settings. </p>
<p> Properties: </p>
<p> <code>auth-alg</code></p>
<dl>
<dd>When WEP is used (ie, key-mgmt = &quot;none&quot; or &quot;ieee8021x&quot;) indicate the 802.11 authentication algorithm required by the AP here. One of &quot;open&quot; for Open System, &quot;shared&quot; for Shared Key, or &quot;leap&quot; for Cisco LEAP. When using Cisco LEAP (ie, key-mgmt = &quot;ieee8021x&quot; and auth-alg = &quot;leap&quot;) the &quot;leap-username&quot; and &quot;leap-password&quot; properties must be specified. </p>
<p> Format: string</dl>
<p> <code>fils</code></p>
<dl>
<dd>Indicates whether Fast Initial Link Setup (802.11ai) must be enabled for the connection. One of NM_SETTING_WIRELESS_SECURITY_FILS_DEFAULT (0) (use global default value), NM_SETTING_WIRELESS_SECURITY_FILS_DISABLE (1) (disable FILS), NM_SETTING_WIRELESS_SECURITY_FILS_OPTIONAL (2) (enable FILS if the supplicant and the access point support it) or NM_SETTING_WIRELESS_SECURITY_FILS_REQUIRED (3) (enable FILS and fail if not supported). When set to NM_SETTING_WIRELESS_SECURITY_FILS_DEFAULT (0) and no global default is set, FILS will be optionally enabled. </p>
<p> Format: int32</dl>
<p> <code>group</code></p>
<dl>
<dd>A list of group/broadcast encryption algorithms which prevents connections to Wi-Fi networks that do not utilize one of the algorithms in the list. For maximum compatibility leave this property empty. Each list element may be one of &quot;wep40&quot;, &quot;wep104&quot;, &quot;tkip&quot;, or &quot;ccmp&quot;. </p>
<p> Format: array of string</dl>
<p> <code>key-mgmt</code></p>
<dl>
<dd>Key management used for the connection. One of &quot;none&quot; (WEP or no password protection), &quot;ieee8021x&quot; (Dynamic WEP), &quot;owe&quot; (Opportunistic Wireless Encryption), &quot;wpa-psk&quot; (WPA2 + WPA3 personal), &quot;sae&quot; (WPA3 personal only), &quot;wpa-eap&quot; (WPA2 + WPA3 enterprise) or &quot;wpa-eap-suite-b-192&quot; (WPA3 enterprise only). This property must be set for any Wi-Fi connection that uses security. </p>
<p> Format: string</dl>
<p> <code>leap-password</code></p>
<dl>
<dd>The login password for legacy LEAP connections (ie, key-mgmt = &quot;ieee8021x&quot; and auth-alg = &quot;leap&quot;). </p>
<p> Format: string</dl>
<p> <code>leap-password-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;leap-password&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>leap-username</code></p>
<dl>
<dd>The login username for legacy LEAP connections (ie, key-mgmt = &quot;ieee8021x&quot; and auth-alg = &quot;leap&quot;). </p>
<p> Format: string</dl>
<p> <code>pairwise</code></p>
<dl>
<dd>A list of pairwise encryption algorithms which prevents connections to Wi-Fi networks that do not utilize one of the algorithms in the list. For maximum compatibility leave this property empty. Each list element may be one of &quot;tkip&quot; or &quot;ccmp&quot;. </p>
<p> Format: array of string</dl>
<p> <code>pmf</code></p>
<dl>
<dd>Indicates whether Protected Management Frames (802.11w) must be enabled for the connection. One of NM_SETTING_WIRELESS_SECURITY_PMF_DEFAULT (0) (use global default value), NM_SETTING_WIRELESS_SECURITY_PMF_DISABLE (1) (disable PMF), NM_SETTING_WIRELESS_SECURITY_PMF_OPTIONAL (2) (enable PMF if the supplicant and the access point support it) or NM_SETTING_WIRELESS_SECURITY_PMF_REQUIRED (3) (enable PMF and fail if not supported). When set to NM_SETTING_WIRELESS_SECURITY_PMF_DEFAULT (0) and no global default is set, PMF will be optionally enabled. </p>
<p> Format: int32</dl>
<p> <code>proto</code></p>
<dl>
<dd>List of strings specifying the allowed WPA protocol versions to use. Each element may be one &quot;wpa&quot; (allow WPA) or &quot;rsn&quot; (allow WPA2/RSN). If not specified, both WPA and RSN connections are allowed. </p>
<p> Format: array of string</dl>
<p> <code>psk</code></p>
<dl>
<dd>Pre-Shared-Key for WPA networks. For WPA-PSK, it&#8217;s either an ASCII passphrase of 8 to 63 characters that is (as specified in the 802.11i standard) hashed to derive the actual key, or the key in form of 64 hexadecimal character. The WPA3-Personal networks use a passphrase of any length for SAE authentication. </p>
<p> Format: string</dl>
<p> <code>psk-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;psk&quot; property. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>wep-key-flags</code></p>
<dl>
<dd>Flags indicating how to handle the &quot;wep-key0&quot;, &quot;wep-key1&quot;, &quot;wep-key2&quot;, and &quot;wep-key3&quot; properties. See the section called &#8220;Secret flag types:&#8221; for flag values. </p>
<p> Format: NMSettingSecretFlags (uint32)</dl>
<p> <code>wep-key-type</code></p>
<dl>
<dd>Controls the interpretation of WEP keys. Allowed values are NM_WEP_KEY_TYPE_KEY (1), in which case the key is either a 10- or 26-character hexadecimal string, or a 5- or 13-character ASCII password; or NM_WEP_KEY_TYPE_PASSPHRASE (2), in which case the passphrase is provided as a string and will be hashed using the de-facto MD5 method to derive the actual WEP key. </p>
<p> Format: NMWepKeyType (uint32)</dl>
<p> <code>wep-key0</code></p>
<dl>
<dd>Index 0 WEP key. This is the WEP key used in most networks. See the &quot;wep-key-type&quot; property for a description of how this key is interpreted. </p>
<p> Format: string</dl>
<p> <code>wep-key1</code></p>
<dl>
<dd>Index 1 WEP key. This WEP index is not used by most networks. See the &quot;wep-key-type&quot; property for a description of how this key is interpreted. </p>
<p> Format: string</dl>
<p> <code>wep-key2</code></p>
<dl>
<dd>Index 2 WEP key. This WEP index is not used by most networks. See the &quot;wep-key-type&quot; property for a description of how this key is interpreted. </p>
<p> Format: string</dl>
<p> <code>wep-key3</code></p>
<dl>
<dd>Index 3 WEP key. This WEP index is not used by most networks. See the &quot;wep-key-type&quot; property for a description of how this key is interpreted. </p>
<p> Format: string</dl>
<p> <code>wep-tx-keyidx</code></p>
<dl>
<dd>When static WEP is used (ie, key-mgmt = &quot;none&quot;) and a non-default WEP key index is used by the AP, put that WEP key index here. Valid values are 0 (default key) through 3. Note that some consumer access points (like the Linksys WRT54G) number the keys 1 &#8211; 4. </p>
<p> Format: uint32</dl>
<p> <code>wps-method</code></p>
<dl>
<dd>Flags indicating which mode of WPS is to be used if any. There&#8217;s little point in changing the default setting as NetworkManager will automatically determine whether it&#8217;s feasible to start WPS enrollment from the Access Point capabilities. WPS can be disabled by setting this property to a value of 1. </p>
<p> Format: uint32</dl>
<h3>wpan setting</h3>
<p>IEEE 802.15.4 (WPAN) MAC Settings. </p>
<p> Properties: </p>
<p> <code>channel</code></p>
<dl>
<dd>Alias: channel </p>
<p> IEEE 802.15.4 channel. A positive integer or -1, meaning &quot;do not set, use whatever the device is already set to&quot;. </p>
<p> Format: int32</dl>
<p> <code>mac-address</code></p>
<dl>
<dd>Alias: mac </p>
<p> If specified, this connection will only apply to the IEEE 802.15.4 (WPAN) MAC layer device whose permanent MAC address matches. </p>
<p> Format: string</dl>
<p> <code>page</code></p>
<dl>
<dd>Alias: page </p>
<p> IEEE 802.15.4 channel page. A positive integer or -1, meaning &quot;do not set, use whatever the device is already set to&quot;. </p>
<p> Format: int32</dl>
<p> <code>pan-id</code></p>
<dl>
<dd>Alias: pan-id </p>
<p> IEEE 802.15.4 Personal Area Network (PAN) identifier. </p>
<p> Format: uint32</dl>
<p> <code>short-address</code></p>
<dl>
<dd>Alias: short-addr </p>
<p> Short IEEE 802.15.4 address to be used within a restricted environment. </p>
<p> Format: uint32</dl>
<h3>bond-port setting</h3>
<p>Bond Port Settings. </p>
<p> Properties: </p>
<p> <code>queue-id</code></p>
<dl>
<dd>Alias: queue-id </p>
<p> The queue ID of this bond port. The maximum value of queue ID is the number of TX queues currently active in device. </p>
<p> Format: uint32</dl>
<h3>hostname setting</h3>
<p>Hostname settings. </p>
<p> Properties: </p>
<p> <code>from-dhcp</code></p>
<dl>
<dd>Whether the system hostname can be determined from DHCP on this connection. When set to NM_TERNARY_DEFAULT (-1), the value from global configuration is used. If the property doesn&#8217;t have a value in the global configuration, NetworkManager assumes the value to be NM_TERNARY_TRUE (1). </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>from-dns-lookup</code></p>
<dl>
<dd>Whether the system hostname can be determined from reverse DNS lookup of addresses on this device. When set to NM_TERNARY_DEFAULT (-1), the value from global configuration is used. If the property doesn&#8217;t have a value in the global configuration, NetworkManager assumes the value to be NM_TERNARY_TRUE (1). </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>only-from-default</code></p>
<dl>
<dd>If set to NM_TERNARY_TRUE (1), NetworkManager attempts to get the hostname via DHCPv4/DHCPv6 or reverse DNS lookup on this device only when the device has the default route for the given address family (IPv4/IPv6). If set to NM_TERNARY_FALSE (0), the hostname can be set from this device even if it doesn&#8217;t have the default route. When set to NM_TERNARY_DEFAULT (-1), the value from global configuration is used. If the property doesn&#8217;t have a value in the global configuration, NetworkManager assumes the value to be NM_TERNARY_FALSE (0). </p>
<p> Format: NMTernary (int32)</dl>
<p> <code>priority</code></p>
<dl>
<dd>The relative priority of this connection to determine the system hostname. A lower numerical value is better (higher priority). A connection with higher priority is considered before connections with lower priority. If the value is zero, it can be overridden by a global value from NetworkManager configuration. If the property doesn&#8217;t have a value in the global configuration, the value is assumed to be 100. Negative values have the special effect of excluding other connections with a greater numerical priority value; so in presence of at least one negative priority, only connections with the lowest priority value will be used to determine the hostname. </p>
<p> Format: int32</dl>
<h3>veth setting</h3>
<p>Veth Settings. </p>
<p> Properties: </p>
<p> <code>peer</code></p>
<dl>
<dd>Alias: peer </p>
<p> This property specifies the peer interface name of the veth. This property is mandatory. </p>
<p> Format: string</dl>
<h3>Secret flag types:</h3>
<p>Each password or secret property in a setting has an associated <i>flags</i> property that describes how to handle that secret. The <i>flags</i> property is a bitfield that contains zero or more of the following values logically OR-ed together. </p>
<dl>
<dd>&bull; 0x0 (none) &#8211; the system is responsible for providing and storing this secret. This may be required so that secrets are already available before the user logs in. It also commonly means that the secret will be stored in plain text on disk, accessible to root only. For example via the keyfile settings plugin as described in the &quot;PLUGINS&quot; section in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5).</dl>
<dl>
<dd>&bull; 0x1 (agent-owned) &#8211; a user-session secret agent is responsible for providing and storing this secret; when it is required, agents will be asked to provide it.</dl>
<dl>
<dd>&bull; 0x2 (not-saved) &#8211; this secret should not be saved but should be requested from the user each time it is required. This flag should be used for One-Time-Pad secrets, PIN codes from hardware tokens, or if the user simply does not want to save the secret.</dl>
<dl>
<dd>&bull; 0x4 (not-required) &#8211; in some situations it cannot be automatically determined that a secret is required or not. This flag hints that the secret is not required and should not be requested from the user.</dl>
<h2>Files</h2>
<p>/etc/NetworkManager/system-connections or distro plugin-specific location</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-nm-settings-dbus/">nm-settings-dbus</a></code>(5), <code><a href="/docs/linux/man/5-nm-settings-keyfile/">nm-settings-keyfile</a></code>(5), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) </p>
