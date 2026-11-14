---
title: "rngtest(1)"
name: "rngtest"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rngtest/"
description: "rngtest – Check the randomness of data using FIPS 140-2 tests"
---

<h2 class="name">NAME</h2>
<p> rngtest &#8211; Check the randomness of data using FIPS 140-2 tests</p>
<h2>SYNOPSIS</h2>
<p> <code>rngtest</code> [<code>-c</code> <i>n</i> | <code>&#8211;blockcount=</code><i>n</i>] [<code>-b</code> <i>n</i> | <code>&#8211;blockstats=</code><i>n</i>] [<code>-t</code> <i>n</i> | <code>&#8211;timedstats=</code><i>n</i>] [<code>-p</code> | <code>&#8211;pipe</code>] [<code>-?</code>] [<code>&#8211;help</code>] [<code>-V</code>] [<code>&#8211;version</code>] </p>
<h2>DESCRIPTION</h2>
<p> <i>rngtest</i> works on blocks of 20000 bits at a time, using the FIPS 140-2 (errata of 2001-10-10) tests to verify the randomness of the block of data. </p>
<p> It takes input from <i>stdin</i>, and outputs statistics to <i>stderr</i>, optionally echoing blocks that passed the FIPS tests to <i>stdout</i> (when operating in <i>pipe mode</i>). Errors are sent to <i>stderr</i>. </p>
<p> At startup, <i>rngtest</i> will trow away the first 32 bits of data when operating in <i>pipe mode</i>. It will use the next 32 bits of data to bootstrap the FIPS tests (even when not operating in <i>pipe mode</i>). These bits are not tested for randomness. </p>
<p> Statistics are dumped to <i>stderr</i> when the program exits. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;pipe</code></p>
<dd> Enable <i>pipe mode</i>. All data blocks that pass the FIPS tests are echoed to <i>stdout</i>, and <i>rngtest</i> operates in silent mode.</p>
<dt><code>-c</code> <i>n</i>, <code>&#8211;blockcount=</code><i>n</i> (default: 0)</p>
<dd> Exit after processing n input blocks, if n is not zero.</p>
<dt><code>-b</code> <i>n</i>, <code>&#8211;blockstats=</code><i>n</i> (default: 0)</p>
<dd> Dump statistics every n blocks, if n is not zero.</p>
<dt><code>-t</code> <i>n</i>, <code>&#8211;timedstats=</code><i>n</i> (default: 0)</p>
<dd> Dump statistics every n seconds, if n is not zero.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Give a short summary of all program options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version </p>
</dl>
<h2>STATISTICS</h2>
<p> <i>rngtest</i> will dump statistics to <i>stderr</i> when it exits, and when told to by <i>blockstats</i> or <i>timedstats</i>. </p>
<p> <code>FIPS 140-2 successes</code> and <code>FIPS 140-2 failures</code> counts the number of 20000-bit blocks either accepted or rejected by the FIPS 140-2 tests. The other statistics show a breakdown of the FIPS 140-2 failures by FIPS 140-2 test. See the FIPS 140-2 document for more information (note that these tests are defined on FIPS 140-1 and FIPS 140-2 errata of 2001-10-10. They were removed in FIPS 140-2 errata of 2002-12-03). </p>
<p> The speed statistics are taken for every 20000-bit block transferred or processed. </p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code> if no errors happen, and no blocks fail the FIPS tests.</p>
<dd>
<dt><code>1</code> if no errors happen, but at least one block fails the FIPS tests.</p>
<dd>
<dt><code>10</code> if there are problems with the parameters.</p>
<dd>
<dt><code>11</code> if an input/output error happens.</p>
<dd>
<dt><code>12</code> if an operating system or resource starvation error happens.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/4-random/">random</a>(4), <a href="/docs/linux/man/8-rngd/">rngd</a>(8)</p>
<dl>
<dt>FIPS PUB 140-2 Security Requirements for Cryptographic Modules, NIST,</p>
<dd> <a rel="nofollow" href="http://csrc.nist.gov/groups/STM/cmvp/standards.html">http://csrc.nist.gov/groups/STM/cmvp/standards.html</a> </p>
</dl>
<h2>AUTHORS</h2>
<p> Henrique de Moraes Holschuh &lt;hmh [at] debian.org&gt; </p>
<h2>Index</h2>
