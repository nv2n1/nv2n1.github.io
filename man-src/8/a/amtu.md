---
title: "amtu(8)"
name: "amtu"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amtu/"
description: "amtu – Abstract Machine Test Utility (AMTU)"
---

<p>amtu &#8211; Abstract Machine Test Utility (AMTU)</p>
<h2>Synopsis</h2>
<pre><code>amtu</code> [<code>-dmsinph</code>]</pre>
<h2>Description</h2>
<p>Abstract Machine Test Utility (AMTU) is an administrative utility that checks whether the underlying protection mechanisms of the hardware are being enforced. These checks are a requirement of the Controlled Access Protection Profile (CAPP) FPT_AMT.1 (see <a rel="nofollow" href="http://www.radium.ncsc.mil/tpep/library/protection_profiles/CAPP-1.d.pdf">http://www.radium.ncsc.mil/tpep/library/protection_profiles/CAPP-1.d.pdf</a>). AMTU executes the following tests:</p>
<dl>
<dt>* Memory</dt>
<dd>Randomly writes to areas of memory, then reads the memory back to ensure the values written remain unchanged.</dd>
<dt>* Memory Separation</dt>
<dd>Ensures that user space programs cannot read and write to areas of memory utilized by items such as Video RAM and kernel code.</dd>
<dt>* I/O Controller &#8211; Network</dt>
<dd>Verifies random data transmitted is also the data received for each configured network device. Checks only Ethernet and token ring devices that are configured and up. Does not check async devices.</dd>
<dt>* I/O Controller &#8211; Disk</dt>
<dd>Verifies random data written to disks remains unchanged. Only IDE and SCI controllers that are associated with mounted file systems are checked. Disk controllers with read-only mounted file systems are not checked.</dd>
<dt>* Supervisor Mode Instructions</dt>
<dd>Ensures that the enforcement of the property that privileged instructions should only be in supervisor mode is still in effect. The set of privileged instructions tested to confirm this is architecture dependent. </dd>
<h2>Options</h2>
<p>Options available for the <code>amtu</code> command are the following: </p>
<dl>
<dt><code>-d</code></dt>
<dd>Print debug messages. </dd>
<dt><code>-m</code></dt>
<dd>Execute Memory Test. </dd>
<dt><code>-s</code></dt>
<dd>Execute Memory Separation Test. </dd>
<dt><code>-i</code></dt>
<dd>Execute I/O Controller &#8211; Disk Test. </dd>
<dt><code>-n</code></dt>
<dd>Execute I/O Controller &#8211; Network Test </dd>
<dt><code>-p</code></dt>
<dd>Execute Supervisor Mode Instructions Test. </dd>
<dt><code>-h</code></dt>
<dd>Print help message. </dd>
</dl>
<h2>Return Codes</h2>
<p>The <code>amtu</code> command issues the following return codes when executed: </p>
<dl>
<dt>-1</dt>
<dd>Failure </dd>
<dt>0</dt>
<dd>Success. </dd>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to amtueal-devel [at] lists.sourceforge.net .</p>
<h2>Author</h2>
<p>Emily Ratliff, Joy Latten, and Kimberly Simon.</p>
</dl>