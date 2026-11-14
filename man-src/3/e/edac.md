---
title: "edac(3)"
name: "edac"
section: "3"
letter: "e"
url: "/docs/linux/man/3-edac/"
description: "libedac – EDAC error reporting library"
---

<h2 class="name">NAME</h2>
<p> libedac &#8211; EDAC error reporting library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;edac.h&gt;
cc... - ledac
            edac_handle *
            edac_handle_create(void);
void edac_handle_destroy(edac_handle *edac);
int edac_handle_init(edac_handle *edac);
unsigned int edac_mc_count(edac_handle *edac);
int edac_handle_reset(edac_handle *edac);
int edac_error_totals(edac_handle *edac, struct edac_totals *totals);
edac_mc *edac_next_mc(edac_handle *edac);
int edac_mc_get_info(edac_mc *mc, struct edac_mc_info *info);
edac_mc *edac_next_mc_info(edac_handle *edac,
                           struct edac_mc_info *info);
int edac_mc_reset(struct edac_mc *mc);
edac_csrow *edac_next_csrow(struct edac_mc *mc);
int edac_csrow_get_info(edac_csrow *csrow,
                        struct edac_csrow_info *info);
edac_csrow *edac_next_csrow_info(edac_mc *mc,
                                 struct edac_csrow_info *info);
const char *edac_strerror(edac_handle *edac);
edac_for_each_mc_info(edac_handle *edac, edac_mc *mc,
                      struct edac_csrow_info *info){...} edac_for_each_csrow_info(edac_mc *mc, edac_csrow *csrow,
                                                                                  struct edac_csrow_info *info)
{
    ...
}
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>libedac</i> library offers a very simple programming interface to the information exported from in-kernel EDAC (Error Detection and Correction) drivers in sysfs. The <i><a href="/docs/linux/man/8-edac-util/">edac-util</a></i>(8) utility uses <i>libedac</i> to report errors in a user-friendly manner from the command line. </p>
<p> EDAC errors for most systems are recorded in sysfs on a per memory controller (MC) basis. Memory controllers are further subdivided by csrow and channel. The <i>libedac</i> library provides a method to loop through multiple MCs, and their corresponding csrows, obtaining information about each component from sysfs along the way. There is also a simple single call to retrieve the total error counts for a given machine. </p>
<p> In order to use <i>libedac</i> an <code>edac_handle</code> must first be opened via the call <code>edac_handle_create</code>(). Once the handle is created, sysfs data can be loaded into the handle with <code>edac_handle_init</code>(). A final call to <code>edac_handle_destroy</code>() will free all memory and open files associated with the edac handle. </p>
<p> <code>edac_handle_create</code>() will return <code>NULL</code> on failure to allocate memory. </p>
<p> The <code>edac_strerror</code> function will return a descriptive string representation of the last error for the <i>libedac</i> handle <i>edac</i>. </p>
<p> The <code>edac_error_totals</code>() function will return the total counts of memory and pci errors in the <i>totals</i> structure passed to the function. The <i>totals</i> structure is of type <i>edac_totals</i> which has the form: </p>
<dl>
<dt>
<dd>
struct edac_totals {<br />
    unsigned int ce_total;         /* Total corrected errors   */<br />
    unsigned int ue_total;         /* Total uncorrected errors */<br />
    unsigned int pci_parity_total; /* Total PCI Parity errors  */<br />
};
</dl>
<h2>MEMORY CONTROLLER INFORMATION</h2>
<p> Systems may have one or more memory controllers (MCs) with EDAC information. The number of MCs detected by EDAC drivers may be queried with the <code>edac_mc_count</code>() function, while the <code>edac_next_mc</code> function will return a handle to the next memory controller in the <i>libedac</i> handle&#8217;s internal list. This memory controller is represented by the opaque <code>edac_mc</code> type. </p>
<p> <code>edac_next_mc</code> will return <code>NULL</code> when there are no further memory controllers to return. Thus the following example code is another method to count all EDAC MCs (assuming the EDAC library handle <i>edac</i> has already been initialized): </p>
<dl>
<dt>
<dd>
int i = 0;<br />
edac_mc *mc;<br />
while ((mc = edac_next_mc(edac)))<br />
    i++;<br />
return (i);
</dl>
<p> To query information about an <code>edac_mc</code>, use the <code>edac_mc_get_info</code> function. This function fills in the given <code>info</code> structure, which is of type <code>edac_mc_info</code>: </p>
<dl>
<dt>
<dd>
struct edac_mc_info {<br />
    char id[];                    /* Id of memory controller */<br />
    char mc_name[];               /* Name of MC              */<br />
    unsigned int size_mb;         /* Amount of RAM in MB     */<br />
    unsigned int ce_count;        /* Corrected error count   */<br />
    unsigned int ce_noinfo_count; /* noinfo Corrected errors */<br />
    unsigned int ue_count;        /* Uncorrected error count */<br />
    unsigned int ue_noinfo_count; /* noinfo Uncorrected errors*/<br />
};
</dl>
<p> The function <code>edac_next_mc_info</code>() can be used to loop through all EDAC memory controllers and obtain MC information in a single call. It is a combined <code>edac_next_mc</code>() and <code>edac_mc_get_info</code>(). </p>
<p> The function <code>edac_handle_reset</code>() will reset the internal memory controller iterator in the <i>libedac</i> handle. A subsequent call to <code>edac_next_mc</code>() would thus return the first EDAC MC. </p>
<p> A convenience macro, <code>edac_for_each_mc_info</code>(), is provided which defines a for loop that iterates through all memory controller<br />
&nbsp;<wbr>objects for a given EDAC handle, returning the MC information in the <i>info</i> structure on each iteration. For example (assuming initialized <i>libedac</i> handle <i>edac</i>): </p>
<dl>
<dt>
<dd>
edac_mc *mc;<br />
struct edac_mc_info info;<br />
int count = 0;<br />
edac_for_each_mc_info(edac, mc, info)<br />
{<br />
    count++;<br />
    printf(&#8220;MC info: id=%s name=%s
&#8221;, info.id, info.mc_name);<br />
}
</dl>
<h2>CSROW INFORMATION</h2>
<p> Each EDAC memory controller may have one or more <i>csrow</i>s associated with it. Similar to the MC iterator functions described above, the <code>edac_next_csrow</code>() function allows <i>libedac</i> users to loop through all csrows within a given MC. Once the last csrow is reached, the function will return <code>NULL</code>. </p>
<p> The <code>edac_csrow_get_info</code>() function returns information about <code>edac_csrow in the edac_csrow_info</code> structure, which has the contents: </p>
<dl>
<dt>
<dd>
struct edac_csrow_info {<br />
    char id[];             /* CSROW Identity (e.g. csrow0)  */<br />
    unsigned int size_mb;  /* CSROW size in MB              */<br />
    unsigned int ce_count; /* Total corrected errors        */<br />
    unsigned int ue_count; /* Total uncorrected errors      */<br />
    struct edac_channel channel[EDAC_MAX_CHANNELS];<br />
};<br />
struct edac_channel {<br />
    int valid;             /* Is this channel valid */<br />
    unsigned int ce_count; /* Corrected error count */<br />
    int dimm_label_valid;  /* Is DIMM label valid?  */<br />
    char dimm_label[];     /* DIMM name             */<br />
};
</dl>
<p> The <code>edac_next_csrow_info</code>() function is a combined version of <code>edac_next_csrow</code>() and <code>edac_csrow_get_info</code>() for convenience. </p>
<p> The <code>edac_mc_reset</code>() function is provided to reset the <code>edac_mc</code> internal csrow iterator. </p>
<p> A convenience macro, <code>edac_for_each_csrow_info</code>(), is provided which defines a for loop that iterates through all csrow objects in an EDAC memory controller, returning the csrow information in the <i>info</i> structure on each iteration. </p>
<h2>EXAMPLES</h2>
<p> Initialize <i>libedac</i> handle: </p>
<dl>
<dt>
<dd>
edac_handle *edac;<br />
if (!(edac = edac_handle_create())) {<br />
    fprintf(stderr, &#8220;edac_handle_create: Out of memory!
&#8221;);<br />
    exit(1);<br />
}<br />
if (edac_handle_init(edac) &lt; 0) {<br />
    fprintf(stderr, &#8220;Unable to get EDAC data: %s
&#8221;,<br />
            edac_strerror(edac));<br />
    exit(1);<br />
}<br />
printf(&#8220;EDAC initialized with %d MCs
&#8221;, edac_mc_count(edac));<br />
edac_handle_destroy(edac);
</dl>
<p> Report all DIMM labels for MC:csrow:channel combinations </p>
<dl>
<dt>
<dd>
<pre><code>
edac_mc *mc;
edac_csrow *csrow;
struct edac_mc_info mci;
struct edac_csrow_info csi;
edac_for_each_mc_info(ctx-&gt;edac, mc, mci)
{
    edac_for_each_csrow_info(mc, csrow, csi)
    {
        char *label[2] = {"unset", "unset"};
        if (csi.channel[0].dimm_label_valid)
            label[0] = csi.channel[0].dimm_label;
        if (csi.channel[1].dimm_label_valid)
            label[1] = csi.channel[1].dimm_label;
        printf("%s:%s:ch0 = %s
", mci.id, csi.id, label[0]);
        printf("%s:%s:ch1 = %s
", mci.id, csi.id, label[1]);
    }
}
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-edac-util/">edac-util</a></code>(8), <code><a href="/docs/linux/man/8-edac-ctl/">edac-ctl</a></code>(8) </p>
<h2>Index</h2>
