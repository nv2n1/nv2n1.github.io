---

title: "reporter-ureport(1)"
name: "reporter-ureport"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-ureport/"
---

reporter-ureport - Reports ABRT problems in format of micro report 

<i>reporter-ureport</i> [-v] [-c CONFFILE] [-u URL] [-k] [-A -a bthash -B -b bug-id -E -e email -l DATA -L FIELD -T TYPE -r RESULT_TYPE] [-d DIR]

The tool reads problem directory DIR, assembles an micro report from the loaded problem data and sends the micro report to uReport server for updating statistics and fast analysis. The results of the analysis are stored in problem data in form of problems elements. <i>reporter-ureport</i> updates <i>reported_to</i>

<h3>Configuration file</h3>

 

 If not specified, CONFFILE defaults to /etc/libreport/plugins/ureport.conf. Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: 

 <i>URL</i>
<dl>
<dt>
</dt><dd> Base sever HTTP(S) address.</dd></dl>
 

 <i>SSLVerify</i>
<dl>
<dt>
</dt><dd> Use no/false/off/0 to disable verification of server's SSL certificate. (default: yes)</dd></dl>
 

 <i>SSLClientAuth</i>
<dl>
<dt>
</dt><dd> If this option is set, client-side SSL certificate is used to authenticate to the server so that it knows which machine it came from. Assigning any value to this option changes the default value of IncludeAuthData to yes. 
</dd><dl>
<dt>
</dt><dd> <pre>
Possible values are:
</pre></dd></dl>
 

 <i>rhsm</i>
<dl>
<dt>
</dt><dd> Uses the system V3 entitlement certificate that is used for Red Hat subscription management.</dd></dl>
 

 <i>puppet</i>
<dl>
<dt>
</dt><dd> Uses the certificate that is used by the Puppet configuration management tool.</dd></dl>
 

 <i>&lt;cert_path&gt;:&lt;key_path&gt;</i>
<dl>
<dt>
</dt><dd> Manually supply paths to certificate and the corresponding key in PEM format.</dd></dl>
</dl>
 

 <i>HTTPAuth</i>
<dl>
<dt>
</dt><dd> Use the configured values to as HTTP Basic Authentication credentials. Assigning any value to this option changes the default value of IncludeAuthData to yes.</dd></dl>
 

 Possible values are
<dl>
<dt>
</dt><dd> 
 <i>rhts-credentials</i>
</dd><dl>
<dt>
</dt><dd> Uses Login= and Password= values from /etc/libreport/plugins/rhtsupport.conf.</dd></dl>
 

 <i>&lt;user_name&gt;:&lt;password&gt;</i>
<dl>
<dt>
</dt><dd> Manually supply credentials.</dd></dl>
</dl>
 

 <i>ContactEmail</i>
<dl>
<dt>
</dt><dd> Email address attached to a bthash on the server.</dd></dl>
 

 <i>IncludeAuthData</i>
<dl>
<dt>
</dt><dd> If this option is set to <i>yes</i>, uploaded uReport will contain <i>auth</i> object consisting from key value pairs made from CSV list stored in <i>AuthDataItems</i> option. Keys are file names and values are bites of these files. 
</dd><dl>
<dt>
</dt><dd> <pre>
The default value is no, unless you set SSLClientAuth to some value. In that
case, the default value is yes.
</pre></dd></dl>
</dl>
 

 <i>AuthDataItems</i>
<dl>
<dt>
</dt><dd> CSV list of files included in the <i>auth</i> uReport object.</dd></dl>
 

 Parameters can be overridden via $uReport_PARAM environment variables.

<h2>OPTIONS</h2>

 

 -c FILE
<dl>
<dt>
</dt><dd> Path to configuration file</dd></dl>
 

 -a, --attach BTHASH
<dl>
<dt>
</dt><dd> bthash of uReport to attach (conflicts with -A)</dd></dl>
 

 -A, --attach-rt
<dl>
<dt>
</dt><dd> Attach to a bthash from reported_to (conflicts with -a)</dd></dl>
 

 -b, --bug-id NUM
<dl>
<dt>
</dt><dd> Attach RHBZ bug (requires -a)</dd></dl>
 

 -B, --bug-id-rt
<dl>
<dt>
</dt><dd> Attach last RHBZ bug from reported_to (requires -a|-A, conflicts with -b)</dd></dl>
 

 -e, --email EMAIL
<dl>
<dt>
</dt><dd> Contact e-mail address (requires -a|-A, conflicts with -E)</dd></dl>
 

 -E, --email-env
<dl>
<dt>
</dt><dd> Contact e-mail address from environment (requires -a|-A, conflicts with -e)</dd></dl>
 

 -d, --problem-dir DIR
<dl>
<dt>
</dt><dd> Path to problem directory.</dd></dl>
 

 -k, --insecure
<dl>
<dt>
</dt><dd> Allow insecure connection to ureport server</dd></dl>
 

 -t, --auth SOURCE
<dl>
<dt>
</dt><dd> Enables client authentication. See <i>SSLClientAuth</i> configuration file option for list of possible values.</dd></dl>
 

 -h, --http-auth CREDENTIALS
<dl>
<dt>
</dt><dd> Enables client authentication via HTTP Authentication. See <i>HTTPAuth</i> configuration file option for list of possible values.</dd></dl>
 

 -v
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -u, --url URL
<dl>
<dt>
</dt><dd> Specify server URL</dd></dl>
 

 -i AUTH_DATA_ITEMS
<dl>
<dt>
</dt><dd> List of dump dir files included in the <i>auth</i> uReport object.</dd></dl>
 

 -l DATA
<dl>
<dt>
</dt><dd> Attach DATA (requires -T and -a|-A)</dd></dl>
 

 -L REPORT_RESULT_FILED
<dl>
<dt>
</dt><dd> Attach the value of REPORT_RESULT_FILED member of the last report result indentified by REPORT_RESULT_TYPE passed with -r option (requires -r, -T and -a|-A).</dd></dl>
 

 -T ATTACHMENT_TYPE
<dl>
<dt>
</dt><dd> Specifies the attachment type when attaching an arbitrary data to BTHASH (takes effect only with -l or -L)</dd></dl>
 

 -r REPORT_RESULT_TYP
<dl>
<dt>
</dt><dd> Used to single out report results (<i>reported_to</i> file lines) when attaching an arbitrary data to BTHASH (takes effect only with -L)</dd></dl>

<h2>ENVIRONMENT VARIABLES</h2>

 

 Environment variables take precedence over values provided in the configuration file. 

 <i>uReport_URL</i>
<dl>
<dt>
</dt><dd> Base sever HTTP(S) address.</dd></dl>
 

 <i>uReport_SSLVerify</i>
<dl>
<dt>
</dt><dd> Use yes/true/on/1 to verify server's SSL certificate. (default: yes)</dd></dl>
 

 <i>uReport_ContactEmail</i>
<dl>
<dt>
</dt><dd> Email address attached to a bthash on the server.</dd></dl>
 

 <i>uReport_IncludeAuthData</i>
<dl>
<dt>
</dt><dd> See IncludeAuthData configuration option for details.</dd></dl>
 

 <i>uReport_AuthDataItems</i>
<dl>
<dt>
</dt><dd> See AuthDataItems configuration option for details.</dd></dl>

<h2>FILES</h2>

 

 /usr/share/libreport/conf.d/plugins/ureport.conf
<dl>
<dt>
</dt><dd> Readonly default configuration files.</dd></dl>
 

 /etc/libreport/plugins/ureport.conf
<dl>
<dt>
</dt><dd> Configuration file.</dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-ureport-conf/">ureport.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
