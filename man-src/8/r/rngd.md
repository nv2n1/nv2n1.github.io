---
title: "rngd(8)"
name: "rngd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rngd/"
description: "rngd – Check and feed random data from hardware device to kernel random device"
---

<p>rngd &#8211; Check and feed random data from hardware device to kernel random device</p>
<h2>Synopsis</h2>
<p><code>rngd</code> [<code>-b</code>, <code>&#8211;background</code>] [<code>-f</code>, <code>&#8211;foreground</code>] [<code>-i</code>, <code>&#8211;ignorefail</code>] [<code>-o</code>, <code>&#8211;random-device=</code><i>file</i>] [<code>-p</code>, <code>&#8211;pid-file=</code><i>file</i>] [<code>-r</code>, <code>&#8211;rng-device=</code><i>file</i>] [<code>-s</code>, <code>&#8211;random-step=</code><i>nnn</i>] [<code>-W</code>, <code>&#8211;fill-watermark=</code><i>nnn</i>] [<code>-d</code>, <code>&#8211;no-drng=</code><i>1|0</i>] [<code>-n</code>, <code>&#8211;no-tpm=</code><i>1|0</i>] [<code>-q</code>, <code>&#8211;quiet</code>] [<code>-v</code>, <code>&#8211;verbose</code>] [<code>-?</code>, <code>&#8211;help</code>] [<code>-V</code>, <code>&#8211;version</code>] </p>
<h2>Description</h2>
<p>This daemon feeds data from a random number generator to the kernel&#8217;s random number entropy pool, after first checking the data to ensure that it is properly random. The <code>-f</code> or <code>&#8211;foreground</code> options can be used to tell <code>rngd</code> to avoid forking on startup. This is typically used for debugging. The <code>-b</code> or <code>&#8211;background</code> options, which fork and put <code>rngd</code> into the background automatically, are the default. The <code>-r</code> or <code>&#8211;rng-device</code> options can be used to select an alternate source of input, besides the default /dev/hwrng. The <code>-o</code> or <code>&#8211;random-device</code> options can be used to select an alternate entropy output device, besides the default /dev/random. Note that this device must support the Linux kernel /dev/random ioctl API. </p>
<h2>Options</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;background</code></dt>
<dd>Become a daemon (default)</dd>
<dt><code>-f</code>, <code>&#8211;foreground</code></dt>
<dd>Do not fork and become a daemon</dd>
<dt><code>-p</code><i> file</i>, <code>&#8211;pid-file=</code><i>file</i></dt>
<dd>File used for recording daemon PID, and multiple exclusion (default: /var/run/rngd.pid)</dd>
<dt><code>-i</code>, <code>&#8211;ignorefail</code></dt>
<dd>Ignore repeated fips failures</dd>
<dt><code>-o</code><i> file</i>, <code>&#8211;random-device=</code><i>file</i></dt>
<dd>Kernel device used for random number output (default: /dev/random)</dd>
<dt><code>-r</code><i> file</i>, <code>&#8211;rng-device=</code><i>file</i></dt>
<dd>Kernel device used for random number input (default: /dev/hwrng)</dd>
<dt><code>-s</code><i> nnn</i>, <code>&#8211;random-step=</code><i>nnn</i></dt>
<dd>Number of bytes written to random-device at a time (default: 64)</dd>
<dt><code>-e</code><i> nnn</i>, <code>&#8211;entropy-count=</code><i>nnn</i></dt>
<dd>Number of bits to consider random when adding entropy. 1&lt;=e&lt;=8 (default: 8)</dd>
<dt><code>-W</code><i> n</i>, <code>&#8211;fill-watermark=</code><i>nnn</i></dt>
<dd>Once we start doing it, feed entropy to <i>random-device</i> until at least <i>fill-watermark</i> bits of entropy are available in its entropy pool (default: 2048). Setting this too high will cause <i>rngd</i> to dominate the contents of the entropy pool. Low values will hurt system performance during entropy starves. Do not set <i>fill-watermark</i> above the size of the entropy pool (usually 4096 bits).</dd>
<dt><code>-d</code><i> 1|0</i>, <code>&#8211;no-drng=</code><i>1|0</i></dt>
<dd>Do not use drng as a source of random number input (default:0)</dd>
<dt><code>-n</code><i> 1|0</i>, <code>&#8211;no-tpm=</code><i>1|0</i></dt>
<dd>Do not use tpm as a source of random number input (default:0)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd>Suppress error messages</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Report available entropy sources, and exit</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd>Give a short summary of all program options.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Print program version </dd>
</dl>
<h2>Authors</h2>
<p>Philipp Rumpf<br/>
 Jeff Garzik &#8211; jgarzik [at] pobox.com<br/>
 Matt Sottek<br/>
 Brad Hill</p>
