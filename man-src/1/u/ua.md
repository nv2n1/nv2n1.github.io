---
title: "ua(1)"
name: "ua"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ua/"
description: "pro – Manage Ubuntu Pro services from Canonical"
---

<h2 class="name">NAME</h2>
<p> pro &#8211; Manage Ubuntu Pro services from Canonical </p>
<h2>SYNOPSIS</h2>
<p> <code>pro</code> &lt;command&gt; [&lt;args&gt;]<br />
 <code>ua</code> &lt;command&gt; [&lt;args&gt;]<br />
 <code>ubuntu-advantage</code> &lt;command&gt; [&lt;args&gt;] </p>
<h2>DESCRIPTION</h2>
<p> Ubuntu Pro is a collection of services offered by Canonical to Ubuntu users. The Ubuntu Pro command line tool is used to attach a system to an Ubuntu Pro contract to then enable and disable services from Canonical. The available commands and services are described in more detail below. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>attach</code> [&#8211;no-auto-enable] [&#8211;attach-config=/path/to/file.yaml] &lt;token&gt;</p>
<dd> Connect an Ubuntu Pro support contract to this machine. </p>
<p> The <i>token</i> parameter can be obtained from <a rel="nofollow" href="https://auth.contracts.canonical.com/.">https://auth.contracts.canonical.com/.</a> </p>
<p> The <i>&#8211;attach-config</i> option can be used to provide a file with the token and optionally, a list of services to enable after attaching. The <i>token</i> parameter should not be used if this option is provided. An attach config file looks like the following:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;token: YOUR_TOKEN_HERE&nbsp;<wbr>&nbsp;#&nbsp;required<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;enable_services:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;optional list of service names to auto-enable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; esm-infra<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; esm-apps<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; cis </p>
<p> The optional <i>&#8211;no-auto-enable</i> flag will disable the automatic enablement of recommended entitlements which usually happens immediately after a successful attach. </p>
<p> The exit code can be:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0: on successful attach<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1: in case of any error while trying to attach<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2: if the machine is already attached </p>
<dt><code>collect-logs [-o &lt;file&gt;| &#8211;output &lt;file&gt;]</code></p>
<dd> Create a tarball with all relevant logs and debug data. </p>
<p> The <i>&#8211;output</i> parameter defines the path to the tarball. If not provided, the file is saved as <code>ua_logs.tar.gz</code> in the current directory. </p>
<dt><code>detach</code></p>
<dd> Remove the Ubuntu Pro support contract from this machine. This also disables all enabled services that can be. </p>
<dt><code>disable</code> [cc-eal|cis|esm|fips|fips-updates|livepatch|ros|ros-updates]</p>
<dd> Disable this machine&#8217;s access to an Ubuntu Pro service. </p>
<dt><code>enable</code> [cc-eal|cis|esm|fips|fips-updates|livepatch|ros|ros-updates]</p>
<dd> Activate and configure this machine&#8217;s access to an Ubuntu Pro service. </p>
<dt><code>fix</code> &lt;security_issue&gt;</p>
<dd> Fix a CVE or USN on the system by upgrading the appropriate package(s). </p>
<p> &lt;security_issue&gt; can be any of the following formats: CVE-yyyy-nnnn, CVE-yyyy-nnnnnnn, or USN-nnnn-dd. </p>
<p> The exit code can be 0, 1, or 2.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0: the fix was successfully applied<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1: the fix cannot be applied<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2: the fix was applied but requires a reboot before it takes effect </p>
<dt><code>refresh</code></p>
<dd> Refresh contract and service details from Canonical. </p>
<dt><code>security-status</code></p>
<dd> Show security updates for packages in the system, including all available ESM related content. </p>
<dt><code>status</code> [&#8211;format=tabular|json|yaml] [&#8211;simulate-with-token TOKEN] [&#8211;all]</p>
<dd> Report current status of Ubuntu Pro services on system. </p>
<p> This shows whether this machine is attached to an Ubuntu Pro support contract. When attached, the report includes the specific support contract details including contract name, expiry dates, and the status of each service on this system. </p>
<p> The attached status output has four columns: </p>
<p> <code>SERVICE</code>: name of the service </p>
<p> <code>ENTITLED</code>: whether the contract to which this machine is attached entitles use of this service. Possible values are: <i>yes</i> or <i>no</i> </p>
<p> <code>STATUS</code>: whether the service is enabled on this machine. Possible values are: <i>enabled</i>, <i>disabled</i>, <i>n/a</i> (if your contract entitles you to the service, but it isn&#8217;t available for this machine) or <i>—</i> (if you aren&#8217;t entitled to this service) </p>
<p> <code>DESCRIPTION</code>: a brief description of the service </p>
<p> The unattached status output instead has three columns. <code>SERVICE</code> and <code>DESCRIPTION</code> are the same as above, and there is the addition of: </p>
<p> <code>AVAILABLE</code>: whether this service would be available if this machine were attached. The possible values are <i>yes</i> or <i>no</i>. </p>
<p> If &#8211;simulate-with-token is used, then the output has five columns. <code>SERVICE</code>, <code>AVAILABLE</code>, <code>ENTITLED</code> and <code>DESCRIPTION</code> are the same as mentioned above, and <code>AUTO_ENABLED</code> shows whether the service is set to be enabled when that token is attached. </p>
<p> If the &#8211;all flag is set, beta and unavailable services are also listed in the output. </p>
<dt><code>version</code></p>
<dd> Show version of the Ubuntu Pro package. </p>
</dl>
<h2>PRO UPGRADE DAEMON</h2>
<p> Ubuntu Pro client sets up a daemon on supported platforms (currently GCP only) to detect if an Ubuntu Pro license is purchased for the machine. If an Ubuntu Pro license is detected, then the machine is automatically attached. If you are uninterested in Ubuntu Pro services, you can safely stop and disable the daemon using systemctl: </p>
<p> sudo systemctl stop ubuntu-advantage.service sudo systemctl disable ubuntu-advantage.service </p>
<h2>TIMER JOBS</h2>
<p> Ubuntu Pro client sets up a systemd timer to run jobs that need to be executed recurrently. The timer itself ticks every 5 minutes on average, and decides which jobs need to be executed based on their intervals. </p>
<p> Jobs are executed by the timer script if the script has not yet run successfully, or their interval since last successful run is already exceeded. There is a random delay applied to the timer, to desynchronize job execution time on machines spinned at the same time, avoiding multiple synchronized calls to the same service. </p>
<p> Current jobs being checked and executed are:</p>
<dl>
<dt><code>update_messaging</code></p>
<dd> Makes sure that the MOTD and APT messages match the available/enabled services on the system, showing information about available packages or security updates. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> By default, Ubuntu Pro client configuration options are read from <code>/etc/ubuntu-advantage/uaclient.conf. </p>
<p> The following configuration options are available:</p>
<dl>
<dt>contract_url</code></p>
<dd> The Ubuntu Pro contract server URL</p>
<dt><code>security_url</code></p>
<dd> The Ubuntu Pro security server URL</p>
<dt><code>data_dir</code></p>
<dd> Where Ubuntu Pro client stores its data files</p>
<dt><code>log_level</code></p>
<dd> The logging level used when writing to <code>log_file</code></p>
<dt><code>log_file</code></p>
<dd> The log file for the Ubuntu Pro client cli</p>
<dt><code>timer_log_file</code></p>
<dd> The log file for the Ubuntu Pro timer and timer jobs</p>
<dt><code>daemon_log_file</code></p>
<dd> The log file for the Ubuntu Pro daemon </p>
</dl>
<p> <code>The following options must be nested under the &quot;ua_config&quot; key:</code> </p>
<dl>
<dt><code>http_proxy</code></p>
<dd> If set, pro will use the specified http proxy when making any http requests</p>
<dt><code>https_proxy</code></p>
<dd> If set, pro will use the specified https proxy when making any https requests</p>
<dt><code>apt_http_proxy</code></p>
<dd> <code>[DEPRECATED]</code> If set, pro will configure apt to use the specified http proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. (Please use <code>global_apt_http_proxy</code>)</p>
<dt><code>apt_https_proxy</code></p>
<dd> <code>[DEPRECATED]</code> If set, pro will configure apt to use the specified https proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. (Please use <code>global_apt_https_proxy</code>)</p>
<dt><code>global_apt_http_proxy</code></p>
<dd> If set, pro will configure apt to use the specified http proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. Set this if you prefer a global proxy for all resources, not just the ones from <i>esm.ubuntu.com</i><code></p>
<dt>global_apt_https_proxy</code></p>
<dd> If set, pro will configure apt to use the specified https proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. Set this if you prefer a global proxy for all resources, not just the ones from <i>esm.ubuntu.com</i><code></p>
<dt>ua_apt_http_proxy</code></p>
<dd> If set, pro will configure apt to use the specified http proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. This proxy is limited to accessing resources from <i>esm.ubuntu.com</i><code></p>
<dt>ua_apt_https_proxy</code></p>
<dd> If set, pro will configure apt to use the specified https proxy by writing a apt config file to /etc/apt/apt.conf.d/90ubuntu-advantage-aptproxy. This proxy is limited to accessing resources from <i>esm.ubuntu.com</i><code></p>
<dt>&lt;job_name&gt;_timer</code></p>
<dd> Sets the timer running interval for a specific job. Those intervals are checked every time the systemd timer runs. </p>
</dl>
<p> If needed, authentication to the proxy server can be performed by setting username and password in the URL itself, as in: </p>
<pre>
  http_proxy: http://&lt;username&gt;:&lt;password&gt;@&lt;fqdn&gt;:&lt;port&gt;
</pre>
<p> Additionally, some configuration options can be overridden in the environment by setting an environment variable prefaced by <code>UA_&lt;option_name&gt;</code>. Both uppercase and lowercase environment variables are allowed. The configuration options that support this are: data_dir, log_file, timer_log_file, daemon_log_file, log_level, and security_url. </p>
<p> For example, the following overrides the log_level found in uaclient.conf: </p>
<pre>
  UA_LOG_LEVEL=info pro attach
</pre>
<h2>SERVICES</h2>
<dl>
<dt><code>Common Criteria EAL2 Provisioning (cc-eal)</code></p>
<dd> Enables and install the Common Criteria artifacts. </p>
<p> The artifacts include a configure script, a tarball with additional packages, and post install scripts. The artifacts will be installed in /usr/lib/common-criteria directory and the README and configuration guide are available in /usr/share/doc/ubuntu-commoncriteria directory. </p>
<dt><code>CIS Audit (cis)</code></p>
<dd> Enables and installs the CIS Audit artifacts. </p>
<dt><code>Expanded Security Maintenance (esm)</code></p>
<dd> Expanded Security Maintenance ensures the ongoing security and integrity of systems running Ubuntu Long Term Support (LTS) releases through Ubuntu Pro for Infrastructure. </p>
<p> See <a rel="nofollow" href="https://ubuntu.com/esm">https://ubuntu.com/esm</a> for more information. </p>
<dt><code>FIPS 140-2 certified modules (fips)</code></p>
<dd> Install, configure, and enable FIPS 140-2 certified modules. </p>
<p> After successfully enabling FIPS, the system MUST be rebooted. Failing to reboot will result in the system not running the updated FIPS kernel. </p>
<p> Disabling FIPS is not currently supported. </p>
<dt><code>FIPS 140-2 certified modules with updates (fips-updates)</code></p>
<dd> Install, configure, and enable FIPS 140-2 certified modules with updates. Enabling FIPS with updates will take the system out of FIPS compliance as the updated modules are not FIPS certified. </p>
<p> After successfully enabling FIPS with updates, the system MUST be rebooted. Failing to reboot will result in the system not running the updated FIPS kernel. </p>
<p> Disabling FIPS with updates is not currently supported. </p>
<dt><code>Livepatch Service (livepatch)</code></p>
<dd> Automatically apply critical kernel patches without rebooting. Reduces downtime, keeping your Ubuntu LTS systems secure and compliant. </p>
<p> See <a rel="nofollow" href="https://ubuntu.com/livepatch">https://ubuntu.com/livepatch</a> for more information. </p>
<dt><code>ROS ESM Security Updates (ros)</code></p>
<dd> Robot Operating System Expanded Security Maintenance &#8211; Only Security Updates provides security fixes for ROS packages to ensure the ongoing integrity of ROS based applications. </p>
<p> See <a rel="nofollow" href="https://ubuntu.com/robotics/ros-esm">https://ubuntu.com/robotics/ros-esm</a> for more information. </p>
<dt><code>ROS ESM All Updates (ros-updates)</code></p>
<dd> Robot Operating System Expanded Security Maintenance &#8211; All Updates provides additional bug fixes in addition to security fixes for ROS packages to ensure the ongoing integrity of ROS based applications. </p>
<p> See <a rel="nofollow" href="https://ubuntu.com/robotics/ros-esm">https://ubuntu.com/robotics/ros-esm</a> for more information. </p>
</dl>
<h2>REPORTING BUGS</h2>
<p> Please report bugs either by running `ubuntu-bug ubuntu-advantage-tools` or login to Launchpad and navigate to <a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/ubuntu-advantage-tools/+filebug">https://bugs.launchpad.net/ubuntu/+source/ubuntu-advantage-tools/+filebug</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2019-2020 Canonical Ltd. </p>
<h2>Index</h2>
