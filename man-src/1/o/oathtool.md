---
title: "oathtool(1)"
name: "oathtool"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oathtool/"
description: "oathtool – OATH one-time password tool"
---

<h2>NAME</h2>
<p> oathtool &#8211; OATH one-time password tool</p>
<h2>SYNOPSIS</h2>
<p> <code>oathtool</code> [<i>OPTIONS</i>]&#8230; [<i>KEY </i>[<i>OTP</i>]]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> oathtool 2.4.1 </p>
<p> Generate and validate OATH one-time passwords.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>&#8211;hotp</code></p>
<dd> use event-based HOTP mode (default=on)</p>
<dt><code>&#8211;totp</code></p>
<dd> use time-variant TOTP mode (default=off)</p>
<dt><code>-b</code>, <code>&#8211;base32</code></p>
<dd> use base32 encoding of KEY instead of hex (default=off)</p>
<dt><code>-c</code>, <code>&#8211;counter</code>=<i>COUNTER</i></p>
<dd> HOTP counter value</p>
<dt><code>-s</code>, <code>&#8211;time-step-size</code>=<i>DURATION</i> TOTP time-step duration</p>
<dd> (default=`30s&#8217;)</p>
<dt><code>-S</code>, <code>&#8211;start-time</code>=<i>TIME</i></p>
<dd> when to start counting time steps for TOTP (default=`1970-01-01 00:00:00 UTC&#8217;)</p>
<dt><code>-N</code>, <code>&#8211;now</code>=<i>TIME</i></p>
<dd> use this time as current time for TOTP (default=`now&#8217;)</p>
<dt><code>-d</code>, <code>&#8211;digits</code>=<i>DIGITS</i></p>
<dd> number of digits in one-time password</p>
<dt><code>-w</code>, <code>&#8211;window</code>=<i>WIDTH</i></p>
<dd> window of counter values to test when validating OTPs</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> explain what is being done (default=off)</dl>
<h2>EXAMPLES</h2>
<p> To generate the first event-based (HOTP) one-time password for an all-zero key: </p>
<p>$&nbsp;<wbr>oathtool 00<br />
328482<br />
$ </p>
<p> Sometime you want to generate more than a single OTP. To generate 10 additional event-based one-time passwords, with the secret key used in the examples of RFC 4226, use the -w (&#8211;window) parameter: </p>
<p>$&nbsp;<wbr>oathtool -w 10 3132333435363738393031323334353637383930<br />
755224<br />
287082<br />
359152<br />
969429<br />
338314<br />
254676<br />
287922<br />
162583<br />
399871<br />
520489<br />
403154<br />
$ </p>
<p> In the last output, the counter for the first OTP was 0, the second OTP had a counter of 1, and so on up to 10. </p>
<p> In order to use keys encoded in Base32 instead of hex, you may provide the -b (&#8211;base32) parameter: </p>
<p>$&nbsp;<wbr>oathtool &#8211;base32 -w 3 GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ<br />
755224<br />
287082<br />
359152<br />
969429<br />
$ </p>
<p> The tool ignore whitespace in base32 data and re-add padding if necessary, thus you may supply keys formatted like the one below. </p>
<p>$&nbsp;<wbr>oathtool &#8211;base32 &#8211;totp&nbsp;<wbr>&quot;gr6d 5br7 25s6 vnck v4vl hlao re&quot;<br />
977872<br />
$ </p>
<p> To generate a particular OTP, use the -c (&#8211;counter) parameter to give the exact position directly: </p>
<p>$&nbsp;<wbr>oathtool -c 5 3132333435363738393031323334353637383930<br />
254676<br />
$ </p>
<p> To validate a HOTP one-time password supply the OTP last on the command line: </p>
<p>$&nbsp;<wbr>oathtool -w 10 3132333435363738393031323334353637383930 969429<br />
3<br />
$ </p>
<p> The output indicates the counter that was used. It works by starting with counter 0 and increment until it founds a match (or not), within the supplied window of 10 OTPs. </p>
<p> The tool supports time-variant one-time passwords, in so called TOTP mode. Usage is similar, but &#8211;totp needs to be provided: </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp 00<br />
943388<br />
$ </p>
<p> Don&#8217;t be alarmed if you do not get the same output, this is because the output is time variant. To generate a TOTP for a particular fixed time use the -N (&#8211;now) parameter: </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp &#8211;now&nbsp;<wbr>&quot;2008-04-23 17:42:17 UTC&quot;&nbsp;<wbr>00<br />
974945<br />
$ </p>
<p> The format is a mostly free format human readable date string such as &quot;Sun, 29 Feb 2004 16:21:42 -0800&quot; or &quot;2004-02-29 16:21:42&quot; or even &quot;next Thursday&quot;. It is the same used as the &#8211;date parameter of the <a href="/docs/linux/man/1-date/">date</a>(1) tool. </p>
<p> You may generate several TOTPs by specifying the &#8211;window parameter, similar to how it works for HOTP. The OTPs generated here will be for the initial time (normally current time) and then each following time step (e.g., 30 second window). </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp 00 -w5<br />
815120<br />
003818<br />
814756<br />
184042<br />
582326<br />
733842<br />
$ </p>
<p> You can validate a TOTP one-time password by supplying the secret and a window parameter (number of time steps before or after current time): </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp -w 5 00&nbsp;<wbr>`oathtool &#8211;totp 00`<br />
0<br />
$ </p>
<p> Similar when generating TOTPs, you can use a -N (&#8211;now) parameter to specify the time to use instead of the current time: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>oathtool &#8211;totp &#8211;now=&quot;2005-03-18 01:58:29 UTC&quot;&nbsp;<wbr>-w 10000000 3132333435363738393031323334353637383930 89005924<br />
&nbsp;<wbr>&nbsp;<wbr>4115227<br />
&nbsp;<wbr>&nbsp;<wbr>$ </p>
<p> The previous test uses values from the TOTP specification and will stress test the tool because the expected window is around 4 million time-steps. </p>
<p> There are two system parameters for TOTP: the time-step size and the time start. </p>
<p> By default the time-step size is 30 seconds, which means you get a new OTP every 30 seconds. You may modify this with the -s (&#8211;time-step-size) parameter: </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp &#8211;time-step-size=45s 00<br />
109841<br />
$ </p>
<p> The values are valid ISO-8601 durations, see: <a rel="nofollow" href="http://en.wikipedia.org/wiki/ISO_8601#Durations">http://en.wikipedia.org/wiki/ISO_8601#Durations</a> </p>
<p> The time start is normally 1970-01-01 00:00:00 UTC but you may change it using the -S (&#8211;start-time): </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp &#8211;start-time&nbsp;<wbr>&quot;1980-01-01 00:00:00 UTC&quot;&nbsp;<wbr>00<br />
273884<br />
$ </p>
<p> To get more information about what the tool is using use the -v (&#8211;verbose) parameter. Finally, to generate the last TOTP (for SHA-1) in the test vector table of draft-mraihi-totp-timebased-07 you can invoke the tool like this: </p>
<p>$&nbsp;<wbr>oathtool &#8211;totp -v -N&nbsp;<wbr>&quot;2033-05-18 03:33:20 UTC&quot;&nbsp;<wbr>-d8 3132333435363738393031323334353637383930<br />
Hex secret: 3132333435363738393031323334353637383930<br />
Base32 secret: GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ<br />
Digits: 8<br />
Window size: 0<br />
Step size&nbsp;<wbr>(seconds): 30<br />
Start time: 1970-01-01 00:00:00 UTC&nbsp;<wbr>(0)<br />
Time now: 2033-05-18 03:33:20 UTC&nbsp;<wbr>(2000000000)<br />
Counter: 0x3F940AA&nbsp;<wbr>(66666666) </p>
<p>69279037<br />
$</p>
<h2>AUTHOR</h2>
<p> Written by Simon Josefsson.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: oath-toolkit-help [at] nongnu.org oathtool home page: &lt;<a rel="nofollow" href="http://www.nongnu.org/oath-toolkit/">http://www.nongnu.org/oath-toolkit/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Simon Josefsson. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
