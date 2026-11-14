---
title: "puppet-conf(5)"
name: "puppet-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-puppet-conf/"
---

<h2>Configuration Settings</h2>
<dl>
<dt>&bull;</p>
<dd>Each of these settings can be specified in <code>puppet.conf</code> or on the command line.</p>
<dt>&bull;</p>
<dd>When using boolean settings on the command line, use <code>&#8211;setting</code> and <code>&#8211;no-setting</code> instead of <code>&#8211;setting (true|false)</code>.</p>
<dt>&bull;</p>
<dd>Settings can be interpolated as <code>$variables</code> in other settings; <code>$environment</code> is special, in that puppet master will interpolate each agent node&#8217;s environment instead of its own.</p>
<dt>&bull;</p>
<dd>Multiple values should be specified as comma-separated lists; multiple directories should be separated with the system path separator (usually a colon).</p>
<dt>&bull;</p>
<dd>Settings that represent time intervals should be specified in duration format: an integer immediately followed by one of the units &#8216;y&#8217; (years of 365 days), &#8216;d&#8217; (days), &#8216;h&#8217; (hours), &#8216;m&#8217; (minutes), or &#8216;s&#8217; (seconds). The unit cannot be combined with other units, and defaults to seconds when omitted. Examples are &#8216;3600&#8217; which is equivalent to &#8216;1h&#8217; (one hour), and &#8216;1825d&#8217; which is equivalent to &#8216;5y&#8217; (5 years).</p>
<dt>&bull;</p>
<dd>Settings that take a single file or directory can optionally set the owner, group, and mode for their value: <code>rundir = $vardir/run { owner = puppet, group = puppet, mode = 644 }</code></p>
<dt>&bull;</p>
<dd>The Puppet executables will ignore any setting that isn&#8217;t relevant to their function.</p>
<dd></dl>
<p> See the configuration guide <i><a rel="nofollow" href="http://docs.puppetlabs.com/guides/configuring.html">http://docs.puppetlabs.com/guides/configuring.html</a></i> for more details.</p>
<h3>agent_catalog_run_lockfile</h3>
<p>A lock file to indicate that a puppet agent catalog run is currently in progress. The file contains the pid of the process that holds the lock on the catalog run.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/agent_catalog_run.lock</p>
<dd></dl>
<h3>agent_disabled_lockfile</h3>
<p>A lock file to indicate that puppet agent runs have been administratively disabled. File contains a JSON object with state information.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/agent_disabled.lock</p>
<dd></dl>
<h3>allow_duplicate_certs</h3>
<p>Whether to allow a new certificate request to overwrite an existing certificate.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>allow_variables_with_dashes</h3>
<p>Permit hyphens (<code>&#8211;</code>) in variable names and issue deprecation warnings about them. This setting <code>should always be false</code>; setting it to <code>true</code> will cause subtle and wide-ranging bugs. It will be removed in a future version. Hyphenated variables caused major problems in the language, but were allowed between Puppet 2.7.3 and 2.7.14. If you used them during this window, we apologize for the inconvenience &#8212; you can temporarily set this to <code>true</code> in order to upgrade, and can rename your variables at your leisure. Please revert it to <code>false</code> after you have renamed all affected variables.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>archive_file_server</h3>
<p>During an inspect run, the file bucket server to archive files to if archive_files is set.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $server</p>
<dd></dl>
<h3>archive_files</h3>
<p>During an inspect run, whether to archive files whose contents are audited to a file bucket.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>async_storeconfigs</h3>
<p>Whether to use a queueing system to provide asynchronous database integration. Requires that <code>puppet queue</code> be running.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>autoflush</h3>
<p>Whether log files should always flush to disk.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>autosign</h3>
<p>Whether to enable autosign. Valid values are true (which autosigns any key request, and is a very bad idea), false (which never autosigns any key request), and the path to a file, which uses that configuration file to determine which keys to sign.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/autosign.conf</p>
<dd></dl>
<h3>bindaddress</h3>
<p>The address a listening server should bind to.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 0.0.0.0</p>
<dd></dl>
<h3>bucketdir</h3>
<p>Where FileBucket files are stored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/bucket</p>
<dd></dl>
<h3>ca</h3>
<p>Whether the master should function as a certificate authority.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>ca_name</h3>
<p>The name to use the Certificate Authority certificate.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: Puppet CA: $certname</p>
<dd></dl>
<h3>ca_port</h3>
<p>The port to use for the certificate authority.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $masterport</p>
<dd></dl>
<h3>ca_server</h3>
<p>The server to use for certificate authority requests. It&#8217;s a separate server because it cannot and does not need to horizontally scale.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $server</p>
<dd></dl>
<h3>ca_ttl</h3>
<p>The default TTL for new certificates. If this setting is set, ca_days is ignored. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 5y</p>
<dd></dl>
<h3>cacert</h3>
<p>The CA certificate.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/ca_crt.pem</p>
<dd></dl>
<h3>cacrl</h3>
<p>The certificate revocation list (CRL) for the CA. Will be used if present but otherwise ignored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/ca_crl.pem</p>
<dd></dl>
<h3>cadir</h3>
<p>The root directory for the certificate authority.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/ca</p>
<dd></dl>
<h3>cakey</h3>
<p>The CA private key.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/ca_key.pem</p>
<dd></dl>
<h3>capass</h3>
<p>Where the CA stores the password for the private key</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $caprivatedir/ca.pass</p>
<dd></dl>
<h3>caprivatedir</h3>
<p>Where the CA stores private certificate information.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/private</p>
<dd></dl>
<h3>capub</h3>
<p>The CA public key.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/ca_pub.pem</p>
<dd></dl>
<h3>catalog_cache_terminus</h3>
<p>How to store cached catalogs. Valid values are &#8216;json&#8217; and &#8216;yaml&#8217;. The agent application defaults to &#8216;json&#8217;.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>catalog_format</h3>
<p>(Deprecated for &#8216;preferred_serialization_format&#8217;) What format to use to dump the catalog. Only supports &#8216;marshal&#8217; and &#8216;yaml&#8217;. Only matters on the client, since it asks the server for a specific format.</p>
<h3>catalog_terminus</h3>
<p>Where to get node catalogs. This is useful to change if, for instance, you&#8217;d like to pre-compile catalogs and store them in memcached or some other easily-accessed store.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: compiler</p>
<dd></dl>
<h3>cert_inventory</h3>
<p>A Complete listing of all certificates</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/inventory.txt</p>
<dd></dl>
<h3>certdir</h3>
<p>The certificate directory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/certs</p>
<dd></dl>
<h3>certdnsnames</h3>
<p>The <code>certdnsnames</code> setting is no longer functional, after CVE-2011-3872. We ignore the value completely. For your own certificate request you can set <code>dns_alt_names</code> in the configuration and it will apply locally. There is no configuration option to set DNS alt names, or any other <code>subjectAltName</code> value, for another nodes certificate. Alternately you can use the <code>&#8211;dns_alt_names</code> command line option to set the labels added while generating your own CSR.</p>
<h3>certificate_expire_warning</h3>
<p>The window of time leading up to a certificate&#8217;s expiration that a notification will be logged. This applies to CA, master, and agent certificates. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 60d</p>
<dd></dl>
<h3>certificate_revocation</h3>
<p>Whether certificate revocation should be supported by downloading a Certificate Revocation List (CRL) to all clients. If enabled, CA chaining will almost definitely not work.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>certname</h3>
<p>The name to use when handling certificates. Defaults to the fully qualified domain name.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: sirrus.puppetlabs.lan</p>
<dd></dl>
<h3>classfile</h3>
<p>The file in which puppet agent stores a list of the classes associated with the retrieved configuration. Can be loaded in the separate <code>puppet</code> executable using the <code>&#8211;loadclasses</code> option.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/classes.txt</p>
<dd></dl>
<h3>client_datadir</h3>
<p>The directory in which serialized data is stored on the client.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/client_data</p>
<dd></dl>
<h3>clientbucketdir</h3>
<p>Where FileBucket files are stored locally.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/clientbucket</p>
<dd></dl>
<h3>clientyamldir</h3>
<p>The directory in which client-side YAML data is stored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/client_yaml</p>
<dd></dl>
<h3>code</h3>
<p>Code to parse directly. This is essentially only used by <code>puppet</code>, and should only be set if you&#8217;re writing your own Puppet executable</p>
<h3>color</h3>
<p>Whether to use colors when logging to the console. Valid values are <code>ansi</code> (equivalent to <code>true</code>), <code>html</code>, and <code>false</code>, which produces no color. Defaults to false on Windows, as its console does not support ansi colors.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: ansi</p>
<dd></dl>
<h3>confdir</h3>
<p>The main Puppet configuration directory. The default for this setting is calculated based on the user. If the process is running as root or the user that Puppet is supposed to run as, it defaults to a system directory, but if it&#8217;s running as any other user, it defaults to being in the user&#8217;s home directory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: /etc/puppet</p>
<dd></dl>
<h3>config</h3>
<p>The configuration file for the current puppet application</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/${config_file_name}</p>
<dd></dl>
<h3>config_file_name</h3>
<p>The name of the puppet config file.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet.conf</p>
<dd></dl>
<h3>config_version</h3>
<p>How to determine the configuration version. By default, it will be the time that the configuration is parsed, but you can provide a shell script to override how the version is determined. The output of this script will be added to every log message in the reports, allowing you to correlate changes on your hosts to the source version on the server.</p>
<h3>configprint</h3>
<p>Print the value of a specific configuration setting. If the name of a setting is provided for this, then the value is printed and puppet exits. Comma-separate multiple values. For a list of all values, specify &#8216;all&#8217;.</p>
<h3>configtimeout</h3>
<p>How long the client should wait for the configuration to be retrieved before considering it a failure. This can help reduce flapping if too many clients contact the server at one time. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 2m</p>
<dd></dl>
<h3>couchdb_url</h3>
<p>The url where the puppet couchdb database will be created</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: <a rel="nofollow" href="http://127.0.0.1:5984/puppet">http://127.0.0.1:5984/puppet</a></p>
<dd></dl>
<h3>csrdir</h3>
<p>Where the CA stores certificate requests</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/requests</p>
<dd></dl>
<h3>daemonize</h3>
<p>Whether to send the process into the background. This defaults to true on POSIX systems, and to false on Windows (where Puppet currently cannot daemonize).</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>data_binding_terminus</h3>
<p>Where to retrive information about data.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: hiera</p>
<dd></dl>
<h3>dbadapter</h3>
<p>The type of database to use.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: sqlite3</p>
<dd></dl>
<h3>dbconnections</h3>
<p>The number of database connections for networked databases. Will be ignored unless the value is a positive integer.</p>
<h3>dblocation</h3>
<p>The database cache for client configurations. Used for querying within the language.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/clientconfigs.sqlite3</p>
<dd></dl>
<h3>dbmigrate</h3>
<p>Whether to automatically migrate the database.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>dbname</h3>
<p>The name of the database to use.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>dbpassword</h3>
<p>The database password for caching. Only used when networked databases are used.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>dbport</h3>
<p>The database password for caching. Only used when networked databases are used.</p>
<h3>dbserver</h3>
<p>The database server for caching. Only used when networked databases are used.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: localhost</p>
<dd></dl>
<h3>dbsocket</h3>
<p>The database socket location. Only used when networked databases are used. Will be ignored if the value is an empty string.</p>
<h3>dbuser</h3>
<p>The database user for caching. Only used when networked databases are used.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>default_file_terminus</h3>
<p>The default source for files if no server is given in a uri, e.g. <a href="puppet:///file.">puppet:///file.</a> The default of <code>rest</code> causes the file to be retrieved using the <code>server</code> setting. When running <code>apply</code> the default is <code>file_server</code>, causing requests to be filled locally.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: rest</p>
<dd></dl>
<h3>deviceconfig</h3>
<p>Path to the device config file for puppet device</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/device.conf</p>
<dd></dl>
<h3>devicedir</h3>
<p>The root directory of devices&#8217; $vardir</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/devices</p>
<dd></dl>
<h3>diff</h3>
<p>Which diff command to use when printing differences between files. This setting has no default value on Windows, as standard <code>diff</code> is not available, but Puppet can use many third-party diff tools.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: diff</p>
<dd></dl>
<h3>diff_args</h3>
<p>Which arguments to pass to the diff command when printing differences between files. The command to use can be chosen with the <code>diff</code> setting.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: -u</p>
<dd></dl>
<h3>dns_alt_names</h3>
<p>The comma-separated list of alternative DNS names to use for the local host. When the node generates a CSR for itself, these are added to the request as the desired <code>subjectAltName</code> in the certificate: additional DNS labels that the certificate is also valid answering as. This is generally required if you use a non-hostname <code>certname</code>, or if you want to use <code>puppet kick</code> or <code>puppet resource -H</code> and the primary certname does not match the DNS name you use to communicate with the host. This is unnecessary for agents, unless you intend to use them as a server for <code>puppet kick</code> or remote <code>puppet resource</code> management. It is rarely necessary for servers; it is usually helpful only if you need to have a pool of multiple load balanced masters, or for the same master to respond on two physically separate networks under different names.</p>
<h3>document_all</h3>
<p>Document all resources</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>dynamicfacts</h3>
<p>(Deprecated) Facts that are dynamic; these facts will be ignored when deciding whether changed facts should result in a recompile. Multiple facts should be comma-separated.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: memorysize,memoryfree,swapsize,swapfree</p>
<dd></dl>
<h3>environment</h3>
<p>The environment Puppet is running in. For clients (e.g., <code>puppet agent</code>) this determines the environment itself, which is used to find modules and much more. For servers (i.e., <code>puppet master</code>) this provides the default environment for nodes we know nothing about.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: production</p>
<dd></dl>
<h3>evaltrace</h3>
<p>Whether each resource should log when it is being evaluated. This allows you to interactively see exactly what is being done.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>external_nodes</h3>
<p>An external command that can produce node information. The command&#8217;s output must be a YAML dump of a hash, and that hash must have a <code>classes</code> key and/or a <code>parameters</code> key, where <code>classes</code> is an array or hash and <code>parameters</code> is a hash. For unknown nodes, the command should exit with a non-zero exit code. This command makes it straightforward to store your node mapping information in other data sources like databases.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: none</p>
<dd></dl>
<h3>factpath</h3>
<p>Where Puppet should look for facts. Multiple directories should be separated by the system path separator character. (The POSIX path separator is &#8216;:&#8217;, and the Windows path separator is &#8216;;&#8217;.)</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/lib/facter:$vardir/facts</p>
<dd></dl>
<h3>facts_terminus</h3>
<p>The node facts terminus.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: facter</p>
<dd></dl>
<h3>fileserverconfig</h3>
<p>Where the fileserver configuration is stored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/fileserver.conf</p>
<dd></dl>
<h3>filetimeout</h3>
<p>The minimum time to wait between checking for updates in configuration files. This timeout determines how quickly Puppet checks whether a file (such as manifests or templates) has changed on disk. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 15s</p>
<dd></dl>
<h3>freeze_main</h3>
<p>Freezes the &#8216;main&#8217; class, disallowing any code to be added to it. This essentially means that you can&#8217;t have any code outside of a node, class, or definition other than in the site manifest.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>genconfig</h3>
<p>Whether to just print a configuration to stdout and exit. Only makes sense when used interactively. Takes into account arguments specified on the CLI.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>genmanifest</h3>
<p>Whether to just print a manifest to stdout and exit. Only makes sense when used interactively. Takes into account arguments specified on the CLI.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>graph</h3>
<p>Whether to create dot graph files for the different configuration graphs. These dot files can be interpreted by tools like OmniGraffle or dot (which is part of ImageMagick).</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>graphdir</h3>
<p>Where to store dot-outputted graphs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/graphs</p>
<dd></dl>
<h3>group</h3>
<p>The group puppet master should run as.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>hiera_config</h3>
<p>The hiera configuration file</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/hiera.yaml</p>
<dd></dl>
<h3>hostcert</h3>
<p>Where individual hosts store and look for their certificates.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $certdir/$certname.pem</p>
<dd></dl>
<h3>hostcrl</h3>
<p>Where the host&#8217;s certificate revocation list can be found. This is distinct from the certificate authority&#8217;s CRL.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/crl.pem</p>
<dd></dl>
<h3>hostcsr</h3>
<p>Where individual hosts store and look for their certificate requests.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/csr_$certname.pem</p>
<dd></dl>
<h3>hostprivkey</h3>
<p>Where individual hosts store and look for their private key.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $privatekeydir/$certname.pem</p>
<dd></dl>
<h3>hostpubkey</h3>
<p>Where individual hosts store and look for their public key.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $publickeydir/$certname.pem</p>
<dd></dl>
<h3>http_compression</h3>
<p>Allow http compression in REST communication with the master. This setting might improve performance for agent -&gt; master communications over slow WANs. Your puppet master needs to support compression (usually by activating some settings in a reverse-proxy in front of the puppet master, which rules out webrick). It is harmless to activate this settings if your master doesn&#8217;t support compression, but if it supports it, this setting might reduce performance on high-speed LANs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>http_proxy_host</h3>
<p>The HTTP proxy host to use for outgoing connections. Note: You may need to use a FQDN for the server hostname when using a proxy.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: none</p>
<dd></dl>
<h3>http_proxy_port</h3>
<p>The HTTP proxy port to use for outgoing connections</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 3128</p>
<dd></dl>
<h3>httplog</h3>
<p>Where the puppet agent web server logs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $logdir/http.log</p>
<dd></dl>
<h3>ignorecache</h3>
<p>Ignore cache and always recompile the configuration. This is useful for testing new configurations, where the local cache may in fact be stale even if the timestamps are up to date &#8211; if the facts change or if the server changes.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>ignoreimport</h3>
<p>If true, allows the parser to continue without requiring all files referenced with <code>import</code> statements to exist. This setting was primarily designed for use with commit hooks for parse-checking.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>ignoreschedules</h3>
<p>Boolean; whether puppet agent should ignore schedules. This is useful for initial puppet agent runs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>inventory_port</h3>
<p>The port to communicate with the inventory_server.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $masterport</p>
<dd></dl>
<h3>inventory_server</h3>
<p>The server to send facts to.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $server</p>
<dd></dl>
<h3>inventory_terminus</h3>
<p>Should usually be the same as the facts terminus</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $facts_terminus</p>
<dd></dl>
<h3>keylength</h3>
<p>The bit length of keys.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 4096</p>
<dd></dl>
<h3>lastrunfile</h3>
<p>Where puppet agent stores the last run report summary in yaml format.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/last_run_summary.yaml</p>
<dd></dl>
<h3>lastrunreport</h3>
<p>Where puppet agent stores the last run report in yaml format.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/last_run_report.yaml</p>
<dd></dl>
<h3>ldapattrs</h3>
<p>The LDAP attributes to include when querying LDAP for nodes. All returned attributes are set as variables in the top-level scope. Multiple values should be comma-separated. The value &#8216;all&#8217; returns all attributes.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: all</p>
<dd></dl>
<h3>ldapbase</h3>
<p>The search base for LDAP searches. It&#8217;s impossible to provide a meaningful default here, although the LDAP libraries might have one already set. Generally, it should be the &#8216;ou=Hosts&#8217; branch under your main directory.</p>
<h3>ldapclassattrs</h3>
<p>The LDAP attributes to use to define Puppet classes. Values should be comma-separated.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppetclass</p>
<dd></dl>
<h3>ldapparentattr</h3>
<p>The attribute to use to define the parent node.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: parentnode</p>
<dd></dl>
<h3>ldappassword</h3>
<p>The password to use to connect to LDAP.</p>
<h3>ldapport</h3>
<p>The LDAP port. Only used if <code>node_terminus</code> is set to <code>ldap</code>.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 389</p>
<dd></dl>
<h3>ldapserver</h3>
<p>The LDAP server. Only used if <code>node_terminus</code> is set to <code>ldap</code>.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: ldap</p>
<dd></dl>
<h3>ldapssl</h3>
<p>Whether SSL should be used when searching for nodes. Defaults to false because SSL usually requires certificates to be set up on the client side.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>ldapstackedattrs</h3>
<p>The LDAP attributes that should be stacked to arrays by adding the values in all hierarchy elements of the tree. Values should be comma-separated.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppetvar</p>
<dd></dl>
<h3>ldapstring</h3>
<p>The search string used to find an LDAP node.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: (&amp;(objectclass=puppetClient)(cn=%s))</p>
<dd></dl>
<h3>ldaptls</h3>
<p>Whether TLS should be used when searching for nodes. Defaults to false because TLS usually requires certificates to be set up on the client side.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>ldapuser</h3>
<p>The user to use to connect to LDAP. Must be specified as a full DN.</p>
<h3>libdir</h3>
<p>An extra search path for Puppet. This is only useful for those files that Puppet will load on demand, and is only guaranteed to work for those cases. In fact, the autoload mechanism is responsible for making sure this directory is in Ruby&#8217;s search path</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/lib</p>
<dd></dl>
<h3>listen</h3>
<p>Whether puppet agent should listen for connections. If this is true, then puppet agent will accept incoming REST API requests, subject to the default ACLs and the ACLs set in the <code>rest_authconfig</code> file. Puppet agent can respond usefully to requests on the <code>run</code>, <code>facts</code>, <code>certificate</code>, and <code>resource</code> endpoints.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>localcacert</h3>
<p>Where each client stores the CA certificate.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $certdir/ca.pem</p>
<dd></dl>
<h3>localconfig</h3>
<p>Where puppet agent caches the local configuration. An extension indicating the cache format is added automatically.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/localconfig</p>
<dd></dl>
<h3>logdir</h3>
<p>The directory in which to store log files</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>manage_internal_file_permissions</h3>
<p>Whether Puppet should manage the owner, group, and mode of files it uses internally</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>manifest</h3>
<p>The entry-point manifest for puppet master.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $manifestdir/site.pp</p>
<dd></dl>
<h3>manifestdir</h3>
<p>Where puppet master looks for its manifests.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/manifests</p>
<dd></dl>
<h3>masterhttplog</h3>
<p>Where the puppet master web server logs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $logdir/masterhttp.log</p>
<dd></dl>
<h3>masterlog</h3>
<p>Where puppet master logs. This is generally not used, since syslog is the default log destination.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $logdir/puppetmaster.log</p>
<dd></dl>
<h3>masterport</h3>
<p>Which port puppet master listens on.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 8140</p>
<dd></dl>
<h3>maximum_uid</h3>
<p>The maximum allowed UID. Some platforms use negative UIDs but then ship with tools that do not know how to handle signed ints, so the UIDs show up as huge numbers that can then not be fed back into the system. This is a hackish way to fail in a slightly more useful way when that happens.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 4294967290</p>
<dd></dl>
<h3>mkusers</h3>
<p>Whether to create the necessary user and group that puppet agent will run as.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>module_repository</h3>
<p>The module repository</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: <a rel="nofollow" href="https://forge.puppetlabs.com">https://forge.puppetlabs.com</a></p>
<dd></dl>
<h3>module_working_dir</h3>
<p>The directory into which module tool data is stored</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/puppet-module</p>
<dd></dl>
<h3>modulepath</h3>
<p>The search path for modules, as a list of directories separated by the system path separator character. (The POSIX path separator is &#8216;:&#8217;, and the Windows path separator is &#8216;;&#8217;.)</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/modules:/usr/share/puppet/modules</p>
<dd></dl>
<h3>name</h3>
<p>The name of the application, if we are running as one. The default is essentially $0 without the path or <code>.rb</code>.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>node_cache_terminus</h3>
<p>How to store cached nodes. Valid values are (none), &#8216;json&#8217;, &#8216;yaml&#8217; or write only yaml (&#8216;write_only_yaml&#8217;). The master application defaults to &#8216;write_only_yaml&#8217;, all others to none.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>node_name</h3>
<p>How the puppet master determines the client&#8217;s identity and sets the &#8216;hostname&#8217;, &#8216;fqdn&#8217; and &#8216;domain&#8217; facts for use in the manifest, in particular for determining which &#8216;node&#8217; statement applies to the client. Possible values are &#8216;cert&#8217; (use the subject&#8217;s CN in the client&#8217;s certificate) and &#8216;facter&#8217; (use the hostname that the client reported in its facts)</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: cert</p>
<dd></dl>
<h3>node_name_fact</h3>
<p>The fact name used to determine the node name used for all requests the agent makes to the master. WARNING: This setting is mutually exclusive with node_name_value. Changing this setting also requires changes to the default auth.conf configuration on the Puppet Master. Please see <a rel="nofollow" href="http://links.puppetlabs.com/node_name_fact">http://links.puppetlabs.com/node_name_fact</a> for more information.</p>
<h3>node_name_value</h3>
<p>The explicit value used for the node name for all requests the agent makes to the master. WARNING: This setting is mutually exclusive with node_name_fact. Changing this setting also requires changes to the default auth.conf configuration on the Puppet Master. Please see <a rel="nofollow" href="http://links.puppetlabs.com/node_name_value">http://links.puppetlabs.com/node_name_value</a> for more information.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $certname</p>
<dd></dl>
<h3>node_terminus</h3>
<p>Where to find information about nodes.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: plain</p>
<dd></dl>
<h3>noop</h3>
<p>Whether puppet agent should be run in noop mode.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>onetime</h3>
<p>Run the configuration once, rather than as a long-running daemon. This is useful for interactively running puppetd.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>passfile</h3>
<p>Where puppet agent stores the password for its private key. Generally unused.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $privatedir/password</p>
<dd></dl>
<h3>path</h3>
<p>The shell search path. Defaults to whatever is inherited from the parent process.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: none</p>
<dd></dl>
<h3>pidfile</h3>
<p>The file containing the PID of a running process. This file is intended to be used by service management frameworks and monitoring systems to determine if a puppet process is still in the process table.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $rundir/${run_mode}.pid</p>
<dd></dl>
<h3>plugindest</h3>
<p>Where Puppet should store plugins that it pulls down from the central server.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $libdir</p>
<dd></dl>
<h3>pluginsignore</h3>
<p>What files to ignore when pulling down plugins.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: .svn CVS .git</p>
<dd></dl>
<h3>pluginsource</h3>
<p>From where to retrieve plugins. The standard Puppet <code>file</code> type is used for retrieval, so anything that is a valid file source can be used here.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: <a href="puppet://$server/plugins">puppet://$server/plugins</a></p>
<dd></dl>
<h3>pluginsync</h3>
<p>Whether plugins should be synced with the central server.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>postrun_command</h3>
<p>A command to run after every agent run. If this command returns a non-zero return code, the entire Puppet run will be considered to have failed, even though it might have performed work during the normal run.</p>
<h3>preferred_serialization_format</h3>
<p>The preferred means of serializing ruby instances for passing over the wire. This won&#8217;t guarantee that all instances will be serialized using this method, since not all classes can be guaranteed to support this format, but it will be used for all classes that support it.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: pson</p>
<dd></dl>
<h3>prerun_command</h3>
<p>A command to run before every agent run. If this command returns a non-zero return code, the entire Puppet run will fail.</p>
<h3>privatedir</h3>
<p>Where the client stores private certificate information.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/private</p>
<dd></dl>
<h3>privatekeydir</h3>
<p>The private key directory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/private_keys</p>
<dd></dl>
<h3>publickeydir</h3>
<p>The public key directory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/public_keys</p>
<dd></dl>
<h3>puppetdlog</h3>
<p>The log file for puppet agent. This is generally not used.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $logdir/puppetd.log</p>
<dd></dl>
<h3>puppetport</h3>
<p>Which port puppet agent listens on.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 8139</p>
<dd></dl>
<h3>queue_source</h3>
<p>Which type of queue to use for asynchronous processing. If your stomp server requires authentication, you can include it in the URI as long as your stomp client library is at least 1.1.1</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: <a href="stomp://localhost:61613/">stomp://localhost:61613/</a></p>
<dd></dl>
<h3>queue_type</h3>
<p>Which type of queue to use for asynchronous processing.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: stomp</p>
<dd></dl>
<h3>rails_loglevel</h3>
<p>The log level for Rails connections. The value must be a valid log level within Rails. Production environments normally use <code>info</code> and other environments normally use <code>debug</code>.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: info</p>
<dd></dl>
<h3>railslog</h3>
<p>Where Rails-specific logs are sent</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $logdir/rails.log</p>
<dd></dl>
<h3>report</h3>
<p>Whether to send reports after every transaction.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>report_port</h3>
<p>The port to communicate with the report_server.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $masterport</p>
<dd></dl>
<h3>report_server</h3>
<p>The server to send transaction reports to.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $server</p>
<dd></dl>
<h3>reportdir</h3>
<p>The directory in which to store reports received from the client. Each client gets a separate subdirectory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/reports</p>
<dd></dl>
<h3>reportfrom</h3>
<p>The &#8216;from&#8217; email address for the reports.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: report [at] sirrus.puppetlabs.lan</p>
<dd></dl>
<h3>reports</h3>
<p>The list of reports to generate. All reports are looked for in <code>puppet/reports/name.rb</code>, and multiple report names should be comma-separated (whitespace is okay).</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: store</p>
<dd></dl>
<h3>reporturl</h3>
<p>The URL used by the http reports processor to send reports</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: <a rel="nofollow" href="http://localhost:3000/reports/upload">http://localhost:3000/reports/upload</a></p>
<dd></dl>
<h3>req_bits</h3>
<p>The bit length of the certificates.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 4096</p>
<dd></dl>
<h3>requestdir</h3>
<p>Where host certificate requests are stored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $ssldir/certificate_requests</p>
<dd></dl>
<h3>resourcefile</h3>
<p>The file in which puppet agent stores a list of the resources associated with the retrieved configuration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/resources.txt</p>
<dd></dl>
<h3>rest_authconfig</h3>
<p>The configuration file that defines the rights to the different rest indirections. This can be used as a fine-grained authorization system for <code>puppet master</code>.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/auth.conf</p>
<dd></dl>
<h3>route_file</h3>
<p>The YAML file containing indirector route configuration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/routes.yaml</p>
<dd></dl>
<h3>rrddir</h3>
<p>The directory where RRD database files are stored. Directories for each reporting host will be created under this directory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/rrd</p>
<dd></dl>
<h3>rrdinterval</h3>
<p>How often RRD should expect data. This should match how often the hosts report back to the server. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $runinterval</p>
<dd></dl>
<h3>rundir</h3>
<p>Where Puppet PID files are kept.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>runinterval</h3>
<p>How often puppet agent applies the client configuration; in seconds. Note that a runinterval of 0 means &quot;run continuously&quot; rather than &quot;never run.&quot; If you want puppet agent to never run, you should start it with the <code>&#8211;no-client</code> option. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 30m</p>
<dd></dl>
<h3>sendmail</h3>
<p>Where to find the sendmail binary with which to send email.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: /usr/sbin/sendmail</p>
<dd></dl>
<h3>serial</h3>
<p>Where the serial number for certificates is stored.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/serial</p>
<dd></dl>
<h3>server</h3>
<p>The server to which the puppet agent should connect</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>server_datadir</h3>
<p>The directory in which serialized data is stored, usually in a subdirectory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/server_data</p>
<dd></dl>
<h3>show_diff</h3>
<p>Whether to log and report a contextual diff when files are being replaced. This causes partial file contents to pass through Puppet&#8217;s normal logging and reporting system, so this setting should be used with caution if you are sending Puppet&#8217;s reports to an insecure destination. This feature currently requires the <code>diff/lcs</code> Ruby library.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>signeddir</h3>
<p>Where the CA stores signed certificates.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $cadir/signed</p>
<dd></dl>
<h3>smtpserver</h3>
<p>The server through which to send email reports.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: none</p>
<dd></dl>
<h3>splay</h3>
<p>Whether to sleep for a pseudo-random (but consistent) amount of time before a run.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>splaylimit</h3>
<p>The maximum time to delay before runs. Defaults to being the same as the run interval. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $runinterval</p>
<dd></dl>
<h3>srv_domain</h3>
<p>The domain which will be queried to find the SRV records of servers to use.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppetlabs.lan</p>
<dd></dl>
<h3>ssl_client_ca_auth</h3>
<p>Certificate authorities who issue server certificates. SSL servers will not be considered authentic unless they posses a certificate issued by an authority listed in this file. If this setting has no value then the Puppet master&#8217;s CA certificate (localcacert) will be used.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>ssl_client_header</h3>
<p>The header containing an authenticated client&#8217;s SSL DN. This header must be set by the proxy to the authenticated client&#8217;s SSL DN (e.g., <code>/CN=puppet.puppetlabs.com</code>).</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: HTTP_X_CLIENT_DN</p>
<dd></dl>
<h3>ssl_client_verify_header</h3>
<p>The header containing the status message of the client verification. This header must be set by the proxy to &#8216;SUCCESS&#8217; if the client successfully authenticated, and anything else otherwise.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: HTTP_X_CLIENT_VERIFY</p>
<dd></dl>
<h3>ssl_server_ca_auth</h3>
<p>Certificate authorities who issue client certificates. SSL clients will not be considered authentic unless they posses a certificate issued by an authority listed in this file. If this setting has no value then the Puppet master&#8217;s CA certificate (localcacert) will be used.</p>
<dl>
<dt><i>Default</i>:</p>
<dd></dl>
<h3>ssldir</h3>
<p>Where SSL certificates are kept.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/ssl</p>
<dd></dl>
<h3>statedir</h3>
<p>The directory where Puppet state is stored. Generally, this directory can be removed without causing harm (although it might result in spurious service restarts).</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/state</p>
<dd></dl>
<h3>statefile</h3>
<p>Where puppet agent and puppet master store state associated with the running configuration. In the case of puppet master, this file reflects the state discovered through interacting with clients.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $statedir/state.yaml</p>
<dd></dl>
<h3>storeconfigs</h3>
<p>Whether to store each client&#8217;s configuration, including catalogs, facts, and related data. This also enables the import and export of resources in the Puppet language &#8211; a mechanism for exchange resources between nodes. By default this uses ActiveRecord and an SQL database to store and query the data; this, in turn, will depend on Rails being available. You can adjust the backend using the storeconfigs_backend setting.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>storeconfigs_backend</h3>
<p>Configure the backend terminus used for StoreConfigs. By default, this uses the ActiveRecord store, which directly talks to the database from within the Puppet Master process.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: active_record</p>
<dd></dl>
<h3>strict_hostname_checking</h3>
<p>Whether to only search for the complete hostname as it is in the certificate when searching for node information in the catalogs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>summarize</h3>
<p>Whether to print a transaction summary.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>syslogfacility</h3>
<p>What syslog facility to use when logging to syslog. Syslog has a fixed list of valid facilities, and you must choose one of those; you cannot just make one up.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: daemon</p>
<dd></dl>
<h3>tagmap</h3>
<p>The mapping between reporting tags and email addresses.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $confdir/tagmail.conf</p>
<dd></dl>
<h3>tags</h3>
<p>Tags to use to find resources. If this is set, then only resources tagged with the specified tags will be applied. Values must be comma-separated.</p>
<h3>templatedir</h3>
<p>Where Puppet looks for template files. Can be a list of colon-separated directories.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/templates</p>
<dd></dl>
<h3>thin_storeconfigs</h3>
<p>Boolean; whether Puppet should store only facts and exported resources in the storeconfigs database. This will improve the performance of exported resources with the older <code>active_record</code> backend, but will disable external tools that search the storeconfigs database. Thinning catalogs is generally unnecessary when using PuppetDB to store catalogs.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>trace</h3>
<p>Whether to print stack traces on some errors</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>use_cached_catalog</h3>
<p>Whether to only use the cached catalog rather than compiling a new catalog on every run. Puppet can be run with this enabled by default and then selectively disabled when a recompile is desired.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>use_srv_records</h3>
<p>Whether the server will search for SRV records in DNS for the current domain.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: false</p>
<dd></dl>
<h3>usecacheonfailure</h3>
<p>Whether to use the cached configuration when the remote configuration will not compile. This option is useful for testing new configurations, where you want to fix the broken configuration rather than reverting to a known-good one.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<h3>user</h3>
<p>The user puppet master should run as.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: puppet</p>
<dd></dl>
<h3>vardir</h3>
<p>Where Puppet stores dynamic and growing data. The default for this setting is calculated specially, like <code>confdir</code>_.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: /var/lib/puppet</p>
<dd></dl>
<h3>waitforcert</h3>
<p>The time interval &#8216;puppet agent&#8217; should connect to the server and ask it to sign a certificate request. This is useful for the initial setup of a puppet client. You can turn off waiting for certificates by specifying a time of 0. Can be specified as a duration.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: 2m</p>
<dd></dl>
<h3>yamldir</h3>
<p>The directory in which YAML data is stored, usually in a subdirectory.</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: $vardir/yaml</p>
<dd></dl>
<h3>zlib</h3>
<p>Boolean; whether to use the zlib library</p>
<dl>
<dt>&bull;</p>
<dd><i>Default</i>: true</p>
<dd></dl>
<p> <i>This page autogenerated on Tue Jan 15 12:33:09 -0800 2013</i></p>
