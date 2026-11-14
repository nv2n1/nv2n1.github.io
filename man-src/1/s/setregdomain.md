---
title: "setregdomain(1)"
name: "setregdomain"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setregdomain/"
description: "setregdomain – set regulatory domain based on country code"
---

<h2>NAME</h2>
<p> setregdomain &#8211; set regulatory domain based on country code</p>
<h2>SYNOPSIS</h2>
<p> <code>setregdomain </code></p>
<h2>DESCRIPTION</h2>
<p> setregdomain sets the regulatory domain for your system; it takes no arguments and is normally called via system script (eg, udev) rather than manually by an administrator. </p>
<p> The regulatory domain is represented by an ISO / IEC 3166-1 alpha2 country code. By default, setregdomain attempts to determine the appropriate country code by examining the target of the <i>/etc/localtime</i> symbolic link. That information is used to look-up the matching country code in the <i>/usr/share/zoneinfo/zone.tab</i> file. </p>
<p> The country code look-up may fail. This could be due to faulty or incomplete information in the <i>/usr/share/zoneinfo/zone.tab</i> file, or the use of an actual file rather than a symlink for <i>/etc/localtime</i> , among other possibilities. In those cases the system administrator should define a COUNTRY environment variable in the <i>/etc/sysconfig/regdomain</i> file. This value will be used as the country code and the country code look-up will be skipped.</p>
<h2>FILES</h2>
<p> <code>/etc/sysconfig/regdomain</code> <code>/etc/localtime</code> <code>/usr/share/zoneinfo/zone.tab</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iw/">iw</a></code>(1) </p>
<h2>Index</h2>
