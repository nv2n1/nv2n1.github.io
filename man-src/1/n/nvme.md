---
title: "nvme(1)"
name: "nvme"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme/"
description: "nvme – the dumb pci-e storage utility"
---

<h2 class="name">NAME</h2>
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
<dd> Admin Passthrough Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-compare/">nvme-compare</a></code>(1)</p>
<dl>
<dt>
<dd> IO Compare</dl>
<p> <code><a href="/docs/linux/man/1-nvme-error-log/">nvme-error-log</a></code>(1)</p>
<dl>
<dt>
<dd> Retrieve error logs</dl>
<p> <code><a href="/docs/linux/man/1-nvme-flush/">nvme-flush</a></code>(1)</p>
<dl>
<dt>
<dd> Submit flush</dl>
<p> <code><a href="/docs/linux/man/1-nvme-dms/">nvme-dms</a></code>(1)</p>
<dl>
<dt>
<dd> Submit Data Set Management</dl>
<p> <code><a href="/docs/linux/man/1-nvme-format/">nvme-format</a></code>(1)</p>
<dl>
<dt>
<dd> Format namespace(s)</dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-activate/">nvme-fw-activate</a></code>(1)</p>
<dl>
<dt>
<dd> F/W Activate</dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-download/">nvme-fw-download</a></code>(1)</p>
<dl>
<dt>
<dd> F/W Download</dl>
<p> <code><a href="/docs/linux/man/1-nvme-fw-log/">nvme-fw-log</a></code>(1)</p>
<dl>
<dt>
<dd> Retrieve f/w log</dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-feature/">nvme-get-feature</a></code>(1)</p>
<dl>
<dt>
<dd> Get Features</dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-log/">nvme-get-log</a></code>(1)</p>
<dl>
<dt>
<dd> Generic Get Log</dl>
<p> <code><a href="/docs/linux/man/1-nvme-smart-log/">nvme-smart-log</a></code>(1)</p>
<dl>
<dt>
<dd> Retrieve Smart Log</dl>
<p> <code><a href="/docs/linux/man/1-nvme-get-ns-id/">nvme-get-ns-id</a></code>(1)</p>
<dl>
<dt>
<dd> Retrieve namespace identifier</dl>
<p> <code><a href="/docs/linux/man/1-nvme-help/">nvme-help</a></code>(1)</p>
<dl>
<dt>
<dd> NVMe CLI Help</dl>
<p> <code><a href="/docs/linux/man/1-nvme-id-ctrl/">nvme-id-ctrl</a></code>(1)</p>
<dl>
<dt>
<dd> Identify Controller</dl>
<p> <code><a href="/docs/linux/man/1-nvme-id-ns/">nvme-id-ns</a></code>(1)</p>
<dl>
<dt>
<dd> Identify Namespace</dl>
<p> <code><a href="/docs/linux/man/1-nvme-create-ns/">nvme-create-ns</a></code>(1)</p>
<dl>
<dt>
<dd> Create a new namespace</dl>
<p> <code><a href="/docs/linux/man/1-nvme-delete-ns/">nvme-delete-ns</a></code>(1)</p>
<dl>
<dt>
<dd> Delete existing namespace</dl>
<p> <code><a href="/docs/linux/man/1-nvme-attach-ns/">nvme-attach-ns</a></code>(1)</p>
<dl>
<dt>
<dd> Attach namespace</dl>
<p> <code><a href="/docs/linux/man/1-nvme-detach-ns/">nvme-detach-ns</a></code>(1)</p>
<dl>
<dt>
<dd> Detach namespace</dl>
<p> <code><a href="/docs/linux/man/1-nvme-io-passthru/">nvme-io-passthru</a></code>(1)</p>
<dl>
<dt>
<dd> IO Passthrough Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-list-ns/">nvme-list-ns</a></code>(1)</p>
<dl>
<dt>
<dd> List all nvme namespaces</dl>
<p> <code><a href="/docs/linux/man/1-nvme-list/">nvme-list</a></code>(1)</p>
<dl>
<dt>
<dd> List all nvme controllers</dl>
<p> <code><a href="/docs/linux/man/1-nvme-list-ctrl/">nvme-list-ctrl</a></code>(1)</p>
<dl>
<dt>
<dd> List controller in NVMe subsystem</dl>
<p> <code><a href="/docs/linux/man/1-nvme-read/">nvme-read</a></code>(1)</p>
<dl>
<dt>
<dd> Issue IO Read Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-write/">nvme-write</a></code>(1)</p>
<dl>
<dt>
<dd> Issue IO Write Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-write-zeroes/">nvme-write-zeroes</a></code>(1)</p>
<dl>
<dt>
<dd> Issue IO Write Zeroes Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-write-uncor/">nvme-write-uncor</a></code>(1)</p>
<dl>
<dt>
<dd> Issue IO Write Uncorrectable Command</dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-acquire/">nvme-resv-acquire</a></code>(1)</p>
<dl>
<dt>
<dd> Acquire Namespace Reservation</dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-register/">nvme-resv-register</a></code>(1)</p>
<dl>
<dt>
<dd> Register Namespace Reservation</dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-release/">nvme-resv-release</a></code>(1)</p>
<dl>
<dt>
<dd> Release Namespace Reservation</dl>
<p> <code><a href="/docs/linux/man/1-nvme-resv-report/">nvme-resv-report</a></code>(1)</p>
<dl>
<dt>
<dd> Report Reservation Capabilities</dl>
<p> <code><a href="/docs/linux/man/1-nvme-security-recv/">nvme-security-recv</a></code>(1)</p>
<dl>
<dt>
<dd> Security Receive</dl>
<p> <code><a href="/docs/linux/man/1-nvme-security-send/">nvme-security-send</a></code>(1)</p>
<dl>
<dt>
<dd> Security Send</dl>
<p> <code><a href="/docs/linux/man/1-nvme-set-feature/">nvme-set-feature</a></code>(1)</p>
<dl>
<dt>
<dd> Set Feature</dl>
<p> <code><a href="/docs/linux/man/1-nvme-show-regs/">nvme-show-regs</a></code>(1)</p>
<dl>
<dt>
<dd> Show NVMe Controller Registers</dl>
<h2>FURTHER DOCUMENTATION</h2>
<p> See the freely available references on the m[blue]<code>Official NVM-Express Site</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>AUTHORS</h2>
<p> This is written and maintained by m[blue]<code>Keith Busch</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>REPORTING BUGS</h2>
<p> Patches and issues may be submitted to the official repository at m[blue]<code><a rel="nofollow" href="https://github.com/linux-nvme/nvme-cli">https://github.com/linux-nvme/nvme-cli</a></code>m[].</p>
<h2>NVME</h2>
<p> Part of the nvme suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Official NVM-Express Site</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://nvmexpress.org">http://nvmexpress.org</a></dl>
<dt> 2.</p>
<dd> Keith Busch</p>
<dl>
<dt>
<dd> mailto:keith.busch [at] intel.com</dl>
</dl>
<h2>Index</h2>
