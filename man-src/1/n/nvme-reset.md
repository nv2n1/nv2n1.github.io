---

title: "nvme-reset(1)"
name: "nvme-reset"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-reset/"
---

nvme-reset - Reset the nvme controller. 

<pre>
<i>nvme reset</i> &lt;device&gt;
</pre>

Requests NVMe controller reset. The &lt;device&gt; param is mandatory and must be an NVMe character device (ex: /dev/nvme0).

<h2>OPTIONS</h2>

 

 None

<h2>EXAMPLES</h2>

 

<dl>
<dt>
</dt><dd> &bull; Resets the controller. 
</dd><dl>
<dt>
</dt><dd> <pre>
# nvme reset /dev/nvme0
</pre></dd></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite
