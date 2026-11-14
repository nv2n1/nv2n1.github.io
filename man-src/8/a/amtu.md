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
<dt>* Memory</p>
<dd>Randomly writes to areas of memory, then reads the memory back to ensure the values written remain unchanged.</p>
<dt>* Memory Separation</p>
<dd>Ensures that user space programs cannot read and write to areas of memory utilized by items such as Video RAM and kernel code.</p>
<dt>* I/O Controller &#8211; Network</p>
<dd>Verifies random data transmitted is also the data received for each configured network device. Checks only Ethernet and token ring devices that are configured and up. Does not check async devices.</p>
<dt>* I/O Controller &#8211; Disk</p>
<dd>Verifies random data written to disks remains unchanged. Only IDE and SCI controllers that are associated with mounted file systems are checked. Disk controllers with read-only mounted file systems are not checked.</p>
<dt>* Supervisor Mode Instructions</p>
<dd>Ensures that the enforcement of the property that privileged instructions should only be in supervisor mode is still in effect. The set of privileged instructions tested to confirm this is architecture dependent. </p>
<h2>Options</h2>
<p>Options available for the <code>amtu</code> command are the following: </p>
<dl>
<dt><code>-d</code></p>
<dd>Print debug messages. </p>
<dt><code>-m</code></p>
<dd>Execute Memory Test. </p>
<dt><code>-s</code></p>
<dd>Execute Memory Separation Test. </p>
<dt><code>-i</code></p>
<dd>Execute I/O Controller &#8211; Disk Test. </p>
<dt><code>-n</code></p>
<dd>Execute I/O Controller &#8211; Network Test </p>
<dt><code>-p</code></p>
<dd>Execute Supervisor Mode Instructions Test. </p>
<dt><code>-h</code></p>
<dd>Print help message. </p>
</dl>
<h2>Return Codes</h2>
<p>The <code>amtu</code> command issues the following return codes when executed: </p>
<dl>
<dt>-1</p>
<dd>Failure </p>
<dt>0</p>
<dd>Success. </p>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to amtueal-devel [at] lists.sourceforge.net .</p>
<h2>Author</h2>
<p>Emily Ratliff, Joy Latten, and Kimberly Simon.</p>
