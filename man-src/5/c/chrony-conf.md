---
title: "chrony-conf(5)"
name: "chrony-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-chrony-conf/"
description: "chrony.conf – chronyd configuration file"
---

<p>chrony.conf &#8211; chronyd configuration file</p>
<h2>Synopsis</h2>
<p><code>chrony.conf</code></p>
<h2>Description</h2>
<p>This file configures the <code>chronyd</code> daemon. The compiled-in location is <i>/etc/chrony.conf</i>, but other locations can be specified on the <code>chronyd</code> command line with the <code>-f</code> option. </p>
<p> Each directive in the configuration file is placed on a separate line. The following sections describe each of the directives in turn. The directives can occur in any order in the file and they are not case-sensitive. </p>
<p> The configuration directives can also be specified directly on the <code>chronyd</code> command line. In this case each argument is parsed as a new line and the configuration file is ignored. </p>
<p> While the number of supported directives is large, only a few of them are typically needed. See the <code>EXAMPLES</code> section for configuration in typical operating scenarios. </p>
<p> The configuration file might contain comment lines. A comment line is any line that starts with zero or more spaces followed by any one of the following characters: <code>!</code>, <code>;</code>, <code>#</code>, <code>%</code>. Any line with this format will be ignored.</p>
<h2>Directives</h2>
<h3>Time sources</h3>
<p><code>server</code> <i>hostname</i> [<i>option</i>]&#8230;</p>
<dl>
<dd>The <code>server</code> directive specifies an NTP server which can be used as a time source. The client-server relationship is strictly hierarchical: a client might synchronise its system time to that of the server, but the server&#8217;s system time will never be influenced by that of a client. </p>
<p> The <code>server</code> directive is immediately followed by either the name of the server, or its IP address. The <code>server</code> directive supports the following options: </p>
<p> <code>minpoll</code> <i>poll</i></p>
<dl>
<dd>Although <code>chronyd</code> will trim the rate at which it samples the server during normal operation, the user might want to constrain the minimum polling interval. This is always defined as a power of 2, so <code>minpoll 5</code> would mean that the polling interval cannot drop below 32 seconds. The default is 6 (64 seconds), the minimum is -4 (1/16th of a second), and the maximum is 24 (6 months). Note that intervals shorter than 6 (64 seconds) should generally not be used with public servers on the Internet, because it might be considered abuse.</dl>
<p> <code>maxpoll</code> <i>poll</i></p>
<dl>
<dd>In a similar way, the user might want to constrain the maximum polling interval. Again this is specified as a power of 2, <code>maxpoll 9</code> indicates that the polling interval must stay at or below 512 seconds. The default is 10 (1024 seconds), the minimum is 0 (1 second), and the maximum is 24 (6 months).</dl>
<p> <code>iburst</code></p>
<dl>
<dd>If this option is set, the interval between the first four polls will be 2 seconds instead of <i>minpoll</i>. This is useful to quickly get the first update of the clock after <code>chronyd</code> is started.</dl>
<p> <code>key</code> <i>id</i></p>
<dl>
<dd>The NTP protocol supports the inclusion of checksums in the packets, to prevent computers having their system time upset by rogue packets being sent to them. The checksums are generated as a function of a password, using the cryptographic hash function set in the key file, which is specified by the <code>keyfile</code> directive. </p>
<p> If the key option is present, <code>chronyd</code> will attempt to use authenticated packets when communicating with this server. The key number used will be the single argument to the key option (an unsigned integer in the range 1 through 2^32-1). The server must have the same password for this key number configured, otherwise no relationship between the computers will be possible.</dl>
<p> <code>maxdelay</code> <i>delay</i></p>
<dl>
<dd><code>chronyd</code> uses the network round-trip delay to the server to determine how accurate a particular measurement is likely to be. Long round-trip delays indicate that the request, or the response, or both were delayed. If only one of the messages was delayed the measurement error is likely to be substantial. </p>
<p> For small variations in the round-trip delay, <code>chronyd</code> uses a weighting scheme when processing the measurements. However, beyond a certain level of delay the measurements are likely to be so corrupted as to be useless. (This is particularly so on dial-up or other slow links, where a long delay probably indicates a highly asymmetric delay caused by the response waiting behind a lot of packets related to a download of some sort). </p>
<p> If the user knows that round trip delays above a certain level should cause the measurement to be ignored, this level can be defined with the <code>maxdelay</code> option. For example, <code>maxdelay 0.3</code> would indicate that measurements with a round-trip delay of 0.3 seconds or more should be ignored. The default value is 3 seconds and the maximum value is 1000 seconds.</dl>
<p> <code>maxdelayratio</code> <i>ratio</i></p>
<dl>
<dd>This option is similar to the maxdelay option above. <code>chronyd</code> keeps a record of the minimum round-trip delay amongst the previous measurements that it has buffered. If a measurement has a round trip delay that is greater than the maxdelayratio times the minimum delay, it will be rejected. This option works only in the <code>server</code> directive when not in the interleaved mode.</dl>
<p> <code>maxdelaydevratio</code> <i>ratio</i></p>
<dl>
<dd>If a measurement has a ratio of the increase in the round-trip delay from the minimum delay amongst the previous measurements to the standard deviation of the previous measurements that is greater than the specified ratio, it will be rejected. The default is 10.0.</dl>
<p> <code>offset</code> <i>offset</i></p>
<dl>
<dd>This option specifies a correction (in seconds) which will be applied to offsets measured with this source. It&#8217;s particularly useful to compensate for a known asymmetry in network delay or timestamping errors. For example, if packets sent to the source were on average delayed by 100 microseconds more than packets sent from the source back, the correction would be -0.00005 (-50 microseconds). The default is 0.0.</dl>
<p> <code>minsamples</code> <i>samples</i></p>
<dl>
<dd>Set the minimum number of samples kept for this source. This overrides the <code>minsamples</code> directive.</dl>
<p> <code>maxsamples</code> <i>samples</i></p>
<dl>
<dd>Set the maximum number of samples kept for this source. This overrides the <code>maxsamples</code> directive.</dl>
<p> <code>offline</code></p>
<dl>
<dd>If the server will not be reachable when <code>chronyd</code> is started, the <code>offline</code> option can be specified. <code>chronyd</code> will not try to poll the server until it is enabled to do so (by using the <code>online</code> command in <code>chronyc</code>).</dl>
<p> <code>auto_offline</code></p>
<dl>
<dd>If this option is set, the server will be assumed to have gone offline when 2 requests have been sent to it without receiving a response. This option avoids the need to run the <code>offline</code> command from <code>chronyc</code> when disconnecting the network link. (It will still be necessary to use the <code>online</code> command when the link has been established, to enable measurements to start.)</dl>
<p> <code>prefer</code></p>
<dl>
<dd>Prefer this source over sources without prefer option.</dl>
<p> <code>noselect</code></p>
<dl>
<dd>Never select this source. This is particularly useful for monitoring.</dl>
<p> <code>trust</code></p>
<dl>
<dd>Assume time from this source is always true. It can be rejected as a falseticker in the source selection only if another source with this option does not agree with it.</dl>
<p> <code>require</code></p>
<dl>
<dd>Require that at least one of the sources specified with this option is selectable (i.e. recently reachable and not a falseticker) before updating the clock. Together with the <code>trust</code> option this might be useful to allow a trusted authenticated source to be safely combined with unauthenticated sources in order to improve the accuracy of the clock. They can be selected and used for synchronisation only if they agree with the trusted and required source.</dl>
<p> <code>xleave</code></p>
<dl>
<dd>This option enables an interleaved mode which allows the server or the peer to send transmit timestamps captured after the actual transmission (e.g. when the server or the peer is running <code>chronyd</code> with software (kernel) or hardware timestamping). This can significantly improve the accuracy of the measurements. </p>
<p> The interleaved mode is compatible with servers that support only the basic mode, but peers must both support and have enabled the interleaved mode, otherwise the synchronisation will work only in one direction. Note that even servers that support the interleaved mode might respond in the basic mode as the interleaved mode requires the servers to keep some state for each client and the state might be dropped when there are too many clients (e.g. <code>clientloglimit</code> is too small), or it might be overwritten by other clients that have the same IP address (e.g. computers behind NAT or someone sending requests with a spoofed source address). </p>
<p> With longer polling intervals, it is recommended to combine the <code>xleave</code> option with the <code>presend</code> option in order to shorten the interval in which the server has to keep the state to be able to respond in the interleaved mode. The shorter interval also improves accuracy of the measured offset and delay.</dl>
<p> <code>polltarget</code> <i>target</i></p>
<dl>
<dd>Target number of measurements to use for the regression algorithm which <code>chronyd</code> will try to maintain by adjusting the polling interval between <code>minpoll</code> and <code>maxpoll</code>. A higher target makes <code>chronyd</code> prefer shorter polling intervals. The default is 8 and a useful range is from 6 to 60.</dl>
<p> <code>port</code> <i>port</i></p>
<dl>
<dd>This option allows the UDP port on which the server understands NTP requests to be specified. For normal servers this option should not be required (the default is 123, the standard NTP port).</dl>
<p> <code>presend</code> <i>poll</i></p>
<dl>
<dd>If the timing measurements being made by <code>chronyd</code> are the only network data passing between two computers, you might find that some measurements are badly skewed due to either the client or the server having to do an ARP lookup on the other party prior to transmitting a packet. This is more of a problem with long sampling intervals, which might be similar in duration to the lifetime of entries in the ARP caches of the machines. </p>
<p> In order to avoid this problem, the <code>presend</code> option can be used. It takes a single integer argument, which is the smallest polling interval for which an extra pair of NTP packets will be exchanged between the client and the server prior to the actual measurement. For example, with the following option included in a <code>server</code> directive: </p>
<dl>
<dd>
<pre>presend 9</pre>
</dl>
<p> when the polling interval is 512 seconds or more, an extra NTP client packet will be sent to the server a short time (2 seconds) before making the actual measurement. </p>
<p> The <code>presend</code> option cannot be used in the <code>peer</code> directive. If it is used with the <code>xleave</code> option, <code>chronyd</code> will send two extra packets instead of one.</dl>
<p> <code>minstratum</code> <i>stratum</i></p>
<dl>
<dd>When the synchronisation source is selected from available sources, sources with lower stratum are normally slightly preferred. This option can be used to increase stratum of the source to the specified minimum, so <code>chronyd</code> will avoid selecting that source. This is useful with low stratum sources that are known to be unreliable or inaccurate and which should be used only when other sources are unreachable.</dl>
<p> <code>version</code> <i>version</i></p>
<dl>
<dd>This option sets the NTP version of packets sent to the server. This can be useful when the server runs an old NTP implementation that does not respond to requests using a newer version. The default version depends on whether a key is specified by the <code>key</code> option and which authentication hash function the key is using. If the output size of the hash function is longer than 160 bits, the default version is 3 for compatibility with older <code>chronyd</code> servers. Otherwise, the default version is 4.</dl>
</dl>
<p> <code>pool</code> <i>name</i> [<i>option</i>]&#8230;</p>
<dl>
<dd>The syntax of this directive is similar to that for the <code>server</code> directive, except that it is used to specify a pool of NTP servers rather than a single NTP server. The pool name is expected to resolve to multiple addresses which might change over time. </p>
<p> All options valid in the <code>server</code> directive can be used in this directive too. There is one option specific to the <code>pool</code> directive: <code>maxsources</code> sets the maximum number of sources that can be used from the pool, the default value is 4. </p>
<p> On start, when the pool name is resolved, <code>chronyd</code> will add up to 16 sources, one for each resolved address. When the number of sources from which at least one valid reply was received reaches the number specified by the <code>maxsources</code> option, the other sources will be removed. When a pool source is unreachable, marked as a falseticker, or has a distance larger than the limit set by the <code>maxdistance</code> directive, <code>chronyd</code> will try to replace the source with a newly resolved address from the pool. </p>
<p> An example of the <code>pool</code> directive is </p>
<dl>
<dd>
<pre>pool pool.ntp.org iburst maxsources 3</pre>
</dl>
</dl>
<p> <code>peer</code> <i>hostname</i> [<i>option</i>]&#8230;</p>
<dl>
<dd>The syntax of this directive is identical to that for the <code>server</code> directive, except that it specifies a symmetric association with an NTP peer instead of a client/server association with an NTP server. A single symmetric association allows the peers to be both servers and clients to each other. This is mainly useful when the NTP implementation of the peer (e.g. <code>ntpd</code>) supports ephemeral symmetric associations and does not need to be configured with an address of this host. <code>chronyd</code> does not support ephemeral associations. </p>
<p> When a key is specified by the <code>key</code> option to enable authentication, both peers must use the same key and the same key number. </p>
<p> Note that the symmetric mode is less secure than the client/server mode. A denial-of-service attack is possible on unauthenticated symmetric associations, i.e. when the peer was specified without the <code>key</code> option. An attacker who does not see network traffic between two hosts, but knows that they are peering with each other, can periodically send them unauthenticated packets with spoofed source addresses in order to disrupt their NTP state and prevent them from synchronising to each other. When the association is authenticated, an attacker who does see the network traffic, but cannot prevent the packets from reaching the other host, can still disrupt the state by replaying old packets. The attacker has effectively the same power as a man-in-the-middle attacker. A partial protection against this attack is implemented in <code>chronyd</code>, which can protect the peers if they are using the same polling interval and they never sent an authenticated packet with a timestamp from future, but it should not be relied on as it is difficult to ensure the conditions are met. If two hosts should be able to synchronise to each other in both directions, it is recommended to use two separate client/server associations (specified by the <code>server</code> directive on both hosts) instead.</dl>
<p> <code>initstepslew</code> <i>step-threshold</i> [<i>hostname</i>]&#8230;</p>
<dl>
<dd>In normal operation, <code>chronyd</code> slews the time when it needs to adjust the system clock. For example, to correct a system clock which is 1 second slow, <code>chronyd</code> slightly increases the amount by which the system clock is advanced on each clock interrupt, until the error is removed. Note that at no time does time run backwards with this method. </p>
<p> On most Unix systems it is not desirable to step the system clock, because many programs rely on time advancing monotonically forwards. </p>
<p> When the <code>chronyd</code> daemon is initially started, it is possible that the system clock is considerably in error. Attempting to correct such an error by slewing might not be sensible, since it might take several hours to correct the error by this means. </p>
<p> The purpose of the <code>initstepslew</code> directive is to allow <code>chronyd</code> to make a rapid measurement of the system clock error at boot time, and to correct the system clock by stepping before normal operation begins. Since this would normally be performed only at an appropriate point in the system boot sequence, no other software should be adversely affected by the step. </p>
<p> If the correction required is less than a specified threshold, a slew is used instead. This makes it safer to restart <code>chronyd</code> whilst the system is in normal operation. </p>
<p> The <code>initstepslew</code> directive takes a threshold and a list of NTP servers as arguments. Each of the servers is rapidly polled several times, and a majority voting mechanism used to find the most likely range of system clock error that is present. A step or slew is applied to the system clock to correct this error. <code>chronyd</code> then enters its normal operating mode. </p>
<p> An example of the use of the directive is: </p>
<dl>
<dd>
<pre>initstepslew 30 foo.example.net bar.example.net</pre>
</dl>
<p> where 2 NTP servers are used to make the measurement. The <i>30</i> indicates that if the system&#8217;s error is found to be 30 seconds or less, a slew will be used to correct it; if the error is above 30 seconds, a step will be used. </p>
<p> The <code>initstepslew</code> directive can also be used in an isolated LAN environment, where the clocks are set manually. The most stable computer is chosen as the master, and the other computers are slaved to it. If each of the slaves is configured with the <code>local</code> directive, the master can be set up with an <code>initstepslew</code> directive which references some or all of the slaves. Then, if the master machine has to be rebooted, the slaves can be relied on to act analogously to a flywheel and preserve the time for a short period while the master completes its reboot. </p>
<p> The <code>initstepslew</code> directive is functionally similar to a combination of the <code>makestep</code> and <code>server</code> directives with the <code>iburst</code> option. The main difference is that the <code>initstepslew</code> servers are used only before normal operation begins and that the foreground <code>chronyd</code> process waits for <code>initstepslew</code> to finish before exiting. This is useful to prevent programs started in the boot sequence after <code>chronyd</code> from reading the clock before it has been stepped.</dl>
<p> <code>refclock</code> <i>driver</i> <i>parameter</i> [<i>option</i>]&#8230;</p>
<dl>
<dd>The <code>refclock</code> directive specifies a hardware reference clock to be used as a time source. It has two mandatory parameters, a driver name and a driver-specific parameter. </p>
<p> There are currently four drivers included: </p>
<p> <code>PPS</code></p>
<dl>
<dd>Driver for the kernel PPS (pulse per second) API. The parameter is the path to the PPS device (typically <i>/dev/pps?</i>). The assert events are used for synchronisation by default. String <code>:clear</code> can be appended to the path to use the clear events instead. </p>
<p> As PPS refclocks don&#8217;t supply full time, <code>chronyd</code> needs to be configured with another time source (NTP or non-PPS refclock) in order to complete samples from the PPS refclock. An alternative is to enable the <code>local</code> directive to allow synchronisation with some unknown but constant offset. For example: </p>
<dl>
<dd>
<pre>refclock PPS /dev/pps0 lock NMEA
refclock SHM 0 offset 0.5 delay 0.2 refid NMEA noselect</pre>
</dl>
</dl>
<p> <code>SHM</code></p>
<dl>
<dd>NTP shared memory driver. This driver uses a shared memory segment to receive samples from another process. The parameter is the number of the shared memory segment, typically 0, 1, 2 or 3. For example: </p>
<dl>
<dd>
<pre>refclock SHM 1 poll 3 refid GPS1</pre>
</dl>
<p> A driver option in form of <code>:perm=NNN</code> can be appended to the segment number to create the segment with permissions other than the default 0600. </p>
<p> Examples of applications that can be used as SHM refclocks are <code>gpsd</code> &lt;URL: <a rel="nofollow" href="http://www.catb.org/gpsd/">http://www.catb.org/gpsd/</a> &gt;, <code>radioclk</code> &lt;URL: <a rel="nofollow" href="http://www.buzzard.me.uk/jonathan/radioclock.html">http://www.buzzard.me.uk/jonathan/radioclock.html</a> &gt;, and <code>omnisync</code> &lt;URL: <a rel="nofollow" href="https://www.vanheusden.com/time/omnisync/">https://www.vanheusden.com/time/omnisync/</a> &gt;.</dl>
<p> <code>SOCK</code></p>
<dl>
<dd>Unix domain socket driver. It is similar to the SHM driver, but samples are received from a Unix domain socket instead of shared memory and the messages have a different format. The parameter is the path to the socket, which <code>chronyd</code> creates on start. An advantage over the SHM driver is that SOCK does not require polling and it can receive PPS samples with incomplete time. The format of the messages is described in the <i>refclock_sock.c</i> file in the chrony source code. </p>
<p> An application which supports the SOCK protocol is the <code>gpsd</code> daemon. The path where <code>gpsd</code> expects the socket to be created is described in the <code><a href="/docs/linux/man/8-gpsd/">gpsd</a>(8)</code> man page. For example: </p>
<dl>
<dd>
<pre>refclock SOCK /var/run/chrony.ttyS0.sock</pre>
</dl>
</dl>
<p> <code>PHC</code></p>
<dl>
<dd>PTP hardware clock (PHC) driver. The parameter is the path to the device of the PTP clock, which for example can be synchronised by <code>ptp4l</code> from <code>linuxptp</code> &lt;URL: <a rel="nofollow" href="http://linuxptp.sourceforge.net">http://linuxptp.sourceforge.net</a> &gt;. String <code>:nocrossts</code> can be appended to the path to disable use of precise cross timestamping. PTP clocks are typically kept in TAI instead of UTC, so the <code>offset</code> option should be used to compensate for the current UTC-TAI offset. For example: </p>
<dl>
<dd>
<pre>refclock PHC /dev/ptp0 poll 3 dpoll -2 offset -36</pre>
</dl>
</dl>
</dl>
<dl>
<dd>The <code>refclock</code> directive also supports a number of options: </p>
<p> <code>poll</code> <i>poll</i></p>
<dl>
<dd>Timestamps produced by refclock drivers are not used immediately, but they are stored and processed by a median filter in the polling interval specified by this option. This is defined as a power of 2 and can be negative to specify a sub-second interval. The default is 4 (16 seconds). A shorter interval allows <code>chronyd</code> to react faster to changes in the frequency of the system clock, but it might have a negative effect on its accuracy if the samples have a lot of jitter.</dl>
<p> <code>dpoll</code> <i>dpoll</i></p>
<dl>
<dd>Some drivers do not listen for external events and try to produce samples in their own polling interval. This is defined as a power of 2 and can be negative to specify a sub-second interval. The default is 0 (1 second).</dl>
<p> <code>refid</code> <i>refid</i></p>
<dl>
<dd>This option is used to specify the reference ID of the refclock, as up to four ASCII characters. The default reference ID is composed from the first three characters of the driver name and the number of the refclock. Each refclock must have a unique reference ID.</dl>
<p> <code>lock</code> <i>refid</i></p>
<dl>
<dd>This option can be used to lock a PPS refclock to another refclock, which is specified by its reference ID. In this mode received PPS samples are paired directly with raw samples from the specified refclock.</dl>
<p> <code>rate</code> <i>rate</i></p>
<dl>
<dd>This option sets the rate of the pulses in the PPS signal (in Hz). This option controls how the pulses will be completed with real time. To actually receive more than one pulse per second, a negative <code>dpoll</code> has to be specified (-3 for a 5Hz signal). The default is 1.</dl>
<p> <code>maxlockage</code> <i>pulses</i></p>
<dl>
<dd>This option specifies in number of pulses how old can be samples from the refclock specified by the <code>lock</code> option to be paired with the pulses. Increasing this value is useful when the samples are produced at a lower rate than the pulses. The default is 2.</dl>
<p> <code>offset</code> <i>offset</i></p>
<dl>
<dd>This option can be used to compensate for a constant error. The specified offset (in seconds) is applied to all samples produced by the reference clock. The default is 0.0.</dl>
<p> <code>delay</code> <i>delay</i></p>
<dl>
<dd>This option sets the NTP delay of the source (in seconds). Half of this value is included in the maximum assumed error which is used in the source selection algorithm. Increasing the delay is useful to avoid having no majority in the source selection or to make it prefer other sources. The default is 1e-9 (1 nanosecond).</dl>
<p> <code>precision</code> <i>precision</i></p>
<dl>
<dd>This option sets the refclock precision (in seconds). The default is 1e-6 (1 microsecond) for SHM refclock, and 1e-9 (1 nanosecond) for SOCK, PPS and PHC refclocks.</dl>
<p> <code>maxdispersion</code> <i>dispersion</i></p>
<dl>
<dd>Maximum allowed dispersion for filtered samples (in seconds). Samples with larger estimated dispersion are ignored. By default, this limit is disabled.</dl>
<p> <code>filter</code> <i>samples</i></p>
<dl>
<dd>This option sets the length of the median filter which is used to reduce the noise in the measurements. With each poll about 40 percent of the stored samples are discarded and one final sample is calculated as an average of the remaining samples. If the length is 4 or more, at least 4 samples have to be collected between polls. For lengths below 4, the filter has to be full. The default is 64.</dl>
<p> <code>prefer</code></p>
<dl>
<dd>Prefer this source over sources without the prefer option.</dl>
<p> <code>noselect</code></p>
<dl>
<dd>Never select this source. This is useful for monitoring or with sources which are not very accurate, but are locked with a PPS refclock.</dl>
<p> <code>trust</code></p>
<dl>
<dd>Assume time from this source is always true. It can be rejected as a falseticker in the source selection only if another source with this option does not agree with it.</dl>
<p> <code>require</code></p>
<dl>
<dd>Require that at least one of the sources specified with this option is selectable (i.e. recently reachable and not a falseticker) before updating the clock. Together with the <code>trust</code> option this can be useful to allow a trusted, but not very precise, reference clock to be safely combined with unauthenticated NTP sources in order to improve the accuracy of the clock. They can be selected and used for synchronisation only if they agree with the trusted and required source.</dl>
<p> <code>minsamples</code> <i>samples</i></p>
<dl>
<dd>Set the minimum number of samples kept for this source. This overrides the <code>minsamples</code> directive.</dl>
<p> <code>maxsamples</code> <i>samples</i></p>
<dl>
<dd>Set the maximum number of samples kept for this source. This overrides the <code>maxsamples</code> directive.</dl>
</dl>
<p> <code>manual</code></p>
<dl>
<dd>The <code>manual</code> directive enables support at run-time for the <code>settime</code> command in <code>chronyc</code>. If no <code>manual</code> directive is included, any attempt to use the <code>settime</code> command in <code>chronyc</code> will be met with an error message. </p>
<p> Note that the <code>settime</code> command can be enabled at run-time using the <code>manual</code> command in <code>chronyc</code>. (The idea of the two commands is that the <code>manual</code> command controls the manual clock driver&#8217;s behaviour, whereas the <code>settime</code> command allows samples of manually entered time to be provided.)</dl>
<p> <code>acquisitionport</code> <i>port</i></p>
<dl>
<dd>By default, <code>chronyd</code> uses a separate client socket for each configured server and their source port is chosen arbitrarily by the operating system. However, you can use the <code>acquisitionport</code> directive to explicitly specify a port and use only one socket (per IPv4 or IPv6 address family) for all configured servers. This can be useful for getting through some firewalls. If set to 0, the source port of the socket will be chosen arbitrarily. </p>
<p> It can be set to the same port as is used by the NTP server (which can be configured with the <code>port</code> directive) to use only one socket for all NTP packets. </p>
<p> An example of the <code>acquisitionport</code> directive is: </p>
<dl>
<dd>
<pre>acquisitionport 1123</pre>
</dl>
<p> This would change the source port used for client requests to UDP port 1123. You could then persuade the firewall administrator to open that port.</dl>
<p> <code>bindacqaddress</code> <i>address</i></p>
<dl>
<dd>The <code>bindacqaddress</code> directive sets the network interface to which <code>chronyd</code> will bind its NTP client sockets. The syntax is similar to the <code>bindaddress</code> and <code>bindcmdaddress</code> directives. </p>
<p> For each of the IPv4 and IPv6 protocols, only one <code>bindacqaddress</code> directive can be specified.</dl>
<p> <code>dumpdir</code> <i>directory</i></p>
<dl>
<dd>To compute the rate of gain or loss of time, <code>chronyd</code> has to store a measurement history for each of the time sources it uses. </p>
<p> Certain systems (Linux, FreeBSD, NetBSD, Solaris) have operating system support for setting the rate of gain or loss to compensate for known errors. (On Mac OS X, <code>chronyd</code> must simulate such a capability by periodically slewing the system clock forwards or backwards by a suitable amount to compensate for the error built up since the previous slew.) </p>
<p> For such systems, it is possible to save the measurement history across restarts of <code>chronyd</code> (assuming no changes are made to the system clock behaviour whilst it is not running). If this capability is to be used (via the <code>dumponexit</code> directive in the configuration file, or the <code>dump</code> command in <code>chronyc</code>), the <code>dumpdir</code> directive should be used to define the directory where the measurement histories are saved. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>dumpdir /var/run/chrony</pre>
</dl>
<p> A source whose IP address is <i>1.2.3.4</i> would have its measurement history saved in the file <i>/var/run/chrony/1.2.3.4.dat</i>. History of reference clocks is saved to files named by their reference ID in form of <i>refid:XXXXXXXX.dat</i>.</dl>
<p> <code>dumponexit</code></p>
<dl>
<dd>If this directive is present, it indicates that <code>chronyd</code> should save the measurement history for each of its time sources recorded whenever the program exits. (See the <code>dumpdir</code> directive above.)</dl>
<p> <code>maxsamples</code> <i>samples</i></p>
<dl>
<dd>The <code>maxsamples</code> directive sets the default maximum number of samples that <code>chronyd</code> should keep for each source. This setting can be overridden for individual sources in the <code>server</code> and <code>refclock</code> directives. The default value is 0, which disables the configurable limit. The useful range is 4 to 64.</dl>
<p> <code>minsamples</code> <i>samples</i></p>
<dl>
<dd>The <code>minsamples</code> directive sets the default minimum number of samples that <code>chronyd</code> should keep for each source. This setting can be overridden for individual sources in the <code>server</code> and <code>refclock</code> directives. The default value is 6. The useful range is 4 to 64.</dl>
<h3>Source selection</h3>
<p><code>combinelimit</code> <i>limit</i></p>
<dl>
<dd>When <code>chronyd</code> has multiple sources available for synchronisation, it has to select one source as the synchronisation source. The measured offsets and frequencies of the system clock relative to the other sources, however, can be combined with the selected source to improve the accuracy of the system clock. </p>
<p> The <code>combinelimit</code> directive limits which sources are included in the combining algorithm. Their synchronisation distance has to be shorter than the distance of the selected source multiplied by the value of the limit. Also, their measured frequencies have to be close to the frequency of the selected source. </p>
<p> By default, the limit is 3. Setting the limit to 0 effectively disables the source combining algorithm and only the selected source will be used to control the system clock.</dl>
<p> <code>maxdistance</code> <i>distance</i></p>
<dl>
<dd>The <code>maxdistance</code> directive sets the maximum allowed root distance of the sources to not be rejected by the source selection algorithm. The distance includes the accumulated dispersion, which might be large when the source is no longer synchronised, and half of the total round-trip delay to the primary source. </p>
<p> By default, the maximum root distance is 3 seconds. </p>
<p> Setting <code>maxdistance</code> to a larger value can be useful to allow synchronisation with a server that only has a very infrequent connection to its sources and can accumulate a large dispersion between updates of its clock.</dl>
<p> <code>maxjitter</code> <i>jitter</i></p>
<dl>
<dd>The <code>maxjitter</code> directive sets the maximum allowed jitter of the sources to not be rejected by the source selection algorithm. This prevents synchronisation with sources that have a small root distance, but their time is too variable. </p>
<p> By default, the maximum jitter is 1 second.</dl>
<p> <code>minsources</code> <i>sources</i></p>
<dl>
<dd>The <code>minsources</code> directive sets the minimum number of sources that need to be considered as selectable in the source selection algorithm before the local clock is updated. The default value is 1. </p>
<p> Setting this option to a larger number can be used to improve the reliability. More sources will have to agree with each other and the clock will not be updated when only one source (which could be serving incorrect time) is reachable.</dl>
<p> <code>reselectdist</code> <i>distance</i></p>
<dl>
<dd>When <code>chronyd</code> selects a synchronisation source from available sources, it will prefer the one with the shortest synchronisation distance. However, to avoid frequent reselecting when there are sources with similar distance, a fixed distance is added to the distance for sources that are currently not selected. This can be set with the <code>reselectdist</code> directive. By default, the distance is 100 microseconds.</dl>
<p> <code>stratumweight</code> <i>distance</i></p>
<dl>
<dd>The <code>stratumweight</code> directive sets how much distance should be added per stratum to the synchronisation distance when <code>chronyd</code> selects the synchronisation source from available sources. </p>
<p> By default, the weight is 0.001 seconds. This means that the stratum of the sources in the selection process matters only when the differences between the distances are in milliseconds.</dl>
<h3>System clock</h3>
<p><code>corrtimeratio</code> <i>ratio</i></p>
<dl>
<dd>When <code>chronyd</code> is slewing the system clock to correct an offset, the rate at which it is slewing adds to the frequency error of the clock. On Linux, FreeBSD, NetBSD and Solaris this rate can be controlled. </p>
<p> The <code>corrtimeratio</code> directive sets the ratio between the duration in which the clock is slewed for an average correction according to the source history and the interval in which the corrections are done (usually the NTP polling interval). Corrections larger than the average take less time and smaller corrections take more time, the amount of the correction and the correction time are inversely proportional. </p>
<p> Increasing <code>corrtimeratio</code> improves the overall frequency error of the system clock, but increases the overall time error as the corrections take longer. </p>
<p> By default, the ratio is set to 3, the time accuracy of the clock is preferred over its frequency accuracy. </p>
<p> The maximum allowed slew rate can be set by the <code>maxslewrate</code> directive. The current remaining correction is shown in the <code>tracking</code> report as the <code>System time</code> value.</dl>
<p> <code>driftfile</code> <i>file</i></p>
<dl>
<dd>One of the main activities of the <code>chronyd</code> program is to work out the rate at which the system clock gains or loses time relative to real time. </p>
<p> Whenever <code>chronyd</code> computes a new value of the gain or loss rate, it is desirable to record it somewhere. This allows <code>chronyd</code> to begin compensating the system clock at that rate whenever it is restarted, even before it has had a chance to obtain an equally good estimate of the rate during the new run. (This process can take many minutes, at least.) </p>
<p> The <code>driftfile</code> directive allows a file to be specified into which <code>chronyd</code> can store the rate information. Two parameters are recorded in the file. The first is the rate at which the system clock gains or loses time, expressed in parts per million, with gains positive. Therefore, a value of 100.0 indicates that when the system clock has advanced by a second, it has gained 100 microseconds in reality (so the true time has only advanced by 999900 microseconds). The second is an estimate of the error bound around the first value in which the true rate actually lies. </p>
<p> An example of the driftfile directive is: </p>
<dl>
<dd>
<pre>driftfile /var/lib/chrony/drift</pre>
</dl>
</dl>
<p> <code>fallbackdrift</code> <i>min-interval</i> <i>max-interval</i></p>
<dl>
<dd>Fallback drifts are long-term averages of the system clock drift calculated over exponentially increasing intervals. They are used when the clock is no longer synchronised to avoid quickly drifting away from true time if there was a short-term deviation in the drift before the synchronisation was lost. </p>
<p> The directive specifies the minimum and maximum interval since the last clock update to switch between fallback drifts. They are defined as a power of 2 (in seconds). The syntax is as follows: </p>
<dl>
<dd>
<pre>fallbackdrift 16 19</pre>
</dl>
<p> In this example, the minimum interval is 16 (18 hours) and the maximum interval is 19 (6 days). The system clock frequency will be set to the first fallback 18 hours after last clock update, to the second after 36 hours, etc. This might be a good setting to cover daily and weekly temperature fluctuations. </p>
<p> By default (or if the specified maximum or minimum is 0), no fallbacks are used and the clock frequency changes only with new measurements from NTP sources, reference clocks, or manual input.</dl>
<p> <code>leapsecmode</code> <i>mode</i></p>
<dl>
<dd>A leap second is an adjustment that is occasionally applied to UTC to keep it close to the mean solar time. When a leap second is inserted, the last day of June or December has an extra second 23:59:60. </p>
<p> For computer clocks that is a problem. The Unix time is defined as number of seconds since 00:00:00 UTC on 1 January 1970 without leap seconds. The system clock cannot have time 23:59:60, every minute has 60 seconds and every day has 86400 seconds by definition. The inserted leap second is skipped and the clock is suddenly ahead of UTC by one second. The <code>leapsecmode</code> directive selects how that error is corrected. There are four options: </p>
<p> <code>system</code></p>
<dl>
<dd>When inserting a leap second, the kernel steps the system clock backwards by one second when the clock gets to 00:00:00 UTC. When deleting a leap second, it steps forward by one second when the clock gets to 23:59:59 UTC. This is the default mode when the system driver supports leap seconds (i.e. on Linux, FreeBSD, NetBSD and Solaris).</dl>
<p> <code>step</code></p>
<dl>
<dd>This is similar to the <code>system</code> mode, except the clock is stepped by <code>chronyd</code> instead of the kernel. It can be useful to avoid bugs in the kernel code that would be executed in the <code>system</code> mode. This is the default mode when the system driver does not support leap seconds.</dl>
<p> <code>slew</code></p>
<dl>
<dd>The clock is corrected by slewing started at 00:00:00 UTC when a leap second is inserted or 23:59:59 UTC when a leap second is deleted. This might be preferred over the <code>system</code> and <code>step</code> modes when applications running on the system are sensitive to jumps in the system time and it is acceptable that the clock will be off for a longer time. On Linux with the default <code>maxslewrate</code> value the correction takes 12 seconds.</dl>
<p> <code>ignore</code></p>
<dl>
<dd>No correction is applied to the clock for the leap second. The clock will be corrected later in normal operation when new measurements are made and the estimated offset includes the one second error.</dl>
</dl>
<dl>
<dd>When serving time to NTP clients that cannot be configured to correct their clocks for a leap second by slewing, or to clients that would correct at slightly different rates when it is necessary to keep them close together, the <code>slew</code> mode can be combined with the <code>smoothtime</code> directive to enable a server leap smear. </p>
<p> When smearing a leap second, the leap status is suppressed on the server and the served time is corrected slowly be slewing instead of stepping. The clients do not need any special configuration as they do not know there is any leap second and they follow the server time which eventually brings them back to UTC. Care must be taken to ensure they use only NTP servers which smear the leap second in exactly the same way for synchronisation. </p>
<p> This feature must be used carefully, because the server is intentionally not serving its best estimate of the true time. </p>
<p> A recommended configuration to enable a server leap smear is: </p>
<dl>
<dd>
<pre>leapsecmode slew
maxslewrate 1000
smoothtime 400 0.001 leaponly</pre>
</dl>
<p> The first directive is necessary to disable the clock step which would reset the smoothing process. The second directive limits the slewing rate of the local clock to 1000 ppm, which improves the stability of the smoothing process when the local correction starts and ends. The third directive enables the server time smoothing process. It will start when the clock gets to 00:00:00 UTC and it will take 17 hours 34 minutes to finish. The frequency offset will be changing by 0.001 ppm per second and will reach a maximum of 31.623 ppm. The <code>leaponly</code> option makes the duration of the leap smear constant and allows the clients to safely synchronise with multiple identically configured leap smearing servers.</dl>
<p> <code>leapsectz</code> <i>timezone</i></p>
<dl>
<dd>This directive is used to set the name of the timezone in the system tz database which <code>chronyd</code> can use to find out when will the next leap second occur. It will periodically check if the times 23:59:59 and 23:59:60 are valid on Jun 30 and Dec 31 in the timezone. This typically works with the <code>right/UTC</code> timezone. </p>
<p> This directive is mainly useful with reference clocks which do not provide leap second information. It is not necessary to restart <code>chronyd</code> if the tz database is updated with a new leap second at least 12 hours before the event. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>leapsectz right/UTC</pre>
</dl>
<p> The following shell command verifies that the timezone contains leap seconds and can be used with this directive: </p>
<dl>
<dd>
<pre>$ TZ=right/UTC date -d 'Dec 31 2008 23:59:60'
Wed Dec 31 23:59:60 UTC 2008</pre>
</dl>
</dl>
<p> <code>makestep</code> <i>threshold</i> <i>limit</i></p>
<dl>
<dd>Normally <code>chronyd</code> will cause the system to gradually correct any time offset, by slowing down or speeding up the clock as required. In certain situations, the system clock might be so far adrift that this slewing process would take a very long time to correct the system clock. </p>
<p> This directive forces <code>chronyd</code> to step the system clock if the adjustment is larger than a threshold value, but only if there were no more clock updates since <code>chronyd</code> was started than a specified limit (a negative value can be used to disable the limit). </p>
<p> This is particularly useful when using reference clocks, because the <code>initstepslew</code> directive works only with NTP sources. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>makestep 0.1 3</pre>
</dl>
<p> This would step the system clock if the adjustment is larger than 0.1 seconds, but only in the first three clock updates.</dl>
<p> <code>maxchange</code> <i>offset</i> <i>start</i> <i>ignore</i></p>
<dl>
<dd>This directive sets the maximum allowed offset corrected on a clock update. The check is performed only after the specified number of updates to allow a large initial adjustment of the system clock. When an offset larger than the specified maximum occurs, it will be ignored for the specified number of times and then <code>chronyd</code> will give up and exit (a negative value can be used to never exit). In both cases a message is sent to syslog. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>maxchange 1000 1 2</pre>
</dl>
<p> After the first clock update, <code>chronyd</code> will check the offset on every clock update, it will ignore two adjustments larger than 1000 seconds and exit on another one.</dl>
<p> <code>maxclockerror</code> <i>error-in-ppm</i></p>
<dl>
<dd>The <code>maxclockerror</code> directive sets the maximum assumed frequency error that the system clock can gain on its own between clock updates. It describes the stability of the clock. </p>
<p> By default, the maximum error is 1 ppm. </p>
<p> Typical values for <i>error-in-ppm</i> might be 10 for a low quality clock and 0.1 for a high quality clock using a temperature compensated crystal oscillator.</dl>
<p> <code>maxdrift</code> <i>drift-in-ppm</i></p>
<dl>
<dd>This directive specifies the maximum assumed drift (frequency error) of the system clock. It limits the frequency adjustment that <code>chronyd</code> is allowed to use to correct the measured drift. It is an additional limit to the maximum adjustment that can be set by the system driver (100000 ppm on Linux, 500 ppm on FreeBSD and NetBSD, 32500 ppm on Solaris). </p>
<p> By default, the maximum assumed drift is 500000 ppm, i.e. the adjustment is limited by the system driver rather than this directive.</dl>
<p> <code>maxupdateskew</code> <i>skew-in-ppm</i></p>
<dl>
<dd>One of <code>chronyd</code>&#8216;s tasks is to work out how fast or slow the computer&#8217;s clock runs relative to its reference sources. In addition, it computes an estimate of the error bounds around the estimated value. </p>
<p> If the range of error is too large, it probably indicates that the measurements have not settled down yet, and that the estimated gain or loss rate is not very reliable. </p>
<p> The <code>maxupdateskew</code> directive sets the threshold for determining whether an estimate might be so unreliable that it should not be used. By default, the threshold is 1000 ppm. </p>
<p> Typical values for <i>skew-in-ppm</i> might be 100 for a dial-up connection to servers over a phone line, and 5 or 10 for a computer on a LAN. </p>
<p> It should be noted that this is not the only means of protection against using unreliable estimates. At all times, <code>chronyd</code> keeps track of both the estimated gain or loss rate, and the error bound on the estimate. When a new estimate is generated following another measurement from one of the sources, a weighted combination algorithm is used to update the master estimate. So if <code>chronyd</code> has an existing highly-reliable master estimate and a new estimate is generated which has large error bounds, the existing master estimate will dominate in the new master estimate.</dl>
<p> <code>maxslewrate</code> <i>rate-in-ppm</i></p>
<dl>
<dd>The <code>maxslewrate</code> directive sets the maximum rate at which <code>chronyd</code> is allowed to slew the time. It limits the slew rate controlled by the correction time ratio (which can be set by the <code>corrtimeratio</code> directive) and is effective only on systems where <code>chronyd</code> is able to control the rate (i.e. Linux, FreeBSD, NetBSD, Solaris). </p>
<p> For each system there is a maximum frequency offset of the clock that can be set by the driver. On Linux it is 100000 ppm, on FreeBSD and NetBSD it is 5000 ppm, and on Solaris it is 32500 ppm. Also, due to a kernel limitation, setting <code>maxslewrate</code> on FreeBSD and NetBSD to a value between 500 ppm and 5000 ppm will effectively set it to 500 ppm. </p>
<p> By default, the maximum slew rate is set to 83333.333 ppm (one twelfth).</dl>
<p> <code>tempcomp</code> <i>file</i> <i>interval</i> <i>T0</i> <i>k0</i> <i>k1</i> <i>k2</i>, <code>tempcomp</code> <i>file</i> <i>interval</i> <i>points-file</i></p>
<dl>
<dd>Normally, changes in the rate of drift of the system clock are caused mainly by changes in the temperature of the crystal oscillator on the motherboard. </p>
<p> If there are temperature measurements available from a sensor close to the oscillator, the <code>tempcomp</code> directive can be used to compensate for the changes in the temperature and improve the stability and accuracy of the clock. </p>
<p> The result depends on many factors, including the resolution of the sensor, the amount of noise in the measurements, the polling interval of the time source, the compensation update interval, how well the compensation is specified, and how close the sensor is to the oscillator. When it is working well, the frequency reported in the <i>tracking.log</i> file is more stable and the maximum reached offset is smaller. </p>
<p> There are two forms of the directive. The first one has six parameters: a path to the file containing the current temperature from the sensor (in text format), the compensation update interval (in seconds), and temperature coefficients <i>T0</i>, <i>k0</i>, <i>k1</i>, <i>k2</i>. </p>
<p> The frequency compensation is calculated (in ppm) as </p>
<dl>
<dd>
<pre>k0 + (T - T0) * k1 + (T - T0)^2 * k2</pre>
</dl>
<p> The result has to be between -10 ppm and 10 ppm, otherwise the measurement is considered invalid and will be ignored. The <i>k0</i> coefficient can be adjusted to keep the compensation in that range. </p>
<p> An example of the use is: </p>
<dl>
<dd>
<pre>tempcomp /sys/class/hwmon/hwmon0/temp2_input 30 26000 0.0 0.000183 0.0</pre>
</dl>
<p> The measured temperature will be read from the file in the Linux sysfs filesystem every 30 seconds. When the temperature is 26000 (26 degrees Celsius), the frequency correction will be zero. When it is 27000 (27 degrees Celsius), the clock will be set to run faster by 0.183 ppm, etc. </p>
<p> The second form has three parameters: the path to the sensor file, the update interval, and a path to a file containing a list of (temperature, compensation) points, from which the compensation is linearly interpolated or extrapolated. </p>
<p> An example is: </p>
<dl>
<dd>
<pre>tempcomp /sys/class/hwmon/hwmon0/temp2_input 30 /etc/chrony.tempcomp</pre>
</dl>
<p> where the <i>/etc/chrony.tempcomp</i> file could have </p>
<dl>
<dd>
<pre>20000 1.0
21000 0.64
22000 0.36
23000 0.16
24000 0.04
25000 0.0
26000 0.04
27000 0.16
28000 0.36
29000 0.64
30000 1.0</pre>
</dl>
<p> Valid measurements with corresponding compensations are logged to the <i>tempcomp.log</i> file if enabled by the <code>log tempcomp</code> directive.</dl>
<h3>NTP server</h3>
<p><code>allow</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dd>The <code>allow</code> directive is used to designate a particular subnet from which NTP clients are allowed to access the computer as an NTP server. </p>
<p> The default is that no clients are allowed access, i.e. <code>chronyd</code> operates purely as an NTP client. If the <code>allow</code> directive is used, <code>chronyd</code> will be both a client of its servers, and a server to other clients. </p>
<p> Examples of the use of the directive are as follows: </p>
<dl>
<dd>
<pre>allow 1.2.3.4
allow 1.2
allow 3.4.5
allow 6.7.8/22
allow 6.7.8.9/22
allow 2001:db8::/32
allow 0/0
allow ::/0
allow</pre>
</dl>
<p> The first directive allows a node with IPv4 address <i>1.2.3.4</i> to be an NTP client of this computer. The second directive allows any node with an IPv4 address of the form <i>1.2.x.y</i> (with <i>x</i> and <i>y</i> arbitrary) to be an NTP client of this computer. Likewise, the third directive allows any node with an IPv4 address of the form <i>3.4.5.x</i> to have client NTP access. The fourth and fifth forms allow access from any node with an IPv4 address of the form <i>6.7.8.x</i>, <i>6.7.9.x</i>, <i>6.7.10.x</i> or <i>6.7.11.x</i> (with <i>x</i> arbitrary), i.e. the value 22 is the number of bits defining the specified subnet. In the fifth form, the final byte is ignored. The sixth form is used for IPv6 addresses. The seventh and eighth forms allow access by any IPv4 and IPv6 node respectively. The ninth forms allows access by any node (IPv4 or IPv6). </p>
<p> A second form of the directive, <code>allow all</code>, has a greater effect, depending on the ordering of directives in the configuration file. To illustrate the effect, consider the two examples: </p>
<dl>
<dd>
<pre>allow 1.2.3.4
deny 1.2.3
allow 1.2</pre>
</dl>
<p> and </p>
<dl>
<dd>
<pre>allow 1.2.3.4
deny 1.2.3
allow all 1.2</pre>
</dl>
<p> In the first example, the effect is the same regardless of what order the three directives are given in. So the <i>1.2.x.y</i> subnet is allowed access, except for the <i>1.2.3.x</i> subnet, which is denied access, however the host <i>1.2.3.4</i> is allowed access. </p>
<p> In the second example, the <code>allow all 1.2</code> directives overrides the effect of <i>any</i> previous directive relating to a subnet within the specified subnet. Within a configuration file this capability is probably rather moot; however, it is of greater use for reconfiguration at run-time via <code>chronyc</code> with the <code>allow all</code> command. </p>
<p> The directive allows a hostname to be specified instead of an IP address, but the name must be resolvable when <code>chronyd</code> is started (i.e. <code>chronyd</code> needs to be started when the network is already up and DNS is working). </p>
<p> Note, if the <code>initstepslew</code> directive is used in the configuration file, each of the computers listed in that directive must allow client access by this computer for it to work.</dl>
<p> <code>deny</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dd>This is similar to the <code>allow</code> directive, except that it denies NTP client access to a particular subnet or host, rather than allowing it. </p>
<p> The syntax is identical. </p>
<p> There is also a <code>deny all</code> directive with similar behaviour to the <code>allow all</code> directive.</dl>
<p> <code>bindaddress</code> <i>address</i></p>
<dl>
<dd>The <code>bindaddress</code> directive binds the socket on which <code>chronyd</code> listens for NTP requests to a local address of the computer. On systems other than Linux, the address of the computer needs to be already configured when <code>chronyd</code> is started. </p>
<p> An example of the use of the directive is: </p>
<dl>
<dd>
<pre>bindaddress 192.168.1.1</pre>
</dl>
<p> Currently, for each of the IPv4 and IPv6 protocols, only one <code>bindaddress</code> directive can be specified. Therefore, it is not useful on computers which should serve NTP on multiple network interfaces.</dl>
<p> <code>broadcast</code> <i>interval</i> <i>address</i> [<i>port</i>]</p>
<dl>
<dd>The <code>broadcast</code> directive is used to declare a broadcast address to which chronyd should send packets in the NTP broadcast mode (i.e. make <code>chronyd</code> act as a broadcast server). Broadcast clients on that subnet will be able to synchronise. </p>
<p> The syntax is as follows: </p>
<dl>
<dd>
<pre>broadcast 30 192.168.1.255
broadcast 60 192.168.2.255 12123
broadcast 60 ff02::101</pre>
</dl>
<p> In the first example, the destination port defaults to UDP port 123 (the normal NTP port). In the second example, the destination port is specified as 12123. The first parameter in each case (30 or 60 respectively) is the interval in seconds between broadcast packets being sent. The second parameter in each case is the broadcast address to send the packet to. This should correspond to the broadcast address of one of the network interfaces on the computer where <code>chronyd</code> is running. </p>
<p> You can have more than 1 <code>broadcast</code> directive if you have more than 1 network interface onto which you want to send NTP broadcast packets. </p>
<p> <code>chronyd</code> itself cannot act as a broadcast client; it must always be configured as a point-to-point client by defining specific NTP servers and peers. This broadcast server feature is intended for providing a time source to other NTP implementations. </p>
<p> If <code>ntpd</code> is used as the broadcast client, it will try to measure the round-trip delay between the server and client with normal client mode packets. Thus, the broadcast subnet should also be the subject of an <code>allow</code> directive.</dl>
<p> <code>clientloglimit</code> <i>limit</i></p>
<dl>
<dd>This directive specifies the maximum amount of memory that <code>chronyd</code> is allowed to allocate for logging of client accesses and the state that <code>chronyd</code> as an NTP server needs to support the interleaved mode for its clients. The default limit is 524288 bytes, which is sufficient for monitoring about four thousand clients at the same time. </p>
<p> In older <code>chrony</code> versions if the limit was set to 0, the memory allocation was unlimited. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>clientloglimit 1048576</pre>
</dl>
</dl>
<p> <code>noclientlog</code></p>
<dl>
<dd>This directive, which takes no arguments, specifies that client accesses are not to be logged. Normally they are logged, allowing statistics to be reported using the <code>clients</code> command in <code>chronyc</code>. This option also effectively disables server support for the NTP interleaved mode.</dl>
<p> <code>local</code> [<i>option</i>]&#8230;</p>
<dl>
<dd>The <code>local</code> directive enables a local reference mode, which allows <code>chronyd</code> operating as an NTP server to appear synchronised to real time (from the viewpoint of clients polling it), even when it was never synchronised or the last update of the clock happened a long time ago. </p>
<p> This directive is normally used in an isolated network, where computers are required to be synchronised to one another, but not necessarily to real time. The server can be kept vaguely in line with real time by manual input. </p>
<p> The <code>local</code> directive has the following options: </p>
<p> <code>stratum</code> <i>stratum</i></p>
<dl>
<dd>This option sets the stratum of the server which will be reported to clients when the local reference is active. The specified value is in the range 1 through 15, and the default value is 10. It should be larger than the maximum expected stratum in the network when external NTP servers are accessible. </p>
<p> Stratum 1 indicates a computer that has a true real-time reference directly connected to it (e.g. GPS, atomic clock, etc.), such computers are expected to be very close to real time. Stratum 2 computers are those which have a stratum 1 server; stratum 3 computers have a stratum 2 server and so on. A value of 10 indicates that the clock is so many hops away from a reference clock that its time is fairly unreliable.</dl>
<p> <code>distance</code> <i>distance</i></p>
<dl>
<dd>This option sets the threshold for the root distance which will activate the local reference. If <code>chronyd</code> was synchronised to some source, the local reference will not be activated until its root distance reaches the specified value (the rate at which the distance is increasing depends on how well the clock was tracking the source). The default value is 1 second. </p>
<p> The current root distance can be calculated from root delay and root dispersion (reported by the <code>tracking</code> command in <code>chronyc</code>) as: </p>
<dl>
<dd>
<pre>distance = delay / 2 + dispersion</pre>
</dl>
</dl>
<p> <code>orphan</code></p>
<dl>
<dd>This option enables a special &#8216;orphan&#8217; mode, where sources with stratum equal to the local <i>stratum</i> are assumed to not serve real time. They are ignored unless no other source is selectable and their reference IDs are smaller than the local reference ID. </p>
<p> This allows multiple servers in the network to use the same <code>local</code> configuration and to be synchronised to one another, without confusing clients that poll more than one server. Each server needs to be configured to poll all other servers with the <code>local</code> directive. This ensures only the server with the smallest reference ID has the local reference active and others are synchronised to it. When that server fails, another will take over. </p>
<p> The <code>orphan</code> mode is compatible with the <code>ntpd</code>&#8216;s orphan mode (enabled by the <code>tos orphan</code> command).</dl>
</dl>
<dl>
<dd>An example of the directive is: </p>
<dl>
<dd>
<pre>local stratum 10 orphan</pre>
</dl>
</dl>
<p> <code>ntpsigndsocket</code> <i>directory</i></p>
<dl>
<dd>This directive specifies the location of the Samba <code>ntp_signd</code> socket when it is running as a Domain Controller (DC). If <code>chronyd</code> is compiled with this feature, responses to MS-SNTP clients will be signed by the <code>smbd</code> daemon. </p>
<p> Note that MS-SNTP requests are not authenticated and any client that is allowed to access the server by the <code>allow</code> directive, or the <code>allow</code> command in <code>chronyc</code>, can get an MS-SNTP response signed with a trust account&#8217;s password and try to crack the password in a brute-force attack. Access to the server should be carefully controlled. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>ntpsigndsocket /var/lib/samba/ntp_signd</pre>
</dl>
</dl>
<p> <code>port</code> <i>port</i></p>
<dl>
<dd>This option allows you to configure the port on which <code>chronyd</code> will listen for NTP requests. The port will be open only when an address is allowed by the <code>allow</code> directive or the <code>allow</code> command in <code>chronyc</code>, an NTP peer is configured, or the broadcast server mode is enabled. </p>
<p> The default value is 123, the standard NTP port. If set to 0, <code>chronyd</code> will never open the server port and will operate strictly in a client-only mode. The source port used in NTP client requests can be set by the <code>acquisitionport</code> directive.</dl>
<p> <code>ratelimit</code> [<i>option</i>]&#8230;</p>
<dl>
<dd>This directive enables response rate limiting for NTP packets. Its purpose is to reduce network traffic with misconfigured or broken NTP clients that are polling the server too frequently. The limits are applied to individual IP addresses. If multiple clients share one IP address (e.g. multiple hosts behind NAT), the sum of their traffic will be limited. If a client that increases its polling rate when it does not receive a reply is detected, its rate limiting will be temporarily suspended to avoid increasing the overall amount of traffic. The maximum number of IP addresses which can be monitored at the same time depends on the memory limit set by the <code>clientloglimit</code> directive. </p>
<p> The <code>ratelimit</code> directive supports a number of options (which can be defined in any order): </p>
<p> <code>interval</code></p>
<dl>
<dd>This option sets the minimum interval between responses. It is defined as a power of 2 in seconds. The default value is 3 (8 seconds). The minimum value is -19 (524288 packets per second) and the maximum value is 12 (one packet per 4096 seconds). Note that with values below -4 the rate limiting is coarse (responses are allowed in bursts, even if the interval between them is shorter than the specified interval).</dl>
<p> <code>burst</code></p>
<dl>
<dd>This option sets the maximum number of responses that can be sent in a burst, temporarily exceeding the limit specified by the <code>interval</code> option. This is useful for clients that make rapid measurements on start (e.g. <code>chronyd</code> with the <code>iburst</code> option). The default value is 8. The minimum value is 1 and the maximum value is 255.</dl>
<p> <code>leak</code></p>
<dl>
<dd>This option sets the rate at which responses are randomly allowed even if the limits specified by the <code>interval</code> and <code>burst</code> options are exceeded. This is necessary to prevent an attacker who is sending requests with a spoofed source address from completely blocking responses to that address. The leak rate is defined as a power of 1/2 and it is 2 by default, i.e. on average at least every fourth request has a response. The minimum value is 1 and the maximum value is 4.</dl>
</dl>
<dl>
<dd>An example use of the directive is: </p>
<dl>
<dd>
<pre>ratelimit interval 1 burst 16</pre>
</dl>
<p> This would reduce the response rate for IP addresses sending packets on average more than once per 2 seconds, or sending packets in bursts of more than 16 packets, by up to 75% (with default <code>leak</code> of 2).</dl>
<p> <code>smoothtime</code> <i>max-freq</i> <i>max-wander</i> [<code>leaponly</code>]</p>
<dl>
<dd>The <code>smoothtime</code> directive can be used to enable smoothing of the time that <code>chronyd</code> serves to its clients to make it easier for them to track it and keep their clocks close together even when large offset or frequency corrections are applied to the server&#8217;s clock, for example after being offline for a longer time. </p>
<p> BE WARNED: The server is intentionally not serving its best estimate of the true time. If a large offset has been accumulated, it can take a very long time to smooth it out. This directive should be used only when the clients are not configured to also poll another NTP server, because they could reject this server as a falseticker or fail to select a source completely. </p>
<p> The smoothing process is implemented with a quadratic spline function with two or three pieces. It is independent from any slewing applied to the local system clock, but the accumulated offset and frequency will be reset when the clock is corrected by stepping, e.g. by the <code>makestep</code> directive or the <code>makestep</code> command in <code>chronyc</code>. The process can be reset without stepping the clock by the <code>smoothtime reset</code> command. </p>
<p> The first two arguments of the directive are the maximum frequency offset of the smoothed time to the tracked NTP time (in ppm) and the maximum rate at which the frequency offset is allowed to change (in ppm per second). <code>leaponly</code> is an optional third argument which enables a mode where only leap seconds are smoothed out and normal offset and frequency changes are ignored. The <code>leaponly</code> option is useful in a combination with the <code>leapsecmode slew</code> directive to allow the clients to use multiple time smoothing servers safely. </p>
<p> The smoothing process is activated automatically when 1/10000 of the estimated skew of the local clock falls below the maximum rate of frequency change. It can be also activated manually by the <code>smoothtime activate</code> command, which is particularly useful when the clock is synchronised only with manual input and the skew is always larger than the threshold. The <code>smoothing</code> command can be used to monitor the process. </p>
<p> An example suitable for clients using <code>ntpd</code> and 1024 second polling interval could be: </p>
<dl>
<dd>
<pre>smoothtime 400 0.001</pre>
</dl>
<p> An example suitable for clients using <code>chronyd</code> on Linux could be: </p>
<dl>
<dd>
<pre>smoothtime 50000 0.01</pre>
</dl>
</dl>
<h3>Command and monitoring access</h3>
<p><code>bindcmdaddress</code> <i>address</i></p>
<dl>
<dd>The <code>bindcmdaddress</code> directive allows you to specify an IP address of an interface on which <code>chronyd</code> will listen for monitoring command packets (issued by <code>chronyc</code>). On systems other than Linux, the address of the interface needs to be already configured when <code>chronyd</code> is started. </p>
<p> This directive can also change the path of the Unix domain command socket, which is used by <code>chronyc</code> to send configuration commands. The socket must be in a directory that is accessible only by the root or <i>chrony</i> user. The directory will be created on start if it does not exist. The compiled-in default path of the socket is <i>/var/run/chrony/chronyd.sock</i>. The socket can be disabled by setting the path to <i>/</i>. </p>
<p> By default, <code>chronyd</code> binds to the loopback interface (with addresses <i>127.0.0.1</i> and <i>::1</i>). This blocks all access except from localhost. To listen for command packets on all interfaces, you can add the lines: </p>
<dl>
<dd>
<pre>bindcmdaddress 0.0.0.0
bindcmdaddress ::</pre>
</dl>
<p> to the configuration file. </p>
<p> For each of the IPv4, IPv6, and Unix domain protocols, only one <code>bindcmdaddress</code> directive can be specified. </p>
<p> An example that sets the path of the Unix domain command socket is: </p>
<dl>
<dd>
<pre>bindcmdaddress /var/run/chrony/chronyd.sock</pre>
</dl>
</dl>
<p> <code>cmdallow</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dd>This is similar to the <code>allow</code> directive, except that it allows monitoring access (rather than NTP client access) to a particular subnet or host. (By &#8216;monitoring access&#8217; is meant that <code>chronyc</code> can be run on those hosts and retrieve monitoring data from <code>chronyd</code> on this computer.) </p>
<p> The syntax is identical to the <code>allow</code> directive. </p>
<p> There is also a <code>cmdallow all</code> directive with similar behaviour to the <code>allow all</code> directive (but applying to monitoring access in this case, of course). </p>
<p> Note that <code>chronyd</code> has to be configured with the <code>bindcmdaddress</code> directive to not listen only on the loopback interface to actually allow remote access.</dl>
<p> <code>cmddeny</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dd>This is similar to the <code>cmdallow</code> directive, except that it denies monitoring access to a particular subnet or host, rather than allowing it. </p>
<p> The syntax is identical. </p>
<p> There is also a <code>cmddeny all</code> directive with similar behaviour to the <code>cmdallow all</code> directive.</dl>
<p> <code>cmdport</code> <i>port</i></p>
<dl>
<dd>The <code>cmdport</code> directive allows the port that is used for run-time monitoring (via the <code>chronyc</code> program) to be altered from its default (323). If set to 0, <code>chronyd</code> will not open the port, this is useful to disable <code>chronyc</code> access from the Internet. (It does not disable the Unix domain command socket.) </p>
<p> An example shows the syntax: </p>
<dl>
<dd>
<pre>cmdport 257</pre>
</dl>
<p> This would make <code>chronyd</code> use UDP 257 as its command port. (<code>chronyc</code> would need to be run with the <code>-p 257</code> switch to inter-operate correctly.)</dl>
<p> <code>cmdratelimit</code> [<i>option</i>]&#8230;</p>
<dl>
<dd>This directive enables response rate limiting for command packets. It is similar to the <code>ratelimit</code> directive, except responses to localhost are never limited and the default interval is -4 (16 packets per second). </p>
<p> An example of the use of the directive is: </p>
<dl>
<dd>
<pre>cmdratelimit interval 2</pre>
</dl>
</dl>
<h3>Real-time clock (RTC)</h3>
<p><code>hwclockfile</code> <i>file</i></p>
<dl>
<dd>The <code>hwclockfile</code> directive sets the location of the adjtime file which is used by the <code>hwclock</code> program on Linux. <code>chronyd</code> parses the file to find out if the RTC keeps local time or UTC. It overrides the <code>rtconutc</code> directive. </p>
<p> The compiled-in default value is &#8216;<i>/etc/adjtime</i>&#8216;. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>hwclockfile /etc/adjtime</pre>
</dl>
</dl>
<p> <code>rtcautotrim</code> <i>threshold</i></p>
<dl>
<dd>The <code>rtcautotrim</code> directive is used to keep the RTC close to the system clock automatically. When the system clock is synchronised and the estimated error between the two clocks is larger than the specified threshold, <code>chronyd</code> will trim the RTC as if the <code>trimrtc</code> command in <code>chronyc</code> was issued. </p>
<p> This directive is effective only with the <code>rtcfile</code> directive. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>rtcautotrim 30</pre>
</dl>
<p> This would set the threshold error to 30 seconds.</dl>
<p> <code>rtcdevice</code> <i>device</i></p>
<dl>
<dd>The <code>rtcdevice</code> directive sets the path to the device file for accessing the RTC. The default path is <i>/dev/rtc</i>.</dl>
<p> <code>rtcfile</code> <i>file</i></p>
<dl>
<dd>The <code>rtcfile</code> directive defines the name of the file in which <code>chronyd</code> can save parameters associated with tracking the accuracy of the RTC. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>rtcfile /var/lib/chrony/rtc</pre>
</dl>
<p> <code>chronyd</code> saves information in this file when it exits and when the <code>writertc</code> command is issued in <code>chronyc</code>. The information saved is the RTC&#8217;s error at some epoch, that epoch (in seconds since January 1 1970), and the rate at which the RTC gains or loses time. </p>
<p> So far, the support for real-time clocks is limited; their code is even more system-specific than the rest of the software. You can only use the RTC facilities (the <code>rtcfile</code> directive and the <code>-s</code> command-line option to <code>chronyd</code>) if the following three conditions apply: </p>
<dl>
<dd>1. You are running Linux.</dl>
<dl>
<dd>2. The kernel is compiled with extended real-time clock support (i.e. the <i>/dev/rtc</i> device is capable of doing useful things).</dl>
<dl>
<dd>3. You do not have other applications that need to make use of <i>/dev/rtc</i> at all.</dl>
</dl>
<p> <code>rtconutc</code></p>
<dl>
<dd><code>chronyd</code> assumes by default that the RTC keeps local time (including any daylight saving changes). This is convenient on PCs running Linux which are dual-booted with Windows. </p>
<p> If you keep the RTC on local time and your computer is off when daylight saving (summer time) starts or ends, the computer&#8217;s system time will be one hour in error when you next boot and start chronyd. </p>
<p> An alternative is for the RTC to keep Universal Coordinated Time (UTC). This does not suffer from the 1 hour problem when daylight saving starts or ends. </p>
<p> If the <code>rtconutc</code> directive appears, it means the RTC is required to keep UTC. The directive takes no arguments. It is equivalent to specifying the <code>-u</code> switch to the Linux <code>hwclock</code> program. </p>
<p> Note that this setting is overridden when the <code>hwclockfile</code> directive is specified.</dl>
<p> <code>rtcsync</code></p>
<dl>
<dd>The <code>rtcsync</code> directive enables a mode where the system time is periodically copied to the RTC and <code>chronyd</code> does not try to track its drift. This directive cannot be used with the <code>rtcfile</code> directive. </p>
<p> On Linux, the RTC copy is performed by the kernel every 11 minutes. </p>
<p> On macOS, <code>chronyd</code> will perform the RTC copy every 60 minutes when the system clock is in a synchronised state. </p>
<p> On other systems this directive does nothing.</dl>
<h3>Logging</h3>
<p><code>log</code> [<i>option</i>]&#8230;</p>
<dl>
<dd>The <code>log</code> directive indicates that certain information is to be logged. The log files are written to the directory specified by the <code>logdir</code> directive. A banner is periodically written to the files to indicate the meanings of the columns. </p>
<p> <code>rawmeasurements</code></p>
<dl>
<dd>This option logs the raw NTP measurements and related information to a file called <i>measurements.log</i>. An entry is made for each packet received from the source. This can be useful when debugging a problem. An example line (which actually appears as a single line in the file) from the log file is shown below. </p>
<dl>
<dd>
<pre>2016-11-09 05:40:50 203.0.113.15 N 2 111 111 1111 10 10 1.0 \
 -4.966e-03 2.296e-01 1.577e-05 1.615e-01 7.446e-03 CB00717B 4B D K</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above): </p>
<dl>
<dd>1. Date [2015-10-13]</dl>
<dl>
<dd>2. Hour:Minute:Second. Note that the date-time pair is expressed in UTC, not the local time zone. [05:40:50]</dl>
<dl>
<dd>3. IP address of server or peer from which measurement came [203.0.113.15]</dl>
<dl>
<dd>4. Leap status (<i>N</i> means normal, <i>+</i> means that the last minute of the current month has 61 seconds, <i>&#8211;</i> means that the last minute of the month has 59 seconds, <i>?</i> means the remote computer is not currently synchronised.) [N]</dl>
<dl>
<dd>5. Stratum of remote computer. [2]</dl>
<dl>
<dd>6. RFC 5905 tests 1 through 3 (1=pass, 0=fail) [111]</dl>
<dl>
<dd>7. RFC 5905 tests 5 through 7 (1=pass, 0=fail) [111]</dl>
<dl>
<dd>8. Tests for maximum delay, maximum delay ratio and maximum delay dev ratio, against defined parameters, and a test for synchronisation loop (1=pass, 0=fail) [1111]</dl>
<dl>
<dd>9. Local poll [10]</dl>
<dl>
<dd>10. Remote poll [10]</dl>
<dl>
<dd>11. &#8216;Score&#8217; (an internal score within each polling level used to decide when to increase or decrease the polling level. This is adjusted based on number of measurements currently being used for the regression algorithm). [1.0]</dl>
<dl>
<dd>12. The estimated local clock error (<i>theta</i> in RFC 5905). Positive indicates that the local clock is slow of the remote source. [-4.966e-03]</dl>
<dl>
<dd>13. The peer delay (<i>delta</i> in RFC 5905). [2.296e-01]</dl>
<dl>
<dd>14. The peer dispersion (<i>epsilon</i> in RFC 5905). [1.577e-05]</dl>
<dl>
<dd>15. The root delay (<i>DELTA</i> in RFC 5905). [1.615e-01]</dl>
<dl>
<dd>16. The root dispersion (<i>EPSILON</i> in RFC 5905). [7.446e-03]</dl>
<dl>
<dd>17. Reference ID of the server&#8217;s source as a hexadecimal number. [CB00717B]</dl>
<dl>
<dd>18. NTP mode of the received packet (<i>1</i>=active peer, <i>2</i>=passive peer, <i>3</i>=server, <i>B</i>=basic, <i>I</i>=interleaved). [4B]</dl>
<dl>
<dd>19. Source of the local transmit timestamp (<i>D</i>=daemon, <i>K</i>=kernel, <i>H</i>=hardware). [D]</dl>
<dl>
<dd>20. Source of the local receive timestamp (<i>D</i>=daemon, <i>K</i>=kernel, <i>H</i>=hardware). [K]</dl>
</dl>
<p> <code>measurements</code></p>
<dl>
<dd>This option is identical to the <code>rawmeasurements</code> option, except it logs only valid measurements from synchronised sources, i.e. measurements which passed the RFC 5905 tests 1 through 7. This can be useful for producing graphs of the source&#8217;s performance.</dl>
<p> <code>statistics</code></p>
<dl>
<dd>This option logs information about the regression processing to a file called <i>statistics.log</i>. An example line (which actually appears as a single line in the file) from the log file is shown below. </p>
<dl>
<dd>
<pre>2016-08-10 05:40:50 203.0.113.15 6.261e-03 -3.247e-03 \
 2.220e-03 1.874e-06 1.080e-06 7.8e-02 16 0 8 0.00</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above): </p>
<dl>
<dd>1. Date [2015-07-22]</dl>
<dl>
<dd>2. Hour:Minute:Second. Note that the date-time pair is expressed in UTC, not the local time zone. [05:40:50]</dl>
<dl>
<dd>3. IP address of server or peer from which measurement comes [203.0.113.15]</dl>
<dl>
<dd>4. The estimated standard deviation of the measurements from the source (in seconds). [6.261e-03]</dl>
<dl>
<dd>5. The estimated offset of the source (in seconds, positive means the local clock is estimated to be fast, in this case). [-3.247e-03]</dl>
<dl>
<dd>6. The estimated standard deviation of the offset estimate (in seconds). [2.220e-03]</dl>
<dl>
<dd>7. The estimated rate at which the local clock is gaining or losing time relative to the source (in seconds per second, positive means the local clock is gaining). This is relative to the compensation currently being applied to the local clock, <i>not</i> to the local clock without any compensation. [1.874e-06]</dl>
<dl>
<dd>8. The estimated error in the rate value (in seconds per second). [1.080e-06].</dl>
<dl>
<dd>9. The ratio of |old_rate &#8211; new_rate| / old_rate_error. Large values indicate the statistics are not modelling the source very well. [7.8e-02]</dl>
<dl>
<dd>10. The number of measurements currently being used for the regression algorithm. [16]</dl>
<dl>
<dd>11. The new starting index (the oldest sample has index 0; this is the method used to prune old samples when it no longer looks like the measurements fit a linear model). [0, i.e. no samples discarded this time]</dl>
<dl>
<dd>12. The number of runs. The number of runs of regression residuals with the same sign is computed. If this is too small it indicates that the measurements are no longer represented well by a linear model and that some older samples need to be discarded. The number of runs for the data that is being retained is tabulated. Values of approximately half the number of samples are expected. [8]</dl>
<dl>
<dd>13. The estimated asymmetry of network jitter on the path to the source which was used to correct the measured offsets. The asymmetry can be between -0.5 and 0.5. A negative value means the delay of packets sent to the source is more variable than the delay of packets sent from the source back. [0.00, i.e. no correction for asymmetry]</dl>
</dl>
<p> <code>tracking</code></p>
<dl>
<dd>This option logs changes to the estimate of the system&#8217;s gain or loss rate, and any slews made, to a file called <i>tracking.log</i>. An example line (which actually appears as a single line in the file) from the log file is shown below. </p>
<dl>
<dd>
<pre>2015-02-23 05:40:50 203.0.113.15 3 340.529 1.606 1.046e-03 N \
 4 6.849e-03 -4.670e-04</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above) : </p>
<dl>
<dd>1. Date [2015-02-03]</dl>
<dl>
<dd>2. Hour:Minute:Second. Note that the date-time pair is expressed in UTC, not the local time zone. [05:40:50]</dl>
<dl>
<dd>3. The IP address of the server or peer to which the local system is synchronised. [203.0.113.15]</dl>
<dl>
<dd>4. The stratum of the local system. [3]</dl>
<dl>
<dd>5. The local system frequency (in ppm, positive means the local system runs fast of UTC). [340.529]</dl>
<dl>
<dd>6. The error bounds on the frequency (in ppm). [1.606]</dl>
<dl>
<dd>7. The estimated local offset at the epoch (which is rapidly corrected by slewing the local clock. (In seconds, positive indicates the local system is fast of UTC). [1.046e-3]</dl>
<dl>
<dd>8. Leap status (<i>N</i> means normal, <i>+</i> means that the last minute of this month has 61 seconds, <i>&#8211;</i> means that the last minute of the month has 59 seconds, <i>?</i> means the clock is not currently synchronised.) [N]</dl>
<dl>
<dd>9. The number of combined sources. [4]</dl>
<dl>
<dd>10. The estimated standard deviation of the combined offset (in seconds). [6.849e-03]</dl>
<dl>
<dd>11. The remaining offset correction from the previous update (in seconds, positive means the system clock is slow of UTC). [-4.670e-04]</dl>
</dl>
<p> <code>rtc</code></p>
<dl>
<dd>This option logs information about the system&#8217;s real-time clock. An example line (which actually appears as a single line in the file) from the <i>rtc.log</i> file is shown below. </p>
<dl>
<dd>
<pre>2015-07-22 05:40:50 -0.037360 1 -0.037434\
 -37.948 12 5 120</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above): </p>
<dl>
<dd>1. Date [2015-07-22]</dl>
<dl>
<dd>2. Hour:Minute:Second. Note that the date-time pair is expressed in UTC, not the local time zone. [05:40:50]</dl>
<dl>
<dd>3. The measured offset between the RTC and the system clock in seconds. Positive indicates that the RTC is fast of the system time [-0.037360].</dl>
<dl>
<dd>4. Flag indicating whether the regression has produced valid coefficients. (1 for yes, 0 for no). [1]</dl>
<dl>
<dd>5. Offset at the current time predicted by the regression process. A large difference between this value and the measured offset tends to indicate that the measurement is an outlier with a serious measurement error. [-0.037434]</dl>
<dl>
<dd>6. The rate at which the RTC is losing or gaining time relative to the system clock. In ppm, with positive indicating that the RTC is gaining time. [-37.948]</dl>
<dl>
<dd>7. The number of measurements used in the regression. [12]</dl>
<dl>
<dd>8. The number of runs of regression residuals of the same sign. Low values indicate that a straight line is no longer a good model of the measured data and that older measurements should be discarded. [5]</dl>
<dl>
<dd>9. The measurement interval used prior to the measurement being made (in seconds). [120]</dl>
</dl>
<p> <code>refclocks</code></p>
<dl>
<dd>This option logs the raw and filtered reference clock measurements to a file called <i>refclocks.log</i>. An example line (which actually appears as a single line in the file) from the log file is shown below. </p>
<dl>
<dd>
<pre>2009-11-30 14:33:27.000000 PPS2 7 N 1 4.900000e-07 -6.741777e-07 1.000e-06</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above): </p>
<dl>
<dd>1. Date [2009-11-30]</dl>
<dl>
<dd>2. Hour:Minute:Second.Microsecond. Note that the date-time pair is expressed in UTC, not the local time zone. [14:33:27.000000]</dl>
<dl>
<dd>3. Reference ID of the reference clock from which the measurement came. [PPS2]</dl>
<dl>
<dd>4. Sequence number of driver poll within one polling interval for raw samples, or <i>&#8211;</i> for filtered samples. [7]</dl>
<dl>
<dd>5. Leap status (<i>N</i> means normal, <i>+</i> means that the last minute of the current month has 61 seconds, <i>&#8211;</i> means that the last minute of the month has 59 seconds). [N]</dl>
<dl>
<dd>6. Flag indicating whether the sample comes from PPS source. (1 for yes, 0 for no, or <i>&#8211;</i> for filtered sample). [1]</dl>
<dl>
<dd>7. Local clock error measured by reference clock driver, or <i>&#8211;</i> for filtered sample. [4.900000e-07]</dl>
<dl>
<dd>8. Local clock error with applied corrections. Positive indicates that the local clock is slow. [-6.741777e-07]</dl>
<dl>
<dd>9. Assumed dispersion of the sample. [1.000e-06]</dl>
</dl>
<p> <code>tempcomp</code></p>
<dl>
<dd>This option logs the temperature measurements and system rate compensations to a file called <i>tempcomp.log</i>. An example line (which actually appears as a single line in the file) from the log file is shown below. </p>
<dl>
<dd>
<pre>2015-04-19 10:39:48 2.8000e+04 3.6600e-01</pre>
</dl>
<p> The columns are as follows (the quantities in square brackets are the values from the example line above): </p>
<dl>
<dd>1. Date [2015-04-19]</dl>
<dl>
<dd>2. Hour:Minute:Second. Note that the date-time pair is expressed in UTC, not the local time zone. [10:39:48]</dl>
<dl>
<dd>3. Temperature read from the sensor. [2.8000e+04]</dl>
<dl>
<dd>4. Applied compensation in ppm, positive means the system clock is running faster than it would be without the compensation. [3.6600e-01]</dl>
</dl>
</dl>
<dl>
<dd>An example of the directive is: </p>
<dl>
<dd>
<pre>log measurements statistics tracking</pre>
</dl>
</dl>
<p> <code>logbanner</code> <i>entries</i></p>
<dl>
<dd>A banner is periodically written to the log files enabled by the <code>log</code> directive to indicate the meanings of the columns. </p>
<p> The <code>logbanner</code> directive specifies after how many entries in the log file should be the banner written. The default is 32, and 0 can be used to disable it entirely.</dl>
<p> <code>logchange</code> <i>threshold</i></p>
<dl>
<dd>This directive sets the threshold for the adjustment of the system clock that will generate a syslog message. Clock errors detected via NTP packets, reference clocks, or timestamps entered via the <code>settime</code> command of <code>chronyc</code> are logged. </p>
<p> By default, the threshold is 1 second. </p>
<p> An example of the use is: </p>
<dl>
<dd>
<pre>logchange 0.1</pre>
</dl>
<p> which would cause a syslog message to be generated if a system clock error of over 0.1 seconds starts to be compensated.</dl>
<p> <code>logdir</code> <i>directory</i></p>
<dl>
<dd>This directive allows the directory where log files are written to be specified. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>logdir /var/log/chrony</pre>
</dl>
</dl>
<p> <code>mailonchange</code> <i>email</i> <i>threshold</i></p>
<dl>
<dd>This directive defines an email address to which mail should be sent if <code>chronyd</code> applies a correction exceeding a particular threshold to the system clock. </p>
<p> An example of the use of this directive is: </p>
<dl>
<dd>
<pre>mailonchange root [at] localhost 0.5</pre>
</dl>
<p> This would send a mail message to root if a change of more than 0.5 seconds were applied to the system clock. </p>
<p> This directive cannot be used when a system call filter is enabled by the <code>-F</code> option as the <code>chronyd</code> process will not be allowed to fork and execute the sendmail binary.</dl>
<h3>Miscellaneous</h3>
<p><code>hwtimestamp</code> <i>interface</i> [<i>option</i>]&#8230;</p>
<dl>
<dd>This directive enables hardware timestamping of NTP packets sent to and received from the specified network interface. The network interface controller (NIC) uses its own clock to accurately timestamp the actual transmissions and receptions, avoiding processing and queueing delays in the kernel, network driver, and hardware. This can significantly improve the accuracy of the timestamps and the measured offset, which is used for synchronisation of the system clock. In order to get the best results, both sides receiving and sending NTP packets (i.e. server and client, or two peers) need to use HW timestamping. If the server or peer supports the interleaved mode, it needs to be enabled by the <code>xleave</code> option in the <code>server</code> or the <code>peer</code> directive. </p>
<p> This directive is supported on Linux. The NIC must support HW timestamping, which can be verified with the <code>ethtool -T</code> command. The list of capabilities should include <i>SOF_TIMESTAMPING_RAW_HARDWARE</i>, <i>SOF_TIMESTAMPING_TX_HARDWARE</i>, <i>SOF_TIMESTAMPING_RX_HARDWARE</i>, and the filter modes should have <i>HWTSTAMP_FILTER_ALL</i>. When <code>chronyd</code> is running, no other process should be working with the clock on the NIC. If no <code>hwtimestamp</code> directive is specified, <code>chronyd</code> will try to use software (kernel) timestamping. With both hardware and software timestamping there are some limitations on which packets can be actually timestamped, e.g. transmit timestamping does not currently work with IPv6 packets using IP options and hardware receive timestamping does not work with packets from bridged interfaces. The timestamping used in measurements is indicated in the <i>measurements.log</i> file if enabled by the <code>log measurements</code> directive, and the <code>ntpdata</code> report in <code>chronyc</code>. </p>
<p> If the specified interface is <i>*</i>, <code>chronyd</code> will try to enable HW timestamping on all available interfaces. </p>
<p> The <code>hwtimestamp</code> directive has the following options: </p>
<p> <code>minpoll</code> <i>poll</i></p>
<dl>
<dd>This option specifies the minimum interval between readings of the NIC clock. It&#8217;s defined as a power of two. It should correspond to the minimum polling interval of all NTP sources and the minimum expected polling interval of NTP clients. The default value is 0 (1 second) and the minimum value is -6 (1/64th of a second).</dl>
<p> <code>precision</code> <i>precision</i></p>
<dl>
<dd>This option specifies the assumed precision of reading of the NIC clock. The default value is 100e-9 (100 nanoseconds).</dl>
<p> <code>txcomp</code> <i>compensation</i></p>
<dl>
<dd>This option specifies the difference in seconds between the actual transmission time at the physical layer and the reported transmit timestamp. This value will be added to transmit timestamps obtained from the NIC. The default value is 0.</dl>
<p> <code>rxcomp</code> <i>compensation</i></p>
<dl>
<dd>This option specifies the difference in seconds between the reported receive timestamp and the actual reception time at the physical layer. This value will be subtracted from receive timestamps obtained from the NIC. The default value is 0.</dl>
<p> <code>nocrossts</code></p>
<dl>
<dd>Some hardware can precisely cross timestamp the NIC clock with the system clock. This option disables the use of the cross timestamping.</dl>
</dl>
<dl>
<dd>Examples of the directive are: </p>
<dl>
<dd>
<pre>hwtimestamp eth0
hwtimestamp eth1 txcomp 300e-9 rxcomp 645e-9
hwtimestamp *</pre>
</dl>
</dl>
<p> <code>include</code> <i>pattern</i></p>
<dl>
<dd>The <code>include</code> directive includes a configuration file or multiple configuration files if a wildcard pattern is specified. This can be useful when maintaining configuration on multiple hosts to keep the differences in separate files. </p>
<p> An example of the directive is: </p>
<dl>
<dd>
<pre>include /etc/chrony.d/*.conf</pre>
</dl>
</dl>
<p> <code>keyfile</code> <i>file</i></p>
<dl>
<dd>This directive is used to specify the location of the file containing ID-key pairs for authentication of NTP packets. </p>
<p> The format of the directive is shown in the example below: </p>
<dl>
<dd>
<pre>keyfile /etc/chrony.keys</pre>
</dl>
<p> The argument is simply the name of the file containing the ID-key pairs. The format of the file is shown below: </p>
<dl>
<dd>
<pre>10 tulip
11 hyacinth
20 MD5 ASCII:crocus
25 SHA1 HEX:1dc764e0791b11fa67efc7ecbc4b0d73f68a070c
 ...</pre>
</dl>
<p> Each line consists of an ID, name of an authentication hash function (optional), and a password. The ID can be any unsigned integer in the range 1 through 2^32-1. The default hash function is <code>MD5</code>. Depending on how <code>chronyd</code> was compiled, other supported functions might be <code>SHA1</code>, <code>SHA256</code>, <code>SHA384</code>, <code>SHA512</code>, <code>RMD128</code>, <code>RMD160</code>, <code>RMD256</code>, <code>RMD320</code>, <code>TIGER</code>, and <code>WHIRLPOOL</code>. The password can be specified as a string of characters not containing white space with an optional <code>ASCII:</code> prefix, or as a hexadecimal number with the <code>HEX:</code> prefix. The maximum length of the line is 2047 characters. </p>
<p> The password is used with the hash function to generate and verify a message authentication code (MAC) in NTP packets. It is recommended to use SHA1, or stronger, hash function with random passwords specified in the hexadecimal format that have at least 128 bits. <code>chronyd</code> will log a warning to syslog on start if a source is specified in the configuration file with a key that has password shorter than 80 bits. </p>
<p> The <code>keygen</code> command of <code>chronyc</code> can be used to generate random keys for the key file. By default, it generates 160-bit MD5 or SHA1 keys.</dl>
<p> <code>lock_all</code></p>
<dl>
<dd>The <code>lock_all</code> directive will lock chronyd into RAM so that it will never be paged out. This mode is only supported on Linux. This directive uses the Linux <code>mlockall()</code> system call to prevent <code>chronyd</code> from ever being swapped out. This should result in lower and more consistent latency. It should not have significant impact on performance as <code>chronyd&#8217;s</code> memory usage is modest. The <code><a href="/docs/linux/man/2-mlockall/">mlockall</a>(2)</code> man page has more details.</dl>
<p> <code>pidfile</code> <i>file</i></p>
<dl>
<dd><code>chronyd</code> always writes its process ID (PID) to a file, and checks this file on startup to see if another <code>chronyd</code> might already be running on the system. By default, the file used is <i>/var/run/chronyd.pid</i>. The <code>pidfile</code> directive allows the name to be changed, e.g.: </p>
<dl>
<dd>
<pre>pidfile /run/chronyd.pid</pre>
</dl>
</dl>
<p> <code>sched_priority</code> <i>priority</i></p>
<dl>
<dd>On Linux, the <code>sched_priority</code> directive will select the SCHED_FIFO real-time scheduler at the specified priority (which must be between 0 and 100). On macOS, this option must have either a value of 0 (the default) to disable the thread time constraint policy or 1 for the policy to be enabled. Other systems do not support this option. </p>
<p> On Linux, this directive uses the <code>sched_setscheduler()</code> system call to instruct the kernel to use the SCHED_FIFO first-in, first-out real-time scheduling policy for <code>chronyd</code> with the specified priority. This means that whenever <code>chronyd</code> is ready to run it will run, interrupting whatever else is running unless it is a higher priority real-time process. This should not impact performance as <code>chronyd</code> resource requirements are modest, but it should result in lower and more consistent latency since <code>chronyd</code> will not need to wait for the scheduler to get around to running it. You should not use this unless you really need it. The <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a>(2)</code> man page has more details. </p>
<p> On macOS, this directive uses the <code>thread_policy_set()</code> kernel call to specify real-time scheduling. As noted for Linux, you should not use this directive unless you really need it.</dl>
<p> <code>user</code> <i>user</i></p>
<dl>
<dd>The <code>user</code> directive sets the name of the system user to which <code>chronyd</code> will switch after start in order to drop root privileges. </p>
<p> On Linux, <code>chronyd</code> needs to be compiled with support for the <code>libcap</code> library. On macOS, FreeBSD, NetBSD and Solaris <code>chronyd</code> forks into two processes. The child process retains root privileges, but can only perform a very limited range of privileged system calls on behalf of the parent. </p>
<p> The compiled-in default value is <i>chrony</i>.</dl>
<h2>Examples</h2>
<h3>NTP client with permanent connection to NTP servers</h3>
<p>This section shows how to configure <code>chronyd</code> for computers that are connected to the Internet (or to any network containing true NTP servers which ultimately derive their time from a reference clock) permanently or most of the time. </p>
<p> To operate in this mode, you will need to know the names of the NTP servers you want to use. You might be able to find names of suitable servers by one of the following methods: </p>
<dl>
<dd>&bull; Your institution might already operate servers on its network. Contact your system administrator to find out.</dl>
<dl>
<dd>&bull; Your ISP probably has one or more NTP servers available for its customers.</dl>
<dl>
<dd>&bull; Somewhere under the NTP homepage there is a list of public stratum 1 and stratum 2 servers. You should find one or more servers that are near to you. Check that their access policy allows you to use their facilities.</dl>
<dl>
<dd>&bull; Use public servers from the pool.ntp.org &lt;URL: <a rel="nofollow" href="http://www.pool.ntp.org/">http://www.pool.ntp.org/</a> &gt; project.</dl>
<p> Assuming that your NTP servers are called <i>foo.example.net</i>, <i>bar.example.net</i> and <i>baz.example.net</i>, your <i>chrony.conf</i> file could contain as a minimum: </p>
<dl>
<dd>
<pre>server foo.example.net
server bar.example.net
server baz.example.net</pre>
</dl>
<p> However, you will probably want to include some of the other directives. The <code>driftfile</code>, <code>makestep</code> and <code>rtcsync</code> might be particularly useful. Also, the <code>iburst</code> option of the <code>server</code> directive is useful to speed up the initial synchronisation. The smallest useful configuration file would look something like: </p>
<dl>
<dd>
<pre>server foo.example.net iburst
server bar.example.net iburst
server baz.example.net iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync</pre>
</dl>
<p> When using a pool of NTP servers (one name is used for multiple servers which might change over time), it is better to specify them with the <code>pool</code> directive instead of multiple <code>server</code> directives. The configuration file could in this case look like: </p>
<dl>
<dd>
<pre>pool pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync</pre>
</dl>
<h3>NTP client with infrequent connection to NTP servers</h3>
<p>This section shows how to configure <code>chronyd</code> for computers that have occasional connections to NTP servers. In this case, you will need some additional configuration to tell <code>chronyd</code> when the connection goes up and down. This saves the program from continuously trying to poll the servers when they are inaccessible. </p>
<p> Again, assuming that your NTP servers are called <i>foo.example.net</i>, <i>bar.example.net</i> and <i>baz.example.net</i>, your <i>chrony.conf</i> file would now contain: </p>
<dl>
<dd>
<pre>server foo.example.net offline
server bar.example.net offline
server baz.example.net offline
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync</pre>
</dl>
<p> The <code>offline</code> keyword indicates that the servers start in an offline state, and that they should not be contacted until <code>chronyd</code> receives notification from <code>chronyc</code> that the link to the Internet is present. To tell <code>chronyd</code> when to start and finish sampling the servers, the <code>online</code> and <code>offline</code> commands of <code>chronyc</code> need to be used. </p>
<p> To give an example of their use, assuming that <code>pppd</code> is the program being used to connect to the Internet and that <code>chronyc</code> has been installed at <i>/usr/bin/chronyc</i>, the script <i>/etc/ppp/ip-up</i> would include: </p>
<dl>
<dd>
<pre>/usr/bin/chronyc online</pre>
</dl>
<p> and the script <i>/etc/ppp/ip-down</i> would include: </p>
<dl>
<dd>
<pre>/usr/bin/chronyc offline</pre>
</dl>
<p> <code>chronyd</code>&#8216;s polling of the servers would now only occur whilst the machine is actually connected to the Internet.</p>
<h3>Isolated networks</h3>
<p>This section shows how to configure <code>chronyd</code> for computers that never have network conectivity to any computer which ultimately derives its time from a reference clock. </p>
<p> In this situation, one computer is selected to be the master timeserver. The other computers are either direct clients of the master, or clients of clients. </p>
<p> The <code>local</code> directive enables a local reference mode, which allows <code>chronyd</code> to appear synchronised even when it is not. </p>
<p> The rate value in the master&#8217;s drift file needs to be set to the average rate at which the master gains or loses time. <code>chronyd</code> includes support for this, in the form of the <code>manual</code> directive and the <code>settime</code> command in the <code>chronyc</code> program. </p>
<p> If the master is rebooted, <code>chronyd</code> can re-read the drift rate from the drift file. However, the master has no accurate estimate of the current time. To get around this, the system can be configured so that the master can initially set itself to a &#8216;majority-vote&#8217; of selected clients&#8217; times; this allows the clients to &#8216;flywheel&#8217; the master while it is rebooting. </p>
<p> The <code>smoothtime</code> directive is useful when the clocks of the clients need to stay close together when the local time is adjusted by the <code>settime</code> command. The smoothing process needs to be activated by the <code>smoothtime activate</code> command when the local time is ready to be served. After that point, any adjustments will be smoothed out. </p>
<p> A typical configuration file for the master (called <i>master</i>) might be (assuming the clients and the master are in the <i>192.168.165.x</i> subnet): </p>
<dl>
<dd>
<pre>initstepslew 1 client1 client3 client6
driftfile /var/lib/chrony/drift
local stratum 8
manual
allow 192.168.165.0/24
smoothtime 400 0.01
rtcsync</pre>
</dl>
<p> For the clients that have to resynchronise the master when it restarts, the configuration file might be: </p>
<dl>
<dd>
<pre>server master iburst
driftfile /var/lib/chrony/drift
allow 192.168.165.0/24
makestep 1.0 3
rtcsync</pre>
</dl>
<p> The rest of the clients would be the same, except that the <code>allow</code> directive is not required. </p>
<p> If there is no suitable computer to be designated as the master, or there is a requirement to keep the clients synchronised even when it fails, the <code>orphan</code> option of the <code>local</code> directive enables a special mode where the master is selected from multiple computers automatically. They all need to use the same <code>local</code> configuration and poll one another. The server with the smallest reference ID (which is based on its IP address) will take the role of the master and others will be synchronised to it. When it fails, the server with the second smallest reference ID will take over and so on. </p>
<p> A configuration file for the first server might be (assuming there are three servers called <i>master1</i>, <i>master2</i>, and <i>master3</i>): </p>
<dl>
<dd>
<pre>initstepslew 1 master2 master3
server master2
server master3
driftfile /var/lib/chrony/drift
local stratum 8 orphan
manual
allow 192.168.165.0/24
rtcsync</pre>
</dl>
<p> The other servers would be the same, except the hostnames in the <code>initstepslew</code> and <code>server</code> directives would be modified to specify the other servers. Their clients might be configured to poll all three servers.</p>
<h3>RTC tracking</h3>
<p>This section considers a computer which has occasional connections to the Internet and is turned off between &#8216;sessions&#8217;. In this case, <code>chronyd</code> relies on the computer&#8217;s RTC to maintain the time between the periods when it is powered up. It assumes that Linux is run exclusively on the computer. Dual-boot systems might work; it depends what (if anything) the other system does to the RTC. On 2.6 and later kernels, if your motherboard has a HPET, you will need to enable the <code>HPET_EMULATE_RTC</code> option in your kernel configuration. Otherwise, <code>chronyd</code> will not be able to interact with the RTC device and will give up using it. </p>
<p> When the computer is connected to the Internet, <code>chronyd</code> has access to external NTP servers which it makes measurements from. These measurements are saved, and straight-line fits are performed on them to provide an estimate of the computer&#8217;s time error and rate of gaining or losing time. </p>
<p> When the computer is taken offline from the Internet, the best estimate of the gain or loss rate is used to free-run the computer until it next goes online. </p>
<p> Whilst the computer is running, <code>chronyd</code> makes measurements of the RTC (via the <i>/dev/rtc</i> interface, which must be compiled into the kernel). An estimate is made of the RTC error at a particular RTC second, and the rate at which the RTC gains or loses time relative to true time. </p>
<p> When the computer is powered down, the measurement histories for all the NTP servers are saved to files (if the <code>dumponexit</code> directive is specified in the configuration file), and the RTC tracking information is also saved to a file (if the <code>rtcfile</code> directive has been specified). These pieces of information are also saved if the <code>dump</code> and <code>writertc</code> commands respectively are issued through <code>chronyc</code>. </p>
<p> When the computer is rebooted, <code>chronyd</code> reads the current RTC time and the RTC information saved at the last shutdown. This information is used to set the system clock to the best estimate of what its time would have been now, had it been left running continuously. The measurement histories for the servers are then reloaded. </p>
<p> The next time the computer goes online, the previous sessions&#8217; measurements can contribute to the line-fitting process, which gives a much better estimate of the computer&#8217;s gain or loss rate. </p>
<p> One problem with saving the measurements and RTC data when the machine is shut down is what happens if there is a power failure; the most recent data will not be saved. Although <code>chronyd</code> is robust enough to cope with this, some performance might be lost. (The main danger arises if the RTC has been changed during the session, with the <code>trimrtc</code> command in <code>chronyc</code>. Because of this, <code>trimrtc</code> will make sure that a meaningful RTC file is saved after the change is completed). </p>
<p> The easiest protection against power failure is to put the <code>dump</code> and <code>writertc</code> commands in the same place as the <code>offline</code> command is issued to take <code>chronyd</code> offline; because <code>chronyd</code> free-runs between online sessions, no parameters will change significantly between going offline from the Internet and any power failure. </p>
<p> A final point regards computers which are left running for extended periods and where it is desired to spin down the hard disc when it is not in use (e.g. when not accessed for 15 minutes). <code>chronyd</code> has been planned so it supports such operation; this is the reason why the RTC tracking parameters are not saved to disc after every update, but only when the user requests such a write, or during the shutdown sequence. The only other facility that will generate periodic writes to the disc is the <code>log rtc</code> facility in the configuration file; this option should not be used if you want your disc to spin down. </p>
<p> To illustrate how a computer might be configured for this case, example configuration files are shown. </p>
<p> For the <i>chrony.conf</i> file, the following can be used as an example. </p>
<dl>
<dd>
<pre>server foo.example.net maxdelay 0.4 offline
server bar.example.net maxdelay 0.4 offline
server baz.example.net maxdelay 0.4 offline
logdir /var/log/chrony
log statistics measurements tracking
driftfile /var/lib/chrony/drift
makestep 1.0 3
maxupdateskew 100.0
dumponexit
dumpdir /var/lib/chrony
rtcfile /var/lib/chrony/rtc</pre>
</dl>
<p> <code>pppd</code> is used for connecting to the Internet. This runs two scripts <i>/etc/ppp/ip-up</i> and <i>/etc/ppp/ip-down</i> when the link goes online and offline respectively. </p>
<p> The relevant part of the <i>/etc/ppp/ip-up</i> file is: </p>
<dl>
<dd>
<pre>/usr/bin/chronyc online</pre>
</dl>
<p> and the relevant part of the <i>/etc/ppp/ip-down</i> script is: </p>
<dl>
<dd>
<pre>/usr/bin/chronyc -m offline dump writertc</pre>
</dl>
<p> <code>chronyd</code> is started during the boot sequence with the <code>-r</code> and <code>-s</code> options. It might need to be started before any software that depends on the system clock not jumping or moving backwards, depending on the directives in <code>chronyd</code>&#8216;s configuration file. </p>
<p> For the system shutdown, <code>chronyd</code> should receive a SIGTERM several seconds before the final SIGKILL; the SIGTERM causes the measurement histories and RTC information to be saved.</p>
<h3>Public NTP server</h3>
<p><code>chronyd</code> can be configured to operate as a public NTP server, e.g. to join the pool.ntp.org &lt;URL: <a rel="nofollow" href="http://www.pool.ntp.org/en/join.html">http://www.pool.ntp.org/en/join.html</a> &gt; project. The configuration is similar to the NTP client with permanent connection, except it needs to allow client access from all addresses. It is recommended to find at least four good servers (e.g. from the pool, or on the NTP homepage). If the server has a hardware reference clock (e.g. a GPS receiver), it can be specified by the <code>refclock</code> directive. </p>
<p> The amount of memory used for logging client accesses can be increased in order to enable clients to use the interleaved mode even when the server has a large number of clients, and better support rate limiting if it is enabled by the <code>ratelimit</code> directive. The system timezone database, if it is kept up to date and includes the <code>right/UTC</code> timezone, can be used as a reliable source to determine when a leap second will be applied to UTC. The <code>-r</code> option with the <code>dumpdir</code> directive shortens the time in which <code>chronyd</code> will not be able to serve time to its clients when it needs to be restarted (e.g. after upgrading to a newer version, or a change in the configuration). </p>
<p> The configuration file could look like: </p>
<dl>
<dd>
<pre>server foo.example.net iburst
server bar.example.net iburst
server baz.example.net iburst
server qux.example.net iburst
makestep 1.0 3
rtcsync
allow
clientloglimit 100000000
leapsectz right/UTC
driftfile /var/lib/chrony/drift
dumpdir /var/run/chrony
dumponexit</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chronyc/">chronyc</a>(1)</code>, <code><a href="/docs/linux/man/8-chronyd/">chronyd</a>(8)</code></p>
<h2>Bugs</h2>
<p>For instructions on how to report bugs, please visit &lt;URL: <a rel="nofollow" href="https://chrony.tuxfamily.org/">https://chrony.tuxfamily.org/</a> &gt;.</p>
<h2>Authors</h2>
<p>chrony was written by Richard Curnow, Miroslav Lichvar, and others.</p>
