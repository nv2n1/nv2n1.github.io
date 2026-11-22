---

title: "nvme(1)"
name: "nvme"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme/"
description: "nvme – the dumb pci-e storage utility"
---

<p> nvme &#8211; the dumb pci-e storage utility </p>
<h2>SYNOPSIS</h2>
<pre>
<i>nvme</i> &lt;command&gt; &lt;device&gt; [&lt;args&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> NVM-Express is a fast, scalable host controller interface designed to address the needs for PCI Express based solid state drives. </p>
<p> This <i>nvme</i> program is a user space utility to provide standards compliant tooling for NVM-Express drives. It was made specifically for Linux as it relies on the IOCTLs defined by the mainline kernel driver.</p>
<h2>NVME COMMANDS</h2>
<p> The utility has sub-commands for all admin and io commands defined in the specification and for displaying controller registers. There is also an option to submit completely arbitrary commands. For a list of commands available, run &quot;nvme help&quot;.</p>
<h2>NVME CLI SUB-COMMANDS</h2>
<h3>Main commands</h3>
<p> <code><a href="/docs/linux/man/1-nvme-admin-passthru/">nvme-admin-passthru</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Admin Passthrough Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-compare/">nvme-compare</a></code>(1)</p>
<dl>
<dt>
</dt><dd> IO Compare</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-error-log/">nvme-error-log</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Retrieve error logs</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-flush/">nvme-flush</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Submit flush</dd></dl>
<p> <code>nvme-dms</code>(1)</p>
<dl>
<dt>
</dt><dd> Submit Data Set Management</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-format/">nvme-format</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Format namespace(s)</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-activate/">nvme-fw-activate</a></code>(1)</p>
<dl>
<dt>
</dt><dd> F/W Activate</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-download/">nvme-fw-download</a></code>(1)</p>
<dl>
<dt>
</dt><dd> F/W Download</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-log/">nvme-fw-log</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Retrieve f/w log</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-feature/">nvme-get-feature</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Get Features</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-log/">nvme-get-log</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Generic Get Log</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-smart-log/">nvme-smart-log</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Retrieve Smart Log</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-ns-id/">nvme-get-ns-id</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Retrieve namespace identifier</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-help/">nvme-help</a></code>(1)</p>
<dl>
<dt>
</dt><dd> NVMe CLI Help</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-id-ctrl/">nvme-id-ctrl</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Identify Controller</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-id-ns/">nvme-id-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Identify Namespace</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-create-ns/">nvme-create-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Create a new namespace</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-delete-ns/">nvme-delete-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Delete existing namespace</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-attach-ns/">nvme-attach-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Attach namespace</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-detach-ns/">nvme-detach-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Detach namespace</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-io-passthru/">nvme-io-passthru</a></code>(1)</p>
<dl>
<dt>
</dt><dd> IO Passthrough Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-list-ns/">nvme-list-ns</a></code>(1)</p>
<dl>
<dt>
</dt><dd> List all nvme namespaces</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-list/">nvme-list</a></code>(1)</p>
<dl>
<dt>
</dt><dd> List all nvme controllers</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-list-ctrl/">nvme-list-ctrl</a></code>(1)</p>
<dl>
<dt>
</dt><dd> List controller in NVMe subsystem</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-read/">nvme-read</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Issue IO Read Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-write/">nvme-write</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Issue IO Write Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-write-zeroes/">nvme-write-zeroes</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Issue IO Write Zeroes Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-write-uncor/">nvme-write-uncor</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Issue IO Write Uncorrectable Command</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-acquire/">nvme-resv-acquire</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Acquire Namespace Reservation</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-register/">nvme-resv-register</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Register Namespace Reservation</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-release/">nvme-resv-release</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Release Namespace Reservation</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-report/">nvme-resv-report</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Report Reservation Capabilities</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-security-recv/">nvme-security-recv</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Security Receive</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-security-send/">nvme-security-send</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Security Send</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-set-feature/">nvme-set-feature</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Set Feature</dd></dl>
<p> <code><a href="/docs/linux/man/1-nvme-show-regs/">nvme-show-regs</a></code>(1)</p>
<dl>
<dt>
</dt><dd> Show NVMe Controller Registers</dd></dl>
<h2>FURTHER DOCUMENTATION</h2>
<p> See the freely available references on the m[blue]<code>Official NVM-Express Site</code>m[][1].</p>
<h2>AUTHORS</h2>
<p> This is written and maintained by m[blue]<code>Keith Busch</code>m[][2].</p>
<h2>REPORTING BUGS</h2>
<p> Patches and issues may be submitted to the official repository at m[blue]<code><a rel="nofollow" href="https://github.com/linux-nvme/nvme-cli">https://github.com/linux-nvme/nvme-cli</a></code>m[].</p>
<h2>NVME</h2>
<p> Part of the nvme suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Official NVM-Express Site</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://nvmexpress.org">http://nvmexpress.org</a></dd></dl>
<dt> 2.</dt>
<dd> Keith Busch</dd>
<dl>
<dt>
</dt><dd> mailto:keith.busch [at] intel.com</dd></dl>
</dl>
