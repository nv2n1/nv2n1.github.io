---
title: "dahdi_genconf(8)"
name: "dahdi_genconf"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_genconf/"
---

dahdi_genconf - Generate configuration for dahdi channels.

<h2>Synopsis</h2>

dahdi_genconf [<font SIZE="-1">FILES</font>...]

<h2>Description</h2>

This script generate configuration files for <font SIZE="-1">DAHDI</font> hardware. The parameters are types of files to generate. By default it will generate the types 'dahdi' and 'chan_dahdi'. See below a complete list.
<dl><dt>dahdi - /etc/dahdi/system.conf
<dd>Configuration for <i><a HREF="/docs/linux/man/1-dahdi_cfg/">dahdi_cfg</a></i>(1). Its location may be overriden by the environment variable <font SIZE="-1">DAHDI_CONF_FILE</font>.
<dt>modules /etc/dahdi/modules
<dd>List of <font SIZE="-1">DAHDI</font> kernel modules to be loaded by the init.d script. One module per line. Its location may be overriden with the variable <font SIZE="-1">DAHDI_MODS_FILE</font>.
<dt>chan_dahdi - /etc/asterisk/dahdi-channels.conf
<dd>Configuration for <i><a HREF="/docs/linux/man/1-asterisk/">asterisk</a></i>(1). It should be included in the main /etc/asterisk/chan_dahdi.conf. Its location may be overriden by the environment variable <font SIZE="-1">CHAN_DAHDI_CHANNELS_FILE</font>.
<dt>users - /etc/asterisk/users.conf
<dd>Configuration for <i><a HREF="/docs/linux/man/1-asterisk/">asterisk</a></i>(1) and AsteriskGUI. Its location may be overriden by the environment variable <font SIZE="-1">USERS_FILE</font>.
<dt>chan_dahdi_full - /etc/asterisk/chan_dahdi.conf
<dd>Configuration for <i><a HREF="/docs/linux/man/1-asterisk/">asterisk</a></i>(1) and AsteriskGUI. Its location may be overriden by the environment variable <font SIZE="-1">CHAN_DAHDI_CONF_FILE</font>.</dl>

<h2>Examples</h2>

Generate /etc/dahdi/system.conf ('dahdi') and a snippet of chan_dahdi.conf ('chan_dahdi'): <pre> dahdi_genconf</pre>Create those two files, and /etc/dahdi/modules: <pre> dahdi_genconf chan_dahdi dahdi modules</pre>
