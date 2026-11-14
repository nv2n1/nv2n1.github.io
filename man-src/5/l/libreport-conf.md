---
title: "libreport-conf(5)"
name: "libreport-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libreport-conf/"
---

libreport.conf - Configuration file for libreport and its plugins.

<h2>Description</h2>

<i>libreport</i> is libraries providing API for reporting different problems in applications to different bug targets like Bugzilla, ftp, trac, etc... 

 The configuration file consists of items in the format &quot;Option = Value&quot;. A description of each item follows: 

 AlwaysExcludedElements = <i>name, name1, name2</i>
<dl><dd>A colon separated list of problem element names (problem element is usually represented by a single file in a directory (i.e. environment variables are stored in <i>environ</i> file)). The list is used by libreport and its plugins to exclude the listed problem elements from reports. If you do not want to include some information in reports, add the name of problem element that contain this information on this list.</dl>

<h2>Files</h2>

/etc/libreport/libreport.conf
<dl><dd>system configuration</dl>
 

 $XDG_CONFIG_HOME/abrt/settings/libreport.conf
<dl><dd>user specific configuration</dl>

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
