---
title: "libfreeipmi(3)"
name: "libfreeipmi"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libfreeipmi/"
description: "libfreeipmi – FreeIPMI library"
---

<h2>NAME</h2>
<p> libfreeipmi &#8211; FreeIPMI library</p>
<h2>Introduction</h2>
<p> Libfreeipmi is the primary library that most of the FreeIPMI tools are based upon. The following describe the sub-sections of the library.</p>
<dl>
<dt><code>api</code></p>
<dd> The highest level API provided by libfreeipmi. It abstracts away the details of inband and outofband protocols from the user. It also provides useful error codes for the user to easily interpret IPMI problems. &#8216;api&#8217; is used by most FreeIPMI tools and libraries, such as <code><a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8),</code> <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8),</code> and <code><a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3).</code></p>
<dt><code>cmds</code></p>
<dd> Provides fiid templates and &#8216;fill&#8217; functions for IPMI commands. Also provides macros definining common parameters for IPMI commands. The cmds are used by most other portions of libfreeipmi including the &#8216;api&#8217; sub-section and tools such as <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code></p>
<dt><code>debug</code></p>
<dd> Provides various packet/record dumping utility functions. Utilized by the &#8216;api&#8217; subsection and by tools such as <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code></p>
<dt><code>driver</code></p>
<dd> Provides APIs for in-band IPMI communication. Currently supported drivers are KCS, SSIF, and OpenIPMI. The &#8216;driver&#8217; subsction is used by tools such as <code><a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8)</code> and the &#8216;api&#8217; sub-section.</p>
<dt><code>fiid</code></p>
<dd> The &quot;FreeIPMI Interface Definition&quot; provides an API used for the construction/deconstruction of packets in libfreeipmi. The API works around fiid-templates, which are then used to create fiid-objects. Fiid-templates are used to describe packets through a string-name to bit-field mapping. The API allows users to read/write fields in an object using the string to bit-field mapping. Marshalling, packing, endian, and various other network issues are handled within &#8216;fiid&#8217;. Fiid objects are used throughout libfreeipmi, including the &#8216;api&#8217; sub-section, &#8216;cmds&#8217; sub-sections, and various tools.</p>
<dt><code>fru-parse</code></p>
<dd> Provides an API for parsing Field Replaceable Unit (FRU) records. Utilized by tools such as <a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8).</p>
<dt><code>interface</code></p>
<dd> Provides &#8216;assemble&#8217; and &#8216;disassemble&#8217; functions for building packets for individual in-band or out-of-band protocols. Also provides all necessary fiid templates, &#8216;fill&#8217; functions, and other utility functions necessary to communicate on an IPMI interface. Utilized by the &#8216;api&#8217; sub-section and tools such as <code><a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8) and</code> <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8).</code></p>
<dt><code>interpret</code></p>
<dd> Provides an API for interpreting sensor events by mapping them into Nominal, Warning, or Critical states. Utilized by FreeIPMI tools and libraries such as <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code> and <code><a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3).</code></p>
<dt><code>locate</code></p>
<dd> Provides an API to probe several standards to find default values for in-band IPMI communication. Utilized by the &#8216;api&#8217; sub-section and the <code><a href="/docs/linux/man/8-ipmi-locate/">ipmi-locate</a>(8)</code> tool.</p>
<dt><code>record-format</code></p>
<dd> Provides macros, fiid-templates, and information on records used in IPMI. Utilized by the &#8216;sdr-cache&#8217; subsection and tools like <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code></p>
<dt><code>sdr-cache</code></p>
<dd> Provides an API for creating, caching, reading, and parsing a sensor data repository (SDR). Utilized by tools such as <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code></p>
<dt><code>sdr-parse</code></p>
<dd> Provides an API for parsing SDR records. Utilized by tools such as <code><a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8)</code> and <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8)</code></p>
<dt><code>sel-parse</code></p>
<dd> Provides an API for reading and parsing System Event Log (SEL) entries. Utilized by tools such as <code><a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8).</code></p>
<dt><code>sensor-read</code></p>
<dd> Provides an API for reading a sensor. Utilized by tools such as <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code></p>
<dt><code>spec</code></p>
<dd> Provides macros and arrays for various other definitions and tables in IPMI. Utilized by tools such as <code><a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8).</code></p>
<dt><code>util</code></p>
<dd> Provides various utility functions for the calculation of keys, sensor readings, etc. Utilized by most of the rest of FreeIPMI.</dl>
<h2>FILES</h2>
<p> /usr/include/freeipmi.h </p>
<p> /usr/include/freeipmi/</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2012 FreeIPMI Core Team. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libipmiconsole/">libipmiconsole</a>(3), <a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3), <a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3), <a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-info/">bmc-info</a>(8), <a href="/docs/linux/man/8-bmc-watchdog/">bmc-watchdog</a>(8), <a href="/docs/linux/man/8-ipmi-chassis/">ipmi-chassis</a>(8), <a href="/docs/linux/man/8-ipmi-fru/">ipmi-fru</a>(8), <a href="/docs/linux/man/8-ipmi-locate/">ipmi-locate</a>(8), <a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8), <a href="/docs/linux/man/8-ipmi-raw/">ipmi-raw</a>(8), <a href="/docs/linux/man/8-ipmi-sel/">ipmi-sel</a>(8), <a href="/docs/linux/man/8-ipmi-sensors/">ipmi-sensors</a>(8), <a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8), <a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8), <a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8), <a href="/docs/linux/man/8-ipmiping/">ipmiping</a>(8), <a href="/docs/linux/man/8-ipmipower/">ipmipower</a>(8), <a href="/docs/linux/man/8-ipmi-pef-config/">ipmi-pef-config</a>(8), <a href="/docs/linux/man/8-rmcpping/">rmcpping</a>(8) </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
<h2>Index</h2>
