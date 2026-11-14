---
title: "struct_nand_sdr_timings(9)"
name: "struct_nand_sdr_timings"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_sdr_timings/"
description: "struct_nand_sdr_timings – SDR NAND chip timings"
---

<p>struct_nand_sdr_timings &#8211; SDR NAND chip timings</p>
<h2>Synopsis</h2>
<pre><code>struct nand_sdr_timings {
    u32 tALH_min;
    u32 tADL_min;
    u32 tALS_min;
    u32 tAR_min;
    u32 tCEA_max;
    u32 tCH_min;
    u32 tCHZ_max;
    u32 tCLH_min;
    u32 tCLR_min;
    u32 tCLS_min;
    u32 tCOH_min;
    u32 tCS_min;
    u32 tDH_min;
    u32 tDS_min;
    u32 tFEAT_max;
    u32 tIR_min;
    u32 tITC_max;
    u32 tRC_min;
    u32 tREA_max;
    u32 tREH_min;
    u32 tRHOH_min;
    u32 tRHW_min;
    u32 tRHZ_max;
    u32 tRLOH_min;
    u32 tRP_min;
    u32 tRR_min;
    u64 tRST_max;
    u32 tWB_max;
    u32 tWC_min;
    u32 tWH_min;
    u32 tWHR_min;
    u32 tWP_min;
    u32 tWW_min;
};</code></pre>
<h2>Members</h2>
<p>tALH_min</p>
<dl>
<dd>ALE hold time</dl>
<p> tADL_min</p>
<dl>
<dd>ALE to data loading time</dl>
<p> tALS_min</p>
<dl>
<dd>ALE setup time</dl>
<p> tAR_min</p>
<dl>
<dd>ALE to RE# delay</dl>
<p> tCEA_max</p>
<dl>
<dd>CE# access time</dl>
<p> tCH_min</p>
<dl>
<dd>CE# hold time</dl>
<p> tCHZ_max</p>
<dl>
<dd>CE# high to output hi-Z</dl>
<p> tCLH_min</p>
<dl>
<dd>CLE hold time</dl>
<p> tCLR_min</p>
<dl>
<dd>CLE to RE# delay</dl>
<p> tCLS_min</p>
<dl>
<dd>CLE setup time</dl>
<p> tCOH_min</p>
<dl>
<dd>CE# high to output hold</dl>
<p> tCS_min</p>
<dl>
<dd>CE# setup time</dl>
<p> tDH_min</p>
<dl>
<dd>Data hold time</dl>
<p> tDS_min</p>
<dl>
<dd>Data setup time</dl>
<p> tFEAT_max</p>
<dl>
<dd>Busy time for Set Features and Get Features</dl>
<p> tIR_min</p>
<dl>
<dd>Output hi-Z to RE# low</dl>
<p> tITC_max</p>
<dl>
<dd>Interface and Timing Mode Change time</dl>
<p> tRC_min</p>
<dl>
<dd>RE# cycle time</dl>
<p> tREA_max</p>
<dl>
<dd>RE# access time</dl>
<p> tREH_min</p>
<dl>
<dd>RE# high hold time</dl>
<p> tRHOH_min</p>
<dl>
<dd>RE# high to output hold</dl>
<p> tRHW_min</p>
<dl>
<dd>RE# high to WE# low</dl>
<p> tRHZ_max</p>
<dl>
<dd>RE# high to output hi-Z</dl>
<p> tRLOH_min</p>
<dl>
<dd>RE# low to output hold</dl>
<p> tRP_min</p>
<dl>
<dd>RE# pulse width</dl>
<p> tRR_min</p>
<dl>
<dd>Ready to RE# low (data only)</dl>
<p> tRST_max</p>
<dl>
<dd>Device reset time, measured from the falling edge of R/B# to the rising edge of R/B#.</dl>
<p> tWB_max</p>
<dl>
<dd>WE# high to SR[6] low</dl>
<p> tWC_min</p>
<dl>
<dd>WE# cycle time</dl>
<p> tWH_min</p>
<dl>
<dd>WE# high hold time</dl>
<p> tWHR_min</p>
<dl>
<dd>WE# high to RE# low</dl>
<p> tWP_min</p>
<dl>
<dd>WE# pulse width</dl>
<p> tWW_min</p>
<dl>
<dd>WP# transition to WE# low</dl>
<h2>Description</h2>
<p>This struct defines the timing requirements of a SDR NAND chip. These information can be found in every NAND datasheets and the timings meaning are described in the ONFI specifications: <a rel="nofollow" href="http://www.onfi.org">www.onfi.org</a>/~/media/ONFI/specs/onfi_3_1_spec.pdf (chapter 4.15 Timing Parameters) </p>
<p> All these timings are expressed in picoseconds.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
