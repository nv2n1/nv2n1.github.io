---
title: "struct_platform_nand_ctrl(9)"
name: "struct_platform_nand_ctrl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_platform_nand_ctrl/"
description: "struct_platform_nand_ctrl – controller level device structure"
---

<p>struct_platform_nand_ctrl &#8211; controller level device structure</p>
<h2>Synopsis</h2>
<pre><code>struct platform_nand_ctrl {
    int (*probe)(struct platform_device *pdev);
    void (*remove)(struct platform_device *pdev);
    void (*hwcontrol)(struct mtd_info *mtd, int cmd);
    int (*dev_ready)(struct mtd_info *mtd);
    void (*select_chip)(struct mtd_info *mtd, int chip);
    void (*cmd_ctrl)(struct mtd_info *mtd, int dat, unsigned int ctrl);
    void (*write_buf)(struct mtd_info *mtd, const uint8_t *buf, int len);
    void (*read_buf)(struct mtd_info *mtd, uint8_t *buf, int len);
    unsigned char (*read_byte)(struct mtd_info *mtd);
    void *priv;
};</code></pre>
<h2>Members</h2>
<p>probe</p>
<dl>
<dd>platform specific function to probe/setup hardware</dl>
<p> remove</p>
<dl>
<dd>platform specific function to remove/teardown hardware</dl>
<p> hwcontrol</p>
<dl>
<dd>platform specific hardware control structure</dl>
<p> dev_ready</p>
<dl>
<dd>platform specific function to read ready/busy pin</dl>
<p> select_chip</p>
<dl>
<dd>platform specific chip select function</dl>
<p> cmd_ctrl</p>
<dl>
<dd>platform specific function for controlling ALE/CLE/nCE. Also used to write command and address</dl>
<p> write_buf</p>
<dl>
<dd>platform specific function for write buffer</dl>
<p> read_buf</p>
<dl>
<dd>platform specific function for read buffer</dl>
<p> read_byte</p>
<dl>
<dd>platform specific function to read one byte from chip</dl>
<p> priv</p>
<dl>
<dd>private data to transport driver specific settings</dl>
<h2>Description</h2>
<p>All fields are optional and depend on the hardware driver requirements</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
