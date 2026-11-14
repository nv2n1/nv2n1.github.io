---
title: "struct_nand_chip(9)"
name: "struct_nand_chip"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_chip/"
description: "struct_nand_chip – NAND Private Flash Chip Data"
---

<p>struct_nand_chip &#8211; NAND Private Flash Chip Data</p>
<h2>Synopsis</h2>
<pre><code>struct nand_chip {
    struct mtd_info mtd;
    void __iomem *IO_ADDR_R;
    void __iomem *IO_ADDR_W;
    uint8_t (*read_byte)(struct mtd_info *mtd);
    u16 (*read_word)(struct mtd_info *mtd);
    void (*write_byte)(struct mtd_info *mtd, uint8_t byte);
    void (*write_buf)(struct mtd_info *mtd, const uint8_t *buf, int len);
    void (*read_buf)(struct mtd_info *mtd, uint8_t *buf, int len);
    void (*select_chip)(struct mtd_info *mtd, int chip);
    int (*block_bad)(struct mtd_info *mtd, loff_t ofs);
    int (*block_markbad)(struct mtd_info *mtd, loff_t ofs);
    void (*cmd_ctrl)(struct mtd_info *mtd, int dat, unsigned int ctrl);
    int (*dev_ready)(struct mtd_info *mtd);
    void (*cmdfunc)(struct mtd_info *mtd, unsigned command, int column, int page_addr);
    int (*waitfunc)(struct mtd_info *mtd, struct nand_chip *this);
    int (*erase)(struct mtd_info *mtd, int page);
    int (*scan_bbt)(struct mtd_info *mtd);
    int (*errstat)(struct mtd_info *mtd, struct nand_chip *this, int state, int status, int page);
    int (*write_page)(struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, int data_len, const uint8_t *buf, int oob_required, int page, int cached, int raw);
    int (*onfi_set_features)(struct mtd_info *mtd, struct nand_chip *chip, int feature_addr, uint8_t *subfeature_para);
    int (*onfi_get_features)(struct mtd_info *mtd, struct nand_chip *chip, int feature_addr, uint8_t *subfeature_para);
    int (*setup_read_retry)(struct mtd_info *mtd, int retry_mode);
    int (*setup_data_interface)(struct mtd_info *mtd, const struct nand_data_interface *conf, bool check_only);
    int chip_delay;
    unsigned int options;
    unsigned int bbt_options;
    int page_shift;
    int phys_erase_shift;
    int bbt_erase_shift;
    int chip_shift;
    int numchips;
    uint64_t chipsize;
    int pagemask;
    int pagebuf;
    unsigned int pagebuf_bitflips;
    int subpagesize;
    uint8_t bits_per_cell;
    uint16_t ecc_strength_ds;
    uint16_t ecc_step_ds;
    int onfi_timing_mode_default;
    int badblockpos;
    int badblockbits;
    int onfi_version;
    int jedec_version;
    union {
        unnamed_union
    };
    int read_retries;
    flstate_t state;
    uint8_t *oob_poi;
    struct nand_hw_control *controller;
    struct nand_ecc_ctrl ecc;
    struct nand_buffers *buffers;
    struct nand_hw_control hwcontrol;
    uint8_t *bbt;
    struct nand_bbt_descr *bbt_td;
    struct nand_bbt_descr *bbt_md;
    struct nand_bbt_descr *badblock_pattern;
    void *priv;
};</code></pre>
<h2>Members</h2>
<p>mtd</p>
<dl>
<dd>MTD device registered to the MTD framework</dl>
<p> IO_ADDR_R</p>
<dl>
<dd>[BOARDSPECIFIC] address to read the 8 I/O lines of the flash device</dl>
<p> IO_ADDR_W</p>
<dl>
<dd>[BOARDSPECIFIC] address to write the 8 I/O lines of the flash device.</dl>
<p> read_byte</p>
<dl>
<dd>[REPLACEABLE] read one byte from the chip</dl>
<p> read_word</p>
<dl>
<dd>[REPLACEABLE] read one word from the chip</dl>
<p> write_byte</p>
<dl>
<dd>[REPLACEABLE] write a single byte to the chip on the low 8 I/O lines</dl>
<p> write_buf</p>
<dl>
<dd>[REPLACEABLE] write data from the buffer to the chip</dl>
<p> read_buf</p>
<dl>
<dd>[REPLACEABLE] read data from the chip into the buffer</dl>
<p> select_chip</p>
<dl>
<dd>[REPLACEABLE] select chip nr</dl>
<p> block_bad</p>
<dl>
<dd>[REPLACEABLE] check if a block is bad, using OOB markers</dl>
<p> block_markbad</p>
<dl>
<dd>[REPLACEABLE] mark a block bad</dl>
<p> cmd_ctrl</p>
<dl>
<dd>[BOARDSPECIFIC] hardwarespecific function for controlling ALE/CLE/nCE. Also used to write command and address</dl>
<p> dev_ready</p>
<dl>
<dd>[BOARDSPECIFIC] hardwarespecific function for accessing device ready/busy line. If set to NULL no access to ready/busy is available and the ready/busy information is read from the chip status register.</dl>
<p> cmdfunc</p>
<dl>
<dd>[REPLACEABLE] hardwarespecific function for writing commands to the chip.</dl>
<p> waitfunc</p>
<dl>
<dd>[REPLACEABLE] hardwarespecific function for wait on ready.</dl>
<p> erase</p>
<dl>
<dd>[REPLACEABLE] erase function</dl>
<p> scan_bbt</p>
<dl>
<dd>[REPLACEABLE] function to scan bad block table</dl>
<p> errstat</p>
<dl>
<dd>[OPTIONAL] hardware specific function to perform additional error status checks (determine if errors are correctable).</dl>
<p> write_page</p>
<dl>
<dd>[REPLACEABLE] High-level page write function</dl>
<p> onfi_set_features</p>
<dl>
<dd>[REPLACEABLE] set the features for ONFI nand</dl>
<p> onfi_get_features</p>
<dl>
<dd>[REPLACEABLE] get the features for ONFI nand</dl>
<p> setup_read_retry</p>
<dl>
<dd>[FLASHSPECIFIC] flash (vendor) specific function for setting the read-retry mode. Mostly needed for MLC NAND.</dl>
<p> setup_data_interface</p>
<dl>
<dd>[OPTIONAL] setup the data interface and timing</dl>
<p> chip_delay</p>
<dl>
<dd>[BOARDSPECIFIC] chip dependent delay for transferring data from array to read regs (tR).</dl>
<p> options</p>
<dl>
<dd>[BOARDSPECIFIC] various chip options. They can partly be set to inform nand_scan about special functionality. See the defines for further explanation.</dl>
<p> bbt_options</p>
<dl>
<dd>[INTERN] bad block specific options. All options used here must come from bbm.h. By default, these options will be copied to the appropriate nand_bbt_descr&#8217;s.</dl>
<p> page_shift</p>
<dl>
<dd>[INTERN] number of address bits in a page (column address bits).</dl>
<p> phys_erase_shift</p>
<dl>
<dd>[INTERN] number of address bits in a physical eraseblock</dl>
<p> bbt_erase_shift</p>
<dl>
<dd>[INTERN] number of address bits in a bbt entry</dl>
<p> chip_shift</p>
<dl>
<dd>[INTERN] number of address bits in one chip</dl>
<p> numchips</p>
<dl>
<dd>[INTERN] number of physical chips</dl>
<p> chipsize</p>
<dl>
<dd>[INTERN] the size of one chip for multichip arrays</dl>
<p> pagemask</p>
<dl>
<dd>[INTERN] page number mask = number of (pages / chip) &#8211; 1</dl>
<p> pagebuf</p>
<dl>
<dd>[INTERN] holds the pagenumber which is currently in data_buf.</dl>
<p> pagebuf_bitflips</p>
<dl>
<dd>[INTERN] holds the bitflip count for the page which is currently in data_buf.</dl>
<p> subpagesize</p>
<dl>
<dd>[INTERN] holds the subpagesize</dl>
<p> bits_per_cell</p>
<dl>
<dd>[INTERN] number of bits per cell. i.e., 1 means SLC.</dl>
<p> ecc_strength_ds</p>
<dl>
<dd>[INTERN] ECC correctability from the datasheet. Minimum amount of bit errors per <i>ecc_step_ds</i> guaranteed to be correctable. If unknown, set to zero.</dl>
<p> ecc_step_ds</p>
<dl>
<dd>[INTERN] ECC step required by the <i>ecc_strength_ds</i>, also from the datasheet. It is the recommended ECC step size, if known; if unknown, set to zero.</dl>
<p> onfi_timing_mode_default</p>
<dl>
<dd>[INTERN] default ONFI timing mode. This field is set to the actually used ONFI mode if the chip is ONFI compliant or deduced from the datasheet if the NAND chip is not ONFI compliant.</dl>
<p> badblockpos</p>
<dl>
<dd>[INTERN] position of the bad block marker in the oob area.</dl>
<p> badblockbits</p>
<dl>
<dd>[INTERN] minimum number of set bits in a good block&#8217;s bad block marker position; i.e., BBM == 11110111b is not bad when badblockbits == 7</dl>
<p> onfi_version</p>
<dl>
<dd>[INTERN] holds the chip ONFI version (BCD encoded), non 0 if ONFI supported.</dl>
<p> jedec_version</p>
<dl>
<dd>[INTERN] holds the chip JEDEC version (BCD encoded), non 0 if JEDEC supported.</dl>
<p> {unnamed_union}</p>
<dl>
<dd>anonymous</dl>
<p> read_retries</p>
<dl>
<dd>[INTERN] the number of read retry modes supported</dl>
<p> state</p>
<dl>
<dd>[INTERN] the current state of the NAND device</dl>
<p> oob_poi</p>
<dl>
<dd>&quot;poison value buffer,&quot; used for laying out OOB data before writing</dl>
<p> controller</p>
<dl>
<dd>[REPLACEABLE] a pointer to a hardware controller structure which is shared among multiple independent devices.</dl>
<p> ecc</p>
<dl>
<dd>[BOARDSPECIFIC] ECC control structure</dl>
<p> buffers</p>
<dl>
<dd>buffer structure for read/write</dl>
<p> hwcontrol</p>
<dl>
<dd>platform-specific hardware control structure</dl>
<p> bbt</p>
<dl>
<dd>[INTERN] bad block table pointer</dl>
<p> bbt_td</p>
<dl>
<dd>[REPLACEABLE] bad block table descriptor for flash lookup.</dl>
<p> bbt_md</p>
<dl>
<dd>[REPLACEABLE] bad block table mirror descriptor</dl>
<p> badblock_pattern</p>
<dl>
<dd>[REPLACEABLE] bad block scan pattern used for initial bad block scan.</dl>
<p> priv</p>
<dl>
<dd>[OPTIONAL] pointer to private chip data</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
