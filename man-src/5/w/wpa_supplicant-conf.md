---
title: "wpa_supplicant-conf(5)"
name: "wpa_supplicant-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wpa_supplicant-conf/"
description: "wpa_supplicant.conf – configuration file for wpa_supplicant"
---

<p>wpa_supplicant.conf &#8211; configuration file for wpa_supplicant</p>
<h2>Overview</h2>
<p><code>wpa_supplicant</code> is configured using a text file that lists all accepted networks and security policies, including pre-shared keys. See the example configuration file, probably in <code>/usr/share/doc/wpa_supplicant/</code>, for detailed information about the configuration format and supported fields. </p>
<p> All file paths in this configuration file should use full (absolute, not relative to working directory) path in order to allow working directory to be changed. This can happen if wpa_supplicant is run in the background. </p>
<p> Changes to configuration file can be reloaded be sending SIGHUP signal to <code>wpa_supplicant</code> (&#8216;killall -HUP wpa_supplicant&#8217;). Similarly, reloading can be triggered with the <code>wpa_cli reconfigure</code> command. </p>
<p> Configuration file can include one or more network blocks, e.g., one for each used SSID. wpa_supplicant will automatically select the best network based on the order of network blocks in the configuration file, network security level (WPA/WPA2 is preferred), and signal strength.</p>
<h2>Quick Examples</h2>
<dl>
<dt>1.</p>
<dd>WPA-Personal (PSK) as home network and WPA-Enterprise with EAP-TLS as work network. </p>
<dl>
<dd>
<pre># allow frontend (e.g., wpa_cli) to be used by all users in 'netdev' group
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
#
# home network; allow all valid ciphers
network={
 ssid=&quot;home&quot;
 scan_ssid=1
 key_mgmt=WPA-PSK
 psk=&quot;very secret passphrase&quot;
}
#
# work network; use EAP-TLS with WPA; allow only CCMP and TKIP ciphers
network={
 ssid=&quot;work&quot;
 scan_ssid=1
 key_mgmt=WPA-EAP
 pairwise=CCMP TKIP
 group=CCMP TKIP
 eap=TLS
 identity=&quot;user [at] example.com&quot;
 ca_cert=&quot;/etc/cert/ca.pem&quot;
 client_cert=&quot;/etc/cert/user.pem&quot;
 private_key=&quot;/etc/cert/user.prv&quot;
 private_key_passwd=&quot;password&quot;
}</pre>
</dl>
<dt>2.</p>
<dd>WPA-RADIUS/EAP-PEAP/MSCHAPv2 with RADIUS servers that use old peaplabel (e.g., Funk Odyssey and SBR, Meetinghouse Aegis, Interlink RAD-Series) </p>
<dl>
<dd>
<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
 ssid=&quot;example&quot;
 scan_ssid=1
 key_mgmt=WPA-EAP
 eap=PEAP
 identity=&quot;user [at] example.com&quot;
 password=&quot;foobar&quot;
 ca_cert=&quot;/etc/cert/ca.pem&quot;
 phase1=&quot;peaplabel=0&quot;
 phase2=&quot;auth=MSCHAPV2&quot;
}</pre>
</dl>
<dt>3.</p>
<dd>EAP-TTLS/EAP-MD5-Challenge configuration with anonymous identity for the unencrypted use. Real identity is sent only within an encrypted TLS tunnel. </p>
<dl>
<dd>
<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
 ssid=&quot;example&quot;
 scan_ssid=1
 key_mgmt=WPA-EAP
 eap=TTLS
 identity=&quot;user [at] example.com&quot;
 anonymous_identity=&quot;anonymous [at] example.com&quot;
 password=&quot;foobar&quot;
 ca_cert=&quot;/etc/cert/ca.pem&quot;
 phase2=&quot;auth=MD5&quot;
}</pre>
</dl>
<dt>4.</p>
<dd>IEEE 802.1X (i.e., no WPA) with dynamic WEP keys (require both unicast and broadcast); use EAP-TLS for authentication </p>
<dl>
<dd>
<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
 ssid=&quot;1x-test&quot;
 scan_ssid=1
 key_mgmt=IEEE8021X
 eap=TLS
 identity=&quot;user [at] example.com&quot;
 ca_cert=&quot;/etc/cert/ca.pem&quot;
 client_cert=&quot;/etc/cert/user.pem&quot;
 private_key=&quot;/etc/cert/user.prv&quot;
 private_key_passwd=&quot;password&quot;
 eapol_flags=3
}</pre>
</dl>
<dt>5.</p>
<dd>Catch all example that allows more or less all configuration modes. The configuration options are used based on what security policy is used in the selected SSID. This is mostly for testing and is not recommended for normal use. </p>
<dl>
<dd>
<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
 ssid=&quot;example&quot;
 scan_ssid=1
 key_mgmt=WPA-EAP WPA-PSK IEEE8021X NONE
 pairwise=CCMP TKIP
 group=CCMP TKIP WEP104 WEP40
 psk=&quot;very secret passphrase&quot;
 eap=TTLS PEAP TLS
 identity=&quot;user [at] example.com&quot;
 password=&quot;foobar&quot;
 ca_cert=&quot;/etc/cert/ca.pem&quot;
 client_cert=&quot;/etc/cert/user.pem&quot;
 private_key=&quot;/etc/cert/user.prv&quot;
 private_key_passwd=&quot;password&quot;
 phase1=&quot;peaplabel=0&quot;
 ca_cert2=&quot;/etc/cert/ca2.pem&quot;
 client_cert2=&quot;/etc/cer/user.pem&quot;
 private_key2=&quot;/etc/cer/user.prv&quot;
 private_key2_passwd=&quot;password&quot;
}</pre>
</dl>
<dt>6.</p>
<dd>Authentication for wired Ethernet. This can be used with <code>wired</code> or <code>roboswitch</code> interface (-Dwired or -Droboswitch on command line). </p>
<dl>
<dd>
<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
ap_scan=0
network={
 key_mgmt=IEEE8021X
 eap=MD5
 identity=&quot;user&quot;
 password=&quot;password&quot;
 eapol_flags=0
}</pre>
</dl>
</dl>
<h2>Certificates</h2>
<p>Some EAP authentication methods require use of certificates. EAP-TLS uses both server side and client certificates whereas EAP-PEAP and EAP-TTLS only require the server side certificate. When client certificate is used, a matching private key file has to also be included in configuration. If the private key uses a passphrase, this has to be configured in wpa_supplicant.conf (&quot;private_key_passwd&quot;). </p>
<p> wpa_supplicant supports X.509 certificates in PEM and DER formats. User certificate and private key can be included in the same file. </p>
<p> If the user certificate and private key is received in PKCS#12/PFX format, they need to be converted to suitable PEM/DER format for wpa_supplicant. This can be done, e.g., with following commands: </p>
<dl>
<dd>
<pre># convert client certificate and private key to PEM format
openssl pkcs12 -in example.pfx -out user.pem -clcerts
# convert CA certificate (if included in PFX file) to PEM format
openssl pkcs12 -in example.pfx -out ca.pem -cacerts -nokeys</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8) <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1) </p>
