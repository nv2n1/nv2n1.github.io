---
title: "chrony(1)"
name: "chrony"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chrony/"
description: "chrony – programs for keeping computer clocks accurate"
---

<h2>NAME</h2>
<p> chrony &#8211; programs for keeping computer clocks accurate </p>
<h2>SYNOPSIS</h2>
<p> <code>chronyc</code> [<i>OPTIONS</i>] </p>
<p> <code>chronyd</code> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>chrony</code> is a pair of programs for keeping computer clocks accurate. <i>chronyd</i> is a background (daemon) program and <i>chronyc</i> is a command-line interface to it. Time reference sources for chronyd can be RFC1305 NTP servers, human (via keyboard and <i>chronyc</i>), or the computer&#8217;s real-time clock at boot time (Linux only). chronyd can determine the rate at which the computer gains or loses time and compensate for it while no external reference is present. Its use of NTP servers can be switched on and off (through <i>chronyc</i>) to support computers with dial-up/intermittent access to the Internet, and it can also act as an RFC1305-compatible NTP server. </p>
<h2>USAGE</h2>
<p> <i>chronyc</i> is a command-line interface program which can be used to monitor <i>chronyd</i>&#8216;s performance and to change various operating parameters whilst it is running. </p>
<p> <i>chronyd</i>&#8216;s main function is to obtain measurements of the true (UTC) time from one of several sources, and correct the system clock accordingly. It also works out the rate at which the system clock gains or loses time and uses this information to keep it accurate between measurements from the reference. </p>
<p> The reference time can be derived from either Network Time Protocol (NTP) servers, reference clocks, or wristwatch-and-keyboard (via <i>chronyc</i>). The main source of information about the Network Time Protocol is <i><a rel="nofollow" href="http://www.ntp.org">http://www.ntp.org</a></i>. </p>
<p> It is designed so that it can work on computers which only have intermittent access to reference sources, for example computers which use a dial-up account to access the Internet or laptops. Of course, it will work well on computers with permanent connections too. </p>
<p> In addition, on Linux it can monitor the system&#8217;s real time clock performance, so the system can maintain accurate time even across reboots. </p>
<p> Typical accuracies available between 2 machines are </p>
<p> On an ethernet LAN : 100-200 microseconds, often much better On a V32bis dial-up modem connection : 10&#8217;s of milliseconds (from one session to the next) </p>
<p> With a good reference clock the accuracy can reach one microsecond. </p>
<p> <i>chronyd</i> can also operate as an RFC1305-compatible NTP server and peer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chronyc/">chronyc</a>(1),</code> <code><a href="/docs/linux/man/5-chrony-conf/">chrony.conf</a>(5),</code> <code><a href="/docs/linux/man/8-chronyd/">chronyd</a>(8)</code> </p>
<p> <i><a rel="nofollow" href="http://chrony.tuxfamily.org/">http://chrony.tuxfamily.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> Richard Curnow &lt;rc [at] rc0.org.uk&gt; </p>
<p> This man-page was written by Jan Schaumann &lt;jschauma [at] netmeister.org&gt; as part of &quot;The Missing Man Pages Project&quot;. Please see <i><a rel="nofollow" href="http://www.netmeister.org/misc/m2p2/index.html">http://www.netmeister.org/misc/m2p2/index.html</a></i> for details. </p>
<p> The complete chrony documentation is supplied in texinfo format. </p>
<h2>Index</h2>
