---
title: "rhsm-conf(5)"
name: "rhsm-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rhsm-conf/"
description: "rhsm.conf – Configuration file for the subscription-manager tooling"
---

<p>rhsm.conf &#8211; Configuration file for the subscription-manager tooling</p>
<h2>Description</h2>
<p>The rhsm.conf file is the configuration file for various subscription manager tooling. This includes <code>subscription-manager</code>, <code>subscription-manager-gui</code>, <code>rhsmcertd</code>, and <code>virt-who</code>.</p>
<h2>[Server] Options</h2>
<p>hostname</p>
<dl>
<dd>The hostname of the subscription service being used. The default is the Red Hat Customer Portal which is subscription.rhsm.redhat.com. This default should not be retrofitted to previously installed versions. It should be incorporated as the default going forward.</dl>
<p> prefix</p>
<dl>
<dd>Server prefix where the subscription service is registered.</dl>
<p> port</p>
<dl>
<dd>The port which the subscription service is listening on.</dl>
<p> insecure</p>
<dl>
<dd>This flag enables or disables entitlement server certification verification using the certificate authorities which are installed in /etc/rhsm/ca.</dl>
<p> ssl_verify_depth</p>
<dl>
<dd>Sets the number of certificates which should be used to verify the servers identity. This is an advanced control which can be used to secure on premise installations.</dl>
<p> proxy_hostname</p>
<dl>
<dd>Set this to a non-blank value if <code>subscription-manager</code> should use a reverse proxy to access the subscription service. This sets the host for the reverse proxy.</dl>
<p> proxy_port</p>
<dl>
<dd>Set this to a non-blank value if <code>subscription-manager</code> should use a reverse proxy to access the subscription service. This sets the port for the reverse proxy.</dl>
<p> proxy_username</p>
<dl>
<dd>Set this to a non-blank value if <code>subscription-manager</code> should use an authenticated reverse proxy to access the subscription service. This sets the username for the reverse proxy.</dl>
<p> proxy_password</p>
<dl>
<dd>Set this to a non-blank value if <code>subscription-manager</code> should use an authenticated reverse proxy to access the subscription service. This sets the password for the reverse proxy.</dl>
<h2>[Rhsm] Options</h2>
<p>baseurl</p>
<dl>
<dd>This setting is the prefix for all content which is managed by the subscription service. This should be the hostname for the Red Hat CDN, the local Satellite or Capsule depending on your deployment.</dl>
<p> ca_cert_dir</p>
<dl>
<dd>The location for the certificates which are used to communicate with the server and to pull down content.</dl>
<p> repo_ca_cert</p>
<dl>
<dd>The certificate to use for server side authentication during content downloads.</dl>
<p> productCertDir</p>
<dl>
<dd>The directory where product certificates should be stored.</dl>
<p> entitlementCertDir</p>
<dl>
<dd>The directory where entitlement certificates should be stored.</dl>
<p> consumerCertDir</p>
<dl>
<dd>The directory where the consumers identity certificate is stored.</dl>
<p> manage_repos</p>
<dl>
<dd>Set this to <i>1</i> if subscription manager should manage a yum repos file. If set, it will manage the file /etc/yum.repos.d/redhat.repo. If set to <i>0</i> then the subscription is only used for tracking purposes, not content. The /etc/yum.repos.d/redhat.repo file will either be purged or deleted.</dl>
<p> full_refresh_on_yum</p>
<dl>
<dd>Set to <i>1</i> if the /etc/yum.repos.d/redhat.repo should be updated with every server command. This will make yum less efficient, but can ensure that the most recent data is brought down from the subscription service.</dl>
<p> report_package_profile</p>
<dl>
<dd>Set to <i>1</i> if <code>rhsmcertd</code> should report the system&#8217;s current package profile to the subscription service. This report helps the subscription service provide better errata notifications.</dl>
<p> pluginDir</p>
<dl>
<dd>The directory to search for subscription manager plug-ins</dl>
<p> pluginConfDir</p>
<dl>
<dd>The directory to search for plug-in configuration files</dl>
<h2>[Rhsmcertd] Options</h2>
<p>certCheckInterval</p>
<dl>
<dd>The number of minutes between runs of the <code>rhsmcertd</code> daemon</dl>
<p> autoAttachInterval</p>
<dl>
<dd>The number of minutes between attempts to run auto-attach on this consumer.</dl>
<h2>[Logging] Options</h2>
<p>default_log_level</p>
<dl>
<dd>The default log level for all loggers in subscription-manager, python-rhsm, rhsmd, and rhsmcertd. Note: Other keys in this section will override this value for the specified logger.</dl>
<p> MODULE_NAME[.SUBMODULE &#8230;] = [log_level]</p>
<dl>
<dd>Logging can be configured on a module-level basis via entries of the format above where:</p>
<dl>
<dd><code>module_name</code> is subscription_manager, rhsm, or rhsm-app. </p>
<p> <code>submodule</code> can be optionally specified to further override the logging level down to a specific file. </p>
<p> <code>log_level</code> is the log level to set the specified logger (one of: DEBUG, INFO, WARNING, ERROR, or CRITICAL).</dl>
</dl>
<h2>Author</h2>
<p>Bryan Kearney &lt;bkearney [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-subscription-manager/">subscription-manager</a></code>(8), <code><a href="/docs/linux/man/8-subscription-manager-gui/">subscription-manager-gui</a></code>(8), <code><a href="/docs/linux/man/8-rhsmcertd/">rhsmcertd</a></code>(8)</p>
<h2>Resources</h2>
<p>Main web site: <a rel="nofollow" href="http://www.candlepinproject.org/">http://www.candlepinproject.org/</a></p>
<h2>Copying</h2>
<p>Copyright (c) 2010-2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
