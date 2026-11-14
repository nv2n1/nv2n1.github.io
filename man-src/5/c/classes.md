---
title: "classes(5)"
name: "classes"
section: "5"
letter: "c"
url: "/docs/linux/man/5-classes/"
---

classes.conf - class configuration file for cups

<h2>Description</h2>

The <i>classes.conf</i> file defines the local printer classes that are available. It is normally located in the <i>/etc/cups</i> directory and is generated automatically by the <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i> program when printer classes are added or deleted. 

 Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.

<h2>Directives</h2>

<dl><dt>&lt;Class name&gt; ... &lt;/Class&gt;
<dd>Defines a specific printer class.
<dt>&lt;DefaultClass name&gt; ... &lt;/Class&gt;
<dd>Defines a default printer class.
<dt>Accepting Yes
<dd><dt>Accepting No
<dd>Specifies whether the printer is accepting new jobs.
<dt>AllowUser [ user @group ... ]
<dd>Allows specific users and groups to print to the printer.
<dt>DenyUser [ user @group ... ]
<dd>Prevents specific users and groups from printing to the printer.
<dt>Info text
<dd>Specifies human-readable text describing the printer.
<dt>JobSheets banner banner
<dd>Specifies the banner pages to use for the printer.
<dt>KLimit number
<dd>Specifies the job-k-limit value for the printer.
<dt>Location text
<dd>Specifies human-readable text describing the location of the printer.
<dt>OpPolicy name
<dd>Specifies the operation policy for the printer.
<dt>PageLimit number
<dd>Specifies the job-page-limit value for the printer.
<dt>Printer
<dd>Specifies a printer that is a member of the printer class.
<dt>QuotaPeriod seconds
<dd>Specifies the job-quota-period value for the printer.
<dt>Shared Yes
<dd><dt>Shared No
<dd>Specifies whether the printer is shared.
<dt>State idle
<dd><dt>State stopped
<dd>Specifies the initial state of the printer (Idle or Stopped)
<dt>StateMessage text
<dd>Specifies the message associated with the state.
<dt>StateTime seconds
<dd>Specifies the date/time associated with the state.</dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a HREF="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, <i><a HREF="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
