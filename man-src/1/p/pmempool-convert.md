---

title: "pmempool-convert(1)"
name: "pmempool-convert"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-convert/"
description: "pmempool-convert – Convert pool files from old layout versions to the newest one."
---

<h2>NAME</h2>
<p> pmempool-convert &#8211; Convert pool files from old layout versions to the newest one.</p>
<p> <code>pmempool convert</code> &lt;file&gt;</p>
<p> The <code>pmempool</code> invoked with the <code>convert</code> command performs a conversion of the specified pool to the newest layout supported by this tool. Currently only <code>libpmemobj(3)</code> pools are supported. It is advised to have a backup of the pool before conversion. The conversion process is not fail-safe &#8211; power interruption may damage the pool.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool convert pool.obj</dt>
<dd> # Updates pool.obj to the latest layout version.</dd>
<dt></dt></dl>
<h2>SEE ALSO</h2>
<dd> <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1) <a href="/docs/linux/man/1-pmempool-info/">pmempool-info</a>(1) libpmemobj(3)</code></dd>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
