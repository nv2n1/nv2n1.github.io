---
title: "cgsnapshot(1)"
name: "cgsnapshot"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgsnapshot/"
description: "cgsnapshot – generate the configuration file for given controllers"
---

<h2>NAME</h2>
<p> cgsnapshot &#8211; generate the configuration file for given controllers </p>
<h2>SYNOPSIS</h2>
<p> <code>cgsnapshot</code> [<code>-h</code>] [<code>-s</code>] [<code>-t</code>] [<code>-b</code> <i>file</i>] [<code>-w</code> <i>file</i>] [<code>-f</code> <i>output_file</i>] [<code>controller</code>] [&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>cgsnapshot</code> generates the cgconfig compatible configuration file for the given controllers. If no controller is set, then cgsnapshot shows all mounted hierarchies. The output is in the same format as the <code>cgconfig.conf</code> configuration file. </p>
<dl>
<dt><code>-b file</code></p>
<dd> Display only variables from the blacklist. The default location of the blacklist is <code>/etc/cgsnapshot_blacklist.conf.</code> This list contains all variables which should be ignored by the <code>cgsnapshot</code> If the variable is blacklisted, it will not be displayed. If it is not present on the blacklist, the whitelist is checked. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> display this help and exit </p>
<dt><code>-f, &#8211;file</code></p>
<dd> Redirect the output to output_file </p>
<dt><code>-s, &#8211;silent</code></p>
<dd> Ignore all warnings </p>
<dt><code>-t, &#8211;strict</code></p>
<dd> Do not display the variables which are not on the whitelist </p>
<dt><code>-w file</code></p>
<dd> Set the blacklist configuration file. This list contains all variables which should be displayed by <code>cgsnapshot</code> If the variable is not blacklisted, the whitelist is checked. If the variable is on the whitelist, it is displayed by <code>cgsnapshot</code> If the variable is not on the whitelist, the variable is displayed and a warning message is produced. By default the whitelist is not used. </p>
<p> The warning message can be omitted using the <code>-s, &#8211;silent</code> flag. If the <code>-t, &#8211;strict</code> flag is used, the variable which is not on the whitelist is not displayed. </p>
<dt><code>controller</code></p>
<dd> defines the controller whose hierarchies will be output </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/cgsnapshot_blacklist.conf</code></p>
<dd> default blacklist </p>
<dt><code>/etc/cgsnapshot_whitelist.conf</code></p>
<dd> default whitelist </p>
<dt><code>/etc/cgconfig.conf</code></p>
<dd> default libcgroup configuration file </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgsnapshot -s -f /etc/cgconfig.conf.cgsnapshot</code></p>
<dd> create configuration file which contains all mounted controllers and all control groups which are on the actual system </p>
<dt><code>cgsnapshot -s -f /etc/cgconfig.conf.cgsnapshot cpu</code></p>
<dd> create configuration file which contains hierarchy containing cpu controller and all its control groups on the actual system </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgconfig.conf (5) </p>
<h2>Index</h2>
