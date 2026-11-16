---
title: "opagetvf(1)"
name: "opagetvf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opagetvf/"
---

<h2>NAME</h2>

 opagetvf 

 

 

 Used for scripting application use of vFabrics, such as for mpirun parameters. You can query by VF Name, VF Index, Service ID, MGID, PKey, or SL. Fetches the Virtual Fabric info in a delimited format. Returns exactly one matching VF. When multiple VFs match the query, it prefers non-default VFs in which the calling server is a full member. If multiple choices remain, it returns the one with the lowest VF Index. Uses the same algorithm as the Distributed SA Plug-in (DSAP). 

 The tool can be used with additional scripts to help set PKey, SL, MTU, and Rate when running MPI jobs. Internally, this tool is based on the opasaquery -o vfinfocsv command. For more information, see <i>opasaquery</i>

<h2>Syntax</h2>

 opagetvf [-h <i>hfi</i>] [-p <i>port</i>] [-e] [-d <i>vfname</i>|-S <i>serviceId</i>|-m <i>mcgid</i>|-i <i>vfIndex</i>| -k <i>pkey</i>|-L <i>sl</i>]

<h2>Options</h2>

 

<dl>
<dt>--help
</dt><dd> Produces full help text.
</dd><dt>-h <i>hfi</i>
</dt><dd> HFI to send by. Default is first HFI.
</dd><dt>-p <i>port</i>
</dt><dd> Port to send by, default is first active port.
</dd><dt>-e
</dt><dd> Output MTU and rate as enum values.
</dd><dt>-d <i>vfname</i>
</dt><dd> Queries by VirtualFabric Name.
</dd><dt>-S <i>serviceId</i>
</dt><dd> Queries by Application ServiceId.
</dd><dt>-m <i>gid</i>
</dt><dd> Queries by Application Multicast GID.
</dd><dt>-i <i>vfindex</i>
</dt><dd> Queries by VirtualFabric Index.
</dd><dt>-k <i>pkey</i>
</dt><dd> Queries by VirtualFabric PKey.
</dd><dt>-L <i>SL</i>
</dt><dd> Queries by VirtualFabric SL.</dd></dl>

<h2>Examples</h2>

 opagetvf -d 'Compute' 
 opagetvf -h 2 -p 2 -d 'Compute'

<h2>Sample Outputs</h2>

 

 

 The output is of the form: name:index:pkey:sl:mtu:rate:optionflag as shown in the following example. 

 Option flag (bitmask) values include:
<dl>
<dt>&bull;
</dt><dd> 0x00 Indicates no bits are set. Specifically, no QOS, no Security, and no flow control disabled (which means flow control is enabled).
</dd><dt>&bull;
</dt><dd> 0x01 Security
</dd><dt>&bull;
</dt><dd> 0x02 QOS
</dd><dt>&bull;
</dt><dd> 0x04 Flow Control Disable</dd></dl>
 

 

 
 # opagetvf -d Default 
 Default:0:0xffff:0:unlimited:unlimited:0x0 

 
 

<h2>Index</h2>


