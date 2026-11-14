---
title: "opaconfig(1)"
name: "opaconfig"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opaconfig/"
description: "opaconfig"
---

<h2>NAME</h2>
<p> opaconfig </p>
<p> <code>(Switch and Host)</code> Configures the Intel(R) Omni-Path Fabric Suite FastFabric.</p>
<h2>Syntax</h2>
<p> opaconfig [-r <i>root</i>] [-v|-vv] [-u|-s|-e <i>comp</i>] [-E#8217#160; <i>comp</i>] [-D <i>comp</i>]<br />
 [&#8211;user_queries|&#8211;no_user_queries] [&#8211;answer <i>keyword=value</i>] </p>
<p> or<br />
 opaconfig -C </p>
<p> or<br />
 opaconfig -V</p>
<h2>Options</h2>
<dl>
<dt>No option</p>
<dd> Starts the Intel(R) OP Software TUI. </p>
<dt>&#8211;help</p>
<dd> Produces full help text. </p>
<dt>-r <i>root</i></p>
<dd> Specifies alternate root directory; default is /. </p>
<dt>-v</p>
<dd> Verbose logging. </p>
<dt>-vv</p>
<dd> Very verbose debug logging. </p>
<dt>-u</p>
<dd> Uninstalls all ULPs and drivers with default options. </p>
<dt>-s</p>
<dd> Enables autostart for all installed drivers. </p>
<dt>-e <i>comp</i></p>
<dd> Uninstalls the given component with default options. This option can appear more than once on the command line. </p>
<dt>-E <i>comp</i></p>
<dd> Enables autostart of a given component. This option can appear with -D or more than once on the command line. </p>
<dt>-D <i>comp</i></p>
<dd> Disables autostart of given component. This option can appear with -E or more than once on the command line. </p>
<dt>-C</p>
<dd> Outputs list of supported components. </p>
<dt>
<dd> Supported components include: opa_stack ibacm mpi_selector intel_hfi oftools opa_stack_dev fastfa bric delta_ipoib opafm mvapich2 openmpi gasnet openshmem mvapich2_gcc_hfi mvapic h2_pgi_hfi mvapich2_intel_hfi openmpi_gcc_hfi openmpi_pgi_hfi openmpi_intel_hfi delta_mpisrc delta_debug</p>
<dt>
<dd> Supported component name aliases include: opa ipoib mpi mpisrc opadev</p>
<dt>-V</p>
<dd> Outputs version. </p>
<dt>&#8211;user_queries</p>
<dd> Permits non-root users to query the fabric (default). </p>
<dt>&#8211;no_user_queries</p>
<dd> Prohibits non-root users from querying the fabric. </p>
<dt>&#8211;answer <i>keyword=value</i></p>
<dd> Provides an answer to a question that may occur during the operation. Answers to questions not asked are ignored. Invalid answers result in prompting for interactive installs, or using default options for non-interactive installs. </p>
<dt>
<dd>
<p> <code>Possible Questions</code> ( <i>keyword=value</i>):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> UserQueries Allow non-root users to access the UMAD interface? </p>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> Allowing access to UMAD device files may present a security risk. However, this allows tools such as opasaquery and opaportinfo to be used by non-root users. </p>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> IrqBalance Set IrqBalance to Exact? </p>
</dl>
</dl>
</dl>
<h2>Example</h2>
<p> # opaconfig<br />
 Intel OPA <i>x.x.x.x.x</i> Software </p>
<p> #8217#160; 1) Show Installed Software<br />
 #8217#160; 2) Reconfigure OFED IP over IB<br />
 #8217#160; 3) Reconfigure Driver Autostart<br />
 #8217#160; 4) Generate Supporting Information for Problem Report<br />
 #8217#160; 5) FastFabric (Host/Chassis/Switch Setup/Admin)<br />
 #8217#160; 6) Uninstall Software </p>
<p> #8217#160; X) Exit </p>
<h2>Index</h2>
