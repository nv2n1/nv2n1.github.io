---
title: "qmgr(8)"
name: "qmgr"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qmgr/"
description: "qmgr – Postfix queue manager"
---

<p>qmgr &#8211; Postfix queue manager</p>
<h2>Synopsis</h2>
<pre><code>qmgr</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon awaits the arrival of incoming mail and arranges for its delivery via Postfix delivery processes. The actual mail routing strategy is delegated to the <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> Mail addressed to the local <code>double-bounce</code> address is logged and discarded. This stops potential loops caused by undeliverable bounce notifications.</p>
<h2>Mail Queues</h2>
<p>The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon maintains the following queues:</p>
<dl>
<dt><code>incoming</code></p>
<dd>Inbound mail from the network, or mail picked up by the local <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) daemon from the <code>maildrop</code> directory.</p>
<dt><code>active</code></p>
<dd>Messages that the queue manager has opened for delivery. Only a limited number of messages is allowed to enter the <code>active</code> queue (leaky bucket strategy, for a fixed delivery rate).</p>
<dt><code>deferred</code></p>
<dd>Mail that could not be delivered upon the first attempt. The queue manager implements exponential backoff by doubling the time between delivery attempts.</p>
<dt><code>corrupt</code></p>
<dd>Unreadable or damaged queue files are moved here for inspection.</p>
<dt><code>hold</code></p>
<dd>Messages that are kept &quot;on hold&quot; are kept here until someone sets them free.</dl>
<h2>Delivery Status Reports</h2>
<p>The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon keeps an eye on per-message delivery status reports in the following directories. Each status report file has the same name as the corresponding message file:</p>
<dl>
<dt><code>bounce</code></p>
<dd>Per-recipient status information about why mail is bounced. These files are maintained by the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) daemon.</p>
<dt><code>defer</code></p>
<dd>Per-recipient status information about why mail is delayed. These files are maintained by the <code><a href="/docs/linux/man/8-defer/">defer</a></code>(8) daemon.</p>
<dt><code>trace</code></p>
<dd>Per-recipient status information as requested with the Postfix &quot;<code>sendmail -v</code>&quot; or &quot;<code>sendmail -bv</code>&quot; command. These files are maintained by the <code><a href="/docs/linux/man/8-trace/">trace</a></code>(8) daemon.</dl>
<p> The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon is responsible for asking the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8), <code><a href="/docs/linux/man/8-defer/">defer</a></code>(8) or <code><a href="/docs/linux/man/8-trace/">trace</a></code>(8) daemons to send delivery reports.</p>
<h2>Strategies</h2>
<p>The queue manager implements a variety of strategies for either opening queue files (input) or for message delivery (output).</p>
<dl>
<dt><code>leaky bucket</code></p>
<dd>This strategy limits the number of messages in the <code>active</code> queue and prevents the queue manager from running out of memory under heavy load.</p>
<dt><code>fairness</code></p>
<dd>When the <code>active</code> queue has room, the queue manager takes one message from the <code>incoming</code> queue and one from the <code>deferred</code> queue. This prevents a large mail backlog from blocking the delivery of new mail.</p>
<dt><code>slow start</code></p>
<dd>This strategy eliminates &quot;thundering herd&quot; problems by slowly adjusting the number of parallel deliveries to the same destination.</p>
<dt><code>round robin</code></p>
<dd>The queue manager sorts delivery requests by destination. Round-robin selection prevents one destination from dominating deliveries to other destinations.</p>
<dt><code>exponential backoff</code></p>
<dd>Mail that cannot be delivered upon the first attempt is deferred. The time interval between delivery attempts is doubled after each attempt.</p>
<dt><code>destination status cache</code></p>
<dd>The queue manager avoids unnecessary delivery attempts by maintaining a short-term, in-memory list of unreachable destinations.</p>
<dt><code>preemptive message scheduling</code></p>
<dd>The queue manager attempts to minimize the average per-recipient delay while still preserving the correct per-message delays, using a sophisticated preemptive message scheduling.</dl>
<h2>Triggers</h2>
<p>On an idle system, the queue manager waits for the arrival of trigger events, or it waits for a timer to go off. A trigger is a one-byte message. Depending on the message received, the queue manager performs one of the following actions (the message is followed by the symbolic constant used internally by the software):</p>
<dl>
<dt><code>D (QMGR_REQ_SCAN_DEFERRED)</code></p>
<dd>Start a deferred queue scan. If a deferred queue scan is already in progress, that scan will be restarted as soon as it finishes.</p>
<dt><code>I (QMGR_REQ_SCAN_INCOMING)</code></p>
<dd>Start an incoming queue scan. If an incoming queue scan is already in progress, that scan will be restarted as soon as it finishes.</p>
<dt><code>A (QMGR_REQ_SCAN_ALL)</code></p>
<dd>Ignore deferred queue file time stamps. The request affects the next deferred queue scan.</p>
<dt><code>F (QMGR_REQ_FLUSH_DEAD)</code></p>
<dd>Purge all information about dead transports and destinations.</p>
<dt><code>W (TRIGGER_REQ_WAKEUP)</code></p>
<dd>Wakeup call, This is used by the master server to instantiate servers that should not go away forever. The action is to start an incoming queue scan.</dl>
<p> The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon reads an entire buffer worth of triggers. Multiple identical trigger requests are collapsed into one, and trigger requests are sorted so that <code>A</code> and <code>F</code> precede <code>D</code> and <code>I</code>. Thus, in order to force a deferred queue run, one would request <code>A F D</code>; in order to notify the queue manager of the arrival of new mail one would request <code>I</code>.</p>
<h2>Standards</h2>
<pre>RFC 3463 (Enhanced status codes)
RFC 3464 (Delivery status notifications)</pre>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon is not security sensitive. It reads single-character messages from untrusted local users, and thus may be susceptible to denial of service attacks. The <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon does not talk to the outside world, and it can be run at fixed low privilege in a chrooted environment.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to the syslog daemon. Corrupted message files are saved to the <code>corrupt</code> queue for further inspection. </p>
<p> Depending on the setting of the <code>notify_classes</code> parameter, the postmaster is notified of bounces and of other trouble.</p>
<h2>Bugs</h2>
<p>A single queue manager process has to compete for disk access with multiple front-end processes such as <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8). A sudden burst of inbound mail can negatively impact outbound delivery rates.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are not picked up automatically as <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) is a persistent process. Use the &quot;<code>postfix reload</code>&quot; command after a configuration change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples. </p>
<p> In the text below, <i>transport</i> is the first field in a <code>master.cf</code> entry.</p>
<h2>Compatibility Controls</h2>
<p>Available before Postfix version 2.5:</p>
<dl>
<dt><code>allow_min_user (no)</code></p>
<dd>Allow a sender or recipient address to have `-&#8216; as the first character.</dl>
<p> Available with Postfix version 2.7 and later:</p>
<dl>
<dt><code>default_filter_nexthop (empty)</code></p>
<dd>When a content_filter or FILTER request specifies no explicit next-hop destination, use $default_filter_nexthop instead; when that value is empty, use the domain in the recipient address.</dl>
<h2>Active Queue Controls</h2>
<dl>
<dt><code>qmgr_clog_warn_time (300s)</code></p>
<dd>The minimal delay between warnings that a specific destination is clogging up the Postfix active queue.</p>
<dt><code>qmgr_message_active_limit (20000)</code></p>
<dd>The maximal number of messages in the active queue.</p>
<dt><code>qmgr_message_recipient_limit (20000)</code></p>
<dd>The maximal number of recipients held in memory by the Postfix queue manager, and the maximal size of the short-term, in-memory &quot;dead&quot; destination status cache.</p>
<dt><code>qmgr_message_recipient_minimum (10)</code></p>
<dd>The minimal number of in-memory recipients for any message.</p>
<dt><code>default_recipient_limit (20000)</code></p>
<dd>The default per-transport upper limit on the number of in-memory recipients.</p>
<dt><i>transport</i><code>_recipient_limit ($default_recipient_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_extra_recipient_limit (1000)</code></p>
<dd>The default value for the extra per-transport limit imposed on the number of in-memory recipients.</p>
<dt><i>transport</i><code>_extra_recipient_limit ($default_extra_recipient_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</dl>
<p> Available in Postfix version 2.4 and later:</p>
<dl>
<dt><code>default_recipient_refill_limit (100)</code></p>
<dd>The default per-transport limit on the number of recipients refilled at once.</p>
<dt><i>transport</i><code>_recipient_refill_limit ($default_recipient_refill_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_recipient_refill_delay (5s)</code></p>
<dd>The default per-transport maximum delay between recipients refills.</p>
<dt><i>transport</i><code>_recipient_refill_delay ($default_recipient_refill_delay)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</dl>
<h2>Delivery Concurrency Controls</h2>
<dl>
<dt><code>initial_destination_concurrency (5)</code></p>
<dd>The initial per-destination concurrency level for parallel delivery to the same destination.</p>
<dt><code>default_destination_concurrency_limit (20)</code></p>
<dd>The default maximal number of parallel deliveries to the same destination.</p>
<dt><i>transport</i><code>_destination_concurrency_limit ($default_destination_concurrency_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><i>transport</i><code>_initial_destination_concurrency ($initial_destination_concurrency)</code></p>
<dd>Initial concurrency for delivery via the named message <i>transport</i>.</p>
<dt><code>default_destination_concurrency_failed_cohort_limit (1)</code></p>
<dd>How many pseudo-cohorts must suffer connection or handshake failure before a specific destination is considered unavailable (and further delivery is suspended).</p>
<dt><i>transport</i><code>_destination_concurrency_failed_cohort_limit ($default_destination_concurrency_failed_cohort_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_destination_concurrency_negative_feedback (1)</code></p>
<dd>The per-destination amount of delivery concurrency negative feedback, after a delivery completes with a connection or handshake failure.</p>
<dt><i>transport</i><code>_destination_concurrency_negative_feedback ($default_destination_concurrency_negative_feedback)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_destination_concurrency_positive_feedback (1)</code></p>
<dd>The per-destination amount of delivery concurrency positive feedback, after a delivery completes without connection or handshake failure.</p>
<dt><i>transport</i><code>_destination_concurrency_positive_feedback ($default_destination_concurrency_positive_feedback)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>destination_concurrency_feedback_debug (no)</code></p>
<dd>Make the queue manager&#8217;s feedback algorithm verbose for performance analysis purposes.</dl>
<h2>Recipient Scheduling Controls</h2>
<dl>
<dt><code>default_destination_recipient_limit (50)</code></p>
<dd>The default maximal number of recipients per message delivery.</p>
<dt><i>transport</i><code>_destination_recipient_limit ($default_destination_recipient_limit)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</dl>
<h2>Message Scheduling Controls</h2>
<dl>
<dt><code>default_delivery_slot_cost (5)</code></p>
<dd>How often the Postfix queue manager&#8217;s scheduler is allowed to preempt delivery of one message with another.</p>
<dt><i>transport</i><code>_delivery_slot_cost ($default_delivery_slot_cost)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_minimum_delivery_slots (3)</code></p>
<dd>How many recipients a message must have in order to invoke the Postfix queue manager&#8217;s scheduling algorithm at all.</p>
<dt><i>transport</i><code>_minimum_delivery_slots ($default_minimum_delivery_slots)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_delivery_slot_discount (50)</code></p>
<dd>The default value for transport-specific _delivery_slot_discount settings.</p>
<dt><i>transport</i><code>_delivery_slot_discount ($default_delivery_slot_discount)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</p>
<dt><code>default_delivery_slot_loan (3)</code></p>
<dd>The default value for transport-specific _delivery_slot_loan settings.</p>
<dt><i>transport</i><code>_delivery_slot_loan ($default_delivery_slot_loan)</code></p>
<dd>Idem, for delivery via the named message <i>transport</i>.</dl>
<h2>Other Resource And Rate Controls</h2>
<dl>
<dt><code>minimal_backoff_time (300s)</code></p>
<dd>The minimal time between attempts to deliver a deferred message; prior to Postfix 2.4 the default value was 1000s.</p>
<dt><code>maximal_backoff_time (4000s)</code></p>
<dd>The maximal time between attempts to deliver a deferred message.</p>
<dt><code>maximal_queue_lifetime (5d)</code></p>
<dd>The maximal time a message is queued before it is sent back as undeliverable.</p>
<dt><code>queue_run_delay (300s)</code></p>
<dd>The time between deferred queue scans by the queue manager; prior to Postfix 2.4 the default value was 1000s.</p>
<dt><code>transport_retry_time (60s)</code></p>
<dd>The time between attempts by the Postfix queue manager to contact a malfunctioning message delivery transport.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>bounce_queue_lifetime (5d)</code></p>
<dd>The maximal time a bounce message is queued before it is considered undeliverable.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>default_destination_rate_delay (0s)</code></p>
<dd>The default amount of delay that is inserted between individual deliveries to the same destination; the resulting behavior depends on the value of the corresponding per-destination recipient limit.</p>
<dt><i>transport</i><code>_destination_rate_delay $default_destination_rate_delay</p>
<dd>Idem, for delivery via the named message </code><i>transport</i>.</dl>
<h2>Safety Controls</h2>
<dl>
<dt><code>qmgr_daemon_timeout (1000s)</code></p>
<dd>How much time a Postfix queue manager process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>qmgr_ipc_timeout (60s)</code></p>
<dd>The time limit for the queue manager to send or receive information over an internal communication channel.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>defer_transports (empty)</code></p>
<dd>The names of message delivery transports that should not deliver mail unless someone issues &quot;<code>sendmail -q</code>&quot; or equivalent.</p>
<dt><code>delay_logging_resolution_limit (2)</code></p>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</p>
<dt><code>helpful_warnings (yes)</code></p>
<dd>Log warnings about problematic configuration settings, and provide helpful suggestions.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>Files</h2>
<pre>/var/spool/postfix/incoming, incoming queue
/var/spool/postfix/active, active queue
/var/spool/postfix/deferred, deferred queue
/var/spool/postfix/bounce, non-delivery status
/var/spool/postfix/defer, non-delivery status
/var/spool/postfix/trace, delivery status</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), address routing
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), delivery status reports
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>SCHEDULER_README, scheduling algorithm
QSHAPE_README, Postfix queue analysis</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Preemptive scheduler enhancements:
Patrik Rak
Modra 6
155 00, Prague, Czech Republic</pre>
