---
title: "sge_ca(8)"
name: "sge_ca"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_ca/"
description: "util/sgeCA/sge_ca – xxQS_NAMExx CSP Support control command"
---

<p>util/sgeCA/sge_ca &#8211; xxQS_NAMExx CSP Support control command</p>
<h2>Syntax</h2>
<p><code>sge_ca</code> <i>command</i> [<i>command options</i>]</p>
<h2>Description</h2>
<p><i></i><code>sge_ca</code> controls a simple xxQS_NAMExx Certificate Authority that is used for the special Certificate Security Protocol (CSP) mode. CSP mode improves the security behavior of xxQS_NAMExx by enabling OpenSSL secured communication channels and X509v3 certificates for authentication. In addition it is possible to export the key material or to create JKS keystores for the JMX connector. There follows a list of possible commands and command options to give an overview of what functionality is available. For further details about every command refer to the COMMAND DETAILS section.</p>
<h2>Command Overview</h2>
<dl>
<dt><code>-help</code></p>
<dd>Show usage.</p>
<dt><code>-init </code>[<i>command options</i>]</p>
<dd>Create the infrastructure for a new xxQS_NAMExx Certificate Authority with its corresponding files and directories, and a set of keys and certificates for the xxQS_NAMExx daemon, root and admin user.</p>
<dt><code>-req </code>|<code> -verify </code><i>cert</i> |<code> -sign </code>|<code> -copy </code>[<i>command options</i>]</p>
<dd>Manipulate individual keys and certificates.</p>
<dt><code>-print </code><i>cert</i> |<code> -printkey</code> <i>key</i> |<code> -printcrl</code> <i>crl</i></p>
<dd>Print out certificates, keys and certificate revocation lists in human readable form.</p>
<dt><code>-showCaTop </code>|<code> -showCaLocalTop </code>[<i>command options</i>]</p>
<dd>Echo the $CATOP or $CALOCALTOP directory. This command is usually run as root on the qmaster host after a CA infrastructure has been created. If &quot;<code>-cadir</code>&quot;, &quot;<code>-catop</code>&quot; or &quot;<code>-calocaltop</code>&quot; are set, the corresponding directories are printed.</p>
<dt><code>-usercert</code> <i>user file</i> |<code> -user</code> <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i> |<code> -sdm_daemon</code> <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i> [<i>command options</i>]</p>
<dd>Create certificates and keys for a bunch of users contained in <i>user file</i>, a single user, or SDM daemon in the form <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i>.</p>
<dt><code>-pkcs12</code> <i>user</i> |<code> -sdm_pkcs12</code> <i>g</i> |<code> -sys_pkcs12 </code>[<i>command options</i>]</p>
<dd>Export the certificate and key for user <i>user</i> or SDM daemon <i>g</i> in PKCS12 format and to export the xxQS_NAMExx daemon certificate and key in PKCS12 format.</p>
<dt><code>-userks </code>|<code> -ks</code> <i>user</i> |<code> -sysks </code>[<i>command options</i>]</p>
<dd>Create keystore for all users with a certificate and key, the keystore for a single user <i>user</i>, or the keystore containing the xxQS_NAMExx daemon certificate and key.</p>
<dt><code>-renew</code> <i>user</i> |<code> -renew_ca </code>|<code> -renew_sys </code>|<code> -renew_sdm</code> <i>g</i> [<i>command options</i>]</p>
<dd>Renew the certificate for user <i>user</i>, for the CA, for the xxQS_NAMExx daemon, or the SDM daemon with common name <i>g</i>. The old certificate remains valid until it expires. NB. The option of this name was re-named to <code>-rrenew</code> in xxQS_NAMExx 8.1.9.</p>
<dt><code>-rrenew</code> <i>user</i> |<code> -rrenew_ca </code>|<code> -rrenew_sys </code>|<code> -rrenew_sdm</code> <i>g</i> [<i>command options</i>]</p>
<dd>Renew the certificate for user <i>user</i>, for the CA, for the xxQS_NAMExx daemon, or the SDM daemon with common name <i>g</i>, and revoke the old ones (updating the revocation list). NB. This requires <code>unique_subject=no</code> in <i>sge_ssl_template.cnf</i>, which is the default for new installations, but might not be set for old ones.</p>
<dt><code>-revoke</code> <i>cert</i></p>
<dd>Revoke the certificate <i>cert</i>, which should be an actual PEM file, updating the revocation list.</dl>
<p> In the above, &quot;<i>command options</i>&quot; is a combination of the following options depending on the command. The COMMAND DETAILS section explains which options are usable for each command.</p>
<dl>
<dt><code>-days</code> <i>days</i></p>
<dd>days of validity of the certificate</p>
<dt><code>-sha1</code></p>
<dd>Use SHA-1 instead of MD5 as message digest</p>
<dt><code>-encryptkey</code></p>
<dd>Use DES to encrypt the generated private key with a passphrase. The passphrase is requested when a key is created or used.</p>
<dt><code>-outdir</code> <i>dir</i></p>
<dd>Write to directory <i>dir</i></p>
<dt><code>-cahost</code> <i>host</i></p>
<dd>Define CA hostname (CA master host)</p>
<dt><code>-cadir</code> <i>dir</i></p>
<dd>Define $CALOCALTOP and $CATOP settings as <i>dir</i>.</p>
<dt><code>-calocaltop </code><i>dir</i></p>
<dd>Define $CALOCALTOP setting</p>
<dt><code>-catop</code> <i>dir</i></p>
<dd>Define $CATOP setting</p>
<dt><code>-kspwf</code> <i>file</i></p>
<dd>Define a keystore password file that contains a password that is used to encrypt the keystore and the keys contained therein</p>
<dt><code>-ksout</code> <i>file</i></p>
<dd>Define output file to write the keystore to</p>
<dt><code>-pkcs12pwf</code> <i>file</i></p>
<dd>Define a PKCS12 password file that contains a password that is used to encrypt the PKCS12 export file and the keys contained therein</p>
<dt><code>-pkcs12dir</code> <i>dir</i></p>
<dd>Define the output directory <i>dir</i> to write the exported PKCS12 format file to. Otherwise the current working directory is used.</dl>
<h2>Command Details</h2>
<dl>
<dt><code>sge_ca -init </code>[<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>num days</i>]</p>
<dd>The <code>-init</code> command creates a new xxQS_NAMExx certificate authority and its corresponding files. Usually &quot;<code>sge_ca -init</code>&quot; is run by user root on the master host. If the options <code>-adminuser</code>, <code>-cadir</code>, <code>-calocaltop</code>, and <code>-catop</code> are not used, and the xxQS_NAMExx environment variables SGE_ROOT, SGE_CELL and SGE_QMASTER_PORT are set, the CA directories are created in the following locations: <i>$SGE_ROOT/$SGE_CELL/common/sgeCA</i> (can be overruled by <code>-catop</code> <i>dir</i> or <code>-cadir</code> <i>dir</i>)<br />
 <i>/var/lib/sgeCA/port$SGE_QMASTER_PORT/$SGE_CELL</i> or <i>/var/lib/sgeCA/sge_qmaster/$SGE_CELL</i> (can be overruled by <code>-calocaltop</code> <i>dir</i> or <code>-cadir</code> <i>dir</i>).<br />
 The following information must be delivered for the site: two letter country code, state, location, e.g. city or your building code, organization (e.g. your company name), organizational unit, e.g. your department, and email address of the CA administrator (you!).</dl>
<p> Certificates and keys are generated for the CA itself, the xxQS_NAMExx daemon, installation user (usually root), and finally for the admin user. </p>
<p> How and where the certificates and keys are created can be influenced additionally by:</p>
<dl>
<dt><code>-days</code> <i>days</i></p>
<dd>Change the time of validity of the certificates to number of <i>days</i> instead of 365 days</p>
<dt><code>-sha1</code></p>
<dd>Change the message digest algorithm from MD5 to SHA-1</p>
<dt><code>-encryptkey</code></p>
<dd>Encrypt the generated keys with a passphrase</p>
<dt><code>-adminuser</code> <i>user</i></p>
<dd>Use <i>user</i> as admin user</p>
<dt><code>-cahost</code> <i>host</i></p>
<dd>Use <i>host</i> as the CA master host</p>
<dt>[<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>]</p>
<dd>Set $CATOP and $CALOCALTOP to <i>dir</i> to use something other than the xxQS_NAMExx default directories. Either <code>-cadir</code> <i>dir</i> has to be specified to replace $CATOP and $CALOCALTOP by the same directory or <code>-catop</code> <i>dir</i> for $CATOP and <code>-calocaltop</code> <i>dir</i> for $CALOCALTOP.</p>
<dt><code>sge_ca -user</code> <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>]</p>
<dd>Generate user certificate and keys for <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i>, where <i>u</i> is the user id, <i>g</i> is the &quot;common name&quot; (real name of the user), and <i>e</i> is the user&#8217;s email address. By default the certificate is valid for 365 days or for <i>days</i>, as specified with <code>-days</code> <i>days</i>. This command is usually run as user root on the qmaster host. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code>, and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -sdm_daemon</code> <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i></p>
<dd>Generate daemon certificate and keys for <i>u</i><code>:</code><i>g</i><code>:</code><i>e</i> with parameters and lifetime as for <code>-user</code>. This command is usually run as user root on the qmaster host.</p>
<dt><code>sge_ca -usercert</code> <i>user file</i> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>] [<code>-encryptkey</code>] [<code>-sha1</code>]</p>
<dd>Usually <code>sge_ca</code> <code>-usercert</code> <i>user file</i> is run as user root on the master host. The argument <i>user file</i> contains a list of users in the following format: </p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;eddy:Eddy Smith:eddy [at] griders.org</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sarah:Sarah Miller:sarah [at] griders.org</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;leo:Leo Lion:leo [at] griders.org</p>
<dl>
<dd>where the fields separated by colon are:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Unix user:Gecos field:email address</p>
<dl>
<dt><code>sge_ca -renew</code> <i>user</i> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>]</p>
<dd>Renew the certificate for <i>user</i>. By default the certificate is extended for 365 days or for <i>days</i> specified with <code>-days</code> <i>days</i>. If the value is negative the certificate becomes invalid. This command is usually run as user root on the qmaster host. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code>, and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -renew_ca</code> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>]</p>
<dd>Renew the CA certificate, similarly to <code>-renew</code>.</p>
<dt><code>sge_ca -renew_sys</code> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>]</p>
<dd>Renew the xxQS_NAMExx daemon certificate, similarly to <code>-renew</code>.</p>
<dt><code>sge_ca -renew_sdm</code> <i>g</i> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>]</p>
<dd>Renew the SDM daemon certificate of <i>g</i>, where <i>g</i> is the common name of the daemon, similarly to <code>-renew</code>.</p>
<dt><code>sge_ca -pkcs12</code> <i>user</i> [<code>-pkcs12pwf</code> <i>file</i>] [<code>-pkcs12dir</code> <i>dir</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Export certificate and key of user <i>user</i> (Unix user name) in PKCS12 format. This command is usually run as user root on the qmaster host. If <code>-pkcs12pwf</code> <i>file</i> is used, the file and the corresponding key will be encrypted with the password in <i>file</i>. If <code>-pkcs12dir</code> <i>dir</i> is used, the output file is written into <i>dir</i>/<i>user</i>.p12 instead of ./<i>user</i>.p12. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code>, and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -sys_pkcs12</code> [<code>-pkcs12pwf</code> <i>file</i>] [<code>-pkcs12dir</code> <i>dir</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Export certificate and key of xxQS_NAMExx daemon in PKCS12 format, similarly to <code>-pkcs12</code>.</p>
<dt><code>sge_ca -sdm_pkcs12</code> <i>g</i> [<code>-pkcs12pwf</code> <i>file</i>] [<code>-pkcs12dir</code> <i>dir</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Export certificate and key of SDM daemon with common name <i>g</i> in PKCS12 format,, similarly to <code>-renew</code>.</p>
<dt><code>sge_ca -ks</code> <i>user</i> [<code>-ksout</code> <i>file</i>] [<code>-kspwf</code> <i>file</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Create a keystore containing certificate and key of user <i>user</i> in JKS format where <i>user</i> is the Unix user name. This command is usually run as user root on the qmaster host. If <code>-kspwf</code> <i>file</i> is used the keystore and the corresponding key will be encrypted with the password in <i>file</i>. The <code>-ksout</code> <i>file</i> option specifies the keystore file that is created. If the <code>-ksout</code> <i>file</i> option is missing the default location for the keystore is $CALOCALTOP/userkeys/<i>user</i>/keystore. This command is usually invoked by <code>sge_ca -userks</code>. A prerequisite is a valid JAVA_HOME environment variable setting. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code> and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -userks</code> [<code>-kspwf</code> <i>file</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Generate a keystore in JKS format for all users having a key and certificate. This command is usually run as user root on the qmaster host. If <code>-kspwf</code> <i>file</i> is used, the keystore and the corresponding key will be encrypted with the password in <i>file</i>. The keystore files are created in $CALOCALTOP/userkeys/<i>user</i>/keystore. This command is run after user certificates and keys have been created with Bsge_ca -usercert <i>userfile</i> or if any of the certificates have been renewed. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code> and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -sysks</code> [<code>-kspwf</code> <i>file</i>] [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Generate a keystore containing the xxQS_NAMExx daemon certificate and key in JKS format. This command is usually run as user root on the qmaster host. If <code>-kspwf</code> <i>file</i> is used the keystore and the corresponding key will be encrypted with the password in <i>file</i>. The keystore file is created in $CALOCALTOP/private/keystore. $CATOP and $CALOCALTOP may be overruled by <code>-cadir</code>, <code>-catop</code> and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -print</code> <i>cert</i></p>
<dd>Print a PEM-format certificate <i>cert</i>.</p>
<dt><code>sge_ca -printkey</code> <i>key</i></p>
<dd>Print a PEM-format key <i>key</i>.</p>
<dt><code>sge_ca -printcrl</code> <i>crl</i></p>
<dd>Print a PEM-format certificate revocation list <i>crl</i>.</p>
<dt><code>sge_ca -req</code> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>] [<code>-encryptkey</code>] [<code>-sha1</code>] [<code>-outdir</code> <i>dir</i>]</p>
<dd>Create a private key and a certificate request for the calling user. These are created as newkey.pem and newreq.pem in the current working directory. If the option -outdir <i>dir</i> is specified in addition the files are created in <i>dir</i>.</p>
<dt><code>sge_ca -sign</code> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>] [<code>-days</code> <i>days</i>] [<code>-encryptkey</code>] [<code>-sha1</code>] [<code>-outdir</code> <i>dir</i>]</p>
<dd>Sign a certificate request. The CA certificate under $CATOP (default $SGE_ROOT/$SGE_CELL/common/sgeCA), and CA key from $CALOCALTOP (default /var/sgaCA/{port$SGE_QMASTER_PORT|sge_qmaster}/$SGE_CELL) are used for the signature. If $CATOP and $CALOCALTOP are set to a different directory the information there is used. The certificate is created as newcert.pem in the current working directory or in <i>dir</i> if the option <code>-outdir</code> <i>dir</i> has been specified. In addition the option &quot;<code>-days</code> <i>number of days</i>&quot; can be specified to change the default validity from 365 to number of days.</p>
<dt><code>sge_ca -verify</code> <i>cert</i> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>] [<code>-adminuser</code> <i>admin</i>]</p>
<dd>Verify a certificate&#8217;s validity where <i>cert</i> is the certificate in pem format. $CATOP and $CALOCALTOP can be overruled by <code>-cadir</code>, <code>-catop</code> and <code>-calocaltop</code>.</p>
<dt><code>sge_ca -copy</code> [<code>-cadir</code> <i>dir</i>] [<code>-catop</code> <i>dir</i>] [<code>-calocaltop</code> <i>dir</i>]</p>
<dd>Run by a user to copy their certificate and key on the master host to $HOME/.sge/port$SGE_QMASTER_PORT/$SGE_CELL/certs/cert.pem and the corresponding private key to $HOME/.sge/port$SGE_QMASTER_PORT/$SGE_CELL/private/key.pem, which are used instead of the files in $CATOP and $CALOCALTOP. The command is only recommended for testing purposes, or where $HOME is on a secure shared file system. </p>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Examples</h2>
<dl>
<dt># sge_ca -init -cadir /tmp -sha1 -encryptkey -days 31</p>
<dd>Create a CA infrastructure in /tmp with a certificate validity of 31 days using SHA-1 instead of MD5 as message digest. The keys are encrypted and a passphrase has to be entered during the creation of the different keys or during signing a certificate with the created CA key.</p>
<dt># sge_ca -usercert /tmp/myusers.txt -cadir /tmp</p>
<dd>/tmp/myusers.txt contains<br />
 user1:My User:user1 [at] myorg.org<br />
 and user1 is a valid Unix user account. Create a key and certificate for user1.</p>
<dt># sge_ca -userks -cadir /tmp</p>
<dd>Create a keystore for all users of the simple CA. The keystore is stored under /tmp/userkeys/<i>user</i>/keystore.</p>
<dt># sge_ca -renew root -cadir /tmp -days -1</p>
<dd>Make the root certificate temporarily invalid.</p>
<dt># sge_ca -renew_ca -days 365 -cadir /tmp</p>
<dd>Renew the CA certificate for 365 days.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>SGE_ROOT</code></p>
<dd>Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>SGE_CELL</code></p>
<dd>If set, specifies the default xxQS_NAMExx cell.</dl>
<h2>Restrictions</h2>
<p>The command must usually be called with xxQS_NAMExx root permissions on the master host. For more details on the permission requirements consult the detailed description for the different commands above.</p>
<h2>Files</h2>
<p><code>sge_ca</code> creates a file tree starting in <code>$CATOP</code> and <code>$CALOCALTOP</code>. The default for <code>$CATOP</code> is usually $SGE_ROOT/$SGE_CELL/common/sgeCA and for <code>$CALOCALTOP</code> /var/lib/sgeCA/{port$SGE_QMASTER_PORT|sge_qmaster}/$SGE_CELL where the subpaths beginning with $ expand to the content of the corresponding environment variable. </p>
<p> In addition there may optionally exist the user certificate in $HOME/.sge/port$SGE_QMASTER_PORT/$SGE_CELL/certs/cert.pem and the corresponding private key in $HOME/.sge/port$SGE_QMASTER_PORT/$SGE_CELL/private/key.pem which are used instead of the files in $CATOP and $CALOCALTOP. (See <code>sge_ca -copy</code> above.) </p>
<p> <i>SGE_ROOT/util/sgeCA/sge_ssl_template.cnf</i>: OpenSSL configuration file. </p>
<p> <i>SGE_ROOT/util/sgeCA/sge_ssl.cnf</i>: OpenSSL configuration file used for signing.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
