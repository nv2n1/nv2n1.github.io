---
title: "tlsmgr(8)"
name: "tlsmgr"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tlsmgr/"
description: "tlsmgr – Postfix TLS session cache and PRNG manager"
---

<p>tlsmgr &#8211; Postfix TLS session cache and PRNG manager</p>
<h2>Synopsis</h2>
<pre><code>tlsmgr</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) manages the Postfix TLS session caches. It stores and retrieves cache entries on request by <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) and <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) processes, and periodically removes entries that have expired. </p>
<p> The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) also manages the PRNG (pseudo random number generator) pool. It answers queries by the <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) and <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) processes to seed their internal PRNG pools. </p>
<p> The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8)&#8217;s PRNG pool is initially seeded from an external source (EGD, /dev/urandom, or regular file). It is updated at configurable pseudo-random intervals with data from the external source. It is updated periodically with data from TLS session cache entries and with the time of day, and is updated with the time of day whenever a process requests <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) service. </p>
<p> The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) saves the PRNG state to an exchange file periodically and when the process terminates, and reads the exchange file when initializing its PRNG.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) is not security-sensitive. The code that maintains the external and internal PRNG pools does not &quot;trust&quot; the data that it manipulates, and the code that maintains the TLS session cache does not touch the contents of the cached entries, except for seeding its internal PRNG pool. </p>
<p> The <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) can be run chrooted and with reduced privileges. At process startup it connects to the entropy source and exchange file, and creates or truncates the optional TLS session cache files. </p>
<p> With Postfix version 2.5 and later, the <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) no longer uses root privileges when opening cache files. These files should now be stored under the Postfix-owned <code>data_directory</code>. As a migration aid, an attempt to open a cache file under a non-Postfix directory is redirected to the Postfix-owned <code>data_directory</code>, and a warning is logged.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to the syslog daemon.</p>
<h2>Bugs</h2>
<p>There is no automatic means to limit the number of entries in the TLS session caches and/or the size of the TLS cache files.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are not picked up automatically, because <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) is a persistent processes. Use the command &quot;<code>postfix reload</code>&quot; after a configuration change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Tls Session Cache</h2>
<dl>
<dt><code>lmtp_tls_loglevel (0)</code></p>
<dd>The LMTP-specific version of the smtp_tls_loglevel configuration parameter.</p>
<dt><code>lmtp_tls_session_cache_database (empty)</code></p>
<dd>The LMTP-specific version of the smtp_tls_session_cache_database configuration parameter.</p>
<dt><code>lmtp_tls_session_cache_timeout (3600s)</code></p>
<dd>The LMTP-specific version of the smtp_tls_session_cache_timeout configuration parameter.</p>
<dt><code>smtp_tls_loglevel (0)</code></p>
<dd>Enable additional Postfix SMTP client logging of TLS activity.</p>
<dt><code>smtp_tls_session_cache_database (empty)</code></p>
<dd>Name of the file containing the optional Postfix SMTP client TLS session cache.</p>
<dt><code>smtp_tls_session_cache_timeout (3600s)</code></p>
<dd>The expiration time of Postfix SMTP client TLS session cache information.</p>
<dt><code>smtpd_tls_loglevel (0)</code></p>
<dd>Enable additional Postfix SMTP server logging of TLS activity.</p>
<dt><code>smtpd_tls_session_cache_database (empty)</code></p>
<dd>Name of the file containing the optional Postfix SMTP server TLS session cache.</p>
<dt><code>smtpd_tls_session_cache_timeout (3600s)</code></p>
<dd>The expiration time of Postfix SMTP server TLS session cache information.</dl>
<h2>Pseudo Random Number Generator</h2>
<dl>
<dt><code>tls_random_source (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The external entropy source for the in-memory <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) pseudo random number generator (PRNG) pool.</p>
<dt><code>tls_random_bytes (32)</code></p>
<dd>The number of bytes that <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) reads from $tls_random_source when (re)seeding the in-memory pseudo random number generator (PRNG) pool.</p>
<dt><code>tls_random_exchange_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Name of the pseudo random number generator (PRNG) state file that is maintained by <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8).</p>
<dt><code>tls_random_prng_update_period (3600s)</code></p>
<dd>The time between attempts by <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) to save the state of the pseudo random number generator (PRNG) to the file specified with $tls_random_exchange_name.</p>
<dt><code>tls_random_reseed_period (3600s)</code></p>
<dd>The maximal time between attempts by <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) to re-seed the in-memory pseudo random number generator (PRNG) pool from external sources.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>data_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory with Postfix-writable data files (for example: caches, pseudo-random numbers).</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtp/">smtp</a>(8), Postfix SMTP client
<a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>TLS_README, Postfix TLS configuration and operation</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Lutz Jaenicke
BTU Cottbus
Allgemeine Elektrotechnik
Universitaetsplatz 3-4
D-03044 Cottbus, Germany
Adapted by:
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
