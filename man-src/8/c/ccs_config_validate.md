---
title: "ccs_config_validate(8)"
name: "ccs_config_validate"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ccs_config_validate/"
description: "ccs_config_validate"
---

<p>ccs_config_validate</p>
<h2>Description</h2>
<p>Usage: </p>
<p> ccs_config_validate [options]</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Print this help, then exit</dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit</dd>
<dt><code>-v</code></dt>
<dd>Produce verbose output</dd></dl>
<h3>Validating XML configuraton files:</h3>
<dl>
<dt><code>-f</code> configfile</dt>
<dd>Validate an alternate config file without preloading it with default values.</dd>
<dt><code>-l</code> configfile</dt>
<dd>Validate an alternate config file with preloading of default values (recommended option).</dd></dl>
<h3>Advanced options:</h3>
<dl>
<dt><code>-r</code></dt>
<dd>Force validation of runtime config</dd>
<dt> <code>-C</code> config_loader</dt>
<dd>Override config plugin loader</dd>
<dt><code>-t</code> tempfile</dt>
<dd>Force temporay file to tempfile</dd>
<dt><code>-n</code></dt>
<dd>Do not remove temporary file</dd>
<dt><code>-o</code></dt>
<dd>Overwrite temporary file (dangerous)</dd></dl>
<h2>Default</h2>
<p>Default operation for ccs_config_validate is to load the currently configured environment and verify the outcoming configuration.</p>
<dl>
<dt>Example 1: current environment uses a configuration file (/etc/cluster/cluster.conf).</dt>
<dd>The user modifies cluser.conf and executes ccs_config_validate without options. The tool will validate the modified cluster.conf after including default values.</dd>
<dt>Example 2: current environment is set to load the configuration from LDAP. Users</dt>
<dd>modifies LDAP databse and before pushing the change to the nodes, she/he can issue ccs_config_validate to verify the contents o the LDAP database automatically (as long as the correct LDAP environment is set in the cman/cluster sysconfig/defaults files). </dd>
</dl>
