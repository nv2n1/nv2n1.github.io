---
title: "glite-lb-setup(8)"
name: "glite-lb-setup"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-setup/"
description: "glite-lb-setup – script for setting up L&B services"
---

<p>glite-lb-setup &#8211; script for setting up L&amp;B services</p>
<h2>Synopsis</h2>
<p><code>glite-lb-setup</code> [<i>OPTIONS</i>] [<i>ACTION&#8230;</i>] </p>
<h2>Description</h2>
<p>The <code>glite-lb-setup</code> script sets up the L&amp;B server based on environment and sourced files. The setup process is divided into individual <code>ACTIONS</code>. </p>
<h2>Options</h2>
<dl>
<dt><code>-q</code>, &#8211;quiet</p>
<dd>Print only errors. </p>
<dt><code>-c</code>, &#8211;check</p>
<dd>Check database availability (check if setup has been already performed). In case there are no other <code>ACTIONS</code> listed, no default actions are performed and <code>glite-lb-setup</code> will exit immediately with return code 0 (if database exists) or 1 (in other cases). </p>
<dt><code>-l</code>, &#8211;list</p>
<dd>List <code>ACTIONS</code> to be executed and exit. This option can be used to view and/or select actions to be performed during setup. For example, the following pair of commands lists available actions and runs the setup omitting BDII: </p>
<p>&nbsp;<wbr>glite-lb-setup &#8211;list<br />
&nbsp;<wbr>glite-lb-setup&nbsp;<wbr>`glite-lb-setup &#8211;list | sed&nbsp;<wbr>&#8216;s/bdii//&#8217;` </p>
<dt><code>-h</code>, &#8211;help</p>
<dd>Display help. </p>
</dl>
<h2>Actions</h2>
<p>ACTIONS are individual tasks or groups of tasks to be performed during setup. </p>
<dl>
<dt><code>all</code> (group)</p>
<dd>All default actions. If no action is listed in the command line, this one will be performed. </p>
<dt><code>none</code> (group)</p>
<dd>No action. </p>
<dt><code>yaim</code> (group)</p>
<dd>Actions to be run when launching setup from within the YAIM configurator. Some regular actions (like BDII or CRL) are already covered by YAIM, so they are not performed. </p>
<dt><code>logger</code> (group)</p>
<dd>Only actions needed to set up and L&amp;B logger will be performed. This action consists in setting up certificates, messaging, and running the update action. </p>
<dt><code>upgrade</code> (group)</p>
<dd>All upgrade actions (remove various obsolete files, &#8230;). </p>
<dt><code>emir</code> (group)</p>
<dd>Publish L&amp;B service info to EMIR &#8211; complete setup. Provides service info for L&amp;B (emir_info action) and setup and launch emir-serp daemon (emir_daemon action). </p>
<dt><code>db</code></p>
<dd>Checks MySQL, enables MySQL configuration for L&amp;B, sets up the database with grants if it doesn&#8217;t exist and creates indices. Migrates DB from L&amp;B version 3.x if necessary. MySQL server startup is handled in <code>startup</code>, if enabled. </p>
<dt><code>certs</code></p>
<dd>Checks and copies host certificates for L&amp;B services. </p>
<dt><code>msg</code></p>
<dd>Configures EMI Messaging using the <code>glite-lb-msg-config</code> utility. </p>
<dt><code>authz</code></p>
<dd>Creates file <i>/etc/glite-lb/glite-lb-authz.conf</i> based on all of the following configuration variables: type of L&amp;B node ($GLITE_LB_TYPE), service DNs ($GLITE_LB_WMS_DN, $GLITE_LB_SUPER_USERS, $GLITE_LB_RTM_DN) and fine-tuning variables $GLITE_LB_AUTHZ_*. </p>
<dt><code>harvester</code></p>
<dd>If enabled ($GLITE_LB_HARVESTER_ENABLED), L&amp;B harvester will be set up and launched. It will be configured to gather notifications from local L&amp;B server. </p>
<dt><code>bdii</code></p>
<dd>Sets up the BDII service and gLite info provider wrappers for L&amp;B. BDII service startup is handled in <code>startup</code>, if enabled. </p>
<p> Packages <i>bdii</i>, <i>sudo</i>, and <i>glite-info-provider-service</i> must be intalled for this action to take effect. </p>
<dt><code>emir_info</code></p>
<dd>Creates service info file for L&amp;B. </p>
<p> Package <i>emir-serp</i> must be installed for this action to take effect. </p>
<dt><code>emir_daemon</code></p>
<dd>Sets up emir-serp daemon. </p>
<p> Package <i>emir-serp</i> must be installed and $EMIR_URL must be specified for this action to take effect. </p>
<dt><code>upgrade_files</code></p>
<dd>Remove old obsolete files (upgrade from L&amp;B &lt;= 3.1.1). </p>
<dt><code>upgrade_logger</code></p>
<dd>Move L&amp;B logger event files, if needed (upgrade from L&amp;B &lt;= 4.0.1). </p>
<dt><code>upgrade_notif</code></p>
<dd>Move L&amp;B notification event files, if needed (upgrade from L&amp;B &gt;= 4.0.1). </p>
<dt><code>upgrade_proxy</code></p>
<dd>Move L&amp;B proxy event files, if needed (upgrade from L&amp;B &gt;= 4.0.1). </p>
<dt><code>upgrade_log4c</code></p>
<dd>Check the log4c config file used by L&amp;B and fix it if necessary. </p>
<dt><code>crl</code></p>
<dd>Sets up fetch-crl to fetch CRLs automatically. </p>
<dt><code>startup</code></p>
<dd>Sets up automatic startup of all enabled daemons after boot. </p>
<dt><code>krb</code> (run only when GLITE_GSS_MECH=krb5)</p>
<dd>Sets up Kerberos ticket and credential cache files for L&amp;B. </p>
<p> Requires L&amp;B built with Kerberos support. </p>
<dt><code>krbgsi</code> (not run by default)</p>
<dd>Sets up Kerberos and enables GSI authentication. </p>
<p> Requires L&amp;B built with Kerberos support and modified Globus and Kerberos libraries. Tested only with Heimdal implementation of Kerberos. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/profile.d/gridenv.sh</i> Environment variables for setup and startup scripts. Used for interoperability with the YAIM configurator. </p>
<p> <i>/etc/sysconfig/glite-lb</i> Environment variables for setup and startup scripts in RedHat-like distributions (RedHat, Scientific Linux, Fedora, &#8230;). </p>
<p> <i>/etc/default/glite-lb</i> Environment variables for setup and startup scripts in Debian.</p>
<h2>Environment</h2>
<p>See L&amp;B Admin Guide, chapter 2.3.2 &quot;Standard Installation.&quot;</p>
<h2>Examples</h2>
<p>Set up an L&amp;B server running in the combined proxy and server (&quot;BOTH&quot;) mode in Scientific Linux, granting WMS-specific permissions to the given gLite WMS instance: </p>
<pre><code>cat &gt;&gt; /etc/sysconfig/glite-lb &lt;&lt;EOF

SITE_NAME=mysite

SITE_EMAIL=email [at] example.com

GLITE_LB_TYPE=both

GLITE_LB_WMS_DN=\

&quot;/C=UG/L=Tropic/O=Utopia/OU=Relaxation/CN=wms.example.com&quot;

EOF
mysqladmin -u root password [Edited]

MYSQL_PASSWORD=[Edited] glite-lb-setup
</code></pre>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yaim/">yaim</a></code>(1) <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-harvester/">glite-lb-harvester</a></code>(8) </p>
<h2>Author</h2>
<p>L&amp;B Product Team, JRA1, EMI.</p>
