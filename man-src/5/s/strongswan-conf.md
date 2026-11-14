---
title: "strongswan-conf(5)"
name: "strongswan-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-strongswan-conf/"
description: "strongswan.conf – strongSwan configuration file"
---

<p>strongswan.conf &#8211; strongSwan configuration file</p>
<h2>Description</h2>
<p>While the <i><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></i>(5) configuration file is well suited to define IPsec related configuration parameters, it is not useful for other strongSwan applications to read options from this file. The file is hard to parse and only <i>ipsec starter</i> is capable of doing so. As the number of components of the strongSwan project is continually growing, a more flexible configuration file was needed, one that is easy to extend and can be used by all components. With strongSwan 4.2.1 <i><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></i>(5) was introduced which meets these requirements. </p>
<h2>Syntax</h2>
<p>The format of the strongswan.conf file consists of hierarchical <code>sections</code> and a list of <code>key/value pairs</code> in each section. Each section has a name, followed by C-Style curly brackets defining the section body. Each section body contains a set of subsections and key/value pairs: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>settings := (section|keyvalue)*<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section := name { settings }<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>keyvalue := key = value
</p>
<p> Values must be terminated by a newline. </p>
<p> Comments are possible using the <code>#</code>-character, but be careful: The parser implementation is currently limited and does not like brackets in comments. </p>
<p> Section names and keys may contain any printable character except: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>. { } # 
 	 space</p>
<p> An example file in this format might look like this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a = b<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section-one {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>somevalue = asdf<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>subsection {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>othervalue = xxx<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># yei, a comment<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>yetanother = zz<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section-two {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>x = 12<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> Indentation is optional, you may use tabs or spaces.</p>
<h2>Including Files</h2>
<p>Using the <code>include</code> statement it is possible to include other files into strongswan.conf, e.g. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>include /some/path/*.conf</p>
<p> If the file name is not an absolute path, it is considered to be relative to the directory of the file containing the include statement. The file name may include shell wildcards (see <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1)). Also, such inclusions can be nested. </p>
<p> Sections loaded from included files <i>extend</i> previously loaded sections; already existing values are <i>replaced</i>. It is important to note that settings are added relative to the section the include statement is in. </p>
<p> As an example, the following three files result in the same final config as the one given above: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a = b<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section-one {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>somevalue = before include<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>include include.conf<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>include other.conf</p>
<p> include.conf: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># settings loaded from this file are added to section-one<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># the following replaces the previous value<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>somevalue = asdf<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>subsection {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>othervalue = yyy<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>yetanother = zz</p>
<p> other.conf: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># this extends section-one and subsection<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section-one {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>subsection {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># this replaces the previous value<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>othervalue = xxx<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>section-two {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>x = 12<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<h2>Reading Values</h2>
<p>Values are accessed using a dot-separated section list and a key. With reference to the example above, accessing <code>section-one.subsection.othervalue</code> will return <code>xxx</code>.</p>
<h2>Defined Keys</h2>
<p>The following keys are currently defined (using dot notation). The default value (if any) is listed in brackets after the key.</p>
<dl>
<dt><code>aikgen.load</code> []</p>
<dd>Plugins to load in ipsec aikgen tool. </p>
<dt><code>attest.database</code> []</p>
<dd>File measurement information database URI. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>attest.load</code> []</p>
<dd>Plugins to load in ipsec attest tool. </p>
<dt><code>charon</code></p>
<dd>Options for the charon IKE daemon. </p>
<p> <code>Note</code>: Many of the options in this section also apply to <code>charon-cmd</code> and other <code>charon</code> derivatives. Just use their respective name (e.g. <code>charon-cmd</code> instead of <code>charon</code>). For many options defaults can be defined in the <code>libstrongswan</code> section. </p>
<dt><code>charon.accept_unencrypted_mainmode_messages</code> [no]</p>
<dd>Accept unencrypted ID and HASH payloads in IKEv1 Main Mode. </p>
<p> Some implementations send the third Main Mode message unencrypted, probably to find the PSKs for the specified ID for authentication. This is very similar to Aggressive Mode, and has the same security implications: A passive attacker can sniff the negotiated Identity, and start brute forcing the PSK using the HASH payload. </p>
<p> It is recommended to keep this option to no, unless you know exactly what the implications are and require compatibility to such devices (for example, some SonicWall boxes). </p>
<dt><code>charon.block_threshold</code> [5]</p>
<dd>Maximum number of half-open IKE_SAs for a single peer IP. </p>
<dt><code>charon.cache_crls</code> [no]</p>
<dd>Whether Certicate Revocation Lists (CRLs) fetched via HTTP or LDAP should be saved under a unique file name derived from the public key of the Certification Authority (CA) to <code>/etc/ipsec.d/crls</code> (stroke) or <code>/etc/swanctl/x509crl</code> (vici), respectively. </p>
<dt><code>charon.cert_cache</code> [yes]</p>
<dd>Whether relations in validated certificate chains should be cached in memory. </p>
<dt><code>charon.cisco_unity</code> [no]</p>
<dd>Send Cisco Unity vendor ID payload (IKEv1 only). </p>
<dt><code>charon.close_ike_on_child_failure</code> [no]</p>
<dd>Close the IKE_SA if setup of the CHILD_SA along with IKE_AUTH failed. </p>
<dt><code>charon.cookie_threshold</code> [10]</p>
<dd>Number of half-open IKE_SAs that activate the cookie mechanism. </p>
<dt><code>charon.crypto_test.bench</code> [no]</p>
<dd>Benchmark crypto algorithms and order them by efficiency. </p>
<dt><code>charon.crypto_test.bench_size</code> [1024]</p>
<dd>Buffer size used for crypto benchmark. </p>
<dt><code>charon.crypto_test.bench_time</code> [50]</p>
<dd>Number of iterations to test each algorithm. </p>
<dt><code>charon.crypto_test.on_add</code> [no]</p>
<dd>Test crypto algorithms during registration (requires test vectors provided by the <i>test-vectors</i> plugin). </p>
<dt><code>charon.crypto_test.on_create</code> [no]</p>
<dd>Test crypto algorithms on each crypto primitive instantiation. </p>
<dt><code>charon.crypto_test.required</code> [no]</p>
<dd>Strictly require at least one test vector to enable an algorithm. </p>
<dt><code>charon.crypto_test.rng_true</code> [no]</p>
<dd>Whether to test RNG with TRUE quality; requires a lot of entropy. </p>
<dt><code>charon.delete_rekeyed</code> [no]</p>
<dd>Delete CHILD_SAs right after they got successfully rekeyed (IKEv1 only). Reduces the number of stale CHILD_SAs in scenarios with a lot of rekeyings. However, this might cause problems with implementations that continue to use rekeyed SAs until they expire. </p>
<dt><code>charon.delete_rekeyed_delay</code> [5]</p>
<dd>Delay in seconds until inbound IPsec SAs are deleted after rekeyings (IKEv2 only). To process delayed packets the inbound part of a CHILD_SA is kept installed up to the configured number of seconds after it got replaced during a rekeying. If set to 0 the CHILD_SA will be kept installed until it expires (if no lifetime is set it will be destroyed immediately). </p>
<dt><code>charon.dh_exponent_ansi_x9_42</code> [yes]</p>
<dd>Use ANSI X9.42 DH exponent size or optimum size matched to cryptographic strength. </p>
<dt><code>charon.dlopen_use_rtld_now</code> [no]</p>
<dd>Use RTLD_NOW with dlopen when loading plugins and IMV/IMCs to reveal missing symbols immediately. </p>
<dt><code>charon.dns1</code> []</p>
<dd>DNS server assigned to peer via configuration payload (CP). </p>
<dt><code>charon.dns2</code> []</p>
<dd>DNS server assigned to peer via configuration payload (CP). </p>
<dt><code>charon.dos_protection</code> [yes]</p>
<dd>Enable Denial of Service protection using cookies and aggressiveness checks. </p>
<dt><code>charon.ecp_x_coordinate_only</code> [yes]</p>
<dd>Compliance with the errata for RFC 4753. </p>
<dt><code>charon.filelog</code></p>
<dd>Section to define file loggers, see LOGGER CONFIGURATION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.filelog.&lt;filename&gt;</code></p>
<dd>&lt;filename&gt; is the full path to the log file. </p>
<dt><code>charon.filelog.&lt;filename&gt;.&lt;subsystem&gt;</code> [&lt;default&gt;]</p>
<dd>Loglevel for a specific subsystem. </p>
<dt><code>charon.filelog.&lt;filename&gt;.append</code> [yes]</p>
<dd>If this option is enabled log entries are appended to the existing file. </p>
<dt><code>charon.filelog.&lt;filename&gt;.default</code> [1]</p>
<dd>Specifies the default loglevel to be used for subsystems for which no specific loglevel is defined. </p>
<dt><code>charon.filelog.&lt;filename&gt;.flush_line</code> [no]</p>
<dd>Enabling this option disables block buffering and enables line buffering. </p>
<dt><code>charon.filelog.&lt;filename&gt;.ike_name</code> [no]</p>
<dd>Prefix each log entry with the connection name and a unique numerical identifier for each IKE_SA. </p>
<dt><code>charon.filelog.&lt;filename&gt;.time_add_ms</code> [no]</p>
<dd>Adds the milliseconds within the current second after the timestamp (separated by a dot, so <i>time_format</i> should end with %S or %T). </p>
<dt><code>charon.filelog.&lt;filename&gt;.time_format</code> []</p>
<dd>Prefix each log entry with a timestamp. The option accepts a format string as passed to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). </p>
<dt><code>charon.flush_auth_cfg</code> [no]</p>
<dd>If enabled objects used during authentication (certificates, identities etc.) are released to free memory once an IKE_SA is established. Enabling this might conflict with plugins that later need access to e.g. the used certificates. </p>
<dt><code>charon.follow_redirects</code> [yes]</p>
<dd>Whether to follow IKEv2 redirects (RFC 5685). </p>
<dt><code>charon.fragment_size</code> [1280]</p>
<dd>Maximum size (complete IP datagram size in bytes) of a sent IKE fragment when using proprietary IKEv1 or standardized IKEv2 fragmentation, defaults to 1280 (use 0 for address family specific default values, which uses a lower value for IPv4). If specified this limit is used for both IPv4 and IPv6. </p>
<dt><code>charon.group</code> []</p>
<dd>Name of the group the daemon changes to after startup. </p>
<dt><code>charon.half_open_timeout</code> [30]</p>
<dd>Timeout in seconds for connecting IKE_SAs (also see IKE_SA_INIT DROPPING). </p>
<dt><code>charon.hash_and_url</code> [no]</p>
<dd>Enable hash and URL support. </p>
<dt><code>charon.host_resolver.max_threads</code> [3]</p>
<dd>Maximum number of concurrent resolver threads (they are terminated if unused). </p>
<dt><code>charon.host_resolver.min_threads</code> [0]</p>
<dd>Minimum number of resolver threads to keep around. </p>
<dt><code>charon.i_dont_care_about_security_and_use_aggressive_mode_psk</code> [no]</p>
<dd>If enabled responders are allowed to use IKEv1 Aggressive Mode with pre-shared keys, which is discouraged due to security concerns (offline attacks on the openly transmitted hash of the PSK). </p>
<dt><code>charon.ignore_acquire_ts</code> [no]</p>
<dd>If this is disabled the traffic selectors from the kernel&#8217;s acquire events, which are derived from the triggering packet, are prepended to the traffic selectors from the configuration for IKEv2 connection. By enabling this, such specific traffic selectors will be ignored and only the ones in the config will be sent. This always happens for IKEv1 connections as the protocol only supports one set of traffic selectors per CHILD_SA. </p>
<dt><code>charon.ignore_routing_tables</code> []</p>
<dd>A space-separated list of routing tables to be excluded from route lookups. </p>
<dt><code>charon.ikesa_limit</code> [0]</p>
<dd>Maximum number of IKE_SAs that can be established at the same time before new connection attempts are blocked. </p>
<dt><code>charon.ikesa_table_segments</code> [1]</p>
<dd>Number of exclusively locked segments in the hash table. </p>
<dt><code>charon.ikesa_table_size</code> [1]</p>
<dd>Size of the IKE_SA hash table. </p>
<dt><code>charon.imcv</code></p>
<dd>Defaults for options in this section can be configured in the <i>libimcv</i> section. </p>
<dt><code>charon.imcv.assessment_result</code> [yes]</p>
<dd>Whether IMVs send a standard IETF Assessment Result attribute. </p>
<dt><code>charon.imcv.database</code> []</p>
<dd>Global IMV policy database URI. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.imcv.os_info.default_password_enabled</code> [no]</p>
<dd>Manually set whether a default password is enabled </p>
<dt><code>charon.imcv.os_info.name</code> []</p>
<dd>Manually set the name of the client OS (e.g. Ubuntu). </p>
<dt><code>charon.imcv.os_info.version</code> []</p>
<dd>Manually set the version of the client OS (e.g. 12.04 i686). </p>
<dt><code>charon.imcv.policy_script</code> [ipsec _imv_policy]</p>
<dd>Script called for each TNC connection to generate IMV policies. </p>
<dt><code>charon.inactivity_close_ike</code> [no]</p>
<dd>Whether to close IKE_SA if the only CHILD_SA closed due to inactivity. </p>
<dt><code>charon.init_limit_half_open</code> [0]</p>
<dd>Limit new connections based on the current number of half open IKE_SAs, see IKE_SA_INIT DROPPING in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.init_limit_job_load</code> [0]</p>
<dd>Limit new connections based on the number of jobs currently queued for processing (see IKE_SA_INIT DROPPING). </p>
<dt><code>charon.initiator_only</code> [no]</p>
<dd>Causes charon daemon to ignore IKE initiation requests. </p>
<dt><code>charon.install_routes</code> [yes]</p>
<dd>Install routes into a separate routing table for established IPsec tunnels. </p>
<dt><code>charon.install_virtual_ip</code> [yes]</p>
<dd>Install virtual IP addresses. </p>
<dt><code>charon.install_virtual_ip_on</code> []</p>
<dd>The name of the interface on which virtual IP addresses should be installed. If not specified the addresses will be installed on the outbound interface. </p>
<dt><code>charon.integrity_test</code> [no]</p>
<dd>Check daemon, libstrongswan and plugin integrity at startup. </p>
<dt><code>charon.interfaces_ignore</code> []</p>
<dd>A comma-separated list of network interfaces that should be ignored, if <code>interfaces_use</code> is specified this option has no effect. </p>
<dt><code>charon.interfaces_use</code> []</p>
<dd>A comma-separated list of network interfaces that should be used by charon. All other interfaces are ignored. </p>
<dt><code>charon.keep_alive</code> [20s]</p>
<dd>NAT keep alive interval. </p>
<dt><code>charon.leak_detective.detailed</code> [yes]</p>
<dd>Includes source file names and line numbers in leak detective output. </p>
<dt><code>charon.leak_detective.usage_threshold</code> [10240]</p>
<dd>Threshold in bytes for leaks to be reported (0 to report all). </p>
<dt><code>charon.leak_detective.usage_threshold_count</code> [0]</p>
<dd>Threshold in number of allocations for leaks to be reported (0 to report all). </p>
<dt><code>charon.load</code> []</p>
<dd>Plugins to load in the IKE daemon charon. </p>
<dt><code>charon.load_modular</code> [no]</p>
<dd>If enabled, the list of plugins to load is determined via the value of the <i>charon.plugins.&lt;name&gt;.load</i> options. In addition to a simple boolean flag that option may take an integer value indicating the priority of a plugin, which would influence the order of a plugin in the plugin list (the default is 1). If two plugins have the same priority their order in the default plugin list is preserved. Enabled plugins not found in that list are ordered alphabetically before other plugins with the same priority. </p>
<dt><code>charon.make_before_break</code> [no]</p>
<dd>Initiate IKEv2 reauthentication with a make-before-break instead of a break-before-make scheme. Make-before-break uses overlapping IKE and CHILD_SA during reauthentication by first recreating all new SAs before deleting the old ones. This behavior can be beneficial to avoid connectivity gaps during reauthentication, but requires support for overlapping SAs by the peer. strongSwan can handle such overlapping SAs since version 5.3.0. </p>
<dt><code>charon.max_ikev1_exchanges</code> [3]</p>
<dd>Maximum number of IKEv1 phase 2 exchanges per IKE_SA to keep state about and track concurrently. </p>
<dt><code>charon.max_packet</code> [10000]</p>
<dd>Maximum packet size accepted by charon. </p>
<dt><code>charon.multiple_authentication</code> [yes]</p>
<dd>Enable multiple authentication exchanges (RFC 4739). </p>
<dt><code>charon.nbns1</code> []</p>
<dd>WINS servers assigned to peer via configuration payload (CP). </p>
<dt><code>charon.nbns2</code> []</p>
<dd>WINS servers assigned to peer via configuration payload (CP). </p>
<dt><code>charon.plugins.addrblock.strict</code> [yes]</p>
<dd>If set to yes, a subject certificate without an addrblock extension is rejected if the issuer certificate has such an addrblock extension. If set to no, subject certificates issued without the addrblock extension are accepted without any traffic selector checks and no policy is enforced by the plugin. </p>
<dt><code>charon.plugins.android_log.loglevel</code> [1]</p>
<dd>Loglevel for logging to Android specific logger. </p>
<dt><code>charon.plugins.attr</code></p>
<dd>Section to specify arbitrary attributes that are assigned to a peer via configuration payload (CP). </p>
<dt><code>charon.plugins.attr.&lt;attr&gt;</code> []</p>
<dd><code>&lt;attr&gt;</code> can be either <i>address</i>, <i>netmask</i>, <i>dns</i>, <i>nbns</i>, <i>dhcp</i>, <i>subnet</i>, <i>split-include</i>, <i>split-exclude</i> or the numeric identifier of the attribute type. The assigned value can be an IPv4/IPv6 address, a subnet in CIDR notation or an arbitrary value depending on the attribute type. For some attribute types multiple values may be specified as a comma separated list. </p>
<dt><code>charon.plugins.attr-sql.crash_recovery</code> [yes]</p>
<dd>Release all online leases during startup. Disable this to share the DB between multiple VPN gateways. </p>
<dt><code>charon.plugins.attr-sql.database</code> []</p>
<dd>Database URI for attr-sql plugin used by charon. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.attr-sql.lease_history</code> [yes]</p>
<dd>Enable logging of SQL IP pool leases. </p>
<dt><code>charon.plugins.bliss.use_bliss_b</code> [yes]</p>
<dd>Use the enhanced BLISS-B key generation and signature algorithm. </p>
<dt><code>charon.plugins.bypass-lan.interfaces_ignore</code> []</p>
<dd>A comma-separated list of network interfaces for which connected subnets should be ignored, if <code>interfaces_use</code> is specified this option has no effect. </p>
<dt><code>charon.plugins.bypass-lan.interfaces_use</code> []</p>
<dd>A comma-separated list of network interfaces for which connected subnets should be considered. All other interfaces are ignored. </p>
<dt><code>charon.plugins.certexpire.csv.cron</code> []</p>
<dd>Cron style string specifying CSV export times. </p>
<dt><code>charon.plugins.certexpire.csv.empty_string</code> []</p>
<dd>String to use in empty intermediate CA fields. </p>
<dt><code>charon.plugins.certexpire.csv.fixed_fields</code> [yes]</p>
<dd>Use a fixed intermediate CA field count. </p>
<dt><code>charon.plugins.certexpire.csv.force</code> [yes]</p>
<dd>Force export of all trustchains we have a private key for. </p>
<dt><code>charon.plugins.certexpire.csv.format</code> [%d:%m:%Y]</p>
<dd><code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) format string to export expiration dates as. </p>
<dt><code>charon.plugins.certexpire.csv.local</code> []</p>
<dd><code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) format string for the CSV file name to export local certificates to. </p>
<dt><code>charon.plugins.certexpire.csv.remote</code> []</p>
<dd><code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) format string for the CSV file name to export remote certificates to. </p>
<dt><code>charon.plugins.certexpire.csv.separator</code> [,]</p>
<dd>CSV field separator. </p>
<dt><code>charon.plugins.coupling.file</code> []</p>
<dd>File to store coupling list to. </p>
<dt><code>charon.plugins.coupling.hash</code> [sha1]</p>
<dd>Hashing algorithm to fingerprint coupled certificates. </p>
<dt><code>charon.plugins.coupling.max</code> [1]</p>
<dd>Maximum number of coupling entries to create. </p>
<dt><code>charon.plugins.dhcp.force_server_address</code> [no]</p>
<dd>Always use the configured server address. This might be helpful if the DHCP server runs on the same host as strongSwan, and the DHCP daemon does not listen on the loopback interface. In that case the server cannot be reached via unicast (or even 255.255.255.255) as that would be routed via loopback. Setting this option to yes and configuring the local broadcast address (e.g. 192.168.0.255) as server address might work. </p>
<dt><code>charon.plugins.dhcp.identity_lease</code> [no]</p>
<dd>Derive user-defined MAC address from hash of IKE identity. </p>
<dt><code>charon.plugins.dhcp.interface</code> []</p>
<dd>Interface name the plugin uses for address allocation. The default is to bind to any (0.0.0.0) and let the system decide which way to route the packets to the DHCP server. </p>
<dt><code>charon.plugins.dhcp.server</code> [255.255.255.255]</p>
<dd>DHCP server unicast or broadcast IP address. </p>
<dt><code>charon.plugins.dnscert.enable</code> [no]</p>
<dd>Enable fetching of CERT RRs via DNS. </p>
<dt><code>charon.plugins.duplicheck.enable</code> [yes]</p>
<dd>Enable duplicheck plugin (if loaded). </p>
<dt><code>charon.plugins.duplicheck.socket</code> [<a href="unix://${piddir}/charon.dck]">unix://${piddir}/charon.dck]</a></p>
<dd>Socket provided by the duplicheck plugin. </p>
<dt><code>charon.plugins.eap-aka.request_identity</code> [yes]</p>
<dd>
<dt><code>charon.plugins.eap-aka-3ggp2.seq_check</code> []</p>
<dd>
<dt><code>charon.plugins.eap-dynamic.prefer_user</code> [no]</p>
<dd>If enabled the EAP methods proposed in an EAP-Nak message sent by the peer are preferred over the methods registered locally. </p>
<dt><code>charon.plugins.eap-dynamic.preferred</code> []</p>
<dd>The preferred EAP method(s) to be used. If it is not given the first registered method will be used initially. If a comma separated list is given the methods are tried in the given order before trying the rest of the registered methods. </p>
<dt><code>charon.plugins.eap-gtc.backend</code> [pam]</p>
<dd>XAuth backend to be used for credential verification. </p>
<dt><code>charon.plugins.eap-peap.fragment_size</code> [1024]</p>
<dd>Maximum size of an EAP-PEAP packet. </p>
<dt><code>charon.plugins.eap-peap.include_length</code> [no]</p>
<dd>Include length in non-fragmented EAP-PEAP packets. </p>
<dt><code>charon.plugins.eap-peap.max_message_count</code> [32]</p>
<dd>Maximum number of processed EAP-PEAP packets (0 = no limit). </p>
<dt><code>charon.plugins.eap-peap.phase2_method</code> [mschapv2]</p>
<dd>Phase2 EAP client authentication method. </p>
<dt><code>charon.plugins.eap-peap.phase2_piggyback</code> [no]</p>
<dd>Phase2 EAP Identity request piggybacked by server onto TLS Finished message. </p>
<dt><code>charon.plugins.eap-peap.phase2_tnc</code> [no]</p>
<dd>Start phase2 EAP TNC protocol after successful client authentication. </p>
<dt><code>charon.plugins.eap-peap.request_peer_auth</code> [no]</p>
<dd>Request peer authentication based on a client certificate. </p>
<dt><code>charon.plugins.eap-radius.accounting</code> [no]</p>
<dd>Send RADIUS accounting information to RADIUS servers. </p>
<dt><code>charon.plugins.eap-radius.accounting_close_on_timeout</code> [yes]</p>
<dd>Close the IKE_SA if there is a timeout during interim RADIUS accounting updates. </p>
<dt><code>charon.plugins.eap-radius.accounting_interval</code> [0]</p>
<dd>Interval in seconds for interim RADIUS accounting updates, if not specified by the RADIUS server in the Access-Accept message. </p>
<dt><code>charon.plugins.eap-radius.accounting_requires_vip</code> [no]</p>
<dd>If enabled, accounting is disabled unless an IKE_SA has at least one virtual IP. Only for IKEv2, for IKEv1 a virtual IP is strictly necessary. </p>
<dt><code>charon.plugins.eap-radius.class_group</code> [no]</p>
<dd>Use the <i>class</i> attribute sent in the RADIUS-Accept message as group membership information that is compared to the groups specified in the <code>rightgroups</code> option in <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5). </p>
<dt><code>charon.plugins.eap-radius.close_all_on_timeout</code> [no]</p>
<dd>Closes all IKE_SAs if communication with the RADIUS server times out. If it is not set only the current IKE_SA is closed. </p>
<dt><code>charon.plugins.eap-radius.dae.enable</code> [no]</p>
<dd>Enables support for the Dynamic Authorization Extension (RFC 5176). </p>
<dt><code>charon.plugins.eap-radius.dae.listen</code> [0.0.0.0]</p>
<dd>Address to listen for DAE messages from the RADIUS server. </p>
<dt><code>charon.plugins.eap-radius.dae.port</code> [3799]</p>
<dd>Port to listen for DAE requests. </p>
<dt><code>charon.plugins.eap-radius.dae.secret</code> []</p>
<dd>Shared secret used to verify/sign DAE messages. If set, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.eap-radius.eap_start</code> [no]</p>
<dd>Send EAP-Start instead of EAP-Identity to start RADIUS conversation. </p>
<dt><code>charon.plugins.eap-radius.filter_id</code> [no]</p>
<dd>If the RADIUS <i>tunnel_type</i> attribute with value <code>ESP</code> is received, use the <i>filter_id</i> attribute sent in the RADIUS-Accept message as group membership information that is compared to the groups specified in the <code>rightgroups</code> option in <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5). </p>
<dt><code>charon.plugins.eap-radius.forward.ike_to_radius</code> []</p>
<dd>RADIUS attributes to be forwarded from IKEv2 to RADIUS (can be defined by name or attribute number, a colon can be used to specify vendor-specific attributes, e.g. Reply-Message, or 11, or 36906:12). </p>
<dt><code>charon.plugins.eap-radius.forward.radius_to_ike</code> []</p>
<dd>Same as <i>charon.plugins.eap-radius.forward.ike_to_radius</i> but from RADIUS to IKEv2, a strongSwan specific private notify (40969) is used to transmit the attributes. </p>
<dt><code>charon.plugins.eap-radius.id_prefix</code> []</p>
<dd>Prefix to EAP-Identity, some AAA servers use a IMSI prefix to select the EAP method. </p>
<dt><code>charon.plugins.eap-radius.nas_identifier</code> [strongSwan]</p>
<dd>NAS-Identifier to include in RADIUS messages. </p>
<dt><code>charon.plugins.eap-radius.port</code> [1812]</p>
<dd>Port of RADIUS server (authentication). </p>
<dt><code>charon.plugins.eap-radius.retransmit_base</code> [1.4]</p>
<dd>Base to use for calculating exponential back off. </p>
<dt><code>charon.plugins.eap-radius.retransmit_timeout</code> [2.0]</p>
<dd>Timeout in seconds before sending first retransmit. </p>
<dt><code>charon.plugins.eap-radius.retransmit_tries</code> [4]</p>
<dd>Number of times to retransmit a packet before giving up. </p>
<dt><code>charon.plugins.eap-radius.secret</code> []</p>
<dd>Shared secret between RADIUS and NAS. If set, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.eap-radius.server</code> []</p>
<dd>IP/Hostname of RADIUS server. </p>
<dt><code>charon.plugins.eap-radius.servers</code></p>
<dd>Section to specify multiple RADIUS servers. The <code>nas_identifier</code>, <code>secret</code>, <code>sockets</code> and <code>port</code> (or <code>auth_port</code>) options can be specified for each server. A server&#8217;s IP/Hostname can be configured using the <code>address</code> option. The <code>acct_port</code> [1813] option can be used to specify the port used for RADIUS accounting. For each RADIUS server a priority can be specified using the <code>preference</code> [0] option. The retransmission time for each server can set set using <code>retransmit_base</code>, <code>retransmit_timeout</code> and <code>retransmit_tries</code>. </p>
<dt><code>charon.plugins.eap-radius.sockets</code> [1]</p>
<dd>Number of sockets (ports) to use, increase for high load. </p>
<dt><code>charon.plugins.eap-radius.xauth</code></p>
<dd>Section to configure multiple XAuth authentication rounds via RADIUS. The subsections define so called authentication profiles with arbitrary names. In each profile section one or more XAuth types can be configured, with an assigned message. For each type a separate XAuth exchange will be initiated and all replies get concatenated into the User-Password attribute, which then gets verified over RADIUS. </p>
<p> Available XAuth types are <code>password</code>, <code>passcode</code>, <code>nextpin</code>, and <code>answer</code>. This type is not relevant to strongSwan or the AAA server, but the client may show a different dialog (along with the configured message). </p>
<p> To use the configured profiles, they have to be configured in the respective connection in <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) by appending the profile name, separated by a colon, to the <code>xauth-radius</code> XAauth backend configuration in <i>rightauth</i> or <i>rightauth2</i>, for instance, <i>rightauth2=xauth-radius:profile</i>. </p>
<dt><code>charon.plugins.eap-sim.request_identity</code> [yes]</p>
<dd>
<dt><code>charon.plugins.eap-simaka-sql.database</code> []</p>
<dd>
<dt><code>charon.plugins.eap-simaka-sql.remove_used</code> [no]</p>
<dd>
<dt><code>charon.plugins.eap-tls.fragment_size</code> [1024]</p>
<dd>Maximum size of an EAP-TLS packet. </p>
<dt><code>charon.plugins.eap-tls.include_length</code> [yes]</p>
<dd>Include length in non-fragmented EAP-TLS packets. </p>
<dt><code>charon.plugins.eap-tls.max_message_count</code> [32]</p>
<dd>Maximum number of processed EAP-TLS packets (0 = no limit). </p>
<dt><code>charon.plugins.eap-tnc.max_message_count</code> [10]</p>
<dd>Maximum number of processed EAP-TNC packets (0 = no limit). </p>
<dt><code>charon.plugins.eap-tnc.protocol</code> [tnccs-2.0]</p>
<dd>IF-TNCCS protocol version to be used (<i>tnccs-1.1</i>, <i>tnccs-2.0</i>, <i>tnccs-dynamic</i>). </p>
<dt><code>charon.plugins.eap-ttls.fragment_size</code> [1024]</p>
<dd>Maximum size of an EAP-TTLS packet. </p>
<dt><code>charon.plugins.eap-ttls.include_length</code> [yes]</p>
<dd>Include length in non-fragmented EAP-TTLS packets. </p>
<dt><code>charon.plugins.eap-ttls.max_message_count</code> [32]</p>
<dd>Maximum number of processed EAP-TTLS packets (0 = no limit). </p>
<dt><code>charon.plugins.eap-ttls.phase2_method</code> [md5]</p>
<dd>Phase2 EAP client authentication method. </p>
<dt><code>charon.plugins.eap-ttls.phase2_piggyback</code> [no]</p>
<dd>Phase2 EAP Identity request piggybacked by server onto TLS Finished message. </p>
<dt><code>charon.plugins.eap-ttls.phase2_tnc</code> [no]</p>
<dd>Start phase2 EAP TNC protocol after successful client authentication. </p>
<dt><code>charon.plugins.eap-ttls.phase2_tnc_method</code> [pt]</p>
<dd>Phase2 EAP TNC transport protocol (<i>pt</i> as IETF standard or legacy <i>tnc</i>) </p>
<dt><code>charon.plugins.eap-ttls.request_peer_auth</code> [no]</p>
<dd>Request peer authentication based on a client certificate. </p>
<dt><code>charon.plugins.error-notify.socket</code> [<a href="unix://${piddir}/charon.enfy]">unix://${piddir}/charon.enfy]</a></p>
<dd>Socket provided by the error-notify plugin. </p>
<dt><code>charon.plugins.ext-auth.script</code> []</p>
<dd>Command to pass to the system shell for peer authorization. Authorization is considered successful if the command executes normally with an exit code of zero. For all other exit codes IKE_SA authorization is rejected. </p>
<p> The following environment variables get passed to the script: <i>IKE_UNIQUE_ID</i>: The IKE_SA numerical unique identifier. <i>IKE_NAME</i>: The peer configuration connection name. <i>IKE_LOCAL_HOST</i>: Local IKE IP address. <i>IKE_REMOTE_HOST</i>: Remote IKE IP address. <i>IKE_LOCAL_ID</i>: Local IKE identity. <i>IKE_REMOTE_ID</i>: Remote IKE identity. <i>IKE_REMOTE_EAP_ID</i>: Remote EAP or XAuth identity, if used. </p>
<dt><code>charon.plugins.forecast.groups</code> [224.0.0.1,224.0.0.22,224.0.0.251,224.0.0.252,239.255.255.250]</p>
<dd>Comma separated list of multicast groups to join locally. The local host receives and forwards packets in the local LAN for joined multicast groups only. Packets matching the list of multicast groups get forwarded to connected clients. The default group includes host multicasts, IGMP, mDNS, LLMNR and SSDP/WS-Discovery, and is usually a good choice for Windows clients. </p>
<dt><code>charon.plugins.forecast.interface</code> []</p>
<dd>Name of the local interface to listen for broadcasts messages to forward. If no interface is configured, the first usable interface is used, which is usually just fine for single-homed hosts. If your host has multiple interfaces, set this option to the local LAN interface you want to forward broadcasts from/to. </p>
<dt><code>charon.plugins.forecast.reinject</code> []</p>
<dd>Comma separated list of CHILD_SA configuration names for which to perform multi/broadcast reinjection. For clients connecting over such a configuration, any multi/broadcast received over the tunnel gets reinjected to all active tunnels. This makes the broadcasts visible to other peers, and for examples allows clients to see others shares. If disabled, multi/broadcast messages received over a tunnel are injected to the local network only, but not to other IPsec clients. </p>
<dt><code>charon.plugins.gcrypt.quick_random</code> [no]</p>
<dd>Use faster random numbers in gcrypt; for testing only, produces weak keys! </p>
<dt><code>charon.plugins.ha.autobalance</code> [0]</p>
<dd>Interval in seconds to automatically balance handled segments between nodes. Set to 0 to disable. </p>
<dt><code>charon.plugins.ha.fifo_interface</code> [yes]</p>
<dd>
<dt><code>charon.plugins.ha.heartbeat_delay</code> [1000]</p>
<dd>
<dt><code>charon.plugins.ha.heartbeat_timeout</code> [2100]</p>
<dd>
<dt><code>charon.plugins.ha.local</code> []</p>
<dd>
<dt><code>charon.plugins.ha.monitor</code> [yes]</p>
<dd>
<dt><code>charon.plugins.ha.pools</code> []</p>
<dd>
<dt><code>charon.plugins.ha.remote</code> []</p>
<dd>
<dt><code>charon.plugins.ha.resync</code> [yes]</p>
<dd>
<dt><code>charon.plugins.ha.secret</code> []</p>
<dd>
<dt><code>charon.plugins.ha.segment_count</code> [1]</p>
<dd>
<dt><code>charon.plugins.ipseckey.enable</code> [no]</p>
<dd>Enable fetching of IPSECKEY RRs via DNS. </p>
<dt><code>charon.plugins.kernel-libipsec.allow_peer_ts</code> [no]</p>
<dd>Allow that the remote traffic selector equals the IKE peer. The route installed for such traffic (via TUN device) usually prevents further IKE traffic. The fwmark options for the <i>kernel-netlink</i> and <i>socket-default</i> plugins can be used to circumvent that problem. </p>
<dt><code>charon.plugins.kernel-netlink.buflen</code> [&lt;min(PAGE_SIZE, 8192)&gt;]</p>
<dd>Buffer size for received Netlink messages. </p>
<dt><code>charon.plugins.kernel-netlink.force_receive_buffer_size</code> [no]</p>
<dd>If the maximum Netlink socket receive buffer in bytes set by <i>receive_buffer_size</i> exceeds the system-wide maximum from /proc/sys/net/core/rmem_max, this option can be used to override the limit. Enabling this option requires special priviliges (CAP_NET_ADMIN). </p>
<dt><code>charon.plugins.kernel-netlink.fwmark</code> []</p>
<dd>Firewall mark to set on the routing rule that directs traffic to our routing table. The format is [!]mark[/mask], where the optional exclamation mark inverts the meaning (i.e. the rule only applies to packets that don&#8217;t match the mark). </p>
<dt><code>charon.plugins.kernel-netlink.ignore_retransmit_errors</code> [no]</p>
<dd>Whether to ignore errors potentially resulting from a retransmission. </p>
<dt><code>charon.plugins.kernel-netlink.mss</code> [0]</p>
<dd>MSS to set on installed routes, 0 to disable. </p>
<dt><code>charon.plugins.kernel-netlink.mtu</code> [0]</p>
<dd>MTU to set on installed routes, 0 to disable. </p>
<dt><code>charon.plugins.kernel-netlink.parallel_route</code> [no]</p>
<dd>Whether to perform concurrent Netlink ROUTE queries on a single socket. While parallel queries can improve throughput, it has more overhead. On vanilla Linux, DUMP queries fail with EBUSY and must be retried, further decreasing performance. </p>
<dt><code>charon.plugins.kernel-netlink.parallel_xfrm</code> [no]</p>
<dd>Whether to perform concurrent Netlink XFRM queries on a single socket. </p>
<dt><code>charon.plugins.kernel-netlink.policy_update</code> [no]</p>
<dd>Whether to always use XFRM_MSG_UPDPOLICY to install policies. </p>
<dt><code>charon.plugins.kernel-netlink.port_bypass</code> [no]</p>
<dd>Whether to use port or socket based IKE XFRM bypass policies. IKE bypass policies are used to exempt IKE traffic from XFRM processing. The default socket based policies are directly tied to the IKE UDP sockets, port based policies use global XFRM bypass policies for the used IKE UDP ports. </p>
<dt><code>charon.plugins.kernel-netlink.receive_buffer_size</code> [0]</p>
<dd>Maximum Netlink socket receive buffer in bytes. This value controls how many bytes of Netlink messages can be received on a Netlink socket. The default value is set by /proc/sys/net/core/rmem_default. The specified value cannot exceed the system-wide maximum from /proc/sys/net/core/rmem_max, unless <i>force_receive_buffer_size</i> is enabled. </p>
<dt><code>charon.plugins.kernel-netlink.retries</code> [0]</p>
<dd>Number of Netlink message retransmissions to send on timeout. </p>
<dt><code>charon.plugins.kernel-netlink.roam_events</code> [yes]</p>
<dd>Whether to trigger roam events when interfaces, addresses or routes change. </p>
<dt><code>charon.plugins.kernel-netlink.set_proto_port_transport_sa</code> [no]</p>
<dd>Whether to set protocol and ports in the selector installed on transport mode IPsec SAs in the kernel. While doing so enforces policies for inbound traffic, it also prevents the use of a single IPsec SA by more than one traffic selector. </p>
<dt><code>charon.plugins.kernel-netlink.spdh_thresh</code></p>
<dd>XFRM policy hashing threshold configuration for IPv4 and IPv6. </p>
<p> The section defines hashing thresholds to configure in the kernel during daemon startup. Each address family takes a threshold for the local subnet of an IPsec policy (src in out-policies, dst in in- and forward-policies) and the remote subnet (dst in out-policies, src in in- and forward-policies). </p>
<p> If the subnet has more or equal net bits than the threshold, the first threshold bits are used to calculate a hash to lookup the policy. </p>
<p> Policy hashing thresholds are not supported before Linux 3.18 and might conflict with socket policies before Linux 4.8. </p>
<dt><code>charon.plugins.kernel-netlink.spdh_thresh.ipv4.lbits</code> [32]</p>
<dd>Local subnet XFRM policy hashing threshold for IPv4. </p>
<dt><code>charon.plugins.kernel-netlink.spdh_thresh.ipv4.rbits</code> [32]</p>
<dd>Remote subnet XFRM policy hashing threshold for IPv4. </p>
<dt><code>charon.plugins.kernel-netlink.spdh_thresh.ipv6.lbits</code> [128]</p>
<dd>Local subnet XFRM policy hashing threshold for IPv6. </p>
<dt><code>charon.plugins.kernel-netlink.spdh_thresh.ipv6.rbits</code> [128]</p>
<dd>Remote subnet XFRM policy hashing threshold for IPv6. </p>
<dt><code>charon.plugins.kernel-netlink.timeout</code> [0]</p>
<dd>Netlink message retransmission timeout, 0 to disable retransmissions. </p>
<dt><code>charon.plugins.kernel-netlink.xfrm_acq_expires</code> [165]</p>
<dd>Lifetime of XFRM acquire state created by the kernel when traffic matches a trap policy. The value gets written to /proc/sys/net/core/xfrm_acq_expires. Indirectly controls the delay between XFRM acquire messages triggered by the kernel for a trap policy. The same value is used as timeout for SPIs allocated by the kernel. The default value equals the total retransmission timeout for IKE messages, see IKEv2 RETRANSMISSION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.plugins.kernel-pfkey.events_buffer_size</code> [0]</p>
<dd>Size of the receive buffer for the event socket (0 for default size). Because events are received asynchronously installing e.g. lots of policies may require a larger buffer than the default on certain platforms in order to receive all messages. </p>
<dt><code>charon.plugins.kernel-pfroute.vip_wait</code> [1000]</p>
<dd>Time in ms to wait until virtual IP addresses appear/disappear before failing. </p>
<dt><code>charon.plugins.led.activity_led</code> []</p>
<dd>
<dt><code>charon.plugins.led.blink_time</code> [50]</p>
<dd>
<dt><code>charon.plugins.load-tester</code></p>
<dd>Section to configure the load-tester plugin, see LOAD TESTS in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5) for details. </p>
<dt><code>charon.plugins.load-tester.addrs</code></p>
<dd>Section that contains key/value pairs with address pools (in CIDR notation) to use for a specific network interface e.g. eth0 = 10.10.0.0/16. </p>
<dt><code>charon.plugins.load-tester.addrs_keep</code> [no]</p>
<dd>Whether to keep dynamic addresses even after the associated SA got terminated. </p>
<dt><code>charon.plugins.load-tester.addrs_prefix</code> [16]</p>
<dd>Network prefix length to use when installing dynamic addresses. If set to -1 the full address is used (i.e. 32 or 128). </p>
<dt><code>charon.plugins.load-tester.ca_dir</code> []</p>
<dd>Directory to load (intermediate) CA certificates from. </p>
<dt><code>charon.plugins.load-tester.child_rekey</code> [600]</p>
<dd>Seconds to start CHILD_SA rekeying after setup. </p>
<dt><code>charon.plugins.load-tester.crl</code> []</p>
<dd>URI to a CRL to include as certificate distribution point in generated certificates. </p>
<dt><code>charon.plugins.load-tester.delay</code> [0]</p>
<dd>Delay between initiatons for each thread. </p>
<dt><code>charon.plugins.load-tester.delete_after_established</code> [no]</p>
<dd>Delete an IKE_SA as soon as it has been established. </p>
<dt><code>charon.plugins.load-tester.digest</code> [sha1]</p>
<dd>Digest algorithm used when issuing certificates. </p>
<dt><code>charon.plugins.load-tester.dpd_delay</code> [0]</p>
<dd>DPD delay to use in load test. </p>
<dt><code>charon.plugins.load-tester.dynamic_port</code> [0]</p>
<dd>Base port to be used for requests (each client uses a different port). </p>
<dt><code>charon.plugins.load-tester.eap_password</code> [default-pwd]</p>
<dd>EAP secret to use in load test. </p>
<dt><code>charon.plugins.load-tester.enable</code> [no]</p>
<dd>Enable the load testing plugin. <code>WARNING</code>: Never enable this plugin on productive systems. It provides preconfigured credentials and allows an attacker to authenticate as any user. </p>
<dt><code>charon.plugins.load-tester.esp</code> [aes128-sha1]</p>
<dd>CHILD_SA proposal to use for load tests. </p>
<dt><code>charon.plugins.load-tester.fake_kernel</code> [no]</p>
<dd>Fake the kernel interface to allow load-testing against self. </p>
<dt><code>charon.plugins.load-tester.ike_rekey</code> [0]</p>
<dd>Seconds to start IKE_SA rekeying after setup. </p>
<dt><code>charon.plugins.load-tester.init_limit</code> [0]</p>
<dd>Global limit of concurrently established SAs during load test. </p>
<dt><code>charon.plugins.load-tester.initiator</code> [0.0.0.0]</p>
<dd>Address to initiate from. </p>
<dt><code>charon.plugins.load-tester.initiator_auth</code> [pubkey]</p>
<dd>Authentication method(s) the intiator uses. </p>
<dt><code>charon.plugins.load-tester.initiator_id</code> []</p>
<dd>Initiator ID used in load test. </p>
<dt><code>charon.plugins.load-tester.initiator_match</code> []</p>
<dd>Initiator ID to match against as responder. </p>
<dt><code>charon.plugins.load-tester.initiator_tsi</code> []</p>
<dd>Traffic selector on initiator side, as proposed by initiator. </p>
<dt><code>charon.plugins.load-tester.initiator_tsr</code> []</p>
<dd>Traffic selector on responder side, as proposed by initiator. </p>
<dt><code>charon.plugins.load-tester.initiators</code> [0]</p>
<dd>Number of concurrent initiator threads to use in load test. </p>
<dt><code>charon.plugins.load-tester.issuer_cert</code> []</p>
<dd>Path to the issuer certificate (if not configured a hard-coded default value is used). </p>
<dt><code>charon.plugins.load-tester.issuer_key</code> []</p>
<dd>Path to private key that is used to issue certificates (if not configured a hard-coded default value is used). </p>
<dt><code>charon.plugins.load-tester.iterations</code> [1]</p>
<dd>Number of IKE_SAs to initiate by each initiator in load test. </p>
<dt><code>charon.plugins.load-tester.mode</code> [tunnel]</p>
<dd>IPsec mode to use, one of <i>tunnel</i>, <i>transport</i>, or <i>beet</i>. </p>
<dt><code>charon.plugins.load-tester.pool</code> []</p>
<dd>Provide INTERNAL_IPV4_ADDRs from a named pool. </p>
<dt><code>charon.plugins.load-tester.preshared_key</code> [&lt;default-psk&gt;]</p>
<dd>Preshared key to use in load test. </p>
<dt><code>charon.plugins.load-tester.proposal</code> [aes128-sha1-modp768]</p>
<dd>IKE proposal to use in load test. </p>
<dt><code>charon.plugins.load-tester.request_virtual_ip</code> [no]</p>
<dd>Request an INTERNAL_IPV4_ADDR from the server. </p>
<dt><code>charon.plugins.load-tester.responder</code> [127.0.0.1]</p>
<dd>Address to initiation connections to. </p>
<dt><code>charon.plugins.load-tester.responder_auth</code> [pubkey]</p>
<dd>Authentication method(s) the responder uses. </p>
<dt><code>charon.plugins.load-tester.responder_id</code> []</p>
<dd>Responder ID used in load test. </p>
<dt><code>charon.plugins.load-tester.responder_tsi</code> [initiator_tsi]</p>
<dd>Traffic selector on initiator side, as narrowed by responder. </p>
<dt><code>charon.plugins.load-tester.responder_tsr</code> [initiator_tsr]</p>
<dd>Traffic selector on responder side, as narrowed by responder. </p>
<dt><code>charon.plugins.load-tester.shutdown_when_complete</code> [no]</p>
<dd>Shutdown the daemon after all IKE_SAs have been established. </p>
<dt><code>charon.plugins.load-tester.socket</code> [<a href="unix://${piddir}/charon.ldt]">unix://${piddir}/charon.ldt]</a></p>
<dd>Socket provided by the load-tester plugin. </p>
<dt><code>charon.plugins.load-tester.version</code> [0]</p>
<dd>IKE version to use (0 means use IKEv2 as initiator and accept any version as responder). </p>
<dt><code>charon.plugins.lookip.socket</code> [<a href="unix://${piddir}/charon.lkp]">unix://${piddir}/charon.lkp]</a></p>
<dd>Socket provided by the lookip plugin. </p>
<dt><code>charon.plugins.ntru.max_drbg_requests</code> [4294967294]</p>
<dd>Number of pseudo-random bit requests from the DRBG before an automatic reseeding occurs. </p>
<dt><code>charon.plugins.ntru.parameter_set</code> [optimum]</p>
<dd>The following parameter sets are available: <code>x9_98_speed</code>, <code>x9_98_bandwidth</code>, <code>x9_98_balance</code> and <code>optimum</code>, the last set not being part of the X9.98 standard but having the best performance. </p>
<dt><code>charon.plugins.openssl.engine_id</code> [pkcs11]</p>
<dd>ENGINE ID to use in the OpenSSL plugin. </p>
<dt><code>charon.plugins.openssl.fips_mode</code> [0]</p>
<dd>Set OpenSSL FIPS mode: disabled(0), <a href="/docs/linux/man/1-enabled/">enabled</a>(1), Suite B <a href="/docs/linux/man/2-enabled/">enabled</a>(2). </p>
<dt><code>charon.plugins.osx-attr.append</code> [yes]</p>
<dd>Whether DNS servers are appended to existing entries, instead of replacing them. </p>
<dt><code>charon.plugins.p-cscf.enable</code></p>
<dd>Section to enable requesting P-CSCF server addresses for individual connections. </p>
<dt><code>charon.plugins.p-cscf.enable.&lt;conn&gt;</code> [no]</p>
<dd>&lt;conn&gt; is the name of a connection with an ePDG from which to request P-CSCF server addresses. Requests will be sent for addresses of the same families for which internal IPs are requested. </p>
<dt><code>charon.plugins.pkcs11.modules</code></p>
<dd>List of available PKCS#11 modules. </p>
<dt><code>charon.plugins.pkcs11.modules.&lt;name&gt;.load_certs</code> [yes]</p>
<dd>Whether to automatically load certificates from tokens. </p>
<dt><code>charon.plugins.pkcs11.modules.&lt;name&gt;.os_locking</code> [no]</p>
<dd>Whether OS locking should be enabled for this module. </p>
<dt><code>charon.plugins.pkcs11.modules.&lt;name&gt;.path</code> []</p>
<dd>Full path to the shared object file of this PKCS#11 module. </p>
<dt><code>charon.plugins.pkcs11.reload_certs</code> [no]</p>
<dd>Reload certificates from all tokens if charon receives a SIGHUP. </p>
<dt><code>charon.plugins.pkcs11.use_dh</code> [no]</p>
<dd>Whether the PKCS#11 modules should be used for DH and ECDH (see <i>use_ecc</i> option). </p>
<dt><code>charon.plugins.pkcs11.use_ecc</code> [no]</p>
<dd>Whether the PKCS#11 modules should be used for ECDH and ECDSA public key operations. ECDSA private keys can be used regardless of this option. </p>
<dt><code>charon.plugins.pkcs11.use_hasher</code> [no]</p>
<dd>Whether the PKCS#11 modules should be used to hash data. </p>
<dt><code>charon.plugins.pkcs11.use_pubkey</code> [no]</p>
<dd>Whether the PKCS#11 modules should be used for public key operations, even for keys not stored on tokens. </p>
<dt><code>charon.plugins.pkcs11.use_rng</code> [no]</p>
<dd>Whether the PKCS#11 modules should be used as RNG. </p>
<dt><code>charon.plugins.radattr.dir</code> []</p>
<dd>Directory where RADIUS attributes are stored in client-ID specific files. </p>
<dt><code>charon.plugins.radattr.message_id</code> [-1]</p>
<dd>Attributes are added to all IKE_AUTH messages by default (-1), or only to the IKE_AUTH message with the given IKEv2 message ID. </p>
<dt><code>charon.plugins.random.random</code> [${random_device}]</p>
<dd>File to read random bytes from. </p>
<dt><code>charon.plugins.random.strong_equals_true</code> [no]</p>
<dd>If set to yes the RNG_STRONG class reads random bytes from the same source as the RNG_TRUE class. </p>
<dt><code>charon.plugins.random.urandom</code> [${urandom_device}]</p>
<dd>File to read pseudo random bytes from. </p>
<dt><code>charon.plugins.resolve.file</code> [/etc/resolv.conf]</p>
<dd>File where to add DNS server entries. </p>
<dt><code>charon.plugins.resolve.resolvconf.iface_prefix</code> [lo.inet.ipsec.]</p>
<dd>Prefix used for interface names sent to <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8). The nameserver address is appended to this prefix to make it unique. The result has to be a valid interface name according to the rules defined by resolvconf. Also, it should have a high priority according to the order defined in <code><a href="/docs/linux/man/5-interface-order/">interface-order</a></code>(5). </p>
<dt><code>charon.plugins.revocation.enable_crl</code> [yes]</p>
<dd>Whether CRL validation should be enabled. </p>
<dt><code>charon.plugins.revocation.enable_ocsp</code> [yes]</p>
<dd>Whether OCSP validation should be enabled. </p>
<dt><code>charon.plugins.socket-default.fwmark</code> []</p>
<dd>Firewall mark to set on outbound packets. </p>
<dt><code>charon.plugins.socket-default.set_source</code> [yes]</p>
<dd>Set source address on outbound packets, if possible. </p>
<dt><code>charon.plugins.socket-default.set_sourceif</code> [no]</p>
<dd>Force sending interface on outbound packets, if possible. This allows using IPv6 link-local addresses as tunnel endpoints. </p>
<dt><code>charon.plugins.socket-default.use_ipv4</code> [yes]</p>
<dd>Listen on IPv4, if possible. </p>
<dt><code>charon.plugins.socket-default.use_ipv6</code> [yes]</p>
<dd>Listen on IPv6, if possible. </p>
<dt><code>charon.plugins.sql.database</code> []</p>
<dd>Database URI for charon&#8217;s SQL plugin. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.sql.loglevel</code> [-1]</p>
<dd>Loglevel for logging to SQL database. </p>
<dt><code>charon.plugins.stroke.allow_swap</code> [yes]</p>
<dd>Analyze addresses/hostnames in <i>left|right</i> to detect which side is local and swap configuration options if necessary. If disabled <i>left</i> is always <i>local</i>. </p>
<dt><code>charon.plugins.stroke.ignore_missing_ca_basic_constraint</code> [no]</p>
<dd>Treat certificates in ipsec.d/cacerts and ipsec.conf ca sections as CA certificates even if they don&#8217;t contain a CA basic constraint. </p>
<dt><code>charon.plugins.stroke.max_concurrent</code> [4]</p>
<dd>Maximum number of stroke messages handled concurrently. </p>
<dt><code>charon.plugins.stroke.prevent_loglevel_changes</code> [no]</p>
<dd>If enabled log level changes via stroke socket are not allowed. </p>
<dt><code>charon.plugins.stroke.secrets_file</code> [${sysconfdir}/ipsec.secrets]</p>
<dd>Location of the ipsec.secrets file </p>
<dt><code>charon.plugins.stroke.socket</code> [<a href="unix://${piddir}/charon.ctl]">unix://${piddir}/charon.ctl]</a></p>
<dd>Socket provided by the stroke plugin. </p>
<dt><code>charon.plugins.stroke.timeout</code> [0]</p>
<dd>Timeout in ms for any stroke command. Use 0 to disable the timeout. </p>
<dt><code>charon.plugins.systime-fix.interval</code> [0]</p>
<dd>Interval in seconds to check system time for validity. 0 disables the check. </p>
<dt><code>charon.plugins.systime-fix.reauth</code> [no]</p>
<dd>Whether to use reauth or delete if an invalid cert lifetime is detected. </p>
<dt><code>charon.plugins.systime-fix.threshold</code> []</p>
<dd>Threshold date where system time is considered valid. Disabled if not specified. </p>
<dt><code>charon.plugins.systime-fix.threshold_format</code> [%Y]</p>
<dd><code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3) format used to parse threshold option. </p>
<dt><code>charon.plugins.tnc-ifmap.client_cert</code> []</p>
<dd>Path to X.509 certificate file of IF-MAP client. </p>
<dt><code>charon.plugins.tnc-ifmap.client_key</code> []</p>
<dd>Path to private key file of IF-MAP client. </p>
<dt><code>charon.plugins.tnc-ifmap.device_name</code> []</p>
<dd>Unique name of strongSwan server as a PEP and/or PDP device. </p>
<dt><code>charon.plugins.tnc-ifmap.renew_session_interval</code> [150]</p>
<dd>Interval in seconds between periodic IF-MAP RenewSession requests. </p>
<dt><code>charon.plugins.tnc-ifmap.server_cert</code> []</p>
<dd>Path to X.509 certificate file of IF-MAP server. </p>
<dt><code>charon.plugins.tnc-ifmap.server_uri</code> [<a rel="nofollow" href="https://localhost:8444/imap]">https://localhost:8444/imap]</a></p>
<dd>URI of the form [<a rel="nofollow" href="https://]servername[:port][/path].">https://]servername[:port][/path].</a> </p>
<dt><code>charon.plugins.tnc-ifmap.username_password</code> []</p>
<dd>Credentials of IF-MAP client of the form username:password. If set, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.tnc-imc.dlclose</code> [yes]</p>
<dd>Unload IMC after use. </p>
<dt><code>charon.plugins.tnc-imc.preferred_language</code> [en]</p>
<dd>Preferred language for TNC recommendations. </p>
<dt><code>charon.plugins.tnc-imv.dlclose</code> [yes]</p>
<dd>Unload IMV after use. </p>
<dt><code>charon.plugins.tnc-imv.recommendation_policy</code> [default]</p>
<dd>TNC recommendation policy, one of <i>default</i>, <i>any</i>, or <i>all</i>. </p>
<dt><code>charon.plugins.tnc-pdp.pt_tls.enable</code> [yes]</p>
<dd>Enable PT-TLS protocol on the strongSwan PDP. </p>
<dt><code>charon.plugins.tnc-pdp.pt_tls.port</code> [271]</p>
<dd>PT-TLS server port the strongSwan PDP is listening on. </p>
<dt><code>charon.plugins.tnc-pdp.radius.enable</code> [yes]</p>
<dd>Enable RADIUS protocol on the strongSwan PDP. </p>
<dt><code>charon.plugins.tnc-pdp.radius.method</code> [ttls]</p>
<dd>EAP tunnel method to be used. </p>
<dt><code>charon.plugins.tnc-pdp.radius.port</code> [1812]</p>
<dd>RADIUS server port the strongSwan PDP is listening on. </p>
<dt><code>charon.plugins.tnc-pdp.radius.secret</code> []</p>
<dd>Shared RADIUS secret between strongSwan PDP and NAS. If set, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>charon.plugins.tnc-pdp.server</code> []</p>
<dd>Name of the strongSwan PDP as contained in the AAA certificate. </p>
<dt><code>charon.plugins.tnc-pdp.timeout</code> []</p>
<dd>Timeout in seconds before closing incomplete connections. </p>
<dt><code>charon.plugins.tnccs-11.max_message_size</code> [45000]</p>
<dd>Maximum size of a PA-TNC message (XML &amp; Base64 encoding). </p>
<dt><code>charon.plugins.tnccs-20.max_batch_size</code> [65522]</p>
<dd>Maximum size of a PB-TNC batch (upper limit via PT-EAP = 65529). </p>
<dt><code>charon.plugins.tnccs-20.max_message_size</code> [65490]</p>
<dd>Maximum size of a PA-TNC message (upper limit via PT-EAP = 65497). </p>
<dt><code>charon.plugins.tnccs-20.mutual</code> [no]</p>
<dd>Enable PB-TNC mutual protocol. </p>
<dt><code>charon.plugins.tnccs-20.tests.pb_tnc_noskip</code> [no]</p>
<dd>Send an unsupported PB-TNC message type with the NOSKIP flag set. </p>
<dt><code>charon.plugins.tnccs-20.tests.pb_tnc_version</code> [2]</p>
<dd>Send a PB-TNC batch with a modified PB-TNC version. </p>
<dt><code>charon.plugins.tpm.use_rng</code> [no]</p>
<dd>Whether the TPM should be used as RNG. </p>
<dt><code>charon.plugins.unbound.dlv_anchors</code> []</p>
<dd>File to read trusted keys for DLV (DNSSEC Lookaside Validation) from. It uses the same format as <i>trust_anchors</i>. Only one DLV can be configured, which is then used as a root trusted DLV, this means that it is a lookaside for the root. </p>
<dt><code>charon.plugins.unbound.resolv_conf</code> [/etc/resolv.conf]</p>
<dd>File to read DNS resolver configuration from. </p>
<dt><code>charon.plugins.unbound.trust_anchors</code> [/etc/ipsec.d/dnssec.keys]</p>
<dd>File to read DNSSEC trust anchors from (usually root zone KSK). The format of the file is the standard DNS Zone file format, anchors can be stored as DS or DNSKEY entries in the file. </p>
<dt><code>charon.plugins.updown.dns_handler</code> [no]</p>
<dd>Whether the updown script should handle DNS servers assigned via IKEv1 Mode Config or IKEv2 Config Payloads (if enabled they can&#8217;t be handled by other plugins, like resolve) </p>
<dt><code>charon.plugins.vici.socket</code> [<a href="unix://${piddir}/charon.vici]">unix://${piddir}/charon.vici]</a></p>
<dd>Socket the vici plugin serves clients. </p>
<dt><code>charon.plugins.whitelist.enable</code> [yes]</p>
<dd>Enable loaded whitelist plugin. </p>
<dt><code>charon.plugins.whitelist.socket</code> [<a href="unix://${piddir}/charon.wlst]">unix://${piddir}/charon.wlst]</a></p>
<dd>Socket provided by the whitelist plugin. </p>
<dt><code>charon.plugins.xauth-eap.backend</code> [radius]</p>
<dd>EAP plugin to be used as backend for XAuth credential verification. </p>
<dt><code>charon.plugins.xauth-pam.pam_service</code> [login]</p>
<dd>PAM service to be used for authentication. </p>
<dt><code>charon.plugins.xauth-pam.session</code> [no]</p>
<dd>Open/close a PAM session for each active IKE_SA. </p>
<dt><code>charon.plugins.xauth-pam.trim_email</code> [yes]</p>
<dd>If an email address is received as an XAuth username, trim it to just the username part. </p>
<dt><code>charon.port</code> [500]</p>
<dd>UDP port used locally. If set to 0 a random port will be allocated. </p>
<dt><code>charon.port_nat_t</code> [4500]</p>
<dd>UDP port used locally in case of NAT-T. If set to 0 a random port will be allocated. Has to be different from <code>charon.port</code>, otherwise a random port will be allocated. </p>
<dt><code>charon.prefer_best_path</code> [no]</p>
<dd>By default, charon keeps SAs on the routing path with addresses it previously used if that path is still usable. By setting this option to yes, it tries more aggressively to update SAs with MOBIKE on routing priority changes using the cheapest path. This adds more noise, but allows to dynamically adapt SAs to routing priority changes. This option has no effect if MOBIKE is not supported or disabled. </p>
<dt><code>charon.prefer_configured_proposals</code> [yes]</p>
<dd>Prefer locally configured proposals for IKE/IPsec over supplied ones as responder (disabling this can avoid keying retries due to INVALID_KE_PAYLOAD notifies). </p>
<dt><code>charon.prefer_temporary_addrs</code> [no]</p>
<dd>By default public IPv6 addresses are preferred over temporary ones (RFC 4941), to make connections more stable. Enable this option to reverse this. </p>
<dt><code>charon.process_route</code> [yes]</p>
<dd>Process RTM_NEWROUTE and RTM_DELROUTE events. </p>
<dt><code>charon.processor.priority_threads</code></p>
<dd>Section to configure the number of reserved threads per priority class see JOB PRIORITY MANAGEMENT in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.receive_delay</code> [0]</p>
<dd>Delay in ms for receiving packets, to simulate larger RTT. </p>
<dt><code>charon.receive_delay_request</code> [yes]</p>
<dd>Delay request messages. </p>
<dt><code>charon.receive_delay_response</code> [yes]</p>
<dd>Delay response messages. </p>
<dt><code>charon.receive_delay_type</code> [0]</p>
<dd>Specific IKEv2 message type to delay, 0 for any. </p>
<dt><code>charon.replay_window</code> [32]</p>
<dd>Size of the AH/ESP replay window, in packets. </p>
<dt><code>charon.retransmit_base</code> [1.8]</p>
<dd>Base to use for calculating exponential back off, see IKEv2 RETRANSMISSION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.retransmit_jitter</code> [0]</p>
<dd>Maximum jitter in percent to apply randomly to calculated retransmission timeout (0 to disable). </p>
<dt><code>charon.retransmit_limit</code> [0]</p>
<dd>Upper limit in seconds for calculated retransmission timeout (0 to disable). </p>
<dt><code>charon.retransmit_timeout</code> [4.0]</p>
<dd>Timeout in seconds before sending first retransmit. </p>
<dt><code>charon.retransmit_tries</code> [5]</p>
<dd>Number of times to retransmit a packet before giving up. </p>
<dt><code>charon.retry_initiate_interval</code> [0]</p>
<dd>Interval in seconds to use when retrying to initiate an IKE_SA (e.g. if DNS resolution failed), 0 to disable retries. </p>
<dt><code>charon.reuse_ikesa</code> [yes]</p>
<dd>Initiate CHILD_SA within existing IKE_SAs (always enabled for IKEv1). </p>
<dt><code>charon.routing_table</code> []</p>
<dd>Numerical routing table to install routes to. </p>
<dt><code>charon.routing_table_prio</code> []</p>
<dd>Priority of the routing table. </p>
<dt><code>charon.send_delay</code> [0]</p>
<dd>Delay in ms for sending packets, to simulate larger RTT. </p>
<dt><code>charon.send_delay_request</code> [yes]</p>
<dd>Delay request messages. </p>
<dt><code>charon.send_delay_response</code> [yes]</p>
<dd>Delay response messages. </p>
<dt><code>charon.send_delay_type</code> [0]</p>
<dd>Specific IKEv2 message type to delay, 0 for any. </p>
<dt><code>charon.send_vendor_id</code> [no]</p>
<dd>Send strongSwan vendor ID payload </p>
<dt><code>charon.signature_authentication</code> [yes]</p>
<dd>Whether to enable Signature Authentication as per RFC 7427. </p>
<dt><code>charon.signature_authentication_constraints</code> [yes]</p>
<dd>If enabled, signature schemes configured in <i>rightauth</i>, in addition to getting used as constraints against signature schemes employed in the certificate chain, are also used as constraints against the signature scheme used by peers during IKEv2. </p>
<dt><code>charon.spi_max</code> [0xcfffffff]</p>
<dd>The upper limit for SPIs requested from the kernel for IPsec SAs. </p>
<dt><code>charon.spi_min</code> [0xc0000000]</p>
<dd>The lower limit for SPIs requested from the kernel for IPsec SAs. Should not be set lower than 0x00000100 (256), as SPIs between 1 and 255 are reserved by IANA. </p>
<dt><code>charon.start-scripts</code></p>
<dd>Section containing a list of scripts (name = path) that are executed when the daemon is started. </p>
<dt><code>charon.stop-scripts</code></p>
<dd>Section containing a list of scripts (name = path) that are executed when the daemon is terminated. </p>
<dt><code>charon.syslog</code></p>
<dd>Section to define syslog loggers, see LOGGER CONFIGURATION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.syslog.&lt;facility&gt;</code></p>
<dd>&lt;facility&gt; is one of the supported syslog facilities, see LOGGER CONFIGURATION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon.syslog.&lt;facility&gt;.&lt;subsystem&gt;</code> [&lt;default&gt;]</p>
<dd>Loglevel for a specific subsystem. </p>
<dt><code>charon.syslog.&lt;facility&gt;.default</code> [1]</p>
<dd>Specifies the default loglevel to be used for subsystems for which no specific loglevel is defined. </p>
<dt><code>charon.syslog.&lt;facility&gt;.ike_name</code> [no]</p>
<dd>Prefix each log entry with the connection name and a unique numerical identifier for each IKE_SA. </p>
<dt><code>charon.syslog.identifier</code> []</p>
<dd>Global identifier used for an <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3) call, prepended to each log message by syslog. If not configured, <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3) is not called, so the value will depend on system defaults (often the program name). </p>
<dt><code>charon.threads</code> [16]</p>
<dd>Number of worker threads in charon. Several of these are reserved for long running tasks in internal modules and plugins. Therefore, make sure you don&#8217;t set this value too low. The number of idle worker threads listed in <i>ipsec statusall</i> might be used as indicator on the number of reserved threads. </p>
<dt><code>charon.tls.cipher</code> []</p>
<dd>List of TLS encryption ciphers. </p>
<dt><code>charon.tls.key_exchange</code> []</p>
<dd>List of TLS key exchange methods. </p>
<dt><code>charon.tls.mac</code> []</p>
<dd>List of TLS MAC algorithms. </p>
<dt><code>charon.tls.suites</code> []</p>
<dd>List of TLS cipher suites. </p>
<dt><code>charon.tnc.tnc_config</code> [/etc/tnc_config]</p>
<dd>TNC IMC/IMV configuration file. </p>
<dt><code>charon.user</code> []</p>
<dd>Name of the user the daemon changes to after startup. </p>
<dt><code>charon.x509.enforce_critical</code> [yes]</p>
<dd>Discard certificates with unsupported or unknown critical extensions. </p>
<dt><code>charon-nm.ca_dir</code> [&lt;default&gt;]</p>
<dd>Directory from which to load CA certificates if no certificate is configured. </p>
<dt><code>charon-systemd.journal</code></p>
<dd>Section to configure native systemd journal logger, very similar to the syslog logger as described in LOGGER CONFIGURATION in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>charon-systemd.journal.&lt;subsystem&gt;</code> [&lt;default&gt;]</p>
<dd>Loglevel for a specific subsystem. </p>
<dt><code>charon-systemd.journal.default</code> [1]</p>
<dd>Specifies the default loglevel to be used for subsystems for which no specific loglevel is defined. </p>
<dt><code>imv_policy_manager.command_allow</code> []</p>
<dd>Shell command to be executed with recommendation allow. </p>
<dt><code>imv_policy_manager.command_block</code> []</p>
<dd>Shell command to be executed with all other recommendations. </p>
<dt><code>imv_policy_manager.database</code> []</p>
<dd>Database URI for the database that stores the package information. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>imv_policy_manager.load</code> [sqlite]</p>
<dd>Plugins to load in IMV policy manager. </p>
<dt><code>libimcv.debug_level</code> [1]</p>
<dd>Debug level for a stand-alone <i>libimcv</i> library. </p>
<dt><code>libimcv.load</code> [random nonce gmp pubkey x509]</p>
<dd>Plugins to load in IMC/IMVs with stand-alone <i>libimcv</i> library. </p>
<dt><code>libimcv.plugins.imc-attestation.aik_blob</code> []</p>
<dd>AIK encrypted private key blob file. </p>
<dt><code>libimcv.plugins.imc-attestation.aik_cert</code> []</p>
<dd>AIK certificate file. </p>
<dt><code>libimcv.plugins.imc-attestation.aik_handle</code> []</p>
<dd>AIK object handle. </p>
<dt><code>libimcv.plugins.imc-attestation.aik_pubkey</code> []</p>
<dd>AIK public key file. </p>
<dt><code>libimcv.plugins.imc-attestation.mandatory_dh_groups</code> [yes]</p>
<dd>Enforce mandatory Diffie-Hellman groups. </p>
<dt><code>libimcv.plugins.imc-attestation.nonce_len</code> [20]</p>
<dd>DH nonce length. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr17_after</code> []</p>
<dd>PCR17 value after measurement. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr17_before</code> []</p>
<dd>PCR17 value before measurement. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr17_meas</code> []</p>
<dd>Dummy measurement value extended into PCR17 if the TBOOT log is not available. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr18_after</code> []</p>
<dd>PCR18 value after measurement. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr18_before</code> []</p>
<dd>PCR18 value before measurement. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr18_meas</code> []</p>
<dd>Dummy measurement value extended into PCR17 if the TBOOT log is not available. </p>
<dt><code>libimcv.plugins.imc-attestation.pcr_info</code> [no]</p>
<dd>Whether to send pcr_before and pcr_after info. </p>
<dt><code>libimcv.plugins.imc-attestation.use_quote2</code> [yes]</p>
<dd>Use Quote2 AIK signature instead of Quote signature. </p>
<dt><code>libimcv.plugins.imc-attestation.use_version_info</code> [no]</p>
<dd>Version Info is included in Quote2 signature. </p>
<dt><code>libimcv.plugins.imc-hcd.push_info</code> [yes]</p>
<dd>Send quadruple info without being prompted. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes</code> []</p>
<dd>Section to define PWG HCD PA subtypes. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;</code> []</p>
<dd>Defines a PWG HCD PA subtype section. Recognized subtype section names are <i>system</i>, <i>control</i>, <i>marker</i>, <i>finisher</i>, <i>interface</i> and <i>scanner</i>. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;</code> []</p>
<dd>Defines a software type section. Recognized software type section names are <i>firmware</i>, <i>resident_application</i> and <i>user_application</i>. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;.&lt;software&gt;</code> []</p>
<dd>Defines a software section having an arbitrary name. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;.&lt;software&gt;.name</code> []</p>
<dd>Name of the software installed on the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;.&lt;software&gt;.patches</code> []</p>
<dd>String describing all patches applied to the given software on this hardcopy device. The individual patches are separated by a newline character &#8216;
&#8217;. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;.&lt;software&gt;.string_version</code> []</p>
<dd>String describing the version of the given software on this hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.&lt;sw_type&gt;.&lt;software&gt;.version</code> []</p>
<dd>Hex-encoded version string with a length of 16 octets consisting of the fields major version number (4 octets), minor version number (4 octets), build number (4 octets), service pack major number (2 octets) and service pack minor number (2 octets). </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.&lt;section&gt;.attributes_natural_language</code> [en]</p>
<dd>Variable length natural language tag conforming to RFC 5646 specifies the language to be used in the health assessment message of a given subtype. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.certification_state</code> []</p>
<dd>Hex-encoded certification state. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.configuration_state</code> []</p>
<dd>Hex-encoded configuration state. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.machine_type_model</code> []</p>
<dd>String specifying the machine type and model of the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.pstn_fax_enabled</code> [no]</p>
<dd>Specifies if a PSTN facsimile interface is installed and enabled on the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.time_source</code> []</p>
<dd>String specifying the hostname of the network time server used by the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.user_application_enabled</code> [no]</p>
<dd>Specifies if users can dynamically download and execute applications on the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.user_application_persistence_enabled</code> [no]</p>
<dd>Specifies if user dynamically downloaded applications can persist outside the boundaries of a single job on the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.vendor_name</code> []</p>
<dd>String specifying the manufacturer of the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-hcd.subtypes.system.vendor_smi_code</code> []</p>
<dd>Integer specifying the globally unique 24-bit SMI code assigned to the manufacturer of the hardcopy device. </p>
<dt><code>libimcv.plugins.imc-os.device_cert</code> []</p>
<dd>Manually set the path to the client device certificate (e.g. /etc/pts/aikCert.der) </p>
<dt><code>libimcv.plugins.imc-os.device_id</code> []</p>
<dd>Manually set the client device ID in hexadecimal format (e.g. 1083f03988c9762703b1c1080c2e46f72b99cc31) </p>
<dt><code>libimcv.plugins.imc-os.device_pubkey</code> []</p>
<dd>Manually set the path to the client device public key (e.g. /etc/pts/aikPub.der) </p>
<dt><code>libimcv.plugins.imc-os.push_info</code> [yes]</p>
<dd>Send operating system info without being prompted. </p>
<dt><code>libimcv.plugins.imc-scanner.push_info</code> [yes]</p>
<dd>Send open listening ports without being prompted. </p>
<dt><code>libimcv.plugins.imc-swid.swid_directory</code> [${prefix}/share]</p>
<dd>Directory where SWID tags are located. </p>
<dt><code>libimcv.plugins.imc-swid.swid_full</code> [FALSE]</p>
<dd>Include file information in the XML-encoded SWID tags. </p>
<dt><code>libimcv.plugins.imc-swid.swid_generator</code> [/usr/local/bin/swid_generator]</p>
<dd>SWID generator command to be executed. </p>
<dt><code>libimcv.plugins.imc-swid.swid_pretty</code> [FALSE]</p>
<dd>Generate XML-encoded SWID tags with pretty indentation. </p>
<dt><code>libimcv.plugins.imc-test.additional_ids</code> [0]</p>
<dd>Number of additional IMC IDs. </p>
<dt><code>libimcv.plugins.imc-test.command</code> [none]</p>
<dd>Command to be sent to the Test IMV. </p>
<dt><code>libimcv.plugins.imc-test.dummy_size</code> [0]</p>
<dd>Size of dummy attribute to be sent to the Test IMV (0 = disabled). </p>
<dt><code>libimcv.plugins.imc-test.retry</code> [no]</p>
<dd>Do a handshake retry. </p>
<dt><code>libimcv.plugins.imc-test.retry_command</code> []</p>
<dd>Command to be sent to the Test IMV in the handshake retry. </p>
<dt><code>libimcv.plugins.imv-attestation.cadir</code> []</p>
<dd>Path to directory with AIK cacerts. </p>
<dt><code>libimcv.plugins.imv-attestation.dh_group</code> [ecp256]</p>
<dd>Preferred Diffie-Hellman group. </p>
<dt><code>libimcv.plugins.imv-attestation.hash_algorithm</code> [sha256]</p>
<dd>Preferred measurement hash algorithm. </p>
<dt><code>libimcv.plugins.imv-attestation.mandatory_dh_groups</code> [yes]</p>
<dd>Enforce mandatory Diffie-Hellman groups. </p>
<dt><code>libimcv.plugins.imv-attestation.min_nonce_len</code> [0]</p>
<dd>DH minimum nonce length. </p>
<dt><code>libimcv.plugins.imv-os.remediation_uri</code> []</p>
<dd>URI pointing to operating system remediation instructions. </p>
<dt><code>libimcv.plugins.imv-scanner.remediation_uri</code> []</p>
<dd>URI pointing to scanner remediation instructions. </p>
<dt><code>libimcv.plugins.imv-swid.rest_api_timeout</code> [120]</p>
<dd>Timeout of SWID REST API HTTP POST transaction. </p>
<dt><code>libimcv.plugins.imv-swid.rest_api_uri</code> []</p>
<dd>HTTP URI of the SWID REST API. </p>
<dt><code>libimcv.plugins.imv-test.rounds</code> [0]</p>
<dd>Number of IMC-IMV retry rounds. </p>
<dt><code>libimcv.stderr_quiet</code> [no]</p>
<dd>Disable output to stderr with a stand-alone <i>libimcv</i> library. </p>
<dt><code>manager.database</code> []</p>
<dd>Credential database URI for manager. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>manager.debug</code> [no]</p>
<dd>Enable debugging in manager. </p>
<dt><code>manager.load</code> []</p>
<dd>Plugins to load in manager. </p>
<dt><code>manager.socket</code> []</p>
<dd>FastCGI socket of manager, to run it statically. </p>
<dt><code>manager.threads</code> [10]</p>
<dd>Threads to use for request handling. </p>
<dt><code>manager.timeout</code> [15m]</p>
<dd>Session timeout for manager. </p>
<dt><code>medsrv.database</code> []</p>
<dd>Mediation server database URI. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>medsrv.debug</code> [no]</p>
<dd>Debugging in mediation server web application. </p>
<dt><code>medsrv.dpd</code> [5m]</p>
<dd>DPD timeout to use in mediation server plugin. </p>
<dt><code>medsrv.load</code> []</p>
<dd>Plugins to load in mediation server plugin. </p>
<dt><code>medsrv.password_length</code> [6]</p>
<dd>Minimum password length required for mediation server user accounts. </p>
<dt><code>medsrv.rekey</code> [20m]</p>
<dd>Rekeying time on mediation connections in mediation server plugin. </p>
<dt><code>medsrv.socket</code> []</p>
<dd>Run Mediation server web application statically on socket. </p>
<dt><code>medsrv.threads</code> [5]</p>
<dd>Number of thread for mediation service web application. </p>
<dt><code>medsrv.timeout</code> [15m]</p>
<dd>Session timeout for mediation service. </p>
<dt><code>pacman.database</code> []</p>
<dd>Database URI for the database that stores the package information. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>pacman.load</code> []</p>
<dd>Plugins to load in package manager. </p>
<dt><code>pki.load</code> []</p>
<dd>Plugins to load in ipsec pki tool. </p>
<dt><code>pool.database</code> []</p>
<dd>Database URI for the database that stores IP pools and configuration attributes. If it contains a password, make sure to adjust the permissions of the config file accordingly. </p>
<dt><code>pool.load</code> []</p>
<dd>Plugins to load in ipsec pool tool. </p>
<dt><code>scepclient.load</code> []</p>
<dd>Plugins to load in ipsec scepclient tool. </p>
<dt><code>starter.config_file</code> [${sysconfdir}/ipsec.conf]</p>
<dd>Location of the ipsec.conf file </p>
<dt><code>starter.load_warning</code> [yes]</p>
<dd>Disable charon plugin load option warning. </p>
<dt><code>swanctl.load</code> []</p>
<dd>Plugins to load in swanctl. </p>
</dl>
<h2>Logger Configuration</h2>
<p>Options in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5) provide a much more flexible way to configure loggers for the IKE daemon charon than using the <code>charondebug</code> option in <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5). </p>
<p> <code>Note</code>: If any loggers are specified in strongswan.conf, <code>charondebug</code> does not have any effect. </p>
<p> There are currently two types of loggers:</p>
<dl>
<dt><code>File loggers</code></p>
<dd>Log directly to a file and are defined by specifying the full path to the file as subsection in the <code>charon.filelog</code> section. To log to the console the two special filenames <code>stdout</code> and <code>stderr</code> can be used.</p>
<dt><code>Syslog loggers</code></p>
<dd>Log into a syslog facility and are defined by specifying the facility to log to as the name of a subsection in the <code>charon.syslog</code> section. The following facilities are currently supported: <code>daemon</code> and <code>auth</code>.</dl>
<p> Multiple loggers can be defined for each type with different log verbosity for the different subsystems of the daemon.</p>
<h3>Subsystems</h3>
<dl>
<dt><code>dmn</code></p>
<dd>Main daemon setup/cleanup/signal handling</p>
<dt><code>mgr</code></p>
<dd>IKE_SA manager, handling synchronization for IKE_SA access</p>
<dt><code>ike</code></p>
<dd>IKE_SA</p>
<dt><code>chd</code></p>
<dd>CHILD_SA</p>
<dt><code>job</code></p>
<dd>Jobs queueing/processing and thread pool management</p>
<dt><code>cfg</code></p>
<dd>Configuration management and plugins</p>
<dt><code>knl</code></p>
<dd>IPsec/Networking kernel interface</p>
<dt><code>net</code></p>
<dd>IKE network communication</p>
<dt><code>asn</code></p>
<dd>Low-level encoding/decoding (ASN.1, X.509 etc.)</p>
<dt><code>enc</code></p>
<dd>Packet encoding/decoding encryption/decryption operations</p>
<dt><code>tls</code></p>
<dd>libtls library messages</p>
<dt><code>esp</code></p>
<dd>libipsec library messages</p>
<dt><code>lib</code></p>
<dd>libstrongwan library messages</p>
<dt><code>tnc</code></p>
<dd>Trusted Network Connect</p>
<dt><code>imc</code></p>
<dd>Integrity Measurement Collector</p>
<dt><code>imv</code></p>
<dd>Integrity Measurement Verifier</p>
<dt><code>pts</code></p>
<dd>Platform Trust Service</dl>
<h3>Loglevels</h3>
<dl>
<dt><code>-1</code></p>
<dd>Absolutely silent</p>
<dt><code>0</code></p>
<dd>Very basic auditing logs, (e.g. SA up/SA down)</p>
<dt><code>1</code></p>
<dd>Generic control flow with errors, a good default to see whats going on</p>
<dt><code>2</code></p>
<dd>More detailed debugging control flow</p>
<dt><code>3</code></p>
<dd>Including RAW data dumps in Hex</p>
<dt><code>4</code></p>
<dd>Also include sensitive material in dumps, e.g. keys</dl>
<h3>Example</h3>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>charon {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>filelog {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/var/log/charon.log {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>time_format = %b %e %T<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>append = no<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default = 1<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>stderr {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ike = 2<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>knl = 3<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ike_name = yes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>syslog {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># enable logging to LOG_DAEMON, use defaults<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>daemon {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># minimalistic IKE auditing logging to LOG_AUTHPRIV<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>auth {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default = -1<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ike = 0<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<h2>Job Priority Management</h2>
<p>Some operations in the IKEv2 daemon charon are currently implemented synchronously and blocking. Two examples for such operations are communication with a RADIUS server via EAP-RADIUS, or fetching CRL/OCSP information during certificate chain verification. Under high load conditions, the thread pool may run out of available threads, and some more important jobs, such as liveness checking, may not get executed in time. </p>
<p> To prevent thread starvation in such situations job priorities were introduced. The job processor will reserve some threads for higher priority jobs, these threads are not available for lower priority, locking jobs.</p>
<h3>Implementation</h3>
<p>Currently 4 priorities have been defined, and they are used in charon as follows:</p>
<dl>
<dt><code>CRITICAL</code></p>
<dd>Priority for long-running dispatcher jobs.</p>
<dt><code>HIGH</code></p>
<dd>INFORMATIONAL exchanges, as used by liveness checking (DPD).</p>
<dt><code>MEDIUM</code></p>
<dd>Everything not HIGH/LOW, including IKE_SA_INIT processing.</p>
<dt><code>LOW</code></p>
<dd>IKE_AUTH message processing. RADIUS and CRL fetching block here</dl>
<p> Although IKE_SA_INIT processing is computationally expensive, it is explicitly assigned to the MEDIUM class. This allows charon to do the DH exchange while other threads are blocked in IKE_AUTH. To prevent the daemon from accepting more IKE_SA_INIT requests than it can handle, use IKE_SA_INIT DROPPING. </p>
<p> The thread pool processes jobs strictly by priority, meaning it will consume all higher priority jobs before looking for ones with lower priority. Further, it reserves threads for certain priorities. A priority class having reserved <i>n</i> threads will always have <i>n</i> threads available for this class (either currently processing a job, or waiting for one).</p>
<h3>Configuration</h3>
<p>To ensure that there are always enough threads available for higher priority tasks, threads must be reserved for each priority class.</p>
<dl>
<dt><code>charon.processor.priority_threads.critical</code> [0]</p>
<dd>Threads reserved for CRITICAL priority class jobs</p>
<dt><code>charon.processor.priority_threads.high</code> [0]</p>
<dd>Threads reserved for HIGH priority class jobs</p>
<dt><code>charon.processor.priority_threads.medium</code> [0]</p>
<dd>Threads reserved for MEDIUM priority class jobs</p>
<dt><code>charon.processor.priority_threads.low</code> [0]</p>
<dd>Threads reserved for LOW priority class jobs</dl>
<p> Let&#8217;s consider the following configuration: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>charon {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>processor {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>priority_threads {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>high = 1<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>medium = 4<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> With this configuration, one thread is reserved for HIGH priority tasks. As currently only liveness checking and stroke message processing is done with high priority, one or two threads should be sufficient. </p>
<p> The MEDIUM class mostly processes non-blocking jobs. Unless your setup is experiencing many blocks in locks while accessing shared resources, threads for one or two times the number of CPU cores is fine. </p>
<p> It is usually not required to reserve threads for CRITICAL jobs. Jobs in this class rarely return and do not release their thread to the pool. </p>
<p> The remaining threads are available for LOW priority jobs. Reserving threads does not make sense (until we have an even lower priority).</p>
<h3>Monitoring</h3>
<p>To see what the threads are actually doing, invoke <i>ipsec statusall</i>. Under high load, something like this will show up: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>worker threads: 2 or 32 idle, 5/1/2/22 working,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>job queue: 0/0/1/149, scheduled: 198</p>
<p> From 32 worker threads,</p>
<dl>
<dt>2</p>
<dd>are currently idle.</p>
<dt>5</p>
<dd>are running CRITICAL priority jobs (dispatching from sockets, etc.).</p>
<dt>1</p>
<dd>is currently handling a HIGH priority job. This is actually the thread currently providing this information via stroke.</p>
<dt>2</p>
<dd>are handling MEDIUM priority jobs, likely IKE_SA_INIT or CREATE_CHILD_SA messages.</p>
<dt>22</p>
<dd>are handling LOW priority jobs, probably waiting for an EAP-RADIUS response while processing IKE_AUTH messages.</dl>
<p> The job queue load shows how many jobs are queued for each priority, ready for execution. The single MEDIUM priority job will get executed immediately, as we have two spare threads reserved for MEDIUM class jobs.</p>
<h2>Ike_Sa_Init Dropping</h2>
<p>If a responder receives more connection requests per seconds than it can handle, it does not make sense to accept more IKE_SA_INIT messages. And if they are queued but can&#8217;t get processed in time, an answer might be sent after the client has already given up and restarted its connection setup. This additionally increases the load on the responder. </p>
<p> To limit the responder load resulting from new connection attempts, the daemon can drop IKE_SA_INIT messages just after reception. There are two mechanisms to decide if this should happen, configured with the following options:</p>
<dl>
<dt><code>charon.init_limit_half_open</code> [0]</p>
<dd>Limit based on the number of half open IKE_SAs. Half open IKE_SAs are SAs in connecting state, but not yet established.</p>
<dt><code>charon.init_limit_job_load</code> [0]</p>
<dd>Limit based on the number of jobs currently queued for processing (sum over all job priorities).</dl>
<p> The second limit includes load from other jobs, such as rekeying. Choosing a good value is difficult and depends on the hardware and expected load. </p>
<p> The first limit is simpler to calculate, but includes the load from new connections only. If your responder is capable of negotiating 100 tunnels/s, you might set this limit to 1000. The daemon will then drop new connection attempts if generating a response would require more than 10 seconds. If you are allowing for a maximum response time of more than 30 seconds, consider adjusting the timeout for connecting IKE_SAs (<code>charon.half_open_timeout</code>). A responder, by default, deletes an IKE_SA if the initiator does not establish it within 30 seconds. Under high load, a higher value might be required.</p>
<h2>Load Tests</h2>
<p>To do stability testing and performance optimizations, the IKE daemon charon provides the <i>load-tester</i> plugin. This plugin allows one to setup thousands of tunnels concurrently against the daemon itself or a remote host. </p>
<p> <code>WARNING:</code> Never enable the load-testing plugin on productive systems. It provides preconfigured credentials and allows an attacker to authenticate as any user.</p>
<h3>Configuration details</h3>
<p>For public key authentication, the responder uses the <code>&quot;CN=srv, OU=load-test, O=strongSwan&quot;</code> identity. For the initiator, each connection attempt uses a different identity in the form <code>&quot;CN=c1-r1, OU=load-test, O=strongSwan&quot;</code>, where the first number inidicates the client number, the second the authentication round (if multiple authentication rounds are used). </p>
<p> For PSK authentication, FQDN identities are used. The server uses <code>srv.strongswan.org</code>, the client uses an identity in the form <code>c1-r1.strongswan.org</code>. </p>
<p> For EAP authentication, the client uses a NAI in the form <code>100000000010001 [at] strongswan.org</code>. </p>
<p> To configure multiple authentication rounds, concatenate multiple methods using, e.g. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>initiator_auth = pubkey|psk|eap-md5|eap-aka</p>
<p> The responder uses a hardcoded certificate based on a 1024-bit RSA key. This certificate additionally serves as CA certificate. A peer uses the same private key, but generates client certificates on demand signed by the CA certificate. Install the Responder/CA certificate on the remote host to authenticate all clients. </p>
<p> To speed up testing, the load tester plugin implements a special Diffie-Hellman implementation called <i>modpnull</i>. By setting <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>proposal = aes128-sha1-modpnull<br />
 this wicked fast DH implementation is used. It does not provide any security at all, but allows one to run tests without DH calculation overhead.</p>
<h3>Examples</h3>
<p>In the simplest case, the daemon initiates IKE_SAs against itself using the loopback interface. This will actually establish double the number of IKE_SAs, as the daemon is initiator and responder for each IKE_SA at the same time. Installation of IPsec SAs would fail, as each SA gets installed twice. To simulate the correct behavior, a fake kernel interface can be enabled which does not install the IPsec SAs at the kernel level. </p>
<p> A simple loopback configuration might look like this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>charon {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># create new IKE_SAs for each CHILD_SA to simulate<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># different clients<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>reuse_ikesa = no<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># turn off denial of service protection<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dos_protection = no</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>plugins {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>load-tester {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># enable the plugin<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>enable = yes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># use 4 threads to initiate connections<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># simultaneously<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>initiators = 4<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># each thread initiates 1000 connections<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iterations = 1000<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># delay each initiation in each thread by 20ms<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>delay = 20<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># enable the fake kernel interface to<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># avoid SA conflicts<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fake_kernel = yes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> This will initiate 4000 IKE_SAs within 20 seconds. You may increase the delay value if your box can not handle that much load, or decrease it to put more load on it. If the daemon starts retransmitting messages your box probably can not handle all connection attempts. </p>
<p> The plugin also allows one to test against a remote host. This might help to test against a real world configuration. A connection setup to do stress testing of a gateway might look like this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>charon {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>reuse_ikesa = no<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>threads = 32</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>plugins {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>load-tester {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>enable = yes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># 10000 connections, ten in parallel<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>initiators = 10<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iterations = 1000<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># use a delay of 100ms, overall time is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># iterations * delay = 100s<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>delay = 100<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># address of the gateway<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>remote = 1.2.3.4<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># IKE-proposal to use<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>proposal = aes128-sha1-modp1024<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># use faster PSK authentication instead<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># of 1024bit RSA<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>initiator_auth = psk<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>responder_auth = psk<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># request a virtual IP using configuration<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># payloads<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>request_virtual_ip = yes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># enable CHILD_SA every 60s<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>child_rekey = 60<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<h2>IKEv2 RETRANSMISSION</h2>
<p>Retransmission timeouts in the IKEv2 daemon charon can be configured globally using the three keys listed below: </p>
<dl>
<dd>
<pre><code>charon.retransmit_base</code> [1.8]
<code>charon.retransmit_timeout</code> [4.0]
<code>charon.retransmit_tries</code> [5]
<code>charon.retransmit_jitter</code> [0]
<code>charon.retransmit_limit</code> [0]</pre>
</dl>
<p> The following algorithm is used to calculate the timeout: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>relative timeout = retransmit_timeout * retransmit_base ^ (n-1)</p>
<p> Where <i>n</i> is the current retransmission count. The calculated timeout can&#8217;t exceed the configured retransmit_limit (if any), which is useful if the number of retries is high. </p>
<p> If a jitter in percent is configured, the timeout is modified as follows: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>relative timeout -= random(0, retransmit_jitter * relative timeout)</p>
<p> Using the default values, packets are retransmitted in: </p>
<table>
<tr VALIGN=top>
<td>Retransmission</td>
<td ALIGN=right>Relative Timeout</td>
<td ALIGN=right>Absolute Timeout
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
</tr>
<tr VALIGN=top>
<td><code>2</code></td>
<td ALIGN=right>7s</td>
<td ALIGN=right>11s
</td>
</tr>
<tr VALIGN=top>
<td><code>3</code></td>
<td ALIGN=right>13s</td>
<td ALIGN=right>24s
</td>
</tr>
<tr VALIGN=top>
<td><code>4</code></td>
<td ALIGN=right>23s</td>
<td ALIGN=right>47s
</td>
</tr>
<tr VALIGN=top>
<td><code>5</code></td>
<td ALIGN=right>42s</td>
<td ALIGN=right>89s
</td>
</tr>
<tr VALIGN=top>
<td><code>giving up</code></td>
<td ALIGN=right>76s</td>
<td ALIGN=right>165s
</td>
</tr>
</table>
<h2>Variables</h2>
<p>The variables used above are configured as follows: </p>
<pre>${piddir} /var/run
${prefix} /usr
${random_device} /dev/random
${urandom_device} /dev/urandom</pre>
<h2>Files</h2>
<pre>/etc/strongswan.conf configuration file
/etc/strongswan.d/ directory containing included config snippets
/etc/strongswan.d/charon/ plugin specific config snippets</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-charon-cmd/">charon-cmd</a></code>(8) </p>
<h2>History</h2>
<p>Written for the strongSwan project by Tobias Brunner, Andreas Steffen and Martin Willi.</p>
