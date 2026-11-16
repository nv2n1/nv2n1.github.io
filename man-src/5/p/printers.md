---
title: "printers(5)"
name: "printers"
section: "5"
letter: "p"
url: "/docs/linux/man/5-printers/"
---

printers.conf - printer configuration file for cups

<h2>Description</h2>

The <i>printers.conf</i> file defines the local printers that are available. It is normally located in the <i>/etc/cups</i> directory and is generated automatically by the <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i> program when printers are added or deleted. 

 Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.

<h2>Directives</h2>

<dl><dt>&lt;Printer name&gt; ... &lt;/Printer&gt;
</dt><dd>Defines a specific printer.
</dd><dt>&lt;DefaultPrinter name&gt; ... &lt;/Printer&gt;
</dt><dd>Defines a default printer.
</dd><dt>Accepting Yes
</dt><dd></dd><dt>Accepting No
</dt><dd>Specifies whether the printer is accepting new jobs.
</dd><dt>AllowUser [ user @group ... ]
</dt><dd>Allows specific users and groups to print to the printer.
</dd><dt>DenyUser [ user @group ... ]
</dt><dd>Prevents specific users and groups from printing to the printer.
</dd><dt>DeviceURI uri
</dt><dd>Specifies the device URI for a printer.
</dd><dt>ErrorPolicy abort-job
</dt><dd></dd><dt>ErrorPolicy retry-current-job
</dt><dd></dd><dt>ErrorPolicy retry-job
</dt><dd></dd><dt>ErrorPolicy stop-printer
</dt><dd>Specifies the error policy for the printer.
</dd><dt>Info text
</dt><dd>Specifies human-readable text describing the printer.
</dd><dt>JobSheets banner banner
</dt><dd>Specifies the banner pages to use for the printer.
</dd><dt>KLimit number
</dt><dd>Specifies the job-k-limit value for the printer.
</dd><dt>Location text
</dt><dd>Specifies human-readable text describing the location of the printer.
</dd><dt>OpPolicy name
</dt><dd>Specifies the operation policy for the printer.
</dd><dt>PageLimit number
</dt><dd>Specifies the job-page-limit value for the printer.
</dd><dt>PortMonitor monitor
</dt><dd>Specifies the port monitor for a printer.
</dd><dt>QuotaPeriod seconds
</dt><dd>Specifies the job-quota-period value for the printer.
</dd><dt>Shared Yes
</dt><dd></dd><dt>Shared No
</dt><dd>Specifies whether the printer is shared.
</dd><dt>State idle
</dt><dd></dd><dt>State stopped
</dt><dd>Specifies the initial state of the printer (Idle or Stopped)
</dd><dt>StateMessage text
</dt><dd>Specifies the message associated with the state.
</dd><dt>StateTime seconds
</dt><dd>Specifies the date/time associated with the state.</dd></dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a HREF="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
