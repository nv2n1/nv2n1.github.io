---
title: "struct_nand_ecc_ctrl(9)"
name: "struct_nand_ecc_ctrl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_ecc_ctrl/"
description: "struct_nand_ecc_ctrl – Control structure for ECC"
---

<p>struct_nand_ecc_ctrl &#8211; Control structure for ECC</p>
<h2>Synopsis</h2>
<pre><code>struct nand_ecc_ctrl {
    nand_ecc_modes_t mode;
    enum nand_ecc_algo algo;
    int steps;
    int size;
    int bytes;
    int total;
    int strength;
    int prepad;
    int postpad;
    unsigned int options;
    void *priv;
    void (*hwctl)(struct mtd_info *mtd, int mode);
    int (*calculate)(struct mtd_info *mtd, const uint8_t *dat, uint8_t *ecc_code);
    int (*correct)(struct mtd_info *mtd, uint8_t *dat, uint8_t *read_ecc, uint8_t *calc_ecc);
    int (*read_page_raw)(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page);
    int (*write_page_raw)(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page);
    int (*read_page)(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page);
    int (*read_subpage)(struct mtd_info *mtd, struct nand_chip *chip, uint32_t offs, uint32_t len, uint8_t *buf, int page);
    int (*write_subpage)(struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, uint32_t data_len, const uint8_t *data_buf, int oob_required, int page);
    int (*write_page)(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page);
    int (*write_oob_raw)(struct mtd_info *mtd, struct nand_chip *chip, int page);
    int (*read_oob_raw)(struct mtd_info *mtd, struct nand_chip *chip, int page);
    int (*read_oob)(struct mtd_info *mtd, struct nand_chip *chip, int page);
    int (*write_oob)(struct mtd_info *mtd, struct nand_chip *chip, int page);
};</code></pre>
<h2>Members</h2>
<p>mode</p>
<dl>
<dd>ECC mode</dl>
<p> algo</p>
<dl>
<dd>ECC algorithm</dl>
<p> steps</p>
<dl>
<dd>number of ECC steps per page</dl>
<p> size</p>
<dl>
<dd>data bytes per ECC step</dl>
<p> bytes</p>
<dl>
<dd>ECC bytes per step</dl>
<p> total</p>
<dl>
<dd>total number of ECC bytes per page</dl>
<p> strength</p>
<dl>
<dd>max number of correctible bits per ECC step</dl>
<p> prepad</p>
<dl>
<dd>padding information for syndrome based ECC generators</dl>
<p> postpad</p>
<dl>
<dd>padding information for syndrome based ECC generators</dl>
<p> options</p>
<dl>
<dd>ECC specific options (see NAND_ECC_XXX flags defined above)</dl>
<p> priv</p>
<dl>
<dd>pointer to private ECC control data</dl>
<p> hwctl</p>
<dl>
<dd>function to control hardware ECC generator. Must only be provided if an hardware ECC is available</dl>
<p> calculate</p>
<dl>
<dd>function for ECC calculation or readback from ECC hardware</dl>
<p> correct</p>
<dl>
<dd>function for ECC correction, matching to ECC generator (sw/hw). Should return a positive number representing the number of corrected bitflips, -EBADMSG if the number of bitflips exceed ECC strength, or any other error code if the error is not directly related to correction. If -EBADMSG is returned the input buffers should be left untouched.</dl>
<p> read_page_raw</p>
<dl>
<dd>function to read a raw page without ECC. This function should hide the specific layout used by the ECC controller and always return contiguous in-band and out-of-band data even if they&#8217;re not stored contiguously on the NAND chip (e.g. NAND_ECC_HW_SYNDROME interleaves in-band and out-of-band data).</dl>
<p> write_page_raw</p>
<dl>
<dd>function to write a raw page without ECC. This function should hide the specific layout used by the ECC controller and consider the passed data as contiguous in-band and out-of-band data. ECC controller is responsible for doing the appropriate transformations to adapt to its specific layout (e.g. NAND_ECC_HW_SYNDROME interleaves in-band and out-of-band data).</dl>
<p> read_page</p>
<dl>
<dd>function to read a page according to the ECC generator requirements; returns maximum number of bitflips corrected in any single ECC step, 0 if bitflips uncorrectable, -EIO hw error</dl>
<p> read_subpage</p>
<dl>
<dd>function to read parts of the page covered by ECC; returns same as <code>read_page</code></dl>
<p> write_subpage</p>
<dl>
<dd>function to write parts of the page covered by ECC.</dl>
<p> write_page</p>
<dl>
<dd>function to write a page according to the ECC generator requirements.</dl>
<p> write_oob_raw</p>
<dl>
<dd>function to write chip OOB data without ECC</dl>
<p> read_oob_raw</p>
<dl>
<dd>function to read chip OOB data without ECC</dl>
<p> read_oob</p>
<dl>
<dd>function to read chip OOB data</dl>
<p> write_oob</p>
<dl>
<dd>function to write chip OOB data</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
