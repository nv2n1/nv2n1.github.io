---
title: "nwipe(1)"
name: "nwipe"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwipe/"
description: "nwipe – securely erase disks"
---

<h2>NAME</h2>
<p> nwipe &#8211; securely erase disks</p>
<h2>SYNOPSIS</h2>
<p> <code>nwipe</code> [<i>options</i>] [<i>device1</i>] [<i>device2</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> nwipe is a command that will securely erase disks using a variety of recognised methods. It is a fork of the dwipe command used by Darik&#8217;s Boot and Nuke (dban). nwipe is included with partedmagic if want a quick and easy bootable CD version. nwipe was created out of a need to run the DBAN dwipe command outside of DBAN, in order to allow its use with any host distribution, thus giving better hardware support. It is essentially the same as dwipe, with a few changes:</p>
<dl>
<dt>&#8211; pthreads is used instead of fork</p>
<dd>
<dt>&#8211; The parted library is used to detect drives</p>
<dd>
<dt>&#8211; The code is designed to be compiled with gcc</p>
<dd>
<dt>&#8211; SIGUSR1 can be used to log the stats of the current wipe</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Prints the version number</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Prints a help summary</p>
<dt><code>&#8211;autonuke</code></p>
<dd> If no devices have been specified on the command line, starts wiping all devices immediately. If devices have been specified, starts wiping only those specified devices immediately.</p>
<dt><code>&#8211;sync</code></p>
<dd> Open devices in sync mode</p>
<dt><code>&#8211;nowait</code></p>
<dd> Do not wait for a key before exiting (default is to wait).</p>
<dt><code>&#8211;nosignals</code></p>
<dd> Do not allow signals to interrupt a wipe (default is to allow).</p>
<dt><code>&#8211;nogui</code></p>
<dd> Do not show the GUI interface. Can only be used with the autonuke option. Nowait option is automatically invoked with the nogui option. SIGUSR1 can be used to retrieve the current wiping statistics.</p>
<dt><code>&#8211;verify</code>=<i>TYPE</i></p>
<dd> Whether to perform verification of erasure (default: last) off &#8211; Do not verify last &#8211; Verify after the last pass all &#8211; Verify every pass</p>
<dt><code>-m</code>, <code>&#8211;method</code>=<i>METHOD</i></p>
<dd> The wiping method (default: dodshort).</p>
<dt>
<dd> dod522022m / dod &#8211; 7 pass DOD 5220.22-M method</p>
<dt>
<dd> dodshort / dod3pass &#8211; 3 pass DOD method</p>
<dt>
<dd> gutmann &#8211; Peter Gutmann&#8217;s Algorithm</p>
<dt>
<dd> ops2 &#8211; RCMP TSSIT OPS-II</p>
<dt>
<dd> random / prng / stream &#8211; PRNG Stream</p>
<dt>
<dd> zero / quick &#8211; Overwrite with zeros</p>
<dt><code>-l</code>, <code>&#8211;logfile</code>=<i>FILE</i></p>
<dd> Filename to log to. Default is STDOUT</p>
<dt><code>-p</code>, <code>&#8211;prng</code>=<i>METHOD</i></p>
<dd> PRNG option (mersenne|twister|isaac)</p>
<dt><code>-r</code>, <code>&#8211;rounds</code>=<i>NUM</i></p>
<dd> Number of times to wipe the device using the selected method (default: 1)</dl>
<h2>BUGS</h2>
<p> Please see the sourceforge site for the latest list (<a rel="nofollow" href="http://nwipe.sourceforge.net)">http://nwipe.sourceforge.net)</a></p>
<h2>AUTHOR</h2>
<p> Nwipe was released by Andy Beverley &lt;andy [at] andybev.com&gt; as modified version of dwipe from DBAN by Darik Horn &lt;dajhorn-dban [at] vanadac.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-shred/">shred</a></code>(1), <code><a href="/docs/linux/man/1-dwipe/">dwipe</a></code>(1), <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1), <code><a href="/docs/linux/man/1-dcfldd/">dcfldd</a></code>(1), <code><a href="/docs/linux/man/1-dc3dd/">dc3dd</a></code>(1) </p>
<h2>Index</h2>
