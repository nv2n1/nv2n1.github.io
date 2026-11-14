---
title: "wdmd(8)"
name: "wdmd"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wdmd/"
description: "wdmd – watchdog multiplexing daemon"
---

<p>wdmd &#8211; watchdog multiplexing daemon</p>
<h2>Synopsis</h2>
<p><code>wdmd</code> [OPTIONS] </p>
<h2>Description</h2>
<p>This daemon opens /dev/watchdog and allows multiple independent sources to detmermine whether each KEEPALIVE is done. Every test interval (10 seconds), the daemon tests each source. If any test fails, the KEEPALIVE is not done. In a standard configuration, the watchdog timer will reset the system if no KEEPALIVE is done for 60 seconds (&quot;fire timeout&quot;). This means that if a single test fails 5-6 times in row, the watchdog will fire and reset the system. With multiple test sources, fewer separate failures back to back can also cause a reset, e.g. T seconds, P pass, F fail<br />
 T00: test1 P, test2 P, test3 P: KEEPALIVE done<br />
 T10: test1 F, test2 F, test3 P: KEEPALIVE skipped<br />
 T20: test1 F, test2 P, test3 P: KEEPALIVE skipped<br />
 T30: test1 P, test2 F, test3 P: KEEPALIVE skipped<br />
 T40: test1 P, test2 P, test3 F: KEEPALIVE skipped<br />
 T50: test1 F, test2 F, test3 P: KEEPALIVE skipped<br />
 T60: test1 P, test2 F, test3 P: KEEPALIVE skipped<br />
 T60: watchdog fires, system resets (Depending on timings, the system may be reset sometime shortly before T60, and the tests at T60 would not be run.) A crucial aspect to the design and function of wdmd is that if any single source does not pass tests for the fire timeout, the watchdog is guaranteed to fire, regardless of whether other sources on the system have passed or failed. A spurious reset due to the combined effects of multiple failing tests as shown above, is an accepted side effect. The wdmd init script will load the softdog module if no other watchdog module has been loaded. wdmd cannot be used on the system with any other program that needs to open /dev/watchdog, e.g. <a href="/docs/linux/man/8-watchdog/">watchdog</a>(8).</p>
<h3>Test Source: clients</h3>
<p>Using libwdmd, programs connect to wdmd via a unix socket, and send regular messages to wdmd to update an expiry time for their connection. Every test interval, wdmd will check if the expiry time for a connection has been reached. If so, the test for that client fails.</p>
<h3>Test Source: scripts</h3>
<p>wdmd will run scripts from a designated directory every test interval. If a script exits with 0, the test is considered a success, otherwise a failure. If a script does not exit by the end of the test interval, it is considered a failure. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version, -V</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Print version. </p>
<dt><code>&#8211;help, -h</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Print usage. </p>
<dt><code>&#8211;dump, -d</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Print debug information from the daemon. </p>
<dt><code>&#8211;probe, -p</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Print path of functional watchdog device.&nbsp;<wbr>&nbsp;<wbr>Exit code 0 indicates a<br />
&nbsp;<wbr>&nbsp;<wbr>functional device was found.&nbsp;<wbr>&nbsp;<wbr>Exit code 1 indicates a functional device<br />
&nbsp;<wbr>&nbsp;<wbr>was not found. </p>
<dt><code>-D</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Enable debugging to stderr and don&#8217;t fork. </p>
<dt><code>-H</code><i> 0|1</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Enable&nbsp;<wbr>(1)&nbsp;<wbr>or disable&nbsp;<wbr>(0)&nbsp;<wbr>high priority features such as realtime<br />
&nbsp;<wbr>&nbsp;<wbr>scheduling priority and mlockall. </p>
<dt><code>-G</code><i> name</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Group ownership for the socket. </p>
<dt><code>-S</code><i> 0|1</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Enable&nbsp;<wbr>(1)&nbsp;<wbr>or disable&nbsp;<wbr>(0)&nbsp;<wbr>script tests. </p>
<dt><code>-s</code><i> path</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Path to scripts dir. </p>
<dt><code>-k</code><i> num</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>Kill unfinished scripts after num seconds. </p>
<dt><code>-w</code><i> path</i></p>
<dd>&nbsp;<wbr>&nbsp;<wbr>The path to the watchdog device to try first. </p>
</dl>
