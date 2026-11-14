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
<dd>Produces full help text. 

<dt>-s
<dd>Enables strict check mode. This option points out inconsistencies or invalid settings in VF and multicast configurations. 

<dt>-c <i>config_file</i>
<dd>Specifies configuration file. Default = /etc/sysconfig/opafm.xml 

<dt>-v
<dd>Displays debugging and status information. 

<dt>-d
<dd>Displays configuration checksum information. 

</dl>

<h2>Example</h2>

opafmconfigcheck 
 opafmconfigcheck -v 
 opafmconfigcheck -sv 
