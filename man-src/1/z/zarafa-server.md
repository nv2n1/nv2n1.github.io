---
title: "zarafa-server(1)"
name: "zarafa-server"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-server/"
description: "zarafa-server – Start the Zarafa storage server."
---

<h2 class="name">NAME</h2>
<p> zarafa-server &#8211; Start the Zarafa storage server. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-server</code> [<i>OPTION</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The zarafa-server is the Zafara storage server. It contacts a database server and provides services to Zarafa clients. The user base can be retreived from an external source, like LDAP, or can be setup with a separate list of users. </p>
<p> After starting, the server keeps listening for connections on the configured TCP port and/or Unix socket.</p>
<h2>OPTIONS</h2>
<p> The Zarafa server program takes the following configuration options: </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>file</i></p>
<dl>
<dt>
<dd> Specify the location of the configuration file. </p>
<p> Default: <i>/etc/zarafa/server.cfg</i></dl>
<p> <code>&#8211;foreground</code>, <code>-F</code></p>
<dl>
<dt>
<dd> Run in the foreground. Normally the server will daemonize and run in the background.</dl>
<p> <code>&#8211;restart-searches</code>, <code>-R</code></p>
<dl>
<dt>
<dd> Rebuild all search folders. This may take some time and is only needed when your search folders have become out-of-sync with the actual data in the database. The sync will start synchronously at the start of the server, and you will have to wait for all searches to complete before connecting to the server.</dl>
<p> <code>&#8211;ignore-database-version-conflict</code></p>
<dl>
<dt>
<dd> Ignore version information from the database. Zarafa will normally not start the server if the database has a newer version than the zarafa-server binary. This makes sure you cannot downgrade your server binary while keeping the same database. If you know what you&#8217;re doing, you can use this option to bypass the start-up version check of the database.</dl>
<p> <code>&#8211;ignore-attachment-storage-conflict</code></p>
<dl>
<dt>
<dd> Override the attachment storage option from the configuration file. When you change the option of the location where to store attachments after you&#8217;ve already started the zarafa-server once, this location will conflict. Attachments will not be found when they are stored in a different location.</dl>
<p> <code>&#8211;override-multiserver-lock</code></p>
<dl>
<dt>
<dd> When you upgrade/downgrade from/to multiserver setups, the server will not start, because of database differences. If you know what you&#8217;re doing, and want to circumvent this and start the server anyway, you can use this option.</dl>
<p> <code>&#8211;force-database-upgrade</code></p>
<dl>
<dt>
<dd> The upgrade from 6.x to 7.0 is blocked, since it will take a long time. We provide 2 methods to upgrade the database. One is using the preferred zarafa7-upgrade python script. This is preferred since it shows the upgrade progress, and you can estimate the time it will take for the upgrade to complete. The second option is letting the zarafa-server do the normal upgrade as usual. Pass this option to use this method. The server will only daemonize when the upgrade is complete. Simple progress can be followed in the log output of the server.</dl>
<p> <code>&#8211;ignore-unknown-config-options</code></p>
<dl>
<dt>
<dd> When unknown options exists in the configuration file the server will report an error and shutdown. Pass this option to ignore unknown options so the server will start.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Print the version and exit.</dl>
<p> When invoked with no options, the server will search for a configuration file in /etc/zarafa/server.cfg. If no configuration file is found, default values are used. See <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) for all configuration options and their default values.</p>
<h2>USAGE</h2>
<p> Starting the server with an alternative configuration: </p>
<p> <code>zarafa-server</code><code>-c</code><i>/path/to/server.cfg</i> </p>
<p> You may also use the init.d scripts: </p>
<p> <code>/etc/init.d/zarafa-server</code> [<i>start</i>| <i>stop</i>| <i>restart</i>]</p>
<h2>FILES</h2>
<p> /etc/zarafa/server.cfg</p>
<dl>
<dt>
<dd> The server configuration file.</dl>
<p> /etc/zarafa/license/base, /etc/zarafa/license/*</p>
<dl>
<dt>
<dd> The base file contains your license key. When you have extra CAL license keys, these are found in the other files available in the license/ directory, one key per file. This directory is configurable.</dl>
<p> Configuration options for user plugins are in their respective configuration file. The name of these files is set in the server.cfg file. See <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) for information on the server.cfg settings.</p>
<h2>DIAGNOSTICS</h2>
<p> If you run into problems, check the log for any errors. If you made a mistake in the configuration of the log method, this will be reported on standard error. You can also restart the server with a higher log level. Also, before starting the server, always make sure the database server is running at the right location and no other server is listening on the configured TCP port. </p>
<p> For extended diagnostics, there are special extended log options available for enhanced debugging capabilities. The parameter <i>log_level</i> has special or-ed values which can be set to investigate different modules within the server process: </p>
<p> SQL: 0x00010000, User backend: 0x00020000, Server cache: 0x00040000, SOAP: 0x00100000, ICS: 0x00200000 </p>
<p> For example, if you are using LDAP as the user plugin, you can set the <i>log_level</i> to 0x00020006 for extended LDAP logging (the last digit 6 enables extended verbose logging). To enable SQL and LDAP logging at the same time, set <i>log_level</i> to 0x00030006 </p>
<p> WARNING: The log options create huge amounts of log entries in production environments, this results in abnormal large logfiles which can fill up available disk space very fast. Only use this with extreme caution.</p>
<h2>SECURITY</h2>
<p> The normal way for user clients to connect to the server is over TCP, either direct using the Zarafa port, or over HTTP when Apache is setup as a proxy. Users can only login with their username and password. </p>
<p> The normal way for admin clients, like the spooler and admin tool, to connect to the server is through the Unix socket on Unix type servers. The admin clients are able to login when they are run as root or as the user the Zarafa server process is running as. Most of the time this will be root only, since the Zarafa server process runs as root by default. </p>
<p> As an exception for the dagent, a unix user can also connect to it&#8217;s own store without a password. Any other store cannot be accessed this way. </p>
<p> Direct SSL connections are also possible. The server needs to be configured to accept SSL connections on a new port. Login via an SSL key is also possible. Please read the next section on how to setup SSL.</p>
<h2>SSL</h2>
<p> To accept SSL connections directly by the server, the Zarafa server will need to listen on a different port to separate the normal connections from the encrypted connections. This is set in the <i>server_ssl_port</i> setting in the configuration file. </p>
<p> Then, you must setup a signed SSL certificate. First, we&#8217;ll create a Certificate Authority to be able to sign certificate requests. We provide a script which makes it easy to create certificates on any distribution. This script is located in /usr/share/zarafa, called ssl-certificate.sh. Enter the following commands to create a certificate for the Zarafa server. </p>
<p> <code> mkdir -p /etc/zarafa/ssl </code><code> cd /etc/zarafa/ssl </code><code> sh /usr/share/zarafa/ssl-certificate.sh server </code> </p>
<p> Press enter twice to start the creation of a new CA, probably called demoCA. Enter a password when asked for. This is the password later used to sign certificate requests. Then enter your certificate information. Do not leave the Common Name field blank, otherwise the creation will fail. A good example for the Common Name field is your hostname. </p>
<p> Now that we have a CA, we can create self-signed certificates. The script will automatically start the creation of this certificate. The CA certificate must be set in the server.cfg file in the <i>server_ssl_ca_file</i> setting. We need a signed certificate for the server to start with SSL support. </p>
<p> Enter a password for the request, and enter the certificate details. Some details need to be different from what you typed when creating the CA. Type at least a different name in the &#8216;Organizational Unit Name&#8217; field. The challenge password at the end may be left empty. </p>
<p> The script will automatically continue with signing this certificate request. You will need to enter your CA certificate password again to sign this request. Then you must accept the new certificate into the CA. </p>
<p> After accepting, a new signed certificate is created, with the name server.pem. This file contains the private key, so keep this file safe. </p>
<p> The script will ask if a public key should also be created. Since we&#8217;re creating the certificate for the server, this is not needed. So enter &#8216;n&#8217; and press enter. </p>
<p> The server.pem file should be set in the server.cfg file in the <i>server_ssl_key_file</i> option. See <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) for information on the possible SSL settings. The password of this key needs to be set in the <i>server_ssl_key_pass</i> option. Do not forget this password in the server.cfg file, otherwise the zarafa-server program will ask for this password when an SSL connection is accepted. </p>
<p> To create a new certificate for a client service, run the script again. You can create one new certificate for all clients, or seperate certificates for each client. </p>
<p> <code> sh /usr/share/zarafa/ssl-certificates.sh </code> </p>
<p> When typing the certificate information, type at least a different &#8216;Organizational Unit Name&#8217; field. When asked for a public key, type &#8216;y&#8217; and enter to create the public key. </p>
<p> Install the new service.pem on the server that will be logging in. Install the service-public.pem file in the /etc/zarafa/sslkeys directory: </p>
<p> <code> mkdir /etc/zarafa/sslkeys </code><code> mv service-public.pem /etc/zarafa/sslkeys </code> </p>
<p> The remote service, which has the service.pem private key, can now login with the certificate, because the known public key matches.</p>
<h2>ADDRESSBOOK SORTING</h2>
<p> With special chars (like umlauts) the sorting is working more the dictionary way according to DIN 5007-1, section 6.1.1.4.1. Depending on the behaviour wanted, the collation setting can be changed with the (not per default included) parameter <i> default_sort_locale_id</i>. When setting this parameter to de_DE [at] collation=phonebook for example the sorting will be oriented to the DIN 5007-2, section 6.1.1.4.2 standard which is rather used in phonebooks and actually decomposes umlauts for sorting inline within non-umlaut based ASCII characters.</p>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the Zarafa server process: </p>
<p> <code>HUP</code></p>
<dl>
<dt>
<dd> When the HUP signal is received, some options from the configuration file are reloaded. The reloadable options are listed in the <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) manual page. </p>
<p> Also, when using <i>log_method = file</i>, the logfile will be closed and a new logfile will be opened. You can use this signal in your logrotate system.</dl>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> To gracefully let the server exit, the normal TERM signal is used. Because of open sessions by clients it may take up to 60 seconds for the server to completely shutdown.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5)<code><a href="/docs/linux/man/1-zarafa-admin/">zarafa-admin</a></code>(1) </p>
<h2>Index</h2>
