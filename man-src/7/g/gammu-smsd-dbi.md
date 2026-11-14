---
title: "gammu-smsd-dbi(7)"
name: "gammu-smsd-dbi"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gammu-smsd-dbi/"
---

gammu-smsd-dbi - <a HREF="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) backend using DBI abstraction layer to use any supported database as a message storage 

<h2>Description</h2>

<a HREF="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) supports several backends. Actual backend is chosen in a config file <a HREF="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5). DBI backend stores all data in any database supported by libdbi, which parameters are defined by configuration (see <a HREF="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5) for description of configuration options). For tables description see <a HREF="/docs/linux/man/7-gammu-smsd-tables/">gammu-smsd-tables</a>(7). 

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a HREF="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5), <a HREF="/docs/linux/man/1-gammu/">gammu</a>(1), <a HREF="/docs/linux/man/5-gammurc/">gammurc</a>(5), <a HREF="/docs/linux/man/7-gammu-smsd-tables/">gammu-smsd-tables</a>(7)

<h2>Author</h2>

gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.

<h2>Copyright</h2>

Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" HREF="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt; 
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

<h2>Reporting Bugs</h2>

Please report bugs to &lt;<a rel="nofollow" HREF="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;.
