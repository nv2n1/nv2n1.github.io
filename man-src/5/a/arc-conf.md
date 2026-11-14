---
title: "arc-conf(5)"
name: "arc-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-arc-conf/"
description: "arc.conf – ARC configuration"
---

<p>arc.conf &#8211; ARC configuration</p>
<h2>Synopsis</h2>
<p><code>/etc/arc.conf</code> <code>${ARC_LOCATION}/etc/arc.conf</code> </p>
<h2>Description</h2>
<p>ARC has two separate configuration files &#8211; one for client tools and another for services. This document describes the services configuration file. For client configuration please see &quot;ARC Clients User Manual&quot; at <a rel="nofollow" href="http://www.nordugrid.org/documents/arc-ui.pdf">http://www.nordugrid.org/documents/arc-ui.pdf</a> ARC configuration uses a plain-text &quot;ini-style&quot; format. It is also possible to use an XML format, however that is outside the scope of this document. The configuration file consists of several configuration blocks. Each configuration block is identified by a keyword and contains the configuration options for a specific part of the ARC middleware. Each configuration block starts with its identifying keyword inside square brackets. Thereafter follows one or more attribute value pairs written one on each line in the following format (note that the attribute names are CASE-SENSITIVE): </p>
<pre><code>[keyword1]</code>
<code>attribute1</code>=value1
<code>attribute2</code>=value2
<code>[keyword2]</code>
<code>attribute</code>=value</pre>
<p>If the ARC_LOCATION environment variable is set the ARC configuration file located at ${ARC_LOCATION}/etc/arc.conf is read first. If this file is not present or the relevant configuration information is not found in this file, the file at /etc/arc.conf is read. </p>
<h2>The [common] block</h2>
<p>The parameters set within this block are available for all the other blocks. These are the configuration parameters shared by the different components of ARC (e.g. grid-manager, infosys) </p>
<dl>
<dt><code>hostname</code></p>
<dd>hostname &#8211; the FQDN of the frontend node, optional in the common block but MUST be set in the cluster block </p>
<p> <i>Example:</i><br />
 hostname=&quot;myhost.org&quot; </p>
<dt><code>x509_voms_dir</code></p>
<dd>x509_voms_dir path &#8211; the path to the directory containing *.lsc files needed for checking validity of VOMS extensions. If not specified default value /etc/grid-security/vomsdir is used. </p>
<p> <i>Example:</i><br />
 x509_voms_dir=&quot;/etc/grid-security/vomsdir&quot; </p>
<dt><code>lrms</code></p>
<dd>ARC supports various LRMS flavours, as listed in this section. For detailed description of options please refer to ARC CE sysadmin guide: </p>
<p> <a rel="nofollow" href="http://www.nordugrid.org/documents/arc-ce-sysadm-guide.pdf">http://www.nordugrid.org/documents/arc-ce-sysadm-guide.pdf</a> </p>
<p> <code>ONLY ONE LRMS IS ALLOWED. MULTIPLE lrms ENTRIES WILL TRIGGER UNEXPECTED BEHAVIOUR.</code> </p>
<p> <code>lrms</code> sets the type of the Local Resource Management System (queue system), and optionally &#8211; the default queue name, separated with a blank space: <code>lrmstype queue_name.</code> For <code>lrmstype,</code> the following systems are supported and can be chosen (one per server):<br />
fork&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; simple forking of jobs to the same node as the server<br />
sge&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>(Sun/Oracle)&nbsp;<wbr>Grid Engine<br />
condor &#8211; Condor<br />
pbs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; PBS<br />
lsf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; LSF<br />
ll&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; LoadLeveler<br />
slurm&nbsp;<wbr>&nbsp;<wbr>&#8211; SLURM<br />
dgbridge &#8211; Desktop Grid<br />
 PBS has many flavours, ARC currenly supports OpenPBS, PBSPro, ScalablePBS and Torque (the official name for ScalablePBS). There is no need to specify the flavour or the version number of the PBS, simply write &#8216;pbs&#8217;. Similarly, there is no need to specify (Sun/Oracle) Grid Engine versions and flavours. &quot;lrmstype&quot; MUST be set here, it is a MANDATORY parameter! </p>
<p> The optional <code>queue</code> parameter specifies the default Grid queue of the LRMS. Jobs will be submitted to this queue if they do not specify queue name in job description. Queue name must match one of the [queue/queue_name] block labels, see below. </p>
<p> <i>Example:</i><br />
 lrms=&quot;pbs gridlong&quot;<br />
 lrms=&quot;pbs&quot; </p>
</dl>
<h2>PBS options</h2>
<dl>
<dt><code>pbs_bin_path</code></p>
<dd>the path to the qstat,pbsnodes,qmgr etc PBS binaries, no need to set if PBS is not used </p>
<p> <i>Example:</i><br />
 pbs_bin_path=&quot;/usr/bin&quot; </p>
<dt><code>pbs_log_path</code></p>
<dd>the path of the PBS server logfiles which are used by A-REX to determine whether a PBS job is completed. If not specified, A-REX will use qstat for that. </p>
<p> <i>Example:</i><br />
 pbs_log_path=&quot;/var/spool/pbs/server_logs&quot; </p>
</dl>
<h2>Condor options</h2>
<dl>
<dt><code>condor_rank</code></p>
<dd>condor_rank &#8211; If you are not happy with the way Condor picks nodes when running jobs, you can define your own ranking algorithm by optionally setting the condor_rank attribute. condor_rank should be set to a ClassAd float expression that you could use in the Rank attribute in a Condor job description. Obviously no need to set if Condor is not used. An example: </p>
<p> <i>Example:</i><br />
 condor_rank=&quot;(1-LoadAvg/2)*(1-LoadAvg/2)*Memory/1000*KFlops/1000000&quot; </p>
<dt><code>condor_bin_path</code></p>
<dd>condor_bin_path &#8211; Path to Condor binaries. Must be set if Condor is used. </p>
<p> <i>Example:</i><br />
 condor_bin_path=/opt/condor/bin </p>
<dt><code>condor_config</code></p>
<dd>condor_config &#8211; Path to Condor config file. Must be set if Condor is used and the config file is not in its default location (/etc/condor/condir_config or ~/condor/condor_config). The full path to the file should be given. </p>
<p> <i>Example:</i><br />
 condor_config=/opt/condor/etc/condor_config </p>
</dl>
<h2>SGE options</h2>
<dl>
<dt><code>sge_bin_path</code></p>
<dd>sge_bin_path &#8211; Path to Sun Grid Engine (SGE) binaries, MUST be set if SGE is the LRMS used </p>
<p> <i>Example:</i><br />
 sge_bin_path=&quot;/opt/n1ge6/bin/lx24-x86&quot; </p>
<dt><code>sge_root</code></p>
<dd>sge_root &#8211; Path to SGE installation directory. MUST be set if SGE is used. </p>
<p> <i>Example:</i><br />
 sge_root=&quot;/opt/n1ge6&quot; </p>
<dt><code>sge_cell</code></p>
<dd>sge_cell &#8211; The name of the SGE cell to use. This option is only necessary in case SGE is set up with a cell name different from &#8216;default&#8217; </p>
<p> <i>Example:</i><br />
 sge_cell=&quot;default&quot; </p>
<dt><code>sge_qmaster_port</code></p>
<dd>sge_qmaster_port, sge_execd_port &#8211; these options should be used in case SGE command line clients require SGE_QMASTER_PORT and SGE_EXECD_PORT environment variables to be set. Usually they are not necessary. </p>
<p> <i>Example:</i><br />
 sge_qmaster_port=&quot;536&quot;<br />
 sge_execd_port=&quot;537&quot; </p>
</dl>
<h2>SLURM options</h2>
<dl>
<dt><code>slurm_bin_path</code></p>
<dd>slurm_bin_path &#8211; Path to SLURM binaries, must be set if installed outside of normal $PATH </p>
<p> <i>Example:</i><br />
 slurm_bin_path=&quot;/usr/bin&quot; </p>
<dt><code>slurm_wakeupperiod</code></p>
<dd>How long should infosys wait before querying SLURM for new data (seconds) </p>
<p> <i>Example:</i><br />
 slurm_wakeupperiod=&quot;15&quot; </p>
<dt><code>slurm_use_sacct</code></p>
<dd>Should ARC use sacct instead of scontrol to get information on finished jobs. Requires that accounting is turned on in SLURM. Default is &quot;no&quot;. </p>
<p> <i>Example:</i><br />
 slurm_use_sacct=&quot;yes&quot; </p>
</dl>
<h2>LSF options</h2>
<dl>
<dt><code>lsf_bin_path</code></p>
<dd>the PATH to LSF bin folder no need to set if LSF is not used </p>
<p> <i>Example:</i><br />
 lsf_bin_path=&quot;/usr/local/lsf/bin/&quot; </p>
<dt><code>lsf_profile_path</code></p>
<dd>the PATH to profile.lsf no need to set if LSF is not used </p>
<p> <i>Example:</i><br />
 lsf_profile_path=&quot;/usr/share/lsf/conf&quot; </p>
</dl>
<h2>LL options</h2>
<dl>
<dt><code>ll_bin_path</code></p>
<dd>the PATH to the LoadLeveler bin folder no need to set if LoadLeveler is not used </p>
<p> <i>Example:</i><br />
 ll_bin_path=&quot;/opt/ibmll/LoadL/full/bin&quot; </p>
<dt><code>ll_consumable_resources</code></p>
<dd>support for a LoadLeveler setup using Consumable Resources no need to set if LoadLeveler is not used </p>
<p> <i>Example:</i><br />
 ll_consumable_resources=&quot;yes&quot; </p>
</dl>
<h2>Desktop Grid options</h2>
<dl>
<dt><code>dgbridge_stage_dir</code></p>
<dd>Desktop Bridge www publish dir </p>
<p> <i>Example:</i><br />
 dgbridge_stage_dir=&quot;/var/www/DGBridge&quot; </p>
<dt><code>dgbridge_stage_prepend</code></p>
<dd>Desktop Bridge URL prefix pointing to dgbridge_stage_dir </p>
<p> <i>Example:</i><br />
 dgbridge_stage_prepend=&quot;<a rel="nofollow" href="http://edgi-bridge.example.com/DGBridge/">http://edgi-bridge.example.com/DGBridge/</a>&quot; </p>
</dl>
<h2>Boinc options</h2>
<dl>
<dt><code>boinc_db_host boinc_db_port boinc_db_name boinc_db_user boinc_db_pass</code></p>
<dd>Connection details for the Boinc database. </p>
<p> <i>Example:</i><br />
 boinc_db_host=&quot;localhost&quot;<br />
 boinc_db_port=&quot;3306&quot;<br />
 boinc_db_name=&quot;myproject&quot;<br />
 boinc_db_user=&quot;boinc&quot;<br />
 boinc_db_pass=&quot;password&quot; </p>
</dl>
<h2>Other [common] options</h2>
<dl>
<dt><code>globus_tcp_port_range</code></p>
<dd>globus_tcp_port_range, globus_udp_port_range &#8211; Firewall configuration In a firewalled environment the software which uses GSI needs to know what ports are available. The full documentation can be found at: <a rel="nofollow" href="http://dev.globus.org/wiki/FirewallHowTo">http://dev.globus.org/wiki/FirewallHowTo</a> These variable are similar to the Globus environment variables: GLOBUS_TCP_PORT_RANGE and GLOBUS_UDP_PORT_RANGE. These variables are not limited to [common], but can be set individually for each service in corresponding section: [grid-manager], [gridftpd] Example: </p>
<p> <i>Example:</i><br />
 globus_tcp_port_range=&quot;9000,12000&quot;<br />
 globus_udp_port_range=&quot;9000,12000&quot; </p>
<dt><code>x509_user_key</code></p>
<dd>x509_user_cert, x509_user_key &#8211; Server credentials location. These variables are similar to the GSI environment variables: X509_USER_KEY and X509_USER_CERT These variables are not limited to [common], but can be set individually for each service in corresponding section: [grid-manager], [gridftpd], [nordugridmap] </p>
<p> <i>Example:</i><br />
 x509_user_key=&quot;/etc/grid-security/hostkey.pem&quot;<br />
 x509_user_cert=&quot;/etc/grid-security/hostcert.pem&quot; </p>
<dt><code>x509_cert_dir</code></p>
<dd>x509_cert_dir &#8211; Location of trusted CA certificates This variable is similar to the GSI environment variable: X509_CERT_DIR This variable is not limited to [common], but can be set individually for each service in corresponding section: [grid-manager], [gridftpd] </p>
<p> <i>Example:</i><br />
 x509_cert_dir=&quot;/etc/grid-security/certificates&quot; </p>
<dt><code>gridmap</code></p>
<dd>gridmap &#8211; The gridmap file location This variable is similar to the GSI environment variable: GRIDMAP This variable is not limited to [common], but can be set individually for each service in corresponding section: [grid-manager], [gridftpd] The default is /etc/grid-security/grid-mapfile </p>
<p> <i>Example:</i><br />
 gridmap=&quot;/etc/grid-security/grid-mapfile&quot; </p>
<dt><code>voms_processing</code></p>
<dd>voms_processing &#8211; Defines how to behave if errors in VOMS AC processing detected.<br />
&nbsp;<wbr>&nbsp;<wbr>relaxed &#8211; use everything that passed validation.<br />
&nbsp;<wbr>&nbsp;<wbr>standard &#8211; same as relaxed but fail if parsing errors took place and VOMS extension is marked as critical. This is the default.<br />
&nbsp;<wbr>&nbsp;<wbr>strict &#8211; fail if any parsing error was discovered.<br />
&nbsp;<wbr>&nbsp;<wbr>noerrors &#8211; fail if any parsing or validation error happened. This command can also be used in [grid-manager] and [gridftpd] blocks. </p>
<p> <i>Example:</i><br />
 voms_processing=&quot;standard&quot; </p>
<dt><code>voms_trust_chain </code></p>
<dd>voms_trust_chain &#8211; Define the DN chain that the host services trust when the VOMS AC from peer VOMS proxy certificate is parsed and validated. There can be multiple &quot;voms_trust_chain&quot; existing, each one corresponds to a VOMS server. This variable is similar to the information in *.lsc file, but with two differences:<br />
&nbsp;<wbr>1, You don&#8217;t need to create a&nbsp;<wbr>*.lsc file per VOMS server, but create a chain per VOMS server;<br />
&nbsp;<wbr>2, Regular expressions are supported when matching the DNs. </p>
<p> This variable is not limited to [common], but can be used in [grid-manager] and [gridftpd] blocks. This variable should be used together with voms_processing. This variable will overwrite the information in *.lsc if *.lsc exists. </p>
<pre><i>Example:</i>
<br>
voms_trust_chain = &quot;/O=Grid/O=NorduGrid/CN=host/arthur.hep.lu.se&quot; &quot;/O=Grid/O=NorduGrid/CN=NorduGrid Certification Authority&quot;
<br>
voms_trust_chain = &quot;/O=Grid/O=NorduGrid/CN=host/emi-arc.eu&quot; &quot;/O=Grid/O=NorduGrid/CN=NorduGrid Certification Authority&quot;
<br>
voms_trust_chain = &quot;^/O=Grid/O=NorduGrid&quot;</pre>
<dt><code>enable_perflog_reporting</code></p>
<dd>enable_perflog_reporting expert-debug-on/no &#8211; Switch on or off performance reporting. Default is no. Only switch on if you specifically need it, and are aware of the possible local root exploit due to permissive directory. </p>
<p> <i>Example:</i><br />
 enable_perflog_reporting=&quot;expert-debug-on&quot; </p>
<dt><code>perflogdir</code></p>
<dd>perflogdir logdir &#8211; Directory where performance logs should be stored. Default is /var/log/arc/perflogs </p>
<p> <i>Example:</i><br />
 perflogdir=&quot;/var/log/arc/perflogs&quot; </p>
</dl>
<h2>[vo] block</h2>
<p>[vo] block is used to define VOs and generate mapfiles from user list maintained by VO databases. VO block is a configuration block for the nordugridmap utility. Please note that [vo] block processing by nordugridmap utility depend on parameters defined in the [nordugridmap] block. </p>
<p> [vo] block by itself does not affect authorization of client/user. For that label defined by vo=&quot;&quot; attribute may be used in [group] block with with &#8216;file&#8217; rule. </p>
<dl>
<dt><code>id</code></p>
<dd>id blockid &#8211; specifies the unique configuration block id (this does not affect nordugridmap utility) </p>
<p> <i>Example:</i><br />
 id=&quot;vo_1&quot; </p>
<dt><code>vo</code></p>
<dd>vo vo_name &#8211; specifies the VO name, this name can be used in other blocks. MUST be given. </p>
<p> <i>Example:</i><br />
 vo=&quot;nordugrid&quot; </p>
<dt><code>file</code></p>
<dd>file path &#8211; output gridmap-file where GENERATED mapping list will be stored. See parameters below to define how to generate this file. If the same file specified as output for different [vo] blocks, nordugridmap will automatically merge entries in given blocks order. Default is &#8216;/etc/grid-security/gridmapfile&#8217;. </p>
<p> <i>Example:</i><br />
 file=&quot;/etc/grid-security/VOs/atlas-users&quot; </p>
<dt><code>source</code></p>
<dd>source URL &#8211; the URL of the VO database which is assigned to this VO. The nordugridmap will use this URL to automatically generate and keep up-to-date userlist (mapfile) specified by the &#8216;file&#8217; attribute. URL is a multivalued attribute, several sources can be specified for the [vo] block and all the users from those sources will be merged into the same file. The source URLs are processed in the given order. Currently supported URL types are:<br />
http(s)://&nbsp;<wbr>&#8211; URL to plain text file. File should contain a list<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of DNs with optional issuer certificate authority DN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(see require_issuerdn):&nbsp;<wbr>&quot;user DN&quot;&nbsp;<wbr>[&quot;issuer DN&quot;]<br />
voms(s)://&nbsp;<wbr>&#8211; URL to VOMS-Admin interface<br />
nordugrid&nbsp;<wbr>&nbsp;<wbr>&#8211; add NorduGrid VO members<br />
ldap://&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; expect LDAP-schema formatted VO Group<br />
file://&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; local file&nbsp;<wbr>(stand-alone or dynamically generated by&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nordugridmap). File should contain a list of DNs with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>optional mapped unixid:&nbsp;<wbr>&quot;user DN&quot;&nbsp;<wbr>[mapped user ID]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Result of optional mapped unixid processing depend<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on mapuser_processing option settings.<br />
vo://&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; reference to another&nbsp;<wbr>[vo]&nbsp;<wbr>configuration block&nbsp;<wbr><br />
edg-mkgridmap://&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; local configuration file used by edg-mkgridmap tool.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nordugridmap will parse configuration from file and&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>process it as additional&nbsp;<wbr>[vo]&nbsp;<wbr>block that will be referred&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>authomatically in place URL specified. This allow&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>easy migration from edg-mkgridmap solution without&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rewriting your previous configuration&nbsp;<wbr>(NOTE that rarely&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>used&nbsp;<wbr>&#8216;auth&#8217;&nbsp;<wbr>directive and&nbsp;<wbr>&#8216;AUTO&#8217;&nbsp;<wbr>mapping options are not&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>supported) </p>
<p> You can use either vo:// or file:// entries to specify dependencies between [vo] blocks, but using vo:// is a recommended way. For each separate source URL it is possible to override some parameters value. You can use the following syntax to perform this:<br />
source=&quot;URL&nbsp;<wbr>&lt;&nbsp;<wbr>parameter1=value1 parameter2=value2&quot; </p>
<p> You can override the following parameters:<br />
mapped_unixid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for http(s),voms(s),ldap and file URLs<br />
cache_enable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for http(s),voms(s),ldap and file URLs<br />
voms_method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for voms(s)&nbsp;<wbr>URLs<br />
mapuser_processing&nbsp;<wbr>&nbsp;<wbr>for file URLs with mapped_unixid='&lt;unixid&gt;&#8217;&nbsp;<wbr>overrides<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(control mapped_unixid overriding behaviour for URL) </p>
<p> <i>Example:</i><br />
 source=&quot;<a href="vomss://voms.ndgf.org:8443/voms/nordugrid.org">vomss://voms.ndgf.org:8443/voms/nordugrid.org</a>&quot;<br />
 source=&quot;<a href="vomss://lcg-voms.cern.ch:8443/voms/atlas?/atlas/Role=VO-Admin">vomss://lcg-voms.cern.ch:8443/voms/atlas?/atlas/Role=VO-Admin</a> &lt; mapped_unixid=atlasadmin&quot;<br />
 source=&quot;<a href="vomss://kuiken.nikhef.nl:8443/voms/gin.ggf.org">vomss://kuiken.nikhef.nl:8443/voms/gin.ggf.org</a> &lt; voms_method=get&quot;<br />
 source=&quot;<a rel="nofollow" href="http://www.nordugrid.org/developers.dn">http://www.nordugrid.org/developers.dn</a>&quot;<br />
 source=&quot;<a href="ldap://grid-vo.nikhef.nl/ou=lcg1,o=atlas,dc=eu-datagrid,dc=org">ldap://grid-vo.nikhef.nl/ou=lcg1,o=atlas,dc=eu-datagrid,dc=org</a>&quot;<br />
 source=&quot;file:///etc/grid-security/priviliged_users.dn&quot;<br />
 source=&quot;vo://nordugrid_community&quot;<br />
 source=&quot;nordugrid&quot; </p>
<dt><code>mapped_unixid</code></p>
<dd>mapped_unixid unixid &#8211; the local UNIXID which is used in the generated grid-mapfile by the nordugridmap utility. </p>
<p> If any of the sources have already provided mapping information (file:// or vo://) behaviour depends on &#8216;mapuser_processing&#8217; [nordugridmap] block configuration:<br />
mapuser_processing&nbsp;<wbr>=&nbsp;<wbr>&#8216;overwrite&#8217;: ignore already provided mapping and&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>apply mapped_unixid for all sources<br />
mapuser_processing&nbsp;<wbr>=&nbsp;<wbr>&#8216;keep&#8217;: apply mapped_unixid only for sources that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>does not already has mapping information </p>
<p> [vo] block can only have one UNIXID. If &#8216;mapped_unixid&#8217; is not specified behaviour depends on &#8216;allow_empty_unixid&#8217; [nordugridmap] block configuration value:<br />
allow_empty_unixid&nbsp;<wbr>=&nbsp;<wbr>&#8216;yes&#8217;: empty value will be used for mapped_unixid<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>which means that nordugridmap will generate only&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the list of DNs without mapping&nbsp;<wbr>(consider using&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mapuser_processing=&#8217;overwrite&#8217;&nbsp;<wbr>along with this&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>option or sources that does not provide previously<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>defined mapping information)<br />
allow_empty_unixid&nbsp;<wbr>=&nbsp;<wbr>&#8216;no&#8217;: skip users without mapping information&nbsp;<wbr>(if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no mapping information provided by sources) </p>
<p> <i>Example:</i><br />
 mapped_unixid=&quot;gridtest&quot; </p>
<dt><code>voms_fqan_map</code></p>
<dd>voms_fqan_map fqan unixid &#8211; the local UNIXID which is used to map voms(s) sources with specific FQAN given. Several voms_fqan_map can be specified for a [vo] block. For each voms(s) sources in [vo] block and every voms_fqan_map record separate source record will be authomatically generated with mapped_unixid overrided to specified one. Sources are generated in a given voms_fqan_map order. Original voms(s) source URL are processed LAST. This allows to simplify configuration, especially in redundancy cases when several VOMS servers are used for the same VO. </p>
<p> <i>Example:</i><br />
 voms_fqan_map=&quot;/atlas/Role=VO-Admin atlasadmin&quot;<br />
 voms_fqan_map=&quot;/atlas/Role=production atlasprod&quot; </p>
<dt><code>require_issuerdn</code></p>
<dd>require_issuerdn yes/no &#8211; another nordugridmap option. YES would map only those DNs obtained from the URLs which have the corresponding public CA packages installed. Default is &#8216;no&#8217;. Note, that some sources does not provide issuer information (like voms(s):// or file://). If this sources are used within [vo] block and require_issuerdn is set to &#8216;yes&#8217; behaviour depends on issuer_processing [nordugridmap] block configuration:<br />
issuer_processing&nbsp;<wbr>=&nbsp;<wbr>&#8216;relaxed&#8217;: check only those records that have issuer&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>information provided, allow other sources<br />
issuer_processing&nbsp;<wbr>=&nbsp;<wbr>&#8216;strict&#8217;: if issuer information was not found record&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is filtered and will not be passed into mapfile </p>
<p> <i>Example:</i><br />
 require_issuerdn=&quot;no&quot; </p>
<dt><code>filter</code></p>
<dd>filter ACL string &#8211; An ACL filter for the nordugridmap utility. Multiple allow/deny statements are possible. The fetched DNs are filtered against the specified rules before they are added to the generated mapfile. * can be used as a wildcard. You may run the nordugridmap with the &#8211;test command line option to see how the filters you specified work. If at least one allow filter is specified implicit deny is used at the end of ACL. If only deny filters are present &#8211; implicit allow used at the end. </p>
<p> <i>Example:</i><br />
 filter=&quot;deny *infn*&quot;<br />
 filter=&quot;allow *NorduGrid*&quot; </p>
</dl>
<h2>[group] Authorisation block</h2>
<p>These configuration blocks define rules used to define to which authorization group a user belongs. The group should not be mistaken for a virtual organisation (VO). A group may match a single vo if only a single check (rule) on vo membership is performed. It is however more common to allow multiple VOs in a single group. ARC also allows many other ways to assign users to groups. Technically, permissions are only granted to groups, not directly to VOs. </p>
<p> The block specifies single authorization group. There may be multiple [group] blocks in configuration defining multiple authorization groups. </p>
<p> The block can be specified in two ways &#8211; either using [group/group1] like subblock declaration per group or just [group]. The two formats are equivalent. Every block (till the beginning of next block or the end of the file) defines one authorization group. </p>
<p> <code>IMPORTANT:</code> Rules in a group are processed in their order of appearance. The first matching rule decides the membership of a the user to a group and the processing STOPS. There are positively and negatively matching rules. If a rule is matched positively then the user tested is accepted into the respective group and further processing is stopped. Upon a negative match the user would be rejected for that group &#8211; processing stops too. The sign of rule is determined by prepending the rule with be omitted. A rule may also be prepended with &#8216;!&#8217; to invert result of rule, which will let the rule match the complement of users. That complement operator (&#8216;!&#8217;) may be combined with the operator for positive or negative matching. </p>
<p> A group MUST be defined before it may be used. In this respect the arc.conf is ORDER SENSITIVE. </p>
<p> The authorization groups can be used in [gridftpd] and in its sub-blocks. The syntax of their specification varies with the service they are used for. For using authorization groups and VO blocks in HED framework please read &quot;Security Framework of ARC&quot; at <a rel="nofollow" href="http://www.nordugrid.org/documents/arc-security-documentation.pdf">http://www.nordugrid.org/documents/arc-security-documentation.pdf</a> </p>
<dl>
<dt><code>name</code></p>
<dd>name group_name &#8211; Specify name of group. If there is no such command in block, name of subblock is used instead (that is what subblocks are used for). For example [group/users]. </p>
<p> <i>Example:</i><br />
 name=&quot;users&quot; </p>
<dt><code>subject</code></p>
<dd>subject certificate_subject &#8211; Rule to match specific subject of user&#8217;s X.509 certificate. No masks, patterns and regular expressions are allowed. For more information about X.509 refer to <a rel="nofollow" href="http://www.wikipedia.org/wiki/X509">http://www.wikipedia.org/wiki/X509</a> </p>
<p> <i>Example:</i><br />
 subject=&quot;/O=Grid/O=Big VO/CN=Main Boss&quot; </p>
<dt><code>file</code></p>
<dd>file path &#8211; Start reading rules from another file. That file has a bit different format. It can&#8217;t contain blocks and commands are separated from arguments by space. Also word &quot;subject&quot; in subject command may be skipped. That makes it convenient to directly add gridmap-like lists to authorization group. </p>
<p> <i>Example:</i><br />
 file=&quot;/etc/grid-security/local_users&quot; </p>
<dt><code>voms</code></p>
<dd>voms vo group role capabilities &#8211; Match VOMS attribute in user&#8217;s credential. Use &#8216;*&#8217; to match any value. More information about VOMS can be found at <a rel="nofollow" href="http://grid-auth.infn.it">http://grid-auth.infn.it</a> </p>
<p> <i>Example:</i><br />
 voms=&quot;nordugrid /nordugrid/Guests * *&quot; </p>
<dt><code>group</code></p>
<dd>group group_name [group_name &#8230;] &#8211; Match user already belonging to one of specified groups. Groups refered here must be defined earlier in configuration file. Multiple group names may be specified for this rule. That allows creating hierarchical structure of authorization groups like </p>
<p> <i>Example:</i><br />
 group=&quot;local_admins&quot; </p>
<dt><code>plugin</code></p>
<dd>plugin timeout path [argument &#8230;] &#8211; Run external executable or function from shared library. Rule is matched if plugin returns 0. In arguments following substitutions are supported:<br />
&nbsp;<wbr>&nbsp;<wbr>%D &#8211; subject of certificate<br />
&nbsp;<wbr>&nbsp;<wbr>%P &#8211; path to proxy </p>
<p> For more about plugins read documentation. </p>
<p> <i>Example:</i><br />
 plugin=&quot;10 /opt/external/bin/permis %P&quot; </p>
<dt><code>lcas</code></p>
<dd>lcas library directory database &#8211; Call LCAS functions to check rule. Here library is path to shared library of LCAS, either absolute or relative to directory; directory is path to LCAS installation directory, equivalent of LCAS_DIR variable; database is path to LCAS database, equivalent to LCAS_DB_FILE variable. Each arguments except library is optional and may be either skipped or replaced with ’*’. </p>
<p> <i>Example:</i><br />
 lcas=&quot;&quot; </p>
<dt><code>remote</code></p>
<dd>remote URL &#8230; &#8211; Check user&#8217;s credentials against remote service. Only DN groups stored at LDAP directories are supported. Multiple URLs are allowed in this rule. </p>
<p> <i>Example:</i><br />
 remote=&quot;<a href="ldap://grid-vo.nordugrid.org/ou=People,dc=nordugrid,dc=org">ldap://grid-vo.nordugrid.org/ou=People,dc=nordugrid,dc=org</a>&quot; </p>
<dt><code>vo</code></p>
<dd>vo vo_name &#8230; &#8211; Match user belonging to VO specified by &quot;vo=vo_name&quot; as configured in one of PREVIOUSLY defined [vo] blocks. Multiple VO names are allowed for this rule. </p>
<p> <i>Example:</i><br />
 vo=&quot;nordugrid&quot; </p>
<dt><code>all</code></p>
<dd>all &#8211; Matches any user identity. This command requires no arguments but<br />
&nbsp;<wbr>still can be written as all=&quot;&quot;&nbsp;<wbr>or all=&nbsp;<wbr>for consistency. </p>
<p> <i>Example:</i><br />
 all=&quot;&quot; </p>
</dl>
<h2>The [grid-manager] block</h2>
<p>The [grid-manager] block configures the part of A-REX service hosted in <code>arched</code> taking care of the grid tasks on the frontend (stagein/stageout, LRMS job submission, caching, etc..). Name of this block is historical and comes from times then this functionality was handled by separate process called grid-manager. This section also configures WS interfaces of A-REX service also hosted by same container. </p>
<dl>
<dt><code>controldir</code></p>
<dd>controldir path &#8211; The directory of the A-REX&#8217;s internal job log files, not needed on the nodes. &lt;must be set&gt; </p>
<p> <i>Example:</i><br />
 controldir=&quot;/var/spool/nordugrid/jobstatus&quot; </p>
<dt><code>sessiondir</code></p>
<dd>sessiondir path [drain] &#8211; the directory which holds the sessiondirs of the grid jobs. Multiple session directories may be specified by specifying multiple sessiondir commands. In this case jobs are spread evenly over the session directories. If sessiondir=&quot;*&quot; is set, the session directory will be spread over the ${HOME}/.jobs directories of every locally mapped unix user. It is preferred to use common session directories. The path may be followed by &quot;drain&quot;, in which case no new jobs will be assigned to that sessiondir, but current jobs will still be processed and accessible. &lt;sessiondir must be set&gt; </p>
<p> <i>Example:</i><br />
 sessiondir=&quot;/scratch/grid&quot;<br />
 sessiondir=&quot;/mnt/grid drain&quot; </p>
<dt><code>runtimedir</code></p>
<dd>runtimedir path &#8211; The directory which holds the runtimeenvironment scripts, should be available on the nodes as well! The runtimeenvironments are automatically detected and advertised in the information system. </p>
<p> <i>Example:</i><br />
 runtimedir=&quot;/SOFTWARE/runtime&quot; </p>
<dt><code>scratchdir</code></p>
<dd>scratchdir path &#8211; path on computing node to move session directory to before execution. If defined should contain the path to the directory on the computing node which can be used to store a jobs&#8217; files during execution. Sets the environment variable RUNTIME_LOCAL_SCRATCH_DIR. Default is not to move session directory before execution. </p>
<p> <i>Example:</i><br />
 scratchdir=&quot;/local/scratch/&quot; </p>
<dt><code>shared_scratch</code></p>
<dd>shared_scratch path &#8211; path on frontend where scratchdir can be found. If defined should contain the path corresponding to that set in scratchdir as seen on the frontend machine. Sets the environment variable RUNTIME_FRONTEND_SEES_NODE. </p>
<p> <i>Example:</i><br />
 shared_scratch=&quot;/mnt/scratch&quot; </p>
<dt><code>nodename</code></p>
<dd>nodename path &#8211; command to obtain hostname of computing node. </p>
<p> <i>Example:</i><br />
 nodename=&quot;/bin/hostname&quot; </p>
<dt><code>cachedir</code></p>
<dd>cachedir cache_path [link_path] &#8211; specifies a directory to store cached data. Multiple cache directories may be specified by specifying multiple cachedir commands. Cached data will be distributed evenly over the caches. Specifying no cachedir command or commands with an empty path disables caching. Optional link_path specifies the path at which the cache_path is accessible on computing nodes, if it is different from the path on the A-REX host. Example: cache=&quot;/shared/cache /frontend/jobcache&quot; If &quot;link-path&quot; is set to &#8216;.&#8217; files are not soft-linked, but copied to session directory. If a cache directory needs to be drained, then cachedir should specify &quot;drain&quot; as the link path, in which case no new files will be added to the cache. </p>
<p> <i>Example:</i><br />
 cachedir=&quot;/scratch/cache&quot;<br />
 cachedir=&quot;/fs1/cache drain&quot; </p>
<dt><code>remotecachedir</code></p>
<dd>remotecachedir cache_path [link_path] &#8211; specifies caches which are under the control of other A-REXs, but which this A-REX can have read-only access to. Multiple remote cache directories may be specified by specifying multiple remotecachedir commands. If a file is not available in paths specified by cachedir, A-REX looks in remote caches. link_path has the same meaning as in cachedir, but the special path &#8220;replicate&#8221; means files will be replicated from remote caches to local caches when they are requested. </p>
<p> <i>Example:</i><br />
 remotecachedir=&quot;/mnt/fs1/cache replicate&quot; </p>
<dt><code>cachesize</code></p>
<dd>cachesize max min &#8211; specifies high and low watermarks for space used by cache, as a percentage of the space on the file system on which the cache directory is located. When the max is exceeded, files will be deleted to bring the used space down to the min level. It is a good idea to have the cache on its own separate file system. To turn off this feature &quot;cachesize&quot; without parameters can be specified. </p>
<p> <i>Example:</i><br />
 cachesize=&quot;80 70&quot; </p>
<dt><code>cachelifetime</code></p>
<dd>If cache cleaning is enabled, files accessed less recently than the given time period will be deleted. Example values of this option are 1800, 90s, 24h, 30d. When no suffix is given the unit is seconds. </p>
<p> <i>Example:</i><br />
 cachelifetime=&quot;30d&quot; </p>
<dt><code>cacheshared</code></p>
<dd>cacheshared yes|no &#8211; specifies whether the caches share a filesystem with other data. If set to yes then cache-clean calculates the size of the cache instead of using filesystem used space. </p>
<p> <i>Example:</i><br />
 cacheshared=&quot;yes&quot; </p>
<dt><code>cachespacetool</code></p>
<dd>cachespacetool path [options] &#8211; specifies an alternative tool to &quot;df&quot; that cache-clean should use to obtain space information on the cache file system. The output of this command must be &quot;total_bytes used_bytes&quot;. The cache directory is passed as the last argument to this command. </p>
<p> <i>Example:</i><br />
 cachespacetool=&quot;/etc/getspace.sh&quot; </p>
<dt><code>cachelogfile</code></p>
<dd>cachelogfile path &#8211; specifies the filename where output of the cache-clean tool should be logged. Defaults to /var/log/arc/cache-clean.log. </p>
<p> <i>Example:</i><br />
 cachelogfile=&quot;/tmp/cache-clean.log&quot; </p>
<dt><code>cacheloglevel</code></p>
<dd>cacheloglevel level &#8211; specifies the level of logging by the cache-clean tool, between 0 (FATAL) and 5 (DEBUG). Defaults to 3 (INFO). </p>
<p> <i>Example:</i><br />
 cacheloglevel=&quot;4&quot; </p>
<dt><code>cachecleantimeout</code></p>
<dd>cachecleantimeout time &#8211; the timeout in seconds for running the cache-clean tool. If using a large cache or slow file system this value can be increased to allow the cleaning to complete. Defaults to 3600 (1 hour). </p>
<p> <i>Example:</i><br />
 cachecleantimeout=&quot;10000&quot; </p>
<dt><code>cacheaccess</code></p>
<dd>cacheaccess rule &#8211; rules for allowing access to files in the cache remotely through the A-REX web interface. A rule has three parts:<br />
&nbsp;<wbr>1. Regular expression defining a URL pattern<br />
&nbsp;<wbr>2. Credential attribute to match against a client&#8217;s credential<br />
&nbsp;<wbr>3. Regular expression defining a credential value to match against a client&#8217;s<br />
&nbsp;<wbr>credential A client is allowed to access the cached file if a URL pattern matches the cached file URL and the client&#8217;s credential has the attribute and matches the value required for that pattern. Possible values for credential attribute are dn, voms:vo, voms:role and voms:group. Remote cache access requires that the A-REX web interface is enabled via arex_mount_point. </p>
<p> <i>Examples:</i><br />
 cacheaccess=&quot;<a href="gsiftp://host.org/private/data/.*">gsiftp://host.org/private/data/.*</a> voms:vo myvo:production&quot;<br />
 cacheaccess=&quot;<a href="gsiftp://host.org/private/data/ng/.*">gsiftp://host.org/private/data/ng/.*</a> dn /O=Grid/O=NorduGrid/.*&quot; </p>
<dt><code>enable_cache_service</code></p>
<dd>enable_cache_service yes|no &#8211; Turn on or off the cache service interface. If turned on the cache service must be installed and the A-REX WS interface must be enabled via arex_mount_point. The interface is accessible at the same host and port as given inn arex_mount_point with path /cacheservice. Default is off. </p>
<p> <i>Example:</i><br />
 enable_cache_service=&quot;yes&quot; </p>
<dt><code>user</code></p>
<dd>user user[:group] &#8211; Switch to a non root user/group after startup. Use with caution. </p>
<p> <i>Example:</i><br />
 user=&quot;grid&quot; </p>
<dt><code>debug</code></p>
<dd>debug debuglevel &#8211; Set debug level of the arched daemon hosting A-REX service, between 0 (FATAL) and 5 (DEBUG). Defaults to 3 (INFO). </p>
<p> <i>Example:</i><br />
 debug=&quot;2&quot; </p>
<dt><code>logfile</code></p>
<dd>logfile path &#8211; Specify log file location. If using an external log rotation tool be careful to make sure it matches the path specified here. Default log file is &quot;/var/log/arc/grid-manager.log&quot; </p>
<p> <i>Example:</i><br />
 logfile=&quot;/var/log/arc/grid-manager.log&quot; </p>
<dt><code>wslogfile</code></p>
<dd>wslogfile path &#8211; Specify log file location for WS-interface operations. This file is only created if the WS-interface is enabled through the arex_mount_point option. The logsize, logreopen and debug options also apply to this file. If using an external log rotation tool be careful to make sure it matches the path specified here. It is possible to specify the same file as logfile to combine the logs. Default is /var/log/arc/ws-interface.log. </p>
<p> <i>Example:</i><br />
 wslogfile=&quot;/var/log/arc/ws-interface.log&quot; </p>
<dt><code>logsize</code></p>
<dd>logsize size [number] &#8211; &#8216;Size&#8217; specifies in bytes how big log file is allowed to grow (approximately). If log file exceeds specified size it is renamed into logfile.0. And logfile.0 is renamed into logfile.1, etc. up to &#8216;number&#8217; logfiles. Don&#8217;t set logsize if you don&#8217;t want to enable the ARC logrotation because another logrotation tool is used. </p>
<p> <i>Example:</i><br />
 logsize=&quot;100000 2&quot; </p>
<dt><code>logreopen</code></p>
<dd>logreopen yes|no &#8211; Specifies if log file must be closed after each record is added. By default arched keeps log file open. This option can be used to make behaviour of arched compatible with external log rotation utilities. </p>
<p> <i>Example:</i><br />
 logreopen=&quot;no&quot; </p>
<dt><code>pidfile</code></p>
<dd>pidfile path &#8211; Specify location of file containing PID of daemon process. This is useful for automatic start/stop scripts. </p>
<p> <i>Example:</i><br />
 pidfile=&quot;/var/run/arched-arex.pid&quot; </p>
<dt><code>gnu_time</code></p>
<dd>the gnu time command, default /usr/bin/time </p>
<p> <i>Example:</i><br />
 gnu_time=&quot;/usr/bin/time&quot; </p>
<dt><code>shared_filesystem</code></p>
<dd>if computing node can access session directory at frontend, defaults to &#8216;yes&#8217; </p>
<p> <i>Example:</i><br />
 shared_filesystem=&quot;yes&quot; </p>
<dt><code>mail</code></p>
<dd>specifies the email address from where the notification mails are sent, &lt;must be specified&gt; </p>
<p> <i>Example:</i><br />
 mail=&quot;grid.support [at] somewhere.org&quot; </p>
<dt><code>joblog</code></p>
<dd>joblog path &#8211; specifies where to store specialized log about started and finished jobs. If path is empty or no such command &#8211; log is not written. This log is not used by any other part of ARC, so keep it disabled unless needed. </p>
<p> <i>Example:</i><br />
 joblog=&quot;/var/log/arc/gm-jobs.log&quot; </p>
<dt><code>jobreport</code></p>
<dd>jobreport [URL &#8230;] [timeout] &#8211; tells to report all started and finished jobs to logger service at &#8216;URL&#8217;. Multiple URLs and multiple jobreport commands are allowed. In that case the job info will be sent to all of them. Timeout specifies how long (in days) to try to pass information before give up. Suggested value is 30 days. </p>
<p> <i>Example:</i><br />
 jobreport=&quot;<a rel="nofollow" href="https://grid.uio.no:8001/logger">https://grid.uio.no:8001/logger</a>&quot; </p>
<dt><code>jobreport_publisher</code></p>
<dd>jobreport publisher &#8211; name of the accounting records publisher. </p>
<p> <i>Example:</i><br />
 jobreport_publisher=&quot;jura&quot; </p>
<dt><code>jobreport_credentials</code></p>
<dd>jobreport credentials path [key_file [cert_file [ca_dir]]] &#8211; specifies the credentials for accessing the accounting service. </p>
<p> <i>Example:</i><br />
 jobreport_credentials=&quot;/etc/grid-security/hostkey.pem /etc/grid-security/hostcert.pem /etc/grid-security/certificates&quot; </p>
<dt><code>jobreport_options</code></p>
<dd>jobreport options [name:value, &#8230;]- specifies additional parameters for the jobreporter. </p>
<p> <i>Example:</i><br />
 jobreport_options=&quot;urbatch:50,archiving:/tmp/archive,topic:/topic/global.accounting.cpu.central&quot; </p>
<dt><code>jobreport_logfile</code></p>
<dd>jobreport logfile &#8211; name of the file to store stderr of the publisher executable. </p>
<p> <i>Example:</i><br />
 jobreport_logfile=&quot;/var/log/arc/jura.log&quot; </p>
<dt><code>max_job_control_requests</code></p>
<dd>max_job_control_requests number &#8211; max number of simultaneously processed job management requests over WS interface &#8211; like job submission, cancel, status check etc. Default value is 100. </p>
<p> <i>Example:</i><br />
 max_job_control_requests=&quot;100&quot; </p>
<dt><code>max_infosys_requests</code></p>
<dd>max_infosys_requests number &#8211; max number of simultaneously processed resource info requests over WS interface. Default value is 1. </p>
<p> <i>Example:</i><br />
 max_infosys_requests=&quot;1&quot; </p>
<dt><code>max_data_transfer_requests</code></p>
<dd>max_data_transfer_requests number &#8211; max number of simultaneously processed data transfer requests over WS interface &#8211; like data staging. Default value is 100. </p>
<p> <i>Example:</i><br />
 max_data_transfer_requests=&quot;100&quot; </p>
<dt><code>maxjobs</code></p>
<dd>maxjobs number1 number2 number3 number4 &#8211; specifies maximum allowed number of jobs.<br />
&nbsp;<wbr>number1 &#8211; jobs which are not in FINISHED state&nbsp;<wbr>(jobs tracked in RAM)<br />
&nbsp;<wbr>number2 &#8211; jobs being run&nbsp;<wbr>(SUBMITTING, INLRMS states)<br />
&nbsp;<wbr>number3 &#8211; jobs being processed per DN<br />
&nbsp;<wbr>number4 &#8211; jobs in whole system<br />
&nbsp;<wbr> Missing number or -1 means no limit. </p>
<p> <i>Example:</i><br />
 maxjobs=&quot;10000 10 2000&quot; </p>
<dt><code>wakeupperiod</code></p>
<dd>wakeupperiod time &#8211; specifies how often A-REX cheks for new jobs arrived, job state change requests, etc. That is resposivity of A-REX. &#8216;time&#8217; is time period in seconds. Default is 3 minutes. Usually this command is not needed because important state changes are also trigering out-of-schedule checks. </p>
<p> NOTE: This parameter does not affect responsivity of backend scripts &#8211; especially scan-*-job. That means that upper estimation of time for detecting job finished executing is sum of responsivity of backend script + wakeupperiod. </p>
<p> <i>Example:</i><br />
 wakeupperiod=&quot;180&quot; </p>
<dt><code>defaultttl</code></p>
<dd>defaultttl [ttl [ttr]] &#8211; ttl is the time in seconds for how long a session directory will survive after job execution has finished. If not specified the default is 1 week. ttr is how long information about a job will be kept after the session directory is deleted. If not specified, the ttr default is one month. </p>
<p> <i>Example:</i><br />
 defaultttl=&quot;259200&quot; </p>
<dt><code>authplugin</code></p>
<dd>authplugin state options plugin_path &#8211; Every time job goes to &#8216;state&#8217; run &#8216;plugin_path&#8217; executable. Options consist of key=value pairs separated by &#8216;,&#8217;. </p>
<p> Possible keys are<br />
&nbsp;<wbr>timeout &#8211; wait for result no longer that&nbsp;<wbr>&#8216;value&#8217;&nbsp;<wbr>seconds&nbsp;<wbr>(timeout=&nbsp;<wbr>can be omitted).<br />
&nbsp;<wbr>onsuccess,onfailure,ontimeout &#8211; what to do if plugin exited with exit code 0, not 0, timeout achieved.<br />
&nbsp;<wbr>&nbsp;<wbr>Possible actions are:<br />
pass &#8211; continue executing job,<br />
fail &#8211; cancel job,<br />
log &#8211; write to log fail about problem and continue executing job. </p>
<p> <i>Example:</i><br />
 authplugin=&quot;ACCEPTED timeout=10 /usr/libexec/arc/bank %C/job.%I.local %S&quot; </p>
<dt><code>authplugin</code></p>
<dd>ARC is distributed with the plugin &quot;inputcheck&quot;. Its purpose is to check if input files requested in job&#8217;s RSL are accessible from this machine. It is better to run it before job enters cluster. It accepts 2 arguments: names of files containing RSL and credentials&#8217; proxy. This plugin is only guaranteed to work for job submitted through the legacy GridFTP interface, as this is the only interface for which credentials in the form of proxy certificate files are guaranteed to exist. </p>
<p> <i>Example:</i><br />
 authplugin=&quot;ACCEPTED 60 /usr/libexec/arc/inputcheck %C/job.%I.description %C/job.%I.proxy&quot; </p>
<dt><code>authplugin</code></p>
<dd>ARC is distributed with the plugin &quot;arc-vomsac-check&quot;. Its purpose is to enforce per-queue access policies based on VOMS attributes present in user&#8217;s proxy-certificate. Plugin should be run before job enters the cluster. It requires 2 argments: path to job information .local file and path to credentials file. Enforced per-queue access policies are configured with &#8216;ac_policy&#8217; option in the [queue/name] configuration block. </p>
<p> <i>Example:</i><br />
 authplugin=&quot;ACCEPTED 60 /usr/libexec/arc/arc-vomsac-check -L %C/job.%I.local -P %C/job.%I.proxy&quot; </p>
<dt><code>localcred</code></p>
<dd>localcred timeout plugin_path &#8211; Every time an external executable is run this plugin will be called. Its purpose is to set non-unix permissions/credentials on running tasks. Note: the process itself can still be run under the root account. If plugin_path looks like somename [at] somepath, then function &#8216;somename&#8217; from the shared library located at &#8216;somepath&#8217; will be called (timeout is not effective in that case). A-REX must be run as root to use this option. Comment it out unless you really know what you are doing. </p>
<p> <i>Example:</i><br />
 localcred=&quot;0 acquire@/opt/nordugrid/lib/afs.so %C/job.%I.proxy&quot; </p>
<dt><code>norootpower</code></p>
<dd>norootpower yes|no &#8211; if set to yes, all job management proccesses will switch to mapped user&#8217;s identity while accessing session directory. This is useful if session directory is on NFS root squashing turned on. Default is no. </p>
<p> <i>Example:</i><br />
 norootpower=&quot;yes&quot; </p>
<dt><code>allowsubmit</code></p>
<dd>allowsubmit [group &#8230;] &#8211; list of authorization groups of users allowed to submit new jobs while &quot;allownew=no&quot; is active in jobplugin configuration. Multiple commands are allowed. </p>
<p> <i>Example:</i><br />
 allowsubmit=&quot;mygroup&quot;<br />
 allowsubmit=&quot;yourgroup&quot; </p>
<dt><code>helper</code></p>
<dd>helper user executable arguments &#8211; associates an external program with A-REX. This program will be kept running under the account of the user specified by username. Currently only ’.’ is supported as username, corresponding to the user running A-REX. Every time this executable finishes it will be started again. This helper plugin mechanism can be used as an alternative to /etc/init.d or cron to (re)start external processes. </p>
<p> <i>Example:</i><br />
 helper=&quot;. /usr/local/bin/myutility&quot; </p>
<dt><code>tmpdir</code></p>
<dd>tmpdir &#8211; used by the A-REX, default is /tmp </p>
<p> <i>Example:</i><br />
 tmpdir=&quot;/tmp&quot; </p>
<dt><code>maxrerun</code></p>
<dd>maxrerun &#8211; specifies how many times job can be rerun if it failed in LRMS. Default value is 5. This is only an upper limit, the actual rerun value is set by the user in his xrsl. </p>
<p> <i>Example:</i><br />
 maxrerun=&quot;5&quot; </p>
<dt><code>globus_tcp_port_range</code></p>
<dd>globus_tcp_port_range, globus_udp_port_range &#8211; Firewall configuration. </p>
<p> <i>Example:</i><br />
 globus_tcp_port_range=&quot;9000,12000&quot;<br />
 globus_udp_port_range=&quot;9000,12000&quot; </p>
<dt><code>x509_user_key</code></p>
<dd>x509_user_cert, x509_user_key &#8211; Location of credentials for service. These may be used by any module or external utility which need to contact another service not on behalf of user who submited job. </p>
<p> <i>Example:</i><br />
 x509_user_key=&quot;/etc/grid-security/hostkey.pem&quot;<br />
 x509_user_cert=&quot;/etc/grid-security/hostcert.pem&quot; </p>
<dt><code>x509_cert_dir</code></p>
<dd>x509_cert_dir &#8211; Location of trusted CA certificates </p>
<p> <i>Example:</i><br />
 x509_cert_dir=&quot;/etc/grid-security/certificates&quot; </p>
<dt><code>http_proxy</code></p>
<dd>http_proxy &#8211; http proxy server location </p>
<p> <i>Example:</i><br />
 http_proxy=&quot;proxy.mydomain.org:3128&quot; </p>
<dt><code>fixdirectories</code></p>
<dd>fixdirectories yes|missing|no &#8211; specifies during startup A-REX should create all directories needed for it operation and set suitable default permissions. If &quot;no&quot; is specified then A-REX does nothing to prepare its operational environment. In case of &quot;missing&quot; A-REX only creates and sets permissions for directories which are not present yet. For &quot;yes&quot; all directories are created and permisisons for all used directories are set to default safe values. Default behaviour is as if &quot;yes&quot; is specified. </p>
<p> <i>Example:</i><br />
 fixdirectories=&quot;yes&quot; </p>
<dt><code>arex_mount_point</code></p>
<dd>arex_mount_point &#8211; enables web services interfaces, including job execution and information system. The argument is an https URL defining the endpoint port and path: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>https://&lt;hostname&gt;:&lt;port&gt;/&lt;path&gt; </p>
<p> In order to submit job a client must specify the exact published path. Make sure the chosen port is not blocked by firewall or other security rules. </p>
<p> <i>Example:</i><br />
 arex_mount_point=&quot;<a rel="nofollow" href="https://piff.hep.lu.se:443/arex">https://piff.hep.lu.se:443/arex</a>&quot; </p>
<dt><code>enable_arc_interface</code></p>
<dd>enable_arc_interface yes|no &#8211; turns on or off the ARC own WS interface based on OGSA BES and WSRF. If enabled the interface can be accessed at the URL specified by arex_mount_point (this option must also be specified). Default is yes. </p>
<p> <i>Example:</i><br />
 enable_arc_interface=&quot;yes&quot; </p>
<dt><code>enable_emies_interface</code></p>
<dd>enable_emies_interface &#8211; enable the EMI Execution Service interface. If enabled the interface can be accessed at the URL specified in arex_mount_point (this option must also be specified) </p>
<p> <i>Example:</i><br />
 enable_emies_interface=&quot;yes&quot; </p>
<dt><code>arguspep_endpoint</code></p>
<dd>arguspep_endpoint &#8211; specifies URL of Argus PEPD service (by default, the argus pepd service runs on port 8154 with path /authz) to use for authorization and user mapping. It is worth to mention that &quot;requireClientCertAuthentication&quot; (default is false) item of pepd.ini (configuration of Argus PEPD service) is set to be &#8216;true&#8217;, then https should be used, otherwise http is proper. If specified Argus is contacted for every operation requested through WS interface (see arex_mount_point). </p>
<p> <i>Example:</i><br />
 arguspep_endpoint=&quot;<a rel="nofollow" href="https://somehost.somedomain:8154/authz">https://somehost.somedomain:8154/authz</a>&quot; </p>
<dt><code>arguspep_profile</code></p>
<dd>arguspep_profile &#8211; defines which communication profile to use while communicationg with Argus PEPD service. Possible values are:<br />
&nbsp;<wbr>direct &#8211; pass all authorization attributes&nbsp;<wbr>(only for debugging)<br />
&nbsp;<wbr>subject &#8211; pass only subject name of client<br />
&nbsp;<wbr>cream &#8211; makes A-REX pretend it is gLite CREAM service. This is&nbsp;<wbr>&nbsp;<wbr><br />
recommended profile for interoperability with gLite.<br />
&nbsp;<wbr>emi &#8211; new profile devloped in EMI project. This is default option. </p>
<p> <i>Example:</i><br />
 arguspep_profile=&quot;cream&quot; </p>
<dt><code>arguspep_usermap</code></p>
<dd>arguspep_usermap &#8211; specifies either response from Argus servie may define mapping of client to local account. Possible values are &#8216;yes&#8217; and &#8216;no&#8217;. Default is &#8216;no&#8217;. Argus is contacted after all other user mapping is performed. Hence it can overwrite all other decisions. </p>
<p> <i>Example:</i><br />
 arguspep_usermap=&quot;no&quot; </p>
<dt><code>arguspdp_endpoint</code></p>
<dd>arguspdp_endpoint &#8211; specifies URL of Argus PDP service (by default, the argus pepd service runs on port 8152 with path /authz) to use for authorization and user mapping. It is worth to mention that &quot;requireClientCertAuthentication&quot; (default is false) item of pdp.ini (configuration of Argus PDP service) is set to be &#8216;true&#8217;, then https should be used, otherwise http is proper. If specified Argus is contacted for every operation requested through WS interface (see arex_mount_point). </p>
<p> <i>Example:</i><br />
 arguspdp_endpoint=&quot;<a rel="nofollow" href="https://somehost.somedomain:8152/authz">https://somehost.somedomain:8152/authz</a>&quot; </p>
<dt><code>arguspdp_profile</code></p>
<dd>arguspdp_profile &#8211; defines which communication profile to use while communicationg with Argus PDP service. Possible values are:<br />
&nbsp;<wbr>subject &#8211; pass only subject name of client<br />
&nbsp;<wbr>cream &#8211; makes A-REX pretend it is gLite CREAM service. This is&nbsp;<wbr>&nbsp;<wbr><br />
recommended profile for interoperability with gLite.<br />
&nbsp;<wbr>emi &#8211; new profile devloped in EMI project. This is default option. </p>
<p> <i>Example:</i><br />
 arguspdp_profile=&quot;cream&quot; </p>
<dt><code>arguspdp_acceptnotapplicable</code></p>
<dd>arguspdp_accpetnotapplicable &#8211; specify if the &quot;NotApplicable&quot; decision returned by Argus PDP service is treated as reason to deny request. Default is no, which treats &quot;NotApplicable&quot; as reson to deny request.<br />
&nbsp;<wbr> <i>Example:</i><br />
 arguspdp_acceptnotapplicable=&quot;no&quot; </p>
<dt><code>watchdog</code></p>
<dd>watchdog &#8211; specifies if additinal watchdog processes is spawned to restart main process if it is stuck or dies. Possible values are &#8216;yes&#8217; and &#8216;no&#8217;. Default is &#8216;no&#8217;. </p>
<p> <i>Example:</i><br />
 watchdog=&quot;no&quot; </p>
<dt><code>groupcfg</code></p>
<dd>groupcfg group_name [group_name &#8230;] &#8211; specifies authorization groups for grid-manager to accept. The main location of this parameter is inside [gridftpd/jobs] block. The &#8216;groupcfg&#8217; located here is only effective if computing service is configured without GridFTP interface and hence [gridftpd/jobs] block is missing. </p>
<p> <i>Example:</i><br />
 groupcfg=&quot;users&quot; </p>
<dt><code>unixmap unixgroup unixvo</code></p>
<dd>unixmap [unixname][:unixgroup] rule &#8211; more sophisticated mapping to local account<br />
 unixgroup group rule &#8211; more sophisticated mapping to local account for specific authorization groups.<br />
 unixvo vo rule &#8211; more sophisticated mapping to local account for users belonging to specified VO.<br />
 The main location for these parameters is [gridftpd] section. If located here they are only active if computing service is configured without GridFTP interface and hence [gridftpd/jobs] block is missing. For more detailed information see section [gridftpd] and read &quot;ARC Computing Element. System Administrator guide&quot; manual. </p>
<p> <i>Example:</i><br />
 unixmap=&quot;nobody:nogroup all&quot;<br />
 unixgroup=&quot;users simplepool /etc/grid-security/pool/users&quot;<br />
 unixvo=&quot;ATLAS unixuser atlas:atlas&quot; </p>
<dt><code>allowunknown</code></p>
<dd>allowunknown yes|no &#8211; check user subject against grid-mapfile. The main location for this parameter is [gridftpd] section. If located here it is only active if computing service is configured without GridFTP interface and hence [gridftpd/jobs] block is missing. For more detailed information see section [gridftpd]. </p>
<p> <i>Example:</i><br />
 allowunknown=&quot;no&quot; </p>
<dt><code>delegationdb</code></p>
<dd>delegationdb db_name &#8211; specify which DB to use to store delegations. Currently supported db_names are bdb and sqlite. Default is bdb. </p>
<p> <i>Example:</i><br />
 delegationdb=&quot;bdb&quot; </p>
<dt><code>forcedefaultvoms</code></p>
<dd>forcedefaultvoms VOMS_FQAN &#8211; specify VOMS FQAN which user will be assigned if his/her credentials contain no VOMS attributes. To assign different values to different queues put this command into [queue] block. </p>
<p> <i>Example:</i><br />
 forcedefaultvoms=&quot;/vo/group/subgroup&quot; </p>
</dl>
<h2>[data-staging] block</h2>
<p>[data-staging] block configures DTR data staging parameters. </p>
<dl>
<dt><code>debug</code></p>
<dd>debug &#8211; Log level for transfer logging in job.id.errors files, between 0 (FATAL) and 5 (DEBUG). Default is to use value set by debug option in [grid-manager] section. </p>
<p> <i>Example:</i><br />
 debug=&quot;4&quot; </p>
<dt><code>maxdelivery</code></p>
<dd>maxdelivery &#8211; Maximum number of concurrent file transfers, i.e. active transfers using network bandwidth. This is the total number for the whole system including any remote staging hosts. Default is 10. </p>
<p> <i>Example:</i><br />
 maxdelivery=&quot;40&quot; </p>
<dt><code>maxprocessor</code></p>
<dd>maxprocessor &#8211; Maximum number of concurrent files in each pre- and post- processing state, eg cache check or replica resolution. Default is 10. </p>
<p> <i>Example:</i><br />
 maxprocessor=&quot;20&quot; </p>
<dt><code>maxemergency</code></p>
<dd>maxemergency &#8211; Maximum &quot;emergency&quot; slots which can be assigned to transfer shares when all slots up to the limits configured by the above two options are used by other shares. This ensures shares cannot be blocked by others. Default is 1. </p>
<p> <i>Example:</i><br />
 maxemergency=&quot;5&quot; </p>
<dt><code>maxprepared</code></p>
<dd>maxprepared &#8211; Maximum number of files in a prepared state, i.e. pinned on a remote storage such as SRM for transfer. A good value is a small multiple of maxdelivery. Default is 200. </p>
<p> <i>Example:</i><br />
 maxprepared=&quot;250&quot; </p>
<dt><code>sharetype</code></p>
<dd>sharetype &#8211; Scheme to assign transfer shares. Possible values are dn, voms:vo, voms:role and voms:group. </p>
<p> <i>Example:</i><br />
 sharetype=&quot;voms:role&quot; </p>
<dt><code>definedshare</code></p>
<dd>definedshare &#8211; Defines a share with a fixed priority, different from the default (50). Priority is an integer between 1 (lowest) and 100 (highest). </p>
<p> <i>Example:</i><br />
 definedshare=&quot;myvo:production 80&quot;<br />
 definedshare=&quot;myvo:student 20&quot; </p>
<dt><code>dtrlog</code></p>
<dd>dtrlog &#8211; A file in which data staging state information (for monitoring and recovery purposes) is periodically dumped. Default is controldir/dtrstate.log </p>
<p> <i>Example:</i><br />
 dtrlog=&quot;/tmp/dtrstate.log&quot; </p>
<dt><code>deliveryservice</code></p>
<dd>The following 4 options are used to configure multi-host data staging. deliveryservice &#8211; URL to a data delivery service which can perform remote data staging </p>
<p> <i>Example:</i><br />
 deliveryservice=&quot;<a rel="nofollow" href="https://myhost.org:60003/datadeliveryservice">https://myhost.org:60003/datadeliveryservice</a>&quot; </p>
<dt><code>localdelivery</code></p>
<dd>localdelivery &#8211; If any deliveryservice is defined, this option determines whether local data transfer is also performed. Default is no. </p>
<p> <i>Example:</i><br />
 localdelivery=&quot;yes&quot; </p>
<dt><code>remotesizelimit</code></p>
<dd>remotesizelimit &#8211; Lower limit on file size (in bytes) of files that remote hosts should transfer. Can be used to increase performance by transferring small files using local processes. </p>
<p> <i>Example:</i><br />
 remotesizelimit=&quot;100000&quot; </p>
<dt><code>usehostcert</code></p>
<dd>usehostcert &#8211; Whether the A-REX host certificate should be used for communication with remote hosts instead of the users&#8217; proxies. Default is no. </p>
<p> <i>Example:</i><br />
 usehostcert=&quot;yes&quot; </p>
<dt><code>acix_endpoint</code></p>
<dd>acix_endpoint URL &#8211; the ARC Cache Index specified here will be queried for every input file specified in a job description and any replicas found in sites with accessible caches will be added to the replica list of the input file. The replicas will be tried in the order specified by <code>preferredpattern.</code> </p>
<p> <i>Example:</i><br />
 acix_endpoint=&quot;<a rel="nofollow" href="https://cacheindex.ndgf.org:6443/data/index">https://cacheindex.ndgf.org:6443/data/index</a>&quot; </p>
<dt><code>securetransfer</code></p>
<dd>securetransfer yes|no &#8211; if data connection allows to choose use secure|non-secure data transfer. Currently only works for gridftp. default is no </p>
<p> <i>Example:</i><br />
 securetransfer=&quot;no&quot; </p>
<dt><code>passivetransfer</code></p>
<dd>passivetransfer yes|no &#8211; If yes, gridftp transfers are passive. Setting this option to yes can solve transfer problems caused by firewalls. default is no </p>
<p> <i>Example:</i><br />
 passivetransfer=&quot;no&quot; </p>
<dt><code>httpgetpartial</code></p>
<dd>httpgetpartial yes|no &#8211; If yes, HTTP GET transfers may transfer data in chunks/parts. If no &#8211; data is always transfered in one piece. Default is yes. </p>
<p> <i>Example:</i><br />
 httpgetpartial=&quot;yes&quot; </p>
<dt><code>speedcontrol</code></p>
<dd>speedcontrol min_speed min_time min_average_speed max_inactivity &#8211; specifies how slow data transfer must be to trigger error. Tranfer is canceled if speed is below min_speed bytes per second for at least min_time seconds, or if average rate is below min_average_speed bytes per second, or no data was transfered for longer than max_inactivity seconds. Value of zero turns feature off. Default is &quot;0 300 0 300&quot; </p>
<p> <i>Example:</i><br />
 speedcontrol=&quot;0 300 0 300&quot; </p>
<dt><code>preferredpattern</code></p>
<dd>preferredpattern pattern &#8211; specifies a preferred pattern on which to sort multiple replicas of an input file. It consists of one or more patterns separated by a pipe character (|) listed in order of preference. Replicas will be ordered by the earliest match. If the dollar character ($) is used at the end of a pattern, the pattern will be matched to the end of the hostname of the replica. </p>
<p> <i>Example:</i><br />
 preferredpattern=&quot;<a href="srm://myhost.ac.uk|.uk$|ndgf.org$">srm://myhost.ac.uk|.uk$|ndgf.org$</a>&quot; </p>
<dt><code>copyurl</code></p>
<dd>copyurl url_head local_path &#8211; specifies that URLs, starting from &#8216;url_head&#8217; should be accessed in a different way (most probaly unix open). The file from obtained path will be copied to the session directory. NOTE: &#8216;local_path&#8217; can also be of URL type. you can have several copyurl lines </p>
<p> <i>Example:</i><br />
 copyurl=&quot;<a href="gsiftp://example.org:2811/data/">gsiftp://example.org:2811/data/</a> <a href="gsiftp://example.org/data/">gsiftp://example.org/data/</a>&quot;<br />
 copyurl=&quot;<a href="gsiftp://example2.org:2811/data/">gsiftp://example2.org:2811/data/</a> <a href="gsiftp://example2.org/data/">gsiftp://example2.org/data/</a>&quot; </p>
<dt><code>linkurl</code></p>
<dd>linkurl url_head local_path [node_path] &#8211; identical to &#8216;copyurl&#8217;, only file won&#8217;t be copied, but soft-link will be created. The &#8216;local_path&#8217; specifies the way to access the file from the gatekeeper, and is used to check permissions. The &#8216;node_path&#8217; specifies how the file can be accessed from computing nodes, and will be used for soft-link creation. If &#8216;node_path&#8217; is missing &#8211; &#8216;local_path&#8217; will be used. you can have multiple linkurl settings </p>
<p> <i>Example:</i><br />
 linkurl=&quot;<a href="gsiftp://somewhere.org/data">gsiftp://somewhere.org/data</a> /data&quot;<br />
 linkurl=&quot;<a href="gsiftp://example.org:2811/data/">gsiftp://example.org:2811/data/</a> /scratch/data/&quot; </p>
<dt><code>maxtransfertries</code></p>
<dd>maxtransfertries &#8211; the maximum number of times download and upload will be attempted per job (retries are only performed if an error is judged to be temporary) </p>
<p> <i>Example:</i><br />
 maxtransfertries=&quot;10&quot; </p>
</dl>
<h2>[gridftpd] block</h2>
<p>The <code>[gridftpd]</code> block configures the gridftpd server </p>
<dl>
<dt><code>user</code></p>
<dd>user user[:group] &#8211; Switch to a non root user/group after startup </p>
<p> WARNING: Make sure that the certificate files are owned by the user/group specified by this option. Default value is root. </p>
<p> <i>Example:</i><br />
 user=&quot;grid&quot; </p>
<dt><code>debug</code></p>
<dd>debug debuglevel &#8211; Set debug level of the gridftpd daemon, between 0 (FATAL) and 5 (DEBUG). Default is 3 (INFO). </p>
<p> <i>Example:</i><br />
 debug=&quot;2&quot; </p>
<dt><code>daemon</code></p>
<dd>daemon yes|no &#8211; Whether GFS is run in daemon mode. Default is yes. </p>
<p> <i>Example:</i><br />
 daemon=&quot;yes&quot; </p>
<dt><code>logfile</code></p>
<dd>logfile path &#8211; Set logfile location </p>
<p> <i>Example:</i><br />
 logfile=&quot;/var/log/arc/gridftpd.log&quot; </p>
<dt><code>logsize</code></p>
<dd>logsize size [number] &#8211; &#8216;Size&#8217; specifies in bytes how big log file is allowed to grow (approximately). If log file exceeds specified size it is renamed into logfile.0. And logfile.0 is renamed into logfile.1, etc. up to &#8216;number&#8217; logfiles. Don&#8217;t set logsize if you don&#8217;t want to enable the ARC logrotation because another logrotation tool is used. </p>
<p> <i>Example:</i><br />
 logsize=&quot;100000 2&quot; </p>
<dt><code>pidfile</code></p>
<dd>pidfile path &#8211; Specify location of file containig PID of daemon process. This is useful for automatic star/stop scripts. </p>
<p> <i>Example:</i><br />
 pidfile=&quot;/var/run/gridftpd.pid&quot; </p>
<dt><code>port</code></p>
<dd>port bindport &#8211; Port to listen on (default 2811) </p>
<p> <i>Example:</i><br />
 port=&quot;2811&quot; </p>
<dt><code>pluginpath</code></p>
<dd>pluginpath &#8211; directory where the plugin libraries are installed, default is $ARC_LOCATION/lib(64)/arc </p>
<p> <i>Example:</i><br />
 pluginpath=&quot;/usr/lib/arc/&quot; </p>
<dt><code>encryption</code></p>
<dd>encryption yes|no &#8211; should data encryption be allowed, default is no, encryption is very heavy </p>
<p> <i>Example:</i><br />
 encryption=&quot;no&quot; </p>
<dt><code>include</code></p>
<dd>include &#8211; Include contents of another configuration file. </p>
<p> <i>Example:</i><br />
 include=&quot;path&quot; </p>
<dt><code>allowunknown</code></p>
<dd>allowunknown yes|no &#8211; if no, check user subject against grid-mapfile and reject if missing. By default unknown (not in the grid-mapfile) grid users are rejected </p>
<p> <i>Example:</i><br />
 allowunknown=&quot;no&quot; </p>
<dt><code>maxconnections</code></p>
<dd>maxconnections &#8211; maximum number of connections accepted by a gridftpd server. Default is 100. </p>
<p> <i>Example:</i><br />
 maxconnections=&quot;200&quot; </p>
<dt><code>defaultbuffer</code></p>
<dd>defaultbuffer size &#8211; defines size of every buffer for data reading/writing. Default is 65536. The actual value may decrease if the cumulative size of all buffers exceeds value specified by maxbuffer. </p>
<p> <i>Example:</i><br />
 defaultbuffer=&quot;65536&quot; </p>
<dt><code>maxbuffer</code></p>
<dd>maxbuffer size &#8211; defines maximal amount of memory in bytes to be allocated for all data reading/writing buffers. Default is 640kB. The number of buffers is (max {3, min {41, 2P + 1}}), where P is the parallelism level requested by the client. Hence, even without parallel streams enabled number of buffers will be 3. </p>
<p> <i>Example:</i><br />
 maxbuffer=&quot;655360&quot; </p>
<dt><code>globus_tcp_port_range</code></p>
<dd>globus_tcp_port_range, globus_udp_port_range &#8211; Firewall configuration </p>
<p> <i>Example:</i><br />
 globus_tcp_port_range=&quot;9000,12000&quot;<br />
 globus_udp_port_range=&quot;9000,12000&quot; </p>
<dt><code>firewall</code></p>
<dd>firewall &#8211; hostname or IP addres to use in response to PASV command instead of IP address of a network interface of computer. </p>
<p> <i>Example:</i><br />
 firewall=&quot;hostname&quot; </p>
<dt><code>x509_user_key</code></p>
<dd>x509_user_cert, x509_user_key &#8211; Server credentials location </p>
<p> <i>Example:</i><br />
 x509_user_key=&quot;/etc/grid-security/hostkey.pem&quot;<br />
 x509_user_cert=&quot;/etc/grid-security/hostcert.pem&quot; </p>
<dt><code>x509_cert_dir</code></p>
<dd>x509_cert_dir &#8211; Location of trusted CA certificates </p>
<p> <i>Example:</i><br />
 x509_cert_dir=&quot;/etc/grid-security/certificates&quot; </p>
<dt><code>gridmap</code></p>
<dd>gridmap &#8211; The gridmap file location The default is /etc/grid-security/grid-mapfile </p>
<p> <i>Example:</i><br />
 gridmap=&quot;/etc/grid-security/grid-mapfile&quot; </p>
<dt><code>unixmap</code></p>
<dd>unixmap [unixname][:unixgroup] rule &#8211; more sophisticated way to map Grid identity of client to local account. If client matches &#8216;rule&#8217; it&#8217;s assigned specified unix identity or one generated by rule. Mapping commands are processed sequentially and processing stops at first successful one (like in [group] section). For possible rules read &quot;ARC Computing Element. System Administrator guide&quot; manual. All rules defined in [group] section canbe used. There are also additional rules which produce not only yes/no result but also give back user and group names to which mapping should happen. The way it works is quite complex so it is better to read full documentation. </p>
<p> For safety reasons if sophisticated mapping is used it is better to finish mapping sequence with default mapping to nonexistent or safe account. </p>
<p> <i>Example:</i><br />
 unixmap=&quot;nobody:nogroup all&quot; </p>
<dt><code>unixgroup</code></p>
<dd>unixgroup group rule &#8211; do mapping only for users belonging to specified authorization &#8216;group&#8217;. It is similar to an additional filter for unixmap command which filters out all users not belonging to specified authorization group. Only rules which generate unix user and group names may be used in this command. Please read &quot;ARC Computing Element System Administrator Guide&quot; for more information. </p>
<p> <i>Example:</i><br />
 unixgroup=&quot;users simplepool /etc/grid-security/pool/users&quot; </p>
<dt><code>unixvo</code></p>
<dd>unixvo vo rule &#8211; do mapping only for users belonging to specified VO. Only rules which generate unix identity name may be used in this command. Please read &quot;ARC Computing Element. System Administrator Guide&quot; for more information. This command is similar to &#8216;unixgroup&#8217; described above and exists for convenience for setups which base mapping on VOs users belong to. </p>
<p> <i>Example:</i><br />
 unixvo=&quot;ATLAS unixuser atlas:atlas&quot; </p>
</dl>
<h2>[gridftpd/filedir] block</h2>
<p>[gridftpd/filedir] &quot;fileplugin&quot; storage block subblock for &quot;exporting&quot; a directory using the gridftpd&#8217;s fileplugin plugin. gridftp plugins are shared libraries. &quot;filedir&quot; is a unique label. The access control is set by using the &quot;dir&quot; configuration option </p>
<dl>
<dt><code>plugin</code></p>
<dd>plugin name &#8211; specifies name of shared library to be loaded relative to &quot;pluginpath&quot;. The next line is MUST for a gridftp file server with &quot;fileplugin&quot;, don&#8217;t change anything </p>
<p> <i>Example:</i><br />
 plugin=&quot;fileplugin.so&quot; </p>
<dt><code>groupcfg</code></p>
<dd>groupcfg group_name [group_name &#8230;] &#8211; specifies authorization groups for which this plugin is activated. In case groupcfg is not used the plugin is loaded for every mapped grid user. Multiple names were may be specified delimited by blank space. Group names are as specified in [group] sections. </p>
<p> <i>Example:</i><br />
 groupcfg=&quot;users&quot; </p>
<dt><code>path</code></p>
<dd>the name of the virtual directory served by the gridftp server, REQUIRED the exported storage area is accessible as <a href="gsiftp://my_server/topdir.">gsiftp://my_server/topdir.</a> &quot;topdir&quot; is just an example, call the virtual path anything you like, even &quot;/&quot; is a valid choice. </p>
<p> <i>Example:</i><br />
 path=&quot;/topdir&quot; </p>
<dt><code>mount</code></p>
<dd>the physical directory corresponding to the virtual one: <a href="gsiftp://my_server/topdir">gsiftp://my_server/topdir</a> will give access to the /scratch/grid directory on my_server, REQUIRED </p>
<p> <i>Example:</i><br />
 mount=&quot;/scratch/grid&quot; </p>
<dt><code>dir</code></p>
<dd>dir &#8211; this is the access control parameter, you can have several &quot;dir&quot; lines controlling different directories within then same block </p>
<p>&nbsp;<wbr>dir path options&nbsp;<wbr>&nbsp;<wbr>&#8211; specifies access rules for accessing files in&nbsp;<wbr>&#8216;path&#8217; (relative to virtual and real path) and all the files and directories below.<br />
&nbsp;<wbr>&#8216;options&#8217;&nbsp;<wbr>are:<br />
nouser&nbsp;<wbr>&nbsp;<wbr>&#8211; do not use local file system rights, only use those<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies in this line<br />
owner&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; check only file owner access rights<br />
group&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; check only group access rights<br />
other&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; check only&nbsp;<wbr>&quot;others&quot;&nbsp;<wbr>access rights<br />
&nbsp;<wbr>&nbsp;<wbr>if none of the above specified usual unix access rights are applied.<br />
read&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; allow reading files<br />
delete&nbsp;<wbr>&nbsp;<wbr>&#8211; allow deleting files<br />
append&nbsp;<wbr>&nbsp;<wbr>&#8211; allow appending files&nbsp;<wbr>(does not allow creation)<br />
overwrite &#8211; allow overwriting already existing files&nbsp;<wbr>(does not&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow creation, file attributes are not changed)<br />
dirlist &#8211; allow obtaining list of the files<br />
cd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; allow to make this directory current<br />
create owner:group permissions_or:permissions_and&nbsp;<wbr>&nbsp;<wbr>&#8211; allow creating<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>new files. File will be owned by&nbsp;<wbr>&#8216;owner&#8217;&nbsp;<wbr>and owning group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>will be&nbsp;<wbr>&#8216;group&#8217;. If&nbsp;<wbr>&#8216;*&#8217;&nbsp;<wbr>is used, the user/group to which<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connected user is mapped will be used. The permissions&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>will be set to permissions_or&nbsp;<wbr>&amp;&nbsp;<wbr>permissions_and.&nbsp;<wbr>(second<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>number is reserved for the future usage).&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
mkdir owner:group permissions_or:permissions_and&nbsp;<wbr>&nbsp;<wbr>&#8211; allow creating new directories. </p>
<p> <i>Example:</i><br />
 Set permissions on mounted directory:<br />
 dir=&quot;/ nouser read cd dirlist delete create *:* 664:664 mkdir *:* 775:775&quot; </p>
<p> <i>Example:</i><br />
 Adjust permissions on some subdirectories:<br />
 dir=&quot;/section1 nouser read mkdir *:* 700:700 cd dirlist&quot;<br />
 dir=&quot;/section2 nouser read mkdir *:* 700:700 cd dirlist&quot; </p>
</dl>
<h2>[gridftpd/jobs] subblock</h2>
<p>[gridftpd/jobs] subblock which creates the jobsubmission interface, using the jobplugin of the gridftpd service. gridftp plugins are shared libraries. &#8216;jobs&#8217; is a unique label. </p>
<dl>
<dt><code>path</code></p>
<dd>the path to the virtual gridftpd directory which is used during the job submission. MUST be set. </p>
<p> <i>Example:</i><br />
 path=&quot;/jobs&quot; </p>
<dt><code>plugin</code></p>
<dd>plugin name &#8211; specifies name of shared library to be loaded relative to &quot;pluginpath&quot;. The next line is MUST for a job submission service via gridftpd &quot;jobplugin&quot;, don&#8217;t change anything! </p>
<p> <i>Example:</i><br />
 plugin=&quot;jobplugin.so&quot; </p>
<dt><code>groupcfg</code></p>
<dd>groupcfg group_name [group_name &#8230;] &#8211; specifies authorization groups for which this plugin is activated. In case groupcfg is not used the plugin is loaded for every mapped grid user. </p>
<p> <i>Example:</i><br />
 groupcfg=&quot;users&quot; </p>
<dt><code>allownew</code></p>
<dd>The &#8216;allownew&#8217; configuration parameter sets if the grid resource accepts submission of new jobs. This parameter can be used to close down a grid. The default is yes </p>
<p> <i>Example:</i><br />
 allownew=&quot;yes&quot; </p>
<dt><code>remotegmdirs</code></p>
<dd>remotegmdirs controldir sessiondir &#8211; Specifies control and session directories to which jobs can be submitted but which are under the control of another A-REX. The corresponding controldir and sessiondir parameters must be defined in another A-REX&#8217;s configuration. Multiple remotegmdirs can be specified. </p>
<p> <i>Example:</i><br />
 remotegmdirs=&quot;/mnt/host1/control /mnt/host1/session&quot; </p>
<dt><code>maxjobdesc</code></p>
<dd>maxjobdesc size &#8211; specifies maximal allowed size of job description in bytes. Default value is 5MB. If value is missing or 0 size is not limited. </p>
<p> <i>Example:</i><br />
 maxjobdesc=&quot;5242880&quot; </p>
<dt><code>configfile</code></p>
<dd>configfile service_configuration_path &#8211; If [gridftpd] and [grid-manager] configuration parts are located in separate files this configuration option allows to link them. The service_configuration_path points to configuration file containing [grid-manager] section. Use this option only if You really know what You are doing. </p>
<p> <i>Example:</i><br />
 configfile=&quot;/etc/arc.conf&quot; </p>
</dl>
<h2>[infosys] block</h2>
<p>[infosys] block configures the hosting environment of the Information services (Local Info Tree, Index Service, Registrations, see the Information System manual) provided by the OpenLDAP slapd server. </p>
<dl>
<dt><code>infosys_compat</code></p>
<dd>infosys_compat &#8211; Setting this variable will cause ARC to use the old infoproviders. Basically, the new version uses A-REX to create LDIF while the old version uses a BDII provider-script to do it. The new version is required for GLUE2 output. </p>
<p> <i>Example:</i><br />
 infosys_compat=&quot;disable&quot; </p>
<dt><code>infoproviders_timeout </code></p>
<dd>infoproviders_timeout &#8211; this only applies to new infoproviders. it changes A-REX behaviour with respect to a single infoprovider run. Increase this value if you have many jobs in the controldir and infoproviders need more time to process. The value is in seconds. Default is 600 seconds. </p>
<p> <i>Example:</i><br />
 infoproviders_timeout = &quot;600&quot; </p>
<dt><code>debug</code></p>
<dd>debug &#8211; sets the debug level/verbosity of the startup script {0 or 1}. Default is 0. </p>
<p> <i>Example:</i><br />
 debug=&quot;1&quot; </p>
<dt><code>hostname</code></p>
<dd>hostname &#8211; the hostname of the machine running the slapd service will be the bind for slapd. If not present, will be taken from the [common] block or guessed </p>
<p> <i>Example:</i><br />
 hostname=&quot;my.testbox&quot; </p>
<dt><code>port</code></p>
<dd>port &#8211; the port where the slapd service runs. Default infosys port is 2135. </p>
<p> <i>Example:</i><br />
 port=&quot;2135&quot; </p>
<dt><code>slapd_loglevel</code></p>
<dd>slapd_loglevel &#8211; sets the native slapd loglevel (see man slapd). Slapd logs via syslog. The default is set to no-logging (0) and it is RECOMMENDED not to be changed in a production environment. Non-zero slap_loglevel value causes serious performance decrease. </p>
<p> <i>Example:</i><br />
 slapd_loglevel=&quot;0&quot; </p>
<dt><code>slapd_hostnamebind</code></p>
<dd>slapd_hostnamebind &#8211; may be used to set the hostname part of the network interface to which the slapd process will bind. Most of the cases no need to set since the hostname configuration parameter is already sufficient. The default is empty. The example below will bind the slapd process to all the network interfaces available on the server. </p>
<p> <i>Example:</i><br />
 slapd_hostnamebind=&quot;*&quot; </p>
<dt><code>threads</code></p>
<dd>threads &#8211; the native slapd threads parameter, default is 32. If you run an Index service too you should modify this value. </p>
<p> <i>Example:</i><br />
 threads=&quot;128&quot; </p>
<dt><code>timelimit</code></p>
<dd>timelimit &#8211; the native slapd timelimit parameter. Maximum number of seconds the slapd server will spend answering a search request. Default is 3600. You probably want a much lower value. </p>
<p> <i>Example:</i><br />
 timelimit=&quot;1800&quot; </p>
<dt><code>idletimeout</code></p>
<dd>idletimeout &#8211; the native slapd idletimeout parameter. Maximum number of seconds the slapd server will wait before forcibly closing idle client connections. Its value must be larger than the value of &quot;timelimit&quot; option. If not set, it defaults to timelimit + 1. </p>
<p> <i>Example:</i><br />
 idletimeout=&quot;1800&quot; </p>
<dt><code>ldap_schema_dir</code></p>
<dd>ldap_schema_dir &#8211; allows to explicitly specify a path to the schema files. Note that this doesn&#8217;t override standard location, but adds the specified path to the standard locations /etc/ldap and /etc/openldap. If you plan to relocate Glue1 and GLUE2 schemas, all these should be in the same directory that you specify here. this option does NOT apply to nordugrid.schema file. Such file has a release dependent location. Default is to use only standard locations described above. </p>
<p> <i>Example:</i><br />
 ldap_schema_dir=&quot;/nfs/ldap/schema/&quot; </p>
<dt><code>oldconfsuffix</code></p>
<dd>oldconfsuffix .suffix &#8211; sets the suffix of the backup files of the low-level slapd configuration files in case they are regenerated. Default is &quot;.oldconfig&quot;. </p>
<p> <i>Example:</i><br />
 oldconfsuffix=&quot;.oldconfig&quot; </p>
<dt><code>overwrite_config</code></p>
<dd>overwrite_config yes|no &#8211; determines if the infosys startup scripts should generate new low-level slapd configuration files. By default the low-level configuration files are regenerated with every server startup making use of the values specified in the arc.conf. </p>
<p> <i>Example:</i><br />
 overwrite_config=&quot;yes&quot; </p>
<dt><code>registrationlog</code></p>
<dd>registrationlog path &#8211; specifies the logfile for the registration processes initiated by your machine. Default is &quot;/var/log/arc/inforegistration.log&quot; </p>
<p> <i>Example:</i><br />
 registrationlog=&quot;/var/log/arc/inforegistration.log&quot; </p>
<dt><code>providerlog</code></p>
<dd>providerlog path &#8211; Specifies log file location for the information provider scripts. The feature is only available with &gt;= 0.5.26 tag. Default is &quot;/var/log/arc/infoprovider.log&quot; </p>
<p> <i>Example:</i><br />
 providerlog=&quot;/var/log/arc/infoprovider.log&quot; </p>
<dt><code>provider_loglevel</code></p>
<dd>provider_loglevel &#8211; loglevel for the infoprovider scripts (0-5). The default is 1 (critical errors are logged) </p>
<p> <i>Example:</i><br />
 provider_loglevel=&quot;2&quot; </p>
<dt><code>user</code></p>
<dd>user unix_user &#8211; the unix user running the infosys processes such as the slapd, the registrations and infoprovider scripts. By default the ldap-user is used, you can run it as root if you wish. In case of non-root value you must make sure that the A-REX directories and their content are readable by the &#8216;user&#8217; and the &#8216;user&#8217; has access to the full LRMS information including jobs submitted by other users. The A-REX directories (controldir, sessiondir runtimedir, cachedir) are specified in the [grid-manager] block </p>
<p> <i>Example:</i><br />
 user=&quot;root&quot; </p>
<dt><code>giis_location</code></p>
<dd>giis_location &#8211; If giis_location is not set, ARC_LOCATION will be used instead. </p>
<p> <i>Example:</i><br />
 giis_location=&quot;/usr/&quot; </p>
<dt><code>infosys_nordugrid</code></p>
<dd>These three variables decide which schema should be used for publishing data. They can all be enabled at the same time. Default is to enable nordugrid mds and disable glue. infosys_nordugrid &#8211; Enables NorduGrid schema </p>
<p> <i>Example:</i><br />
 infosys_nordugrid=&quot;enable&quot; </p>
<dt><code>infosys_glue12</code></p>
<dd>infosys_glue12 &#8211; Enables glue1.2/1.3 schema If infosys_glue12 is enabled, then resource_location, resource_latitude and resource_longitude need to be set in the [infosys/glue12] block. These variables do not have default values. The rest of the variables defaults are showcased below. </p>
<p> <i>Example:</i><br />
 infosys_glue12=&quot;disable&quot; </p>
<dt><code>infosys_glue2_ldap</code></p>
<dd>infosys_glue2 &#8211; Enables GLUE2 schema </p>
<p> <i>Example:</i><br />
 infosys_glue2_ldap=&quot;disable&quot; </p>
<dt><code>infosys_glue2_ldap_showactivities</code></p>
<dd>infosys_glue2_ldap_showactivities &#8211; Enables GLUE2 ComputingActivities to appear in the LDAP rendering they&#8217;re currently disabled by default. </p>
<p> <i>Example:</i><br />
 infosys_glue2_ldap_showactivities=&quot;disable&quot; </p>
<dt><code>infosys_glue2_service_qualitylevel</code></p>
<dd>infosys_glue2_service_qualitylevel &#8211; Allows a sysadmin to define a different GLUE2 QualityLevel for A-REX. This can be used for operations. default: production Allowed value is one of: &quot;production&quot;, &quot;pre-production&quot;, &quot;testing&quot;, &quot;development&quot; Refer to GLUE2 documentation for the meaning of these strings. </p>
<p> <i>Example:</i><br />
 infosys_glue2_service_qualitylevel=&quot;production&quot; </p>
<dt><code>slapd</code></p>
<dd>slapd &#8211; Configure where the slapd command is located, default is: /usr/sbin/slapd </p>
<p> <i>Example:</i><br />
 slapd=&quot;/usr/sbin/slapd&quot; </p>
<dt><code>slapadd</code></p>
<dd>slapadd &#8211; Configure where the slapadd command is located, default is: /usr/sbin/slapadd </p>
<p> <i>Example:</i><br />
 slapadd=&quot;/usr/sbin/slapadd&quot; </p>
</dl>
<h2>BDII specific</h2>
<p>Starting from 11.05, Nordugrid ARC only supports BDII5. These variables are usually automatically set by ARC, and are here mostly for debug purposes and to tweak exotic BDII5 installations. In general, a sysadmin should not set these. </p>
<dl>
<dt><code>bdii_debug_level</code></p>
<dd>bdii_debug_level &#8211; set the following to DEBUG to check bdii errors in bdii-update.log useful not to enable slapd logs reducing performance issues. </p>
<p> <i>Example:</i><br />
 bdii_debug_level=&quot;ERROR&quot; </p>
<dt><code>provider_timeout</code></p>
<dd>provider_timeout &#8211; This variable allows a system administrator to modify the behaviour of bdii-update. This is the time BDII waits for the scripts generated by A-REX infoproviders to produce their output. Default is 300 seconds. </p>
<p> <i>Example:</i><br />
 provider_timeout=300 </p>
<dt><code>infosys_debug</code></p>
<dd>infosys_debug &#8211; This variable disables/enables an ldap-database containing information about the ldap database itself on &quot;o=infosys&quot; it is very useful for debugging. Default is enabled. </p>
<p> <i>Example:</i><br />
 infosys_debug=&quot;disable&quot; </p>
</dl>
<p> BDII5 uses the following variables. These might change depending on BDII version. ARC sets them by inspecting distributed bdii configuration files. <code>DO NOT CHANGE UNLESS YOU KNOW WHAT YOU&#8217;RE DOING</code> </p>
<dl>
<dt><code>bdii_location</code></p>
<dd>bdii_location &#8211; The installation directory for the BDII. Default is /usr </p>
<p> <i>Example:</i><br />
 bdii_location=&quot;/usr&quot; </p>
<dt><code>bdii_var_dir</code></p>
<dd>bdii_var_dir &#8211; Contains BDII pid files and slapd pid files </p>
<p> <i>Example:</i><br />
 bdii_var_dir=&quot;/var/run/arc/bdii&quot; </p>
<dt><code>bdii_log_dir</code></p>
<dd>bdii_log_dir &#8211; Contains infosys logs </p>
<p> <i>Example:</i><br />
 bdii_log_dir=&quot;/var/log/arc/bdii&quot; </p>
<dt><code>bdii_tmp_dir</code></p>
<dd>bdii_tmp_dir &#8211; Contains provider scripts </p>
<p> <i>Example:</i><br />
 bdii_tmp_dir=&quot;/var/tmp/arc/bdii&quot; </p>
<dt><code>bdii_lib_dir</code></p>
<dd>bdii_lib_dir &#8211; Contains slapd databases </p>
<p> <i>Example:</i><br />
 bdii_lib_dir=&quot;/var/lib/arc/bdii&quot; </p>
<dt><code>bdii_update_pid_file</code></p>
<dd>bdii_update_pid_file, slapd_pid_file &#8211; Allows to change bdii-update and slapd pidfiles filename and location </p>
<p> <i>Example:</i><br />
 bdii_update_pid_file=&quot;/var/run/arc/bdii-update.pid&quot;<br />
 slapd_pid_file=&quot;$bdii_var_dir/db/slapd.pid&quot; </p>
<dt><code>bdii_database</code></p>
<dd>bdii_database &#8211; Configure what ldap database backend should be used, default is: bdb </p>
<p> <i>Example:</i><br />
 bdii_database=&quot;bdb&quot; </p>
</dl>
<p> The following options are for tweaking only. Usually one should not configure them. They change the BDII configuration file generated by ARC. Please consult BDII manual for details. </p>
<dl>
<dt><code>bdii_conf</code></p>
<dd>bdii_conf &#8211; Location of the bdii configuration file. ARC modifies the original and sets it as default /var/run/arc/infosys/bdii.conf </p>
<p> <i>Example:</i><br />
 bdii_conf=&quot;/var/run/arc/infosys/bdii.conf&quot; </p>
</dl>
<p> Command line options used to run bdii-update. ARC finds it looking into bdii configuration. default: ${bdii_location}/sbin/bdii-update </p>
<p> <code>bdii_update_cmd</code><br />
 <code>bdii_archive_size</code><br />
 <code>bdii_db_config</code><br />
 <code>bdii_breathe_time</code><br />
 <code>bdii_delete_delay</code><br />
 <code>bdii_read_timeout</code><br />
 <code>bdii_run_dir</code><br />
 <code>bindmethod</code><br />
 <code>cachettl</code><br />
 <code>db_archive</code><br />
 <code>db_checkpoint</code></p>
<h2>EGIIS-related commands</h2>
<dl>
<dt><code>giis_fifo</code></p>
<dd>giis_fifo &#8211; path to fifo used by EGIIS. default is /var/run/arc/giis-fifo This file is automatically created by ARC, the option is only for tweaking. </p>
<p> <i>Example:</i><br />
 giis_fifo=/var/run/arc/giis-fifo </p>
</dl>
<p> LDAP parameters of the cluster.pl (old) infoprovider, use the defaults, do NOT change them unless you know what you are doing </p>
<dl>
<dt><code>cachetime</code></p>
<dd>cachetime affects old infoproviders, and forces the validity time of the record. </p>
<p> <i>Example:</i><br />
 cachetime=&quot;30&quot; </p>
<dt><code>sizelimit</code></p>
<dd>sizelimit affects registration to egiis </p>
<p> <i>Example:</i><br />
 sizelimit=&quot;10&quot; </p>
<dt><code>slapd_cron_checkpoint</code></p>
<dd>slapd_cron_checkpoint &#8211; LDAP checkpoint enable/disable This option was introduced to solve bug #2032, to reduce the number of log files produced by BDII. It is usually not needed, but if BDII produces large logs and huge number of files, should help solving the issues related to that. </p>
<p> <i>Example:</i><br />
 slapd_cron_checkpoint=&quot;enable&quot; </p>
</dl>
<h2>[infosys/glue12] block</h2>
<p>This block holds information that is needed by the glue 1.2 generation. This is only necessary if infosys_glue12 is enabled. </p>
<dl>
<dt><code>resource_location</code></p>
<dd>These variables need to be set if infosys_glue12 is enabled. IMPORTANT: no slashes or backslashes here! Example: &quot;Kastrup, Denmark&quot; </p>
<p> <i>Example:</i><br />
 resource_location=&quot;&quot; </p>
<dt><code>resource_latitude</code></p>
<dd>Example: &quot;55.75000&quot; </p>
<p> <i>Example:</i><br />
 resource_latitude=&quot;&quot; </p>
<dt><code>resource_longitude</code></p>
<dd>Example: &quot;12.41670&quot; </p>
<p> <i>Example:</i><br />
 resource_longitude=&quot;&quot; </p>
<dt><code>cpu_scaling_reference_si00</code></p>
<dd>Example 2400 </p>
<p> <i>Example:</i><br />
 cpu_scaling_reference_si00=&quot;&quot; </p>
<dt><code>processor_other_description</code></p>
<dd>Example Cores=3,Benchmark=9.8-HEP-SPEC06 </p>
<p> <i>Example:</i><br />
 processor_other_description=&quot;&quot; </p>
<dt><code>glue_site_web</code></p>
<dd>Example <a rel="nofollow" href="http://www.ndgf.org">http://www.ndgf.org</a> </p>
<p> <i>Example:</i><br />
 glue_site_web=&quot;&quot; </p>
<dt><code>glue_site_unique_id</code></p>
<dd>Example NDGF-T1 </p>
<p> <i>Example:</i><br />
 glue_site_unique_id=&quot;&quot; </p>
<dt><code>provide_glue_site_info</code></p>
<dd>This variable decides if the GlueSite should be published. In case you want to set up a more complicated setup with several publishers of data to a GlueSite, then you may wish to tweak this parameter. </p>
<p> <i>Example:</i><br />
 provide_glue_site_info=&quot;true&quot; </p>
</dl>
<h2>[infosys/site/sitename] block</h2>
<p>[infosys/site/sitename] Site BDII configuration block, this block is used to configure ARC to generate a site-bdii that can be registered in GOCDB etc to make it a part of a gLite network. The sitename part is to be declarative of the site-bdii being generated. </p>
<dl>
<dt><code>unique_id</code></p>
<dd>The unique id used to identify this site, eg &quot;NDGF-T1&quot; </p>
<p> <i>Example:</i><br />
 unique_id=&quot;&quot; </p>
<dt><code>url</code></p>
<dd>The URL is of the format: <a href="ldap://host.domain:2170/mds-vo-name=something,o=grid">ldap://host.domain:2170/mds-vo-name=something,o=grid</a> and should point to the resource-bdii </p>
<p> <i>Example:</i><br />
 url=&quot;&quot; </p>
</dl>
<h2>[infosys/admindomain] block</h2>
<p>[infosys/admindomain] GLUE2 AdminDomain configuration block, to configure administrative items of the cluster. This values do not affect neither glue12 or nordugrid renderings. If the whole block is not specified, will default to an AdminDomain called UNDEFINEDVALUE. </p>
<dl>
<dt><code>name</code></p>
<dd>name &#8211; the Name attribute for the domain. This will show in top-BDII to group the resources belonging to this cluster. to group a bunch of clusters under the same AdminDomain, just use the same name. If not specified, will default to UNDEFINEDVALUE. </p>
<p> <i>Example:</i><br />
 name=&quot;ARC-TESTDOMAIN&quot; </p>
<dt><code>description</code></p>
<dd>description &#8211; description of this domain. Not mandatory. </p>
<p> <i>Example:</i><br />
 description=&quot;ARC test Domain&quot; </p>
<dt><code>www</code></p>
<dd>www &#8211; URL pointing at a site holding information about the AdminDomain. Not mandatory. </p>
<p> <i>Example:</i><br />
 www=&quot;<a rel="nofollow" href="http://www.nordugrid.org/">http://www.nordugrid.org/</a>&quot; </p>
<dt><code>distributed</code></p>
<dd>distributed &#8211; set this to yes if the domain is distributed that means, if the resources belonging to the domain are considered geographically distributed. </p>
<p> <i>Example:</i><br />
 distributed=yes </p>
<dt><code>owner</code></p>
<dd>owner &#8211; contact email of a responsible subject for the domain </p>
<p> <i>Example:</i><br />
 owner=admin [at] nordugrid.org </p>
<dt><code>otherinfo</code></p>
<dd>otherinfo &#8211; fills the OtherInfo GLUE2 field. no need to set, used only for future development. </p>
<p> <i>Example:</i><br />
 otherinfo=Test Other info </p>
</dl>
<h2>[infosys/index/indexname] block</h2>
<p>[infosys/index/indexname] Index Service block configures and enables an Information Index Service. A separate Index block is required for every Index Service you may run on the given machine. The &#8216;indexname&#8217; constitutes to the </p>
<dl>
<dt><code>name</code></p>
<dd>name &#8211; The unique (within the hosting machine) name of the Index Service. Its value becomes part of the LDAP suffix of the Index Service: (mds-vo-name=value of the name attribute, o=grid) </p>
<p> <i>Example:</i><br />
 name=&quot;indexname&quot; </p>
<dt><code>allowreg</code></p>
<dd>allowregistration &#8211; Implements registration filtering within an Index Sevice Sets the Local Information Trees or lower level Index Services allowed to register to the Index Service. List each allowed registrants with the allowreg attribute. </p>
<p> WARNING: specifying allowreg implies setting up a strict filtering, only the matching registrants will be able to register to the Index. The wildcard * can be used in allowreg. Several allowreg lines can be used. Some examples:<br />
&nbsp;<wbr>-All the Swedish machines can register regardless they are resources or Indices allowreg=&quot;*.se:2135&quot;<br />
&nbsp;<wbr>-Cluster resources from Denmark can register allowreg=&quot;*.dk:2135/nordugrid-cluster-name=*, Mds-Vo-name=local, o=grid&quot;<br />
&nbsp;<wbr>-Storage resources from HIP, Finland can register allowreg=&quot;*hip.fi:2135/nordugrid-se-name=*, Mds-Vo-name=local, o=grid&quot;<br />
&nbsp;<wbr>-The index1.sweden.se can register as a Sweden Index&nbsp;<wbr>&nbsp;<wbr>(and only as a Sweden Index) allowreg=&quot;index1.sweden.se:2135/Mds-vo-Name=Sweden,o=Grid&quot;<br />
&nbsp;<wbr>-Any Index Service can register allowreg=&quot;*:2135/Mds-vo-Name=*,o=Grid&quot; </p>
<p> <i>Example:</i><br />
 allowreg=&quot;trusted.host.org.se:2135/Mds-vo-Name=Trusted-Index,o=Grid&quot; </p>
</dl>
<h2>[infosys/index/indexname/registration/registrationname] block</h2>
<p>[infosys/index/indexname/registration/registrationname] Index service registration block This block enables a registration process initiated by the to a target Index Service. NorduGrid maintains a webpage with information on major Index Services: <a rel="nofollow" href="http://www.nordugrid.org/NorduGridMDS/index_service.html">http://www.nordugrid.org/NorduGridMDS/index_service.html</a> </p>
<dl>
<dt><code>targethostname</code></p>
<dd>targethostname &#8211; the hostname of the machine running the registration target Index Service </p>
<p> <i>Example:</i><br />
 targethostname=&quot;index.myinstitute.org&quot; </p>
<dt><code>targetport</code></p>
<dd>targetport &#8211; the port on which the target Index Service is running. The default is the 2135 Infosys port. </p>
<p> <i>Example:</i><br />
 targetport=&quot;2135&quot; </p>
<dt><code>targetsuffix</code></p>
<dd>targetsuffix &#8211; the LDAP suffix of the target Index Service </p>
<p> <i>Example:</i><br />
 targetsuffix=&quot;mds-vo-name=BigIndex,o=grid&quot; </p>
<dt><code>regperiod</code></p>
<dd>regperiod &#8211; The registration period in seconds, the registration messages are continously sent according to the regperiod. Default is 120 sec. </p>
<p> <i>Example:</i><br />
 regperiod=&quot;300&quot; </p>
<dt><code>registranthostname</code></p>
<dd>registranthostname &#8211; the hostname of the machine sending the registrations. This attribute inherits its value from the [common] and [infosys] blocks, most cases no need to set. </p>
<p> <i>Example:</i><br />
 registranthostname=&quot;myhost.org&quot; </p>
<dt><code>registrantport</code></p>
<dd>registrantport &#8211; the port of the slapd service hosting the registrant Index Service. The attribute inherits its value from the [infosys] block (and therefore defaults to 2135) </p>
<p> <i>Example:</i><br />
 registrantport=&quot;2135&quot; </p>
<dt><code>registrantsuffix</code></p>
<dd>registrantsuffix &#8211; the LDAP suffix of the registrant Index Service. It is automatically determined from the registration block name, therefore most of the cases no need to specify. In this case the default registrantsuffix will be:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;Mds-Vo-name=indexname&quot; </p>
<p> please mind uppercase/lowercase characters in the above string when defining allowreg in an index! Don&#8217;t set it unless you want to overwrite the default. </p>
<p> <i>Example:</i><br />
 registrantsuffix=&quot;mds-vo-name=indexname,o=grid&quot; </p>
</dl>
<h2>[cluster] block</h2>
<p>This block configures how your cluster is seen on the grid monitor (infosys point of view). Please consult the Infosys manual for detailed information on cluster attributes. If you want your cluster (configured below) to appear in the infosys (on the monitor) you also need to create a cluster registration block (see the next block). </p>
<dl>
<dt><code>hostname</code></p>
<dd>hostname &#8211; the FQDN of the frontend node, if the hostname is not set already in the common block then it MUST be set here </p>
<p> <i>Example:</i><br />
 hostname=&quot;myhost.org&quot; </p>
<dt><code>interactive_contactstring</code></p>
<dd>interactive_contactstring &#8211; the contact string for interactive logins, set this if the cluster supports some sort of grid-enabled interactive login (gsi-ssh), multivalued </p>
<p> <i>Example:</i><br />
 interactive_contactstring=&quot;<a href="gsissh://frontend.cluster:2200">gsissh://frontend.cluster:2200</a>&quot; </p>
<dt><code>cluster_alias</code></p>
<dd>alias &#8211; an arbitrary alias name of the cluster, optional </p>
<p> <i>Example:</i><br />
 cluster_alias=&quot;Big Blue Cluster in Nowhere&quot; </p>
<dt><code>comment</code></p>
<dd>comment &#8211; a free text field for additional comments on the cluster in a single line, no newline character is allowed! </p>
<p> <i>Example:</i><br />
 comment=&quot;This cluster is specially designed for XYZ applications: <a rel="nofollow" href="http://www.xyz.org">www.xyz.org</a>&quot; </p>
<dt><code>cluster_location</code></p>
<dd>cluster_location &#8211; The geographical location of the cluster, preferably specified as a postal code with a two letter country prefix </p>
<p> <i>Example:</i><br />
 cluster_location=&quot;DK-2100&quot; </p>
<dt><code>cluster_owner</code></p>
<dd>cluster_owner &#8211; it can be used to indicate the owner of a resource, multiple entries can be used </p>
<p> <i>Example:</i><br />
 cluster_owner=&quot;World Grid Project&quot;<br />
 cluster_owner=&quot;University of NeverLand&quot; </p>
<dt><code>authorizedvo</code></p>
<dd>authorizedvo &#8211; this attribute is used to advertise which VOs are authorized on the cluster. Multiple entries are allowed. This entries will be shown in GLUE2 AccessPolicy and MappingPolicy objects. </p>
<p> <i>Example:</i><br />
 authorizedvo=&quot;developer.nordugrid.org&quot;<br />
 authorizedvo=&quot;community.nordugrid.org&quot; </p>
<dt><code>clustersupport</code></p>
<dd>clustersupport &#8211; this is the support email address of the resource, multiple entries can be used </p>
<p> <i>Example:</i><br />
 clustersupport=&quot;grid.support [at] mysite.org&quot;<br />
 clustersupport=&quot;grid.support [at] myproject.org&quot; </p>
<dt><code>lrmsconfig</code></p>
<dd>lrmsconfig &#8211; an optional free text field to describe the configuration of your Local Resource Management System (batch system). </p>
<p> <i>Example:</i><br />
 lrmsconfig=&quot;single job per processor&quot; </p>
<dt><code>homogeneity</code></p>
<dd>homogeneity &#8211; determines whether the cluster consists of identical NODES with respect to cputype, memory, installed software (opsys). The frontend is NOT needed to be homogeneous with the nodes. In case of inhomogeneous nodes, try to arrange the nodes into homogeneous groups assigned to a queue and use queue-level attributes. Possible values: True,False, the default is True. False will trigger multiple GLUE2 ExecutionEnvironments to be published if applicable. </p>
<p> <i>Example:</i><br />
 homogeneity=&quot;True&quot; </p>
<dt><code>architecture</code></p>
<dd>architecture &#8211; sets the hardware architecture of the NODES. The &quot;architecture&quot; is defined as the output of the &quot;uname -m&quot; (e.g. i686). Use this cluster attribute if only the NODES are homogeneous with respect to the architecture. Otherwise the queue-level attribute may be used for inhomogeneous nodes. If the frontend&#8217;s architecture agrees to the nodes, the &quot;adotf&quot; (Automatically Determine On The Frontend) can be used to request automatic determination. </p>
<p> <i>Example:</i><br />
 architecture=&quot;adotf&quot; </p>
<dt><code>opsys</code></p>
<dd>opsys &#8211; this multivalued attribute is meant to describe the operating system of the computing NODES. Set it to the opsys distribution of the NODES and not the frontend! opsys can also be used to describe the kernel or libc version in case those differ from the originally shipped ones. The distribution name should be given as distroname-version.number, where spaces are not allowed. Kernel version should come in the form kernelname-version.number. If the NODES are inhomogeneous with respect to this attribute do NOT set it on cluster level, arrange your nodes into homogeneous groups assigned to a queue and use queue-level attributes. </p>
<p> <i>Example:</i><br />
 opsys=&quot;Linux-2.6.18&quot;<br />
 opsys=&quot;glibc-2.5.58&quot;<br />
 opsys=&quot;CentOS-5.6&quot; </p>
<dt><code>nodecpu</code></p>
<dd>nodecpu &#8211; this is the cputype of the homogeneous nodes. The string is constructed from the /proc/cpuinfo as the value of &quot;model name&quot; and &quot;@&quot; and value of &quot;cpu MHz&quot;. Do NOT set this attribute on cluster level if the NODES are inhomogeneous with respect to cputype, instead arrange the nodes into homogeneous groups assigned to a queue and use queue-level attributes. Setting the nodecpu=&quot;adotf&quot; will result in Automatic Determination On The Frontend, which should only be used if the frontend has the same cputype as the homogeneous nodes. </p>
<p> <i>Example:</i><br />
 nodecpu=&quot;AMD Duron(tm) Processor @ 700 MHz&quot; </p>
<dt><code>nodememory</code></p>
<dd>nodememory &#8211; this is the amount of memory (specified in MB) on the node which can be guaranteed to be available for the application. Please note in most cases it is less than the physical memory installed in the nodes. Do NOT set this attribute on cluster level if the NODES are inhomogeneous with respect to their memories, instead arrange the nodes into homogeneous groups assigned to a queue and use queue-level attributes. </p>
<p> <i>Example:</i><br />
 nodememory=&quot;512&quot; </p>
<dt><code>defaultmemory</code></p>
<dd>defaultmemory &#8211; If a user submits a job without specifying how much memory should be used, this value will be taken first. The order is: xrsl -&gt; defaultmemory -&gt; nodememory -&gt; 1GB. This is the amount of memory (specified in MB) that a job will request(per rank). </p>
<p> <i>Example:</i><br />
 defaultmemory=&quot;512&quot; </p>
<dt><code>benchmark</code></p>
<dd>benchmark name value &#8211; this optional multivalued attribute can be used to specify benchmark results on the cluster level. Use this cluster attribute if only the NODES are homogeneous with respect to the benchmark performance. Otherwise the similar queue-level attribute should be used. Please try to use one of standard benchmark names given below if possible. </p>
<p> <i>Example:</i><br />
 benchmark=&quot;SPECINT2000 222&quot;<br />
 benchmark=&quot;SPECFP2000 333&quot; </p>
<dt><code>middleware</code></p>
<dd>middleware &#8211; the multivalued attribute shows the installed grid software on the cluster, nordugrid and globus-ng is automatically set, no need to specify middleware=nordugrid or middleware=globus </p>
<p> <i>Example:</i><br />
 middleware=&quot;my grid software&quot; </p>
<dt><code>nodeaccess</code></p>
<dd>nodeaccess &#8211; determines how the nodes can connect to the internet. Not setting anything means the nodes are sitting on a private isolated network. &quot;outbound&quot; access means the nodes can connect to the outside world while &quot;inbound&quot; access means the nodes can be connected from outside. inbound &amp; outbound access together means the nodes are sitting on a fully open network. </p>
<p> <i>Example:</i><br />
 nodeaccess=&quot;inbound&quot;<br />
 nodeaccess=&quot;outbound&quot; </p>
<dt><code>dedicated_node_string</code></p>
<dd>dedicated_node_string &#8211; the string which is used in the PBS node configuration to distinguish the grid nodes from the rest. Suppose only a subset of nodes are available for grid jobs, and these nodes have a common &quot;node property&quot; string, this case the dedicated_node_string should be set to this value and only the nodes with the corresponding &quot;pbs node property&quot; are counted as grid enabled nodes. Setting the dedicated_node_string to the value of the &quot;pbs node property&quot; of the grid-enabled nodes will influence how the totalcpus, user freecpus is calculated. You don&#8217;t need to set this attribute if your cluster is fully available for the grid and your cluster&#8217;s PBS configuration does not use the &quot;node property&quot; method to assign certain nodes to grid queues. You shouldn&#8217;t use this configuration option unless you make sure your PBS configuration makes use of the above described setup. </p>
<p> <i>Example:</i><br />
 dedicated_node_string=&quot;gridnode&quot; </p>
<dt><code>localse</code></p>
<dd>localse &#8211; this multivalued parameter tells the BROKER that certain URLs (and locations below that) should be considered &quot;locally&quot; available to the cluster. </p>
<p> <i>Example:</i><br />
 localse=&quot;<a href="gsiftp://my.storage/data1/">gsiftp://my.storage/data1/</a>&quot;<br />
 localse=&quot;<a href="gsiftp://my.storage/data2/">gsiftp://my.storage/data2/</a>&quot; </p>
<dt><code>gm_mount_point</code></p>
<dd>gm_mount_point &#8211; this is the same as the &quot;path&quot; from the [gridftpd/jobs] block. The default is &quot;/jobs&quot;. Will be cleaned up later, do NOT touch it. </p>
<p> <i>Example:</i><br />
 gm_mount_point=&quot;/jobs&quot; </p>
<dt><code>gm_port</code></p>
<dd>gm_port &#8211; this is the same as the &quot;port&quot; from the [gridftpd] block. The default is &quot;2811&quot;. Will be cleaned up later. </p>
<p> <i>Example:</i><br />
 gm_port=&quot;2811&quot; </p>
<dt><code>cpudistribution</code></p>
<dd>cpudistribution &#8211; this is the CPU distribution over nodes given in the form: ncpu:m where<br />
&nbsp;<wbr>&nbsp;<wbr>n is the number of CPUs per machine<br />
&nbsp;<wbr>&nbsp;<wbr>m is the number of such computers </p>
<p> Example: 1cpu:3,2cpu:4,4cpu:1 represents a cluster with 3 single CPU machines, 4 dual CPU machines, one machine with 4 CPUs. This command is needed to tweak and overwrite the values returned by the underlying LRMS. In general there is no need to configure it. </p>
<p> <i>Example:</i><br />
 cpudistribution=1cpu:3,2cpu:4,4cpu:1 </p>
</dl>
<h2>[infosys/cluster/registration/registrationname] block</h2>
<p>Computing resource (cluster) registration block configures and enables the registration process of a computing resource to an Index Service. A cluster can register to several Index Services this case each registration process should have its own block. NorduGrid maintains a webpage with information on major Index Services: <a rel="nofollow" href="http://www.nordugrid.org/NorduGridMDS/index_service.html">http://www.nordugrid.org/NorduGridMDS/index_service.html</a> </p>
<dl>
<dt><code>targethostname</code></p>
<dd>targethostname &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 targethostname=&quot;index.myinstitute.org&quot; </p>
<dt><code>targetport</code></p>
<dd>targetport &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 targetport=&quot;2135&quot; </p>
<dt><code>targetsuffix</code></p>
<dd>targetsuffix &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 targetsuffix=&quot;mds-vo-name=BigIndex,o=grid&quot; </p>
<dt><code>regperiod</code></p>
<dd>regperiod &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 regperiod=&quot;300&quot; </p>
<dt><code>registranthostname</code></p>
<dd>registranthostname &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 registranthostname=&quot;myhost.org&quot; </p>
<dt><code>registrantport</code></p>
<dd>registrantport &#8211; see description earlier </p>
<p> <i>Example:</i><br />
 registrantport=&quot;2135&quot; </p>
<dt><code>registrantsuffix</code></p>
<dd>registrantsuffix &#8211; the LDAP suffix of the registrant cluster resource It is automatically determined from the [infosys] block and the registration blockname. In this case the default registrantsuffix will be:<br />
&quot;nordugrid-cluster-name=hostname,Mds-Vo-name=local,o=Grid&quot; </p>
<p> please mind uppercase/lowercase characters above if defining allowreg in an index! Don&#8217;t set it unless you want to overwrite the default. </p>
<p> <i>Example:</i><br />
 registrantsuffix=&quot;nordugrid-cluster-name=myhost.org,Mds-Vo-name=local,o=grid&quot; </p>
</dl>
<h2>[queue/queue_name] block</h2>
<p>Each grid-enabled queue should have a separate queue block. The queuename should be used as a label in the block name. A queue can represent a PBS/LSF/SGE/SLURM/LL queue, a SGE pool, a Condor pool or a single machine in case &#8216;fork&#8217; type of LRMS is specified in the [common] block. </p>
<p> Queues don&#8217;t need to be registered (there is no queue registration block), once you configured your cluster to register to an Index Service the queue entries (configured with this block) automatically will be there. Please consult the ARC Information System manual for detailed information on queue attributes:<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.nordugrid.org/documents/arc_infosys.pdf">http://www.nordugrid.org/documents/arc_infosys.pdf</a><br />
&nbsp;<wbr>&nbsp;<wbr> use the queue_name for labeling the block. The special name &#8216;fork&#8217; should be used for labeling the queue block in case you specified &#8216;fork&#8217; type of LRMS in the [common] block. </p>
<dl>
<dt><code>name</code></p>
<dd>name sets the name of the grid-enabled queue. It MUST match the queue_name label of the corresponding queue block, see above. Use &quot;fork&quot; if you specified &#8216;fork&#8217; type of LRMS in the [common] block. Queue name MUST be specified, even if the queue block is already correctly labeled. </p>
<p> <i>Example:</i><br />
 name=&quot;gridlong&quot; </p>
<dt><code>homogeneity</code></p>
<dd>homogeneity &#8211; determines whether the queue consists of identical NODES with respect to cputype, memory, installed software (opsys). In case of inhomogeneous nodes, try to arrange the nodes into homogeneous groups and assigned them to a queue. Possible values: True,False, the default is True. </p>
<p> <i>Example:</i><br />
 homogeneity=&quot;True&quot; </p>
<dt><code>scheduling_policy</code></p>
<dd>scheduling_policy &#8211; this optional parameter tells the schedulling policy of the queue, PBS by default offers the FIFO scheduller, many sites run the MAUI. At the moment FIFO &amp; MAUI is supported. If you have a MAUI scheduller you should specify the &quot;MAUI&quot; value since it modifies the way the queue resources are calculated. BY default the &quot;FIFO&quot; sceduller is assumed. </p>
<p> <i>Example:</i><br />
 scheduling_policy=&quot;FIFO&quot; </p>
<dt><code>comment</code></p>
<dd>comment &#8211; a free text field for additional comments on the queue in a single line, no newline character is allowed! </p>
<p> <i>Example:</i><br />
 comment=&quot;This queue is nothing more than a condor pool&quot; </p>
<dt><code>maui_bin_path</code></p>
<dd>maui_bin_path &#8211; set this parameter for the path of the maui commands like showbf in case you specified the &quot;MAUI&quot; scheduling_policy above. This parameter can be set in the [common] block as well. </p>
<p> <i>Example:</i><br />
 maui_bin_path=&quot;/usr/local/bin&quot; </p>
<dt><code>queue_node_string</code></p>
<dd>queue_node_string &#8211; In PBS you can assign nodes to a queue (or a queue to nodes) by using the &quot;node property&quot; PBS node configuration method and asssigning the marked nodes to the queue (setting the resources_default.neednodes = queue_node_string for that queue). This parameter should contain the &quot;node property&quot; string of the queue-assigned nodes. Setting the queue_node_string changes how the queue-totalcpus, user freecpus are determined for this queue. Essentially, queue_node_string value is used to construct nodes= string in PBS script, such as nodes=count:queue_node_string where count is taken from the job description (1 if not specified). You shouldn&#8217;t use this option unless you are sure that your PBS configuration makes use of the above configuration. Read NorduGrid PBS instructions for more information:<br />
<a rel="nofollow" href="http://www.nordugrid.org/documents/pbs-config.html">http://www.nordugrid.org/documents/pbs-config.html</a> </p>
<p> <i>Example:</i><br />
 queue_node_string=&quot;gridlong_nodes&quot;<br />
 queue_node_string=&quot;ppn=4:ib&quot; </p>
<dt><code>sge_jobopts</code></p>
<dd>sge_jobopts &#8211; additional SGE options to be used when submitting jobs to SGE from this queue. If in doubt, leave it commented out </p>
<p> <i>Example:</i><br />
 sge_jobopts=&quot;-P atlas -r yes&quot; </p>
<dt><code>condor_requirements</code></p>
<dd>condor_requirements &#8211; only needed if using Condor. It needs to be defined for each queue. Use this option to determine which nodes belong to the current queue. The value of &#8216;condor_requirements&#8217; must be a valid constraints string which is recognized by a condor_status -constraint &#8216;&#8230;.&#8217; command. It can reference pre-defined ClassAd attributes (like Memory, Opsys, Arch, HasJava, etc) but also custom ClassAd attributes. To define a custom attribute on a condor node, just add two lines like the ones below in the `hostname`.local config file on the node:<br />
&nbsp;<wbr>&nbsp;<wbr>NORDUGRID_RESOURCE=TRUE<br />
&nbsp;<wbr>&nbsp;<wbr>STARTD_EXPRS&nbsp;<wbr>=&nbsp;<wbr>NORDUGRID_RESOURCE,&nbsp;<wbr>$(STARTD_EXPRS) </p>
<p> A job submitted to this queue is allowed to run on any node which satisfies the &#8216;condor_requirements&#8217; constraint. If &#8216;condor_requirements&#8217; is not set, jobs will be allowed to run on any of the nodes in the pool. When configuring multiple queues, you can differentiate them based on memory size or disk space, for example: </p>
<p> <i>Example:</i><br />
 condor_requirements=&quot;(OpSys == &quot;linux&quot; &amp;&amp; NORDUGRID_RESOURCE &amp;&amp; Memory &gt;= 1000 &amp;&amp; Memory &lt; 2000)&quot; </p>
<dt><code>lsf_architecture</code></p>
<dd>CPU architecture to request when submitting jobs to LSF. Use only if you know what you are doing. </p>
<p> <i>Example:</i><br />
 lsf_architecture=&quot;PowerPC&quot; </p>
<dt><code>totalcpus</code></p>
<dd>totalcpus &#8211; manually sets the number of cpus assigned to the queue. No need to specify the parameter in case the queue_node_string method was used to assign nodes to the queue (this case it is dynamically calculated and the static value is overwritten) or when the queue have access to the entire cluster (this case the cluster level totalcpus is the relevant parameter). Use this static parameter only if some special method is applied to assign a subset of totalcpus to the queue. </p>
<p> <i>Example:</i><br />
 totalcpus=&quot;32&quot; </p>
<dt><code>nodecpu</code></p>
<dd>queue-level configuration parameters: nodecpu, nodememory, architecture, opsys and benchmark should be set if they are homogeneous over the nodes assigned to the queue AND they are different from the cluster-level value. Their meanings are described in the cluster block. Usage: this queue collects nodes with &quot;nodememory=512&quot; while another queue has nodes with &quot;nodememory=256&quot; -&gt; don&#8217;t set the cluster attributes but use the queue-level attributes. When the frontend&#8217;s architecture or cputype agrees with the queue nodes, the &quot;adotf&quot; (Automatically Determine On The Frontend) can be used to request automatic determination of architecture or nodecpu. </p>
<p> <i>Example:</i><br />
 nodecpu=&quot;adotf&quot;<br />
 nodememory=&quot;512&quot;<br />
 architecture=&quot;adotf&quot;<br />
 opsys=&quot;Fedora 16&quot;<br />
 opsys=&quot;Linux-3.0&quot;<br />
 benchmark=&quot;SPECINT2000 222&quot;<br />
 benchmark=&quot;SPECFP2000 333&quot; </p>
<dt><code>ac_policy</code></p>
<dd>queue access policy rules based on VOMS attributes in user&#8217;s proxy certificate (requires the arc-vomsac-check plugin to be enabled). Matching rules have the following format:<br />
&nbsp;<wbr>&nbsp;<wbr>ac_policy=&quot;[+/-]VOMS:&nbsp;<wbr>&lt;FQAN&gt;&quot; </p>
<p> Please read arc-vomsac-check manual page for more information. </p>
<p> <i>Example:</i><br />
 ac_policy=&quot;-VOMS: /badvo&quot;<br />
 ac_policy=&quot;VOMS: /.*/Role=production&quot; </p>
<dt><code>authorizedvo</code></p>
<dd>authorizedvo &#8211; this attribute is used to advertise which VOs are authorized on the specific queue. Multiple entries are allowed. This entries will be shown in the MappingPolicy objects. If something is already defined in the [cluster] block, the shown VOs will be the union set of those defined in [cluster] with those specific to this [queue] block. </p>
<p> <i>Example:</i><br />
 authorizedvo=&quot;LocalUsers&quot;<br />
 authorizedvo=&quot;atlas&quot;<br />
 authorizedvo=&quot;community.nordugrid.org&quot; </p>
<dt><code>cachetime</code></p>
<dd>this affects old infoproviders, and forces the validity time of the record. </p>
<p> <i>Example:</i><br />
 cachetime=&quot;30&quot; </p>
<dt><code>sizelimit</code></p>
<dd>sizelimit affects registration to EGIIS </p>
<p> <i>Example:</i><br />
 sizelimit=&quot;5000&quot; </p>
</dl>
<h2>[registration/emir] block</h2>
<p>Services registration into EMIR block configures and enables the registration process of a services enabled in this configuration file into EMI indexing service (EMIR). </p>
<dl>
<dt><code>emirurls</code></p>
<dd>List of URL separated by comma of EMIR services which are to accept registration. This is mandatory. </p>
<p> <i>Example:</i><br />
 emirurls=&quot;<a rel="nofollow" href="https://somehost:60002/emir">https://somehost:60002/emir</a>&quot; </p>
<dt><code>validity</code></p>
<dd>Time in seconds for which registration records should stay valid. </p>
<p> <i>Example:</i><br />
 validity=600 </p>
<dt><code>period</code></p>
<dd>Time in seconds how othen registration record should be sent to the registration service. </p>
<p> <i>Example:</i><br />
 period=60 </p>
<dt><code>disablereg_xbes</code></p>
<dd>disablereg_xbes may be used to selectively disable registration of A-REX service. Possible values are yes and no. Default is no, </p>
<p> <i>Example:</i><br />
 disablereg_xbes=&quot;no&quot; </p>
</dl>
<h2>[nordugridmap] block</h2>
<p>[nordugridmap] block configuration is used to fine-tune behaviour of the nordugridmap &#8211; an ARC tool used to generate grid-mapfiles. Please refer to [vo] block description to find information how to specify VO sources for mapfile generation. This section setup general VO-independent parameters. </p>
<dl>
<dt><code>x509_user_key</code></p>
<dd>x509_user_cert, x509_user_key &#8211; public certificate and privat key to be used when fetching sources over TLS (https:// and vomss:// sources retrieval rely on this parameter) If not specified, values defined in [common] section will be used. If there is also no [common] section, X509_USER_{CERT,KEY} variables are used. Default is &#8216;/etc/grid-security/host{cert,key}.pem&#8217; </p>
<p> <i>Example:</i><br />
 x509_user_key=&quot;/etc/grid-security/hostkey.pem&quot;<br />
 x509_user_cert=&quot;/etc/grid-security/hostcert.pem&quot; </p>
<dt><code>x509_cert_dir</code></p>
<dd>x509_cert_dir &#8211; the directory containing CA certificates. This information is needed by the &#8216;require_issuerdn&#8217; [vo] block option. Default is &#8216;/etc/grid-security/certificates/&#8217;. </p>
<p> <i>Example:</i><br />
 x509_cert_dir=&quot;/etc/grid-security/certificates/&quot; </p>
<dt><code>generate_vomapfile</code></p>
<dd>generate_vomapfile &#8211; control is nordugridmap will generate vo-mapfile used by arc-ur-logger. Default is &#8216;yes&#8217;. </p>
<p> <i>Example:</i><br />
 generate_vomapfile=&quot;yes&quot; </p>
<dt><code>vomapfile</code></p>
<dd>vomapfile &#8211; path to vo-mapfile location. Default is /etc/grid-security/grid-vo-mapfile </p>
<p> <i>Example:</i><br />
 vomapfile=&quot;/etc/grid-security/grid-vo-mapfile&quot; </p>
<dt><code>log_to_file</code></p>
<dd>log_to_file &#8211; control whether logging output of nordugridmap will be saved to file. Default is &#8216;no&#8217; (STDERR is used). </p>
<p> <i>Example:</i><br />
 log_to_file=&quot;yes&quot; </p>
<dt><code>logfile</code></p>
<dd>logfile &#8211; specify the nordugridmap log file location when in use. Default is &#8216;/var/log/arc/nordugridmap.log&#8217;. </p>
<p> <i>Example:</i><br />
 logfile=&quot;/var/log/arc/nordugridmap.log&quot; </p>
<dt><code>cache_enable</code></p>
<dd>cache_enable &#8211; control whether caching of external sources will be used. Default is &#8216;yes&#8217;. </p>
<p> <i>Example:</i><br />
 cache_enable=&quot;yes&quot; </p>
<dt><code>cachedir</code></p>
<dd>cachedir &#8211; specify the path where cached sources will be stored. Default is &#8216;/var/spool/nordugrid/gridmapcache/&#8217; </p>
<p> <i>Example:</i><br />
 cachedir=&quot;/var/spool/nordugrid/gridmapcache/&quot; </p>
<dt><code>cachetime</code></p>
<dd>cachetime &#8211; controls how many time (in seconds) cached information remains valid. Default is 259200 (3 days). </p>
<p> <i>Example:</i><br />
 cachetime=&quot;259200&quot; </p>
<dt><code>issuer_processing</code></p>
<dd>issuer_processing &#8211; control the behaviour of [vo] block require_issuerdn parameter. Valid values are &#8216;relaxed&#8217; and &#8216;strict&#8217;. Please see &#8216;require_issuerdn&#8217; description in [vo] block for details. Default is &#8216;relaxed&#8217;. </p>
<p> <i>Example:</i><br />
 issuer_processing=&quot;relaxed&quot; </p>
<dt><code>mapuser_processing</code></p>
<dd>mapuser_processing &#8211; control the behaviour of [vo] block mapped_unixid parameter usage. Valid values are &#8216;overwrite&#8217; and &#8216;keep&#8217;. Please see &#8216;mapped_unixid&#8217; description in [vo] block for details. Default is &#8216;keep&#8217;. </p>
<p> <i>Example:</i><br />
 mapuser_processing=&quot;keep&quot; </p>
<dt><code>allow_empty_unixid</code></p>
<dd>allow_empty_unixid &#8211; control whether empty (or unspecified) Please see &#8216;mapped_unixid&#8217; description of [vo] block for details. Default is &#8216;no&#8217; </p>
<p> <i>Example:</i><br />
 allow_empty_unixid=&quot;no&quot; </p>
<dt><code>voms_method</code></p>
<dd>voms_method &#8211; control how to get information from voms(s) sources. Valid values are:<br />
&nbsp;<wbr>&nbsp;<wbr>soap &#8211; call SOAP method directly using SOAP::Lite<br />
&nbsp;<wbr>&nbsp;<wbr>get&nbsp;<wbr>&nbsp;<wbr>&#8211; use old implementation that manually parses XML response Default is &#8216;soap&#8217;. </p>
<p> <i>Example:</i><br />
 voms_method=&quot;soap&quot; </p>
<dt><code>debug</code></p>
<dd>debug level &#8211; controls the verbosity of nordugridmap output. Valid values are:<br />
&nbsp;<wbr>&nbsp;<wbr>0 &#8211; FATAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; only critical fatal error shown<br />
&nbsp;<wbr>&nbsp;<wbr>1 &#8211; ERROR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; errors, including non-critical are shown<br />
&nbsp;<wbr>&nbsp;<wbr>2 &#8211; WARNING&nbsp;<wbr>(default)&nbsp;<wbr>&#8211; configuration errors that can be ignored<br />
&nbsp;<wbr>&nbsp;<wbr>3 &#8211; INFO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; processing information<br />
&nbsp;<wbr>&nbsp;<wbr>4 &#8211; VERBOSE &#8211; a bit more processing information<br />
&nbsp;<wbr>&nbsp;<wbr>5 &#8211; DEBUG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; lot of processing information </p>
<p> When test run is requested (&#8211;test command line option of the nordugridmap) debug level is automatically set to 5 (DEBUG). Default is 2 (WARNING) </p>
<p> <i>Example:</i><br />
 debug=&quot;4&quot; </p>
<dt><code>fetch_timeout</code></p>
<dd>fetch_timeout &#8211; control how many time (in seconds) nordugridmap will wait for external sources retrieval. Default is 15. </p>
<p> <i>Example:</i><br />
 fetch_timeout=&quot;15&quot; </p>
</dl>
<h2>[acix/cacheserver] block</h2>
<p>The cache server component of ACIX runs alongside A-REX. It periodically scans the cache directories and composes a Bloom filter of cache content which can be pulled by an ACIX index server. </p>
<dl>
<dt><code>hostname</code></p>
<dd>Hostname on which the cache server listens. Default is all available interfaces. </p>
<p> <i>Example:</i><br />
 hostname=&quot;myhost.org&quot; </p>
<dt><code>port</code></p>
<dd>Port on which the cache server listens. Default is 5443. </p>
<p> <i>Example:</i><br />
 port=&quot;6000&quot; </p>
<dt><code>logfile</code></p>
<dd>Log file location for the cache server. Default is /var/log/arc/acix-cache.log </p>
<p> <i>Example:</i><br />
 logfile=&quot;/tmp/acix-cache.log&quot; </p>
<dt><code>cachedump</code></p>
<dd>Whether to make a dump of the cache contents in a file at $TMP/ARC-ACIX/timestamp each time the cache server runs. Default is no. </p>
<p> <i>Example:</i><br />
 cachedump=&quot;yes&quot; </p>
</dl>
<h2>[acix/indexserver] block</h2>
<p>The index server component of ACIX collects cache content filters from a set of cache servers configured in this block. The index server can be queried for the location of cached files. </p>
<dl>
<dt><code>cacheserver</code></p>
<dd>ACIX cache servers from which to pull information </p>
<p> <i>Example:</i><br />
 cacheserver=&quot;<a rel="nofollow" href="https://some.host:5443/data/cache">https://some.host:5443/data/cache</a>&quot;<br />
 cacheserver=&quot;<a rel="nofollow" href="https://another.host:5443/data/cache">https://another.host:5443/data/cache</a>&quot; </p>
</dl>
<h2>[gangliarc] block</h2>
<p>Gangliarc provides monitoring of ARC-specific metrics through ganglia. It can be run with zero configuration or customised with options in the [gangliarc] block. </p>
<dl>
<dt><code>frequency</code></p>
<dd>The period between each information gathering cycle, in seconds. Default is 20. </p>
<p> <i>Example:</i><br />
 frequency=&quot;30&quot; </p>
<dt><code>gmetric_exec</code></p>
<dd>Path to gmetric executable. Default is /usr/bin/gmetric. </p>
<p> <i>Example:</i><br />
 gmetric_exec=&quot;/usr/local/bin/gmetric&quot; </p>
<dt><code>logfile</code></p>
<dd>log file of the daemon. Default is /var/log/arc/gangliarc.log. </p>
<p> <i>Example:</i><br />
 logfile=&quot;/tmp/gangliarc.log&quot; </p>
<dt><code>pidfile</code></p>
<dd>pid file of the daemon. Default is /var/run/gangliarc.pid. </p>
<p> <i>Example:</i><br />
 pidfile=&quot;/tmp/gangliarc.pid&quot; </p>
<dt><code>python_bin_path</code></p>
<dd>path to python executable. Default is /usr/bin/python. </p>
<p> <i>Example:</i><br />
 python_bin_path=&quot;/usr/local/bin/python&quot; </p>
<dt><code>metrics</code></p>
<dd>the metrics to be monitored. Default is &quot;all&quot;. metrics takes a comma-separated list of one or more of the following metrics:<br />
&nbsp;<wbr>&#8211; staging &#8212; number of tasks in different data staging states<br />
&nbsp;<wbr>&#8211; cache &#8212; free cache space<br />
&nbsp;<wbr>&#8211; session &#8212; free session directory space<br />
&nbsp;<wbr>&#8211; heartbeat &#8212; last modification time of A-REX heartbeat&nbsp;<wbr><br />
&nbsp;<wbr>&#8211; processingjobs &#8212; the number of jobs currently being processed by ARC&nbsp;<wbr>(jobs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>between PREPARING and FINISHING states)<br />
&nbsp;<wbr>&#8211; failedjobs &#8212; the number of failed jobs per last 100 finished<br />
&nbsp;<wbr>&#8211; jobstates &#8212; number of jobs in different A-REX internal stages<br />
&nbsp;<wbr>&#8211; all &#8212; all of the above metrics </p>
<p> <i>Example:</i><br />
 metrics=&quot;all&quot; </p>
</dl>
