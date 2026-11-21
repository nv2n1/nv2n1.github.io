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
<dt>No option</dt>
<dd> Starts the Intel(R) OP Software TUI. </dd>
<dt>&#8211;help</dt>
<dd> Produces full help text. </dd>
<dt>-r <i>root</i></dt>
<dd> Specifies alternate root directory; default is /. </dd>
<dt>-v</dt>
<dd> Verbose logging. </dd>
<dt>-vv</dt>
<dd> Very verbose debug logging. </dd>
<dt>-u</dt>
<dd> Uninstalls all ULPs and drivers with default options. </dd>
<dt>-s</dt>
<dd> Enables autostart for all installed drivers. </dd>
<dt>-e <i>comp</i></dt>
<dd> Uninstalls the given component with default options. This option can appear more than once on the command line. </dd>
<dt>-E <i>comp</i></dt>
<dd> Enables autostart of a given component. This option can appear with -D or more than once on the command line. </dd>
<dt>-D <i>comp</i></dt>
<dd> Disables autostart of given component. This option can appear with -E or more than once on the command line. </dd>
<dt>-C</dt>
<dd> Outputs list of supported components. </dd>
<dt>
</dt><dd> Supported components include: opa_stack ibacm mpi_selector intel_hfi oftools opa_stack_dev fastfa bric delta_ipoib opafm mvapich2 openmpi gasnet openshmem mvapich2_gcc_hfi mvapic h2_pgi_hfi mvapich2_intel_hfi openmpi_gcc_hfi openmpi_pgi_hfi openmpi_intel_hfi delta_mpisrc delta_debug</dd>
<dt>
</dt><dd> Supported component name aliases include: opa ipoib mpi mpisrc opadev</dd>
<dt>-V</dt>
<dd> Outputs version. </dd>
<dt>&#8211;user_queries</dt>
<dd> Permits non-root users to query the fabric (default). </dd>
<dt>&#8211;no_user_queries</dt>
<dd> Prohibits non-root users from querying the fabric. </dd>
<dt>&#8211;answer <i>keyword=value</i></dt>
<dd> Provides an answer to a question that may occur during the operation. Answers to questions not asked are ignored. Invalid answers result in prompting for interactive installs, or using default options for non-interactive installs. </dd>
<dt>
</dt><dd>
<p> <code>Possible Questions</code> ( <i>keyword=value</i>):</p>
</dd><dl>
<dl>
<dt>
</dt><dd>
<p> UserQueries Allow non-root users to access the UMAD interface? </p>
</dd></dl>
<p> <code>NOTE:</code> Allowing access to UMAD device files may present a security risk. However, this allows tools such as opasaquery and opaportinfo to be used by non-root users. </p>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> IrqBalance Set IrqBalance to Exact? </p>
</dd></dl>
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
