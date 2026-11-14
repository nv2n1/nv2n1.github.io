---
title: "libipmimonitoring(3)"
name: "libipmimonitoring"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libipmimonitoring/"
description: "libipmimonitoring – a library for IPMI system event and sensor monitoring"
---

<h2>NAME</h2>
<p> libipmimonitoring &#8211; a library for IPMI system event and sensor monitoring</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ipmi_monitoring.h&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>Libipmimonitoring</code> implements a high level sensor and system event monitoring API. For system events, an iterator interface is provided that allows the user to iterate through system events, types, states, and more. For sensors, an iterator and callback interface is provided that allows the user to iterate through sensor values, types, units, states, and more. </p>
<p> In order to improve efficiency, SDR data will be cached on the host. By default it is cached in /var/cache/ipmimonitoringsdrcache. </p>
<p> Interpretation rules for system events and sensors are guided by <code><a href="/docs/linux/man/3-libfreeipmi/">libfreeipmi</a>(3)&#8217;s</code> interpretation library. Configuration of the interpretation rules can be configurd via the configuration file /etc/freeipmi//freeipmi_interpret_sel.conf. and /etc/freeipmi//freeipmi_interpret_sensor.conf See <code><a href="/docs/linux/man/5-freeipmi_interpret_sel-conf/">freeipmi_interpret_sel.conf</a>(5)</code> and <code><a href="/docs/linux/man/5-freeipmi_interpret_sensor-conf/">freeipmi_interpret_sensor.conf</a>(5)</code> for more information on configuring sensor and system event interpretations.</p>
<h2>FILES</h2>
<p> /var/cache/ipmimonitoringsdrcache</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2006-2007 The Regents of the University of California. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-freeipmi_interpret_sel-conf/">freeipmi_interpret_sel.conf</a>(5), <a href="/docs/linux/man/5-freeipmi_interpret_sensors-conf/">freeipmi_interpret_sensors.conf</a>(5) </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
<h2>Index</h2>
