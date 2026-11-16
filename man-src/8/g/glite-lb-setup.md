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
<dt><code>-q</code>, &#8211;quiet</dt>
<dd>Print only errors. </dd>
<dt><code>-c</code>, &#8211;check</dt>
<dd>Check database availability (check if setup has been already performed). In case there are no other <code>ACTIONS</code> listed, no default actions are performed and <code>glite-lb-setup</code> will exit immediately with return code 0 (if database exists) or 1 (in other cases). </dd>
<dt><code>-l</code>, &#8211;list</dt>
<dd>List <code>ACTIONS</code> to be executed and exit. This option can be used to view and/or select actions to be performed during setup. For example, the following pair of commands lists available actions and runs the setup omitting BDII: </dd>
<p>&nbsp;<wbr>glite-lb-setup &#8211;list<br />
&nbsp;<wbr>glite-lb-setup&nbsp;<wbr>`glite-lb-setup &#8211;list | sed&nbsp;<wbr>&#8216;s/bdii//&#8217;` </p>
<dt><code>-h</code>, &#8211;help</dt>
<dd>Display help. </dd>
</dl>
<h2>Actions</h2>
<p>ACTIONS are individual tasks or groups of tasks to be performed during setup. </p>
<dl>
<dt><code>all</code> (group)</dt>
<dd>All default actions. If no action is listed in the command line, this one will be performed. </dd>
<dt><code>none</code> (group)</dt>
<dd>No action. </dd>
<dt><code>yaim</code> (group)</dt>
<dd>Actions to be run when launching setup from within the YAIM configurator. Some regular actions (like BDII or CRL) are already covered by YAIM, so they are not performed. </dd>
<dt><code>logger</code> (group)</dt>
<dd>Only actions needed to set up and L&amp;B logger will be performed. This action consists in setting up certificates, messaging, and running the update action. </dd>
<dt><code>upgrade</code> (group)</dt>
<dd>All upgrade actions (remove various obsolete files, &#8230;). </dd>
<dt><code>emir</code> (group)</dt>
<dd>Publish L&amp;B service info to EMIR &#8211; complete setup. Provides service info for L&amp;B (emir_info action) and setup and launch emir-serp daemon (emir_daemon action). </dd>
<dt><code>db</code></dt>
<dd>Checks MySQL, enables MySQL configuration for L&amp;B, sets up the database with grants if it doesn&#8217;t exist and creates indices. Migrates DB from L&amp;B version 3.x if necessary. MySQL server startup is handled in <code>startup</code>, if enabled. </dd>
<dt><code>certs</code></dt>
<dd>Checks and copies host certificates for L&amp;B services. </dd>
<dt><code>msg</code></dt>
<dd>Configures EMI Messaging using the <code>glite-lb-msg-config</code> utility. </dd>
<dt><code>authz</code></dt>
<dd>Creates file <i>/etc/glite-lb/glite-lb-authz.conf</i> based on all of the following configuration variables: type of L&amp;B node ($GLITE_LB_TYPE), service DNs ($GLITE_LB_WMS_DN, $GLITE_LB_SUPER_USERS, $GLITE_LB_RTM_DN) and fine-tuning variables $GLITE_LB_AUTHZ_*. </dd>
<dt><code>harvester</code></dt>
<dd>If enabled ($GLITE_LB_HARVESTER_ENABLED), L&amp;B harvester will be set up and launched. It will be configured to gather notifications from local L&amp;B server. </dd>
<dt><code>bdii</code></dt>
<dd>Sets up the BDII service and gLite info provider wrappers for L&amp;B. BDII service startup is handled in <code>startup</code>, if enabled. </dd>
<p> Packages <i>bdii</i>, <i>sudo</i>, and <i>glite-info-provider-service</i> must be intalled for this action to take effect. </p>
<dt><code>emir_info</code></dt>
<dd>Creates service info file for L&amp;B. </dd>
<p> Package <i>emir-serp</i> must be installed for this action to take effect. </p>
<dt><code>emir_daemon</code></dt>
<dd>Sets up emir-serp daemon. </dd>
<p> Package <i>emir-serp</i> must be installed and $EMIR_URL must be specified for this action to take effect. </p>
<dt><code>upgrade_files</code></dt>
<dd>Remove old obsolete files (upgrade from L&amp;B &lt;= 3.1.1). </dd>
<dt><code>upgrade_logger</code></dt>
<dd>Move L&amp;B logger event files, if needed (upgrade from L&amp;B &lt;= 4.0.1). </dd>
<dt><code>upgrade_notif</code></dt>
<dd>Move L&amp;B notification event files, if needed (upgrade from L&amp;B &gt;= 4.0.1). </dd>
<dt><code>upgrade_proxy</code></dt>
<dd>Move L&amp;B proxy event files, if needed (upgrade from L&amp;B &gt;= 4.0.1). </dd>
<dt><code>upgrade_log4c</code></dt>
<dd>Check the log4c config file used by L&amp;B and fix it if necessary. </dd>
<dt><code>crl</code></dt>
<dd>Sets up fetch-crl to fetch CRLs automatically. </dd>
<dt><code>startup</code></dt>
<dd>Sets up automatic startup of all enabled daemons after boot. </dd>
<dt><code>krb</code> (run only when GLITE_GSS_MECH=krb5)</dt>
<dd>Sets up Kerberos ticket and credential cache files for L&amp;B. </dd>
<p> Requires L&amp;B built with Kerberos support. </p>
<dt><code>krbgsi</code> (not run by default)</dt>
<dd>Sets up Kerberos and enables GSI authentication. </dd>
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
<p><code>yaim</code>(1) <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a></code>(8) <code><a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a></code>(8) <code>glite-lb-harvester</code>(8) </p>
<h2>Author</h2>
<p>L&amp;B Product Team, JRA1, EMI.</p>
