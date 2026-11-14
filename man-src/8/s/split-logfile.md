---
title: "split-logfile(8)"
name: "split-logfile"
section: "8"
letter: "s"
url: "/docs/linux/man/8-split-logfile/"
description: "split-logfile – Split combined virtual hosts access log into one file per virtual host"
---

<p>split-logfile &#8211; Split combined virtual hosts access log into one file per virtual host</p>
<h2>Synopsis</h2>
<p> <code>split-logfile</code> &lt; <i>logfile</i> </p>
<h2>Summary</h2>
<p>&nbsp; </p>
<p> This script will take a combined Web server access log file and break its contents into separate files. It assumes that the first field of each line is the virtual host identity (put there by &quot;%v&quot;), and that the logfiles should be named that+&quot;.log&quot; in the current directory. </p>
<p> The combined log file is read from stdin. Records read will be appended to any existing log files.</p>
<h2>Examples</h2>
<p>split-logfile &lt; /var/log/apache2/other_vhosts_access.log </p>
