---
title: "ipa-client-install(1)"
name: "ipa-client-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-client-install/"
description: "ipa-client-install – Configure an IPA client"
---

<h2>NAME</h2>
<p> ipa-client-install &#8211; Configure an IPA client</p>
<h2>SYNOPSIS</h2>
<p> ipa-client-install [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Configures a client machine to use IPA for authentication and identity services. </p>
<p> By default this configures SSSD to connect to an IPA server for authentication and authorization. Optionally one can instead configure PAM and NSS (Name Switching Service) to work with an IPA server over Kerberos and LDAP. </p>
<p> An authorized user is required to join a client machine to IPA. This can take the form of a kerberos principal or a one-time password associated with the machine. </p>
<p> This same tool is used to unconfigure IPA and attempts to return the machine to its previous state. Part of this process is to unenroll the host from the IPA server. Unenrollment consists of disabling the principal key on the IPA server so that it may be re-enrolled. The machine principal in /etc/krb5.keytab (host/&lt;fqdn&gt;@REALM) is used to authenticate to the IPA server to unenroll itself. If this principal does not exist then unenrollment will fail and an administrator will need to disable the host principal (ipa host-disable &lt;fqdn&gt;). </p>
<h3>Assumptions</h3>
<p> The ipa-client-install script assumes that the machine has already generated SSH keys. It will not generate SSH keys of its own accord. If SSH keys are not present (e.g when running the ipa-client-install in a kickstart, before ever running sshd), they will not be uploaded to the client host entry on the server. </p>
<h3>Hostname Requirements</h3>
<p> Client must use a <code>static hostname</code>. If the machine hostname changes for example due to a dynamic hostname assignment by a DHCP server, client enrollment to IPA server breaks and user then would not be able to perform Kerberos authentication. </p>
<p> &#8211;hostname option may be used to specify a static hostname that persists over reboot. </p>
<h3>DNS Autodiscovery</h3>
<p> Client installer by default tries to search for _ldap._tcp.DOMAIN DNS SRV records for all domains that are parent to its hostname. For example, if a client machine has a hostname &#8216;client1.lab.example.com&#8217;, the installer will try to retrieve an IPA server hostname from _ldap._tcp.lab.example.com, _ldap._tcp.example.com and _ldap._tcp.com DNS SRV records, respectively. The discovered domain is then used to configure client components (e.g. SSSD and Kerberos 5 configuration) on the machine. </p>
<p> When the client machine hostname is not in a subdomain of an IPA server, its domain can be passed with &#8211;domain option. In that case, both SSSD and Kerberos components have the domain set in the configuration files and will use it to autodiscover IPA servers. </p>
<p> Client machine can also be configured without a DNS autodiscovery at all. When both &#8211;server and &#8211;domain options are used, client installer will use the specified server and domain directly. &#8211;server option accepts multiple server hostnames which can be used for failover mechanism. Without DNS autodiscovery, Kerberos is configured with a fixed list of KDC and Admin servers. SSSD is still configured to either try to read domain&#8217;s SRV records or the specified fixed list of servers. When &#8211;fixed-primary option is specified, SSSD will not try to read DNS SRV record at all (see <a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a>(5) for details). </p>
<h3>The Failover Mechanism</h3>
<p> When some of the IPA servers is not available, client components are able to fallback to other IPA replica and thus preserving a continued service. When client machine is configured to use DNS SRV record autodiscovery (no fixed server was passed to the installer), client components do the fallback automatically, based on the IPA server hostnames and priorities discovered from the DNS SRV records. </p>
<p> If DNS autodiscovery is not available, clients should be configured at least with a fixed list of IPA servers that can be used in case of a failure. When only one IPA server is configured, IPA client services will not be available in case of a failure of the IPA server. Please note, that in case of a fixed list of IPA servers, the fixed server lists in client components need to be updated when a new IPA server is enrolled or a current IPA server is decommissioned. </p>
<h3>Coexistence With Other Directory Servers</h3>
<p> Other directory servers deployed in the network (e.g. Microsoft Active Directory) may use the same DNS SRV records to denote hosts with a directory service (_ldap._tcp.DOMAIN). Such DNS SRV records may break the installation if the installer discovers these DNS records before it finds DNS SRV records pointing to IPA servers. The installer would then fail to discover the IPA server and exit with error. </p>
<p> In order to avoid the aforementioned DNS autodiscovery issues, the client machine hostname should be in a domain with properly defined DNS SRV records pointing to IPA servers, either manually with a custom DNS server or with IPA DNS integrated solution. A second approach would be to avoid autodiscovery and configure the installer to use a fixed list of IPA server hostnames using the &#8211;server option and with a &#8211;fixed-primary option disabling DNS SRV record autodiscovery in SSSD. </p>
<h3>Re-enrollment of the host</h3>
<p> Requirements: </p>
<p> 1. Host has not been un-enrolled (the ipa-client-install &#8211;uninstall command has not been run).<br />
 2. The host entry has not been disabled via the ipa host-disable command. </p>
<p> If this has been the case, host can be re-enrolled using the usual methods. </p>
<p> There are two method of authenticating a re-enrollment: </p>
<p> 1. You can use &#8211;force-join option with ipa-client-install command. This authenticates the re-enrollment using the admin&#8217;s credentials provided via the -w/&#8211;password option.<br />
 2. If providing the admin&#8217;s password via the command line is not an option (e.g you want to create a script to re-enroll a host and keep the admin&#8217;s password secure), you can use backed up keytab from the previous enrollment of this host to authenticate. See &#8211;keytab option. </p>
<p> Consequences of the re-enrollment on the host entry: </p>
<p> 1. A new host certificate is issued<br />
 2. The old host certificate is revoked<br />
 3. New SSH keys are generated<br />
 4. ipaUniqueID is preserved </p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>&#8211;domain</code>=<i>DOMAIN</i></p>
<dd> The primary DNS domain of an existing IPA deployment, e.g. example.com. This DNS domain should contain the SRV records generated by the IPA server installer. Usually the name is a lower-cased name of an IPA Kerberos realm name. </p>
<p> When no &#8211;server option is specified, this domain will be used by the installer to discover all available servers via DNS SRV record autodiscovery (see DNS Autodiscovery section for details). </p>
<p> The default value used by the installer is the domain part of the hostname. This option needs to be specified if the primary IPA DNS domain is different from the default value.</p>
<dt><code>&#8211;server</code>=<i>SERVER</i></p>
<dd> Set the FQDN of the IPA server to connect to. May be specified multiple times to add multiple servers to ipa_server value in sssd.conf or krb5.conf. Only the first value is considered when used with &#8211;no-sssd. When this option is used, DNS autodiscovery for Kerberos is disabled and a fixed list of KDC and Admin servers is configured. </p>
<p> Under normal circumstances, this option is not needed as the list of servers is retrieved from the primary IPA DNS domain.</p>
<dt><code>&#8211;realm</code>=<i>REALM_NAME</i></p>
<dd> The Kerberos realm of an existing IPA deployment. Usually it is an upper-cased name of the primary DNS domain used by the IPA installation. </p>
<p> Under normal circumstances, this option is not needed as the realm name is retrieved from the IPA server.</p>
<dt><code>&#8211;fixed-primary</code></p>
<dd> Configure SSSD to use a fixed server as the primary IPA server. The default is to use DNS SRV records to determine the primary server to use and fall back to the server the client is enrolled with. When used in conjunction with &#8211;server then no _srv_ value is set in the ipa_server option in sssd.conf.</p>
<dt><code>-p</code>, <code>&#8211;principal</code></p>
<dd> Authorized kerberos principal to use to join the IPA realm.</p>
<dt><code>-w</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd> Password for joining a machine to the IPA realm. Assumes bulk password unless principal is also set.</p>
<dt><code>-W</code></p>
<dd> Prompt for the password for joining a machine to the IPA realm.</p>
<dt><code>-k</code>, <code>&#8211;keytab</code></p>
<dd> Path to backed up host keytab from previous enrollment. Joins the host even if it is already enrolled.</p>
<dt><code>&#8211;mkhomedir</code></p>
<dd> Configure PAM to create a users home directory if it does not exist.</p>
<dt><code>&#8211;hostname</code></p>
<dd> The hostname of this machine (FQDN). If specified, the hostname will be set and the system configuration will be updated to persist over reboot. By default the result of getfqdn() call from Python&#8217;s socket module is used.</p>
<dt><code>&#8211;force-join</code></p>
<dd> Join the host even if it is already enrolled.</p>
<dt><code>&#8211;ntp-server</code>=<i>NTP_SERVER</i></p>
<dd> Configure ntpd to use this NTP server. This option can be used multiple times.</p>
<dt><code>-N</code>, <code>&#8211;no-ntp</code></p>
<dd> Do not configure or enable NTP.</p>
<dt><code>&#8211;force-ntpd</code></p>
<dd> Stop and disable any time&amp;date synchronization services besides ntpd.</p>
<dt><code>&#8211;nisdomain</code>=<i>NIS_DOMAIN</i></p>
<dd> Set the NIS domain name as specified. By default, this is set to the IPA domain name.</p>
<dt><code>&#8211;no-nisdomain</code></p>
<dd> Do not configure NIS domain name.</p>
<dt><code>&#8211;ssh-trust-dns</code></p>
<dd> Configure OpenSSH client to trust DNS SSHFP records.</p>
<dt><code>&#8211;no-ssh</code></p>
<dd> Do not configure OpenSSH client.</p>
<dt><code>&#8211;no-sshd</code></p>
<dd> Do not configure OpenSSH server.</p>
<dt><code>&#8211;no-sudo</code></p>
<dd> Do not configure SSSD as a data source for sudo.</p>
<dt><code>&#8211;no-dns-sshfp</code></p>
<dd> Do not automatically create DNS SSHFP records.</p>
<dt><code>&#8211;noac</code></p>
<dd> Do not use Authconfig to modify the nsswitch.conf and PAM configuration.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force the settings even if errors occur</p>
<dt><code>&#8211;kinit-attempts</code>=<i>KINIT_ATTEMPTS</i></p>
<dd> In case of unresponsive KDC (e.g. when enrolling multiple hosts at once in a heavy load environment) repeat the request for host Kerberos ticket up to a total number of <i>KINIT_ATTEMPTS</i> times before giving up and aborting client installation. Default number of attempts is 5. The request is not repeated when there is a problem with host credentials themselves (e.g. wrong keytab format or invalid principal) so using this option will not lead to account lockouts.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information to stdout</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> Unattended installation. The user will not be prompted.</p>
<dt><code>&#8211;ca-cert-file</code>=<i>CA_FILE</i></p>
<dd> Do not attempt to acquire the IPA CA certificate via automated means, instead use the CA certificate found locally in in <i>CA_FILE</i>. The <i>CA_FILE</i> must be an absolute path to a PEM formatted certificate file. The CA certificate found in <i>CA_FILE</i> is considered authoritative and will be installed without checking to see if it&#8217;s valid for the IPA domain.</p>
<dt><code>&#8211;request-cert</code></p>
<dd> Request certificate for the machine. The certificate will be stored in /etc/ipa/nssdb under the nickname &quot;Local IPA host&quot;. </p>
<p> Using this option requires that D-Bus is properly configured or not configured at all. In environment where this condition is not met (e.g. anaconda kickstart chroot environment) set the system bus address to /dev/null to enable workaround in ipa-client-install. </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>env DBUS_SYSTEM_BUS_ADDRESS=unix:path=/dev/null ipa-client-install &#8211;request-cert </p>
<p> Note that requesting the certificate when certmonger is not running only creates tracking request and the certmonger service must be started to be able to track certificates.</p>
<dt><code>&#8211;automount-location</code>=<i>LOCATION</i></p>
<dd> Configure automount by running <a href="/docs/linux/man/1-ipa-client-automount/">ipa-client-automount</a>(1) with <i>LOCATION</i> as automount location.</p>
<dt><code>&#8211;configure-firefox</code></p>
<dd> Configure Firefox to use IPA domain credentials.</p>
<dt><code>&#8211;firefox-dir</code>=<i>DIR</i></p>
<dd> Specify Firefox installation directory. For example: &#8216;/usr/lib/firefox&#8217;</p>
<dt><code>&#8211;ip-address</code>=<i>IP_ADDRESS</i></p>
<dd> Use <i>IP_ADDRESS</i> in DNS A/AAAA record for this host. May be specified multiple times to add multiple DNS records.</p>
<dt><code>&#8211;all-ip-addresses</code></p>
<dd> Create DNS A/AAAA record for each IP address on this host. </p>
</dl>
<h3>SSSD OPTIONS</h3>
<dl>
<dt><code>&#8211;permit</code></p>
<dd> Configure SSSD to permit all access. Otherwise the machine will be controlled by the Host-based Access Controls (HBAC) on the IPA server.</p>
<dt><code>&#8211;enable-dns-updates</code></p>
<dd> This option tells SSSD to automatically update DNS with the IP address of this client.</p>
<dt><code>&#8211;no-krb5-offline-passwords</code></p>
<dd> Configure SSSD not to store user password when the server is offline.</p>
<dt><code>-S</code>, <code>&#8211;no-sssd</code></p>
<dd> Do not configure the client to use SSSD for authentication, use nss_ldap instead.</p>
<dt><code>&#8211;preserve-sssd</code></p>
<dd> Disabled by default. When enabled, preserves old SSSD configuration if it is not possible to merge it with a new one. Effectively, if the merge is not possible due to SSSDConfig reader encountering unsupported options, <code>ipa-client-install</code> will not run further and ask to fix SSSD config first. When this option is not specified, <code>ipa-client-install</code> will back up SSSD config and create new one. The back up version will be restored during uninstall. </p>
</dl>
<h3>UNINSTALL OPTIONS</h3>
<dl>
<dt><code>&#8211;uninstall</code></p>
<dd> Remove the IPA client software and restore the configuration to the pre-IPA state.</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> Unattended uninstallation. The user will not be prompted. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>Files that will be replaced if SSSD is configured (default):</p>
<dd>
<p> /etc/sssd/sssd.conf</p>
<dt>Files that will be replaced if they exist and SSSD is not configured (&#8211;no-sssd):</p>
<dd>
<p> /etc/ldap.conf<br />
 /etc/nss_ldap.conf<br />
 /etc/libnss-ldap.conf<br />
 /etc/pam_ldap.conf<br />
 /etc/nslcd.conf</p>
<dt>Files replaced if NTP is enabled:</p>
<dd>
<p> /etc/ntp.conf<br />
 /etc/sysconfig/ntpd<br />
 /etc/ntp/step-tickers</p>
<dt>Files always created (replacing existing content):</p>
<dd>
<p> /etc/krb5.conf<br />
 /etc/ipa/ca.crt<br />
 /etc/ipa/default.conf<br />
 /etc/ipa/nssdb<br />
 /etc/openldap/ldap.conf</p>
<dt>Files updated, existing content is maintained:</p>
<dd>
<p> /etc/nsswitch.conf<br />
 /etc/krb5.keytab<br />
 /etc/sysconfig/network</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred </p>
<p> 2 if uninstalling and the client is not configured </p>
<p> 3 if installing and the client is already configured </p>
<p> 4 if an uninstall error occurred </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipa-client-automount/">ipa-client-automount</a>(1),</code> <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5),</code> <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a>(5)</code> </p>
<h2>Index</h2>
