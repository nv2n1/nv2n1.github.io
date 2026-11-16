---
title: "opafmconfigcheck(8)"
name: "opafmconfigcheck"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opafmconfigcheck/"
---

opafmconfigcheck 

 

 

 Parses and verifies the configuration file of a Fabric Manager (FM). Displays debugging and status information.

<h2>Syntax</h2>

opafmconfigcheck [-s] [-c <i>config_file</i>] [-v] [-d]

<h2>Options</h2>

<dl><dt>--help
</dt><dd>Produces full help text. 
</dd><dt>-s
</dt><dd>Enables strict check mode. This option points out inconsistencies or invalid settings in VF and multicast configurations. 
</dd><dt>-c <i>config_file</i>
</dt><dd>Specifies configuration file. Default = /etc/sysconfig/opafm.xml 
</dd><dt>-v
</dt><dd>Displays debugging and status information. 
</dd><dt>-d
</dt><dd>Displays configuration checksum information. 
</dd></dl>

<h2>Example</h2>

opafmconfigcheck 
 opafmconfigcheck -v 
 opafmconfigcheck -sv 
