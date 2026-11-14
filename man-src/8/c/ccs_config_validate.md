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
<dt><code>-h</code></p>
<dd>Print this help, then exit</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit</p>
<dt><code>-v</code></p>
<dd>Produce verbose output</dl>
<h3>Validating XML configuraton files:</h3>
<dl>
<dt><code>-f</code> configfile</p>
<dd>Validate an alternate config file without preloading it with default values.</p>
<dt><code>-l</code> configfile</p>
<dd>Validate an alternate config file with preloading of default values (recommended option).</dl>
<h3>Advanced options:</h3>
<dl>
<dt><code>-r</code></p>
<dd>Force validation of runtime config</p>
<dt> <code>-C</code> config_loader</p>
<dd>Override config plugin loader</p>
<dt><code>-t</code> tempfile</p>
<dd>Force temporay file to tempfile</p>
<dt><code>-n</code></p>
<dd>Do not remove temporary file</p>
<dt><code>-o</code></p>
<dd>Overwrite temporary file (dangerous)</dl>
<h2>Default</h2>
<p>Default operation for ccs_config_validate is to load the currently configured environment and verify the outcoming configuration.</p>
<dl>
<dt>Example 1: current environment uses a configuration file (/etc/cluster/cluster.conf).</p>
<dd>The user modifies cluser.conf and executes ccs_config_validate without options. The tool will validate the modified cluster.conf after including default values.</p>
<dt>Example 2: current environment is set to load the configuration from LDAP. Users</p>
<dd>modifies LDAP databse and before pushing the change to the nodes, she/he can issue ccs_config_validate to verify the contents o the LDAP database automatically (as long as the correct LDAP environment is set in the cman/cluster sysconfig/defaults files). </p>
</dl>
