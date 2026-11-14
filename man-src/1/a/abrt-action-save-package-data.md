---
title: "abrt-action-save-package-data(1)"
name: "abrt-action-save-package-data"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-save-package-data/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-save-package-data - Query package database and save package and component name. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-save-package-data</i> [-v] [-c CONFFILE] -d DIR

<h2>DESCRIPTION</h2>

 

 The tool reads problem directory DIR. It analyzes contents of <i>analyzer</i>, <i>executable</i>, <i>cmdline</i> and <i>remote</i> elements, checks database of installed packages, and creates new elements <i>package</i> and <i>component</i>. 

 This data is usually necessary if the problem will be reported to a bug tracking database.

<h3>Integration with ABRT events</h3>

 

 This tool can be used as an ABRT reporter. Example fragment for /etc/libreport/report_event.conf: 

<dl>
<dt>
<dd> <pre>
# Determine in which package/component the crash happened (if not yet done):
EVENT=post-create component=
        abrt-action-save-package-data
</pre></dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> Be verbose</dl>
 

 -c CONFFILE
<dl>
<dt>
<dd> Path to configuration file.</dl>
 

 -d DIR
<dl>
<dt>
<dd> Path to problem directory.</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt_event-conf/">abrt_event.conf</a>(5), <a HREF="/docs/linux/man/5-abrt-action-save-package-data-conf/">abrt-action-save-package-data.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


