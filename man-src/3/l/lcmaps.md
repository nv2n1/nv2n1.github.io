---

title: "lcmaps(3)"
name: "lcmaps"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lcmaps/"
description: "lcmaps – The Local Credential MAPping Service"
---

<h2>NAME</h2>
<p> lcmaps &#8211; The Local Credential MAPping Service</p>
<p> <code>lcmaps</code> </p>
<p> The LCMAPS framework is designed to take various credentials as input, e.g. a certificate and/or VOMS credentials, and map them to Unix credentials as output. Unix credentials are the basic POSIX credentials, i.e. User ID, Group ID and Secondary Group IDs. LCMAPS is a framework that can load and run one or more &#8216;credential mapping&#8217; plugins. The framework will load and run plugins to perform the identity mapping. Site and organizations can create their own new functionality by creating new plugins. The LCMAPS framework exposes various APIs to push credentials into the framework and to get the account mapping results in return. The <code>lcmaps.db</code> configuration file configures the LCMAPS plugins and configures the order in which the plugins are launch. Some practical examples are shown below. </p>
<p> LCMAPS is used by <code>gLExec</code>, the <code>lcas-lcmaps-gt(4)-interface</code> to interface with a Globus GT4 and GT5 Gatekeeper, GridFTP daemon and GSI-OpenSSHd, in StoRM and somewhere in XRootD. </p>
<h2>INVOCATION</h2>
<p> When an application initializes LCMAPS the plugins will be loaded based on the <code>lcmaps.db</code> configuration file. The application can use one of the APIs to provide credentials as input. The loaded plugins will be executed in the sequence described in the same <code>lcmaps.db</code> configuration file. </p>
<p> During a plugin&#8217;s execution it has access to the credential data in the LCMAPS core memory. The plugin is also capable of writing credential mapping results in LCMAPS. The plugins can each resolve a part of the mapping and they can also perform actions based on these (intermediate) results, e.g. run setuid, setgid and setgroup calls or interact with an LDAP service. </p>
<p> The plugins are executed in a state machine. When a plugin finishes successfully it can execute a different next plugin then when it failed. This allows LCMAPS to pass different plugins to resolve a credential mapping. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GATEKEEPER_JM_ID</code></dt>
<dd> Extra Gatekeeper log message to be able to more easily track a Job Manager ID.</dd>
<dt><code>GLOBUSID</code></dt>
<dd> See $GATEKEEPER_JM_ID.</dd>
<dt><code>JOB_REPOSITORY_ID</code></dt>
<dd> See $GATEKEEPER_JM_ID, but explicitly for the purpose of the LCMAPS Job Repository plugin.</dd>
<dt><code>LCMAPS_DB_FILE</code></dt>
<dd> Override the build-in default filename for the <code>lcmaps.db</code> configuration file with the value of this environment variable.</dd>
<dt><code>LCMAPS_DEBUG_LEVEL</code></dt>
<dd> Tune the logging output cut off level. The numbers resemble the numbers as used in previous released in the range [1-5]. However, since LCMAPS version 1.5.0 these numbers resemble a numerically shifted Syslog number.</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> Silent logging, <code>no messages</code> will be written to file or Syslog.</dd>
<dt><code>1</code></dt>
<dd> All messages with a priority of <code>LOG_ERR</code> are written to file or Syslog. More severe error messages are squashed down to the LOG_ERR priority. This is to prevent Syslog from blocking on default configurations and to prevent Syslog from broadcasting LCMAPS related messages on the connected TTYs when old plug-ins are used.</dd>
<dt><code>2</code></dt>
<dd> All messages with a priority of <code>LOG_WARNING</code> or more severe, i.e. LOG_ERR, are written to file and/or Syslog.</dd>
<dt><code>3</code></dt>
<dd> All messages with a priority of <code>LOG_NOTICE</code> or more severe, i.e. LOG_ERR or LOG_WARNING, are written to file and/or Syslog. This is the default advertised setting for the <code>lcas-lcmaps-gt-interface</code> and <code>glexec</code>. The &quot;FINAL CRED&quot; messages are written on LOG_NOTICE and indicate the resulting LCMAPS mapping from an X.509 and/or VOMS credential to a Unix/POSIX credential.</dd>
<dt><code>4</code></dt>
<dd> All messages with a priority of <code>LOG_INFO</code> or more severe, i.e. all messages between (and including) LOG_ERR and LOG_INFO, are written to file and/or Syslog. This value is the <code>build-in default</code>. The success or failures of plug-ins are written on LOG_INFO. To see the flow of plug-ins this log level is the advised log level to set.</dd>
<dt><code>5</code></dt>
<dd> All messages with a priority of <code>LOG_DEBUG</code> or more severe, i.e. all messages between (and including) LOG_ERR and LOG_DEBUG, are written to file and/or Syslog. This is the most verbose mode and should be used carefully as the amount of information flowing from here might hinder normal operation performance if the syslogd isn&#8217;t able to keep up.</dd></dl>
</dl>
<dt><code>LCMAPS_DIR</code></dt>
<dd> The base directory of the $LCMAPS_DB_FILE parameter. This variable is concatenated with the $LCMAPS_DB_FILE</dd>
<dt><code>LCMAPS_ETC_DIR</code></dt>
<dd> See $LCMAPS_DIR</dd>
<dt><code>LCMAPS_LOG_FILE</code></dt>
<dd> Overrides the build-in default file path to log the output to. When set, the logging will not go to Syslog.</dd>
<dt><code>LCMAPS_LOG_STRING</code></dt>
<dd> Prepend all log output messages with value of this environment variable</dd>
<dt><code>LCMAPS_MODULES_DIR</code></dt>
<dd> Directory to search for the LCMAPS plugins (or modules). Same as the <code>path</code> option in the <code>lcmaps.db</code> file..</dd>
<dt><code>LCMAPS_POLICY_NAME</code></dt>
<dd> A colon separated list of LCMAPS plugin execution policies. When this environment variable is present, only the listed execution policies will be executed. They will be executed in the order as written in the <code>lcmaps.db</code> file (from top to bottom).</dd>
<dt><code>LCMAPS_VERIFY_TYPE</code></dt>
<dd> Deprecated</dd>
<dt><code>LCMAPS_VOMS_EXTRACT</code></dt>
<dd> Deprecated</dd>
<dt><code>LCMAPS_X509_CERT_DIR</code></dt>
<dd> Specific setting equal to the $X509_CERT_DIR environment variable</dd>
<dt><code>LCMAPS_X509_VOMS_DIR</code></dt>
<dd> Specific setting equal to the $X509_VOMS_DIR environment variable</dd>
<dt><code>X509_CERT_DIR</code></dt>
<dd> The directory where all the CA files, e.g. CA certificate and CRL files, are located. The default location is: /etc/grid-security/certificates/.</dd>
<dt><code>X509_VOMS_DIR</code></dt>
<dd> This VOMS directory will hold the VOMS .lsc files and/or PEM files to authenticate the VOMS Attributes Certificates. Subdirectories are named by the VO name and scope the .lsc and PEM files in their authentication to one particular VO. The default location is: /etc/grid-security/vomsdir/. </dd>
</dl>
<h2>RETURN VALUES</h2>
<dl>
<dt><code>LCMAPS_SUCCESS</code></dt>
<dd> Success.</dd>
<dt><code>LCMAPS_FAIL</code></dt>
<dd> Failure. </dd>
</dl>
<h2>NOTES</h2>
<p> For an API specification, please use <code>make doc</code> to make the apidoc. </p>
<h2>BUGS</h2>
<p> The apidoc is not complete. It has most interfaces, but needs to be checked for completeness. </p>
<p> Please report any errors to the Nikhef Grid Middleware Security Team &lt;grid-mw-security-support [at] nikhef.nl&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code>lcmaps.db</code>(5), <code>lcas_lcmaps_gt4_interface</code>(8), <code>lcas_lcmaps_gt_interface</code>(8), <code>lcmaps_dummy_bad.mod</code>(8), <code>lcmaps_dummy_good.mod</code>(8), <code>lcmaps_ldap_enf.mod</code>(8), <code>lcmaps_localaccount.mod</code>(8), <code>lcmaps-plugins-c-pep</code>(8), <code>lcmaps_plugins_scas_client</code>(8), <code>lcmaps_poolaccount.mod</code>(8), <code>lcmaps_posix_enf.mod</code>(8), <code>lcmaps_tracking_groupid.mod</code>(8), <code>lcmaps_verify_proxy.mod</code>(8), <code>scas</code>(8), <code>scas.conf</code>(5), <code>glexec</code>(1), <code>glexec.conf</code>(5), <code>ees</code>(1), <code>ees.conf</code>(5) </p>
<h2>AUTHORS</h2>
<p> LCMAPS and the LCMAPS plug-ins were written by the Grid Middleware Security Team &lt;grid-mw-security [at] nikhef.nl&gt;. </p>
